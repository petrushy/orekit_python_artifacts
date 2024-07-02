import com.sun.source.util
import typing



class DefaultDataContextPlugin(com.sun.source.util.Plugin, com.sun.source.util.TaskListener):
    def __init__(self): ...
    def finished(self, taskEvent: com.sun.source.util.TaskEvent) -> None: ...
    def getName(self) -> str: ...
    def init(self, javacTask: com.sun.source.util.JavacTask, *string: str) -> None: ...
    def started(self, taskEvent: com.sun.source.util.TaskEvent) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.compiler.plugin")``.

    DefaultDataContextPlugin: typing.Type[DefaultDataContextPlugin]
