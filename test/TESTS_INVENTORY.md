# Tests inventory

This file tracks the Python test suite for the JCC-built `orekit` package
relative to its two reference points:

1. **Java upstream** — `Orekit/src/test/java/...` in the petrushy/Orekit fork.
   Most Python tests are line-by-line translations of one Java JUnit test.
2. **jpype binding** — the parallel `orekit_jpype` project at
   `gitlab.orekit.org/orekit/orekit_jpype`. They have been translating Java
   tests into pytest/unittest form on their side. Many of those translations
   are also valuable to JCC, modulo the JCC ↔ jpype API differences.

This file's purpose is to make the gap visible and trackable across multiple
sessions. Update it whenever a test is translated, deferred, or marked
not-applicable.

For the per-test conventions (data-root mirroring Java's `Utils.setDataRoot`,
the `unittest.TestCase` style, etc.) see [../CLAUDE.md](../CLAUDE.md).

## Status legend

- ✅ **done** — translated and passing in JCC.
- 🟡 **in-progress** — translation started, not green yet.
- 🔵 **planned** — known candidate, not started.
- ⛔ **n/a** — jpype-specific (or otherwise inapplicable to JCC) and won't
  be translated. Reason recorded.
- 🟠 **JCC-only** — exists here, no jpype counterpart. Listed for symmetry.

## Conventions for translation work

There are two distinct translation paths:

- **jpype Python → JCC Python** (covered first below). Easier — most of the
  code structure carries over; you mostly swap a handful of jpype-specific
  patterns for JCC-specific ones.
- **Java JUnit → JCC Python directly** (covered second). Used when no jpype
  port exists, or when the jpype port lags behind the Java upstream.

Both share the same JCC-side conventions; they differ in what you start from.

### A. Porting from jpype to JCC

When porting a jpype test to JCC, expect to change at minimum:

1. **Module imports** — `orekit_jpype` → `orekit`,
   `orekit_jpype.pyhelpers` → `orekit.pyhelpers`.
2. **Interface implementations** — replace `@JImplements(EventHandler)` /
   `@JOverride` with subclassing of the corresponding `PythonXxx` bridge
   class (e.g. `class MyHandler(PythonEventHandler):`). The bridge class
   requires `super().__init__()` in `__init__` to register the Python
   instance with the Java side. All abstract methods must be defined,
   even as no-ops, because JCC dispatches via `registerNatives` on the
   declared method set.
3. **Abstract-class subclassing** — same pattern, `PythonAbstractXxx`.
4. **Type casting** — JCC needs explicit `Foo.cast_(obj)` where jpype
   auto-casts.
5. **Data root** — change `setup_orekit_curdir("resources")` to mirror
   the Java equivalent's `Utils.setDataRoot(...)` value (most often
   `"resources/regular-data"`). See the EOP gap gotcha in CLAUDE.md.
   Multi-root tests should use the new
   `setup_orekit_data(filenames=[...], from_pip_library=False)`.
6. **Test runner shape** — keep `unittest.TestCase` classes ending with
   `if __name__ == '__main__': unittest.main()` to match the existing
   28-test convention. The conda recipe runs each `*.py` as a script and
   trusts the exit code.
7. **Numpy / `JArray_double*` numpy converters** — not available in the
   JCC pyhelpers (deferred). If a jpype test uses
   `JArray_double2D(np_array)` or similar numpy-aware helpers, either
   construct the `JArray('double')` manually or skip the affected
   assertions.
8. **`clear_factories()`** — not available in JCC pyhelpers. If a jpype
   test relies on it for isolation between test methods, restructure or
   skip the relevant logic.
9. **Prefer Python stdlib over Java equivalents.** When a Java call has
   a behaviour-equivalent Python stdlib counterpart, use the Python form
   — it reads better and avoids an unnecessary JVM round-trip:
   `FastMath.toRadians/toDegrees` → `math.radians/math.degrees`,
   `FastMath.PI` → `math.pi`, `FastMath.cos/sin/sqrt/exp/log/atan2` →
   `math.cos/sin/...`, `FastMath.abs` → `abs()`, `FastMath.min/max` →
   `min/max`. Drop the `org.hipparchus.util.FastMath` import once all
   call sites are replaced. Keep the Java call only when the argument is
   a `CalculusFieldElement<T>` (Python's `math` doesn't handle field
   types) or when bit-exact agreement with the Java reference matters
   for a tight assertion.

### B. Porting directly from Java to JCC

Use this path when the jpype side has no port, or when the Java upstream
has changed substantially since jpype's port was written. Read the Java
source first, understand what it asserts, then write Python that exercises
the same Orekit code paths. The translation is not mechanical — Java is
class-and-type-heavy, Python is duck-typed; just transliterating a Java
file character-for-character produces ugly Python.

#### Mechanical mappings

| Java | Python (JCC) |
|---|---|
| `@Test public void testFoo()` | `def testFoo(self):` inside a `unittest.TestCase` subclass |
| `@BeforeEach public void setUp()` | `def setUp(self):` |
| `@BeforeAll public static void setUpClass()` | `@classmethod def setUpClass(cls):` |
| `@AfterEach` / `@AfterAll` | `def tearDown(self):` / `@classmethod def tearDownClass(cls):` |
| `Assertions.assertEquals(expected, actual)` | `self.assertEqual(expected, actual)` |
| `Assertions.assertEquals(exp, act, eps)` | `self.assertAlmostEqual(exp, act, delta=eps)` |
| `Assertions.assertTrue(x)` / `assertFalse(x)` | `self.assertTrue(x)` / `self.assertFalse(x)` |
| `Assertions.assertNull(x)` / `assertNotNull(x)` | `self.assertIsNone(x)` / `self.assertIsNotNone(x)` |
| `Assertions.assertThrows(E.class, () -> code)` | `with self.assertRaises(...)` (use `JavaError`/`InvalidArgsError` from `orekit` for Java-side exceptions) |
| `Utils.setDataRoot("regular-data")` | module-level `setup_orekit_curdir("resources/regular-data")` (single root) or `setup_orekit_data(filenames=[...], from_pip_library=False)` (multi root). See gotcha in [../CLAUDE.md](../CLAUDE.md). |
| `final double x = 1.5;` | `x = 1.5` (drop `final`, drop type) |
| `double[] arr = {1.0, 2.0};` | `arr = JArray('double')([1.0, 2.0])` if Java needs an array, else just a Python list |
| `String s = "foo";` | `s = "foo"` |
| `List<Foo> list = new ArrayList<>();` then `list.add(x)` | `list = ArrayList()` then `list.add(x)` (don't try `ArrayList([...])` — JCC has no Python-list overload) |
| `Map<K,V> m = new HashMap<>(); m.put(k, v);` | `m = HashMap(); m.put(k, v)` |
| `for (Foo f : iter)` | `for f in iter:` (most Orekit collections expose Python iteration) |
| `Stream<X> s = ...; s.filter(...).map(...)` | restructure as Python loop / list comprehension; JCC's stream wrapping is awkward |
| `try (var x = ...)` | `with x:` only if the Java type is wrapped as a Python context manager — most aren't, so use explicit `try / finally` and call `close()` yourself |
| `throw new RuntimeException("msg");` | `raise RuntimeError("msg")` (don't call into Java unless you specifically want a Java exception in the test) |
| Anonymous inner class implementing `EventHandler` | a local Python class subclassing `PythonEventHandler` (see "Subclassing" below) |
| `(date) -> { ... }` lambda | a small class subclassing the matching `PythonXxx` bridge (JCC can't bridge a bare Python lambda back to Java) |
| `FastMath.toRadians(deg)` | `math.radians(deg)` (see rule 9 above) |

#### Subclassing Java types in Python

This is the place Java-direct ports differ most from jpype. Java tests
freely use `new EventHandler() { ... }` anonymous subclasses; JCC needs an
explicit `PythonXxx` bridge subclass.

```python
from org.orekit.propagation.events.handlers import PythonEventHandler
from org.hipparchus.ode.events import Action

class MyHandler(PythonEventHandler):
    def __init__(self, outer_test):
        super().__init__()           # required: registers Python obj with Java
        self.outer = outer_test

    def init(self, initialState, target, detector):
        pass

    def eventOccurred(self, s, detector, increasing):
        # ... do work ...
        return Action.CONTINUE

    def resetState(self, detector, oldState):
        return oldState

    def getHandler(self):            # required by JCC bridge even though
        pass                          # the Java EventHandler interface
                                      # doesn't declare it

    def finish(self, finalState, detector):
        pass
```

Rules:

- The bridge class for `org.orekit.X.Y` lives at `org.orekit.X.PythonY`
  (or `PythonAbstractY` for abstract bases). Find it via `javap` against
  `orekit-<ver>-python-wrapper.jar` if uncertain.
- Always call `super().__init__()` at the top of `__init__`. Without it,
  the Python instance pointer is never set on the Java side and the next
  Java→Python callback dereferences NULL and SEGVs.
- Implement every native method the bridge declares — even if the Java
  interface only marks one method abstract. JCC `registerNatives` binds
  against the bridge's full method set; an unimplemented native fails at
  the JNI call. When in doubt, mirror the method set used by an
  established `PythonXxx` subclass elsewhere in `test/`.
- Don't try to bridge a Python lambda back to Java. Always wrap in a
  bridge subclass.

#### Numerics, types, and overload selection

- **`int` ≠ `double`.** JCC's `_parseArgs` does not widen Python `int` to
  Java `double`. Whenever Java has `double`/`float` parameters and your
  Python value is a literal or `int`-valued, write `2500.0` not `2500`.
  This is the single biggest source of `InvalidArgsError` after a port.
- **Generics drop in Python.** `List<Foo>` becomes `List`; `Foo<T>`
  becomes `Foo`. If the original Java code uses `Foo.<Bar>bar()` style
  type witnesses, drop them — JCC chooses the overload at runtime from
  argument types.
- **Casting.** Java's implicit upcasts and downcasts via `(Foo) x` become
  `Foo.cast_(x)` in JCC. If a Java method returns `Object` or a parent
  type and the Python code needs a method on the actual subtype, cast
  first. Casting is also the workaround for the JCC-ignores-default-method
  gotcha (see [../CLAUDE.md](../CLAUDE.md)).
- **Strings.** Java `String` and Python `str` interconvert transparently
  in arguments and return values. No conversion calls needed.

#### Test discovery and the conda recipe

The conda recipe runs each `*.py` in `test/` as a script (see
`orekit-feedstock/recipe/run_test.sh`) and trusts the exit code. So:

- End every translated test file with `if __name__ == '__main__':
  unittest.main()`.
- Don't put work at module level beyond `orekit.initVM()` and
  `setup_orekit_curdir(...)` — anything failing at import time is reported
  as a test failure with no per-method granularity.
- Helper modules (no `unittest.TestCase`) still need to exit 0 when run
  as scripts. Put any throwaway smoke test under `if __name__ ==
  '__main__':`.

#### Workflow

1. Find the Java file at `Orekit/src/test/java/.../<Name>Test.java`.
2. Read its `@BeforeEach setUp()` for the data root pattern. Note any
   `GravityFieldFactory.addPotentialCoefficientsReader(...)` and similar
   model-registration calls — those need explicit registration in Python
   too.
3. Write the Python skeleton: imports, `unittest.TestCase` subclass,
   `setUp` mirroring the Java setup, then one `test_xxx` per `@Test` Java
   method.
4. Translate each `@Test` method body. Apply the mechanical mappings
   above; substitute Pythonic forms where rule 9 allows.
5. Run with `~/miniforge3/envs/orekit_validate/bin/python
   test/<Name>Test.py -v` from the repo root. Iterate on
   `InvalidArgsError`s (usually int-vs-double) and missing imports.
6. Re-run the full suite to confirm no regression. Update this inventory
   with a ✅ row noting the non-obvious adaptations.

If a Java test pattern does not have a clean Python translation (e.g. it
relies heavily on Java reflection, anonymous subclasses of classes
without a `PythonXxx` bridge, or stream-fluent APIs), prefer marking the
test ⛔ with a clear reason rather than producing a contorted Python
adaptation that drifts from the Java upstream.

## Translated tests (✅) — already in `test/`

These exist in both bindings or are originals on the JCC side. Listed for
completeness so the table reflects total coverage.

| File | jpype counterpart | Java original | Notes |
|---|---|---|---|
| AltitudeDetectorTest.py | yes | propagation/events/ | |
| BackAndForthDetectorTest.py | yes | propagation/events/ | |
| BrouwerLyddanePropagatorTest.py | yes | propagation/analytical/ | uses multi-root `setup_orekit_data` |
| Context.py | yes | (helper, not a test) | |
| DateconversionTest.py | yes | (Python-specific; date conversion) | |
| EstimationTestUtils.py | yes | estimation/EstimationTestUtils.java | helper used by IodGibbs/IodLaplace; uses `setup_orekit_data` |
| EventDetectorTest.py | yes | propagation/events/ | |
| EventHandlerTest.py | yes | propagation/events/handlers/ | |
| FieldStopOnDecreasingTest.py | yes | propagation/events/ | |
| FixedRateTest.py | no (JCC-only) | attitudes/ | |
| GroundFieldOfViewDetectorTest.py | yes | propagation/events/ | |
| ImpulseManeuverTest.py | yes | forces/maneuvers/ | |
| InterSatDirectViewDetectorTest.py | yes | propagation/events/ | uses cast to `PVCoordinatesProvider` for the `getPVCoordinates(date, frame)` interface-default-method gotcha |
| IodGibbsTest.py | yes | estimation/iod/ | |
| IodLaplaceTest.py | yes | estimation/iod/ | |
| KeplerianConverterTest.py | yes | orbits/ | |
| KlobucharModelTest.py | yes | models/earth/ionosphere/ | |
| MeasurementCreator.py | yes | (helper, not a test) | |
| NodeDetectorTest.py | yes | propagation/events/ | |
| OrekitDataLoadTest.py | no (JCC-only) | (Python-specific; data loader) | |
| OrekitStepHandlerTest.py | yes | propagation/sampling/ | |
| PVMeasurementCreator.py | yes | (helper, not a test) | |
| SmallManeuverAnalyticalModelTest.py | yes | propagation/analytical/ | |
| SpinStabilizedTest.py | yes | attitudes/ | |
| TransformTest.py | yes | frames/ | |

## JCC-only (🟠)

These are part of the JCC suite but the jpype side hasn't translated them.
No translation work is needed on our side; flagged for symmetry.

| File | Why JCC-only |
|---|---|
| AbstractDetectorTest.py | Tests Python subclassing of `AbstractDetector` via `PythonAbstractDetector` — only possible with JCC |
| FixedRateTest.py | Existed in the JCC suite before the jpype project started |
| GroundPointingTest.py | Tests subclassing of `PythonGroundPointing` — JCC-specific bridge |
| OrekitDataLoadTest.py | Python-side helper test |

## Translation candidates from jpype (🔵 / 🟡 / ⛔)

Source: `Orekit/orekit_jpype/test/`. Sorted by recommended translation order.

| Status | File | Lines | Java original | Notes / blockers |
|---|---|---|---|---|
| ✅ done | EphemerisEventsTest.py | 162 | propagation/analytical/EphemerisEventsTest.java | Translated 2026-05-11. Adaptations: `int → float` for `mass=2500.0` and `math.radians(261.0)` (Pythonic substitution; JCC's `_parseArgs` is strict on primitive types where jpype auto-converts); `ArrayList(python_list)` → populate via `.add()` in a loop; `ephem.clearStepHandlers()` → `Propagator.cast_(ephem).clearStepHandlers()` because `clearStepHandlers` is a default method on the `Propagator` interface. Same `regular-data` root as Java. 4/4 test methods pass. |
| ✅ done | LeastSquaresTleGenerationAlgorithmTest.py | 91 | propagation/analytical/tle/generation/ | Translated 2026-05-11. Adaptations: `forEach(lambda d: d.setSelected(True))` → `for d in tle.getParametersDrivers(): d.setSelected(True)` (JCC can't bridge Python lambdas into a `java.util.function.Consumer`). 3/3 test methods pass. |
| ✅ done | FixedPointTleGenerationAlgorithmTest.py | 214 | propagation/analytical/tle/generation/ | Translated 2026-05-11. Same lambda-to-loop fix as above; `int → float` already in source; `math.pi` substituted for `FastMath.PI`. NEW gotcha: `FieldTLE.getParameters(field)` and `getParameters(field, date)` are default methods on `ParameterDriversProvider` interface — JCC doesn't dispatch them on subclasses, so cast: `ParameterDriversProvider.cast_(tle).getParameters(field)`. 12/12 test methods pass. |
| ✅ done | HaloOrbitTest.py | 218 | orbits/HaloOrbitTest.java | Translated 2026-05-11. CR3BP / three-body. Adaptations: multi-root data via `setup_orekit_data(["resources/cr3bp", "resources/regular-data"])` (mirrors Java's `setDataRoot("cr3bp:regular-data")`); explicit `JArray_double([...])` for the integrator's `vecAbsoluteTolerances`/`vecRelativeTolerances` `double[]` parameters; `OrekitException` (Java) → `JavaError` (Python) in `assertRaises`; `int → float` in literals (`8.0e6`, `1.0`). 5/5 test methods pass. |
| ✅ done | SpacecraftStateInterpolatorTest.py | 307 | propagation/SpacecraftStateInterpolatorTest.java | Translated 2026-05-11. NEW gotcha: `NumericalPropagator.tolerances(...)` returns `double[][]`, which JCC wraps as `JArray_object`; indexing returns Object that the integrator constructor rejects. Cast each row: `JArray('double').cast_(tolerances[0])`. Also: `addAdditionalData("quadratic", JArray_double([dt*dt]))` instead of bare `dt*dt` (JCC needs explicit boxing); `sample` Python list → `ArrayList` for `interpolator.interpolate`. 2/2 test methods pass. |
| ✅ done | OpmParserTest.py | 347 | files/ccsds/ndm/odm/opm/OpmParserTest.java | Translated 2026-05-11. Several JCC-specific patterns surfaced: (1) `parser.parseMessage(source)` returns Object (generic erasure) — wrap in `Opm.cast_(...)`; (2) `OpmWriter.writeMessage` is on the `MessageWriter` interface as a default method — cast: `MessageWriter.cast_(writer).writeMessage(...)`; (3) `oe.getParts()[0]` returns Object — coerce with `str(...)` for string compares; (4) `assertEqual(date1, date2)` fails because JCC's `__eq__` on wrapped objects is identity, not `.equals()` — added an `assertDateEqual` helper that compares via `durationFrom`; (5) `len(java_list)` and `java_list[i]` don't work on JCC's `List` wrapper — use `.size()` and `.get(i)`; (6) `java.io.CharArrayWriter` not in JCC's java.io wrapping — `StringWriter` substitutes (both `Appendable`); (7) jpype's `myReader(@JImplements(DataSource.StreamOpener))` has no JCC bridge — round-trip writes to a `tempfile.NamedTemporaryFile` and re-reads via `DataSource(File(path))`. 5/5 test methods pass. |
| ✅ done (partial) | PyhelpersTest.py | 120 (jpype) → 99 (JCC) | (no Java equivalent — pyhelpers is Python-only) | Translated 2026-05-11 as a partial port. Covers: `setup_orekit_data` from a single folder, from a list of paths (multi-root), with `None` (raises), with an invalid path (raises `FileNotFoundError`); `setup_orekit_curdir` backward-compat wrapper; `download_orekit_data_curdir` (gated behind `OREKIT_TEST_NETWORK=1` env var). Skipped: `clear_factories` tests (helper deferred), numpy `JArray_double2D` (not ported), numpy `to_elevationmask` (not ported). 5 active tests pass + 1 skipped (network). pytest-style → unittest.TestCase conversion. |
| ⛔ n/a | OrekitConvertersTest.py | 49 | n/a | Tests jpype's automatic Python ↔ Java converters: `abs_date.to_datetime()`, `AbsoluteDate(py_datetime, 0.0)`, `__repr__` formatting, numpy-aware `JArray_double2D`. None of these mechanisms exist in JCC; the test surface is jpype-specific by design. |
| ⛔ n/a | DefaultMethodsTest.py | 117 | (no Java equivalent — this test specifically validates jpype handles default methods on inherited interfaces) | Was written for jpype to verify it dispatches Java interface default methods on subclasses. JCC explicitly does NOT (see CLAUDE.md "JCC ignores Java interface default methods"). The corresponding JCC behaviour is "raise InvalidArgsError"; the workaround is `cast_()`. Translating this test would just hard-code the limitation; better to leave it as a jpype-only invariant. |

## In-development tests on the jpype side

Source: `Orekit/orekit_jpype/test-in-development/` and
`Orekit/orekit_jpype/tests-in-development/`.

| File | Notes |
|---|---|
| PythonDocstringTest.py | Tests stub-rendered docstrings; jpype-specific (jpype renders javadoc into docstrings; JCC does not) — likely ⛔. |
| TLEConverterTest.py | TLE conversion; candidate once the TLE generation tests above are done. |
| GroundPointingTest.py (jpype side) | jpype's port of the same test JCC already has — JCC ↔ jpype divergence point. |

## In-development tests on the JCC side

Source: `tests_in_development/` in this repo. Listed for completeness.

| File | Notes |
|---|---|
| AEMTest.py | CCSDS AEM; needs review |
| DateDetectorTest.py | event detection on a fixed date |
| IntegratedEphemerisTest.py | uses the legacy `JArray_double2D(rows, cols)` signature — leave intact (we kept the old signature in pyhelpers for this caller) |
| OrekitFixedStepHandlerMultiplexerTest.py | step-handler multiplexer |
| MeasurementCreator.py | helper |

## Workflow for adding a new translation

1. Pick a 🔵 from "Translation candidates from jpype" (smallest first when
   possible).
2. Read both the jpype test source and the Java original; note the data
   root used in `Utils.setDataRoot(...)`.
3. Translate following the conventions above. Place the new file in
   `test/`. End the file with `if __name__ == '__main__': unittest.main()`.
4. Validate locally with `~/miniforge3/envs/orekit_validate/bin/python
   test/<NewTest>.py`. (If the new test depends on the modernised
   pyhelpers, copy `pyhelpers.py` over the env's installed copy first —
   see [../CLAUDE.md](../CLAUDE.md) "Running tests locally without a full
   conda build".)
5. Re-run the full suite (28 + 1 = 29 expected) to confirm no regression.
6. Move the entry from 🔵 to ✅ in this file with a short note on any
   non-obvious adaptations.
7. Commit with a message like `test: translate <Name>Test from
   orekit_jpype`.

## Counts

- JCC suite today: 35 files (31 tests + 3 helpers + 1 `__init__.py`).
- jpype suite: 35 files (incl. helpers and runner).
- Translation queue (🔵): 1 (Rugged).
- Translated to date (✅): 7 (EphemerisEvents, LeastSquaresTleGen, FixedPointTleGen, Pyhelpers-partial, HaloOrbit, SpacecraftStateInterpolator, OpmParser).
- Marked n/a (⛔): 2 (OrekitConverters, DefaultMethods).

## Translation lessons learned (running list)

Patterns observed during ports — add to this list as new ones surface so
future translators don't repeat the discovery cost.

- **JCC primitive-type strictness.** `_parseArgs` does NOT widen Python
  `int` to Java `double`. Use `2500.0`, not `2500`; `FastMath.toRadians(261.0)`,
  not `FastMath.toRadians(261)`. jpype auto-widens; JCC fails with
  `InvalidArgsError`. Whenever jpype source has a literal int passed to a
  Java method that takes `double`, change to a float literal.
- **`ArrayList(python_list)` doesn't auto-convert.** JCC's `ArrayList`
  exposes only `ArrayList()`, `ArrayList(int)`, and `ArrayList(Collection)`;
  a Python list isn't a Collection. Build with `.add()` in a loop.
- **Interface default methods need a cast.** Anywhere the jpype test calls
  a method that's a `default` method on a Java interface (e.g.
  `Propagator.clearStepHandlers()`, the `Orbit.getPVCoordinates(date,
  frame)` case from `InterSatDirectViewDetectorTest`), JCC won't dispatch
  it on the subclass. Cast to the declaring interface first:
  `Propagator.cast_(ephem).clearStepHandlers()`.
- **`PythonXxx` bridge subclassing requires `super().__init__()`.** Without
  it, the Python instance isn't registered with the Java handle and JCC
  callbacks find a NULL Python pointer at runtime. Add it as the first
  line of every `__init__`.
- **Bridge subclasses must define every native method**, even if no-op.
  JCC `registerNatives` binds against the declared method set on the
  bridge class. If you skip one (e.g. omit `getHandler` on a
  `PythonEventHandler`), the JNI call hits an unbound native and fails.
  When in doubt, mirror the method set used by other working JCC tests
  in this directory.
- **Java lambdas → Python for-loops.** Anywhere the jpype source uses
  `collection.forEach(lambda x: do_thing(x))`, JCC needs explicit
  iteration: `for x in collection: do_thing(x)`. JCC can't bridge a
  Python lambda into a `java.util.function.Consumer` (the Java functional
  interface). Same applies to `Stream.map(...)`, `Stream.filter(...)`
  etc. — restructure as comprehensions or loops.
- **`getParameters(Field)` and `getParameters(Field, FieldAbsoluteDate)`
  on TLE / FieldTLE / similar.** These are default methods on
  `org.orekit.utils.ParameterDriversProvider`. JCC's wrapper for
  `FieldTLE` does NOT expose them (only `getParametersDrivers` /
  `parameters_`). Cast first:
  `ParameterDriversProvider.cast_(tle).getParameters(field)`. Same root
  cause as the `Orbit.getPVCoordinates(date, frame)` and
  `Propagator.clearStepHandlers()` cases.
- **Pytest → unittest.** When the jpype test uses pytest functions
  (`def test_xxx():`, `pytest.raises(...)`), wrap the methods in a
  `unittest.TestCase` subclass and use `self.assertRaises(...)`,
  `self.assertEqual(...)`, etc. Match the existing JCC suite convention
  so the conda recipe's `run_test.sh` (which calls each `*.py` as a
  script) treats them uniformly.
- **Network-dependent tests** (e.g. `download_orekit_data_curdir`)
  should be gated behind `@unittest.skipUnless(os.environ.get(
  "OREKIT_TEST_NETWORK"), ...)` so the conda CI doesn't depend on
  external connectivity. Run locally with `OREKIT_TEST_NETWORK=1` to
  exercise.
- **Java exception classes are NOT Python exceptions.** `assertRaises`
  needs `JavaError` (re-exported from `orekit`), not the Java
  exception class itself (`OrekitException`,
  `OrekitIllegalArgumentException`, etc.). To inspect the underlying
  Java side: `with self.assertRaises(JavaError) as ctx: ...; oe =
  OrekitException.cast_(ctx.exception.getJavaException())`. Then
  `oe.getSpecifier()` / `oe.getParts()` work as in Java.
- **Generic methods erase to Object.** Anywhere the Java method is
  generic (`<T> T parseMessage(DataSource)`,
  `<T> T cast(...)`), JCC returns the erased Object. Cast back at the
  call site: `Opm.cast_(parser.parseMessage(source))`. This pattern
  applies to all CCSDS parsers, generic factories, and the Field-aware
  TLE / propagator APIs.
- **`Object[]` returned by Java surfaces as JCC Object indexing.**
  `oe.getParts()[0]` returns Object, not str — coerce with
  `str(oe.getParts()[0])` or `String.cast_(...)` if you need a Python
  string for an `assertEqual` against a Python literal. Same applies to
  `Map.values()`, `Map.keySet()` returns, etc.
- **`==` on Java wrappers is identity, not `.equals()`.** Two distinct
  `AbsoluteDate` (or any other Java) wrapper instances representing the
  same value will compare unequal under `assertEqual`. Either:
  (a) compare via the domain-specific equality method
  (e.g. `actual.durationFrom(expected) == 0.0` for AbsoluteDate); or
  (b) call `.equals()` directly. For repeated patterns, define a small
  helper like `assertDateEqual` on the test class.
- **`len(java_list)` / `java_list[i]` don't work on JCC's `List`
  wrapper.** Even though concrete `ArrayList` instances may
  occasionally support them, JCC's wrapper for the `List` interface
  generally does NOT implement `__len__` or `__getitem__`. Use
  `java_list.size()` and `java_list.get(i)` — the underlying Java
  methods. Same caveat for `Map`: `m.size()` and `m.get(key)`.
- **`double[][]` index returns Object.** When a Java method returns
  `double[][]`, JCC wraps it as `JArray_object`. Indexing yields a
  generic Object that subsequent Java calls expecting `double[]` will
  reject with `InvalidArgsError`. Cast each row:
  `JArray('double').cast_(matrix[0])`.
- **`SpacecraftState.addAdditionalData("name", value)` needs explicit
  boxing.** The Java signature is `addAdditionalData(String, Object)`.
  Pass a Python float and JCC won't auto-box; pass a `JArray_double([
  value])` (or `Double` from `java.lang`) instead. Mirrors how
  `getAdditionalState("name")` returns a `double[]` on the read side.
- **java.io's wrapping is incomplete.** Not every `java.io` class is in
  the JCC build (see `--package java.io` in
  `orekit-feedstock/recipe/build.sh` for what is). `CharArrayWriter` is
  out; `StringWriter` is in. Both implement `Appendable`, so for
  Generator-style writers `StringWriter` is a clean substitute.
- **No `PythonStreamOpener` (or generally, no bridge for many Java
  functional interfaces).** When jpype tests use
  `@JImplements(DataSource.StreamOpener)` to provide a stream from
  memory, JCC has no equivalent because the Orekit Python wrapper jar
  doesn't ship a `PythonStreamOpener` bridge. The portable workaround
  is to write the bytes to a `tempfile.NamedTemporaryFile`, use
  `DataSource(File(path))`, and clean up in a `finally` block.
