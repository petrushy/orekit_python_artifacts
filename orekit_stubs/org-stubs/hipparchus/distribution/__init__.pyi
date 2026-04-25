
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import jpype
import org.hipparchus.distribution.continuous
import org.hipparchus.distribution.discrete
import org.hipparchus.distribution.multivariate
import org.hipparchus.util
import typing



_EnumeratedDistribution__T = typing.TypeVar('_EnumeratedDistribution__T')  # <T>
class EnumeratedDistribution(java.io.Serializable, typing.Generic[_EnumeratedDistribution__T]):
    """
    implements Serializable
    
    A generic implementation of a ` discrete probability distribution (Wikipedia) <http://en.wikipedia.org/wiki/Probability_distribution#Discrete_probability_distribution>` over a finite sample space, based on an enumerated list of <value, probability> pairs.
    
    Input probabilities must all be non-negative, but zero values are allowed and their sum does not have to equal one. Constructors will normalize input probabilities to make them sum to one.
    
    The list of <value, probability> pairs does not, strictly speaking, have to be a function and it can contain null values. The pmf created by the constructor will combine probabilities of equal values and will treat null values as equal.
    
    For example, if the list of pairs <"dog", 0.2>, <null, 0.1>, <"pig", 0.2>, <"dog", 0.1>, <null, 0.4> is provided to the constructor, the resulting pmf will assign mass of 0.5 to null, 0.3 to "dog" and 0.2 to null.
    
          - serialized
    """
    def __init__(self, pmf: java.util.List[org.hipparchus.util.Pair[_EnumeratedDistribution__T, float]]):
        """
        Create an enumerated distribution using the given probability mass function enumeration.
        
        Parameters:
            pmf (List<Pair<EnumeratedDistribution,Double>>): probability mass function enumerated as a list of <T, probability> pairs.
        
        Raises:
            MathIllegalArgumentException: of weights includes negative, NaN or infinite values or only 0's
        
        
        """
        ...
    @staticmethod
    def checkAndNormalize(weights: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Checks to make sure that weights is neither null nor empty and contains only non-negative, finite, non-NaN values and if necessary normalizes it to sum to 1.
        
        Parameters:
            weights (double[]): input array to be used as the basis for the values of a PMF
        
        Returns:
            a possibly rescaled copy of the array that sums to 1 and contains only valid probability values
        
        Raises:
            MathIllegalArgumentException: of weights is null or empty or includes negative, NaN or infinite values or only 0's
        
        
        """
        ...
    def getPmf(self) -> java.util.List[org.hipparchus.util.Pair[_EnumeratedDistribution__T, float]]:
        """
        Return the probability mass function as a list of (value, probability) pairs.
        
        Note that if duplicate and / or null values were provided to the constructor when creating this EnumeratedDistribution, the returned list will contain these values. If duplicates values exist, what is returned will not represent a pmf (i.e., it is up to the caller to consolidate duplicate mass points).
        
        Returns:
            the probability mass function.
        
        
        """
        ...
    def probability(self, x: _EnumeratedDistribution__T) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Note that if x1 and x2 satisfy equals(x2), or both are null, then probability(x1) = probability(x2).
        
        Parameters:
            x (EnumeratedDistribution): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class IntegerDistribution:
    """
    Interface for discrete distributions.
    """
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
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY or NaN if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in Z | P(X <= x) > 0}.
        
        Returns:
            lower bound of the support (MIN_VALUE for negative infinity)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}.
        
        Returns:
            upper bound of the support (MAX_VALUE for positive infinity)
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> int:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in Z | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in Z | P(X<=x) > 0} for p = 0.
        
        If the result exceeds the range of the data type int, then MIN_VALUE or MAX_VALUE is returned.
        
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
        Use this method to get information about whether the support is connected, i.e. whether all integers between the lower and upper bound of the support are included in the support.
        
        Returns:
            whether the support is connected or not
        
        
        """
        ...
    def logProbability(self, x: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns log(P(X = x)), where log is the natural logarithm. In other words, this method represents the logarithm of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of probability.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the logarithm of the value of the probability mass function at x
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (int): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        double probability(int x0, int x1) throws MathIllegalArgumentException
        
        For a random variable X whose values are distributed according to this distribution, this method returns P(x0 < X <= x1).
        
        Parameters:
            x0 (int): the exclusive lower bound
            x1 (int): the inclusive upper bound
        
        Returns:
            the probability that a random variable with this distribution will take a value between x0 and x1,
            excluding the lower and including the upper endpoint
        
        Raises:
            MathIllegalArgumentException: if x0 > x1
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...

class MultivariateRealDistribution:
    """
    Base interface for multivariate continuous distributions.
    
    This is based largely on the RealDistribution interface, but cumulative distribution functions are not required because they are often quite difficult to compute for multivariate distributions.
    """
    def density(self, x: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Returns the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulative distribution function. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient.
        
        Parameters:
            x (double[]): Point at which the PDF is evaluated.
        
        Returns:
            the value of the probability density function at point x.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Gets the number of random variables of the distribution. It is the size of the array returned by the sample method.
        
        Returns:
            the number of variables.
        
        
        """
        ...
    def reseedRandomGenerator(self, seed: int) -> None:
        """
        Reseeds the random generator used to generate samples.
        
        Parameters:
            seed (long): Seed with which to initialize the random number generator.
        
        
        """
        ...
    @typing.overload
    def sample(self) -> typing.MutableSequence[float]:
        """
        Generates a random value vector sampled from this distribution.
        
        Returns:
            a random value vector.
        
        double[][] sample(int sampleSize) throws MathIllegalArgumentException
        
        Generates a list of a random value vectors from the distribution.
        
        Parameters:
            sampleSize (int): the number of random vectors to generate.
        
        Returns:
            an array representing the random samples.
        
        Raises:
            MathIllegalArgumentException: if sampleSize is not positive.
        
              - sample
        
        
        
        """
        ...
    @typing.overload
    def sample(self, int: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

class RealDistribution:
    """
    Base interface for continuous distributions.
    """
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        Parameters:
            x (double): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def density(self, x: float) -> float:
        """
        Returns the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient.
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the value of the probability density function at point x
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}.
        
        Returns:
            lower bound of the support (might be NEGATIVE_INFINITY)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}.
        
        Returns:
            upper bound of the support (might be POSITIVE_INFINITY)
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        
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
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support.
        
        Returns:
            whether the support is connected or not
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...
    def probability(self, x0: float, x1: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(x0 < X <= x1).
        
        Parameters:
            x0 (double): the exclusive lower bound
            x1 (double): the inclusive upper bound
        
        Returns:
            the probability that a random variable with this distribution takes a value between x0 and x1, excluding
            the lower and including the upper endpoint
        
        Raises:
            MathIllegalArgumentException: if x0 > x1
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.distribution")``.

    EnumeratedDistribution: typing.Type[EnumeratedDistribution]
    IntegerDistribution: typing.Type[IntegerDistribution]
    MultivariateRealDistribution: typing.Type[MultivariateRealDistribution]
    RealDistribution: typing.Type[RealDistribution]
    continuous: org.hipparchus.distribution.continuous.__module_protocol__
    discrete: org.hipparchus.distribution.discrete.__module_protocol__
    multivariate: org.hipparchus.distribution.multivariate.__module_protocol__
