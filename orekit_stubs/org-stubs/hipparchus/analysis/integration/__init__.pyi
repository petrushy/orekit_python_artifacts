
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.integration.gauss
import typing



_FieldUnivariateIntegrator__T = typing.TypeVar('_FieldUnivariateIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateIntegrator(typing.Generic[_FieldUnivariateIntegrator__T]):
    """
    Interface for univariate real integration algorithms.
    
    Since:
        2.0
    """
    def getAbsoluteAccuracy(self) -> float:
        """
        Get the absolute accuracy.
        
        Returns:
            the accuracy
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of function evaluations of the last run of the integrator.
        
        Returns:
            number of function evaluations
        
        
        """
        ...
    def getIterations(self) -> int:
        """
        Get the number of iterations of the last run of the integrator.
        
        Returns:
            number of iterations
        
        
        """
        ...
    def getMaximalIterationCount(self) -> int:
        """
        Get the upper limit for the number of iterations.
        
        Returns:
            the actual upper limit
        
        
        """
        ...
    def getMinimalIterationCount(self) -> int:
        """
        Get the min limit for the number of iterations.
        
        Returns:
            the actual min limit
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
        Get the relative accuracy.
        
        Returns:
            the accuracy
        
        
        """
        ...
    def integrate(self, maxEval: int, f: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldUnivariateIntegrator__T], typing.Callable[[_FieldUnivariateIntegrator__T], _FieldUnivariateIntegrator__T]], min: _FieldUnivariateIntegrator__T, max: _FieldUnivariateIntegrator__T) -> _FieldUnivariateIntegrator__T:
        """
        Integrate the function in the given interval.
        
        Parameters:
            maxEval (int): Maximum number of evaluations.
            f (CalculusFieldUnivariateFunction<FieldUnivariateIntegrator> f): the integrand function
            min (FieldUnivariateIntegrator): the lower bound for the interval
            max (FieldUnivariateIntegrator): the upper bound for the interval
        
        Returns:
            the value of integral
        
        Raises:
            MathIllegalStateException: if the maximum number of function evaluations is exceeded
            MathIllegalStateException: if the maximum iteration count is exceeded or the integrator detects convergence problems otherwise
            MathIllegalArgumentException: if min > max or the endpoints do not satisfy the requirements specified by the integrator
            NullArgumentException: if f is null.
        
        
        """
        ...

class UnivariateIntegrator:
    """
    Interface for univariate real integration algorithms.
    """
    def getAbsoluteAccuracy(self) -> float:
        """
        Get the absolute accuracy.
        
        Returns:
            the accuracy
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of function evaluations of the last run of the integrator.
        
        Returns:
            number of function evaluations
        
        
        """
        ...
    def getIterations(self) -> int:
        """
        Get the number of iterations of the last run of the integrator.
        
        Returns:
            number of iterations
        
        
        """
        ...
    def getMaximalIterationCount(self) -> int:
        """
        Get the upper limit for the number of iterations.
        
        Returns:
            the actual upper limit
        
        
        """
        ...
    def getMinimalIterationCount(self) -> int:
        """
        Get the min limit for the number of iterations.
        
        Returns:
            the actual min limit
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
        Get the relative accuracy.
        
        Returns:
            the accuracy
        
        
        """
        ...
    def integrate(self, maxEval: int, f: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], min: float, max: float) -> float:
        """
        Integrate the function in the given interval.
        
        Parameters:
            maxEval (int): Maximum number of evaluations.
            f (UnivariateFunction): the integrand function
            min (double): the lower bound for the interval
            max (double): the upper bound for the interval
        
        Returns:
            the value of integral
        
        Raises:
            MathIllegalStateException: if the maximum number of function evaluations is exceeded
            MathIllegalStateException: if the maximum iteration count is exceeded or the integrator detects convergence problems otherwise
            MathIllegalArgumentException: if min > max or the endpoints do not satisfy the requirements specified by the integrator
            NullArgumentException: if f is null.
        
        
        """
        ...

_BaseAbstractFieldUnivariateIntegrator__T = typing.TypeVar('_BaseAbstractFieldUnivariateIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class BaseAbstractFieldUnivariateIntegrator(FieldUnivariateIntegrator[_BaseAbstractFieldUnivariateIntegrator__T], typing.Generic[_BaseAbstractFieldUnivariateIntegrator__T]):
    """
    Provide a default implementation for several generic functions.
    
    Since:
        2.0
    """
    DEFAULT_ABSOLUTE_ACCURACY: typing.ClassVar[float] = ...
    """
    Default absolute accuracy.
    
    Also see:
        constant
    
    
    """
    DEFAULT_RELATIVE_ACCURACY: typing.ClassVar[float] = ...
    """
    Default relative accuracy.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MIN_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Default minimal iteration count.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Default maximal iteration count.
    
    Also see:
        constant
    
    
    """
    def getAbsoluteAccuracy(self) -> float:
        """
        Get the absolute accuracy.
        
        Specified by: getAbsoluteAccuracy in interface FieldUnivariateIntegrator
        
        Returns:
            the accuracy
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of function evaluations of the last run of the integrator.
        
        Specified by: getEvaluations in interface FieldUnivariateIntegrator
        
        Returns:
            number of function evaluations
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_BaseAbstractFieldUnivariateIntegrator__T]:
        """
        Get the field to which function argument and value belong.
        
        Returns:
            field to which function argument and value belong
        
        
        """
        ...
    def getIterations(self) -> int:
        """
        Get the number of iterations of the last run of the integrator.
        
        Specified by: getIterations in interface FieldUnivariateIntegrator
        
        Returns:
            number of iterations
        
        
        """
        ...
    def getMaximalIterationCount(self) -> int:
        """
        Get the upper limit for the number of iterations.
        
        Specified by: getMaximalIterationCount in interface FieldUnivariateIntegrator
        
        Returns:
            the actual upper limit
        
        
        """
        ...
    def getMinimalIterationCount(self) -> int:
        """
        Get the min limit for the number of iterations.
        
        Specified by: getMinimalIterationCount in interface FieldUnivariateIntegrator
        
        Returns:
            the actual min limit
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
        Get the relative accuracy.
        
        Specified by: getRelativeAccuracy in interface FieldUnivariateIntegrator
        
        Returns:
            the accuracy
        
        
        """
        ...
    def integrate(self, maxEval: int, f: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_BaseAbstractFieldUnivariateIntegrator__T], typing.Callable[[_BaseAbstractFieldUnivariateIntegrator__T], _BaseAbstractFieldUnivariateIntegrator__T]], lower: _BaseAbstractFieldUnivariateIntegrator__T, upper: _BaseAbstractFieldUnivariateIntegrator__T) -> _BaseAbstractFieldUnivariateIntegrator__T:
        """
        Integrate the function in the given interval.
        
        Specified by: integrate in interface FieldUnivariateIntegrator
        
        Parameters:
            maxEval (int): Maximum number of evaluations.
            f (CalculusFieldUnivariateFunction<BaseAbstractFieldUnivariateIntegrator> f): the integrand function
            lower (BaseAbstractFieldUnivariateIntegrator): the lower bound for the interval
            upper (BaseAbstractFieldUnivariateIntegrator): the upper bound for the interval
        
        Returns:
            the value of integral
        
        Raises:
            MathIllegalArgumentException: if min > max or the endpoints do not satisfy the requirements specified by the integrator
            MathIllegalStateException: if the maximum number of function evaluations is exceeded
            NullArgumentException: if f is null.
        
        
        """
        ...

class BaseAbstractUnivariateIntegrator(UnivariateIntegrator):
    """
    Provide a default implementation for several generic functions.
    """
    DEFAULT_ABSOLUTE_ACCURACY: typing.ClassVar[float] = ...
    """
    Default absolute accuracy.
    
    Also see:
        constant
    
    
    """
    DEFAULT_RELATIVE_ACCURACY: typing.ClassVar[float] = ...
    """
    Default relative accuracy.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MIN_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Default minimal iteration count.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Default maximal iteration count.
    
    Also see:
        constant
    
    
    """
    def getAbsoluteAccuracy(self) -> float:
        """
        Get the absolute accuracy.
        
        Specified by: getAbsoluteAccuracy in interface UnivariateIntegrator
        
        Returns:
            the accuracy
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
        Get the number of function evaluations of the last run of the integrator.
        
        Specified by: getEvaluations in interface UnivariateIntegrator
        
        Returns:
            number of function evaluations
        
        
        """
        ...
    def getIterations(self) -> int:
        """
        Get the number of iterations of the last run of the integrator.
        
        Specified by: getIterations in interface UnivariateIntegrator
        
        Returns:
            number of iterations
        
        
        """
        ...
    def getMaximalIterationCount(self) -> int:
        """
        Get the upper limit for the number of iterations.
        
        Specified by: getMaximalIterationCount in interface UnivariateIntegrator
        
        Returns:
            the actual upper limit
        
        
        """
        ...
    def getMinimalIterationCount(self) -> int:
        """
        Get the min limit for the number of iterations.
        
        Specified by: getMinimalIterationCount in interface UnivariateIntegrator
        
        Returns:
            the actual min limit
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
        Get the relative accuracy.
        
        Specified by: getRelativeAccuracy in interface UnivariateIntegrator
        
        Returns:
            the accuracy
        
        
        """
        ...
    def integrate(self, maxEval: int, f: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], lower: float, upper: float) -> float:
        """
        Integrate the function in the given interval.
        
        Specified by: integrate in interface UnivariateIntegrator
        
        Parameters:
            maxEval (int): Maximum number of evaluations.
            f (UnivariateFunction): the integrand function
            lower (double): the lower bound for the interval
            upper (double): the upper bound for the interval
        
        Returns:
            the value of integral
        
        Raises:
            MathIllegalArgumentException: if min > max or the endpoints do not satisfy the requirements specified by the integrator
            MathIllegalStateException: if the maximum number of function evaluations is exceeded
            NullArgumentException: if f is null.
        
        
        """
        ...

_FieldMidPointIntegrator__T = typing.TypeVar('_FieldMidPointIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldMidPointIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldMidPointIntegrator__T], typing.Generic[_FieldMidPointIntegrator__T]):
    """
    Implements the ` Midpoint Rule <http://en.wikipedia.org/wiki/Midpoint_method>` for integration of real univariate functions. For reference, see Numerical Mathematics, ISBN 0387989595, chapter 9.2.
    
    The function should be integrable.
    
    Since:
        2.0
    """
    MIDPOINT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximum number of iterations for midpoint.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldMidPointIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldMidPointIntegrator__T], relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldMidPointIntegrator__T], minimalIterationCount: int, maximalIterationCount: int): ...

_FieldRombergIntegrator__T = typing.TypeVar('_FieldRombergIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRombergIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldRombergIntegrator__T], typing.Generic[_FieldRombergIntegrator__T]):
    """
    Implements the ` Romberg Algorithm <http://mathworld.wolfram.com/RombergIntegration.html>` for integration of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 3.
    
    Romberg integration employs k successive refinements of the trapezoid rule to remove error terms less than order O(N^(-2k)). Simpson's rule is a special case of k = 2.
    
    Since:
        2.0
    """
    ROMBERG_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximal number of iterations for Romberg.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldRombergIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldRombergIntegrator__T], relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldRombergIntegrator__T], minimalIterationCount: int, maximalIterationCount: int): ...

_FieldSimpsonIntegrator__T = typing.TypeVar('_FieldSimpsonIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSimpsonIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldSimpsonIntegrator__T], typing.Generic[_FieldSimpsonIntegrator__T]):
    """
    Implements ` Simpson's Rule <http://mathworld.wolfram.com/SimpsonsRule.html>` for integration of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 3.
    
    This implementation employs the basic trapezoid rule to calculate Simpson's rule.
    
    Since:
        2.0
    """
    SIMPSON_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximal number of iterations for Simpson.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSimpsonIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSimpsonIntegrator__T], relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSimpsonIntegrator__T], minimalIterationCount: int, maximalIterationCount: int): ...

_FieldTrapezoidIntegrator__T = typing.TypeVar('_FieldTrapezoidIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTrapezoidIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldTrapezoidIntegrator__T], typing.Generic[_FieldTrapezoidIntegrator__T]):
    """
    Implements the ` Trapezoid Rule <http://mathworld.wolfram.com/TrapezoidalRule.html>` for integration of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 3.
    
    The function should be integrable.
    
    Since:
        2.0
    """
    TRAPEZOID_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximum number of iterations for trapezoid.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTrapezoidIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTrapezoidIntegrator__T], relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTrapezoidIntegrator__T], minimalIterationCount: int, maximalIterationCount: int): ...

_IterativeLegendreFieldGaussIntegrator__T = typing.TypeVar('_IterativeLegendreFieldGaussIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class IterativeLegendreFieldGaussIntegrator(BaseAbstractFieldUnivariateIntegrator[_IterativeLegendreFieldGaussIntegrator__T], typing.Generic[_IterativeLegendreFieldGaussIntegrator__T]):
    """
    This algorithm divides the integration interval into equally-sized sub-interval and on each of them performs a ` Legendre-Gauss <http://mathworld.wolfram.com/Legendre-GaussQuadrature.html>` quadrature. Because of its non-adaptive nature, this algorithm can converge to a wrong value for the integral (for example, if the function is significantly different from zero toward the ends of the integration interval). In particular, a change of variables aimed at estimating integrals over infinite intervals as proposed ` here <http://en.wikipedia.org/w/index.php?title=Numerical_integration#Integrals_over_infinite_intervals>` should be avoided when using this class.
    
    Since:
        2.0
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_IterativeLegendreFieldGaussIntegrator__T], int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_IterativeLegendreFieldGaussIntegrator__T], n: int, relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_IterativeLegendreFieldGaussIntegrator__T], int: int, int2: int, int3: int): ...

class IterativeLegendreGaussIntegrator(BaseAbstractUnivariateIntegrator):
    """
    This algorithm divides the integration interval into equally-sized sub-interval and on each of them performs a ` Legendre-Gauss <http://mathworld.wolfram.com/Legendre-GaussQuadrature.html>` quadrature. Because of its non-adaptive nature, this algorithm can converge to a wrong value for the integral (for example, if the function is significantly different from zero toward the ends of the integration interval). In particular, a change of variables aimed at estimating integrals over infinite intervals as proposed ` here <http://en.wikipedia.org/w/index.php?title=Numerical_integration#Integrals_over_infinite_intervals>` should be avoided when using this class.
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, n: int, relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...

class MidPointIntegrator(BaseAbstractUnivariateIntegrator):
    """
    Implements the ` Midpoint Rule <http://en.wikipedia.org/wiki/Midpoint_method>` for integration of real univariate functions. For reference, see Numerical Mathematics, ISBN 0387989595, chapter 9.2.
    
    The function should be integrable.
    """
    MIDPOINT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximum number of iterations for midpoint.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, minimalIterationCount: int, maximalIterationCount: int): ...

class RombergIntegrator(BaseAbstractUnivariateIntegrator):
    """
    Implements the ` Romberg Algorithm <http://mathworld.wolfram.com/RombergIntegration.html>` for integration of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 3.
    
    Romberg integration employs k successive refinements of the trapezoid rule to remove error terms less than order O(N^(-2k)). Simpson's rule is a special case of k = 2.
    """
    ROMBERG_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximal number of iterations for Romberg.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, minimalIterationCount: int, maximalIterationCount: int): ...

class SimpsonIntegrator(BaseAbstractUnivariateIntegrator):
    """
    Implements ` Simpson's Rule <http://mathworld.wolfram.com/SimpsonsRule.html>` for integration of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 3.
    
    This implementation employs the basic trapezoid rule to calculate Simpson's rule.
    """
    SIMPSON_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximal number of iterations for Simpson.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, minimalIterationCount: int, maximalIterationCount: int): ...

class TrapezoidIntegrator(BaseAbstractUnivariateIntegrator):
    """
    Implements the ` Trapezoid Rule <http://mathworld.wolfram.com/TrapezoidalRule.html>` for integration of real univariate functions. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 3.
    
    The function should be integrable.
    """
    TRAPEZOID_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    Maximum number of iterations for trapezoid.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, relativeAccuracy: float, absoluteAccuracy: float, minimalIterationCount: int, maximalIterationCount: int): ...
    @typing.overload
    def __init__(self, minimalIterationCount: int, maximalIterationCount: int): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.integration")``.

    BaseAbstractFieldUnivariateIntegrator: typing.Type[BaseAbstractFieldUnivariateIntegrator]
    BaseAbstractUnivariateIntegrator: typing.Type[BaseAbstractUnivariateIntegrator]
    FieldMidPointIntegrator: typing.Type[FieldMidPointIntegrator]
    FieldRombergIntegrator: typing.Type[FieldRombergIntegrator]
    FieldSimpsonIntegrator: typing.Type[FieldSimpsonIntegrator]
    FieldTrapezoidIntegrator: typing.Type[FieldTrapezoidIntegrator]
    FieldUnivariateIntegrator: typing.Type[FieldUnivariateIntegrator]
    IterativeLegendreFieldGaussIntegrator: typing.Type[IterativeLegendreFieldGaussIntegrator]
    IterativeLegendreGaussIntegrator: typing.Type[IterativeLegendreGaussIntegrator]
    MidPointIntegrator: typing.Type[MidPointIntegrator]
    RombergIntegrator: typing.Type[RombergIntegrator]
    SimpsonIntegrator: typing.Type[SimpsonIntegrator]
    TrapezoidIntegrator: typing.Type[TrapezoidIntegrator]
    UnivariateIntegrator: typing.Type[UnivariateIntegrator]
    gauss: org.hipparchus.analysis.integration.gauss.__module_protocol__
