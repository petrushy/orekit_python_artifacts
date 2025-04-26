
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang.annotation
import typing



class DefaultDataContext(java.lang.annotation.Annotation):
    """
    :class:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.Documented?is` :class:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.Target?is`({:meth:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.ElementType.html?is`,:meth:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.ElementType.html?is`,:meth:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.ElementType.html?is`,:meth:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.ElementType.html?is`}) :class:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.Retention?is`(:meth:`~org.orekit.annotation.https:.docs.oracle.com.javase.8.docs.api.java.lang.annotation.RetentionPolicy.html?is`) public @interface DefaultDataContext
    
        Indicates that the annotated method, field, or constructor uses the default data context. Can be used to emit warnings
        similar to :code:`@Deprecated`.
    
        Since:
            10.1
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.annotation")``.

    DefaultDataContext: typing.Type[DefaultDataContext]
