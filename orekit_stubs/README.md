# orekit_jpype
This repository contains a python installable packaage of stubs for orekit and hipparcus libraries.

They are generated with stubgenj
 
To generate stub files (not working yet), use the stubgenj package 
https://gitlab.cern.ch/scripting-tools/stubgenj

and command line:
python -m stubgenj --convert-strings --classpat "orekit_jpype/jars/*.jar" org.orekit  org.hipparchus java
