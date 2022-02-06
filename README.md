# orekit_python_artifacts
Primary jar's for python orekit


# To update:
- Update branch name to version-X.Y
- Copy new python orekit jar to repository, add to git
- Remove old python jar from repository
- Check if updated hipparcus libraries exist, in that case update the ones in repo
- Generate stub files:
  - install stubgenj (https://gitlab.cern.ch/scripting-tools/stubgenj) and jpype
  - stubs are installed as a separate "package", located in orekit_stubs
  - subs are generated from both the java and javadoc jar files
  - remove the old data dirs in orekit_stubs, while in the orekit_stubs directory:
  - python -m stubgenj --convert-strings --classpath "../*.jar" org.orekit  org.hipparchus
  - 
