import com.sun.source.util
import typing



class DefaultDataContextPlugin(com.sun.source.util.Plugin, com.sun.source.util.TaskListener):
    """
    @SupportedAnnotationTypes(value="org.orekit.annotation.DefaultDataContext") @SupportedSourceVersion(value=RELEASE_8) public class DefaultDataContextPlugin extends Object implements com.sun.source.util.Plugin, com.sun.source.util.TaskListener
    
        Processes :class:`~org.orekit.annotation.DefaultDataContext` to issue warnings at compile time.
    
        To use this plugin add :code:`-Xplugin:dataContextPlugin` to the javac command line. Tested with OpenJDK 8 and 11.
    
        Do not reference this class unless executing within :code:`javac` or you have added :code:`tools.jar` to the class path.
        :code:`tools.jar` is part of the JDK, not JRE, and is typically located at :code:`JAVA_HOME/../lib/tools.jar`.
    
        Since:
            10.1
    """
    def __init__(self): ...
    def finished(self, taskEvent: com.sun.source.util.TaskEvent) -> None:
        """
        
            Specified by:
                :code:`finished` in interface :code:`com.sun.source.util.TaskListener`
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`com.sun.source.util.Plugin`
        
        
        """
        ...
    def init(self, javacTask: com.sun.source.util.JavacTask, *string: str) -> None:
        """
        
            Specified by:
                :code:`init` in interface :code:`com.sun.source.util.Plugin`
        
        
        """
        ...
    def started(self, taskEvent: com.sun.source.util.TaskEvent) -> None:
        """
        
            Specified by:
                :code:`started` in interface :code:`com.sun.source.util.TaskListener`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.compiler.plugin")``.

    DefaultDataContextPlugin: typing.Type[DefaultDataContextPlugin]
