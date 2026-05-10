
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import com.sun.source.util
import typing



class DefaultDataContextPlugin(com.sun.source.util.Plugin, com.sun.source.util.TaskListener):
    """
    Processes DefaultDataContext to issue warnings at compile time.
    
    To use this plugin add -Xplugin:dataContextPlugin to the javac command line. Tested with OpenJDK 8 and 11.
    
    Do not reference this class unless executing within javac or you have added jar to the class path. jar is part of the JDK, not JRE, and is typically located at jar.
    
    Since:
        10.1
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def finished(self, taskEvent: com.sun.source.util.TaskEvent) -> None:
        """
        Specified by: finished in interface TaskListener
        
        
        """
        ...
    def getName(self) -> str:
        """
        Specified by: getName in interface Plugin
        
        
        """
        ...
    def init(self, javacTask: com.sun.source.util.JavacTask, *args: str) -> None:
        """
        Specified by: init in interface Plugin
        
        
        """
        ...
    def started(self, taskEvent: com.sun.source.util.TaskEvent) -> None:
        """
        Specified by: started in interface TaskListener
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.compiler.plugin")``.

    DefaultDataContextPlugin: typing.Type[DefaultDataContextPlugin]
