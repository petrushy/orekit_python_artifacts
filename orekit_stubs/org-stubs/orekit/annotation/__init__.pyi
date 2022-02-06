import java.lang.annotation
import typing



class DefaultDataContext(java.lang.annotation.Annotation):
    """
    @Documented @Target(value={CONSTRUCTOR,FIELD,METHOD,TYPE}) @Retention(value=CLASS) public @interface DefaultDataContext
    
        Indicates that the annotated method, field, or constructor uses the default data context. Can be used to emit warnings
        similar to :code:`@Deprecated`.
    
        Since:
            10.1
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.annotation")``.

    DefaultDataContext: typing.Type[DefaultDataContext]
