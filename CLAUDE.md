# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in
`orekit_python_artifacts` and the wider Orekit-for-Python ecosystem.

## TL;DR

`orekit_python_artifacts` is **the staging repository** that bundles the JARs
needed to build the conda-forge `orekit` (Python) package. It is not where
Orekit's Java code lives, not where the JNI generator lives, and not where the
conda recipe lives. It sits in the middle of a four-repo chain:

```
┌──────────────────────────────┐    ┌──────────────────────────────┐
│ Orekit fork                  │    │ Hipparchus / Rugged          │
│ (petrushy/Orekit)            │    │ (upstream releases via Maven)│
│ - upstream Orekit source     │    │ - no Python additions        │
│ - + PythonXxx bridge classes │    │                              │
│   that expose Java callbacks │    │                              │
│   to Python via JCC          │    │                              │
└───────────────┬──────────────┘    └────────────────┬─────────────┘
                │ mvn package                        │ mvn download
                │                                    │
                │  orekit-<ver>.jar                  │
                │  orekit-<ver>-python-wrapper.jar   │  hipparchus-*-<ver>.jar
                │  orekit-<ver>-javadoc.jar          │  rugged-*-<ver>.jar
                ▼                                    ▼
         ┌──────────────────────────────────────────────────┐
         │ orekit_python_artifacts  (THIS REPO)             │
         │ - holds the JARs (loose, at repo root)           │
         │ - holds shared Python helpers (pyhelpers.py)     │
         │ - holds the Python test suite (test/)            │
         │ - holds the type-stub package (orekit_stubs/)    │
         │ - tagged as v<X>_<Y>_<Z>_<rev>                   │
         └───────────────┬──────────────────────────────────┘
                         │ GitHub source archive of the tag
                         │ (this is what conda-forge downloads)
                         ▼
         ┌──────────────────────────────────────────────────┐
         │ orekit-feedstock         (conda-forge recipe)    │
         │ - meta.yaml pins the tag + SHA256                │
         │ - build.sh invokes JCC against the bundled JARs  │
         │ - publishes the `orekit` conda package           │
         └───────────────┬──────────────────────────────────┘
                         │ uses
                         ▼
         ┌──────────────────────────────────────────────────┐
         │ JCC + jcc-feedstock                              │
         │ - reflection-driven Java→Python JNI compiler     │
         │ - generates the C++ extension that *is* the      │
         │   `orekit` Python module                         │
         └──────────────────────────────────────────────────┘
```

The same JARs are also used by an **jpype-based binding**
([orekit_jpype/](orekit_jpype/)) and by the **stub generator**
([dl_jars_and_render_stubs.py](dl_jars_and_render_stubs.py)). Those paths are
out-of-scope for the conda-forge build but share the JARs.

## What's in this repository

### JARs at the repository root

These are the artifacts the conda-forge build consumes. They are committed in
**loose form** (no subdirectory). For the v13_1_5_0 line:

| File | Source | Role |
| --- | --- | --- |
| `orekit-<ver>.jar` | petrushy/Orekit fork, `mvn package` | Orekit Java classes (incl. PythonXxx bridges) |
| `orekit-<ver>-python-wrapper.jar` | same fork, `mvn -Ppython-jar package` | **Just** the `PythonXxx` bridge classes |
| `orekit-<ver>-javadoc.jar` | same fork | Used by stub generators, not by JCC |
| `hipparchus-<module>-<ver>.jar` | conda-forge / Maven Central | Numerical library; Orekit depends on it |
| `rugged-<ver>.jar` | Orekit's Maven repo | Optional Earth-surface lighting library |
| `rugged-<ver>-python-wrapper.jar` | Orekit's Maven repo | Rugged's PythonXxx bridges |

**Naming is load-bearing.** [recipe/build.sh](../orekit-feedstock/recipe/build.sh)
in `orekit-feedstock` references these by their **exact** literal filenames. If
the bundled JAR is `hipparchus-core-4.0.3.jar` but build.sh asks for
`hipparchus-core-4.0.1.jar`, JCC fails with "No such file" before doing any
work. **Always bump the names in both places in lockstep.**

### `pyhelpers.py`

Pure-Python helper module that gets compiled into the conda-forge `orekit`
extension (via JCC's `--module $SRC_DIR/pyhelpers.py`). It is the only place
runtime Python helpers live in this repo; everything else is generated from
Java. Notable contents:

- `setup_orekit_curdir(filename='orekit-data.zip')` — wires
  `DataProvidersManager` to a local zip or directory of Orekit data files.
- `datetime_to_absolutedate` / `absolutedate_to_datetime` — bidirectional
  conversion between Python `datetime` and Orekit `AbsoluteDate`, including
  the `TimeOffset`/`TimeUnit` plumbing introduced in newer Orekit versions.
- Other small adapters that smooth over JCC ergonomics.

If you add a Python helper, this is the file to extend. Avoid creating new
top-level Python modules — they will not be packaged into the JCC extension.

### `test/`

The test suite that conda-forge runs in its `test:` phase (see
[recipe/run_test.sh](../orekit-feedstock/recipe/run_test.sh)). Each `*.py`
is invoked as a standalone script; **exit code matters, stdout does not**.
Most tests use `unittest.main()` so a failed assertion exits non-zero. Tests
share `test/resources/` (orekit data files, AGI, USNO, IERS, atmosphere
models, etc.) and **must remain runnable from inside `test/` as cwd**.

The tests are Python translations of Orekit's Java JUnit tests, written
incrementally by Petrus and contributors over many years. They are
**also the primary integration check** that the JCC-compiled extension
actually exposes the right API surface — if a test relies on
`Foo.bar(x, y)` and JCC didn't generate that overload, the failure shows up
here, not at build time. (Today's session uncovered exactly that pattern:
see "Known gotchas" below.)

### `orekit_stubs/`

A **separate** Python package — `pip`-installable, containing only `.pyi`
files. It is built once per release by running
[dl_jars_and_render_stubs.py](dl_jars_and_render_stubs.py) (uses
[stubgenj](https://gitlab.cern.ch/scripting-tools/stubgenj) under jpype) and
committed back to this repo. The conda recipe installs it as a second step
after the main `orekit` package:

```bash
cd orekit_stubs && $PYTHON setup.py install
```

Stubs are reference material for IDEs (Pyright, mypy, IDEA). They are
**not** loaded at runtime and **not** consulted by JCC. They can drift
behind the JCC-generated wrapper without breaking anything except IDE
hints — but they should be regenerated alongside any JAR bump.

### `orekit_jpype/`

An **experimental** alternative binding that uses
[jpype](https://github.com/jpype-project/jpype) instead of JCC. Same JARs,
different runtime: `orekit_jpype.jars/` holds a subset of the runtime JARs and
the Python side calls Java via jpype's reflection-based bridge. This is not
what conda-forge ships; it lives here only because it consumes the same JAR
set. Treat it as a separate, parallel project.

### `pom.xml`

A Maven config used **only by [dl_jars_and_render_stubs.py](dl_jars_and_render_stubs.py)** to download
fresh JARs (release + javadoc) from the Orekit Maven repository for stub
generation. It is **not** used by the conda-forge build, which downloads the
GitHub source archive of a tag instead.

**Known footgun:** the `<outputDirectory>` is set per-artifact, and is currently
inconsistent — most runtime JARs land in `orekit_jpype/jars/` but a few
(`hipparchus-core`, `hipparchus-filtering`, `rugged`) are misrouted to
`temp_jars/` (see [pom.xml](pom.xml) lines 57, 74, 91). When refreshing JARs,
fix the routing or you'll think they downloaded but they didn't end up in the
expected place.

### `download_dependencies.py`

Older script that uses Maven directly (without a pom). It hardcodes
`VERSION = "4.0.1"` for hipparchus. Treat as legacy — `dl_jars_and_render_stubs.py`
is the maintained path.

## The wider ecosystem

### 1. Orekit (fork at `petrushy/Orekit`)

- Local checkout: [/Users/sepehy/Development/GitHub/Orekit](/Users/sepehy/Development/GitHub/Orekit)
- Tracks upstream `orekit/orekit` but adds **`PythonXxx` bridge classes** in
  the same packages as the interfaces/abstract classes they wrap. These are
  the *only* thing that lets Python subclass Java classes through JCC.
- The fork's [PYTHON_WRAPPER_PROCESS.md](/Users/sepehy/Development/GitHub/Orekit/PYTHON_WRAPPER_PROCESS.md)
  is the canonical reference for the bridge-class pattern. Every bridge has
  the same boilerplate (pythonObject field, `pythonExtension(long)`
  getter/setter, `finalize()`, `native pythonDecRef()`) and then `native`
  declarations for every abstract/interface method that Python should be
  able to override.
- The fork's [python_wrapper_validation/](/Users/sepehy/Development/GitHub/Orekit/python_wrapper_validation)
  contains static validators that check for missing bridges and broken
  templates.
- Two POM profiles produce two JARs:
  - `mvn package` → `orekit-<ver>.jar` (everything)
  - `mvn -Ppython-jar package` → `orekit-<ver>-python-wrapper.jar` (just
    the bridges)

  JCC needs **both** at build time. They must be the same version.

### 2. Hipparchus, Rugged

Numerical and Earth-surface libraries that Orekit depends on. **No Python
additions** — JCC wraps them directly from upstream releases.

### 3. JCC

- Local checkout: [/Users/sepehy/Development/jcc](/Users/sepehy/Development/jcc)
  (mirrors Apache PyLucene's JCC source).
- Conda-forge build: [/Users/sepehy/Development/GitHub/jcc-feedstock](/Users/sepehy/Development/GitHub/jcc-feedstock).
- See [/Users/sepehy/Development/jcc/CLAUDE.md](/Users/sepehy/Development/jcc/CLAUDE.md)
  and [/Users/sepehy/Development/jcc/JCC_ARCHITECTURE.md](/Users/sepehy/Development/jcc/JCC_ARCHITECTURE.md)
  for the deep dive.
- One-sentence model: at build time JCC starts a JVM, reflects on the
  requested classes, and emits C++/JNI + Python glue compiled into a single
  CPython extension named (in our case) `orekit`.

### 4. orekit-feedstock (conda-forge recipe)

- Local checkout: [/Users/sepehy/Development/GitHub/orekit-feedstock](/Users/sepehy/Development/GitHub/orekit-feedstock).
- [recipe/meta.yaml](/Users/sepehy/Development/GitHub/orekit-feedstock/recipe/meta.yaml)
  pins the tag (`v13_1_5_0`) and the SHA256 of the GitHub-served zip of that
  tag.
- [recipe/build.sh](/Users/sepehy/Development/GitHub/orekit-feedstock/recipe/build.sh)
  sets JCC env vars, invokes `python -m jcc` with the JAR list, and
  installs the resulting extension. It also installs activation scripts
  under `$PREFIX/etc/conda/activate.d/` that set `JCC_JDK=$CONDA_PREFIX`
  so users can re-compile their own JCC extensions inside the env.
- [recipe/run_test.sh](/Users/sepehy/Development/GitHub/orekit-feedstock/recipe/run_test.sh)
  runs every `test/*.py` from this repo as a standalone script.

## Per-release update process

The README has the official checklist. Annotated and corrected version:

1. **Cut a branch in this repo** named after the Orekit major.minor:
   `git switch -c version-X.Y` (e.g. `version-13.1`).
2. **In the Orekit fork**, rebase onto the upstream `orekit-X.Y.Z` tag,
   resolve conflicts (mostly around new abstract methods needing bridge
   declarations), and run the validators in `python_wrapper_validation/`.
   Push and confirm CI is green.
3. **`mvn package` and `mvn -Ppython-jar package` in the Orekit fork.**
   Copy the two produced JARs to this repo root, replacing the old ones.
4. **Refresh Hipparchus / Rugged JARs** if they bumped upstream. Edit
   [pom.xml](pom.xml) `<version>` properties, run
   [dl_jars_and_render_stubs.py](dl_jars_and_render_stubs.py), then move
   the runtime JARs from `orekit_jpype/jars/` (or `temp_jars/`, depending
   on the broken-routing footgun) up to the repo root.
5. **Regenerate stubs.** The script does this if you let it run past the
   download step. Otherwise, in `orekit_stubs/` cwd, run
   `python -m stubgenj --convert-strings --classpath "../*.jar" org.orekit org.hipparchus java`.
   Commit the changed `*.pyi` tree.
6. **Tag and push.** Use the GitHub-archive-friendly format `v<X>_<Y>_<Z>_<rev>`
   (e.g. `v13_1_5_0`). This is what the feedstock pins.
7. **Update orekit-feedstock**:
   - bump `version`, `artifact_filename`, and `sha256` in
     [recipe/meta.yaml](/Users/sepehy/Development/GitHub/orekit-feedstock/recipe/meta.yaml).
     Get the SHA from
     `curl -sL https://github.com/petrushy/orekit_python_artifacts/archive/<tag>.zip | shasum -a 256`.
   - bump the literal JAR filenames in
     [recipe/build.sh](/Users/sepehy/Development/GitHub/orekit-feedstock/recipe/build.sh)
     to match what you committed. If hipparchus minor changed,
     **every** `--jar $SRC_DIR/hipparchus-*-<ver>.jar` line needs to change.
   - Open the PR; conda-forge bots will rerender CI and build all
     supported (python × platform) combos.

## Known gotchas

The history of "build was green then suddenly red" usually traces back to
one of these:

### Source archive SHA drifts

GitHub's auto-generated `archive/<tag>.zip` is generally stable but
**not guaranteed to be**. If the upstream tag is re-cut, or GitHub changes
its archive generation, the SHA will move. Symptom: conda-build fails in
the source-download phase with
`RuntimeError: SHA256 mismatch: '<actual>' != '<pinned>'`.

Fix: re-pin in [recipe/meta.yaml](/Users/sepehy/Development/GitHub/orekit-feedstock/recipe/meta.yaml).
But first check **why** the archive changed — if the tag was force-moved,
you may be packaging the wrong commit.

### JAR filename drift between this repo and the feedstock

build.sh references JARs by literal name (no globbing). Bumping a JAR
version here without updating build.sh causes
`No such file or directory` at the JCC step.

### JCC default `-Xss` too small on aarch64 JDK 8

JCC ≤ 3.15 (current conda-forge release) sets
`initvm_args['maxstack'] = '512k'` in `jcc/cpp.py`. aarch64 JDK 8 rejects
anything below 640k with `The stack size specified is too small, Specify at
least 640k`. The fix in JCC main (`'2m'`) is unreleased. Workaround is a
sed patch in build.sh — see the comment block above the `python -m jcc`
invocation in
[recipe/build.sh](/Users/sepehy/Development/GitHub/orekit-feedstock/recipe/build.sh).
Remove the workaround once JCC > 3.15 ships.

### JCC ignores Java interface *default methods*

JCC's reflection generator walks each class's *declared* methods. A default
method declared on an interface is **not** declared on the implementing
class, so JCC's generated dispatcher for the subclass omits it. Symptom:
`InvalidArgsError` / `RuntimeException: InvalidArgsError` at runtime when
Python calls what looks like a valid Java method.

Diagnose with `javap -p` (you'll see the overload *missing* on the subclass
but present on the interface). Workaround in Python:

```python
from org.orekit.utils import PVCoordinatesProvider
pos = PVCoordinatesProvider.cast_(orbit).getPVCoordinates(date, frame).getPosition()
```

The pattern: cast to the interface that *declares* the default method, then
call. This came up in
[test/InterSatDirectViewDetectorTest.py:131](test/InterSatDirectViewDetectorTest.py#L131)
after Orekit moved `getPVCoordinates(AbsoluteDate, Frame)` from `Orbit`
onto `ShiftablePVCoordinatesHolder` as a default method.

### Python threads must be attached to the JVM

JCC's `JCCEnv` stores the `JNIEnv*` in thread-local storage. Python
`threading.Thread` workers that touch Java objects (even just `repr()`,
which calls Java's `toString()`) will SEGV unless attached. Use:

```python
vm = orekit.initVM()      # idempotent
def worker():
    vm.attachCurrentThread()
    ...
```

This is not a bug — it's the JCC contract. JVM crash logs from unattached
threads typically show a fault in `JCCEnv::callObjectMethod` with the
`this` pointer NULL.

### JCC `initVM()` is one-shot per process

Heap/stack/startup options are fixed by the first call. Subsequent calls
mostly just return the running env and may try to extend the classpath.
This matters when developing tests interactively — re-importing or
re-calling `initVM` does not give you a fresh VM.

### `setup_orekit_curdir("resources")` on the full Java test tree

The Java Orekit project's `src/test/resources/` contains many parallel EOP
fixture sets (`bulletinA/`, `eopc04/`, `eop-prediction/`, `linear-EOP/`,
`zero-EOP/`, `missing-months/`, `new-bulletinB/`, `eop-xml/`,
`compressed-data/`, `earth/finals2000A.all`, ...). Each is a deliberate test
fixture covering a specific date range — they are **not** intended to be
loaded together. The Java tests pick one curated subset per test via
`Utils.setDataRoot("regular-data")` (or
`"regular-data:atmosphere:potential/icgem-format"` etc.).

If a Python test calls `setup_orekit_curdir("resources")`, `DirectoryCrawler`
walks the **entire** tree, Orekit's `LazyLoadedEop` merges all fixtures into
one EOP timeline, and `EOPHistory.checkEOPContinuity` then refuses any
frame computation with:

```text
org.orekit.errors.OrekitException: missing Earth Orientation Parameters
  between 2020-06-07T00:00:00.000Z and 2022-01-01T00:00:00.000Z, gap is 4.95072E7 s
```

The fix is **per-test**: mirror the Java equivalent's `Utils.setDataRoot(...)`
value. For most tests that means `setup_orekit_curdir("resources/regular-data")`.

For multi-root tests (Java's `setDataRoot` accepts `:`-separated roots) call
the new `setup_orekit_data(filenames=[...])` helper with a list of paths —
it clears providers once and adds one crawler per path:

```python
from orekit.pyhelpers import setup_orekit_data
setup_orekit_data(filenames=["resources/regular-data",
                             "resources/atmosphere",
                             "resources/potential/icgem-format"],
                  from_pip_library=False)
```

`setup_orekit_curdir` is preserved as a one-path wrapper (it now delegates
to `setup_orekit_data`). Note both functions now **raise `FileNotFoundError`
if a path is missing**, instead of the previous silent print-and-return.

In test fixtures predating `setup_orekit_data` (e.g. the inline
`DataContext.getDefault().getDataProvidersManager()` + `DirectoryCrawler`
loop in [test/BrouwerLyddanePropagatorTest.py:46](test/BrouwerLyddanePropagatorTest.py#L46))
the manual pattern still works but is no longer the preferred form.

When a Python test fails on `FramesFactory.getITRF(...)` with the EOP-gap
error after a resource refresh, this is almost always the cause. Look at
the corresponding Java test's `@BeforeEach setUp()` for the right data root.

## Running tests locally without a full conda build

If a single test fails inside conda-forge CI and you need to iterate, you
do **not** need a full `conda-build` cycle (~15 min). Faster loop:

1. Install the latest published `orekit` package (or, after a failed
   conda-build, install from `~/miniforge3/conda-bld/broken/orekit-*.tar.bz2`):
   ```bash
   conda create -n orekit_validate -c conda-forge "python=3.12" "openjdk=8.*" jcc
   conda install -n orekit_validate <path-to-package>.tar.bz2
   ```
2. Run the patched test directly from `test/` cwd, against the env's python:
   ```bash
   cd test
   ~/miniforge3/envs/orekit_validate/bin/python -m unittest \
     SomeTest.SomeTestClass.someTestMethod -v
   ```
   Each test sets its own data root (e.g. `setup_orekit_curdir("resources/regular-data")`
   or `setup_orekit_data(filenames=[...])`) so paths resolve relative to
   `test/` as cwd.

This proves the test logic without rebuilding JCC. Use it when you
already trust the build pipeline.

## AI working notes

- **This repo is a staging area, not a build system.** When the user says
  "the build", they usually mean the conda-forge build in `orekit-feedstock`.
- **Loose JARs at the repo root are intentional.** Do not move them into a
  subdirectory — build.sh expects them next to `$SRC_DIR`.
- **Don't regenerate stubs unless asked.** The `orekit_stubs/` tree is
  ~30 MB of `.pyi` files and rebuilding requires a JVM with jpype.
- **`orekit_jpype/` is unrelated to the conda package.** Don't conflate.
- **The four-repo chain matters for debugging:** failures in conda-build
  often point at the wrong repo. A C++ compile error is *probably* JCC, a
  Java method missing is *probably* the Orekit fork, a SHA mismatch is
  *this* repo, a `--jar` filename mismatch is the feedstock.
- The user (Petrus) is a core contributor to this whole stack. Default to
  treating his judgement on architecture choices as authoritative; ask
  before refactoring shared conventions.
