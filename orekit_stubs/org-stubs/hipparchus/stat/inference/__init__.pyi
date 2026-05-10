
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
    def valueOf(name: str) -> 'AlternativeHypothesis':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AlternativeHypothesis']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AlternativeHypothesis c : AlternativeHypothesis.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class BinomialTest:
    """
    Implements binomial test statistics.
    
    Exact test for the statistical significance of deviations from a theoretically expected distribution of observations into two categories.
    
    Also see:
        `Binomial test (Wikipedia) <http://en.wikipedia.org/wiki/Binomial_test>`
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    def binomialTest(self, numberOfTrials: int, numberOfSuccesses: int, probability: float, alternativeHypothesis: AlternativeHypothesis, alpha: float) -> bool:
        """
        Returns whether the null hypothesis can be rejected with the given confidence level.
        
        Preconditions:
        
          - Number of trials must be ≥ 0.
          - Number of successes must be ≥ 0.
          - Number of successes must be ≤ number of trials.
          - Probability must be ≥ 0 and ≤ 1.
        
        
        Parameters:
            numberOfTrials (int): number of trials performed
            numberOfSuccesses (int): number of successes observed
            probability (double): assumed probability of a single trial under the null hypothesis
            alternativeHypothesis (AlternativeHypothesis): type of hypothesis being evaluated (one- or two-sided)
            alpha (double): significance level of the test
        
        Returns:
            true if the null hypothesis can be rejected with confidence 1 - alpha
        
        Raises:
            hipparchus: if numberOfTrials or numberOfSuccesses is negative
            hipparchus: if probability is not between 0 and 1
            hipparchus: if numberOfTrials < numberOfSuccesses or if alternateHypothesis is null.
        
        Also see:
            AlternativeHypothesis
        
        """
        ...
    @typing.overload
    def binomialTest(self, numberOfTrials: int, numberOfSuccesses: int, probability: float, alternativeHypothesis: AlternativeHypothesis) -> float:
        """
        Returns the observed significance level, or `p-value <http://www.cas.lancs.ac.uk/glossary_v1.1/hyptest.html#pvalue>`, associated with a ` Binomial test <http://en.wikipedia.org/wiki/Binomial_test>`.
        
        The number returned is the smallest significance level at which one can reject the null hypothesis. The form of the hypothesis depends on alternativeHypothesis.
        
        The p-Value represents the likelihood of getting a result at least as extreme as the sample, given the provided probability of success on a single trial. For single-sided tests, this value can be directly derived from the Binomial distribution. For the two-sided test, the implementation works as follows: we start by looking at the most extreme cases (0 success and n success where n is the number of trials from the sample) and determine their likelihood. The lower value is added to the p-Value (if both values are equal, both are added). Then we continue with the next extreme value, until we added the value for the actual observed sample.
        
        * Preconditions:
        
          - Number of trials must be ≥ 0.
          - Number of successes must be ≥ 0.
          - Number of successes must be ≤ number of trials.
          - Probability must be ≥ 0 and ≤ 1.
        
        
        Parameters:
            numberOfTrials (int): number of trials performed
            numberOfSuccesses (int): number of successes observed
            probability (double): assumed probability of a single trial under the null hypothesis
            alternativeHypothesis (AlternativeHypothesis): type of hypothesis being evaluated (one- or two-sided)
        
        Returns:
            p-value
        
        Raises:
            hipparchus: if numberOfTrials or numberOfSuccesses is negative
            hipparchus: if probability is not between 0 and 1
            hipparchus: if numberOfTrials < numberOfSuccesses or if alternateHypothesis is null.
        
        Also see:
            AlternativeHypothesis
        
        
        """
        ...

class ChiSquareTest:
    """
    Implements Chi-Square test statistics.
    
    This implementation handles both known and unknown distributions.
    
    Two samples tests can be used when the distribution is unknown a priori but provided by one sample, or when the hypothesis under test is that the two samples come from the same underlying distribution.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    def chiSquare(self, expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def chiSquare(self, counts: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    def chiSquareDataSetsComparison(self, observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Computes a ` Chi-Square two sample test statistic <http://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/chi2samp.htm>` comparing bin frequency counts in observed1 and observed2.
        
        The sums of frequency counts in the two samples are not required to be the same. The formula used to compute the test statistic is 2` / (observed1[i] + observed2[i])]`
        
        where K = √[∑(observed2 / ∑(observed1)]
        
        This statistic can be used to perform a Chi-Square test evaluating the null hypothesis that both observed counts follow the same distribution.
        
        Preconditions:
        
          - Observed counts must be non-negative.
          - Observed counts for a specific bin must not both be zero.
          - Observed counts for a specific sample must not all be 0.
          -         The arrays observed1 and observed2 must have the same length and their common length must be at least 2.
        
        If any of the preconditions are not met, an IllegalArgumentException is thrown.
        
        Parameters:
            observed1 (long[]): array of observed frequency counts of the first data set
            observed2 (long[]): array of observed frequency counts of the second data set
        
        Returns:
            test statistic
        
        Raises:
            hipparchus: the the length of the arrays does not match
            hipparchus: if any entries in observed1 or observed2 are negative
            hipparchus: if either all counts of observed1 or observed2 are zero, or if the count at some index is zero for both
                arrays
        
        
        """
        ...
    @typing.overload
    def chiSquareTest(self, expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    def chiSquareTest(self, longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    def chiSquareTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def chiSquareTest(self, counts: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    @typing.overload
    def chiSquareTestDataSetsComparison(self, observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    def chiSquareTestDataSetsComparison(self, observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...

class GTest:
    """
    Implements `G Test <http://en.wikipedia.org/wiki/G-test>` statistics.
    
    This is known in statistical genetics as the McDonald-Kreitman test. The implementation handles both known and unknown distributions.
    
    Two samples tests can be used when the distribution is unknown a priori but provided by one sample, or when the hypothesis under test is that the two samples come from the same underlying distribution.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def g(self, expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Computes the `G statistic for Goodness of Fit <http://en.wikipedia.org/wiki/G-test>` comparing observed and expected frequency counts.
        
        This statistic can be used to perform a G test (Log-Likelihood Ratio Test) evaluating the null hypothesis that the observed counts follow the expected distribution.
        
        Preconditions:
        
          - Expected counts must all be positive.
          - Observed counts must all be ≥ 0.
          - The observed and expected arrays must have the same length and their common length must be at least 2.
        
        If any of the preconditions are not met, a MathIllegalArgumentException is thrown.
        
        Note:This implementation rescales the expected array if necessary to ensure that the sum of the expected and observed counts are equal.
        
        Parameters:
            observed (double[]): array of observed frequency counts
            expected (long[]): array of expected frequency counts
        
        Returns:
            G-Test statistic
        
        Raises:
            hipparchus: if observed has negative entries
            hipparchus: if expected has entries that are not strictly positive
            hipparchus: if the array lengths do not match or are less than 2.
        
        
        """
        ...
    def gDataSetsComparison(self, observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Computes a G (Log-Likelihood Ratio) two sample test statistic for independence comparing frequency counts in observed1 and observed2. The sums of frequency counts in the two samples are not required to be the same. The formula used to compute the test statistic is
        
        2 * totalSum * [H(rowSums) + H(colSums) - H(k)]
        
        where H is the ` Shannon Entropy <http://en.wikipedia.org/wiki/Entropy_%28information_theory%29>` of the random
        variable formed by viewing the elements of the argument array as incidence counts;
        
        
        k is a matrix with rows [observed1, observed2];
        
        
        rowSums, colSums are the row/col sums of k;
        
        and totalSum is the overall sum of all entries in k.
        
        This statistic can be used to perform a G test evaluating the null hypothesis that both observed counts are independent
        
        Preconditions:
        
          - Observed counts must be non-negative.
          - Observed counts for a specific bin must not both be zero.
          - Observed counts for a specific sample must not all be 0.
          -         The arrays observed1 and observed2 must have the same length and their common length must be at least 2.
        
        If any of the preconditions are not met, a MathIllegalArgumentException is thrown.
        
        Parameters:
            observed1 (long[]): array of observed frequency counts of the first data set
            observed2 (long[]): array of observed frequency counts of the second data set
        
        Returns:
            G-Test statistic
        
        Raises:
            hipparchus: the the lengths of the arrays do not match or their common length is less than 2
            hipparchus: if any entry in observed1 or observed2 is negative
            hipparchus: if either all counts of observed1 or observed2 are zero, or if the count at the same index is zero for
                both arrays.
        
        
        """
        ...
    @typing.overload
    def gTest(self, expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    def gTest(self, expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    def gTestDataSetsComparison(self, observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    def gTestDataSetsComparison(self, observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    def gTestIntrinsic(self, expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Returns the intrinsic (Hardy-Weinberg proportions) p-Value, as described in p64-69 of McDonald, J.H. 2009. Handbook of Biological Statistics (2nd ed.). Sparky House Publishing, Baltimore, Maryland.
        
        The probability returned is the tail probability beyond g in the ChiSquare distribution with degrees of freedom two less than the common length of expected and observed.
        
        Parameters:
            observed (double[]): array of observed frequency counts
            expected (long[]): array of expected frequency counts
        
        Returns:
            p-value
        
        Raises:
            hipparchus: if observed has negative entries
            hipparchus: expected has entries that are not strictly positive
            hipparchus: if the array lengths do not match or are less than 2.
            hipparchus: if an error occurs computing the p-value.
        
        
        """
        ...
    def rootLogLikelihoodRatio(self, k11: int, k12: int, k21: int, k22: int) -> float:
        """
        Calculates the root log-likelihood ratio for 2 state Datasets. See gDataSetsComparison.
        
        Given two events A and B, let k11 be the number of times both events occur, k12 the incidence of B without A, k21 the count of A without B, and k22 the number of times neither A nor B occurs. What is returned by this method is
        
        (sgn) sqrt(gValueDataSetsComparison({k11, k12}, {k21, k22})
        
        where sgn is -1 if k11 / (k11 + k12) < k21 / (k21 + k22));
        
        1 otherwise.
        
        Signed root LLR has two advantages over the basic LLR: a) it is positive where k11 is bigger than expected, negative where it is lower b) if there is no difference it is asymptotically normally distributed. This allows one to talk about "number of standard deviations" which is a more common frame of reference than the chi^2 distribution.
        
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
    A collection of static methods to create inference test instances or to perform inference tests.
    """
    @staticmethod
    def approximateP(d: float, n: int, m: int) -> float:
        """
        Uses the Kolmogorov-Smirnov distribution to approximate \(P(D_{n,m} > d)\) where \(D_{n,m}\) is the 2-sample Kolmogorov-Smirnov statistic. See kolmogorovSmirnovStatistic for the definition of \(D_{n,m}\).
        
        Specifically, what is returned is \(1 - k(d \sqrt{mn / (m + n)})\) where \(k(t) = 1 + 2 \sum_{i=1}^\infty (-1)^i e^{-2 i^2 t^2}\). See ksSum for details on how convergence of the sum is determined. This implementation passes ksSum KS_SUM_CAUCHY_CRITERION as tolerance and MAXIMUM_PARTIAL_SUM_COUNT as maxIterations.
        
        Parameters:
            d (double): D-statistic value
            n (int): first sample size
            m (int): second sample size
        
        Returns:
            approximate probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than d
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def chiSquare(expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquare(counts: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    @staticmethod
    def chiSquareDataSetsComparison(observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Computes a ` Chi-Square two sample test statistic <http://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/chi2samp.htm>` comparing bin frequency counts in observed1 and observed2.
        
        The sums of frequency counts in the two samples are not required to be the same. The formula used to compute the test statistic is 2` / (observed1[i] + observed2[i])]`
        
        where K = √[∑(observed2 / ∑(observed1)]
        
        This statistic can be used to perform a Chi-Square test evaluating the null hypothesis that both observed counts follow the same distribution.
        
        Preconditions:
        
          - Observed counts must be non-negative.
          - Observed counts for a specific bin must not both be zero.
          - Observed counts for a specific sample must not all be 0.
          -         The arrays observed1 and observed2 must have the same length and their common length must be at least 2.
        
        If any of the preconditions are not met, an IllegalArgumentException is thrown.
        
        Parameters:
            observed1 (long[]): array of observed frequency counts of the first data set
            observed2 (long[]): array of observed frequency counts of the second data set
        
        Returns:
            test statistic
        
        Raises:
            hipparchus: the the length of the arrays does not match
            hipparchus: if any entries in observed1 or observed2 are negative
            hipparchus: if either all counts of observed1 or observed2 are zero, or if the count at some index is zero for both
                arrays
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def chiSquareTest(expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(longArray: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray], double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(doubleArray: typing.Union[typing.List[float], jpype.JArray], longArray: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTest(counts: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def chiSquareTestDataSetsComparison(observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    @staticmethod
    def chiSquareTestDataSetsComparison(observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @staticmethod
    def exactP(d: float, m: int, n: int, strict: bool) -> float:
        """
        Computes \(P(D_{n,m} > d)\) if strict is true; otherwise \(P(D_{n,m} \ge d)\), where \(D_{n,m}\) is the 2-sample Kolmogorov-Smirnov statistic. See kolmogorovSmirnovStatistic for the definition of \(D_{n,m}\).
        
        The returned probability is exact, implemented by unwinding the recursive function definitions presented in [4] from the class javadoc.
        
        Parameters:
            d (double): D-statistic value
            n (int): first sample size
            m (int): second sample size
            strict (boolean): whether or not the probability to compute is expressed as a strict inequality
        
        Returns:
            probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than (resp. greater than or
            equal to) d
        
        
        """
        ...
    @staticmethod
    def g(expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Computes the `G statistic for Goodness of Fit <http://en.wikipedia.org/wiki/G-test>` comparing observed and expected frequency counts.
        
        This statistic can be used to perform a G test (Log-Likelihood Ratio Test) evaluating the null hypothesis that the observed counts follow the expected distribution.
        
        Preconditions:
        
          - Expected counts must all be positive.
          - Observed counts must all be ≥ 0.
          - The observed and expected arrays must have the same length and their common length must be at least 2.
        
        If any of the preconditions are not met, a MathIllegalArgumentException is thrown.
        
        Note:This implementation rescales the expected array if necessary to ensure that the sum of the expected and observed counts are equal.
        
        Parameters:
            observed (double[]): array of observed frequency counts
            expected (long[]): array of expected frequency counts
        
        Returns:
            G-Test statistic
        
        Raises:
            hipparchus: if observed has negative entries
            hipparchus: if expected has entries that are not strictly positive
            hipparchus: if the array lengths do not match or are less than 2.
        
        
        """
        ...
    @staticmethod
    def gDataSetsComparison(observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Computes a G (Log-Likelihood Ratio) two sample test statistic for independence comparing frequency counts in observed1 and observed2. The sums of frequency counts in the two samples are not required to be the same. The formula used to compute the test statistic is
        
        2 * totalSum * [H(rowSums) + H(colSums) - H(k)]
        
        where H is the ` Shannon Entropy <http://en.wikipedia.org/wiki/Entropy_%28information_theory%29>` of the random
        variable formed by viewing the elements of the argument array as incidence counts;
        
        
        k is a matrix with rows [observed1, observed2];
        
        
        rowSums, colSums are the row/col sums of k;
        
        and totalSum is the overall sum of all entries in k.
        
        This statistic can be used to perform a G test evaluating the null hypothesis that both observed counts are independent
        
        Preconditions:
        
          - Observed counts must be non-negative.
          - Observed counts for a specific bin must not both be zero.
          - Observed counts for a specific sample must not all be 0.
          -         The arrays observed1 and observed2 must have the same length and their common length must be at least 2.
        
        If any of the preconditions are not met, a MathIllegalArgumentException is thrown.
        
        Parameters:
            observed1 (long[]): array of observed frequency counts of the first data set
            observed2 (long[]): array of observed frequency counts of the second data set
        
        Returns:
            G-Test statistic
        
        Raises:
            hipparchus: the the lengths of the arrays do not match or their common length is less than 2
            hipparchus: if any entry in observed1 or observed2 is negative
            hipparchus: if either all counts of observed1 or observed2 are zero, or if the count at the same index is zero for
                both arrays.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def gTest(expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    @staticmethod
    def gTest(expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def gTestDataSetsComparison(observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    @staticmethod
    def gTestDataSetsComparison(observed1: typing.Union[typing.List[int], jpype.JArray], observed2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @staticmethod
    def gTestIntrinsic(expected: typing.Union[typing.List[float], jpype.JArray], observed: typing.Union[typing.List[int], jpype.JArray]) -> float:
        """
        Returns the intrinsic (Hardy-Weinberg proportions) p-Value, as described in p64-69 of McDonald, J.H. 2009. Handbook of Biological Statistics (2nd ed.). Sparky House Publishing, Baltimore, Maryland.
        
        The probability returned is the tail probability beyond g in the ChiSquare distribution with degrees of freedom two less than the common length of expected and observed.
        
        Parameters:
            observed (double[]): array of observed frequency counts
            expected (long[]): array of expected frequency counts
        
        Returns:
            p-value
        
        Raises:
            hipparchus: if observed has negative entries
            hipparchus: expected has entries that are not strictly positive
            hipparchus: if the array lengths do not match or are less than 2.
            hipparchus: if an error occurs computing the p-value.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def homoscedasticT(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticT(statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    @typing.overload
    @staticmethod
    def homoscedasticTTest(sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray], alpha: float) -> bool: ...
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
    def oneWayAnovaFValue(categoryData: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float:
        """
        Computes the ANOVA F-value for a collection of double[] arrays.
        
        Preconditions:
        
          - The categoryData Collection must contain double[] arrays.
          - There must be at least two double[] arrays in the categoryData collection and each of these arrays must
            contain at least two values.
        
        This implementation computes the F statistic using the definitional formula
        
           F = msbg/mswg
        
        where
        
          msbg = between group mean square mswg = within group mean square
        
        are as defined ` here <http://faculty.vassar.edu/lowry/ch13pt1.html>`
        
        Parameters:
            categoryData (Collection<double[]> categoryData): Collection of double[] arrays each containing data for one category
        
        Returns:
            Fvalue
        
        Raises:
            hipparchus: if categoryData is null
            hipparchus: if the length of the categoryData array is less than 2 or a contained double[] array does not have at
                least two values
        
        
        """
        ...
    @staticmethod
    def oneWayAnovaPValue(categoryData: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float:
        """
        Computes the ANOVA P-value for a collection of double[] arrays.
        
        Preconditions:
        
          - The categoryData Collection must contain double[] arrays.
          - There must be at least two double[] arrays in the categoryData collection and each of these arrays must
            contain at least two values.
        
        This implementation uses the hipparchus to estimate the exact p-value, using the formula
        
           p = 1 - cumulativeProbability(F)
        
        where F is the F value and cumulativeProbability is the Hipparchus implementation of the F distribution.
        
        Parameters:
            categoryData (Collection<double[]> categoryData): Collection of double[] arrays each containing data for one category
        
        Returns:
            Pvalue
        
        Raises:
            hipparchus: if categoryData is null
            hipparchus: if the length of the categoryData array is less than 2 or a contained double[] array does not have at
                least two values
            hipparchus: if the p-value can not be computed due to a convergence error
            hipparchus: if the maximum number of iterations is exceeded
        
        
        """
        ...
    @staticmethod
    def oneWayAnovaTest(categoryData: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]], alpha: float) -> bool:
        """
        Performs an ANOVA test, evaluating the null hypothesis that there is no difference among the means of the data categories.
        
        Preconditions:
        
          - The categoryData Collection must contain double[] arrays.
          - There must be at least two double[] arrays in the categoryData collection and each of these arrays must
            contain at least two values.
          - alpha must be strictly greater than 0 and less than or equal to 0.5.
        
        This implementation uses the hipparchus to estimate the exact p-value, using the formula
        
           p = 1 - cumulativeProbability(F)
        
        where F is the F value and cumulativeProbability is the Hipparchus implementation of the F distribution.
        
        True is returned iff the estimated p-value is less than alpha.
        
        Parameters:
            categoryData (Collection<double[]> categoryData): Collection of double[] arrays each containing data for one category
            alpha (double): significance level of the test
        
        Returns:
            true if the null hypothesis can be rejected with confidence 1 - alpha
        
        Raises:
            hipparchus: if categoryData is null
            hipparchus: if the length of the categoryData array is less than 2 or a contained double[] array does not have at
                least two values
            hipparchus: if alpha is not in the range (0, 0.5]
            hipparchus: if the p-value can not be computed due to a convergence error
            hipparchus: if the maximum number of iterations is exceeded
        
        
        """
        ...
    @staticmethod
    def pairedT(sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes a paired, 2-sample t-statistic based on the data in the input arrays. The t-statistic returned is equivalent to what would be returned by computing the one-sample t-statistic t, with mu = 0 and the sample array consisting of the (signed) differences between corresponding entries in sample1 and sample2
        
        Preconditions:
        
          - The input arrays must have the same length and their common length must be at least 2.
        
        
        Parameters:
            sample1 (double[]): array of sample data values
            sample2 (double[]): array of sample data values
        
        Returns:
            t statistic
        
        Raises:
            hipparchus: if the arrays are null
            hipparchus: if the arrays are empty
            hipparchus: if the length of the arrays is not equal
            hipparchus: if the length of the arrays is < 2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def pairedTTest(sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    @staticmethod
    def pairedTTest(sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @staticmethod
    def rootLogLikelihoodRatio(k11: int, k12: int, k21: int, k22: int) -> float:
        """
        Calculates the root log-likelihood ratio for 2 state Datasets. See gDataSetsComparison.
        
        Given two events A and B, let k11 be the number of times both events occur, k12 the incidence of B without A, k21 the count of A without B, and k22 the number of times neither A nor B occurs. What is returned by this method is
        
        (sgn) sqrt(gValueDataSetsComparison({k11, k12}, {k21, k22})
        
        where sgn is -1 if k11 / (k11 + k12) < k21 / (k21 + k22));
        
        1 otherwise.
        
        Signed root LLR has two advantages over the basic LLR: a) it is positive where k11 is bigger than expected, negative where it is lower b) if there is no difference it is asymptotically normally distributed. This allows one to talk about "number of standard deviations" which is a more common frame of reference than the chi^2 distribution.
        
        Parameters:
            k11 (long): number of times the two events occurred together (AB)
            k12 (long): number of times the second event occurred WITHOUT the first event (notA,B)
            k21 (long): number of times the first event occurred WITHOUT the second event (A, notB)
            k22 (long): number of times something else occurred (i.e. was neither of these events (notA, notB)
        
        Returns:
            root log-likelihood ratio
        
        Raises:
            hipparchus: 
        
        """
        ...
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
    Implementation of the ` Kolmogorov-Smirnov (K-S) test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` for equality of continuous distributions.
    
    The K-S test uses a statistic based on the maximum deviation of the empirical distribution of sample data points from the distribution expected under the null hypothesis. For one-sample tests evaluating the null hypothesis that a set of sample data points follow a given distribution, the test statistic is \(D_n=\sup_x |F_n(x)-F(x)|\), where \(F\) is the expected distribution and \(F_n\) is the empirical distribution of the \(n\) sample data points. The distribution of \(D_n\) is estimated using a method based on [1] with certain quick decisions for extreme values given in [2].
    
    Two-sample tests are also supported, evaluating the null hypothesis that the two samples x and y come from the same underlying distribution. In this case, the test statistic is \(D_{n,m}=\sup_t | F_n(t)-F_m(t)|\) where \(n\) is the length of x, \(m\) is the length of y, \(F_n\) is the empirical distribution that puts mass \(1/n\) at each of the values in x and \(F_m\) is the empirical distribution of the y values. The default 2-sample test method, kolmogorovSmirnovTest works as follows:
    
      - For small samples (where the product of the sample sizes is less than
        LARGE_SAMPLE_PRODUCT), the method presented in [4] is used
        to compute the exact p-value for the 2-sample test.
      - When the product of the sample sizes exceeds
        LARGE_SAMPLE_PRODUCT, the asymptotic distribution of
        \(D_{n,m}\) is used. See approximateP for details on the
        approximation.
    
    If the product of the sample sizes is less than LARGE_SAMPLE_PRODUCT and the sample data contains ties, random jitter is added to the sample data to break ties before applying the algorithm above. Alternatively, the bootstrap method, modeled after `ks.boot <http://sekhon.berkeley.edu/matching/ks.boot.html>` in the R Matching package [3], can be used if ties are known to be present in the data.
    
    In the two-sample case, \(D_{n,m}\) has a discrete distribution. This makes the p-value associated with the null hypothesis \(H_0 : D_{n,m} \ge d \) differ from \(H_0 : D_{n,m} > d \) by the mass of the observed value \(d\). To distinguish these, the two-sample tests use a boolean strict parameter. This parameter is ignored for large samples.
    
    The methods used by the 2-sample default implementation are also exposed directly:
    
      - exactP computes exact 2-sample p-values
      - approximateP uses the asymptotic distribution The
        boolean arguments in the first two methods allow the probability used to estimate the p-value to be expressed
        using strict or non-strict inequality. See
        kolmogorovSmirnovTest.
    
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
    
    Note that [1] contains an error in computing h, refer to MATH for details.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, seed: int): ...
    def approximateP(self, d: float, n: int, m: int) -> float:
        """
        Uses the Kolmogorov-Smirnov distribution to approximate \(P(D_{n,m} > d)\) where \(D_{n,m}\) is the 2-sample Kolmogorov-Smirnov statistic. See kolmogorovSmirnovStatistic for the definition of \(D_{n,m}\).
        
        Specifically, what is returned is \(1 - k(d \sqrt{mn / (m + n)})\) where \(k(t) = 1 + 2 \sum_{i=1}^\infty (-1)^i e^{-2 i^2 t^2}\). See ksSum for details on how convergence of the sum is determined. This implementation passes ksSum KS_SUM_CAUCHY_CRITERION as tolerance and MAXIMUM_PARTIAL_SUM_COUNT as maxIterations.
        
        Parameters:
            d (double): D-statistic value
            n (int): first sample size
            m (int): second sample size
        
        Returns:
            approximate probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than d
        
        
        """
        ...
    @typing.overload
    def bootstrap(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], iterations: int) -> float:
        """
        Estimates the p-value of a two-sample ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that x and y are samples drawn from the same probability distribution. This method estimates the p-value by repeatedly sampling sets of size length and length from the empirical distribution of the combined sample. When strict is true, this is equivalent to the algorithm implemented in the R function boot, described in
        
         Jasjeet S. Sekhon. 2011. 'Multivariate and Propensity Score Matching Software with Automated Balance Optimization: The Matching package for R.' Journal of Statistical Software, 42(7): 1-52.
        
        Parameters:
            x (double[]): first sample
            y (double[]): second sample
            iterations (int): number of bootstrap resampling iterations
            strict (boolean): whether or not the null hypothesis is expressed as a strict inequality
        
        Returns:
            estimated p-value
        
        Computes bootstrap(x, y, iterations, true). This is equivalent to ks.boot(x,y, nboots=iterations) using the R Matching package function. See #bootstrap(double[], double[], int, boolean).
        
        Parameters:
            x (double[]): first sample
            y (double[]): second sample
            iterations (int): number of bootstrap resampling iterations
        
        Returns:
            estimated p-value
        
        
        """
        ...
    @typing.overload
    def bootstrap(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], iterations: int, strict: bool) -> float: ...
    @typing.overload
    def cdf(self, d: float, n: int) -> float: ...
    @typing.overload
    def cdf(self, d: float, n: int, exact: bool) -> float: ...
    def cdfExact(self, d: float, n: int) -> float:
        """
        Calculates P(D_n < d). The result is exact in the sense that BigFraction/BigReal is used everywhere at the expense of very slow execution time. Almost never choose this in real applications unless you are very sure; this is almost solely for verification purposes. Normally, you would choose cdf. See the class javadoc for definitions and algorithm description.
        
        Parameters:
            d (double): statistic
            n (int): sample size
        
        Returns:
            \(P(D_n < d)\)
        
        Raises:
            hipparchus: if the algorithm fails to convert h to a
                hipparchus in expressing d as \((k - h) / m\)
                for integer k, m and \(0 <= h < 1\)
        
        
        """
        ...
    def exactP(self, d: float, n: int, m: int, strict: bool) -> float:
        """
        Computes \(P(D_{n,m} > d)\) if strict is true; otherwise \(P(D_{n,m} \ge d)\), where \(D_{n,m}\) is the 2-sample Kolmogorov-Smirnov statistic. See kolmogorovSmirnovStatistic for the definition of \(D_{n,m}\).
        
        The returned probability is exact, implemented by unwinding the recursive function definitions presented in [4] from the class javadoc.
        
        Parameters:
            d (double): D-statistic value
            n (int): first sample size
            m (int): second sample size
            strict (boolean): whether or not the probability to compute is expressed as a strict inequality
        
        Returns:
            probability that a randomly selected m-n partition of m + n generates \(D_{n,m}\) greater than (resp. greater than or
            equal to) d
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovStatistic(self, distribution: typing.Union[typing.List[float], jpype.JArray], data: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the one-sample Kolmogorov-Smirnov test statistic, \(D_n=\sup_x |F_n(x)-F(x)|\) where \(F\) is the distribution (cdf) function associated with distribution, \(n\) is the length of data and \(F_n\) is the empirical distribution that puts mass \(1/n\) at each of the values in data.
        
        Parameters:
            distribution (hipparchus): reference distribution
            data (double[]): sample being evaluated
        
        Returns:
            Kolmogorov-Smirnov statistic \(D_n\)
        
        Raises:
            hipparchus: if data does not have length at least 2
            hipparchus: if data is null
        
        Computes the two-sample Kolmogorov-Smirnov test statistic, \(D_{n,m}=\sup_x |F_n(x)-F_m(x)|\) where \(n\) is the length of x, \(m\) is the length of y, \(F_n\) is the empirical distribution that puts mass \(1/n\) at each of the values in x and \(F_m\) is the empirical distribution of the y values.
        
        Parameters:
            x (double[]): first sample
            y (double[]): second sample
        
        Returns:
            test statistic \(D_{n,m}\) used to evaluate the null hypothesis that x and y represent samples from the
            same underlying distribution
        
        Raises:
            hipparchus: if either x or y does not have length at least 2
            hipparchus: if either x or y is null
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovStatistic(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, distribution: org.hipparchus.distribution.RealDistribution, data: typing.Union[typing.List[float], jpype.JArray], exact: float) -> bool:
        """
        Computes the p-value, or observed significance level, of a one-sample ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that data conforms to distribution. If exact is true, the distribution used to compute the p-value is computed using extended precision. See cdfExact.
        
        Parameters:
            distribution (hipparchus): reference distribution
            data (double[]): sample being being evaluated
            exact (boolean): whether or not to force exact computation of the p-value
        
        Returns:
            the p-value associated with the null hypothesis that data is a sample from distribution
        
        Raises:
            hipparchus: if data does not have length at least 2
            hipparchus: if data is null
        
        Computes the p-value, or observed significance level, of a two-sample ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that x and y are samples drawn from the same probability distribution. Specifically, what is returned is an estimate of the probability that the kolmogorovSmirnovStatistic associated with a randomly selected partition of the combined sample into subsamples of sizes length and length will strictly exceed (if strict is true) or be at least as large as strict = false) as kolmogorovSmirnovStatistic(x, y).
        
          - For small samples (where the product of the sample sizes is less than
            LARGE_SAMPLE_PRODUCT), the exact p-value is computed using
            the method presented in [4], implemented in exactP.
          - When the product of the sample sizes exceeds
            LARGE_SAMPLE_PRODUCT, the asymptotic distribution of
            \(D_{n,m}\) is used. See approximateP for details on the
            approximation.
        
        If length < LARGE_SAMPLE_PRODUCT and the combined set of values in x and y contains ties, random jitter is added to x and y to break ties before computing \(D_{n,m}\) and the p-value. The jitter is uniformly distributed on (-minDelta / 2, minDelta / 2) where minDelta is the smallest pairwise difference between values in the combined sample.
        
        If ties are known to be present in the data, bootstrap may be used as an alternative method for estimating the p-value.
        
        Parameters:
            x (double[]): first sample dataset
            y (double[]): second sample dataset
            strict (boolean): whether or not the probability to compute is expressed as a strict inequality (ignored for large samples)
        
        Returns:
            p-value associated with the null hypothesis that x and y represent samples from the same distribution
        
        Raises:
            hipparchus: if either x or y does not have length at least 2
            hipparchus: if either x or y is null
        
        Also see:
            bootstrap
        
        Performs a ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that data conforms to distribution.
        
        Parameters:
            distribution (hipparchus): reference distribution
            data (double[]): sample being being evaluated
            alpha (double): significance level of the test
        
        Returns:
            true iff the null hypothesis that data is a sample from distribution can be rejected with confidence 1 -
            alpha
        
        Raises:
            hipparchus: if data does not have length at least 2
            hipparchus: if data is null
        
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovTest(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the p-value, or observed significance level, of a two-sample ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that x and y are samples drawn from the same probability distribution. Assumes the strict form of the inequality used to compute the p-value. See kolmogorovSmirnovTest.
        
        Parameters:
            x (double[]): first sample dataset
            y (double[]): second sample dataset
        
        Returns:
            p-value associated with the null hypothesis that x and y represent samples from the same distribution
        
        Raises:
            hipparchus: if either x or y does not have length at least 2
            hipparchus: if either x or y is null
        
        Computes the p-value, or observed significance level, of a one-sample ` Kolmogorov-Smirnov test <http://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test>` evaluating the null hypothesis that data conforms to distribution.
        
        Parameters:
            distribution (hipparchus): reference distribution
            data (double[]): sample being being evaluated
        
        Returns:
            the p-value associated with the null hypothesis that data is a sample from distribution
        
        Raises:
            hipparchus: if data does not have length at least 2
            hipparchus: if data is null
        
        """
        ...
    @typing.overload
    def kolmogorovSmirnovTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def kolmogorovSmirnovTest(self, realDistribution: org.hipparchus.distribution.RealDistribution, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool) -> float: ...
    def ksSum(self, t: float, tolerance: float, maxIterations: int) -> float:
        """
        Computes \( 1 + 2 \sum_{i=1}^\infty (-1)^i e^{-2 i^2 t^2} \) stopping when successive partial sums are within tolerance of one another, or when maxIterations partial sums have been computed. If the sum does not converge before maxIterations iterations a hipparchus is thrown.
        
        Parameters:
            t (double): argument
            tolerance (double): Cauchy criterion for partial sums
            maxIterations (int): maximum number of partial sums to compute
        
        Returns:
            Kolmogorov sum evaluated at t
        
        Raises:
            hipparchus: if the series does not converge
        
        
        """
        ...
    def pelzGood(self, d: float, n: int) -> float:
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
    An implementation of the Mann-Whitney U test.
    
    The definitions and computing formulas used in this implementation follow those in the article, ` Mann-Whitney U Test <http://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U>`
    
    In general, results correspond to (and have been tested against) the R wilcox.test function, with exact meaning the same thing in both APIs and CORRECT uniformly true in this implementation. For example, wilcox.test(x, y, alternative = "two.sided", mu = 0, paired = FALSE, exact = FALSE correct = TRUE) will return the same p-value as mannWhitneyUTest(x, y, false). The minimum of the W value returned by R for wilcox.test(x, y...) and wilcox.test(y, x...) should equal mannWhitneyU(x, y...).
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, nanStrategy: org.hipparchus.stat.ranking.NaNStrategy, tiesStrategy: org.hipparchus.stat.ranking.TiesStrategy): ...
    def mannWhitneyU(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the ` Mann-Whitney U statistic <http://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U>` comparing means for two independent samples possibly of different lengths.
        
        This statistic can be used to perform a Mann-Whitney U test evaluating the null hypothesis that the two independent samples have equal mean.
        
        Let X :sub:`i` denote the i'th individual of the first sample and Y :sub:`j` the j'th individual in the second sample. Note that the samples can have different lengths.
        
        Preconditions:
        
          - All observations in the two samples are independent.
          - The observations are at least ordinal (continuous are also ordinal).
        
        
        Parameters:
            x (double[]): the first sample
            y (double[]): the second sample
        
        Returns:
            Mann-Whitney U statistic (minimum of U :sup:`x` and U :sup:`y` )
        
        Raises:
            hipparchus: if x or y are null.
            hipparchus: if x or y are zero-length.
        
        
        """
        ...
    @typing.overload
    def mannWhitneyUTest(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def mannWhitneyUTest(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], exact: bool) -> float: ...

class OneWayAnova:
    """
    Implements one-way ANOVA (analysis of variance) statistics.
    
    Tests for differences between two or more categories of univariate data (for example, the body mass index of accountants, lawyers, doctors and computer programmers). When two categories are given, this is equivalent to the TTest.
    
    Uses the hipparchus to estimate exact p-values.
    
    This implementation is based on a description at `One way Anova (dead link) <http://faculty.vassar.edu/lowry/ch13pt1.html>`
    
     Abbreviations: bg = between groups, wg = within groups, ss = sum squared deviations
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def anovaFValue(self, categoryData: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float:
        """
        Computes the ANOVA F-value for a collection of double[] arrays.
        
        Preconditions:
        
          - The categoryData Collection must contain double[] arrays.
          - There must be at least two double[] arrays in the categoryData collection and each of these arrays must
            contain at least two values.
        
        This implementation computes the F statistic using the definitional formula
        
           F = msbg/mswg
        
        where
        
          msbg = between group mean square mswg = within group mean square
        
        are as defined ` here <http://faculty.vassar.edu/lowry/ch13pt1.html>`
        
        Parameters:
            categoryData (Collection<double[]> categoryData): Collection of double[] arrays each containing data for one category
        
        Returns:
            Fvalue
        
        Raises:
            hipparchus: if categoryData is null
            hipparchus: if the length of the categoryData array is less than 2 or a contained double[] array does not have at
                least two values
        
        
        """
        ...
    @typing.overload
    def anovaPValue(self, categoryData: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]]) -> float: ...
    @typing.overload
    def anovaPValue(self, categoryData: typing.Union[java.util.Collection[org.hipparchus.stat.descriptive.StreamingStatistics], typing.Sequence[org.hipparchus.stat.descriptive.StreamingStatistics], typing.Set[org.hipparchus.stat.descriptive.StreamingStatistics]], allowOneElementData: bool) -> float: ...
    def anovaTest(self, categoryData: typing.Union[java.util.Collection[typing.Union[typing.List[float], jpype.JArray]], typing.Sequence[typing.Union[typing.List[float], jpype.JArray]], typing.Set[typing.Union[typing.List[float], jpype.JArray]]], alpha: float) -> bool:
        """
        Performs an ANOVA test, evaluating the null hypothesis that there is no difference among the means of the data categories.
        
        Preconditions:
        
          - The categoryData Collection must contain double[] arrays.
          - There must be at least two double[] arrays in the categoryData collection and each of these arrays must
            contain at least two values.
          - alpha must be strictly greater than 0 and less than or equal to 0.5.
        
        This implementation uses the hipparchus to estimate the exact p-value, using the formula
        
           p = 1 - cumulativeProbability(F)
        
        where F is the F value and cumulativeProbability is the Hipparchus implementation of the F distribution.
        
        True is returned iff the estimated p-value is less than alpha.
        
        Parameters:
            categoryData (Collection<double[]> categoryData): Collection of double[] arrays each containing data for one category
            alpha (double): significance level of the test
        
        Returns:
            true if the null hypothesis can be rejected with confidence 1 - alpha
        
        Raises:
            hipparchus: if categoryData is null
            hipparchus: if the length of the categoryData array is less than 2 or a contained double[] array does not have at
                least two values
            hipparchus: if alpha is not in the range (0, 0.5]
            hipparchus: if the p-value can not be computed due to a convergence error
            hipparchus: if the maximum number of iterations is exceeded
        
        
        """
        ...

class TTest:
    """
    An implementation for Student's t-tests.
    
    Tests can be:
    
      - One-sample or two-sample
      - One-sided or two-sided
      - Paired or unpaired (for two-sample tests)
      - Homoscedastic (equal variance assumption) or heteroscedastic (for two sample tests)
      - Fixed significance level (boolean-valued) or returning p-values.
    
    Test statistics are available for all tests. Methods including "Test" in in their names perform tests, all other methods return t-statistics. Among the "Test" methods, double-valued methods return p-values; boolean-valued methods perform fixed significance level tests. Significance levels are always specified as numbers between 0 and 0.5 (e.g. tests at the 95% level use alpha=0).
    
    Input to tests can be either double[] arrays or StatisticalSummary instances.
    
    Uses Hipparchus hipparchus implementation to estimate exact p-values.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
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
    def homoscedasticTTest(self, sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    def homoscedasticTTest(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def homoscedasticTTest(self, statisticalSummary: org.hipparchus.stat.descriptive.StatisticalSummary, statisticalSummary2: org.hipparchus.stat.descriptive.StatisticalSummary) -> float: ...
    def pairedT(self, sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes a paired, 2-sample t-statistic based on the data in the input arrays. The t-statistic returned is equivalent to what would be returned by computing the one-sample t-statistic t, with mu = 0 and the sample array consisting of the (signed) differences between corresponding entries in sample1 and sample2
        
        * Preconditions:
        
          - The input arrays must have the same length and their common length must be at least 2.
        
        
        Parameters:
            sample1 (double[]): array of sample data values
            sample2 (double[]): array of sample data values
        
        Returns:
            t statistic
        
        Raises:
            hipparchus: if the arrays are null
            hipparchus: if the arrays are empty
            hipparchus: if the length of the arrays is not equal
            hipparchus: if the length of the arrays is < 2
        
        
        """
        ...
    @typing.overload
    def pairedTTest(self, sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray], alpha: float) -> bool: ...
    @typing.overload
    def pairedTTest(self, sample1: typing.Union[typing.List[float], jpype.JArray], sample2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
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
    An implementation of the Wilcoxon signed-rank test. This implementation currently handles only paired (equal length) samples and discards tied pairs from the analysis. The latter behavior differs from the R implementation of wilcox.test and corresponds to the "wilcox" zero_method configurable in scipy.stats.wilcoxon.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, nanStrategy: org.hipparchus.stat.ranking.NaNStrategy, tiesStrategy: org.hipparchus.stat.ranking.TiesStrategy): ...
    def wilcoxonSignedRank(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the ` Wilcoxon signed ranked statistic <http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test>` comparing means for two related samples or repeated measurements on a single sample.
        
        This statistic can be used to perform a Wilcoxon signed ranked test evaluating the null hypothesis that the two related samples or repeated measurements on a single sample have equal mean.
        
        Let X :sub:`i` denote the i'th individual of the first sample and Y :sub:`i` the related i'th individual in the second sample. Let Z :sub:`i` = Y :sub:`i` - X :sub:`i` .
        
        * Preconditions:
        
          - The differences Z :sub:`i` must be independent.
          - Each Z :sub:`i` comes from a continuous population (they must be identical) and is symmetric about a common median.
          - The values that X :sub:`i` and Y :sub:`i` represent are ordered, so the comparisons greater than, less than, and equal
            to are meaningful.
        
        
        Parameters:
            x (double[]): the first sample
            y (double[]): the second sample
        
        Returns:
            statistic (the larger of W+ and W-)
        
        Raises:
            hipparchus: if x or y are null.
            hipparchus: if x or y are zero-length.
            hipparchus: if x and y do not have the same length.
        
        
        """
        ...
    def wilcoxonSignedRankTest(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], exactPValue: bool) -> float:
        """
        Returns the observed significance level, or ` p-value <http://www.cas.lancs.ac.uk/glossary_v1.1/hyptest.html#pvalue>`, associated with a ` Wilcoxon signed ranked statistic <http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test>` comparing mean for two related samples or repeated measurements on a single sample.
        
        Let X :sub:`i` denote the i'th individual of the first sample and Y :sub:`i` the related i'th individual in the second sample. Let Z :sub:`i` = Y :sub:`i` - X :sub:`i` .
        
        Preconditions:
        
          - The differences Z :sub:`i` must be independent.
          - Each Z :sub:`i` comes from a continuous population (they must be identical) and is symmetric about a common median.
          - The values that X :sub:`i` and Y :sub:`i` represent are ordered, so the comparisons greater than, less than, and equal
            to are meaningful.
        
        Implementation notes:
        
          - Tied pairs are discarded from the data.
          - When exactPValue is false, the normal approximation is used to estimate the p-value including a continuity
            correction factor. wilcoxonSignedRankTest(x, y, true) should give the same results as sided", mu = 0, paired = TRUE, exact = FALSE, correct = TRUE) in R (as long as there are no tied
            pairs in the data).
        
        
        Parameters:
            x (double[]): the first sample
            y (double[]): the second sample
            exactPValue (boolean): if the exact p-value is wanted (only works for x.length <= 30, if true and x.length > 30, MathIllegalArgumentException
                is thrown)
        
        Returns:
            p-value
        
        Raises:
            hipparchus: if x or y are null.
            hipparchus: if x or y are zero-length or for all i, x[i] == y[i]
            hipparchus: if x and y do not have the same length.
            hipparchus: if exactPValue is true and length > 30
            hipparchus: if the p-value can not be computed due to a convergence error
            hipparchus: if the maximum number of iterations is exceeded
        
        
        """
        ...


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
