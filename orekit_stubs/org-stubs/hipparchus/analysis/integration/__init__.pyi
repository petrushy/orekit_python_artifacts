
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
    public interfaceFieldUnivariateIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>>
    
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
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldUnivariateIntegrator__T], typing.Callable[[_FieldUnivariateIntegrator__T], _FieldUnivariateIntegrator__T]], t: _FieldUnivariateIntegrator__T, t2: _FieldUnivariateIntegrator__T) -> _FieldUnivariateIntegrator__T: ...

class UnivariateIntegrator:
    """
    public interfaceUnivariateIntegrator
    
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
    def integrate(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float) -> float: ...

_BaseAbstractFieldUnivariateIntegrator__T = typing.TypeVar('_BaseAbstractFieldUnivariateIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class BaseAbstractFieldUnivariateIntegrator(FieldUnivariateIntegrator[_BaseAbstractFieldUnivariateIntegrator__T], typing.Generic[_BaseAbstractFieldUnivariateIntegrator__T]):
    """
    public abstract classBaseAbstractFieldUnivariateIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator`<T>
    
        Provide a default implementation for several generic functions.
    
        Since:
            2.0
    """
    DEFAULT_ABSOLUTE_ACCURACY: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ABSOLUTE_ACCURACY
    
        Default absolute accuracy.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_RELATIVE_ACCURACY: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_RELATIVE_ACCURACY
    
        Default relative accuracy.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_MIN_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MIN_ITERATIONS_COUNT
    
        Default minimal iteration count.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITERATIONS_COUNT
    
        Default maximal iteration count.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    def getAbsoluteAccuracy(self) -> float:
        """
            Get the absolute accuracy.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator.getAbsoluteAccuracy` in
                interface :class:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator`
        
            Returns:
                the accuracy
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of function evaluations of the last run of the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator.getEvaluations` in
                interface :class:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator`
        
            Returns:
                number of function evaluations
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_BaseAbstractFieldUnivariateIntegrator__T]: ...
    def getIterations(self) -> int:
        """
            Get the number of iterations of the last run of the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator.getIterations` in
                interface :class:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator`
        
            Returns:
                number of iterations
        
        
        """
        ...
    def getMaximalIterationCount(self) -> int:
        """
            Get the upper limit for the number of iterations.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator.getMaximalIterationCount` in
                interface :class:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator`
        
            Returns:
                the actual upper limit
        
        
        """
        ...
    def getMinimalIterationCount(self) -> int:
        """
            Get the min limit for the number of iterations.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator.getMinimalIterationCount` in
                interface :class:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator`
        
            Returns:
                the actual min limit
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
            Get the relative accuracy.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator.getRelativeAccuracy` in
                interface :class:`~org.hipparchus.analysis.integration.FieldUnivariateIntegrator`
        
            Returns:
                the accuracy
        
        
        """
        ...
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_BaseAbstractFieldUnivariateIntegrator__T], typing.Callable[[_BaseAbstractFieldUnivariateIntegrator__T], _BaseAbstractFieldUnivariateIntegrator__T]], t: _BaseAbstractFieldUnivariateIntegrator__T, t2: _BaseAbstractFieldUnivariateIntegrator__T) -> _BaseAbstractFieldUnivariateIntegrator__T: ...

class BaseAbstractUnivariateIntegrator(UnivariateIntegrator):
    """
    public abstract classBaseAbstractUnivariateIntegrator extends :class:`~org.hipparchus.analysis.integration.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.integration.UnivariateIntegrator`
    
        Provide a default implementation for several generic functions.
    """
    DEFAULT_ABSOLUTE_ACCURACY: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ABSOLUTE_ACCURACY
    
        Default absolute accuracy.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_RELATIVE_ACCURACY: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_RELATIVE_ACCURACY
    
        Default relative accuracy.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_MIN_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MIN_ITERATIONS_COUNT
    
        Default minimal iteration count.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_MAX_ITERATIONS_COUNT
    
        Default maximal iteration count.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    def getAbsoluteAccuracy(self) -> float:
        """
            Get the absolute accuracy.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.UnivariateIntegrator.getAbsoluteAccuracy` in
                interface :class:`~org.hipparchus.analysis.integration.UnivariateIntegrator`
        
            Returns:
                the accuracy
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of function evaluations of the last run of the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.UnivariateIntegrator.getEvaluations` in
                interface :class:`~org.hipparchus.analysis.integration.UnivariateIntegrator`
        
            Returns:
                number of function evaluations
        
        
        """
        ...
    def getIterations(self) -> int:
        """
            Get the number of iterations of the last run of the integrator.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.UnivariateIntegrator.getIterations` in
                interface :class:`~org.hipparchus.analysis.integration.UnivariateIntegrator`
        
            Returns:
                number of iterations
        
        
        """
        ...
    def getMaximalIterationCount(self) -> int:
        """
            Get the upper limit for the number of iterations.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.UnivariateIntegrator.getMaximalIterationCount` in
                interface :class:`~org.hipparchus.analysis.integration.UnivariateIntegrator`
        
            Returns:
                the actual upper limit
        
        
        """
        ...
    def getMinimalIterationCount(self) -> int:
        """
            Get the min limit for the number of iterations.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.UnivariateIntegrator.getMinimalIterationCount` in
                interface :class:`~org.hipparchus.analysis.integration.UnivariateIntegrator`
        
            Returns:
                the actual min limit
        
        
        """
        ...
    def getRelativeAccuracy(self) -> float:
        """
            Get the relative accuracy.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.integration.UnivariateIntegrator.getRelativeAccuracy` in
                interface :class:`~org.hipparchus.analysis.integration.UnivariateIntegrator`
        
            Returns:
                the accuracy
        
        
        """
        ...
    def integrate(self, int: int, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable], double: float, double2: float) -> float: ...

_FieldMidPointIntegrator__T = typing.TypeVar('_FieldMidPointIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldMidPointIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldMidPointIntegrator__T], typing.Generic[_FieldMidPointIntegrator__T]):
    """
    public classFieldMidPointIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.BaseAbstractFieldUnivariateIntegrator`<T>
    
        Implements the ` Midpoint Rule <http://en.wikipedia.org/wiki/Midpoint_method>` for integration of real univariate
        functions. For reference, see **Numerical Mathematics**, ISBN 0387989595, chapter 9.2.
    
        The function should be integrable.
    
        Since:
            2.0
    """
    MIDPOINT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int MIDPOINT_MAX_ITERATIONS_COUNT
    
        Maximum number of iterations for midpoint.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldMidPointIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldMidPointIntegrator__T], double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldMidPointIntegrator__T], int: int, int2: int): ...

_FieldRombergIntegrator__T = typing.TypeVar('_FieldRombergIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldRombergIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldRombergIntegrator__T], typing.Generic[_FieldRombergIntegrator__T]):
    """
    public classFieldRombergIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.BaseAbstractFieldUnivariateIntegrator`<T>
    
        Implements the ` Romberg Algorithm <http://mathworld.wolfram.com/RombergIntegration.html>` for integration of real
        univariate functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 3.
    
        Romberg integration employs k successive refinements of the trapezoid rule to remove error terms less than order
        O(N^(-2k)). Simpson's rule is a special case of k = 2.
    
        Since:
            2.0
    """
    ROMBERG_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int ROMBERG_MAX_ITERATIONS_COUNT
    
        Maximal number of iterations for Romberg.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldRombergIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldRombergIntegrator__T], double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldRombergIntegrator__T], int: int, int2: int): ...

_FieldSimpsonIntegrator__T = typing.TypeVar('_FieldSimpsonIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSimpsonIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldSimpsonIntegrator__T], typing.Generic[_FieldSimpsonIntegrator__T]):
    """
    public classFieldSimpsonIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.BaseAbstractFieldUnivariateIntegrator`<T>
    
        Implements ` Simpson's Rule <http://mathworld.wolfram.com/SimpsonsRule.html>` for integration of real univariate
        functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 3.
    
        This implementation employs the basic trapezoid rule to calculate Simpson's rule.
    
        Since:
            2.0
    """
    SIMPSON_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int SIMPSON_MAX_ITERATIONS_COUNT
    
        Maximal number of iterations for Simpson.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSimpsonIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSimpsonIntegrator__T], double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSimpsonIntegrator__T], int: int, int2: int): ...

_FieldTrapezoidIntegrator__T = typing.TypeVar('_FieldTrapezoidIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTrapezoidIntegrator(BaseAbstractFieldUnivariateIntegrator[_FieldTrapezoidIntegrator__T], typing.Generic[_FieldTrapezoidIntegrator__T]):
    """
    public classFieldTrapezoidIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.BaseAbstractFieldUnivariateIntegrator`<T>
    
        Implements the ` Trapezoid Rule <http://mathworld.wolfram.com/TrapezoidalRule.html>` for integration of real univariate
        functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 3.
    
        The function should be integrable.
    
        Since:
            2.0
    """
    TRAPEZOID_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int TRAPEZOID_MAX_ITERATIONS_COUNT
    
        Maximum number of iterations for trapezoid.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTrapezoidIntegrator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTrapezoidIntegrator__T], double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTrapezoidIntegrator__T], int: int, int2: int): ...

_IterativeLegendreFieldGaussIntegrator__T = typing.TypeVar('_IterativeLegendreFieldGaussIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class IterativeLegendreFieldGaussIntegrator(BaseAbstractFieldUnivariateIntegrator[_IterativeLegendreFieldGaussIntegrator__T], typing.Generic[_IterativeLegendreFieldGaussIntegrator__T]):
    """
    public classIterativeLegendreFieldGaussIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.BaseAbstractFieldUnivariateIntegrator`<T>
    
        This algorithm divides the integration interval into equally-sized sub-interval and on each of them performs a `
        Legendre-Gauss <http://mathworld.wolfram.com/Legendre-GaussQuadrature.html>` quadrature. Because of its *non-adaptive*
        nature, this algorithm can converge to a wrong value for the integral (for example, if the function is significantly
        different from zero toward the ends of the integration interval). In particular, a change of variables aimed at
        estimating integrals over infinite intervals as proposed ` here
        <http://en.wikipedia.org/w/index.php?title=Numerical_integration#Integrals_over_infinite_intervals>` should be avoided
        when using this class.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_IterativeLegendreFieldGaussIntegrator__T], int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_IterativeLegendreFieldGaussIntegrator__T], int: int, double: float, double2: float, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_IterativeLegendreFieldGaussIntegrator__T], int: int, int2: int, int3: int): ...

class IterativeLegendreGaussIntegrator(BaseAbstractUnivariateIntegrator):
    """
    public classIterativeLegendreGaussIntegrator extends :class:`~org.hipparchus.analysis.integration.BaseAbstractUnivariateIntegrator`
    
        This algorithm divides the integration interval into equally-sized sub-interval and on each of them performs a `
        Legendre-Gauss <http://mathworld.wolfram.com/Legendre-GaussQuadrature.html>` quadrature. Because of its *non-adaptive*
        nature, this algorithm can converge to a wrong value for the integral (for example, if the function is significantly
        different from zero toward the ends of the integration interval). In particular, a change of variables aimed at
        estimating integrals over infinite intervals as proposed ` here
        <http://en.wikipedia.org/w/index.php?title=Numerical_integration#Integrals_over_infinite_intervals>` should be avoided
        when using this class.
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...

class MidPointIntegrator(BaseAbstractUnivariateIntegrator):
    """
    public classMidPointIntegrator extends :class:`~org.hipparchus.analysis.integration.BaseAbstractUnivariateIntegrator`
    
        Implements the ` Midpoint Rule <http://en.wikipedia.org/wiki/Midpoint_method>` for integration of real univariate
        functions. For reference, see **Numerical Mathematics**, ISBN 0387989595, chapter 9.2.
    
        The function should be integrable.
    """
    MIDPOINT_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int MIDPOINT_MAX_ITERATIONS_COUNT
    
        Maximum number of iterations for midpoint.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...

class RombergIntegrator(BaseAbstractUnivariateIntegrator):
    """
    public classRombergIntegrator extends :class:`~org.hipparchus.analysis.integration.BaseAbstractUnivariateIntegrator`
    
        Implements the ` Romberg Algorithm <http://mathworld.wolfram.com/RombergIntegration.html>` for integration of real
        univariate functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 3.
    
        Romberg integration employs k successive refinements of the trapezoid rule to remove error terms less than order
        O(N^(-2k)). Simpson's rule is a special case of k = 2.
    """
    ROMBERG_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int ROMBERG_MAX_ITERATIONS_COUNT
    
        Maximal number of iterations for Romberg.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...

class SimpsonIntegrator(BaseAbstractUnivariateIntegrator):
    """
    public classSimpsonIntegrator extends :class:`~org.hipparchus.analysis.integration.BaseAbstractUnivariateIntegrator`
    
        Implements ` Simpson's Rule <http://mathworld.wolfram.com/SimpsonsRule.html>` for integration of real univariate
        functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 3.
    
        This implementation employs the basic trapezoid rule to calculate Simpson's rule.
    """
    SIMPSON_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int SIMPSON_MAX_ITERATIONS_COUNT
    
        Maximal number of iterations for Simpson.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...

class TrapezoidIntegrator(BaseAbstractUnivariateIntegrator):
    """
    public classTrapezoidIntegrator extends :class:`~org.hipparchus.analysis.integration.BaseAbstractUnivariateIntegrator`
    
        Implements the ` Trapezoid Rule <http://mathworld.wolfram.com/TrapezoidalRule.html>` for integration of real univariate
        functions. For reference, see **Introduction to Numerical Analysis**, ISBN 038795452X, chapter 3.
    
        The function should be integrable.
    """
    TRAPEZOID_MAX_ITERATIONS_COUNT: typing.ClassVar[int] = ...
    """
    public static final int TRAPEZOID_MAX_ITERATIONS_COUNT
    
        Maximum number of iterations for trapezoid.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...


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
