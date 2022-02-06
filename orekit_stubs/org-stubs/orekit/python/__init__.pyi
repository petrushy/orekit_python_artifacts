import java.util.function
import org.hipparchus.analysis
import typing



class PythonSupplier(java.util.function.Supplier):
    """
    public class PythonSupplier extends Object implements Supplier
    
        A wrapper of the import java.util.function.Supplier Interface
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def get(self) -> typing.Any:
        """
            Gets a result.
        
            Specified by:
                 in interface 
        
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
    public class PythonUnivariateFunction extends Object implements UnivariateFunction
    
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
                 in interface 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.python")``.

    PythonSupplier: typing.Type[PythonSupplier]
    PythonUnivariateFunction: typing.Type[PythonUnivariateFunction]
