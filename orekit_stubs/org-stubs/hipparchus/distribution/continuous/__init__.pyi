
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



class AbstractRealDistribution(org.hipparchus.distribution.RealDistribution, java.io.Serializable):
    """
    implements RealDistribution, Serializable
    
    Base class for probability distributions on the reals.
    
    Default implementations are provided for some of the methods that do not vary from distribution to distribution.
    
          - serialized
    """
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Parameters:
            p (double): the cumulative probability
        
        Returns:
            the smallest p-quantile of this distribution (largest 0-quantile for p = 0)
        
        Raises:
            MathIllegalArgumentException: if p < 0 or p > 1
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...
    def probability(self, x0: float, x1: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(x0 < X <= x1).
        
        Specified by: probability in interface RealDistribution
        
        Parameters:
            x0 (double): Lower bound (excluded).
            x1 (double): Upper bound (included).
        
        Returns:
            the probability that a random variable with this distribution takes a value between x0 and x1, excluding
            the lower and including the upper endpoint.
        
        Raises:
            MathIllegalArgumentException: if x0 > x1. The default implementation uses the identity P(x0 < X <= x1) = P(X <= x1) - P(X <= x0)
        
        
        """
        ...

class BetaDistribution(AbstractRealDistribution):
    """
    Implements the Beta distribution.
    
          - `Beta distribution <http://en.wikipedia.org/wiki/Beta_distribution>`
          - serialized
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
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
    def getAlpha(self) -> float:
        """
        Access the first shape parameter, alpha.
        
        Returns:
            the first shape parameter.
        
        
        """
        ...
    def getBeta(self) -> float:
        """
        Access the second shape parameter, beta.
        
        Returns:
            the second shape parameter.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For first shape parameter alpha and second shape parameter beta, the mean is alpha / (alpha + beta).
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For first shape parameter alpha and second shape parameter beta, the variance is (alpha * beta) / [(alpha + beta)^2 * (alpha + beta + 1)].
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the parameters.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always 1 no matter the parameters.
        
        Returns:
            upper bound of the support (always 1)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class CauchyDistribution(AbstractRealDistribution):
    """
    Implementation of the Cauchy distribution.
    
          - `Cauchy distribution (Wikipedia) <http://en.wikipedia.org/wiki/Cauchy_distribution>`
          - `Cauchy Distribution (MathWorld) <http://mathworld.wolfram.com/CauchyDistribution.html>`
          - serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
    def getMedian(self) -> float:
        """
        Access the median.
        
        Returns:
            the median for this distribution.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. The mean is always undefined no matter the parameters.
        
        Returns:
            mean (always Double.NaN)
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. The variance is always undefined no matter the parameters.
        
        Returns:
            variance (always Double.NaN)
        
        
        """
        ...
    def getScale(self) -> float:
        """
        Access the scale parameter.
        
        Returns:
            the scale parameter for this distribution.
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always negative infinity no matter the parameters.
        
        Returns:
            lower bound of the support (always Double.NEGATIVE_INFINITY)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Returns NEGATIVE_INFINITY when p == 0 and POSITIVE_INFINITY when p == 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...

class ChiSquaredDistribution(AbstractRealDistribution):
    """
    Implementation of the chi-squared distribution.
    
          - `Chi-squared distribution (Wikipedia) <http://en.wikipedia.org/wiki/Chi-squared_distribution>`
          - `Chi-squared Distribution (MathWorld) <http://mathworld.wolfram.com/Chi-SquaredDistribution.html>`
          - serialized
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
    def getDegreesOfFreedom(self) -> float:
        """
        Access the number of degrees of freedom.
        
        Returns:
            the degrees of freedom.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For k degrees of freedom, the mean is k.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution.
        
        Returns:
            2 * k, where k is the number of degrees of freedom.
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the degrees of freedom.
        
        Returns:
            zero.
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the degrees of freedom.
        
        Returns:
            POSITIVE_INFINITY.
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class ConstantRealDistribution(AbstractRealDistribution):
    """
    Implementation of the constant real distribution.
    
          - serialized
    """
    def __init__(self, value: float):
        """
        Create a constant real distribution with the given value.
        
        Parameters:
            value (double): the constant value of this distribution
        
        
        """
        ...
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
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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

class EnumeratedRealDistribution(AbstractRealDistribution):
    """
    Implementation of a real-valued EnumeratedDistribution.
    
    Values with zero-probability are allowed but they do not extend the support.
    
    Duplicate values are allowed. Probabilities of duplicate values are combined when computing cumulative probabilities and statistics.
    
          - serialized
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
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
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Parameters:
            x (double): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at point x
        
        
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
    def getPmf(self) -> java.util.List[org.hipparchus.util.Pair[float, float]]:
        """
        Return the probability mass function as a list of (value, probability) pairs.
        
        Returns:
            the probability mass function.
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. Returns the lowest value with non-zero probability.
        
        Returns:
            the lowest value with non-zero probability.
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. Returns the highest value with non-zero probability.
        
        Returns:
            the highest value with non-zero probability.
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    @typing.overload
    def probability(self, double: float, double2: float) -> float: ...
    @typing.overload
    def probability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X = x). In other words, this method represents the probability mass function (PMF) for the distribution.
        
        Note that if x1 and x2 satisfy equals(x2), or both are null, then probability(x1) = probability(x2).
        
        Parameters:
            x (double): the point at which the PMF is evaluated
        
        Returns:
            the value of the probability mass function at x
        
        
        """
        ...

class ExponentialDistribution(AbstractRealDistribution):
    """
    Implementation of the exponential distribution.
    
          - `Exponential distribution (Wikipedia) <http://en.wikipedia.org/wiki/Exponential_distribution>`
          - `Exponential distribution (MathWorld) <http://mathworld.wolfram.com/ExponentialDistribution.html>`
          - serialized
    """
    def __init__(self, mean: float):
        """
        Create an exponential distribution with the given mean.
        
        Parameters:
            mean (double): Mean of this distribution.
        
        Raises:
            MathIllegalArgumentException: if mean <= 0.
        
        
        """
        ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution. The implementation of this method is based on:
        
          - ` Exponential Distribution <http://mathworld.wolfram.com/ExponentialDistribution.html>`, equation (1).
        
        
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
    def getMean(self) -> float:
        """
        Access the mean.
        
        Returns:
            the mean.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For mean parameter k, the mean is k.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For mean parameter k, the variance is k^2.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the mean parameter.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the mean parameter.
        
        Returns:
            upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Returns  when p= = 0 and POSITIVE_INFINITY when p == 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class FDistribution(AbstractRealDistribution):
    """
    Implementation of the F-distribution.
    
          - `F-distribution (Wikipedia) <http://en.wikipedia.org/wiki/F-distribution>`
          - `F-distribution (MathWorld) <http://mathworld.wolfram.com/F-Distribution.html>`
          - serialized
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution. The implementation of this method is based on
        
          - ` F-Distribution <http://mathworld.wolfram.com/F-Distribution.html>`, equation (4).
        
        
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
    def getDenominatorDegreesOfFreedom(self) -> float:
        """
        Access the denominator degrees of freedom.
        
        Returns:
            the denominator degrees of freedom.
        
        
        """
        ...
    def getNumeratorDegreesOfFreedom(self) -> float:
        """
        Access the numerator degrees of freedom.
        
        Returns:
            the numerator degrees of freedom.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For denominator degrees of freedom parameter b, the mean is
        
          - if b > 2 then b / (b - 2),
          - else undefined (NaN).
        
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For numerator degrees of freedom parameter a and denominator degrees of freedom parameter b, the variance is
        
          - if b > 4 then [2 * b^2 * (a + b - 2)] / [a * (b - 2)^2 * (b - 4)],
          - else undefined (NaN).
        
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the parameters.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class GammaDistribution(AbstractRealDistribution):
    """
    Implementation of the Gamma distribution.
    
          - `Gamma distribution (Wikipedia) <http://en.wikipedia.org/wiki/Gamma_distribution>`
          - `Gamma distribution (MathWorld) <http://mathworld.wolfram.com/GammaDistribution.html>`
          - serialized
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution. The implementation of this method is based on:
        
          - ` Chi-Squared Distribution <http://mathworld.wolfram.com/Chi-SquaredDistribution.html>`, equation (9).
          - Casella, G., & Berger, R. (1990). Statistical Inference. Belmont, CA: Duxbury Press.
        
        
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
        Use this method to get the numerical value of the mean of this distribution. For shape parameter alpha and scale parameter beta, the mean is alpha * beta.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For shape parameter alpha and scale parameter beta, the variance is alpha * beta^2.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getScale(self) -> float:
        """
        Returns the scale parameter of this distribution.
        
        Returns:
            the scale parameter
        
        
        """
        ...
    def getShape(self) -> float:
        """
        Returns the shape parameter of this distribution.
        
        Returns:
            the shape parameter
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the parameters.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class GumbelDistribution(AbstractRealDistribution):
    """
    This class implements the Gumbel distribution.
    
          - `Gumbel Distribution (Wikipedia) <http://en.wikipedia.org/wiki/Gumbel_distribution>`
          - `Gumbel Distribution (Mathworld) <http://mathworld.wolfram.com/GumbelDistribution.html>`
          - serialized
    """
    def __init__(self, mu: float, beta: float):
        """
        Build a new instance.
        
        Parameters:
            mu (double): location parameter
            beta (double): scale parameter (must be positive)
        
        Raises:
            MathIllegalArgumentException: if beta <= 0
        
        
        """
        ...
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
    def getLocation(self) -> float:
        """
        Access the location parameter, mu.
        
        Returns:
            the location parameter.
        
        
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
    def getScale(self) -> float:
        """
        Access the scale parameter, beta.
        
        Returns:
            the scale parameter.
        
        
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
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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

class LaplaceDistribution(AbstractRealDistribution):
    """
    This class implements the Laplace distribution.
    
          - `Laplace distribution (Wikipedia) <http://en.wikipedia.org/wiki/Laplace_distribution>`
          - serialized
    """
    def __init__(self, mu: float, beta: float):
        """
        Build a new instance.
        
        Parameters:
            mu (double): location parameter
            beta (double): scale parameter (must be positive)
        
        Raises:
            MathIllegalArgumentException: if beta <= 0
        
        
        """
        ...
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
    def getLocation(self) -> float:
        """
        Access the location parameter, mu.
        
        Returns:
            the location parameter.
        
        
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
    def getScale(self) -> float:
        """
        Access the scale parameter, beta.
        
        Returns:
            the scale parameter.
        
        
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
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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

class LevyDistribution(AbstractRealDistribution):
    """
    This class implements the ` Lévy distribution <http://en.wikipedia.org/wiki/L%C3%A9vy_distribution>`.
    
          - serialized
    """
    def __init__(self, mu: float, c: float):
        """
        Build a new instance.
        
        Parameters:
            mu (double): location parameter
            c (double): scale parameter
        
        
        """
        ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        From Wikipedia: the cumulative distribution function is
        
         f(x; u, c) = erfc (√ (c / 2 (x - u )))
        
        Parameters:
            x (double): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def density(self, x: float) -> float:
        """
        Returns the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient.
        
        From Wikipedia: The probability density function of the Lévy distribution over the domain is \[ f(x; \mu, c) = \sqrt{\frac{c}{2\pi}} \frac{e^{\frac{-c}{2 (x - \mu)}}}{(x - \mu)^\frac{3}{2}} \]
        
        For this distribution, X, this method returns P(X < x). If x is less than location parameter μ, NaN is returned, as in these cases the distribution is not defined.
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the value of the probability density function at point x
        
        
        """
        ...
    def getLocation(self) -> float:
        """
        Get the location parameter of the distribution.
        
        Returns:
            location parameter of the distribution
        
        
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
    def getScale(self) -> float:
        """
        Get the scale parameter of the distribution.
        
        Returns:
            scale parameter of the distribution
        
        
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
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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
        
        The default implementation simply computes the logarithm of density(x). See documentation of density for computation details.
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class LogNormalDistribution(AbstractRealDistribution):
    """
    Implementation of the log-normal (gaussian) distribution.
    
    Parameters: X is log-normally distributed if its natural logarithm log(X) is normally distributed. The probability distribution function of X is given by (for x > 0)
    
    5 * ((ln(x) - m) / s)^2) / (s * sqrt(2 * pi) * x)
    
      - m is the location parameter: this is the mean of the normally distributed natural logarithm of this
        distribution,
      - s is the shape parameter: this is the standard deviation of the normally distributed natural logarithm of this
        distribution.
    
    
          - ` Log-normal distribution (Wikipedia) <http://en.wikipedia.org/wiki/Log-normal_distribution>`
          - ` Log Normal distribution (MathWorld) <http://mathworld.wolfram.com/LogNormalDistribution.html>`
          - serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution. For location m, and shape s of this distribution, the CDF is given by
        
          -  if x <= 0,
          -  if ln(x) - m < 0 and m - ln(x) > 40 * s, as in these cases the actual value is within
            MIN_VALUE of 0,
          -  if ln(x) - m >= 0 and ln(x) - m > 40 * s, as in these cases the actual value is within
            MIN_VALUE of 1,
          - 5 * erf((ln(x) - m) / (s * sqrt(2)) otherwise.
        
        
        Parameters:
            x (double): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def density(self, x: float) -> float:
        """
        Returns the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. For location m, and shape s of this distribution, the PDF is given by
        
          -  if x <= 0,
          - 5 * ((ln(x) - m) / s)^2) / (s * sqrt(2 * pi) * x) otherwise.
        
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the value of the probability density function at point x
        
        
        """
        ...
    def getLocation(self) -> float:
        """
        Returns the location parameter of this distribution.
        
        Returns:
            the location parameter
        
        Since:
            1.4
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For location m and shape s, the mean is exp(m + s^2 / 2).
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For location m and shape s, the variance is (exp(s^2) - 1) * exp(2 * m + s^2).
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getShape(self) -> float:
        """
        Returns the shape parameter of this distribution.
        
        Returns:
            the shape parameter
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the parameters.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always POSITIVE_INFINITY)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x). See documentation of density for computation details.
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...
    def probability(self, x0: float, x1: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(x0 < X <= x1).
        
        Specified by: probability in interface RealDistribution
        
        Overrides: probability in class AbstractRealDistribution
        
        Parameters:
            x0 (double): Lower bound (excluded).
            x1 (double): Upper bound (included).
        
        Returns:
            the probability that a random variable with this distribution takes a value between x0 and x1, excluding
            the lower and including the upper endpoint.
        
        Raises:
            MathIllegalArgumentException: if x0 > x1. The default implementation uses the identity P(x0 < X <= x1) = P(X <= x1) - P(X <= x0)
        
        
        """
        ...

class LogisticDistribution(AbstractRealDistribution):
    """
    This class implements the Logistic distribution.
    
          - `Logistic Distribution (Wikipedia) <http://en.wikipedia.org/wiki/Logistic_distribution>`
          - `Logistic Distribution (Mathworld) <http://mathworld.wolfram.com/LogisticDistribution.html>`
          - serialized
    """
    def __init__(self, mu: float, s: float):
        """
        Build a new instance.
        
        Parameters:
            mu (double): location parameter
            s (double): scale parameter (must be positive)
        
        Raises:
            MathIllegalArgumentException: if beta <= 0
        
        
        """
        ...
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
    def getLocation(self) -> float:
        """
        Access the location parameter, mu.
        
        Returns:
            the location parameter.
        
        
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
    def getScale(self) -> float:
        """
        Access the scale parameter, s.
        
        Returns:
            the scale parameter.
        
        
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
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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

class NakagamiDistribution(AbstractRealDistribution):
    """
    This class implements the Nakagami distribution.
    
          - `Nakagami Distribution (Wikipedia) <http://en.wikipedia.org/wiki/Nakagami_distribution>`
          - serialized
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
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
    def getScale(self) -> float:
        """
        Access the scale parameter, omega.
        
        Returns:
            the scale parameter.
        
        
        """
        ...
    def getShape(self) -> float:
        """
        Access the shape parameter, mu.
        
        Returns:
            the shape parameter.
        
        
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
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support.
        
        Returns:
            whether the support is connected or not
        
        
        """
        ...

class NormalDistribution(AbstractRealDistribution):
    """
    Implementation of the normal (gaussian) distribution.
    
          - `Normal distribution (Wikipedia) <http://en.wikipedia.org/wiki/Normal_distribution>`
          - `Normal distribution (MathWorld) <http://mathworld.wolfram.com/NormalDistribution.html>`
          - serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution. If x is more than 40 standard deviations from the mean, 0 or 1 is returned, as in these cases the actual value is within MIN_VALUE of 0 or 1.
        
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
    def getMean(self) -> float:
        """
        Access the mean.
        
        Returns:
            the mean for this distribution.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For mean parameter mu, the mean is mu.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For standard deviation parameter s, the variance is s^2.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getStandardDeviation(self) -> float:
        """
        Access the standard deviation.
        
        Returns:
            the standard deviation for this distribution.
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always negative infinity no matter the parameters.
        
        Returns:
            lower bound of the support (always NEGATIVE_INFINITY)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always POSITIVE_INFINITY)
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...
    def probability(self, x0: float, x1: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(x0 < X <= x1).
        
        Specified by: probability in interface RealDistribution
        
        Overrides: probability in class AbstractRealDistribution
        
        Parameters:
            x0 (double): Lower bound (excluded).
            x1 (double): Upper bound (included).
        
        Returns:
            the probability that a random variable with this distribution takes a value between x0 and x1, excluding
            the lower and including the upper endpoint.
        
        Raises:
            MathIllegalArgumentException: if x0 > x1. The default implementation uses the identity P(x0 < X <= x1) = P(X <= x1) - P(X <= x0)
        
        
        """
        ...

class ParetoDistribution(AbstractRealDistribution):
    """
    Implementation of the Pareto distribution.
    
    Parameters: The probability distribution function of X is given by (for x >= k):
    
      α * k^α / x^(α + 1)
    
      - k is the scale parameter: this is the minimum possible value of X,
      - α is the shape parameter: this is the Pareto index
    
    
          - ` Pareto distribution (Wikipedia) <http://en.wikipedia.org/wiki/Pareto_distribution>`
          - ` Pareto distribution (MathWorld) <http://mathworld.wolfram.com/ParetoDistribution.html>`
          - serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution.
        
        For scale k, and shape α of this distribution, the CDF is given by
        
          -  if x < k,
          - 1 - (k / x)^α otherwise.
        
        
        Parameters:
            x (double): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def density(self, x: float) -> float:
        """
        Returns the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient.
        
        For scale k, and shape α of this distribution, the PDF is given by
        
          -  if x < k,
          - α * k^α / x^(α + 1) otherwise.
        
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the value of the probability density function at point x
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution.
        
        For scale k and shape α, the mean is given by
        
          - ∞ if α <= 1,
          - α * k / (α - 1) otherwise.
        
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution.
        
        For scale k and shape α, the variance is given by
        
          - ∞ if 1 < α <= 2,
          - k^2 * α / ((α - 1)^2 * (α - 2)) otherwise.
        
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getScale(self) -> float:
        """
        Returns the scale parameter of this distribution.
        
        Returns:
            the scale parameter
        
        
        """
        ...
    def getShape(self) -> float:
        """
        Returns the shape parameter of this distribution.
        
        Returns:
            the shape parameter
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}.
        
        The lower bound of the support is equal to the scale parameter k.
        
        Returns:
            lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}.
        
        The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always POSITIVE_INFINITY)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support.
        
        The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x). See documentation of density for computation details.
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class TDistribution(AbstractRealDistribution):
    """
    Implementation of Student's t-distribution.
    
          - serialized
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
    def getDegreesOfFreedom(self) -> float:
        """
        Access the degrees of freedom.
        
        Returns:
            the degrees of freedom.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For degrees of freedom parameter df, the mean is
        
          - if df > 1 then ,
          - else undefined (NaN).
        
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For degrees of freedom parameter df, the variance is
        
          - if df > 2 then df / (df - 2),
          - if 1 < df <= 2 then positive infinity (POSITIVE_INFINITY),
          - else undefined (NaN).
        
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always negative infinity no matter the parameters.
        
        Returns:
            lower bound of the support (always NEGATIVE_INFINITY)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always POSITIVE_INFINITY)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...

class TriangularDistribution(AbstractRealDistribution):
    """
    Implementation of the triangular real distribution.
    
          - ` Triangular distribution (Wikipedia) <http://en.wikipedia.org/wiki/Triangular_distribution>`
          - serialized
    """
    def __init__(self, a: float, c: float, b: float):
        """
        Creates a triangular real distribution using the given lower limit, upper limit, and mode.
        
        Parameters:
            a (double): Lower limit of this distribution (inclusive).
            c (double): Mode of this distribution.
            b (double): Upper limit of this distribution (inclusive).
        
        Raises:
            MathIllegalArgumentException: if a >= b or if c > b.
            MathIllegalArgumentException: if c < a.
        
        
        """
        ...
    def cumulativeProbability(self, x: float) -> float:
        """
        For a random variable X whose values are distributed according to this distribution, this method returns P(X <= x). In other words, this method represents the (cumulative) distribution function (CDF) for this distribution. For lower limit a, upper limit b and mode c, the CDF is given by
        
          -  if x < a,
          - (x - a)^2 / [(b - a) * (c - a)] if a <= x < c,
          - (c - a) / (b - a) if x = c,
          - 1 - (b - x)^2 / [(b - a) * (b - c)] if c < x <= b,
          -  if x > b.
        
        
        Parameters:
            x (double): the point at which the CDF is evaluated
        
        Returns:
            the probability that a random variable with this distribution takes a value less than or equal to x
        
        
        """
        ...
    def density(self, x: float) -> float:
        """
        Returns the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. For lower limit a, upper limit b and mode c, the PDF is given by
        
          - 2 * (x - a) / [(b - a) * (c - a)] if a <= x < c,
          - 2 / (b - a) if x = c,
          - 2 * (b - x) / [(b - a) * (b - c)] if c < x <= b,
          -  otherwise.
        
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the value of the probability density function at point x
        
        
        """
        ...
    def getMode(self) -> float:
        """
        Returns the mode c of this distribution.
        
        Returns:
            the mode c of this distribution
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
        Use this method to get the numerical value of the mean of this distribution. For lower limit a, upper limit b, and mode c, the mean is (a + b + c) / 3.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For lower limit a, upper limit b, and mode c, the variance is (a^2 + b^2 + c^2 - a * b - a * c - b * c) / 18.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is equal to the lower limit parameter a of the distribution.
        
        Returns:
            lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is equal to the upper limit parameter b of the distribution.
        
        Returns:
            upper bound of the support
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...

class UniformRealDistribution(AbstractRealDistribution):
    """
    Implementation of the uniform real distribution.
    
          - ` Uniform distribution (continuous), at Wikipedia <http://en.wikipedia.org/wiki/Uniform_distribution_(continuous)>`
          - serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
        Use this method to get the numerical value of the mean of this distribution. For lower bound lower and upper bound upper, the mean is 5 * (lower + upper).
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. For lower bound lower and upper bound upper, the variance is (upper - lower)^2 / 12.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is equal to the lower bound parameter of the distribution.
        
        Returns:
            lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is equal to the upper bound parameter of the distribution.
        
        Returns:
            upper bound of the support
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
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
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...

class WeibullDistribution(AbstractRealDistribution):
    """
    Implementation of the Weibull distribution. This implementation uses the two parameter form of the distribution defined by ` Weibull Distribution <http://mathworld.wolfram.com/WeibullDistribution.html>`, equations (1) and (2).
    
          - `Weibull distribution (Wikipedia) <http://en.wikipedia.org/wiki/Weibull_distribution>`
          - `Weibull distribution (MathWorld) <http://mathworld.wolfram.com/WeibullDistribution.html>`
          - serialized
    """
    def __init__(self, alpha: float, beta: float):
        """
        Create a Weibull distribution with the given shape and scale.
        
        Parameters:
            alpha (double): Shape parameter.
            beta (double): Scale parameter.
        
        Raises:
            MathIllegalArgumentException: if alpha <= 0 or beta <= 0.
        
        
        """
        ...
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
        Use this method to get the numerical value of the mean of this distribution. The mean is scale * Gamma(1 + (1 / shape)), where Gamma() is the Gamma-function.
        
        Returns:
            the mean or NaN if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
        Use this method to get the numerical value of the variance of this distribution. The variance is scale^2 * Gamma(1 + (2 / shape)) - mean^2 where Gamma() is the Gamma-function.
        
        Returns:
            the variance (possibly POSITIVE_INFINITY as for certain cases in
            TDistribution) or NaN if it is not defined
        
        
        """
        ...
    def getScale(self) -> float:
        """
        Access the scale parameter, beta.
        
        Returns:
            the scale parameter, beta.
        
        
        """
        ...
    def getShape(self) -> float:
        """
        Access the shape parameter, alpha.
        
        Returns:
            the shape parameter, alpha.
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
        Access the lower bound of the support. This method must return the same value as inverseCumulativeProbability(0). In other words, this method must return
        
        inf {x in R | P(X <= x) > 0}. The lower bound of the support is always 0 no matter the parameters.
        
        Returns:
            lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
        Access the upper bound of the support. This method must return the same value as inverseCumulativeProbability(1). In other words, this method must return
        
        inf {x in R | P(X <= x) = 1}. The upper bound of the support is always positive infinity no matter the parameters.
        
        Returns:
            upper bound of the support (always POSITIVE_INFINITY)
        
        
        """
        ...
    def inverseCumulativeProbability(self, p: float) -> float:
        """
        Computes the quantile function of this distribution. For a random variable X distributed according to this distribution, the returned value is
        
          - inf{x in R | P(X<=x) >= p} for 0 < p <= 1,
          - inf{x in R | P(X<=x) > 0} for p = 0.
        
        The default implementation returns
        
          - getSupportLowerBound for p = 0,
          - getSupportUpperBound for p = 1.
        
        Returns  when p == 0 and POSITIVE_INFINITY when p == 1.
        
        Specified by: inverseCumulativeProbability in interface RealDistribution
        
        Overrides: inverseCumulativeProbability in class AbstractRealDistribution
        
        Parameters:
            p (double): the cumulative probability
        
        Returns:
            the smallest p-quantile of this distribution (largest 0-quantile for p = 0)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
        Use this method to get information about whether the support is connected, i.e. whether all values between the lower and upper bound of the support are included in the support. The support of this distribution is connected.
        
        Returns:
            true
        
        
        """
        ...
    def logDensity(self, x: float) -> float:
        """
        Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified point x. In general, the PDF is the derivative of the cumulativeProbability. If the derivative does not exist at x, then an appropriate replacement should be returned, e.g. POSITIVE_INFINITY, NaN, or the limit inferior or limit superior of the difference quotient. Note that due to the floating point precision and under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm of density.
        
        The default implementation simply computes the logarithm of density(x).
        
        Specified by: logDensity in interface RealDistribution
        
        Overrides: logDensity in class AbstractRealDistribution
        
        Parameters:
            x (double): the point at which the PDF is evaluated
        
        Returns:
            the logarithm of the value of the probability density function at point x
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.distribution.continuous")``.

    AbstractRealDistribution: typing.Type[AbstractRealDistribution]
    BetaDistribution: typing.Type[BetaDistribution]
    CauchyDistribution: typing.Type[CauchyDistribution]
    ChiSquaredDistribution: typing.Type[ChiSquaredDistribution]
    ConstantRealDistribution: typing.Type[ConstantRealDistribution]
    EnumeratedRealDistribution: typing.Type[EnumeratedRealDistribution]
    ExponentialDistribution: typing.Type[ExponentialDistribution]
    FDistribution: typing.Type[FDistribution]
    GammaDistribution: typing.Type[GammaDistribution]
    GumbelDistribution: typing.Type[GumbelDistribution]
    LaplaceDistribution: typing.Type[LaplaceDistribution]
    LevyDistribution: typing.Type[LevyDistribution]
    LogNormalDistribution: typing.Type[LogNormalDistribution]
    LogisticDistribution: typing.Type[LogisticDistribution]
    NakagamiDistribution: typing.Type[NakagamiDistribution]
    NormalDistribution: typing.Type[NormalDistribution]
    ParetoDistribution: typing.Type[ParetoDistribution]
    TDistribution: typing.Type[TDistribution]
    TriangularDistribution: typing.Type[TriangularDistribution]
    UniformRealDistribution: typing.Type[UniformRealDistribution]
    WeibullDistribution: typing.Type[WeibullDistribution]
