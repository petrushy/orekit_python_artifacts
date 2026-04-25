
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang.annotation
import typing



class DefaultDataContext(java.lang.annotation.Annotation):
    """
    Indicates that the annotated method, field, or constructor uses the default data context. Can be used to emit warnings similar to @Deprecated.
    
    Since:
        10.1
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.annotation")``.

    DefaultDataContext: typing.Type[DefaultDataContext]
