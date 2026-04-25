
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jpype
import org
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.differentiation
import typing



_FieldPolynomialFunction__T = typing.TypeVar('_FieldPolynomialFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPolynomialFunction(org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldPolynomialFunction__T], typing.Generic[_FieldPolynomialFunction__T]):
    """
    implements CalculusFieldUnivariateFunction<T>
    
    Immutable representation of a real polynomial function with real coefficients.
    
    `Horner's Method <http://mathworld.wolfram.com/HornersMethod.html>` is used to evaluate the function.
    
    Since:
        1.5
    """
    def __init__(self, c: typing.Union[typing.List[_FieldPolynomialFunction__T], jpype.JArray]):
        """
        Construct a polynomial with the given coefficients. The first element of the coefficients array is the constant term. Higher degree coefficients follow in sequence. The degree of the resulting polynomial is the index of the last non-null element of the array, or 0 if all elements are null.
        
        The constructor makes a copy of the input array and assigns the copy to the coefficients property.
        
        Parameters:
            c (FieldPolynomialFunction[]): Polynomial coefficients.
        
        Raises:
            NullArgumentException: if c is null.
            MathIllegalArgumentException: if c is empty.
        
        
        """
        ...
    def add(self, p: 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]:
        """
        Add a polynomial to the instance.
        
        Parameters:
            p (FieldPolynomialFunction<FieldPolynomialFunction> p): Polynomial to add.
        
        Returns:
            a new polynomial which is the sum of the instance and p.
        
        
        """
        ...
    def antiDerivative(self) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]:
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
    def getCoefficients(self) -> typing.MutableSequence[_FieldPolynomialFunction__T]:
        """
        Returns a copy of the coefficients array.
        
        Changes made to the returned copy will not affect the coefficients of the polynomial.
        
        Returns:
            a fresh copy of the coefficients array.
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldPolynomialFunction__T]:
        """
        Get the Field to which the instance belongs.
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
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
            MathIllegalArgumentException: if the bounds do not describe a finite interval
        
        Returns the definite integral of this polymomial over the given interval.
        
        [lower, upper] must describe a finite interval (neither can be infinite and lower must be less than or equal to upper).
        
        Parameters:
            lower (FieldPolynomialFunction): lower bound for the integration
            upper (FieldPolynomialFunction): upper bound for the integration
        
        Returns:
            the integral of this polymomial over the given interval
        
        Raises:
            MathIllegalArgumentException: if the bounds do not describe a finite interval
        
        
        """
        ...
    @typing.overload
    def integrate(self, t: _FieldPolynomialFunction__T, t2: _FieldPolynomialFunction__T) -> _FieldPolynomialFunction__T: ...
    def multiply(self, p: 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]:
        """
        Multiply the instance by a polynomial.
        
        Parameters:
            p (FieldPolynomialFunction<FieldPolynomialFunction> p): Polynomial to multiply by.
        
        Returns:
            a new polynomial equal to this times p
        
        
        """
        ...
    def negate(self) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]:
        """
        Negate the instance.
        
        Returns:
            a new polynomial with all coefficients negated
        
        
        """
        ...
    def polynomialDerivative(self) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]:
        """
        Returns the derivative as a FieldPolynomialFunction.
        
        Returns:
            the derivative polynomial.
        
        
        """
        ...
    def subtract(self, p: 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]) -> 'FieldPolynomialFunction'[_FieldPolynomialFunction__T]:
        """
        Subtract a polynomial from the instance.
        
        Parameters:
            p (FieldPolynomialFunction<FieldPolynomialFunction> p): Polynomial to subtract.
        
        Returns:
            a new polynomial which is the instance minus p.
        
        
        """
        ...
    @typing.overload
    def value(self, double: float) -> _FieldPolynomialFunction__T:
        """
        Compute the value of the function for the given argument.
        
        The value returned is
        
         + coefficients[1] * x + coefficients[0]
        
        Parameters:
            x (double): Argument for which the function value should be computed.
        
        Returns:
            the value of the polynomial at the given point.
        
              - value
        
        Compute the value of the function for the given argument.
        
        The value returned is
        
         + coefficients[1] * x + coefficients[0]
        
        Specified by: value in interface CalculusFieldUnivariateFunction
        
        Parameters:
            x (FieldPolynomialFunction): Argument for which the function value should be computed.
        
        Returns:
            the value of the polynomial at the given point.
        
              - value
        
        
        
        """
        ...
    @typing.overload
    def value(self, t: _FieldPolynomialFunction__T) -> _FieldPolynomialFunction__T: ...

_FieldPolynomialFunctionLagrangeForm__T = typing.TypeVar('_FieldPolynomialFunctionLagrangeForm__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPolynomialFunctionLagrangeForm(org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldPolynomialFunctionLagrangeForm__T], typing.Generic[_FieldPolynomialFunctionLagrangeForm__T]):
    """
    implements CalculusFieldUnivariateFunction<T>
    
    Implements the representation of a real polynomial function in ` Lagrange Form <http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html>`. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 2.
    
    The approximated function should be smooth enough for Lagrange polynomial to work well. Otherwise, consider using splines instead.
    
    Since:
        4.0
    
          - PolynomialFunctionLagrangeForm
    """
    def __init__(self, x: typing.Union[typing.List[_FieldPolynomialFunctionLagrangeForm__T], jpype.JArray], y: typing.Union[typing.List[_FieldPolynomialFunctionLagrangeForm__T], jpype.JArray]):
        """
        Construct a Lagrange polynomial with the given abscissas and function values. The order of interpolating points is important.
        
        The constructor makes copy of the input arrays and assigns them.
        
        Parameters:
            x (FieldPolynomialFunctionLagrangeForm[]): interpolating points
            y (FieldPolynomialFunctionLagrangeForm[]): function values at interpolating points
        
        Raises:
            MathIllegalArgumentException: if the array lengths are different.
            MathIllegalArgumentException: if the number of points is less than 2.
            MathIllegalArgumentException: if two abscissae have the same value.
            MathIllegalArgumentException: if the abscissae are not sorted.
        
        
        """
        ...
    def degree(self) -> int:
        """
        Returns the degree of the polynomial.
        
        Returns:
            the degree of the polynomial
        
        
        """
        ...
    def getCoefficients(self) -> typing.MutableSequence[_FieldPolynomialFunctionLagrangeForm__T]:
        """
        Returns a copy of the coefficients array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Note that coefficients computation can be ill-conditioned. Use with caution and only when it is necessary.
        
        Returns:
            a fresh copy of the coefficients array
        
        
        """
        ...
    def getInterpolatingPoints(self) -> typing.MutableSequence[_FieldPolynomialFunctionLagrangeForm__T]:
        """
        Returns a copy of the interpolating points array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Returns:
            a fresh copy of the interpolating points array
        
        
        """
        ...
    def getInterpolatingValues(self) -> typing.MutableSequence[_FieldPolynomialFunctionLagrangeForm__T]:
        """
        Returns a copy of the interpolating values array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Returns:
            a fresh copy of the interpolating values array
        
        
        """
        ...
    def value(self, z: _FieldPolynomialFunctionLagrangeForm__T) -> _FieldPolynomialFunctionLagrangeForm__T:
        """
        Calculate the function value at the given point.
        
        Specified by: value in interface CalculusFieldUnivariateFunction
        
        Parameters:
            z (FieldPolynomialFunctionLagrangeForm): Point at which the function value is to be computed.
        
        Returns:
            the function value.
        
        Raises:
            MathIllegalArgumentException: if x and y have different lengths.
            MathIllegalArgumentException: if x is not sorted in strictly increasing order.
            MathIllegalArgumentException: if the size of x is less than 2.
        
        
        """
        ...

_FieldPolynomialSplineFunction__T = typing.TypeVar('_FieldPolynomialSplineFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPolynomialSplineFunction(org.hipparchus.analysis.CalculusFieldUnivariateFunction[_FieldPolynomialSplineFunction__T], typing.Generic[_FieldPolynomialSplineFunction__T]):
    """
    implements CalculusFieldUnivariateFunction<T>
    
    Represents a polynomial spline function.
    
    A polynomial spline function consists of a set of interpolating polynomials and an ascending array of domain knot points, determining the intervals over which the spline function is defined by the constituent polynomials. The polynomials are assumed to have been computed to match the values of another function at the knot points. The value consistency constraints are not currently enforced by PolynomialSplineFunction itself, but are assumed to hold among the polynomials and knot points passed to the constructor.
    
    N.B.: The polynomials in the polynomials property must be centered on the knot points to compute the spline function values. See below.
    
    The domain of the polynomial spline function is [smallest knot, largest knot]. Attempts to evaluate the function at values outside of this range generate IllegalArgumentExceptions.
    
    The value of the polynomial spline function for an argument x is computed as follows:
    
      1.  The knot array is searched to find the segment to which x belongs. If x is less than the smallest knot point or greater than the largest one, an IllegalArgumentException is thrown. 2.  Let j be the index of the largest knot point that is less than or equal to x. The value returned is polynomials[j](x - knot[j])
    
    
    Since:
        1.5
    """
    def __init__(self, knots: typing.Union[typing.List[_FieldPolynomialSplineFunction__T], jpype.JArray], polynomials: typing.Union[typing.List[FieldPolynomialFunction[_FieldPolynomialSplineFunction__T]], jpype.JArray]):
        """
        Construct a polynomial spline function with the given segment delimiters and interpolating polynomials. The constructor copies both arrays and assigns the copies to the knots and polynomials properties, respectively.
        
        Parameters:
            knots (FieldPolynomialSplineFunction[]): Spline segment interval delimiters.
            polynomials (FieldPolynomialFunction<FieldPolynomialSplineFunction>[]): Polynomial functions that make up the spline.
        
        Raises:
            NullArgumentException: if either of the input arrays is null.
            MathIllegalArgumentException: if knots has length less than 2.
            MathIllegalArgumentException: if length - 1.
            MathIllegalArgumentException: if the knots array is not strictly increasing.
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldPolynomialSplineFunction__T]:
        """
        Get the Field to which the instance belongs.
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getKnots(self) -> typing.MutableSequence[_FieldPolynomialSplineFunction__T]:
        """
        Get an array copy of the knot points. It returns a fresh copy of the array. Changes made to the copy will not affect the knots property.
        
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
    def getPolynomials(self) -> typing.MutableSequence[FieldPolynomialFunction[_FieldPolynomialSplineFunction__T]]:
        """
        Get a copy of the interpolating polynomials array. It returns a fresh copy of the array. Changes made to the copy will not affect the polynomials property.
        
        Returns:
            the interpolating polynomials.
        
        
        """
        ...
    def isValidPoint(self, x: _FieldPolynomialSplineFunction__T) -> bool:
        """
        Indicates whether a point is within the interpolation range.
        
        Parameters:
            x (FieldPolynomialSplineFunction): Point.
        
        Returns:
            true if x is a valid point.
        
        
        """
        ...
    def polynomialSplineDerivative(self) -> 'FieldPolynomialSplineFunction'[_FieldPolynomialSplineFunction__T]:
        """
        Get the derivative of the polynomial spline function.
        
        Returns:
            the derivative function.
        
        
        """
        ...
    @typing.overload
    def value(self, double: float) -> _FieldPolynomialSplineFunction__T:
        """
        Compute the value for the function. See FieldPolynomialSplineFunction for details on the algorithm for computing the value of the function.
        
        Parameters:
            v (double): Point for which the function value should be computed.
        
        Returns:
            the value.
        
        Raises:
            MathIllegalArgumentException: if v is outside of the domain of the spline function (smaller than the smallest knot point or larger than the
                largest knot point).
        
        Compute the value for the function. See FieldPolynomialSplineFunction for details on the algorithm for computing the value of the function.
        
        Specified by: value in interface CalculusFieldUnivariateFunction
        
        Parameters:
            v (FieldPolynomialSplineFunction): Point for which the function value should be computed.
        
        Returns:
            the value.
        
        Raises:
            MathIllegalArgumentException: if v is outside of the domain of the spline function (smaller than the smallest knot point or larger than the
                largest knot point).
        
        
        """
        ...
    @typing.overload
    def value(self, t: _FieldPolynomialSplineFunction__T) -> _FieldPolynomialSplineFunction__T: ...

class JacobiKey:
    """
    Class for handling Jacobi polynomials keys.
    
    Since:
        3.1
    """
    def __init__(self, v: int, w: int):
        """
        Simple constructor.
        
        Parameters:
            v (int): first exponent
            w (int): second exponent
        
        
        """
        ...
    def equals(self, key: typing.Any) -> bool:
        """
        Check if the instance represent the same key as another instance.
        
        Overrides: equals in class Object
        
        Parameters:
            key (Object): other key
        
        Returns:
            true if the instance and the other key refer to the same polynomial
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get hash code.
        
        Overrides: hashCode in class Object
        
        Returns:
            hash code
        
        
        """
        ...

class PolynomialFunction(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, org.hipparchus.analysis.FieldUnivariateFunction, java.io.Serializable):
    """
    implements UnivariateDifferentiableFunction, FieldUnivariateFunction, Serializable
    
    Immutable representation of a real polynomial function with real coefficients.
    
    `Horner's Method <http://mathworld.wolfram.com/HornersMethod.html>` is used to evaluate the function.
    
          - serialized
    """
    def __init__(self, *c: float):
        """
        Construct a polynomial with the given coefficients. The first element of the coefficients array is the constant term. Higher degree coefficients follow in sequence. The degree of the resulting polynomial is the index of the last non-null element of the array, or 0 if all elements are null.
        
        The constructor makes a copy of the input array and assigns the copy to the coefficients property.
        
        Parameters:
            c (double...): Polynomial coefficients.
        
        Raises:
            NullArgumentException: if c is null.
            MathIllegalArgumentException: if c is empty.
        
        
        """
        ...
    def add(self, p: 'PolynomialFunction') -> 'PolynomialFunction':
        """
        Add a polynomial to the instance.
        
        Parameters:
            p (PolynomialFunction): Polynomial to add.
        
        Returns:
            a new polynomial which is the sum of the instance and p.
        
        
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
        Overrides: equals in class Object
        
        
        """
        ...
    def getCoefficients(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the coefficients array.
        
        Changes made to the returned copy will not affect the coefficients of the polynomial.
        
        Returns:
            a fresh copy of the coefficients array.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class Object
        
        
        """
        ...
    def integrate(self, lower: float, upper: float) -> float:
        """
        Returns the definite integral of this polymomial over the given interval.
        
        [lower, upper] must describe a finite interval (neither can be infinite and lower must be less than or equal to upper).
        
        Parameters:
            lower (double): lower bound for the integration
            upper (double): upper bound for the integration
        
        Returns:
            the integral of this polymomial over the given interval
        
        Raises:
            MathIllegalArgumentException: if the bounds do not describe a finite interval
        
        
        """
        ...
    def multiply(self, p: 'PolynomialFunction') -> 'PolynomialFunction':
        """
        Multiply the instance by a polynomial.
        
        Parameters:
            p (PolynomialFunction): Polynomial to multiply by.
        
        Returns:
            a new polynomial equal to this times p
        
        
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
        Returns the derivative as a PolynomialFunction.
        
        Returns:
            the derivative polynomial.
        
        
        """
        ...
    def subtract(self, p: 'PolynomialFunction') -> 'PolynomialFunction':
        """
        Subtract a polynomial from the instance.
        
        Parameters:
            p (PolynomialFunction): Polynomial to subtract.
        
        Returns:
            a new polynomial which is the instance minus p.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Returns a string representation of the polynomial.
        
        The representation is user oriented. Terms are displayed lowest degrees first. The multiplications signs, coefficients equals to one and null terms are not displayed (except if the polynomial is 0, in which case the 0 constant term is displayed). Addition of terms with negative coefficients are replaced by subtraction of terms with positive coefficients except for the first displayed term (i.e. we display -3 for a constant negative polynomial, but 1 - 3 x + x^2 if the negative coefficient is not the first one displayed).
        
        Overrides: toString in class Object
        
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
        
         + coefficients[1] * x + coefficients[0]
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            x (double): Argument for which the function value should be computed.
        
        Returns:
            the value of the polynomial at the given point.
        
              - value
        
        public <T extends Derivative<T>> T value(T t) throws MathIllegalArgumentException, NullArgumentException
        
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        Raises:
            MathIllegalArgumentException: if coefficients is empty.
            NullArgumentException: if coefficients is null.
        
        public <T extends CalculusFieldElement<T>> T value(T t) throws MathIllegalArgumentException, NullArgumentException
        
        Compute the value of the function.
        
        Specified by: value in interface FieldUnivariateFunction
        
        Parameters:
            t (T): Point at which the function value should be computed.
        
        Returns:
            the value of the function.
        
        Raises:
            MathIllegalArgumentException: if coefficients is empty.
            NullArgumentException: if coefficients is null.
        
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
        def gradient(self, double: float, *double2: float) -> typing.MutableSequence[float]: ...
        def value(self, double: float, *double2: float) -> float: ...

class PolynomialFunctionLagrangeForm(org.hipparchus.analysis.UnivariateFunction):
    """
    implements UnivariateFunction
    
    Implements the representation of a real polynomial function in ` Lagrange Form <http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html>`. For reference, see Introduction to Numerical Analysis, ISBN 038795452X, chapter 2.
    
    The approximated function should be smooth enough for Lagrange polynomial to work well. Otherwise, consider using splines instead.
    """
    def __init__(self, x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]):
        """
        Construct a Lagrange polynomial with the given abscissas and function values. The order of interpolating points are not important.
        
        The constructor makes copy of the input arrays and assigns them.
        
        Parameters:
            x (double[]): interpolating points
            y (double[]): function values at interpolating points
        
        Raises:
            MathIllegalArgumentException: if the array lengths are different.
            MathIllegalArgumentException: if the number of points is less than 2.
            MathIllegalArgumentException: if two abscissae have the same value.
        
        
        """
        ...
    def degree(self) -> int:
        """
        Returns the degree of the polynomial.
        
        Returns:
            the degree of the polynomial
        
        
        """
        ...
    @staticmethod
    def evaluate(x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], z: float) -> float:
        """
        Evaluate the Lagrange polynomial using ` Neville's Algorithm <http://mathworld.wolfram.com/NevillesAlgorithm.html>`. It takes O(n^2) time.
        
        Parameters:
            x (double[]): Interpolating points array.
            y (double[]): Interpolating values array.
            z (double): Point at which the function value is to be computed.
        
        Returns:
            the function value.
        
        Raises:
            MathIllegalArgumentException: if x and y have different lengths.
            MathIllegalArgumentException: if x is not sorted in strictly increasing order.
            MathIllegalArgumentException: if the size of x is less than 2.
        
        
        """
        ...
    def getCoefficients(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the coefficients array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Note that coefficients computation can be ill-conditioned. Use with caution and only when it is necessary.
        
        Returns:
            a fresh copy of the coefficients array
        
        
        """
        ...
    def getInterpolatingPoints(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the interpolating points array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Returns:
            a fresh copy of the interpolating points array
        
        
        """
        ...
    def getInterpolatingValues(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the interpolating values array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Returns:
            a fresh copy of the interpolating values array
        
        
        """
        ...
    def value(self, z: float) -> float:
        """
        Calculate the function value at the given point.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            z (double): Point at which the function value is to be computed.
        
        Returns:
            the function value.
        
        Raises:
            MathIllegalArgumentException: if x and y have different lengths.
            MathIllegalArgumentException: if x is not sorted in strictly increasing order.
            MathIllegalArgumentException: if the size of x is less than 2.
        
        
        """
        ...
    @staticmethod
    def verifyInterpolationArray(x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray], abort: bool) -> bool:
        """
        Check that the interpolation arrays are valid. The arrays features checked by this method are that both arrays have the same length and this length is at least 2.
        
        Parameters:
            x (double[]): Interpolating points array.
            y (double[]): Interpolating values array.
            abort (boolean): Whether to throw an exception if x is not sorted.
        
        Returns:
            false if the x is not sorted in increasing order, true otherwise.
        
        Raises:
            MathIllegalArgumentException: if the array lengths are different.
            MathIllegalArgumentException: if the number of points is less than 2.
            MathIllegalArgumentException: if x is not sorted in strictly increasing order and abort is true.
        
              - evaluate
              - computeCoefficients
        
        
        
        """
        ...

class PolynomialFunctionNewtonForm(org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction, org.hipparchus.analysis.FieldUnivariateFunction):
    """
    implements UnivariateDifferentiableFunction, FieldUnivariateFunction
    
    Implements the representation of a real polynomial function in Newton Form. For reference, see Elementary Numerical Analysis, ISBN 0070124477, chapter 2.
    
    The formula of polynomial in Newton form is p(x) = a[0] + a[1](x-c[0]) + a[2](x-c[0])(x-c[1]) + ... + a[n](x-c[0])(x-c[1])...(x-c[n-1]) Note that the length of a[] is one more than the length of c[]
    """
    def __init__(self, a: typing.Union[typing.List[float], jpype.JArray], c: typing.Union[typing.List[float], jpype.JArray]):
        """
        Construct a Newton polynomial with the given a[] and c[]. The order of centers are important in that if c[] shuffle, then values of a[] would completely change, not just a permutation of old a[].
        
        The constructor makes copy of the input arrays and assigns them.
        
        Parameters:
            a (double[]): Coefficients in Newton form formula.
            c (double[]): Centers.
        
        Raises:
            NullArgumentException: if any argument is null.
            MathIllegalArgumentException: if any array has zero length.
            MathIllegalArgumentException: if the size difference between a and c is not equal to 1.
        
        
        """
        ...
    def degree(self) -> int:
        """
        Returns the degree of the polynomial.
        
        Returns:
            the degree of the polynomial
        
        
        """
        ...
    @staticmethod
    def evaluate(a: typing.Union[typing.List[float], jpype.JArray], c: typing.Union[typing.List[float], jpype.JArray], z: float) -> float:
        """
        Evaluate the Newton polynomial using nested multiplication. It is also called ` Horner's Rule <http://mathworld.wolfram.com/HornersRule.html>` and takes O(N) time.
        
        Parameters:
            a (double[]): Coefficients in Newton form formula.
            c (double[]): Centers.
            z (double): Point at which the function value is to be computed.
        
        Returns:
            the function value.
        
        Raises:
            NullArgumentException: if any argument is null.
            MathIllegalArgumentException: if any array has zero length.
            MathIllegalArgumentException: if the size difference between a and c is not equal to 1.
        
        
        """
        ...
    def getCenters(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the centers array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Returns:
            a fresh copy of the centers array.
        
        
        """
        ...
    def getCoefficients(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the coefficients array.
        
        Changes made to the returned copy will not affect the polynomial.
        
        Returns:
            a fresh copy of the coefficients array.
        
        
        """
        ...
    def getNewtonCoefficients(self) -> typing.MutableSequence[float]:
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
    def value(self, z: float) -> float:
        """
        Calculate the function value at the given point.
        
        Specified by: value in interface UnivariateFunction
        
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
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        Compute the value of the function.
        
        Specified by: value in interface FieldUnivariateFunction
        
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
    implements UnivariateDifferentiableFunction, FieldUnivariateFunction
    
    Represents a polynomial spline function.
    
    A polynomial spline function consists of a set of interpolating polynomials and an ascending array of domain knot points, determining the intervals over which the spline function is defined by the constituent polynomials. The polynomials are assumed to have been computed to match the values of another function at the knot points. The value consistency constraints are not currently enforced by PolynomialSplineFunction itself, but are assumed to hold among the polynomials and knot points passed to the constructor.
    
    N.B.: The polynomials in the polynomials property must be centered on the knot points to compute the spline function values. See below.
    
    The domain of the polynomial spline function is [smallest knot, largest knot]. Attempts to evaluate the function at values outside of this range generate IllegalArgumentExceptions.
    
    The value of the polynomial spline function for an argument x is computed as follows:
    
      1.  The knot array is searched to find the segment to which x belongs. If x is less than the smallest knot point or greater than the largest one, an IllegalArgumentException is thrown. 2.  Let j be the index of the largest knot point that is less than or equal to x. The value returned is polynomials[j](x - knot[j])
    """
    def __init__(self, knots: typing.Union[typing.List[float], jpype.JArray], polynomials: typing.Union[typing.List[PolynomialFunction], jpype.JArray]):
        """
        Construct a polynomial spline function with the given segment delimiters and interpolating polynomials. The constructor copies both arrays and assigns the copies to the knots and polynomials properties, respectively.
        
        Parameters:
            knots (double[]): Spline segment interval delimiters.
            polynomials (PolynomialFunction[]): Polynomial functions that make up the spline.
        
        Raises:
            NullArgumentException: if either of the input arrays is null.
            MathIllegalArgumentException: if knots has length less than 2.
            MathIllegalArgumentException: if length - 1.
            MathIllegalArgumentException: if the knots array is not strictly increasing.
        
        
        """
        ...
    def getKnots(self) -> typing.MutableSequence[float]:
        """
        Get an array copy of the knot points. It returns a fresh copy of the array. Changes made to the copy will not affect the knots property.
        
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
    def getPolynomials(self) -> typing.MutableSequence[PolynomialFunction]:
        """
        Get a copy of the interpolating polynomials array. It returns a fresh copy of the array. Changes made to the copy will not affect the polynomials property.
        
        Returns:
            the interpolating polynomials.
        
        
        """
        ...
    def isValidPoint(self, x: float) -> bool:
        """
        Indicates whether a point is within the interpolation range.
        
        Parameters:
            x (double): Point.
        
        Returns:
            true if x is a valid point.
        
        
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
    def value(self, v: float) -> float:
        """
        Compute the value for the function. See PolynomialSplineFunction for details on the algorithm for computing the value of the function.
        
        Specified by: value in interface UnivariateFunction
        
        Parameters:
            v (double): Point for which the function value should be computed.
        
        Returns:
            the value.
        
        Raises:
            MathIllegalArgumentException: if v is outside of the domain of the spline function (smaller than the smallest knot point or larger than the
                largest knot point).
        
        """
        ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T:
        """
        Compute the value for the function.
        
        Specified by: value in interface UnivariateDifferentiableFunction
        
        Parameters:
            t (T): the point for which the function value should be computed
        
        Returns:
            the value
        
        Compute the value of the function.
        
        Specified by: value in interface FieldUnivariateFunction
        
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
    A collection of static methods that operate on or return polynomials.
    """
    @staticmethod
    def createChebyshevPolynomial(degree: int) -> PolynomialFunction:
        """
        Create a Chebyshev polynomial of the first kind.
        
        Chebyshev_polynomials are orthogonal polynomials. They can be defined by the following recurrence relations:
        
        \( T_0(x) = 1 \\ T_1(x) = x \\ T_{k+1}(x) = 2x T_k(x) - T_{k-1}(x) \)
        
        Parameters:
            degree (int): degree of the polynomial
        
        Returns:
            Chebyshev polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createHermitePolynomial(degree: int) -> PolynomialFunction:
        """
        Create a Hermite polynomial.
        
        `Hermite polynomials <http://mathworld.wolfram.com/HermitePolynomial.html>` are orthogonal polynomials. They can be defined by the following recurrence relations:
        
        \( H_0(x) = 1 \\ H_1(x) = 2x \\ H_{k+1}(x) = 2x H_k(X) - 2k H_{k-1}(x) \)
        
        Parameters:
            degree (int): degree of the polynomial
        
        Returns:
            Hermite polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createJacobiPolynomial(degree: int, v: int, w: int) -> PolynomialFunction:
        """
        Create a Jacobi polynomial.
        
        `Jacobi polynomials <http://mathworld.wolfram.com/JacobiPolynomial.html>` are orthogonal polynomials. They can be defined by the following recurrence relations:
        
        \( P_0^{vw}(x) = 1 \\ P_{-1}^{vw}(x) = 0 \\ 2k(k + v + w)(2k + v + w - 2) P_k^{vw}(x) = \\ (2k + v + w - 1)[(2k + v + w)(2k + v + w - 2) x + v^2 - w^2] P_{k-1}^{vw}(x) \\ - 2(k + v - 1)(k + w - 1)(2k + v + w) P_{k-2}^{vw}(x) \)
        
        Parameters:
            degree (int): degree of the polynomial
            v (int): first exponent
            w (int): second exponent
        
        Returns:
            Jacobi polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createLaguerrePolynomial(degree: int) -> PolynomialFunction:
        """
        Create a Laguerre polynomial.
        
        `Laguerre polynomials <http://mathworld.wolfram.com/LaguerrePolynomial.html>` are orthogonal polynomials. They can be defined by the following recurrence relations:
        
        \( L_0(x) = 1 \\ L_1(x) = 1 - x \\ (k+1) L_{k+1}(x) = (2k + 1 - x) L_k(x) - k L_{k-1}(x) \)
        
        Parameters:
            degree (int): degree of the polynomial
        
        Returns:
            Laguerre polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def createLegendrePolynomial(degree: int) -> PolynomialFunction:
        """
        Create a Legendre polynomial.
        
        `Legendre polynomials <http://mathworld.wolfram.com/LegendrePolynomial.html>` are orthogonal polynomials. They can be defined by the following recurrence relations:
        
        \( P_0(x) = 1 \\ P_1(x) = x \\ (k+1) P_{k+1}(x) = (2k+1) x P_k(x) - k P_{k-1}(x) \)
        
        Parameters:
            degree (int): degree of the polynomial
        
        Returns:
            Legendre polynomial of specified degree
        
        
        """
        ...
    @staticmethod
    def shift(coefficients: typing.Union[typing.List[float], jpype.JArray], shift: float) -> typing.MutableSequence[float]:
        """
        Compute the coefficients of the polynomial \(P_s(x)\) whose values at point x will be the same as the those from the original polynomial \(P(x)\) when computed at x + shift.
        
        More precisely, let \(\Delta = \) shift and let \(P_s(x) = P(x + \Delta)\). The returned array consists of the coefficients of \(P_s\). So if \(a_0..., a_{n-1}\) are the coefficients of \(P\), then the returned array \(b_0..., b_{n-1}\) satisfies the identity \(\sum_{i=0}^{n-1} b_i x^i = \sum_{i=0}^{n-1} a_i (x + \Delta)^i\) for all \(x\).
        
        Parameters:
            coefficients (double[]): Coefficients of the original polynomial.
            shift (double): Shift value.
        
        Returns:
            the coefficients \(b_i\) of the shifted polynomial.
        
        
        """
        ...

_SmoothStepFactory__FieldSmoothStepFunction__T = typing.TypeVar('_SmoothStepFactory__FieldSmoothStepFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class SmoothStepFactory:
    """
    Smoothstep function factory.
    
    It allows for quick creation of common and generic smoothstep functions as defined Smoothstep.
    """
    @staticmethod
    def checkBetweenZeroAndOneIncluded(input: float) -> None:
        """
        Check that input is between [0:1].
        
        Parameters:
            input (double): input to be checked
        
        Raises:
            MathIllegalArgumentException: if input is not between [0:1]
        
        
        """
        ...
    _getClamp_0__T = typing.TypeVar('_getClamp_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getClamp(field: org.hipparchus.Field[_getClamp_0__T]) -> 'SmoothStepFactory.FieldSmoothStepFunction'[_getClamp_0__T]:
        """
        Get the SmoothStepFunction.
        
        Parameters:
            field (Field<T> field): field of the element
        
        Returns:
            clamping smoothstep function
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getClamp() -> 'SmoothStepFactory.SmoothStepFunction':
        """
        Get the SmoothStepFunction.
        
        Returns:
            clamping smoothstep function
        
        """
        ...
    _getCubic_0__T = typing.TypeVar('_getCubic_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getCubic(field: org.hipparchus.Field[_getCubic_0__T]) -> 'SmoothStepFactory.FieldSmoothStepFunction'[_getCubic_0__T]:
        """
        Get the SmoothStepFunction.
        
        Parameters:
            field (Field<T> field): field of the element
        
        Returns:
            cubic smoothstep function
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getCubic() -> 'SmoothStepFactory.SmoothStepFunction':
        """
        Get the SmoothStepFunction.
        
        Returns:
            cubic smoothstep function
        
        """
        ...
    _getFieldGeneralOrder__T = typing.TypeVar('_getFieldGeneralOrder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getFieldGeneralOrder(field: org.hipparchus.Field[_getFieldGeneralOrder__T], N: int) -> 'SmoothStepFactory.FieldSmoothStepFunction'[_getFieldGeneralOrder__T]:
        """
        Create a SmoothStepFunction of order 2N + 1.
        
        It uses the general smoothstep equation presented Smoothstep : $S_{N}(x) = \sum_{n=0}^{N} \begin{pmatrix} -N-1 \\ n \end{pmatrix} \begin{pmatrix} 2N+1 \\ N-n \end{pmatrix} x^{N+n+1}$
        
        Parameters:
            field (Field<T> field): field of the element
            N (int): determines the order of the output smoothstep function (=2N + 1)
        
        Returns:
            smoothstep function of order 2N + 1
        
        
        """
        ...
    @staticmethod
    def getGeneralOrder(N: int) -> 'SmoothStepFactory.SmoothStepFunction':
        """
        Create a SmoothStepFunction of order 2N + 1.
        
        It uses the general smoothstep equation presented Smoothstep : $S_{N}(x) = \sum_{n=0}^{N} \begin{pmatrix} -N-1 \\ n \end{pmatrix} \begin{pmatrix} 2N+1 \\ N-n \end{pmatrix} x^{N+n+1}$
        
        Parameters:
            N (int): determines the order of the output smoothstep function (=2N + 1)
        
        Returns:
            smoothstep function of order 2N + 1
        
        
        """
        ...
    _getQuadratic_0__T = typing.TypeVar('_getQuadratic_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getQuadratic(field: org.hipparchus.Field[_getQuadratic_0__T]) -> 'SmoothStepFactory.FieldSmoothStepFunction'[_getQuadratic_0__T]:
        """
        Get the SmoothStepFunction.
        
        Parameters:
            field (Field<T> field): field of the element
        
        Returns:
            clamping smoothstep function
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getQuadratic() -> 'SmoothStepFactory.SmoothStepFunction':
        """
        Get the SmoothStepFunction.
        
        Returns:
            clamping smoothstep function
        
        """
        ...
    _getQuintic_0__T = typing.TypeVar('_getQuintic_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getQuintic(field: org.hipparchus.Field[_getQuintic_0__T]) -> 'SmoothStepFactory.FieldSmoothStepFunction'[_getQuintic_0__T]:
        """
        Get the SmoothStepFunction.
        
        Parameters:
            field (Field<T> field): field of the element
        
        Returns:
            quintic smoothstep function
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getQuintic() -> 'SmoothStepFactory.SmoothStepFunction':
        """
        Get the SmoothStepFunction.
        
        Returns:
            quintic smoothstep function
        
        """
        ...
    class FieldSmoothStepFunction(FieldPolynomialFunction[_SmoothStepFactory__FieldSmoothStepFunction__T], typing.Generic[_SmoothStepFactory__FieldSmoothStepFunction__T]):
        @typing.overload
        def value(self, double: float) -> _SmoothStepFactory__FieldSmoothStepFunction__T: ...
        @typing.overload
        def value(self, double: float, double2: float, t: _SmoothStepFactory__FieldSmoothStepFunction__T) -> _SmoothStepFactory__FieldSmoothStepFunction__T: ...
        @typing.overload
        def value(self, t: _SmoothStepFactory__FieldSmoothStepFunction__T) -> _SmoothStepFactory__FieldSmoothStepFunction__T: ...
    class QuadraticSmoothStepFunction(org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction):
        _value_2__T = typing.TypeVar('_value_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        _value_3__T = typing.TypeVar('_value_3__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
        @typing.overload
        def value(self, double: float) -> float: ...
        @typing.overload
        def value(self, double: float, double2: float, double3: float) -> float: ...
        @typing.overload
        def value(self, t: _value_2__T) -> _value_2__T: ...
        @typing.overload
        def value(self, t: _value_3__T) -> _value_3__T: ...
    class SmoothStepFunction(PolynomialFunction):
        _value_2__T = typing.TypeVar('_value_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        _value_3__T = typing.TypeVar('_value_3__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
        @typing.overload
        def value(self, double: float) -> float: ...
        @typing.overload
        def value(self, double: float, double2: float, double3: float) -> float: ...
        @typing.overload
        def value(self, t: _value_2__T) -> _value_2__T: ...
        @typing.overload
        def value(self, t: _value_3__T) -> _value_3__T: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.polynomials")``.

    FieldPolynomialFunction: typing.Type[FieldPolynomialFunction]
    FieldPolynomialFunctionLagrangeForm: typing.Type[FieldPolynomialFunctionLagrangeForm]
    FieldPolynomialSplineFunction: typing.Type[FieldPolynomialSplineFunction]
    JacobiKey: typing.Type[JacobiKey]
    PolynomialFunction: typing.Type[PolynomialFunction]
    PolynomialFunctionLagrangeForm: typing.Type[PolynomialFunctionLagrangeForm]
    PolynomialFunctionNewtonForm: typing.Type[PolynomialFunctionNewtonForm]
    PolynomialSplineFunction: typing.Type[PolynomialSplineFunction]
    PolynomialsUtils: typing.Type[PolynomialsUtils]
    SmoothStepFactory: typing.Type[SmoothStepFactory]
