
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
    public abstract classAbstractIntegerDistribution extends :class:`~org.hipparchus.distribution.discrete.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.distribution.IntegerDistribution`, :class:`~org.hipparchus.distribution.discrete.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Base class for integer-valued discrete distributions.
    
        Default implementations are provided for some of the methods that do not vary from distribution to distribution.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def inverseCumulativeProbability(self, double: float) -> int: ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            The default implementation simply computes the logarithm of :code:`probability(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.IntegerDistribution.logProbability` in
                interface :class:`~org.hipparchus.distribution.IntegerDistribution`
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int) -> float: ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...

class BinomialDistribution(AbstractIntegerDistribution):
    """
    public classBinomialDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of the binomial distribution.
    
        Also see:
    
              - `Binomial distribution (Wikipedia) <http://en.wikipedia.org/wiki/Binomial_distribution>`
              - `Binomial Distribution (MathWorld) <http://mathworld.wolfram.com/BinomialDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, int: int, double: float): ...
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
    def getNumberOfTrials(self) -> int:
        """
            Access the number of trials for this distribution.
        
            Returns:
                the number of trials.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For :code:`n` trials and probability
            parameter :code:`p`, the mean is :code:`n * p`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For :code:`n` trials and probability
            parameter :code:`p`, the variance is :code:`n * p * (1 - p)`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            The lower bound of the support is always 0 except for the probability parameter :code:`p = 1`.
        
            Returns:
                lower bound of the support (0 or the number of trials)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is the number of trials except for the probability parameter :code:`p = 0`.
        
            Returns:
                upper bound of the support (number of trials or 0)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            The default implementation simply computes the logarithm of :code:`probability(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.IntegerDistribution.logProbability` in
                interface :class:`~org.hipparchus.distribution.IntegerDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution.logProbability` in
                class :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class EnumeratedIntegerDistribution(AbstractIntegerDistribution):
    """
    public classEnumeratedIntegerDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of an integer-valued :class:`~org.hipparchus.distribution.EnumeratedDistribution`.
    
        Values with zero-probability are allowed but they do not extend the support.
    
        Duplicate values are allowed. Probabilities of duplicate values are combined when computing cumulative probabilities and
        statistics.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, intArray: typing.Union[typing.List[int], jpype.JArray]): ...
    @typing.overload
    def __init__(self, intArray: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
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
    def getPmf(self) -> java.util.List[org.hipparchus.util.Pair[int, float]]: ...
    def getSupportLowerBound(self) -> int:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            Returns the lowest value with non-zero probability.
        
            Returns:
                the lowest value with non-zero probability.
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            Returns the highest value with non-zero probability.
        
            Returns:
                the highest value with non-zero probability.
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class GeometricDistribution(AbstractIntegerDistribution):
    """
    public classGeometricDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of the geometric distribution.
    
        Also see:
    
              - `Geometric distribution (Wikipedia) <http://en.wikipedia.org/wiki/Geometric_distribution>`
              - `Geometric Distribution (MathWorld) <http://mathworld.wolfram.com/GeometricDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, double: float): ...
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
            Use this method to get the numerical value of the mean of this distribution. For probability parameter :code:`p`, the
            mean is :code:`(1 - p) / p`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For probability parameter :code:`p`,
            the variance is :code:`(1 - p) / (p * p)`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            The lower bound of the support is always 0.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is infinite (which we approximate as :code:`Integer.MAX_VALUE`).
        
            Returns:
                upper bound of the support (always Integer.MAX_VALUE)
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> int: ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            The default implementation simply computes the logarithm of :code:`probability(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.IntegerDistribution.logProbability` in
                interface :class:`~org.hipparchus.distribution.IntegerDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution.logProbability` in
                class :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class HypergeometricDistribution(AbstractIntegerDistribution):
    """
    public classHypergeometricDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of the hypergeometric distribution.
    
        Also see:
    
              - `Hypergeometric distribution (Wikipedia) <http://en.wikipedia.org/wiki/Hypergeometric_distribution>`
              - `Hypergeometric distribution (MathWorld) <http://mathworld.wolfram.com/HypergeometricDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int, int3: int): ...
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
    def getNumberOfSuccesses(self) -> int:
        """
            Access the number of successes.
        
            Returns:
                the number of successes.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For population size :code:`N`, number of
            successes :code:`m`, and sample size :code:`n`, the mean is :code:`n * m / N`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For population size :code:`N`, number
            of successes :code:`m`, and sample size :code:`n`, the variance is :code:`[n * m * (N - n) * (N - m)] / [N^2 * (N -
            1)]`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            For population size :code:`N`, number of successes :code:`m`, and sample size :code:`n`, the lower bound of the support
            is :code:`max(0, n + m - N)`.
        
            Returns:
                lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            For number of successes :code:`m` and sample size :code:`n`, the upper bound of the support is :code:`min(m, n)`.
        
            Returns:
                upper bound of the support
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            The default implementation simply computes the logarithm of :code:`probability(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.IntegerDistribution.logProbability` in
                interface :class:`~org.hipparchus.distribution.IntegerDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution.logProbability` in
                class :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...
    def upperCumulativeProbability(self, int: int) -> float:
        """
            For this distribution, :code:`X`, this method returns :code:`P(X >= x)`.
        
            Parameters:
                x (int): Value at which the CDF is evaluated.
        
            Returns:
                the upper tail CDF for this distribution.
        
        
        """
        ...

class PascalDistribution(AbstractIntegerDistribution):
    """
    public classPascalDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of the Pascal distribution.
    
        The Pascal distribution is a special case of the Negative Binomial distribution where the number of successes parameter
        is an integer.
    
        There are various ways to express the probability mass and distribution functions for the Pascal distribution. The
        present implementation represents the distribution of the number of failures before :code:`r` successes occur. This is
        the convention adopted in e.g. `MathWorld <http://mathworld.wolfram.com/NegativeBinomialDistribution.html>`, but *not*
        in `Wikipedia <http://en.wikipedia.org/wiki/Negative_binomial_distribution>`.
    
        For a random variable :code:`X` whose values are distributed according to this distribution, the probability mass
        function is given by
    
    
        :code:`P(X = k) = C(k + r - 1, r - 1) * p^r * (1 - p)^k,`
    
    
        where :code:`r` is the number of successes, :code:`p` is the probability of success, and :code:`X` is the total number
        of failures. :code:`C(n, k)` is the binomial coefficient (:code:`n` choose :code:`k`). The mean and variance of
        :code:`X` are
    
    
        :code:`E(X) = (1 - p) * r / p, var(X) = (1 - p) * r / p^2.`
    
    
        Finally, the cumulative distribution function is given by
    
    
        :code:`P(X <= k) = I(p, r, k + 1)`, where I is the regularized incomplete Beta function.
    
        Also see:
    
              - ` Negative binomial distribution (Wikipedia) <http://en.wikipedia.org/wiki/Negative_binomial_distribution>`
              - ` Negative binomial distribution (MathWorld) <http://mathworld.wolfram.com/NegativeBinomialDistribution.html>`
              - :meth:`~serialized`
    """
    def __init__(self, int: int, double: float): ...
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
    def getNumberOfSuccesses(self) -> int:
        """
            Access the number of successes for this distribution.
        
            Returns:
                the number of successes.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For number of successes :code:`r` and
            probability of success :code:`p`, the mean is :code:`r * (1 - p) / p`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For number of successes :code:`r` and
            probability of success :code:`p`, the variance is :code:`r * (1 - p) / p^2`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
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
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            The lower bound of the support is always 0 no matter the parameters.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is always positive infinity no matter the parameters. Positive infinity is symbolized by
            :code:`Integer.MAX_VALUE`.
        
            Returns:
                upper bound of the support (always :code:`Integer.MAX_VALUE` for positive infinity)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            The default implementation simply computes the logarithm of :code:`probability(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.IntegerDistribution.logProbability` in
                interface :class:`~org.hipparchus.distribution.IntegerDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution.logProbability` in
                class :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class PoissonDistribution(AbstractIntegerDistribution):
    """
    public classPoissonDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of the Poisson distribution.
    
        Also see:
    
              - `Poisson distribution (Wikipedia) <http://en.wikipedia.org/wiki/Poisson_distribution>`
              - `Poisson distribution (MathWorld) <http://mathworld.wolfram.com/PoissonDistribution.html>`
              - :meth:`~serialized`
    """
    DEFAULT_MAX_ITERATIONS: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITERATIONS
    
        Default maximum number of iterations for cumulative probability calculations.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_EPSILON
    
        Default convergence criterion.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
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
    def getMean(self) -> float:
        """
            Get the mean for the distribution.
        
            Returns:
                the mean for the distribution.
        
        
        """
        ...
    def getNumericalMean(self) -> float:
        """
            Use this method to get the numerical value of the mean of this distribution. For mean parameter :code:`p`, the mean is
            :code:`p`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For mean parameter :code:`p`, the
            variance is :code:`p`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            The lower bound of the support is always 0 no matter the mean parameter.
        
            Returns:
                lower bound of the support (always 0)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is positive infinity, regardless of the parameter values. There is no integer infinity,
            so this method returns :code:`Integer.MAX_VALUE`.
        
            Returns:
                upper bound of the support (always :code:`Integer.MAX_VALUE` for positive infinity)
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            The default implementation simply computes the logarithm of :code:`probability(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.IntegerDistribution.logProbability` in
                interface :class:`~org.hipparchus.distribution.IntegerDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution.logProbability` in
                class :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    def normalApproximateProbability(self, int: int) -> float:
        """
            Calculates the Poisson distribution function using a normal approximation. The :code:`N(mean, sqrt(mean))` distribution
            is used to approximate the Poisson distribution. The computation uses "half-correction" (evaluating the normal
            distribution function at :code:`x + 0.5`).
        
            Parameters:
                x (int): Upper bound, inclusive.
        
            Returns:
                the distribution function value calculated using a normal approximation.
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class UniformIntegerDistribution(AbstractIntegerDistribution):
    """
    public classUniformIntegerDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of the uniform integer distribution.
    
        Also see:
    
              - ` Uniform distribution (discrete), at Wikipedia <http://en.wikipedia.org/wiki/Uniform_distribution_(discrete)>`
              - :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int): ...
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
            Use this method to get the numerical value of the mean of this distribution. For lower bound :code:`lower` and upper
            bound :code:`upper`, the mean is :code:`0.5 * (lower + upper)`.
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For lower bound :code:`lower` and upper
            bound :code:`upper`, and :code:`n = upper - lower + 1`, the variance is :code:`(n^2 - 1) / 12`.
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            The lower bound of the support is equal to the lower bound parameter of the distribution.
        
            Returns:
                lower bound of the support
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is equal to the upper bound parameter of the distribution.
        
            Returns:
                upper bound of the support
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
        """
        ...

class ZipfDistribution(AbstractIntegerDistribution):
    """
    public classZipfDistribution extends :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
    
        Implementation of the Zipf distribution.
    
        **Parameters:** For a random variable :code:`X` whose values are distributed according to this distribution, the
        probability mass function is given by
    
        .. code-block: java
        
           P(X = k) = H(N,s) * 1 / k^s    for k = 1,2,...,N.
         
    
        :code:`H(N,s)` is the normalizing constant which corresponds to the generalized harmonic number of order N of s.
    
          - :code:`N` is the number of elements
          - :code:`s` is the exponent
    
    
        Also see:
    
              - :class:`~org.hipparchus.distribution.discrete.https:.en.wikipedia.org.wiki.Zipf's_law`
              - :meth:`~org.hipparchus.distribution.discrete.https:.en.wikipedia.org.wiki.Harmonic_number#Generalized_harmonic_numbers`
              - :meth:`~serialized`
    """
    def __init__(self, int: int, double: float): ...
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
            Use this method to get the numerical value of the mean of this distribution. For number of elements :code:`N` and
            exponent :code:`s`, the mean is :code:`Hs1 / Hs`, where
        
              - :code:`Hs1 = generalizedHarmonic(N, s - 1)`,
              - :code:`Hs = generalizedHarmonic(N, s)`.
        
        
            Returns:
                the mean or :code:`Double.NaN` if it is not defined
        
        
        """
        ...
    def getNumericalVariance(self) -> float:
        """
            Use this method to get the numerical value of the variance of this distribution. For number of elements :code:`N` and
            exponent :code:`s`, the mean is :code:`(Hs2 / Hs) - (Hs1^2 / Hs^2)`, where
        
              - :code:`Hs2 = generalizedHarmonic(N, s - 2)`,
              - :code:`Hs1 = generalizedHarmonic(N, s - 1)`,
              - :code:`Hs = generalizedHarmonic(N, s)`.
        
        
            Returns:
                the variance (possibly :code:`Double.POSITIVE_INFINITY` or :code:`Double.NaN` if it is not defined)
        
        
        """
        ...
    def getSupportLowerBound(self) -> int:
        """
            Access the lower bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(0)`. In other words, this method must return
        
            :code:`inf {x in Z | P(X <= x) > 0}`.
            The lower bound of the support is always 1 no matter the parameters.
        
            Returns:
                lower bound of the support (always 1)
        
        
        """
        ...
    def getSupportUpperBound(self) -> int:
        """
            Access the upper bound of the support. This method must return the same value as
            :code:`inverseCumulativeProbability(1)`. In other words, this method must return
        
            :code:`inf {x in R | P(X <= x) = 1}`.
            The upper bound of the support is the number of elements.
        
            Returns:
                upper bound of the support
        
        
        """
        ...
    def isSupportConnected(self) -> bool:
        """
            Use this method to get information about whether the support is connected, i.e. whether all integers between the lower
            and upper bound of the support are included in the support. The support of this distribution is connected.
        
            Returns:
                :code:`true`
        
        
        """
        ...
    def logProbability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`log(P(X = x))`, where :code:`log` is the natural logarithm. In other words, this method represents the logarithm
            of the probability mass function (PMF) for the distribution. Note that due to the floating point precision and
            under/overflow issues, this method will for some distributions be more precise and faster than computing the logarithm
            of :meth:`~org.hipparchus.distribution.IntegerDistribution.probability`.
        
            The default implementation simply computes the logarithm of :code:`probability(x)`.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.IntegerDistribution.logProbability` in
                interface :class:`~org.hipparchus.distribution.IntegerDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution.logProbability` in
                class :class:`~org.hipparchus.distribution.discrete.AbstractIntegerDistribution`
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the logarithm of the value of the probability mass function at :code:`x`
        
        
        """
        ...
    @typing.overload
    def probability(self, int: int, int2: int) -> float: ...
    @typing.overload
    def probability(self, int: int) -> float:
        """
            For a random variable :code:`X` whose values are distributed according to this distribution, this method returns
            :code:`P(X = x)`. In other words, this method represents the probability mass function (PMF) for the distribution.
        
            Parameters:
                x (int): the point at which the PMF is evaluated
        
            Returns:
                the value of the probability mass function at :code:`x`
        
        
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
