
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import jpype
import org.hipparchus.distribution
import org.hipparchus.util
import typing



class AbstractIntegerDistribution(org.hipparchus.distribution.IntegerDistribution, java.io.Serializable):
    """
    Base class for integer-valued discrete distributions.
    
    Default implementations are provided for some of the methods that do not vary from distribution to distribution.
    
    Also see:
        serialized
    """
    def inverseCumulativeProbability(self, p: float) -> int:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in Z | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in Z | P(X<=x) > 0} for p = 0.
        
        If the result exceeds the range of the data type int, then MIN_VALUE or MAX_VALUE is returned. The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1, and
          - solveInverseCumulativeProbability for 0
            < p < 1.
        
        Specified by: inverseCumulativeProbability in interface IntegerDistribution
        
        Parameters:
            p (double): the cumulative probability
        
        Returns:
            the smallest p-quantile of this distribution (largest 0-quantile for p = 0)
        
        Raises:
            MathIllegalArgumentException: if p < 0 or p > 1
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        The default implementation simply computes the logarithm of probability(x).
        
        Specified by: logProbability in interface IntegerDistribution
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, x0: int, x1: int) -> float: ...

class BinomialDistribution(AbstractIntegerDistribution):
    """
    Implementation of the binomial distribution.
    
    Also see:
        `Binomial distribution (Wikipedia) <http://en.wikipedia.org/wiki/Binomial_distribution>`, `Binomial Distribution
        (MathWorld) <http://mathworld.wolfram.com/BinomialDistribution.html>`, serialized
    """
    def __init__(self, trials: int, p: float):
        """
        Create a binomial distribution with the given number of trials and probability of success.
        
        Parameters:
            trials (int): Number of trials.
            p (double): Probability of success.
        
        Raises:
            MathIllegalArgumentException: if trials < 0.
            MathIllegalArgumentException: if p < 0 or p > 1.
        
        
        """
        ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getNumberOfTrials(self) -> int:
        """
        Access the number of trials for this distribution.
        
        Returns:
            the number of trials.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For n trials and probability parameter p, the mean is n * p.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For n trials and probability parameter p, the variance is n * p * (1 - p).
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getProbabilityOfSuccess(self) -> float:
        """
        Access the probability of success for this distribution.
        
        Returns:
            the probability of success.
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. The lower bound of the support is always 0 except for the probability parameter p = 1.
        
        Returns:
            lower bound of the support (0 or the number of trials)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is the number of trials except for the probability parameter p = 0.
        
        Returns:
            upper bound of the support (number of trials or 0)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        The default implementation simply computes the logarithm of probability(x).
        
        Specified by: logProbability in interface IntegerDistribution
        
        Overrides: logProbability in class AbstractIntegerDistribution
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class EnumeratedIntegerDistribution(AbstractIntegerDistribution):
    """
    Implementation of an integer-valued EnumeratedDistribution.
    
    Values with zero-probability are allowed but they do not extend the support.
    
    Duplicate values are allowed. Probabilities of duplicate values are combined when computing cumulative probabilities and statistics.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, data: typing.Union[typing.List[int], jpype.JArray]): ...
    @typing.overload
    def __init__(self, singletons: typing.Union[typing.List[int], jpype.JArray], probabilities: typing.Union[typing.List[float], jpype.JArray]): ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution.
        
        Returns:
            sum(singletons[i] * probabilities[i])
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution.
        
        Returns:
            sum((singletons[i] - mean) ^ 2 * probabilities[i])
        
        
        """
        ...
    def getPmf(self) -> java.util.List[org.hipparchus.util.Pair[int, float]]:
        """
        Return the probability mass function as a list of (value, probability) pairs.
        
        Returns:
            the probability mass function.
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. Returns the lowest value with non-zero probability.
        
        Returns:
            the lowest value with non-zero probability.
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. Returns the highest value with non-zero probability.
        
        Returns:
            the highest value with non-zero probability.
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class GeometricDistribution(AbstractIntegerDistribution):
    """
    Implementation of the geometric distribution.
    
    Also see:
        `Geometric distribution (Wikipedia) <http://en.wikipedia.org/wiki/Geometric_distribution>`, `Geometric Distribution
        (MathWorld) <http://mathworld.wolfram.com/GeometricDistribution.html>`, serialized
    """
    def __init__(self, p: float):
        """
        Create a geometric distribution with the given probability of success.
        
        Parameters:
            p (double): probability of success.
        
        Raises:
            MathIllegalArgumentException: if p <= 0 or p > 1.
        
        
        """
        ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For probability parameter p, the mean is (1 - p) / p.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For probability parameter p, the variance is (1 - p) / (p * p).
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getProbabilityOfSuccess(self) -> float:
        """
        Access the probability of success for this distribution.
        
        Returns:
            the probability of success.
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. The lower bound of the support is always 0.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is infinite (which we approximate as MAX_VALUE).
        
        Returns:
            upper bound of the support (always Integer.MAX_VALUE)
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> int:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in Z | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in Z | P(X<=x) > 0} for p = 0.
        
        If the result exceeds the range of the data type int, then MIN_VALUE or MAX_VALUE is returned. The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1, and
          - solveInverseCumulativeProbability for 0
            < p < 1.
        
        Specified by: inverseCumulativeProbability in interface IntegerDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractIntegerDistribution
        
        Parameters:
            p (double): the cumulative probability
        
        Returns:
            the smallest p-quantile of this distribution (largest 0-quantile for p = 0)
        
        Raises:
            MathIllegalArgumentException: if p < 0 or p > 1
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        The default implementation simply computes the logarithm of probability(x).
        
        Specified by: logProbability in interface IntegerDistribution
        
        Overrides: logProbability in class AbstractIntegerDistribution
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class HypergeometricDistribution(AbstractIntegerDistribution):
    """
    Implementation of the hypergeometric distribution.
    
    Also see:
        `Hypergeometric distribution (Wikipedia) <http://en.wikipedia.org/wiki/Hypergeometric_distribution>`, `Hypergeometric
        distribution (MathWorld) <http://mathworld.wolfram.com/HypergeometricDistribution.html>`, serialized
    """
    def __init__(self, populationSize: int, numberOfSuccesses: int, sampleSize: int):
        """
        Construct a new hypergeometric distribution with the specified population size, number of successes in the population, and sample size.
        
        Parameters:
            populationSize (int): Population size.
            numberOfSuccesses (int): Number of successes in the population.
            sampleSize (int): Sample size.
        
        Raises:
            MathIllegalArgumentException: if numberOfSuccesses < 0.
            MathIllegalArgumentException: if populationSize <= 0.
            MathIllegalArgumentException: if numberOfSuccesses > populationSize, or sampleSize > populationSize.
        
        
        """
        ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getNumberOfSuccesses(self) -> int:
        """
        Access the number of successes.
        
        Returns:
            the number of successes.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For population size N, number of successes m, and sample size n, the mean is n * m / N.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For population size N, number of successes m, and sample size n, the variance is [n * m * (N - n) * (N - m)] / [N^2 * (N - 1)].
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getPopulationSize(self) -> int:
        """
        Access the population size.
        
        Returns:
            the population size.
        
        
        """
        ...
    def getSampleSize(self) -> int:
        """
        Access the sample size.
        
        Returns:
            the sample size.
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. For population size N, number of successes m, and sample size n, the lower bound of the support is max(0, n + m - N).
        
        Returns:
            lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. For number of successes m and sample size n, the upper bound of the support is min(m, n).
        
        Returns:
            upper bound of the support
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        The default implementation simply computes the logarithm of probability(x).
        
        Specified by: logProbability in interface IntegerDistribution
        
        Overrides: logProbability in class AbstractIntegerDistribution
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...
    def upperCumulativeProbability(self, x: int) -> float:
        """
        For this distribution, X, this method returns P(X >= x).
        
        Parameters:
            x (int): Value at which the CDF is evaluated.
        
        Returns:
            the upper tail CDF for this distribution.
        
        
        """
        ...

class PascalDistribution(AbstractIntegerDistribution):
    """
    Implementation of the Pascal distribution.
    
    The Pascal distribution is a special case of the Negative Binomial distribution where the number of successes parameter is an integer.
    
    There are various ways to express the probability mass and distribution functions for the Pascal distribution. The present implementation represents the distribution of the number of failures before r successes occur. This is the convention adopted in e.g. `MathWorld <http://mathworld.wolfram.com/NegativeBinomialDistribution.html>`, but not in `Wikipedia <http://en.wikipedia.org/wiki/Negative_binomial_distribution>`.
    
    For a random variable X whose values are distributed according to this distribution, the probability mass function is given by
    
    P(X = k) = C(k + r - 1, r - 1) * p^r * (1 - p)^k,
    
    where r is the number of successes, p is the probability of success, and X is the total number of failures. C(n, k) is the binomial coefficient (n choose k). The mean and variance of X are
    
    E(X) = (1 - p) * r / p, var(X) = (1 - p) * r / p^2
    
    Finally, the cumulative distribution function is given by
    
    P(X <= k) = I(p, r, k + 1), where I is the regularized incomplete Beta function.
    
    Also see:
        ` Negative binomial distribution (Wikipedia) <http://en.wikipedia.org/wiki/Negative_binomial_distribution>`, ` Negative
        binomial distribution (MathWorld) <http://mathworld.wolfram.com/NegativeBinomialDistribution.html>`, serialized
    """
    def __init__(self, r: int, p: float):
        """
        Create a Pascal distribution with the given number of successes and probability of success.
        
        Parameters:
            r (int): Number of successes.
            p (double): Probability of success.
        
        Raises:
            MathIllegalArgumentException: if the number of successes is not positive
            MathIllegalArgumentException: if the probability of success is not in the range [0, 1].
        
        
        """
        ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getNumberOfSuccesses(self) -> int:
        """
        Access the number of successes for this distribution.
        
        Returns:
            the number of successes.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For number of successes r and probability of success p, the mean is r * (1 - p) / p.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For number of successes r and probability of success p, the variance is r * (1 - p) / p^2.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getProbabilityOfSuccess(self) -> float:
        """
        Access the probability of success for this distribution.
        
        Returns:
            the probability of success.
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the parameters.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters. Positive infinity is symbolized by MAX_VALUE.
        
        Returns:
            upper bound of the support (always MAX_VALUE for positive infinity)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        The default implementation simply computes the logarithm of probability(x).
        
        Specified by: logProbability in interface IntegerDistribution
        
        Overrides: logProbability in class AbstractIntegerDistribution
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class PoissonDistribution(AbstractIntegerDistribution):
    """
    Implementation of the Poisson distribution.
    
    Also see:
        `Poisson distribution (Wikipedia) <http://en.wikipedia.org/wiki/Poisson_distribution>`, `Poisson distribution
        (MathWorld) <http://mathworld.wolfram.com/PoissonDistribution.html>`, serialized
    """
    DEFAULT_MAX_ITERATIONS: typing.ClassVar[int] = ...
    """
    Default maximum number of iterations for cumulative probability calculations.
    
    Also see:
        constant
    
    
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    Default convergence criterion.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, p: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, p: float, epsilon: float, maxIterations: int): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getMean(self) -> float:
        """
        Get the mean for the distribution.
        
        Returns:
            the mean for the distribution.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For mean parameter p, the mean is p.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For mean parameter p, the variance is p.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the mean parameter.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is positive infinity, regardless of the parameter values. There is no integer infinity, so this method returns MAX_VALUE.
        
        Returns:
            upper bound of the support (always MAX_VALUE for positive infinity)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        The default implementation simply computes the logarithm of probability(x).
        
        Specified by: logProbability in interface IntegerDistribution
        
        Overrides: logProbability in class AbstractIntegerDistribution
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    def normalApproximateProbability(self, x: int) -> float:
        """
        Calculates the Poisson distribution function using a normal approximation. The N(mean, sqrt(mean)) distribution is used to approximate the Poisson distribution. The computation uses "half-correction" (evaluating the normal distribution function at x + 0).
        
        Parameters:
            x (int): Upper bound, inclusive.
        
        Returns:
            the distribution function value calculated using a normal approximation.
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class UniformIntegerDistribution(AbstractIntegerDistribution):
    """
    Implementation of the uniform integer distribution.
    
    Also see:
        ` Uniform distribution (discrete), at Wikipedia <http://en.wikipedia.org/wiki/Uniform_distribution_(discrete)>`,
        serialized
    """
    def __init__(self, lower: int, upper: int):
        """
        Creates a new uniform integer distribution using the given lower and upper bounds (both inclusive).
        
        Parameters:
            lower (int): Lower bound (inclusive) of this distribution.
            upper (int): Upper bound (inclusive) of this distribution.
        
        Raises:
            MathIllegalArgumentException: if lower >= upper.
        
        
        """
        ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For lower bound lower and upper bound upper, the mean is 5 * (lower + upper).
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For lower bound lower and upper bound upper, and n = upper - lower + 1, the variance is (n^2 - 1) / 12.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. The lower bound of the support is equal to the lower bound parameter of the distribution.
        
        Returns:
            lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is equal to the upper bound parameter of the distribution.
        
        Returns:
            upper bound of the support
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class ZipfDistribution(AbstractIntegerDistribution):
    """
    Implementation of the Zipf distribution.
    
    Parameters: For a random variable X whose values are distributed according to this distribution, the probability mass function is given by
    
       P(X = k) = H(N,s) * 1 / k^s    for k = 1,2...,N.
    
    H(N,s) is the normalizing constant which corresponds to the generalized harmonic number of order N of s.
    
      - N is the number of elements
      - s is the exponent
    
    
    Also see:
        Zipf's_law,
        Harmonic_number,
        serialized
    """
    def __init__(self, numberOfElements: int, exponent: float):
        """
        Create a new Zipf distribution with the given number of elements and exponent.
        
        Parameters:
            numberOfElements (int): Number of elements.
            exponent (double): Exponent.
        
        Raises:
            MathIllegalArgumentException: if numberOfElements <= 0 or exponent <= 0.
        
        
        """
        ...
    def cumulativeProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (int): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def getExponent(self) -> float:
        """
        Get the exponent characterizing the distribution.
        
        Returns:
            the exponent
        
        
        """
        ...
    def getNumberOfElements(self) -> int:
        """
        Get the number of elements (e.g. corpus size) for the distribution.
        
        Returns:
            the number of elements
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For number of elements N and exponent s, the mean is Hs1 / Hs, where
        
          - Hs1 = generalizedHarmonic(N, s - 1),
          - Hs = generalizedHarmonic(N, s).
        
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For number of elements N and exponent s, the mean is (Hs2 / Hs) - (Hs1^2 / Hs^2), where
        
          - Hs2 = generalizedHarmonic(N, s - 2),
          - Hs1 = generalizedHarmonic(N, s - 1),
          - Hs = generalizedHarmonic(N, s).
        
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}. The lower bound of the support is always 1 no matter the parameters.
        
        Returns:
            lower bound of the support (always 1)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is the number of elements.
        
        Returns:
            upper bound of the support
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        The default implementation simply computes the logarithm of probability(x).
        
        Specified by: logProbability in interface IntegerDistribution
        
        Overrides: logProbability in class AbstractIntegerDistribution
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...


class __module_protocol__(Protocol):
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
