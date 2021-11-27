import java.util
import org.hipparchus.distribution
import org.hipparchus.linear
import org.hipparchus.random
import org.hipparchus.util
import typing



class AbstractMultivariateRealDistribution(org.hipparchus.distribution.MultivariateRealDistribution):
    def getDimension(self) -> int: ...
    def reseedRandomGenerator(self, long: int) -> None: ...
    @typing.overload
    def sample(self) -> typing.List[float]: ...
    @typing.overload
    def sample(self, int: int) -> typing.List[typing.List[float]]: ...

_MixtureMultivariateRealDistribution__T = typing.TypeVar('_MixtureMultivariateRealDistribution__T', bound=org.hipparchus.distribution.MultivariateRealDistribution)  # <T>
class MixtureMultivariateRealDistribution(AbstractMultivariateRealDistribution, typing.Generic[_MixtureMultivariateRealDistribution__T]):
    @typing.overload
    def __init__(self, list: java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, list: java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]): ...
    def density(self, doubleArray: typing.List[float]) -> float: ...
    def getComponents(self) -> java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]: ...
    def reseedRandomGenerator(self, long: int) -> None: ...
    @typing.overload
    def sample(self) -> typing.List[float]: ...
    @typing.overload
    def sample(self, int: int) -> typing.List[typing.List[float]]: ...

class MultivariateNormalDistribution(AbstractMultivariateRealDistribution):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], double3: float): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], double3: float): ...
    def density(self, doubleArray: typing.List[float]) -> float: ...
    def getCovariances(self) -> org.hipparchus.linear.RealMatrix: ...
    def getMeans(self) -> typing.List[float]: ...
    def getSingularMatrixCheckTolerance(self) -> float: ...
    def getStandardDeviations(self) -> typing.List[float]: ...
    @typing.overload
    def sample(self) -> typing.List[float]: ...
    @typing.overload
    def sample(self, int: int) -> typing.List[typing.List[float]]: ...

class MixtureMultivariateNormalDistribution(MixtureMultivariateRealDistribution[MultivariateNormalDistribution]):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[typing.List[typing.List[float]]]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.hipparchus.util.Pair[float, MultivariateNormalDistribution]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, list: java.util.List[org.hipparchus.util.Pair[float, MultivariateNormalDistribution]]): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.distribution.multivariate")``.

    AbstractMultivariateRealDistribution: typing.Type[AbstractMultivariateRealDistribution]
    MixtureMultivariateNormalDistribution: typing.Type[MixtureMultivariateNormalDistribution]
    MixtureMultivariateRealDistribution: typing.Type[MixtureMultivariateRealDistribution]
    MultivariateNormalDistribution: typing.Type[MultivariateNormalDistribution]
