
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util.function
import org.hipparchus
import org.hipparchus.analysis
import typing



class PythonFieldUnivariateFunction(org.hipparchus.analysis.FieldUnivariateFunction):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> _value__T:
        """
        Specified by: FieldUnivariateFunction in interface FieldUnivariateFunction
        
        
        """
        ...

_PythonFunction__T = typing.TypeVar('_PythonFunction__T')  # <T>
_PythonFunction__R = typing.TypeVar('_PythonFunction__R')  # <R>
class PythonFunction(java.util.function.Function[_PythonFunction__T, _PythonFunction__R], typing.Generic[_PythonFunction__T, _PythonFunction__R]):
    def __init__(self): ...
    def apply(self, t: _PythonFunction__T) -> _PythonFunction__R:
        """
        Specified by: Function in interface Function
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

_PythonSupplier__T = typing.TypeVar('_PythonSupplier__T')  # <T>
class PythonSupplier(java.util.function.Supplier[_PythonSupplier__T], typing.Generic[_PythonSupplier__T]):
    """
    A wrapper of the import java.util.function.Supplier Interface
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def get(self) -> _PythonSupplier__T:
        """
        Specified by: Supplier in interface Supplier
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonUnivariateFunction(org.hipparchus.analysis.UnivariateFunction):
    """
    import org.hipparchus.analysis.UnivariateFunction;
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...
    def value(self, x: float) -> float:
        """
        Specified by: UnivariateFunction in interface UnivariateFunction
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.python")``.

    PythonFieldUnivariateFunction: typing.Type[PythonFieldUnivariateFunction]
    PythonFunction: typing.Type[PythonFunction]
    PythonSupplier: typing.Type[PythonSupplier]
    PythonUnivariateFunction: typing.Type[PythonUnivariateFunction]
