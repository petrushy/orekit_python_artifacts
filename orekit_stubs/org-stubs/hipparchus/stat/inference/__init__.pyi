import java.lang
import java.util
import org.hipparchus.distribution
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.inference.class-use
import org.hipparchus.stat.ranking
import typing



class AlternativeHypothesis(java.lang.Enum['AlternativeHypothesis']):
    TWO_SIDED: typing.ClassVar['AlternativeHypothesis'] = ...
    GREATER_THAN: typing.ClassVar['AlternativeHypothesis'] = ...
    LESS_THAN: typing.ClassVar['AlternativeHypothesis'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AlternativeHypothesis': ...
    @staticmethod
    def values() -> typing.List['AlternativeHypothesis']: ...

class BinomialTest:
    def __init__(self): ...
    @typing.overload
    def binomialTest(self, int: int, int2: int, double: float, alternativeHypothesis: AlternativeHypothesis, double2: float) -> bool: ...
    @typing.overload
    def binomialTest(self, int: int, int2: int, double: float, alternativeHypothesis: AlternativeHypothesis) -> float: ...

class ChiSquareTest:
    def __init__(self): ...
    @typing.overload
    def chiSquare(self, doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @typing.overload
    def chiSquare(self, longArray: typing.List[typing.List[int]]) -> float: ...
    def chiSquareDataSetsComparison(self, longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...
    @typing.overload
    def chiSquareTest(self, doubleArray: typing.List[float], longArray: typing.List[int], double2: float) -> bool: ...
    @typing.overload
    def chiSquareTest(self, longArray: typing.List[typing.List[int]], double: float) -> bool: ...
    @typing.overload
    def chiSquareTest(self, doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @typing.overload
    def chiSquareTest(self, longArray: typing.List[typing.List[int]]) -> float: ...
    @typing.overload
    def chiSquareTestDataSetsComparison(self, longArray: typing.List[int], longArray2: typing.List[int], double: float) -> bool: ...
    @typing.overload
    def chiSquareTestDataSetsComparison(self, longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...

class GTest:
    def __init__(self): ...
    def g(self, doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    def gDataSetsComparison(self, longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...
    @typing.overload
    def gTest(self, doubleArray: typing.List[float], longArray: typing.List[int], double2: float) -> bool: ...
    @typing.overload
    def gTest(self, doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @typing.overload
    def gTestDataSetsComparison(self, longArray: typing.List[int], longArray2: typing.List[int], double: float) -> bool: ...
    @typing.overload
    def gTestDataSetsComparison(self, longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...
    def gTestIntrinsic(self, doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    def rootLogLikelihoodRatio(self, long: int, long2: int, long3: int, long4: int) -> float: ...

class InferenceTestUtils:
    @staticmethod
    def approximateP(double: float, int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquare(doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquare(longArray: typing.List[typing.List[int]]) -> float: ...
    @staticmethod
    def chiSquareDataSetsComparison(longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(doubleArray: typing.List[float], longArray: typing.List[int], double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(longArray: typing.List[typing.List[int]], double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(longArray: typing.List[typing.List[int]]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTestDataSetsComparison(longArray: typing.List[int], longArray2: typing.List[int], double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTestDataSetsComparison(longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...
    @staticmethod
    def exactP(double: float, int: int, int2: int, boolean: bool) -> float: ...
    @staticmethod
    def g(doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @staticmethod
    def gDataSetsComparison(longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...
    @typing.overload
    @staticmethod
    def gTest(doubleArray: typing.List[float], longArray: typing.List[int], double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def gTest(doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @typing.overload
    @staticmethod
    def gTestDataSetsComparison(longArray: typing.List[int], longArray2: typing.List[int], double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def gTestDataSetsComparison(longArray: typing.List[int], longArray2: typing.List[int]) -> float: ...
    @staticmethod
    def gTestIntrinsic(doubleArray: typing.List[float], longArray: typing.List[int]) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticT(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticT(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticTTest(doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def homoscedasticTTest(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticTTest(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovStatistic(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovStatistic(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float], double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float], boolean: bool) -> float: ...
    @staticmethod
    def oneWayAnovaFValue(collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]]]) -> float: ...
    @staticmethod
    def oneWayAnovaPValue(collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]]]) -> float: ...
    @staticmethod
    def oneWayAnovaTest(collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]]], double: float) -> bool: ...
    @staticmethod
    def pairedT(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def pairedTTest(doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def pairedTTest(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @staticmethod
    def rootLogLikelihoodRatio(long: int, long2: int, long3: int, long4: int) -> float: ...
    @typing.overload
    @staticmethod
    def t(double: float, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def t(double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def t(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def t(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, doubleArray: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary, double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...

class KolmogorovSmirnovTest:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int): ...
    def approximateP(self, double: float, int: int, int2: int) -> float: ...
    @typing.overload
    def bootstrap(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int) -> float: ...
    @typing.overload
    def bootstrap(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, boolean: bool) -> float: ...
    @typing.overload
    def cdf(self, double: float, int: int) -> float: ...
    @typing.overload
    def cdf(self, double: float, int: int, boolean: bool) -> float: ...
    def cdfExact(self, double: float, int: int) -> float: ...
    def exactP(self, double: float, int: int, int2: int, boolean: bool) -> float: ...
    @typing.overload
    def kolmogorovSmirnovStatistic(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovStatistic(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float], double2: float) -> bool: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float], boolean: bool) -> float: ...
    def ksSum(self, double: float, double2: float, int: int) -> float: ...
    def pelzGood(self, double: float, int: int) -> float: ...

class MannWhitneyUTest:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy, tiesStrategy: org.hipparchus.stat.ranking.TiesStrategy): ...
    def mannWhitneyU(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def mannWhitneyUTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def mannWhitneyUTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> float: ...

class OneWayAnova:
    def __init__(self): ...
    def anovaFValue(self, collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]]]) -> float: ...
    @typing.overload
    def anovaPValue(self, collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]]]) -> float: ...
    @typing.overload
    def anovaPValue(self, collection: typing.Union[java.util.Collection[org.hipparchus.stat.descriptive.StreamingStatistics], typing.Sequence[org.hipparchus.stat.descriptive.StreamingStatistics]], boolean: bool) -> float: ...
    def anovaTest(self, collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]]], double: float) -> bool: ...

class TTest:
    def __init__(self): ...
    @typing.overload
    def homoscedasticT(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def homoscedasticT(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def homoscedasticTTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    def homoscedasticTTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def homoscedasticTTest(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    def pairedT(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def pairedTTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    def pairedTTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def t(self, double: float, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def t(self, double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def t(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def t(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def tTest(self, double: float, doubleArray: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    def tTest(self, double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, double2: float) -> bool: ...
    @typing.overload
    def tTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> bool: ...
    @typing.overload
    def tTest(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary, double: float) -> bool: ...
    @typing.overload
    def tTest(self, double: float, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def tTest(self, double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def tTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def tTest(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...

class WilcoxonSignedRankTest:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy, tiesStrategy: org.hipparchus.stat.ranking.TiesStrategy): ...
    def wilcoxonSignedRank(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    def wilcoxonSignedRankTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.inference")``.

    AlternativeHypothesis: typing.Type[AlternativeHypothesis]
    BinomialTest: typing.Type[BinomialTest]
    ChiSquareTest: typing.Type[ChiSquareTest]
    GTest: typing.Type[GTest]
    InferenceTestUtils: typing.Type[InferenceTestUtils]
    KolmogorovSmirnovTest: typing.Type[KolmogorovSmirnovTest]
    MannWhitneyUTest: typing.Type[MannWhitneyUTest]
    OneWayAnova: typing.Type[OneWayAnova]
    TTest: typing.Type[TTest]
    WilcoxonSignedRankTest: typing.Type[WilcoxonSignedRankTest]
    class-use: org.hipparchus.stat.inference.class-use.__module_protocol__
