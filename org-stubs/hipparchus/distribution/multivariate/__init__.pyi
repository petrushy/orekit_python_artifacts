import java.util
import org.hipparchus.distribution
import org.hipparchus.linear
import org.hipparchus.random
import org.hipparchus.util
import typing



class AbstractMultivariateRealDistribution(org.hipparchus.distribution.MultivariateRealDistribution):
    """
    public abstract class AbstractMultivariateRealDistribution extends Object implements :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
    
        Base class for multivariate probability distributions.
    """
    def getDimension(self) -> int:
        """
            Gets the number of random variables of the distribution. It is the size of the array returned by the
            :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample` method.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.getDimension`Â in
                interfaceÂ :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Returns:
                the number of variables.
        
        
        """
        ...
    def reseedRandomGenerator(self, long: int) -> None:
        """
            Reseeds the random generator used to generate samples.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.reseedRandomGenerator`Â in
                interfaceÂ :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Parameters:
                seed (long): Seed with which to initialize the random number generator.
        
        
        """
        ...
    @typing.overload
    def sample(self) -> typing.List[float]:
        """
            Generates a random value vector sampled from this distribution.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample`Â in
                interfaceÂ :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Returns:
                a random value vector.
        
        """
        ...
    @typing.overload
    def sample(self, int: int) -> typing.List[typing.List[float]]:
        """
            Generates a list of a random value vectors from the distribution.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample`Â in
                interfaceÂ :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Parameters:
                sampleSize (int): the number of random vectors to generate.
        
            Returns:
                an array representing the random samples.
        
            Also see:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample`
        
        
        """
        ...

_MixtureMultivariateRealDistribution__T = typing.TypeVar('_MixtureMultivariateRealDistribution__T', bound=org.hipparchus.distribution.MultivariateRealDistribution)  # <T>
class MixtureMultivariateRealDistribution(AbstractMultivariateRealDistribution, typing.Generic[_MixtureMultivariateRealDistribution__T]):
    """
    public class MixtureMultivariateRealDistribution<T extends :class:`~org.hipparchus.distribution.MultivariateRealDistribution`> extends :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
    
        Class for representing ` mixture model <http://en.wikipedia.org/wiki/Mixture_model>` distributions.
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, list: java.util.List[org.hipparchus.util.Pair[float, _MixtureMultivariateRealDistribution__T]]): ...
    def density(self, doubleArray: typing.List[float]) -> float:
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
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.reseedRandomGenerator`Â in
                interfaceÂ :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Overrides:
                :meth:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution.reseedRandomGenerator`Â in
                classÂ :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
        
            Parameters:
                seed (long): Seed with which to initialize the random number generator.
        
        
        """
        ...
    @typing.overload
    def sample(self) -> typing.List[float]:
        """
            Generates a random value vector sampled from this distribution.
        
            Specified by:
                :meth:`~org.hipparchus.distribution.MultivariateRealDistribution.sample`Â in
                interfaceÂ :class:`~org.hipparchus.distribution.MultivariateRealDistribution`
        
            Specified by:
                :meth:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution.sample`Â in
                classÂ :class:`~org.hipparchus.distribution.multivariate.AbstractMultivariateRealDistribution`
        
            Returns:
                a random value vector.
        
        
        """
        ...
    @typing.overload
    def sample(self, int: int) -> typing.List[typing.List[float]]: ...

class MultivariateNormalDistribution(AbstractMultivariateRealDistribution):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], double3: float): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], double3: float): ...
    def density(self, doubleArray: typing.List[float]) -> float: ...
    def getCovariances(self) -> org.hipparchus.linear.RealMatrix: ...
    def getMeans(self) -> typing.List[float]: ...
    def getSingularMatrixCheckTolerance(self) -> float: ...
    def getStandardDeviations(self) -> typing.List[float]: ...
    @typing.overload
    def sample(self) -> typing.List[float]: ...
    @typing.overload
    def sample(self, int: int) -> typing.List[typing.List[float]]: ...

class MixtureMultivariateNormalDistribution(MixtureMultivariateRealDistribution[MultivariateNormalDistribution]):
    """
    public class MixtureMultivariateNormalDistribution extends :class:`~org.hipparchus.distribution.multivariate.MixtureMultivariateRealDistribution`<:class:`~org.hipparchus.distribution.multivariate.MultivariateNormalDistribution`>
    
        Multivariate normal mixture distribution. This class is mainly syntactic sugar.
    
        Also see:
            :class:`~org.hipparchus.distribution.multivariate.MixtureMultivariateRealDistribution`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[typing.List[typing.List[float]]]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.hipparchus.util.Pair[float, MultivariateNormalDistribution]]): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator, list: java.util.List[org.hipparchus.util.Pair[float, MultivariateNormalDistribution]]): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.distribution.multivariate")``.

    AbstractMultivariateRealDistribution: typing.Type[AbstractMultivariateRealDistribution]
    MixtureMultivariateNormalDistribution: typing.Type[MixtureMultivariateNormalDistribution]
    MixtureMultivariateRealDistribution: typing.Type[MixtureMultivariateRealDistribution]
    MultivariateNormalDistribution: typing.Type[MultivariateNormalDistribution]
