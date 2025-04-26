
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.net
import java.util
import jpype
import jpype.protocol
import org.hipparchus.distribution.continuous
import org.hipparchus.distribution.multivariate
import org.hipparchus.random
import org.hipparchus.stat.descriptive
import typing



class EmpiricalDistribution(org.hipparchus.distribution.continuous.AbstractRealDistribution):
    """
    public classEmpiricalDistribution extends :class:`~org.hipparchus.stat.fitting.https:.www.hipparchus.org.hipparchus`
    
    
        Represents an ` empirical probability distribution
        <http://http://en.wikipedia.org/wiki/Empirical_distribution_function>` -- a probability distribution derived from
        observed data without making any assumptions about the functional form of the population distribution that the data come
        from.
    
        An :code:`EmpiricalDistribution` maintains data structures, called *distribution digests*, that describe empirical
        distributions and support the following operations:
    
          - loading the distribution from a file of observed data values
          - dividing the input data into "bin ranges" and reporting bin frequency counts (data for histogram)
          - reporting univariate statistics describing the full set of data values as well as the observations within each bin
          - generating random values from the distribution
    
    
        Applications can use :code:`EmpiricalDistribution` to build grouped frequency histograms representing the input data or
        to generate random values "like" those in the input file -- i.e., the values generated will follow the distribution of
        the values in the file.
    
        The implementation uses what amounts to the ` Variable Kernel Method
        <http://nedwww.ipac.caltech.edu/level5/March02/Silverman/Silver2_6.html>` with Gaussian smoothing:
    
        **Digesting the input file**
    
          1.  Pass the file once to compute min and max.
          2.  Divide the range from min-max into :code:`binCount` "bins."
          3.  Pass the data file again, computing bin counts and univariate statistics (mean, std dev.) for each of the bins
          4.  Divide the interval (0,1) into subintervals associated with the bins, with the length of a bin's subinterval
            proportional to its count.
    
        **Generating random values from the distribution**
    
          1.  Generate a uniformly distributed value in (0,1)
          2.  Select the subinterval to which the value belongs.
          3.  Generate a random Gaussian value with mean = mean of the associated bin and std dev = std dev of associated bin.
    
    
        EmpiricalDistribution implements the :class:`~org.hipparchus.stat.fitting.https:.www.hipparchus.org.hipparchus`
        interface as follows. Given x within the range of values in the dataset, let B be the bin containing x and let K be the
        within-bin kernel for B. Let P(B-) be the sum of the probabilities of the bins below B and let K(B) be the mass of B
        under K (i.e., the integral of the kernel density over B). Then set P(X < x) = P(B-) + P(B) * K(x) / K(B) where K(x) is
        the kernel distribution evaluated at x. This results in a cdf that matches the grouped frequency distribution at the bin
        endpoints and interpolates within bins using within-bin kernels.
    
        **USAGE NOTES:**
    
          - The :code:`binCount` is set by default to 1000. A good rule of thumb is to set the bin count to approximately the length
            of the input file divided by 10.
          - The input file *must* be a plain text file containing one valid numeric entry per line.
    
    
        Also see:
    
              - :meth:`~serialized`
    """
    DEFAULT_BIN_COUNT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_BIN_COUNT
    
        Default bin count
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    def cumulativeProbability(self, double: float) -> float:
        """
        
            Algorithm description:
        
              1.  Find the bin B that x belongs to.
              2.  Compute P(B) = the mass of B and P(B-) = the combined mass of the bins below B.
              3.  Compute K(B) = the probability mass of B with respect to the within-bin kernel and K(B-) = the kernel distribution
                evaluated at the lower endpoint of B
              4.  Return P(B-) + P(B) * [K(x) - K(B-)] / K(B) where K(x) is the within-bin kernel distribution function evaluated at x.
        
        
            If K is a constant distribution, we return P(B-) + P(B) (counting the full mass of B).
        
        """
        ...
    def density(self, double: float) -> float:
        """
        
            Returns the kernel density normalized so that its integral over each bin equals the bin mass.
        
            Algorithm description:
        
              1.  Find the bin B that x belongs to.
              2.  Compute K(B) = the mass of B with respect to the within-bin kernel (i.e., the integral of the kernel density over B).
              3.  Return k(x) * P(B) / K(B), where k is the within-bin kernel density and P(B) is the mass of B.
        
        
        """
        ...
    def getBinCount(self) -> int:
        """
            Returns the number of bins.
        
            Returns:
                the number of bins.
        
        
        """
        ...
    def getBinStats(self) -> java.util.List[org.hipparchus.stat.descriptive.StreamingStatistics]: ...
    def getGeneratorUpperBounds(self) -> typing.MutableSequence[float]:
        """
        
            Returns a fresh copy of the array of upper bounds of the subintervals of [0,1] used in generating data from the
            empirical distribution. Subintervals correspond to bins with lengths proportional to bin counts.
            **Preconditions:**
        
              - the distribution must be loaded before invoking this method
        
        
            Returns:
                array of upper bounds of subintervals used in data generation
        
            Raises:
                :class:`~org.hipparchus.stat.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: unless a :code:`load` method has been called beforehand.
        
        
        """
        ...
    def getNextValue(self) -> float: ...
    def getNumericalMean(self) -> float: ...
    def getNumericalVariance(self) -> float: ...
    def getSampleStats(self) -> org.hipparchus.stat.descriptive.StatisticalSummary:
        """
            Returns a :class:`~org.hipparchus.stat.descriptive.StatisticalSummary` describing this distribution. **Preconditions:**
        
              - the distribution must be loaded before invoking this method
        
        
            Returns:
                the sample statistics
        
            Raises:
                :class:`~org.hipparchus.stat.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalStateException`: if the distribution has not been loaded
        
        
        """
        ...
    def getSupportLowerBound(self) -> float: ...
    def getSupportUpperBound(self) -> float: ...
    def getUpperBounds(self) -> typing.MutableSequence[float]:
        """
        
            Returns a fresh copy of the array of upper bounds for the bins. Bins are:
        
        
            [min,upperBounds[0]],(upperBounds[0],upperBounds[1]],..., (upperBounds[binCount-2], upperBounds[binCount-1] = max].
        
            Returns:
                array of bin upper bounds
        
        
        """
        ...
    def inverseCumulativeProbability(self, double: float) -> float: ...
    def isLoaded(self) -> bool:
        """
            Property indicating whether or not the distribution has been loaded.
        
            Returns:
                true if the distribution has been loaded
        
        
        """
        ...
    def isSupportConnected(self) -> bool: ...
    @typing.overload
    def load(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    def load(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    @typing.overload
    def load(self, uRL: java.net.URL) -> None: ...
    def reSeed(self, long: int) -> None:
        """
            Reseeds the random number generator used by :meth:`~org.hipparchus.stat.fitting.EmpiricalDistribution.getNextValue`.
        
            Parameters:
                seed (long): random generator seed
        
        
        """
        ...
    def reseedRandomGenerator(self, long: int) -> None:
        """
            Reseed the underlying PRNG.
        
            Parameters:
                seed (long): new seed value
        
        
        """
        ...

class MultivariateNormalMixtureExpectationMaximization:
    """
    public classMultivariateNormalMixtureExpectationMaximization extends :class:`~org.hipparchus.stat.fitting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Expectation-Maximization algorithm for fitting the parameters of multivariate normal mixture model distributions. This
        implementation is pure original code based on
        :class:`~org.hipparchus.stat.fitting.https:.www.ee.washington.edu.techsite.papers.documents.UWEETR` by Yihua Chen and
        Maya R. Gupta, Department of Electrical Engineering, University of Washington, Seattle, WA 98195. It was verified using
        external tools like `CRAN Mixtools <http://cran.r-project.org/web/packages/mixtools/index.html>` (see the JUnit test
        cases) but it is **not** based on Mixtools code at all. The discussion of the origin of this class can be seen in the
        comments of the :class:`~org.hipparchus.stat.fitting.https:.issues.apache.org.jira.browse.MATH` JIRA issue.
    """
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @staticmethod
    def estimate(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], int: int) -> org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution: ...
    @typing.overload
    def fit(self, mixtureMultivariateNormalDistribution: org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution) -> None: ...
    @typing.overload
    def fit(self, mixtureMultivariateNormalDistribution: org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution, int: int, double: float) -> None: ...
    def getFittedModel(self) -> org.hipparchus.distribution.multivariate.MixtureMultivariateNormalDistribution:
        """
            Gets the fitted model.
        
            Returns:
                fitted model or :code:`null` if no fit has been performed yet.
        
        
        """
        ...
    def getLogLikelihood(self) -> float:
        """
            Gets the log likelihood of the data under the fitted model.
        
            Returns:
                Log likelihood of data or zero of no data has been fit
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.fitting")``.

    EmpiricalDistribution: typing.Type[EmpiricalDistribution]
    MultivariateNormalMixtureExpectationMaximization: typing.Type[MultivariateNormalMixtureExpectationMaximization]
