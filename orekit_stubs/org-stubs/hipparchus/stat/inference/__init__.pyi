import java.lang
import java.util
import org.hipparchus.distribution
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.ranking
import typing



class AlternativeHypothesis(java.lang.Enum['AlternativeHypothesis']):
    """
    public enum AlternativeHypothesis extends Enum<:class:`~org.hipparchus.stat.inference.AlternativeHypothesis`>
    
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
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['AlternativeHypothesis']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AlternativeHypothesis c : AlternativeHypothesis.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class BinomialTest:
    """
    public class BinomialTest extends Object
    
        Implements binomial test statistics.
    
        Exact test for the statistical significance of deviations from a theoretically expected distribution of observations
        into two categories.
    
        Also see:
            `Binomial test (Wikipedia) <http://en.wikipedia.org/wiki/Binomial_test>`
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
                : if :code:`numberOfTrials` or :code:`numberOfSuccesses` is negative
                : if :code:`probability` is not between 0 and 1
                : if :code:`numberOfTrials` < :code:`numberOfSuccesses` or if :code:`alternateHypothesis` is null.
        
            Also see:
                :class:`~org.hipparchus.stat.inference.AlternativeHypothesis`
        
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
        
            Returns:
                p-value
        
            Raises:
                : if :code:`numberOfTrials` or :code:`numberOfSuccesses` is negative
                : if :code:`probability` is not between 0 and 1
                : if :code:`numberOfTrials` < :code:`numberOfSuccesses` or if :code:`alternateHypothesis` is null.
        
            Also see:
                :class:`~org.hipparchus.stat.inference.AlternativeHypothesis`
        
        
        """
        ...

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
    """
    public class InferenceTestUtils extends Object
    
        A collection of static methods to create inference test instances or to perform inference tests.
    """
    @staticmethod
    def approximateP(double: float, int: int, int2: int) -> float:
        """
        
            Also see:
                :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.approximateP`
        
        
        """
        ...
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
    def exactP(double: float, int: int, int2: int, boolean: bool) -> float:
        """
        
            Also see:
                :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.exactP`
        
        
        """
        ...
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
    def oneWayAnovaFValue(collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]], typing.Set[typing.List[float]]]) -> float: ...
    @staticmethod
    def oneWayAnovaPValue(collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]], typing.Set[typing.List[float]]]) -> float: ...
    @staticmethod
    def oneWayAnovaTest(collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]], typing.Set[typing.List[float]]], double: float) -> bool: ...
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
    """
    public class KolmogorovSmirnovTest extends Object
    
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
        default 2-sample test method, null works as follows:
    
          - For small samples (where the product of the sample sizes is less than
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT`), the method presented in [4] is used
            to compute the exact p-value for the 2-sample test.
          - When the product of the sample sizes exceeds
            :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT`, the asymptotic distribution of
            \(D_{n,m}\) is used. See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.approximateP` for details on the
            approximation.
    
    
        If the product of the sample sizes is less than
        :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.LARGE_SAMPLE_PRODUCT` and the sample data contains ties,
        random jitter is added to the sample data to break ties before applying the algorithm above. Alternatively, the null
        method, modeled after `ks.boot <http://sekhon.berkeley.edu/matching/ks.boot.html>` in the R Matching package [3], can be
        used if ties are known to be present in the data.
    
        In the two-sample case, \(D_{n,m}\) has a discrete distribution. This makes the p-value associated with the null
        hypothesis \(H_0 : D_{n,m} \ge d \) differ from \(H_0 : D_{n,m} > d \) by the mass of the observed value \(d\). To
        distinguish these, the two-sample tests use a boolean :code:`strict` parameter. This parameter is ignored for large
        samples.
    
        The methods used by the 2-sample default implementation are also exposed directly:
    
          - :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.exactP` computes exact 2-sample p-values
          - :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.approximateP` uses the asymptotic distribution The
            :code:`boolean` arguments in the first two methods allow the probability used to estimate the p-value to be expressed
            using strict or non-strict inequality. See null.
    
    
        References:
    
          - [1] ` Evaluating Kolmogorov's Distribution <http://www.jstatsoft.org/v08/i18/>` by George Marsaglia, Wai Wan Tsang, and
            Jingbo Wang
          - [2] ` Computing the Two-Sided Kolmogorov-Smirnov Distribution <http://www.jstatsoft.org/v39/i11/>` by Richard Simard and
            Pierre L'Ecuyer
          - [3] Jasjeet S. Sekhon. 2011. ` Multivariate and Propensity Score Matching Software with Automated Balance Optimization:
            The Matching package for R <http://www.jstatsoft.org/article/view/v042i07>` Journal of Statistical Software, 42(7):
            1-52.
          - [4] Kim, P. J. and Jennrich, R. I. (1970). Tables of the Exact Sampling Distribution of the Two-Sample
            Kolmogorov-Smirnov Criterion D_mn ,mÃ¢â€°Â¦n in Selected Tables in Mathematical Statistics, Vol. 1, H. L. Harter and D.
            B. Owen, editors.
    
    
        Note that [1] contains an error in computing h, refer to MATH-437 for details.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int): ...
    def approximateP(self, double: float, int: int, int2: int) -> float:
        """
            Uses the Kolmogorov-Smirnov distribution to approximate \(P(D_{n,m} > d)\) where \(D_{n,m}\) is the 2-sample
            Kolmogorov-Smirnov statistic. See null for the definition of \(D_{n,m}\).
        
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
    def bootstrap(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int) -> float:
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
    def bootstrap(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, boolean: bool) -> float: ...
    @typing.overload
    def cdf(self, double: float, int: int) -> float: ...
    @typing.overload
    def cdf(self, double: float, int: int, boolean: bool) -> float: ...
    def cdfExact(self, double: float, int: int) -> float: ...
    def exactP(self, double: float, int: int, int2: int, boolean: bool) -> float:
        """
            Computes \(P(D_{n,m} > d)\) if :code:`strict` is :code:`true`; otherwise \(P(D_{n,m} \ge d)\), where \(D_{n,m}\) is the
            2-sample Kolmogorov-Smirnov statistic. See null for the definition of \(D_{n,m}\).
        
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
    def kolmogorovSmirnovStatistic(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float:
        """
            Computes the one-sample Kolmogorov-Smirnov test statistic, \(D_n=\sup_x |F_n(x)-F(x)|\) where \(F\) is the distribution
            (cdf) function associated with :code:`distribution`, \(n\) is the length of :code:`data` and \(F_n\) is the empirical
            distribution that puts mass \(1/n\) at each of the values in :code:`data`.
        
            Parameters:
                distribution (RealDistribution): reference distribution
                data (double[]): sample being evaluated
        
            Returns:
                Kolmogorov-Smirnov statistic \(D_n\)
        
            Raises:
                : if :code:`data` does not have length at least 2
                : if :code:`data` is null
        
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
                : if either :code:`x` or :code:`y` does not have length at least 2
                : if either :code:`x` or :code:`y` is null
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovStatistic(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float], double2: float) -> bool:
        """
            Computes the *p-value*, or *observed significance level*, of a one-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`data` conforms to
            :code:`distribution`. If :code:`exact` is true, the distribution used to compute the p-value is computed using extended
            precision. See :meth:`~org.hipparchus.stat.inference.KolmogorovSmirnovTest.cdfExact`.
        
            Parameters:
                distribution (RealDistribution): reference distribution
                data (double[]): sample being being evaluated
                exact (boolean): whether or not to force exact computation of the p-value
        
            Returns:
                the p-value associated with the null hypothesis that :code:`data` is a sample from :code:`distribution`
        
            Raises:
                : if :code:`data` does not have length at least 2
                : if :code:`data` is null
        
            Computes the *p-value*, or *observed significance level*, of a two-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`x` and :code:`y` are
            samples drawn from the same probability distribution. Specifically, what is returned is an estimate of the probability
            that the null associated with a randomly selected partition of the combined sample into subsamples of sizes
            :code:`x.length` and :code:`y.length` will strictly exceed (if :code:`strict` is :code:`true`) or be at least as large
            as :code:`strict = false`) as :code:`kolmogorovSmirnovStatistic(x, y)`.
        
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
        
            If ties are known to be present in the data, null may be used as an alternative method for estimating the p-value.
        
            Parameters:
                x (double[]): first sample dataset
                y (double[]): second sample dataset
                strict (boolean): whether or not the probability to compute is expressed as a strict inequality (ignored for large samples)
        
            Returns:
                p-value associated with the null hypothesis that :code:`x` and :code:`y` represent samples from the same distribution
        
            Raises:
                : if either :code:`x` or :code:`y` does not have length at least 2
                : if either :code:`x` or :code:`y` is null
        
            Also see:
        
            Performs a ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null
            hypothesis that :code:`data` conforms to :code:`distribution`.
        
            Parameters:
                distribution (RealDistribution): reference distribution
                data (double[]): sample being being evaluated
                alpha (double): significance level of the test
        
            Returns:
                true iff the null hypothesis that :code:`data` is a sample from :code:`distribution` can be rejected with confidence 1 -
                :code:`alpha`
        
            Raises:
                : if :code:`data` does not have length at least 2
                : if :code:`data` is null
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float:
        """
            Computes the *p-value*, or *observed significance level*, of a two-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`x` and :code:`y` are
            samples drawn from the same probability distribution. Assumes the strict form of the inequality used to compute the
            p-value. See null.
        
            Parameters:
                x (double[]): first sample dataset
                y (double[]): second sample dataset
        
            Returns:
                p-value associated with the null hypothesis that :code:`x` and :code:`y` represent samples from the same distribution
        
            Raises:
                : if either :code:`x` or :code:`y` does not have length at least 2
                : if either :code:`x` or :code:`y` is null
        
            Computes the *p-value*, or *observed significance level*, of a one-sample ` Kolmogorov-Smirnov test
            <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that :code:`data` conforms to
            :code:`distribution`.
        
            Parameters:
                distribution (RealDistribution): reference distribution
                data (double[]): sample being being evaluated
        
            Returns:
                the p-value associated with the null hypothesis that :code:`data` is a sample from :code:`distribution`
        
            Raises:
                : if :code:`data` does not have length at least 2
                : if :code:`data` is null
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.List[float], boolean: bool) -> float: ...
    def ksSum(self, double: float, double2: float, int: int) -> float:
        """
            Computes \( 1 + 2 \sum_{i=1}^\infty (-1)^i e^{-2 i^2 t^2} \) stopping when successive partial sums are within
            :code:`tolerance` of one another, or when :code:`maxIterations` partial sums have been computed. If the sum does not
            converge before :code:`maxIterations` iterations a null is thrown.
        
            Parameters:
                t (double): argument
                tolerance (double): Cauchy criterion for partial sums
                maxIterations (int): maximum number of partial sums to compute
        
            Returns:
                Kolmogorov sum evaluated at t
        
            Raises:
                : if the series does not converge
        
        
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
    public class MannWhitneyUTest extends Object
    
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
    def mannWhitneyU(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def mannWhitneyUTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def mannWhitneyUTest(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> float: ...

class OneWayAnova:
    """
    public class OneWayAnova extends Object
    
        Implements one-way ANOVA (analysis of variance) statistics.
    
        Tests for differences between two or more categories of univariate data (for example, the body mass index of
        accountants, lawyers, doctors and computer programmers). When two categories are given, this is equivalent to the
        :class:`~org.hipparchus.stat.inference.TTest`.
    
        Uses the null to estimate exact p-values.
    
        This implementation is based on a description at http://faculty.vassar.edu/lowry/ch13pt1.html
    
        .. code-block: java
        
         Abbreviations: bg = between groups,
                        wg = within groups,
                        ss = sum squared deviations
    """
    def __init__(self): ...
    def anovaFValue(self, collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]], typing.Set[typing.List[float]]]) -> float: ...
    @typing.overload
    def anovaPValue(self, collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]], typing.Set[typing.List[float]]]) -> float: ...
    @typing.overload
    def anovaPValue(self, collection: typing.Union[java.util.Collection[org.hipparchus.stat.descriptive.StreamingStatistics], typing.Sequence[org.hipparchus.stat.descriptive.StreamingStatistics], typing.Set[org.hipparchus.stat.descriptive.StreamingStatistics]], boolean: bool) -> float: ...
    def anovaTest(self, collection: typing.Union[java.util.Collection[typing.List[float]], typing.Sequence[typing.List[float]], typing.Set[typing.List[float]]], double: float) -> bool: ...

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
    """
    public class WilcoxonSignedRankTest extends Object
    
        An implementation of the Wilcoxon signed-rank test. This implementation currently handles only paired (equal length)
        samples and discards tied pairs from the analysis. The latter behavior differs from the R implementation of wilcox.test
        and corresponds to the "wilcox" zero_method configurable in scipy.stats.wilcoxon.
    """
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
