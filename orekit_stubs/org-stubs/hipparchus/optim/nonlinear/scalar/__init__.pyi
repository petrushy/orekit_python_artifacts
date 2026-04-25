
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import jpype
import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar.gradient
import org.hipparchus.optim.nonlinear.scalar.noderiv
import org.hipparchus.optim.univariate
import org.hipparchus.random
import typing



class GoalType(java.lang.Enum['GoalType'], org.hipparchus.optim.OptimizationData):
    """
    implements OptimizationData
    
    Goal type for an optimization problem (minimization or maximization of a scalar function.
    """
    MAXIMIZE: typing.ClassVar['GoalType'] = ...
    MINIMIZE: typing.ClassVar['GoalType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'GoalType':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['GoalType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared.
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LeastSquaresConverter(org.hipparchus.analysis.MultivariateFunction):
    """
    implements hipparchus
    
    This class converts hipparchus to hipparchus when the goal is to minimize them.
    
    This class is mostly used when the vectorial objective function represents a theoretical result computed from a point set applied to a model and the models point must be adjusted to fit the theoretical result to some reference observations. The observations may be obtained for example from physical measurements whether the model is built from theoretical considerations.
    
    This class computes a possibly weighted squared sum of the residuals, which is a scalar value. The residuals are the difference between the theoretical model (i.e. the output of the vectorial objective function) and the observations. The class implements the hipparchus interface and can therefore be minimized by any optimizer supporting scalar objectives functions.This is one way to perform a least square estimation. There are other ways to do this without using this converter, as some optimization algorithms directly support vectorial objective functions.
    
    This class support combination of residuals with or without weights and correlations.
    
          - hipparchus
          - hipparchus
    """
    @typing.overload
    def __init__(self, multivariateVectorFunction: typing.Union[org.hipparchus.analysis.MultivariateVectorFunction, typing.Callable], doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, multivariateVectorFunction: typing.Union[org.hipparchus.analysis.MultivariateVectorFunction, typing.Callable], doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, multivariateVectorFunction: typing.Union[org.hipparchus.analysis.MultivariateVectorFunction, typing.Callable], doubleArray: typing.Union[typing.List[float], jpype.JArray], realMatrix: org.hipparchus.linear.RealMatrix): ...
    def value(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Specified by: hipparchus in interface hipparchus
        
        
        """
        ...

class LineSearch:
    """
    Class for finding the minimum of the objective function along a given direction.
    """
    def __init__(self, optimizer: 'MultivariateOptimizer', relativeTolerance: float, absoluteTolerance: float, initialBracketingRange: float):
        """
        The BrentOptimizer default stopping criterion uses the tolerances to check the domain (point) values, not the function values. The relativeTolerance and absoluteTolerance arguments are thus passed to a SimpleUnivariateValueChecker that will use the function values.
        
        Parameters:
            optimizer (MultivariateOptimizer): Optimizer on behalf of which the line search be performed. Its
                computeObjectiveValue method will be called by the
                search method.
            relativeTolerance (double): Search will stop when the function relative difference between successive iterations is below this value.
            absoluteTolerance (double): Search will stop when the function absolute difference between successive iterations is below this value.
            initialBracketingRange (double): Extent of the initial interval used to find an interval that brackets the optimum. If the optimized function varies a
                lot in the vicinity of the optimum, it may be necessary to provide a value lower than the distance between successive
                local minima.
        
        
        """
        ...
    def search(self, startPoint: typing.Union[typing.List[float], jpype.JArray], direction: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.optim.univariate.UnivariatePointValuePair:
        """
        Finds the number alpha that optimizes f(startPoint + alpha * direction).
        
        Parameters:
            startPoint (double[]): Starting point.
            direction (double[]): Search direction.
        
        Returns:
            the optimum.
        
        Raises:
            hipparchus: if the number of evaluations is exceeded.
        
        
        """
        ...

class MultiStartMultivariateOptimizer(org.hipparchus.optim.BaseMultiStartMultivariateOptimizer[org.hipparchus.optim.PointValuePair]):
    """
    Multi-start optimizer. This class wraps an optimizer in order to use it several times in turn with different starting points (trying to avoid being trapped in a local extremum when looking for a global one).
    """
    def __init__(self, optimizer: 'MultivariateOptimizer', starts: int, generator: typing.Union[org.hipparchus.random.RandomVectorGenerator, typing.Callable]):
        """
        Create a multi-start optimizer from a single-start optimizer.
        
        Parameters:
            optimizer (MultivariateOptimizer): Single-start optimizer to wrap.
            starts (int):             Number of starts to perform. If starts == 1, the result will be same as if optimizer is called directly.
            generator (hipparchus): Random vector generator to use for restarts.
        
        Raises:
            hipparchus: if optimizer or generator is null.
            hipparchus: if starts < 1.
        
        
        """
        ...
    def getOptima(self) -> typing.MutableSequence[org.hipparchus.optim.PointValuePair]:
        """
        Gets all the optima found during the last call to optimize. The optimizer stores all the optima found during a set of restarts. The optimize method returns the best point only. This method returns all the points found at the end of each starts, including the best one already returned by the optimize method.
        
        The returned array as one element for each start as specified in the constructor. It is ordered with the results from the runs that did converge first, sorted from best to worst objective value (i.e in ascending order if minimizing and in descending order if maximizing), followed by null elements corresponding to the runs that did not converge. This means all elements will be null if the optimize method did throw an exception. This also means that if the first element is not null, it is the best point found across all starts.
        
        The behaviour is undefined if this method is called before optimize; it will likely throw NullPointerException.
        
        Specified by: getOptima in class BaseMultiStartMultivariateOptimizer
        
        Returns:
            an array containing the optima sorted from best to worst.
        
        
        """
        ...

class MultivariateFunctionMappingAdapter(org.hipparchus.analysis.MultivariateFunction):
    """
    implements hipparchus
    
    Adapter for mapping bounded hipparchus to unbounded ones.
    
    This adapter can be used to wrap functions subject to simple bounds on parameters so they can be used by optimizers that do not directly support simple bounds.
    
    The principle is that the user function that will be wrapped will see its parameters bounded as required, i.e when its value method is called with argument array point, the elements array will fulfill requirement lower[i] <= point[i] <= upper[i] for all i. Some of the components may be unbounded or bounded only on one side if the corresponding bound is set to an infinite value. The optimizer will not manage the user function by itself, but it will handle this adapter and it is this adapter that will take care the bounds are fulfilled. The adapter value method will be called by the optimizer with unbound parameters, and the adapter will map the unbounded value to the bounded range using appropriate functions like hipparchus for double bounded elements for example.
    
    As the optimizer sees only unbounded parameters, it should be noted that the start point or simplex expected by the optimizer should be unbounded, so the user is responsible for converting his bounded point to unbounded by calling boundedToUnbounded before providing them to the optimizer. For the same reason, the point returned by the optimize method is unbounded. So to convert this point to bounded, users must call unboundedToBounded by themselves!
    
    This adapter is only a poor man solution to simple bounds optimization constraints that can be used with simple optimizers like SimplexOptimizer. A better solution is to use an optimizer that directly supports simple bounds like CMAESOptimizer or BOBYQAOptimizer. One caveat of this poor-man's solution is that behavior near the bounds may be numerically unstable as bounds are mapped from infinite values. Another caveat is that convergence values are evaluated by the optimizer with respect to unbounded variables, so there will be scales differences when converted to bounded variables.
    
          - MultivariateFunctionPenaltyAdapter
    """
    def __init__(self, bounded: typing.Union[org.hipparchus.analysis.MultivariateFunction, typing.Callable], lower: typing.Union[typing.List[float], jpype.JArray], upper: typing.Union[typing.List[float], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            bounded (hipparchus): bounded function
            lower (double[]): lower bounds for each element of the input parameters array (some elements may be set to
                NEGATIVE_INFINITY for unbounded values)
            upper (double[]): upper bounds for each element of the input parameters array (some elements may be set to
                POSITIVE_INFINITY for unbounded values)
        
        Raises:
            hipparchus: if lower and upper bounds are not consistent, either according to dimension or to values
        
        
        """
        ...
    def boundedToUnbounded(self, point: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Maps an array from bounded to unbounded.
        
        Parameters:
            point (double[]): Bounded values.
        
        Returns:
            the unbounded values.
        
        
        """
        ...
    def unboundedToBounded(self, point: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Maps an array from unbounded to bounded.
        
        Parameters:
            point (double[]): Unbounded values.
        
        Returns:
            the bounded values.
        
        
        """
        ...
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the underlying function value from an unbounded point.
        
        This method simply bounds the unbounded point using the mappings set up at construction and calls the underlying function using the bounded point.
        
        Specified by: hipparchus in interface hipparchus
        
        Parameters:
            point (double[]): unbounded value
        
        Returns:
            underlying function value
        
              - unboundedToBounded
        
        
        
        """
        ...

class MultivariateFunctionPenaltyAdapter(org.hipparchus.analysis.MultivariateFunction):
    """
    implements hipparchus
    
    Adapter extending bounded hipparchus to an unbouded domain using a penalty function.
    
    This adapter can be used to wrap functions subject to simple bounds on parameters so they can be used by optimizers that do not directly support simple bounds.
    
    The principle is that the user function that will be wrapped will see its parameters bounded as required, i.e when its value method is called with argument array point, the elements array will fulfill requirement lower[i] <= point[i] <= upper[i] for all i. Some of the components may be unbounded or bounded only on one side if the corresponding bound is set to an infinite value. The optimizer will not manage the user function by itself, but it will handle this adapter and it is this adapter that will take care the bounds are fulfilled. The adapter value method will be called by the optimizer with unbound parameters, and the adapter will check if the parameters is within range or not. If it is in range, then the underlying user function will be called, and if it is not the value of a penalty function will be returned instead.
    
    This adapter is only a poor-man's solution to simple bounds optimization constraints that can be used with simple optimizers like SimplexOptimizer. A better solution is to use an optimizer that directly supports simple bounds like CMAESOptimizer or BOBYQAOptimizer. One caveat of this poor-man's solution is that if start point or start simplex is completely outside of the allowed range, only the penalty function is used, and the optimizer may converge without ever entering the range.
    
          - MultivariateFunctionMappingAdapter
    """
    def __init__(self, bounded: typing.Union[org.hipparchus.analysis.MultivariateFunction, typing.Callable], lower: typing.Union[typing.List[float], jpype.JArray], upper: typing.Union[typing.List[float], jpype.JArray], offset: float, scale: typing.Union[typing.List[float], jpype.JArray]):
        """
        Simple constructor.
        
        When the optimizer provided points are out of range, the value of the penalty function will be used instead of the value of the underlying function. In order for this penalty to be effective in rejecting this point during the optimization process, the penalty function value should be defined with care. This value is computed as:
        
        penalty(point) = offset + ∑ :sub:`i` [scale[i] * √|point[i]-boundary[i]|]
        
        where indices i correspond to all the components that violates their boundaries.
        
        So when attempting a function minimization, offset should be larger than the maximum expected value of the underlying function and scale components should all be positive. When attempting a function maximization, offset should be lesser than the minimum expected value of the underlying function and scale components should all be negative. minimization, and lesser than the minimum expected value of the underlying function when attempting maximization.
        
        These choices for the penalty function have two properties. First, all out of range points will return a function value that is worse than the value returned by any in range point. Second, the penalty is worse for large boundaries violation than for small violations, so the optimizer has an hint about the direction in which it should search for acceptable points.
        
        Parameters:
            bounded (hipparchus): bounded function
            lower (double[]): lower bounds for each element of the input parameters array (some elements may be set to
                NEGATIVE_INFINITY for unbounded values)
            upper (double[]): upper bounds for each element of the input parameters array (some elements may be set to
                POSITIVE_INFINITY for unbounded values)
            offset (double): base offset of the penalty function
            scale (double[]): scale of the penalty function
        
        Raises:
            hipparchus: if lower bounds, upper bounds and scales are not consistent, either according to dimension or to bounadary values
        
        
        """
        ...
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the underlying function value from an unbounded point.
        
        This method simply returns the value of the underlying function if the unbounded point already fulfills the bounds, and compute a replacement value using the offset and scale if bounds are violated, without calling the function at all.
        
        Specified by: hipparchus in interface hipparchus
        
        Parameters:
            point (double[]): unbounded point
        
        Returns:
            either underlying function value or penalty function value
        
        
        """
        ...

class MultivariateOptimizer(org.hipparchus.optim.BaseMultivariateOptimizer[org.hipparchus.optim.PointValuePair]):
    """
    Base class for a multivariate scalar function optimizer.
    """
    def computeObjectiveValue(self, params: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Computes the objective function value. This method must be called by subclasses to enforce the evaluation counter limit.
        
        Parameters:
            params (double[]): Point at which the objective function must be evaluated.
        
        Returns:
            the objective function value at the specified point.
        
        Raises:
            hipparchus: if the maximal number of evaluations is exceeded.
        
        
        """
        ...
    def getGoalType(self) -> GoalType:
        """
        Get optimization type.
        
        Returns:
            the optimization type.
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...

class ObjectiveFunction(org.hipparchus.optim.OptimizationData):
    """
    implements OptimizationData
    
    Scalar function to be optimized.
    """
    def __init__(self, f: typing.Union[org.hipparchus.analysis.MultivariateFunction, typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            f (hipparchus): Function to be optimized.
        
        
        """
        ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.MultivariateFunction:
        """
        Gets the function to be optimized.
        
        Returns:
            the objective function.
        
        
        """
        ...

class ObjectiveFunctionGradient(org.hipparchus.optim.OptimizationData):
    """
    implements OptimizationData
    
    Gradient of the scalar function to be optimized.
    """
    def __init__(self, g: typing.Union[org.hipparchus.analysis.MultivariateVectorFunction, typing.Callable]):
        """
        Simple constructor.
        
        Parameters:
            g (hipparchus): Gradient of the function to be optimized.
        
        
        """
        ...
    def getObjectiveFunctionGradient(self) -> org.hipparchus.analysis.MultivariateVectorFunction:
        """
        Gets the gradient of the function to be optimized.
        
        Returns:
            the objective function gradient.
        
        
        """
        ...

class GradientMultivariateOptimizer(MultivariateOptimizer):
    """
    Base class for implementing optimizers for multivariate scalar differentiable functions. It contains boiler-plate code for dealing with gradient evaluation.
    """
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.scalar")``.

    GoalType: typing.Type[GoalType]
    GradientMultivariateOptimizer: typing.Type[GradientMultivariateOptimizer]
    LeastSquaresConverter: typing.Type[LeastSquaresConverter]
    LineSearch: typing.Type[LineSearch]
    MultiStartMultivariateOptimizer: typing.Type[MultiStartMultivariateOptimizer]
    MultivariateFunctionMappingAdapter: typing.Type[MultivariateFunctionMappingAdapter]
    MultivariateFunctionPenaltyAdapter: typing.Type[MultivariateFunctionPenaltyAdapter]
    MultivariateOptimizer: typing.Type[MultivariateOptimizer]
    ObjectiveFunction: typing.Type[ObjectiveFunction]
    ObjectiveFunctionGradient: typing.Type[ObjectiveFunctionGradient]
    gradient: org.hipparchus.optim.nonlinear.scalar.gradient.__module_protocol__
    noderiv: org.hipparchus.optim.nonlinear.scalar.noderiv.__module_protocol__
