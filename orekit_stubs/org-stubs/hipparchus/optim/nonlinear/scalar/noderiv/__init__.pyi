
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar
import org.hipparchus.random
import typing



class AbstractSimplex(org.hipparchus.optim.OptimizationData):
    """
    This class implements the simplex concept. It is intended to be used in conjunction with SimplexOptimizer.
    
    The initial configuration of the simplex is set by the constructors or . The other will set all steps to 1, thus building a default configuration from a unit hypercube.
    
    Users must call the build method in order to create the data structure that will be acted on by the other methods of this class.
    
    Also see:
        SimplexOptimizer
    """
    def build(self, startPoint: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Build an initial simplex.
        
        Parameters:
            startPoint (double[]): First point of the simplex.
        
        Raises:
            hipparchus: if the start point does not match simplex dimension.
        
        
        """
        ...
    def evaluate(self, evaluationFunction: typing.Union[org.hipparchus.analysis.MultivariateFunction, typing.Callable], comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None:
        """
        Evaluate all the non-evaluated points of the simplex.
        
        Parameters:
            evaluationFunction (hipparchus): Evaluation function.
            comparator (Comparator<PointValuePair> comparator): Comparator to use to sort simplex vertices from best to worst.
        
        Raises:
            hipparchus: if the maximal number of evaluations is exceeded.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get simplex dimension.
        
        Returns:
            the dimension of the simplex.
        
        
        """
        ...
    def getPoint(self, index: int) -> org.hipparchus.optim.PointValuePair:
        """
        Get the simplex point stored at the requested index.
        
        Parameters:
            index (int): Location.
        
        Returns:
            the point at location index.
        
        
        """
        ...
    def getPoints(self) -> typing.MutableSequence[org.hipparchus.optim.PointValuePair]:
        """
        Get the points of the simplex.
        
        Returns:
            all the simplex points.
        
        
        """
        ...
    def getSize(self) -> int:
        """
        Get simplex size. After calling the build method, this method will will be equivalent to getDimension() + 1.
        
        Returns:
            the size of the simplex.
        
        
        """
        ...
    def iterate(self, evaluationFunction: typing.Union[org.hipparchus.analysis.MultivariateFunction, typing.Callable], comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None:
        """
        Compute the next simplex of the algorithm.
        
        Parameters:
            evaluationFunction (hipparchus): Evaluation function.
            comparator (Comparator<PointValuePair> comparator): Comparator to use to sort simplex vertices from best to worst.
        
        Raises:
            hipparchus: if the algorithm fails to converge.
        
        
        """
        ...

class BOBYQAOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    """
    Powell's BOBYQA algorithm. This implementation is translated and adapted from the Fortran version available `here <http://plato.asu.edu/ftp/other_software/bobyqa.zip>`. See ` this paper <http://www.optimization-online.org/DB_HTML/2010/05/2616.html>` for an introduction.
    
    BOBYQA is particularly well suited for high dimensional problems where derivatives are not available. In most cases it outperforms the PowellOptimizer significantly. Stochastic algorithms like CMAESOptimizer succeed more often than BOBYQA, but are more expensive. BOBYQA could also be considered as a replacement of any derivative-based optimizer when the derivatives are approximated by finite differences.
    """
    MINIMUM_PROBLEM_DIMENSION: typing.ClassVar[int] = ...
    """
    Minimum dimension of the problem: 2
    
    Also see:
        constant
    
    
    """
    DEFAULT_INITIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Default value for initialTrustRegionRadius: 10.0 .
    
    Also see:
        constant
    
    
    """
    DEFAULT_STOPPING_RADIUS: typing.ClassVar[float] = ...
    """
    Default value for stoppingTrustRegionRadius: 1.0E-8 .
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, numberOfInterpolationPoints: int): ...
    @typing.overload
    def __init__(self, numberOfInterpolationPoints: int, initialTrustRegionRadius: float, stoppingTrustRegionRadius: float): ...

class CMAESOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    """
    An implementation of the active Covariance Matrix Adaptation Evolution Strategy (CMA-ES) for non-linear, non-convex, non-smooth, global function minimization.
    
    The CMA-Evolution Strategy (CMA-ES) is a reliable stochastic optimization method which should be applied if derivative-based methods, e.g. quasi-Newton BFGS or conjugate gradient, fail due to a rugged search landscape (e.g. noise, local optima, outlier, etc.) of the objective function. Like a quasi-Newton method, the CMA-ES learns and applies a variable metric on the underlying search space. Unlike a quasi-Newton method, the CMA-ES neither estimates nor uses gradients, making it considerably more reliable in terms of finding a good, or even close to optimal, solution.
    
    In general, on smooth objective functions the CMA-ES is roughly ten times slower than BFGS (counting objective function evaluations, no gradients provided). For up to \(n=10\) variables also the derivative-free simplex direct search method (Nelder and Mead) can be faster, but it is far less reliable than CMA-ES.
    
    The CMA-ES is particularly well suited for non-separable and/or badly conditioned problems. To observe the advantage of CMA compared to a conventional evolution strategy, it will usually take about \(30 n\) function evaluations. On difficult problems the complete optimization (a single run) is expected to take roughly between \(30 n\) and \(300 n^2\) function evaluations.
    
    This implementation is translated and adapted from the Matlab version of the CMA-ES algorithm as implemented in module m version 3.51.
    
    For more information, please refer to the following links:
    
      - `Matlab code <http://www.lri.fr/~hansen/cmaes.m>`
      - `Introduction to CMA-ES <http://www.lri.fr/~hansen/cmaesintro.html>`
      - `Wikipedia <http://en.wikipedia.org/wiki/CMA-ES>`
    """
    def __init__(self, maxIterations: int, stopFitness: float, isActiveCMA: bool, diagonalOnly: int, checkFeasableCount: int, random: org.hipparchus.random.RandomGenerator, generateStatistics: bool, checker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], typing.Callable[[int, org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], bool]]):
        """
        Simple constructor.
        
        Parameters:
            maxIterations (int): Maximal number of iterations.
            stopFitness (double): Whether to stop if objective function value is smaller than stopFitness.
            isActiveCMA (boolean): Chooses the covariance matrix update method.
            diagonalOnly (int): Number of initial iterations, where the covariance matrix remains diagonal.
            checkFeasableCount (int): Determines how often new random objective variables are generated in case they are out of bounds.
            random (hipparchus): Random generator.
            generateStatistics (boolean): Whether statistic data is collected.
            checker (ConvergenceChecker<PointValuePair> checker): Convergence checker.
        
        
        """
        ...
    def getStatisticsDHistory(self) -> java.util.List[org.hipparchus.linear.RealMatrix]:
        """
        Get history of D matrix.
        
        Returns:
            History of D matrix
        
        
        """
        ...
    def getStatisticsFitnessHistory(self) -> java.util.List[float]:
        """
        Get history of fitness values.
        
        Returns:
            History of fitness values
        
        
        """
        ...
    def getStatisticsMeanHistory(self) -> java.util.List[org.hipparchus.linear.RealMatrix]:
        """
        Get history of mean matrix.
        
        Returns:
            History of mean matrix
        
        
        """
        ...
    def getStatisticsSigmaHistory(self) -> java.util.List[float]:
        """
        Get history of sigma values.
        
        Returns:
            History of sigma values
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...
    class PopulationSize(org.hipparchus.optim.OptimizationData):
        def __init__(self, int: int): ...
        def getPopulationSize(self) -> int: ...
    class Sigma(org.hipparchus.optim.OptimizationData):
        def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
        def getSigma(self) -> typing.MutableSequence[float]: ...

class PowellOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    """
    Powell's algorithm. This code is translated and adapted from the Python version of this algorithm (as implemented in module py v0.5 of SciPy).
    
    The default stopping criterion is based on the differences of the function value between two successive iterations. It is however possible to define a custom convergence checker that might terminate the algorithm earlier.
    
    Line search is performed by the LineSearch class.
    
    Constraints are not supported: the call to optimize optimize} will throw hipparchus if bounds are passed to it. In order to impose simple constraints, the objective function must be wrapped in an adapter like MultivariateFunctionMappingAdapter or MultivariateFunctionPenaltyAdapter.
    """
    @typing.overload
    def __init__(self, rel: float, abs: float): ...
    @typing.overload
    def __init__(self, rel: float, abs: float, lineRel: float, lineAbs: float): ...
    @typing.overload
    def __init__(self, rel: float, abs: float, lineRel: float, lineAbs: float, checker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], typing.Callable[[int, org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], bool]]): ...
    @typing.overload
    def __init__(self, rel: float, abs: float, checker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], typing.Callable[[int, org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], bool]]): ...

class SimplexOptimizer(org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer):
    """
    This class implements simplex-based direct search optimization.
    
    Direct search methods only use objective function values, they do not need derivatives and don't either try to compute approximation of the derivatives. According to a 1996 paper by Margaret H. Wright (`Direct Search Methods: Once Scorned, Now Respectable <http://cm.bell-labs.com/cm/cs/doc/96/4-02.ps.gz>`), they are used when either the computation of the derivative is impossible (noisy functions, unpredictable discontinuities) or difficult (complexity, computation cost). In the first cases, rather than an optimum, a not too bad point is desired. In the latter cases, an optimum is desired but cannot be reasonably found. In all cases direct search methods can be useful.
    
    Simplex-based direct search methods are based on comparison of the objective function values at the vertices of a simplex (which is a set of n+1 points in dimension n) that is updated by the algorithms steps.
    
    The simplex update procedure (NelderMeadSimplex or MultiDirectionalSimplex) must be passed to the optimize method.
    
    Each call to optimize will re-use the start configuration of the current simplex and move it such that its first vertex is at the provided start point of the optimization. If the optimize method is called to solve a different problem and the number of parameters change, the simplex must be re-initialized to one with the appropriate dimensions.
    
    Convergence is checked by providing the worst points of previous and current simplex to the convergence checker, not the best ones.
    
    This simplex optimizer implementation does not directly support constrained optimization with simple bounds; so, for such optimizations, either a more dedicated algorithm must be used like CMAESOptimizer or BOBYQAOptimizer, or the objective function must be wrapped in an adapter like MultivariateFunctionMappingAdapter or MultivariateFunctionPenaltyAdapter.
    
    The call to optimize will throw hipparchus if bounds are passed to it.
    """
    @typing.overload
    def __init__(self, rel: float, abs: float): ...
    @typing.overload
    def __init__(self, checker: typing.Union[org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], typing.Callable[[int, org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], bool]]): ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair:
        """
        Stores data and performs the optimization.
        
        The list of parameters is open-ended so that sub-classes can extend it with arguments specific to their concrete implementations.
        
        When the method is called multiple times, instance data is overwritten only when actually present in the list of arguments: when not specified, data set in a previous call is retained (and thus is optional in subsequent calls).
        
        Important note: Subclasses must override parseOptimizationData if they need to register their own options; but then, they must also call parseOptimizationData(optData) within that method.
        
        Overrides: optimize in class MultivariateOptimizer
        
        Parameters:
            optData (OptimizationData...): Optimization data. In addition to those documented in
                parseOptimizationData, this method will register
                the following data:
        
                  - AbstractSimplex
        
        
        Returns:
            a point/value pair that satisfies the convergence criteria.
        
        
        """
        ...

class MultiDirectionalSimplex(AbstractSimplex):
    """
    This class implements the multi-directional direct search method.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, double3: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float, double3: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, n: int, sideLength: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, n: int, sideLength: float, khi: float, gamma: float): ...
    def iterate(self, evaluationFunction: typing.Union[org.hipparchus.analysis.MultivariateFunction, typing.Callable], comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None:
        """
        Compute the next simplex of the algorithm.
        
        Specified by: iterate in class AbstractSimplex
        
        Parameters:
            evaluationFunction (hipparchus): Evaluation function.
            comparator (Comparator<PointValuePair> comparator): Comparator to use to sort simplex vertices from best to worst.
        
        
        """
        ...

class NelderMeadSimplex(AbstractSimplex):
    """
    This class implements the Nelder-Mead simplex algorithm.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, n: int, sideLength: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, n: int, sideLength: float, rho: float, khi: float, gamma: float, sigma: float): ...
    def iterate(self, evaluationFunction: typing.Union[org.hipparchus.analysis.MultivariateFunction, typing.Callable], comparator: typing.Union[java.util.Comparator[org.hipparchus.optim.PointValuePair], typing.Callable[[org.hipparchus.optim.PointValuePair, org.hipparchus.optim.PointValuePair], int]]) -> None:
        """
        Compute the next simplex of the algorithm.
        
        Specified by: iterate in class AbstractSimplex
        
        Parameters:
            evaluationFunction (hipparchus): Evaluation function.
            comparator (Comparator<PointValuePair> comparator): Comparator to use to sort simplex vertices from best to worst.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.scalar.noderiv")``.

    AbstractSimplex: typing.Type[AbstractSimplex]
    BOBYQAOptimizer: typing.Type[BOBYQAOptimizer]
    CMAESOptimizer: typing.Type[CMAESOptimizer]
    MultiDirectionalSimplex: typing.Type[MultiDirectionalSimplex]
    NelderMeadSimplex: typing.Type[NelderMeadSimplex]
    PowellOptimizer: typing.Type[PowellOptimizer]
    SimplexOptimizer: typing.Type[SimplexOptimizer]
