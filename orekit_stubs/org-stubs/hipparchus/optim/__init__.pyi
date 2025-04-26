
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import org.hipparchus.exception
import org.hipparchus.optim.linear
import org.hipparchus.optim.nonlinear
import org.hipparchus.optim.univariate
import org.hipparchus.util
import typing



_BaseOptimizer__P = typing.TypeVar('_BaseOptimizer__P')  # <P>
class BaseOptimizer(typing.Generic[_BaseOptimizer__P]):
    """
    public abstract classBaseOptimizer<P> extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
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
    def optimize(self, *optimizationData: 'OptimizationData') -> _BaseOptimizer__P: ...

_ConvergenceChecker__P = typing.TypeVar('_ConvergenceChecker__P')  # <P>
class ConvergenceChecker(typing.Generic[_ConvergenceChecker__P]):
    """
    public interfaceConvergenceChecker<P>
    
        This interface specifies how to check if an optimization algorithm has converged.
    
    
        Deciding if convergence has been reached is a problem-dependent issue. The user should provide a class implementing this
        interface to allow the optimization algorithm to stop its search according to the problem at hand.
    
    
        For convenience, three implementations that fit simple needs are already provided:
        :class:`~org.hipparchus.optim.SimpleValueChecker`, :class:`~org.hipparchus.optim.SimpleVectorValueChecker` and
        :class:`~org.hipparchus.optim.SimplePointChecker`. The first two consider that convergence is reached when the objective
        function value does not change much anymore, it does not use the point set at all. The third one considers that
        convergence is reached when the input point set does not change much anymore, it does not use objective function value
        at all.
    
        Also see:
    
              - :class:`~org.hipparchus.optim.SimplePointChecker`
              - :class:`~org.hipparchus.optim.SimpleValueChecker`
              - :class:`~org.hipparchus.optim.SimpleVectorValueChecker`
    """
    def converged(self, int: int, p: _ConvergenceChecker__P, p2: _ConvergenceChecker__P) -> bool:
        """
            Check if the optimization algorithm has converged.
        
            Parameters:
                iteration (int): Current iteration.
                previous (:class:`~org.hipparchus.optim.ConvergenceChecker`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.ConvergenceChecker`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the algorithm is considered to have converged.
        
        
        """
        ...

class LocalizedOptimFormats(java.lang.Enum['LocalizedOptimFormats'], org.hipparchus.exception.Localizable):
    """
    public enumLocalizedOptimFormats extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.optim.LocalizedOptimFormats`>
    implements :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`
    
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
    CONSTRAINTS_RANK: typing.ClassVar['LocalizedOptimFormats'] = ...
    @typing.overload
    def getLocalizedString(self, string: str, string2: str, locale: java.util.Locale) -> str: ...
    @typing.overload
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`
        
        
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
                name (:class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['LocalizedOptimFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OptimizationData:
    """
    public interfaceOptimizationData
    
        Marker interface. Implementations will provide functionality (optional or required) needed by the optimizers, and those
        will need to check the actual type of the arguments and perform the appropriate cast in order to access the data they
        need.
    """
    ...

_OptimizationProblem__P = typing.TypeVar('_OptimizationProblem__P')  # <P>
class OptimizationProblem(typing.Generic[_OptimizationProblem__P]):
    """
    public interfaceOptimizationProblem<P>
    
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

class PointValuePair(org.hipparchus.util.Pair[typing.MutableSequence[float], float], java.io.Serializable):
    """
    public classPointValuePair extends :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`<double[],:class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double`>
    implements :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class holds a point and the value of an objective function at that point.
    
        Also see:
    
              - :class:`~org.hipparchus.optim.PointVectorValuePair`
              - :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, boolean: bool): ...
    def getPoint(self) -> typing.MutableSequence[float]:
        """
            Gets the point.
        
            Returns:
                a copy of the stored point.
        
        
        """
        ...
    def getPointRef(self) -> typing.MutableSequence[float]:
        """
            Gets a reference to the point.
        
            Returns:
                a reference to the internal array storing the point.
        
        
        """
        ...

class PointVectorValuePair(org.hipparchus.util.Pair[typing.MutableSequence[float], typing.MutableSequence[float]], java.io.Serializable):
    """
    public classPointVectorValuePair extends :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`<double[],double[]>
    implements :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class holds a point and the vectorial value of an objective function at that point.
    
        Also see:
    
              - :class:`~org.hipparchus.optim.PointValuePair`
              - :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], boolean: bool): ...
    def getPoint(self) -> typing.MutableSequence[float]:
        """
            Gets the point.
        
            Returns:
                a copy of the stored point.
        
        
        """
        ...
    def getPointRef(self) -> typing.MutableSequence[float]:
        """
            Gets a reference to the point.
        
            Returns:
                a reference to the internal array storing the point.
        
        
        """
        ...
    def getValue(self) -> typing.MutableSequence[float]:
        """
            Gets the value of the objective function.
        
            Overrides:
                :meth:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus` in
                class :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`
        
            Returns:
                a copy of the stored value of the objective function.
        
        
        """
        ...
    def getValueRef(self) -> typing.MutableSequence[float]:
        """
            Gets a reference to the value of the objective function.
        
            Returns:
                a reference to the internal array storing the value of the objective function.
        
        
        """
        ...

_AbstractConvergenceChecker__P = typing.TypeVar('_AbstractConvergenceChecker__P')  # <P>
class AbstractConvergenceChecker(ConvergenceChecker[_AbstractConvergenceChecker__P], typing.Generic[_AbstractConvergenceChecker__P]):
    """
    public abstract classAbstractConvergenceChecker<P> extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.ConvergenceChecker`<P>
    
        Base class for all convergence checker implementations.
    """
    def converged(self, int: int, p: _AbstractConvergenceChecker__P, p2: _AbstractConvergenceChecker__P) -> bool:
        """
            Check if the optimization algorithm has converged.
        
            Specified by:
                :meth:`~org.hipparchus.optim.ConvergenceChecker.converged` in
                interface :class:`~org.hipparchus.optim.ConvergenceChecker`
        
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
            Get absolute threshold.
        
            Returns:
                the absolute threshold.
        
        
        """
        ...
    def getRelativeThreshold(self) -> float:
        """
            Get relative threshold.
        
            Returns:
                the relative threshold.
        
        
        """
        ...

_AbstractOptimizationProblem__P = typing.TypeVar('_AbstractOptimizationProblem__P')  # <P>
class AbstractOptimizationProblem(OptimizationProblem[_AbstractOptimizationProblem__P], typing.Generic[_AbstractOptimizationProblem__P]):
    """
    public abstract classAbstractOptimizationProblem<P> extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.OptimizationProblem`<P>
    
        Base class for implementing optimization problems. It contains the boiler-plate code for counting the number of
        evaluations of the objective function and the number of iterations of the algorithm, and storing the convergence
        checker.
    """
    def getConvergenceChecker(self) -> ConvergenceChecker[_AbstractOptimizationProblem__P]: ...
    def getEvaluationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of evaluations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getEvaluationCounter` in
                interface :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...
    def getIterationCounter(self) -> org.hipparchus.util.Incrementor:
        """
            Get a independent Incrementor that counts up to the maximum number of iterations and then throws an exception.
        
            Specified by:
                :meth:`~org.hipparchus.optim.OptimizationProblem.getIterationCounter` in
                interface :class:`~org.hipparchus.optim.OptimizationProblem`
        
            Returns:
                a counter for the evaluations.
        
        
        """
        ...

_BaseMultivariateOptimizer__P = typing.TypeVar('_BaseMultivariateOptimizer__P')  # <P>
class BaseMultivariateOptimizer(BaseOptimizer[_BaseMultivariateOptimizer__P], typing.Generic[_BaseMultivariateOptimizer__P]):
    """
    public abstract classBaseMultivariateOptimizer<P> extends :class:`~org.hipparchus.optim.BaseOptimizer`<P>
    
        Base class for implementing optimizers for multivariate functions. It contains the boiler-plate code for initial guess
        and bounds specifications. *It is not a "user" class.*
    """
    def getLowerBound(self) -> typing.MutableSequence[float]:
        """
            Get lower bounds.
        
            Returns:
                the lower bounds, or :code:`null` if not set.
        
        
        """
        ...
    def getStartPoint(self) -> typing.MutableSequence[float]:
        """
            Gets the initial guess.
        
            Returns:
                the initial guess, or :code:`null` if not set.
        
        
        """
        ...
    def getUpperBound(self) -> typing.MutableSequence[float]:
        """
            Get upper bounds.
        
            Returns:
                the upper bounds, or :code:`null` if not set.
        
        
        """
        ...
    @typing.overload
    def optimize(self, *optimizationData: OptimizationData) -> _BaseMultivariateOptimizer__P:
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

_ConvergenceCheckerAndMultiplexer__P = typing.TypeVar('_ConvergenceCheckerAndMultiplexer__P')  # <P>
class ConvergenceCheckerAndMultiplexer(ConvergenceChecker[_ConvergenceCheckerAndMultiplexer__P], typing.Generic[_ConvergenceCheckerAndMultiplexer__P]):
    """
    public classConvergenceCheckerAndMultiplexer<P> extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.ConvergenceChecker`<P>
    
        Multiplexer for :class:`~org.hipparchus.optim.ConvergenceChecker`, checking *all* the checkers converged.
    
        The checkers are checked in the order of the initial list and the check loop is interrupted as soon as one checker fails
        to converge (that is the remaining checkers may *not* be called in first iterations.
    
        Since:
            2.1
    """
    def __init__(self, list: java.util.List[typing.Union[ConvergenceChecker[_ConvergenceCheckerAndMultiplexer__P], typing.Callable[[int, _ConvergenceCheckerAndMultiplexer__P, _ConvergenceCheckerAndMultiplexer__P], bool]]]): ...
    def converged(self, int: int, p: _ConvergenceCheckerAndMultiplexer__P, p2: _ConvergenceCheckerAndMultiplexer__P) -> bool:
        """
            Check if the optimization algorithm has converged.
        
            Specified by:
                :meth:`~org.hipparchus.optim.ConvergenceChecker.converged` in
                interface :class:`~org.hipparchus.optim.ConvergenceChecker`
        
            Parameters:
                iteration (int): Current iteration.
                previous (:class:`~org.hipparchus.optim.ConvergenceCheckerAndMultiplexer`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.ConvergenceCheckerAndMultiplexer`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the algorithm is considered to have converged.
        
        
        """
        ...

_ConvergenceCheckerOrMultiplexer__P = typing.TypeVar('_ConvergenceCheckerOrMultiplexer__P')  # <P>
class ConvergenceCheckerOrMultiplexer(ConvergenceChecker[_ConvergenceCheckerOrMultiplexer__P], typing.Generic[_ConvergenceCheckerOrMultiplexer__P]):
    """
    public classConvergenceCheckerOrMultiplexer<P> extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.ConvergenceChecker`<P>
    
        Multiplexer for :class:`~org.hipparchus.optim.ConvergenceChecker`, checking *one* of the checkers converged.
    
        The checkers are checked in the order of the initial list and the check loop is interrupted as soon as one checker has
        converged (that is the remaining checkers may *not* be called in the final iteration.
    
        Since:
            2.1
    """
    def __init__(self, list: java.util.List[typing.Union[ConvergenceChecker[_ConvergenceCheckerOrMultiplexer__P], typing.Callable[[int, _ConvergenceCheckerOrMultiplexer__P, _ConvergenceCheckerOrMultiplexer__P], bool]]]): ...
    def converged(self, int: int, p: _ConvergenceCheckerOrMultiplexer__P, p2: _ConvergenceCheckerOrMultiplexer__P) -> bool:
        """
            Check if the optimization algorithm has converged.
        
            Specified by:
                :meth:`~org.hipparchus.optim.ConvergenceChecker.converged` in
                interface :class:`~org.hipparchus.optim.ConvergenceChecker`
        
            Parameters:
                iteration (int): Current iteration.
                previous (:class:`~org.hipparchus.optim.ConvergenceCheckerOrMultiplexer`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.ConvergenceCheckerOrMultiplexer`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the algorithm is considered to have converged.
        
        
        """
        ...

class InitialGuess(OptimizationData):
    """
    public classInitialGuess extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Starting point (first guess) of the optimization procedure.
    
    
        Immutable class.
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    def getInitialGuess(self) -> typing.MutableSequence[float]:
        """
            Gets the initial guess.
        
            Returns:
                the initial guess.
        
        
        """
        ...

class MaxEval(OptimizationData):
    """
    public classMaxEval extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.OptimizationData`
    
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
                a new instance suitable for allowing
                :meth:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Integer.MAX_VALUE` evaluations.
        
        
        """
        ...

class MaxIter(OptimizationData):
    """
    public classMaxIter extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.OptimizationData`
    
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
                a new instance suitable for allowing
                :meth:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Integer.MAX_VALUE` evaluations.
        
        
        """
        ...

class SimpleBounds(OptimizationData):
    """
    public classSimpleBounds extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.optim.OptimizationData`
    
        Simple optimization constraints: lower and upper bounds. The valid range of the parameters is an interval that can be
        infinite (in one or both directions).
    
    
        Immutable class.
    """
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    def getLower(self) -> typing.MutableSequence[float]:
        """
            Gets the lower bounds.
        
            Returns:
                the lower bounds.
        
        
        """
        ...
    def getUpper(self) -> typing.MutableSequence[float]:
        """
            Gets the upper bounds.
        
            Returns:
                the upper bounds.
        
        
        """
        ...
    @staticmethod
    def unbounded(int: int) -> 'SimpleBounds':
        """
            Factory method that creates instance of this class that represents unbounded ranges.
        
            Parameters:
                dim (int): Number of parameters.
        
            Returns:
                a new instance suitable for passing to an optimizer that requires bounds specification.
        
        
        """
        ...

_BaseMultiStartMultivariateOptimizer__P = typing.TypeVar('_BaseMultiStartMultivariateOptimizer__P')  # <P>
class BaseMultiStartMultivariateOptimizer(BaseMultivariateOptimizer[_BaseMultiStartMultivariateOptimizer__P], typing.Generic[_BaseMultiStartMultivariateOptimizer__P]):
    """
    public abstract classBaseMultiStartMultivariateOptimizer<P> extends :class:`~org.hipparchus.optim.BaseMultivariateOptimizer`<P>
    
        Base class multi-start optimizer for a multivariate function.
    
    
        This class wraps an optimizer in order to use it several times in turn with different starting points (trying to avoid
        being trapped in a local extremum when looking for a global one). *It is not a "user" class.*
    """
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
    def getOptima(self) -> typing.MutableSequence[_BaseMultiStartMultivariateOptimizer__P]:
        """
            Gets all the optima found during the last call to :code:`optimize`. The optimizer stores all the optima found during a
            set of restarts. The :code:`optimize` method returns the best point only. This method returns all the points found at
            the end of each starts, including the best one already returned by the :code:`optimize` method.
        
        
            The returned array as one element for each start as specified in the constructor. It is ordered with the results from
            the runs that did converge first, sorted from best to worst objective value (i.e in ascending order if minimizing and in
            descending order if maximizing), followed by :code:`null` elements corresponding to the runs that did not converge. This
            means all elements will be :code:`null` if the :code:`optimize` method did throw an exception. This also means that if
            the first element is not :code:`null`, it is the best point found across all starts.
        
        
            The behaviour is undefined if this method is called before :code:`optimize`; it will likely throw
            :code:`NullPointerException`.
        
            Returns:
                an array containing the optima sorted from best to worst.
        
        
        """
        ...
    @typing.overload
    def optimize(self, *optimizationData: OptimizationData) -> _BaseMultiStartMultivariateOptimizer__P:
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
                :meth:`~org.hipparchus.optim.BaseMultivariateOptimizer.optimize` in
                class :class:`~org.hipparchus.optim.BaseMultivariateOptimizer`
        
            Parameters:
                optData (:class:`~org.hipparchus.optim.OptimizationData`...): Optimization data. In addition to those documented in :meth:`~org.hipparchus.optim.BaseOptimizer.parseOptimizationData`,
                    this method will register the following data:
        
                      - :class:`~org.hipparchus.optim.InitialGuess`
                      - :class:`~org.hipparchus.optim.SimpleBounds`
        
        
            Returns:
                a point/value pair that satisfies the convergence criteria.
        
            Raises:
                :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`: if :code:`optData` does not contain an instance of :class:`~org.hipparchus.optim.MaxEval` or
                    :class:`~org.hipparchus.optim.InitialGuess`.
        
        
        """
        ...
    @typing.overload
    def optimize(self) -> _BaseMultiStartMultivariateOptimizer__P: ...

_SimplePointChecker__P = typing.TypeVar('_SimplePointChecker__P', bound=org.hipparchus.util.Pair)  # <P>
class SimplePointChecker(AbstractConvergenceChecker[_SimplePointChecker__P], typing.Generic[_SimplePointChecker__P]):
    """
    public classSimplePointChecker<P extends :class:`~org.hipparchus.optim.https:.www.hipparchus.org.hipparchus`<double[],? extends :class:`~org.hipparchus.optim.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`>> extends :class:`~org.hipparchus.optim.AbstractConvergenceChecker`<P>
    
        Simple implementation of the :class:`~org.hipparchus.optim.ConvergenceChecker` interface using only point coordinates.
        Convergence is considered to have been reached if either the relative difference between each point coordinate are
        smaller than a threshold or if either the absolute difference between the point coordinates are smaller than another
        threshold.
    
    
        The :meth:`~org.hipparchus.optim.SimplePointChecker.converged` method will also return :code:`true` if the number of
        iterations has been set (see :meth:`~org.hipparchus.optim.SimplePointChecker.%3Cinit%3E`).
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, p: _SimplePointChecker__P, p2: _SimplePointChecker__P) -> bool:
        """
            Check if the optimization algorithm has converged considering the last two points. This method may be called several
            times from the same algorithm iteration with different points. This can be detected by checking the iteration number at
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
                previous (:class:`~org.hipparchus.optim.SimplePointChecker`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.SimplePointChecker`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the arguments satify the convergence criterion.
        
        
        """
        ...

class SimpleValueChecker(AbstractConvergenceChecker[PointValuePair]):
    """
    public classSimpleValueChecker extends :class:`~org.hipparchus.optim.AbstractConvergenceChecker`<:class:`~org.hipparchus.optim.PointValuePair`>
    
        Simple implementation of the :class:`~org.hipparchus.optim.ConvergenceChecker` interface using only objective function
        values. Convergence is considered to have been reached if either the relative difference between the objective function
        values is smaller than a threshold or if either the absolute difference between the objective function values is smaller
        than another threshold.
    
    
        The :meth:`~org.hipparchus.optim.SimpleValueChecker.converged` method will also return :code:`true` if the number of
        iterations has been set (see :meth:`~org.hipparchus.optim.SimpleValueChecker.%3Cinit%3E`).
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, pointValuePair: PointValuePair, pointValuePair2: PointValuePair) -> bool:
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
                previous (:class:`~org.hipparchus.optim.PointValuePair`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.PointValuePair`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the algorithm has converged.
        
        
        """
        ...

class SimpleVectorValueChecker(AbstractConvergenceChecker[PointVectorValuePair]):
    """
    public classSimpleVectorValueChecker extends :class:`~org.hipparchus.optim.AbstractConvergenceChecker`<:class:`~org.hipparchus.optim.PointVectorValuePair`>
    
        Simple implementation of the :class:`~org.hipparchus.optim.ConvergenceChecker` interface using only objective function
        values. Convergence is considered to have been reached if either the relative difference between the objective function
        values is smaller than a threshold or if either the absolute difference between the objective function values is smaller
        than another threshold for all vectors elements.
    
    
        The :meth:`~org.hipparchus.optim.SimpleVectorValueChecker.converged` method will also return :code:`true` if the number
        of iterations has been set (see :meth:`~org.hipparchus.optim.SimpleVectorValueChecker.%3Cinit%3E`).
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    def converged(self, int: int, pointVectorValuePair: PointVectorValuePair, pointVectorValuePair2: PointVectorValuePair) -> bool:
        """
            Check if the optimization algorithm has converged considering the last two points. This method may be called several
            times from the same algorithm iteration with different points. This can be detected by checking the iteration number at
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
                previous (:class:`~org.hipparchus.optim.PointVectorValuePair`): Best point in the previous iteration.
                current (:class:`~org.hipparchus.optim.PointVectorValuePair`): Best point in the current iteration.
        
            Returns:
                :code:`true` if the arguments satify the convergence criterion.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim")``.

    AbstractConvergenceChecker: typing.Type[AbstractConvergenceChecker]
    AbstractOptimizationProblem: typing.Type[AbstractOptimizationProblem]
    BaseMultiStartMultivariateOptimizer: typing.Type[BaseMultiStartMultivariateOptimizer]
    BaseMultivariateOptimizer: typing.Type[BaseMultivariateOptimizer]
    BaseOptimizer: typing.Type[BaseOptimizer]
    ConvergenceChecker: typing.Type[ConvergenceChecker]
    ConvergenceCheckerAndMultiplexer: typing.Type[ConvergenceCheckerAndMultiplexer]
    ConvergenceCheckerOrMultiplexer: typing.Type[ConvergenceCheckerOrMultiplexer]
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
