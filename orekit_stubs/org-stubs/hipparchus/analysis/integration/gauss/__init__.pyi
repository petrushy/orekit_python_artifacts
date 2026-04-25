
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
    Class that implements the Gaussian rule for integrate a weighted function.
    
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
    def getPoint(self, index: int) -> _FieldGaussIntegrator__T:
        """
        Gets the integration point at the given index. The index must be in the valid range but no check is performed.
        
        Parameters:
            index (int): index of the integration point
        
        Returns:
            the integration point.
        
        
        """
        ...
    def getWeight(self, index: int) -> _FieldGaussIntegrator__T:
        """
        Gets the weight of the integration point at the given index. The index must be in the valid range but no check is performed.
        
        Parameters:
            index (int): index of the integration point
        
        Returns:
            the weight.
        
        
        """
        ...
    def integrate(self, f: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldGaussIntegrator__T], typing.Callable[[_FieldGaussIntegrator__T], _FieldGaussIntegrator__T]]) -> _FieldGaussIntegrator__T:
        """
        Returns an estimate of the integral of f(x) * w(x), where w is a weight function that depends on the actual flavor of the Gauss integration scheme. The algorithm uses the points and associated weights, as passed to the .
        
        Parameters:
            f (CalculusFieldUnivariateFunction<FieldGaussIntegrator> f): Function to integrate.
        
        Returns:
            the integral of the weighted function.
        
        
        """
        ...

_FieldGaussIntegratorFactory__T = typing.TypeVar('_FieldGaussIntegratorFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGaussIntegratorFactory(typing.Generic[_FieldGaussIntegratorFactory__T]):
    """
    Class that provides different ways to compute the nodes and weights to be used by the GaussIntegrator.
    
    Since:
        2.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldGaussIntegratorFactory__T]):
        """
        Simple constructor.
        
        Parameters:
            field (Field<FieldGaussIntegratorFactory> field): field to which function argument and value belong
        
        
        """
        ...
    def hermite(self, numberOfPoints: int) -> 'SymmetricFieldGaussIntegrator'[_FieldGaussIntegratorFactory__T]:
        """
        Creates a Gauss-Hermite integrator of the given order. The call to the integrate method will perform a weighted integration on the interval \([-\infty, +\infty]\): the computed value is the improper integral of \(e^{-x^2}f(x)\) where \(f(x)\) is the function passed to the integrate method.
        
        Parameters:
            numberOfPoints (int): Order of the integration rule.
        
        Returns:
            a Gauss-Hermite integrator.
        
        
        """
        ...
    def laguerre(self, numberOfPoints: int) -> FieldGaussIntegrator[_FieldGaussIntegratorFactory__T]:
        """
        Creates a Gauss-Laguerre integrator of the given order. The call to the integrate method will perform an integration on the interval \([0, +\infty)\): the computed value is the improper integral of \(e^{-x} f(x)\) where \(f(x)\) is the function passed to the integrate method.
        
        Parameters:
            numberOfPoints (int): Order of the integration rule.
        
        Returns:
            a Gauss-Legendre integrator.
        
        
        """
        ...
    @typing.overload
    def legendre(self, int: int) -> FieldGaussIntegrator[_FieldGaussIntegratorFactory__T]: ...
    @typing.overload
    def legendre(self, int: int, t: _FieldGaussIntegratorFactory__T, t2: _FieldGaussIntegratorFactory__T) -> FieldGaussIntegrator[_FieldGaussIntegratorFactory__T]: ...

_FieldRuleFactory__T = typing.TypeVar('_FieldRuleFactory__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldRuleFactory(typing.Generic[_FieldRuleFactory__T]):
    """
    Interface for rules that determines the integration nodes and their weights.
    
    Since:
        2.0
    """
    def getRule(self, numberOfPoints: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldRuleFactory__T], typing.MutableSequence[_FieldRuleFactory__T]]:
        """
        Gets a copy of the quadrature rule with the given number of integration points. The number of points is arbitrarily limited to 1000. It prevents resources exhaustion. In practice the number of points is often much lower.
        
        Parameters:
            numberOfPoints (int): Number of integration points.
        
        Returns:
            a copy of the integration rule.
        
        Raises:
            MathIllegalArgumentException: if numberOfPoints < 1.
            MathIllegalArgumentException: if numberOfPoints > 1000.
            MathIllegalArgumentException: if the elements of the rule pair do not have the same length.
        
        
        """
        ...

class GaussIntegrator:
    """
    Class that implements the Gaussian rule for integrate a weighted function.
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
    def getPoint(self, index: int) -> float:
        """
        Gets the integration point at the given index. The index must be in the valid range but no check is performed.
        
        Parameters:
            index (int): index of the integration point
        
        Returns:
            the integration point.
        
        
        """
        ...
    def getWeight(self, index: int) -> float:
        """
        Gets the weight of the integration point at the given index. The index must be in the valid range but no check is performed.
        
        Parameters:
            index (int): index of the integration point
        
        Returns:
            the weight.
        
        
        """
        ...
    def integrate(self, f: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> float:
        """
        Returns an estimate of the integral of f(x) * w(x), where w is a weight function that depends on the actual flavor of the Gauss integration scheme. The algorithm uses the points and associated weights, as passed to the .
        
        Parameters:
            f (UnivariateFunction): Function to integrate.
        
        Returns:
            the integral of the weighted function.
        
        
        """
        ...

class GaussIntegratorFactory:
    """
    Class that provides different ways to compute the nodes and weights to be used by the GaussIntegrator.
    """
    DEFAULT_DECIMAL_DIGITS: typing.ClassVar[int] = ...
    """
    Number of digits for Legendre high precision.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def hermite(self, numberOfPoints: int) -> 'SymmetricGaussIntegrator':
        """
        Creates a Gauss-Hermite integrator of the given order. The call to the integrate method will perform a weighted integration on the interval \([-\infty, +\infty]\): the computed value is the improper integral of \(e^{-x^2}f(x)\) where \(f(x)\) is the function passed to the integrate method.
        
        Parameters:
            numberOfPoints (int): Order of the integration rule.
        
        Returns:
            a Gauss-Hermite integrator.
        
        
        """
        ...
    def laguerre(self, numberOfPoints: int) -> GaussIntegrator:
        """
        Creates a Gauss-Laguerre integrator of the given order. The call to the integrate method will perform an integration on the interval \([0, +\infty)\): the computed value is the improper integral of \(e^{-x} f(x)\) where \(f(x)\) is the function passed to the integrate method.
        
        Parameters:
            numberOfPoints (int): Order of the integration rule.
        
        Returns:
            a Gauss-Legendre integrator.
        
        
        """
        ...
    @typing.overload
    def legendre(self, int: int) -> GaussIntegrator:
        """
        Creates a Gauss-Legendre integrator of the given order. The call to the integrate method will perform an integration on the natural interval [-1 , 1].
        
        Parameters:
            numberOfPoints (int): Order of the integration rule.
        
        Returns:
            a Gauss-Legendre integrator.
        
        public GaussIntegrator legendre(int numberOfPoints, double lowerBound, double upperBound) throws MathIllegalArgumentException
        
        Creates a Gauss-Legendre integrator of the given order. The call to the integrate method will perform an integration on the given interval.
        
        Parameters:
            numberOfPoints (int): Order of the integration rule.
            lowerBound (double): Lower bound of the integration interval.
            upperBound (double): Upper bound of the integration interval.
        
        Returns:
            a Gauss-Legendre integrator.
        
        Raises:
            MathIllegalArgumentException: if number of points is not positive
        
        
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
    Interface for rules that determines the integration nodes and their weights.
    
    Since:
        2.0
    """
    def getRule(self, numberOfPoints: int) -> org.hipparchus.util.Pair[typing.MutableSequence[float], typing.MutableSequence[float]]:
        """
        Gets a copy of the quadrature rule with the given number of integration points. The number of points is arbitrarily limited to 1000. It prevents resources exhaustion. In practice the number of points is often much lower.
        
        Parameters:
            numberOfPoints (int): Number of integration points.
        
        Returns:
            a copy of the integration rule.
        
        Raises:
            MathIllegalArgumentException: if numberOfPoints < 1.
            MathIllegalArgumentException: if numberOfPoints > 1000.
            MathIllegalArgumentException: if the elements of the rule pair do not have the same length.
        
        
        """
        ...

class AbstractRuleFactory(RuleFactory):
    """
    implements RuleFactory
    
    Base class for rules that determines the integration nodes and their weights. Subclasses must implement the computeRule method.
    
    Since:
        2.0
    """
    def getRule(self, numberOfPoints: int) -> org.hipparchus.util.Pair[typing.MutableSequence[float], typing.MutableSequence[float]]:
        """
        Gets a copy of the quadrature rule with the given number of integration points. The number of points is arbitrarily limited to 1000. It prevents resources exhaustion. In practice the number of points is often much lower.
        
        Specified by: getRule in interface RuleFactory
        
        Parameters:
            numberOfPoints (int): Number of integration points.
        
        Returns:
            a copy of the integration rule.
        
        Raises:
            MathIllegalArgumentException: if numberOfPoints < 1.
            MathIllegalArgumentException: if numberOfPoints > 1000.
            MathIllegalArgumentException: if the elements of the rule pair do not have the same length.
        
        
        """
        ...

_FieldAbstractRuleFactory__T = typing.TypeVar('_FieldAbstractRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractRuleFactory(FieldRuleFactory[_FieldAbstractRuleFactory__T], typing.Generic[_FieldAbstractRuleFactory__T]):
    """
    implements FieldRuleFactory<T>
    
    Base class for rules that determines the integration nodes and their weights. Subclasses must implement the computeRule method.
    
    Since:
        2.0
    """
    def getField(self) -> org.hipparchus.Field[_FieldAbstractRuleFactory__T]:
        """
        Get the field to which rule coefficients belong.
        
        Returns:
            field to which rule coefficients belong
        
        
        """
        ...
    def getRule(self, numberOfPoints: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldAbstractRuleFactory__T], typing.MutableSequence[_FieldAbstractRuleFactory__T]]:
        """
        Gets a copy of the quadrature rule with the given number of integration points. The number of points is arbitrarily limited to 1000. It prevents resources exhaustion. In practice the number of points is often much lower.
        
        Specified by: getRule in interface FieldRuleFactory
        
        Parameters:
            numberOfPoints (int): Number of integration points.
        
        Returns:
            a copy of the integration rule.
        
        Raises:
            MathIllegalArgumentException: if numberOfPoints < 1.
            MathIllegalArgumentException: if numberOfPoints > 1000.
            MathIllegalArgumentException: if the elements of the rule pair do not have the same length.
        
        
        """
        ...

_SymmetricFieldGaussIntegrator__T = typing.TypeVar('_SymmetricFieldGaussIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class SymmetricFieldGaussIntegrator(FieldGaussIntegrator[_SymmetricFieldGaussIntegrator__T], typing.Generic[_SymmetricFieldGaussIntegrator__T]):
    """
    This class's implements integrate method assuming that the integral is symmetric about 0. This allows to reduce numerical errors.
    
    Since:
        2.0
    """
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray], tArray2: typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, pair: org.hipparchus.util.Pair[typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray], typing.Union[typing.List[_SymmetricFieldGaussIntegrator__T], jpype.JArray]]): ...
    def integrate(self, f: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[_SymmetricFieldGaussIntegrator__T], typing.Callable[[_SymmetricFieldGaussIntegrator__T], _SymmetricFieldGaussIntegrator__T]]) -> _SymmetricFieldGaussIntegrator__T:
        """
        Returns an estimate of the integral of f(x) * w(x), where w is a weight function that depends on the actual flavor of the Gauss integration scheme. The algorithm uses the points and associated weights, as passed to the .
        
        Overrides: integrate in class FieldGaussIntegrator
        
        Parameters:
            f (CalculusFieldUnivariateFunction<SymmetricFieldGaussIntegrator> f): Function to integrate.
        
        Returns:
            the integral of the weighted function.
        
        
        """
        ...

class SymmetricGaussIntegrator(GaussIntegrator):
    """
    This class's implements integrate method assuming that the integral is symmetric about 0. This allows to reduce numerical errors.
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, pair: org.hipparchus.util.Pair[typing.Union[typing.List[float], jpype.JArray], typing.Union[typing.List[float], jpype.JArray]]): ...
    def integrate(self, f: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> float:
        """
        Returns an estimate of the integral of f(x) * w(x), where w is a weight function that depends on the actual flavor of the Gauss integration scheme. The algorithm uses the points and associated weights, as passed to the .
        
        Overrides: integrate in class GaussIntegrator
        
        Parameters:
            f (UnivariateFunction): Function to integrate.
        
        Returns:
            the integral of the weighted function.
        
        
        """
        ...

_ConvertingRuleFactory__T = typing.TypeVar('_ConvertingRuleFactory__T', bound=org.hipparchus.FieldElement)  # <T>
class ConvertingRuleFactory(AbstractRuleFactory, typing.Generic[_ConvertingRuleFactory__T]):
    """
    Factory converting CalculusFieldElement FieldRuleFactory into RuleFactory.
    
    Since:
        2.0
    """
    def __init__(self, fieldFactory: typing.Union[FieldRuleFactory[_ConvertingRuleFactory__T], typing.Callable[[int], org.hipparchus.util.Pair[typing.MutableSequence[org.hipparchus.FieldElement], typing.MutableSequence[org.hipparchus.FieldElement]]]]):
        """
        Simple constructor.
        
        Parameters:
            fieldFactory (FieldRuleFactory<ConvertingRuleFactory> fieldFactory): field-based factory to convert
        
        
        """
        ...

_FieldHermiteRuleFactory__T = typing.TypeVar('_FieldHermiteRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHermiteRuleFactory(FieldAbstractRuleFactory[_FieldHermiteRuleFactory__T], typing.Generic[_FieldHermiteRuleFactory__T]):
    """
    Factory that creates a ` Gauss-type quadrature rule using Hermite polynomials <http://en.wikipedia.org/wiki/Gauss-Hermite_quadrature>` of the first kind. Such a quadrature rule allows the calculation of improper integrals of a function
    
    \(f(x) e^{-x^2}\)
    
    Recurrence relation and weights computation follow ` Abramowitz and Stegun, 1964 <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    
    The coefficients of the standard Hermite polynomials grow very rapidly. In order to avoid overflows, each Hermite polynomial is normalized with respect to the underlying scalar product.
    
    Since:
        2.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldHermiteRuleFactory__T]):
        """
        Simple constructor
        
        Parameters:
            field (Field<FieldHermiteRuleFactory> field): field to which rule coefficients belong
        
        
        """
        ...

_FieldLaguerreRuleFactory__T = typing.TypeVar('_FieldLaguerreRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLaguerreRuleFactory(FieldAbstractRuleFactory[_FieldLaguerreRuleFactory__T], typing.Generic[_FieldLaguerreRuleFactory__T]):
    """
    Factory that creates Gauss-type quadrature rule using Laguerre polynomials.
    
    Since:
        2.0
    
          - `Gauss-Laguerre quadrature (Wikipedia) <http://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature>`
    """
    def __init__(self, field: org.hipparchus.Field[_FieldLaguerreRuleFactory__T]):
        """
        Simple constructor
        
        Parameters:
            field (Field<FieldLaguerreRuleFactory> field): field to which rule coefficients belong
        
        
        """
        ...
    def computeRule(self, numberOfPoints: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldLaguerreRuleFactory__T], typing.MutableSequence[_FieldLaguerreRuleFactory__T]]:
        """
        Computes the rule for the given order.
        
        Specified by: computeRule in class FieldAbstractRuleFactory
        
        Parameters:
            numberOfPoints (int): Order of the rule to be computed.
        
        Returns:
            the computed rule.
        
        Raises:
            MathIllegalArgumentException: if the elements of the pair do not have the same length.
        
        
        """
        ...

_FieldLegendreRuleFactory__T = typing.TypeVar('_FieldLegendreRuleFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLegendreRuleFactory(FieldAbstractRuleFactory[_FieldLegendreRuleFactory__T], typing.Generic[_FieldLegendreRuleFactory__T]):
    """
    Factory that creates Gauss-type quadrature rule using Legendre polynomials. In this implementation, the lower and upper bounds of the natural interval of integration are -1 and 1, respectively. The Legendre polynomials are evaluated using the recurrence relation presented in ` Abramowitz and Stegun, 1964 <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    
    Since:
        2.0
    """
    def __init__(self, field: org.hipparchus.Field[_FieldLegendreRuleFactory__T]):
        """
        Simple constructor
        
        Parameters:
            field (Field<FieldLegendreRuleFactory> field): field to which rule coefficients belong
        
        
        """
        ...
    def computeRule(self, numberOfPoints: int) -> org.hipparchus.util.Pair[typing.MutableSequence[_FieldLegendreRuleFactory__T], typing.MutableSequence[_FieldLegendreRuleFactory__T]]:
        """
        Computes the rule for the given order.
        
        Specified by: computeRule in class FieldAbstractRuleFactory
        
        Parameters:
            numberOfPoints (int): Order of the rule to be computed.
        
        Returns:
            the computed rule.
        
        Raises:
            MathIllegalArgumentException: if the elements of the pair do not have the same length.
        
        
        """
        ...

class HermiteRuleFactory(AbstractRuleFactory):
    """
    Factory that creates a ` Gauss-type quadrature rule using Hermite polynomials <http://en.wikipedia.org/wiki/Gauss-Hermite_quadrature>` of the first kind. Such a quadrature rule allows the calculation of improper integrals of a function
    
    \(f(x) e^{-x^2}\)
    
    Recurrence relation and weights computation follow ` Abramowitz and Stegun, 1964 <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...

class LaguerreRuleFactory(AbstractRuleFactory):
    """
    Factory that creates Gauss-type quadrature rule using Laguerre polynomials.
    
          - `Gauss-Laguerre quadrature (Wikipedia) <http://en.wikipedia.org/wiki/Gauss%E2%80%93Laguerre_quadrature>`
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...

class LegendreRuleFactory(AbstractRuleFactory):
    """
    Factory that creates Gauss-type quadrature rule using Legendre polynomials. In this implementation, the lower and upper bounds of the natural interval of integration are -1 and 1, respectively. The Legendre polynomials are evaluated using the recurrence relation presented in ` Abramowitz and Stegun, 1964 <http://en.wikipedia.org/wiki/Abramowitz_and_Stegun>`.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...


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
