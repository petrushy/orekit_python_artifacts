import java.io
import java.net
import java.util
import jpype.protocol
import org.hipparchus.distribution.continuous
import org.hipparchus.distribution.multivariate
import org.hipparchus.random
import org.hipparchus.stat.descriptive
import typing



class EmpiricalDistribution(org.hipparchus.distribution.continuous.AbstractRealDistribution):
    DEFAULT_BIN_COUNT: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    def cumulativeProbability(self, double: float) -> float: ...
    def density(self, double: float) -> float: ...
    def getBinCount(self) -> int: ...
    def getBinStats(self) -> java.util.List[org.hipparchus.stat.descriptive.StreamingStatistics]: ...
    def getGeneratorUpperBounds(self) -> typing.List[float]: ...
    def getNextValue(self) -> float: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getSampleStats(self) -> org.hipparchus.stat.descriptive.StatisticalSummary: ...
    def getSupportLowerBound(self) -> float: ...
    def getSupportUpperBound(self) -> float: ...
    def getUpperBounds(self) -> typing.List[float]: ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isLoaded(self) -> bool: ...
    def isSupportConnected(self) -> bool: ...
    @typing.overload
    def load(self, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def load(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    @typing.overload
    def load(self, uRL: java.net.URL) -> None: ...
    def reSeed(self, long: int) -> None: ...
    def reseedRandomGenerator(self, long: int) -> None: ...

class MultivariateNormalMixtureExpectationMaximization:
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @staticmethod
    def estimate(doubleArray: typing.List[typing.List[float]], int: int) -> org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution: ...
    @typing.overload
    def fit(self, mixtureMultivariateNormalDistribution: org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution) -> None: ...
    @typing.overload
    def fit(self, mixtureMultivariateNormalDistribution: org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution, int: int, double: float) -> None: ...
    def getFittedModel(self) -> org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution: ...
    def getLogLikelihood(self) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.fitting")``.

    EmpiricalDistribution: typing.Type[EmpiricalDistribution]
    MultivariateNormalMixtureExpectationMaximization: typing.Type[MultivariateNormalMixtureExpectationMaximization]
