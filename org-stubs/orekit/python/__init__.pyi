import org.hipparchus.analysis
import typing



class PythonUnivariateFunction(org.hipparchus.analysis.UnivariateFunction):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def value(self, double: float) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.python")``.

    PythonUnivariateFunction: typing.Type[PythonUnivariateFunction]
