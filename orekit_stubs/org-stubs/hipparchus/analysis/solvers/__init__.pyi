
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.differentiation
import org.hipparchus.analysis.polynomials
import org.hipparchus.complex
import typing



class AllowedSolution(java.lang.Enum['AllowedSolution']):
    """
    public enumAllowedSolution extends :class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.analysis.solvers.AllowedSolution`>
    
        The kinds of solutions that a :class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver` may accept as
        solutions. This basically controls whether or not under-approximations and over-approximations are allowed.
    
        If all solutions are accepted (:meth:`~org.hipparchus.analysis.solvers.AllowedSolution.ANY_SIDE`), then the solution
        that the root-finding algorithm returns for a given root may be equal to the actual root, but it may also be an
        approximation that is slightly smaller or slightly larger than the actual root. Root-finding algorithms generally only
        guarantee that the returned solution is within the requested tolerances. In certain cases however, it may be necessary
        to guarantee that a solution is returned that lies on a specific side the solution.
    
        Also see:
    
              - :class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver`
    """
    ANY_SIDE: typing.ClassVar['AllowedSolution'] = ...
    LEFT_SIDE: typing.ClassVar['AllowedSolution'] = ...
    RIGHT_SIDE: typing.ClassVar['AllowedSolution'] = ...
    BELOW_SIDE: typing.ClassVar['AllowedSolution'] = ...
    ABOVE_SIDE: typing.ClassVar['AllowedSolution'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AllowedSolution':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AllowedSolution']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_BaseUnivariateSolver__F = typing.TypeVar('_BaseUnivariateSolver__F', bound=org.hipparchus.analysis.UnivariateFunction)  # <F>
class BaseUnivariateSolver(typing.Generic[_BaseUnivariateSolver__F]):
    """
    public interfaceBaseUnivariateSolver<F extends :class:`~org.hipparchus.analysis.UnivariateFunction`>
    
        Interface for (univariate real) rootfinding algorithms. Implementations will search for only one zero in the given
        interval. This class is not intended for use outside of the Hipparchus library, regular user should rely on more
        specific interfaces like :class:`~org.hipparchus.analysis.solvers.UnivariateSolver`,
        :class:`~org.hipparchus.analysis.solvers.PolynomialSolver` or
        :class:`~org.hipparchus.analysis.solvers.UnivariateDifferentiableSolver`.
    
        Also see:
    
              - :class:`~org.hipparchus.analysis.solvers.UnivariateSolver`
              - :class:`~org.hipparchus.analysis.solvers.PolynomialSolver`
              - :class:`~org.hipparchus.analysis.solvers.UnivariateDifferentiableSolver`
    """
    def getAbsoluteAccuracy(self) -> float:
        """
            Get the absolute accuracy of the solver. Solutions returned by the solver should be accurate to this tolerance, i.e., if
            ε is the absolute accuracy of the solver and :code:`v` is a value returned by one of the :code:`solve` methods, then a
            root of the function should exist somewhere in the interval (:code:`v` - ε, :code:`v` + ε).
        
            Returns:
                the absolute accuracy.
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the objective function. The number of evaluations corresponds to the last call to the
            :code:`optimize` method. It is 0 if the method has not been called yet.
        
            Returns:
                the number of evaluations of the objective function.
        
        
        """
        ...
    def getFunctionValueAccuracy(self) -> float:
        """
            Get the function value accuracy of the solver. If :code:`v` is a value returned by the solver for a function :code:`f`,
            then by contract, :code:`|f(v)|` should be less than or equal to the function value accuracy configured for the solver.
        
            Returns:
                the function value accuracy.
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
            Get the relative accuracy of the solver. The contract for relative accuracy is the same as
            :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.getAbsoluteAccuracy`, but using relative, rather than
            absolute error. If ρ is the relative accuracy configured for a solver and :code:`v` is a value returned, then a root of
            the function should exist somewhere in the interval (:code:`v` - ρ :code:`v`, :code:`v` + ρ :code:`v`).
        
            Returns:
                the relative accuracy.
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, f: _BaseUnivariateSolver__F, double: float) -> float:
        """
            Solve for a zero in the vicinity of :code:`startValue`.
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`): Function to solve.
                startValue (double): Start value to use.
        
            Returns:
                a value where the function is zero.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the arguments do not satisfy the requirements specified by the solver.
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the allowed number of evaluations is exceeded.
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, f: _BaseUnivariateSolver__F, double: float, double2: float) -> float: ...
    @typing.overload
    def solve(self, int: int, f: _BaseUnivariateSolver__F, double: float, double2: float, double3: float) -> float: ...

_BracketedRealFieldUnivariateSolver__Interval__T = typing.TypeVar('_BracketedRealFieldUnivariateSolver__Interval__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_BracketedRealFieldUnivariateSolver__T = typing.TypeVar('_BracketedRealFieldUnivariateSolver__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class BracketedRealFieldUnivariateSolver(typing.Generic[_BracketedRealFieldUnivariateSolver__T]):
    """
    public interfaceBracketedRealFieldUnivariateSolver<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>>
    
        Interface for :class:`~org.hipparchus.analysis.solvers.UnivariateSolver` that maintain a bracketed solution. There are
        several advantages to having such root-finding algorithms:
    
          - The bracketed solution guarantees that the root is kept within the interval. As such, these algorithms generally also
            guarantee convergence.
          - The bracketed solution means that we have the opportunity to only return roots that are greater than or equal to the
            actual root, or are less than or equal to the actual root. That is, we can control whether under-approximations and
            over-approximations are :class:`~org.hipparchus.analysis.solvers.AllowedSolution`. Other root-finding algorithms can
            usually only guarantee that the solution (the root that was found) is around the actual root.
    
    
        For backwards compatibility, all root-finding algorithms must have
        :meth:`~org.hipparchus.analysis.solvers.AllowedSolution.ANY_SIDE` as default for the allowed solutions.
    
        Also see:
    
              - :class:`~org.hipparchus.analysis.solvers.AllowedSolution`
    """
    def getAbsoluteAccuracy(self) -> _BracketedRealFieldUnivariateSolver__T:
        """
            Get the absolute accuracy of the solver. Solutions returned by the solver should be accurate to this tolerance, i.e., if
            ε is the absolute accuracy of the solver and :code:`v` is a value returned by one of the :code:`solve` methods, then a
            root of the function should exist somewhere in the interval (:code:`v` - ε, :code:`v` + ε).
        
            Returns:
                the absolute accuracy.
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the objective function. The number of evaluations corresponds to the last call to the
            :code:`optimize` method. It is 0 if the method has not been called yet.
        
            Returns:
                the number of evaluations of the objective function.
        
        
        """
        ...
    def getFunctionValueAccuracy(self) -> _BracketedRealFieldUnivariateSolver__T:
        """
            Get the function value accuracy of the solver. If :code:`v` is a value returned by the solver for a function :code:`f`,
            then by contract, :code:`|f(v)|` should be less than or equal to the function value accuracy configured for the solver.
        
            Returns:
                the function value accuracy.
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
            Get the maximum number of function evaluations.
        
            Returns:
                the maximum number of function evaluations.
        
        
        """
        ...
    def getRelativeAccuracy(self) -> _BracketedRealFieldUnivariateSolver__T:
        """
            Get the relative accuracy of the solver. The contract for relative accuracy is the same as
            :meth:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver.getAbsoluteAccuracy`, but using relative,
            rather than absolute error. If ρ is the relative accuracy configured for a solver and :code:`v` is a value returned,
            then a root of the function should exist somewhere in the interval (:code:`v` - ρ :code:`v`, :code:`v` + ρ :code:`v`).
        
            Returns:
                the relative accuracy.
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_BracketedRealFieldUnivariateSolver__T], typing.Callable[[_BracketedRealFieldUnivariateSolver__T], _BracketedRealFieldUnivariateSolver__T]], t: _BracketedRealFieldUnivariateSolver__T, t2: _BracketedRealFieldUnivariateSolver__T, t3: _BracketedRealFieldUnivariateSolver__T, allowedSolution: AllowedSolution) -> _BracketedRealFieldUnivariateSolver__T: ...
    @typing.overload
    def solve(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_BracketedRealFieldUnivariateSolver__T], typing.Callable[[_BracketedRealFieldUnivariateSolver__T], _BracketedRealFieldUnivariateSolver__T]], t: _BracketedRealFieldUnivariateSolver__T, t2: _BracketedRealFieldUnivariateSolver__T, allowedSolution: AllowedSolution) -> _BracketedRealFieldUnivariateSolver__T: ...
    @typing.overload
    def solveInterval(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_BracketedRealFieldUnivariateSolver__T], typing.Callable[[_BracketedRealFieldUnivariateSolver__T], _BracketedRealFieldUnivariateSolver__T]], t: _BracketedRealFieldUnivariateSolver__T, t2: _BracketedRealFieldUnivariateSolver__T, t3: _BracketedRealFieldUnivariateSolver__T) -> 'BracketedRealFieldUnivariateSolver.Interval'[_BracketedRealFieldUnivariateSolver__T]: ...
    @typing.overload
    def solveInterval(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_BracketedRealFieldUnivariateSolver__T], typing.Callable[[_BracketedRealFieldUnivariateSolver__T], _BracketedRealFieldUnivariateSolver__T]], t: _BracketedRealFieldUnivariateSolver__T, t2: _BracketedRealFieldUnivariateSolver__T) -> 'BracketedRealFieldUnivariateSolver.Interval'[_BracketedRealFieldUnivariateSolver__T]: ...
    class Interval(typing.Generic[_BracketedRealFieldUnivariateSolver__Interval__T]):
        def __init__(self, t: _BracketedRealFieldUnivariateSolver__Interval__T, t2: _BracketedRealFieldUnivariateSolver__Interval__T, t3: _BracketedRealFieldUnivariateSolver__Interval__T, t4: _BracketedRealFieldUnivariateSolver__Interval__T): ...
        def getLeftAbscissa(self) -> _BracketedRealFieldUnivariateSolver__Interval__T: ...
        def getLeftValue(self) -> _BracketedRealFieldUnivariateSolver__Interval__T: ...
        def getRightAbscissa(self) -> _BracketedRealFieldUnivariateSolver__Interval__T: ...
        def getRightValue(self) -> _BracketedRealFieldUnivariateSolver__Interval__T: ...
        def getSide(self, allowedSolution: AllowedSolution) -> _BracketedRealFieldUnivariateSolver__Interval__T: ...

class UnivariateSolverUtils:
    """
    public classUnivariateSolverUtils extends :class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Utility routines for :class:`~org.hipparchus.analysis.solvers.UnivariateSolver` objects.
    """
    _bracket_3__T = typing.TypeVar('_bracket_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bracket_4__T = typing.TypeVar('_bracket_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _bracket_5__T = typing.TypeVar('_bracket_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def bracket(univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float) -> typing.MutableSequence[float]: ...
    @typing.overload
    @staticmethod
    def bracket(univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float, double4: float, double5: float, int: int) -> typing.MutableSequence[float]: ...
    @typing.overload
    @staticmethod
    def bracket(univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float, int: int) -> typing.MutableSequence[float]: ...
    @typing.overload
    @staticmethod
    def bracket(calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_bracket_3__T], typing.Callable[[_bracket_3__T], _bracket_3__T]], t: _bracket_3__T, t2: _bracket_3__T, t3: _bracket_3__T) -> typing.MutableSequence[_bracket_3__T]: ...
    @typing.overload
    @staticmethod
    def bracket(calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_bracket_4__T], typing.Callable[[_bracket_4__T], _bracket_4__T]], t: _bracket_4__T, t2: _bracket_4__T, t3: _bracket_4__T, int: int) -> typing.MutableSequence[_bracket_4__T]: ...
    @typing.overload
    @staticmethod
    def bracket(calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_bracket_5__T], typing.Callable[[_bracket_5__T], _bracket_5__T]], t: _bracket_5__T, t2: _bracket_5__T, t3: _bracket_5__T, t4: _bracket_5__T, t5: _bracket_5__T, int: int) -> typing.MutableSequence[_bracket_5__T]: ...
    @staticmethod
    def forceSide(int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], bracketedUnivariateSolver: 'BracketedUnivariateSolver'[typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]], double: float, double2: float, double3: float, allowedSolution: AllowedSolution) -> float: ...
    @staticmethod
    def isBracketing(univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float) -> bool: ...
    @staticmethod
    def isSequence(double: float, double2: float, double3: float) -> bool:
        """
            Check whether the arguments form a (strictly) increasing sequence.
        
            Parameters:
                start (double): First number.
                mid (double): Second number.
                end (double): Third number.
        
            Returns:
                :code:`true` if the arguments form an increasing sequence.
        
        
        """
        ...
    @staticmethod
    def midpoint(double: float, double2: float) -> float:
        """
            Compute the midpoint of two values.
        
            Parameters:
                a (double): first value.
                b (double): second value.
        
            Returns:
                the midpoint.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def solve(univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def solve(univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float) -> float: ...
    @staticmethod
    def verifyBracketing(univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float) -> None: ...
    @staticmethod
    def verifyInterval(double: float, double2: float) -> None: ...
    @staticmethod
    def verifySequence(double: float, double2: float, double3: float) -> None: ...

_BaseAbstractUnivariateSolver__F = typing.TypeVar('_BaseAbstractUnivariateSolver__F', bound=org.hipparchus.analysis.UnivariateFunction)  # <F>
class BaseAbstractUnivariateSolver(BaseUnivariateSolver[_BaseAbstractUnivariateSolver__F], typing.Generic[_BaseAbstractUnivariateSolver__F]):
    """
    public abstract classBaseAbstractUnivariateSolver<F extends :class:`~org.hipparchus.analysis.UnivariateFunction`> extends :class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`<F>
    
        Provide a default implementation for several functions useful to generic solvers. The default values for relative and
        function tolerances are 1e-14 and 1e-15, respectively. It is however highly recommended to not rely on the default, but
        rather carefully consider values that match user's expectations, as well as the specifics of each implementation.
    """
    def getAbsoluteAccuracy(self) -> float:
        """
            Get the absolute accuracy of the solver. Solutions returned by the solver should be accurate to this tolerance, i.e., if
            ε is the absolute accuracy of the solver and :code:`v` is a value returned by one of the :code:`solve` methods, then a
            root of the function should exist somewhere in the interval (:code:`v` - ε, :code:`v` + ε).
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.getAbsoluteAccuracy` in
                interface :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`
        
            Returns:
                the absolute accuracy.
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the objective function. The number of evaluations corresponds to the last call to the
            :code:`optimize` method. It is 0 if the method has not been called yet.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.getEvaluations` in
                interface :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`
        
            Returns:
                the number of evaluations of the objective function.
        
        
        """
        ...
    def getFunctionValueAccuracy(self) -> float:
        """
            Get the function value accuracy of the solver. If :code:`v` is a value returned by the solver for a function :code:`f`,
            then by contract, :code:`|f(v)|` should be less than or equal to the function value accuracy configured for the solver.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.getFunctionValueAccuracy` in
                interface :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`
        
            Returns:
                the function value accuracy.
        
        
        """
        ...
    def getMax(self) -> float:
        """
            Get higher end of the search interval.
        
            Returns:
                the higher end of the search interval
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Get lower end of the search interval.
        
            Returns:
                the lower end of the search interval
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
            Get the relative accuracy of the solver. The contract for relative accuracy is the same as
            :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.getAbsoluteAccuracy`, but using relative, rather than
            absolute error. If ρ is the relative accuracy configured for a solver and :code:`v` is a value returned, then a root of
            the function should exist somewhere in the interval (:code:`v` - ρ :code:`v`, :code:`v` + ρ :code:`v`).
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.getRelativeAccuracy` in
                interface :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`
        
            Returns:
                the relative accuracy.
        
        
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
    def solve(self, int: int, f: _BaseAbstractUnivariateSolver__F, double: float) -> float:
        """
            Solve for a zero root in the given interval. A solver may require that the interval brackets a single zero root. Solvers
            that do require bracketing should be able to handle the case where one of the endpoints is itself a root.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.solve` in
                interface :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver`): Function to solve.
                min (double): Lower bound for the interval.
                max (double): Upper bound for the interval.
        
            Returns:
                a value where the function is zero.
        
        public double solve(int maxEval, :class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver` f, double startValue) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`, :class:`~org.hipparchus.exception.MathIllegalStateException`
        
            Solve for a zero in the vicinity of :code:`startValue`.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.solve` in
                interface :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver`): Function to solve.
                startValue (double): Start value to use.
        
            Returns:
                a value where the function is zero.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the arguments do not satisfy the requirements specified by the solver.
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the allowed number of evaluations is exceeded.
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, f: _BaseAbstractUnivariateSolver__F, double: float, double2: float) -> float: ...
    @typing.overload
    def solve(self, int: int, f: _BaseAbstractUnivariateSolver__F, double: float, double2: float, double3: float) -> float: ...

_BracketedUnivariateSolver__F = typing.TypeVar('_BracketedUnivariateSolver__F', bound=org.hipparchus.analysis.UnivariateFunction)  # <F>
class BracketedUnivariateSolver(BaseUnivariateSolver[_BracketedUnivariateSolver__F], typing.Generic[_BracketedUnivariateSolver__F]):
    """
    public interfaceBracketedUnivariateSolver<F extends :class:`~org.hipparchus.analysis.UnivariateFunction`>extends :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`<F>
    
        Interface for :class:`~org.hipparchus.analysis.solvers.UnivariateSolver` that maintain a bracketed solution. There are
        several advantages to having such root-finding algorithms:
    
          - The bracketed solution guarantees that the root is kept within the interval. As such, these algorithms generally also
            guarantee convergence.
          - The bracketed solution means that we have the opportunity to only return roots that are greater than or equal to the
            actual root, or are less than or equal to the actual root. That is, we can control whether under-approximations and
            over-approximations are :class:`~org.hipparchus.analysis.solvers.AllowedSolution`. Other root-finding algorithms can
            usually only guarantee that the solution (the root that was found) is around the actual root.
    
    
        For backwards compatibility, all root-finding algorithms must have
        :meth:`~org.hipparchus.analysis.solvers.AllowedSolution.ANY_SIDE` as default for the allowed solutions.
    
        Also see:
    
              - :class:`~org.hipparchus.analysis.solvers.AllowedSolution`
    """
    @typing.overload
    def solve(self, int: int, f: _BracketedUnivariateSolver__F, double: float) -> float:
        """
            Solve for a zero in the given interval. A solver may require that the interval brackets a single zero root. Solvers that
            do require bracketing should be able to handle the case where one of the endpoints is itself a root.
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver`): Function to solve.
                min (double): Lower bound for the interval.
                max (double): Upper bound for the interval.
                allowedSolution (:class:`~org.hipparchus.analysis.solvers.AllowedSolution`): The kind of solutions that the root-finding algorithm may accept as solutions.
        
            Returns:
                A value where the function is zero.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the arguments do not satisfy the requirements specified by the solver.
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the allowed number of evaluations is exceeded.
        
            Solve for a zero in the given interval, start at :code:`startValue`. A solver may require that the interval brackets a
            single zero root. Solvers that do require bracketing should be able to handle the case where one of the endpoints is
            itself a root.
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver`): Function to solve.
                min (double): Lower bound for the interval.
                max (double): Upper bound for the interval.
                startValue (double): Start value to use.
                allowedSolution (:class:`~org.hipparchus.analysis.solvers.AllowedSolution`): The kind of solutions that the root-finding algorithm may accept as solutions.
        
            Returns:
                A value where the function is zero.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the arguments do not satisfy the requirements specified by the solver.
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the allowed number of evaluations is exceeded.
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, f: _BracketedUnivariateSolver__F, double: float, double2: float) -> float: ...
    @typing.overload
    def solve(self, int: int, f: _BracketedUnivariateSolver__F, double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    def solve(self, int: int, f: _BracketedUnivariateSolver__F, double: float, double2: float, double3: float, allowedSolution: AllowedSolution) -> float: ...
    @typing.overload
    def solve(self, int: int, f: _BracketedUnivariateSolver__F, double: float, double2: float, allowedSolution: AllowedSolution) -> float: ...
    @typing.overload
    def solveInterval(self, int: int, f: _BracketedUnivariateSolver__F, double: float, double2: float, double3: float) -> 'BracketedUnivariateSolver.Interval': ...
    @typing.overload
    def solveInterval(self, int: int, f: _BracketedUnivariateSolver__F, double: float, double2: float) -> 'BracketedUnivariateSolver.Interval': ...
    class Interval:
        def __init__(self, double: float, double2: float, double3: float, double4: float): ...
        def getLeftAbscissa(self) -> float: ...
        def getLeftValue(self) -> float: ...
        def getRightAbscissa(self) -> float: ...
        def getRightValue(self) -> float: ...
        def getSide(self, allowedSolution: AllowedSolution) -> float: ...

_FieldBracketingNthOrderBrentSolver__T = typing.TypeVar('_FieldBracketingNthOrderBrentSolver__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBracketingNthOrderBrentSolver(BracketedRealFieldUnivariateSolver[_FieldBracketingNthOrderBrentSolver__T], typing.Generic[_FieldBracketingNthOrderBrentSolver__T]):
    """
    public classFieldBracketingNthOrderBrentSolver<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver`<T>
    
        This class implements a modification of the ` Brent algorithm <http://mathworld.wolfram.com/BrentsMethod.html>`.
    
        The changes with respect to the original Brent algorithm are:
    
          - the returned value is chosen in the current interval according to user specified
            :class:`~org.hipparchus.analysis.solvers.AllowedSolution`
          - the maximal order for the invert polynomial root search is user-specified instead of being invert quadratic only
    
    
        The given interval must bracket the root.
    """
    def __init__(self, t: _FieldBracketingNthOrderBrentSolver__T, t2: _FieldBracketingNthOrderBrentSolver__T, t3: _FieldBracketingNthOrderBrentSolver__T, int: int): ...
    def getAbsoluteAccuracy(self) -> _FieldBracketingNthOrderBrentSolver__T:
        """
            Get the absolute accuracy.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver.getAbsoluteAccuracy` in
                interface :class:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver`
        
            Returns:
                absolute accuracy
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of evaluations of the objective function. The number of evaluations corresponds to the last call to the
            :code:`optimize` method. It is 0 if the method has not been called yet.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver.getEvaluations` in
                interface :class:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver`
        
            Returns:
                the number of evaluations of the objective function.
        
        
        """
        ...
    def getFunctionValueAccuracy(self) -> _FieldBracketingNthOrderBrentSolver__T:
        """
            Get the function accuracy.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver.getFunctionValueAccuracy` in
                interface :class:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver`
        
            Returns:
                function accuracy
        
        
        """
        ...
    def getMaxEvaluations(self) -> int:
        """
            Get the maximal number of function evaluations.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver.getMaxEvaluations` in
                interface :class:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver`
        
            Returns:
                the maximal number of function evaluations.
        
        
        """
        ...
    def getMaximalOrder(self) -> int:
        """
            Get the maximal order.
        
            Returns:
                maximal order
        
        
        """
        ...
    def getRelativeAccuracy(self) -> _FieldBracketingNthOrderBrentSolver__T:
        """
            Get the relative accuracy.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver.getRelativeAccuracy` in
                interface :class:`~org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver`
        
            Returns:
                relative accuracy
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldBracketingNthOrderBrentSolver__T], typing.Callable[[_FieldBracketingNthOrderBrentSolver__T], _FieldBracketingNthOrderBrentSolver__T]], t: _FieldBracketingNthOrderBrentSolver__T, t2: _FieldBracketingNthOrderBrentSolver__T, t3: _FieldBracketingNthOrderBrentSolver__T, allowedSolution: AllowedSolution) -> _FieldBracketingNthOrderBrentSolver__T: ...
    @typing.overload
    def solve(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldBracketingNthOrderBrentSolver__T], typing.Callable[[_FieldBracketingNthOrderBrentSolver__T], _FieldBracketingNthOrderBrentSolver__T]], t: _FieldBracketingNthOrderBrentSolver__T, t2: _FieldBracketingNthOrderBrentSolver__T, allowedSolution: AllowedSolution) -> _FieldBracketingNthOrderBrentSolver__T: ...
    @typing.overload
    def solveInterval(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldBracketingNthOrderBrentSolver__T], typing.Callable[[_FieldBracketingNthOrderBrentSolver__T], _FieldBracketingNthOrderBrentSolver__T]], t: _FieldBracketingNthOrderBrentSolver__T, t2: _FieldBracketingNthOrderBrentSolver__T) -> BracketedRealFieldUnivariateSolver.Interval[_FieldBracketingNthOrderBrentSolver__T]: ...
    @typing.overload
    def solveInterval(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldBracketingNthOrderBrentSolver__T], typing.Callable[[_FieldBracketingNthOrderBrentSolver__T], _FieldBracketingNthOrderBrentSolver__T]], t: _FieldBracketingNthOrderBrentSolver__T, t2: _FieldBracketingNthOrderBrentSolver__T, t3: _FieldBracketingNthOrderBrentSolver__T) -> BracketedRealFieldUnivariateSolver.Interval[_FieldBracketingNthOrderBrentSolver__T]: ...

class PolynomialSolver(BaseUnivariateSolver[org.hipparchus.analysis.polynomials.PolynomialFunction]):
    """
    public interfacePolynomialSolverextends :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`<:class:`~org.hipparchus.analysis.polynomials.PolynomialFunction`>
    
        Interface for (polynomial) root-finding algorithms. Implementations will search for only one zero in the given interval.
    """
    ...

class UnivariateDifferentiableSolver(BaseUnivariateSolver[org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction]):
    """
    public interfaceUnivariateDifferentiableSolverextends :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`<:class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`>
    
        Interface for (univariate real) rootfinding algorithms. Implementations will search for only one zero in the given
        interval.
    """
    ...

class UnivariateSolver(BaseUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]):
    """
    public interfaceUnivariateSolverextends :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`<:class:`~org.hipparchus.analysis.UnivariateFunction`>
    
        Interface for (univariate real) root-finding algorithms. Implementations will search for only one zero in the given
        interval.
    """
    ...

class AbstractPolynomialSolver(BaseAbstractUnivariateSolver[org.hipparchus.analysis.polynomials.PolynomialFunction], PolynomialSolver):
    """
    public abstract classAbstractPolynomialSolver extends :class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver`<:class:`~org.hipparchus.analysis.polynomials.PolynomialFunction`>
    implements :class:`~org.hipparchus.analysis.solvers.PolynomialSolver`
    
        Base class for solvers.
    """
    ...

class AbstractUnivariateDifferentiableSolver(BaseAbstractUnivariateSolver[org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction], UnivariateDifferentiableSolver):
    """
    public abstract classAbstractUnivariateDifferentiableSolver extends :class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver`<:class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`>
    implements :class:`~org.hipparchus.analysis.solvers.UnivariateDifferentiableSolver`
    
        Provide a default implementation for several functions useful to generic solvers.
    """
    ...

class AbstractUnivariateSolver(BaseAbstractUnivariateSolver[org.hipparchus.analysis.UnivariateFunction], UnivariateSolver):
    """
    public abstract classAbstractUnivariateSolver extends :class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver`<:class:`~org.hipparchus.analysis.UnivariateFunction`>
    implements :class:`~org.hipparchus.analysis.solvers.UnivariateSolver`
    
        Base class for solvers.
    """
    ...

class BaseSecantSolver(AbstractUnivariateSolver, BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]):
    """
    public abstract classBaseSecantSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    implements :class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver`<:class:`~org.hipparchus.analysis.UnivariateFunction`>
    
        Base class for all bracketing *Secant*-based methods for root-finding (approximating a zero of a univariate real
        function).
    
        Implementation of the :class:`~org.hipparchus.analysis.solvers.RegulaFalsiSolver` and
        :class:`~org.hipparchus.analysis.solvers.IllinoisSolver` methods is based on the following article: M. Dowell and P.
        Jarratt, *A modified regula falsi method for computing the root of an equation*, BIT Numerical Mathematics, volume 11,
        number 2, pages 168-174, Springer, 1971.
    
        Implementation of the :class:`~org.hipparchus.analysis.solvers.PegasusSolver` method is based on the following article:
        M. Dowell and P. Jarratt, *The "Pegasus" method for computing the root of an equation*, BIT Numerical Mathematics,
        volume 12, number 4, pages 503-508, Springer, 1972.
    
        The :class:`~org.hipparchus.analysis.solvers.SecantSolver` method is *not* a bracketing method, so it is not implemented
        here. It has a separate implementation.
    """
    @typing.overload
    def solve(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float) -> float:
        """
            Solve for a zero in the given interval. A solver may require that the interval brackets a single zero root. Solvers that
            do require bracketing should be able to handle the case where one of the endpoints is itself a root.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver.solve` in
                interface :class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver`
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to solve.
                min (double): Lower bound for the interval.
                max (double): Upper bound for the interval.
                allowedSolution (:class:`~org.hipparchus.analysis.solvers.AllowedSolution`): The kind of solutions that the root-finding algorithm may accept as solutions.
        
            Returns:
                A value where the function is zero.
        
            Solve for a zero in the given interval, start at :code:`startValue`. A solver may require that the interval brackets a
            single zero root. Solvers that do require bracketing should be able to handle the case where one of the endpoints is
            itself a root.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver.solve` in
                interface :class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver`
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to solve.
                min (double): Lower bound for the interval.
                max (double): Upper bound for the interval.
                startValue (double): Start value to use.
                allowedSolution (:class:`~org.hipparchus.analysis.solvers.AllowedSolution`): The kind of solutions that the root-finding algorithm may accept as solutions.
        
            Returns:
                A value where the function is zero.
        
            Solve for a zero in the given interval, start at :code:`startValue`. A solver may require that the interval brackets a
            single zero root. Solvers that do require bracketing should be able to handle the case where one of the endpoints is
            itself a root.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver.solve` in
                interface :class:`~org.hipparchus.analysis.solvers.BaseUnivariateSolver`
        
            Overrides:
                :meth:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver.solve` in
                class :class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver`
        
            Parameters:
                maxEval (int): Maximum number of evaluations.
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to solve.
                min (double): Lower bound for the interval.
                max (double): Upper bound for the interval.
                startValue (double): Start value to use.
        
            Returns:
                a value where the function is zero.
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float) -> float: ...
    @typing.overload
    def solve(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    def solve(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float, allowedSolution: AllowedSolution) -> float: ...
    @typing.overload
    def solve(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, allowedSolution: AllowedSolution) -> float: ...
    @typing.overload
    def solveInterval(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float) -> BracketedUnivariateSolver.Interval: ...
    @typing.overload
    def solveInterval(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float) -> BracketedUnivariateSolver.Interval: ...

class BisectionSolver(AbstractUnivariateSolver):
    """
    public classBisectionSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    
        Implements the ` bisection algorithm <http://mathworld.wolfram.com/Bisection.html>` for finding zeros of univariate real
        functions.
    
        The function should be continuous but not necessarily smooth.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...

class BracketingNthOrderBrentSolver(AbstractUnivariateSolver, BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]):
    """
    public classBracketingNthOrderBrentSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    implements :class:`~org.hipparchus.analysis.solvers.BracketedUnivariateSolver`<:class:`~org.hipparchus.analysis.UnivariateFunction`>
    
        This class implements a modification of the ` Brent algorithm <http://mathworld.wolfram.com/BrentsMethod.html>`.
    
        The changes with respect to the original Brent algorithm are:
    
          - the returned value is chosen in the current interval according to user specified
            :class:`~org.hipparchus.analysis.solvers.AllowedSolution`,
          - the maximal order for the invert polynomial root search is user-specified instead of being invert quadratic only
    
    
        The given interval must bracket the root.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    def getMaximalOrder(self) -> int:
        """
            Get the maximal order.
        
            Returns:
                maximal order
        
        
        """
        ...
    @typing.overload
    def solve(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float) -> float: ...
    @typing.overload
    def solve(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float) -> float: ...
    @typing.overload
    def solve(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    def solve(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float, allowedSolution: AllowedSolution) -> float: ...
    @typing.overload
    def solve(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, allowedSolution: AllowedSolution) -> float: ...
    @typing.overload
    def solveInterval(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float) -> BracketedUnivariateSolver.Interval: ...
    @typing.overload
    def solveInterval(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float, double3: float) -> BracketedUnivariateSolver.Interval: ...

class BrentSolver(AbstractUnivariateSolver):
    """
    public classBrentSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    
        This class implements the ` Brent algorithm <http://mathworld.wolfram.com/BrentsMethod.html>` for finding zeros of real
        univariate functions. The function should be continuous but not necessarily smooth. The :code:`solve` method returns a
        zero :code:`x` of the function :code:`f` in the given interval :code:`[a, b]` to within a tolerance :code:`2 eps abs(x)
        + t` where :code:`eps` is the relative accuracy and :code:`t` is the absolute accuracy.
    
        The given interval must bracket the root.
    
        The reference implementation is given in chapter 4 of
            **Algorithms for Minimization Without Derivatives**, *Richard P. Brent*, Dover, 2002
    
        Also see:
    
              - :class:`~org.hipparchus.analysis.solvers.BaseAbstractUnivariateSolver`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...

class LaguerreSolver(AbstractPolynomialSolver):
    """
    public classLaguerreSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractPolynomialSolver`
    
        Implements the ` Laguerre's Method <http://mathworld.wolfram.com/LaguerresMethod.html>` for root finding of real
        coefficient polynomials. For reference, see
            **A First Course in Numerical Analysis**, ISBN 048641454X, chapter 8.
        Laguerre's method is global in the sense that it can start with any initial approximation and be able to solve all roots
        from that point. The algorithm requires a bracketing condition.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    def doSolve(self) -> float: ...
    @typing.overload
    def solveAllComplex(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> typing.MutableSequence[org.hipparchus.complex.Complex]: ...
    @typing.overload
    def solveAllComplex(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, double2: float) -> typing.MutableSequence[org.hipparchus.complex.Complex]: ...
    def solveComplex(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.complex.Complex: ...

class MullerSolver(AbstractUnivariateSolver):
    """
    public classMullerSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    
        This class implements the ` Muller's Method <http://mathworld.wolfram.com/MullersMethod.html>` for root finding of real
        univariate functions. For reference, see **Elementary Numerical Analysis**, ISBN 0070124477, chapter 3.
    
        Muller's method applies to both real and complex functions, but here we restrict ourselves to real functions. This class
        differs from :class:`~org.hipparchus.analysis.solvers.MullerSolver` in the way it avoids complex operations.
    
        Muller's original method would have function evaluation at complex point. Since our f(x) is real, we have to find ways
        to avoid that. Bracketing condition is one way to go: by requiring bracketing in every iteration, the newly computed
        approximation is guaranteed to be real.
    
        Normally Muller's method converges quadratically in the vicinity of a zero, however it may be very slow in regions far
        away from zeros. For example, f(x) = exp(x) - 1, min = -50, max = 100. In such case we use bisection as a safety backup
        if it performs very poorly.
    
        The formulas here use divided differences directly.
    
        Also see:
    
              - :class:`~org.hipparchus.analysis.solvers.MullerSolver2`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...

class MullerSolver2(AbstractUnivariateSolver):
    """
    public classMullerSolver2 extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    
        This class implements the ` Muller's Method <http://mathworld.wolfram.com/MullersMethod.html>` for root finding of real
        univariate functions. For reference, see **Elementary Numerical Analysis**, ISBN 0070124477, chapter 3.
    
        Muller's method applies to both real and complex functions, but here we restrict ourselves to real functions. This class
        differs from :class:`~org.hipparchus.analysis.solvers.MullerSolver` in the way it avoids complex operations.
    
        Except for the initial [min, max], it does not require bracketing condition, e.g. f(x0), f(x1), f(x2) can have the same
        sign. If a complex number arises in the computation, we simply use its modulus as a real approximation.
    
        Because the interval may not be bracketing, the bisection alternative is not applicable here. However in practice our
        treatment usually works well, especially near real zeroes where the imaginary part of the complex approximation is often
        negligible.
    
        The formulas here do not use divided differences directly.
    
        Also see:
    
              - :class:`~org.hipparchus.analysis.solvers.MullerSolver`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...

class NewtonRaphsonSolver(AbstractUnivariateDifferentiableSolver):
    """
    public classNewtonRaphsonSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateDifferentiableSolver`
    
        Implements ` Newton's Method <http://mathworld.wolfram.com/NewtonsMethod.html>` for finding zeros of real univariate
        differentiable functions.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def solve(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float) -> float: ...
    @typing.overload
    def solve(self, int: int, f: org.hipparchus.analysis.UnivariateFunction, double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    def solve(self, int: int, univariateDifferentiableFunction: org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, double: float, double2: float) -> float: ...

class RiddersSolver(AbstractUnivariateSolver):
    """
    public classRiddersSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    
        Implements the ` Ridders' Method <http://mathworld.wolfram.com/RiddersMethod.html>` for root finding of real univariate
        functions. For reference, see C. Ridders, *A new algorithm for computing a single root of a real continuous function*,
        IEEE Transactions on Circuits and Systems, 26 (1979), 979 - 980.
    
        The function should be continuous but not necessarily smooth.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...

class SecantSolver(AbstractUnivariateSolver):
    """
    public classSecantSolver extends :class:`~org.hipparchus.analysis.solvers.AbstractUnivariateSolver`
    
        Implements the *Secant* method for root-finding (approximating a zero of a univariate real function). The solution that
        is maintained is not bracketed, and as such convergence is not guaranteed.
    
        Implementation based on the following article: M. Dowell and P. Jarratt, *A modified regula falsi method for computing
        the root of an equation*, BIT Numerical Mathematics, volume 11, number 2, pages 168-174, Springer, 1971.
    
        Note that since release 3.0 this class implements the actual *Secant* algorithm, and not a modified one. As such, the
        3.0 version is not backwards compatible with previous versions. To use an algorithm similar to the pre-3.0 releases, use
        the :class:`~org.hipparchus.analysis.solvers.IllinoisSolver` algorithm or the
        :class:`~org.hipparchus.analysis.solvers.PegasusSolver` algorithm.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...

class IllinoisSolver(BaseSecantSolver):
    """
    public classIllinoisSolver extends :class:`~org.hipparchus.analysis.solvers.BaseSecantSolver`
    
        Implements the *Illinois* method for root-finding (approximating a zero of a univariate real function). It is a modified
        :class:`~org.hipparchus.analysis.solvers.RegulaFalsiSolver` method.
    
        Like the *Regula Falsi* method, convergence is guaranteed by maintaining a bracketed solution. The *Illinois* method
        however, should converge much faster than the original *Regula Falsi* method. Furthermore, this implementation of the
        *Illinois* method should not suffer from the same implementation issues as the *Regula Falsi* method, which may fail to
        convergence in certain cases.
    
        The *Illinois* method assumes that the function is continuous, but not necessarily smooth.
    
        Implementation based on the following article: M. Dowell and P. Jarratt, *A modified regula falsi method for computing
        the root of an equation*, BIT Numerical Mathematics, volume 11, number 2, pages 168-174, Springer, 1971.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...

class PegasusSolver(BaseSecantSolver):
    """
    public classPegasusSolver extends :class:`~org.hipparchus.analysis.solvers.BaseSecantSolver`
    
        Implements the *Pegasus* method for root-finding (approximating a zero of a univariate real function). It is a modified
        :class:`~org.hipparchus.analysis.solvers.RegulaFalsiSolver` method.
    
        Like the *Regula Falsi* method, convergence is guaranteed by maintaining a bracketed solution. The *Pegasus* method
        however, should converge much faster than the original *Regula Falsi* method. Furthermore, this implementation of the
        *Pegasus* method should not suffer from the same implementation issues as the *Regula Falsi* method, which may fail to
        convergence in certain cases. Also, the *Pegasus* method should converge faster than the
        :class:`~org.hipparchus.analysis.solvers.IllinoisSolver` method, another *Regula Falsi*-based method.
    
        The *Pegasus* method assumes that the function is continuous, but not necessarily smooth.
    
        Implementation based on the following article: M. Dowell and P. Jarratt, *The "Pegasus" method for computing the root of
        an equation*, BIT Numerical Mathematics, volume 12, number 4, pages 503-508, Springer, 1972.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...

class RegulaFalsiSolver(BaseSecantSolver):
    """
    public classRegulaFalsiSolver extends :class:`~org.hipparchus.analysis.solvers.BaseSecantSolver`
    
        Implements the *Regula Falsi* or *False position* method for root-finding (approximating a zero of a univariate real
        function). It is a modified :class:`~org.hipparchus.analysis.solvers.SecantSolver` method.
    
        The *Regula Falsi* method is included for completeness, for testing purposes, for educational purposes, for comparison
        to other algorithms, etc. It is however **not** intended to be used for actual problems, as one of the bounds often
        remains fixed, resulting in very slow convergence. Instead, one of the well-known modified *Regula Falsi* algorithms can
        be used (:class:`~org.hipparchus.analysis.solvers.IllinoisSolver` or
        :class:`~org.hipparchus.analysis.solvers.PegasusSolver`). These two algorithms solve the fundamental issues of the
        original *Regula Falsi* algorithm, and greatly out-performs it for most, if not all, (practical) functions.
    
        Unlike the *Secant* method, the *Regula Falsi* guarantees convergence, by maintaining a bracketed solution. Note
        however, that due to the finite/limited precision of Java's
        :class:`~org.hipparchus.analysis.solvers.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double` type, which is used
        in this implementation, the algorithm may get stuck in a situation where it no longer makes any progress. Such cases are
        detected and result in a :code:`MathIllegalStateException` exception being thrown. In other words, the algorithm
        theoretically guarantees convergence, but the implementation does not.
    
        The *Regula Falsi* method assumes that the function is continuous, but not necessarily smooth.
    
        Implementation based on the following article: M. Dowell and P. Jarratt, *A modified regula falsi method for computing
        the root of an equation*, BIT Numerical Mathematics, volume 11, number 2, pages 168-174, Springer, 1971.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.solvers")``.

    AbstractPolynomialSolver: typing.Type[AbstractPolynomialSolver]
    AbstractUnivariateDifferentiableSolver: typing.Type[AbstractUnivariateDifferentiableSolver]
    AbstractUnivariateSolver: typing.Type[AbstractUnivariateSolver]
    AllowedSolution: typing.Type[AllowedSolution]
    BaseAbstractUnivariateSolver: typing.Type[BaseAbstractUnivariateSolver]
    BaseSecantSolver: typing.Type[BaseSecantSolver]
    BaseUnivariateSolver: typing.Type[BaseUnivariateSolver]
    BisectionSolver: typing.Type[BisectionSolver]
    BracketedRealFieldUnivariateSolver: typing.Type[BracketedRealFieldUnivariateSolver]
    BracketedUnivariateSolver: typing.Type[BracketedUnivariateSolver]
    BracketingNthOrderBrentSolver: typing.Type[BracketingNthOrderBrentSolver]
    BrentSolver: typing.Type[BrentSolver]
    FieldBracketingNthOrderBrentSolver: typing.Type[FieldBracketingNthOrderBrentSolver]
    IllinoisSolver: typing.Type[IllinoisSolver]
    LaguerreSolver: typing.Type[LaguerreSolver]
    MullerSolver: typing.Type[MullerSolver]
    MullerSolver2: typing.Type[MullerSolver2]
    NewtonRaphsonSolver: typing.Type[NewtonRaphsonSolver]
    PegasusSolver: typing.Type[PegasusSolver]
    PolynomialSolver: typing.Type[PolynomialSolver]
    RegulaFalsiSolver: typing.Type[RegulaFalsiSolver]
    RiddersSolver: typing.Type[RiddersSolver]
    SecantSolver: typing.Type[SecantSolver]
    UnivariateDifferentiableSolver: typing.Type[UnivariateDifferentiableSolver]
    UnivariateSolver: typing.Type[UnivariateSolver]
    UnivariateSolverUtils: typing.Type[UnivariateSolverUtils]
