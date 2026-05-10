
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import decimal
import java.io
import java.lang
import java.math
import java.text
import java.util
import java.util.stream
import jpype
import org
import org.hipparchus
import org.hipparchus.exception
import org.hipparchus.linear
import org.hipparchus.random
import typing



class AbstractOpenIntHashMap:
    """
    Base class for open addressed map from int.
    
    Since:
        3.1
    """
    @typing.overload
    def containsKey(self, key: int) -> bool:
        """
        Check if a value is associated with a key.
        
        Parameters:
            key (int): key to check
        
        Returns:
            true if a value is associated with key
        
        Check if the tables contain an element associated with specified key at specified index.
        
        Parameters:
            key (int): key to check
            index (int): index to check
        
        Returns:
            true if an element is associated with key at index
        
        
        """
        ...
    @typing.overload
    def containsKey(self, key: int, index: int) -> bool: ...
    def getSize(self) -> int:
        """
        Get the number of elements stored in the map.
        
        Returns:
            number of elements stored in the map
        
        
        """
        ...
    def size(self) -> int:
        """
        Get the number of elements stored in the map.
        
        Returns:
            number of elements stored in the map
        
        
        """
        ...

class ArithmeticUtils:
    """
    Some useful, arithmetics related, additions to the built-in functions in Math.
    """
    @typing.overload
    @staticmethod
    def addAndCheck(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def addAndCheck(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def divideUnsigned(dividend: int, divisor: int) -> int:
        """
        Returns the unsigned quotient of dividing the first argument by the second where each argument and the result is interpreted as an unsigned value.
        
        Note that in two's complement arithmetic, the three other basic arithmetic operations of add, subtract, and multiply are bit-wise identical if the two operands are regarded as both being signed or both being unsigned. Therefore separate addUnsigned, etc. methods are not provided.
        
        This method does not use the long datatype.
        
        Parameters:
            dividend (int): the value to be divided
            divisor (int): the value doing the dividing
        
        Returns:
            the unsigned quotient of the first argument divided by the second argument
        
        Returns the unsigned quotient of dividing the first argument by the second where each argument and the result is interpreted as an unsigned value.
        
        Note that in two's complement arithmetic, the three other basic arithmetic operations of add, subtract, and multiply are bit-wise identical if the two operands are regarded as both being signed or both being unsigned. Therefore separate addUnsigned, etc. methods are not provided.
        
        This method does not use the BigInteger datatype.
        
        Parameters:
            dividend (long): the value to be divided
            divisor (long): the value doing the dividing
        
        Returns:
            the unsigned quotient of the first argument divided by the second argument.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def divideUnsigned(dividend: int, divisor: int) -> int: ...
    @typing.overload
    @staticmethod
    def gcd(p: int, q: int) -> int: ...
    @typing.overload
    @staticmethod
    def gcd(p: int, q: int) -> int: ...
    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        """
        Returns true if the argument is a power of two.
        
        Parameters:
            n (long): the number to test
        
        Returns:
            true if the argument is a power of two
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def lcm(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def lcm(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def mulAndCheck(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def mulAndCheck(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def pow(k: int, e: int) -> int: ...
    @typing.overload
    @staticmethod
    def pow(k: java.math.BigInteger, e: int) -> java.math.BigInteger: ...
    @typing.overload
    @staticmethod
    def pow(k: java.math.BigInteger, e: java.math.BigInteger) -> java.math.BigInteger: ...
    @typing.overload
    @staticmethod
    def pow(k: java.math.BigInteger, e: int) -> java.math.BigInteger: ...
    @typing.overload
    @staticmethod
    def pow(k: int, e: int) -> int: ...
    @typing.overload
    @staticmethod
    def remainderUnsigned(dividend: int, divisor: int) -> int:
        """
        Returns the unsigned remainder from dividing the first argument by the second where each argument and the result is interpreted as an unsigned value.
        
        This method does not use the long datatype.
        
        Parameters:
            dividend (int): the value to be divided
            divisor (int): the value doing the dividing
        
        Returns:
            the unsigned remainder of the first argument divided by the second argument.
        
        Returns the unsigned remainder from dividing the first argument by the second where each argument and the result is interpreted as an unsigned value.
        
        This method does not use the BigInteger datatype.
        
        Parameters:
            dividend (long): the value to be divided
            divisor (long): the value doing the dividing
        
        Returns:
            the unsigned remainder of the first argument divided by the second argument.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def remainderUnsigned(dividend: int, divisor: int) -> int: ...
    @typing.overload
    @staticmethod
    def subAndCheck(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def subAndCheck(long: int, long2: int) -> int: ...

class BigReal(org.hipparchus.FieldElement['BigReal'], java.lang.Comparable['BigReal'], java.io.Serializable):
    """
    Arbitrary precision decimal number.
    
    This class is a simple wrapper around the standard BigDecimal in order to implement the FieldElement interface.
    
    Also see:
        serialized
    """
    ZERO: typing.ClassVar['BigReal'] = ...
    """
    A big real representing 0.
    """
    ONE: typing.ClassVar['BigReal'] = ...
    """
    A big real representing 1.
    """
    @typing.overload
    def __init__(self, charArray: typing.Union[typing.List[str], jpype.JArray]): ...
    @typing.overload
    def __init__(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, in_: typing.Union[typing.List[str], jpype.JArray], offset: int, len: int, mc: java.math.MathContext): ...
    @typing.overload
    def __init__(self, charArray: typing.Union[typing.List[str], jpype.JArray], mathContext: java.math.MathContext): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, mathContext: java.math.MathContext): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, mathContext: java.math.MathContext): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, mathContext: java.math.MathContext): ...
    @typing.overload
    def __init__(self, bigDecimal: typing.Union[java.math.BigDecimal, decimal.Decimal]): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, int: int): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, int: int, mathContext: java.math.MathContext): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, mathContext: java.math.MathContext): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def __init__(self, long: int, mathContext: java.math.MathContext): ...
    def add(self, a: 'BigReal') -> 'BigReal':
        """
        Compute this + a.
        
        Specified by: add in interface FieldElement
        
        Parameters:
            a (BigReal): element to add
        
        Returns:
            a new element representing this + a
        
        
        """
        ...
    def bigDecimalValue(self) -> java.math.BigDecimal:
        """
        Get the BigDecimal value corresponding to the instance.
        
        Returns:
            BigDecimal value corresponding to the instance
        
        
        """
        ...
    def compareTo(self, a: 'BigReal') -> int:
        """
        Specified by: Comparable in interface Comparable
        
        
        """
        ...
    def divide(self, a: 'BigReal') -> 'BigReal':
        """
        Compute this ÷ a.
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            a (BigReal): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        Raises:
            MathRuntimeException: if a is zero
        
        
        """
        ...
    def doubleValue(self) -> float:
        """
        Get the double value corresponding to the instance.
        
        Returns:
            double value corresponding to the instance
        
        
        """
        ...
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['BigReal']:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
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
    def getRoundingMode(self) -> java.math.RoundingMode:
        """
        Gets the rounding mode for division operations The default is HALF_UP
        
        Returns:
            the rounding mode.
        
        
        """
        ...
    def getScale(self) -> int:
        """
        Sets the scale for division operations. The default is 64
        
        Returns:
            the scale
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @typing.overload
    def multiply(self, a: int) -> 'BigReal':
        """
        Compute this × a.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            a (BigReal): element to multiply
        
        Returns:
            a new element representing this × a
        
        Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} = \sum_{i=1}^n \mathrm{this} \]
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            n (int): Number of times this must be added to itself.
        
        Returns:
            A new element representing n × this.
        
        
        """
        ...
    @typing.overload
    def multiply(self, bigReal: 'BigReal') -> 'BigReal': ...
    def negate(self) -> 'BigReal':
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def reciprocal(self) -> 'BigReal':
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        Raises:
            MathRuntimeException: if this is zero
        
        
        """
        ...
    def setRoundingMode(self, roundingMode: java.math.RoundingMode) -> None:
        """
        Sets the rounding mode for decimal divisions.
        
        Parameters:
            roundingMode (RoundingMode): rounding mode for decimal divisions
        
        
        """
        ...
    def setScale(self, scale: int) -> None:
        """
        Sets the scale for division operations.
        
        Parameters:
            scale (int): scale for division operations
        
        
        """
        ...
    def subtract(self, a: 'BigReal') -> 'BigReal':
        """
        Compute this - a.
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            a (BigReal): element to subtract
        
        Returns:
            a new element representing this - a
        
        
        """
        ...

class BigRealField(org.hipparchus.Field[BigReal], java.io.Serializable):
    """
    Representation of real numbers with arbitrary precision field.
    
    This class is a singleton.
    
    Also see:
        BigReal, serialized
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'BigRealField':
        """
        Get the unique instance.
        
        Returns:
            the unique instance
        
        
        """
        ...
    def getOne(self) -> BigReal:
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[BigReal]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> BigReal:
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

class Binary64(java.lang.Number, org.hipparchus.CalculusFieldElement['Binary64'], java.lang.Comparable['Binary64']):
    """
    This class wraps a double value in an object. It is similar to the standard class Double, while also implementing the CalculusFieldElement interface.
    
    Also see:
        serialized
    """
    ZERO: typing.ClassVar['Binary64'] = ...
    """
    The constant value of 0d as a Binary64.
    """
    ONE: typing.ClassVar['Binary64'] = ...
    """
    The constant value of 1d as a Binary64.
    """
    PI: typing.ClassVar['Binary64'] = ...
    """
    The constant value of π as a Binary64.
    """
    NEGATIVE_INFINITY: typing.ClassVar['Binary64'] = ...
    """
    The constant value of Double as a Binary64.
    """
    POSITIVE_INFINITY: typing.ClassVar['Binary64'] = ...
    """
    The constant value of Double as a Binary64.
    """
    NAN: typing.ClassVar['Binary64'] = ...
    """
    The constant value of Double as a Binary64.
    """
    def __init__(self, x: float):
        """
        Creates a new instance of this class.
        
        Parameters:
            x (double): the primitive double value of the object to be created
        
        
        """
        ...
    def abs(self) -> 'Binary64':
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    def acos(self) -> 'Binary64':
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> 'Binary64':
        """
        Inverse hyperbolic cosine operation.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> 'Binary64':
        """
        Specified by: add in interface FieldElement
        
        Parameters:
            a (Binary64): element to add
        
        Returns:
            a new element representing this + a
        
        '+' operator.
        
        Specified by: add in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this+a
        
        
        """
        ...
    @typing.overload
    def add(self, a: 'Binary64') -> 'Binary64': ...
    def asin(self) -> 'Binary64':
        """
        Arc sine operation.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> 'Binary64':
        """
        Inverse hyperbolic sine operation.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'Binary64':
        """
        Arc tangent operation.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            atan(this)
        
        
        """
        ...
    def atan2(self, x: 'Binary64') -> 'Binary64':
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (Binary64): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def atanh(self) -> 'Binary64':
        """
        Inverse hyperbolic tangent operation.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def byteValue(self) -> int:
        """
        The current implementation performs casting to a byte.
        
        Overrides: Number in class Number
        
        
        """
        ...
    def cbrt(self) -> 'Binary64':
        """
        Cubic root.
        
        Specified by: cbrt in interface CalculusFieldElement
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'Binary64':
        """
        Get the smallest whole number larger than instance.
        
        Specified by: ceil in interface CalculusFieldElement
        
        Returns:
            ceil(this)
        
        
        """
        ...
    def compareTo(self, o: 'Binary64') -> int:
        """
        The current implementation returns the same value as doubleValue()))
        
        Specified by: Comparable in interface Comparable
        
        Also see:
            Double
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'Binary64':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (Binary64): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: 'Binary64') -> 'Binary64': ...
    def cos(self) -> 'Binary64':
        """
        Cosine operation.
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> 'Binary64':
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Returns:
            cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'Binary64':
        """
        Specified by: divide in interface CalculusFieldElement
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            a (Binary64): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        '÷' operator.
        
        Specified by: divide in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this÷a
        
        
        """
        ...
    @typing.overload
    def divide(self, a: 'Binary64') -> 'Binary64': ...
    def doubleValue(self) -> float:
        """
        Specified by: Number in class Number
        
        
        """
        ...
    def equals(self, obj: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def exp(self) -> 'Binary64':
        """
        Exponential.
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'Binary64':
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def floatValue(self) -> float:
        """
        The current implementation performs casting to a float.
        
        Specified by: Number in class Number
        
        
        """
        ...
    def floor(self) -> 'Binary64':
        """
        Get the largest whole number smaller than instance.
        
        Specified by: floor in interface CalculusFieldElement
        
        Returns:
            floor(this)
        
        
        """
        ...
    def getAddendum(self) -> 'Binary64':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['Binary64']:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getPi(self) -> 'Binary64':
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
        Get the real value of the number.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        The current implementation returns the same value as hashCode()
        
        Overrides: Object in class Object
        
        Also see:
            Double
        
        
        """
        ...
    def hypot(self, y: 'Binary64') -> 'Binary64':
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (Binary64): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    def intValue(self) -> int:
        """
        The current implementation performs casting to a int.
        
        Specified by: Number in class Number
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Returns true if this double precision number is infinite (Double or Double).
        
        Specified by: isInfinite in interface CalculusFieldElement
        
        Returns:
            true if this number is infinite
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Returns true if this double precision number is Not-a-Number (NaN), false otherwise.
        
        Specified by: isNaN in interface CalculusFieldElement
        
        Returns:
            true if this is NaN
        
        
        """
        ...
    def isZero(self) -> bool:
        """
        Check if an element is semantically equal to zero.
        
        The default implementation simply calls getZero()). However, this may need to be overridden in some cases as due to compatibility with hashCode() some classes implements equals(Object) in such a way that -0.0 and +0.0 are different, which may be a problem. It prevents for example identifying a diagonal element is zero and should be avoided when doing partial pivoting in LU decomposition.
        
        This implementation considers +0.0 and -0.0 to be equal.
        
        Specified by: isZero in interface FieldElement
        
        Returns:
            true if the element is semantically equal to zero
        
        Since:
            1.8
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Binary64', a2: float, b2: 'Binary64') -> 'Binary64':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Binary64): first factor of the first term
            b1 (Binary64): second factor of the first term
            a2 (Binary64): first factor of the second term
            b2 (Binary64): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Binary64): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Binary64): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Binary64): first factor of the first term
            b1 (Binary64): second factor of the first term
            a2 (Binary64): first factor of the second term
            b2 (Binary64): second factor of the second term
            a3 (Binary64): first factor of the third term
            b3 (Binary64): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Binary64): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Binary64): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Binary64): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Binary64): first factor of the first term
            b1 (Binary64): second factor of the first term
            a2 (Binary64): first factor of the second term
            b2 (Binary64): second factor of the second term
            a3 (Binary64): first factor of the third term
            b3 (Binary64): second factor of the third term
            a4 (Binary64): first factor of the fourth term
            b4 (Binary64): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Binary64): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Binary64): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Binary64): second factor of the third term
            a4 (double): first factor of the fourth term
            b4 (Binary64): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Binary64', a2: float, b2: 'Binary64', a3: float, b3: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Binary64', a2: float, b2: 'Binary64', a3: float, b3: 'Binary64', a4: float, b4: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['Binary64'], jpype.JArray]) -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, a1: 'Binary64', b1: 'Binary64', a2: 'Binary64', b2: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, a1: 'Binary64', b1: 'Binary64', a2: 'Binary64', b2: 'Binary64', a3: 'Binary64', b3: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, a1: 'Binary64', b1: 'Binary64', a2: 'Binary64', b2: 'Binary64', a3: 'Binary64', b3: 'Binary64', a4: 'Binary64', b4: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['Binary64'], jpype.JArray], b: typing.Union[typing.List['Binary64'], jpype.JArray]) -> 'Binary64': ...
    def log(self) -> 'Binary64':
        """
        Natural logarithm.
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'Binary64':
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'Binary64':
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    def longValue(self) -> int:
        """
        The current implementation performs casting to a long.
        
        Specified by: Number in class Number
        
        
        """
        ...
    @typing.overload
    def multiply(self, a: float) -> 'Binary64':
        """
        Specified by: multiply in interface FieldElement
        
        Parameters:
            a (Binary64): element to multiply
        
        Returns:
            a new element representing this × a
        
        Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} = \sum_{i=1}^n \mathrm{this} \] The current implementation strictly enforces doubleValue())).
        
        Specified by: multiply in interface CalculusFieldElement
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            n (int): Number of times this must be added to itself.
        
        Returns:
            A new element representing n × this.
        
        '×' operator.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this×a
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'Binary64': ...
    @typing.overload
    def multiply(self, binary64: 'Binary64') -> 'Binary64': ...
    def negate(self) -> 'Binary64':
        """
        Returns the additive inverse of this element. The current implementation strictly enforces doubleValue())).
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, v: float) -> 'Binary64':
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            v (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, p: float) -> 'Binary64':
        """
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            e (Binary64): exponent
        
        Returns:
            this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'Binary64': ...
    @typing.overload
    def pow(self, binary64: 'Binary64') -> 'Binary64': ...
    def reciprocal(self) -> 'Binary64':
        """
        Returns the multiplicative inverse of this element. The current implementation strictly enforces doubleValue())).
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> 'Binary64':
        """
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (Binary64): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: 'Binary64') -> 'Binary64': ...
    def rint(self) -> 'Binary64':
        """
        Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
        Specified by: rint in interface CalculusFieldElement
        
        Returns:
            a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, n: int) -> 'Binary64':
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'Binary64':
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def shortValue(self) -> int:
        """
        The current implementation performs casting to a short.
        
        Overrides: Number in class Number
        
        
        """
        ...
    def sign(self) -> 'Binary64':
        """
        Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
        Specified by: sign in interface CalculusFieldElement
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'Binary64':
        """
        Sine operation.
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> 'FieldSinCos'['Binary64']:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'Binary64':
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> 'FieldSinhCosh'['Binary64']:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'Binary64':
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> 'Binary64':
        """
        Description copied from interface: square Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> 'Binary64':
        """
        Specified by: subtract in interface CalculusFieldElement
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            a (Binary64): element to subtract
        
        Returns:
            a new element representing this - a
        
        '-' operator.
        
        Specified by: subtract in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this-a
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: 'Binary64') -> 'Binary64': ...
    def tan(self) -> 'Binary64':
        """
        Tangent operation.
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> 'Binary64':
        """
        Hyperbolic tangent operation.
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> 'Binary64':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'Binary64':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def toString(self) -> str:
        """
        The returned String is equal to doubleValue())
        
        Overrides: Object in class Object
        
        Also see:
            Double
        
        
        """
        ...
    def ulp(self) -> 'Binary64':
        """
        Compute least significant bit (Unit in Last Position) for a number.
        
        Specified by: ulp in interface CalculusFieldElement
        
        Returns:
            ulp(this)
        
        
        """
        ...

class Binary64Field(org.hipparchus.Field[Binary64], java.io.Serializable):
    """
    The field of Binary64.
    
    Also see:
        Binary64, serialized
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'Binary64Field':
        """
        Returns the unique instance of this class.
        
        Returns:
            the unique instance of this class
        
        
        """
        ...
    def getOne(self) -> Binary64:
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Binary64]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> Binary64:
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

_Blendable__B = typing.TypeVar('_Blendable__B')  # <B>
class Blendable(typing.Generic[_Blendable__B]):
    """
    Interface representing classes that can blend with other instances of themselves using a given blending value.
    
    The blending value is commonly given from a SmoothStepFunction.
    """
    def blendArithmeticallyWith(self, other: _Blendable__B, blendingValue: float) -> _Blendable__B:
        """
        Blend arithmetically this instance with another one.
        
        Parameters:
            other (Blendable): other instance to blend arithmetically with
            blendingValue (double): value from smoothstep function B(x). It is expected to be between [0:1] and will throw an exception otherwise.
        
        Returns:
            this * (1 - B(x)) + other * B(x)
        
        Raises:
            MathIllegalArgumentException: if blending value is not within [0:1]
        
        
        """
        ...

class Combinations(java.lang.Iterable[typing.MutableSequence[int]]):
    """
    Utility to create combinations (n, k) of k elements in a set of n elements.
    
    Also see:
        ` Combination @ Wikipedia <http://en.wikipedia.org/wiki/Combination>`
    """
    def __init__(self, n: int, k: int):
        """
        Creates an instance whose range is the k-element subsets of {0..., n - 1} represented as int[] arrays.
        
        The iteration order is lexicographic: the arrays returned by the iterator are sorted in descending order and they are visited in lexicographic order with significance from right to left. For example, iterator() returns an iterator that will generate the following sequence of arrays on successive calls to next():
        
        
        [0, 1], [0, 2], [1, 2], [0, 3], [1, 3], [2, 3]
        If k == 0 an iterator containing an empty array is returned; if k == n an iterator containing [0..., n
        - 1] is returned.
        
        Parameters:
            n (int): Size of the set from which subsets are selected.
            k (int): Size of the subsets to be enumerated.
        
        Raises:
            MathIllegalArgumentException: if n < 0.
            MathIllegalArgumentException: if k > n.
        
        
        """
        ...
    def comparator(self) -> java.util.Comparator[typing.MutableSequence[int]]:
        """
        Defines a lexicographic ordering of combinations. The returned comparator allows to compare any two combinations that can be produced by this instance's iterator. Its compare(int[],int[]) method will throw exceptions if passed combinations that are inconsistent with this instance:
        
          - if the array lengths are not equal to k,
          - if an element of the array is not within the interval [0, n).
        
        
        Returns:
            a lexicographic comparator.
        
        
        """
        ...
    def getK(self) -> int:
        """
        Gets the number of elements in each combination.
        
        Returns:
            the size of the subsets to be enumerated.
        
        
        """
        ...
    def getN(self) -> int:
        """
        Gets the size of the set from which combinations are drawn.
        
        Returns:
            the size of the universe.
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[typing.MutableSequence[int]]:
        """
        Specified by: Iterable in interface Iterable
        
        
        """
        ...

class CombinatoricsUtils:
    """
    Combinatorial utilities.
    """
    MAX_BELL: typing.ClassVar[int] = ...
    """
    Maximum index of Bell number that fits into a long.
    
    Since:
        2.2
    
    Also see:
        constant
    
    
    """
    @staticmethod
    def bellNumber(n: int) -> int:
        """
        Compute the Bell number (number of partitions of a set).
        
        Parameters:
            n (int): number of elements of the set
        
        Returns:
            Bell number Bₙ
        
        Since:
            2.2
        
        
        """
        ...
    @staticmethod
    def binomialCoefficient(n: int, k: int) -> int:
        """
        Returns an exact representation of the ` Binomial Coefficient <http://mathworld.wolfram.com/BinomialCoefficient.html>`, "n choose k", the number of k-element subsets that can be selected from an n-element set.
        
        Preconditions:
        
          - 0 <= k <= n (otherwise MathIllegalArgumentException is thrown)
          - The result is small enough to fit into a long. The largest value of n for which all coefficients are
            MAX_VALUE is 66. If the computed value exceeds MAX_VALUE a MathRuntimeException is
            thrown.
        
        
        Parameters:
            n (int): the size of the set
            k (int): the size of the subsets to be counted
        
        Returns:
            n choose k
        
        Raises:
            MathIllegalArgumentException: if n < 0.
            MathIllegalArgumentException: if k > n.
            MathRuntimeException: if the result is too large to be represented by a long integer.
        
        
        """
        ...
    @staticmethod
    def binomialCoefficientDouble(n: int, k: int) -> float:
        """
        Returns a double representation of the ` Binomial Coefficient <http://mathworld.wolfram.com/BinomialCoefficient.html>`, "n choose k", the number of k-element subsets that can be selected from an n-element set.
        
        * Preconditions:
        
          - 0 <= k <= n (otherwise IllegalArgumentException is thrown)
          - The result is small enough to fit into a double. The largest value of n for which all coefficients are <
            Double.MAX_VALUE is 1029. If the computed value exceeds Double.MAX_VALUE, Double.POSITIVE_INFINITY is returned
        
        
        Parameters:
            n (int): the size of the set
            k (int): the size of the subsets to be counted
        
        Returns:
            n choose k
        
        Raises:
            MathIllegalArgumentException: if n < 0.
            MathIllegalArgumentException: if k > n.
            MathRuntimeException: if the result is too large to be represented by a long integer.
        
        
        """
        ...
    @staticmethod
    def binomialCoefficientLog(n: int, k: int) -> float:
        """
        Returns the natural log of the ` Binomial Coefficient <http://mathworld.wolfram.com/BinomialCoefficient.html>`, "n choose k", the number of k-element subsets that can be selected from an n-element set.
        
        * Preconditions:
        
          - 0 <= k <= n (otherwise MathIllegalArgumentException is thrown)
        
        
        Parameters:
            n (int): the size of the set
            k (int): the size of the subsets to be counted
        
        Returns:
            n choose k
        
        Raises:
            MathIllegalArgumentException: if n < 0.
            MathIllegalArgumentException: if k > n.
            MathRuntimeException: if the result is too large to be represented by a long integer.
        
        
        """
        ...
    @staticmethod
    def checkBinomial(n: int, k: int) -> None:
        """
        Check binomial preconditions.
        
        Parameters:
            n (int): Size of the set.
            k (int): Size of the subsets to be counted.
        
        Raises:
            MathIllegalArgumentException: if n < 0.
            MathIllegalArgumentException: if k > n.
        
        
        """
        ...
    @staticmethod
    def combinationsIterator(n: int, k: int) -> java.util.Iterator[typing.MutableSequence[int]]:
        """
        Returns an iterator whose range is the k-element subsets of {0..., n - 1} represented as int[] arrays.
        
        The arrays returned by the iterator are sorted in descending order and they are visited in lexicographic order with significance from right to left. For example, combinationsIterator(4, 2) returns an Iterator that will generate the following sequence of arrays on successive calls to next():
        
        [0, 1], [0, 2], [1, 2], [0, 3], [1, 3], [2, 3]
        
        If k == 0 an Iterator containing an empty array is returned and if k == n an Iterator containing [0..., n -1] is returned.
        
        Parameters:
            n (int): Size of the set from which subsets are selected.
            k (int): Size of the subsets to be enumerated.
        
        Returns:
            an Iterator over the k-sets in n.
        
        Raises:
            MathIllegalArgumentException: if n < 0.
            MathIllegalArgumentException: if k > n.
        
        
        """
        ...
    @staticmethod
    def factorial(n: int) -> int:
        """
        Returns n!. Shorthand for n ` Factorial <http://mathworld.wolfram.com/Factorial.html>`, the product of the numbers ,n.
        
        * Preconditions:
        
          - n >= 0 (otherwise MathIllegalArgumentException is thrown)
          - The result is small enough to fit into a long. The largest value of n for which n! does not
            exceed Long.MAX_VALUE} is 20. If the computed value exceeds MAX_VALUE an MathRuntimeException is
            thrown.
        
        
        Parameters:
            n (int): argument
        
        Returns:
            n!
        
        Raises:
            MathRuntimeException: if the result is too large to be represented by a long.
            MathIllegalArgumentException: if n < 0.
            MathIllegalArgumentException: if n > 20: The factorial value is too large to fit in a long.
        
        
        """
        ...
    @staticmethod
    def factorialDouble(n: int) -> float:
        """
        Compute n!, the` factorial <http://mathworld.wolfram.com/Factorial.html>` of n (the product of the numbers 1 to n), as a double. The result should be small enough to fit into a double: The largest n for which n! does not exceed MAX_VALUE is 170. If the computed value exceeds MAX_VALUE, POSITIVE_INFINITY is returned.
        
        Parameters:
            n (int): Argument.
        
        Returns:
            n!
        
        Raises:
            MathIllegalArgumentException: if n < 0.
        
        
        """
        ...
    @staticmethod
    def factorialLog(n: int) -> float:
        """
        Compute the natural logarithm of the factorial of n.
        
        Parameters:
            n (int): Argument.
        
        Returns:
            log(n!)
        
        Raises:
            MathIllegalArgumentException: if n < 0.
        
        
        """
        ...
    _partitions__T = typing.TypeVar('_partitions__T')  # <T>
    @staticmethod
    def partitions(list: java.util.List[_partitions__T]) -> java.util.stream.Stream[typing.MutableSequence[java.util.List[_partitions__T]]]:
        """
        Generate a stream of partitions of a list.
        
        This method implements the iterative algorithm described in article by B. Djokić, M. Miyakawa, S. Sekiguchi, I. Semba, and I. Stojmenović (The Computer Journal, Volume 32, Issue 3, 1989, Pages 281–282, comjnl
        
        Parameters:
            list (List<T> list): list to partition
        
        Returns:
            stream of partitions of the list, each partition is an array or parts and each part is a list of elements
        
        Since:
            2.2
        
        
        """
        ...
    _permutations__T = typing.TypeVar('_permutations__T')  # <T>
    @staticmethod
    def permutations(list: java.util.List[_permutations__T]) -> java.util.stream.Stream[java.util.List[_permutations__T]]:
        """
        Generate a stream of permutations of a list.
        
        This method implements the Steinhaus–Johnson–Trotter algorithm with Even's speedup
        
        
        Parameters:
            list (List<T> list): list to permute
        
        Returns:
            stream of permutations of the list
        
        Since:
            2.2
        
        
        """
        ...
    @staticmethod
    def stirlingS2(n: int, k: int) -> int:
        """
        Returns the ` Stirling number of the second kind <http://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html>`, "S(n,k)", the number of ways of partitioning an n-element set into k non-empty subsets.
        
        The preconditions are 0 <= k <= n (otherwise MathIllegalArgumentException is thrown)
        
        Parameters:
            n (int): the size of the set
            k (int): the number of non-empty subsets
        
        Returns:
            S(n,k)
        
        Raises:
            MathIllegalArgumentException: if k < 0.
            MathIllegalArgumentException: if k > n.
            MathRuntimeException: if some overflow happens, typically for n exceeding 25 and k between 20 and n-2 (S(n,n-1) is handled specifically and
                does not overflow)
        
        
        """
        ...
    class FactorialLog:
        @staticmethod
        def create() -> 'CombinatoricsUtils.FactorialLog': ...
        def value(self, int: int) -> float: ...
        def withCache(self, int: int) -> 'CombinatoricsUtils.FactorialLog': ...

class CompositeFormat:
    """
    Base class for formatters of composite objects (complex numbers, vectors ...).
    """
    @staticmethod
    def formatDouble(value: float, format: java.text.NumberFormat, toAppendTo: java.lang.StringBuffer, pos: java.text.FieldPosition) -> java.lang.StringBuffer:
        """
        Formats a double value to produce a string. In general, the value is formatted using the formatting rules of format. There are three exceptions to this:
        
          1.  NaN is formatted as '(NaN)' 2.  Positive infinity is formatted as '(Infinity)' 3.  Negative infinity is formatted as '(-Infinity)'
        
        
        Parameters:
            value (double): the double to format.
            format (NumberFormat): the format used.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDefaultNumberFormat() -> java.text.NumberFormat:
        """
        NumberFormat with the only customizing that the maximum number of fraction digits is set to 10.
        
        Returns:
            the default number format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDefaultNumberFormat(locale: java.util.Locale) -> java.text.NumberFormat:
        """
        NumberFormat with the only customizing that the maximum number of fraction digits is set to 10.
        
        Parameters:
            locale (Locale): the specific locale used by the format.
        
        Returns:
            the default number format specific to the given locale.
        
        
        """
        ...
    @staticmethod
    def parseAndIgnoreWhitespace(source: str, pos: java.text.ParsePosition) -> None:
        """
        Parses source until a non-whitespace character is found.
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/output parsing parameter. On output, pos holds the index of the next non-whitespace character.
        
        
        """
        ...
    @staticmethod
    def parseFixedstring(source: str, expected: str, pos: java.text.ParsePosition) -> bool:
        """
        Parse source for an expected fixed string.
        
        Parameters:
            source (String): the string to parse
            expected (String): expected string
            pos (ParsePosition): input/output parsing parameter.
        
        Returns:
            true if the expected string was there
        
        
        """
        ...
    @staticmethod
    def parseNextCharacter(source: str, pos: java.text.ParsePosition) -> str:
        """
        Parses source until a non-whitespace character is found.
        
        Parameters:
            source (String): the string to parse
            pos (ParsePosition): input/output parsing parameter.
        
        Returns:
            the first non-whitespace character.
        
        
        """
        ...
    @staticmethod
    def parseNumber(source: str, format: java.text.NumberFormat, pos: java.text.ParsePosition) -> java.lang.Number:
        """
        Parses source for a number. This method can parse normal, numeric values as well as special values. These special values include Double.NaN, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY.
        
        Parameters:
            source (String): the string to parse
            format (NumberFormat): the number format used to parse normal, numeric values.
            pos (ParsePosition): input/output parsing parameter.
        
        Returns:
            the parsed number.
        
        
        """
        ...

class ContinuedFraction:
    """
    Provides a generic means to evaluate continued fractions. Subclasses simply provided the a and b coefficients to evaluate the continued fraction.
    
    References:
    
      - ` Continued Fraction <http://mathworld.wolfram.com/ContinuedFraction.html>`
    """
    @typing.overload
    def evaluate(self, x: float) -> float: ...
    @typing.overload
    def evaluate(self, double: float, double2: float) -> float: ...
    @typing.overload
    def evaluate(self, x: float, epsilon: float, maxIterations: int) -> float: ...
    @typing.overload
    def evaluate(self, double: float, int: int) -> float: ...

class FastMath:
    """
    Faster, more accurate, portable alternative to Math and StrictMath for large scale computation.
    
    FastMath is a drop-in replacement for both Math and StrictMath. This means that for any method in Math (say sin(x) or cbrt(y)), user can directly change the class and use the methods as is (using sin(x) or cbrt(y) in the previous example).
    
    FastMath speed is achieved by relying heavily on optimizing compilers to native code present in many JVMs today and use of large tables. The larger tables are lazily initialized on first use, so that the setup time does not penalize methods that don't need them.
    
    Note that FastMath is extensively used inside Hipparchus, so by calling some algorithms, the overhead when the the tables need to be initialized will occur regardless of the end-user calling FastMath methods directly or not. Performance figures for a specific JVM and hardware can be evaluated by running the FastMathTestPerformance tests in the test directory of the source distribution.
    
    FastMath accuracy should be mostly independent of the JVM as it relies only on IEEE-754 basic operations and on embedded tables. Almost all operations are accurate to about 0.5 ulp throughout the domain range. This statement, of course is only a rough global observed behavior, it is not a guarantee for every double numbers input (see William Kahan's `Table Maker's Dilemma <http://en.wikipedia.org/wiki/Rounding#The_table-maker.27s_dilemma>`).
    
    FastMath additionally implements the following methods not found in Math/StrictMath:
    
      - asinh
      - acosh
      - atanh
    
    The following methods are found in Math/StrictMath since 1.6 only, they are provided by FastMath even in 1.5 Java virtual machines
    
      - copySign
      - getExponent
      - nextAfter
      - nextUp
      - scalb
      - copySign
      - getExponent
      - nextAfter
      - nextUp
      - scalb
    """
    PI: typing.ClassVar[float] = ...
    """
    Archimede's constant PI, ratio of circle circumference to diameter.
    
    Also see:
        constant
    
    
    """
    E: typing.ClassVar[float] = ...
    """
    Napier's constant e, base of the natural logarithm.
    
    Also see:
        constant
    
    
    """
    _IEEEremainder_1__T = typing.TypeVar('_IEEEremainder_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _IEEEremainder_2__T = typing.TypeVar('_IEEEremainder_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def IEEEremainder(dividend: float, divisor: float) -> float:
        """
        Computes the remainder as prescribed by the IEEE 754 standard.
        
        The remainder value is mathematically equal to x - y*n where n is the mathematical integer closest to the exact mathematical value of the quotient x/y. If two mathematical integers are equally close to x/y then n is the integer that is even.
        
          - If either operand is NaN, the result is NaN.
          - If the result is not NaN, the sign of the result equals the sign of the dividend.
          - If the dividend is an infinity, or the divisor is a zero, or both, the result is NaN.
          - If the dividend is finite and the divisor is an infinity, the result equals the dividend.
          - If the dividend is a zero and the divisor is finite, the result equals the dividend.
        
        
        Parameters:
            dividend (double): the number to be divided
            divisor (double): the number by which to divide
        
        Returns:
            the remainder, rounded
        
        """
        ...
    @typing.overload
    @staticmethod
    def IEEEremainder(dividend: _IEEEremainder_1__T, divisor: float) -> _IEEEremainder_1__T:
        """
        Computes the remainder as prescribed by the IEEE 754 standard.
        
        The remainder value is mathematically equal to x - yn where n is the mathematical integer closest to the exact mathematical value of the quotient x/y. If two mathematical integers are equally close to x/y then n is the integer that is even.
        
          - If either operand is NaN, the result is NaN.
          - If the result is not NaN, the sign of the result equals the sign of the dividend.
          - If the dividend is an infinity, or the divisor is a zero, or both, the result is NaN.
          - If the dividend is finite and the divisor is an infinity, the result equals the dividend.
          - If the dividend is a zero and the divisor is finite, the result equals the dividend.
        
        
        Parameters:
            dividend (T): the number to be divided
            divisor (double): the number by which to divide
        
        Returns:
            the remainder, rounded
        
        Since:
            1.3
        
        Computes the remainder as prescribed by the IEEE 754 standard.
        
        The remainder value is mathematically equal to x - yn where n is the mathematical integer closest to the exact mathematical value of the quotient x/y. If two mathematical integers are equally close to x/y then n is the integer that is even.
        
          - If either operand is NaN, the result is NaN.
          - If the result is not NaN, the sign of the result equals the sign of the dividend.
          - If the dividend is an infinity, or the divisor is a zero, or both, the result is NaN.
          - If the dividend is finite and the divisor is an infinity, the result equals the dividend.
          - If the dividend is a zero and the divisor is finite, the result equals the dividend.
        
        
        Parameters:
            dividend (T): the number to be divided
            divisor (T): the number by which to divide
        
        Returns:
            the remainder, rounded
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def IEEEremainder(dividend: _IEEEremainder_2__T, divisor: _IEEEremainder_2__T) -> _IEEEremainder_2__T: ...
    _abs_4__T = typing.TypeVar('_abs_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def abs(x: float) -> float:
        """
        Absolute value.
        
        Parameters:
            x (int): number from which absolute value is requested
        
        Returns:
            abs(x)
        
        Absolute value.
        
        Parameters:
            x (long): number from which absolute value is requested
        
        Returns:
            abs(x)
        
        Absolute value.
        
        Parameters:
            x (float): number from which absolute value is requested
        
        Returns:
            abs(x)
        
        Since:
            2.0
        
        Absolute value.
        
        Parameters:
            x (double): number from which absolute value is requested
        
        Returns:
            abs(x)
        
        """
        ...
    @typing.overload
    @staticmethod
    def abs(x: float) -> float: ...
    @typing.overload
    @staticmethod
    def abs(x: int) -> int: ...
    @typing.overload
    @staticmethod
    def abs(x: int) -> int: ...
    @typing.overload
    @staticmethod
    def abs(x: _abs_4__T) -> _abs_4__T:
        """
        Absolute value.
        
        Parameters:
            x (T): number from which absolute value is requested
        
        Returns:
            abs(x)
        
        Since:
            2.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def absExact(x: int) -> int:
        """
        Absolute value.
        
        Parameters:
            x (int): number from which absolute value is requested
        
        Returns:
            abs(x), or throws an exception for MIN_VALUE
        
        Since:
            2.0
        
        Absolute value.
        
        Parameters:
            x (long): number from which absolute value is requested
        
        Returns:
            abs(x), or throws an exception for MIN_VALUE
        
        Since:
            2.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def absExact(x: int) -> int: ...
    _acos_1__T = typing.TypeVar('_acos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def acos(x: float) -> float:
        """
        Compute the arc cosine of a number.
        
        Parameters:
            x (double): number on which evaluation is done
        
        Returns:
            arc cosine of x
        
        """
        ...
    @typing.overload
    @staticmethod
    def acos(x: _acos_1__T) -> _acos_1__T:
        """
        Compute the arc cosine of a number.
        
        Parameters:
            x (T): number on which evaluation is done
        
        Returns:
            arc cosine of x
        
        Since:
            1.3
        
        
        """
        ...
    _acosh_1__T = typing.TypeVar('_acosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def acosh(a: float) -> float:
        """
        Compute the inverse hyperbolic cosine of a number.
        
        Parameters:
            a (double): number on which evaluation is done
        
        Returns:
            inverse hyperbolic cosine of a
        
        """
        ...
    @typing.overload
    @staticmethod
    def acosh(a: _acosh_1__T) -> _acosh_1__T:
        """
        Compute the inverse hyperbolic cosine of a number.
        
        Parameters:
            a (T): number on which evaluation is done
        
        Returns:
            inverse hyperbolic cosine of a
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def addExact(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def addExact(a: int, b: int) -> int: ...
    _asin_1__T = typing.TypeVar('_asin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def asin(x: float) -> float:
        """
        Compute the arc sine of a number.
        
        Parameters:
            x (double): number on which evaluation is done
        
        Returns:
            arc sine of x
        
        """
        ...
    @typing.overload
    @staticmethod
    def asin(x: _asin_1__T) -> _asin_1__T:
        """
        Compute the arc sine of a number.
        
        Parameters:
            x (T): number on which evaluation is done
        
        Returns:
            arc sine of x
        
        Since:
            1.3
        
        
        """
        ...
    _asinh_1__T = typing.TypeVar('_asinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def asinh(a: float) -> float:
        """
        Compute the inverse hyperbolic sine of a number.
        
        Parameters:
            a (double): number on which evaluation is done
        
        Returns:
            inverse hyperbolic sine of a
        
        """
        ...
    @typing.overload
    @staticmethod
    def asinh(a: _asinh_1__T) -> _asinh_1__T:
        """
        Compute the inverse hyperbolic sine of a number.
        
        Parameters:
            a (T): number on which evaluation is done
        
        Returns:
            inverse hyperbolic sine of a
        
        Since:
            1.3
        
        
        """
        ...
    _atan_1__T = typing.TypeVar('_atan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def atan(x: float) -> float:
        """
        Arctangent function
        
        Parameters:
            x (double): a number
        
        Returns:
            atan(x)
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan(x: _atan_1__T) -> _atan_1__T:
        """
        Arctangent function
        
        Parameters:
            x (T): a number
        
        Returns:
            atan(x)
        
        Since:
            1.3
        
        
        """
        ...
    _atan2_1__T = typing.TypeVar('_atan2_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def atan2(y: float, x: float) -> float:
        """
        Two arguments arctangent function
        
        Parameters:
            y (double): ordinate
            x (double): abscissa
        
        Returns:
            phase angle of point (x,y) between -PI and PI
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(y: _atan2_1__T, x: _atan2_1__T) -> _atan2_1__T:
        """
        Two arguments arctangent function
        
        Parameters:
            y (T): ordinate
            x (T): abscissa
        
        Returns:
            phase angle of point (x,y) between -PI and PI
        
        Since:
            1.3
        
        
        """
        ...
    _atanh_1__T = typing.TypeVar('_atanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def atanh(a: float) -> float:
        """
        Compute the inverse hyperbolic tangent of a number.
        
        Parameters:
            a (double): number on which evaluation is done
        
        Returns:
            inverse hyperbolic tangent of a
        
        """
        ...
    @typing.overload
    @staticmethod
    def atanh(a: _atanh_1__T) -> _atanh_1__T:
        """
        Compute the inverse hyperbolic tangent of a number.
        
        Parameters:
            a (T): number on which evaluation is done
        
        Returns:
            inverse hyperbolic tangent of a
        
        Since:
            1.3
        
        
        """
        ...
    _cbrt_1__T = typing.TypeVar('_cbrt_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def cbrt(x: float) -> float:
        """
        Compute the cubic root of a number.
        
        Parameters:
            x (double): number on which evaluation is done
        
        Returns:
            cubic root of x
        
        """
        ...
    @typing.overload
    @staticmethod
    def cbrt(x: _cbrt_1__T) -> _cbrt_1__T:
        """
        Compute the cubic root of a number.
        
        Parameters:
            x (T): number on which evaluation is done
        
        Returns:
            cubic root of x
        
        Since:
            1.3
        
        
        """
        ...
    _ceil_1__T = typing.TypeVar('_ceil_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def ceil(x: float) -> float:
        """
        Get the smallest whole number larger than x.
        
        Parameters:
            x (double): number from which ceil is requested
        
        Returns:
            a double number c such that c is an integer c - 1.0 < x <= c
        
        """
        ...
    @typing.overload
    @staticmethod
    def ceil(x: _ceil_1__T) -> _ceil_1__T:
        """
        Get the smallest whole number larger than x.
        
        Parameters:
            x (T): number from which ceil is requested
        
        Returns:
            a double number c such that c is an integer c - 1.0 < x <= c
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def ceilDiv(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDiv(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDiv(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDivExact(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDivExact(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilMod(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilMod(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilMod(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def clamp(value: float, inf: float, sup: float) -> float:
        """
        Clamp a value within an interval.
        
        Parameters:
            value (int): value to clamp
            inf (int): lower bound of the clamping interval
            sup (int): upper bound of the clamping interval
        
        Returns:
            value clamped within [inf; sup], or value if already within bounds.
        
        Since:
            3.0
        
        Clamp a value within an interval.
        
        Parameters:
            value (long): value to clamp
            inf (long): lower bound of the clamping interval
            sup (long): upper bound of the clamping interval
        
        Returns:
            value clamped within [inf; sup], or value if already within bounds.
        
        Since:
            3.0
        
        Clamp a value within an interval.
        
        Parameters:
            value (long): value to clamp
            inf (int): lower bound of the clamping interval
            sup (int): upper bound of the clamping interval
        
        Returns:
            value clamped within [inf; sup], or value if already within bounds.
        
        Since:
            3.0
        
        Clamp a value within an interval.
        
        This method assumes -0.0 is below +0.0
        
        Parameters:
            value (float): value to clamp
            inf (float): lower bound of the clamping interval
            sup (float): upper bound of the clamping interval
        
        Returns:
            value clamped within [inf; sup], or value if already within bounds.
        
        Since:
            3.0
        
        Clamp a value within an interval.
        
        This method assumes -0.0 is below +0.0
        
        Parameters:
            value (double): value to clamp
            inf (double): lower bound of the clamping interval
            sup (double): upper bound of the clamping interval
        
        Returns:
            value clamped within [inf; sup], or value if already within bounds.
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def clamp(value: float, inf: float, sup: float) -> float: ...
    @typing.overload
    @staticmethod
    def clamp(value: int, inf: int, sup: int) -> int: ...
    @typing.overload
    @staticmethod
    def clamp(value: int, inf: int, sup: int) -> int: ...
    @typing.overload
    @staticmethod
    def clamp(value: int, inf: int, sup: int) -> int: ...
    _copySign_2__T = typing.TypeVar('_copySign_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _copySign_3__T = typing.TypeVar('_copySign_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def copySign(magnitude: float, sign: float) -> float:
        """
        Returns the first argument with the sign of the second argument. A NaN sign argument is treated as positive.
        
        Parameters:
            magnitude (double): the value to return
            sign (double): the sign for the returned value
        
        Returns:
            the magnitude with the same sign as the sign argument
        
        Returns the first argument with the sign of the second argument. A NaN sign argument is treated as positive.
        
        Parameters:
            magnitude (float): the value to return
            sign (float): the sign for the returned value
        
        Returns:
            the magnitude with the same sign as the sign argument
        
        """
        ...
    @typing.overload
    @staticmethod
    def copySign(magnitude: float, sign: float) -> float: ...
    @typing.overload
    @staticmethod
    def copySign(magnitude: _copySign_2__T, sign: float) -> _copySign_2__T:
        """
        Returns the first argument with the sign of the second argument. A NaN sign argument is treated as positive.
        
        Parameters:
            magnitude (T): the value to return
            sign (T): the sign for the returned value
        
        Returns:
            the magnitude with the same sign as the sign argument
        
        Since:
            1.3
        
        Returns the first argument with the sign of the second argument. A NaN sign argument is treated as positive.
        
        Parameters:
            magnitude (T): the value to return
            sign (double): the sign for the returned value
        
        Returns:
            the magnitude with the same sign as the sign argument
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def copySign(magnitude: _copySign_3__T, sign: _copySign_3__T) -> _copySign_3__T: ...
    _cos_1__T = typing.TypeVar('_cos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def cos(x: float) -> float:
        """
        Cosine function.
        
        Parameters:
            x (double): Argument.
        
        Returns:
            cos(x)
        
        """
        ...
    @typing.overload
    @staticmethod
    def cos(x: _cos_1__T) -> _cos_1__T:
        """
        Cosine function.
        
        Parameters:
            x (T): Argument.
        
        Returns:
            cos(x)
        
        Since:
            1.3
        
        
        """
        ...
    _cosh_1__T = typing.TypeVar('_cosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def cosh(x: float) -> float:
        """
        Compute the hyperbolic cosine of a number.
        
        Parameters:
            x (double): number on which evaluation is done
        
        Returns:
            hyperbolic cosine of x
        
        """
        ...
    @typing.overload
    @staticmethod
    def cosh(x: _cosh_1__T) -> _cosh_1__T:
        """
        Compute the hyperbolic cosine of a number.
        
        Parameters:
            x (T): number on which evaluation is done
        
        Returns:
            hyperbolic cosine of x
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def decrementExact(n: int) -> int: ...
    @typing.overload
    @staticmethod
    def decrementExact(n: int) -> int: ...
    @typing.overload
    @staticmethod
    def divideExact(x: int, y: int) -> int:
        """
        Divide two integers, checking for overflow.
        
        Parameters:
            x (int): dividend
            y (int): divisor
        
        Returns:
            x / y
        
        Raises:
            MathRuntimeException: if an overflow occurs
        
        Since:
            3.0
        
        Divide two long integers, checking for overflow.
        
        Parameters:
            x (long): dividend
            y (long): divisor
        
        Returns:
            x / y
        
        Raises:
            MathRuntimeException: if an overflow occurs
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def divideExact(x: int, y: int) -> int: ...
    _exp_1__T = typing.TypeVar('_exp_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def exp(x: float) -> float:
        """
        theoretical value for 99.9% of input values, otherwise it will have a 1 ULP error. Method: Lookup intVal = exp(int(x)) Lookup fracVal = exp(int(x-int(x) / 1024.0) * 1024.0 ); Compute z as the exponential of the remaining bits by a polynomial minus one exp(x) = intVal * fracVal * (1 + z) Accuracy: Calculation is done with 63 bits of precision, so result should be correctly rounded for 99.9% of input values, with less than 1 ULP error otherwise.
        
        Parameters:
            x (double): a double
        
        Returns:
            double e :sup:`x`
        
        """
        ...
    @typing.overload
    @staticmethod
    def exp(x: _exp_1__T) -> _exp_1__T:
        """
        theoretical value for 99.9% of input values, otherwise it will have a 1 ULP error. Method: Lookup intVal = exp(int(x)) Lookup fracVal = exp(int(x-int(x) / 1024.0) * 1024.0 ); Compute z as the exponential of the remaining bits by a polynomial minus one exp(x) = intVal * fracVal * (1 + z) Accuracy: Calculation is done with 63 bits of precision, so result should be correctly rounded for 99.9% of input values, with less than 1 ULP error otherwise.
        
        Parameters:
            x (T): a double
        
        Returns:
            double e :sup:`x`
        
        Since:
            1.3
        
        
        """
        ...
    _expm1_1__T = typing.TypeVar('_expm1_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def expm1(x: float) -> float:
        """
        Parameters:
            x (double): number to compute shifted exponential
        
        Returns:
            exp(x) - 1
        
        """
        ...
    @typing.overload
    @staticmethod
    def expm1(x: _expm1_1__T) -> _expm1_1__T:
        """
        Parameters:
            x (T): number to compute shifted exponential
        
        Returns:
            exp(x) - 1
        
        Since:
            1.3
        
        
        """
        ...
    _floor_1__T = typing.TypeVar('_floor_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def floor(x: float) -> float:
        """
        Get the largest whole number smaller than x.
        
        Parameters:
            x (double): number from which floor is requested
        
        Returns:
            a double number f such that f is an integer f <= x < f + 1.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def floor(x: _floor_1__T) -> _floor_1__T:
        """
        Get the largest whole number smaller than x.
        
        Parameters:
            x (T): number from which floor is requested
        
        Returns:
            a double number f such that f is an integer f <= x < f + 1.0
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def floorDiv(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDiv(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDiv(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDivExact(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDivExact(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorMod(a: int, b: int) -> int:
        """
        Finds r such that a = q b + r with 0 <= r < b if b > 0 and b < r <= 0 if b < 0.
        
        This methods returns the same value as integer modulo when a and b are same signs, but returns a different value when they are opposite (i.e. q is negative).
        
        Parameters:
            a (long): dividend
            b (int): divisor
        
        Returns:
            r such that a = q b + r with 0 <= r < b if b > 0 and b < r <= 0 if b < 0
        
        Raises:
            MathRuntimeException: if b == 0
        
        Since:
            1.3
        
        Also see:
            floorDiv
        
        Finds r such that a = q b + r with 0 <= r < b if b > 0 and b < r <= 0 if b < 0.
        
        This methods returns the same value as integer modulo when a and b are same signs, but returns a different value when they are opposite (i.e. q is negative).
        
        Parameters:
            a (long): dividend
            b (long): divisor
        
        Returns:
            r such that a = q b + r with 0 <= r < b if b > 0 and b < r <= 0 if b < 0
        
        Raises:
            MathRuntimeException: if b == 0
        
        Also see:
            floorDiv
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def floorMod(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorMod(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def fma(a: float, b: float, c: float) -> float:
        """
        Compute Fused-multiply-add operation a * b + c.
        
        This method was introduced in the regular Math and StrictMath methods with Java 9, and then added to Hipparchus for consistency. However, a more general method was available in Hipparchus that also allow to repeat this computation across several terms: linearCombination. The linear combination method should probably be preferred in most cases.
        
        Parameters:
            a (double): first factor
            b (double): second factor
            c (double): additive term
        
        Returns:
            a * b + c, using extended precision in the multiplication
        
        Since:
            1.3
        
        Also see:
            linearCombination, linearCombination,
            linearCombination, linearCombination
        
        Compute Fused-multiply-add operation a * b + c.
        
        This method was introduced in the regular Math and StrictMath methods with Java 9, and then added to Hipparchus for consistency. However, a more general method was available in Hipparchus that also allow to repeat this computation across several terms: linearCombination. The linear combination method should probably be preferred in most cases.
        
        Parameters:
            a (float): first factor
            b (float): second factor
            c (float): additive term
        
        Returns:
            a * b + c, using extended precision in the multiplication
        
        Also see:
            linearCombination, linearCombination,
            linearCombination, linearCombination
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def fma(a: float, b: float, c: float) -> float: ...
    @typing.overload
    @staticmethod
    def getExponent(d: float) -> int:
        """
        Return the exponent of a double number, removing the bias.
        
        For double numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
        Parameters:
            d (double): number from which exponent is requested
        
        Returns:
            exponent for d in IEEE754 representation, without bias
        
        Return the exponent of a float number, removing the bias.
        
        For float numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
        Parameters:
            f (float): number from which exponent is requested
        
        Returns:
            exponent for d in IEEE754 representation, without bias
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getExponent(float: float) -> int: ...
    _hypot_1__T = typing.TypeVar('_hypot_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def hypot(x: float, y: float) -> float:
        """
        Returns the hypotenuse of a triangle with sides x and y - sqrt(x :sup:`2`  +y :sup:`2` )
        
        avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        
        Parameters:
            x (double): a value
            y (double): a value
        
        Returns:
            sqrt(x :sup:`2`  +y :sup:`2` )
        
        """
        ...
    @typing.overload
    @staticmethod
    def hypot(x: _hypot_1__T, y: _hypot_1__T) -> _hypot_1__T:
        """
        Returns the hypotenuse of a triangle with sides x and y - sqrt(x :sup:`2`  +y :sup:`2` )
        
        avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        
        Parameters:
            x (T): a value
            y (T): a value
        
        Returns:
            sqrt(x :sup:`2`  +y :sup:`2` )
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def incrementExact(n: int) -> int: ...
    @typing.overload
    @staticmethod
    def incrementExact(n: int) -> int: ...
    _log_2__T = typing.TypeVar('_log_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def log(x: float) -> float:
        """
        Natural logarithm.
        
        Parameters:
            x (double): a double
        
        Returns:
            log(x)
        
        Computes the ` logarithm <http://mathworld.wolfram.com/Logarithm.html>` in a given base. Returns NaN if either argument is negative. If base is 0 and x is positive, 0 is returned. If base is positive and x is 0, NEGATIVE_INFINITY is returned. If both arguments are 0, the result is NaN.
        
        Parameters:
            base (double): Base of the logarithm, must be greater than 0.
            x (double): Argument, must be greater than 0.
        
        Returns:
            the value of the logarithm, i.e. the number y such that y` = x`.
        
        """
        ...
    @typing.overload
    @staticmethod
    def log(base: float, x: float) -> float: ...
    @typing.overload
    @staticmethod
    def log(x: _log_2__T) -> _log_2__T:
        """
        Natural logarithm.
        
        Parameters:
            x (T): a double
        
        Returns:
            log(x)
        
        Since:
            1.3
        
        
        """
        ...
    _log10_1__T = typing.TypeVar('_log10_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def log10(x: float) -> float:
        """
        Compute the base 10 logarithm.
        
        Parameters:
            x (double): a number
        
        Returns:
            log10(x)
        
        """
        ...
    @typing.overload
    @staticmethod
    def log10(x: _log10_1__T) -> _log10_1__T:
        """
        Compute the base 10 logarithm.
        
        Parameters:
            x (T): a number
        
        Returns:
            log10(x)
        
        Since:
            1.3
        
        
        """
        ...
    _log1p_1__T = typing.TypeVar('_log1p_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def log1p(x: float) -> float:
        """
        Parameters:
            x (double): Number.
        
        Returns:
            log(1 + x).
        
        """
        ...
    @typing.overload
    @staticmethod
    def log1p(x: _log1p_1__T) -> _log1p_1__T:
        """
        Parameters:
            x (T): Number.
        
        Returns:
            log(1 + x).
        
        Since:
            1.3
        
        
        """
        ...
    _max_4__T = typing.TypeVar('_max_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _max_5__T = typing.TypeVar('_max_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def max(a: float, b: float) -> float:
        """
        Compute the maximum of two values
        
        Parameters:
            a (int): first value
            b (int): second value
        
        Returns:
            b if a is lesser or equal to b, a otherwise
        
        Compute the maximum of two values
        
        Parameters:
            a (long): first value
            b (long): second value
        
        Returns:
            b if a is lesser or equal to b, a otherwise
        
        Compute the maximum of two values
        
        Parameters:
            a (float): first value
            b (float): second value
        
        Returns:
            b if a is lesser or equal to b, a otherwise
        
        Compute the maximum of two values
        
        Parameters:
            a (double): first value
            b (double): second value
        
        Returns:
            b if a is lesser or equal to b, a otherwise
        
        """
        ...
    @typing.overload
    @staticmethod
    def max(a: float, b: float) -> float: ...
    @typing.overload
    @staticmethod
    def max(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def max(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def max(a: _max_4__T, b: float) -> _max_4__T:
        """
        Compute the maximum of two values
        
        Parameters:
            a (T): first value
            b (T): second value
        
        Returns:
            b if a is lesser or equal to b, a otherwise
        
        Since:
            1.3
        
        Compute the maximum of two values
        
        Parameters:
            a (T): first value
            b (double): second value
        
        Returns:
            b if a is lesser or equal to b, a otherwise
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def max(a: _max_5__T, b: _max_5__T) -> _max_5__T: ...
    _min_4__T = typing.TypeVar('_min_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _min_5__T = typing.TypeVar('_min_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def min(a: float, b: float) -> float:
        """
        Compute the minimum of two values
        
        Parameters:
            a (int): first value
            b (int): second value
        
        Returns:
            a if a is lesser or equal to b, b otherwise
        
        Compute the minimum of two values
        
        Parameters:
            a (long): first value
            b (long): second value
        
        Returns:
            a if a is lesser or equal to b, b otherwise
        
        Compute the minimum of two values
        
        Parameters:
            a (float): first value
            b (float): second value
        
        Returns:
            a if a is lesser or equal to b, b otherwise
        
        Compute the minimum of two values
        
        Parameters:
            a (double): first value
            b (double): second value
        
        Returns:
            a if a is lesser or equal to b, b otherwise
        
        """
        ...
    @typing.overload
    @staticmethod
    def min(a: float, b: float) -> float: ...
    @typing.overload
    @staticmethod
    def min(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def min(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def min(a: _min_4__T, b: float) -> _min_4__T:
        """
        Compute the minimum of two values
        
        Parameters:
            a (T): first value
            b (T): second value
        
        Returns:
            a if a is lesser or equal to b, b otherwise
        
        Since:
            1.3
        
        Compute the minimum of two values
        
        Parameters:
            a (T): first value
            b (double): second value
        
        Returns:
            a if a is lesser or equal to b, b otherwise
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def min(a: _min_5__T, b: _min_5__T) -> _min_5__T: ...
    @typing.overload
    @staticmethod
    def multiplyExact(a: int, b: int) -> int:
        """
        Multiply two numbers, detecting overflows.
        
        Parameters:
            a (int): first number to multiply
            b (int): second number to multiply
        
        Returns:
            ab if no overflows occur
        
        Raises:
            MathRuntimeException: if an overflow occurs
        
        Multiply two numbers, detecting overflows.
        
        Parameters:
            a (long): first number to multiply
            b (int): second number to multiply
        
        Returns:
            ab if no overflows occur
        
        Raises:
            MathRuntimeException: if an overflow occurs
        
        Since:
            1.3
        
        Multiply two numbers, detecting overflows.
        
        Parameters:
            a (long): first number to multiply
            b (long): second number to multiply
        
        Returns:
            a*b if no overflows occur
        
        Raises:
            MathRuntimeException: if an overflow occurs
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiplyExact(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def multiplyExact(a: int, b: int) -> int: ...
    @staticmethod
    def multiplyFull(a: int, b: int) -> int:
        """
        Multiply two integers and give an exact result without overflow.
        
        Parameters:
            a (int): first factor
            b (int): second factor
        
        Returns:
            a * b exactly
        
        Since:
            1.3
        
        
        """
        ...
    @staticmethod
    def multiplyHigh(a: int, b: int) -> int:
        """
        Multiply two long integers and give the 64 most significant bits of the result.
        
        Beware that as Java primitive long are always considered to be signed, there are some intermediate values a and b for which a * b exceeds MAX_VALUE but this method will still return 0l. This happens for example for a = 2³¹ and b = 2³² as MAX_VALUE + 1, so it exceeds the max value for a long, but still fits in 64 bits, so this method correctly returns 0l in this case, but multiplication result would be considered negative (and in fact equal to MIN_VALUE
        
        Parameters:
            a (long): first factor
            b (long): second factor
        
        Returns:
            a * b / 2 :sup:`64`
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def negateExact(x: int) -> int:
        """
        Negates the argument.
        
        Parameters:
            x (int): number from which opposite value is requested
        
        Returns:
            -x, or throws an exception for MIN_VALUE
        
        Since:
            2.0
        
        Negates the argument.
        
        Parameters:
            x (long): number from which opposite value is requested
        
        Returns:
            -x, or throws an exception for MIN_VALUE
        
        Since:
            2.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def negateExact(x: int) -> int: ...
    @typing.overload
    @staticmethod
    def nextAfter(d: float, direction: float) -> float:
        """
        Get the next machine representable number after a number, moving in the direction of another number.
        
        The ordering is as follows (increasing):
        
          - -INFINITY
          - -MAX_VALUE
          - -MIN_VALUE
          - -0.0
          - +0.0
          - +MIN_VALUE
          - +MAX_VALUE
          - +INFINITY
        
        If arguments compare equal, then the second argument is returned.
        
        If direction is greater than d, the smallest machine representable number strictly greater than d is returned; if less, then the largest representable number strictly less than d is returned.
        
        If d is infinite and direction does not bring it back to finite numbers, it is returned unchanged.
        
        Parameters:
            d (double): base number
            direction (double): (the only important thing is whether direction is greater or smaller than d)
        
        Returns:
            the next machine representable number in the specified direction
        
        Get the next machine representable number after a number, moving in the direction of another number.
        
        * The ordering is as follows (increasing):
        
          - -INFINITY
          - -MAX_VALUE
          - -MIN_VALUE
          - -0.0
          - +0.0
          - +MIN_VALUE
          - +MAX_VALUE
          - +INFINITY
        
        If arguments compare equal, then the second argument is returned.
        
        If direction is greater than f, the smallest machine representable number strictly greater than f is returned; if less, then the largest representable number strictly less than f is returned.
        
        If f is infinite and direction does not bring it back to finite numbers, it is returned unchanged.
        
        Parameters:
            f (float): base number
            direction (double): (the only important thing is whether direction is greater or smaller than f)
        
        Returns:
            the next machine representable number in the specified direction
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def nextAfter(float: float, double: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextDown(a: float) -> float:
        """
        Compute next number towards negative infinity.
        
        Parameters:
            a (double): number to which neighbor should be computed
        
        Returns:
            neighbor of a towards negative infinity
        
        Compute next number towards negative infinity.
        
        Parameters:
            a (float): number to which neighbor should be computed
        
        Returns:
            neighbor of a towards negative infinity
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def nextDown(a: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextUp(a: float) -> float:
        """
        Compute next number towards positive infinity.
        
        Parameters:
            a (double): number to which neighbor should be computed
        
        Returns:
            neighbor of a towards positive infinity
        
        Compute next number towards positive infinity.
        
        Parameters:
            a (float): number to which neighbor should be computed
        
        Returns:
            neighbor of a towards positive infinity
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def nextUp(a: float) -> float: ...
    _norm__T = typing.TypeVar('_norm__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def norm(x: _norm__T) -> float:
        """
        Norm.
        
        Parameters:
            x (T): number from which norm is requested
        
        Returns:
            norm(x)
        
        Since:
            2.0
        
        
        """
        ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_4__T = typing.TypeVar('_pow_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_5__T = typing.TypeVar('_pow_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def pow(x: float, y: float) -> float:
        """
        Power function. Compute x^y.
        
        Parameters:
            x (double): a double
            y (double): a double
        
        Returns:
            double
        
        Raise a double to an int power.
        
        Parameters:
            d (double): Number to raise.
            e (int): Exponent.
        
        Returns:
            d :sup:`e`
        
        Raise a double to a long power.
        
        Parameters:
            d (double): Number to raise.
            e (long): Exponent.
        
        Returns:
            d :sup:`e`
        
        """
        ...
    @typing.overload
    @staticmethod
    def pow(double: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def pow(double: float, long: int) -> float: ...
    @typing.overload
    @staticmethod
    def pow(x: _pow_3__T, y: float) -> _pow_3__T:
        """
        Power function. Compute x :sup:`y` .
        
        Parameters:
            x (T): a double
            y (T): a double
        
        Returns:
            x :sup:`y`
        
        Since:
            1.3
        
        Power function. Compute x :sup:`y` .
        
        Parameters:
            x (T): a double
            y (double): a double
        
        Returns:
            x :sup:`y`
        
        Since:
            1.7
        
        Raise a double to an int power.
        
        Parameters:
            d (T): Number to raise.
            e (int): Exponent.
        
        Returns:
            d :sup:`e`
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def pow(t: _pow_4__T, int: int) -> _pow_4__T: ...
    @typing.overload
    @staticmethod
    def pow(t: _pow_5__T, t2: _pow_5__T) -> _pow_5__T: ...
    @staticmethod
    def random() -> float:
        """
        Returns a pseudo-random number between 0.0 and 1.0.
        
        Note: this implementation currently delegates to Math
        
        Returns:
            a random number between 0.0 and 1.0
        
        
        """
        ...
    _rint_1__T = typing.TypeVar('_rint_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rint(x: float) -> float:
        """
        Get the whole number that is the nearest to x, or the even one if x is exactly half way between two integers.
        
        Parameters:
            x (double): number from which nearest whole number is requested
        
        Returns:
            a double number r such that r is an integer r - 0.5 <= x <= r + 0.5
        
        """
        ...
    @typing.overload
    @staticmethod
    def rint(x: _rint_1__T) -> _rint_1__T:
        """
        Get the whole number that is the nearest to x, or the even one if x is exactly half way between two integers.
        
        Parameters:
            x (T): number from which nearest whole number is requested
        
        Returns:
            a double number r such that r is an integer r - 0.5 <= x <= r + 0.5
        
        Since:
            1.3
        
        
        """
        ...
    _round_2__T = typing.TypeVar('_round_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def round(x: float) -> int:
        """
        Get the closest long to x.
        
        Parameters:
            x (double): number from which closest long is requested
        
        Returns:
            closest long to x
        
        Get the closest int to x.
        
        Parameters:
            x (float): number from which closest int is requested
        
        Returns:
            closest int to x
        
        """
        ...
    @typing.overload
    @staticmethod
    def round(x: float) -> int: ...
    @typing.overload
    @staticmethod
    def round(x: _round_2__T) -> int:
        """
        Get the closest long to x.
        
        Parameters:
            x (T): number from which closest long is requested
        
        Returns:
            closest long to x
        
        Since:
            1.3
        
        
        """
        ...
    _scalb_2__T = typing.TypeVar('_scalb_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def scalb(d: float, n: int) -> float:
        """
        Multiply a double number by a power of 2.
        
        Parameters:
            d (double): number to multiply
            n (int): power of 2
        
        Returns:
            d × 2 :sup:`n`
        
        Multiply a float number by a power of 2.
        
        Parameters:
            f (float): number to multiply
            n (int): power of 2
        
        Returns:
            f × 2 :sup:`n`
        
        """
        ...
    @typing.overload
    @staticmethod
    def scalb(float: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def scalb(d: _scalb_2__T, n: int) -> _scalb_2__T:
        """
        Multiply a double number by a power of 2.
        
        Parameters:
            d (T): number to multiply
            n (int): power of 2
        
        Returns:
            d × 2 :sup:`n`
        
        Since:
            1.3
        
        
        """
        ...
    _sign__T = typing.TypeVar('_sign__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def sign(a: _sign__T) -> _sign__T:
        """
        Compute the sign of a number. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
        Parameters:
            a (T): number on which evaluation is done
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        Since:
            2.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def signum(a: float) -> float:
        """
        Compute the signum of a number. The signum is -1 for negative numbers, +1 for positive numbers and 0 otherwise
        
        Parameters:
            a (double): number on which evaluation is done
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        Compute the signum of a number. The signum is -1 for negative numbers, +1 for positive numbers and 0 otherwise
        
        Parameters:
            a (float): number on which evaluation is done
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def signum(a: float) -> float: ...
    _sin_1__T = typing.TypeVar('_sin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sin(x: float) -> float:
        """
        Sine function.
        
        Parameters:
            x (double): Argument.
        
        Returns:
            sin(x)
        
        """
        ...
    @typing.overload
    @staticmethod
    def sin(x: _sin_1__T) -> _sin_1__T:
        """
        Sine function.
        
        Parameters:
            x (T): Argument.
        
        Returns:
            sin(x)
        
        Since:
            1.3
        
        
        """
        ...
    _sinCos_0__T = typing.TypeVar('_sinCos_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sinCos(x: _sinCos_0__T) -> 'FieldSinCos'[_sinCos_0__T]:
        """
        Combined Sine and Cosine function.
        
        Parameters:
            x (T): Argument.
        
        Returns:
            [sin(x), cos(x)]
        
        Since:
            1.4
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def sinCos(x: float) -> 'SinCos':
        """
        Combined Sine and Cosine function.
        
        Parameters:
            x (double): Argument.
        
        Returns:
            [sin(x), cos(x)]
        
        """
        ...
    _sinh_1__T = typing.TypeVar('_sinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sinh(x: float) -> float:
        """
        Compute the hyperbolic sine of a number.
        
        Parameters:
            x (double): number on which evaluation is done
        
        Returns:
            hyperbolic sine of x
        
        """
        ...
    @typing.overload
    @staticmethod
    def sinh(x: _sinh_1__T) -> _sinh_1__T:
        """
        Compute the hyperbolic sine of a number.
        
        Parameters:
            x (T): number on which evaluation is done
        
        Returns:
            hyperbolic sine of x
        
        Since:
            1.3
        
        
        """
        ...
    _sinhCosh_0__T = typing.TypeVar('_sinhCosh_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sinhCosh(x: _sinhCosh_0__T) -> 'FieldSinhCosh'[_sinhCosh_0__T]:
        """
        Combined hyperbolic sine and hyperbolic cosine function.
        
        Parameters:
            x (T): Argument.
        
        Returns:
            [sinh(x), cosh(x)]
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def sinhCosh(x: float) -> 'SinhCosh':
        """
        Combined hyperbolic sine and hyperbolic cosine function.
        
        Parameters:
            x (double): Argument.
        
        Returns:
            [sinh(x), cosh(x)]
        
        """
        ...
    _sqrt_1__T = typing.TypeVar('_sqrt_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sqrt(a: float) -> float:
        """
        Compute the square root of a number.
        
        Note: this implementation currently delegates to Math
        
        Parameters:
            a (double): number on which evaluation is done
        
        Returns:
            square root of a
        
        """
        ...
    @typing.overload
    @staticmethod
    def sqrt(a: _sqrt_1__T) -> _sqrt_1__T:
        """
        Compute the square root of a number.
        
        Parameters:
            a (T): number on which evaluation is done
        
        Returns:
            square root of a
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtractExact(a: int, b: int) -> int:
        """
        Subtract two numbers, detecting overflows.
        
        Parameters:
            a (int): first number
            b (int): second number to subtract from a
        
        Returns:
            a-b if no overflows occur
        
        Raises:
            MathRuntimeException: if an overflow occurs
        
        Subtract two numbers, detecting overflows.
        
        Parameters:
            a (long): first number
            b (long): second number to subtract from a
        
        Returns:
            a-b if no overflows occur
        
        Raises:
            MathRuntimeException: if an overflow occurs
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtractExact(a: int, b: int) -> int: ...
    _tan_1__T = typing.TypeVar('_tan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tan(x: float) -> float:
        """
        Tangent function.
        
        Parameters:
            x (double): Argument.
        
        Returns:
            tan(x)
        
        """
        ...
    @typing.overload
    @staticmethod
    def tan(x: _tan_1__T) -> _tan_1__T:
        """
        Tangent function.
        
        Parameters:
            x (T): Argument.
        
        Returns:
            tan(x)
        
        Since:
            1.3
        
        
        """
        ...
    _tanh_1__T = typing.TypeVar('_tanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tanh(x: float) -> float:
        """
        Compute the hyperbolic tangent of a number.
        
        Parameters:
            x (double): number on which evaluation is done
        
        Returns:
            hyperbolic tangent of x
        
        """
        ...
    @typing.overload
    @staticmethod
    def tanh(x: _tanh_1__T) -> _tanh_1__T:
        """
        Compute the hyperbolic tangent of a number.
        
        Parameters:
            x (T): number on which evaluation is done
        
        Returns:
            hyperbolic tangent of x
        
        Since:
            1.3
        
        
        """
        ...
    _toDegrees_1__T = typing.TypeVar('_toDegrees_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def toDegrees(x: float) -> float:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Parameters:
            x (double): angle in radians
        
        Returns:
            x converted into degrees
        
        """
        ...
    @typing.overload
    @staticmethod
    def toDegrees(x: _toDegrees_1__T) -> _toDegrees_1__T:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Parameters:
            x (T): angle in radians
        
        Returns:
            x converted into degrees
        
        
        """
        ...
    @staticmethod
    def toIntExact(n: int) -> int:
        """
        Convert a long to interger, detecting overflows
        
        Parameters:
            n (long): number to convert to int
        
        Returns:
            integer with same valie as n if no overflows occur
        
        Raises:
            MathRuntimeException: if n cannot fit into an int
        
        
        """
        ...
    _toRadians_1__T = typing.TypeVar('_toRadians_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def toRadians(x: float) -> float:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Parameters:
            x (double): angle in degrees
        
        Returns:
            x converted into radians
        
        """
        ...
    @typing.overload
    @staticmethod
    def toRadians(x: _toRadians_1__T) -> _toRadians_1__T:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Parameters:
            x (T): angle in degrees
        
        Returns:
            x converted into radians
        
        
        """
        ...
    _ulp_2__T = typing.TypeVar('_ulp_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def ulp(x: float) -> float:
        """
        Parameters:
            x (double): number from which ulp is requested
        
        Returns:
            ulp(x)
        
        Compute least significant bit (Unit in Last Position) for a number.
        
        Parameters:
            x (float): number from which ulp is requested
        
        Returns:
            ulp(x)
        
        """
        ...
    @typing.overload
    @staticmethod
    def ulp(x: float) -> float: ...
    @typing.overload
    @staticmethod
    def ulp(x: _ulp_2__T) -> _ulp_2__T:
        """
        Parameters:
            x (T): number from which ulp is requested
        
        Returns:
            ulp(x)
        
        Since:
            2.0
        
        
        """
        ...
    @staticmethod
    def unsignedMultiplyHigh(a: int, b: int) -> int:
        """
        Multiply two long unsigned integers and give the 64 most significant bits of the unsigned result.
        
        Beware that as Java primitive long are always considered to be signed, there are some intermediate values a and b for which a * b exceeds MAX_VALUE but this method will still return 0l. This happens for example for a = 2³¹ and b = 2³² as MAX_VALUE + 1, so it exceeds the max value for a long, but still fits in 64 bits, so this method correctly returns 0l in this case, but multiplication result would be considered negative (and in fact equal to MIN_VALUE
        
        Parameters:
            a (long): first factor
            b (long): second factor
        
        Returns:
            a * b / 2 :sup:`64`
        
        Since:
            3.0
        
        
        """
        ...

_FieldBlendable__B = typing.TypeVar('_FieldBlendable__B')  # <B>
_FieldBlendable__T = typing.TypeVar('_FieldBlendable__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldBlendable(typing.Generic[_FieldBlendable__B, _FieldBlendable__T]):
    """
    Interface representing classes that can blend with other instances of themselves using a given blending value.
    
    The blending value is commonly given from a FieldSmoothStepFunction.
    """
    def blendArithmeticallyWith(self, other: _FieldBlendable__B, blendingValue: _FieldBlendable__T) -> _FieldBlendable__B:
        """
        Blend arithmetically this instance with another one.
        
        Parameters:
            other (FieldBlendable): other instance to blend arithmetically with
            blendingValue (FieldBlendable): value from smoothstep function B(x). It is expected to be between [0:1] and will throw an exception otherwise.
        
        Returns:
            this * (1 - B(x)) + other * B(x)
        
        Raises:
            MathIllegalArgumentException: if blending value is not within [0:1]
        
        
        """
        ...

class FieldContinuedFraction:
    """
    Provides a generic means to evaluate continued fractions. Subclasses simply provided the a and b coefficients to evaluate the continued fraction.
    
    References:
    
      - ` Continued Fraction <http://mathworld.wolfram.com/ContinuedFraction.html>`
    """
    _evaluate_0__T = typing.TypeVar('_evaluate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _evaluate_1__T = typing.TypeVar('_evaluate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _evaluate_2__T = typing.TypeVar('_evaluate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _evaluate_3__T = typing.TypeVar('_evaluate_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def evaluate(self, x: _evaluate_0__T) -> _evaluate_0__T: ...
    @typing.overload
    def evaluate(self, t: _evaluate_1__T, double: float) -> _evaluate_1__T: ...
    @typing.overload
    def evaluate(self, x: _evaluate_2__T, epsilon: float, maxIterations: int) -> _evaluate_2__T: ...
    @typing.overload
    def evaluate(self, t: _evaluate_3__T, int: int) -> _evaluate_3__T: ...
    _getA__T = typing.TypeVar('_getA__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getA(self, n: int, x: _getA__T) -> _getA__T:
        """
        Access the n-th a coefficient of the continued fraction. Since a can be a function of the evaluation point, x, that is passed in as well.
        
        Parameters:
            n (int): the coefficient index to retrieve.
            x (T): the evaluation point.
        
        Returns:
            the n-th a coefficient.
        
        
        """
        ...
    _getB__T = typing.TypeVar('_getB__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getB(self, n: int, x: _getB__T) -> _getB__T:
        """
        Access the n-th b coefficient of the continued fraction. Since b can be a function of the evaluation point, x, that is passed in as well.
        
        Parameters:
            n (int): the coefficient index to retrieve.
            x (T): the evaluation point.
        
        Returns:
            the n-th b coefficient.
        
        
        """
        ...

_FieldSinCos__T = typing.TypeVar('_FieldSinCos__T')  # <T>
class FieldSinCos(typing.Generic[_FieldSinCos__T]):
    """
    Holder for both sine and cosine values.
    
    This class is a simple container, it does not provide any computational method.
    
    Since:
        1.4
    
    Also see:
        sinCos
    """
    def __init__(self, sin: _FieldSinCos__T, cos: _FieldSinCos__T):
        """
        Simple constructor.
        
        Parameters:
            sin (FieldSinCos): value of the sine
            cos (FieldSinCos): value of the cosine
        
        
        """
        ...
    def cos(self) -> _FieldSinCos__T:
        """
        Get the value of the cosine.
        
        Returns:
            value of the cosine
        
        
        """
        ...
    _difference__S = typing.TypeVar('_difference__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def difference(scAlpha: 'FieldSinCos'[_difference__S], scBeta: 'FieldSinCos'[_difference__S]) -> 'FieldSinCos'[_difference__S]:
        """
        Compute sine and cosine of angles difference.
        
        Parameters:
            scAlpha (FieldSinCos<S> scAlpha): \((\sin \alpha, \cos \alpha)\)
            scBeta (FieldSinCos<S> scBeta): \((\sin \beta, \cos \beta)\)
        
        Returns:
            \((\sin \alpha+\beta, \cos \alpha-\beta)\)
        
        Since:
            1.8
        
        
        """
        ...
    def sin(self) -> _FieldSinCos__T:
        """
        Get the value of the sine.
        
        Returns:
            value of the sine
        
        
        """
        ...
    _sum__S = typing.TypeVar('_sum__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def sum(scAlpha: 'FieldSinCos'[_sum__S], scBeta: 'FieldSinCos'[_sum__S]) -> 'FieldSinCos'[_sum__S]:
        """
        Compute sine and cosine of angles sum.
        
        Parameters:
            scAlpha (FieldSinCos<S> scAlpha): \((\sin \alpha, \cos \alpha)\)
            scBeta (FieldSinCos<S> scBeta): \((\sin \beta, \cos \beta)\)
        
        Returns:
            \((\sin \alpha+\beta, \cos \alpha+\beta)\)
        
        Since:
            1.8
        
        
        """
        ...

_FieldSinhCosh__T = typing.TypeVar('_FieldSinhCosh__T')  # <T>
class FieldSinhCosh(typing.Generic[_FieldSinhCosh__T]):
    """
    Holder for both hyperbolic sine and hyperbolic cosine values.
    
    This class is a simple container, it does not provide any computational method.
    
    Since:
        2.0
    
    Also see:
        sinhCosh
    """
    def __init__(self, sinh: _FieldSinhCosh__T, cosh: _FieldSinhCosh__T):
        """
        Simple constructor.
        
        Parameters:
            sinh (FieldSinhCosh): value of the hyperbolic sine
            cosh (FieldSinhCosh): value of the hyperbolic cosine
        
        
        """
        ...
    def cosh(self) -> _FieldSinhCosh__T:
        """
        Get the value of the hyperbolic cosine.
        
        Returns:
            value of the hyperbolic cosine
        
        
        """
        ...
    _difference__S = typing.TypeVar('_difference__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def difference(schAlpha: 'FieldSinhCosh'[_difference__S], schBeta: 'FieldSinhCosh'[_difference__S]) -> 'FieldSinhCosh'[_difference__S]:
        """
        Compute hyperbolic sine and hyperbolic cosine of angles difference.
        
        Parameters:
            schAlpha (FieldSinhCosh<S> schAlpha): \((\sinh \alpha, \cosh \alpha)\)
            schBeta (FieldSinhCosh<S> schBeta): \((\sinh \beta, \cosh \beta)\)
        
        Returns:
            \((\sinh \alpha+\beta, \cosh \alpha-\beta)\)
        
        
        """
        ...
    def sinh(self) -> _FieldSinhCosh__T:
        """
        Get the value of the hyperbolic sine.
        
        Returns:
            value of the hyperbolic sine
        
        
        """
        ...
    _sum__S = typing.TypeVar('_sum__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def sum(schAlpha: 'FieldSinhCosh'[_sum__S], schBeta: 'FieldSinhCosh'[_sum__S]) -> 'FieldSinhCosh'[_sum__S]:
        """
        Compute hyperbolic sine and hyperbolic cosine of angles sum.
        
        Parameters:
            schAlpha (FieldSinhCosh<S> schAlpha): \((\sinh \alpha, \cosh \alpha)\)
            schBeta (FieldSinhCosh<S> schBeta): \((\sinh \beta, \cosh \beta)\)
        
        Returns:
            \((\sinh \alpha+\beta, \cosh \alpha+\beta)\)
        
        
        """
        ...

_FieldTuple__T = typing.TypeVar('_FieldTuple__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTuple(org.hipparchus.CalculusFieldElement['FieldTuple'[_FieldTuple__T]], typing.Generic[_FieldTuple__T]):
    """
    This class allows to perform the same computation of all components of a Tuple at once.
    
    Since:
        1.2
    """
    def __init__(self, *x: _FieldTuple__T):
        """
        Creates a new instance from its components.
        
        Parameters:
            x (FieldTuple...): components of the tuple
        
        
        """
        ...
    def abs(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    def acos(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Inverse hyperbolic cosine operation.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def add(self, a: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def asin(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Arc sine operation.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Inverse hyperbolic sine operation.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Arc tangent operation.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            atan(this)
        
        
        """
        ...
    def atan2(self, x: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (FieldTuple<FieldTuple> x): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def atanh(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Inverse hyperbolic tangent operation.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Cubic root.
        
        Specified by: cbrt in interface CalculusFieldElement
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Get the smallest whole number larger than instance.
        
        Specified by: ceil in interface CalculusFieldElement
        
        Returns:
            ceil(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def copySign(self, sign: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def cos(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Cosine operation.
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Returns:
            cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def divide(self, a: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def equals(self, obj: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def exp(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Exponential.
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Get the largest whole number smaller than instance.
        
        Specified by: floor in interface CalculusFieldElement
        
        Returns:
            floor(this)
        
        
        """
        ...
    def getAddendum(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getComponent(self, index: int) -> _FieldTuple__T:
        """
        Get one component of the tuple.
        
        Parameters:
            index (int): index of the component, between 0 and getDimension - 1
        
        Returns:
            value of the component
        
        
        """
        ...
    def getComponents(self) -> typing.MutableSequence[_FieldTuple__T]:
        """
        Get all components of the tuple.
        
        Returns:
            all components
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the tuple.
        
        Returns:
            dimension of the tuple
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['FieldTuple'[_FieldTuple__T]]:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getPi(self) -> 'FieldTuple'[_FieldTuple__T]:
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
        Get the real value of the number.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def hypot(self, y: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (FieldTuple<FieldTuple> y): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldTuple'[_FieldTuple__T], a2: float, b2: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldTuple'[_FieldTuple__T], a2: float, b2: 'FieldTuple'[_FieldTuple__T], a3: float, b3: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldTuple'[_FieldTuple__T], a2: float, b2: 'FieldTuple'[_FieldTuple__T], a3: float, b3: 'FieldTuple'[_FieldTuple__T], a4: float, b4: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['FieldTuple'[_FieldTuple__T]], jpype.JArray]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldTuple'[_FieldTuple__T], b1: 'FieldTuple'[_FieldTuple__T], a2: 'FieldTuple'[_FieldTuple__T], b2: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldTuple'[_FieldTuple__T], b1: 'FieldTuple'[_FieldTuple__T], a2: 'FieldTuple'[_FieldTuple__T], b2: 'FieldTuple'[_FieldTuple__T], a3: 'FieldTuple'[_FieldTuple__T], b3: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldTuple'[_FieldTuple__T], b1: 'FieldTuple'[_FieldTuple__T], a2: 'FieldTuple'[_FieldTuple__T], b2: 'FieldTuple'[_FieldTuple__T], a3: 'FieldTuple'[_FieldTuple__T], b3: 'FieldTuple'[_FieldTuple__T], a4: 'FieldTuple'[_FieldTuple__T], b4: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['FieldTuple'[_FieldTuple__T]], jpype.JArray], b: typing.Union[typing.List['FieldTuple'[_FieldTuple__T]], jpype.JArray]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def log(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Natural logarithm.
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def multiply(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def negate(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, value: float) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            value (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def pow(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def reciprocal(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def remainder(self, a: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def rint(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
        Specified by: rint in interface CalculusFieldElement
        
        Returns:
            a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, n: int) -> 'FieldTuple'[_FieldTuple__T]:
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
        Specified by: sign in interface CalculusFieldElement
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Sine operation.
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> FieldSinCos['FieldTuple'[_FieldTuple__T]]:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> FieldSinhCosh['FieldTuple'[_FieldTuple__T]]:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def subtract(self, a: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def tan(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Tangent operation.
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Hyperbolic tangent operation.
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def ulp(self) -> 'FieldTuple'[_FieldTuple__T]:
        """
        Compute least significant bit (Unit in Last Position) for a number.
        
        Specified by: ulp in interface CalculusFieldElement
        
        Returns:
            ulp(this)
        
        
        """
        ...

class Incrementor:
    """
    Utility that increments a counter until a maximum is reached, at which point, the instance will by default throw a MathIllegalStateException. However, the user is able to override this behaviour by defining a custom MaxCountExceededCallback, in order to e.g. select which exception must be thrown.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, max: int): ...
    @typing.overload
    def __init__(self, max: int, cb: typing.Union['Incrementor.MaxCountExceededCallback', typing.Callable]): ...
    @typing.overload
    def canIncrement(self) -> bool:
        """
        Checks whether incrementing the counter nTimes is allowed.
        
        Returns:
            false if calling increment will trigger a
            MathIllegalStateException, true otherwise.
        
        """
        ...
    @typing.overload
    def canIncrement(self, nTimes: int) -> bool:
        """
        Checks whether incrementing the counter several times is allowed.
        
        Parameters:
            nTimes (int): Number of increments.
        
        Returns:
            false if calling increment would call the
            MaxCountExceededCallback true otherwise.
        
        Raises:
            MathIllegalArgumentException: if nTimes is negative.
        
        
        """
        ...
    def getCount(self) -> int:
        """
        Gets the current count.
        
        Returns:
            the current count.
        
        
        """
        ...
    def getMaximalCount(self) -> int:
        """
        Gets the upper limit of the counter.
        
        Returns:
            the counter upper limit.
        
        
        """
        ...
    @typing.overload
    def increment(self) -> None:
        """
        Adds the increment value to the current iteration count. At counter exhaustion, this method will call the trigger method of the callback object passed to the withCallback method.
        
        Also see:
            increment
        
        
        """
        ...
    @typing.overload
    def increment(self, nTimes: int) -> None:
        """
        Performs multiple increments.
        
        Parameters:
            nTimes (int): Number of increments.
        
        Raises:
            MathIllegalArgumentException: if nTimes is negative.
        
        Also see:
            increment
        
        """
        ...
    def reset(self) -> None:
        """
        Resets the counter to 0.
        """
        ...
    def withCallback(self, cb: typing.Union['Incrementor.MaxCountExceededCallback', typing.Callable]) -> 'Incrementor':
        """
        Creates a new instance with a given callback. The counter is reset to 0.
        
        Parameters:
            cb (MaxCountExceededCallback): Callback to be called at counter exhaustion.
        
        Returns:
            a new instance.
        
        
        """
        ...
    def withCount(self, value: int) -> 'Incrementor':
        """
        Creates a new instance and set the counter to the given value.
        
        Parameters:
            value (int): Value of the counter.
        
        Returns:
            a new instance.
        
        
        """
        ...
    def withMaximalCount(self, max: int) -> 'Incrementor':
        """
        Creates a new instance with a given maximal count. The counter is reset to 0.
        
        Parameters:
            max (int): Maximal count.
        
        Returns:
            a new instance.
        
        Raises:
            MathIllegalArgumentException: if max is negative.
        
        
        """
        ...
    class MaxCountExceededCallback:
        def trigger(self, int: int) -> None: ...

class IterationEvent(java.util.EventObject):
    """
    The root class from which all events occurring while running an IterationManager should be derived.
    
    Also see:
        serialized
    """
    def __init__(self, source: typing.Any, iterations: int):
        """
        Creates a new instance of this class.
        
        Parameters:
            source (Object): the iterative algorithm on which the event initially occurred
            iterations (int): the number of iterations performed at the time this event is created
        
        
        """
        ...
    def getIterations(self) -> int:
        """
        Returns the number of iterations performed at the time this event is created.
        
        Returns:
            the number of iterations performed
        
        
        """
        ...

class IterationListener(java.util.EventListener):
    """
    The listener interface for receiving events occurring in an iterative algorithm.
    """
    def initializationPerformed(self, e: IterationEvent) -> None:
        """
        Invoked after completion of the initial phase of the iterative algorithm (prior to the main iteration loop).
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...
    def iterationPerformed(self, e: IterationEvent) -> None:
        """
        Invoked each time an iteration is completed (in the main iteration loop).
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...
    def iterationStarted(self, e: IterationEvent) -> None:
        """
        Invoked each time a new iteration is completed (in the main iteration loop).
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...
    def terminationPerformed(self, e: IterationEvent) -> None:
        """
        Invoked after completion of the operations which occur after breaking out of the main iteration loop.
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...

class IterationManager:
    """
    This abstract class provides a general framework for managing iterative algorithms. The maximum number of iterations can be set, and methods are provided to monitor the current iteration count. A lightweight event framework is also provided.
    """
    @typing.overload
    def __init__(self, maxIterations: int): ...
    @typing.overload
    def __init__(self, maxIterations: int, callBack: typing.Union[Incrementor.MaxCountExceededCallback, typing.Callable]): ...
    def addIterationListener(self, listener: IterationListener) -> None:
        """
        Attaches a listener to this manager.
        
        Parameters:
            listener (IterationListener): A IterationListener object.
        
        
        """
        ...
    def fireInitializationEvent(self, e: IterationEvent) -> None:
        """
        Informs all registered listeners that the initial phase (prior to the main iteration loop) has been completed.
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...
    def fireIterationPerformedEvent(self, e: IterationEvent) -> None:
        """
        Informs all registered listeners that a new iteration (in the main iteration loop) has been performed.
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...
    def fireIterationStartedEvent(self, e: IterationEvent) -> None:
        """
        Informs all registered listeners that a new iteration (in the main iteration loop) has been started.
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...
    def fireTerminationEvent(self, e: IterationEvent) -> None:
        """
        Informs all registered listeners that the final phase (post-iterations) has been completed.
        
        Parameters:
            e (IterationEvent): The IterationEvent object.
        
        
        """
        ...
    def getIterations(self) -> int:
        """
        Returns the number of iterations of this solver, 0 if no iterations has been performed yet.
        
        Returns:
            the number of iterations.
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
        Returns the maximum number of iterations.
        
        Returns:
            the maximum number of iterations.
        
        
        """
        ...
    def incrementIterationCount(self) -> None:
        """
        Increments the iteration count by one, and throws an exception if the maximum number of iterations is reached. This method should be called at the beginning of a new iteration.
        
        Raises:
            MathIllegalStateException: if the maximum number of iterations is reached.
        
        
        """
        ...
    def removeIterationListener(self, listener: IterationListener) -> None:
        """
        Removes the specified iteration listener from the list of listeners currently attached to this object. Attempting to remove a listener which was not previously registered does not cause any error.
        
        Parameters:
            listener (IterationListener): The IterationListener to be removed.
        
        
        """
        ...
    def resetIterationCount(self) -> None:
        """
        Sets the iteration count to 0. This method must be called during the initial phase.
        """
        ...

class KthSelector(java.io.Serializable):
    """
    A Simple K :sup:`th` selector implementation to pick up the K :sup:`th` ordered element from a work array containing the input numbers.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, pivotingStrategy: 'PivotingStrategy'): ...
    def getPivotingStrategy(self) -> 'PivotingStrategy':
        """
        Get the pivoting strategy.
        
        Returns:
            pivoting strategy
        
        
        """
        ...
    def select(self, work: typing.Union[typing.List[float], jpype.JArray], pivotsHeap: typing.Union[typing.List[int], jpype.JArray], k: int) -> float:
        """
        Select K :sup:`th` value in the array.
        
        Parameters:
            work (double[]): work array to use to find out the K :sup:`th` value
            pivotsHeap (int[]): cached pivots heap that can be used for efficient estimation
            k (int): the index whose value in the array is of interest
        
        Returns:
            K :sup:`th` value
        
        
        """
        ...

class MathArrays:
    """
    Arrays utilities.
    """
    _buildArray_0__T = typing.TypeVar('_buildArray_0__T', bound=org.hipparchus.FieldElement)  # <T>
    _buildArray_1__T = typing.TypeVar('_buildArray_1__T', bound=org.hipparchus.FieldElement)  # <T>
    _buildArray_2__T = typing.TypeVar('_buildArray_2__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def buildArray(field: org.hipparchus.Field[_buildArray_0__T], length: int) -> typing.MutableSequence[_buildArray_0__T]:
        """
        Build an array of elements.
        
        Arrays are filled with getZero()
        
        Parameters:
            field (Field<T> field): field to which array elements belong
            length (int): of the array
        
        Returns:
            a new array
        
        Build a double dimension array of elements.
        
        Arrays are filled with getZero()
        
        Parameters:
            field (Field<T> field): field to which array elements belong
            rows (int): number of rows in the array
            columns (int): number of columns (may be negative to build partial arrays in the same way new Field[rows][] works)
        
        Returns:
            a new array
        
        Build a triple dimension array of elements.
        
        Arrays are filled with getZero()
        
        Parameters:
            field (Field<T> field): field to which array elements belong
            l1 (int): number of elements along first dimension
            l2 (int): number of elements along second dimension
            l3 (int): number of elements along third dimension (may be negative to build partial arrays in the same way new
                Field[l1][l2][] works)
        
        Returns:
            a new array
        
        Since:
            1.4
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def buildArray(field: org.hipparchus.Field[_buildArray_1__T], rows: int, columns: int) -> typing.MutableSequence[typing.MutableSequence[_buildArray_1__T]]: ...
    @typing.overload
    @staticmethod
    def buildArray(field: org.hipparchus.Field[_buildArray_2__T], l1: int, l2: int, l3: int) -> typing.MutableSequence[typing.MutableSequence[typing.MutableSequence[_buildArray_2__T]]]: ...
    _checkEqualLength_2__T = typing.TypeVar('_checkEqualLength_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _checkEqualLength_5__T = typing.TypeVar('_checkEqualLength_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def checkEqualLength(a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray], abort: bool) -> bool:
        """
        Check that both arrays have the same length.
        
        Parameters:
            a (double[]): Array.
            b (double[]): Array.
            abort (boolean): Whether to throw an exception if the check fails.
        
        Returns:
            true if the arrays have the same length.
        
        Raises:
            MathIllegalArgumentException: if the lengths differ and abort is true.
        
        Check that both arrays have the same length.
        
        Parameters:
            a (int[]): Array.
            b (int[]): Array.
            abort (boolean): Whether to throw an exception if the check fails.
        
        Returns:
            true if the arrays have the same length.
        
        Raises:
            MathIllegalArgumentException: if the lengths differ and abort is true.
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkEqualLength(a: typing.Union[typing.List[int], jpype.JArray], b: typing.Union[typing.List[int], jpype.JArray], abort: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(a: typing.Union[typing.List[_checkEqualLength_2__T], jpype.JArray], b: typing.Union[typing.List[_checkEqualLength_2__T], jpype.JArray], abort: bool) -> bool:
        """
        Check that both arrays have the same length.
        
        Parameters:
            a (T[]): Array.
            b (T[]): Array.
            abort (boolean): Whether to throw an exception if the check fails.
        
        Returns:
            true if the arrays have the same length.
        
        Raises:
            MathIllegalArgumentException: if the lengths differ and abort is true.
        
        Since:
            1.5
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkEqualLength(a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Check that both arrays have the same length.
        
        Parameters:
            a (double[]): Array.
            b (double[]): Array.
        
        Raises:
            MathIllegalArgumentException: if the lengths differ.
        
        Check that both arrays have the same length.
        
        Parameters:
            a (int[]): Array.
            b (int[]): Array.
        
        Raises:
            MathIllegalArgumentException: if the lengths differ.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkEqualLength(a: typing.Union[typing.List[int], jpype.JArray], b: typing.Union[typing.List[int], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(a: typing.Union[typing.List[_checkEqualLength_5__T], jpype.JArray], b: typing.Union[typing.List[_checkEqualLength_5__T], jpype.JArray]) -> None:
        """
        Check that both arrays have the same length.
        
        Parameters:
            a (T[]): Array.
            b (T[]): Array.
        
        Raises:
            MathIllegalArgumentException: if the lengths differ.
        
        Since:
            1.5
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkNonNegative(in_: typing.Union[typing.List[int], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def checkNonNegative(in_: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> None: ...
    @staticmethod
    def checkNotNaN(in_: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Check that no entry of the input array is NaN.
        
        Parameters:
            in (double[]): Array to be tested.
        
        Raises:
            MathIllegalArgumentException: if an entry is NaN.
        
        
        """
        ...
    _checkOrder_1__T = typing.TypeVar('_checkOrder_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _checkOrder_4__T = typing.TypeVar('_checkOrder_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _checkOrder_5__T = typing.TypeVar('_checkOrder_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def checkOrder(val: typing.Union[typing.List[float], jpype.JArray], dir: 'MathArrays.OrderDirection', strict: bool, abort: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkOrder(val: typing.Union[typing.List[_checkOrder_1__T], jpype.JArray], dir: 'MathArrays.OrderDirection', strict: bool, abort: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkOrder(val: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def checkOrder(val: typing.Union[typing.List[float], jpype.JArray], dir: 'MathArrays.OrderDirection', strict: bool) -> None: ...
    @typing.overload
    @staticmethod
    def checkOrder(val: typing.Union[typing.List[_checkOrder_4__T], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def checkOrder(val: typing.Union[typing.List[_checkOrder_5__T], jpype.JArray], dir: 'MathArrays.OrderDirection', strict: bool) -> None: ...
    @staticmethod
    def checkPositive(in_: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Check that all entries of the input array are strictly positive.
        
        Parameters:
            in (double[]): Array to be tested
        
        Raises:
            MathIllegalArgumentException: if any entries of the array are not strictly positive.
        
        
        """
        ...
    @staticmethod
    def checkRectangular(in_: typing.Union[typing.List[typing.MutableSequence[int]], jpype.JArray]) -> None:
        """
        Throws MathIllegalArgumentException if the input array is not rectangular.
        
        Parameters:
            in (long[][]): array to be tested
        
        Raises:
            NullArgumentException: if input array is null
            MathIllegalArgumentException: if input array is not rectangular
        
        
        """
        ...
    @staticmethod
    def concatenate(*x: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Concatenates a sequence of arrays. The return array consists of the entries of the input arrays concatenated in the order they appear in the argument list. Null arrays cause NullPointerExceptions; zero length arrays are allowed (contributing nothing to the output array).
        
        Parameters:
            x (double[]...): list of double[] arrays to concatenate
        
        Returns:
            a new array consisting of the entries of the argument arrays
        
        Raises:
            NullPointerException: if any of the arrays are null
        
        
        """
        ...
    @staticmethod
    def convolve(x: typing.Union[typing.List[float], jpype.JArray], h: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Calculates the ` convolution <http://en.wikipedia.org/wiki/Convolution>` between two sequences.
        
        The solution is obtained via straightforward computation of the convolution sum (and not via FFT). Whenever the computation needs an element that would be located at an index outside the input arrays, the value is assumed to be zero.
        
        Parameters:
            x (double[]): First sequence. Typically, this sequence will represent an input signal to a system.
            h (double[]): Second sequence. Typically, this sequence will represent the impulse response of the system.
        
        Returns:
            the convolution of x and h. This array's length will be length - 1.
        
        Raises:
            NullArgumentException: if either x or h is null.
            MathIllegalArgumentException: if either x or h is empty.
        
        
        """
        ...
    @staticmethod
    def cosAngle(v1: typing.Union[typing.List[float], jpype.JArray], v2: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Calculates the cosine of the angle between two vectors.
        
        Parameters:
            v1 (double[]): Cartesian coordinates of the first vector.
            v2 (double[]): Cartesian coordinates of the second vector.
        
        Returns:
            the cosine of the angle between the vectors.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def distance(p1: typing.Union[typing.List[float], jpype.JArray], p2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def distance(p1: typing.Union[typing.List[int], jpype.JArray], p2: typing.Union[typing.List[int], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def distance1(p1: typing.Union[typing.List[float], jpype.JArray], p2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def distance1(p1: typing.Union[typing.List[int], jpype.JArray], p2: typing.Union[typing.List[int], jpype.JArray]) -> int: ...
    @typing.overload
    @staticmethod
    def distanceInf(p1: typing.Union[typing.List[float], jpype.JArray], p2: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    @staticmethod
    def distanceInf(p1: typing.Union[typing.List[int], jpype.JArray], p2: typing.Union[typing.List[int], jpype.JArray]) -> int: ...
    @staticmethod
    def ebeAdd(a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Creates an array whose contents will be the element-by-element addition of the arguments.
        
        Parameters:
            a (double[]): First term of the addition.
            b (double[]): Second term of the addition.
        
        Returns:
            a new array r where r[i] = a[i] + b[i].
        
        Raises:
            MathIllegalArgumentException: if the array lengths differ.
        
        
        """
        ...
    @staticmethod
    def ebeDivide(a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Creates an array whose contents will be the element-by-element division of the first argument by the second.
        
        Parameters:
            a (double[]): Numerator of the division.
            b (double[]): Denominator of the division.
        
        Returns:
            a new array r where r[i] = a[i] / b[i].
        
        Raises:
            MathIllegalArgumentException: if the array lengths differ.
        
        
        """
        ...
    @staticmethod
    def ebeMultiply(a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Creates an array whose contents will be the element-by-element multiplication of the arguments.
        
        Parameters:
            a (double[]): First factor of the multiplication.
            b (double[]): Second factor of the multiplication.
        
        Returns:
            a new array r where r[i] = a[i] * b[i].
        
        Raises:
            MathIllegalArgumentException: if the array lengths differ.
        
        
        """
        ...
    @staticmethod
    def ebeSubtract(a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Creates an array whose contents will be the element-by-element subtraction of the second argument from the first.
        
        Parameters:
            a (double[]): First term.
            b (double[]): Element to be subtracted.
        
        Returns:
            a new array r where r[i] = a[i] - b[i].
        
        Raises:
            MathIllegalArgumentException: if the array lengths differ.
        
        
        """
        ...
    _equals_6__T = typing.TypeVar('_equals_6__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(x: typing.Union[typing.List[int], jpype.JArray, bytes], y: typing.Union[typing.List[int], jpype.JArray, bytes]) -> bool:
        """
        Returns true iff both arguments are null or have same dimensions and all their elements are equal as defined by equals.
        
        Parameters:
            x (float[]): first array
            y (float[]): second array
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        Returns true iff both arguments are null or have same dimensions and all their elements are equal as defined by equals.
        
        Parameters:
            x (double[]): First array.
            y (double[]): Second array.
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        Returns true if both arguments are null or have same dimensions and all their elements are equals.
        
        Parameters:
            x (long[]): First array.
            y (long[]): Second array.
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        Returns true if both arguments are null or have same dimensions and all their elements are equals.
        
        Parameters:
            x (int[]): First array.
            y (int[]): Second array.
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        Returns true if both arguments are null or have same dimensions and all their elements are equals.
        
        Parameters:
            x (byte[]): First array.
            y (byte[]): Second array.
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        Returns true if both arguments are null or have same dimensions and all their elements are equals.
        
        Parameters:
            x (short[]): First array.
            y (short[]): Second array.
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(x: typing.Union[typing.List[int], jpype.JArray], y: typing.Union[typing.List[int], jpype.JArray]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(x: typing.Union[typing.List[int], jpype.JArray], y: typing.Union[typing.List[int], jpype.JArray]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(x: typing.Union[typing.List[_equals_6__T], jpype.JArray], y: typing.Union[typing.List[_equals_6__T], jpype.JArray]) -> bool:
        """
        Returns true iff both arguments are null or have same dimensions and all their elements are equal as defined by Object.
        
        Parameters:
            x (T[]): First array.
            y (T[]): Second array.
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        Since:
            4.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(x: typing.Union[typing.List[int], jpype.JArray], y: typing.Union[typing.List[int], jpype.JArray]) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> bool:
        """
        Returns true iff both arguments are null or have same dimensions and all their elements are equal as defined by equalsIncludingNaN.
        
        Parameters:
            x (float[]): first array
            y (float[]): second array
        
        Returns:
            true if the values are both null or have same dimension and equal elements
        
        Returns true iff both arguments are null or have same dimensions and all their elements are equal as defined by equalsIncludingNaN.
        
        Parameters:
            x (double[]): First array.
            y (double[]): Second array.
        
        Returns:
            true if the values are both null or have same dimension and equal elements.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(x: typing.Union[typing.List[float], jpype.JArray], y: typing.Union[typing.List[float], jpype.JArray]) -> bool: ...
    _isMonotonic_1__T = typing.TypeVar('_isMonotonic_1__T', bound=java.lang.Comparable)  # <T>
    @typing.overload
    @staticmethod
    def isMonotonic(val: typing.Union[typing.List[float], jpype.JArray], dir: 'MathArrays.OrderDirection', strict: bool) -> bool:
        """
        Check that an array is monotonically increasing or decreasing.
        
        Parameters:
            val (double[]): Values.
            dir (OrderDirection): Ordering direction.
            strict (boolean): Whether the order should be strict.
        
        Returns:
            true if sorted, false otherwise.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isMonotonic(val: typing.Union[typing.List[_isMonotonic_1__T], jpype.JArray], dir: 'MathArrays.OrderDirection', strict: bool) -> bool:
        """
        Check that an array is monotonically increasing or decreasing.
        
        Parameters:
            val (T[]): Values.
            dir (OrderDirection): Ordering direction.
            strict (boolean): Whether the order should be strict.
        
        Returns:
            true if sorted, false otherwise.
        
        """
        ...
    @typing.overload
    @staticmethod
    def linearCombination(a1: float, b1: float, a2: float, b2: float) -> float:
        """
        Compute a linear combination accurately.
        
        This method computes a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` to high accuracy. It does so by using specific multiplication and addition algorithms to preserve accuracy and reduce cancellation effects. It is based on the 2005 paper ` Accurate Sum and Dot Product <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.1547>` by Takeshi Ogita, Siegfried M. Rump, and Shin'ichi Oishi published in SIAM J. Sci. Comput.
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (double): second factor of the first term
            a2 (double): first factor of the second term
            b2 (double): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination, linearCombination
        
        Compute a linear combination accurately.
        
        This method computes a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` to high accuracy. It does so by using specific multiplication and addition algorithms to preserve accuracy and reduce cancellation effects. It is based on the 2005 paper ` Accurate Sum and Dot Product <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.1547>` by Takeshi Ogita, Siegfried M. Rump, and Shin'ichi Oishi published in SIAM J. Sci. Comput.
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (double): second factor of the first term
            a2 (double): first factor of the second term
            b2 (double): second factor of the second term
            a3 (double): first factor of the third term
            b3 (double): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination, linearCombination
        
        Compute a linear combination accurately.
        
        This method computes a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4` to high accuracy. It does so by using specific multiplication and addition algorithms to preserve accuracy and reduce cancellation effects. It is based on the 2005 paper ` Accurate Sum and Dot Product <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.1547>` by Takeshi Ogita, Siegfried M. Rump, and Shin'ichi Oishi published in SIAM J. Sci. Comput.
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (double): second factor of the first term
            a2 (double): first factor of the second term
            b2 (double): second factor of the second term
            a3 (double): first factor of the third term
            b3 (double): second factor of the third term
            a4 (double): first factor of the third term
            b4 (double): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination, linearCombination
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def linearCombination(a1: float, b1: float, a2: float, b2: float, a3: float, b3: float) -> float: ...
    @typing.overload
    @staticmethod
    def linearCombination(a1: float, b1: float, a2: float, b2: float, a3: float, b3: float, a4: float, b4: float) -> float: ...
    @typing.overload
    @staticmethod
    def linearCombination(a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @staticmethod
    def natural(n: int) -> typing.MutableSequence[int]:
        """
        Returns an array representing the natural number n.
        
        Parameters:
            n (int): Natural number.
        
        Returns:
            an array whose entries are the numbers 0, 1..., n-1. If n == 0, the returned array is empty.
        
        
        """
        ...
    @staticmethod
    def normalizeArray(values: typing.Union[typing.List[float], jpype.JArray], normalizedSum: float) -> typing.MutableSequence[float]:
        """
        Normalizes an array to make it sum to a specified value. Returns the result of the transformation
        
            x ↦ x * normalizedSum / sum applied to each non-NaN element x of the input array, where sum is the sum of the non-NaN entries in the input array.
        
        Throws IllegalArgumentException if normalizedSum is infinite or NaN and ArithmeticException if the input array contains any infinite elements or sums to 0.
        
        Ignores (i.e., copies unchanged to the output array) NaNs in the input array. The input array is unchanged by this method.
        
        Parameters:
            values (double[]): Input array to be normalized
            normalizedSum (double): Target sum for the normalized array
        
        Returns:
            the normalized array
        
        Raises:
            MathRuntimeException: if the input array contains infinite elements or sums to zero
            MathIllegalArgumentException: if the target sum is infinite or NaN
        
        
        """
        ...
    @staticmethod
    def safeNorm(v: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Returns the Cartesian norm (2-norm), handling both overflow and underflow. Translation of the minpack enorm subroutine.
        
        The redistribution policy for MINPACK is available `here <http://www.netlib.org/minpack/disclaimer>`, for convenience, it is reproduced below.
        
            Minpack Copyright Notice (1999) University of Chicago. All rights reserved
        
            Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
        
              1.  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 2.  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. 3.  The end-user documentation included with the redistribution, if any, must include the following acknowledgment: This product includes software developed by the University of Chicago, as Operator of Argonne National Laboratory Alternately, this acknowledgment may appear in the software itself, if and wherever such third-party acknowledgments normally appear. 4.  WARRANTY DISCLAIMER. THE SOFTWARE IS SUPPLIED "AS IS" WITHOUT WARRANTY OF ANY KIND. THE COPYRIGHT HOLDER, THE UNITED STATES, THE UNITED STATES DEPARTMENT OF ENERGY, AND THEIR EMPLOYEES: (1) DISCLAIM ANY WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR NON-INFRINGEMENT, (2) DO NOT ASSUME ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF THE SOFTWARE, (3) DO NOT REPRESENT THAT USE OF THE SOFTWARE WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS, (4) DO NOT WARRANT THAT THE SOFTWARE WILL FUNCTION UNINTERRUPTED, THAT IT IS ERROR-FREE OR THAT ANY ERRORS WILL BE CORRECTED. 5.  LIMITATION OF LIABILITY. IN NO EVENT WILL THE COPYRIGHT HOLDER, THE UNITED STATES, THE UNITED STATES DEPARTMENT OF ENERGY, OR THEIR EMPLOYEES: BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL OR PUNITIVE DAMAGES OF ANY KIND OR NATURE, INCLUDING BUT NOT LIMITED TO LOSS OF PROFITS OR LOSS OF DATA, FOR ANY REASON WHATSOEVER, WHETHER SUCH LIABILITY IS ASSERTED ON THE BASIS OF CONTRACT, TORT (INCLUDING NEGLIGENCE OR STRICT LIABILITY), OR OTHERWISE, EVEN IF ANY OF SAID PARTIES HAS BEEN WARNED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGES.
        
        
        Parameters:
            v (double[]): Vector of doubles.
        
        Returns:
            the 2-norm of the vector.
        
        
        """
        ...
    @staticmethod
    def scale(val: float, arr: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Create a copy of an array scaled by a value.
        
        Parameters:
            arr (double): Array to scale.
            val (double[]): Scalar.
        
        Returns:
            scaled copy of array with each entry multiplied by val.
        
        
        """
        ...
    @staticmethod
    def scaleInPlace(val: float, arr: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Multiply each element of an array by a value.
        
        The array is modified in place (no copy is created).
        
        Parameters:
            arr (double): Array to scale
            val (double[]): Scalar
        
        
        """
        ...
    @staticmethod
    def sequence(size: int, start: int, stride: int) -> typing.MutableSequence[int]:
        """
        Returns an array of size integers starting at start, skipping stride numbers.
        
        Parameters:
            size (int): Natural number.
            start (int): Natural number.
            stride (int): Natural number.
        
        Returns:
            an array whose entries are the numbers , start + (size - 1) * stride. If size
            == 0, the returned array is empty.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def shuffle(list: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
        Shuffle the entries of the given array.
        
        Parameters:
            list (int[]): Array whose entries will be shuffled (in-place).
        
        Also see:
            shuffle
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def shuffle(list: typing.Union[typing.List[int], jpype.JArray], start: int, pos: 'MathArrays.Position') -> None:
        """
        Shuffle the entries of the given array. The start and pos parameters select which portion of the array is randomized and which is left untouched.
        
        Parameters:
            list (int[]): Array whose entries will be shuffled (in-place).
            start (int): Index at which shuffling begins.
            pos (Position): Shuffling is performed for index positions between start and either the end (if
                TAIL) or the beginning (if
                HEAD) of the array.
        
        Also see:
            shuffle
        
        Shuffle the entries of the given array, using the Fisher algorithm. The start and pos parameters select which portion of the array is randomized and which is left untouched.
        
        Parameters:
            list (int[]): Array whose entries will be shuffled (in-place).
            start (int): Index at which shuffling begins.
            pos (Position): Shuffling is performed for index positions between start and either the end (if
                TAIL) or the beginning (if
                HEAD) of the array.
            rng (RandomGenerator): Random number generator.
        
        """
        ...
    @typing.overload
    @staticmethod
    def shuffle(list: typing.Union[typing.List[int], jpype.JArray], start: int, pos: 'MathArrays.Position', rng: org.hipparchus.random.RandomGenerator) -> None: ...
    @typing.overload
    @staticmethod
    def shuffle(list: typing.Union[typing.List[int], jpype.JArray], rng: org.hipparchus.random.RandomGenerator) -> None:
        """
        Shuffle the entries of the given array.
        
        Parameters:
            list (int[]): Array whose entries will be shuffled (in-place).
            rng (RandomGenerator): Random number generator.
        
        Also see:
            shuffle
        
        """
        ...
    @typing.overload
    @staticmethod
    def sortInPlace(x: typing.Union[typing.List[float], jpype.JArray], *yList: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def sortInPlace(x: typing.Union[typing.List[float], jpype.JArray], dir: 'MathArrays.OrderDirection', *yList: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @staticmethod
    def unique(data: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Returns an array consisting of the unique values in data. The return array is sorted in descending order. Empty arrays are allowed, but null arrays result in NullPointerException. Infinities are allowed. NaN values are allowed with maximum sort order - i.e., if there are NaN values in data, NaN will be the first element of the output array, even if the array also contains POSITIVE_INFINITY.
        
        Parameters:
            data (double[]): array to scan
        
        Returns:
            descending list of values included in the input array
        
        Raises:
            NullPointerException: if data is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def verifyValues(doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> bool: ...
    @typing.overload
    @staticmethod
    def verifyValues(values: typing.Union[typing.List[float], jpype.JArray], weights: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int, allowEmpty: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def verifyValues(values: typing.Union[typing.List[float], jpype.JArray], begin: int, length: int) -> bool: ...
    @typing.overload
    @staticmethod
    def verifyValues(doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int, boolean: bool) -> bool: ...
    class Function:
        @typing.overload
        def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
        @typing.overload
        def evaluate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> float: ...
    class OrderDirection(java.lang.Enum['MathArrays.OrderDirection']):
        INCREASING: typing.ClassVar['MathArrays.OrderDirection'] = ...
        DECREASING: typing.ClassVar['MathArrays.OrderDirection'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MathArrays.OrderDirection': ...
        @staticmethod
        def values() -> typing.MutableSequence['MathArrays.OrderDirection']: ...
    class Position(java.lang.Enum['MathArrays.Position']):
        HEAD: typing.ClassVar['MathArrays.Position'] = ...
        TAIL: typing.ClassVar['MathArrays.Position'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MathArrays.Position': ...
        @staticmethod
        def values() -> typing.MutableSequence['MathArrays.Position']: ...

_MathUtils__FieldSumAndResidual__T = typing.TypeVar('_MathUtils__FieldSumAndResidual__T', bound=org.hipparchus.FieldElement)  # <T>
class MathUtils:
    """
    Miscellaneous utility functions.
    
    Also see:
        ArithmeticUtils, Precision,
        MathArrays
    """
    TWO_PI: typing.ClassVar[float] = ...
    """
    \(2\pi\)
    
    Also see:
        constant
    
    
    """
    PI_SQUARED: typing.ClassVar[float] = ...
    """
    \(\pi^2\)
    
    Also see:
        constant
    
    
    """
    SEMI_PI: typing.ClassVar[float] = ...
    """
    \(\pi/2\).
    
    Also see:
        constant
    
    
    """
    @staticmethod
    def checkDimension(dimension: int, otherDimension: int) -> None:
        """
        Checks that the given dimensions match.
        
        Parameters:
            dimension (int): the first dimension.
            otherDimension (int): the second dimension.
        
        Raises:
            MathIllegalArgumentException: if length != otherLength.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkFinite(double: float) -> None: ...
    @typing.overload
    @staticmethod
    def checkFinite(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def checkNotNull(o: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkNotNull(o: typing.Any, pattern: org.hipparchus.exception.Localizable, *args: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkRangeInclusive(value: float, lo: float, hi: float) -> None:
        """
        Checks that the given value is strictly within the range [lo, hi].
        
        Parameters:
            value (long): value to be checked.
            lo (long): the lower bound (inclusive).
            hi (long): the upper bound (inclusive).
        
        Raises:
            MathIllegalArgumentException: if value is strictly outside [lo, hi].
        
        Checks that the given value is strictly within the range [lo, hi].
        
        Parameters:
            value (double): value to be checked.
            lo (double): the lower bound (inclusive).
            hi (double): the upper bound (inclusive).
        
        Raises:
            MathIllegalArgumentException: if value is strictly outside [lo, hi].
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkRangeInclusive(value: int, lo: int, hi: int) -> None: ...
    @typing.overload
    @staticmethod
    def copySign(magnitude: int, sign: int) -> int: ...
    @typing.overload
    @staticmethod
    def copySign(magnitude: int, sign: int) -> int: ...
    @typing.overload
    @staticmethod
    def copySign(magnitude: int, sign: int) -> int: ...
    @typing.overload
    @staticmethod
    def copySign(magnitude: int, sign: int) -> int: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true if the values are equal according to semantics of Double.
        
        Parameters:
            x (double): Value
            y (double): Value
        
        Returns:
            valueOf(y))
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(x: float, y: float) -> bool: ...
    @staticmethod
    def getHipparchusVersion() -> str:
        """
        Get Hipparchus version.
        
        The version is automatically retrieved from a properties file generated at maven compilation time. When using an IDE not configured to use maven, then a default value "unknown" will be returned.
        
        Returns:
            hipparchus version
        
        Since:
            4.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def hash(value: float) -> int:
        """
        Returns an integer hash code representing the given double value.
        
        Parameters:
            value (double): the value to be hashed
        
        Returns:
            the hash code
        
        Returns an integer hash code representing the given double array.
        
        Parameters:
            value (double[]): the value to be hashed (may be null)
        
        Returns:
            the hash code
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def hash(value: typing.Union[typing.List[float], jpype.JArray]) -> int: ...
    _max__T = typing.TypeVar('_max__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def max(e1: _max__T, e2: _max__T) -> _max__T:
        """
        Find the maximum of two field elements.
        
        Parameters:
            e1 (T): first element
            e2 (T): second element
        
        Returns:
            max(a1, e2)
        
        
        """
        ...
    _min__T = typing.TypeVar('_min__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def min(e1: _min__T, e2: _min__T) -> _min__T:
        """
        Find the minimum of two field elements.
        
        Parameters:
            e1 (T): first element
            e2 (T): second element
        
        Returns:
            min(a1, e2)
        
        
        """
        ...
    _normalizeAngle_1__T = typing.TypeVar('_normalizeAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def normalizeAngle(a: float, center: float) -> float:
        """
        Normalize an angle in a 2π wide interval around a center value.
        
        This method has three main uses:
        
          - normalize an angle between 0 and 2π:
        
        
        PI);
          - normalize an angle between -π and +π
        
        
        0);
          - compute the angle between two defining angular positions:
        
        
        normalizeAngle(end, start) - start;
        
        Note that due to numerical accuracy and since π cannot be represented exactly, the result interval is closed, it cannot be half-closed as would be more satisfactory in a purely mathematical view.
        
        Parameters:
            a (double): angle to normalize
            center (double): center of the desired 2π interval for the result
        
        Returns:
            a-2kπ with integer k and center-π <= a-2kπ <= center+π
        
        """
        ...
    @typing.overload
    @staticmethod
    def normalizeAngle(a: _normalizeAngle_1__T, center: _normalizeAngle_1__T) -> _normalizeAngle_1__T:
        """
        Normalize an angle in a 2π wide interval around a center value.
        
        This method has three main uses:
        
          - normalize an angle between 0 and 2π:
        
        
        PI);
          - normalize an angle between -π and +π
        
        
        normalizeAngle(a, zero);
          - compute the angle between two defining angular positions:
        
        
        subtract(start);
        
        Note that due to numerical accuracy and since π cannot be represented exactly, the result interval is closed, it cannot be half-closed as would be more satisfactory in a purely mathematical view.
        
        Parameters:
            a (T): angle to normalize
            center (T): center of the desired 2π interval for the result
        
        Returns:
            a-2kπ with integer k and center-π <= a-2kπ <= center+π
        
        
        """
        ...
    @staticmethod
    def reduce(a: float, period: float, offset: float) -> float:
        """
        Reduce |a - offset| to the primary interval [0, |period|).
        
        Specifically, the value returned is
        
        a - |period| * floor((a - offset) / |period|) - offset.
        
        If any of the parameters are NaN or infinite, the result is NaN.
        
        Parameters:
            a (double): Value to reduce.
            period (double): Period.
            offset (double): Value that will be mapped to .
        
        Returns:
            the value, within the interval [0 |period|), that corresponds to a.
        
        
        """
        ...
    _twoSum_0__T = typing.TypeVar('_twoSum_0__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def twoSum(a: _twoSum_0__T, b: _twoSum_0__T) -> 'MathUtils.FieldSumAndResidual'[_twoSum_0__T]:
        """
        Sums a and b using Møller's 2Sum algorithm.
        
        References:
        
          - Møller, Ole. "Quasi double-precision in floating point addition." BIT 5, 37–50 (1965).
          - Shewchuk, Richard J. "Adaptive Precision Floating-Point Arithmetic and Fast Robust Geometric Predicates." Discrete &
            Computational Geometry 18, 305–363 (1997).
          - 2Sum
        
        
        Parameters:
            a (T): first summand
            b (T): second summand
        
        Returns:
            sum and residual error in the sum
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def twoSum(a: float, b: float) -> 'MathUtils.SumAndResidual':
        """
        Sums a and b using Møller's 2Sum algorithm.
        
        References:
        
          - Møller, Ole. "Quasi double-precision in floating point addition." BIT 5, 37–50 (1965).
          - Shewchuk, Richard J. "Adaptive Precision Floating-Point Arithmetic and Fast Robust Geometric Predicates." Discrete &
            Computational Geometry 18, 305–363 (1997).
          - 2Sum
        
        
        Parameters:
            a (double): first summand
            b (double): second summand
        
        Returns:
            sum and residual error in the sum
        
        """
        ...
    class FieldSumAndResidual(typing.Generic[_MathUtils__FieldSumAndResidual__T]):
        def getResidual(self) -> _MathUtils__FieldSumAndResidual__T: ...
        def getSum(self) -> _MathUtils__FieldSumAndResidual__T: ...
    class SumAndResidual:
        def getResidual(self) -> float: ...
        def getSum(self) -> float: ...

class MultidimensionalCounter(java.lang.Iterable[int]):
    """
    Converter between unidimensional storage structure and multidimensional conceptual structure. This utility will convert from indices in a multidimensional structure to the corresponding index in a one-dimensional array. For example, assuming that the ranges (in 3 dimensions) of indices are 2, 4 and 3, the following correspondences, between 3-tuples indices and unidimensional indices, will hold:
    
      - (0, 0, 0) corresponds to 0
      - (0, 0, 1) corresponds to 1
      - (0, 0, 2) corresponds to 2
      - (0, 1, 0) corresponds to 3
      - ...
      - (1, 0, 0) corresponds to 12
      - ...
      - (1, 3, 2) corresponds to 23
    """
    def __init__(self, *size: int):
        """
        Create a counter.
        
        Parameters:
            size (int...): Counter sizes (number of slots in each dimension).
        
        Raises:
            MathIllegalArgumentException: if one of the sizes is negative or zero.
        
        
        """
        ...
    def getCount(self, *c: int) -> int:
        """
        Convert to unidimensional counter.
        
        Parameters:
            c (int...): Indices in multidimensional counter.
        
        Returns:
            the index within the unidimensionl counter.
        
        Raises:
            MathIllegalArgumentException: if the size of c does not match the size of the array given in the constructor.
            MathIllegalArgumentException: if a value of c is not in the range of the corresponding dimension, as defined in the
                .
        
        
        """
        ...
    def getCounts(self, index: int) -> typing.MutableSequence[int]:
        """
        Convert to multidimensional counter.
        
        Parameters:
            index (int): Index in unidimensional counter.
        
        Returns:
            the multidimensional counts.
        
        Raises:
            MathIllegalArgumentException: if index is not between  and the value returned by
                getSize (excluded).
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the number of dimensions of the multidimensional counter.
        
        Returns:
            the number of dimensions.
        
        
        """
        ...
    def getSize(self) -> int:
        """
        Get the total number of elements.
        
        Returns:
            the total size of the unidimensional counter.
        
        
        """
        ...
    def getSizes(self) -> typing.MutableSequence[int]:
        """
        Get the number of multidimensional counter slots in each dimension.
        
        Returns:
            the sizes of the multidimensional counter in each dimension.
        
        
        """
        ...
    def iterator(self) -> 'MultidimensionalCounter.Iterator':
        """
        Create an iterator over this counter.
        
        Specified by: Iterable in interface Iterable
        
        Returns:
            the iterator.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    class Iterator(java.util.Iterator[int]):
        @typing.overload
        def getCount(self) -> int: ...
        @typing.overload
        def getCount(self, int: int) -> int: ...
        def getCounts(self) -> typing.MutableSequence[int]: ...
        def hasNext(self) -> bool: ...
        def next(self) -> int: ...
        def remove(self) -> None: ...

_Pair__K = typing.TypeVar('_Pair__K')  # <K>
_Pair__V = typing.TypeVar('_Pair__V')  # <V>
class Pair(typing.Generic[_Pair__K, _Pair__V]):
    """
    Generic pair.
    
    Although the instances of this class are immutable, it is impossible to ensure that the references passed to the constructor will not be modified by the caller.
    """
    @typing.overload
    def __init__(self, k: _Pair__K, v: _Pair__V): ...
    @typing.overload
    def __init__(self, entry: 'Pair'[_Pair__K, _Pair__V]): ...
    _create__K = typing.TypeVar('_create__K')  # <K>
    _create__V = typing.TypeVar('_create__V')  # <V>
    @staticmethod
    def create(k: _create__K, v: _create__V) -> 'Pair'[_create__K, _create__V]:
        """
        Convenience factory method that calls the .
        
        Parameters:
            k (K): First element of the pair.
            v (V): Second element of the pair.
        
        Returns:
            a new Pair containing k and v.
        
        
        """
        ...
    def equals(self, o: typing.Any) -> bool:
        """
        Compare the specified object with this entry for equality.
        
        Overrides: Object in class Object
        
        Parameters:
            o (Object): Object.
        
        Returns:
            true if the given object is also a map entry and the two entries represent the same mapping.
        
        
        """
        ...
    def getFirst(self) -> _Pair__K:
        """
        Get the first element of the pair.
        
        Returns:
            the first element of the pair.
        
        
        """
        ...
    def getKey(self) -> _Pair__K:
        """
        Get the key.
        
        Returns:
            the key (first element of the pair).
        
        
        """
        ...
    def getSecond(self) -> _Pair__V:
        """
        Get the second element of the pair.
        
        Returns:
            the second element of the pair.
        
        
        """
        ...
    def getValue(self) -> _Pair__V:
        """
        Get the value.
        
        Returns:
            the value (second element of the pair).
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Compute a hash code.
        
        Overrides: Object in class Object
        
        Returns:
            the hash code value.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class PivotingStrategy(java.lang.Enum['PivotingStrategy']):
    """
    A strategy to pick a pivoting index of an array for doing partitioning.
    """
    CENTRAL: typing.ClassVar['PivotingStrategy'] = ...
    MEDIAN_OF_3: typing.ClassVar['PivotingStrategy'] = ...
    def pivotIndex(self, work: typing.Union[typing.List[float], jpype.JArray], begin: int, end: int) -> int:
        """
        Find pivot index of the array so that partition and K :sup:`th` element selection can be made
        
        Parameters:
            work (double[]): data array
            begin (int): index of the first element of the slice
            end (int): index after the last element of the slice
        
        Returns:
            the index of the pivot element chosen between the first and the last element of the array slice
        
        Raises:
            MathIllegalArgumentException: when indices exceeds range
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'PivotingStrategy':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['PivotingStrategy']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (PivotingStrategy c : PivotingStrategy.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Precision:
    """
    Utilities for comparing numbers.
    """
    EPSILON: typing.ClassVar[float] = ...
    """
    Largest double-precision floating-point number such that 1 + EPSILON is numerically equal to 1. This value is an upper bound on the relative error due to rounding real numbers to double precision floating-point numbers.
    
    In IEEE 754 arithmetic, this is 2 :sup:`-53` .
    
    Also see:
        `Machine epsilon <http://en.wikipedia.org/wiki/Machine_epsilon>`
    
    
    """
    SAFE_MIN: typing.ClassVar[float] = ...
    """
    Safe minimum, such that 1 / SAFE_MIN does not overflow.
    
    In IEEE 754 arithmetic, this is also the smallest normalized number 2 :sup:`-1022` .
    """
    @typing.overload
    @staticmethod
    def compareTo(x: float, y: float, eps: float) -> int:
        """
        Compares two numbers given some amount of allowed error.
        
        Parameters:
            x (double): the first number
            y (double): the second number
            eps (double): the amount of error to allow when checking for equality
        
        Returns:
        
              - 0 if equals
              - < 0 if !equals &&amp; x < y
              - > 0 if !equals &&amp; x > y or either argument is NaN
        
        Compares two numbers given some amount of allowed error. Two float numbers are considered equal if there are (maxUlps - 1) (or fewer) floating point numbers between them, i.e. two adjacent floating point numbers are considered equal. Adapted from ` Bruce Dawson <http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/>`. Returns false if either of the arguments is NaN.
        
        Parameters:
            x (double): first value
            y (double): second value
            maxUlps (int): (maxUlps - 1) is the number of floating point values between x and y.
        
        Returns:
        
              - 0 if equals
              - < 0 if !equals &&amp; x < y
              - > 0 if !equals &&amp; x > y or either argument is NaN
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def compareTo(double: float, double2: float, int: int) -> int: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true iff they are equal as defined by equals.
        
        Parameters:
            x (float): first value
            y (float): second value
        
        Returns:
            true if the values are equal.
        
        Returns true if the arguments are equal or within the range of allowed error (inclusive). Returns false if either of the arguments is NaN.
        
        Parameters:
            x (float): first value
            y (float): second value
            eps (float): the amount of absolute error to allow.
        
        Returns:
            true if the values are equal or within range of each other.
        
        Returns true if the arguments are equal or within the range of allowed error (inclusive). Two float numbers are considered equal if there are (maxUlps - 1) (or fewer) floating point numbers between them, i.e. two adjacent floating point numbers are considered equal. Adapted from ` Bruce Dawson <http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/>`. Returns false if either of the arguments is NaN.
        
        Parameters:
            x (float): first value
            y (float): second value
            maxUlps (int): (maxUlps - 1) is the number of floating point values between x and y.
        
        Returns:
            true if there are fewer than maxUlps floating point values between x and y.
        
        Returns true iff they are equal as defined by equals.
        
        Parameters:
            x (double): first value
            y (double): second value
        
        Returns:
            true if the values are equal.
        
        Returns true if there is no double value strictly between the arguments or the difference between them is within the range of allowed error (inclusive). Returns false if either of the arguments is NaN.
        
        Parameters:
            x (double): First value.
            y (double): Second value.
            eps (double): Amount of allowed absolute error.
        
        Returns:
            true if the values are two adjacent floating point numbers or they are within range of each other.
        
        Returns true if the arguments are equal or within the range of allowed error (inclusive).
        
        Two float numbers are considered equal if there are (maxUlps - 1) (or fewer) floating point numbers between them, i.e. two adjacent floating point numbers are considered equal.
        
        Adapted from ` Bruce Dawson <http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/>`. Returns false if either of the arguments is NaN.
        
        Parameters:
            x (double): first value
            y (double): second value
            maxUlps (int): (maxUlps - 1) is the number of floating point values between x and y.
        
        Returns:
            true if there are fewer than maxUlps floating point values between x and y.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(x: float, y: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float, double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(x: float, y: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(float: float, float2: float, float3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(float: float, float2: float, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(x: float, y: float) -> bool:
        """
        Returns true if both arguments are NaN or they are equal as defined by equals.
        
        Parameters:
            x (float): first value
            y (float): second value
        
        Returns:
            true if the values are equal or both are NaN.
        
        Returns true if the arguments are both NaN, are equal, or are within the range of allowed error (inclusive).
        
        Parameters:
            x (float): first value
            y (float): second value
            eps (float): the amount of absolute error to allow.
        
        Returns:
            true if the values are equal or within range of each other, or both are NaN.
        
        Returns true if the arguments are both NaN or if they are equal as defined by equals.
        
        Parameters:
            x (float): first value
            y (float): second value
            maxUlps (int): (maxUlps - 1) is the number of floating point values between x and y.
        
        Returns:
            true if both arguments are NaN or if there are less than maxUlps floating point values between x
            and y.
        
        Returns true if the arguments are both NaN or they are equal as defined by equals.
        
        Parameters:
            x (double): first value
            y (double): second value
        
        Returns:
            true if the values are equal or both are NaN.
        
        Returns true if the arguments are both NaN, are equal or are within the range of allowed error (inclusive).
        
        Parameters:
            x (double): first value
            y (double): second value
            eps (double): the amount of absolute error to allow.
        
        Returns:
            true if the values are equal or within range of each other, or both are NaN.
        
        Returns true if both arguments are NaN or if they are equal as defined by equals.
        
        Parameters:
            x (double): first value
            y (double): second value
            maxUlps (int): (maxUlps - 1) is the number of floating point values between x and y.
        
        Returns:
            true if both arguments are NaN or if there are less than maxUlps floating point values between x
            and y.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(double: float, double2: float, double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(double: float, double2: float, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(x: float, y: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(float: float, float2: float, float3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(float: float, float2: float, int: int) -> bool: ...
    @staticmethod
    def equalsWithRelativeTolerance(x: float, y: float, eps: float) -> bool:
        """
        Returns true if there is no double value strictly between the arguments or the relative difference between them is less than or equal to the given tolerance. Returns false if either of the arguments is NaN.
        
        Parameters:
            x (double): First value.
            y (double): Second value.
            eps (double): Amount of allowed relative error.
        
        Returns:
            true if the values are two adjacent floating point numbers or they are within range of each other.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isMathematicalInteger(x: float) -> bool:
        """
        Check is x is a mathematical integer.
        
        Parameters:
            x (double): number to check
        
        Returns:
            true if x is a mathematical integer
        
        Since:
            1.7
        
        Check is x is a mathematical integer.
        
        Parameters:
            x (float): number to check
        
        Returns:
            true if x is a mathematical integer
        
        Since:
            1.7
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isMathematicalInteger(x: float) -> bool: ...
    @staticmethod
    def representableDelta(x: float, originalDelta: float) -> float:
        """
        Computes a number delta close to originalDelta with the property that
        
           x + delta - x is exactly machine-representable. This is useful when computing numerical derivatives, in order to reduce roundoff errors.
        
        Parameters:
            x (double): Value.
            originalDelta (double): Offset value.
        
        Returns:
            a number delta so that x + delta and x differ by a representable floating number.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def round(x: float, scale: int) -> float:
        """
        Rounds the given value to the specified number of decimal places. The value is rounded using the BigDecimal method.
        
        Parameters:
            x (double): Value to round.
            scale (int): Number of digits to the right of the decimal point.
        
        Returns:
            the rounded value.
        
        Rounds the given value to the specified number of decimal places. The value is rounded using the given method which is any method defined in BigDecimal. If x is infinite or NaN, then the value of x is returned unchanged, regardless of the other parameters.
        
        Parameters:
            x (double): Value to round.
            scale (int): Number of digits to the right of the decimal point.
            roundingMethod (RoundingMode): Rounding method as defined in
                BigDecimal.
        
        Returns:
            the rounded value.
        
        Raises:
            ArithmeticException: if roundingMethod == ROUND_UNNECESSARY and the specified scaling operation would require rounding.
            IllegalArgumentException: if roundingMethod does not represent a valid rounding mode.
        
        Rounds the given value to the specified number of decimal places. The value is rounded using the BigDecimal method.
        
        Parameters:
            x (float): Value to round.
            scale (int): Number of digits to the right of the decimal point.
        
        Returns:
            the rounded value.
        
        public static float round (float x, int scale, RoundingMode roundingMethod) throws MathRuntimeException, MathIllegalArgumentException
        
        Rounds the given value to the specified number of decimal places. The value is rounded using the given method which is any method defined in BigDecimal.
        
        Parameters:
            x (float): Value to round.
            scale (int): Number of digits to the right of the decimal point.
            roundingMethod (RoundingMode): Rounding method as defined in
                BigDecimal.
        
        Returns:
            the rounded value.
        
        Raises:
            MathRuntimeException: if an exact operation is required but result is not exact
            MathIllegalArgumentException: if roundingMethod is not a valid rounding method.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def round(x: float, scale: int, roundingMethod: java.math.RoundingMode) -> float: ...
    @typing.overload
    @staticmethod
    def round(x: float, scale: int) -> float: ...
    @typing.overload
    @staticmethod
    def round(x: float, scale: int, roundingMethod: java.math.RoundingMode) -> float: ...

class ResizableDoubleArray(java.io.Serializable):
    """
    A variable length primitive double array implementation that automatically handles expanding and contracting its internal storage array as elements are added and removed.
    
    The internal storage array starts with capacity determined by the initialCapacity property, which can be set by the constructor. The default initial capacity is 16. Adding elements using addElement appends elements to the end of the array. When there are no open entries at the end of the internal storage array, the array is expanded. The size of the expanded array depends on the expansionMode and expansionFactor properties. The expansionMode determines whether the size of the array is multiplied by the expansionFactor (MULTIPLICATIVE) or if the expansion is additive (ADDITIVE -- expansionFactor storage locations added). The default expansionMode is MULTIPLICATIVE and the default expansionFactor is 2.
    
    The addElementRolling method adds a new element to the end of the internal storage array and adjusts the "usable window" of the internal array forward by one position (effectively making what was the second element the first, and so on). Repeated activations of this method (or activation of discardFrontElements) will effectively orphan the storage locations at the beginning of the internal storage array. To reclaim this storage, each time one of these methods is activated, the size of the internal storage array is compared to the number of addressable elements (the numElements property) and if the difference is too large, the internal array is contracted to size numElements + 1. The determination of when the internal storage array is "too large" depends on the expansionMode and contractionFactor properties. If the expansionMode is MULTIPLICATIVE, contraction is triggered when the ratio between storage array length and numElements exceeds contractionFactor If the expansionMode is ADDITIVE, the number of excess storage locations is compared to contractionFactor.
    
    To avoid cycles of expansions and contractions, the expansionFactor must not exceed the contractionFactor. Constructors and mutators for both of these properties enforce this requirement, throwing a MathIllegalArgumentException if it is violated.
    
    Note: this class is NOT thread-safe.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, initialCapacity: int, expansionFactor: float): ...
    @typing.overload
    def __init__(self, initialCapacity: int, expansionFactor: float, contractionCriterion: float): ...
    @typing.overload
    def __init__(self, initialCapacity: int, expansionFactor: float, contractionCriterion: float, expansionMode: 'ResizableDoubleArray.ExpansionMode', *data: float): ...
    @typing.overload
    def __init__(self, resizableDoubleArray: 'ResizableDoubleArray'): ...
    def addElement(self, value: float) -> None:
        """
        Adds an element to the end of this expandable array.
        
        Parameters:
            value (double): Value to be added to end of array.
        
        
        """
        ...
    def addElementRolling(self, value: float) -> float:
        """
        Adds an element to the end of the array and removes the first element in the array. Returns the discarded first element.
        
        The effect is similar to a push operation in a FIFO queue.
        
        Example: If the array contains the elements 1, 2, 3, 4 (in that order) and addElementRolling(5) is invoked, the result is an array containing the entries 2, 3, 4, 5 and the value returned is 1.
        
        Parameters:
            value (double): Value to be added to the array.
        
        Returns:
            the value which has been discarded or "pushed" out of the array by this rolling insert.
        
        
        """
        ...
    def addElements(self, values: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Adds several element to the end of this expandable array.
        
        Parameters:
            values (double[]): Values to be added to end of array.
        
        
        """
        ...
    def clear(self) -> None:
        """
        Clear the array contents, resetting the number of elements to zero.
        """
        ...
    def compute(self, f: MathArrays.Function) -> float:
        """
        Performs an operation on the addressable elements of the array.
        
        Parameters:
            f (Function): Function to be applied on this array.
        
        Returns:
            the result.
        
        
        """
        ...
    def contract(self) -> None:
        """
        Contracts the storage array to the (size of the element set) + 1 - to avoid a zero length array. This function also resets the startIndex to zero.
        """
        ...
    def copy(self) -> 'ResizableDoubleArray':
        """
        Returns a copy of the ResizableDoubleArray. Does not contract before the copy, so the returned object is an exact copy of this.
        
        Returns:
            a new ResizableDoubleArray with the same data and configuration properties as this
        
        
        """
        ...
    def discardFrontElements(self, i: int) -> None:
        """
        Discards the i initial elements of the array.
        
        For example, if the array contains the elements 1,2,3,4, invoking discardFrontElements(2) will cause the first two elements to be discarded, leaving 3,4 in the array.
        
        Parameters:
            i (int): the number of elements to discard from the front of the array
        
        Raises:
            MathIllegalArgumentException: if i is greater than numElements.
        
        
        """
        ...
    def discardMostRecentElements(self, i: int) -> None:
        """
        Discards the i last elements of the array.
        
        For example, if the array contains the elements 1,2,3,4, invoking discardMostRecentElements(2) will cause the last two elements to be discarded, leaving 1,2 in the array.
        
        Parameters:
            i (int): the number of elements to discard from the end of the array
        
        Raises:
            MathIllegalArgumentException: if i is greater than numElements.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true iff object is a ResizableDoubleArray with the same properties as this and an identical internal storage array.
        
        Overrides: Object in class Object
        
        Parameters:
            object (Object): object to be compared for equality with this
        
        Returns:
            true iff object is a ResizableDoubleArray with the same data and properties as this
        
        
        """
        ...
    def getCapacity(self) -> int:
        """
        Gets the currently allocated size of the internal data structure used for storing elements. This is not to be confused with getNumElements.
        
        Returns:
            the length of the internal array.
        
        
        """
        ...
    def getContractionCriterion(self) -> float:
        """
        The contraction criterion defines when the internal array will contract to store only the number of elements in the element array.
        
        If the expansionMode is MULTIPLICATIVE, contraction is triggered when the ratio between storage array length and numElements exceeds contractionFactor. If the expansionMode is ADDITIVE, the number of excess storage locations is compared to contractionFactor.
        
        Returns:
            the contraction criterion used to reclaim memory.
        
        
        """
        ...
    def getElement(self, index: int) -> float:
        """
        Returns the element at the specified index.
        
        Parameters:
            index (int): index to fetch a value from
        
        Returns:
            value stored at the specified index
        
        Raises:
            ArrayIndexOutOfBoundsException: if index is less than zero or is greater than getNumElements() - 1.
        
        
        """
        ...
    def getElements(self) -> typing.MutableSequence[float]:
        """
        Returns a double array containing the elements of this ResizableArray.
        
        This method returns a copy, not a reference to the underlying array, so that changes made to the returned array have no effect on this ResizableArray.
        
        Returns:
            the double array.
        
        
        """
        ...
    def getExpansionFactor(self) -> float:
        """
        The expansion factor controls the size of a new array when an array needs to be expanded.
        
        The expansionMode determines whether the size of the array is multiplied by the expansionFactor (MULTIPLICATIVE) or if the expansion is additive (ADDITIVE -- expansionFactor storage locations added). The default expansionMode is MULTIPLICATIVE and the default expansionFactor is 2.0.
        
        Returns:
            the expansion factor of this expandable double array
        
        
        """
        ...
    def getExpansionMode(self) -> 'ResizableDoubleArray.ExpansionMode':
        """
        The expansion mode determines whether the internal storage array grows additively or multiplicatively when it is expanded.
        
        Returns:
            the expansion mode.
        
        
        """
        ...
    def getNumElements(self) -> int:
        """
        Returns the number of elements currently in the array. Please note that this is different from the length of the internal storage array.
        
        Returns:
            the number of elements.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Returns a hash code consistent with equals.
        
        Overrides: Object in class Object
        
        Returns:
            the hash code representing this ResizableDoubleArray.
        
        
        """
        ...
    def setElement(self, index: int, value: float) -> None:
        """
        Sets the element at the specified index.
        
        If the specified index is greater than getNumElements() - 1, the numElements property is increased to index +1 and additional storage is allocated (if necessary) for the new element and all (uninitialized) elements between the new element and the previous end of the array).
        
        Parameters:
            index (int): index to store a value in
            value (double): value to store at the specified index
        
        Raises:
            ArrayIndexOutOfBoundsException: if index < 0.
        
        
        """
        ...
    def setNumElements(self, i: int) -> None:
        """
        This function allows you to control the number of elements contained in this array, and can be used to "throw out" the last n values in an array. This function will also expand the internal array as needed.
        
        Parameters:
            i (int): a new number of elements
        
        Raises:
            MathIllegalArgumentException: if i is negative.
        
        
        """
        ...
    def substituteMostRecentElement(self, value: float) -> float:
        """
        Substitutes value for the most recently added value.
        
        Returns the value that has been replaced. If the array is empty (i.e. if numElements is zero), an MathIllegalStateException is thrown.
        
        Parameters:
            value (double): New value to substitute for the most recently added value
        
        Returns:
            the value that has been replaced in the array.
        
        Raises:
            MathIllegalStateException: if the array is empty
        
        
        """
        ...
    class ExpansionMode(java.lang.Enum['ResizableDoubleArray.ExpansionMode']):
        MULTIPLICATIVE: typing.ClassVar['ResizableDoubleArray.ExpansionMode'] = ...
        ADDITIVE: typing.ClassVar['ResizableDoubleArray.ExpansionMode'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ResizableDoubleArray.ExpansionMode': ...
        @staticmethod
        def values() -> typing.MutableSequence['ResizableDoubleArray.ExpansionMode']: ...

class RosenNumberPartitionIterator(java.util.Iterator[typing.MutableSequence[int]]):
    """
    An iterator that generates all partitions of n elements, into k parts containing the number of elements in each part, based on Rosen's algorithm.
    
    This is a copy of the class (with slight edits) with the same name from the symja_android_library. The original file was published under the terms of the GPLV3 license, but the Hipparchus project was Hipparchus to include it relicensed to Apache V2.
    
    See Kenneth H. Rosen, Discrete Mathematics and Its Applications, 2nd edition (NY: McGraw-Hill, 1991), pp. 284-286
    """
    def __init__(self, n: int, k: int):
        """
        Simple constructor.
        
        Parameters:
            n (int): the number of elements
            k (int): divided into k parts
        
        
        """
        ...
    def hasNext(self) -> bool:
        """
        Specified by: Iterator in interface Iterator
        
        Also see:
            Iterator
        
        
        """
        ...
    def next(self) -> typing.MutableSequence[int]:
        """
        Specified by: Iterator in interface Iterator
        
        Also see:
            Iterator
        
        
        """
        ...
    def reset(self) -> None:
        """
        Reset this iterator to the start condition.
        """
        ...

class RyuDouble:
    """
    An implementation of Ryū for double.
    
    Ryū generates the shortest decimal representation of a floating point number that maintains round-trip safety. That is, a correct parser can recover the exact original number. Ryū is very fast (about 10 time faster than toString()).
    
    Also see:
        cfm
    """
    DEFAULT_LOW_EXP: typing.ClassVar[int] = ...
    """
    Default low switch level to scientific notation.
    
    Also see:
        constant
    
    
    """
    DEFAULT_HIGH_EXP: typing.ClassVar[int] = ...
    """
    Default high switch level to scientific notation.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    @staticmethod
    def doubleToString(value: float) -> str:
        """
        Convert a double to shortest string representation, preserving full accuracy.
        
        This implementation uses the same specifications as toString(), i.e. it uses scientific notation if for numbers smaller than 10⁻³ or larger than 10⁺⁷, and decimal notion in between. That is it call doubleToString.
        
        Parameters:
            value (double): double number to convert
        
        Returns:
            shortest string representation
        
        Also see:
            doubleToString, DEFAULT_LOW_EXP,
            DEFAULT_HIGH_EXP
        
        Convert a double to shortest string representation, preserving full accuracy.
        
        Number inside of the interval [10 :sup:`lowExp` , 10 :sup:`highExp` ] are represented using decimal notation, numbers outside of this range are represented using scientific notation.
        
        Parameters:
            value (double): double number to convert
            lowExp (int): lowest decimal exponent for which decimal notation can be used
            highExp (int): highest decimal exponent for which decimal notation can be used
        
        Returns:
            shortest string representation
        
        Also see:
            doubleToString, DEFAULT_LOW_EXP,
            DEFAULT_HIGH_EXP
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def doubleToString(value: float, lowExp: int, highExp: int) -> str: ...

class SinCos:
    """
    Holder for both sine and cosine values.
    
    This class is a simple container, it does not provide any computational method.
    
    Since:
        1.3
    
    Also see:
        sinCos
    """
    def cos(self) -> float:
        """
        Get the value of the cosine.
        
        Returns:
            value of the cosine
        
        
        """
        ...
    @staticmethod
    def difference(scAlpha: 'SinCos', scBeta: 'SinCos') -> 'SinCos':
        """
        Compute sine and cosine of angles difference.
        
        Parameters:
            scAlpha (SinCos): \((\sin \alpha, \cos \alpha)\)
            scBeta (SinCos): \((\sin \beta, \cos \beta)\)
        
        Returns:
            \((\sin \alpha+\beta, \cos \alpha-\beta)\)
        
        Since:
            1.8
        
        
        """
        ...
    def sin(self) -> float:
        """
        Get the value of the sine.
        
        Returns:
            value of the sine
        
        
        """
        ...
    @staticmethod
    def sum(scAlpha: 'SinCos', scBeta: 'SinCos') -> 'SinCos':
        """
        Compute sine and cosine of angles sum.
        
        Parameters:
            scAlpha (SinCos): \((\sin \alpha, \cos \alpha)\)
            scBeta (SinCos): \((\sin \beta, \cos \beta)\)
        
        Returns:
            \((\sin \alpha+\beta, \cos \alpha+\beta)\)
        
        Since:
            1.8
        
        
        """
        ...

class SinhCosh:
    """
    Holder for both hyperbolic sine and hyperbolic cosine values.
    
    This class is a simple container, it does not provide any computational method.
    
    Since:
        2.0
    
    Also see:
        sinhCosh
    """
    def cosh(self) -> float:
        """
        Get the value of the hyperbolic cosine.
        
        Returns:
            value of the hyperbolic cosine
        
        
        """
        ...
    @staticmethod
    def difference(schAlpha: 'SinhCosh', schBeta: 'SinhCosh') -> 'SinhCosh':
        """
        Compute hyperbolic sine and hyperbolic cosine of angles difference.
        
        Parameters:
            schAlpha (SinhCosh): \((\sinh \alpha, \cosh \alpha)\)
            schBeta (SinhCosh): \((\sinh \beta, \cosh \beta)\)
        
        Returns:
            \((\sinh \alpha+\beta, \cosh \alpha-\beta)\)
        
        
        """
        ...
    def sinh(self) -> float:
        """
        Get the value of the hyperbolic sine.
        
        Returns:
            value of the hyperbolic sine
        
        
        """
        ...
    @staticmethod
    def sum(schAlpha: 'SinhCosh', schBeta: 'SinhCosh') -> 'SinhCosh':
        """
        Compute hyperbolic sine and hyperbolic cosine of angles sum.
        
        Parameters:
            schAlpha (SinhCosh): \((\sinh \alpha, \cosh \alpha)\)
            schBeta (SinhCosh): \((\sinh \beta, \cosh \beta)\)
        
        Returns:
            \((\sinh \alpha+\beta, \cosh \alpha+\beta)\)
        
        
        """
        ...

class Tuple(org.hipparchus.CalculusFieldElement['Tuple']):
    """
    This class allows to perform the same computation of all components of a Tuple at once.
    
    Since:
        1.2
    """
    def __init__(self, *x: float):
        """
        Creates a new instance from its components.
        
        Parameters:
            x (double...): components of the tuple
        
        
        """
        ...
    def abs(self) -> 'Tuple':
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    def acos(self) -> 'Tuple':
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> 'Tuple':
        """
        Inverse hyperbolic cosine operation.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> 'Tuple':
        """
        Compute this + a.
        
        Specified by: add in interface FieldElement
        
        Parameters:
            a (Tuple): element to add
        
        Returns:
            a new element representing this + a
        
        '+' operator.
        
        Specified by: add in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this+a
        
        
        """
        ...
    @typing.overload
    def add(self, a: 'Tuple') -> 'Tuple': ...
    def asin(self) -> 'Tuple':
        """
        Arc sine operation.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> 'Tuple':
        """
        Inverse hyperbolic sine operation.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'Tuple':
        """
        Arc tangent operation.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            atan(this)
        
        
        """
        ...
    def atan2(self, x: 'Tuple') -> 'Tuple':
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (Tuple): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def atanh(self) -> 'Tuple':
        """
        Inverse hyperbolic tangent operation.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'Tuple':
        """
        Cubic root.
        
        Specified by: cbrt in interface CalculusFieldElement
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'Tuple':
        """
        Get the smallest whole number larger than instance.
        
        Specified by: ceil in interface CalculusFieldElement
        
        Returns:
            ceil(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'Tuple':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (Tuple): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: 'Tuple') -> 'Tuple': ...
    def cos(self) -> 'Tuple':
        """
        Cosine operation.
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> 'Tuple':
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Returns:
            cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'Tuple':
        """
        Compute this ÷ a.
        
        Specified by: divide in interface CalculusFieldElement
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            a (Tuple): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        '÷' operator.
        
        Specified by: divide in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this÷a
        
        
        """
        ...
    @typing.overload
    def divide(self, a: 'Tuple') -> 'Tuple': ...
    def equals(self, obj: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def exp(self) -> 'Tuple':
        """
        Exponential.
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'Tuple':
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'Tuple':
        """
        Get the largest whole number smaller than instance.
        
        Specified by: floor in interface CalculusFieldElement
        
        Returns:
            floor(this)
        
        
        """
        ...
    def getAddendum(self) -> 'Tuple':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getComponent(self, index: int) -> float:
        """
        Get one component of the tuple.
        
        Parameters:
            index (int): index of the component, between 0 and getDimension - 1
        
        Returns:
            value of the component
        
        
        """
        ...
    def getComponents(self) -> typing.MutableSequence[float]:
        """
        Get all components of the tuple.
        
        Returns:
            all components
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the tuple.
        
        Returns:
            dimension of the tuple
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['Tuple']:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getPi(self) -> 'Tuple':
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
        Get the real value of the number.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def hypot(self, y: 'Tuple') -> 'Tuple':
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (Tuple): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Tuple', a2: float, b2: 'Tuple') -> 'Tuple':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Tuple): first factor of the first term
            b1 (Tuple): second factor of the first term
            a2 (Tuple): first factor of the second term
            b2 (Tuple): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Tuple): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Tuple): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Tuple): first factor of the first term
            b1 (Tuple): second factor of the first term
            a2 (Tuple): first factor of the second term
            b2 (Tuple): second factor of the second term
            a3 (Tuple): first factor of the third term
            b3 (Tuple): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Tuple): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Tuple): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Tuple): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Tuple): first factor of the first term
            b1 (Tuple): second factor of the first term
            a2 (Tuple): first factor of the second term
            b2 (Tuple): second factor of the second term
            a3 (Tuple): first factor of the third term
            b3 (Tuple): second factor of the third term
            a4 (Tuple): first factor of the fourth term
            b4 (Tuple): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Tuple): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Tuple): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Tuple): second factor of the third term
            a4 (double): first factor of the fourth term
            b4 (Tuple): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Tuple', a2: float, b2: 'Tuple', a3: float, b3: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Tuple', a2: float, b2: 'Tuple', a3: float, b3: 'Tuple', a4: float, b4: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['Tuple'], jpype.JArray]) -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, a1: 'Tuple', b1: 'Tuple', a2: 'Tuple', b2: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, a1: 'Tuple', b1: 'Tuple', a2: 'Tuple', b2: 'Tuple', a3: 'Tuple', b3: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, a1: 'Tuple', b1: 'Tuple', a2: 'Tuple', b2: 'Tuple', a3: 'Tuple', b3: 'Tuple', a4: 'Tuple', b4: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['Tuple'], jpype.JArray], b: typing.Union[typing.List['Tuple'], jpype.JArray]) -> 'Tuple': ...
    def log(self) -> 'Tuple':
        """
        Natural logarithm.
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'Tuple':
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'Tuple':
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, a: float) -> 'Tuple':
        """
        Compute this × a.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            a (Tuple): element to multiply
        
        Returns:
            a new element representing this × a
        
        Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} = \sum_{i=1}^n \mathrm{this} \]
        
        Specified by: multiply in interface CalculusFieldElement
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            n (int): Number of times this must be added to itself.
        
        Returns:
            A new element representing n × this.
        
        '×' operator.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this×a
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'Tuple': ...
    @typing.overload
    def multiply(self, tuple: 'Tuple') -> 'Tuple': ...
    def negate(self) -> 'Tuple':
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, value: float) -> 'Tuple':
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            value (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, p: float) -> 'Tuple':
        """
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            e (Tuple): exponent
        
        Returns:
            this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'Tuple': ...
    @typing.overload
    def pow(self, tuple: 'Tuple') -> 'Tuple': ...
    def reciprocal(self) -> 'Tuple':
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> 'Tuple':
        """
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (Tuple): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: 'Tuple') -> 'Tuple': ...
    def rint(self) -> 'Tuple':
        """
        Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
        Specified by: rint in interface CalculusFieldElement
        
        Returns:
            a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, n: int) -> 'Tuple':
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'Tuple':
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> 'Tuple':
        """
        Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
        Specified by: sign in interface CalculusFieldElement
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'Tuple':
        """
        Sine operation.
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> FieldSinCos['Tuple']:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'Tuple':
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> FieldSinhCosh['Tuple']:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'Tuple':
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> 'Tuple':
        """
        Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> 'Tuple':
        """
        Compute this - a.
        
        Specified by: subtract in interface CalculusFieldElement
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            a (Tuple): element to subtract
        
        Returns:
            a new element representing this - a
        
        '-' operator.
        
        Specified by: subtract in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this-a
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: 'Tuple') -> 'Tuple': ...
    def tan(self) -> 'Tuple':
        """
        Tangent operation.
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> 'Tuple':
        """
        Hyperbolic tangent operation.
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> 'Tuple':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'Tuple':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def ulp(self) -> 'Tuple':
        """
        Compute least significant bit (Unit in Last Position) for a number.
        
        Specified by: ulp in interface CalculusFieldElement
        
        Returns:
            ulp(this)
        
        
        """
        ...

class UnscentedTransformProvider:
    """
    Provider for unscented transform.
    
    Since:
        2.2
    """
    def getUnscentedCovariance(self, sigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray], meanState: org.hipparchus.linear.RealVector) -> org.hipparchus.linear.RealMatrix:
        """
        Computes the unscented covariance matrix from a weighted mean state and a set of sigma points.
        
        This method can be used for computing both the predicted state covariance matrix and the innovation covariance matrix in an Unscented Kalman filter.
        
        It corresponds to Equation 18 of "Wan, E. A., & Van Der Merwe, R. The unscented Kalman filter for nonlinear estimation"
        
        Parameters:
            sigmaPoints (RealVector[]): input sigma points
            meanState (RealVector): weighted mean state
        
        Returns:
            the unscented covariance matrix
        
        
        """
        ...
    def getUnscentedMeanState(self, sigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray]) -> org.hipparchus.linear.RealVector:
        """
        Computes a weighted mean state from a given set of sigma points.
        
        This method can be used for computing both the mean state and the mean measurement in an Unscented Kalman filter.
        
        It corresponds to Equation 17 of "Wan, E. A., & Van Der Merwe, R. The unscented Kalman filter for nonlinear estimation"
        
        Parameters:
            sigmaPoints (RealVector[]): input samples
        
        Returns:
            weighted mean state
        
        
        """
        ...
    def getWc(self) -> org.hipparchus.linear.RealVector:
        """
        Get the covariance weights.
        
        Returns:
            the covariance weights
        
        
        """
        ...
    def getWm(self) -> org.hipparchus.linear.RealVector:
        """
        Get the mean weights.
        
        Returns:
            the mean weights
        
        
        """
        ...
    def inverseUnscentedTransform(self, sigmaPoints: typing.Union[typing.List[org.hipparchus.linear.RealVector], jpype.JArray]) -> Pair[org.hipparchus.linear.RealVector, org.hipparchus.linear.RealMatrix]:
        """
        Perform the inverse unscented transform from an array of sigma points.
        
        Parameters:
            sigmaPoints (RealVector[]): array containing the sigma points of the unscented transform
        
        Returns:
            mean state and associated covariance
        
        
        """
        ...
    def unscentedTransform(self, state: org.hipparchus.linear.RealVector, covariance: org.hipparchus.linear.RealMatrix) -> typing.MutableSequence[org.hipparchus.linear.RealVector]:
        """
        Perform the unscented transform from a state and its covariance.
        
        Parameters:
            state (RealVector): process state
            covariance (RealMatrix): covariance associated with the process state
        
        Returns:
            an array containing the sigma points of the unscented transform
        
        
        """
        ...

class AbstractUnscentedTransform(UnscentedTransformProvider):
    """
    Base class for unscented transform providers.
    
    Since:
        2.2
    """
    def unscentedTransform(self, state: org.hipparchus.linear.RealVector, covariance: org.hipparchus.linear.RealMatrix) -> typing.MutableSequence[org.hipparchus.linear.RealVector]:
        """
        Perform the unscented transform from a state and its covariance.
        
        Let n be the state dimension and Si be the ith row of the covariance matrix square root. The returned array is organized as follow. Element 0 contains the process state, also called the mean state. Elements from 1 to n contain the process state + Si. Finally, elements from n + 1 to 2n contain the process state - Si
        
        Specified by: unscentedTransform in interface UnscentedTransformProvider
        
        Parameters:
            state (RealVector): process state
            covariance (RealMatrix): covariance associated with the process state
        
        Returns:
            an array containing the sigma points of the unscented transform
        
        
        """
        ...

class JulierUnscentedTransform(AbstractUnscentedTransform):
    """
    Unscented transform as defined by Julier and Uhlmann.
    
    The unscented transform uses three parameters: alpha, beta and kappa. Alpha determines the spread of the sigma points around the process state, kappa is a secondary scaling parameter, and beta is used to incorporate prior knowledge of the distribution of the process state.
    
    The Julier transform is a particular case of MerweUnscentedTransform with alpha = 1 and beta = 0.
    
    Since:
        2.2
    
    Also see:
        "S. J. Julier and J. K. Uhlmann. A New Extension of the Kalman Filter to Nonlinear Systems. Proc. SPIE 3068, Signal
        Processing, Sensor Fusion, and Target Recognition VI, 182 (July 28, 1997)"
    """
    DEFAULT_KAPPA: typing.ClassVar[float] = ...
    """
    Default value for kappa, (0.0, see reference).
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, stateDim: int): ...
    @typing.overload
    def __init__(self, stateDim: int, kappa: float): ...
    def getWc(self) -> org.hipparchus.linear.RealVector:
        """
        Get the covariance weights.
        
        Returns:
            the covariance weights
        
        
        """
        ...
    def getWm(self) -> org.hipparchus.linear.RealVector:
        """
        Get the mean weights.
        
        Returns:
            the mean weights
        
        
        """
        ...

class MerweUnscentedTransform(AbstractUnscentedTransform):
    """
    Unscented transform as defined by Merwe and Wan.
    
    The unscented transform uses three parameters: alpha, beta and kappa. Alpha determines the spread of the sigma points around the process state, kappa is a secondary scaling parameter, and beta is used to incorporate prior knowledge of the distribution of the process state.
    
    Since:
        2.2
    
    Also see:
        "E. A. Wan and R. Van der Merwe, The unscented Kalman filter for nonlinear estimation, in Proc. Symp. Adaptive Syst.
        Signal Process., Commun. Contr., Lake Louise, AB, Canada, Oct. 2000."
    """
    DEFAULT_ALPHA: typing.ClassVar[float] = ...
    """
    Default value for alpha (0.5, see reference).
    
    Also see:
        constant
    
    
    """
    DEFAULT_BETA: typing.ClassVar[float] = ...
    """
    Default value for beta (2.0, see reference).
    
    Also see:
        constant
    
    
    """
    DEFAULT_KAPPA: typing.ClassVar[float] = ...
    """
    Default value for kappa, (0.0, see reference).
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, stateDim: int): ...
    @typing.overload
    def __init__(self, stateDim: int, alpha: float, beta: float, kappa: float): ...
    def getWc(self) -> org.hipparchus.linear.RealVector:
        """
        Get the covariance weights.
        
        Returns:
            the covariance weights
        
        
        """
        ...
    def getWm(self) -> org.hipparchus.linear.RealVector:
        """
        Get the mean weights.
        
        Returns:
            the mean weights
        
        
        """
        ...

class OpenIntToDoubleHashMap(AbstractOpenIntHashMap, java.io.Serializable):
    """
    Open addressed map from int to double.
    
    This class provides a dedicated map from integers to doubles with a much smaller memory overhead than standard Map.
    
    This class is not synchronized. The specialized iterators returned by iterator are fail-fast: they throw a ConcurrentModificationException when they detect the map has been modified during iteration.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, expectedSize: int, missingEntries: float): ...
    @typing.overload
    def __init__(self, openIntToDoubleHashMap: 'OpenIntToDoubleHashMap'): ...
    def equals(self, o: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def get(self, key: int) -> float:
        """
        Get the stored value associated with the given key
        
        Parameters:
            key (int): key associated with the data
        
        Returns:
            data associated with the key
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def iterator(self) -> 'OpenIntToDoubleHashMap.Iterator':
        """
        Get an iterator over map elements.
        
        The specialized iterators returned are fail-fast: they throw a ConcurrentModificationException when they detect the map has been modified during iteration.
        
        Returns:
            iterator over the map elements
        
        
        """
        ...
    def put(self, key: int, value: float) -> float:
        """
        Put a value associated with a key in the map.
        
        Parameters:
            key (int): key to which value is associated
            value (double): value to put in the map
        
        Returns:
            previous value associated with the key
        
        
        """
        ...
    def remove(self, key: int) -> float:
        """
        Remove the value associated with a key.
        
        Parameters:
            key (int): key to which the value is associated
        
        Returns:
            removed value
        
        
        """
        ...
    class Iterator(org.hipparchus.util.AbstractOpenIntHashMap.BaseIterator):
        def __init__(self, openIntToDoubleHashMap: 'OpenIntToDoubleHashMap'): ...
        def value(self) -> float: ...

_OpenIntToFieldHashMap__T = typing.TypeVar('_OpenIntToFieldHashMap__T', bound=org.hipparchus.FieldElement)  # <T>
class OpenIntToFieldHashMap(AbstractOpenIntHashMap, java.io.Serializable, typing.Generic[_OpenIntToFieldHashMap__T]):
    """
    Open addressed map from int to FieldElement.
    
    This class provides a dedicated map from integers to FieldElements with a much smaller memory overhead than standard Map.
    
    This class is not synchronized. The specialized iterators returned by iterator are fail-fast: they throw a ConcurrentModificationException when they detect the map has been modified during iteration.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T], expectedSize: int, missingEntries: _OpenIntToFieldHashMap__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T], t: _OpenIntToFieldHashMap__T): ...
    @typing.overload
    def __init__(self, openIntToFieldHashMap: 'OpenIntToFieldHashMap'[_OpenIntToFieldHashMap__T]): ...
    def equals(self, o: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def get(self, key: int) -> _OpenIntToFieldHashMap__T:
        """
        Get the stored value associated with the given key
        
        Parameters:
            key (int): key associated with the data
        
        Returns:
            data associated with the key
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def iterator(self) -> 'OpenIntToFieldHashMap.Iterator':
        """
        Get an iterator over map elements.
        
        The specialized iterators returned are fail-fast: they throw a ConcurrentModificationException when they detect the map has been modified during iteration.
        
        Returns:
            iterator over the map elements
        
        
        """
        ...
    def put(self, key: int, value: _OpenIntToFieldHashMap__T) -> _OpenIntToFieldHashMap__T:
        """
        Put a value associated with a key in the map.
        
        Parameters:
            key (int): key to which value is associated
            value (OpenIntToFieldHashMap): value to put in the map
        
        Returns:
            previous value associated with the key
        
        
        """
        ...
    def remove(self, key: int) -> _OpenIntToFieldHashMap__T:
        """
        Remove the value associated with a key.
        
        Parameters:
            key (int): key to which the value is associated
        
        Returns:
            removed value
        
        
        """
        ...
    class Iterator(org.hipparchus.util.AbstractOpenIntHashMap.BaseIterator):
        def __init__(self, openIntToFieldHashMap: 'OpenIntToFieldHashMap'): ...
        def value(self) -> _OpenIntToFieldHashMap__T: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.util")``.

    AbstractOpenIntHashMap: typing.Type[AbstractOpenIntHashMap]
    AbstractUnscentedTransform: typing.Type[AbstractUnscentedTransform]
    ArithmeticUtils: typing.Type[ArithmeticUtils]
    BigReal: typing.Type[BigReal]
    BigRealField: typing.Type[BigRealField]
    Binary64: typing.Type[Binary64]
    Binary64Field: typing.Type[Binary64Field]
    Blendable: typing.Type[Blendable]
    Combinations: typing.Type[Combinations]
    CombinatoricsUtils: typing.Type[CombinatoricsUtils]
    CompositeFormat: typing.Type[CompositeFormat]
    ContinuedFraction: typing.Type[ContinuedFraction]
    FastMath: typing.Type[FastMath]
    FieldBlendable: typing.Type[FieldBlendable]
    FieldContinuedFraction: typing.Type[FieldContinuedFraction]
    FieldSinCos: typing.Type[FieldSinCos]
    FieldSinhCosh: typing.Type[FieldSinhCosh]
    FieldTuple: typing.Type[FieldTuple]
    Incrementor: typing.Type[Incrementor]
    IterationEvent: typing.Type[IterationEvent]
    IterationListener: typing.Type[IterationListener]
    IterationManager: typing.Type[IterationManager]
    JulierUnscentedTransform: typing.Type[JulierUnscentedTransform]
    KthSelector: typing.Type[KthSelector]
    MathArrays: typing.Type[MathArrays]
    MathUtils: typing.Type[MathUtils]
    MerweUnscentedTransform: typing.Type[MerweUnscentedTransform]
    MultidimensionalCounter: typing.Type[MultidimensionalCounter]
    OpenIntToDoubleHashMap: typing.Type[OpenIntToDoubleHashMap]
    OpenIntToFieldHashMap: typing.Type[OpenIntToFieldHashMap]
    Pair: typing.Type[Pair]
    PivotingStrategy: typing.Type[PivotingStrategy]
    Precision: typing.Type[Precision]
    ResizableDoubleArray: typing.Type[ResizableDoubleArray]
    RosenNumberPartitionIterator: typing.Type[RosenNumberPartitionIterator]
    RyuDouble: typing.Type[RyuDouble]
    SinCos: typing.Type[SinCos]
    SinhCosh: typing.Type[SinhCosh]
    Tuple: typing.Type[Tuple]
    UnscentedTransformProvider: typing.Type[UnscentedTransformProvider]
