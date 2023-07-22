import java.lang
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
    public enum GoalType extends :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.optim.nonlinear.scalar.GoalType`> implements :class:`~org.hipparchus.optim.OptimizationData`
    
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
    def valueOf(string: str) -> 'GoalType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['GoalType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (GoalType c : GoalType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LeastSquaresConverter(org.hipparchus.analysis.MultivariateFunction):
    @typing.overload
    def __init__(self, multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction, doubleArray: typing.List[float], realMatrix: org.hipparchus.linear.RealMatrix): ...
    def value(self, doubleArray: typing.List[float]) -> float: ...

class LineSearch:
    """
    public class LineSearch extends :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class for finding the minimum of the objective function along a given direction.
    """
    def __init__(self, multivariateOptimizer: 'MultivariateOptimizer', double: float, double2: float, double3: float): ...
    def search(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> org.hipparchus.optim.univariate.UnivariatePointValuePair:
        """
            Finds the number :code:`alpha` that optimizes :code:`f(startPoint + alpha * direction)`.
        
            Parameters:
                startPoint (double[]): Starting point.
                direction (double[]): Search direction.
        
            Returns:
                the optimum.
        
            Raises:
                :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus`: if the number of evaluations is exceeded.
        
        
        """
        ...

class MultiStartMultivariateOptimizer(org.hipparchus.optim.BaseMultiStartMultivariateOptimizer[org.hipparchus.optim.PointValuePair]):
    def __init__(self, multivariateOptimizer: 'MultivariateOptimizer', int: int, randomVectorGenerator: org.hipparchus.random.RandomVectorGenerator): ...
    def getOptima(self) -> typing.List[org.hipparchus.optim.PointValuePair]: ...

class MultivariateFunctionMappingAdapter(org.hipparchus.analysis.MultivariateFunction):
    """
    public class MultivariateFunctionMappingAdapter extends :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus`
    
    
        Adapter for mapping bounded :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus` to
        unbounded ones.
    
        This adapter can be used to wrap functions subject to simple bounds on parameters so they can be used by optimizers that
        do *not* directly support simple bounds.
    
        The principle is that the user function that will be wrapped will see its parameters bounded as required, i.e when its
        :code:`value` method is called with argument array :code:`point`, the elements array will fulfill requirement
        :code:`lower[i] <= point[i] <= upper[i]` for all i. Some of the components may be unbounded or bounded only on one side
        if the corresponding bound is set to an infinite value. The optimizer will not manage the user function by itself, but
        it will handle this adapter and it is this adapter that will take care the bounds are fulfilled. The adapter
        :meth:`~org.hipparchus.optim.nonlinear.scalar.MultivariateFunctionMappingAdapter.value` method will be called by the
        optimizer with unbound parameters, and the adapter will map the unbounded value to the bounded range using appropriate
        functions like :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus` for double bounded
        elements for example.
    
        As the optimizer sees only unbounded parameters, it should be noted that the start point or simplex expected by the
        optimizer should be unbounded, so the user is responsible for converting his bounded point to unbounded by calling
        :meth:`~org.hipparchus.optim.nonlinear.scalar.MultivariateFunctionMappingAdapter.boundedToUnbounded` before providing
        them to the optimizer. For the same reason, the point returned by the
        :meth:`~org.hipparchus.optim.BaseMultivariateOptimizer.optimize` method is unbounded. So to convert this point to
        bounded, users must call
        :meth:`~org.hipparchus.optim.nonlinear.scalar.MultivariateFunctionMappingAdapter.unboundedToBounded` by themselves!
    
        This adapter is only a poor man solution to simple bounds optimization constraints that can be used with simple
        optimizers like :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.SimplexOptimizer`. A better solution is to use an
        optimizer that directly supports simple bounds like
        :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.CMAESOptimizer` or
        :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.BOBYQAOptimizer`. One caveat of this poor-man's solution is that
        behavior near the bounds may be numerically unstable as bounds are mapped from infinite values. Another caveat is that
        convergence values are evaluated by the optimizer with respect to unbounded variables, so there will be scales
        differences when converted to bounded variables.
    
        Also see:
            :class:`~org.hipparchus.optim.nonlinear.scalar.MultivariateFunctionPenaltyAdapter`
    """
    def __init__(self, multivariateFunction: org.hipparchus.analysis.MultivariateFunction, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def boundedToUnbounded(self, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Maps an array from bounded to unbounded.
        
            Parameters:
                point (double[]): Bounded values.
        
            Returns:
                the unbounded values.
        
        
        """
        ...
    def unboundedToBounded(self, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Maps an array from unbounded to bounded.
        
            Parameters:
                point (double[]): Unbounded values.
        
            Returns:
                the bounded values.
        
        
        """
        ...
    def value(self, doubleArray: typing.List[float]) -> float:
        """
            Compute the underlying function value from an unbounded point.
        
            This method simply bounds the unbounded point using the mappings set up at construction and calls the underlying
            function using the bounded point.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus`
        
            Parameters:
                point (double[]): unbounded value
        
            Returns:
                underlying function value
        
            Also see:
                :meth:`~org.hipparchus.optim.nonlinear.scalar.MultivariateFunctionMappingAdapter.unboundedToBounded`
        
        
        """
        ...

class MultivariateFunctionPenaltyAdapter(org.hipparchus.analysis.MultivariateFunction):
    """
    public class MultivariateFunctionPenaltyAdapter extends :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus`
    
    
        Adapter extending bounded :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus` to an
        unbouded domain using a penalty function.
    
        This adapter can be used to wrap functions subject to simple bounds on parameters so they can be used by optimizers that
        do *not* directly support simple bounds.
    
        The principle is that the user function that will be wrapped will see its parameters bounded as required, i.e when its
        :code:`value` method is called with argument array :code:`point`, the elements array will fulfill requirement
        :code:`lower[i] <= point[i] <= upper[i]` for all i. Some of the components may be unbounded or bounded only on one side
        if the corresponding bound is set to an infinite value. The optimizer will not manage the user function by itself, but
        it will handle this adapter and it is this adapter that will take care the bounds are fulfilled. The adapter
        :meth:`~org.hipparchus.optim.nonlinear.scalar.MultivariateFunctionPenaltyAdapter.value` method will be called by the
        optimizer with unbound parameters, and the adapter will check if the parameters is within range or not. If it is in
        range, then the underlying user function will be called, and if it is not the value of a penalty function will be
        returned instead.
    
        This adapter is only a poor-man's solution to simple bounds optimization constraints that can be used with simple
        optimizers like :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.SimplexOptimizer`. A better solution is to use an
        optimizer that directly supports simple bounds like
        :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.CMAESOptimizer` or
        :class:`~org.hipparchus.optim.nonlinear.scalar.noderiv.BOBYQAOptimizer`. One caveat of this poor-man's solution is that
        if start point or start simplex is completely outside of the allowed range, only the penalty function is used, and the
        optimizer may converge without ever entering the range.
    
        Also see:
            :class:`~org.hipparchus.optim.nonlinear.scalar.MultivariateFunctionMappingAdapter`
    """
    def __init__(self, multivariateFunction: org.hipparchus.analysis.MultivariateFunction, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float, doubleArray3: typing.List[float]): ...
    def value(self, doubleArray: typing.List[float]) -> float:
        """
            Computes the underlying function value from an unbounded point.
        
            This method simply returns the value of the underlying function if the unbounded point already fulfills the bounds, and
            compute a replacement value using the offset and scale if bounds are violated, without calling the function at all.
        
            Specified by:
                :meth:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus`
        
            Parameters:
                point (double[]): unbounded point
        
            Returns:
                either underlying function value or penalty function value
        
        
        """
        ...

class MultivariateOptimizer(org.hipparchus.optim.BaseMultivariateOptimizer[org.hipparchus.optim.PointValuePair]):
    """
    public abstract class MultivariateOptimizer extends :class:`~org.hipparchus.optim.BaseMultivariateOptimizer`<:class:`~org.hipparchus.optim.PointValuePair`>
    
        Base class for a multivariate scalar function optimizer.
    """
    def computeObjectiveValue(self, doubleArray: typing.List[float]) -> float:
        """
            Computes the objective function value. This method *must* be called by subclasses to enforce the evaluation counter
            limit.
        
            Parameters:
                params (double[]): Point at which the objective function must be evaluated.
        
            Returns:
                the objective function value at the specified point.
        
            Raises:
                :class:`~org.hipparchus.optim.nonlinear.scalar.https:.www.hipparchus.org.hipparchus`: if the maximal number of evaluations is exceeded.
        
        
        """
        ...
    def getGoalType(self) -> GoalType:
        """
        
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
    public class ObjectiveFunction extends :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Scalar function to be optimized.
    """
    def __init__(self, multivariateFunction: org.hipparchus.analysis.MultivariateFunction): ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.MultivariateFunction:
        """
            Gets the function to be optimized.
        
            Returns:
                the objective function.
        
        
        """
        ...

class ObjectiveFunctionGradient(org.hipparchus.optim.OptimizationData):
    """
    public class ObjectiveFunctionGradient extends :class:`~org.hipparchus.optim.nonlinear.scalar.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Gradient of the scalar function to be optimized.
    """
    def __init__(self, multivariateVectorFunction: org.hipparchus.analysis.MultivariateVectorFunction): ...
    def getObjectiveFunctionGradient(self) -> org.hipparchus.analysis.MultivariateVectorFunction:
        """
            Gets the gradient of the function to be optimized.
        
            Returns:
                the objective function gradient.
        
        
        """
        ...

class GradientMultivariateOptimizer(MultivariateOptimizer):
    """
    public abstract class GradientMultivariateOptimizer extends :class:`~org.hipparchus.optim.nonlinear.scalar.MultivariateOptimizer`
    
        Base class for implementing optimizers for multivariate scalar differentiable functions. It contains boiler-plate code
        for dealing with gradient evaluation.
    """
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, *optimizationData: org.hipparchus.optim.OptimizationData) -> org.hipparchus.optim.PointValuePair: ...


class __module_protocol__(typing.Protocol):
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
