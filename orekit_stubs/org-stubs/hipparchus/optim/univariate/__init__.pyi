
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import org.hipparchus.analysis
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar
import org.hipparchus.random
import typing



class BracketFinder:
    """
    public classBracketFinder extends :class:`~org.hipparchus.optim.univariate.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Provide an interval that brackets a local optimum of a function. This code is based on a Python implementation (from
        *SciPy*, module :code:`optimize.py` v0.5).
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    def getEvaluations(self) -> int:
        """
            Get number of evaluations.
        
            Returns:
                the number of evaluations
        
        
        """
        ...
    def getFHi(self) -> float:
        """
            Get function value at :meth:`~org.hipparchus.optim.univariate.BracketFinder.getHi`.
        
            Returns:
                function value at :meth:`~org.hipparchus.optim.univariate.BracketFinder.getHi`
        
        
        """
        ...
    def getFLo(self) -> float:
        """
            Get function value at :meth:`~org.hipparchus.optim.univariate.BracketFinder.getLo`.
        
            Returns:
                function value at :meth:`~org.hipparchus.optim.univariate.BracketFinder.getLo`
        
        
        """
        ...
    def getFMid(self) -> float:
        """
            Get function value at :meth:`~org.hipparchus.optim.univariate.BracketFinder.getMid`.
        
            Returns:
                function value at :meth:`~org.hipparchus.optim.univariate.BracketFinder.getMid`
        
        
        """
        ...
    def getHi(self) -> float:
        """
            Get higher bound of the bracket.
        
            Returns:
                the higher bound of the bracket
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.univariate.BracketFinder.getFHi`
        
        
        
        """
        ...
    def getLo(self) -> float:
        """
            Get lower bound of the bracket.
        
            Returns:
                the lower bound of the bracket
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.univariate.BracketFinder.getFLo`
        
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
            Get maximum number of evaluations.
        
            Returns:
                the maximum number of evaluations
        
        
        """
        ...
    def getMid(self) -> float:
        """
            Get a point in the middle of the bracket.
        
            Returns:
                a point in the middle of the bracket
        
            Also see:
        
                  - :meth:`~org.hipparchus.optim.univariate.BracketFinder.getFMid`
        
        
        
        """
        ...
    def search(self, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], goalType: org.hipparchus.optim.nonlinear.scalar.GoalType, double: float, double2: float) -> None:
        """
            Search new points that bracket a local optimum of the function.
        
            Parameters:
                func (:class:`~org.hipparchus.optim.univariate.https:.www.hipparchus.org.hipparchus`): Function whose optimum should be bracketed.
                goal (:class:`~org.hipparchus.optim.nonlinear.scalar.GoalType`): :class:`~org.hipparchus.optim.nonlinear.scalar.GoalType`.
                xA (double): Initial point.
                xB (double): Initial point.
        
            Raises:
                :class:`~org.hipparchus.optim.univariate.https:.www.hipparchus.org.hipparchus`: if the maximum number of evaluations is exceeded.
        
        
        """
        ...

class SearchInterval(org.hipparchus.optim.OptimizationData):
    """
    public classSearchInterval extends :class:`~org.hipparchus.optim.univariate.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Search interval and (optional) start value.
    
    
        Immutable class.
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def getMax(self) -> float:
        """
            Gets the upper bound.
        
            Returns:
                the upper bound.
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Gets the lower bound.
        
            Returns:
                the lower bound.
        
        
        """
        ...
    def getStartValue(self) -> float:
        """
            Gets the start value.
        
            Returns:
                the start value.
        
        
        """
        ...

class SimpleUnivariateValueChecker(org.hipparchus.optim.AbstractConvergenceChecker['UnivariatePointValuePair']):
    """
    public classSimpleUnivariateValueChecker extends :class:`~org.hipparchus.optim.AbstractConvergenceChecker`<:class:`~org.hipparchus.optim.univariate.UnivariatePointValuePair`>
    
        Simple implementation of the :class:`~org.hipparchus.optim.ConvergenceChecker` interface that uses only objective
        function values. Convergence is considered to have been reached if either the relative difference between the objective
        function values is smaller than a threshold or if either the absolute difference between the objective function values
        is smaller than another threshold.
    
    
        The :meth:`~org.hipparchus.optim.univariate.SimpleUnivariateValueChecker.converged` method will also return :code:`true`
        if the number of iterations has been set (see
        :meth:`~org.hipparchus.optim.univariate.SimpleUnivariateValueChecker.%3Cinit%3E`).
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, univariatePointValuePair: 'UnivariatePointValuePair', univariatePointValuePair2: 'UnivariatePointValuePair') -> bool:
        """
            Check if the optimization algorithm has converged considering the last two points. This method may be called several
            time from the same algorithm iteration with different points. This can be detected by checking the iteration number at
            each call if needed. Each time this method is called, the previous and current point correspond to points with the same
            role at each iteration, so they can be compared. As an example, simplex-based algorithms call this method for all points
            of the simplex, not only for the best or worst ones.
        
            Specified by:
                :meth:`~org.hipparchus.optim.ConvergenceChecker.converged` in
                interface :class:`~org.hipparchus.optim.ConvergenceChecker`
        
            Specified by:
                :meth:`~org.hipparchus.optim.AbstractConvergenceChecker.converged` in
                class :class:`~org.hipparchus.optim.AbstractConvergenceChecker`
        
            Parameters:
                iteration (int): Index of current iteration
                previous (:class:`~org.hipparchus.optim.univariate.UnivariatePointValuePair`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.univariate.UnivariatePointValuePair`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the algorithm has converged.
        
        
        """
        ...

class UnivariateObjectiveFunction(org.hipparchus.optim.OptimizationData):
    """
    public classUnivariateObjectiveFunction extends :class:`~org.hipparchus.optim.univariate.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Scalar function to be optimized.
    """
    def __init__(self, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]): ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.UnivariateFunction:
        """
            Gets the function to be optimized.
        
            Returns:
                the objective function.
        
        
        """
        ...

class UnivariateOptimizer(org.hipparchus.optim.BaseOptimizer['UnivariatePointValuePair']):
    """
    public abstract classUnivariateOptimizer extends :class:`~org.hipparchus.optim.BaseOptimizer`<:class:`~org.hipparchus.optim.univariate.UnivariatePointValuePair`>
    
        Base class for a univariate scalar function optimizer.
    """
    def getGoalType(self) -> org.hipparchus.optim.nonlinear.scalar.GoalType:
        """
            Get optimization type.
        
            Returns:
                the optimization type
        
        
        """
        ...
    def getMax(self) -> float:
        """
            Get upper bounds.
        
            Returns:
                the upper bounds
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Get lower bounds.
        
            Returns:
                the lower bounds
        
        
        """
        ...
    def getStartValue(self) -> float:
        """
            Get initial guess.
        
            Returns:
                the initial guess
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> 'UnivariatePointValuePair': ...

class UnivariatePointValuePair(java.io.Serializable):
    """
    public classUnivariatePointValuePair extends :class:`~org.hipparchus.optim.univariate.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.univariate.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class holds a point and the value of an objective function at this point. This is a simple immutable container.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float): ...
    def getPoint(self) -> float:
        """
            Get the point.
        
            Returns:
                the point.
        
        
        """
        ...
    def getValue(self) -> float:
        """
            Get the value of the objective function.
        
            Returns:
                the stored value of the objective function.
        
        
        """
        ...

class BrentOptimizer(UnivariateOptimizer):
    """
    public classBrentOptimizer extends :class:`~org.hipparchus.optim.univariate.UnivariateOptimizer`
    
        For a function defined on some interval :code:`(lo, hi)`, this class finds an approximation :code:`x` to the point at
        which the function attains its minimum. It implements Richard Brent's algorithm (from his book "Algorithms for
        Minimization without Derivatives", p. 79) for finding minima of real univariate functions.
    
    
        This code is an adaptation, partly based on the Python code from SciPy (module "optimize.py" v0.5); the original
        algorithm is also modified
    
          - to use an initial guess provided by the user,
          - to ensure that the best point encountered is the one returned.
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, convergenceChecker: typing.Union[org.hipparchus.optim.ConvergenceChecker[UnivariatePointValuePair], typing.Callable[[int, UnivariatePointValuePair, UnivariatePointValuePair], bool]]): ...

class MultiStartUnivariateOptimizer(UnivariateOptimizer):
    """
    public classMultiStartUnivariateOptimizer extends :class:`~org.hipparchus.optim.univariate.UnivariateOptimizer`
    
        Special implementation of the :class:`~org.hipparchus.optim.univariate.UnivariateOptimizer` interface adding multi-start
        features to an existing optimizer.
    
    
        This class wraps an optimizer in order to use it several times in turn with different starting points (trying to avoid
        being trapped in a local extremum when looking for a global one).
    """
    def __init__(self, univariateOptimizer: UnivariateOptimizer, int: int, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    def getEvaluations(self) -> int:
        """
            Gets the number of evaluations of the objective function. The number of evaluations corresponds to the last call to the
            :code:`optimize` method. It is 0 if the method has not been called yet.
        
            Overrides:
                :meth:`~org.hipparchus.optim.BaseOptimizer.getEvaluations` in class :class:`~org.hipparchus.optim.BaseOptimizer`
        
            Returns:
                the number of evaluations of the objective function.
        
        
        """
        ...
    def getOptima(self) -> typing.MutableSequence[UnivariatePointValuePair]:
        """
            Gets all the optima found during the last call to :code:`optimize`. The optimizer stores all the optima found during a
            set of restarts. The :code:`optimize` method returns the best point only. This method returns all the points found at
            the end of each starts, including the best one already returned by the :code:`optimize` method.
        
        
            The returned array as one element for each start as specified in the constructor. It is ordered with the results from
            the runs that did converge first, sorted from best to worst objective value (i.e in ascending order if minimizing and in
            descending order if maximizing), followed by :code:`null` elements corresponding to the runs that did not converge. This
            means all elements will be :code:`null` if the :code:`optimize` method did throw an exception. This also means that if
            the first element is not :code:`null`, it is the best point found across all starts.
        
            Returns:
                an array containing the optima.
        
            Raises:
                :class:`~org.hipparchus.optim.univariate.https:.www.hipparchus.org.hipparchus`: if :meth:`~org.hipparchus.optim.univariate.MultiStartUnivariateOptimizer.optimize` has not been called.
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> UnivariatePointValuePair:
        """
            Stores data and performs the optimization.
        
            The list of parameters is open-ended so that sub-classes can extend it with arguments specific to their concrete
            implementations.
        
            When the method is called multiple times, instance data is overwritten only when actually present in the list of
            arguments: when not specified, data set in a previous call is retained (and thus is optional in subsequent calls).
        
            Important note: Subclasses *must* override :meth:`~org.hipparchus.optim.BaseOptimizer.parseOptimizationData` if they
            need to register their own options; but then, they *must* also call :code:`super.parseOptimizationData(optData)` within
            that method.
        
            Overrides:
                :meth:`~org.hipparchus.optim.univariate.UnivariateOptimizer.optimize` in
                class :class:`~org.hipparchus.optim.univariate.UnivariateOptimizer`
        
            Parameters:
                optData (:class:`~org.hipparchus.optim.OptimizationData`...): Optimization data. In addition to those documented in :meth:`~org.hipparchus.optim.BaseOptimizer.parseOptimizationData`,
                    this method will register the following data:
        
                      - :class:`~org.hipparchus.optim.nonlinear.scalar.GoalType`
                      - :class:`~org.hipparchus.optim.univariate.SearchInterval`
                      - :class:`~org.hipparchus.optim.univariate.UnivariateObjectiveFunction`
        
        
            Returns:
                a point/value pair that satisfies the convergence criteria.
        
            Raises:
                :class:`~org.hipparchus.optim.univariate.https:.www.hipparchus.org.hipparchus`: if :code:`optData` does not contain an instance of :class:`~org.hipparchus.optim.MaxEval` or
                    :class:`~org.hipparchus.optim.univariate.SearchInterval`.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.univariate")``.

    BracketFinder: typing.Type[BracketFinder]
    BrentOptimizer: typing.Type[BrentOptimizer]
    MultiStartUnivariateOptimizer: typing.Type[MultiStartUnivariateOptimizer]
    SearchInterval: typing.Type[SearchInterval]
    SimpleUnivariateValueChecker: typing.Type[SimpleUnivariateValueChecker]
    UnivariateObjectiveFunction: typing.Type[UnivariateObjectiveFunction]
    UnivariateOptimizer: typing.Type[UnivariateOptimizer]
    UnivariatePointValuePair: typing.Type[UnivariatePointValuePair]
