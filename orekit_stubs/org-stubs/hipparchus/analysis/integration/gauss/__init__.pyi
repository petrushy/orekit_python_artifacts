
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.util
import typing



_FieldGaussIntegrator__T = typing.TypeVar('_FieldGaussIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGaussIntegrator(typing.Generic[_FieldGaussIntegrator__T]):
    """
    public classFieldGaussIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class that implements the Gaussian rule for
        :meth:`~org.hipparchus.analysis.integration.gauss.FieldGaussIntegrator.integrate` a weighted function.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_FieldGaussIntegrator__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldGaussIntegrator__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, pair: org.hipparchus.util.Pair[typing.Union[typing.List[_FieldGaussIntegrator__T], jpype.JArray], typing.Union[typing.List[_FieldGaussIntegrator__T], jpype.JArray]]): ...
    def getNumberOfPoints(self) -> int:
        """
            Get order of the integration rule.
        
            Returns:
                the order of the integration rule (the number of integration points).
        
        
        """
        ...
    def getPoint(self, int: int) -> _FieldGaussIntegrator__T:
        """
            Gets the integration point at the given index. The index must be in the valid range but no check is performed.
        
            Parameters:
                index (int): index of the integration point
        
            Returns:
                the integration point.
        
        
        """
        ...
    def getWeight(self, int: int) -> _FieldGaussIntegrator__T:
        """
            Gets the weight of the integration point at the given index. The index must be in the valid range but no check is
            performed.
        
            Parameters:
                index (int): index of the integration point
        
            Returns:
                the weight.
        
        
        """
        ...
    def integrate(self, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldGaussIntegrator__T], typing.Callable[[_FieldGaussIntegrator__T], _FieldGaussIntegrator__T]]) -> _FieldGaussIntegrator__T: ...

_FieldGaussIntegratorFactory__T = typing.TypeVar('_FieldGaussIntegratorFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGaussIntegratorFactory(typing.Generic[_FieldGaussIntegratorFactory__T]):
    """
    public classFieldGaussIntegratorFactory<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class that provides different ways to compute the nodes and weights to be used by the
        :class:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator`.
    
        Since:
            2.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldGaussIntegratorFactory__T]): ...
    def hermite(self, int: int) -> 'SymmetricFieldGaussIntegrator'[_FieldGaussIntegratorFactory__T]: ...
    def laguerre(self, int: int) -> FieldGaussIntegrator[_FieldGaussIntegratorFactory__T]: ...
    @typing.overload
    def legendre(self, int: int) -> FieldGaussIntegrator[_FieldGaussIntegratorFactory__T]: ...
    @typing.overload
    def legendre(self, int: int, t: _FieldGaussIntegratorFactory__T, t2: _FieldGaussIntegratorFactory__T) -> FieldGaussIntegrator[_FieldGaussIntegratorFactory__T]: ...

_FieldRuleFactory__T = typing.TypeVar('_FieldRuleFactory__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldRuleFactory(typing.Generic[_FieldRuleFactory__T]):
    """
    public interfaceFieldRuleFactory<T extends :class:`~org.hipparchus.FieldElement`<T>>
    
        Interface for rules that determines the integration nodes and their weights.
    
        Since:
            2.0
    """
    def getRule(self, int: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldRuleFactory__T], typing.MutableSequence[_FieldRuleFactory__T]]: ...

class GaussIntegrator:
    """
    public classGaussIntegrator extends :class:`~org.hipparchus.analysis.integration.gauss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class that implements the Gaussian rule for :meth:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator.integrate`
        a weighted function.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, pair: org.hipparchus.util.Pair[typing.Union[typing.List[float], jpype.JArray], typing.Union[typing.List[float], jpype.JArray]]): ...
    def getNumberOfPoints(self) -> int:
        """
            Get the order of the integration rule.
        
            Returns:
                the order of the integration rule (the number of integration points).
        
        
        """
        ...
    def getPoint(self, int: int) -> float:
        """
            Gets the integration point at the given index. The index must be in the valid range but no check is performed.
        
            Parameters:
                index (int): index of the integration point
        
            Returns:
                the integration point.
        
        
        """
        ...
    def getWeight(self, int: int) -> float:
        """
            Gets the weight of the integration point at the given index. The index must be in the valid range but no check is
            performed.
        
            Parameters:
                index (int): index of the integration point
        
            Returns:
                the weight.
        
        
        """
        ...
    def integrate(self, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> float:
        """
            Returns an estimate of the integral of :code:`f(x) * w(x)`, where :code:`w` is a weight function that depends on the
            actual flavor of the Gauss integration scheme. The algorithm uses the points and associated weights, as passed to the
            :meth:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator.%3Cinit%3E`.
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to integrate.
        
            Returns:
                the integral of the weighted function.
        
        
        """
        ...

class GaussIntegratorFactory:
    """
    public classGaussIntegratorFactory extends :class:`~org.hipparchus.analysis.integration.gauss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Class that provides different ways to compute the nodes and weights to be used by the
        :class:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator`.
    """
    DEFAULT_DECIMAL_DIGITS: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_DECIMAL_DIGITS
    
        Number of digits for Legendre high precision.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def hermite(self, int: int) -> 'SymmetricGaussIntegrator':
        """
            Creates a Gauss-Hermite integrator of the given order. The call to the
            :meth:`~org.hipparchus.analysis.integration.gauss.SymmetricGaussIntegrator.integrate` method will perform a weighted
            integration on the interval \([-\infty, +\infty]\): the computed value is the improper integral of \(e^{-x^2}f(x)\)
            where \(f(x)\) is the function passed to the
            :meth:`~org.hipparchus.analysis.integration.gauss.SymmetricGaussIntegrator.integrate` method.
        
            Parameters:
                numberOfPoints (int): Order of the integration rule.
        
            Returns:
                a Gauss-Hermite integrator.
        
        
        """
        ...
    def laguerre(self, int: int) -> GaussIntegrator:
        """
            Creates a Gauss-Laguerre integrator of the given order. The call to the
            :meth:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator.integrate` method will perform an integration on the
            interval \([0, +\infty)\): the computed value is the improper integral of \(e^{-x} f(x)\) where \(f(x)\) is the function
            passed to the :meth:`~org.hipparchus.analysis.integration.gauss.SymmetricGaussIntegrator.integrate` method.
        
            Parameters:
                numberOfPoints (int): Order of the integration rule.
        
            Returns:
                a Gauss-Legendre integrator.
        
        
        """
        ...
    @typing.overload
    def legendre(self, int: int) -> GaussIntegrator:
        """
            Creates a Gauss-Legendre integrator of the given order. The call to the
            :meth:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator.integrate` method will perform an integration on the
            natural interval :code:`[-1 , 1]`.
        
            Parameters:
                numberOfPoints (int): Order of the integration rule.
        
            Returns:
                a Gauss-Legendre integrator.
        
        public :class:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator` legendre(int numberOfPoints, double lowerBound, double upperBound) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Creates a Gauss-Legendre integrator of the given order. The call to the
            :meth:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator.integrate` method will perform an integration on the
            given interval.
        
            Parameters:
                numberOfPoints (int): Order of the integration rule.
                lowerBound (double): Lower bound of the integration interval.
                upperBound (double): Upper bound of the integration interval.
        
            Returns:
                a Gauss-Legendre integrator.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of points is not positive
        
        
        """
        ...
    @typing.overload
    def legendre(self, int: int, double: float, double2: float) -> GaussIntegrator: ...
    @typing.overload
    def legendreHighPrecision(self, int: int) -> GaussIntegrator: ...
    @typing.overload
    def legendreHighPrecision(self, int: int, double: float, double2: float) -> GaussIntegrator: ...

class RuleFactory:
    """
    public interfaceRuleFactory
    
        Interface for rules that determines the integration nodes and their weights.
    
        Since:
            2.0
    """
    def getRule(self, int: int) -> org.hipparchus.util.Pair[typing.MutableSequence[float], typing.MutableSequence[float]]: ...

class AbstractRuleFactory(RuleFactory):
    """
    public abstract classAbstractRuleFactory extends :class:`~org.hipparchus.analysis.integration.gauss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.integration.gauss.RuleFactory`
    
        Base class for rules that determines the integration nodes and their weights. Subclasses must implement the
        :meth:`~org.hipparchus.analysis.integration.gauss.AbstractRuleFactory.computeRule` method.
    
        Since:
            2.0
    """
    def getRule(self, int: int) -> org.hipparchus.util.Pair[typing.MutableSequence[float], typing.MutableSequence[float]]: ...

_FieldAbstractRuleFactory__T = typing.TypeVar('_FieldAbstractRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractRuleFactory(FieldRuleFactory[_FieldAbstractRuleFactory__T], typing.Generic[_FieldAbstractRuleFactory__T]):
    """
    public abstract classFieldAbstractRuleFactory<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.analysis.integration.gauss.FieldRuleFactory`<T>
    
        Base class for rules that determines the integration nodes and their weights. Subclasses must implement the
        :meth:`~org.hipparchus.analysis.integration.gauss.FieldAbstractRuleFactory.computeRule` method.
    
        Since:
            2.0
    """
    def getField(self) -> org.hipparchus.Field[_FieldAbstractRuleFactory__T]: ...
    def getRule(self, int: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldAbstractRuleFactory__T], typing.MutableSequence[_FieldAbstractRuleFactory__T]]: ...

_SymmetricFieldGaussIntegrator__T = typing.TypeVar('_SymmetricFieldGaussIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class SymmetricFieldGaussIntegrator(FieldGaussIntegrator[_SymmetricFieldGaussIntegrator__T], typing.Generic[_SymmetricFieldGaussIntegrator__T]):
    """
    public classSymmetricFieldGaussIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.FieldGaussIntegrator`<T>
    
        This class's implements :meth:`~org.hipparchus.analysis.integration.gauss.SymmetricFieldGaussIntegrator.integrate`
        method assuming that the integral is symmetric about 0. This allows to reduce numerical errors.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray], tArray2: typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, pair: org.hipparchus.util.Pair[typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray], typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray]]): ...
    def integrate(self, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_SymmetricFieldGaussIntegrator__T], typing.Callable[[_SymmetricFieldGaussIntegrator__T], _SymmetricFieldGaussIntegrator__T]]) -> _SymmetricFieldGaussIntegrator__T: ...

class SymmetricGaussIntegrator(GaussIntegrator):
    """
    public classSymmetricGaussIntegrator extends :class:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator`
    
        This class's implements :meth:`~org.hipparchus.analysis.integration.gauss.SymmetricGaussIntegrator.integrate` method
        assuming that the integral is symmetric about 0. This allows to reduce numerical errors.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, pair: org.hipparchus.util.Pair[typing.Union[typing.List[float], jpype.JArray], typing.Union[typing.List[float], jpype.JArray]]): ...
    def integrate(self, univariateFunction: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> float:
        """
            Returns an estimate of the integral of :code:`f(x) * w(x)`, where :code:`w` is a weight function that depends on the
            actual flavor of the Gauss integration scheme. The algorithm uses the points and associated weights, as passed to the
            :meth:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator.%3Cinit%3E`.
        
            Overrides:
                :meth:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator.integrate` in
                class :class:`~org.hipparchus.analysis.integration.gauss.GaussIntegrator`
        
            Parameters:
                f (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to integrate.
        
            Returns:
                the integral of the weighted function.
        
        
        """
        ...

_ConvertingRuleFactory__T = typing.TypeVar('_ConvertingRuleFactory__T', bound=org.hipparchus.FieldElement)  # <T>
class ConvertingRuleFactory(AbstractRuleFactory, typing.Generic[_ConvertingRuleFactory__T]):
    """
    public classConvertingRuleFactory<T extends :class:`~org.hipparchus.FieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.AbstractRuleFactory`
    
        Factory converting :class:`~org.hipparchus.CalculusFieldElement`
        :class:`~org.hipparchus.analysis.integration.gauss.FieldRuleFactory` into
        :class:`~org.hipparchus.analysis.integration.gauss.RuleFactory`.
    
        Since:
            2.0
    """
    def __init__(self, fieldRuleFactory: typing.Union[FieldRuleFactory[_ConvertingRuleFactory__T], typing.Callable[[int], org.hipparchus.util.Pair[typing.MutableSequence[org.hipparchus.FieldElement], typing.MutableSequence[org.hipparchus.FieldElement]]]]): ...

_FieldHermiteRuleFactory__T = typing.TypeVar('_FieldHermiteRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHermiteRuleFactory(FieldAbstractRuleFactory[_FieldHermiteRuleFactory__T], typing.Generic[_FieldHermiteRuleFactory__T]):
    """
    public classFieldHermiteRuleFactory<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.FieldAbstractRuleFactory`<T>
    
        Factory that creates a ` Gauss-type quadrature rule using Hermite polynomials
        <http://en.wikipedia.org/wiki/Gauss-Hermite_quadrature>` of the first kind. Such a quadrature rule allows the
        calculation of improper integrals of a function
    
        \(f(x) e^{-x^2}\)
    
        Recurrence relation and weights computation follow ` Abramowitz and Stegun, 1964
        <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    
        The coefficients of the standard Hermite polynomials grow very rapidly. In order to avoid overflows, each Hermite
        polynomial is normalized with respect to the underlying scalar product.
    
        Since:
            2.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldHermiteRuleFactory__T]): ...

_FieldLaguerreRuleFactory__T = typing.TypeVar('_FieldLaguerreRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLaguerreRuleFactory(FieldAbstractRuleFactory[_FieldLaguerreRuleFactory__T], typing.Generic[_FieldLaguerreRuleFactory__T]):
    """
    public classFieldLaguerreRuleFactory<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.FieldAbstractRuleFactory`<T>
    
        Factory that creates Gauss-type quadrature rule using Laguerre polynomials.
    
        Since:
            2.0
    
        Also see:
    
              - `Gauss-Laguerre quadrature (Wikipedia) <http://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature>`
    """
    def __init__(self, field: org.hipparchus.Field[_FieldLaguerreRuleFactory__T]): ...
    def computeRule(self, int: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldLaguerreRuleFactory__T], typing.MutableSequence[_FieldLaguerreRuleFactory__T]]: ...

_FieldLegendreRuleFactory__T = typing.TypeVar('_FieldLegendreRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLegendreRuleFactory(FieldAbstractRuleFactory[_FieldLegendreRuleFactory__T], typing.Generic[_FieldLegendreRuleFactory__T]):
    """
    public classFieldLegendreRuleFactory<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.integration.gauss.FieldAbstractRuleFactory`<T>
    
        Factory that creates Gauss-type quadrature rule using Legendre polynomials. In this implementation, the lower and upper
        bounds of the natural interval of integration are -1 and 1, respectively. The Legendre polynomials are evaluated using
        the recurrence relation presented in ` Abramowitz and Stegun, 1964
        <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    
        Since:
            2.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldLegendreRuleFactory__T]): ...
    def computeRule(self, int: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldLegendreRuleFactory__T], typing.MutableSequence[_FieldLegendreRuleFactory__T]]: ...

class HermiteRuleFactory(AbstractRuleFactory):
    """
    public classHermiteRuleFactory extends :class:`~org.hipparchus.analysis.integration.gauss.AbstractRuleFactory`
    
        Factory that creates a ` Gauss-type quadrature rule using Hermite polynomials
        <http://en.wikipedia.org/wiki/Gauss-Hermite_quadrature>` of the first kind. Such a quadrature rule allows the
        calculation of improper integrals of a function
    
        \(f(x) e^{-x^2}\)
    
        Recurrence relation and weights computation follow ` Abramowitz and Stegun, 1964
        <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    """
    def __init__(self): ...

class LaguerreRuleFactory(AbstractRuleFactory):
    """
    public classLaguerreRuleFactory extends :class:`~org.hipparchus.analysis.integration.gauss.AbstractRuleFactory`
    
        Factory that creates Gauss-type quadrature rule using Laguerre polynomials.
    
        Also see:
    
              - `Gauss-Laguerre quadrature (Wikipedia) <http://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature>`
    """
    def __init__(self): ...

class LegendreRuleFactory(AbstractRuleFactory):
    """
    public classLegendreRuleFactory extends :class:`~org.hipparchus.analysis.integration.gauss.AbstractRuleFactory`
    
        Factory that creates Gauss-type quadrature rule using Legendre polynomials. In this implementation, the lower and upper
        bounds of the natural interval of integration are -1 and 1, respectively. The Legendre polynomials are evaluated using
        the recurrence relation presented in ` Abramowitz and Stegun, 1964
        <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    """
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.integration.gauss")``.

    AbstractRuleFactory: typing.Type[AbstractRuleFactory]
    ConvertingRuleFactory: typing.Type[ConvertingRuleFactory]
    FieldAbstractRuleFactory: typing.Type[FieldAbstractRuleFactory]
    FieldGaussIntegrator: typing.Type[FieldGaussIntegrator]
    FieldGaussIntegratorFactory: typing.Type[FieldGaussIntegratorFactory]
    FieldHermiteRuleFactory: typing.Type[FieldHermiteRuleFactory]
    FieldLaguerreRuleFactory: typing.Type[FieldLaguerreRuleFactory]
    FieldLegendreRuleFactory: typing.Type[FieldLegendreRuleFactory]
    FieldRuleFactory: typing.Type[FieldRuleFactory]
    GaussIntegrator: typing.Type[GaussIntegrator]
    GaussIntegratorFactory: typing.Type[GaussIntegratorFactory]
    HermiteRuleFactory: typing.Type[HermiteRuleFactory]
    LaguerreRuleFactory: typing.Type[LaguerreRuleFactory]
    LegendreRuleFactory: typing.Type[LegendreRuleFactory]
    RuleFactory: typing.Type[RuleFactory]
    SymmetricFieldGaussIntegrator: typing.Type[SymmetricFieldGaussIntegrator]
    SymmetricGaussIntegrator: typing.Type[SymmetricGaussIntegrator]
