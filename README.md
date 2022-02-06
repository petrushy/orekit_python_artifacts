# orekit_python_artifacts
Primary jar's for python orekit


# To update:
- Update branch name to version-X.Y
- Copy new python orekit jar to repository, add to git
- Remove old python jar from repository
- Check if updated hipparcus libraries exist, in that case update the ones in repo
- Generate stub files:
  - install stubgenj
  - stubs are installed as a separate "package", located in orekit_stubs
  - remove the old data dirs in orekit_stubs, while in the orekit_stubs directory:
  - python -m stubgenj --convert-strings --classpat "../*.jar" org.orekit  org.hipparchus java
