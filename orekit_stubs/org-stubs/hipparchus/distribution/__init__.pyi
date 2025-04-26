
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
    public classEnumeratedDistribution<T> extends :class:`~org.hipparchus.distribution.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.distribution.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        A generic implementation of a ` discrete probability distribution (Wikipedia)
        <http://en.wikipedia.org/wiki/Probability_distribution#Discrete_probability_distribution>` over a finite sample space,
        based on an enumerated list of <value, probability> pairs.
    
        Input probabilities must all be non-negative, but zero values are allowed and their sum does not have to equal one.
        Constructors will normalize input probabilities to make them sum to one.
    
        The list of <value, probability> pairs does not, strictly speaking, have to be a function and it can contain null
        values. The pmf created by the constructor will combine probabilities of equal values and will treat null values as
        equal.
    
        For example, if the list of pairs <"dog", 0.2>, <null, 0.1>, <"pig", 0.2>, <"dog", 0.1>, <null, 0.4> is provided to the
        constructor, the resulting pmf will assign mass of 0.5 to null, 0.3 to "dog" and 0.2 to null.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, list: java.util.List[org.hipparchus.util.Pair[_EnumeratedDistribution__T, float]]): ...
    @staticmethod
    def checkAndNormalize(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
            Checks to make sure that weights is neither null nor empty and contains only non-negative, finite, non-NaN values and if
            necessary normalizes it to sum to 1.
        
            Parameters:
                weights (double[]): input array to be used as the basis for the values of a PMF
        
            Returns:
                a possibly rescaled copy of the array that sums to 1 and contains only valid probability values
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: of weights is null or empty or includes negative, NaN or infinite values or only 0's
        
        
        """
        ...
    def getPmf(self) -> java.util.List[org.hipparchus.util.Pair[_EnumeratedDistribution__T, float]]: ...
    def probability(self, t: _EnumeratedDistribution__T) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Note that if :code:`x1` and :code:`x2` satisfy :code:`x1.equals(x2)`, or both are null, then :code:`probability(x1) =
            probability(x2)`.
        
            Parameters:
                x (:class:`~org.hipparchus.distribution.EnumeratedDistribution`): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class IntegerDistribution:
    """
    public interfaceIntegerDistribution
    
        Interface for discrete distributions.
    """
    def cumulativeProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution.
        
            Parameters:
                x (int): the point at which the CDF is evaluated
        
            Returns:
                the probability that a random variable with this distribution takes a value less than or equal to :code:`x`
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
        
            Returns:
                lower bound of the support (:code:`Integer.MIN_VALUE` for negative infinity)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
        
            Returns:
                upper bound of the support (:code:`Integer.MAX_VALUE` for positive infinity)
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> int: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support.
        
            Returns:
                whether the support is connected or not
        
        
        """
        ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        double probability(int x0, int x1) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(x0 < X <= x1)`.
        
            Parameters:
                x0 (int): the exclusive lower bound
                x1 (int): the inclusive upper bound
        
            Returns:
                the probability that a random variable with this distribution will take a value between :code:`x0` and :code:`x1`,
                excluding the lower and including the upper endpoint
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x0 > x1`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...

class MultivariateRealDistribution:
    """
    public interfaceMultivariateRealDistribution
    
        Base interface for multivariate continuous distributions.
    
        This is based largely on the RealDistribution interface, but cumulative distribution functions are not required because
        they are often quite difficult to compute for multivariate distributions.
    """
    def density(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Returns the probability density function (PDF) of this distribution evaluated at the specified point :code:`x`. In
            general, the PDF is the derivative of the cumulative distribution function. If the derivative does not exist at
            :code:`x`, then an appropriate replacement should be returned, e.g. :code:`Double.POSITIVE_INFINITY`,
            :code:`Double.NaN`, or the limit inferior or limit superior of the difference quotient.
        
            Parameters:
                x (double[]): Point at which the PDF is evaluated.
        
            Returns:
                the value of the probability density function at point :code:`x`.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Gets the number of random variables of the distribution. It is the size of the array returned by the
            :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample` method.
        
            Returns:
                the number of variables.
        
        
        """
        ...
    def reseedRandomGenerator(self, long: int) -> None:
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
        
        double[][] sample(int sampleSize) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Generates a list of a random value vectors from the distribution.
        
            Parameters:
                sampleSize (int): the number of random vectors to generate.
        
            Returns:
                an array representing the random samples.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`sampleSize` is not positive.
        
            Also see:
        
                  - :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample`
        
        
        
        """
        ...
    @typing.overload
    def sample(self, int: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

class RealDistribution:
    """
    public interfaceRealDistribution
    
        Base interface for continuous distributions.
    """
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution.
        
            Parameters:
                x (double): the point at which the CDF is evaluated
        
            Returns:
                the probability that a random variable with this distribution takes a value less than or equal to :code:`x`
        
        
        """
        ...
    def density(self, double: float) -> float:
        """
            Returns the probability density function (PDF) of this distribution evaluated at the specified point :code:`x`. In
            general, the PDF is the derivative of the :meth:`~org.hipparchus.distribution.RealDistribution.cumulativeProbability`.
            If the derivative does not exist at :code:`x`, then an appropriate replacement should be returned, e.g.
            :code:`Double.POSITIVE_INFINITY`, :code:`Double.NaN`, or the limit inferior or limit superior of the difference
            quotient.
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the value of the probability density function at point :code:`x`
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` as for certain cases in
                :class:`~org.hipparchus.distribution.continuous.TDistribution`) or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
        
            Returns:
                lower bound of the support (might be :code:`Double.NEGATIVE_INFINITY`)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
        
            Returns:
                upper bound of the support (might be :code:`Double.POSITIVE_INFINITY`)
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support.
        
            Returns:
                whether the support is connected or not
        
        
        """
        ...
    def logDensity(self, double: float) -> float:
        """
            Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified
            point :code:`x`. In general, the PDF is the derivative of the
            :meth:`~org.hipparchus.distribution.RealDistribution.cumulativeProbability`. If the derivative does not exist at
            :code:`x`, then an appropriate replacement should be returned, e.g. :code:`Double.POSITIVE_INFINITY`,
            :code:`Double.NaN`, or the limit inferior or limit superior of the difference quotient. Note that due to the floating
            point precision and under/overflow issues, this method will for some distributions be more precise and faster than
            computing the logarithm of :meth:`~org.hipparchus.distribution.RealDistribution.density`.
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...
    def probability(self, double: float, double2: float) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.distribution")``.

    EnumeratedDistribution: typing.Type[EnumeratedDistribution]
    IntegerDistribution: typing.Type[IntegerDistribution]
    MultivariateRealDistribution: typing.Type[MultivariateRealDistribution]
    RealDistribution: typing.Type[RealDistribution]
    continuous: org.hipparchus.distribution.continuous.__module_protocol__
    discrete: org.hipparchus.distribution.discrete.__module_protocol__
    multivariate: org.hipparchus.distribution.multivariate.__module_protocol__
