import java.io
import java.util
import org.hipparchus.distribution
import org.hipparchus.distribution.discrete.class-use
import org.hipparchus.util
import typing



class AbstractIntegerDistribution(org.hipparchus.distribution.IntegerDistribution, java.io.Serializable):
    def __init__(self): ...
    def inverseCumulativeProbability(self, double: float) -> int: ...
    def logProbability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...

class BinomialDistribution(AbstractIntegerDistribution):
    def __init__(self, int: int, double: float): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getNumberOfTrials(self) -> int: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getProbabilityOfSuccess(self) -> float: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def isSupportConnected(self) -> bool: ...
    def logProbability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...

class EnumeratedIntegerDistribution(AbstractIntegerDistribution):
    @typing.overload
    def __init__(self, intArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, intArray: typing.List[int], doubleArray: typing.List[float]): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getPmf(self) -> java.util.List[org.hipparchus.util.Pair[int, float]]: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def isSupportConnected(self) -> bool: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...

class GeometricDistribution(AbstractIntegerDistribution):
    def __init__(self, double: float): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getProbabilityOfSuccess(self) -> float: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def inverseCumulativeProbability(self, double: float) -> int: ...
    def isSupportConnected(self) -> bool: ...
    def logProbability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...

class HypergeometricDistribution(AbstractIntegerDistribution):
    def __init__(self, int: int, int2: int, int3: int): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getNumberOfSuccesses(self) -> int: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getPopulationSize(self) -> int: ...
    def getSampleSize(self) -> int: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def isSupportConnected(self) -> bool: ...
    def logProbability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...
    def upperCumulativeProbability(self, int: int) -> float: ...

class PascalDistribution(AbstractIntegerDistribution):
    def __init__(self, int: int, double: float): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getNumberOfSuccesses(self) -> int: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getProbabilityOfSuccess(self) -> float: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def isSupportConnected(self) -> bool: ...
    def logProbability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...

class PoissonDistribution(AbstractIntegerDistribution):
    DEFAULT_MAX_ITERATIONS: typing.ClassVar[int] = ...
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getMean(self) -> float: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def isSupportConnected(self) -> bool: ...
    def logProbability(self, int: int) -> float: ...
    def normalApproximateProbability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...

class UniformIntegerDistribution(AbstractIntegerDistribution):
    def __init__(self, int: int, int2: int): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def isSupportConnected(self) -> bool: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...

class ZipfDistribution(AbstractIntegerDistribution):
    def __init__(self, int: int, double: float): ...
    def cumulativeProbability(self, int: int) -> float: ...
    def getExponent(self) -> float: ...
    def getNumberOfElements(self) -> int: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getSupportLowerBound(self) -> int: ...
    def getSupportUpperBound(self) -> int: ...
    def isSupportConnected(self) -> bool: ...
    def logProbability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.distribution.discrete")``.

    AbstractIntegerDistribution: typing.Type[AbstractIntegerDistribution]
    BinomialDistribution: typing.Type[BinomialDistribution]
    EnumeratedIntegerDistribution: typing.Type[EnumeratedIntegerDistribution]
    GeometricDistribution: typing.Type[GeometricDistribution]
    HypergeometricDistribution: typing.Type[HypergeometricDistribution]
    PascalDistribution: typing.Type[PascalDistribution]
    PoissonDistribution: typing.Type[PoissonDistribution]
    UniformIntegerDistribution: typing.Type[UniformIntegerDistribution]
    ZipfDistribution: typing.Type[ZipfDistribution]
    class-use: org.hipparchus.distribution.discrete.class-use.__module_protocol__
