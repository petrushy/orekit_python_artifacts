import java.util.function
import org.hipparchus
import org.hipparchus.analysis
import typing



class PythonFieldUnivariateFunction(org.hipparchus.analysis.FieldUnivariateFunction):
    """
    public class PythonFieldUnivariateFunction extends :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.python.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.FieldUnivariateFunction?is`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> _value__T:
        """
        
            Specified by:
                :meth:`~org.orekit.python.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.FieldUnivariateFunction.html?is` in
                interface :class:`~org.orekit.python.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.FieldUnivariateFunction?is`
        
        
        """
        ...

_PythonFunction__T = typing.TypeVar('_PythonFunction__T')  # <T>
_PythonFunction__R = typing.TypeVar('_PythonFunction__R')  # <R>
class PythonFunction(java.util.function.Function[_PythonFunction__T, _PythonFunction__R], typing.Generic[_PythonFunction__T, _PythonFunction__R]):
    """
    public class PythonFunction<T, R> extends :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Function?is`<T, R>
    """
    def __init__(self): ...
    def apply(self, t: _PythonFunction__T) -> _PythonFunction__R:
        """
        
            Specified by:
                :meth:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Function.html?is` in
                interface :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Function?is`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

_PythonSupplier__T = typing.TypeVar('_PythonSupplier__T')  # <T>
class PythonSupplier(java.util.function.Supplier[_PythonSupplier__T], typing.Generic[_PythonSupplier__T]):
    """
    public class PythonSupplier<T> extends :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Supplier?is`<T>
    
        A wrapper of the import java.util.function.Supplier Interface
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def get(self) -> _PythonSupplier__T:
        """
        
            Specified by:
                :meth:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Supplier.html?is` in
                interface :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Supplier?is`
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

class PythonUnivariateFunction(org.hipparchus.analysis.UnivariateFunction):
    """
    public class PythonUnivariateFunction extends :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.python.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.UnivariateFunction?is`
    
        import org.hipparchus.analysis.UnivariateFunction;
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...
    def value(self, double: float) -> float:
        """
        
            Specified by:
                :meth:`~org.orekit.python.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.UnivariateFunction.html?is` in
                interface :class:`~org.orekit.python.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.UnivariateFunction?is`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.python")``.

    PythonFieldUnivariateFunction: typing.Type[PythonFieldUnivariateFunction]
    PythonFunction: typing.Type[PythonFunction]
    PythonSupplier: typing.Type[PythonSupplier]
    PythonUnivariateFunction: typing.Type[PythonUnivariateFunction]
