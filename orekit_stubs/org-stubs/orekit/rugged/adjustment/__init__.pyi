import java.lang
import java.util
import org
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.rugged.adjustment.measurements
import org.orekit.rugged.api
import org.orekit.rugged.linesensor
import typing



class AdjustmentContext:
    def __init__(self, collection: typing.Union[java.util.Collection[org.orekit.rugged.api.Rugged], typing.Sequence[org.orekit.rugged.api.Rugged], typing.Set[org.orekit.rugged.api.Rugged]], observables: org.orekit.rugged.adjustment.measurements.Observables): ...
    def estimateFreeParameters(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str], typing.Set[str]], int: int, double: float) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.Optimum: ...
    def setOptimizer(self, optimizerId: 'OptimizerId') -> None: ...

class LeastSquareAdjuster:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, optimizerId: 'OptimizerId'): ...
    def optimize(self, leastSquaresProblem: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.Optimum: ...

class OptimizerId(java.lang.Enum['OptimizerId']):
    LEVENBERG_MARQUADT: typing.ClassVar['OptimizerId'] = ...
    GAUSS_NEWTON_LU: typing.ClassVar['OptimizerId'] = ...
    GAUSS_NEWTON_QR: typing.ClassVar['OptimizerId'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OptimizerId': ...
    @staticmethod
    def values() -> typing.List['OptimizerId']: ...

class GroundOptimizationProblemBuilder(org.orekit.rugged.adjustment.OptimizationProblemBuilder):
    def __init__(self, list: java.util.List[org.orekit.rugged.linesensor.LineSensor], observables: org.orekit.rugged.adjustment.measurements.Observables, rugged: org.orekit.rugged.api.Rugged): ...
    def build(self, int: int, double: float) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem: ...

class InterSensorsOptimizationProblemBuilder(org.orekit.rugged.adjustment.OptimizationProblemBuilder):
    def __init__(self, list: java.util.List[org.orekit.rugged.linesensor.LineSensor], observables: org.orekit.rugged.adjustment.measurements.Observables, collection: typing.Union[java.util.Collection[org.orekit.rugged.api.Rugged], typing.Sequence[org.orekit.rugged.api.Rugged], typing.Set[org.orekit.rugged.api.Rugged]]): ...
    def build(self, int: int, double: float) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem: ...

class OptimizationProblemBuilder: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.adjustment")``.

    AdjustmentContext: typing.Type[AdjustmentContext]
    GroundOptimizationProblemBuilder: typing.Type[GroundOptimizationProblemBuilder]
    InterSensorsOptimizationProblemBuilder: typing.Type[InterSensorsOptimizationProblemBuilder]
    LeastSquareAdjuster: typing.Type[LeastSquareAdjuster]
    OptimizationProblemBuilder: typing.Type[OptimizationProblemBuilder]
    OptimizerId: typing.Type[OptimizerId]
    measurements: org.orekit.rugged.adjustment.measurements.__module_protocol__
