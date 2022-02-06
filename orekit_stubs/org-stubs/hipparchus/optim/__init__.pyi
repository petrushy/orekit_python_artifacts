import java.io
import java.lang
import java.util
import org.hipparchus.exception
import org.hipparchus.optim.linear
import org.hipparchus.optim.nonlinear
import org.hipparchus.optim.univariate
import org.hipparchus.random
import org.hipparchus.util
import typing



_BaseOptimizer__P = typing.TypeVar('_BaseOptimizer__P')  # <P>
class BaseOptimizer(typing.Generic[_BaseOptimizer__P]):
    """
    public abstract class BaseOptimizer<P> extends Object
    
        Base class for implementing optimizers. It contains the boiler-plate code for counting the number of evaluations of the
        objective function and the number of iterations of the algorithm, and storing the convergence checker. *It is not a
        "user" class.*
    """
    def getConvergenceChecker(self) -> 'ConvergenceChecker'[_BaseOptimizer__P]: ...
    def getEvaluations(self) -> int:
        """
            Gets the number of evaluations of the objective function. The number of evaluations corresponds to the last call to the
            :code:`optimize` method. It is 0 if the method has not been called yet.
        
            Returns:
                the number of evaluations of the objective function.
        
        
        """
        ...
    def getIterations(self) -> int:
        """
            Gets the number of iterations performed by the algorithm. The number iterations corresponds to the last call to the
            :code:`optimize` method. It is 0 if the method has not been called yet.
        
            Returns:
                the number of evaluations of the objective function.
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
            Gets the maximal number of function evaluations.
        
            Returns:
                the maximal number of function evaluations.
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
            Gets the maximal number of iterations.
        
            Returns:
                the maximal number of iterations.
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> _BaseOptimizer__P: ...
    @typing.overload
    def optimize(self, optimizationDataArray: typing.List['OptimizationData']) -> _BaseOptimizer__P: ...

_ConvergenceChecker__P = typing.TypeVar('_ConvergenceChecker__P')  # <P>
class ConvergenceChecker(typing.Generic[_ConvergenceChecker__P]):
    def converged(self, int: int, p: _ConvergenceChecker__P, p2: _ConvergenceChecker__P) -> bool: ...

class LocalizedOptimFormats(java.lang.Enum['LocalizedOptimFormats'], org.hipparchus.exception.Localizable):
    """
    public enum LocalizedOptimFormats extends Enum<:class:`~org.hipparchus.optim.LocalizedOptimFormats`> implements Localizable
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    EQUAL_VERTICES_IN_SIMPLEX: typing.ClassVar['LocalizedOptimFormats'] = ...
    INVALID_IMPLEMENTATION: typing.ClassVar['LocalizedOptimFormats'] = ...
    NO_FEASIBLE_SOLUTION: typing.ClassVar['LocalizedOptimFormats'] = ...
    SIMPLEX_NEED_ONE_POINT: typing.ClassVar['LocalizedOptimFormats'] = ...
    TOO_SMALL_COST_RELATIVE_TOLERANCE: typing.ClassVar['LocalizedOptimFormats'] = ...
    TOO_SMALL_ORTHOGONALITY_TOLERANCE: typing.ClassVar['LocalizedOptimFormats'] = ...
    TOO_SMALL_PARAMETERS_RELATIVE_TOLERANCE: typing.ClassVar['LocalizedOptimFormats'] = ...
    TRUST_REGION_STEP_FAILED: typing.ClassVar['LocalizedOptimFormats'] = ...
    UNABLE_TO_PERFORM_QR_DECOMPOSITION_ON_JACOBIAN: typing.ClassVar['LocalizedOptimFormats'] = ...
    UNABLE_TO_SOLVE_SINGULAR_PROBLEM: typing.ClassVar['LocalizedOptimFormats'] = ...
    UNBOUNDED_SOLUTION: typing.ClassVar['LocalizedOptimFormats'] = ...
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedOptimFormats':
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
    def values() -> typing.List['LocalizedOptimFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LocalizedOptimFormats c : LocalizedOptimFormats.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OptimizationData:
    """
    public interface OptimizationData
    
        Marker interface. Implementations will provide functionality (optional or required) needed by the optimizers, and those
        will need to check the actual type of the arguments and perform the appropriate cast in order to access the data they
        need.
    """
    ...

_OptimizationProblem__P = typing.TypeVar('_OptimizationProblem__P')  # <P>
class OptimizationProblem(typing.Generic[_OptimizationProblem__P]):
    """
    public interface OptimizationProblem<P>
    
        Common settings for all optimization problems. Includes divergence and convergence criteria.
    """
    def getConvergenceChecker(self) -> ConvergenceChecker[_OptimizationProblem__P]: ...
    def getEvaluationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of evaluations and then throws an exception.
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...
    def getIterationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of iterations and then throws an exception.
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...

class PointValuePair(org.hipparchus.util.Pair[typing.List[float], float], java.io.Serializable):
    """
    public class PointValuePair extends Pair<double[],Double> implements Serializable
    
        This class holds a point and the value of an objective function at that point.
    
        Also see:
            :class:`~org.hipparchus.optim.PointVectorValuePair`, null, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], double2: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], double2: float, boolean: bool): ...
    def getPoint(self) -> typing.List[float]:
        """
            Gets the point.
        
            Returns:
                a copy of the stored point.
        
        
        """
        ...
    def getPointRef(self) -> typing.List[float]:
        """
            Gets a reference to the point.
        
            Returns:
                a reference to the internal array storing the point.
        
        
        """
        ...

class PointVectorValuePair(org.hipparchus.util.Pair[typing.List[float], typing.List[float]], java.io.Serializable):
    """
    public class PointVectorValuePair extends Pair<double[],double[]> implements Serializable
    
        This class holds a point and the vectorial value of an objective function at that point.
    
        Also see:
            :class:`~org.hipparchus.optim.PointValuePair`, null, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool): ...
    def getPoint(self) -> typing.List[float]:
        """
            Gets the point.
        
            Returns:
                a copy of the stored point.
        
        
        """
        ...
    def getPointRef(self) -> typing.List[float]:
        """
            Gets a reference to the point.
        
            Returns:
                a reference to the internal array storing the point.
        
        
        """
        ...
    def getValue(self) -> typing.List[float]:
        """
            Gets the value of the objective function.
        
            Overrides:
                 in class 
        
            Returns:
                a copy of the stored value of the objective function.
        
        
        """
        ...
    def getValueRef(self) -> typing.List[float]:
        """
            Gets a reference to the value of the objective function.
        
            Returns:
                a reference to the internal array storing the value of the objective function.
        
        
        """
        ...

_AbstractConvergenceChecker__P = typing.TypeVar('_AbstractConvergenceChecker__P')  # <P>
class AbstractConvergenceChecker(ConvergenceChecker[_AbstractConvergenceChecker__P], typing.Generic[_AbstractConvergenceChecker__P]):
    """
    public abstract class AbstractConvergenceChecker<P> extends Object implements :class:`~org.hipparchus.optim.ConvergenceChecker`<P>
    
        Base class for all convergence checker implementations.
    """
    def __init__(self, double: float, double2: float): ...
    def converged(self, int: int, p: _AbstractConvergenceChecker__P, p2: _AbstractConvergenceChecker__P) -> bool:
        """
            Check if the optimization algorithm has converged.
        
            Specified by:
                :meth:`~org.hipparchus.optim.ConvergenceChecker.converged`Â in
                interfaceÂ :class:`~org.hipparchus.optim.ConvergenceChecker`
        
            Parameters:
                iteration (int): Current iteration.
                previous (:class:`~org.hipparchus.optim.AbstractConvergenceChecker`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.AbstractConvergenceChecker`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the algorithm is considered to have converged.
        
        
        """
        ...
    def getAbsoluteThreshold(self) -> float:
        """
        
            Returns:
                the absolute threshold.
        
        
        """
        ...
    def getRelativeThreshold(self) -> float:
        """
        
            Returns:
                the relative threshold.
        
        
        """
        ...

_AbstractOptimizationProblem__P = typing.TypeVar('_AbstractOptimizationProblem__P')  # <P>
class AbstractOptimizationProblem(OptimizationProblem[_AbstractOptimizationProblem__P], typing.Generic[_AbstractOptimizationProblem__P]):
    """
    public abstract class AbstractOptimizationProblem<P> extends Object implements :class:`~org.hipparchus.optim.OptimizationProblem`<P>
    
        Base class for implementing optimization problems. It contains the boiler-plate code for counting the number of
        evaluations of the objective function and the number of iterations of the algorithm, and storing the convergence
        checker.
    """
    def getConvergenceChecker(self) -> ConvergenceChecker[_AbstractOptimizationProblem__P]: ...
    def getEvaluationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of evaluations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getEvaluationCounter`Â in
                interfaceÂ :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...
    def getIterationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of iterations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getIterationCounter`Â in
                interfaceÂ :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...

_BaseMultivariateOptimizer__P = typing.TypeVar('_BaseMultivariateOptimizer__P')  # <P>
class BaseMultivariateOptimizer(BaseOptimizer[_BaseMultivariateOptimizer__P], typing.Generic[_BaseMultivariateOptimizer__P]):
    """
    public abstract class BaseMultivariateOptimizer<P> extends :class:`~org.hipparchus.optim.BaseOptimizer`<P>
    
        Base class for implementing optimizers for multivariate functions. It contains the boiler-plate code for initial guess
        and bounds specifications. *It is not a "user" class.*
    """
    def getLowerBound(self) -> typing.List[float]:
        """
        
            Returns:
                the lower bounds, or :code:`null` if not set.
        
        
        """
        ...
    def getStartPoint(self) -> typing.List[float]:
        """
            Gets the initial guess.
        
            Returns:
                the initial guess, or :code:`null` if not set.
        
        
        """
        ...
    def getUpperBound(self) -> typing.List[float]:
        """
        
            Returns:
                the upper bounds, or :code:`null` if not set.
        
        
        """
        ...
    @typing.overload
    def optimize(self, optimizationDataArray: typing.List[OptimizationData]) -> _BaseMultivariateOptimizer__P:
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
                :meth:`~org.hipparchus.optim.BaseOptimizer.optimize` in class :class:`~org.hipparchus.optim.BaseOptimizer`
        
            Parameters:
                optData (:class:`~org.hipparchus.optim.OptimizationData`...): Optimization data. In addition to those documented in :meth:`~org.hipparchus.optim.BaseOptimizer.parseOptimizationData`,
                    this method will register the following data:
        
                      - :class:`~org.hipparchus.optim.InitialGuess`
                      - :class:`~org.hipparchus.optim.SimpleBounds`
        
        
            Returns:
                a point/value pair that satisfies the convergence criteria.
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> _BaseMultivariateOptimizer__P: ...

class InitialGuess(OptimizationData):
    def __init__(self, doubleArray: typing.List[float]): ...
    def getInitialGuess(self) -> typing.List[float]: ...

class MaxEval(OptimizationData):
    """
    public class MaxEval extends Object implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Maximum number of evaluations of the function to be optimized.
    """
    def __init__(self, int: int): ...
    def getMaxEval(self) -> int:
        """
            Gets the maximum number of evaluations.
        
            Returns:
                the allowed number of evaluations.
        
        
        """
        ...
    @staticmethod
    def unlimited() -> 'MaxEval':
        """
            Factory method that creates instance of this class that represents a virtually unlimited number of evaluations.
        
            Returns:
                a new instance suitable for allowing null evaluations.
        
        
        """
        ...

class MaxIter(OptimizationData):
    """
    public class MaxIter extends Object implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Maximum number of iterations performed by an (iterative) algorithm.
    """
    def __init__(self, int: int): ...
    def getMaxIter(self) -> int:
        """
            Gets the maximum number of evaluations.
        
            Returns:
                the allowed number of evaluations.
        
        
        """
        ...
    @staticmethod
    def unlimited() -> 'MaxIter':
        """
            Factory method that creates instance of this class that represents a virtually unlimited number of iterations.
        
            Returns:
                a new instance suitable for allowing null evaluations.
        
        
        """
        ...

class SimpleBounds(OptimizationData):
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getLower(self) -> typing.List[float]: ...
    def getUpper(self) -> typing.List[float]: ...
    @staticmethod
    def unbounded(int: int) -> 'SimpleBounds': ...

_BaseMultiStartMultivariateOptimizer__P = typing.TypeVar('_BaseMultiStartMultivariateOptimizer__P')  # <P>
class BaseMultiStartMultivariateOptimizer(BaseMultivariateOptimizer[_BaseMultiStartMultivariateOptimizer__P], typing.Generic[_BaseMultiStartMultivariateOptimizer__P]):
    def __init__(self, baseMultivariateOptimizer: BaseMultivariateOptimizer[_BaseMultiStartMultivariateOptimizer__P], int: int, randomVectorGenerator: org.hipparchus.random.RandomVectorGenerator): ...
    def getEvaluations(self) -> int: ...
    def getOptima(self) -> typing.List[_BaseMultiStartMultivariateOptimizer__P]: ...
    @typing.overload
    def optimize(self, optimizationDataArray: typing.List[OptimizationData]) -> _BaseMultiStartMultivariateOptimizer__P: ...
    @typing.overload
    def optimize(self) -> _BaseMultiStartMultivariateOptimizer__P: ...

_SimplePointChecker__P = typing.TypeVar('_SimplePointChecker__P', bound=org.hipparchus.util.Pair)  # <P>
class SimplePointChecker(AbstractConvergenceChecker[_SimplePointChecker__P], typing.Generic[_SimplePointChecker__P]):
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, p: _SimplePointChecker__P, p2: _SimplePointChecker__P) -> bool: ...

class SimpleValueChecker(AbstractConvergenceChecker[PointValuePair]):
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, pointValuePair: PointValuePair, pointValuePair2: PointValuePair) -> bool: ...

class SimpleVectorValueChecker(AbstractConvergenceChecker[PointVectorValuePair]):
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, pointVectorValuePair: PointVectorValuePair, pointVectorValuePair2: PointVectorValuePair) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim")``.

    AbstractConvergenceChecker: typing.Type[AbstractConvergenceChecker]
    AbstractOptimizationProblem: typing.Type[AbstractOptimizationProblem]
    BaseMultiStartMultivariateOptimizer: typing.Type[BaseMultiStartMultivariateOptimizer]
    BaseMultivariateOptimizer: typing.Type[BaseMultivariateOptimizer]
    BaseOptimizer: typing.Type[BaseOptimizer]
    ConvergenceChecker: typing.Type[ConvergenceChecker]
    InitialGuess: typing.Type[InitialGuess]
    LocalizedOptimFormats: typing.Type[LocalizedOptimFormats]
    MaxEval: typing.Type[MaxEval]
    MaxIter: typing.Type[MaxIter]
    OptimizationData: typing.Type[OptimizationData]
    OptimizationProblem: typing.Type[OptimizationProblem]
    PointValuePair: typing.Type[PointValuePair]
    PointVectorValuePair: typing.Type[PointVectorValuePair]
    SimpleBounds: typing.Type[SimpleBounds]
    SimplePointChecker: typing.Type[SimplePointChecker]
    SimpleValueChecker: typing.Type[SimpleValueChecker]
    SimpleVectorValueChecker: typing.Type[SimpleVectorValueChecker]
    linear: org.hipparchus.optim.linear.__module_protocol__
    nonlinear: org.hipparchus.optim.nonlinear.__module_protocol__
    univariate: org.hipparchus.optim.univariate.__module_protocol__
