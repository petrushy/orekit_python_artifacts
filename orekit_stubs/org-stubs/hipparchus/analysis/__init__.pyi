import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.analysis.function
import org.hipparchus.analysis.integration
import org.hipparchus.analysis.interpolation
import org.hipparchus.analysis.polynomials
import org.hipparchus.analysis.solvers
import typing



class BivariateFunction:
    def value(self, double: float, double2: float) -> float: ...

_CalculusFieldBivariateFunction__T = typing.TypeVar('_CalculusFieldBivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldBivariateFunction(typing.Generic[_CalculusFieldBivariateFunction__T]):
    def value(self, t: _CalculusFieldBivariateFunction__T, t2: _CalculusFieldBivariateFunction__T) -> _CalculusFieldBivariateFunction__T: ...

_CalculusFieldMultivariateFunction__T = typing.TypeVar('_CalculusFieldMultivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldMultivariateFunction(typing.Generic[_CalculusFieldMultivariateFunction__T]):
    def value(self, *t: _CalculusFieldMultivariateFunction__T) -> _CalculusFieldMultivariateFunction__T: ...

_CalculusFieldMultivariateMatrixFunction__T = typing.TypeVar('_CalculusFieldMultivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldMultivariateMatrixFunction(typing.Generic[_CalculusFieldMultivariateMatrixFunction__T]):
    def value(self, *t: _CalculusFieldMultivariateMatrixFunction__T) -> typing.List[typing.List[_CalculusFieldMultivariateMatrixFunction__T]]: ...

_CalculusFieldMultivariateVectorFunction__T = typing.TypeVar('_CalculusFieldMultivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldMultivariateVectorFunction(typing.Generic[_CalculusFieldMultivariateVectorFunction__T]):
    def value(self, *t: _CalculusFieldMultivariateVectorFunction__T) -> typing.List[_CalculusFieldMultivariateVectorFunction__T]: ...

_CalculusFieldUnivariateFunction__T = typing.TypeVar('_CalculusFieldUnivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateFunction(typing.Generic[_CalculusFieldUnivariateFunction__T]):
    def value(self, t: _CalculusFieldUnivariateFunction__T) -> _CalculusFieldUnivariateFunction__T: ...

_CalculusFieldUnivariateMatrixFunction__T = typing.TypeVar('_CalculusFieldUnivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateMatrixFunction(typing.Generic[_CalculusFieldUnivariateMatrixFunction__T]):
    def value(self, t: _CalculusFieldUnivariateMatrixFunction__T) -> typing.List[typing.List[_CalculusFieldUnivariateMatrixFunction__T]]: ...

_CalculusFieldUnivariateVectorFunction__T = typing.TypeVar('_CalculusFieldUnivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class CalculusFieldUnivariateVectorFunction(typing.Generic[_CalculusFieldUnivariateVectorFunction__T]):
    def value(self, t: _CalculusFieldUnivariateVectorFunction__T) -> typing.List[_CalculusFieldUnivariateVectorFunction__T]: ...

class FieldBivariateFunction:
    _toCalculusFieldBivariateFunction__T = typing.TypeVar('_toCalculusFieldBivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldBivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldBivariateFunction__T]) -> CalculusFieldBivariateFunction[_toCalculusFieldBivariateFunction__T]: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T, t2: _value__T) -> _value__T: ...

class FieldMultivariateFunction:
    _toCalculusFieldMultivariateFunction__T = typing.TypeVar('_toCalculusFieldMultivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldMultivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldMultivariateFunction__T]) -> CalculusFieldMultivariateFunction[_toCalculusFieldMultivariateFunction__T]: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, *t: _value__T) -> _value__T: ...

class FieldMultivariateMatrixFunction:
    _toCalculusFieldMultivariateMatrixFunction__T = typing.TypeVar('_toCalculusFieldMultivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldMultivariateMatrixFunction(self, field: org.hipparchus.Field[_toCalculusFieldMultivariateMatrixFunction__T]) -> CalculusFieldMultivariateMatrixFunction[_toCalculusFieldMultivariateMatrixFunction__T]: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, *t: _value__T) -> typing.List[typing.List[_value__T]]: ...

class FieldMultivariateVectorFunction:
    _toCalculusFieldMultivariateVectorFunction__T = typing.TypeVar('_toCalculusFieldMultivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldMultivariateVectorFunction(self, field: org.hipparchus.Field[_toCalculusFieldMultivariateVectorFunction__T]) -> CalculusFieldMultivariateVectorFunction[_toCalculusFieldMultivariateVectorFunction__T]: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, *t: _value__T) -> typing.List[_value__T]: ...

class FieldUnivariateFunction:
    _toCalculusFieldUnivariateFunction__T = typing.TypeVar('_toCalculusFieldUnivariateFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateFunction__T]) -> CalculusFieldUnivariateFunction[_toCalculusFieldUnivariateFunction__T]: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> _value__T: ...

class FieldUnivariateMatrixFunction:
    _toCalculusFieldUnivariateMatrixFunction__T = typing.TypeVar('_toCalculusFieldUnivariateMatrixFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateMatrixFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateMatrixFunction__T]) -> CalculusFieldUnivariateMatrixFunction[_toCalculusFieldUnivariateMatrixFunction__T]: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> typing.List[typing.List[_value__T]]: ...

class FieldUnivariateVectorFunction:
    _toCalculusFieldUnivariateVectorFunction__T = typing.TypeVar('_toCalculusFieldUnivariateVectorFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toCalculusFieldUnivariateVectorFunction(self, field: org.hipparchus.Field[_toCalculusFieldUnivariateVectorFunction__T]) -> CalculusFieldUnivariateVectorFunction[_toCalculusFieldUnivariateVectorFunction__T]: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> typing.List[_value__T]: ...

class FunctionUtils:
    @typing.overload
    @staticmethod
    def add(*univariateFunction: 'UnivariateFunction') -> 'UnivariateFunction': ...
    @typing.overload
    @staticmethod
    def add(*univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @typing.overload
    @staticmethod
    def collector(bivariateFunction: BivariateFunction, double: float) -> 'MultivariateFunction': ...
    @typing.overload
    @staticmethod
    def collector(bivariateFunction: BivariateFunction, univariateFunction: 'UnivariateFunction', double: float) -> 'MultivariateFunction': ...
    @staticmethod
    def combine(bivariateFunction: BivariateFunction, univariateFunction: 'UnivariateFunction', univariateFunction2: 'UnivariateFunction') -> 'UnivariateFunction': ...
    @typing.overload
    @staticmethod
    def compose(*univariateFunction: 'UnivariateFunction') -> 'UnivariateFunction': ...
    @typing.overload
    @staticmethod
    def compose(*univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @typing.overload
    @staticmethod
    def derivative(multivariateDifferentiableFunction: org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction, intArray: typing.List[int]) -> 'MultivariateFunction': ...
    @typing.overload
    @staticmethod
    def derivative(univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, int: int) -> 'UnivariateFunction': ...
    @staticmethod
    def fix1stArgument(bivariateFunction: BivariateFunction, double: float) -> 'UnivariateFunction': ...
    @staticmethod
    def fix2ndArgument(bivariateFunction: BivariateFunction, double: float) -> 'UnivariateFunction': ...
    @typing.overload
    @staticmethod
    def multiply(*univariateFunction: 'UnivariateFunction') -> 'UnivariateFunction': ...
    @typing.overload
    @staticmethod
    def multiply(*univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction) -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...
    @staticmethod
    def sample(univariateFunction: 'UnivariateFunction', double: float, double2: float, int: int) -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def toDifferentiable(multivariateFunction: 'MultivariateFunction', multivariateVectorFunction: 'MultivariateVectorFunction') -> org.hipparchus.analysis.differentiation.MultivariateDifferentiableFunction: ...
    @typing.overload
    @staticmethod
    def toDifferentiable(univariateFunction: 'UnivariateFunction', *univariateFunction2: 'UnivariateFunction') -> org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction: ...

class MultivariateFunction:
    def value(self, doubleArray: typing.List[float]) -> float: ...

class MultivariateMatrixFunction:
    def value(self, doubleArray: typing.List[float]) -> typing.List[typing.List[float]]: ...

class MultivariateVectorFunction:
    def value(self, doubleArray: typing.List[float]) -> typing.List[float]: ...

class ParametricUnivariateFunction:
    def gradient(self, double: float, *double2: float) -> typing.List[float]: ...
    def value(self, double: float, *double2: float) -> float: ...

class TrivariateFunction:
    def value(self, double: float, double2: float, double3: float) -> float: ...

class UnivariateFunction:
    def value(self, double: float) -> float: ...

class UnivariateMatrixFunction:
    def value(self, double: float) -> typing.List[typing.List[float]]: ...

class UnivariateVectorFunction:
    def value(self, double: float) -> typing.List[float]: ...

class PythonFieldUnivariateFunction(FieldUnivariateFunction):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    _value__T = typing.TypeVar('_value__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value(self, t: _value__T) -> _value__T: ...

class PythonUnivariateFunction(UnivariateFunction):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def value(self, double: float) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis")``.

    BivariateFunction: typing.Type[BivariateFunction]
    CalculusFieldBivariateFunction: typing.Type[CalculusFieldBivariateFunction]
    CalculusFieldMultivariateFunction: typing.Type[CalculusFieldMultivariateFunction]
    CalculusFieldMultivariateMatrixFunction: typing.Type[CalculusFieldMultivariateMatrixFunction]
    CalculusFieldMultivariateVectorFunction: typing.Type[CalculusFieldMultivariateVectorFunction]
    CalculusFieldUnivariateFunction: typing.Type[CalculusFieldUnivariateFunction]
    CalculusFieldUnivariateMatrixFunction: typing.Type[CalculusFieldUnivariateMatrixFunction]
    CalculusFieldUnivariateVectorFunction: typing.Type[CalculusFieldUnivariateVectorFunction]
    FieldBivariateFunction: typing.Type[FieldBivariateFunction]
    FieldMultivariateFunction: typing.Type[FieldMultivariateFunction]
    FieldMultivariateMatrixFunction: typing.Type[FieldMultivariateMatrixFunction]
    FieldMultivariateVectorFunction: typing.Type[FieldMultivariateVectorFunction]
    FieldUnivariateFunction: typing.Type[FieldUnivariateFunction]
    FieldUnivariateMatrixFunction: typing.Type[FieldUnivariateMatrixFunction]
    FieldUnivariateVectorFunction: typing.Type[FieldUnivariateVectorFunction]
    FunctionUtils: typing.Type[FunctionUtils]
    MultivariateFunction: typing.Type[MultivariateFunction]
    MultivariateMatrixFunction: typing.Type[MultivariateMatrixFunction]
    MultivariateVectorFunction: typing.Type[MultivariateVectorFunction]
    ParametricUnivariateFunction: typing.Type[ParametricUnivariateFunction]
    PythonFieldUnivariateFunction: typing.Type[PythonFieldUnivariateFunction]
    PythonUnivariateFunction: typing.Type[PythonUnivariateFunction]
    TrivariateFunction: typing.Type[TrivariateFunction]
    UnivariateFunction: typing.Type[UnivariateFunction]
    UnivariateMatrixFunction: typing.Type[UnivariateMatrixFunction]
    UnivariateVectorFunction: typing.Type[UnivariateVectorFunction]
    differentiation: org.hipparchus.analysis.differentiation.__module_protocol__
    function: org.hipparchus.analysis.function.__module_protocol__
    integration: org.hipparchus.analysis.integration.__module_protocol__
    interpolation: org.hipparchus.analysis.interpolation.__module_protocol__
    polynomials: org.hipparchus.analysis.polynomials.__module_protocol__
    solvers: org.hipparchus.analysis.solvers.__module_protocol__
