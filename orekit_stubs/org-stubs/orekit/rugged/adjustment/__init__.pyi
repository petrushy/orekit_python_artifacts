import java.lang
import java.util
import org
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.rugged.adjustment.measurements
import org.orekit.rugged.api
import org.orekit.rugged.linesensor
import typing



class AdjustmentContext:
    """
    public class AdjustmentContext extends Object
    
        Create adjustment context for viewing model refining.
    
        Since:
            2.0
    """
    def __init__(self, collection: typing.Union[java.util.Collection[org.orekit.rugged.api.Rugged], typing.Sequence[org.orekit.rugged.api.Rugged], typing.Set[org.orekit.rugged.api.Rugged]], observables: org.orekit.rugged.adjustment.measurements.Observables): ...
    def estimateFreeParameters(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str], typing.Set[str]], int: int, double: float) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.Optimum:
        """
            Estimate the free parameters in viewing model to match specified sensor to ground mappings.
        
            This method is typically used for calibration of on-board sensor parameters, like rotation angles polynomial
            coefficients.
        
            Before using this method, the :code:`viewing model parameters` retrieved by calling the
            :meth:`~org.orekit.rugged.linesensor.LineSensor.getParametersDrivers` method on the desired sensors must be configured.
            The parameters that should be estimated must have their :code:`selection status` set to :code:`true` whereas the
            parameters that should retain their current value must have their :code:`selection status` set to :code:`false`. If
            needed, the :code:`value` of the estimated/selected parameters can also be changed before calling the method, as this
            value will serve as the initial value in the estimation process.
        
            The method solves a least-squares problem to minimize the residuals between test locations and the reference mappings by
            adjusting the selected viewing models parameters.
        
            The estimated parameters can be retrieved after the method completes by calling again the
            :meth:`~org.orekit.rugged.linesensor.LineSensor.getParametersDrivers` method on the desired sensors and checking the
            updated values of the parameters. In fact, as the values of the parameters are already updated by this method, if users
            want to use the updated values immediately to perform new direct/inverse locations, they can do so without looking at
            the parameters: the viewing models are already aware of the updated parameters.
        
            Parameters:
                ruggedNameList (Collection<String> ruggedNameList): list of rugged to refine
                maxEvaluations (int): maximum number of evaluations
                parametersConvergenceThreshold (double): convergence threshold on normalized parameters (dimensionless, related to parameters scales)
        
            Returns:
                optimum of the least squares problem
        
        
        """
        ...
    def setOptimizer(self, optimizerId: 'OptimizerId') -> None:
        """
            Setter for optimizer algorithm.
        
            Parameters:
                optimizerId (:class:`~org.orekit.rugged.adjustment.OptimizerId`): the chosen algorithm
        
        
        """
        ...

class LeastSquareAdjuster:
    """
    public class LeastSquareAdjuster extends Object
    
        LeastSquareAdjuster Class for setting least square algorithm chosen for solving optimization problem.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, optimizerId: 'OptimizerId'): ...
    def optimize(self, leastSquaresProblem: org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresOptimizer.Optimum:
        """
            Solve the least square problem.
        
            Parameters:
                problem (org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem): the least square problem
        
            Returns:
                the solution
        
        
        """
        ...

class OptimizerId(java.lang.Enum['OptimizerId']):
    """
    public enum OptimizerId extends Enum<:class:`~org.orekit.rugged.adjustment.OptimizerId`>
    
        Enumerate for Optimizer used in Least square optimization.
    
        Since:
            2.0
    """
    LEVENBERG_MARQUADT: typing.ClassVar['OptimizerId'] = ...
    GAUSS_NEWTON_LU: typing.ClassVar['OptimizerId'] = ...
    GAUSS_NEWTON_QR: typing.ClassVar['OptimizerId'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OptimizerId':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OptimizerId']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OptimizerId c : OptimizerId.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class GroundOptimizationProblemBuilder(org.orekit.rugged.adjustment.OptimizationProblemBuilder):
    """
    public class GroundOptimizationProblemBuilder extends Object
    
        Ground optimization problem builder. builds the optimization problem relying on ground measurements.
    
        Since:
            2.0
    """
    def __init__(self, list: java.util.List[org.orekit.rugged.linesensor.LineSensor], observables: org.orekit.rugged.adjustment.measurements.Observables, rugged: org.orekit.rugged.api.Rugged): ...
    def build(self, int: int, double: float) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem:
        """
            Least square problem builder.
        
            Parameters:
                maxEvaluations (int): maxIterations and evaluations
                convergenceThreshold (double): parameter convergence threshold
        
            Returns:
                the least square problem
        
        
        """
        ...

class InterSensorsOptimizationProblemBuilder(org.orekit.rugged.adjustment.OptimizationProblemBuilder):
    """
    public class InterSensorsOptimizationProblemBuilder extends Object
    
        Constructs the optimization problem for a list of tie points.
    
        Since:
            2.0
    """
    def __init__(self, list: java.util.List[org.orekit.rugged.linesensor.LineSensor], observables: org.orekit.rugged.adjustment.measurements.Observables, collection: typing.Union[java.util.Collection[org.orekit.rugged.api.Rugged], typing.Sequence[org.orekit.rugged.api.Rugged], typing.Set[org.orekit.rugged.api.Rugged]]): ...
    def build(self, int: int, double: float) -> org.hipparchus.optim.nonlinear.vector.leastsquares.LeastSquaresProblem:
        """
            Least square problem builder.
        
            Parameters:
                maxEvaluations (int): maxIterations and evaluations
                convergenceThreshold (double): parameter convergence threshold
        
            Returns:
                the least square problem
        
        
        """
        ...

class OptimizationProblemBuilder: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.adjustment")``.

    AdjustmentContext: typing.Type[AdjustmentContext]
    GroundOptimizationProblemBuilder: typing.Type[GroundOptimizationProblemBuilder]
    InterSensorsOptimizationProblemBuilder: typing.Type[InterSensorsOptimizationProblemBuilder]
    LeastSquareAdjuster: typing.Type[LeastSquareAdjuster]
    OptimizationProblemBuilder: typing.Type[OptimizationProblemBuilder]
    OptimizerId: typing.Type[OptimizerId]
    measurements: org.orekit.rugged.adjustment.measurements.__module_protocol__