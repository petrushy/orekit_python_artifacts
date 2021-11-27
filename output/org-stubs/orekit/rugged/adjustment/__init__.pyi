import java.lang
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.rugged.adjustment.measurements
import typing



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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.adjustment")``.

    LeastSquareAdjuster: typing.Type[LeastSquareAdjuster]
    OptimizerId: typing.Type[OptimizerId]
    measurements: org.orekit.rugged.adjustment.measurements.__module_protocol__
