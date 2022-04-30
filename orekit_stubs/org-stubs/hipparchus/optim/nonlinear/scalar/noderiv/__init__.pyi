import java.util
import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar
import org.hipparchus.random
import typing



class AbstractSimplex(org.hipparchus.optim.OptimizationData):
    def build(self, doubleArray: typing.List[float]) -> None: ...
    def evaluate(self, multivariateFunction: org.hipparchus.analysis.MultivariateFunction, comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None: ...
    def getDimension(self) -> int: ...
    def getPoint(self, int: int) -> org.hipparchus.optim.PointValuePair: ...
    def getPoints(self) -> typing.List[org.hipparchus.optim.PointValuePair]: ...
    def getSize(self) -> int: ...
    def iterate(self, multivariateFunction: org.hipparchus.analysis.MultivariateFunction, comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None: ...

class BOBYQAOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    MINIMUM_PROBLEM_DIMENSION: typing.ClassVar[int] = ...
    DEFAULT_INITIAL_RADIUS: typing.ClassVar[float] = ...
    DEFAULT_STOPPING_RADIUS: typing.ClassVar[float] = ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float): ...

class CMAESOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    def __init__(self, int: int, double: float, boolean: bool, int2: int, int3: int, randomGenerator: org.hipparchus.random.RandomGenerator, boolean2: bool, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair]): ...
    def getStatisticsDHistory(self) -> java.util.List[org.hipparchus.linear.RealMatrix]: ...
    def getStatisticsFitnessHistory(self) -> java.util.List[float]: ...
    def getStatisticsMeanHistory(self) -> java.util.List[org.hipparchus.linear.RealMatrix]: ...
    def getStatisticsSigmaHistory(self) -> java.util.List[float]: ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...
    class PopulationSize(org.hipparchus.optim.OptimizationData):
        def __init__(self, int: int): ...
        def getPopulationSize(self) -> int: ...
    class Sigma(org.hipparchus.optim.OptimizationData):
        def __init__(self, doubleArray: typing.List[float]): ...
        def getSigma(self) -> typing.List[float]: ...

class PowellOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair]): ...
    @typing.overload
    def __init__(self, double: float, double2: float, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair]): ...

class SimplexOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair]): ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...

class MultiDirectionalSimplex(AbstractSimplex):
    """
    public class MultiDirectionalSimplex extends :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.AbstractSimplex`
    
        This class implements the multi-directional direct search method.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], double2: float, double3: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]], double2: float, double3: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def iterate(self, multivariateFunction: org.hipparchus.analysis.MultivariateFunction, comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None: ...

class NelderMeadSimplex(AbstractSimplex):
    """
    public class NelderMeadSimplex extends :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.AbstractSimplex`
    
        This class implements the Nelder-Mead simplex algorithm.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]], double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float, double5: float): ...
    def iterate(self, multivariateFunction: org.hipparchus.analysis.MultivariateFunction, comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.scalar.noderiv")``.

    AbstractSimplex: typing.Type[AbstractSimplex]
    BOBYQAOptimizer: typing.Type[BOBYQAOptimizer]
    CMAESOptimizer: typing.Type[CMAESOptimizer]
    MultiDirectionalSimplex: typing.Type[MultiDirectionalSimplex]
    NelderMeadSimplex: typing.Type[NelderMeadSimplex]
    PowellOptimizer: typing.Type[PowellOptimizer]
    SimplexOptimizer: typing.Type[SimplexOptimizer]
