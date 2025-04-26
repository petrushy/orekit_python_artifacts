
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus.distribution
import org.hipparchus.linear
import org.hipparchus.random
import org.hipparchus.util
import typing



class AbstractMultivariateRealDistribution(org.hipparchus.distribution.MultivariateRealDistribution):
    """
    public abstract classAbstractMultivariateRealDistribution extends :class:`~org.hipparchus.distribution.multivariate.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
    
        Base class for multivariate probability distributions.
    """
    def getDimension(self) -> int:
        """
            Gets the number of random variables of the distribution. It is the size of the array returned by the
            :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample` method.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.getDimension` in
                interface :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Returns:
                the number of variables.
        
        
        """
        ...
    def reseedRandomGenerator(self, long: int) -> None:
        """
            Reseeds the random generator used to generate samples.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.reseedRandomGenerator` in
                interface :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Parameters:
                seed (long): Seed with which to initialize the random number generator.
        
        
        """
        ...
    @typing.overload
    def sample(self) -> typing.MutableSequence[float]:
        """
            Generates a random value vector sampled from this distribution.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample` in
                interface :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Returns:
                a random value vector.
        
        """
        ...
    @typing.overload
    def sample(self, int: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Generates a list of a random value vectors from the distribution.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample` in
                interface :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Parameters:
                sampleSize (int): the number of random vectors to generate.
        
            Returns:
                an array representing the random samples.
        
            Also see:
        
                  - :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample`
        
        
        
        """
        ...

_MixtureMultivariateRealDistribution__T = typing.TypeVar('_MixtureMultivariateRealDistribution__T', bound=org.hipparchus.distribution.MultivariateRealDistribution)  # <T>
class MixtureMultivariateRealDistribution(AbstractMultivariateRealDistribution, typing.Generic[_MixtureMultivariateRealDistribution__T]):
    """
    public classMixtureMultivariateRealDistribution<T extends :class:`~org.hipparchus.distribution.MultivariateRealDistribution`> extends :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
    
        Class for representing ` mixture model <http://en.wikipedia.org/wiki/Mixture_model>` distributions.
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, list: java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]): ...
    def density(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Returns the probability density function (PDF) of this distribution evaluated at the specified point :code:`x`. In
            general, the PDF is the derivative of the cumulative distribution function. If the derivative does not exist at
            :code:`x`, then an appropriate replacement should be returned, e.g. :code:`Double.POSITIVE_INFINITY`,
            :code:`Double.NaN`, or the limit inferior or limit superior of the difference quotient.
        
            Parameters:
                values (double[]): Point at which the PDF is evaluated.
        
            Returns:
                the value of the probability density function at point :code:`x`.
        
        
        """
        ...
    def getComponents(self) -> java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]: ...
    def reseedRandomGenerator(self, long: int) -> None:
        """
            Reseeds the random generator used to generate samples.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.reseedRandomGenerator` in
                interface :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution.reseedRandomGenerator` in
                class :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
        
            Parameters:
                seed (long): Seed with which to initialize the random number generator.
        
        
        """
        ...
    @typing.overload
    def sample(self) -> typing.MutableSequence[float]:
        """
            Generates a random value vector sampled from this distribution.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample` in
                interface :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Specified by:
                :meth:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution.sample` in
                class :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
        
            Returns:
                a random value vector.
        
        
        """
        ...
    @typing.overload
    def sample(self, int: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

class MultivariateNormalDistribution(AbstractMultivariateRealDistribution):
    """
    public classMultivariateNormalDistribution extends :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
    
        Implementation of the multivariate normal (Gaussian) distribution.
    
        Also see:
    
              - ` Multivariate normal distribution (Wikipedia) <http://en.wikipedia.org/wiki/Multivariate_normal_distribution>`
              - ` Multivariate normal distribution (MathWorld) <http://mathworld.wolfram.com/MultivariateNormalDistribution.html>`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double3: float): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double3: float): ...
    def density(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    def getCovariances(self) -> org.hipparchus.linear.RealMatrix:
        """
            Gets the covariance matrix.
        
            Returns:
                the covariance matrix.
        
        
        """
        ...
    def getMeans(self) -> typing.MutableSequence[float]:
        """
            Gets the mean vector.
        
            Returns:
                the mean vector.
        
        
        """
        ...
    def getSingularMatrixCheckTolerance(self) -> float:
        """
            Gets the current setting for the tolerance check used during singular checks before inversion
        
            Returns:
                tolerance
        
        
        """
        ...
    def getStandardDeviations(self) -> typing.MutableSequence[float]:
        """
            Gets the square root of each element on the diagonal of the covariance matrix.
        
            Returns:
                the standard deviations.
        
        
        """
        ...
    @typing.overload
    def sample(self) -> typing.MutableSequence[float]:
        """
            Generates a random value vector sampled from this distribution.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample` in
                interface :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Specified by:
                :meth:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution.sample` in
                class :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
        
            Returns:
                a random value vector.
        
        
        """
        ...
    @typing.overload
    def sample(self, int: int) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

class MixtureMultivariateNormalDistribution(MixtureMultivariateRealDistribution[MultivariateNormalDistribution]):
    """
    public classMixtureMultivariateNormalDistribution extends :class:`~org.hipparchus.distribution.multivariate.MixtureMultivariateRealDistribution`<:class:`~org.hipparchus.distribution.multivariate.MultivariateNormalDistribution`>
    
        Multivariate normal mixture distribution. This class is mainly syntactic sugar.
    
        Also see:
    
              - :class:`~org.hipparchus.distribution.multivariate.MixtureMultivariateRealDistribution`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], doubleArray3: typing.Union[typing.List[typing.MutableSequence[typing.MutableSequence[float]]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.hipparchus.util.Pair[float, MultivariateNormalDistribution]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, list: java.util.List[org.hipparchus.util.Pair[float, MultivariateNormalDistribution]]): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.distribution.multivariate")``.

    AbstractMultivariateRealDistribution: typing.Type[AbstractMultivariateRealDistribution]
    MixtureMultivariateNormalDistribution: typing.Type[MixtureMultivariateNormalDistribution]
    MixtureMultivariateRealDistribution: typing.Type[MixtureMultivariateRealDistribution]
    MultivariateNormalDistribution: typing.Type[MultivariateNormalDistribution]
