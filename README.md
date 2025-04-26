# orekit_python_artifacts
Primary jar's for python orekit


# To update:
- Update branch name of this repository to version-X.Y. Only major and minor versions.
- Update Orekit https://github.com/petrushy/Orekit and ensure it compiles well through the CI pipeline
- Copy two python orekit jars artifacts from https://github.com/petrushy/Orekit to repository, add jars to this repo.
- Remove old python jar from repository
- Check if updated hipparcus libraries exist, in that case update the ones in repo
- Generate stub files:
  - install stubgenj (https://gitlab.cern.ch/scripting-tools/stubgenj) and jpype
  - stubs are installed as a separate "package", located in orekit_stubs
  - subs are generated from both the java and javadoc jar files (generate with mvn javadoc:jar -Dmaven.javadoc.failOnError)
  - remove the old data dirs in orekit_stubs, while in the orekit_stubs directory:
  - python -m stubgenj --convert-strings --classpath "../*.jar" org.orekit  org.hipparchus java

in the orekit-feedstock repo:
- to use local file system for testing:

source:
  path: ../../orekit_python_artifacts

The build is now separating between python and original jars, to build only python extension:

mvn -B package -Ppython-jar --file pom.xml