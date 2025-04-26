
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
    public classComplex extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.complex.Complex`>, :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable`<:class:`~org.hipparchus.complex.Complex`>, :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Representation of a Complex number, i.e. a number which has both a real and imaginary part.
    
        Implementations of arithmetic operations handle :code:`NaN` and infinite values according to the rules for
        :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double`, i.e.
        :meth:`~org.hipparchus.complex.Complex.equals` is an equivalence relation for all instances that have a :code:`NaN` in
        either real or imaginary part, e.g. the following are considered equal:
    
          - :code:`1 + NaNi`
          - :code:`NaN + i`
          - :code:`NaN + NaNi`
    
    
        Note that this contradicts the IEEE-754 standard for floating point numbers (according to which the test :code:`x == x`
        must fail if :code:`x` is :code:`NaN`). The method :meth:`~org.hipparchus.util.Precision.equals` in
        :class:`~org.hipparchus.util.Precision` conforms with IEEE-754 while this class conforms with the standard behavior for
        Java object types.
    
        Also see:
    
              - :meth:`~serialized`
    """
    I: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` I
    
        The square root of -1. A number representing "0.0 + 1.0i".
    
    """
    MINUS_I: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` MINUS_I
    
        The square root of -1. A number representing "0.0 - 1.0i".
    
        Since:
            1.7
    
    
    """
    NaN: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` NaN
    
        A complex number representing "NaN + NaNi".
    
    """
    INF: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` INF
    
        A complex number representing "+INF + INFi"
    
    """
    ONE: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` ONE
    
        A complex number representing "1.0 + 0.0i".
    
    """
    MINUS_ONE: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` MINUS_ONE
    
        A complex number representing "-1.0 + 0.0i".
    
        Since:
            1.7
    
    
    """
    ZERO: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` ZERO
    
        A complex number representing "0.0 + 0.0i".
    
    """
    PI: typing.ClassVar['Complex'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Complex` PI
    
        A complex number representing "π + 0.0i".
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def abs(self) -> 'Complex':
        """
            Return the absolute value of this complex number. Returns :code:`NaN` if either real or imaginary part is :code:`NaN`
            and :code:`Double.POSITIVE_INFINITY` if neither part is :code:`NaN`, but at least one part is infinite.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the norm.
        
            Since:
                2.0
        
        
        """
        ...
    def acos(self) -> 'Complex':
        """
            Compute the ` inverse cosine <http://mathworld.wolfram.com/InverseCosine.html>` of this complex number. Implements the
            formula:
        
            :code:`acos(z) = -i (log(z + i (sqrt(1 - z<sup>2</sup>))))`
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN` or infinite.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the inverse cosine of this complex number.
        
        
        """
        ...
    def acosh(self) -> 'Complex':
        """
            Inverse hyperbolic cosine operation.
        
            Branch cuts are on the real axis, below +1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
            Since:
                1.7
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'Complex':
        """
            Returns a :code:`Complex` whose value is :code:`(this + addend)`, with :code:`addend` interpreted as a real number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.add` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                addend (double): Value to be added to this :code:`Complex`.
        
            Returns:
                :code:`this + addend`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.Complex.add`
        
        
        
        """
        ...
    @typing.overload
    def add(self, complex: 'Complex') -> 'Complex': ...
    def asin(self) -> 'Complex':
        """
            Compute the ` inverse sine <http://mathworld.wolfram.com/InverseSine.html>` of this complex number. Implements the
            formula:
        
            :code:`asin(z) = -i (log(sqrt(1 - z<sup>2</sup>) + iz))`
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN` or infinite.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the inverse sine of this complex number.
        
        
        """
        ...
    def asinh(self) -> 'Complex':
        """
            Inverse hyperbolic sine operation.
        
            Branch cuts are on the imaginary axis, above +i and below -i.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
            Since:
                1.7
        
        
        """
        ...
    def atan(self) -> 'Complex':
        """
            Compute the ` inverse tangent <http://mathworld.wolfram.com/InverseTangent.html>` of this complex number. Implements the
            formula:
        
            :code:`atan(z) = (i/2) log((1 - iz)/(1 + iz))`
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN` or infinite.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the inverse tangent of this complex number
        
        
        """
        ...
    def atan2(self, complex: 'Complex') -> 'Complex':
        """
            Two arguments arc tangent operation.
        
            Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with
            arguments order, the instance is the *first* argument and the single provided argument is the *second* argument. In
            order to be consistent with programming languages :code:`atan2`, this method computes :code:`atan2(this, x)`, i.e. the
            instance represents the :code:`y` argument and the :code:`x` argument is the one passed as a single argument. This may
            seem confusing especially for users of Wolfram alpha, as this site is *not* consistent with programming languages
            :code:`atan2` two-arguments arc tangent and puts :code:`x` as its first argument.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan2` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): second argument of the arc tangent
        
            Returns:
            Since:
                1.7
        
        
        """
        ...
    def atanh(self) -> 'Complex':
        """
            Inverse hyperbolic tangent operation.
        
            Branch cuts are on the real axis, above +1 and below -1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
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
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cbrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cubic root of the instance
        
            Since:
                1.7
        
        
        """
        ...
    def ceil(self) -> 'Complex':
        """
            Get the smallest whole number larger than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ceil(this)
        
            Since:
                1.7
        
        
        """
        ...
    def compareTo(self, complex: 'Complex') -> int:
        """
        
            Comparison us performed using real ordering as the primary sort order and imaginary ordering as the secondary sort
            order.
        
            Specified by:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.compareTo` in
                interface :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable`
        
            Since:
                3.0
        
        
        """
        ...
    def conjugate(self) -> 'Complex':
        """
            Returns the conjugate of this complex number. The conjugate of :code:`a + bi` is :code:`a - bi`.
        
            :meth:`~org.hipparchus.complex.Complex.NaN` is returned if either the real or imaginary part of this Complex number
            equals :code:`Double.NaN`.
        
            If the imaginary part is infinite, and the real part is not :code:`NaN`, the returned value has infinite imaginary part
            of the opposite sign, e.g. the conjugate of :code:`1 + POSITIVE_INFINITY i` is :code:`1 - NEGATIVE_INFINITY i`.
        
            Returns:
                the conjugate of this Complex object.
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'Complex':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            The signs of real and imaginary parts are copied independently.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                z (:class:`~org.hipparchus.complex.Complex`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Since:
                1.7
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                r (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Since:
                1.7
        
        
        """
        ...
    @typing.overload
    def copySign(self, complex: 'Complex') -> 'Complex': ...
    def cos(self) -> 'Complex':
        """
            Compute the ` cosine <http://mathworld.wolfram.com/Cosine.html>` of this complex number. Implements the formula:
        
            :code:`cos(a + bi) = cos(a)cosh(b) - sin(a)sinh(b)i`
        
            where the (real) functions on the right-hand side are :meth:`~org.hipparchus.util.FastMath.sin`,
            :meth:`~org.hipparchus.util.FastMath.cos`, :meth:`~org.hipparchus.util.FastMath.cosh` and
            :meth:`~org.hipparchus.util.FastMath.sinh`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
        
            Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the
            result.
        
            .. code-block: java
            
              Examples:
              
               cos(1 ± INFINITY i) = 1 ∓ INFINITY i
               cos(±INFINITY + i) = NaN + NaN i
               cos(±INFINITY ± INFINITY i) = NaN + NaN i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the cosine of this complex number.
        
        
        """
        ...
    def cosh(self) -> 'Complex':
        """
            Compute the ` hyperbolic cosine <http://mathworld.wolfram.com/HyperbolicCosine.html>` of this complex number. Implements
            the formula:
        
            .. code-block: java
            
              
               cosh(a + bi) = cosh(a)cos(b) + sinh(a)sin(b)i
              
             
            where the (real) functions on the right-hand side are :meth:`~org.hipparchus.util.FastMath.sin`,
            :meth:`~org.hipparchus.util.FastMath.cos`, :meth:`~org.hipparchus.util.FastMath.cosh` and
            :meth:`~org.hipparchus.util.FastMath.sinh`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
            Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the
            result.
        
            .. code-block: java
            
              Examples:
              
               cosh(1 ± INFINITY i) = NaN + NaN i
               cosh(±INFINITY + i) = INFINITY ± INFINITY i
               cosh(±INFINITY ± INFINITY i) = NaN + NaN i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the hyperbolic cosine of this complex number.
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'Complex':
        """
            Returns a :code:`Complex` whose value is :code:`(this / divisor)`, with :code:`divisor` interpreted as a real number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.divide` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                divisor (double): Value by which this :code:`Complex` is to be divided.
        
            Returns:
                :code:`this / divisor`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.Complex.divide`
        
        
        
        """
        ...
    @typing.overload
    def divide(self, complex: 'Complex') -> 'Complex': ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
            Test for equality with another object. If both the real and imaginary parts of two complex numbers are exactly the same,
            and neither is :code:`Double.NaN`, the two Complex objects are considered to be equal. The behavior is the same as for
            JDK's :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.equals`:
        
              - All :code:`NaN` values are considered to be equal, i.e, if either (or both) real and imaginary parts of the complex
                number are equal to :code:`Double.NaN`, the complex number is equal to :code:`NaN`.
              -         Instances constructed with different representations of zero (i.e. either "0" or "-0") are *not* considered to be equal.
        
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality with this instance.
        
            Returns:
                :code:`true` if the objects are equal, :code:`false` if object is :code:`null`, not an instance of :code:`Complex`, or
                not equal to this instance.
        
            Test for the floating-point equality between Complex objects. It returns :code:`true` if both arguments are equal or
            within the range of allowed error (inclusive).
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.Complex`): Second value (cannot be :code:`null`).
                maxUlps (int): :code:`(maxUlps - 1)` is the number of floating point values between the real (resp. imaginary) parts of :code:`x` and
                    :code:`y`.
        
            Returns:
                :code:`true` if there are fewer than :code:`maxUlps` floating point values between the real (resp. imaginary) parts of
                :code:`x` and :code:`y`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.util.Precision.equals`
        
        
            Returns :code:`true` iff the values are equal as defined by :meth:`~org.hipparchus.complex.Complex.equals`.
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.Complex`): Second value (cannot be :code:`null`).
        
            Returns:
                :code:`true` if the values are equal.
        
            Returns :code:`true` if, both for the real part and for the imaginary part, there is no double value strictly between
            the arguments or the difference between them is within the range of allowed error (inclusive). Returns :code:`false` if
            either of the arguments is NaN.
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.Complex`): Second value (cannot be :code:`null`).
                eps (double): Amount of allowed absolute error.
        
            Returns:
                :code:`true` if the values are two adjacent floating point numbers or they are within range of each other.
        
            Also see:
        
                  - :meth:`~org.hipparchus.util.Precision.equals`
        
        
        
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
    def equalsWithRelativeTolerance(complex: 'Complex', complex2: 'Complex', double: float) -> bool:
        """
            Returns :code:`true` if, both for the real part and for the imaginary part, there is no double value strictly between
            the arguments or the relative difference between them is smaller or equal to the given tolerance. Returns :code:`false`
            if either of the arguments is NaN.
        
            Parameters:
                x (:class:`~org.hipparchus.complex.Complex`): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.Complex`): Second value (cannot be :code:`null`).
                eps (double): Amount of allowed relative error.
        
            Returns:
                :code:`true` if the values are two adjacent floating point numbers or they are within range of each other.
        
            Also see:
        
                  - :meth:`~org.hipparchus.util.Precision.equalsWithRelativeTolerance`
        
        
        
        """
        ...
    def exp(self) -> 'Complex':
        """
            Compute the ` exponential function <http://mathworld.wolfram.com/ExponentialFunction.html>` of this complex number.
            Implements the formula:
        
            .. code-block: java
            
              
               exp(a + bi) = exp(a)cos(b) + exp(a)sin(b)i
              
             
            where the (real) functions on the right-hand side are :meth:`~org.hipparchus.util.FastMath.exp` p},
            :meth:`~org.hipparchus.util.FastMath.cos`, and :meth:`~org.hipparchus.util.FastMath.sin`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
            Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the
            result.
        
            .. code-block: java
            
              Examples:
              
               exp(1 ± INFINITY i) = NaN + NaN i
               exp(INFINITY + i) = INFINITY + INFINITY i
               exp(-INFINITY + i) = 0 + 0i
               exp(±INFINITY ± INFINITY i) = NaN + NaN i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                :code:`*e* :sup:`this``.
        
        
        """
        ...
    def expm1(self) -> 'Complex':
        """
            Exponential minus 1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.expm1` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential minus one of the instance
        
            Since:
                1.7
        
        
        """
        ...
    def floor(self) -> 'Complex':
        """
            Get the largest whole number smaller than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                floor(this)
        
            Since:
                1.7
        
        
        """
        ...
    def getAddendum(self) -> 'Complex':
        """
            Get the addendum to the real value of the number.
        
            The addendum is considered to be the part that when added back to the :meth:`~org.hipparchus.FieldElement.getReal`
            recovers the instance. This means that when :code:`e.getReal()` is finite (i.e. neither infinite nor NaN), then
            :code:`e.getAddendum().add(e.getReal())` is :code:`e` and :code:`e.subtract(e.getReal())` is :code:`e.getAddendum()`.
            Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always
            holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives
            types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the
            subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getAddendum` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def getArgument(self) -> float:
        """
            Compute the argument of this complex number. The argument is the angle phi between the positive real axis and the point
            representing this number in the complex plane. The value returned is between -PI (not inclusive) and PI (inclusive),
            with negative values returned for numbers with negative imaginary parts.
        
            If either real or imaginary part (or both) is NaN, NaN is returned. Infinite parts are handled as :code:`Math.atan2`
            handles them, essentially treating finite parts as zero in the presence of an infinite coordinate and returning a
            multiple of pi/4 depending on the signs of the infinite parts. See the javadoc for :code:`Math.atan2` for full details.
        
            Returns:
                the argument of :code:`this`.
        
        
        """
        ...
    def getField(self) -> 'ComplexField':
        """
            Get the :class:`~org.hipparchus.Field` to which the instance belongs.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getField` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                :class:`~org.hipparchus.Field` to which the instance belongs
        
        
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
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant π
        
        
        """
        ...
    def getReal(self) -> float:
        """
            Access the real part.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
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
            Get a hashCode for the complex number. Any :code:`Double.NaN` value in real or imaginary part produces the same hash
            code :code:`7`.
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a hash code value for this object.
        
        
        """
        ...
    def hypot(self, complex: 'Complex') -> 'Complex':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2`  +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.hypot` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                y (:class:`~org.hipparchus.complex.Complex`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
            Since:
                1.7
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Checks whether either the real or imaginary part of this complex number takes an infinite value (either
            :code:`Double.POSITIVE_INFINITY` or :code:`Double.NEGATIVE_INFINITY`) and neither part is :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isInfinite` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                true if one or both parts of this complex number are infinite and neither part is :code:`NaN`.
        
        
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
            Checks whether either or both parts of this complex number is :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isNaN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                true if either or both parts of this complex number is :code:`NaN`; false otherwise.
        
        
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
        
            The default implementation simply calls :code:`equals(getField().getZero())`. However, this may need to be overridden in
            some cases as due to compatibility with :code:`hashCode()` some classes implements :code:`equals(Object)` in such a way
            that -0.0 and +0.0 are different, which may be a problem. It prevents for example identifying a diagonal element is zero
            and should be avoided when doing partial pivoting in LU decomposition.
        
            This implementation considers +0.0 and -0.0 to be equal for both real and imaginary components.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.isZero` in interface :class:`~org.hipparchus.FieldElement`
        
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
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.complex.Complex`): first factor of the first term
                b1 (:class:`~org.hipparchus.complex.Complex`): second factor of the first term
                a2 (:class:`~org.hipparchus.complex.Complex`): first factor of the second term
                b2 (:class:`~org.hipparchus.complex.Complex`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Since:
                1.7
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.complex.Complex`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.complex.Complex`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Since:
                1.7
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.complex.Complex`): first factor of the first term
                b1 (:class:`~org.hipparchus.complex.Complex`): second factor of the first term
                a2 (:class:`~org.hipparchus.complex.Complex`): first factor of the second term
                b2 (:class:`~org.hipparchus.complex.Complex`): second factor of the second term
                a3 (:class:`~org.hipparchus.complex.Complex`): first factor of the third term
                b3 (:class:`~org.hipparchus.complex.Complex`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Since:
                1.7
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.complex.Complex`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.complex.Complex`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.complex.Complex`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Since:
                1.7
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.complex.Complex`): first factor of the first term
                b1 (:class:`~org.hipparchus.complex.Complex`): second factor of the first term
                a2 (:class:`~org.hipparchus.complex.Complex`): first factor of the second term
                b2 (:class:`~org.hipparchus.complex.Complex`): second factor of the second term
                a3 (:class:`~org.hipparchus.complex.Complex`): first factor of the third term
                b3 (:class:`~org.hipparchus.complex.Complex`): second factor of the third term
                a4 (:class:`~org.hipparchus.complex.Complex`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.complex.Complex`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Since:
                1.7
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.complex.Complex`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.complex.Complex`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.complex.Complex`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.complex.Complex`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Since:
                1.7
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        
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
            Compute the ` natural logarithm <http://mathworld.wolfram.com/NaturalLogarithm.html>` of this complex number. Implements
            the formula:
        
            .. code-block: java
            
              
               log(a + bi) = ln(|a + bi|) + arg(a + bi)i
              
             
            where ln on the right hand side is :meth:`~org.hipparchus.util.FastMath.log`, :code:`|a + bi|` is the modulus,
            :meth:`~org.hipparchus.complex.Complex.abs`, and :code:`arg(a + bi) =`:meth:`~org.hipparchus.util.FastMath.atan2`(b, a).
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
            Infinite (or critical) values in real or imaginary parts of the input may result in infinite or NaN values returned in
            parts of the result.
        
            .. code-block: java
            
              Examples:
              
               log(1 ± INFINITY i) = INFINITY ± (π/2)i
               log(INFINITY + i) = INFINITY + 0i
               log(-INFINITY + i) = INFINITY + πi
               log(INFINITY ± INFINITY i) = INFINITY ± (π/4)i
               log(-INFINITY ± INFINITY i) = INFINITY ± (3π/4)i
               log(0 + 0i) = -INFINITY + 0i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the value :code:`ln   this`, the natural logarithm of :code:`this`.
        
        
        """
        ...
    def log10(self) -> 'Complex':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
            Since:
                1.7
        
        
        """
        ...
    def log1p(self) -> 'Complex':
        """
            Shifted natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log1p` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of one plus the instance
        
            Since:
                1.7
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Complex':
        """
            Returns a :code:`Complex` whose value is :code:`this * factor`, with :code:`factor` interpreted as a integer number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                factor (int): value to be multiplied by this :code:`Complex`.
        
            Returns:
                :code:`this * factor`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.Complex.multiply`
        
        
            Returns a :code:`Complex` whose value is :code:`this * factor`, with :code:`factor` interpreted as a real number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                factor (double): value to be multiplied by this :code:`Complex`.
        
            Returns:
                :code:`this * factor`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.Complex.multiply`
        
        
        
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
            Returns a :code:`Complex` whose value is :code:`(-this)`. Returns :code:`NaN` if either real or imaginary part of this
            Complex number is :code:`Double.NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                :code:`-this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'Complex':
        """
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                realPart (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    def norm(self) -> float:
        """
            norm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.norm` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                norm(this)
        
        
        """
        ...
    def nthRoot(self, int: int) -> java.util.List['Complex']: ...
    @typing.overload
    def pow(self, double: float) -> 'Complex':
        """
            Returns of value of this complex number raised to the power of :code:`x`.
        
            If :code:`x` has an integer value, returns :meth:`~org.hipparchus.complex.Complex.pow`, if :code:`this` is real and
            :meth:`~org.hipparchus.util.FastMath.pow` with the corresponding real arguments would return a finite number (neither
            NaN nor infinite), then returns the same value converted to :code:`Complex`, with the same special cases. In all other
            cases real cases, implements y :sup:`x` = exp(x·log(y)).
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                x (double): exponent to which this :code:`Complex` is to be raised.
        
            Returns:
                :code:`this :sup:`x``.
        
            Integer power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
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
            Returns the multiplicative inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'Complex':
        """
            IEEE remainder operator.
        
            for complex numbers, the integer n corresponding to :code:`this.subtract(remainder(a)).divide(a)` is a
            :class:`~org.hipparchus.complex.https:.en.wikipedia.org.wiki.Gaussian_integer`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            Since:
                1.7
        
            IEEE remainder operator.
        
            for complex numbers, the integer n corresponding to :code:`this.subtract(remainder(a)).divide(a)` is a
            :class:`~org.hipparchus.complex.https:.en.wikipedia.org.wiki.Gaussian_integer`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.complex.Complex`): right hand side parameter of the operator
        
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
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
            Since:
                1.7
        
        
        """
        ...
    def rootN(self, int: int) -> 'Complex':
        """
            N :sup:`th` root.
        
            This implementation compute the principal n :sup:`th` root by using a branch cut along real negative axis.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rootN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): order of the root
        
            Returns:
                n :sup:`th` root of the instance
        
            Since:
                1.7
        
        
        """
        ...
    def scalb(self, int: int) -> 'Complex':
        """
            Multiply the instance by a power of 2.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.scalb` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
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
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
            Since:
                2.0
        
        
        """
        ...
    def sin(self) -> 'Complex':
        """
            Compute the ` sine <http://mathworld.wolfram.com/Sine.html>` of this complex number. Implements the formula:
        
            .. code-block: java
            
              
               sin(a + bi) = sin(a)cosh(b) + cos(a)sinh(b)i
              
             
            where the (real) functions on the right-hand side are :meth:`~org.hipparchus.util.FastMath.sin`,
            :meth:`~org.hipparchus.util.FastMath.cos`, :meth:`~org.hipparchus.util.FastMath.cosh` and
            :meth:`~org.hipparchus.util.FastMath.sinh`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
        
            Infinite values in real or imaginary parts of the input may result in infinite or :code:`NaN` values returned in parts
            of the result.
        
            .. code-block: java
            
              Examples:
              
               sin(1 ± INFINITY i) = 1 ± INFINITY i
               sin(±INFINITY + i) = NaN + NaN i
               sin(±INFINITY ± INFINITY i) = NaN + NaN i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the sine of this complex number.
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['Complex']: ...
    def sinh(self) -> 'Complex':
        """
            Compute the ` hyperbolic sine <http://mathworld.wolfram.com/HyperbolicSine.html>` of this complex number. Implements the
            formula:
        
            .. code-block: java
            
              
               sinh(a + bi) = sinh(a)cos(b)) + cosh(a)sin(b)i
              
             
            where the (real) functions on the right-hand side are :meth:`~org.hipparchus.util.FastMath.sin`,
            :meth:`~org.hipparchus.util.FastMath.cos`, :meth:`~org.hipparchus.util.FastMath.cosh` and
            :meth:`~org.hipparchus.util.FastMath.sinh`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
        
            Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the
            result.
        
            .. code-block: java
            
              Examples:
              
               sinh(1 ± INFINITY i) = NaN + NaN i
               sinh(±INFINITY + i) = ± INFINITY + INFINITY i
               sinh(±INFINITY ± INFINITY i) = NaN + NaN i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the hyperbolic sine of :code:`this`.
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['Complex']: ...
    def sqrt(self) -> 'Complex':
        """
            Compute the ` square root <http://mathworld.wolfram.com/SquareRoot.html>` of this complex number. Implements the
            following algorithm to compute :code:`sqrt(a + bi)`:
        
              1.  Let :code:`t = sqrt((|a| + |a + bi|) / 2)`
              2.  
                .. code-block: java
                
                if  a ≥ 0 return :code:`t + (b/2t)i`
                  else return :code:`|b|/2t + sign(b)t i`
        
            where
        
              - :code:`|a| =`:meth:`~org.hipparchus.util.FastMath.abs`
              - :code:`|a + bi| =`:meth:`~org.hipparchus.util.FastMath.hypot`
              - :code:`sign(b) =`:meth:`~org.hipparchus.util.FastMath.copySign`
        
            The real part is therefore always nonnegative.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
        
            Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the
            result.
        
            .. code-block: java
            
              Examples:
              
               sqrt(1 ± ∞ i) = ∞ + NaN i
               sqrt(∞ + i) = ∞ + 0i
               sqrt(-∞ + i) = 0 + ∞ i
               sqrt(∞ ± ∞ i) = ∞ + NaN i
               sqrt(-∞ ± ∞ i) = NaN ± ∞ i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the square root of :code:`this` with nonnegative real part.
        
        
        """
        ...
    def sqrt1z(self) -> 'Complex':
        """
            Compute the ` square root <http://mathworld.wolfram.com/SquareRoot.html>` of :code:`1 - this :sup:`2`` for this complex
            number. Computes the result directly as :code:`sqrt(ONE.subtract(z.square()))`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
            Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the
            result.
        
            Returns:
                the square root of :code:`1 - this :sup:`2``.
        
        
        """
        ...
    def square(self) -> 'Complex':
        """
            Compute this × this.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.square` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'Complex':
        """
            Returns a :code:`Complex` whose value is :code:`(this - subtrahend)`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.subtract` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                subtrahend (double): value to be subtracted from this :code:`Complex`.
        
            Returns:
                :code:`this - subtrahend`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.Complex.subtract`
        
        
        
        """
        ...
    @typing.overload
    def subtract(self, complex: 'Complex') -> 'Complex': ...
    def tan(self) -> 'Complex':
        """
            Compute the ` tangent <http://mathworld.wolfram.com/Tangent.html>` of this complex number. Implements the formula:
        
            .. code-block: java
            
              
               tan(a + bi) = sin(2a)/(cos(2a)+cosh(2b)) + [sinh(2b)/(cos(2a)+cosh(2b))]i
              
             
            where the (real) functions on the right-hand side are :meth:`~org.hipparchus.util.FastMath.sin`,
            :meth:`~org.hipparchus.util.FastMath.cos`, :meth:`~org.hipparchus.util.FastMath.cosh` and
            :meth:`~org.hipparchus.util.FastMath.sinh`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
            Infinite (or critical) values in real or imaginary parts of the input may result in infinite or NaN values returned in
            parts of the result.
        
            .. code-block: java
            
              Examples:
              
               tan(a ± INFINITY i) = 0 ± i
               tan(±INFINITY + bi) = NaN + NaN i
               tan(±INFINITY ± INFINITY i) = NaN + NaN i
               tan(±&pi;/2 + 0 i) = ±INFINITY + NaN i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the tangent of :code:`this`.
        
        
        """
        ...
    def tanh(self) -> 'Complex':
        """
            Compute the ` hyperbolic tangent <http://mathworld.wolfram.com/HyperbolicTangent.html>` of this complex number.
            Implements the formula:
        
            .. code-block: java
            
              
               tan(a + bi) = sinh(2a)/(cosh(2a)+cos(2b)) + [sin(2b)/(cosh(2a)+cos(2b))]i
              
             
            where the (real) functions on the right-hand side are :meth:`~org.hipparchus.util.FastMath.sin`,
            :meth:`~org.hipparchus.util.FastMath.cos`, :meth:`~org.hipparchus.util.FastMath.cosh` and
            :meth:`~org.hipparchus.util.FastMath.sinh`.
        
            Returns :meth:`~org.hipparchus.complex.Complex.NaN` if either real or imaginary part of the input argument is
            :code:`NaN`.
            Infinite values in real or imaginary parts of the input may result in infinite or NaN values returned in parts of the
            result.
        
            .. code-block: java
            
              Examples:
              
               tanh(a ± INFINITY i) = NaN + NaN i
               tanh(±INFINITY + bi) = ±1 + 0 i
               tanh(±INFINITY ± INFINITY i) = NaN + NaN i
               tanh(0 + (π/2)i) = NaN + INFINITY i
              
             
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                the hyperbolic tangent of :code:`this`.
        
        
        """
        ...
    def toDegrees(self) -> 'Complex':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'Complex':
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toRadians` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    def ulp(self) -> 'Complex':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
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
    public classComplexComparator extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.util.Comparator`<:class:`~org.hipparchus.complex.Complex`>, :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Comparator for Complex Numbers.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self): ...
    def compare(self, complex: Complex, complex2: Complex) -> int:
        """
            Compare two complex numbers, using real ordering as the primary sort order and imaginary ordering as the secondary sort
            order.
        
            Specified by:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.util.Comparator.compare` in
                interface :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.util.Comparator`
        
            Parameters:
                o1 (:class:`~org.hipparchus.complex.Complex`): first complex number
                o2 (:class:`~org.hipparchus.complex.Complex`): second complex number
        
            Returns:
                a negative value if o1 real part is less than o2 real part or if real parts are equal and o1 imaginary part is less than
                o2 imaginary part
        
        
        """
        ...

class ComplexField(org.hipparchus.Field[Complex], java.io.Serializable):
    """
    public classComplexField extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.complex.Complex`>, :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Representation of the complex numbers field.
    
        This class is a singleton.
    
        Also see:
    
              - :class:`~org.hipparchus.complex.Complex`
              - :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
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
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Complex]: ...
    def getZero(self) -> Complex:
        """
            Get the additive identity of the field.
        
            The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a
            + e :sub:`0` = e :sub:`0` + a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getZero` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...

class ComplexFormat:
    """
    public classComplexFormat extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Formats a Complex number in cartesian format "Re(c) + Im(c)i". 'i' can be replaced with 'j' (or anything else), and the
        number format for both real and imaginary parts can be configured.
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
            This method calls :meth:`~org.hipparchus.complex.ComplexFormat.format`.
        
            Parameters:
                c (:class:`~org.hipparchus.complex.Complex`): Complex object to format.
        
            Returns:
                A formatted number in the form "Re(c) + Im(c)i".
        
            This method calls :meth:`~org.hipparchus.complex.ComplexFormat.format`.
        
            Parameters:
                c (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double`): Double object to format.
        
            Returns:
                A formatted number.
        
            Formats a :class:`~org.hipparchus.complex.Complex` object to produce a string.
        
            Parameters:
                complex (:class:`~org.hipparchus.complex.Complex`): the object to format.
                toAppendTo (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
        public :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer` format(:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object` obj, :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer` toAppendTo, :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition` pos) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Formats a object to produce a string. :code:`obj` must be either a :class:`~org.hipparchus.complex.Complex` object or a
            :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number` object. Any other type of
            object will result in an
            :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException` being
            thrown.
        
            Parameters:
                obj (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): the object to format.
                toAppendTo (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: is :code:`obj` is not a valid type.
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.text.Format.format`
        
        
        
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
        
            This is the same set as the
            :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat` set.
        
            Returns:
                available complex format locales.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getComplexFormat() -> 'ComplexFormat':
        """
            Returns the default complex format for the current locale.
        
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
            Returns the default complex format for the given locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale`): the specific locale used by the format.
        
            Returns:
                the complex format specific to the given locale.
        
            Since:
                1.4
        
        public static :class:`~org.hipparchus.complex.ComplexFormat` getComplexFormat(:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String` imaginaryCharacter, :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale` locale) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`, :class:`~org.hipparchus.exception.NullArgumentException`
        
            Returns the default complex format for the given locale.
        
            Parameters:
                imaginaryCharacter (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): Imaginary character.
                locale (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale`): the specific locale used by the format.
        
            Returns:
                the complex format specific to the given locale.
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if :code:`imaginaryCharacter` is :code:`null`.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`imaginaryCharacter` is an empty string.
        
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
            Parses a string to produce a :class:`~org.hipparchus.complex.Complex` object.
        
            Parameters:
                source (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the string to parse
                pos (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition`): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.complex.Complex` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Complex: ...

class ComplexUnivariateIntegrator:
    """
    public classComplexUnivariateIntegrator extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Wrapper to perform univariate complex integration using an underlying real integration algorithms.
    
        Since:
            2.0
    """
    def __init__(self, univariateIntegrator: org.hipparchus.analysis.integration.UnivariateIntegrator): ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[Complex], typing.Callable[[Complex], Complex]], complex: Complex, complex2: Complex) -> Complex: ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[Complex], typing.Callable[[Complex], Complex]], complex: Complex, *complex2: Complex) -> Complex: ...

class ComplexUtils:
    """
    public classComplexUtils extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Static implementations of common :class:`~org.hipparchus.complex.Complex` utilities functions.
    """
    @staticmethod
    def convertToComplex(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[Complex]:
        """
            Convert an array of primitive doubles to an array of :code:`Complex` objects.
        
            Parameters:
                real (double[]): Array of numbers to be converted to their :code:`Complex` equivalent.
        
            Returns:
                an array of :code:`Complex` objects.
        
        
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
    public classFieldComplex<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.complex.FieldComplex`<T>>
    
        Representation of a Complex number, i.e. a number which has both a real and imaginary part.
    
        Implementations of arithmetic operations handle :code:`NaN` and infinite values according to the rules for
        :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double`, i.e.
        :meth:`~org.hipparchus.complex.FieldComplex.equals` is an equivalence relation for all instances that have a :code:`NaN`
        in either real or imaginary part, e.g. the following are considered equal:
    
          - :code:`1 + NaNi`
          - :code:`NaN + i`
          - :code:`NaN + NaNi`
    
    
        Note that this contradicts the IEEE-754 standard for floating point numbers (according to which the test :code:`x == x`
        must fail if :code:`x` is :code:`NaN`). The method :meth:`~org.hipparchus.util.Precision.equals` in
        :class:`~org.hipparchus.util.Precision` conforms with IEEE-754 while this class conforms with the standard behavior for
        Java object types.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self, t: _FieldComplex__T): ...
    @typing.overload
    def __init__(self, t: _FieldComplex__T, t2: _FieldComplex__T): ...
    def abs(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def acos(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def acosh(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def add(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def add(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def add(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def asin(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def asinh(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def atan(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def atan2(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def atanh(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def cbrt(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def ceil(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def conjugate(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def copySign(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def copySign(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def cos(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def cosh(self) -> 'FieldComplex'[_FieldComplex__T]: ...
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
    def equals(self, object: typing.Any) -> bool:
        """
            Test for equality with another object. If both the real and imaginary parts of two complex numbers are exactly the same,
            and neither is :code:`Double.NaN`, the two Complex objects are considered to be equal. The behavior is the same as for
            JDK's :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.equals`:
        
              - All :code:`NaN` values are considered to be equal, i.e, if either (or both) real and imaginary parts of the complex
                number are equal to :code:`Double.NaN`, the complex number is equal to :code:`NaN`.
              -         Instances constructed with different representations of zero (i.e. either "0" or "-0") are *not* considered to be equal.
        
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): Object to test for equality with this instance.
        
            Returns:
                :code:`true` if the objects are equal, :code:`false` if object is :code:`null`, not an instance of :code:`Complex`, or
                not equal to this instance.
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(fieldComplex: 'FieldComplex'[_equals_1__T], fieldComplex2: 'FieldComplex'[_equals_1__T]) -> bool:
        """
            Returns :code:`true` iff the values are equal as defined by :meth:`~org.hipparchus.complex.FieldComplex.equals`.
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): Second value (cannot be :code:`null`).
        
            Returns:
                :code:`true` if the values are equal.
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(fieldComplex: 'FieldComplex'[_equals_2__T], fieldComplex2: 'FieldComplex'[_equals_2__T], double: float) -> bool:
        """
            Test for the floating-point equality between Complex objects. It returns :code:`true` if both arguments are equal or
            within the range of allowed error (inclusive).
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): Second value (cannot be :code:`null`).
                maxUlps (int): :code:`(maxUlps - 1)` is the number of floating point values between the real (resp. imaginary) parts of :code:`x` and
                    :code:`y`.
        
            Returns:
                :code:`true` if there are fewer than :code:`maxUlps` floating point values between the real (resp. imaginary) parts of
                :code:`x` and :code:`y`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.util.Precision.equals`
        
        
            Returns :code:`true` if, both for the real part and for the imaginary part, there is no T value strictly between the
            arguments or the difference between them is within the range of allowed error (inclusive). Returns :code:`false` if
            either of the arguments is NaN.
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): Second value (cannot be :code:`null`).
                eps (double): Amount of allowed absolute error.
        
            Returns:
                :code:`true` if the values are two adjacent floating point numbers or they are within range of each other.
        
            Also see:
        
                  - :meth:`~org.hipparchus.util.Precision.equals`
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(fieldComplex: 'FieldComplex'[_equals_3__T], fieldComplex2: 'FieldComplex'[_equals_3__T], int: int) -> bool: ...
    _equalsWithRelativeTolerance__T = typing.TypeVar('_equalsWithRelativeTolerance__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def equalsWithRelativeTolerance(fieldComplex: 'FieldComplex'[_equalsWithRelativeTolerance__T], fieldComplex2: 'FieldComplex'[_equalsWithRelativeTolerance__T], double: float) -> bool:
        """
            Returns :code:`true` if, both for the real part and for the imaginary part, there is no T value strictly between the
            arguments or the relative difference between them is smaller or equal to the given tolerance. Returns :code:`false` if
            either of the arguments is NaN.
        
            Parameters:
                x (:class:`~org.hipparchus.complex.FieldComplex`<T> x): First value (cannot be :code:`null`).
                y (:class:`~org.hipparchus.complex.FieldComplex`<T> y): Second value (cannot be :code:`null`).
                eps (double): Amount of allowed relative error.
        
            Returns:
                :code:`true` if the values are two adjacent floating point numbers or they are within range of each other.
        
            Also see:
        
                  - :meth:`~org.hipparchus.util.Precision.equalsWithRelativeTolerance`
        
        
        
        """
        ...
    def exp(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def expm1(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def floor(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def getAddendum(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def getArgument(self) -> _FieldComplex__T:
        """
            Compute the argument of this complex number. The argument is the angle phi between the positive real axis and the point
            representing this number in the complex plane. The value returned is between -PI (not inclusive) and PI (inclusive),
            with negative values returned for numbers with negative imaginary parts.
        
            If either real or imaginary part (or both) is NaN, NaN is returned. Infinite parts are handled as :code:`Math.atan2`
            handles them, essentially treating finite parts as zero in the presence of an infinite coordinate and returning a
            multiple of pi/4 depending on the signs of the infinite parts. See the javadoc for :code:`Math.atan2` for full details.
        
            Returns:
                the argument of :code:`this`.
        
        
        """
        ...
    def getField(self) -> 'FieldComplexField'[_FieldComplex__T]: ...
    _getI__T = typing.TypeVar('_getI__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getI(field: org.hipparchus.Field[_getI__T]) -> 'FieldComplex'[_getI__T]:
        """
            Get the square root of -1.
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
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
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
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
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
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
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
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
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
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
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
            Returns:
                complex number representing "1.0 + 0.0i"
        
        
        """
        ...
    def getPartsField(self) -> org.hipparchus.Field[_FieldComplex__T]: ...
    _getPi_1__T = typing.TypeVar('_getPi_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPi(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    @staticmethod
    def getPi(field: org.hipparchus.Field[_getPi_1__T]) -> 'FieldComplex'[_getPi_1__T]:
        """
            Get a complex number representing "π + 0.0i".
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
            Returns:
                complex number representing "π + 0.0i
        
        public :class:`~org.hipparchus.complex.FieldComplex`<:class:`~org.hipparchus.complex.FieldComplex`> getPi()
        
            Get the Archimedes constant π.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant π
        
        
        """
        ...
    def getReal(self) -> float:
        """
            Access the real part.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
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
                field (:class:`~org.hipparchus.Field`<T> field): field the complex components belong to
        
            Returns:
                complex number representing "0.0 + 0.0i
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the complex number. Any :code:`Double.NaN` value in real or imaginary part produces the same hash
            code :code:`7`.
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a hash code value for this object.
        
        
        """
        ...
    def hypot(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def isInfinite(self) -> bool:
        """
            Checks whether either the real or imaginary part of this complex number takes an infinite value (either
            :code:`Double.POSITIVE_INFINITY` or :code:`Double.NEGATIVE_INFINITY`) and neither part is :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isInfinite` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                true if one or both parts of this complex number are infinite and neither part is :code:`NaN`.
        
        
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
            Checks whether either or both parts of this complex number is :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isNaN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                true if either or both parts of this complex number is :code:`NaN`; false otherwise.
        
        
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
        
            The default implementation simply calls :code:`equals(getField().getZero())`. However, this may need to be overridden in
            some cases as due to compatibility with :code:`hashCode()` some classes implements :code:`equals(Object)` in such a way
            that -0.0 and +0.0 are different, which may be a problem. It prevents for example identifying a diagonal element is zero
            and should be avoided when doing partial pivoting in LU decomposition.
        
            This implementation considers +0.0 and -0.0 to be equal for both real and imaginary components.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.isZero` in interface :class:`~org.hipparchus.FieldElement`
        
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
    def log(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def log10(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def log1p(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def multiply(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def multiply(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def multiplyMinusI(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def multiplyPlusI(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def negate(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def newInstance(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    def nthRoot(self, int: int) -> java.util.List['FieldComplex'[_FieldComplex__T]]: ...
    @typing.overload
    def pow(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def pow(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def pow(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def reciprocal(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def remainder(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def remainder(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def rint(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def rootN(self, int: int) -> 'FieldComplex'[_FieldComplex__T]: ...
    def scalb(self, int: int) -> 'FieldComplex'[_FieldComplex__T]: ...
    def sign(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def sin(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldComplex'[_FieldComplex__T]]: ...
    def sinh(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldComplex'[_FieldComplex__T]]: ...
    def sqrt(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def sqrt1z(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def square(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def subtract(self, double: float) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def subtract(self, t: _FieldComplex__T) -> 'FieldComplex'[_FieldComplex__T]: ...
    @typing.overload
    def subtract(self, fieldComplex: 'FieldComplex'[_FieldComplex__T]) -> 'FieldComplex'[_FieldComplex__T]: ...
    def tan(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def tanh(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def toDegrees(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def toRadians(self) -> 'FieldComplex'[_FieldComplex__T]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    def ulp(self) -> 'FieldComplex'[_FieldComplex__T]: ...
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
    public classFieldComplexField<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.complex.FieldComplex`<T>>
    
        Representation of the complex numbers field.
    
        Since:
            2.0
    
        Also see:
    
              - :class:`~org.hipparchus.complex.FieldComplex`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    _getField__T = typing.TypeVar('_getField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getField(field: org.hipparchus.Field[_getField__T]) -> 'FieldComplexField'[_getField__T]:
        """
            Get the field for complex numbers.
        
            Parameters:
                partsField (:class:`~org.hipparchus.Field`<T> partsField): field for the real and imaginary parts
        
            Returns:
                cached field
        
        
        """
        ...
    def getOne(self) -> FieldComplex[_FieldComplexField__T]: ...
    def getRuntimeClass(self) -> typing.Type[FieldComplex[_FieldComplexField__T]]: ...
    def getZero(self) -> FieldComplex[_FieldComplexField__T]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...

_FieldComplexUnivariateIntegrator__T = typing.TypeVar('_FieldComplexUnivariateIntegrator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldComplexUnivariateIntegrator(typing.Generic[_FieldComplexUnivariateIntegrator__T]):
    """
    public classFieldComplexUnivariateIntegrator<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Wrapper to perform univariate complex integration using an underlying real integration algorithms.
    
        Since:
            2.0
    """
    def __init__(self, fieldUnivariateIntegrator: org.hipparchus.analysis.integration.FieldUnivariateIntegrator[_FieldComplexUnivariateIntegrator__T]): ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[FieldComplex[_FieldComplexUnivariateIntegrator__T]], typing.Callable[[FieldComplex[_FieldComplexUnivariateIntegrator__T]], FieldComplex[_FieldComplexUnivariateIntegrator__T]]], fieldComplex: FieldComplex[_FieldComplexUnivariateIntegrator__T], fieldComplex2: FieldComplex[_FieldComplexUnivariateIntegrator__T]) -> FieldComplex[_FieldComplexUnivariateIntegrator__T]: ...
    @typing.overload
    def integrate(self, int: int, calculusFieldUnivariateFunction: typing.Union[org.hipparchus.analysis.CalculusFieldUnivariateFunction[FieldComplex[_FieldComplexUnivariateIntegrator__T]], typing.Callable[[FieldComplex[_FieldComplexUnivariateIntegrator__T]], FieldComplex[_FieldComplexUnivariateIntegrator__T]]], fieldComplex: FieldComplex[_FieldComplexUnivariateIntegrator__T], *fieldComplex2: FieldComplex[_FieldComplexUnivariateIntegrator__T]) -> FieldComplex[_FieldComplexUnivariateIntegrator__T]: ...

class Quaternion(java.io.Serializable):
    """
    public final classQuaternion extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This class implements ` quaternions <http://mathworld.wolfram.com/Quaternion.html>` (Hamilton's hypercomplex numbers).
    
        Instance of this class are guaranteed to be immutable.
    
        Also see:
    
              - :meth:`~serialized`
    """
    IDENTITY: typing.ClassVar['Quaternion'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Quaternion` IDENTITY
    
        Identity quaternion.
    
    """
    ZERO: typing.ClassVar['Quaternion'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Quaternion` ZERO
    
        Zero quaternion.
    
    """
    I: typing.ClassVar['Quaternion'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Quaternion` I
    
        i
    
    """
    J: typing.ClassVar['Quaternion'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Quaternion` J
    
        j
    
    """
    K: typing.ClassVar['Quaternion'] = ...
    """
    public static final :class:`~org.hipparchus.complex.Quaternion` K
    
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
                q1 (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
                q2 (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
        
            Returns:
                the sum of :code:`q1` and :code:`q2`.
        
            Computes the sum of the instance and another quaternion.
        
            Parameters:
                q (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
        
            Returns:
                the sum of this instance and :code:`q`
        
        
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
                q1 (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
                q2 (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
        
            Returns:
                the dot product of :code:`q1` and :code:`q2`.
        
            Computes the dot-product of the instance by a quaternion.
        
            Parameters:
                q (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
        
            Returns:
                the dot product of this instance and :code:`q`.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def dotProduct(quaternion: 'Quaternion', quaternion2: 'Quaternion') -> float: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Checks whether this instance is equal to another quaternion within a given tolerance.
        
            Parameters:
                q (:class:`~org.hipparchus.complex.Quaternion`): Quaternion with which to compare the current quaternion.
                eps (double): Tolerance.
        
            Returns:
                :code:`true` if the each of the components are equal within the allowed absolute error.
        
        
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
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the norm (squared) of the quaternion is zero.
        
        
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
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.Quaternion.getQ0`
        
        
        
        """
        ...
    def getVectorPart(self) -> typing.MutableSequence[float]:
        """
            Gets the three components of the vector part of the quaternion.
        
            Returns:
                the vector part.
        
            Also see:
        
                  - :meth:`~org.hipparchus.complex.Quaternion.getQ1`
                  - :meth:`~org.hipparchus.complex.Quaternion.getQ2`
                  - :meth:`~org.hipparchus.complex.Quaternion.getQ3`
        
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    def isPureQuaternion(self, double: float) -> bool:
        """
            Checks whether the instance is a pure quaternion within a given tolerance.
        
            Parameters:
                eps (double): Tolerance (absolute error).
        
            Returns:
                :code:`true` if the scalar part of the quaternion is zero.
        
        
        """
        ...
    def isUnitQuaternion(self, double: float) -> bool:
        """
            Checks whether the instance is a unit quaternion within a given tolerance.
        
            Parameters:
                eps (double): Tolerance (absolute error).
        
            Returns:
                :code:`true` if the norm is 1 within the given tolerance, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Quaternion':
        """
            Returns the Hamilton product of two quaternions.
        
            Parameters:
                q1 (:class:`~org.hipparchus.complex.Quaternion`): First quaternion.
                q2 (:class:`~org.hipparchus.complex.Quaternion`): Second quaternion.
        
            Returns:
                the product :code:`q1` and :code:`q2`, in that order.
        
            Returns the Hamilton product of the instance by a quaternion.
        
            Parameters:
                q (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
        
            Returns:
                the product of this instance with :code:`q`, in that order.
        
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
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the norm of the quaternion is zero.
        
        
        """
        ...
    @typing.overload
    def subtract(self, quaternion: 'Quaternion') -> 'Quaternion':
        """
            Subtracts two quaternions.
        
            Parameters:
                q1 (:class:`~org.hipparchus.complex.Quaternion`): First Quaternion.
                q2 (:class:`~org.hipparchus.complex.Quaternion`): Second quaternion.
        
            Returns:
                the difference between :code:`q1` and :code:`q2`.
        
            Subtracts a quaternion from the instance.
        
            Parameters:
                q (:class:`~org.hipparchus.complex.Quaternion`): Quaternion.
        
            Returns:
                the difference between this instance and :code:`q`.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtract(quaternion: 'Quaternion', quaternion2: 'Quaternion') -> 'Quaternion': ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...

class RootsOfUnity(java.io.Serializable):
    """
    public classRootsOfUnity extends :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.complex.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        A helper class for the computation and caching of the :code:`n`-th roots of unity.
    
        Also see:
    
              - :meth:`~serialized`
    """
    def __init__(self): ...
    def computeRoots(self, int: int) -> None: ...
    def getImaginary(self, int: int) -> float: ...
    def getNumberOfRoots(self) -> int:
        """
            Returns the number of roots of unity currently stored.
        
            If :meth:`~org.hipparchus.complex.RootsOfUnity.computeRoots` was called with :code:`n`, then this method returns
            :code:`abs(n)`. If no roots of unity have been computed yet, this method returns 0.
        
            Returns:
                the number of roots of unity currently stored
        
        
        """
        ...
    def getReal(self, int: int) -> float: ...
    def isCounterClockWise(self) -> bool: ...


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
