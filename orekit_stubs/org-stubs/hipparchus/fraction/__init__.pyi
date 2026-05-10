
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
    Representation of a rational number without any overflow. This class is immutable.
    
    Also see:
        serialized
    """
    TWO: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "2 / 1".
    """
    ONE: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "1".
    """
    ZERO: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "0".
    """
    MINUS_ONE: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "-1 / 1".
    """
    FOUR_FIFTHS: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "4/5".
    """
    ONE_FIFTH: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "1/5".
    """
    ONE_HALF: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "1/2".
    """
    ONE_QUARTER: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "1/4".
    """
    ONE_THIRD: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "1/3".
    """
    THREE_FIFTHS: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "3/5".
    """
    THREE_QUARTERS: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "3/4".
    """
    TWO_FIFTHS: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "2/5".
    """
    TWO_QUARTERS: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "2/4".
    """
    TWO_THIRDS: typing.ClassVar['BigFraction'] = ...
    """
    A fraction representing "2/3".
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, value: float, epsilon: float, maxIterations: int): ...
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
        Returns the absolute value of this BigFraction.
        
        Returns:
            the absolute value as a BigFraction.
        
        
        """
        ...
    @typing.overload
    def add(self, i: int) -> 'BigFraction':
        """
        Adds the value of this fraction to the passed integer, returning the result in reduced form.
        
        Parameters:
            i (int): the integer to add.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Adds the value of this fraction to the passed long, returning the result in reduced form.
        
        Parameters:
            l (long): the long to add.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Adds the value of this fraction to another, returning the result in reduced form.
        
        Specified by: add in interface FieldElement
        
        Parameters:
            fraction (BigFraction): the BigFraction to add, must not be null.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Raises:
            NullArgumentException: if the BigFraction is null.
        
        
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
        Gets the fraction as a BigDecimal. This calculates the fraction as the numerator divided by denominator.
        
        Returns:
            the fraction as a BigDecimal.
        
        Raises:
            ArithmeticException: if the exact quotient does not have a terminating decimal expansion.
        
        Also see:
            BigDecimal
        
        """
        ...
    @typing.overload
    def bigDecimalValue(self, scale: int, roundingMode: java.math.RoundingMode) -> java.math.BigDecimal:
        """
        Gets the fraction as a BigDecimal following the passed scale and rounding mode. This calculates the fraction as the numerator divided by denominator.
        
        Parameters:
            scale (int): scale of the BigDecimal quotient to be returned. see
                BigDecimal for more information.
            roundingMode (RoundingMode): rounding mode to apply. see
                BigDecimal constants.
        
        Returns:
            the fraction as a BigDecimal.
        
        Also see:
            BigDecimal
        
        
        """
        ...
    @typing.overload
    def bigDecimalValue(self, roundingMode: java.math.RoundingMode) -> java.math.BigDecimal:
        """
        Gets the fraction as a BigDecimal following the passed rounding mode. This calculates the fraction as the numerator divided by denominator.
        
        Parameters:
            roundingMode (RoundingMode): rounding mode to apply. see
                BigDecimal constants.
        
        Returns:
            the fraction as a BigDecimal.
        
        Raises:
            IllegalArgumentException: if roundingMode does not represent a valid rounding mode.
        
        Also see:
            BigDecimal
        
        """
        ...
    def compareTo(self, object: 'BigFraction') -> int:
        """
        Compares this object to another based on size.
        
        Specified by: Comparable in interface Comparable
        
        Parameters:
            object (BigFraction): the object to compare to, must not be null.
        
        Returns:
            -1 if this is less than object, +1 if this is greater than object, 0 if they are equal.
        
        Also see:
            Comparable
        
        
        """
        ...
    @staticmethod
    def convergent(value: float, maxConvergents: int, convergenceTest: typing.Union['BigFraction.ConvergenceTest', typing.Callable]) -> org.hipparchus.util.Pair['BigFraction', bool]:
        """
        Returns the last element of the series of convergent-steps to approximate the given value.
        
        The series terminates either at the first step that satisfies the given convergenceTest or after at most maxConvergents elements. The returned Pair consists of that terminal BigFraction and a Boolean that indicates if it satisfies the given convergence tests. If the returned pair's value is false the element at position maxConvergents was examined but failed to satisfy the convergenceTest. A caller can then decide to accept the result nevertheless or to discard it. This method is usually faster than convergents if only the terminal element is of interest.
        
        Parameters:
            value (double): value to approximate
            maxConvergents (int): maximum number of convergents to examine
            convergenceTest (ConvergenceTest): the test if the series has converged at a step
        
        Returns:
            the pair of last element of the series of convergents and a boolean indicating if that element satisfies the specified
            convergent test
        
        
        """
        ...
    @staticmethod
    def convergents(value: float, maxConvergents: int) -> java.util.stream.Stream['BigFraction']:
        """
        Generate a Stream of convergents from a real number.
        
        Parameters:
            value (double): value to approximate
            maxConvergents (int): maximum number of convergents.
        
        Returns:
            stream of BigFraction convergents approximating value
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def divide(self, bg: int) -> 'BigFraction':
        """
        Divide the value of this fraction by the passed BigInteger, ie this * 1 / bg, returning the result in reduced form.
        
        Parameters:
            bg (BigInteger): the BigInteger to divide by, must not be null
        
        Returns:
            a BigFraction instance with the resulting values
        
        Raises:
            NullArgumentException: if the BigInteger is null
            MathRuntimeException: if the fraction to divide by is zero
        
        Divide the value of this fraction by the passed int, ie this * 1 / i, returning the result in reduced form.
        
        Parameters:
            i (int): the int to divide by
        
        Returns:
            a BigFraction instance with the resulting values
        
        Raises:
            MathRuntimeException: if the fraction to divide by is zero
        
        Divide the value of this fraction by the passed long, ie this * 1 / l, returning the result in reduced form.
        
        Parameters:
            l (long): the long to divide by
        
        Returns:
            a BigFraction instance with the resulting values
        
        Raises:
            MathRuntimeException: if the fraction to divide by is zero
        
        Divide the value of this fraction by another, returning the result in reduced form.
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            fraction (BigFraction): Fraction to divide by, must not be null.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Raises:
            NullArgumentException: if the fraction is null.
            MathRuntimeException: if the fraction to divide by is zero
        
        
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
        Gets the fraction as a double. This calculates the fraction as the numerator divided by denominator.
        
        Specified by: Number in class Number
        
        Returns:
            the fraction as a double
        
        Also see:
            Number
        
        
        """
        ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two fractions. If the lowest term numerator and denominators are the same for both fractions, the two fractions are considered to be equal.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): fraction to test for equality to this fraction, can be null.
        
        Returns:
            true if two fractions are equal, false if object is null, not an instance of
            BigFraction, or not equal to this fraction instance.
        
        Also see:
            Object
        
        
        """
        ...
    def floatValue(self) -> float:
        """
        Gets the fraction as a float. This calculates the fraction as the numerator divided by denominator.
        
        Specified by: Number in class Number
        
        Returns:
            the fraction as a float.
        
        Also see:
            Number
        
        
        """
        ...
    def gcd(self, s: 'BigFraction') -> 'BigFraction':
        """
        Rational number greatest common divisor.
        
        Parameters:
            s (BigFraction): fraction.
        
        Returns:
            gcd(this, s).
        
        Since:
            3.1
        
        
        """
        ...
    def getDenominator(self) -> java.math.BigInteger:
        """
        Access the denominator as a BigInteger.
        
        Returns:
            the denominator as a BigInteger.
        
        
        """
        ...
    def getDenominatorAsInt(self) -> int:
        """
        Access the denominator as a int.
        
        Returns:
            the denominator as a int.
        
        
        """
        ...
    def getDenominatorAsLong(self) -> int:
        """
        Access the denominator as a long.
        
        Returns:
            the denominator as a long.
        
        
        """
        ...
    def getField(self) -> 'BigFractionField':
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getNumerator(self) -> java.math.BigInteger:
        """
        Access the numerator as a BigInteger.
        
        Returns:
            the numerator as a BigInteger.
        
        
        """
        ...
    def getNumeratorAsInt(self) -> int:
        """
        Access the numerator as a int.
        
        Returns:
            the numerator as a int.
        
        
        """
        ...
    def getNumeratorAsLong(self) -> int:
        """
        Access the numerator as a long.
        
        Returns:
            the numerator as a long.
        
        
        """
        ...
    def getReal(self) -> float:
        """
        Get the real value of the number.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            real value
        
        
        """
        ...
    @staticmethod
    def getReducedFraction(numerator: int, denominator: int) -> 'BigFraction':
        """
        Creates a BigFraction instance with the 2 parts of a fraction Y/Z.
        
        Any negative signs are resolved to be on the numerator.
        
        Parameters:
            numerator (int): the numerator, for example the three in 'three sevenths'.
            denominator (int): the denominator, for example the seven in 'three sevenths'.
        
        Returns:
            a new fraction instance, with the numerator and denominator reduced.
        
        Raises:
            ArithmeticException: if the denominator is zero.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Gets a hashCode for the fraction.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object.
        
        Also see:
            Object
        
        
        """
        ...
    def intValue(self) -> int:
        """
        Gets the fraction as an int. This returns the whole number part of the fraction.
        
        Specified by: Number in class Number
        
        Returns:
            the whole number fraction part.
        
        Also see:
            Number
        
        
        """
        ...
    def isInteger(self) -> bool:
        """
        Check if a fraction is an integer.
        
        Returns:
            true of fraction is an integer
        
        
        """
        ...
    def lcm(self, s: 'BigFraction') -> 'BigFraction':
        """
        Rational number least common multiple.
        
        Parameters:
            s (BigFraction): fraction.
        
        Returns:
            lcm(this, s).
        
        Since:
            3.1
        
        
        """
        ...
    def longValue(self) -> int:
        """
        Gets the fraction as a long. This returns the whole number part of the fraction.
        
        Specified by: Number in class Number
        
        Returns:
            the whole number fraction part.
        
        Also see:
            Number
        
        
        """
        ...
    @typing.overload
    def multiply(self, bg: int) -> 'BigFraction':
        """
        Multiplies the value of this fraction by the passed BigInteger, returning the result in reduced form.
        
        Parameters:
            bg (BigInteger): the BigInteger to multiply by.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Raises:
            NullArgumentException: if bg is null.
        
        Multiply the value of this fraction by the passed int, returning the result in reduced form.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            i (int): the int to multiply by.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Multiply the value of this fraction by the passed long, returning the result in reduced form.
        
        Parameters:
            l (long): the long to multiply by.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Multiplies the value of this fraction by another, returning the result in reduced form.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            fraction (BigFraction): Fraction to multiply by, must not be null.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Raises:
            NullArgumentException: if fraction is null.
        
        
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
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the negation of this fraction.
        
        
        """
        ...
    def percentageValue(self) -> float:
        """
        Gets the fraction percentage as a double. This calculates the fraction as the numerator divided by denominator multiplied by 100.
        
        Returns:
            the fraction percentage as a double.
        
        
        """
        ...
    @typing.overload
    def pow(self, exponent: float) -> float:
        """
        Parameters:
            exponent (int): exponent to which this BigFraction is to be raised.
        
        Returns:
            this :sup:`exponent`
        
        Returns a BigFraction whose value is this :sup:`exponent` , returning the result in reduced form.
        
        Parameters:
            exponent (long): exponent to which this BigFraction is to be raised.
        
        Returns:
            this :sup:`exponent` as a BigFraction.
        
        Returns a BigFraction whose value is this :sup:`exponent` , returning the result in reduced form.
        
        Parameters:
            exponent (BigInteger): exponent to which this BigFraction is to be raised.
        
        Returns:
            this :sup:`exponent` as a BigFraction.
        
        Returns a double whose value is this :sup:`exponent` , returning the result in reduced form.
        
        Parameters:
            exponent (double): exponent to which this BigFraction is to be raised.
        
        Returns:
            this :sup:`exponent`
        
        
        """
        ...
    @typing.overload
    def pow(self, exponent: int) -> 'BigFraction': ...
    @typing.overload
    def pow(self, exponent: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def pow(self, exponent: int) -> 'BigFraction': ...
    def reciprocal(self) -> 'BigFraction':
        """
        Return the multiplicative inverse of this fraction.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the reciprocal fraction.
        
        
        """
        ...
    def reduce(self) -> 'BigFraction':
        """
        Reduce this BigFraction to its lowest terms.
        
        Returns:
            the reduced BigFraction. It doesn't change anything if the fraction can be reduced.
        
        
        """
        ...
    def signum(self) -> int:
        """
        Returns the signum function of this BigFraction.
        
        The return value is -1 if the specified value is negative; 0 if the specified value is zero; and 1 if the specified value is positive.
        
        Returns:
            the signum function of this BigFraction
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    def subtract(self, bg: int) -> 'BigFraction':
        """
        Subtracts the value of an BigInteger from the value of this BigFraction, returning the result in reduced form.
        
        Parameters:
            bg (BigInteger): the BigInteger to subtract,
                cannot be null.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Raises:
            NullArgumentException: if the BigInteger is
                null.
        
        Subtracts the value of an integer from the value of this BigFraction, returning the result in reduced form.
        
        Parameters:
            i (int): the integer to subtract.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Subtracts the value of a long from the value of this BigFraction, returning the result in reduced form.
        
        Parameters:
            l (long): the long to subtract.
        
        Returns:
            a BigFraction instance with the resulting values.
        
        Subtracts the value of another fraction from the value of this one, returning the result in reduced form.
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            fraction (BigFraction): BigFraction to subtract, must not be null.
        
        Returns:
            a BigFraction instance with the resulting values
        
        Raises:
            NullArgumentException: if the fraction is null.
        
        
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
        Returns the String representing this fraction, ie "num / dem" or just "num" if the denominator is one.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of the fraction.
        
        Also see:
            Object
        
        
        """
        ...
    class ConvergenceTest:
        def test(self, long: int, long2: int) -> bool: ...

class BigFractionField(org.hipparchus.Field[BigFraction], java.io.Serializable):
    """
    Representation of the fractional numbers without any overflow field.
    
    This class is a singleton.
    
    Also see:
        Fraction, serialized
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
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
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[BigFraction]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> BigFraction:
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
        Overrides: Object in class Object
        
        
        """
        ...

class Fraction(java.lang.Number, org.hipparchus.FieldElement['Fraction'], java.lang.Comparable['Fraction'], java.io.Serializable):
    """
    Representation of a rational number.
    
    Also see:
        serialized
    """
    TWO: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "2 / 1".
    """
    ONE: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "1".
    """
    ZERO: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "0".
    """
    FOUR_FIFTHS: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "4/5".
    """
    ONE_FIFTH: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "1/5".
    """
    ONE_HALF: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "1/2".
    """
    ONE_QUARTER: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "1/4".
    """
    ONE_THIRD: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "1/3".
    """
    THREE_FIFTHS: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "3/5".
    """
    THREE_QUARTERS: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "3/4".
    """
    TWO_FIFTHS: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "2/5".
    """
    TWO_QUARTERS: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "2/4".
    """
    TWO_THIRDS: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "2/3".
    """
    MINUS_ONE: typing.ClassVar['Fraction'] = ...
    """
    A fraction representing "-1 / 1".
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, value: float, epsilon: float, maxIterations: int): ...
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
    def add(self, fraction: int) -> 'Fraction':
        """
        Adds the value of this fraction to another, returning the result in reduced form. The algorithm follows Knuth, 4.5.1.
        
        Specified by: add in interface FieldElement
        
        Parameters:
            fraction (Fraction): the fraction to add, must not be null
        
        Returns:
            a Fraction instance with the resulting values
        
        Raises:
            NullArgumentException: if the fraction is null
            MathRuntimeException: if the resulting numerator or denominator exceeds MAX_VALUE
        
        Add an integer to the fraction.
        
        Parameters:
            i (int): the integer to add.
        
        Returns:
            this + i
        
        
        """
        ...
    @typing.overload
    def add(self, fraction: 'Fraction') -> 'Fraction': ...
    def compareTo(self, object: 'Fraction') -> int:
        """
        Compares this object to another based on size.
        
        Specified by: Comparable in interface Comparable
        
        Parameters:
            object (Fraction): the object to compare to
        
        Returns:
            -1 if this is less than object, +1 if this is greater than object, 0 if they are equal.
        
        
        """
        ...
    @staticmethod
    def convergent(value: float, maxConvergents: int, convergenceTest: typing.Union['Fraction.ConvergenceTest', typing.Callable]) -> org.hipparchus.util.Pair['Fraction', bool]:
        """
        Returns the last element of the series of convergent-steps to approximate the given value.
        
        The series terminates either at the first step that satisfies the given convergenceTest or after at most maxConvergents elements. The returned Pair consists of that terminal Fraction and a Boolean that indicates if it satisfies the given convergence tests. If the returned pair's value is false the element at position maxConvergents was examined but failed to satisfy the convergenceTest. A caller can then decide to accept the result nevertheless or to discard it. This method is usually faster than convergents if only the terminal element is of interest.
        
        Parameters:
            value (double): value to approximate
            maxConvergents (int): maximum number of convergents to examine
            convergenceTest (ConvergenceTest): the test if the series has converged at a step
        
        Returns:
            the pair of last element of the series of convergents and a boolean indicating if that element satisfies the specified
            convergent test
        
        
        """
        ...
    @staticmethod
    def convergents(value: float, maxConvergents: int) -> java.util.stream.Stream['Fraction']:
        """
        Generate a Stream of convergents from a real number.
        
        Parameters:
            value (double): value to approximate
            maxConvergents (int): maximum number of convergents.
        
        Returns:
            stream of Fraction convergents approximating value
        
        Since:
            2.1
        
        
        """
        ...
    @typing.overload
    def divide(self, fraction: int) -> 'Fraction':
        """
        Divide the value of this fraction by another.
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            fraction (Fraction): the fraction to divide by, must not be null
        
        Returns:
            a Fraction instance with the resulting values
        
        Raises:
            IllegalArgumentException: if the fraction is null
            MathRuntimeException: if the fraction to divide by is zero
            MathRuntimeException: if the resulting numerator or denominator exceeds MAX_VALUE
        
        Divide the fraction by an integer.
        
        Parameters:
            i (int): the integer to divide by.
        
        Returns:
            this * i
        
        
        """
        ...
    @typing.overload
    def divide(self, fraction: 'Fraction') -> 'Fraction': ...
    def doubleValue(self) -> float:
        """
        Gets the fraction as a double. This calculates the fraction as the numerator divided by denominator.
        
        Specified by: Number in class Number
        
        Returns:
            the fraction as a double
        
        
        """
        ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two fractions. If the lowest term numerator and denominators are the same for both fractions, the two fractions are considered to be equal.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): fraction to test for equality to this fraction
        
        Returns:
            true if two fractions are equal, false if object is null, not an instance of
            Fraction, or not equal to this fraction instance.
        
        
        """
        ...
    def floatValue(self) -> float:
        """
        Gets the fraction as a float. This calculates the fraction as the numerator divided by denominator.
        
        Specified by: Number in class Number
        
        Returns:
            the fraction as a float
        
        
        """
        ...
    def gcd(self, s: 'Fraction') -> 'Fraction':
        """
        Rational number greatest common divisor.
        
        Parameters:
            s (Fraction): fraction.
        
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
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
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
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            real value
        
        
        """
        ...
    @staticmethod
    def getReducedFraction(numerator: int, denominator: int) -> 'Fraction':
        """
        Creates a Fraction instance with the 2 parts of a fraction Y/Z.
        
        Any negative signs are resolved to be on the numerator.
        
        Parameters:
            numerator (int): the numerator, for example the three in 'three sevenths'
            denominator (int): the denominator, for example the seven in 'three sevenths'
        
        Returns:
            a new fraction instance, with the numerator and denominator reduced
        
        Raises:
            MathRuntimeException: if the denominator is zero
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Gets a hashCode for the fraction.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def intValue(self) -> int:
        """
        Gets the fraction as an int. This returns the whole number part of the fraction.
        
        Specified by: Number in class Number
        
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
    def lcm(self, s: 'Fraction') -> 'Fraction':
        """
        Rational number least common multiple.
        
        Parameters:
            s (Fraction): fraction.
        
        Returns:
            lcm(this, s).
        
        Since:
            3.1
        
        
        """
        ...
    def longValue(self) -> int:
        """
        Gets the fraction as a long. This returns the whole number part of the fraction.
        
        Specified by: Number in class Number
        
        Returns:
            the whole number fraction part
        
        
        """
        ...
    @typing.overload
    def multiply(self, fraction: int) -> 'Fraction':
        """
        Multiplies the value of this fraction by another, returning the result in reduced form.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            fraction (Fraction): the fraction to multiply by, must not be null
        
        Returns:
            a Fraction instance with the resulting values
        
        Raises:
            NullArgumentException: if the fraction is null
            MathRuntimeException: if the resulting numerator or denominator exceeds MAX_VALUE
        
        Multiply the fraction by an integer.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            i (int): the integer to multiply by.
        
        Returns:
            this * i
        
        
        """
        ...
    @typing.overload
    def multiply(self, fraction: 'Fraction') -> 'Fraction': ...
    def negate(self) -> 'Fraction':
        """
        Return the additive inverse of this fraction.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the negation of this fraction.
        
        
        """
        ...
    def percentageValue(self) -> float:
        """
        Gets the fraction percentage as a double. This calculates the fraction as the numerator divided by denominator multiplied by 100.
        
        Returns:
            the fraction percentage as a double.
        
        
        """
        ...
    def reciprocal(self) -> 'Fraction':
        """
        Return the multiplicative inverse of this fraction.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the reciprocal fraction
        
        
        """
        ...
    def signum(self) -> int:
        """
        Returns the signum function of this fraction.
        
        The return value is -1 if the specified value is negative; 0 if the specified value is zero; and 1 if the specified value is positive.
        
        Returns:
            the signum function of this fraction
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    def subtract(self, fraction: int) -> 'Fraction':
        """
        Subtracts the value of another fraction from the value of this one, returning the result in reduced form.
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            fraction (Fraction): the fraction to subtract, must not be null
        
        Returns:
            a Fraction instance with the resulting values
        
        Raises:
            NullArgumentException: if the fraction is null
            MathRuntimeException: if the resulting numerator or denominator cannot be represented in an int.
        
        Subtract an integer from the fraction.
        
        Parameters:
            i (int): the integer to subtract.
        
        Returns:
            this - i
        
        
        """
        ...
    @typing.overload
    def subtract(self, fraction: 'Fraction') -> 'Fraction': ...
    def toString(self) -> str:
        """
        Returns the String representing this fraction, ie "num / dem" or just "num" if the denominator is one.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of the fraction.
        
        Also see:
            Object
        
        
        """
        ...
    class ConvergenceTest:
        def test(self, int: int, int2: int) -> bool: ...

class FractionField(org.hipparchus.Field[Fraction], java.io.Serializable):
    """
    Representation of the fractional numbers field.
    
    This class is a singleton.
    
    Also see:
        Fraction, serialized
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
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
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Fraction]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> Fraction:
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
        Overrides: Object in class Object
        
        
        """
        ...

class BigFractionFormat(org.hipparchus.fraction.AbstractFormat, java.io.Serializable):
    """
    Formats a BigFraction number in proper format or improper format.
    
    The number format for each of the whole number, numerator and, denominator can be configured.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, format: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numeratorFormat: java.text.NumberFormat, denominatorFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
        Formats a BigFraction object to produce a string. The BigFraction is output in improper format.
        
        Parameters:
            BigFraction (BigFraction): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        Formats an object and appends the result to a StringBuffer. obj must be either a BigFraction object or a BigInteger object or a Number object. Any other type of object will result in an IllegalArgumentException being thrown.
        
        Overrides: NumberFormat in class NumberFormat
        
        Parameters:
            obj (Object): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        Raises:
            MathIllegalArgumentException: if obj is not a valid type.
        
        Also see:
            Format
        
        Formats a double value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (double): the double value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        Formats a long value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (long): the long value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        
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
    def formatBigFraction(f: BigFraction) -> str:
        """
        This static method calls formatBigFraction() on a default instance of BigFractionFormat.
        
        Parameters:
            f (BigFraction): BigFraction object to format
        
        Returns:
            A formatted BigFraction in proper form.
        
        
        """
        ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
        Get the set of locales for which complex formats are available. This is the same set as the NumberFormat set.
        
        Returns:
            available complex format locales.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance() -> 'BigFractionFormat':
        """
        Returns:
            the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance(locale: java.util.Locale) -> 'BigFractionFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance() -> 'BigFractionFormat':
        """
        Returns:
            the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance(locale: java.util.Locale) -> 'BigFractionFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str) -> BigFraction:
        """
        Parses a string to produce a BigFraction object. This method expects the string to be formatted as an improper BigFraction.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/output parsing parameter.
        
        Returns:
            the parsed BigFraction object.
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str, pos: java.text.ParsePosition) -> BigFraction: ...

class FractionFormat(org.hipparchus.fraction.AbstractFormat):
    """
    Formats a Fraction number in proper format or improper format.
    
    The number format for each of the whole number, numerator and, denominator can be configured.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, format: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numeratorFormat: java.text.NumberFormat, denominatorFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
        Formats a Fraction object to produce a string. The fraction is output in improper format.
        
        Parameters:
            fraction (Fraction): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        public StringBuffer format (Object obj, StringBuffer toAppendTo, FieldPosition pos) throws MathIllegalArgumentException, MathIllegalStateException
        
        Formats an object and appends the result to a StringBuffer. obj must be either a Fraction object or a Number object. Any other type of object will result in an IllegalArgumentException being thrown.
        
        Overrides: NumberFormat in class NumberFormat
        
        Parameters:
            obj (Object): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        Raises:
            MathIllegalStateException: if the number cannot be converted to a fraction
            MathIllegalArgumentException: if obj is not a valid type.
        
        Also see:
            Format
        
        Formats a double value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (double): the double value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        Formats a long value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (long): the long value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        
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
    def formatFraction(f: Fraction) -> str:
        """
        This static method calls formatFraction() on a default instance of FractionFormat.
        
        Parameters:
            f (Fraction): Fraction object to format
        
        Returns:
            a formatted fraction in proper form.
        
        
        """
        ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
        Get the set of locales for which complex formats are available. This is the same set as the NumberFormat set.
        
        Returns:
            available complex format locales.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance() -> 'FractionFormat':
        """
        Returns:
            the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getImproperInstance(locale: java.util.Locale) -> 'FractionFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance() -> 'FractionFormat':
        """
        Returns:
            the default complex format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getProperInstance(locale: java.util.Locale) -> 'FractionFormat':
        """
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the complex format specific to the given locale.
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str) -> Fraction:
        """
        Parses a string to produce a Fraction object. This method expects the string to be formatted as an improper fraction.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/output parsing parameter.
        
        Returns:
            the parsed Fraction object.
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str, pos: java.text.ParsePosition) -> Fraction: ...

class ProperBigFractionFormat(BigFractionFormat):
    """
    Formats a BigFraction number in proper format. The number format for each of the whole number, numerator and, denominator can be configured.
    
    Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is invalid and will result in a ParseException.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, format: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, wholeFormat: java.text.NumberFormat, numeratorFormat: java.text.NumberFormat, denominatorFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
        Formats a BigFraction object to produce a string. The BigFraction is output in proper format.
        
        Overrides: format in class BigFractionFormat
        
        Parameters:
            fraction (BigFraction): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        Formats a double value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (double): the double value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        Formats a long value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (long): the long value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        
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
        Parses a string to produce a BigFraction object. This method expects the string to be formatted as a proper BigFraction.
        
        Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is invalid and will result in a ParseException.
        
        Overrides: parse in class BigFractionFormat
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/ouput parsing parameter.
        
        Returns:
            the parsed BigFraction object.
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str, pos: java.text.ParsePosition) -> BigFraction: ...

class ProperFractionFormat(FractionFormat):
    """
    Formats a Fraction number in proper format. The number format for each of the whole number, numerator and, denominator can be configured.
    
    Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is invalid and will result in a ParseException.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, format: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, wholeFormat: java.text.NumberFormat, numeratorFormat: java.text.NumberFormat, denominatorFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str:
        """
        Formats a Fraction object to produce a string. The fraction is output in proper format.
        
        Overrides: format in class FractionFormat
        
        Parameters:
            fraction (Fraction): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        Formats a double value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (double): the double value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        Formats a long value as a fraction and appends the result to a StringBuffer.
        
        Specified by: NumberFormat in class NumberFormat
        
        Parameters:
            value (long): the long value to format
            buffer (StringBuffer): StringBuffer to append to
            position (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            a reference to the appended buffer
        
        Also see:
            NumberFormat
        
        
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
        Parses a string to produce a Fraction object. This method expects the string to be formatted as a proper fraction.
        
        Minus signs are only allowed in the whole number part - i.e., "-3 1/2" is legitimate and denotes -7/2, but "-3 -1/2" is invalid and will result in a ParseException.
        
        Overrides: parse in class FractionFormat
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/ouput parsing parameter.
        
        Returns:
            the parsed Fraction object.
        
        
        """
        ...
    @typing.overload
    def parse(self, source: str, pos: java.text.ParsePosition) -> Fraction: ...

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
