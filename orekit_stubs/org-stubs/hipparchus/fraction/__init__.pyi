
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.math
import java.text
import java.util
import java.util.stream
import org
import org.hipparchus
import org.hipparchus.util
import typing



class BigFraction(java.lang.Number, org.hipparchus.FieldElement['BigFraction'], java.lang.Comparable['BigFraction'], java.io.Serializable):
    """
    public classBigFraction extends :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
    implements :class:`~org.hipparchus.FieldElement`<:class:`~org.hipparchus.fraction.BigFraction`>, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable`<:class:`~org.hipparchus.fraction.BigFraction`>, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Representation of a rational number without any overflow. This class is immutable.
    
        Also see:
    
              - :meth:`~serialized`
    """
    TWO: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` TWO
    
        A fraction representing "2 / 1".
    
    """
    ONE: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` ONE
    
        A fraction representing "1".
    
    """
    ZERO: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` ZERO
    
        A fraction representing "0".
    
    """
    MINUS_ONE: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` MINUS_ONE
    
        A fraction representing "-1 / 1".
    
    """
    FOUR_FIFTHS: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` FOUR_FIFTHS
    
        A fraction representing "4/5".
    
    """
    ONE_FIFTH: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` ONE_FIFTH
    
        A fraction representing "1/5".
    
    """
    ONE_HALF: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` ONE_HALF
    
        A fraction representing "1/2".
    
    """
    ONE_QUARTER: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` ONE_QUARTER
    
        A fraction representing "1/4".
    
    """
    ONE_THIRD: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` ONE_THIRD
    
        A fraction representing "1/3".
    
    """
    THREE_FIFTHS: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` THREE_FIFTHS
    
        A fraction representing "3/5".
    
    """
    THREE_QUARTERS: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` THREE_QUARTERS
    
        A fraction representing "3/4".
    
    """
    TWO_FIFTHS: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` TWO_FIFTHS
    
        A fraction representing "2/5".
    
    """
    TWO_QUARTERS: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` TWO_QUARTERS
    
        A fraction representing "2/4".
    
    """
    TWO_THIRDS: typing.ClassVar['BigFraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.BigFraction` TWO_THIRDS
    
        A fraction representing "2/3".
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, long: int): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def __init__(self, long: int, long2: int): ...
    def abs(self) -> 'BigFraction':
        """
        
            Returns the absolute value of this :class:`~org.hipparchus.fraction.BigFraction`.
        
            Returns:
                the absolute value as a :class:`~org.hipparchus.fraction.BigFraction`.
        
        
        """
        ...
    @typing.overload
    def add(self, int: int) -> 'BigFraction':
        """
        
            Adds the value of this fraction to the passed :code:`integer`, returning the result in reduced form.
        
            Parameters:
                i (int): the :code:`integer` to add.
        
            Returns:
                a :code:`BigFraction` instance with the resulting values.
        
        
            Adds the value of this fraction to the passed :code:`long`, returning the result in reduced form.
        
            Parameters:
                l (long): the :code:`long` to add.
        
            Returns:
                a :code:`BigFraction` instance with the resulting values.
        
        
            Adds the value of this fraction to another, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.BigFraction`): the :class:`~org.hipparchus.fraction.BigFraction` to add, must not be :code:`null`.
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values.
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the :class:`~org.hipparchus.fraction.BigFraction` is :code:`null`.
        
        
        """
        ...
    @typing.overload
    def add(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def add(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def add(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    @typing.overload
    def bigDecimalValue(self) -> java.math.BigDecimal:
        """
        
            Gets the fraction as a :code:`BigDecimal`. This calculates the fraction as the numerator divided by denominator.
        
            Returns:
                the fraction as a :code:`BigDecimal`.
        
            Raises:
                :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.ArithmeticException`: if the exact quotient does not have a terminating decimal expansion.
        
            Also see:
        
                  - :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal`
        
        
        """
        ...
    @typing.overload
    def bigDecimalValue(self, int: int, roundingMode: java.math.RoundingMode) -> java.math.BigDecimal:
        """
        
            Gets the fraction as a :code:`BigDecimal` following the passed scale and rounding mode. This calculates the fraction as
            the numerator divided by denominator.
        
            Parameters:
                scale (int): scale of the :code:`BigDecimal` quotient to be returned. see
                    :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal` for more information.
                roundingMode (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.RoundingMode`): rounding mode to apply. see
                    :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal` constants.
        
            Returns:
                the fraction as a :code:`BigDecimal`.
        
            Also see:
        
                  - :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal`
        
        
        
        """
        ...
    @typing.overload
    def bigDecimalValue(self, roundingMode: java.math.RoundingMode) -> java.math.BigDecimal:
        """
        
            Gets the fraction as a :code:`BigDecimal` following the passed rounding mode. This calculates the fraction as the
            numerator divided by denominator.
        
            Parameters:
                roundingMode (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.RoundingMode`): rounding mode to apply. see
                    :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal` constants.
        
            Returns:
                the fraction as a :code:`BigDecimal`.
        
            Raises:
                :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if :code:`roundingMode` does not represent a valid rounding mode.
        
            Also see:
        
                  - :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal`
        
        
        """
        ...
    def compareTo(self, bigFraction: 'BigFraction') -> int:
        """
        
            Compares this object to another based on size.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.compareTo` in
                interface :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable`
        
            Parameters:
                object (:class:`~org.hipparchus.fraction.BigFraction`): the object to compare to, must not be :code:`null`.
        
            Returns:
                -1 if this is less than :code:`object`, +1 if this is greater than :code:`object`, 0 if they are equal.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.compareTo`
        
        
        
        """
        ...
    @staticmethod
    def convergent(double: float, int: int, convergenceTest: typing.Union['BigFraction.ConvergenceTest', typing.Callable]) -> org.hipparchus.util.Pair['BigFraction', bool]: ...
    @staticmethod
    def convergents(double: float, int: int) -> java.util.stream.Stream['BigFraction']: ...
    @typing.overload
    def divide(self, int: int) -> 'BigFraction':
        """
        
            Divide the value of this fraction by the passed :code:`BigInteger`, ie :code:`this * 1 / bg`, returning the result in
            reduced form.
        
            Parameters:
                bg (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger`): the :code:`BigInteger` to divide by, must not be :code:`null`
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the :code:`BigInteger` is :code:`null`
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the fraction to divide by is zero
        
        
            Divide the value of this fraction by the passed :code:`int`, ie :code:`this * 1 / i`, returning the result in reduced
            form.
        
            Parameters:
                i (int): the :code:`int` to divide by
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the fraction to divide by is zero
        
        
            Divide the value of this fraction by the passed :code:`long`, ie :code:`this * 1 / l`, returning the result in reduced
            form.
        
            Parameters:
                l (long): the :code:`long` to divide by
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the fraction to divide by is zero
        
        
            Divide the value of this fraction by another, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.BigFraction`): Fraction to divide by, must not be :code:`null`.
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values.
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the :code:`fraction` is :code:`null`.
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the fraction to divide by is zero
        
        
        """
        ...
    @typing.overload
    def divide(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def divide(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def divide(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    def doubleValue(self) -> float:
        """
        
            Gets the fraction as a :code:`double`. This calculates the fraction as the numerator divided by denominator.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.doubleValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the fraction as a :code:`double`
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.doubleValue`
        
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Test for the equality of two fractions. If the lowest term numerator and denominators are the same for both fractions,
            the two fractions are considered to be equal.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): fraction to test for equality to this fraction, can be :code:`null`.
        
            Returns:
                true if two fractions are equal, false if object is :code:`null`, not an instance of
                :class:`~org.hipparchus.fraction.BigFraction`, or not equal to this fraction instance.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals`
        
        
        
        """
        ...
    def floatValue(self) -> float:
        """
        
            Gets the fraction as a :code:`float`. This calculates the fraction as the numerator divided by denominator.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.floatValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the fraction as a :code:`float`.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.floatValue`
        
        
        
        """
        ...
    def gcd(self, bigFraction: 'BigFraction') -> 'BigFraction':
        """
            Rational number greatest common divisor.
        
            Parameters:
                s (:class:`~org.hipparchus.fraction.BigFraction`): fraction.
        
            Returns:
                gcd(this, s).
        
            Since:
                3.1
        
        
        """
        ...
    def getDenominator(self) -> java.math.BigInteger:
        """
        
            Access the denominator as a :code:`BigInteger`.
        
            Returns:
                the denominator as a :code:`BigInteger`.
        
        
        """
        ...
    def getDenominatorAsInt(self) -> int:
        """
        
            Access the denominator as a :code:`int`.
        
            Returns:
                the denominator as a :code:`int`.
        
        
        """
        ...
    def getDenominatorAsLong(self) -> int:
        """
        
            Access the denominator as a :code:`long`.
        
            Returns:
                the denominator as a :code:`long`.
        
        
        """
        ...
    def getField(self) -> 'BigFractionField':
        """
            Get the :class:`~org.hipparchus.Field` to which the instance belongs.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getField` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                :class:`~org.hipparchus.Field` to which the instance belongs
        
        
        """
        ...
    def getNumerator(self) -> java.math.BigInteger:
        """
        
            Access the numerator as a :code:`BigInteger`.
        
            Returns:
                the numerator as a :code:`BigInteger`.
        
        
        """
        ...
    def getNumeratorAsInt(self) -> int:
        """
        
            Access the numerator as a :code:`int`.
        
            Returns:
                the numerator as a :code:`int`.
        
        
        """
        ...
    def getNumeratorAsLong(self) -> int:
        """
        
            Access the numerator as a :code:`long`.
        
            Returns:
                the numerator as a :code:`long`.
        
        
        """
        ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    @staticmethod
    def getReducedFraction(int: int, int2: int) -> 'BigFraction':
        """
        
            Creates a :code:`BigFraction` instance with the 2 parts of a fraction Y/Z.
        
            Any negative signs are resolved to be on the numerator.
        
            Parameters:
                numerator (int): the numerator, for example the three in 'three sevenths'.
                denominator (int): the denominator, for example the seven in 'three sevenths'.
        
            Returns:
                a new fraction instance, with the numerator and denominator reduced.
        
            Raises:
                :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.ArithmeticException`: if the denominator is :code:`zero`.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Gets a hashCode for the fraction.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a hash code value for this object.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode`
        
        
        
        """
        ...
    def intValue(self) -> int:
        """
        
            Gets the fraction as an :code:`int`. This returns the whole number part of the fraction.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.intValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the whole number fraction part.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.intValue`
        
        
        
        """
        ...
    def isInteger(self) -> bool:
        """
            Check if a fraction is an integer.
        
            Returns:
                true of fraction is an integer
        
        
        """
        ...
    def lcm(self, bigFraction: 'BigFraction') -> 'BigFraction':
        """
            Rational number least common multiple.
        
            Parameters:
                s (:class:`~org.hipparchus.fraction.BigFraction`): fraction.
        
            Returns:
                lcm(this, s).
        
            Since:
                3.1
        
        
        """
        ...
    def longValue(self) -> int:
        """
        
            Gets the fraction as a :code:`long`. This returns the whole number part of the fraction.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.longValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the whole number fraction part.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.longValue`
        
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'BigFraction':
        """
        
            Multiplies the value of this fraction by the passed :code:`BigInteger`, returning the result in reduced form.
        
            Parameters:
                bg (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger`): the :code:`BigInteger` to multiply by.
        
            Returns:
                a :code:`BigFraction` instance with the resulting values.
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if :code:`bg` is :code:`null`.
        
        
            Multiply the value of this fraction by the passed :code:`int`, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                i (int): the :code:`int` to multiply by.
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values.
        
        
            Multiply the value of this fraction by the passed :code:`long`, returning the result in reduced form.
        
            Parameters:
                l (long): the :code:`long` to multiply by.
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values.
        
        
            Multiplies the value of this fraction by another, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.BigFraction`): Fraction to multiply by, must not be :code:`null`.
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values.
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if :code:`fraction` is :code:`null`.
        
        
        """
        ...
    @typing.overload
    def multiply(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def multiply(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def multiply(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    def negate(self) -> 'BigFraction':
        """
        
            Return the additive inverse of this fraction, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the negation of this fraction.
        
        
        """
        ...
    def percentageValue(self) -> float:
        """
        
            Gets the fraction percentage as a :code:`double`. This calculates the fraction as the numerator divided by denominator
            multiplied by 100.
        
            Returns:
                the fraction percentage as a :code:`double`.
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> float:
        """
        
            Returns a :code:`BigFraction` whose value is :code:`(this<sup>exponent</sup>)`, returning the result in reduced form.
        
            Parameters:
                exponent (int): exponent to which this :code:`BigFraction` is to be raised.
        
            Returns:
                this :sup:`exponent`
        
        
            Returns a :code:`BigFraction` whose value is this :sup:`exponent` , returning the result in reduced form.
        
            Parameters:
                exponent (long): exponent to which this :code:`BigFraction` is to be raised.
        
            Returns:
                this :sup:`exponent` as a :code:`BigFraction`.
        
        
            Returns a :code:`BigFraction` whose value is this :sup:`exponent` , returning the result in reduced form.
        
            Parameters:
                exponent (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger`): exponent to which this :code:`BigFraction` is to be raised.
        
            Returns:
                this :sup:`exponent` as a :code:`BigFraction`.
        
        
            Returns a :code:`double` whose value is this :sup:`exponent` , returning the result in reduced form.
        
            Parameters:
                exponent (double): exponent to which this :code:`BigFraction` is to be raised.
        
            Returns:
                this :sup:`exponent`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'BigFraction': ...
    @typing.overload
    def pow(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def pow(self, long: int) -> 'BigFraction': ...
    def reciprocal(self) -> 'BigFraction':
        """
        
            Return the multiplicative inverse of this fraction.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the reciprocal fraction.
        
        
        """
        ...
    def reduce(self) -> 'BigFraction':
        """
        
            Reduce this :code:`BigFraction` to its lowest terms.
        
            Returns:
                the reduced :code:`BigFraction`. It doesn't change anything if the fraction can be reduced.
        
        
        """
        ...
    def signum(self) -> int:
        """
            Returns the signum function of this :class:`~org.hipparchus.fraction.BigFraction`.
        
            The return value is -1 if the specified value is negative; 0 if the specified value is zero; and 1 if the specified
            value is positive.
        
            Returns:
                the signum function of this :class:`~org.hipparchus.fraction.BigFraction`
        
            Since:
                1.7
        
        
        """
        ...
    @typing.overload
    def subtract(self, int: int) -> 'BigFraction':
        """
        
            Subtracts the value of an
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger` from the value of this
            :code:`BigFraction`, returning the result in reduced form.
        
            Parameters:
                bg (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger`): the :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger` to subtract, cannot
                    be :code:`null`.
        
            Returns:
                a :code:`BigFraction` instance with the resulting values.
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger` is :code:`null`.
        
        
            Subtracts the value of an :code:`integer` from the value of this :code:`BigFraction`, returning the result in reduced
            form.
        
            Parameters:
                i (int): the :code:`integer` to subtract.
        
            Returns:
                a :code:`BigFraction` instance with the resulting values.
        
        
            Subtracts the value of a :code:`long` from the value of this :code:`BigFraction`, returning the result in reduced form.
        
            Parameters:
                l (long): the :code:`long` to subtract.
        
            Returns:
                a :code:`BigFraction` instance with the resulting values.
        
        
            Subtracts the value of another fraction from the value of this one, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.BigFraction`): :class:`~org.hipparchus.fraction.BigFraction` to subtract, must not be :code:`null`.
        
            Returns:
                a :class:`~org.hipparchus.fraction.BigFraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the :code:`fraction` is :code:`null`.
        
        
        """
        ...
    @typing.overload
    def subtract(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def subtract(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def subtract(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    def toString(self) -> str:
        """
        
            Returns the :code:`String` representing this fraction, ie "num / dem" or just "num" if the denominator is one.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a string representation of the fraction.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString`
        
        
        
        """
        ...
    class ConvergenceTest:
        def test(self, long: int, long2: int) -> bool: ...

class BigFractionField(org.hipparchus.Field[BigFraction], java.io.Serializable):
    """
    public classBigFractionField extends :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.fraction.BigFraction`>, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Representation of the fractional numbers without any overflow field.
    
        This class is a singleton.
    
        Also see:
    
              - :class:`~org.hipparchus.fraction.Fraction`
              - :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'BigFractionField':
        """
            Get the unique instance.
        
            Returns:
                the unique instance
        
        
        """
        ...
    def getOne(self) -> BigFraction:
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
    def getRuntimeClass(self) -> typing.Type[BigFraction]: ...
    def getZero(self) -> BigFraction:
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
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...

class Fraction(java.lang.Number, org.hipparchus.FieldElement['Fraction'], java.lang.Comparable['Fraction'], java.io.Serializable):
    """
    public classFraction extends :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
    implements :class:`~org.hipparchus.FieldElement`<:class:`~org.hipparchus.fraction.Fraction`>, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable`<:class:`~org.hipparchus.fraction.Fraction`>, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Representation of a rational number.
    
        Also see:
    
              - :meth:`~serialized`
    """
    TWO: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` TWO
    
        A fraction representing "2 / 1".
    
    """
    ONE: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` ONE
    
        A fraction representing "1".
    
    """
    ZERO: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` ZERO
    
        A fraction representing "0".
    
    """
    FOUR_FIFTHS: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` FOUR_FIFTHS
    
        A fraction representing "4/5".
    
    """
    ONE_FIFTH: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` ONE_FIFTH
    
        A fraction representing "1/5".
    
    """
    ONE_HALF: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` ONE_HALF
    
        A fraction representing "1/2".
    
    """
    ONE_QUARTER: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` ONE_QUARTER
    
        A fraction representing "1/4".
    
    """
    ONE_THIRD: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` ONE_THIRD
    
        A fraction representing "1/3".
    
    """
    THREE_FIFTHS: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` THREE_FIFTHS
    
        A fraction representing "3/5".
    
    """
    THREE_QUARTERS: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` THREE_QUARTERS
    
        A fraction representing "3/4".
    
    """
    TWO_FIFTHS: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` TWO_FIFTHS
    
        A fraction representing "2/5".
    
    """
    TWO_QUARTERS: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` TWO_QUARTERS
    
        A fraction representing "2/4".
    
    """
    TWO_THIRDS: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` TWO_THIRDS
    
        A fraction representing "2/3".
    
    """
    MINUS_ONE: typing.ClassVar['Fraction'] = ...
    """
    public static final :class:`~org.hipparchus.fraction.Fraction` MINUS_ONE
    
        A fraction representing "-1 / 1".
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, double: float, int: int): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    def abs(self) -> 'Fraction':
        """
            Returns the absolute value of this fraction.
        
            Returns:
                the absolute value.
        
        
        """
        ...
    @typing.overload
    def add(self, int: int) -> 'Fraction':
        """
            Adds the value of this fraction to another, returning the result in reduced form. The algorithm follows Knuth, 4.5.1.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.Fraction`): the fraction to add, must not be :code:`null`
        
            Returns:
                a :code:`Fraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the fraction is :code:`null`
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the resulting numerator or denominator exceeds :code:`Integer.MAX_VALUE`
        
            Add an integer to the fraction.
        
            Parameters:
                i (int): the :code:`integer` to add.
        
            Returns:
                this + i
        
        
        """
        ...
    @typing.overload
    def add(self, fraction: 'Fraction') -> 'Fraction': ...
    def compareTo(self, fraction: 'Fraction') -> int:
        """
            Compares this object to another based on size.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.compareTo` in
                interface :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable`
        
            Parameters:
                object (:class:`~org.hipparchus.fraction.Fraction`): the object to compare to
        
            Returns:
                -1 if this is less than :code:`object`, +1 if this is greater than :code:`object`, 0 if they are equal.
        
        
        """
        ...
    @staticmethod
    def convergent(double: float, int: int, convergenceTest: typing.Union['Fraction.ConvergenceTest', typing.Callable]) -> org.hipparchus.util.Pair['Fraction', bool]: ...
    @staticmethod
    def convergents(double: float, int: int) -> java.util.stream.Stream['Fraction']: ...
    @typing.overload
    def divide(self, int: int) -> 'Fraction':
        """
            Divide the value of this fraction by another.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.Fraction`): the fraction to divide by, must not be :code:`null`
        
            Returns:
                a :code:`Fraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if the fraction is :code:`null`
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the fraction to divide by is zero
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the resulting numerator or denominator exceeds :code:`Integer.MAX_VALUE`
        
            Divide the fraction by an integer.
        
            Parameters:
                i (int): the :code:`integer` to divide by.
        
            Returns:
                this * i
        
        
        """
        ...
    @typing.overload
    def divide(self, fraction: 'Fraction') -> 'Fraction': ...
    def doubleValue(self) -> float:
        """
            Gets the fraction as a :code:`double`. This calculates the fraction as the numerator divided by denominator.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.doubleValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the fraction as a :code:`double`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two fractions. If the lowest term numerator and denominators are the same for both fractions,
            the two fractions are considered to be equal.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): fraction to test for equality to this fraction
        
            Returns:
                true if two fractions are equal, false if object is :code:`null`, not an instance of
                :class:`~org.hipparchus.fraction.Fraction`, or not equal to this fraction instance.
        
        
        """
        ...
    def floatValue(self) -> float:
        """
            Gets the fraction as a :code:`float`. This calculates the fraction as the numerator divided by denominator.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.floatValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the fraction as a :code:`float`
        
        
        """
        ...
    def gcd(self, fraction: 'Fraction') -> 'Fraction':
        """
            Rational number greatest common divisor.
        
            Parameters:
                s (:class:`~org.hipparchus.fraction.Fraction`): fraction.
        
            Returns:
                gcd(this, s).
        
            Since:
                3.1
        
        
        """
        ...
    def getDenominator(self) -> int:
        """
            Access the denominator.
        
            Returns:
                the denominator.
        
        
        """
        ...
    def getField(self) -> 'FractionField':
        """
            Get the :class:`~org.hipparchus.Field` to which the instance belongs.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getField` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                :class:`~org.hipparchus.Field` to which the instance belongs
        
        
        """
        ...
    def getNumerator(self) -> int:
        """
            Access the numerator.
        
            Returns:
                the numerator.
        
        
        """
        ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    @staticmethod
    def getReducedFraction(int: int, int2: int) -> 'Fraction':
        """
            Creates a :code:`Fraction` instance with the 2 parts of a fraction Y/Z.
        
            Any negative signs are resolved to be on the numerator.
        
            Parameters:
                numerator (int): the numerator, for example the three in 'three sevenths'
                denominator (int): the denominator, for example the seven in 'three sevenths'
        
            Returns:
                a new fraction instance, with the numerator and denominator reduced
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the denominator is :code:`zero`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Gets a hashCode for the fraction.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def intValue(self) -> int:
        """
            Gets the fraction as an :code:`int`. This returns the whole number part of the fraction.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.intValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the whole number fraction part
        
        
        """
        ...
    def isInteger(self) -> bool:
        """
            Check if a fraction is an integer.
        
            Returns:
                true of fraction is an integer
        
        
        """
        ...
    def lcm(self, fraction: 'Fraction') -> 'Fraction':
        """
            Rational number least common multiple.
        
            Parameters:
                s (:class:`~org.hipparchus.fraction.Fraction`): fraction.
        
            Returns:
                lcm(this, s).
        
            Since:
                3.1
        
        
        """
        ...
    def longValue(self) -> int:
        """
            Gets the fraction as a :code:`long`. This returns the whole number part of the fraction.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.longValue` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number`
        
            Returns:
                the whole number fraction part
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'Fraction':
        """
            Multiplies the value of this fraction by another, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.Fraction`): the fraction to multiply by, must not be :code:`null`
        
            Returns:
                a :code:`Fraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the fraction is :code:`null`
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the resulting numerator or denominator exceeds :code:`Integer.MAX_VALUE`
        
            Multiply the fraction by an integer.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                i (int): the :code:`integer` to multiply by.
        
            Returns:
                this * i
        
        
        """
        ...
    @typing.overload
    def multiply(self, fraction: 'Fraction') -> 'Fraction': ...
    def negate(self) -> 'Fraction':
        """
            Return the additive inverse of this fraction.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the negation of this fraction.
        
        
        """
        ...
    def percentageValue(self) -> float:
        """
            Gets the fraction percentage as a :code:`double`. This calculates the fraction as the numerator divided by denominator
            multiplied by 100.
        
            Returns:
                the fraction percentage as a :code:`double`.
        
        
        """
        ...
    def reciprocal(self) -> 'Fraction':
        """
            Return the multiplicative inverse of this fraction.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the reciprocal fraction
        
        
        """
        ...
    def signum(self) -> int:
        """
            Returns the signum function of this fraction.
        
            The return value is -1 if the specified value is negative; 0 if the specified value is zero; and 1 if the specified
            value is positive.
        
            Returns:
                the signum function of this fraction
        
            Since:
                1.7
        
        
        """
        ...
    @typing.overload
    def subtract(self, int: int) -> 'Fraction':
        """
            Subtracts the value of another fraction from the value of this one, returning the result in reduced form.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.Fraction`): the fraction to subtract, must not be :code:`null`
        
            Returns:
                a :code:`Fraction` instance with the resulting values
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if the fraction is :code:`null`
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the resulting numerator or denominator cannot be represented in an :code:`int`.
        
            Subtract an integer from the fraction.
        
            Parameters:
                i (int): the :code:`integer` to subtract.
        
            Returns:
                this - i
        
        
        """
        ...
    @typing.overload
    def subtract(self, fraction: 'Fraction') -> 'Fraction': ...
    def toString(self) -> str:
        """
            Returns the :code:`String` representing this fraction, ie "num / dem" or just "num" if the denominator is one.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a string representation of the fraction.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString`
        
        
        
        """
        ...
    class ConvergenceTest:
        def test(self, int: int, int2: int) -> bool: ...

class FractionField(org.hipparchus.Field[Fraction], java.io.Serializable):
    """
    public classFractionField extends :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.fraction.Fraction`>, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Representation of the fractional numbers field.
    
        This class is a singleton.
    
        Also see:
    
              - :class:`~org.hipparchus.fraction.Fraction`
              - :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'FractionField':
        """
            Get the unique instance.
        
            Returns:
                the unique instance
        
        
        """
        ...
    def getOne(self) -> Fraction:
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
    def getRuntimeClass(self) -> typing.Type[Fraction]: ...
    def getZero(self) -> Fraction:
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
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...

class BigFractionFormat(org.hipparchus.fraction.AbstractFormat, java.io.Serializable):
    """
    public classBigFractionFormat extends :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
    implements :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        Formats a BigFraction number in proper format or improper format.
    
        The number format for each of the whole number, numerator and, denominator can be configured.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
            Formats a :class:`~org.hipparchus.fraction.BigFraction` object to produce a string. The BigFraction is output in
            improper format.
        
            Parameters:
                BigFraction (:class:`~org.hipparchus.fraction.BigFraction`): the object to format.
                toAppendTo (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
            Formats an object and appends the result to a StringBuffer. :code:`obj` must be either a
            :class:`~org.hipparchus.fraction.BigFraction` object or a
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.math.BigInteger` object or a
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number` object. Any other type of
            object will result in an
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException` being
            thrown.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                obj (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): the object to format.
                toAppendTo (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`obj` is not a valid type.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.Format.format`
        
        
            Formats a double value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (double): the double value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
            Formats a long value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (long): the long value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
        
        """
        ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, bigFraction: BigFraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def formatBigFraction(bigFraction: BigFraction) -> str:
        """
            This static method calls formatBigFraction() on a default instance of BigFractionFormat.
        
            Parameters:
                f (:class:`~org.hipparchus.fraction.BigFraction`): BigFraction object to format
        
            Returns:
                A formatted BigFraction in proper form.
        
        
        """
        ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
            Get the set of locales for which complex formats are available. This is the same set as the
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat` set.
        
            Returns:
                available complex format locales.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance() -> 'BigFractionFormat':
        """
            Returns the default complex format for the current locale.
        
            Returns:
                the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance(locale: java.util.Locale) -> 'BigFractionFormat':
        """
            Returns the default complex format for the given locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale`): the specific locale used by the format.
        
            Returns:
                the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance() -> 'BigFractionFormat':
        """
            Returns the default complex format for the current locale.
        
            Returns:
                the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance(locale: java.util.Locale) -> 'BigFractionFormat':
        """
            Returns the default complex format for the given locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale`): the specific locale used by the format.
        
            Returns:
                the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> BigFraction:
        """
            Parses a string to produce a :class:`~org.hipparchus.fraction.BigFraction` object. This method expects the string to be
            formatted as an improper BigFraction.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.parse` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                source (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the string to parse
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition`): input/output parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.fraction.BigFraction` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> BigFraction: ...

class FractionFormat(org.hipparchus.fraction.AbstractFormat):
    """
    public classFractionFormat extends :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
    
        Formats a Fraction number in proper format or improper format.
    
        The number format for each of the whole number, numerator and, denominator can be configured.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
            Formats a :class:`~org.hipparchus.fraction.Fraction` object to produce a string. The fraction is output in improper
            format.
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.Fraction`): the object to format.
                toAppendTo (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
        public :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer` format(:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object` obj, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer` toAppendTo, :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition` pos) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`, :class:`~org.hipparchus.exception.MathIllegalStateException`
        
            Formats an object and appends the result to a StringBuffer. :code:`obj` must be either a
            :class:`~org.hipparchus.fraction.Fraction` object or a
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number` object. Any other type of
            object will result in an
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException` being
            thrown.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                obj (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): the object to format.
                toAppendTo (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the number cannot be converted to a fraction
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`obj` is not a valid type.
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.Format.format`
        
        
            Formats a double value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (double): the double value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
            Formats a long value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (long): the long value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
        
        """
        ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, fraction: Fraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def formatFraction(fraction: Fraction) -> str:
        """
            This static method calls formatFraction() on a default instance of FractionFormat.
        
            Parameters:
                f (:class:`~org.hipparchus.fraction.Fraction`): Fraction object to format
        
            Returns:
                a formatted fraction in proper form.
        
        
        """
        ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
            Get the set of locales for which complex formats are available. This is the same set as the
            :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat` set.
        
            Returns:
                available complex format locales.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance() -> 'FractionFormat':
        """
            Returns the default complex format for the current locale.
        
            Returns:
                the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance(locale: java.util.Locale) -> 'FractionFormat':
        """
            Returns the default complex format for the given locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale`): the specific locale used by the format.
        
            Returns:
                the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance() -> 'FractionFormat':
        """
            Returns the default complex format for the current locale.
        
            Returns:
                the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance(locale: java.util.Locale) -> 'FractionFormat':
        """
            Returns the default complex format for the given locale.
        
            Parameters:
                locale (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale`): the specific locale used by the format.
        
            Returns:
                the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Fraction:
        """
            Parses a string to produce a :class:`~org.hipparchus.fraction.Fraction` object. This method expects the string to be
            formatted as an improper fraction.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.parse` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                source (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the string to parse
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition`): input/output parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.fraction.Fraction` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Fraction: ...

class ProperBigFractionFormat(BigFractionFormat):
    """
    public classProperBigFractionFormat extends :class:`~org.hipparchus.fraction.BigFractionFormat`
    
        Formats a BigFraction number in proper format. The number format for each of the whole number, numerator and,
        denominator can be configured.
    
        Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is
        invalid and will result in a :code:`ParseException`.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat, numberFormat3: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
            Formats a :class:`~org.hipparchus.fraction.BigFraction` object to produce a string. The BigFraction is output in proper
            format.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.BigFractionFormat.format` in class :class:`~org.hipparchus.fraction.BigFractionFormat`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.BigFraction`): the object to format.
                toAppendTo (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
            Formats a double value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (double): the double value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
            Formats a long value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (long): the long value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
        
        """
        ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, bigFraction: BigFraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    def getWholeFormat(self) -> java.text.NumberFormat:
        """
            Access the whole format.
        
            Returns:
                the whole format.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> BigFraction:
        """
            Parses a string to produce a :class:`~org.hipparchus.fraction.BigFraction` object. This method expects the string to be
            formatted as a proper BigFraction.
        
            Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is
            invalid and will result in a :code:`ParseException`.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.BigFractionFormat.parse` in class :class:`~org.hipparchus.fraction.BigFractionFormat`
        
            Parameters:
                source (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the string to parse
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition`): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.fraction.BigFraction` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> BigFraction: ...

class ProperFractionFormat(FractionFormat):
    """
    public classProperFractionFormat extends :class:`~org.hipparchus.fraction.FractionFormat`
    
        Formats a Fraction number in proper format. The number format for each of the whole number, numerator and, denominator
        can be configured.
    
        Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is
        invalid and will result in a :code:`ParseException`.
    
        Also see:
    
              - :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat, numberFormat3: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
            Formats a :class:`~org.hipparchus.fraction.Fraction` object to produce a string. The fraction is output in proper
            format.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.FractionFormat.format` in class :class:`~org.hipparchus.fraction.FractionFormat`
        
            Parameters:
                fraction (:class:`~org.hipparchus.fraction.Fraction`): the object to format.
                toAppendTo (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
            Formats a double value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (double): the double value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
            Formats a long value as a fraction and appends the result to a StringBuffer.
        
            Specified by:
                :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format` in
                class :class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`
        
            Parameters:
                value (long): the long value to format
                buffer (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): StringBuffer to append to
                position (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                a reference to the appended buffer
        
            Also see:
        
                  - :meth:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.format`
        
        
        
        """
        ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, fraction: Fraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    def getWholeFormat(self) -> java.text.NumberFormat:
        """
            Access the whole format.
        
            Returns:
                the whole format.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> Fraction:
        """
            Parses a string to produce a :class:`~org.hipparchus.fraction.Fraction` object. This method expects the string to be
            formatted as a proper fraction.
        
            Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is
            invalid and will result in a :code:`ParseException`.
        
            Overrides:
                :meth:`~org.hipparchus.fraction.FractionFormat.parse` in class :class:`~org.hipparchus.fraction.FractionFormat`
        
            Parameters:
                source (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the string to parse
                pos (:class:`~org.hipparchus.fraction.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition`): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.fraction.Fraction` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Fraction: ...

class AbstractFormat: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.fraction")``.

    AbstractFormat: typing.Type[AbstractFormat]
    BigFraction: typing.Type[BigFraction]
    BigFractionField: typing.Type[BigFractionField]
    BigFractionFormat: typing.Type[BigFractionFormat]
    Fraction: typing.Type[Fraction]
    FractionField: typing.Type[FractionField]
    FractionFormat: typing.Type[FractionFormat]
    ProperBigFractionFormat: typing.Type[ProperBigFractionFormat]
    ProperFractionFormat: typing.Type[ProperFractionFormat]
