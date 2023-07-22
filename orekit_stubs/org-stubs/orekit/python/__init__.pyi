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
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
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
            Gets a result.
        
            Specified by:
                :meth:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Supplier.html?is` in
                interface :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.util.function.Supplier?is`
        
            Returns:
                a result
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class PythonUnivariateFunction(org.hipparchus.analysis.UnivariateFunction):
    """
    public class PythonUnivariateFunction extends :class:`~org.orekit.python.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.python.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.UnivariateFunction?is`
    
        import org.hipparchus.analysis.UnivariateFunction;
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
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
    PythonSupplier: typing.Type[PythonSupplier]
    PythonUnivariateFunction: typing.Type[PythonUnivariateFunction]
