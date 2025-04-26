
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
    public abstract classAbstractRealDistribution extends :class:`~org.hipparchus.distribution.continuous.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.distribution.RealDistribution`, :class:`~org.hipparchus.distribution.continuous.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Base class for probability distributions on the reals.
    
        Default implementations are provided for some of the methods that do not vary from distribution to distribution.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def logDensity(self, double: float) -> float:
        """
            Returns the natural logarithm of the probability density function (PDF) of this distribution evaluated at the specified
            point :code:`x`. In general, the PDF is the derivative of the
            :meth:`~org.hipparchus.distribution.RealDistribution.cumulativeProbability`. If the derivative does not exist at
            :code:`x`, then an appropriate replacement should be returned, e.g. :code:`Double.POSITIVE_INFINITY`,
            :code:`Double.NaN`, or the limit inferior or limit superior of the difference quotient. Note that due to the floating
            point precision and under/overflow issues, this method will for some distributions be more precise and faster than
            computing the logarithm of :meth:`~org.hipparchus.distribution.RealDistribution.density`.
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...
    def probability(self, double: float, double2: float) -> float: ...

class BetaDistribution(AbstractRealDistribution):
    """
    public classBetaDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implements the Beta distribution.
    
        Also see:
    
              - `Beta distribution <http://en.wikipedia.org/wiki/Beta_distribution>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
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
    def getAlpha(self) -> float:
        """
            Access the first shape parameter, :code:`alpha`.
        
            Returns:
                the first shape parameter.
        
        
        """
        ...
    def getBeta(self) -> float:
        """
            Access the second shape parameter, :code:`beta`.
        
            Returns:
                the second shape parameter.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For first shape parameter :code:`alpha` and
            second shape parameter :code:`beta`, the mean is :code:`alpha / (alpha + beta)`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For first shape parameter :code:`alpha`
            and second shape parameter :code:`beta`, the variance is :code:`(alpha * beta) / [(alpha + beta)^2 * (alpha + beta +
            1)]`.
        
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
            The lower bound of the support is always 0 no matter the parameters.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always 1 no matter the parameters.
        
            Returns:
                upper bound of the support (always 1)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class CauchyDistribution(AbstractRealDistribution):
    """
    public classCauchyDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the Cauchy distribution.
    
        Also see:
    
              - `Cauchy distribution (Wikipedia) <http://en.wikipedia.org/wiki/Cauchy_distribution>`
              - `Cauchy Distribution (MathWorld) <http://mathworld.wolfram.com/CauchyDistribution.html>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
    def getMedian(self) -> float:
        """
            Access the median.
        
            Returns:
                the median for this distribution.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. The mean is always undefined no matter the
            parameters.
        
            Returns:
                mean (always Double.NaN)
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. The variance is always undefined no
            matter the parameters.
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
            The lower bound of the support is always negative infinity no matter the parameters.
        
            Returns:
                lower bound of the support (always Double.NEGATIVE_INFINITY)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...

class ChiSquaredDistribution(AbstractRealDistribution):
    """
    public classChiSquaredDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the chi-squared distribution.
    
        Also see:
    
              - `Chi-squared distribution (Wikipedia) <http://en.wikipedia.org/wiki/Chi-squared_distribution>`
              - `Chi-squared Distribution (MathWorld) <http://mathworld.wolfram.com/Chi-SquaredDistribution.html>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
    def getDegreesOfFreedom(self) -> float:
        """
            Access the number of degrees of freedom.
        
            Returns:
                the degrees of freedom.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For :code:`k` degrees of freedom, the mean
            is :code:`k`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution.
        
            Returns:
                :code:`2 * k`, where :code:`k` is the number of degrees of freedom.
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
            The lower bound of the support is always 0 no matter the degrees of freedom.
        
            Returns:
                zero.
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the degrees of freedom.
        
            Returns:
                :code:`Double.POSITIVE_INFINITY`.
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class ConstantRealDistribution(AbstractRealDistribution):
    """
    public classConstantRealDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the constant real distribution.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, double: float): ...
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

class EnumeratedRealDistribution(AbstractRealDistribution):
    """
    public classEnumeratedRealDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of a real-valued :class:`~org.hipparchus.distribution.EnumeratedDistribution`.
    
        Values with zero-probability are allowed but they do not extend the support.
    
        Duplicate values are allowed. Probabilities of duplicate values are combined when computing cumulative probabilities and
        statistics.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
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
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (double): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at point :code:`x`
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution.
        
            Returns:
                :code:`sum(singletons[i] * probabilities[i])`
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution.
        
            Returns:
                :code:`sum((singletons[i] - mean) ^ 2 * probabilities[i])`
        
        
        """
        ...
    def getPmf(self) -> java.util.List[org.hipparchus.util.Pair[float, float]]: ...
    def getSupportLowerBound(self) -> float:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
            Returns the lowest value with non-zero probability.
        
            Returns:
                the lowest value with non-zero probability.
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            Returns the highest value with non-zero probability.
        
            Returns:
                the highest value with non-zero probability.
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    @typing.overload
    def probability(self, double: float, double2: float) -> float: ...
    @typing.overload
    def probability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Note that if :code:`x1` and :code:`x2` satisfy :code:`x1.equals(x2)`, or both are null, then :code:`probability(x1) =
            probability(x2)`.
        
            Parameters:
                x (double): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class ExponentialDistribution(AbstractRealDistribution):
    """
    public classExponentialDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the exponential distribution.
    
        Also see:
    
              - `Exponential distribution (Wikipedia) <http://en.wikipedia.org/wiki/Exponential_distribution>`
              - `Exponential distribution (MathWorld) <http://mathworld.wolfram.com/ExponentialDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, double: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution. The implementation of this method is based on:
        
              - ` Exponential Distribution <http://mathworld.wolfram.com/ExponentialDistribution.html>`, equation (1).
        
        
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
    def getMean(self) -> float:
        """
            Access the mean.
        
            Returns:
                the mean.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For mean parameter :code:`k`, the mean is
            :code:`k`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For mean parameter :code:`k`, the
            variance is :code:`k^2`.
        
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
            The lower bound of the support is always 0 no matter the mean parameter.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the mean parameter.
        
            Returns:
                upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class FDistribution(AbstractRealDistribution):
    """
    public classFDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the F-distribution.
    
        Also see:
    
              - `F-distribution (Wikipedia) <http://en.wikipedia.org/wiki/F-distribution>`
              - `F-distribution (MathWorld) <http://mathworld.wolfram.com/F-Distribution.html>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution. The implementation of this method is based on
        
              - ` F-Distribution <http://mathworld.wolfram.com/F-Distribution.html>`, equation (4).
        
        
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
            Use this method to get the numerical value of the mean of this distribution. For denominator degrees of freedom
            parameter :code:`b`, the mean is
        
              - if :code:`b > 2` then :code:`b / (b - 2)`,
              - else undefined (:code:`Double.NaN`).
        
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For numerator degrees of freedom
            parameter :code:`a` and denominator degrees of freedom parameter :code:`b`, the variance is
        
              - if :code:`b > 4` then :code:`[2 * b^2 * (a + b - 2)] / [a * (b - 2)^2 * (b - 4)]`,
              - else undefined (:code:`Double.NaN`).
        
        
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
            The lower bound of the support is always 0 no matter the parameters.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class GammaDistribution(AbstractRealDistribution):
    """
    public classGammaDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the Gamma distribution.
    
        Also see:
    
              - `Gamma distribution (Wikipedia) <http://en.wikipedia.org/wiki/Gamma_distribution>`
              - `Gamma distribution (MathWorld) <http://mathworld.wolfram.com/GammaDistribution.html>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution. The implementation of this method is based on:
        
              - ` Chi-Squared Distribution <http://mathworld.wolfram.com/Chi-SquaredDistribution.html>`, equation (9).
              - Casella, G., & Berger, R. (1990). *Statistical Inference*. Belmont, CA: Duxbury Press.
        
        
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
            Use this method to get the numerical value of the mean of this distribution. For shape parameter :code:`alpha` and scale
            parameter :code:`beta`, the mean is :code:`alpha * beta`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For shape parameter :code:`alpha` and
            scale parameter :code:`beta`, the variance is :code:`alpha * beta^2`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` as for certain cases in
                :class:`~org.hipparchus.distribution.continuous.TDistribution`) or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getScale(self) -> float:
        """
            Returns the scale parameter of :code:`this` distribution.
        
            Returns:
                the scale parameter
        
        
        """
        ...
    def getShape(self) -> float:
        """
            Returns the shape parameter of :code:`this` distribution.
        
            Returns:
                the shape parameter
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
            The lower bound of the support is always 0 no matter the parameters.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always Double.POSITIVE_INFINITY)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class GumbelDistribution(AbstractRealDistribution):
    """
    public classGumbelDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        This class implements the Gumbel distribution.
    
        Also see:
    
              - `Gumbel Distribution (Wikipedia) <http://en.wikipedia.org/wiki/Gumbel_distribution>`
              - `Gumbel Distribution (Mathworld) <http://mathworld.wolfram.com/GumbelDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float): ...
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
    def getLocation(self) -> float:
        """
            Access the location parameter, :code:`mu`.
        
            Returns:
                the location parameter.
        
        
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
    def getScale(self) -> float:
        """
            Access the scale parameter, :code:`beta`.
        
            Returns:
                the scale parameter.
        
        
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

class LaplaceDistribution(AbstractRealDistribution):
    """
    public classLaplaceDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        This class implements the Laplace distribution.
    
        Also see:
    
              - `Laplace distribution (Wikipedia) <http://en.wikipedia.org/wiki/Laplace_distribution>`
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float): ...
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
    def getLocation(self) -> float:
        """
            Access the location parameter, :code:`mu`.
        
            Returns:
                the location parameter.
        
        
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
    def getScale(self) -> float:
        """
            Access the scale parameter, :code:`beta`.
        
            Returns:
                the scale parameter.
        
        
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

class LevyDistribution(AbstractRealDistribution):
    """
    public classLevyDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        This class implements the ` Lévy distribution <http://en.wikipedia.org/wiki/L%C3%A9vy_distribution>`.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution.
        
            From Wikipedia: the cumulative distribution function is
        
            .. code-block: java
            
             f(x; u, c) = erfc (√ (c / 2 (x - u )))
             
        
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
        
            From Wikipedia: The probability density function of the Lévy distribution over the domain is
            \[ f(x; \mu, c) = \sqrt{\frac{c}{2\pi}} \frac{e^{\frac{-c}{2 (x - \mu)}}}{(x - \mu)^\frac{3}{2}} \]
        
            For this distribution, :code:`X`, this method returns :code:`P(X < x)`. If :code:`x` is less than location parameter μ,
            :code:`Double.NaN` is returned, as in these cases the distribution is not defined.
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the value of the probability density function at point :code:`x`
        
        
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
    def getScale(self) -> float:
        """
            Get the scale parameter of the distribution.
        
            Returns:
                scale parameter of the distribution
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`. See documentation of
            :meth:`~org.hipparchus.distribution.continuous.LevyDistribution.density` for computation details.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class LogNormalDistribution(AbstractRealDistribution):
    """
    public classLogNormalDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the log-normal (gaussian) distribution.
    
        **Parameters:** :code:`X` is log-normally distributed if its natural logarithm :code:`log(X)` is normally distributed.
        The probability distribution function of :code:`X` is given by (for :code:`x > 0`)
    
        :code:`exp(-0.5 * ((ln(x) - m) / s)^2) / (s * sqrt(2 * pi) * x)`
    
          - :code:`m` is the *location* parameter: this is the mean of the normally distributed natural logarithm of this
            distribution,
          - :code:`s` is the *shape* parameter: this is the standard deviation of the normally distributed natural logarithm of this
            distribution.
    
    
        Also see:
    
              - ` Log-normal distribution (Wikipedia) <http://en.wikipedia.org/wiki/Log-normal_distribution>`
              - ` Log Normal distribution (MathWorld) <http://mathworld.wolfram.com/LogNormalDistribution.html>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution. For location :code:`m`, and shape :code:`s` of this distribution, the CDF is given by
        
              - :code:`0` if :code:`x <= 0`,
              - :code:`0` if :code:`ln(x) - m < 0` and :code:`m - ln(x) > 40 * s`, as in these cases the actual value is within
                :code:`Double.MIN_VALUE` of 0,
              - :code:`1` if :code:`ln(x) - m >= 0` and :code:`ln(x) - m > 40 * s`, as in these cases the actual value is within
                :code:`Double.MIN_VALUE` of 1,
              - :code:`0.5 + 0.5 * erf((ln(x) - m) / (s * sqrt(2))` otherwise.
        
        
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
            quotient. For location :code:`m`, and shape :code:`s` of this distribution, the PDF is given by
        
              - :code:`0` if :code:`x <= 0`,
              - :code:`exp(-0.5 * ((ln(x) - m) / s)^2) / (s * sqrt(2 * pi) * x)` otherwise.
        
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the value of the probability density function at point :code:`x`
        
        
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
            Use this method to get the numerical value of the mean of this distribution. For location :code:`m` and shape :code:`s`,
            the mean is :code:`exp(m + s^2 / 2)`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For location :code:`m` and shape
            :code:`s`, the variance is :code:`(exp(s^2) - 1) * exp(2 * m + s^2)`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` as for certain cases in
                :class:`~org.hipparchus.distribution.continuous.TDistribution`) or :code:`Double.NaN` if it is not defined
        
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
            The lower bound of the support is always 0 no matter the parameters.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always :code:`Double.POSITIVE_INFINITY`)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`. See documentation of
            :meth:`~org.hipparchus.distribution.continuous.LogNormalDistribution.density` for computation details.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...
    def probability(self, double: float, double2: float) -> float: ...

class LogisticDistribution(AbstractRealDistribution):
    """
    public classLogisticDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        This class implements the Logistic distribution.
    
        Also see:
    
              - `Logistic Distribution (Wikipedia) <http://en.wikipedia.org/wiki/Logistic_distribution>`
              - `Logistic Distribution (Mathworld) <http://mathworld.wolfram.com/LogisticDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float): ...
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
    def getLocation(self) -> float:
        """
            Access the location parameter, :code:`mu`.
        
            Returns:
                the location parameter.
        
        
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
    def getScale(self) -> float:
        """
            Access the scale parameter, :code:`s`.
        
            Returns:
                the scale parameter.
        
        
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

class NakagamiDistribution(AbstractRealDistribution):
    """
    public classNakagamiDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        This class implements the Nakagami distribution.
    
        Also see:
    
              - `Nakagami Distribution (Wikipedia) <http://en.wikipedia.org/wiki/Nakagami_distribution>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
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
    def getScale(self) -> float:
        """
            Access the scale parameter, :code:`omega`.
        
            Returns:
                the scale parameter.
        
        
        """
        ...
    def getShape(self) -> float:
        """
            Access the shape parameter, :code:`mu`.
        
            Returns:
                the shape parameter.
        
        
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
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support.
        
            Returns:
                whether the support is connected or not
        
        
        """
        ...

class NormalDistribution(AbstractRealDistribution):
    """
    public classNormalDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the normal (gaussian) distribution.
    
        Also see:
    
              - `Normal distribution (Wikipedia) <http://en.wikipedia.org/wiki/Normal_distribution>`
              - `Normal distribution (MathWorld) <http://mathworld.wolfram.com/NormalDistribution.html>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution. If :code:`x` is more than 40 standard deviations from the mean, 0 or 1 is returned, as in these cases the
            actual value is within :code:`Double.MIN_VALUE` of 0 or 1.
        
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
    def getMean(self) -> float:
        """
            Access the mean.
        
            Returns:
                the mean for this distribution.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For mean parameter :code:`mu`, the mean is
            :code:`mu`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For standard deviation parameter
            :code:`s`, the variance is :code:`s^2`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` as for certain cases in
                :class:`~org.hipparchus.distribution.continuous.TDistribution`) or :code:`Double.NaN` if it is not defined
        
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
            The lower bound of the support is always negative infinity no matter the parameters.
        
            Returns:
                lower bound of the support (always :code:`Double.NEGATIVE_INFINITY`)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always :code:`Double.POSITIVE_INFINITY`)
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...
    def probability(self, double: float, double2: float) -> float: ...

class ParetoDistribution(AbstractRealDistribution):
    """
    public classParetoDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the Pareto distribution.
    
        **Parameters:** The probability distribution function of :code:`X` is given by (for :code:`x >= k`):
    
        .. code-block: java
        
          α * k^α / x^(α + 1)
         
    
          - :code:`k` is the *scale* parameter: this is the minimum possible value of :code:`X`,
          - :code:`α` is the *shape* parameter: this is the Pareto index
    
    
        Also see:
    
              - ` Pareto distribution (Wikipedia) <http://en.wikipedia.org/wiki/Pareto_distribution>`
              - ` Pareto distribution (MathWorld) <http://mathworld.wolfram.com/ParetoDistribution.html>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution.
        
            For scale :code:`k`, and shape :code:`α` of this distribution, the CDF is given by
        
              - :code:`0` if :code:`x < k`,
              - :code:`1 - (k / x)^α` otherwise.
        
        
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
        
            For scale :code:`k`, and shape :code:`α` of this distribution, the PDF is given by
        
              - :code:`0` if :code:`x < k`,
              - :code:`α * k^α / x^(α + 1)` otherwise.
        
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the value of the probability density function at point :code:`x`
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution.
        
            For scale :code:`k` and shape :code:`α`, the mean is given by
        
              - :code:`∞` if :code:`α <= 1`,
              - :code:`α * k / (α - 1)` otherwise.
        
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution.
        
            For scale :code:`k` and shape :code:`α`, the variance is given by
        
              - :code:`∞` if :code:`1 < α <= 2`,
              - :code:`k^2 * α / ((α - 1)^2 * (α - 2))` otherwise.
        
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` as for certain cases in
                :class:`~org.hipparchus.distribution.continuous.TDistribution`) or :code:`Double.NaN` if it is not defined
        
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
        
            The lower bound of the support is equal to the scale parameter :code:`k`.
        
            Returns:
                lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
        
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always :code:`Double.POSITIVE_INFINITY`)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support.
        
            The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`. See documentation of
            :meth:`~org.hipparchus.distribution.continuous.ParetoDistribution.density` for computation details.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class TDistribution(AbstractRealDistribution):
    """
    public classTDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of Student's t-distribution.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
    def getDegreesOfFreedom(self) -> float:
        """
            Access the degrees of freedom.
        
            Returns:
                the degrees of freedom.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For degrees of freedom parameter
            :code:`df`, the mean is
        
              - if :code:`df > 1` then :code:`0`,
              - else undefined (:code:`Double.NaN`).
        
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For degrees of freedom parameter
            :code:`df`, the variance is
        
              - if :code:`df > 2` then :code:`df / (df - 2)`,
              - if :code:`1 < df <= 2` then positive infinity (:code:`Double.POSITIVE_INFINITY`),
              - else undefined (:code:`Double.NaN`).
        
        
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
            The lower bound of the support is always negative infinity no matter the parameters.
        
            Returns:
                lower bound of the support (always :code:`Double.NEGATIVE_INFINITY`)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always :code:`Double.POSITIVE_INFINITY`)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
        """
        ...

class TriangularDistribution(AbstractRealDistribution):
    """
    public classTriangularDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the triangular real distribution.
    
        Also see:
    
              - ` Triangular distribution (Wikipedia) <http://en.wikipedia.org/wiki/Triangular_distribution>`
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def cumulativeProbability(self, double: float) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X <= x)`. In other words, this method represents the (cumulative) distribution function (CDF) for this
            distribution. For lower limit :code:`a`, upper limit :code:`b` and mode :code:`c`, the CDF is given by
        
              - :code:`0` if :code:`x < a`,
              - :code:`(x - a)^2 / [(b - a) * (c - a)]` if :code:`a <= x < c`,
              - :code:`(c - a) / (b - a)` if :code:`x = c`,
              - :code:`1 - (b - x)^2 / [(b - a) * (b - c)]` if :code:`c < x <= b`,
              - :code:`1` if :code:`x > b`.
        
        
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
            quotient. For lower limit :code:`a`, upper limit :code:`b` and mode :code:`c`, the PDF is given by
        
              - :code:`2 * (x - a) / [(b - a) * (c - a)]` if :code:`a <= x < c`,
              - :code:`2 / (b - a)` if :code:`x = c`,
              - :code:`2 * (b - x) / [(b - a) * (b - c)]` if :code:`c < x <= b`,
              - :code:`0` otherwise.
        
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the value of the probability density function at point :code:`x`
        
        
        """
        ...
    def getMode(self) -> float:
        """
            Returns the mode :code:`c` of this distribution.
        
            Returns:
                the mode :code:`c` of this distribution
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For lower limit :code:`a`, upper limit
            :code:`b`, and mode :code:`c`, the mean is :code:`(a + b + c) / 3`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For lower limit :code:`a`, upper limit
            :code:`b`, and mode :code:`c`, the variance is :code:`(a^2 + b^2 + c^2 - a * b - a * c - b * c) / 18`.
        
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
            The lower bound of the support is equal to the lower limit parameter :code:`a` of the distribution.
        
            Returns:
                lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is equal to the upper limit parameter :code:`b` of the distribution.
        
            Returns:
                upper bound of the support
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...

class UniformRealDistribution(AbstractRealDistribution):
    """
    public classUniformRealDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the uniform real distribution.
    
        Also see:
    
              - ` Uniform distribution (continuous), at Wikipedia <http://en.wikipedia.org/wiki/Uniform_distribution_(continuous)>`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
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
            Use this method to get the numerical value of the mean of this distribution. For lower bound :code:`lower` and upper
            bound :code:`upper`, the mean is :code:`0.5 * (lower + upper)`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For lower bound :code:`lower` and upper
            bound :code:`upper`, the variance is :code:`(upper - lower)^2 / 12`.
        
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
            The lower bound of the support is equal to the lower bound parameter of the distribution.
        
            Returns:
                lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is equal to the upper bound parameter of the distribution.
        
            Returns:
                upper bound of the support
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...

class WeibullDistribution(AbstractRealDistribution):
    """
    public classWeibullDistribution extends :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
    
        Implementation of the Weibull distribution. This implementation uses the two parameter form of the distribution defined
        by ` Weibull Distribution <http://mathworld.wolfram.com/WeibullDistribution.html>`, equations (1) and (2).
    
        Also see:
    
              - `Weibull distribution (Wikipedia) <http://en.wikipedia.org/wiki/Weibull_distribution>`
              - `Weibull distribution (MathWorld) <http://mathworld.wolfram.com/WeibullDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float): ...
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
            Use this method to get the numerical value of the mean of this distribution. The mean is :code:`scale * Gamma(1 + (1 /
            shape))`, where :code:`Gamma()` is the Gamma-function.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. The variance is :code:`scale^2 *
            Gamma(1 + (2 / shape)) - mean^2` where :code:`Gamma()` is the Gamma-function.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` as for certain cases in
                :class:`~org.hipparchus.distribution.continuous.TDistribution`) or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getScale(self) -> float:
        """
            Access the scale parameter, :code:`beta`.
        
            Returns:
                the scale parameter, :code:`beta`.
        
        
        """
        ...
    def getShape(self) -> float:
        """
            Access the shape parameter, :code:`alpha`.
        
            Returns:
                the shape parameter, :code:`alpha`.
        
        
        """
        ...
    def getSupportLowerBound(self) -> float:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) > 0}`.
            The lower bound of the support is always 0 no matter the parameters.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> float:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters.
        
            Returns:
                upper bound of the support (always :code:`Double.POSITIVE_INFINITY`)
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float:
        """
            Computes the quantile function of this distribution. For a random variable :code:`X` distributed according to this
            distribution, the returned value is
        
              - :code:`inf{x in R | P(X<=x) >= p}` for :code:`0 < p <= 1`,
              - :code:`inf{x in R | P(X<=x) > 0}` for :code:`p = 0`.
        
            The default implementation returns
        
              - :meth:`~org.hipparchus.distribution.RealDistribution.getSupportLowerBound` for :code:`p = 0`,
              - :meth:`~org.hipparchus.distribution.RealDistribution.getSupportUpperBound` for :code:`p = 1`.
        
            Returns :code:`0` when :code:`p == 0` and :code:`Double.POSITIVE_INFINITY` when :code:`p == 1`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.inverseCumulativeProbability` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.inverseCumulativeProbability` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                p (double): the cumulative probability
        
            Returns:
                the smallest :code:`p`-quantile of this distribution (largest 0-quantile for :code:`p = 0`)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all values between the lower and
            upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
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
        
            The default implementation simply computes the logarithm of :code:`density(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.RealDistribution.logDensity` in
                interface :class:`~org.hipparchus.distribution.RealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.continuous.AbstractRealDistribution.logDensity` in
                class :class:`~org.hipparchus.distribution.continuous.AbstractRealDistribution`
        
            Parameters:
                x (double): the point at which the PDF is evaluated
        
            Returns:
                the logarithm of the value of the probability density function at point :code:`x`
        
        
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
