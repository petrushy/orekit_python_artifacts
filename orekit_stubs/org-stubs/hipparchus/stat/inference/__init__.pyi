
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org.hipparchus.distribution
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.ranking
import typing



class AlternativeHypothesis(java.lang.Enum['AlternativeHypothesis']):
    """
    public enumAlternativeHypothesis extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.stat.inference.AlternativeHypothesis`>
    
        Represents an alternative hypothesis for a hypothesis test.
    """
    TWO_SIDED: typing.ClassVar['AlternativeHypothesis'] = ...
    GREATER_THAN: typing.ClassVar['AlternativeHypothesis'] = ...
    LESS_THAN: typing.ClassVar['AlternativeHypothesis'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AlternativeHypothesis':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AlternativeHypothesis']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class BinomialTest:
    """
    public classBinomialTest extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Implements binomial test statistics.
    
        Exact test for the statistical significance of deviations from a theoretically expected distribution of observations
        into two categories.
    
        Also see:
    
              - `Binomial test (Wikipedia) <http://en.wikipedia.org/wiki/Binomial_test>`
    """
    def __init__(self): ...
    @typing.overload
    def binomialTest(self, int: int, int2: int, double: float, alternativeHypothesis: AlternativeHypothesis, double2: float) -> bool:
        """
            Returns whether the null hypothesis can be rejected with the given confidence level.
        
            **Preconditions**:
        
              - Number of trials must be ≥ 0.
              - Number of successes must be ≥ 0.
              - Number of successes must be ≤ number of trials.
              - Probability must be ≥ 0 and ≤ 1.
        
        
            Parameters:
                numberOfTrials (int): number of trials performed
                numberOfSuccesses (int): number of successes observed
                probability (double): assumed probability of a single trial under the null hypothesis
                alternativeHypothesis (:class:`~org.hipparchus.stat.inference.AlternativeHypothesis`): type of hypothesis being evaluated (one- or two-sided)
                alpha (double): significance level of the test
        
            Returns:
                true if the null hypothesis can be rejected with confidence :code:`1 - alpha`
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`numberOfTrials` or :code:`numberOfSuccesses` is negative
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`probability` is not between 0 and 1
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`numberOfTrials` < :code:`numberOfSuccesses` or if :code:`alternateHypothesis` is null.
        
            Also see:
        
                  - :class:`~org.hipparchus.stat.inference.AlternativeHypothesis`
        
        
        """
        ...
    @typing.overload
    def binomialTest(self, int: int, int2: int, double: float, alternativeHypothesis: AlternativeHypothesis) -> float:
        """
            Returns the *observed significance level*, or `p-value <http://www.cas.lancs.ac.uk/glossary_v1.1/hyptest.html#pvalue>`,
            associated with a ` Binomial test <http://en.wikipedia.org/wiki/Binomial_test>`.
        
            The number returned is the smallest significance level at which one can reject the null hypothesis. The form of the
            hypothesis depends on :code:`alternativeHypothesis`.
        
            The p-Value represents the likelihood of getting a result at least as extreme as the sample, given the provided
            :code:`probability` of success on a single trial. For single-sided tests, this value can be directly derived from the
            Binomial distribution. For the two-sided test, the implementation works as follows: we start by looking at the most
            extreme cases (0 success and n success where n is the number of trials from the sample) and determine their likelihood.
            The lower value is added to the p-Value (if both values are equal, both are added). Then we continue with the next
            extreme value, until we added the value for the actual observed sample.
        
            * **Preconditions**:
        
              - Number of trials must be ≥ 0.
              - Number of successes must be ≥ 0.
              - Number of successes must be ≤ number of trials.
              - Probability must be ≥ 0 and ≤ 1.
        
        
            Parameters:
                numberOfTrials (int): number of trials performed
                numberOfSuccesses (int): number of successes observed
                probability (double): assumed probability of a single trial under the null hypothesis
                alternativeHypothesis (:class:`~org.hipparchus.stat.inference.AlternativeHypothesis`): type of hypothesis being evaluated (one- or two-sided)
        
            Returns:
                p-value
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`numberOfTrials` or :code:`numberOfSuccesses` is negative
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`probability` is not between 0 and 1
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`numberOfTrials` < :code:`numberOfSuccesses` or if :code:`alternateHypothesis` is null.
        
            Also see:
        
                  - :class:`~org.hipparchus.stat.inference.AlternativeHypothesis`
        
        
        
        """
        ...

class ChiSquareTest:
    """
    public classChiSquareTest extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Implements Chi-Square test statistics.
    
        This implementation handles both known and unknown distributions.
    
        Two samples tests can be used when the distribution is unknown *a priori* but provided by one sample, or when the
        hypothesis under test is that the two samples come from the same underlying distribution.
    """
    def __init__(self): ...
    @typing.overload
    def chiSquare(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def chiSquare(self, longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    def chiSquareDataSetsComparison(self, longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def chiSquareTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray], double2: float) -> bool: ...
    @typing.overload
    def chiSquareTest(self, longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    def chiSquareTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def chiSquareTest(self, longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    @typing.overload
    def chiSquareTestDataSetsComparison(self, longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    def chiSquareTestDataSetsComparison(self, longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...

class GTest:
    """
    public classGTest extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Implements `G Test <http://en.wikipedia.org/wiki/G-test>` statistics.
    
        This is known in statistical genetics as the McDonald-Kreitman test. The implementation handles both known and unknown
        distributions.
    
        Two samples tests can be used when the distribution is unknown *a priori* but provided by one sample, or when the
        hypothesis under test is that the two samples come from the same underlying distribution.
    """
    def __init__(self): ...
    def g(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    def gDataSetsComparison(self, longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def gTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray], double2: float) -> bool: ...
    @typing.overload
    def gTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def gTestDataSetsComparison(self, longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    def gTestDataSetsComparison(self, longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    def gTestIntrinsic(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    def rootLogLikelihoodRatio(self, long: int, long2: int, long3: int, long4: int) -> float:
        """
            Calculates the root log-likelihood ratio for 2 state Datasets. See
            :meth:`~org.hipparchus.stat.inference.GTest.gDataSetsComparison`.
        
            Given two events A and B, let k11 be the number of times both events occur, k12 the incidence of B without A, k21 the
            count of A without B, and k22 the number of times neither A nor B occurs. What is returned by this method is
        
            :code:`(sgn) sqrt(gValueDataSetsComparison({k11, k12}, {k21, k22})`
        
            where :code:`sgn` is -1 if :code:`k11 / (k11 + k12) < k21 / (k21 + k22))`;
        
        
            1 otherwise.
        
            Signed root LLR has two advantages over the basic LLR: a) it is positive where k11 is bigger than expected, negative
            where it is lower b) if there is no difference it is asymptotically normally distributed. This allows one to talk about
            "number of standard deviations" which is a more common frame of reference than the chi^2 distribution.
        
            Parameters:
                k11 (long): number of times the two events occurred together (AB)
                k12 (long): number of times the second event occurred WITHOUT the first event (notA,B)
                k21 (long): number of times the first event occurred WITHOUT the second event (A, notB)
                k22 (long): number of times something else occurred (i.e. was neither of these events (notA, notB)
        
            Returns:
                root log-likelihood ratio
        
        
        """
        ...

class InferenceTestUtils:
    """
    public classInferenceTestUtils extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        A collection of static methods to create inference test instances or to perform inference tests.
    """
    @staticmethod
    def approximateP(double: float, int: int, int2: int) -> float:
        """
            Uses the Kolmogorov-Smirnov distribution to approximate \(P(D_{n,m} > d)\) where \(D_{n,m}\) is the 2-sample
            Kolmogorov-Smirnov statistic. See
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovStatistic` for the definition of
            \(D_{n,m}\).
        
            Specifically, what is returned is \(1 - k(d \sqrt{mn / (m + n)})\) where \(k(t) = 1 + 2 \sum_{i=1}^\infty (-1)^i e^{-2
            i^2 t^2}\). See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.ksSum` for details on how convergence of the
            sum is determined. This implementation passes :code:`ksSum`
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.KS_SUM_CAUCHY_CRITERION` as :code:`tolerance` and
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.MAXIMUM_PARTIAL_SUM_COUNT` as :code:`maxIterations`.
        
            Parameters:
                d (double): D-statistic value
                n (int): first sample size
                m (int): second sample size
        
            Returns:
                approximate probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than :code:`d`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def chiSquare(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquare(longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    @staticmethod
    def chiSquareDataSetsComparison(longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray], double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTestDataSetsComparison(longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTestDataSetsComparison(longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @staticmethod
    def exactP(double: float, int: int, int2: int, boolean: bool) -> float:
        """
            Computes \(P(D_{n,m} > d)\) if :code:`strict` is :code:`true`; otherwise \(P(D_{n,m} \ge d)\), where \(D_{n,m}\) is the
            2-sample Kolmogorov-Smirnov statistic. See
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovStatistic` for the definition of
            \(D_{n,m}\).
        
            The returned probability is exact, implemented by unwinding the recursive function definitions presented in [4] from the
            class javadoc.
        
            Parameters:
                d (double): D-statistic value
                m (int): second sample size
                n (int): first sample size
                strict (boolean): whether or not the probability to compute is expressed as a strict inequality
        
            Returns:
                probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than (resp. greater than or
                equal to) :code:`d`
        
        
        """
        ...
    @staticmethod
    def g(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @staticmethod
    def gDataSetsComparison(longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def gTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray], double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def gTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def gTestDataSetsComparison(longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def gTestDataSetsComparison(longArray: typing.Union[typing.List[int], jpype.JArray], longArray2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @staticmethod
    def gTestIntrinsic(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticT(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticT(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticTTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def homoscedasticTTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticTTest(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovStatistic(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovStatistic(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def kolmogorovSmirnovTest(realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...
    @staticmethod
    def oneWayAnovaFValue(collection: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float: ...
    @staticmethod
    def oneWayAnovaPValue(collection: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float: ...
    @staticmethod
    def oneWayAnovaTest(collection: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]], double: float) -> bool: ...
    @staticmethod
    def pairedT(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def pairedTTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def pairedTTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @staticmethod
    def rootLogLikelihoodRatio(long: int, long2: int, long3: int, long4: int) -> float: ...
    @typing.overload
    @staticmethod
    def t(double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def t(double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def t(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def t(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary, double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def tTest(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...

class KolmogorovSmirnovTest:
    """
    public classKolmogorovSmirnovTest extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Implementation of the ` Kolmogorov-Smirnov (K-S) test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` for
        equality of continuous distributions.
    
        The K-S test uses a statistic based on the maximum deviation of the empirical distribution of sample data points from
        the distribution expected under the null hypothesis. For one-sample tests evaluating the null hypothesis that a set of
        sample data points follow a given distribution, the test statistic is \(D_n=\sup_x |F_n(x)-F(x)|\), where \(F\) is the
        expected distribution and \(F_n\) is the empirical distribution of the \(n\) sample data points. The distribution of
        \(D_n\) is estimated using a method based on [1] with certain quick decisions for extreme values given in [2].
    
        Two-sample tests are also supported, evaluating the null hypothesis that the two samples :code:`x` and :code:`y` come
        from the same underlying distribution. In this case, the test statistic is \(D_{n,m}=\sup_t | F_n(t)-F_m(t)|\) where
        \(n\) is the length of :code:`x`, \(m\) is the length of :code:`y`, \(F_n\) is the empirical distribution that puts mass
        \(1/n\) at each of the values in :code:`x` and \(F_m\) is the empirical distribution of the :code:`y` values. The
        default 2-sample test method, :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovTest` works
        as follows:
    
          - For small samples (where the product of the sample sizes is less than
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT`), the method presented in [4] is used
            to compute the exact p-value for the 2-sample test.
          - When the product of the sample sizes exceeds
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT`, the asymptotic distribution of
            \(D_{n,m}\) is used. See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.approximateP` for details on the
            approximation.
    
    
        If the product of the sample sizes is less than
        :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT` and the sample data contains ties,
        random jitter is added to the sample data to break ties before applying the algorithm above. Alternatively, the
        :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.bootstrap` method, modeled after `ks.boot
        <http://sekhon.berkeley.edu/matching/ks.boot.html>` in the R Matching package [3], can be used if ties are known to be
        present in the data.
    
        In the two-sample case, \(D_{n,m}\) has a discrete distribution. This makes the p-value associated with the null
        hypothesis \(H_0 : D_{n,m} \ge d \) differ from \(H_0 : D_{n,m} > d \) by the mass of the observed value \(d\). To
        distinguish these, the two-sample tests use a boolean :code:`strict` parameter. This parameter is ignored for large
        samples.
    
        The methods used by the 2-sample default implementation are also exposed directly:
    
          - :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.exactP` computes exact 2-sample p-values
          - :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.approximateP` uses the asymptotic distribution The
            :code:`boolean` arguments in the first two methods allow the probability used to estimate the p-value to be expressed
            using strict or non-strict inequality. See
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovTest`.
    
    
        References:
    
          - [1] ` Evaluating Kolmogorov's Distribution <http://www.jstatsoft.org/v08/i18/>` by George Marsaglia, Wai Wan Tsang, and
            Jingbo Wang
          - [2] ` Computing the Two-Sided Kolmogorov-Smirnov Distribution <http://www.jstatsoft.org/v39/i11/>` by Richard Simard and
            Pierre L'Ecuyer
          - [3] Jasjeet S. Sekhon. 2011. ` Multivariate and Propensity Score Matching Software with Automated Balance Optimization:
            The Matching package for R <http://www.jstatsoft.org/article/view/v042i07>` Journal of Statistical Software, 42(7):
            1-52.
          - [4] Kim, P. J. and Jennrich, R. I. (1970). Tables of the Exact Sampling Distribution of the Two-Sample
            Kolmogorov-Smirnov Criterion D_mn ,m≦n in Selected Tables in Mathematical Statistics, Vol. 1, H. L. Harter and D. B.
            Owen, editors.
    
    
        Note that [1] contains an error in computing h, refer to
        :class:`~org.hipparchus.stat.inference.https:.issues.apache.org.jira.browse.MATH` for details.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int): ...
    def approximateP(self, double: float, int: int, int2: int) -> float:
        """
            Uses the Kolmogorov-Smirnov distribution to approximate \(P(D_{n,m} > d)\) where \(D_{n,m}\) is the 2-sample
            Kolmogorov-Smirnov statistic. See
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovStatistic` for the definition of
            \(D_{n,m}\).
        
            Specifically, what is returned is \(1 - k(d \sqrt{mn / (m + n)})\) where \(k(t) = 1 + 2 \sum_{i=1}^\infty (-1)^i e^{-2
            i^2 t^2}\). See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.ksSum` for details on how convergence of the
            sum is determined. This implementation passes :code:`ksSum`
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.KS_SUM_CAUCHY_CRITERION` as :code:`tolerance` and
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.MAXIMUM_PARTIAL_SUM_COUNT` as :code:`maxIterations`.
        
            Parameters:
                d (double): D-statistic value
                n (int): first sample size
                m (int): second sample size
        
            Returns:
                approximate probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than :code:`d`
        
        
        """
        ...
    @typing.overload
    def bootstrap(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], int: int) -> float:
        """
            Estimates the *p-value* of a two-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`x` and :code:`y` are
            samples drawn from the same probability distribution. This method estimates the p-value by repeatedly sampling sets of
            size :code:`x.length` and :code:`y.length` from the empirical distribution of the combined sample. When :code:`strict`
            is true, this is equivalent to the algorithm implemented in the R function :code:`ks.boot`, described in
        
            .. code-block: java
            
             Jasjeet S. Sekhon. 2011. 'Multivariate and Propensity Score Matching
             Software with Automated Balance Optimization: The Matching package for R.'
             Journal of Statistical Software, 42(7): 1-52.
             
        
            Parameters:
                x (double[]): first sample
                y (double[]): second sample
                iterations (int): number of bootstrap resampling iterations
                strict (boolean): whether or not the null hypothesis is expressed as a strict inequality
        
            Returns:
                estimated p-value
        
            Computes :code:`bootstrap(x, y, iterations, true)`. This is equivalent to ks.boot(x,y, nboots=iterations) using the R
            Matching package function. See #bootstrap(double[], double[], int, boolean).
        
            Parameters:
                x (double[]): first sample
                y (double[]): second sample
                iterations (int): number of bootstrap resampling iterations
        
            Returns:
                estimated p-value
        
        
        """
        ...
    @typing.overload
    def bootstrap(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], int: int, boolean: bool) -> float: ...
    @typing.overload
    def cdf(self, double: float, int: int) -> float: ...
    @typing.overload
    def cdf(self, double: float, int: int, boolean: bool) -> float: ...
    def cdfExact(self, double: float, int: int) -> float: ...
    def exactP(self, double: float, int: int, int2: int, boolean: bool) -> float:
        """
            Computes \(P(D_{n,m} > d)\) if :code:`strict` is :code:`true`; otherwise \(P(D_{n,m} \ge d)\), where \(D_{n,m}\) is the
            2-sample Kolmogorov-Smirnov statistic. See
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovStatistic` for the definition of
            \(D_{n,m}\).
        
            The returned probability is exact, implemented by unwinding the recursive function definitions presented in [4] from the
            class javadoc.
        
            Parameters:
                d (double): D-statistic value
                n (int): first sample size
                m (int): second sample size
                strict (boolean): whether or not the probability to compute is expressed as a strict inequality
        
            Returns:
                probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than (resp. greater than or
                equal to) :code:`d`
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovStatistic(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Computes the one-sample Kolmogorov-Smirnov test statistic, \(D_n=\sup_x |F_n(x)-F(x)|\) where \(F\) is the distribution
            (cdf) function associated with :code:`distribution`, \(n\) is the length of :code:`data` and \(F_n\) is the empirical
            distribution that puts mass \(1/n\) at each of the values in :code:`data`.
        
            Parameters:
                distribution (:class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`): reference distribution
                data (double[]): sample being evaluated
        
            Returns:
                Kolmogorov-Smirnov statistic \(D_n\)
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` does not have length at least 2
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` is null
        
            Computes the two-sample Kolmogorov-Smirnov test statistic, \(D_{n,m}=\sup_x |F_n(x)-F_m(x)|\) where \(n\) is the length
            of :code:`x`, \(m\) is the length of :code:`y`, \(F_n\) is the empirical distribution that puts mass \(1/n\) at each of
            the values in :code:`x` and \(F_m\) is the empirical distribution of the :code:`y` values.
        
            Parameters:
                x (double[]): first sample
                y (double[]): second sample
        
            Returns:
                test statistic \(D_{n,m}\) used to evaluate the null hypothesis that :code:`x` and :code:`y` represent samples from the
                same underlying distribution
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if either :code:`x` or :code:`y` does not have length at least 2
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if either :code:`x` or :code:`y` is null
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovStatistic(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> bool:
        """
            Computes the *p-value*, or *observed significance level*, of a one-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`data` conforms to
            :code:`distribution`. If :code:`exact` is true, the distribution used to compute the p-value is computed using extended
            precision. See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.cdfExact`.
        
            Parameters:
                distribution (:class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`): reference distribution
                data (double[]): sample being being evaluated
                exact (boolean): whether or not to force exact computation of the p-value
        
            Returns:
                the p-value associated with the null hypothesis that :code:`data` is a sample from :code:`distribution`
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` does not have length at least 2
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` is null
        
            Computes the *p-value*, or *observed significance level*, of a two-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`x` and :code:`y` are
            samples drawn from the same probability distribution. Specifically, what is returned is an estimate of the probability
            that the :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovStatistic` associated with a
            randomly selected partition of the combined sample into subsamples of sizes :code:`x.length` and :code:`y.length` will
            strictly exceed (if :code:`strict` is :code:`true`) or be at least as large as :code:`strict = false`) as
            :code:`kolmogorovSmirnovStatistic(x, y)`.
        
              - For small samples (where the product of the sample sizes is less than
                :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT`), the exact p-value is computed using
                the method presented in [4], implemented in :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.exactP`.
              - When the product of the sample sizes exceeds
                :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT`, the asymptotic distribution of
                \(D_{n,m}\) is used. See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.approximateP` for details on the
                approximation.
        
        
            If :code:`x.length * y.length` < :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT` and
            the combined set of values in :code:`x` and :code:`y` contains ties, random jitter is added to :code:`x` and :code:`y`
            to break ties before computing \(D_{n,m}\) and the p-value. The jitter is uniformly distributed on (-minDelta / 2,
            minDelta / 2) where minDelta is the smallest pairwise difference between values in the combined sample.
        
            If ties are known to be present in the data, :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.bootstrap` may
            be used as an alternative method for estimating the p-value.
        
            Parameters:
                x (double[]): first sample dataset
                y (double[]): second sample dataset
                strict (boolean): whether or not the probability to compute is expressed as a strict inequality (ignored for large samples)
        
            Returns:
                p-value associated with the null hypothesis that :code:`x` and :code:`y` represent samples from the same distribution
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if either :code:`x` or :code:`y` does not have length at least 2
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if either :code:`x` or :code:`y` is null
        
            Also see:
        
                  - :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.bootstrap`
        
        
            Performs a ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null
            hypothesis that :code:`data` conforms to :code:`distribution`.
        
            Parameters:
                distribution (:class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`): reference distribution
                data (double[]): sample being being evaluated
                alpha (double): significance level of the test
        
            Returns:
                true iff the null hypothesis that :code:`data` is a sample from :code:`distribution` can be rejected with confidence 1 -
                :code:`alpha`
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` does not have length at least 2
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` is null
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Computes the *p-value*, or *observed significance level*, of a two-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`x` and :code:`y` are
            samples drawn from the same probability distribution. Assumes the strict form of the inequality used to compute the
            p-value. See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.kolmogorovSmirnovTest`.
        
            Parameters:
                x (double[]): first sample dataset
                y (double[]): second sample dataset
        
            Returns:
                p-value associated with the null hypothesis that :code:`x` and :code:`y` represent samples from the same distribution
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if either :code:`x` or :code:`y` does not have length at least 2
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if either :code:`x` or :code:`y` is null
        
            Computes the *p-value*, or *observed significance level*, of a one-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`data` conforms to
            :code:`distribution`.
        
            Parameters:
                distribution (:class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`): reference distribution
                data (double[]): sample being being evaluated
        
            Returns:
                the p-value associated with the null hypothesis that :code:`data` is a sample from :code:`distribution`
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` does not have length at least 2
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if :code:`data` is null
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...
    def ksSum(self, double: float, double2: float, int: int) -> float:
        """
            Computes \( 1 + 2 \sum_{i=1}^\infty (-1)^i e^{-2 i^2 t^2} \) stopping when successive partial sums are within
            :code:`tolerance` of one another, or when :code:`maxIterations` partial sums have been computed. If the sum does not
            converge before :code:`maxIterations` iterations a
            :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus` is thrown.
        
            Parameters:
                t (double): argument
                tolerance (double): Cauchy criterion for partial sums
                maxIterations (int): maximum number of partial sums to compute
        
            Returns:
                Kolmogorov sum evaluated at t
        
            Raises:
                :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus`: if the series does not converge
        
        
        """
        ...
    def pelzGood(self, double: float, int: int) -> float:
        """
            Computes the Pelz-Good approximation for \(P(D_n < d)\) as described in [2] in the class javadoc.
        
            Parameters:
                d (double): value of d-statistic (x in [2])
                n (int): sample size
        
            Returns:
                \(P(D_n < d)\)
        
        
        """
        ...

class MannWhitneyUTest:
    """
    public classMannWhitneyUTest extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        An implementation of the Mann-Whitney U test.
    
        The definitions and computing formulas used in this implementation follow those in the article, ` Mann-Whitney U Test
        <http://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U>`
    
        In general, results correspond to (and have been tested against) the R wilcox.test function, with :code:`exact` meaning
        the same thing in both APIs and :code:`CORRECT` uniformly true in this implementation. For example, wilcox.test(x, y,
        alternative = "two.sided", mu = 0, paired = FALSE, exact = FALSE correct = TRUE) will return the same p-value as
        mannWhitneyUTest(x, y, false). The minimum of the W value returned by R for wilcox.test(x, y...) and wilcox.test(y,
        x...) should equal mannWhitneyU(x, y...).
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy, tiesStrategy: org.hipparchus.stat.ranking.TiesStrategy): ...
    def mannWhitneyU(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def mannWhitneyUTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def mannWhitneyUTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...

class OneWayAnova:
    """
    public classOneWayAnova extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Implements one-way ANOVA (analysis of variance) statistics.
    
        Tests for differences between two or more categories of univariate data (for example, the body mass index of
        accountants, lawyers, doctors and computer programmers). When two categories are given, this is equivalent to the
        :class:`~org.hipparchus.stat.inference.TTest`.
    
        Uses the :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus` to estimate exact p-values.
    
        This implementation is based on a description at `One way Anova (dead link)
        <http://faculty.vassar.edu/lowry/ch13pt1.html>`
    
        .. code-block: java
        
         Abbreviations: bg = between groups,
                        wg = within groups,
                        ss = sum squared deviations
    """
    def __init__(self): ...
    def anovaFValue(self, collection: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float: ...
    @typing.overload
    def anovaPValue(self, collection: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float: ...
    @typing.overload
    def anovaPValue(self, collection: typing.Union[java.util.Collection[org.hipparchus.stat.descriptive.StreamingStatistics], typing.Sequence[org.hipparchus.stat.descriptive.StreamingStatistics], typing.Set[org.hipparchus.stat.descriptive.StreamingStatistics]], boolean: bool) -> float: ...
    def anovaTest(self, collection: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]], double: float) -> bool: ...

class TTest:
    """
    public classTTest extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        An implementation for Student's t-tests.
    
        Tests can be:
    
          - One-sample or two-sample
          - One-sided or two-sided
          - Paired or unpaired (for two-sample tests)
          - Homoscedastic (equal variance assumption) or heteroscedastic (for two sample tests)
          - Fixed significance level (boolean-valued) or returning p-values.
    
    
        Test statistics are available for all tests. Methods including "Test" in in their names perform tests, all other methods
        return t-statistics. Among the "Test" methods, :code:`double-`valued methods return p-values; :code:`boolean-`valued
        methods perform fixed significance level tests. Significance levels are always specified as numbers between 0 and 0.5
        (e.g. tests at the 95% level use :code:`alpha=0.05`).
    
        Input to tests can be either :code:`double[]` arrays or :class:`~org.hipparchus.stat.descriptive.StatisticalSummary`
        instances.
    
        Uses Hipparchus :class:`~org.hipparchus.stat.inference.https:.www.hipparchus.org.hipparchus` implementation to estimate
        exact p-values.
    """
    def __init__(self): ...
    @typing.overload
    def homoscedasticT(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Computes t test statistic for 2-sample t-test under the hypothesis of equal subpopulation variances.
        
            Parameters:
                m1 (double): first sample mean
                m2 (double): second sample mean
                v1 (double): first sample variance
                v2 (double): second sample variance
                n1 (double): first sample n
                n2 (double): second sample n
        
            Returns:
                t test statistic
        
        
        """
        ...
    @typing.overload
    def homoscedasticT(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def homoscedasticTTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    def homoscedasticTTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def homoscedasticTTest(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    def pairedT(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def pairedTTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    def pairedTTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def t(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Computes t test statistic for 1-sample t-test.
        
            Parameters:
                m (double): sample mean
                mu (double): constant to test against
                v (double): sample variance
                n (double): sample n
        
            Returns:
                t test statistic
        
            Computes t test statistic for 2-sample t-test.
        
            Does not assume that subpopulation variances are equal.
        
            Parameters:
                m1 (double): first sample mean
                m2 (double): second sample mean
                v1 (double): first sample variance
                v2 (double): second sample variance
                n1 (double): first sample n
                n2 (double): second sample n
        
            Returns:
                t test statistic
        
        
        """
        ...
    @typing.overload
    def t(self, double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def t(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def t(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def tTest(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    def tTest(self, double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, double2: float) -> bool: ...
    @typing.overload
    def tTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float) -> bool: ...
    @typing.overload
    def tTest(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary, double: float) -> bool: ...
    @typing.overload
    def tTest(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def tTest(self, double: float, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    def tTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def tTest(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...

class WilcoxonSignedRankTest:
    """
    public classWilcoxonSignedRankTest extends :class:`~org.hipparchus.stat.inference.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        An implementation of the Wilcoxon signed-rank test. This implementation currently handles only paired (equal length)
        samples and discards tied pairs from the analysis. The latter behavior differs from the R implementation of wilcox.test
        and corresponds to the "wilcox" zero_method configurable in scipy.stats.wilcoxon.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy, tiesStrategy: org.hipparchus.stat.ranking.TiesStrategy): ...
    def wilcoxonSignedRank(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    def wilcoxonSignedRankTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...


class __module_protocol__(Protocol):
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
