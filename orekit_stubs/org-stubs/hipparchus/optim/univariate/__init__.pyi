import java.io
import org.hipparchus.analysis
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar
import org.hipparchus.random
import typing



class BracketFinder:
    """
    public class BracketFinder extends Object
    
        Provide an interval that brackets a local optimum of a function. This code is based on a Python implementation (from
        *SciPy*, module :code:`optimize.py` v0.5).
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    def getEvaluations(self) -> int:
        """
        
            Returns:
                the number of evaluations.
        
        
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
        
            Returns:
                the higher bound of the bracket.
        
            Also see:
                :meth:`~org.hipparchus.optim.univariate.BracketFinder.getFHi`
        
        
        """
        ...
    def getLo(self) -> float:
        """
        
            Returns:
                the lower bound of the bracket.
        
            Also see:
                :meth:`~org.hipparchus.optim.univariate.BracketFinder.getFLo`
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
        
            Returns:
                the number of evaluations.
        
        
        """
        ...
    def getMid(self) -> float:
        """
        
            Returns:
                a point in the middle of the bracket.
        
            Also see:
                :meth:`~org.hipparchus.optim.univariate.BracketFinder.getFMid`
        
        
        """
        ...
    def search(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction, goalType: org.hipparchus.optim.nonlinear.scalar.GoalType, double: float, double2: float) -> None:
        """
            Search new points that bracket a local optimum of the function.
        
            Parameters:
                func (UnivariateFunction): Function whose optimum should be bracketed.
                goal (:class:`~org.hipparchus.optim.nonlinear.scalar.GoalType`): :class:`~org.hipparchus.optim.nonlinear.scalar.GoalType`.
                xA (double): Initial point.
                xB (double): Initial point.
        
            Raises:
                : if the maximum number of evaluations is exceeded.
        
        
        """
        ...

class SearchInterval(org.hipparchus.optim.OptimizationData):
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def getMax(self) -> float: ...
    def getMin(self) -> float: ...
    def getStartValue(self) -> float: ...

class SimpleUnivariateValueChecker(org.hipparchus.optim.AbstractConvergenceChecker['UnivariatePointValuePair']):
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, univariatePointValuePair: 'UnivariatePointValuePair', univariatePointValuePair2: 'UnivariatePointValuePair') -> bool: ...

class UnivariateObjectiveFunction(org.hipparchus.optim.OptimizationData):
    """
    public class UnivariateObjectiveFunction extends Object implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Scalar function to be optimized.
    """
    def __init__(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction): ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.UnivariateFunction:
        """
            Gets the function to be optimized.
        
            Returns:
                the objective function.
        
        
        """
        ...

class UnivariateOptimizer(org.hipparchus.optim.BaseOptimizer['UnivariatePointValuePair']):
    """
    public abstract class UnivariateOptimizer extends :class:`~org.hipparchus.optim.BaseOptimizer`<:class:`~org.hipparchus.optim.univariate.UnivariatePointValuePair`>
    
        Base class for a univariate scalar function optimizer.
    """
    def getGoalType(self) -> org.hipparchus.optim.nonlinear.scalar.GoalType:
        """
        
            Returns:
                the optimization type.
        
        
        """
        ...
    def getMax(self) -> float:
        """
        
            Returns:
                the upper bounds.
        
        
        """
        ...
    def getMin(self) -> float:
        """
        
            Returns:
                the lower bounds.
        
        
        """
        ...
    def getStartValue(self) -> float:
        """
        
            Returns:
                the initial guess.
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, optimizationDataArray: typing.List[org.hipparchus.optim.OptimizationData]) -> 'UnivariatePointValuePair': ...

class UnivariatePointValuePair(java.io.Serializable):
    """
    public class UnivariatePointValuePair extends Object implements Serializable
    
        This class holds a point and the value of an objective function at this point. This is a simple immutable container.
    
        Also see:
            :meth:`~serialized`
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
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, convergenceChecker: org.hipparchus.optim.ConvergenceChecker[UnivariatePointValuePair]): ...

class MultiStartUnivariateOptimizer(UnivariateOptimizer):
    def __init__(self, univariateOptimizer: UnivariateOptimizer, int: int, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    def getEvaluations(self) -> int: ...
    def getOptima(self) -> typing.List[UnivariatePointValuePair]: ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, optimizationDataArray: typing.List[org.hipparchus.optim.OptimizationData]) -> UnivariatePointValuePair: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.univariate")``.

    BracketFinder: typing.Type[BracketFinder]
    BrentOptimizer: typing.Type[BrentOptimizer]
    MultiStartUnivariateOptimizer: typing.Type[MultiStartUnivariateOptimizer]
    SearchInterval: typing.Type[SearchInterval]
    SimpleUnivariateValueChecker: typing.Type[SimpleUnivariateValueChecker]
    UnivariateObjectiveFunction: typing.Type[UnivariateObjectiveFunction]
    UnivariateOptimizer: typing.Type[UnivariateOptimizer]
    UnivariatePointValuePair: typing.Type[UnivariatePointValuePair]
