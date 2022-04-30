import java.io
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.differentiation
import typing



_FieldPolynomialFunction__T = typing.TypeVar('_FieldPolynomialFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPolynomialFunction(org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldPolynomialFunction__T], typing.Generic[_FieldPolynomialFunction__T]):
    """
    public class FieldPolynomialFunction<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction`<T>
    
        Immutable representation of a real polynomial function with real coefficients.
    
        `Horner's Method <http://mathworld.wolfram.com/HornersMethod.html>` is used to evaluate the function.
    
        Since:
            1.5
    """
    def __init__(self, tArray: typing.List[_FieldPolynomialFunction__T]): ...
    def add(self, fieldPolynomialFunction: 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]: ...
    def antiDerivative(self) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]: ...
    def degree(self) -> int:
        """
            Returns the degree of the polynomial.
        
            Returns:
                the degree of the polynomial.
        
        
        """
        ...
    def getCoefficients(self) -> typing.List[_FieldPolynomialFunction__T]:
        """
            Returns a copy of the coefficients array.
        
            Changes made to the returned copy will not affect the coefficients of the polynomial.
        
            Returns:
                a fresh copy of the coefficients array.
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldPolynomialFunction__T]: ...
    @typing.overload
    def integrate(self, double: float, double2: float) -> _FieldPolynomialFunction__T:
        """
            Returns the definite integral of this polymomial over the given interval.
        
            [lower, upper] must describe a finite interval (neither can be infinite and lower must be less than or equal to upper).
        
            Parameters:
                lower (double): lower bound for the integration
                upper (double): upper bound for the integration
        
            Returns:
                the integral of this polymomial over the given interval
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the bounds do not describe a finite interval
        
            Returns the definite integral of this polymomial over the given interval.
        
            [lower, upper] must describe a finite interval (neither can be infinite and lower must be less than or equal to upper).
        
            Parameters:
                lower (:class:`~org.hipparchus.analysis.polynomials.FieldPolynomialFunction`): lower bound for the integration
                upper (:class:`~org.hipparchus.analysis.polynomials.FieldPolynomialFunction`): upper bound for the integration
        
            Returns:
                the integral of this polymomial over the given interval
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the bounds do not describe a finite interval
        
        
        """
        ...
    @typing.overload
    def integrate(self, t: _FieldPolynomialFunction__T, t2: _FieldPolynomialFunction__T) -> _FieldPolynomialFunction__T: ...
    def multiply(self, fieldPolynomialFunction: 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]: ...
    def negate(self) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]: ...
    def polynomialDerivative(self) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]: ...
    def subtract(self, fieldPolynomialFunction: 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]: ...
    @typing.overload
    def value(self, double: float) -> _FieldPolynomialFunction__T:
        """
            Compute the value of the function for the given argument.
        
            The value returned is
        
            :code:`coefficients[n] * x^n + ... + coefficients[1] * x + coefficients[0]`
        
            Parameters:
                x (double): Argument for which the function value should be computed.
        
            Returns:
                the value of the polynomial at the given point.
        
            Also see:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`
        
            Compute the value of the function for the given argument.
        
            The value returned is
        
            :code:`coefficients[n] * x^n + ... + coefficients[1] * x + coefficients[0]`
        
            Specified by:
                :meth:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction`
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.polynomials.FieldPolynomialFunction`): Argument for which the function value should be computed.
        
            Returns:
                the value of the polynomial at the given point.
        
            Also see:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`
        
        
        """
        ...
    @typing.overload
    def value(self, t: _FieldPolynomialFunction__T) -> _FieldPolynomialFunction__T: ...

_FieldPolynomialSplineFunction__T = typing.TypeVar('_FieldPolynomialSplineFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPolynomialSplineFunction(org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldPolynomialSplineFunction__T], typing.Generic[_FieldPolynomialSplineFunction__T]):
    """
    public class FieldPolynomialSplineFunction<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction`<T>
    
        Represents a polynomial spline function.
    
        A **polynomial spline function** consists of a set of *interpolating polynomials* and an ascending array of domain *knot
        points*, determining the intervals over which the spline function is defined by the constituent polynomials. The
        polynomials are assumed to have been computed to match the values of another function at the knot points. The value
        consistency constraints are not currently enforced by :code:`PolynomialSplineFunction` itself, but are assumed to hold
        among the polynomials and knot points passed to the constructor.
    
        N.B.: The polynomials in the :code:`polynomials` property must be centered on the knot points to compute the spline
        function values. See below.
    
        The domain of the polynomial spline function is :code:`[smallest knot, largest knot]`. Attempts to evaluate the function
        at values outside of this range generate IllegalArgumentExceptions.
    
        The value of the polynomial spline function for an argument :code:`x` is computed as follows:
    
          1.  The knot array is searched to find the segment to which :code:`x` belongs. If :code:`x` is less than the smallest knot
            point or greater than the largest one, an :code:`IllegalArgumentException` is thrown.
          2.  Let :code:`j` be the index of the largest knot point that is less than or equal to :code:`x`. The value returned is
            :code:`polynomials[j](x - knot[j])`
    
    
        Since:
            1.5
    """
    def __init__(self, tArray: typing.List[_FieldPolynomialSplineFunction__T], fieldPolynomialFunctionArray: typing.List[FieldPolynomialFunction[_FieldPolynomialSplineFunction__T]]): ...
    def getField(self) -> org.hipparchus.Field[_FieldPolynomialSplineFunction__T]: ...
    def getKnots(self) -> typing.List[_FieldPolynomialSplineFunction__T]:
        """
            Get an array copy of the knot points. It returns a fresh copy of the array. Changes made to the copy will not affect the
            knots property.
        
            Returns:
                the knot points.
        
        
        """
        ...
    def getN(self) -> int:
        """
            Get the number of spline segments. It is also the number of polynomials and the number of knot points - 1.
        
            Returns:
                the number of spline segments.
        
        
        """
        ...
    def getPolynomials(self) -> typing.List[FieldPolynomialFunction[_FieldPolynomialSplineFunction__T]]: ...
    def isValidPoint(self, t: _FieldPolynomialSplineFunction__T) -> bool:
        """
            Indicates whether a point is within the interpolation range.
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction`): Point.
        
            Returns:
                :code:`true` if :code:`x` is a valid point.
        
        
        """
        ...
    def polynomialSplineDerivative(self) -> 'FieldPolynomialSplineFunction'[_FieldPolynomialSplineFunction__T]: ...
    @typing.overload
    def value(self, double: float) -> _FieldPolynomialSplineFunction__T:
        """
            Compute the value for the function. See :class:`~org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction` for
            details on the algorithm for computing the value of the function.
        
            Parameters:
                v (double): Point for which the function value should be computed.
        
            Returns:
                the value.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`v` is outside of the domain of the spline function (smaller than the smallest knot point or larger than the
                    largest knot point).
        
            Compute the value for the function. See :class:`~org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction` for
            details on the algorithm for computing the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.CalculusFieldUnivariateFunction`
        
            Parameters:
                v (:class:`~org.hipparchus.analysis.polynomials.FieldPolynomialSplineFunction`): Point for which the function value should be computed.
        
            Returns:
                the value.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`v` is outside of the domain of the spline function (smaller than the smallest knot point or larger than the
                    largest knot point).
        
        
        """
        ...
    @typing.overload
    def value(self, t: _FieldPolynomialSplineFunction__T) -> _FieldPolynomialSplineFunction__T: ...

class PolynomialFunction(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, org.hipparchus.analysis.FieldUnivariateFunction, java.io.Serializable):
    """
    public class PolynomialFunction extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`, :class:`~org.hipparchus.analysis.FieldUnivariateFunction`, Serializable
    
        Immutable representation of a real polynomial function with real coefficients.
    
        `Horner's Method <http://mathworld.wolfram.com/HornersMethod.html>` is used to evaluate the function.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.List[float]): ...
    def add(self, polynomialFunction: 'PolynomialFunction') -> 'PolynomialFunction':
        """
            Add a polynomial to the instance.
        
            Parameters:
                p (:class:`~org.hipparchus.analysis.polynomials.PolynomialFunction`): Polynomial to add.
        
            Returns:
                a new polynomial which is the sum of the instance and :code:`p`.
        
        
        """
        ...
    def antiDerivative(self) -> 'PolynomialFunction':
        """
            Returns an anti-derivative of this polynomial, with 0 constant term.
        
            Returns:
                a polynomial whose derivative has the same coefficients as this polynomial
        
        
        """
        ...
    def degree(self) -> int:
        """
            Returns the degree of the polynomial.
        
            Returns:
                the degree of the polynomial.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getCoefficients(self) -> typing.List[float]:
        """
            Returns a copy of the coefficients array.
        
            Changes made to the returned copy will not affect the coefficients of the polynomial.
        
            Returns:
                a fresh copy of the coefficients array.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def integrate(self, double: float, double2: float) -> float:
        """
            Returns the definite integral of this polymomial over the given interval.
        
            [lower, upper] must describe a finite interval (neither can be infinite and lower must be less than or equal to upper).
        
            Parameters:
                lower (double): lower bound for the integration
                upper (double): upper bound for the integration
        
            Returns:
                the integral of this polymomial over the given interval
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the bounds do not describe a finite interval
        
        
        """
        ...
    def multiply(self, polynomialFunction: 'PolynomialFunction') -> 'PolynomialFunction':
        """
            Multiply the instance by a polynomial.
        
            Parameters:
                p (:class:`~org.hipparchus.analysis.polynomials.PolynomialFunction`): Polynomial to multiply by.
        
            Returns:
                a new polynomial equal to this times :code:`p`
        
        
        """
        ...
    def negate(self) -> 'PolynomialFunction':
        """
            Negate the instance.
        
            Returns:
                a new polynomial with all coefficients negated
        
        
        """
        ...
    def polynomialDerivative(self) -> 'PolynomialFunction':
        """
            Returns the derivative as a :class:`~org.hipparchus.analysis.polynomials.PolynomialFunction`.
        
            Returns:
                the derivative polynomial.
        
        
        """
        ...
    def subtract(self, polynomialFunction: 'PolynomialFunction') -> 'PolynomialFunction':
        """
            Subtract a polynomial from the instance.
        
            Parameters:
                p (:class:`~org.hipparchus.analysis.polynomials.PolynomialFunction`): Polynomial to subtract.
        
            Returns:
                a new polynomial which is the instance minus :code:`p`.
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of the polynomial.
        
            The representation is user oriented. Terms are displayed lowest degrees first. The multiplications signs, coefficients
            equals to one and null terms are not displayed (except if the polynomial is 0, in which case the 0 constant term is
            displayed). Addition of terms with negative coefficients are replaced by subtraction of terms with positive coefficients
            except for the first displayed term (i.e. we display :code:`-3` for a constant negative polynomial, but :code:`1 - 3 x +
            x^2` if the negative coefficient is not the first one displayed).
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the polynomial.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _value_2__T = typing.TypeVar('_value_2__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value of the function for the given argument.
        
            The value returned is
        
            :code:`coefficients[n] * x^n + ... + coefficients[1] * x + coefficients[0]`
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                x (double): Argument for which the function value should be computed.
        
            Returns:
                the value of the polynomial at the given point.
        
            Also see:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`
        
        public <T extends :class:`~org.hipparchus.analysis.differentiation.Derivative`<T>> T value(T t) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`, :class:`~org.hipparchus.exception.NullArgumentException`
        
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`coefficients` is empty.
                :class:`~org.hipparchus.exception.NullArgumentException`: if :code:`coefficients` is :code:`null`.
        
        public <T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> T value(T t) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`, :class:`~org.hipparchus.exception.NullArgumentException`
        
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.FieldUnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.FieldUnivariateFunction`
        
            Parameters:
                t (T): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`coefficients` is empty.
                :class:`~org.hipparchus.exception.NullArgumentException`: if :code:`coefficients` is :code:`null`.
        
            Since:
                1.3
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...
    @typing.overload
    def value(self, t: _value_2__T) -> _value_2__T: ...
    class Parametric(org.hipparchus.analysis.ParametricUnivariateFunction):
        def __init__(self): ...
        def gradient(self, double: float, *double2: float) -> typing.List[float]: ...
        def value(self, double: float, *double2: float) -> float: ...

class PolynomialFunctionLagrangeForm(org.hipparchus.analysis.UnivariateFunction):
    """
    public class PolynomialFunctionLagrangeForm extends Object implements :class:`~org.hipparchus.analysis.UnivariateFunction`
    
        Implements the representation of a real polynomial function in ` Lagrange Form
        <http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html>`. For reference, see **Introduction to Numerical
        Analysis**, ISBN 038795452X, chapter 2.
    
        The approximated function should be smooth enough for Lagrange polynomial to work well. Otherwise, consider using
        splines instead.
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def degree(self) -> int:
        """
            Returns the degree of the polynomial.
        
            Returns:
                the degree of the polynomial
        
        
        """
        ...
    @staticmethod
    def evaluate(doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> float: ...
    def getCoefficients(self) -> typing.List[float]:
        """
            Returns a copy of the coefficients array.
        
            Changes made to the returned copy will not affect the polynomial.
        
            Note that coefficients computation can be ill-conditioned. Use with caution and only when it is necessary.
        
            Returns:
                a fresh copy of the coefficients array
        
        
        """
        ...
    def getInterpolatingPoints(self) -> typing.List[float]:
        """
            Returns a copy of the interpolating points array.
        
            Changes made to the returned copy will not affect the polynomial.
        
            Returns:
                a fresh copy of the interpolating points array
        
        
        """
        ...
    def getInterpolatingValues(self) -> typing.List[float]:
        """
            Returns a copy of the interpolating values array.
        
            Changes made to the returned copy will not affect the polynomial.
        
            Returns:
                a fresh copy of the interpolating values array
        
        
        """
        ...
    def value(self, double: float) -> float:
        """
            Calculate the function value at the given point.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                z (double): Point at which the function value is to be computed.
        
            Returns:
                the function value.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x` and :code:`y` have different lengths.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`x` is not sorted in strictly increasing order.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the size of :code:`x` is less than 2.
        
        
        """
        ...
    @staticmethod
    def verifyInterpolationArray(doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> bool: ...

class PolynomialFunctionNewtonForm(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, org.hipparchus.analysis.FieldUnivariateFunction):
    """
    public class PolynomialFunctionNewtonForm extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`, :class:`~org.hipparchus.analysis.FieldUnivariateFunction`
    
        Implements the representation of a real polynomial function in Newton Form. For reference, see **Elementary Numerical
        Analysis**, ISBN 0070124477, chapter 2.
    
        The formula of polynomial in Newton form is p(x) = a[0] + a[1](x-c[0]) + a[2](x-c[0])(x-c[1]) + ... +
        a[n](x-c[0])(x-c[1])...(x-c[n-1]) Note that the length of a[] is one more than the length of c[]
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def degree(self) -> int:
        """
            Returns the degree of the polynomial.
        
            Returns:
                the degree of the polynomial
        
        
        """
        ...
    @staticmethod
    def evaluate(doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float) -> float: ...
    def getCenters(self) -> typing.List[float]:
        """
            Returns a copy of the centers array.
        
            Changes made to the returned copy will not affect the polynomial.
        
            Returns:
                a fresh copy of the centers array.
        
        
        """
        ...
    def getCoefficients(self) -> typing.List[float]:
        """
            Returns a copy of the coefficients array.
        
            Changes made to the returned copy will not affect the polynomial.
        
            Returns:
                a fresh copy of the coefficients array.
        
        
        """
        ...
    def getNewtonCoefficients(self) -> typing.List[float]:
        """
            Returns a copy of coefficients in Newton form formula.
        
            Changes made to the returned copy will not affect the polynomial.
        
            Returns:
                a fresh copy of coefficients in Newton form formula
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _value_2__T = typing.TypeVar('_value_2__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Calculate the function value at the given point.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                z (double): Point at which the function value is to be computed.
        
            Returns:
                the function value.
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.FieldUnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.FieldUnivariateFunction`
        
            Parameters:
                t (T): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_2__T) -> _value_2__T: ...

class PolynomialSplineFunction(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, org.hipparchus.analysis.FieldUnivariateFunction):
    """
    public class PolynomialSplineFunction extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`, :class:`~org.hipparchus.analysis.FieldUnivariateFunction`
    
        Represents a polynomial spline function.
    
        A **polynomial spline function** consists of a set of *interpolating polynomials* and an ascending array of domain *knot
        points*, determining the intervals over which the spline function is defined by the constituent polynomials. The
        polynomials are assumed to have been computed to match the values of another function at the knot points. The value
        consistency constraints are not currently enforced by :code:`PolynomialSplineFunction` itself, but are assumed to hold
        among the polynomials and knot points passed to the constructor.
    
        N.B.: The polynomials in the :code:`polynomials` property must be centered on the knot points to compute the spline
        function values. See below.
    
        The domain of the polynomial spline function is :code:`[smallest knot, largest knot]`. Attempts to evaluate the function
        at values outside of this range generate IllegalArgumentExceptions.
    
        The value of the polynomial spline function for an argument :code:`x` is computed as follows:
    
          1.  The knot array is searched to find the segment to which :code:`x` belongs. If :code:`x` is less than the smallest knot
            point or greater than the largest one, an :code:`IllegalArgumentException` is thrown.
          2.  Let :code:`j` be the index of the largest knot point that is less than or equal to :code:`x`. The value returned is
            :code:`polynomials[j](x - knot[j])`
    """
    def __init__(self, doubleArray: typing.List[float], polynomialFunctionArray: typing.List[PolynomialFunction]): ...
    def getKnots(self) -> typing.List[float]:
        """
            Get an array copy of the knot points. It returns a fresh copy of the array. Changes made to the copy will not affect the
            knots property.
        
            Returns:
                the knot points.
        
        
        """
        ...
    def getN(self) -> int:
        """
            Get the number of spline segments. It is also the number of polynomials and the number of knot points - 1.
        
            Returns:
                the number of spline segments.
        
        
        """
        ...
    def getPolynomials(self) -> typing.List[PolynomialFunction]:
        """
            Get a copy of the interpolating polynomials array. It returns a fresh copy of the array. Changes made to the copy will
            not affect the polynomials property.
        
            Returns:
                the interpolating polynomials.
        
        
        """
        ...
    def isValidPoint(self, double: float) -> bool:
        """
            Indicates whether a point is within the interpolation range.
        
            Parameters:
                x (double): Point.
        
            Returns:
                :code:`true` if :code:`x` is a valid point.
        
        
        """
        ...
    def polynomialSplineDerivative(self) -> 'PolynomialSplineFunction':
        """
            Get the derivative of the polynomial spline function.
        
            Returns:
                the derivative function.
        
        
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _value_2__T = typing.TypeVar('_value_2__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float:
        """
            Compute the value for the function. See :class:`~org.hipparchus.analysis.polynomials.PolynomialSplineFunction` for
            details on the algorithm for computing the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.UnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.UnivariateFunction`
        
            Parameters:
                v (double): Point for which the function value should be computed.
        
            Returns:
                the value.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`v` is outside of the domain of the spline function (smaller than the smallest knot point or larger than the
                    largest knot point).
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
            Compute the value for the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`
        
            Parameters:
                t (T): the point for which the function value should be computed
        
            Returns:
                the value
        
            Compute the value of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.FieldUnivariateFunction.value`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.FieldUnivariateFunction`
        
            Parameters:
                t (T): Point at which the function value should be computed.
        
            Returns:
                the value of the function.
        
        
        """
        ...
    @typing.overload
    def value(self, t: _value_2__T) -> _value_2__T: ...

class PolynomialsUtils:
    """
    public class PolynomialsUtils extends Object
    
        A collection of static methods that operate on or return polynomials.
    """
    @staticmethod
    def createChebyshevPolynomial(int: int) -> PolynomialFunction:
        """
            Create a Chebyshev polynomial of the first kind.
        
            Chebyshev polynomials of the first kind are orthogonal polynomials. They can be defined by the following recurrence
            relations:
        
            \( T_0(x) = 1 \\ T_1(x) = x \\ T_{k+1}(x) = 2x T_k(x) - T_{k-1}(x) \)
        
            Parameters:
                degree (int): degree of the polynomial
        
            Returns:
                Chebyshev polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createHermitePolynomial(int: int) -> PolynomialFunction:
        """
            Create a Hermite polynomial.
        
            `Hermite polynomials <http://mathworld.wolfram.com/HermitePolynomial.html>` are orthogonal polynomials. They can be
            defined by the following recurrence relations:
        
            \( H_0(x) = 1 \\ H_1(x) = 2x \\ H_{k+1}(x) = 2x H_k(X) - 2k H_{k-1}(x) \)
        
            Parameters:
                degree (int): degree of the polynomial
        
            Returns:
                Hermite polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createJacobiPolynomial(int: int, int2: int, int3: int) -> PolynomialFunction:
        """
            Create a Jacobi polynomial.
        
            `Jacobi polynomials <http://mathworld.wolfram.com/JacobiPolynomial.html>` are orthogonal polynomials. They can be
            defined by the following recurrence relations:
        
            \( P_0^{vw}(x) = 1 \\ P_{-1}^{vw}(x) = 0 \\ 2k(k + v + w)(2k + v + w - 2) P_k^{vw}(x) = \\ (2k + v + w - 1)[(2k + v +
            w)(2k + v + w - 2) x + v^2 - w^2] P_{k-1}^{vw}(x) \\ - 2(k + v - 1)(k + w - 1)(2k + v + w) P_{k-2}^{vw}(x) \)
        
            Parameters:
                degree (int): degree of the polynomial
                v (int): first exponent
                w (int): second exponent
        
            Returns:
                Jacobi polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createLaguerrePolynomial(int: int) -> PolynomialFunction:
        """
            Create a Laguerre polynomial.
        
            `Laguerre polynomials <http://mathworld.wolfram.com/LaguerrePolynomial.html>` are orthogonal polynomials. They can be
            defined by the following recurrence relations:
        
            \( L_0(x) = 1 \\ L_1(x) = 1 - x \\ (k+1) L_{k+1}(x) = (2k + 1 - x) L_k(x) - k L_{k-1}(x) \)
        
            Parameters:
                degree (int): degree of the polynomial
        
            Returns:
                Laguerre polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createLegendrePolynomial(int: int) -> PolynomialFunction:
        """
            Create a Legendre polynomial.
        
            `Legendre polynomials <http://mathworld.wolfram.com/LegendrePolynomial.html>` are orthogonal polynomials. They can be
            defined by the following recurrence relations:
        
            \( P_0(x) = 1 \\ P_1(x) = x \\ (k+1) P_{k+1}(x) = (2k+1) x P_k(x) - k P_{k-1}(x) \)
        
            Parameters:
                degree (int): degree of the polynomial
        
            Returns:
                Legendre polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def shift(doubleArray: typing.List[float], double2: float) -> typing.List[float]:
        """
            Compute the coefficients of the polynomial \(P_s(x)\) whose values at point :code:`x` will be the same as the those from
            the original polynomial \(P(x)\) when computed at :code:`x + shift`.
        
            More precisely, let \(\Delta = \) :code:`shift` and let \(P_s(x) = P(x + \Delta)\). The returned array consists of the
            coefficients of \(P_s\). So if \(a_0, ..., a_{n-1}\) are the coefficients of \(P\), then the returned array \(b_0, ...,
            b_{n-1}\) satisfies the identity \(\sum_{i=0}^{n-1} b_i x^i = \sum_{i=0}^{n-1} a_i (x + \Delta)^i\) for all \(x\).
        
            Parameters:
                coefficients (double[]): Coefficients of the original polynomial.
                shift (double): Shift value.
        
            Returns:
                the coefficients \(b_i\) of the shifted polynomial.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.polynomials")``.

    FieldPolynomialFunction: typing.Type[FieldPolynomialFunction]
    FieldPolynomialSplineFunction: typing.Type[FieldPolynomialSplineFunction]
    PolynomialFunction: typing.Type[PolynomialFunction]
    PolynomialFunctionLagrangeForm: typing.Type[PolynomialFunctionLagrangeForm]
    PolynomialFunctionNewtonForm: typing.Type[PolynomialFunctionNewtonForm]
    PolynomialSplineFunction: typing.Type[PolynomialSplineFunction]
    PolynomialsUtils: typing.Type[PolynomialsUtils]
