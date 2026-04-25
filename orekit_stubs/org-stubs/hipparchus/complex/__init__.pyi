
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.text
import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.integration
import org.hipparchus.util
import typing



class Complex(org.hipparchus.CalculusFieldElement['Complex'], java.lang.Comparable['Complex'], java.io.Serializable):
    """
    implements CalculusFieldElement<Complex>, Comparable<Complex>, Serializable
    
    Representation of a Complex number, i.e. a number which has both a real and imaginary part.
    
    Implementations of arithmetic operations handle NaN and infinite values according to the rules for Double, i.e. equals is an equivalence relation for all instances that have a NaN in either real or imaginary part, e.g. the following are considered equal:
    
      - 1 + NaNi
      - NaN + i
      - NaN + NaNi
    
    Note that this contradicts the IEEE-754 standard for floating point numbers (according to which the test x == x must fail if x is NaN). The method equals in Precision conforms with IEEE-754 while this class conforms with the standard behavior for Java object types.
    
          - serialized
    """
    I: typing.ClassVar['Complex'] = ...
    """
    The square root of -1. A number representing "0.0 + 1.0i".
    """
    MINUS_I: typing.ClassVar['Complex'] = ...
    """
    The square root of -1. A number representing "0.0 - 1.0i".
    
    Since:
        1.7
    
    
    """
    NaN: typing.ClassVar['Complex'] = ...
    """
    A complex number representing "NaN + NaNi".
    """
    INF: typing.ClassVar['Complex'] = ...
    """
    A complex number representing "+INF + INFi"
    """
    ONE: typing.ClassVar['Complex'] = ...
    """
    A complex number representing "1.0 + 0.0i".
    """
    MINUS_ONE: typing.ClassVar['Complex'] = ...
    """
    A complex number representing "-1.0 + 0.0i".
    
    Since:
        1.7
    
    
    """
    ZERO: typing.ClassVar['Complex'] = ...
    """
    A complex number representing "0.0 + 0.0i".
    """
    PI: typing.ClassVar['Complex'] = ...
    """
    A complex number representing "π + 0.0i".
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def abs(self) -> 'Complex':
        """
        Return the absolute value of this complex number. Returns NaN if either real or imaginary part is NaN and POSITIVE_INFINITY if neither part is NaN, but at least one part is infinite.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            the norm.
        
        Since:
            2.0
        
        
        """
        ...
    def acos(self) -> 'Complex':
        """
        Compute the ` inverse cosine <http://mathworld.wolfram.com/InverseCosine.html>` of this complex number. Implements the formula:
        
        acos(z) = -i (log(z + i (sqrt(1 - z<sup>2</sup>)))) Returns NaN if either real or imaginary part of the input argument is NaN or infinite.
        
        Specified by: acos in interface CalculusFieldElement
        
        Returns:
            the inverse cosine of this complex number.
        
        
        """
        ...
    def acosh(self) -> 'Complex':
        """
        Inverse hyperbolic cosine operation.
        
        Branch cuts are on the real axis, below +1.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    def add(self, addend: float) -> 'Complex':
        """
        Specified by: add in interface CalculusFieldElement
        
        Parameters:
            addend (double): Value to be added to this Complex.
        
        Returns:
            this + addend.
        
              - add
        
        
        
        """
        ...
    @typing.overload
    def add(self, complex: 'Complex') -> 'Complex': ...
    def asin(self) -> 'Complex':
        """
        Compute the ` inverse sine <http://mathworld.wolfram.com/InverseSine.html>` of this complex number. Implements the formula:
        
        asin(z) = -i (log(sqrt(1 - z<sup>2</sup>) + iz))
        
        Returns NaN if either real or imaginary part of the input argument is NaN or infinite.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            the inverse sine of this complex number.
        
        
        """
        ...
    def asinh(self) -> 'Complex':
        """
        Inverse hyperbolic sine operation.
        
        Branch cuts are on the imaginary axis, above +i and below -i.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        Since:
            1.7
        
        
        """
        ...
    def atan(self) -> 'Complex':
        """
        Compute the ` inverse tangent <http://mathworld.wolfram.com/InverseTangent.html>` of this complex number. Implements the formula:
        
        atan(z) = (i/2) log((1 - iz)/(1 + iz))
        
        Returns NaN if either real or imaginary part of the input argument is NaN or infinite.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            the inverse tangent of this complex number
        
        
        """
        ...
    def atan2(self, x: 'Complex') -> 'Complex':
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (Complex): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        Since:
            1.7
        
        
        """
        ...
    def atanh(self) -> 'Complex':
        """
        Inverse hyperbolic tangent operation.
        
        Branch cuts are on the real axis, above +1 and below -1.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        Since:
            1.7
        
        
        """
        ...
    def cbrt(self) -> 'Complex':
        """
        Cubic root.
        
        This implementation compute the principal cube root by using a branch cut along real negative axis.
        
        Specified by: cbrt in interface CalculusFieldElement
        
        Returns:
            cubic root of the instance
        
        Since:
            1.7
        
        
        """
        ...
    def ceil(self) -> 'Complex':
        """
        Get the smallest whole number larger than instance.
        
        Specified by: ceil in interface CalculusFieldElement
        
        Returns:
            ceil(this)
        
        Since:
            1.7
        
        
        """
        ...
    def compareTo(self, complex: 'Complex') -> int:
        """
        Comparison us performed using real ordering as the primary sort order and imaginary ordering as the secondary sort order.
        
        Specified by: compareTo in interface Comparable
        
        Since:
            3.0
        
        
        """
        ...
    def conjugate(self) -> 'Complex':
        """
        Returns the conjugate of this complex number. The conjugate of a + bi is a - bi.
        
        NaN is returned if either the real or imaginary part of this Complex number equals NaN.
        
        If the imaginary part is infinite, and the real part is not NaN, the returned value has infinite imaginary part of the opposite sign, e.g. the conjugate of 1 + POSITIVE_INFINITY i is 1 - NEGATIVE_INFINITY i.
        
        Returns:
            the conjugate of this Complex object.
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'Complex':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        The signs of real and imaginary parts are copied independently.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            z (Complex): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Since:
            1.7
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            r (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    def copySign(self, complex: 'Complex') -> 'Complex': ...
    def cos(self) -> 'Complex':
        """
        Compute the ` cosine <http://mathworld.wolfram.com/Cosine.html>` of this complex number. Implements the formula:
        
        cos(a + bi) = cos(a)cosh(b) - sin(a)sinh(b)i
        
        where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns NaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           cos(1 ± INFINITY i) = 1 ∓ INFINITY i
           cos(±INFINITY + i) = NaN + NaN i
           cos(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            the cosine of this complex number.
        
        
        """
        ...
    def cosh(self) -> 'Complex':
        """
        Compute the ` hyperbolic cosine <http://mathworld.wolfram.com/HyperbolicCosine.html>` of this complex number. Implements the formula:
        
           cosh(a + bi) = cosh(a)cos(b) + sinh(a)sin(b)i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns NaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           cosh(1 ± INFINITY i) = NaN + NaN i
           cosh(±INFINITY + i) = INFINITY ± INFINITY i
           cosh(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: cosh in interface CalculusFieldElement
        
        Returns:
            the hyperbolic cosine of this complex number.
        
        
        """
        ...
    @typing.overload
    def divide(self, divisor: float) -> 'Complex':
        """
        Specified by: divide in interface CalculusFieldElement
        
        Parameters:
            divisor (double): Value by which this Complex is to be divided.
        
        Returns:
            this / divisor.
        
              - divide
        
        
        
        """
        ...
    @typing.overload
    def divide(self, complex: 'Complex') -> 'Complex': ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
        Test for equality with another object. If both the real and imaginary parts of two complex numbers are exactly the same, and neither is NaN, the two Complex objects are considered to be equal. The behavior is the same as for JDK's equals:
        
          - All NaN values are considered to be equal, i.e, if either (or both) real and imaginary parts of the complex
            number are equal to NaN, the complex number is equal to NaN.
          -         Instances constructed with different representations of zero (i.e. either "0" or "-0") are not considered to be equal.
        
        Overrides: equals in class Object
        
        Parameters:
            other (Object): Object to test for equality with this instance.
        
        Returns:
            true if the objects are equal, false if object is null, not an instance of Complex, or
            not equal to this instance.
        
        Test for the floating-point equality between Complex objects. It returns true if both arguments are equal or within the range of allowed error (inclusive).
        
        Parameters:
            x (Complex): First value (cannot be null).
            y (Complex): Second value (cannot be null).
            maxUlps (int): (maxUlps - 1) is the number of floating point values between the real (resp. imaginary) parts of x and
                y.
        
        Returns:
            true if there are fewer than maxUlps floating point values between the real (resp. imaginary) parts of
            x and y.
        
              - equals
        
        Returns true iff the values are equal as defined by equals.
        
        Parameters:
            x (Complex): First value (cannot be null).
            y (Complex): Second value (cannot be null).
        
        Returns:
            true if the values are equal.
        
        Returns true if, both for the real part and for the imaginary part, there is no double value strictly between the arguments or the difference between them is within the range of allowed error (inclusive). Returns false if either of the arguments is NaN.
        
        Parameters:
            x (Complex): First value (cannot be null).
            y (Complex): Second value (cannot be null).
            eps (double): Amount of allowed absolute error.
        
        Returns:
            true if the values are two adjacent floating point numbers or they are within range of each other.
        
              - equals
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(complex: 'Complex', complex2: 'Complex') -> bool: ...
    @typing.overload
    @staticmethod
    def equals(complex: 'Complex', complex2: 'Complex', double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(complex: 'Complex', complex2: 'Complex', int: int) -> bool: ...
    @staticmethod
    def equalsWithRelativeTolerance(x: 'Complex', y: 'Complex', eps: float) -> bool:
        """
        Returns true if, both for the real part and for the imaginary part, there is no double value strictly between the arguments or the relative difference between them is smaller or equal to the given tolerance. Returns false if either of the arguments is NaN.
        
        Parameters:
            x (Complex): First value (cannot be null).
            y (Complex): Second value (cannot be null).
            eps (double): Amount of allowed relative error.
        
        Returns:
            true if the values are two adjacent floating point numbers or they are within range of each other.
        
              - equalsWithRelativeTolerance
        
        
        
        """
        ...
    def exp(self) -> 'Complex':
        """
        Compute the ` exponential function <http://mathworld.wolfram.com/ExponentialFunction.html>` of this complex number. Implements the formula:
        
           exp(a + bi) = exp(a)cos(b) + exp(a)sin(b)i where the (real) functions on the right-hand side are exp p}, cos, and sin.
        
        Returns NaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           exp(1 ± INFINITY i) = NaN + NaN i
           exp(INFINITY + i) = INFINITY + INFINITY i
           exp(-INFINITY + i) = 0 + 0i
           exp(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            this``.
        
        
        """
        ...
    def expm1(self) -> 'Complex':
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        Since:
            1.7
        
        
        """
        ...
    def floor(self) -> 'Complex':
        """
        Get the largest whole number smaller than instance.
        
        Specified by: floor in interface CalculusFieldElement
        
        Returns:
            floor(this)
        
        Since:
            1.7
        
        
        """
        ...
    def getAddendum(self) -> 'Complex':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getArgument(self) -> float:
        """
        Compute the argument of this complex number. The argument is the angle phi between the positive real axis and the point representing this number in the complex plane. The value returned is between -PI (not inclusive) and PI (inclusive), with negative values returned for numbers with negative imaginary parts.
        
        If either real or imaginary part (or both) is NaN, NaN is returned. Infinite parts are handled as atan2 handles them, essentially treating finite parts as zero in the presence of an infinite coordinate and returning a multiple of pi/4 depending on the signs of the infinite parts. See the javadoc for atan2 for full details.
        
        Returns:
            the argument of this.
        
        
        """
        ...
    def getField(self) -> 'ComplexField':
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getImaginary(self) -> float:
        """
        Access the imaginary part.
        
        Returns:
            the imaginary part.
        
        
        """
        ...
    def getImaginaryPart(self) -> float:
        """
        Access the imaginary part.
        
        Returns:
            the imaginary part.
        
        Since:
            2.0
        
        
        """
        ...
    def getPi(self) -> 'Complex':
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getReal(self) -> float:
        """
        Access the real part.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            the real part.
        
        
        """
        ...
    def getRealPart(self) -> float:
        """
        Access the real part.
        
        Returns:
            the real part.
        
        Since:
            2.0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the complex number. Any NaN value in real or imaginary part produces the same hash code .
        
        Overrides: hashCode in class Object
        
        Returns:
            a hash code value for this object.
        
        
        """
        ...
    def hypot(self, y: 'Complex') -> 'Complex':
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (Complex): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        Since:
            1.7
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Checks whether either the real or imaginary part of this complex number takes an infinite value (either POSITIVE_INFINITY or NEGATIVE_INFINITY) and neither part is NaN.
        
        Specified by: isInfinite in interface CalculusFieldElement
        
        Returns:
            true if one or both parts of this complex number are infinite and neither part is NaN.
        
        
        """
        ...
    def isMathematicalInteger(self) -> bool:
        """
        Check whether the instance is an integer (i.e. imaginary part is zero and real part has no fractional part).
        
        Returns:
            true if imaginary part is zero and real part has no fractional part
        
        Since:
            1.7
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Checks whether either or both parts of this complex number is NaN.
        
        Specified by: isNaN in interface CalculusFieldElement
        
        Returns:
            true if either or both parts of this complex number is NaN; false otherwise.
        
        
        """
        ...
    def isReal(self) -> bool:
        """
        Check whether the instance is real (i.e. imaginary part is zero).
        
        Returns:
            true if imaginary part is zero
        
        Since:
            1.7
        
        
        """
        ...
    def isZero(self) -> bool:
        """
        Check if an element is semantically equal to zero.
        
        The default implementation simply calls getZero()). However, this may need to be overridden in some cases as due to compatibility with hashCode() some classes implements equals(Object) in such a way that -0.0 and +0.0 are different, which may be a problem. It prevents for example identifying a diagonal element is zero and should be avoided when doing partial pivoting in LU decomposition.
        
        This implementation considers +0.0 and -0.0 to be equal for both real and imaginary components.
        
        Specified by: isZero in interface FieldElement
        
        Returns:
            true if the element is semantically equal to zero
        
        Since:
            1.8
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, complex: 'Complex', double2: float, complex2: 'Complex') -> 'Complex':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Complex): first factor of the first term
            b1 (Complex): second factor of the first term
            a2 (Complex): first factor of the second term
            b2 (Complex): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Since:
            1.7
        
              - linearCombination
              - linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Complex): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Complex): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Since:
            1.7
        
              - linearCombination
              - linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Complex): first factor of the first term
            b1 (Complex): second factor of the first term
            a2 (Complex): first factor of the second term
            b2 (Complex): second factor of the second term
            a3 (Complex): first factor of the third term
            b3 (Complex): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Since:
            1.7
        
              - linearCombination
              - linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Complex): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Complex): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Complex): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Since:
            1.7
        
              - linearCombination
              - linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Complex): first factor of the first term
            b1 (Complex): second factor of the first term
            a2 (Complex): first factor of the second term
            b2 (Complex): second factor of the second term
            a3 (Complex): first factor of the third term
            b3 (Complex): second factor of the third term
            a4 (Complex): first factor of the fourth term
            b4 (Complex): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Since:
            1.7
        
              - linearCombination
              - linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Complex): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Complex): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Complex): second factor of the third term
            a4 (double): first factor of the fourth term
            b4 (Complex): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Since:
            1.7
        
              - linearCombination
              - linearCombination
        
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, complex: 'Complex', double2: float, complex2: 'Complex', double3: float, complex3: 'Complex') -> 'Complex': ...
    @typing.overload
    def linearCombination(self, double: float, complex: 'Complex', double2: float, complex2: 'Complex', double3: float, complex3: 'Complex', double4: float, complex4: 'Complex') -> 'Complex': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], complexArray: typing.Union[typing.List['Complex'], jpype.JArray]) -> 'Complex': ...
    @typing.overload
    def linearCombination(self, complex: 'Complex', complex2: 'Complex', complex3: 'Complex', complex4: 'Complex') -> 'Complex': ...
    @typing.overload
    def linearCombination(self, complex: 'Complex', complex2: 'Complex', complex3: 'Complex', complex4: 'Complex', complex5: 'Complex', complex6: 'Complex') -> 'Complex': ...
    @typing.overload
    def linearCombination(self, complex: 'Complex', complex2: 'Complex', complex3: 'Complex', complex4: 'Complex', complex5: 'Complex', complex6: 'Complex', complex7: 'Complex', complex8: 'Complex') -> 'Complex': ...
    @typing.overload
    def linearCombination(self, complexArray: typing.Union[typing.List['Complex'], jpype.JArray], complexArray2: typing.Union[typing.List['Complex'], jpype.JArray]) -> 'Complex': ...
    def log(self) -> 'Complex':
        """
        Compute the ` natural logarithm <http://mathworld.wolfram.com/NaturalLogarithm.html>` of this complex number. Implements the formula:
        
           log(a + bi) = ln(|a + bi|) + arg(a + bi)i where ln on the right hand side is log, |a + bi| is the modulus, abs, and arg(a + bi) =atan2(b, a).
        
        Returns NaN if either real or imaginary part of the input argument is NaN. Infinite (or critical) values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           log(1 ± INFINITY i) = INFINITY ± (π/2)i
           log(INFINITY + i) = INFINITY + 0i
           log(-INFINITY + i) = INFINITY + πi
           log(INFINITY ± INFINITY i) = INFINITY ± (π/4)i
           log(-INFINITY ± INFINITY i) = INFINITY ± (3π/4)i
           log(0 + 0i) = -INFINITY + 0i
          
         
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            the value ln   this, the natural logarithm of this.
        
        
        """
        ...
    def log10(self) -> 'Complex':
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Returns:
            base 10 logarithm of the instance
        
        Since:
            1.7
        
        
        """
        ...
    def log1p(self) -> 'Complex':
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Complex':
        """
        Returns a Complex whose value is this * factor, with factor interpreted as a integer number.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            factor (int): value to be multiplied by this Complex.
        
        Returns:
            this * factor.
        
              - multiply
        
        Returns a Complex whose value is this * factor, with factor interpreted as a real number.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Parameters:
            factor (double): value to be multiplied by this Complex.
        
        Returns:
            this * factor.
        
              - multiply
        
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'Complex': ...
    @typing.overload
    def multiply(self, complex: 'Complex') -> 'Complex': ...
    def multiplyMinusI(self) -> 'Complex':
        """
        Compute this *- -i.
        
        Returns:
            this * i
        
        Since:
            2.0
        
        
        """
        ...
    def multiplyPlusI(self) -> 'Complex':
        """
        Compute this * i.
        
        Returns:
            this * i
        
        Since:
            2.0
        
        
        """
        ...
    def negate(self) -> 'Complex':
        """
        Returns a Complex whose value is (-this). Returns NaN if either real or imaginary part of this Complex number is NaN.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            -this.
        
        
        """
        ...
    def newInstance(self, realPart: float) -> 'Complex':
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            realPart (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    def norm(self) -> float:
        """
        norm.
        
        Specified by: norm in interface CalculusFieldElement
        
        Returns:
            norm(this)
        
        
        """
        ...
    def nthRoot(self, n: int) -> java.util.List['Complex']:
        """
        Computes the n-th roots of this complex number. The nth roots are defined by the formula:
        
           z :sub:`k`  = abs :sup:`1/n`  (cos(phi + 2πk/n) + i (sin(phi + 2πk/n)) for , n-1, where abs and phi are respectively the abs and getArgument of this complex number.
        
        If one or both parts of this complex number is NaN, a list with just one element, NaN is returned. if neither part is NaN, but at least one part is infinite, the result is a one-element list containing INF.
        
        Parameters:
            n (int): Degree of root.
        
        Returns:
            a List of all n-th roots of this.
        
        Raises:
            MathIllegalArgumentException: if n <= 0.
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'Complex':
        """
        Returns of value of this complex number raised to the power of x.
        
        If x has an integer value, returns pow, if this is real and pow with the corresponding real arguments would return a finite number (neither NaN nor infinite), then returns the same value converted to Complex, with the same special cases. In all other cases real cases, implements y :sup:`x` = exp(x·log(y)).
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            x (double): exponent to which this Complex is to be raised.
        
        Returns:
            x``.
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'Complex': ...
    @typing.overload
    def pow(self, complex: 'Complex') -> 'Complex': ...
    def reciprocal(self) -> 'Complex':
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'Complex':
        """
        IEEE remainder operator.
        
        for complex numbers, the integer n corresponding to divide(a) is a Gaussian_integer.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        Since:
            1.7
        
        IEEE remainder operator.
        
        for complex numbers, the integer n corresponding to divide(a) is a Gaussian_integer.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (Complex): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    def remainder(self, complex: 'Complex') -> 'Complex': ...
    def rint(self) -> 'Complex':
        """
        Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
        Specified by: rint in interface CalculusFieldElement
        
        Returns:
            a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        Since:
            1.7
        
        
        """
        ...
    def rootN(self, n: int) -> 'Complex':
        """
        N :sup:`th` root.
        
        This implementation compute the principal n :sup:`th` root by using a branch cut along real negative axis.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        Since:
            1.7
        
        
        """
        ...
    def scalb(self, n: int) -> 'Complex':
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        Since:
            1.7
        
        
        """
        ...
    def sign(self) -> 'Complex':
        """
        Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
        Specified by: sign in interface CalculusFieldElement
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        Since:
            2.0
        
        
        """
        ...
    def sin(self) -> 'Complex':
        """
        Compute the ` sine <http://mathworld.wolfram.com/Sine.html>` of this complex number. Implements the formula:
        
           sin(a + bi) = sin(a)cosh(b) + cos(a)sinh(b)i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns NaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           sin(1 ± INFINITY i) = 1 ± INFINITY i
           sin(±INFINITY + i) = NaN + NaN i
           sin(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            the sine of this complex number.
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['Complex']:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'Complex':
        """
        Compute the ` hyperbolic sine <http://mathworld.wolfram.com/HyperbolicSine.html>` of this complex number. Implements the formula:
        
           sinh(a + bi) = sinh(a)cos(b)) + cosh(a)sin(b)i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns NaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           sinh(1 ± INFINITY i) = NaN + NaN i
           sinh(±INFINITY + i) = ± INFINITY + INFINITY i
           sinh(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: sinh in interface CalculusFieldElement
        
        Returns:
            the hyperbolic sine of this.
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['Complex']:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'Complex':
        """
        Compute the ` square root <http://mathworld.wolfram.com/SquareRoot.html>` of this complex number. Implements the following algorithm to compute sqrt(a + bi):
        
          1.  Let t = sqrt((|a| + |a + bi|) / 2) 2. if  a ≥ 0 return t + (b/2t)i else return |b|/2t + sign(b)t i
        
        where
        
          - |a| =abs
          - |a + bi| =hypot
          - sign(b) =copySign
        
        The real part is therefore always nonnegative.
        
        Returns NaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           sqrt(1 ± ∞ i) = ∞ + NaN i
           sqrt(∞ + i) = ∞ + 0i
           sqrt(-∞ + i) = 0 + ∞ i
           sqrt(∞ ± ∞ i) = ∞ + NaN i
           sqrt(-∞ ± ∞ i) = NaN ± ∞ i
          
         
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            the square root of this with nonnegative real part.
        
        
        """
        ...
    def sqrt1z(self) -> 'Complex':
        """
        Compute the ` square root <http://mathworld.wolfram.com/SquareRoot.html>` of 2`` for this complex number. Computes the result directly as square())).
        
        Returns NaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        Returns:
            the square root of 2``.
        
        
        """
        ...
    def square(self) -> 'Complex':
        """
        Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, subtrahend: float) -> 'Complex':
        """
        Specified by: subtract in interface CalculusFieldElement
        
        Parameters:
            subtrahend (double): value to be subtracted from this Complex.
        
        Returns:
            this - subtrahend.
        
              - subtract
        
        
        
        """
        ...
    @typing.overload
    def subtract(self, complex: 'Complex') -> 'Complex': ...
    def tan(self) -> 'Complex':
        """
        Compute the ` tangent <http://mathworld.wolfram.com/Tangent.html>` of this complex number. Implements the formula:
        
           tan(a + bi) = sin(2a)/(cos(2a)+cosh(2b)) + [sinh(2b)/(cos(2a)+cosh(2b))]i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns NaN if either real or imaginary part of the input argument is NaN. Infinite (or critical) values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           tan(a ± INFINITY i) = 0 ± i
           tan(±INFINITY + bi) = NaN + NaN i
           tan(±INFINITY ± INFINITY i) = NaN + NaN i
           tan(±&pi;/2 + 0 i) = ±INFINITY + NaN i
          
         
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            the tangent of this.
        
        
        """
        ...
    def tanh(self) -> 'Complex':
        """
        Compute the ` hyperbolic tangent <http://mathworld.wolfram.com/HyperbolicTangent.html>` of this complex number. Implements the formula:
        
           tan(a + bi) = sinh(2a)/(cosh(2a)+cos(2b)) + [sin(2b)/(cosh(2a)+cos(2b))]i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns NaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           tanh(a ± INFINITY i) = NaN + NaN i
           tanh(±INFINITY + bi) = ±1 + 0 i
           tanh(±INFINITY ± INFINITY i) = NaN + NaN i
           tanh(0 + (π/2)i) = NaN + INFINITY i
          
         
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            the hyperbolic tangent of this.
        
        
        """
        ...
    def toDegrees(self) -> 'Complex':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'Complex':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: toString in class Object
        
        
        """
        ...
    def ulp(self) -> 'Complex':
        """
        Compute least significant bit (Unit in Last Position) for a number.
        
        Specified by: ulp in interface CalculusFieldElement
        
        Returns:
            ulp(this)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(double: float) -> 'Complex':
        """
        Create a complex number given the real and imaginary parts.
        
        Parameters:
            realPart (double): Real part.
            imaginaryPart (double): Imaginary part.
        
        Returns:
            a Complex instance.
        
        Create a complex number given only the real part.
        
        Parameters:
            realPart (double): Real part.
        
        Returns:
            a Complex instance.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(double: float, double2: float) -> 'Complex': ...

class ComplexComparator(java.util.Comparator[Complex], java.io.Serializable):
    """
    implements Comparator<Complex>, Serializable
    
    Comparator for Complex Numbers.
    
          - serialized
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def compare(self, o1: Complex, o2: Complex) -> int:
        """
        Compare two complex numbers, using real ordering as the primary sort order and imaginary ordering as the secondary sort order.
        
        Specified by: compare in interface Comparator
        
        Parameters:
            o1 (Complex): first complex number
            o2 (Complex): second complex number
        
        Returns:
            a negative value if o1 real part is less than o2 real part or if real parts are equal and o1 imaginary part is less than
            o2 imaginary part
        
        
        """
        ...

class ComplexField(org.hipparchus.Field[Complex], java.io.Serializable):
    """
    implements Field<Complex>, Serializable
    
    Representation of the complex numbers field.
    
    This class is a singleton.
    
          - Complex
          - serialized
    """
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: equals in class Object
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'ComplexField':
        """
        Get the unique instance.
        
        Returns:
            the unique instance
        
        
        """
        ...
    def getOne(self) -> Complex:
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Complex]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> Complex:
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class Object
        
        
        """
        ...

class ComplexFormat:
    """
    Formats a Complex number in cartesian format "Re(c) + Im(c)i". 'i' can be replaced with 'j' (or anything else), and the number format for both real and imaginary parts can be configured.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, string: str, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat): ...
    @typing.overload
    def format(self, double: float) -> str:
        """
        This method calls format.
        
        Parameters:
            c (Complex): Complex object to format.
        
        Returns:
            A formatted number in the form "Re(c) + Im(c)i".
        
        This method calls format.
        
        Parameters:
            c (Double): Double object to format.
        
        Returns:
            A formatted number.
        
        Formats a Complex object to produce a string.
        
        Parameters:
            complex (Complex): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        public StringBuffer format(Object obj, StringBuffer toAppendTo, FieldPosition pos) throws MathIllegalArgumentException
        
        Formats a object to produce a string. obj must be either a Complex object or a Number object. Any other type of object will result in an IllegalArgumentException being thrown.
        
        Parameters:
            obj (Object): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        Raises:
            MathIllegalArgumentException: is obj is not a valid type.
        
              - format
        
        
        
        """
        ...
    @typing.overload
    def format(self, complex: Complex) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, complex: Complex, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
        Get the set of locales for which complex formats are available.
        
        This is the same set as the NumberFormat set.
        
        Returns:
            available complex format locales.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getComplexFormat() -> 'ComplexFormat':
        """
        Returns:
            the default complex format.
        
        Since:
            1.4
        
        """
        ...
    @typing.overload
    @staticmethod
    def getComplexFormat(string: str, locale: java.util.Locale) -> 'ComplexFormat': ...
    @typing.overload
    @staticmethod
    def getComplexFormat(locale: java.util.Locale) -> 'ComplexFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the complex format specific to the given locale.
        
        Since:
            1.4
        
        public static ComplexFormat getComplexFormat(String imaginaryCharacter, Locale locale) throws MathIllegalArgumentException, NullArgumentException
        
        Returns the default complex format for the given locale.
        
        Parameters:
            imaginaryCharacter (String): Imaginary character.
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the complex format specific to the given locale.
        
        Raises:
            NullArgumentException: if imaginaryCharacter is null.
            MathIllegalArgumentException: if imaginaryCharacter is an empty string.
        
        Since:
            1.4
        
        
        """
        ...
    def getImaginaryCharacter(self) -> str:
        """
        Access the imaginaryCharacter.
        
        Returns:
            the imaginaryCharacter.
        
        
        """
        ...
    def getImaginaryFormat(self) -> java.text.NumberFormat:
        """
        Access the imaginaryFormat.
        
        Returns:
            the imaginaryFormat.
        
        
        """
        ...
    def getRealFormat(self) -> java.text.NumberFormat:
        """
        Access the realFormat.
        
        Returns:
            the realFormat.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Complex:
        """
        Parses a string to produce a Complex object.
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/ouput parsing parameter.
        
        Returns:
            the parsed Complex object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Complex: ...

class ComplexUnivariateIntegrator:
    """
    Wrapper to perform univariate complex integration using an underlying real integration algorithms.
    
    Since:
        2.0
    """
    def __init__(self, integrator: org.hipparchus.analysis.integration.UnivariateIntegrator):
        """
        Crate a complex integrator from a real integrator.
        
        Parameters:
            integrator (UnivariateIntegrator): underlying real integrator to use
        
        
        """
        ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[Complex], typing.Callable[[Complex], Complex]], complex: Complex, complex2: Complex) -> Complex: ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[Complex], typing.Callable[[Complex], Complex]], complex: Complex, *complex2: Complex) -> Complex: ...

class ComplexUtils:
    """
    Static implementations of common Complex utilities functions.
    """
    @staticmethod
    def convertToComplex(real: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[Complex]:
        """
        Convert an array of primitive doubles to an array of Complex objects.
        
        Parameters:
            real (double[]): Array of numbers to be converted to their Complex equivalent.
        
        Returns:
            an array of Complex objects.
        
        
        """
        ...
    _polar2Complex_1__T = typing.TypeVar('_polar2Complex_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def polar2Complex(double: float, double2: float) -> Complex: ...
    @typing.overload
    @staticmethod
    def polar2Complex(t: _polar2Complex_1__T, t2: _polar2Complex_1__T) -> 'FieldComplex'[_polar2Complex_1__T]: ...

_FieldComplex__T = typing.TypeVar('_FieldComplex__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldComplex(org.hipparchus.CalculusFieldElement['FieldComplex'[_FieldComplex__T]], typing.Generic[_FieldComplex__T]):
    """
    implements CalculusFieldElement<FieldComplex<T>>
    
    Representation of a Complex number, i.e. a number which has both a real and imaginary part.
    
    Implementations of arithmetic operations handle NaN and infinite values according to the rules for Double, i.e. equals is an equivalence relation for all instances that have a NaN in either real or imaginary part, e.g. the following are considered equal:
    
      - 1 + NaNi
      - NaN + i
      - NaN + NaNi
    
    Note that this contradicts the IEEE-754 standard for floating point numbers (according to which the test x == x must fail if x is NaN). The method equals in Precision conforms with IEEE-754 while this class conforms with the standard behavior for Java object types.
    
    Since:
        2.0
    """
    @typing.overload
    def __init__(self, t: _FieldComplex__T): ...
    @typing.overload
    def __init__(self, t: _FieldComplex__T, t2: _FieldComplex__T): ...
    def abs(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Return the absolute value of this complex number. Returns NaN if either real or imaginary part is NaN and POSITIVE_INFINITY if neither part is NaN, but at least one part is infinite.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            the absolute value.
        
        
        """
        ...
    def acos(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` inverse cosine <http://mathworld.wolfram.com/InverseCosine.html>` of this complex number. Implements the formula:
        
        acos(z) = -i (log(z + i (sqrt(1 - z<sup>2</sup>)))) Returns getNaN if either real or imaginary part of the input argument is NaN or infinite.
        
        Specified by: acos in interface CalculusFieldElement
        
        Returns:
            the inverse cosine of this complex number.
        
        
        """
        ...
    def acosh(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Inverse hyperbolic cosine operation.
        
        Branch cuts are on the real axis, below +1.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def add(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def add(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def asin(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` inverse sine <http://mathworld.wolfram.com/InverseSine.html>` of this complex number. Implements the formula:
        
        asin(z) = -i (log(sqrt(1 - z<sup>2</sup>) + iz))
        
        Returns getNaN if either real or imaginary part of the input argument is NaN or infinite.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            the inverse sine of this complex number.
        
        
        """
        ...
    def asinh(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Inverse hyperbolic sine operation.
        
        Branch cuts are on the imaginary axis, above +i and below -i.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` inverse tangent <http://mathworld.wolfram.com/InverseTangent.html>` of this complex number. Implements the formula:
        
        atan(z) = (i/2) log((1 - iz)/(1 + iz))
        
        Returns getNaN if either real or imaginary part of the input argument is NaN or infinite.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            the inverse tangent of this complex number
        
        
        """
        ...
    def atan2(self, x: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (FieldComplex<FieldComplex> x): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def atanh(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Inverse hyperbolic tangent operation.
        
        Branch cuts are on the real axis, above +1 and below -1.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Cubic root.
        
        This implementation compute the principal cube root by using a branch cut along real negative axis.
        
        Specified by: cbrt in interface CalculusFieldElement
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Get the smallest whole number larger than instance.
        
        Specified by: ceil in interface CalculusFieldElement
        
        Returns:
            ceil(this)
        
        
        """
        ...
    def conjugate(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Returns the conjugate of this complex number. The conjugate of a + bi is a - bi.
        
        getNaN is returned if either the real or imaginary part of this Complex number equals NaN.
        
        If the imaginary part is infinite, and the real part is not NaN, the returned value has infinite imaginary part of the opposite sign, e.g. the conjugate of 1 + POSITIVE_INFINITY i is 1 - NEGATIVE_INFINITY i.
        
        Returns:
            the conjugate of this Complex object.
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def copySign(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def cos(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` cosine <http://mathworld.wolfram.com/Cosine.html>` of this complex number. Implements the formula:
        
        cos(a + bi) = cos(a)cosh(b) - sin(a)sinh(b)i
        
        where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           cos(1 ± INFINITY i) = 1 ∓ INFINITY i
           cos(±INFINITY + i) = NaN + NaN i
           cos(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            the cosine of this complex number.
        
        
        """
        ...
    def cosh(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` hyperbolic cosine <http://mathworld.wolfram.com/HyperbolicCosine.html>` of this complex number. Implements the formula:
        
           cosh(a + bi) = cosh(a)cos(b) + sinh(a)sin(b)i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           cosh(1 ± INFINITY i) = NaN + NaN i
           cosh(±INFINITY + i) = INFINITY ± INFINITY i
           cosh(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: cosh in interface CalculusFieldElement
        
        Returns:
            the hyperbolic cosine of this complex number.
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def divide(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def divide(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    _equals_1__T = typing.TypeVar('_equals_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _equals_2__T = typing.TypeVar('_equals_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _equals_3__T = typing.TypeVar('_equals_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def equals(self, other: typing.Any) -> bool:
        """
        Test for equality with another object. If both the real and imaginary parts of two complex numbers are exactly the same, and neither is NaN, the two Complex objects are considered to be equal. The behavior is the same as for JDK's equals:
        
          - All NaN values are considered to be equal, i.e, if either (or both) real and imaginary parts of the complex
            number are equal to NaN, the complex number is equal to NaN.
          -         Instances constructed with different representations of zero (i.e. either "0" or "-0") are not considered to be equal.
        
        Overrides: equals in class Object
        
        Parameters:
            other (Object): Object to test for equality with this instance.
        
        Returns:
            true if the objects are equal, false if object is null, not an instance of Complex, or
            not equal to this instance.
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(x: 'FieldComplex'[_equals_1__T], y: 'FieldComplex'[_equals_1__T]) -> bool:
        """
        Returns true iff the values are equal as defined by equals.
        
        Parameters:
            x (FieldComplex<T> x): First value (cannot be null).
            y (FieldComplex<T> y): Second value (cannot be null).
        
        Returns:
            true if the values are equal.
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(fieldComplex: 'FieldComplex'[_equals_2__T], fieldComplex2: 'FieldComplex'[_equals_2__T], double: float) -> bool:
        """
        Test for the floating-point equality between Complex objects. It returns true if both arguments are equal or within the range of allowed error (inclusive).
        
        Parameters:
            x (FieldComplex<T> x): First value (cannot be null).
            y (FieldComplex<T> y): Second value (cannot be null).
            maxUlps (int): (maxUlps - 1) is the number of floating point values between the real (resp. imaginary) parts of x and
                y.
        
        Returns:
            true if there are fewer than maxUlps floating point values between the real (resp. imaginary) parts of
            x and y.
        
              - equals
        
        Returns true if, both for the real part and for the imaginary part, there is no T value strictly between the arguments or the difference between them is within the range of allowed error (inclusive). Returns false if either of the arguments is NaN.
        
        Parameters:
            x (FieldComplex<T> x): First value (cannot be null).
            y (FieldComplex<T> y): Second value (cannot be null).
            eps (double): Amount of allowed absolute error.
        
        Returns:
            true if the values are two adjacent floating point numbers or they are within range of each other.
        
              - equals
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(fieldComplex: 'FieldComplex'[_equals_3__T], fieldComplex2: 'FieldComplex'[_equals_3__T], int: int) -> bool: ...
    _equalsWithRelativeTolerance__T = typing.TypeVar('_equalsWithRelativeTolerance__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def equalsWithRelativeTolerance(x: 'FieldComplex'[_equalsWithRelativeTolerance__T], y: 'FieldComplex'[_equalsWithRelativeTolerance__T], eps: float) -> bool:
        """
        Returns true if, both for the real part and for the imaginary part, there is no T value strictly between the arguments or the relative difference between them is smaller or equal to the given tolerance. Returns false if either of the arguments is NaN.
        
        Parameters:
            x (FieldComplex<T> x): First value (cannot be null).
            y (FieldComplex<T> y): Second value (cannot be null).
            eps (double): Amount of allowed relative error.
        
        Returns:
            true if the values are two adjacent floating point numbers or they are within range of each other.
        
              - equalsWithRelativeTolerance
        
        
        
        """
        ...
    def exp(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` exponential function <http://mathworld.wolfram.com/ExponentialFunction.html>` of this complex number. Implements the formula:
        
           exp(a + bi) = exp(a)cos(b) + exp(a)sin(b)i where the (real) functions on the right-hand side are exp p}, cos, and sin.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           exp(1 ± INFINITY i) = NaN + NaN i
           exp(INFINITY + i) = INFINITY + INFINITY i
           exp(-INFINITY + i) = 0 + 0i
           exp(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            this``.
        
        
        """
        ...
    def expm1(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Get the largest whole number smaller than instance.
        
        Specified by: floor in interface CalculusFieldElement
        
        Returns:
            floor(this)
        
        
        """
        ...
    def getAddendum(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getArgument(self) -> _FieldComplex__T:
        """
        Compute the argument of this complex number. The argument is the angle phi between the positive real axis and the point representing this number in the complex plane. The value returned is between -PI (not inclusive) and PI (inclusive), with negative values returned for numbers with negative imaginary parts.
        
        If either real or imaginary part (or both) is NaN, NaN is returned. Infinite parts are handled as atan2 handles them, essentially treating finite parts as zero in the presence of an infinite coordinate and returning a multiple of pi/4 depending on the signs of the infinite parts. See the javadoc for atan2 for full details.
        
        Returns:
            the argument of this.
        
        
        """
        ...
    def getField(self) -> 'FieldComplexField'[_FieldComplex__T]:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    _getI__T = typing.TypeVar('_getI__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getI(field: org.hipparchus.Field[_getI__T]) -> 'FieldComplex'[_getI__T]:
        """
        Get the square root of -1.
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            number representing "0.0 + 1.0i"
        
        
        """
        ...
    def getImaginary(self) -> _FieldComplex__T:
        """
        Access the imaginary part.
        
        Returns:
            the imaginary part.
        
        
        """
        ...
    def getImaginaryPart(self) -> _FieldComplex__T:
        """
        Access the imaginary part.
        
        Returns:
            the imaginary part.
        
        
        """
        ...
    _getInf__T = typing.TypeVar('_getInf__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getInf(field: org.hipparchus.Field[_getInf__T]) -> 'FieldComplex'[_getInf__T]:
        """
        Get a complex number representing "+INF + INFi".
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            complex number representing "+INF + INFi"
        
        
        """
        ...
    _getMinusI__T = typing.TypeVar('_getMinusI__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getMinusI(field: org.hipparchus.Field[_getMinusI__T]) -> 'FieldComplex'[_getMinusI__T]:
        """
        Get the square root of -1.
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            number representing "0.0 _ 1.0i"
        
        
        """
        ...
    _getMinusOne__T = typing.TypeVar('_getMinusOne__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getMinusOne(field: org.hipparchus.Field[_getMinusOne__T]) -> 'FieldComplex'[_getMinusOne__T]:
        """
        Get a complex number representing "-1.0 + 0.0i".
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            complex number representing "-1.0 + 0.0i"
        
        
        """
        ...
    _getNaN__T = typing.TypeVar('_getNaN__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getNaN(field: org.hipparchus.Field[_getNaN__T]) -> 'FieldComplex'[_getNaN__T]:
        """
        Get a complex number representing "NaN + NaNi".
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            complex number representing "NaN + NaNi"
        
        
        """
        ...
    _getOne__T = typing.TypeVar('_getOne__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getOne(field: org.hipparchus.Field[_getOne__T]) -> 'FieldComplex'[_getOne__T]:
        """
        Get a complex number representing "1.0 + 0.0i".
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            complex number representing "1.0 + 0.0i"
        
        
        """
        ...
    def getPartsField(self) -> org.hipparchus.Field[_FieldComplex__T]:
        """
        Get the Field the real and imaginary parts belong to.
        
        Returns:
            Field the real and imaginary parts belong to
        
        
        """
        ...
    _getPi_1__T = typing.TypeVar('_getPi_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPi(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    @staticmethod
    def getPi(field: org.hipparchus.Field[_getPi_1__T]) -> 'FieldComplex'[_getPi_1__T]:
        """
        Get a complex number representing "π + 0.0i".
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            complex number representing "π + 0.0i
        
        public FieldComplex<FieldComplex> getPi()
        
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getReal(self) -> float:
        """
        Access the real part.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            the real part.
        
        
        """
        ...
    def getRealPart(self) -> _FieldComplex__T:
        """
        Access the real part.
        
        Returns:
            the real part.
        
        
        """
        ...
    _getZero__T = typing.TypeVar('_getZero__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getZero(field: org.hipparchus.Field[_getZero__T]) -> 'FieldComplex'[_getZero__T]:
        """
        Get a complex number representing "0.0 + 0.0i".
        
        Parameters:
            field (Field<T> field): field the complex components belong to
        
        Returns:
            complex number representing "0.0 + 0.0i
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the complex number. Any NaN value in real or imaginary part produces the same hash code .
        
        Overrides: hashCode in class Object
        
        Returns:
            a hash code value for this object.
        
        
        """
        ...
    def hypot(self, y: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (FieldComplex<FieldComplex> y): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Checks whether either the real or imaginary part of this complex number takes an infinite value (either POSITIVE_INFINITY or NEGATIVE_INFINITY) and neither part is NaN.
        
        Specified by: isInfinite in interface CalculusFieldElement
        
        Returns:
            true if one or both parts of this complex number are infinite and neither part is NaN.
        
        
        """
        ...
    def isMathematicalInteger(self) -> bool:
        """
        Check whether the instance is an integer (i.e. imaginary part is zero and real part has no fractional part).
        
        Returns:
            true if imaginary part is zero and real part has no fractional part
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Checks whether either or both parts of this complex number is NaN.
        
        Specified by: isNaN in interface CalculusFieldElement
        
        Returns:
            true if either or both parts of this complex number is NaN; false otherwise.
        
        
        """
        ...
    def isReal(self) -> bool:
        """
        Check whether the instance is real (i.e. imaginary part is zero).
        
        Returns:
            true if imaginary part is zero
        
        
        """
        ...
    def isZero(self) -> bool:
        """
        Check if an element is semantically equal to zero.
        
        The default implementation simply calls getZero()). However, this may need to be overridden in some cases as due to compatibility with hashCode() some classes implements equals(Object) in such a way that -0.0 and +0.0 are different, which may be a problem. It prevents for example identifying a diagonal element is zero and should be avoided when doing partial pivoting in LU decomposition.
        
        This implementation considers +0.0 and -0.0 to be equal for both real and imaginary components.
        
        Specified by: isZero in interface FieldElement
        
        Returns:
            true if the element is semantically equal to zero
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, fieldComplex: 'FieldComplex'[_FieldComplex__T], double2: float, fieldComplex2: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldComplex: 'FieldComplex'[_FieldComplex__T], double2: float, fieldComplex2: 'FieldComplex'[_FieldComplex__T], double3: float, fieldComplex3: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldComplex: 'FieldComplex'[_FieldComplex__T], double2: float, fieldComplex2: 'FieldComplex'[_FieldComplex__T], double3: float, fieldComplex3: 'FieldComplex'[_FieldComplex__T], double4: float, fieldComplex4: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], fieldComplexArray: typing.Union[typing.List['FieldComplex'[_FieldComplex__T]], jpype.JArray]) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def linearCombination(self, fieldComplex: 'FieldComplex'[_FieldComplex__T], fieldComplex2: 'FieldComplex'[_FieldComplex__T], fieldComplex3: 'FieldComplex'[_FieldComplex__T], fieldComplex4: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def linearCombination(self, fieldComplex: 'FieldComplex'[_FieldComplex__T], fieldComplex2: 'FieldComplex'[_FieldComplex__T], fieldComplex3: 'FieldComplex'[_FieldComplex__T], fieldComplex4: 'FieldComplex'[_FieldComplex__T], fieldComplex5: 'FieldComplex'[_FieldComplex__T], fieldComplex6: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def linearCombination(self, fieldComplex: 'FieldComplex'[_FieldComplex__T], fieldComplex2: 'FieldComplex'[_FieldComplex__T], fieldComplex3: 'FieldComplex'[_FieldComplex__T], fieldComplex4: 'FieldComplex'[_FieldComplex__T], fieldComplex5: 'FieldComplex'[_FieldComplex__T], fieldComplex6: 'FieldComplex'[_FieldComplex__T], fieldComplex7: 'FieldComplex'[_FieldComplex__T], fieldComplex8: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def linearCombination(self, fieldComplexArray: typing.Union[typing.List['FieldComplex'[_FieldComplex__T]], jpype.JArray], fieldComplexArray2: typing.Union[typing.List['FieldComplex'[_FieldComplex__T]], jpype.JArray]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def log(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` natural logarithm <http://mathworld.wolfram.com/NaturalLogarithm.html>` of this complex number. Implements the formula:
        
           log(a + bi) = ln(|a + bi|) + arg(a + bi)i where ln on the right hand side is log, |a + bi| is the modulus, abs, and arg(a + bi) =atan2(b, a).
        
        Returns getNaN if either real or imaginary part of the input argument is NaN. Infinite (or critical) values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           log(1 ± INFINITY i) = INFINITY ± (π/2)i
           log(INFINITY + i) = INFINITY + 0i
           log(-INFINITY + i) = INFINITY + πi
           log(INFINITY ± INFINITY i) = INFINITY ± (π/4)i
           log(-INFINITY ± INFINITY i) = INFINITY ± (3π/4)i
           log(0 + 0i) = -INFINITY + 0i
          
         
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            the value ln   this, the natural logarithm of this.
        
        
        """
        ...
    def log10(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def multiply(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def multiply(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def multiplyMinusI(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute this *- -i.
        
        Returns:
            this * i
        
        Since:
            2.0
        
        
        """
        ...
    def multiplyPlusI(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute this * i.
        
        Returns:
            this * i
        
        Since:
            2.0
        
        
        """
        ...
    def negate(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Returns a Complex whose value is (-this). Returns NaN if either real or imaginary part of this Complex number is NaN.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            -this.
        
        
        """
        ...
    def newInstance(self, realPart: float) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            realPart (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    def nthRoot(self, n: int) -> java.util.List['FieldComplex'[_FieldComplex__T]]:
        """
        Computes the n-th roots of this complex number. The nth roots are defined by the formula:
        
           z :sub:`k`  = abs :sup:`1/n`  (cos(phi + 2πk/n) + i (sin(phi + 2πk/n)) for , n-1, where abs and phi are respectively the abs and getArgument of this complex number.
        
        If one or both parts of this complex number is NaN, a list with just one element, getNaN is returned. if neither part is NaN, but at least one part is infinite, the result is a one-element list containing getInf.
        
        Parameters:
            n (int): Degree of root.
        
        Returns:
            a List of all n-th roots of this.
        
        Raises:
            MathIllegalArgumentException: if n <= 0.
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def pow(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def pow(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def reciprocal(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def remainder(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def rint(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
        Specified by: rint in interface CalculusFieldElement
        
        Returns:
            a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, n: int) -> 'FieldComplex'[_FieldComplex__T]:
        """
        N :sup:`th` root.
        
        This implementation compute the principal n :sup:`th` root by using a branch cut along real negative axis.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
        Specified by: sign in interface CalculusFieldElement
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` sine <http://mathworld.wolfram.com/Sine.html>` of this complex number. Implements the formula:
        
           sin(a + bi) = sin(a)cosh(b) + cos(a)sinh(b)i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           sin(1 ± INFINITY i) = 1 ± INFINITY i
           sin(±INFINITY + i) = NaN + NaN i
           sin(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            the sine of this complex number.
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldComplex'[_FieldComplex__T]]:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` hyperbolic sine <http://mathworld.wolfram.com/HyperbolicSine.html>` of this complex number. Implements the formula:
        
           sinh(a + bi) = sinh(a)cos(b)) + cosh(a)sin(b)i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           sinh(1 ± INFINITY i) = NaN + NaN i
           sinh(±INFINITY + i) = ± INFINITY + INFINITY i
           sinh(±INFINITY ± INFINITY i) = NaN + NaN i
          
         
        
        Specified by: sinh in interface CalculusFieldElement
        
        Returns:
            the hyperbolic sine of this.
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldComplex'[_FieldComplex__T]]:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` square root <http://mathworld.wolfram.com/SquareRoot.html>` of this complex number. Implements the following algorithm to compute sqrt(a + bi):
        
          1.  Let t = sqrt((|a| + |a + bi|) / 2) 2. if  a ≥ 0 return t + (b/2t)i else return |b|/2t + sign(b)t i
        
        where
        
          - |a| =abs
          - |a + bi| =hypot
          - sign(b) =copySign
        
        The real part is therefore always nonnegative.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN.
        
        Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           sqrt(1 ± ∞ i) = ∞ + NaN i
           sqrt(∞ + i) = ∞ + 0i
           sqrt(-∞ + i) = 0 + ∞ i
           sqrt(∞ ± ∞ i) = ∞ + NaN i
           sqrt(-∞ ± ∞ i) = NaN ± ∞ i
          
         
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            the square root of this with nonnegative real part.
        
        
        """
        ...
    def sqrt1z(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` square root <http://mathworld.wolfram.com/SquareRoot.html>` of 2`` for this complex number. Computes the result directly as square())).
        
        Returns getNaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        Returns:
            the square root of 2``.
        
        
        """
        ...
    def square(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Description copied from interface: square Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def subtract(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def subtract(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def tan(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` tangent <http://mathworld.wolfram.com/Tangent.html>` of this complex number. Implements the formula:
        
           tan(a + bi) = sin(2a)/(cos(2a)+cosh(2b)) + [sinh(2b)/(cos(2a)+cosh(2b))]i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN. Infinite (or critical) values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           tan(a ± INFINITY i) = 0 ± i
           tan(±INFINITY + bi) = NaN + NaN i
           tan(±INFINITY ± INFINITY i) = NaN + NaN i
           tan(±&pi;/2 + 0 i) = ±INFINITY + NaN i
          
         
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            the tangent of this.
        
        
        """
        ...
    def tanh(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute the ` hyperbolic tangent <http://mathworld.wolfram.com/HyperbolicTangent.html>` of this complex number. Implements the formula:
        
           tan(a + bi) = sinh(2a)/(cosh(2a)+cos(2b)) + [sin(2b)/(cosh(2a)+cos(2b))]i where the (real) functions on the right-hand side are sin, cos, cosh and sinh.
        
        Returns getNaN if either real or imaginary part of the input argument is NaN. Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the result.
        
        
          Examples:
          
           tanh(a ± INFINITY i) = NaN + NaN i
           tanh(±INFINITY + bi) = ±1 + 0 i
           tanh(±INFINITY ± INFINITY i) = NaN + NaN i
           tanh(0 + (π/2)i) = NaN + INFINITY i
          
         
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            the hyperbolic tangent of this.
        
        
        """
        ...
    def toDegrees(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: toString in class Object
        
        
        """
        ...
    def ulp(self) -> 'FieldComplex'[_FieldComplex__T]:
        """
        Compute least significant bit (Unit in Last Position) for a number.
        
        Specified by: ulp in interface CalculusFieldElement
        
        Returns:
            ulp(this)
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(t: _valueOf_0__T) -> 'FieldComplex'[_valueOf_0__T]:
        """
        Create a complex number given the real and imaginary parts.
        
        Parameters:
            realPart (T): Real part.
            imaginaryPart (T): Imaginary part.
        
        Returns:
            a Complex instance.
        
        Create a complex number given only the real part.
        
        Parameters:
            realPart (T): Real part.
        
        Returns:
            a Complex instance.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(t: _valueOf_1__T, t2: _valueOf_1__T) -> 'FieldComplex'[_valueOf_1__T]: ...

_FieldComplexField__T = typing.TypeVar('_FieldComplexField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldComplexField(org.hipparchus.Field[FieldComplex[_FieldComplexField__T]], typing.Generic[_FieldComplexField__T]):
    """
    implements Field<FieldComplex<T>>
    
    Representation of the complex numbers field.
    
    Since:
        2.0
    
          - FieldComplex
    """
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: equals in class Object
        
        
        """
        ...
    _getField__T = typing.TypeVar('_getField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getField(partsField: org.hipparchus.Field[_getField__T]) -> 'FieldComplexField'[_getField__T]:
        """
        Get the field for complex numbers.
        
        Parameters:
            partsField (Field<T> partsField): field for the real and imaginary parts
        
        Returns:
            cached field
        
        
        """
        ...
    def getOne(self) -> FieldComplex[_FieldComplexField__T]:
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[FieldComplex[_FieldComplexField__T]]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> FieldComplex[_FieldComplexField__T]:
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class Object
        
        
        """
        ...

_FieldComplexUnivariateIntegrator__T = typing.TypeVar('_FieldComplexUnivariateIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldComplexUnivariateIntegrator(typing.Generic[_FieldComplexUnivariateIntegrator__T]):
    """
    Wrapper to perform univariate complex integration using an underlying real integration algorithms.
    
    Since:
        2.0
    """
    def __init__(self, integrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_FieldComplexUnivariateIntegrator__T]):
        """
        Crate a complex integrator from a real integrator.
        
        Parameters:
            integrator (FieldUnivariateIntegrator<FieldComplexUnivariateIntegrator> integrator): underlying real integrator to use
        
        
        """
        ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[FieldComplex[_FieldComplexUnivariateIntegrator__T]], typing.Callable[[FieldComplex[_FieldComplexUnivariateIntegrator__T]], FieldComplex[_FieldComplexUnivariateIntegrator__T]]], fieldComplex: FieldComplex[_FieldComplexUnivariateIntegrator__T], fieldComplex2: FieldComplex[_FieldComplexUnivariateIntegrator__T]) -> FieldComplex[_FieldComplexUnivariateIntegrator__T]: ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[FieldComplex[_FieldComplexUnivariateIntegrator__T]], typing.Callable[[FieldComplex[_FieldComplexUnivariateIntegrator__T]], FieldComplex[_FieldComplexUnivariateIntegrator__T]]], fieldComplex: FieldComplex[_FieldComplexUnivariateIntegrator__T], *fieldComplex2: FieldComplex[_FieldComplexUnivariateIntegrator__T]) -> FieldComplex[_FieldComplexUnivariateIntegrator__T]: ...

class Quaternion(java.io.Serializable):
    """
    implements Serializable
    
    This class implements ` quaternions <http://mathworld.wolfram.com/Quaternion.html>` (Hamilton's hypercomplex numbers).
    
    Instance of this class are guaranteed to be immutable.
    
          - serialized
    """
    IDENTITY: typing.ClassVar['Quaternion'] = ...
    """
    Identity quaternion.
    """
    ZERO: typing.ClassVar['Quaternion'] = ...
    """
    Zero quaternion.
    """
    I: typing.ClassVar['Quaternion'] = ...
    """
    i
    """
    J: typing.ClassVar['Quaternion'] = ...
    """
    j
    """
    K: typing.ClassVar['Quaternion'] = ...
    """
    k
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def add(self, quaternion: 'Quaternion') -> 'Quaternion':
        """
        Computes the sum of two quaternions.
        
        Parameters:
            q1 (Quaternion): Quaternion.
            q2 (Quaternion): Quaternion.
        
        Returns:
            the sum of q1 and q2.
        
        Computes the sum of the instance and another quaternion.
        
        Parameters:
            q (Quaternion): Quaternion.
        
        Returns:
            the sum of this instance and q
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def add(quaternion: 'Quaternion', quaternion2: 'Quaternion') -> 'Quaternion': ...
    @typing.overload
    def dotProduct(self, quaternion: 'Quaternion') -> float:
        """
        Computes the dot-product of two quaternions.
        
        Parameters:
            q1 (Quaternion): Quaternion.
            q2 (Quaternion): Quaternion.
        
        Returns:
            the dot product of q1 and q2.
        
        Computes the dot-product of the instance by a quaternion.
        
        Parameters:
            q (Quaternion): Quaternion.
        
        Returns:
            the dot product of this instance and q.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def dotProduct(quaternion: 'Quaternion', quaternion2: 'Quaternion') -> float: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: equals in class Object
        
        Checks whether this instance is equal to another quaternion within a given tolerance.
        
        Parameters:
            q (Quaternion): Quaternion with which to compare the current quaternion.
            eps (double): Tolerance.
        
        Returns:
            true if the each of the components are equal within the allowed absolute error.
        
        
        """
        ...
    @typing.overload
    def equals(self, quaternion: 'Quaternion', double: float) -> bool: ...
    def getConjugate(self) -> 'Quaternion':
        """
        Returns the conjugate quaternion of the instance.
        
        Returns:
            the conjugate quaternion
        
        
        """
        ...
    def getInverse(self) -> 'Quaternion':
        """
        Returns the inverse of this instance. The norm of the quaternion must not be zero.
        
        Returns:
            the inverse.
        
        Raises:
            MathIllegalArgumentException: if the norm (squared) of the quaternion is zero.
        
        
        """
        ...
    def getNorm(self) -> float:
        """
        Computes the norm of the quaternion.
        
        Returns:
            the norm.
        
        
        """
        ...
    def getPositivePolarForm(self) -> 'Quaternion':
        """
        Returns the polar form of the quaternion.
        
        Returns:
            the unit quaternion with positive scalar part.
        
        
        """
        ...
    def getQ0(self) -> float:
        """
        Gets the first component of the quaternion (scalar part).
        
        Returns:
            the scalar part.
        
        
        """
        ...
    def getQ1(self) -> float:
        """
        Gets the second component of the quaternion (first component of the vector part).
        
        Returns:
            the first component of the vector part.
        
        
        """
        ...
    def getQ2(self) -> float:
        """
        Gets the third component of the quaternion (second component of the vector part).
        
        Returns:
            the second component of the vector part.
        
        
        """
        ...
    def getQ3(self) -> float:
        """
        Gets the fourth component of the quaternion (third component of the vector part).
        
        Returns:
            the third component of the vector part.
        
        
        """
        ...
    def getScalarPart(self) -> float:
        """
        Gets the scalar part of the quaternion.
        
        Returns:
            the scalar part.
        
              - getQ0
        
        
        
        """
        ...
    def getVectorPart(self) -> typing.MutableSequence[float]:
        """
        Gets the three components of the vector part of the quaternion.
        
        Returns:
            the vector part.
        
              - getQ1
              - getQ2
              - getQ3
        
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class Object
        
        
        """
        ...
    def isPureQuaternion(self, eps: float) -> bool:
        """
        Checks whether the instance is a pure quaternion within a given tolerance.
        
        Parameters:
            eps (double): Tolerance (absolute error).
        
        Returns:
            true if the scalar part of the quaternion is zero.
        
        
        """
        ...
    def isUnitQuaternion(self, eps: float) -> bool:
        """
        Checks whether the instance is a unit quaternion within a given tolerance.
        
        Parameters:
            eps (double): Tolerance (absolute error).
        
        Returns:
            true if the norm is 1 within the given tolerance, false otherwise
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Quaternion':
        """
        Returns the Hamilton product of two quaternions.
        
        Parameters:
            q1 (Quaternion): First quaternion.
            q2 (Quaternion): Second quaternion.
        
        Returns:
            the product q1 and q2, in that order.
        
        Returns the Hamilton product of the instance by a quaternion.
        
        Parameters:
            q (Quaternion): Quaternion.
        
        Returns:
            the product of this instance with q, in that order.
        
        Multiplies the instance by a scalar.
        
        Parameters:
            alpha (double): Scalar factor.
        
        Returns:
            a scaled quaternion.
        
        
        """
        ...
    @typing.overload
    def multiply(self, quaternion: 'Quaternion') -> 'Quaternion': ...
    @typing.overload
    @staticmethod
    def multiply(quaternion: 'Quaternion', quaternion2: 'Quaternion') -> 'Quaternion': ...
    def normalize(self) -> 'Quaternion':
        """
        Computes the normalized quaternion (the versor of the instance). The norm of the quaternion must not be zero.
        
        Returns:
            a normalized quaternion.
        
        Raises:
            MathIllegalArgumentException: if the norm of the quaternion is zero.
        
        
        """
        ...
    @typing.overload
    def subtract(self, quaternion: 'Quaternion') -> 'Quaternion':
        """
        Subtracts two quaternions.
        
        Parameters:
            q1 (Quaternion): First Quaternion.
            q2 (Quaternion): Second quaternion.
        
        Returns:
            the difference between q1 and q2.
        
        Subtracts a quaternion from the instance.
        
        Parameters:
            q (Quaternion): Quaternion.
        
        Returns:
            the difference between this instance and q.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtract(quaternion: 'Quaternion', quaternion2: 'Quaternion') -> 'Quaternion': ...
    def toString(self) -> str:
        """
        Overrides: toString in class Object
        
        
        """
        ...

class RootsOfUnity(java.io.Serializable):
    """
    implements Serializable
    
    A helper class for the computation and caching of the n-th roots of unity.
    
          - serialized
    """
    def __init__(self):
        """
        Build an engine for computing the n-th roots of unity.
        """
        ...
    def computeRoots(self, n: int) -> None:
        """
        Computes the n-th roots of unity.
        
        The roots are stored in omega[], such that omega[k] = w ^ k, where , n - 1, w = exp(2 * pi * i / n) and i = sqrt(-1).
        
        Note that n can be positive of negative
        
          - abs(n) is always the number of roots of unity.
          - If n > 0, then the roots are stored in counter-clockwise order.
          - If n < 0, then the roots are stored in clockwise order.
        
        
        Parameters:
            n (int): the (signed) number of roots of unity to be computed
        
        Raises:
            MathIllegalArgumentException: if n = 0
        
        
        """
        ...
    def getImaginary(self, k: int) -> float:
        """
        Get the imaginary part of the k-th n-th root of unity.
        
        Parameters:
            k (int): index of the n-th root of unity
        
        Returns:
            imaginary part of the k-th n-th root of unity
        
        Raises:
            MathIllegalStateException: if no roots of unity have been computed yet
            MathIllegalArgumentException: if k is out of range
        
        
        """
        ...
    def getNumberOfRoots(self) -> int:
        """
        Returns the number of roots of unity currently stored.
        
        If computeRoots was called with n, then this method returns abs(n). If no roots of unity have been computed yet, this method returns 0.
        
        Returns:
            the number of roots of unity currently stored
        
        
        """
        ...
    def getReal(self, k: int) -> float:
        """
        Get the real part of the k-th n-th root of unity.
        
        Parameters:
            k (int): index of the n-th root of unity
        
        Returns:
            real part of the k-th n-th root of unity
        
        Raises:
            MathIllegalStateException: if no roots of unity have been computed yet
            MathIllegalArgumentException: if k is out of range
        
        
        """
        ...
    def isCounterClockWise(self) -> bool:
        """
        Returns true if computeRoots was called with a positive value of its argument n. If true, then counter-clockwise ordering of the roots of unity should be used.
        
        Returns:
            true if the roots of unity are stored in counter-clockwise order
        
        Raises:
            MathIllegalStateException: if no roots of unity have been computed yet
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.complex")``.

    Complex: typing.Type[Complex]
    ComplexComparator: typing.Type[ComplexComparator]
    ComplexField: typing.Type[ComplexField]
    ComplexFormat: typing.Type[ComplexFormat]
    ComplexUnivariateIntegrator: typing.Type[ComplexUnivariateIntegrator]
    ComplexUtils: typing.Type[ComplexUtils]
    FieldComplex: typing.Type[FieldComplex]
    FieldComplexField: typing.Type[FieldComplexField]
    FieldComplexUnivariateIntegrator: typing.Type[FieldComplexUnivariateIntegrator]
    Quaternion: typing.Type[Quaternion]
    RootsOfUnity: typing.Type[RootsOfUnity]
