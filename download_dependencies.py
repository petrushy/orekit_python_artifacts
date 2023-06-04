# This stubgenj seems to work best under java v11
# pip index versions stubgenj
# 

import subprocess, os

import shutil

VERSION = "2.3"
TARGET_DIRECTORY_JAVADOC = "./javadoc"
TARGET_DIRECTORY = "."

STUBS_DIRECTORY = "./orekit_stubs"

def backup_directory(dir_path):
    if os.path.exists(dir_path):
        os.rename(dir_path, dir_path + '_backup')

def delete_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
         
items = ["hipparchus-stat",
         "hipparchus-optim",
         "hipparchus-ode",
         "hipparchus-geometry",
         "hipparchus-fitting",
         "hipparchus-filtering",
         "hipparchus-core"]

for item in items:
    # Download the jar file
    command_jar = f"mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:copy -Dartifact=org.hipparchus:{item}:{VERSION} -DoutputDirectory={TARGET_DIRECTORY} -Dmdep.useBaseVersion=true"
    subprocess.call(command_jar, shell=True)

    # Download the javadoc
    command_javadoc = f"mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:copy -Dartifact=org.hipparchus:{item}:{VERSION}:javadoc -DoutputDirectory={TARGET_DIRECTORY_JAVADOC} -Dmdep.useBaseVersion=true"
    subprocess.call(command_javadoc, shell=True)

command_create_stubs = f"python -m stubgenj --convert-strings --classpath \"../*.jar:../javadoc/*.jar\" org.orekit  org.hipparchus"
# --no-jpackage-stubs ?

backup_directory(STUBS_DIRECTORY)
os.makedirs(STUBS_DIRECTORY, exist_ok=True)

subprocess.call(command_create_stubs, shell=True, cwd=STUBS_DIRECTORY)

delete_directory(STUBS_DIRECTORY+"_backup")