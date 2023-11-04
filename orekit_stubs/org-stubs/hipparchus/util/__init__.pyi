import decimal
import java.io
import java.lang
import java.math
import java.text
import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.exception
import org.hipparchus.linear
import org.hipparchus.random
import typing



class ArithmeticUtils:
    """
    public final class ArithmeticUtils extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Some useful, arithmetics related, additions to the built-in functions in
        :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Math?is`.
    """
    @typing.overload
    @staticmethod
    def addAndCheck(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def addAndCheck(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def divideUnsigned(int: int, int2: int) -> int:
        """
            Returns the unsigned quotient of dividing the first argument by the second where each argument and the result is
            interpreted as an unsigned value.
        
            Note that in two's complement arithmetic, the three other basic arithmetic operations of add, subtract, and multiply are
            bit-wise identical if the two operands are regarded as both being signed or both being unsigned. Therefore separate
            :code:`addUnsigned`, etc. methods are not provided.
        
            This method does not use the :code:`long` datatype.
        
            Parameters:
                dividend (int): the value to be divided
                divisor (int): the value doing the dividing
        
            Returns:
                the unsigned quotient of the first argument divided by the second argument
        
            Returns the unsigned quotient of dividing the first argument by the second where each argument and the result is
            interpreted as an unsigned value.
        
            Note that in two's complement arithmetic, the three other basic arithmetic operations of add, subtract, and multiply are
            bit-wise identical if the two operands are regarded as both being signed or both being unsigned. Therefore separate
            :code:`addUnsigned`, etc. methods are not provided.
        
            This method does not use the :code:`BigInteger` datatype.
        
            Parameters:
                dividend (long): the value to be divided
                divisor (long): the value doing the dividing
        
            Returns:
                the unsigned quotient of the first argument divided by the second argument.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def divideUnsigned(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def gcd(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def gcd(long: int, long2: int) -> int: ...
    @staticmethod
    def isPowerOfTwo(long: int) -> bool:
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
    def lcm(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def lcm(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def mulAndCheck(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def mulAndCheck(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def pow(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def pow(bigInteger: java.math.BigInteger, int: int) -> java.math.BigInteger: ...
    @typing.overload
    @staticmethod
    def pow(bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger) -> java.math.BigInteger: ...
    @typing.overload
    @staticmethod
    def pow(bigInteger: java.math.BigInteger, long: int) -> java.math.BigInteger: ...
    @typing.overload
    @staticmethod
    def pow(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def remainderUnsigned(int: int, int2: int) -> int:
        """
            Returns the unsigned remainder from dividing the first argument by the second where each argument and the result is
            interpreted as an unsigned value.
        
            This method does not use the :code:`long` datatype.
        
            Parameters:
                dividend (int): the value to be divided
                divisor (int): the value doing the dividing
        
            Returns:
                the unsigned remainder of the first argument divided by the second argument.
        
            Returns the unsigned remainder from dividing the first argument by the second where each argument and the result is
            interpreted as an unsigned value.
        
            This method does not use the :code:`BigInteger` datatype.
        
            Parameters:
                dividend (long): the value to be divided
                divisor (long): the value doing the dividing
        
            Returns:
                the unsigned remainder of the first argument divided by the second argument.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def remainderUnsigned(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def subAndCheck(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def subAndCheck(long: int, long2: int) -> int: ...

class BigReal(org.hipparchus.FieldElement['BigReal'], java.lang.Comparable['BigReal'], java.io.Serializable):
    """
    public class BigReal extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.FieldElement`<:class:`~org.hipparchus.util.BigReal`>, :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable?is`<:class:`~org.hipparchus.util.BigReal`>, :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Arbitrary precision decimal number.
    
        This class is a simple wrapper around the standard :code:`BigDecimal` in order to implement the
        :class:`~org.hipparchus.FieldElement` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ZERO: typing.ClassVar['BigReal'] = ...
    """
    public static final :class:`~org.hipparchus.util.BigReal` ZERO
    
        A big real representing 0.
    
    """
    ONE: typing.ClassVar['BigReal'] = ...
    """
    public static final :class:`~org.hipparchus.util.BigReal` ONE
    
        A big real representing 1.
    
    """
    @typing.overload
    def __init__(self, charArray: typing.List[str]): ...
    @typing.overload
    def __init__(self, charArray: typing.List[str], int: int, int2: int): ...
    @typing.overload
    def __init__(self, charArray: typing.List[str], int: int, int2: int, mathContext: java.math.MathContext): ...
    @typing.overload
    def __init__(self, charArray: typing.List[str], mathContext: java.math.MathContext): ...
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
    def add(self, bigReal: 'BigReal') -> 'BigReal':
        """
            Compute this + a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.BigReal`): element to add
        
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
    def compareTo(self, bigReal: 'BigReal') -> int:
        """
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.html?is` in
                interface :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable?is`
        
        
        """
        ...
    def divide(self, bigReal: 'BigReal') -> 'BigReal': ...
    def doubleValue(self) -> float:
        """
            Get the double value corresponding to the instance.
        
            Returns:
                double value corresponding to the instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['BigReal']: ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def getRoundingMode(self) -> java.math.RoundingMode:
        """
            Gets the rounding mode for division operations The default is :code:`RoundingMode.HALF_UP`
        
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
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'BigReal':
        """
            Compute this × a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.BigReal`): element to multiply
        
            Returns:
                a new element representing this × a
        
            Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} =
            \sum_{i=1}^n \mathrm{this} \]
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
        
        """
        ...
    @typing.overload
    def multiply(self, bigReal: 'BigReal') -> 'BigReal': ...
    def negate(self) -> 'BigReal':
        """
            Returns the additive inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def reciprocal(self) -> 'BigReal': ...
    def setRoundingMode(self, roundingMode: java.math.RoundingMode) -> None:
        """
            Sets the rounding mode for decimal divisions.
        
            Parameters:
                roundingMode (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.RoundingMode?is`): rounding mode for decimal divisions
        
        
        """
        ...
    def setScale(self, int: int) -> None:
        """
            Sets the scale for division operations.
        
            Parameters:
                scale (int): scale for division operations
        
        
        """
        ...
    def subtract(self, bigReal: 'BigReal') -> 'BigReal':
        """
            Compute this - a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.BigReal`): element to subtract
        
            Returns:
                a new element representing this - a
        
        
        """
        ...

class BigRealField(org.hipparchus.Field[BigReal], java.io.Serializable):
    """
    public class BigRealField extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.util.BigReal`>, :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Representation of real numbers with arbitrary precision field.
    
        This class is a singleton.
    
        Also see:
            :class:`~org.hipparchus.util.BigReal`, :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
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
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[BigReal]: ...
    def getZero(self) -> BigReal:
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
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...

class Binary64(java.lang.Number, org.hipparchus.CalculusFieldElement['Binary64'], java.lang.Comparable['Binary64']):
    """
    public class Binary64 extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number?is` implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.util.Binary64`>, :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable?is`<:class:`~org.hipparchus.util.Binary64`>
    
        This class wraps a :code:`double` value in an object. It is similar to the standard class
        :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double?is`, while also implementing the
        :class:`~org.hipparchus.CalculusFieldElement` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ZERO: typing.ClassVar['Binary64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Binary64` ZERO
    
        The constant value of :code:`0d` as a :code:`Binary64`.
    
    """
    ONE: typing.ClassVar['Binary64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Binary64` ONE
    
        The constant value of :code:`1d` as a :code:`Binary64`.
    
    """
    PI: typing.ClassVar['Binary64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Binary64` PI
    
        The constant value of π as a :code:`Binary64`.
    
    """
    NEGATIVE_INFINITY: typing.ClassVar['Binary64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Binary64` NEGATIVE_INFINITY
    
        The constant value of :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is` as
        a :code:`Binary64`.
    
    """
    POSITIVE_INFINITY: typing.ClassVar['Binary64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Binary64` POSITIVE_INFINITY
    
        The constant value of :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is` as
        a :code:`Binary64`.
    
    """
    NAN: typing.ClassVar['Binary64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Binary64` NAN
    
        The constant value of :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is` as
        a :code:`Binary64`.
    
    """
    def __init__(self, double: float): ...
    def abs(self) -> 'Binary64':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'Binary64':
        """
            Arc cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'Binary64':
        """
            Inverse hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'Binary64':
        """
            Compute this + a. The current implementation strictly enforces :code:`this.add(a).equals(new Binary64(this.doubleValue()
            + a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Binary64`): element to add
        
            Returns:
                a new element representing this + a
        
            '+' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.add` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
        
        """
        ...
    @typing.overload
    def add(self, binary64: 'Binary64') -> 'Binary64': ...
    def asin(self) -> 'Binary64':
        """
            Arc sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'Binary64':
        """
            Inverse hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'Binary64':
        """
            Arc tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atan(this)
        
        
        """
        ...
    def atan2(self, binary64: 'Binary64') -> 'Binary64':
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
                x (:class:`~org.hipparchus.util.Binary64`): second argument of the arc tangent
        
            Returns:
        
        """
        ...
    def atanh(self) -> 'Binary64':
        """
            Inverse hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def byteValue(self) -> int:
        """
            The current implementation performs casting to a :code:`byte`.
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number?is`
        
        
        """
        ...
    def cbrt(self) -> 'Binary64':
        """
            Cubic root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cbrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'Binary64':
        """
            Get the smallest whole number larger than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ceil(this)
        
        
        """
        ...
    def compareTo(self, binary64: 'Binary64') -> int:
        """
            The current implementation returns the same value as :code:`new Double(this.doubleValue()).compareTo(new
            Double(o.doubleValue()))`
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.html?is` in
                interface :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable?is`
        
            Also see:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'Binary64':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (:class:`~org.hipparchus.util.Binary64`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, binary64: 'Binary64') -> 'Binary64': ...
    def cos(self) -> 'Binary64':
        """
            Cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'Binary64':
        """
            Hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'Binary64':
        """
            Compute this ÷ a. The current implementation strictly enforces :code:`this.divide(a).equals(new
            Binary64(this.doubleValue() / a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Binary64`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
            '÷' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.divide` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
        
        """
        ...
    @typing.overload
    def divide(self, binary64: 'Binary64') -> 'Binary64': ...
    def doubleValue(self) -> float:
        """
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number?is`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def exp(self) -> 'Binary64':
        """
            Exponential.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'Binary64':
        """
            Exponential minus 1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.expm1` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floatValue(self) -> float:
        """
            The current implementation performs casting to a :code:`float`.
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number?is`
        
        
        """
        ...
    def floor(self) -> 'Binary64':
        """
            Get the largest whole number smaller than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['Binary64']: ...
    def getPi(self) -> 'Binary64':
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
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            The current implementation returns the same value as :code:`new Double(this.doubleValue()).hashCode()`
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Also see:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`
        
        
        """
        ...
    def hypot(self, binary64: 'Binary64') -> 'Binary64':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2`  +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.hypot` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                y (:class:`~org.hipparchus.util.Binary64`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    def intValue(self) -> int:
        """
            The current implementation performs casting to a :code:`int`.
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number?is`
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Returns :code:`true` if :code:`this` double precision number is infinite
            (:meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is` or
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`).
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isInfinite` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                :code:`true` if :code:`this` number is infinite
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Returns :code:`true` if :code:`this` double precision number is Not-a-Number (:code:`NaN`), false otherwise.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isNaN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                :code:`true` if :code:`this` is :code:`NaN`
        
        
        """
        ...
    def isZero(self) -> bool:
        """
            Check if an element is semantically equal to zero.
        
            The default implementation simply calls :code:`equals(getField().getZero())`. However, this may need to be overridden in
            some cases as due to compatibility with :code:`hashCode()` some classes implements :code:`equals(Object)` in such a way
            that -0.0 and +0.0 are different, which may be a problem. It prevents for example identifying a diagonal element is zero
            and should be avoided when doing partial pivoting in LU decomposition.
        
            This implementation considers +0.0 and -0.0 to be equal.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.isZero` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                true if the element is semantically equal to zero
        
            Since:
                1.8
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, binary64: 'Binary64', double2: float, binary642: 'Binary64') -> 'Binary64':
        """
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Binary64`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Binary64`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Binary64`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Binary64`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Binary64`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Binary64`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Binary64`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Binary64`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Binary64`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Binary64`): second factor of the second term
                a3 (:class:`~org.hipparchus.util.Binary64`): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Binary64`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Binary64`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Binary64`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Binary64`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Binary64`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Binary64`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Binary64`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Binary64`): second factor of the second term
                a3 (:class:`~org.hipparchus.util.Binary64`): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Binary64`): second factor of the third term
                a4 (:class:`~org.hipparchus.util.Binary64`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.util.Binary64`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Binary64`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Binary64`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Binary64`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.util.Binary64`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, binary64: 'Binary64', double2: float, binary642: 'Binary64', double3: float, binary643: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, double: float, binary64: 'Binary64', double2: float, binary642: 'Binary64', double3: float, binary643: 'Binary64', double4: float, binary644: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], binary64Array: typing.List['Binary64']) -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, binary64: 'Binary64', binary642: 'Binary64', binary643: 'Binary64', binary644: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, binary64: 'Binary64', binary642: 'Binary64', binary643: 'Binary64', binary644: 'Binary64', binary645: 'Binary64', binary646: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, binary64: 'Binary64', binary642: 'Binary64', binary643: 'Binary64', binary644: 'Binary64', binary645: 'Binary64', binary646: 'Binary64', binary647: 'Binary64', binary648: 'Binary64') -> 'Binary64': ...
    @typing.overload
    def linearCombination(self, binary64Array: typing.List['Binary64'], binary64Array2: typing.List['Binary64']) -> 'Binary64': ...
    def log(self) -> 'Binary64':
        """
            Natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'Binary64':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'Binary64':
        """
            Shifted natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log1p` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    def longValue(self) -> int:
        """
            The current implementation performs casting to a :code:`long`.
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number?is`
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Binary64':
        """
            Compute this × a. The current implementation strictly enforces :code:`this.multiply(a).equals(new
            Binary64(this.doubleValue() * a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Binary64`): element to multiply
        
            Returns:
                a new element representing this × a
        
            Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} =
            \sum_{i=1}^n \mathrm{this} \] The current implementation strictly enforces :code:`this.multiply(n).equals(new Binary64(n
            * this.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
            '×' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
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
            Returns the additive inverse of :code:`this` element. The current implementation strictly enforces
            :code:`this.negate().equals(new Binary64(-this.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'Binary64':
        """
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                v (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'Binary64':
        """
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
            Integer power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                e (:class:`~org.hipparchus.util.Binary64`): exponent
        
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
            Returns the multiplicative inverse of :code:`this` element. The current implementation strictly enforces
            :code:`this.reciprocal().equals(new Binary64(1.0 / this.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.reciprocal` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'Binary64':
        """
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Binary64`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, binary64: 'Binary64') -> 'Binary64': ...
    def rint(self) -> 'Binary64':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'Binary64':
        """
            N :sup:`th` root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rootN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): order of the root
        
            Returns:
                n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, int: int) -> 'Binary64':
        """
            Multiply the instance by a power of 2.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.scalb` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power of 2
        
            Returns:
                this × 2 :sup:`n`
        
        
        """
        ...
    def shortValue(self) -> int:
        """
            The current implementation performs casting to a :code:`short`.
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Number?is`
        
        
        """
        ...
    def sign(self) -> 'Binary64':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'Binary64':
        """
            Sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> 'FieldSinCos'['Binary64']: ...
    def sinh(self) -> 'Binary64':
        """
            Hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> 'FieldSinhCosh'['Binary64']: ...
    def sqrt(self) -> 'Binary64':
        """
            Square root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'Binary64':
        """
            Compute this - a. The current implementation strictly enforces :code:`this.subtract(a).equals(new
            Binary64(this.doubleValue() - a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Binary64`): element to subtract
        
            Returns:
                a new element representing this - a
        
            '-' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.subtract` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
        
        """
        ...
    @typing.overload
    def subtract(self, binary64: 'Binary64') -> 'Binary64': ...
    def tan(self) -> 'Binary64':
        """
            Tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'Binary64':
        """
            Hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> 'Binary64':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'Binary64':
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
            The returned :code:`String` is equal to :code:`Double.toString(this.doubleValue())`
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Also see:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`
        
        
        """
        ...
    def ulp(self) -> 'Binary64':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ulp(this)
        
        
        """
        ...

class Binary64Field(org.hipparchus.Field[Binary64], java.io.Serializable):
    """
    public class Binary64Field extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.util.Binary64`>, :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        The field of :class:`~org.hipparchus.util.Binary64`.
    
        Also see:
            :class:`~org.hipparchus.util.Binary64`, :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
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
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Binary64]: ...
    def getZero(self) -> Binary64:
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
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...

_Blendable__B = typing.TypeVar('_Blendable__B')  # <B>
class Blendable(typing.Generic[_Blendable__B]):
    """
    public interface Blendable<B>
    
        Interface representing classes that can blend with other instances of themselves using a given blending value.
    
        The blending value is commonly given from a
        :class:`~org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction`.
    """
    def blendArithmeticallyWith(self, b: _Blendable__B, double: float) -> _Blendable__B: ...

class Combinations(java.lang.Iterable[typing.List[int]]):
    """
    public class Combinations extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable?is`<int[]>
    
        Utility to create combinations :code:`(n, k)` of :code:`k` elements in a set of :code:`n` elements.
    
        Also see:
            ` Combination @ Wikipedia <http://en.wikipedia.org/wiki/Combination>`
    """
    def __init__(self, int: int, int2: int): ...
    def comparator(self) -> java.util.Comparator[typing.List[int]]:
        """
            Defines a lexicographic ordering of combinations. The returned comparator allows to compare any two combinations that
            can be produced by this instance's :meth:`~org.hipparchus.util.Combinations.iterator`. Its :code:`compare(int[],int[])`
            method will throw exceptions if passed combinations that are inconsistent with this instance:
        
              - if the array lengths are not equal to :code:`k`,
              - if an element of the array is not within the interval [0, :code:`n`).
        
        
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
    def iterator(self) -> java.util.Iterator[typing.List[int]]:
        """
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable.html?is` in
                interface :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable?is`
        
        
        """
        ...

class CombinatoricsUtils:
    """
    public final class CombinatoricsUtils extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Combinatorial utilities.
    """
    MAX_BELL: typing.ClassVar[int] = ...
    """
    public static final int MAX_BELL
    
        Maximum index of Bell number that fits into a long.
    
        Since:
            2.2
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def bellNumber(int: int) -> int:
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
    def binomialCoefficient(int: int, int2: int) -> int: ...
    @staticmethod
    def binomialCoefficientDouble(int: int, int2: int) -> float: ...
    @staticmethod
    def binomialCoefficientLog(int: int, int2: int) -> float: ...
    @staticmethod
    def checkBinomial(int: int, int2: int) -> None: ...
    @staticmethod
    def combinationsIterator(int: int, int2: int) -> java.util.Iterator[typing.List[int]]:
        """
            Returns an iterator whose range is the k-element subsets of {0, ..., n - 1} represented as :code:`int[]` arrays.
        
            The arrays returned by the iterator are sorted in descending order and they are visited in lexicographic order with
            significance from right to left. For example, combinationsIterator(4, 2) returns an Iterator that will generate the
            following sequence of arrays on successive calls to :code:`next()`:
        
            :code:`[0, 1], [0, 2], [1, 2], [0, 3], [1, 3], [2, 3]`
        
            If :code:`k == 0` an Iterator containing an empty array is returned and if :code:`k == n` an Iterator containing [0,
            ..., n -1] is returned.
        
            Parameters:
                n (int): Size of the set from which subsets are selected.
                k (int): Size of the subsets to be enumerated.
        
            Returns:
                an :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator?is` over the k-sets in n.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`n < 0`.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`k > n`.
        
        
        """
        ...
    @staticmethod
    def factorial(int: int) -> int: ...
    @staticmethod
    def factorialDouble(int: int) -> float: ...
    @staticmethod
    def factorialLog(int: int) -> float: ...
    _partitions__T = typing.TypeVar('_partitions__T')  # <T>
    @staticmethod
    def partitions(list: java.util.List[_partitions__T]) -> java.util.stream.Stream[typing.List[java.util.List[_partitions__T]]]: ...
    _permutations__T = typing.TypeVar('_permutations__T')  # <T>
    @staticmethod
    def permutations(list: java.util.List[_permutations__T]) -> java.util.stream.Stream[java.util.List[_permutations__T]]: ...
    @staticmethod
    def stirlingS2(int: int, int2: int) -> int: ...
    class FactorialLog:
        @staticmethod
        def create() -> 'CombinatoricsUtils.FactorialLog': ...
        def value(self, int: int) -> float: ...
        def withCache(self, int: int) -> 'CombinatoricsUtils.FactorialLog': ...

class CompositeFormat:
    """
    public class CompositeFormat extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for formatters of composite objects (complex numbers, vectors ...).
    """
    @staticmethod
    def formatDouble(double: float, numberFormat: java.text.NumberFormat, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer:
        """
            Formats a double value to produce a string. In general, the value is formatted using the formatting rules of
            :code:`format`. There are three exceptions to this:
        
              1.  NaN is formatted as '(NaN)'
              2.  Positive infinity is formatted as '(Infinity)'
              3.  Negative infinity is formatted as '(-Infinity)'
        
        
            Parameters:
                value (double): the double to format.
                format (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat?is`): the format used.
                toAppendTo (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer?is`): where the text is to be appended
                pos (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition?is`): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDefaultNumberFormat() -> java.text.NumberFormat:
        """
            Create a default number format. The default number format is based on
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.html?is` with the only
            customizing that the maximum number of fraction digits is set to 10.
        
            Returns:
                the default number format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDefaultNumberFormat(locale: java.util.Locale) -> java.text.NumberFormat:
        """
            Create a default number format. The default number format is based on
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat.html?is` with the only
            customizing that the maximum number of fraction digits is set to 10.
        
            Parameters:
                locale (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Locale?is`): the specific locale used by the format.
        
            Returns:
                the default number format specific to the given locale.
        
        
        """
        ...
    @staticmethod
    def parseAndIgnoreWhitespace(string: str, parsePosition: java.text.ParsePosition) -> None:
        """
            Parses :code:`source` until a non-whitespace character is found.
        
            Parameters:
                source (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the string to parse
                pos (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition?is`): input/output parsing parameter. On output, :code:`pos` holds the index of the next non-whitespace character.
        
        
        """
        ...
    @staticmethod
    def parseFixedstring(string: str, string2: str, parsePosition: java.text.ParsePosition) -> bool:
        """
            Parse :code:`source` for an expected fixed string.
        
            Parameters:
                source (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the string to parse
                expected (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): expected string
                pos (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition?is`): input/output parsing parameter.
        
            Returns:
                true if the expected string was there
        
        
        """
        ...
    @staticmethod
    def parseNextCharacter(string: str, parsePosition: java.text.ParsePosition) -> str:
        """
            Parses :code:`source` until a non-whitespace character is found.
        
            Parameters:
                source (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the string to parse
                pos (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition?is`): input/output parsing parameter.
        
            Returns:
                the first non-whitespace character.
        
        
        """
        ...
    @staticmethod
    def parseNumber(string: str, numberFormat: java.text.NumberFormat, parsePosition: java.text.ParsePosition) -> java.lang.Number:
        """
            Parses :code:`source` for a number. This method can parse normal, numeric values as well as special values. These
            special values include Double.NaN, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY.
        
            Parameters:
                source (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the string to parse
                format (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat?is`): the number format used to parse normal, numeric values.
                pos (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.text.ParsePosition?is`): input/output parsing parameter.
        
            Returns:
                the parsed number.
        
        
        """
        ...

class ContinuedFraction:
    """
    public abstract class ContinuedFraction extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Provides a generic means to evaluate continued fractions. Subclasses simply provided the a and b coefficients to
        evaluate the continued fraction.
    
        References:
    
          - ` Continued Fraction <http://mathworld.wolfram.com/ContinuedFraction.html>`
    """
    @typing.overload
    def evaluate(self, double: float) -> float: ...
    @typing.overload
    def evaluate(self, double: float, double2: float) -> float: ...
    @typing.overload
    def evaluate(self, double: float, double2: float, int: int) -> float: ...
    @typing.overload
    def evaluate(self, double: float, int: int) -> float: ...

class FastMath:
    """
    public class FastMath extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Faster, more accurate, portable alternative to
        :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Math?is` and
        :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.StrictMath?is` for large scale
        computation.
    
        FastMath is a drop-in replacement for both Math and StrictMath. This means that for any method in Math (say
        :code:`Math.sin(x)` or :code:`Math.cbrt(y)`), user can directly change the class and use the methods as is (using
        :code:`FastMath.sin(x)` or :code:`FastMath.cbrt(y)` in the previous example).
    
        FastMath speed is achieved by relying heavily on optimizing compilers to native code present in many JVMs today and use
        of large tables. The larger tables are lazily initialized on first use, so that the setup time does not penalize methods
        that don't need them.
    
        Note that FastMath is extensively used inside Hipparchus, so by calling some algorithms, the overhead when the the
        tables need to be initialized will occur regardless of the end-user calling FastMath methods directly or not.
        Performance figures for a specific JVM and hardware can be evaluated by running the FastMathTestPerformance tests in the
        test directory of the source distribution.
    
        FastMath accuracy should be mostly independent of the JVM as it relies only on IEEE-754 basic operations and on embedded
        tables. Almost all operations are accurate to about 0.5 ulp throughout the domain range. This statement, of course is
        only a rough global observed behavior, it is *not* a guarantee for *every* double numbers input (see William Kahan's
        `Table Maker's Dilemma <http://en.wikipedia.org/wiki/Rounding#The_table-maker.27s_dilemma>`).
    
        FastMath additionally implements the following methods not found in Math/StrictMath:
    
          - :meth:`~org.hipparchus.util.FastMath.asinh`
          - :meth:`~org.hipparchus.util.FastMath.acosh`
          - :meth:`~org.hipparchus.util.FastMath.atanh`
    
        The following methods are found in Math/StrictMath since 1.6 only, they are provided by FastMath even in 1.5 Java
        virtual machines
    
          - :meth:`~org.hipparchus.util.FastMath.copySign`
          - :meth:`~org.hipparchus.util.FastMath.getExponent`
          - :meth:`~org.hipparchus.util.FastMath.nextAfter`
          - :meth:`~org.hipparchus.util.FastMath.nextUp`
          - :meth:`~org.hipparchus.util.FastMath.scalb`
          - :meth:`~org.hipparchus.util.FastMath.copySign`
          - :meth:`~org.hipparchus.util.FastMath.getExponent`
          - :meth:`~org.hipparchus.util.FastMath.nextAfter`
          - :meth:`~org.hipparchus.util.FastMath.nextUp`
          - :meth:`~org.hipparchus.util.FastMath.scalb`
    """
    PI: typing.ClassVar[float] = ...
    """
    public static final double PI
    
        Archimede's constant PI, ratio of circle circumference to diameter.
    
        Also see:
            :meth:`~constant`
    
    
    """
    E: typing.ClassVar[float] = ...
    """
    public static final double E
    
        Napier's constant e, base of the natural logarithm.
    
        Also see:
            :meth:`~constant`
    
    
    """
    _IEEEremainder_1__T = typing.TypeVar('_IEEEremainder_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _IEEEremainder_2__T = typing.TypeVar('_IEEEremainder_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def IEEEremainder(double: float, double2: float) -> float:
        """
            Computes the remainder as prescribed by the IEEE 754 standard.
        
            The remainder value is mathematically equal to :code:`x - y*n` where :code:`n` is the mathematical integer closest to
            the exact mathematical value of the quotient :code:`x/y`. If two mathematical integers are equally close to :code:`x/y`
            then :code:`n` is the integer that is even.
        
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
    def IEEEremainder(t: _IEEEremainder_1__T, double: float) -> _IEEEremainder_1__T:
        """
            Computes the remainder as prescribed by the IEEE 754 standard.
        
            The remainder value is mathematically equal to :code:`x - y*n` where :code:`n` is the mathematical integer closest to
            the exact mathematical value of the quotient :code:`x/y`. If two mathematical integers are equally close to :code:`x/y`
            then :code:`n` is the integer that is even.
        
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
        
            The remainder value is mathematically equal to :code:`x - y*n` where :code:`n` is the mathematical integer closest to
            the exact mathematical value of the quotient :code:`x/y`. If two mathematical integers are equally close to :code:`x/y`
            then :code:`n` is the integer that is even.
        
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
    def IEEEremainder(t: _IEEEremainder_2__T, t2: _IEEEremainder_2__T) -> _IEEEremainder_2__T: ...
    _abs_4__T = typing.TypeVar('_abs_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def abs(double: float) -> float:
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
    def abs(float: float) -> float: ...
    @typing.overload
    @staticmethod
    def abs(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def abs(long: int) -> int: ...
    @typing.overload
    @staticmethod
    def abs(t: _abs_4__T) -> _abs_4__T:
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
    def absExact(int: int) -> int:
        """
            Absolute value.
        
            Parameters:
                x (int): number from which absolute value is requested
        
            Returns:
                abs(x), or throws an exception for :code:`Integer.MIN_VALUE`
        
            Since:
                2.0
        
            Absolute value.
        
            Parameters:
                x (long): number from which absolute value is requested
        
            Returns:
                abs(x), or throws an exception for :code:`Long.MIN_VALUE`
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def absExact(long: int) -> int: ...
    _acos_1__T = typing.TypeVar('_acos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def acos(double: float) -> float:
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
    def acos(t: _acos_1__T) -> _acos_1__T:
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
    def acosh(double: float) -> float:
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
    def acosh(t: _acosh_1__T) -> _acosh_1__T:
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
    def addExact(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def addExact(long: int, long2: int) -> int: ...
    _asin_1__T = typing.TypeVar('_asin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def asin(double: float) -> float:
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
    def asin(t: _asin_1__T) -> _asin_1__T:
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
    def asinh(double: float) -> float:
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
    def asinh(t: _asinh_1__T) -> _asinh_1__T:
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
    def atan(double: float) -> float:
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
    def atan(t: _atan_1__T) -> _atan_1__T:
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
    def atan2(double: float, double2: float) -> float:
        """
            Two arguments arctangent function
        
            Parameters:
                y (double): ordinate
                x (double): abscissa
        
            Returns:
                phase angle of point (x,y) between :code:`-PI` and :code:`PI`
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(t: _atan2_1__T, t2: _atan2_1__T) -> _atan2_1__T:
        """
            Two arguments arctangent function
        
            Parameters:
                y (T): ordinate
                x (T): abscissa
        
            Returns:
                phase angle of point (x,y) between :code:`-PI` and :code:`PI`
        
            Since:
                1.3
        
        
        """
        ...
    _atanh_1__T = typing.TypeVar('_atanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def atanh(double: float) -> float:
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
    def atanh(t: _atanh_1__T) -> _atanh_1__T:
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
    def cbrt(double: float) -> float:
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
    def cbrt(t: _cbrt_1__T) -> _cbrt_1__T:
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
    def ceil(double: float) -> float:
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
    def ceil(t: _ceil_1__T) -> _ceil_1__T:
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
    def ceilDiv(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDiv(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDiv(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDivExact(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilDivExact(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilMod(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilMod(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def ceilMod(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def clamp(double: float, double2: float, double3: float) -> float:
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
    def clamp(float: float, float2: float, float3: float) -> float: ...
    @typing.overload
    @staticmethod
    def clamp(int: int, int2: int, int3: int) -> int: ...
    @typing.overload
    @staticmethod
    def clamp(long: int, int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def clamp(long: int, long2: int, long3: int) -> int: ...
    _copySign_2__T = typing.TypeVar('_copySign_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _copySign_3__T = typing.TypeVar('_copySign_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def copySign(double: float, double2: float) -> float:
        """
            Returns the first argument with the sign of the second argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                magnitude (double): the value to return
                sign (double): the sign for the returned value
        
            Returns:
                the magnitude with the same sign as the :code:`sign` argument
        
            Returns the first argument with the sign of the second argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                magnitude (float): the value to return
                sign (float): the sign for the returned value
        
            Returns:
                the magnitude with the same sign as the :code:`sign` argument
        
        """
        ...
    @typing.overload
    @staticmethod
    def copySign(float: float, float2: float) -> float: ...
    @typing.overload
    @staticmethod
    def copySign(t: _copySign_2__T, double: float) -> _copySign_2__T:
        """
            Returns the first argument with the sign of the second argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                magnitude (T): the value to return
                sign (T): the sign for the returned value
        
            Returns:
                the magnitude with the same sign as the :code:`sign` argument
        
            Since:
                1.3
        
            Returns the first argument with the sign of the second argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                magnitude (T): the value to return
                sign (double): the sign for the returned value
        
            Returns:
                the magnitude with the same sign as the :code:`sign` argument
        
            Since:
                1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def copySign(t: _copySign_3__T, t2: _copySign_3__T) -> _copySign_3__T: ...
    _cos_1__T = typing.TypeVar('_cos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def cos(double: float) -> float:
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
    def cos(t: _cos_1__T) -> _cos_1__T:
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
    def cosh(double: float) -> float:
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
    def cosh(t: _cosh_1__T) -> _cosh_1__T:
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
    def decrementExact(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def decrementExact(long: int) -> int: ...
    @typing.overload
    @staticmethod
    def divideExact(int: int, int2: int) -> int:
        """
            Divide two integers, checking for overflow.
        
            Parameters:
                x (int): dividend
                y (int): divisor
        
            Returns:
                x / y
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an overflow occurs
        
            Since:
                3.0
        
            Divide two long integers, checking for overflow.
        
            Parameters:
                x (long): dividend
                y (long): divisor
        
            Returns:
                x / y
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an overflow occurs
        
            Since:
                3.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def divideExact(long: int, long2: int) -> int: ...
    _exp_1__T = typing.TypeVar('_exp_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def exp(double: float) -> float:
        """
            Exponential function. Computes exp(x), function result is nearly rounded. It will be correctly rounded to the
            theoretical value for 99.9% of input values, otherwise it will have a 1 ULP error. Method: Lookup intVal = exp(int(x))
            Lookup fracVal = exp(int(x-int(x) / 1024.0) * 1024.0 ); Compute z as the exponential of the remaining bits by a
            polynomial minus one exp(x) = intVal * fracVal * (1 + z) Accuracy: Calculation is done with 63 bits of precision, so
            result should be correctly rounded for 99.9% of input values, with less than 1 ULP error otherwise.
        
            Parameters:
                x (double): a double
        
            Returns:
                double e :sup:`x`
        
        """
        ...
    @typing.overload
    @staticmethod
    def exp(t: _exp_1__T) -> _exp_1__T:
        """
            Exponential function. Computes exp(x), function result is nearly rounded. It will be correctly rounded to the
            theoretical value for 99.9% of input values, otherwise it will have a 1 ULP error. Method: Lookup intVal = exp(int(x))
            Lookup fracVal = exp(int(x-int(x) / 1024.0) * 1024.0 ); Compute z as the exponential of the remaining bits by a
            polynomial minus one exp(x) = intVal * fracVal * (1 + z) Accuracy: Calculation is done with 63 bits of precision, so
            result should be correctly rounded for 99.9% of input values, with less than 1 ULP error otherwise.
        
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
    def expm1(double: float) -> float:
        """
            Compute exp(x) - 1
        
            Parameters:
                x (double): number to compute shifted exponential
        
            Returns:
                exp(x) - 1
        
        """
        ...
    @typing.overload
    @staticmethod
    def expm1(t: _expm1_1__T) -> _expm1_1__T:
        """
            Compute exp(x) - 1
        
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
    def floor(double: float) -> float:
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
    def floor(t: _floor_1__T) -> _floor_1__T:
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
    def floorDiv(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDiv(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDiv(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDivExact(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorDivExact(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorMod(int: int, int2: int) -> int:
        """
            Finds r such that :code:`a = q b + r` with :code:`0 <= r < b` if :code:`b > 0` and :code:`b < r <= 0` if :code:`b < 0`.
        
            This methods returns the same value as integer modulo when a and b are same signs, but returns a different value when
            they are opposite (i.e. q is negative).
        
            Parameters:
                a (long): dividend
                b (int): divisor
        
            Returns:
                r such that :code:`a = q b + r` with :code:`0 <= r < b` if :code:`b > 0` and :code:`b < r <= 0` if :code:`b < 0`
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if b == 0
        
            Since:
                1.3
        
            Also see:
                :meth:`~org.hipparchus.util.FastMath.floorDiv`
        
            Finds r such that :code:`a = q b + r` with :code:`0 <= r < b` if :code:`b > 0` and :code:`b < r <= 0` if :code:`b < 0`.
        
            This methods returns the same value as integer modulo when a and b are same signs, but returns a different value when
            they are opposite (i.e. q is negative).
        
            Parameters:
                a (long): dividend
                b (long): divisor
        
            Returns:
                r such that :code:`a = q b + r` with :code:`0 <= r < b` if :code:`b > 0` and :code:`b < r <= 0` if :code:`b < 0`
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if b == 0
        
            Also see:
                :meth:`~org.hipparchus.util.FastMath.floorDiv`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def floorMod(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorMod(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def fma(double: float, double2: float, double3: float) -> float:
        """
            Compute Fused-multiply-add operation a * b + c.
        
            This method was introduced in the regular :code:`Math` and :code:`StrictMath` methods with Java 9, and then added to
            Hipparchus for consistency. However, a more general method was available in Hipparchus that also allow to repeat this
            computation across several terms: :meth:`~org.hipparchus.util.MathArrays.linearCombination`. The linear combination
            method should probably be preferred in most cases.
        
            Parameters:
                a (double): first factor
                b (double): second factor
                c (double): additive term
        
            Returns:
                a * b + c, using extended precision in the multiplication
        
            Since:
                1.3
        
            Also see:
                :meth:`~org.hipparchus.util.MathArrays.linearCombination`, :meth:`~org.hipparchus.util.MathArrays.linearCombination`,
                :meth:`~org.hipparchus.util.MathArrays.linearCombination`, :meth:`~org.hipparchus.util.MathArrays.linearCombination`
        
            Compute Fused-multiply-add operation a * b + c.
        
            This method was introduced in the regular :code:`Math` and :code:`StrictMath` methods with Java 9, and then added to
            Hipparchus for consistency. However, a more general method was available in Hipparchus that also allow to repeat this
            computation across several terms: :meth:`~org.hipparchus.util.MathArrays.linearCombination`. The linear combination
            method should probably be preferred in most cases.
        
            Parameters:
                a (float): first factor
                b (float): second factor
                c (float): additive term
        
            Returns:
                a * b + c, using extended precision in the multiplication
        
            Also see:
                :meth:`~org.hipparchus.util.MathArrays.linearCombination`, :meth:`~org.hipparchus.util.MathArrays.linearCombination`,
                :meth:`~org.hipparchus.util.MathArrays.linearCombination`, :meth:`~org.hipparchus.util.MathArrays.linearCombination`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def fma(float: float, float2: float, float3: float) -> float: ...
    @typing.overload
    @staticmethod
    def getExponent(double: float) -> int:
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
    def hypot(double: float, double2: float) -> float:
        """
            Returns the hypotenuse of a triangle with sides :code:`x` and :code:`y` - sqrt(*x* :sup:`2`  +*y* :sup:`2` )
        
        
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Parameters:
                x (double): a value
                y (double): a value
        
            Returns:
                sqrt(*x* :sup:`2`  +*y* :sup:`2` )
        
        """
        ...
    @typing.overload
    @staticmethod
    def hypot(t: _hypot_1__T, t2: _hypot_1__T) -> _hypot_1__T:
        """
            Returns the hypotenuse of a triangle with sides :code:`x` and :code:`y` - sqrt(*x* :sup:`2`  +*y* :sup:`2` )
        
        
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Parameters:
                x (T): a value
                y (T): a value
        
            Returns:
                sqrt(*x* :sup:`2`  +*y* :sup:`2` )
        
            Since:
                1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def incrementExact(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def incrementExact(long: int) -> int: ...
    _log_2__T = typing.TypeVar('_log_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def log(double: float) -> float:
        """
            Natural logarithm.
        
            Parameters:
                x (double): a double
        
            Returns:
                log(x)
        
            Computes the ` logarithm <http://mathworld.wolfram.com/Logarithm.html>` in a given base. Returns :code:`NaN` if either
            argument is negative. If :code:`base` is 0 and :code:`x` is positive, 0 is returned. If :code:`base` is positive and
            :code:`x` is 0, :code:`Double.NEGATIVE_INFINITY` is returned. If both arguments are 0, the result is :code:`NaN`.
        
            Parameters:
                base (double): Base of the logarithm, must be greater than 0.
                x (double): Argument, must be greater than 0.
        
            Returns:
                the value of the logarithm, i.e. the number :code:`y` such that :code:`base :sup:`y` = x`.
        
        """
        ...
    @typing.overload
    @staticmethod
    def log(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def log(t: _log_2__T) -> _log_2__T:
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
    def log10(double: float) -> float:
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
    def log10(t: _log10_1__T) -> _log10_1__T:
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
    def log1p(double: float) -> float:
        """
            Computes log(1 + x).
        
            Parameters:
                x (double): Number.
        
            Returns:
                :code:`log(1 + x)`.
        
        """
        ...
    @typing.overload
    @staticmethod
    def log1p(t: _log1p_1__T) -> _log1p_1__T:
        """
            Computes log(1 + x).
        
            Parameters:
                x (T): Number.
        
            Returns:
                :code:`log(1 + x)`.
        
            Since:
                1.3
        
        
        """
        ...
    _max_4__T = typing.TypeVar('_max_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _max_5__T = typing.TypeVar('_max_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def max(double: float, double2: float) -> float:
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
    def max(float: float, float2: float) -> float: ...
    @typing.overload
    @staticmethod
    def max(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def max(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def max(t: _max_4__T, double: float) -> _max_4__T:
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
    def max(t: _max_5__T, t2: _max_5__T) -> _max_5__T: ...
    _min_4__T = typing.TypeVar('_min_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _min_5__T = typing.TypeVar('_min_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def min(double: float, double2: float) -> float:
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
    def min(float: float, float2: float) -> float: ...
    @typing.overload
    @staticmethod
    def min(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def min(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def min(t: _min_4__T, double: float) -> _min_4__T:
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
    def min(t: _min_5__T, t2: _min_5__T) -> _min_5__T: ...
    @typing.overload
    @staticmethod
    def multiplyExact(int: int, int2: int) -> int:
        """
            Multiply two numbers, detecting overflows.
        
            Parameters:
                a (int): first number to multiply
                b (int): second number to multiply
        
            Returns:
                a*b if no overflows occur
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an overflow occurs
        
            Multiply two numbers, detecting overflows.
        
            Parameters:
                a (long): first number to multiply
                b (int): second number to multiply
        
            Returns:
                a*b if no overflows occur
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an overflow occurs
        
            Since:
                1.3
        
            Multiply two numbers, detecting overflows.
        
            Parameters:
                a (long): first number to multiply
                b (long): second number to multiply
        
            Returns:
                a*b if no overflows occur
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an overflow occurs
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiplyExact(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def multiplyExact(long: int, long2: int) -> int: ...
    @staticmethod
    def multiplyFull(int: int, int2: int) -> int:
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
    def multiplyHigh(long: int, long2: int) -> int:
        """
            Multiply two long integers and give the 64 most significant bits of the result.
        
            Beware that as Java primitive long are always considered to be signed, there are some intermediate values :code:`a` and
            :code:`b` for which :code:`a * b` exceeds :code:`Long.MAX_VALUE` but this method will still return 0l. This happens for
            example for :code:`a = 2³¹` and :code:`b = 2³²` as :code:`a * b = 2⁶³ = Long.MAX_VALUE + 1`, so it exceeds the
            max value for a long, but still fits in 64 bits, so this method correctly returns 0l in this case, but multiplication
            result would be considered negative (and in fact equal to :code:`Long.MIN_VALUE`
        
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
    def negateExact(int: int) -> int:
        """
            Negates the argument.
        
            Parameters:
                x (int): number from which opposite value is requested
        
            Returns:
                -x, or throws an exception for :code:`Integer.MIN_VALUE`
        
            Since:
                2.0
        
            Negates the argument.
        
            Parameters:
                x (long): number from which opposite value is requested
        
            Returns:
                -x, or throws an exception for :code:`Long.MIN_VALUE`
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def negateExact(long: int) -> int: ...
    @typing.overload
    @staticmethod
    def nextAfter(double: float, double2: float) -> float:
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
        
            If :code:`direction` is greater than :code:`d`, the smallest machine representable number strictly greater than
            :code:`d` is returned; if less, then the largest representable number strictly less than :code:`d` is returned.
        
            If :code:`d` is infinite and direction does not bring it back to finite numbers, it is returned unchanged.
        
            Parameters:
                d (double): base number
                direction (double): (the only important thing is whether :code:`direction` is greater or smaller than :code:`d`)
        
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
        
            If :code:`direction` is greater than :code:`f`, the smallest machine representable number strictly greater than
            :code:`f` is returned; if less, then the largest representable number strictly less than :code:`f` is returned.
        
            If :code:`f` is infinite and direction does not bring it back to finite numbers, it is returned unchanged.
        
            Parameters:
                f (float): base number
                direction (double): (the only important thing is whether :code:`direction` is greater or smaller than :code:`f`)
        
            Returns:
                the next machine representable number in the specified direction
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def nextAfter(float: float, double: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextDown(double: float) -> float:
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
    def nextDown(float: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextUp(double: float) -> float:
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
    def nextUp(float: float) -> float: ...
    _norm__T = typing.TypeVar('_norm__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def norm(t: _norm__T) -> float:
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
    def pow(double: float, double2: float) -> float:
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
    def pow(t: _pow_3__T, double: float) -> _pow_3__T:
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
        
            **Note:** this implementation currently delegates to
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Math.html?is`
        
            Returns:
                a random number between 0.0 and 1.0
        
        
        """
        ...
    _rint_1__T = typing.TypeVar('_rint_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rint(double: float) -> float:
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
    def rint(t: _rint_1__T) -> _rint_1__T:
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
    def round(float: float) -> int:
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
    def round(double: float) -> int: ...
    @typing.overload
    @staticmethod
    def round(t: _round_2__T) -> int:
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
    def scalb(double: float, int: int) -> float:
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
    def scalb(t: _scalb_2__T, int: int) -> _scalb_2__T:
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
    def sign(t: _sign__T) -> _sign__T:
        """
            Compute the sign of a number. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex
            number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
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
    def signum(double: float) -> float:
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
    def signum(float: float) -> float: ...
    _sin_1__T = typing.TypeVar('_sin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sin(double: float) -> float:
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
    def sin(t: _sin_1__T) -> _sin_1__T:
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
    def sinCos(t: _sinCos_0__T) -> 'FieldSinCos'[_sinCos_0__T]:
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
    def sinCos(double: float) -> 'SinCos':
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
    def sinh(double: float) -> float:
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
    def sinh(t: _sinh_1__T) -> _sinh_1__T:
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
    def sinhCosh(t: _sinhCosh_0__T) -> 'FieldSinhCosh'[_sinhCosh_0__T]:
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
    def sinhCosh(double: float) -> 'SinhCosh':
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
    def sqrt(double: float) -> float:
        """
            Compute the square root of a number.
        
            **Note:** this implementation currently delegates to
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Math.html?is`
        
            Parameters:
                a (double): number on which evaluation is done
        
            Returns:
                square root of a
        
        """
        ...
    @typing.overload
    @staticmethod
    def sqrt(t: _sqrt_1__T) -> _sqrt_1__T:
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
    def subtractExact(int: int, int2: int) -> int:
        """
            Subtract two numbers, detecting overflows.
        
            Parameters:
                a (int): first number
                b (int): second number to subtract from a
        
            Returns:
                a-b if no overflows occur
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an overflow occurs
        
            Subtract two numbers, detecting overflows.
        
            Parameters:
                a (long): first number
                b (long): second number to subtract from a
        
            Returns:
                a-b if no overflows occur
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an overflow occurs
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtractExact(long: int, long2: int) -> int: ...
    _tan_1__T = typing.TypeVar('_tan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tan(double: float) -> float:
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
    def tan(t: _tan_1__T) -> _tan_1__T:
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
    def tanh(double: float) -> float:
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
    def tanh(t: _tanh_1__T) -> _tanh_1__T:
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
    def toDegrees(double: float) -> float:
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
    def toDegrees(t: _toDegrees_1__T) -> _toDegrees_1__T:
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Parameters:
                x (T): angle in radians
        
            Returns:
                x converted into degrees
        
        
        """
        ...
    @staticmethod
    def toIntExact(long: int) -> int: ...
    _toRadians_1__T = typing.TypeVar('_toRadians_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def toRadians(double: float) -> float:
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
    def toRadians(t: _toRadians_1__T) -> _toRadians_1__T:
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
    def ulp(double: float) -> float:
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
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
    def ulp(float: float) -> float: ...
    @typing.overload
    @staticmethod
    def ulp(t: _ulp_2__T) -> _ulp_2__T:
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            Parameters:
                x (T): number from which ulp is requested
        
            Returns:
                ulp(x)
        
            Since:
                2.0
        
        
        """
        ...
    @staticmethod
    def unsignedMultiplyHigh(long: int, long2: int) -> int:
        """
            Multiply two long unsigned integers and give the 64 most significant bits of the unsigned result.
        
            Beware that as Java primitive long are always considered to be signed, there are some intermediate values :code:`a` and
            :code:`b` for which :code:`a * b` exceeds :code:`Long.MAX_VALUE` but this method will still return 0l. This happens for
            example for :code:`a = 2³¹` and :code:`b = 2³²` as :code:`a * b = 2⁶³ = Long.MAX_VALUE + 1`, so it exceeds the
            max value for a long, but still fits in 64 bits, so this method correctly returns 0l in this case, but multiplication
            result would be considered negative (and in fact equal to :code:`Long.MIN_VALUE`
        
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
    public interface FieldBlendable<B, T extends :class:`~org.hipparchus.FieldElement`<T>>
    
        Interface representing classes that can blend with other instances of themselves using a given blending value.
    
        The blending value is commonly given from a
        :class:`~org.hipparchus.analysis.polynomials.SmoothStepFactory.FieldSmoothStepFunction`.
    """
    def blendArithmeticallyWith(self, b: _FieldBlendable__B, t: _FieldBlendable__T) -> _FieldBlendable__B: ...

class FieldContinuedFraction:
    """
    public abstract class FieldContinuedFraction extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Provides a generic means to evaluate continued fractions. Subclasses simply provided the a and b coefficients to
        evaluate the continued fraction.
    
        References:
    
          - ` Continued Fraction <http://mathworld.wolfram.com/ContinuedFraction.html>`
    """
    _evaluate_0__T = typing.TypeVar('_evaluate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _evaluate_1__T = typing.TypeVar('_evaluate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _evaluate_2__T = typing.TypeVar('_evaluate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _evaluate_3__T = typing.TypeVar('_evaluate_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def evaluate(self, t: _evaluate_0__T) -> _evaluate_0__T: ...
    @typing.overload
    def evaluate(self, t: _evaluate_1__T, double: float) -> _evaluate_1__T: ...
    @typing.overload
    def evaluate(self, t: _evaluate_2__T, double: float, int: int) -> _evaluate_2__T: ...
    @typing.overload
    def evaluate(self, t: _evaluate_3__T, int: int) -> _evaluate_3__T: ...
    _getA__T = typing.TypeVar('_getA__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getA(self, int: int, t: _getA__T) -> _getA__T: ...
    _getB__T = typing.TypeVar('_getB__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getB(self, int: int, t: _getB__T) -> _getB__T: ...

_FieldSinCos__T = typing.TypeVar('_FieldSinCos__T')  # <T>
class FieldSinCos(typing.Generic[_FieldSinCos__T]):
    """
    public class FieldSinCos<T> extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Holder for both sine and cosine values.
    
        This class is a simple container, it does not provide any computational method.
    
        Since:
            1.4
    
        Also see:
            :meth:`~org.hipparchus.util.FastMath.sinCos`
    """
    def __init__(self, t: _FieldSinCos__T, t2: _FieldSinCos__T): ...
    def cos(self) -> _FieldSinCos__T:
        """
            Get the value of the cosine.
        
            Returns:
                value of the cosine
        
        
        """
        ...
    _difference__S = typing.TypeVar('_difference__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def difference(fieldSinCos: 'FieldSinCos'[_difference__S], fieldSinCos2: 'FieldSinCos'[_difference__S]) -> 'FieldSinCos'[_difference__S]:
        """
            Compute sine and cosine of angles difference.
        
            Parameters:
                scAlpha (:class:`~org.hipparchus.util.FieldSinCos`<S> scAlpha): \((\sin \alpha, \cos \alpha)\)
                scBeta (:class:`~org.hipparchus.util.FieldSinCos`<S> scBeta): \((\sin \beta, \cos \beta)\)
        
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
    def sum(fieldSinCos: 'FieldSinCos'[_sum__S], fieldSinCos2: 'FieldSinCos'[_sum__S]) -> 'FieldSinCos'[_sum__S]:
        """
            Compute sine and cosine of angles sum.
        
            Parameters:
                scAlpha (:class:`~org.hipparchus.util.FieldSinCos`<S> scAlpha): \((\sin \alpha, \cos \alpha)\)
                scBeta (:class:`~org.hipparchus.util.FieldSinCos`<S> scBeta): \((\sin \beta, \cos \beta)\)
        
            Returns:
                \((\sin \alpha+\beta, \cos \alpha+\beta)\)
        
            Since:
                1.8
        
        
        """
        ...

_FieldSinhCosh__T = typing.TypeVar('_FieldSinhCosh__T')  # <T>
class FieldSinhCosh(typing.Generic[_FieldSinhCosh__T]):
    """
    public class FieldSinhCosh<T> extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Holder for both hyperbolic sine and hyperbolic cosine values.
    
        This class is a simple container, it does not provide any computational method.
    
        Since:
            2.0
    
        Also see:
            :meth:`~org.hipparchus.util.FastMath.sinhCosh`
    """
    def __init__(self, t: _FieldSinhCosh__T, t2: _FieldSinhCosh__T): ...
    def cosh(self) -> _FieldSinhCosh__T:
        """
            Get the value of the hyperbolic cosine.
        
            Returns:
                value of the hyperbolic cosine
        
        
        """
        ...
    _difference__S = typing.TypeVar('_difference__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
    @staticmethod
    def difference(fieldSinhCosh: 'FieldSinhCosh'[_difference__S], fieldSinhCosh2: 'FieldSinhCosh'[_difference__S]) -> 'FieldSinhCosh'[_difference__S]:
        """
            Compute hyperbolic sine and hyperbolic cosine of angles difference.
        
            Parameters:
                schAlpha (:class:`~org.hipparchus.util.FieldSinhCosh`<S> schAlpha): \((\sinh \alpha, \cosh \alpha)\)
                schBeta (:class:`~org.hipparchus.util.FieldSinhCosh`<S> schBeta): \((\sinh \beta, \cosh \beta)\)
        
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
    def sum(fieldSinhCosh: 'FieldSinhCosh'[_sum__S], fieldSinhCosh2: 'FieldSinhCosh'[_sum__S]) -> 'FieldSinhCosh'[_sum__S]:
        """
            Compute hyperbolic sine and hyperbolic cosine of angles sum.
        
            Parameters:
                schAlpha (:class:`~org.hipparchus.util.FieldSinhCosh`<S> schAlpha): \((\sinh \alpha, \cosh \alpha)\)
                schBeta (:class:`~org.hipparchus.util.FieldSinhCosh`<S> schBeta): \((\sinh \beta, \cosh \beta)\)
        
            Returns:
                \((\sinh \alpha+\beta, \cosh \alpha+\beta)\)
        
        
        """
        ...

_FieldTuple__T = typing.TypeVar('_FieldTuple__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTuple(org.hipparchus.CalculusFieldElement['FieldTuple'[_FieldTuple__T]], typing.Generic[_FieldTuple__T]):
    """
    public class FieldTuple<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.util.FieldTuple`<T>>
    
        This class allows to perform the same computation of all components of a Tuple at once.
    
        Since:
            1.2
    """
    def __init__(self, *t: _FieldTuple__T): ...
    def abs(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def acos(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def acosh(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def add(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def add(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def asin(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def asinh(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def atan(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def atan2(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def atanh(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def cbrt(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def ceil(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def copySign(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def copySign(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def cos(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def cosh(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def divide(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def divide(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def exp(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def expm1(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def floor(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def getComponent(self, int: int) -> _FieldTuple__T:
        """
            Get one component of the tuple.
        
            Parameters:
                index (int): index of the component, between 0 and :meth:`~org.hipparchus.util.FieldTuple.getDimension` - 1
        
            Returns:
                value of the component
        
        
        """
        ...
    def getComponents(self) -> typing.List[_FieldTuple__T]:
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
    def getField(self) -> org.hipparchus.Field['FieldTuple'[_FieldTuple__T]]: ...
    def getPi(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def hypot(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldTuple: 'FieldTuple'[_FieldTuple__T], double2: float, fieldTuple2: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldTuple: 'FieldTuple'[_FieldTuple__T], double2: float, fieldTuple2: 'FieldTuple'[_FieldTuple__T], double3: float, fieldTuple3: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldTuple: 'FieldTuple'[_FieldTuple__T], double2: float, fieldTuple2: 'FieldTuple'[_FieldTuple__T], double3: float, fieldTuple3: 'FieldTuple'[_FieldTuple__T], double4: float, fieldTuple4: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], fieldTupleArray: typing.List['FieldTuple'[_FieldTuple__T]]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, fieldTuple: 'FieldTuple'[_FieldTuple__T], fieldTuple2: 'FieldTuple'[_FieldTuple__T], fieldTuple3: 'FieldTuple'[_FieldTuple__T], fieldTuple4: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, fieldTuple: 'FieldTuple'[_FieldTuple__T], fieldTuple2: 'FieldTuple'[_FieldTuple__T], fieldTuple3: 'FieldTuple'[_FieldTuple__T], fieldTuple4: 'FieldTuple'[_FieldTuple__T], fieldTuple5: 'FieldTuple'[_FieldTuple__T], fieldTuple6: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, fieldTuple: 'FieldTuple'[_FieldTuple__T], fieldTuple2: 'FieldTuple'[_FieldTuple__T], fieldTuple3: 'FieldTuple'[_FieldTuple__T], fieldTuple4: 'FieldTuple'[_FieldTuple__T], fieldTuple5: 'FieldTuple'[_FieldTuple__T], fieldTuple6: 'FieldTuple'[_FieldTuple__T], fieldTuple7: 'FieldTuple'[_FieldTuple__T], fieldTuple8: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def linearCombination(self, fieldTupleArray: typing.List['FieldTuple'[_FieldTuple__T]], fieldTupleArray2: typing.List['FieldTuple'[_FieldTuple__T]]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def log(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def log10(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def log1p(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def multiply(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def negate(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def newInstance(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def pow(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def pow(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def reciprocal(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def remainder(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def remainder(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def rint(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def rootN(self, int: int) -> 'FieldTuple'[_FieldTuple__T]: ...
    def scalb(self, int: int) -> 'FieldTuple'[_FieldTuple__T]: ...
    def sign(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def sin(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def sinCos(self) -> FieldSinCos['FieldTuple'[_FieldTuple__T]]: ...
    def sinh(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def sinhCosh(self) -> FieldSinhCosh['FieldTuple'[_FieldTuple__T]]: ...
    def sqrt(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def subtract(self, double: float) -> 'FieldTuple'[_FieldTuple__T]: ...
    @typing.overload
    def subtract(self, fieldTuple: 'FieldTuple'[_FieldTuple__T]) -> 'FieldTuple'[_FieldTuple__T]: ...
    def tan(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def tanh(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def toDegrees(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def toRadians(self) -> 'FieldTuple'[_FieldTuple__T]: ...
    def ulp(self) -> 'FieldTuple'[_FieldTuple__T]: ...

class Incrementor:
    """
    public class Incrementor extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility that increments a counter until a maximum is reached, at which point, the instance will by default throw a
        :class:`~org.hipparchus.exception.MathIllegalStateException`. However, the user is able to override this behaviour by
        defining a custom :class:`~org.hipparchus.util.Incrementor.MaxCountExceededCallback`, in order to e.g. select which
        exception must be thrown.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, maxCountExceededCallback: 'Incrementor.MaxCountExceededCallback'): ...
    @typing.overload
    def canIncrement(self) -> bool:
        """
            Checks whether incrementing the counter :code:`nTimes` is allowed.
        
            Returns:
                :code:`false` if calling :meth:`~org.hipparchus.util.Incrementor.increment` will trigger a
                :code:`MathIllegalStateException`, :code:`true` otherwise.
        
        """
        ...
    @typing.overload
    def canIncrement(self, int: int) -> bool:
        """
            Checks whether incrementing the counter several times is allowed.
        
            Parameters:
                nTimes (int): Number of increments.
        
            Returns:
                :code:`false` if calling :meth:`~org.hipparchus.util.Incrementor.increment` would call the
                :class:`~org.hipparchus.util.Incrementor.MaxCountExceededCallback` :code:`true` otherwise.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`nTimes` is negative.
        
        
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
            Adds the increment value to the current iteration count. At counter exhaustion, this method will call the
            :meth:`~org.hipparchus.util.Incrementor.MaxCountExceededCallback.trigger` method of the callback object passed to the
            :meth:`~org.hipparchus.util.Incrementor.withCallback` method.
        
            Also see:
                :meth:`~org.hipparchus.util.Incrementor.increment`
        
        
        """
        ...
    @typing.overload
    def increment(self, int: int) -> None:
        """
            Performs multiple increments.
        
            Parameters:
                nTimes (int): Number of increments.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`nTimes` is negative.
        
            Also see:
                :meth:`~org.hipparchus.util.Incrementor.increment`
        
        """
        ...
    def reset(self) -> None:
        """
            Resets the counter to 0.
        
        """
        ...
    def withCallback(self, maxCountExceededCallback: 'Incrementor.MaxCountExceededCallback') -> 'Incrementor':
        """
            Creates a new instance with a given callback. The counter is reset to 0.
        
            Parameters:
                cb (:class:`~org.hipparchus.util.Incrementor.MaxCountExceededCallback`): Callback to be called at counter exhaustion.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withCount(self, int: int) -> 'Incrementor':
        """
            Creates a new instance and set the counter to the given value.
        
            Parameters:
                value (int): Value of the counter.
        
            Returns:
                a new instance.
        
        
        """
        ...
    def withMaximalCount(self, int: int) -> 'Incrementor':
        """
            Creates a new instance with a given maximal count. The counter is reset to 0.
        
            Parameters:
                max (int): Maximal count.
        
            Returns:
                a new instance.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`max` is negative.
        
        
        """
        ...
    class MaxCountExceededCallback:
        def trigger(self, int: int) -> None: ...

class IterationEvent(java.util.EventObject):
    """
    public class IterationEvent extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.EventObject?is`
    
        The root class from which all events occurring while running an :class:`~org.hipparchus.util.IterationManager` should be
        derived.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, object: typing.Any, int: int): ...
    def getIterations(self) -> int:
        """
            Returns the number of iterations performed at the time :code:`this` event is created.
        
            Returns:
                the number of iterations performed
        
        
        """
        ...

class IterationListener(java.util.EventListener):
    """
    public interface IterationListener extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.EventListener?is`
    
        The listener interface for receiving events occurring in an iterative algorithm.
    """
    def initializationPerformed(self, iterationEvent: IterationEvent) -> None:
        """
            Invoked after completion of the initial phase of the iterative algorithm (prior to the main iteration loop).
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
        """
        ...
    def iterationPerformed(self, iterationEvent: IterationEvent) -> None:
        """
            Invoked each time an iteration is completed (in the main iteration loop).
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
        """
        ...
    def iterationStarted(self, iterationEvent: IterationEvent) -> None:
        """
            Invoked each time a new iteration is completed (in the main iteration loop).
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
        """
        ...
    def terminationPerformed(self, iterationEvent: IterationEvent) -> None:
        """
            Invoked after completion of the operations which occur after breaking out of the main iteration loop.
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
        """
        ...

class IterationManager:
    """
    public class IterationManager extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This abstract class provides a general framework for managing iterative algorithms. The maximum number of iterations can
        be set, and methods are provided to monitor the current iteration count. A lightweight event framework is also provided.
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, maxCountExceededCallback: Incrementor.MaxCountExceededCallback): ...
    def addIterationListener(self, iterationListener: IterationListener) -> None:
        """
            Attaches a listener to this manager.
        
            Parameters:
                listener (:class:`~org.hipparchus.util.IterationListener`): A :code:`IterationListener` object.
        
        
        """
        ...
    def fireInitializationEvent(self, iterationEvent: IterationEvent) -> None:
        """
            Informs all registered listeners that the initial phase (prior to the main iteration loop) has been completed.
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
        """
        ...
    def fireIterationPerformedEvent(self, iterationEvent: IterationEvent) -> None:
        """
            Informs all registered listeners that a new iteration (in the main iteration loop) has been performed.
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
        """
        ...
    def fireIterationStartedEvent(self, iterationEvent: IterationEvent) -> None:
        """
            Informs all registered listeners that a new iteration (in the main iteration loop) has been started.
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
        """
        ...
    def fireTerminationEvent(self, iterationEvent: IterationEvent) -> None:
        """
            Informs all registered listeners that the final phase (post-iterations) has been completed.
        
            Parameters:
                e (:class:`~org.hipparchus.util.IterationEvent`): The :class:`~org.hipparchus.util.IterationEvent` object.
        
        
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
    def incrementIterationCount(self) -> None: ...
    def removeIterationListener(self, iterationListener: IterationListener) -> None:
        """
            Removes the specified iteration listener from the list of listeners currently attached to :code:`this` object.
            Attempting to remove a listener which was *not* previously registered does not cause any error.
        
            Parameters:
                listener (:class:`~org.hipparchus.util.IterationListener`): The :class:`~org.hipparchus.util.IterationListener` to be removed.
        
        
        """
        ...
    def resetIterationCount(self) -> None:
        """
            Sets the iteration count to 0. This method must be called during the initial phase.
        
        """
        ...

class KthSelector(java.io.Serializable):
    """
    public class KthSelector extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        A Simple K :sup:`th` selector implementation to pick up the K :sup:`th` ordered element from a work array containing the
        input numbers.
    
        Also see:
            :meth:`~serialized`
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
    def select(self, doubleArray: typing.List[float], intArray: typing.List[int], int2: int) -> float:
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
    public class MathArrays extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Arrays utilities.
    """
    _buildArray_0__T = typing.TypeVar('_buildArray_0__T', bound=org.hipparchus.FieldElement)  # <T>
    _buildArray_1__T = typing.TypeVar('_buildArray_1__T', bound=org.hipparchus.FieldElement)  # <T>
    _buildArray_2__T = typing.TypeVar('_buildArray_2__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def buildArray(field: org.hipparchus.Field[_buildArray_0__T], int: int) -> typing.List[_buildArray_0__T]:
        """
            Build an array of elements.
        
            Arrays are filled with :code:`field.getZero()`
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field to which array elements belong
                length (int): of the array
        
            Returns:
                a new array
        
            Build a double dimension array of elements.
        
            Arrays are filled with :code:`field.getZero()`
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field to which array elements belong
                rows (int): number of rows in the array
                columns (int): number of columns (may be negative to build partial arrays in the same way :code:`new Field[rows][]` works)
        
            Returns:
                a new array
        
            Build a triple dimension array of elements.
        
            Arrays are filled with :code:`field.getZero()`
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field to which array elements belong
                l1 (int): number of elements along first dimension
                l2 (int): number of elements along second dimension
                l3 (int): number of elements along third dimension (may be negative to build partial arrays in the same way :code:`new
                    Field[l1][l2][]` works)
        
            Returns:
                a new array
        
            Since:
                1.4
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def buildArray(field: org.hipparchus.Field[_buildArray_1__T], int: int, int2: int) -> typing.List[typing.List[_buildArray_1__T]]: ...
    @typing.overload
    @staticmethod
    def buildArray(field: org.hipparchus.Field[_buildArray_2__T], int: int, int2: int, int3: int) -> typing.List[typing.List[typing.List[_buildArray_2__T]]]: ...
    _checkEqualLength_2__T = typing.TypeVar('_checkEqualLength_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _checkEqualLength_5__T = typing.TypeVar('_checkEqualLength_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def checkEqualLength(doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> bool:
        """
            Check that both arrays have the same length.
        
            Parameters:
                a (double[]): Array.
                b (double[]): Array.
                abort (boolean): Whether to throw an exception if the check fails.
        
            Returns:
                :code:`true` if the arrays have the same length.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the lengths differ and :code:`abort` is :code:`true`.
        
            Check that both arrays have the same length.
        
            Parameters:
                a (int[]): Array.
                b (int[]): Array.
                abort (boolean): Whether to throw an exception if the check fails.
        
            Returns:
                :code:`true` if the arrays have the same length.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the lengths differ and :code:`abort` is :code:`true`.
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkEqualLength(intArray: typing.List[int], intArray2: typing.List[int], boolean: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(tArray: typing.List[_checkEqualLength_2__T], tArray2: typing.List[_checkEqualLength_2__T], boolean: bool) -> bool:
        """
            Check that both arrays have the same length.
        
            Parameters:
                a (T[]): Array.
                b (T[]): Array.
                abort (boolean): Whether to throw an exception if the check fails.
        
            Returns:
                :code:`true` if the arrays have the same length.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the lengths differ and :code:`abort` is :code:`true`.
        
            Since:
                1.5
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkEqualLength(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None:
        """
            Check that both arrays have the same length.
        
            Parameters:
                a (double[]): Array.
                b (double[]): Array.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the lengths differ.
        
            Check that both arrays have the same length.
        
            Parameters:
                a (int[]): Array.
                b (int[]): Array.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the lengths differ.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkEqualLength(intArray: typing.List[int], intArray2: typing.List[int]) -> None: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(tArray: typing.List[_checkEqualLength_5__T], tArray2: typing.List[_checkEqualLength_5__T]) -> None:
        """
            Check that both arrays have the same length.
        
            Parameters:
                a (T[]): Array.
                b (T[]): Array.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the lengths differ.
        
            Since:
                1.5
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkNonNegative(longArray: typing.List[int]) -> None: ...
    @typing.overload
    @staticmethod
    def checkNonNegative(longArray: typing.List[typing.List[int]]) -> None: ...
    @staticmethod
    def checkNotNaN(doubleArray: typing.List[float]) -> None: ...
    _checkOrder_1__T = typing.TypeVar('_checkOrder_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _checkOrder_4__T = typing.TypeVar('_checkOrder_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _checkOrder_5__T = typing.TypeVar('_checkOrder_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def checkOrder(doubleArray: typing.List[float], orderDirection: 'MathArrays.OrderDirection', boolean: bool, boolean2: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkOrder(tArray: typing.List[_checkOrder_1__T], orderDirection: 'MathArrays.OrderDirection', boolean: bool, boolean2: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkOrder(doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    @staticmethod
    def checkOrder(doubleArray: typing.List[float], orderDirection: 'MathArrays.OrderDirection', boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def checkOrder(tArray: typing.List[_checkOrder_4__T]) -> None: ...
    @typing.overload
    @staticmethod
    def checkOrder(tArray: typing.List[_checkOrder_5__T], orderDirection: 'MathArrays.OrderDirection', boolean: bool) -> None: ...
    @staticmethod
    def checkPositive(doubleArray: typing.List[float]) -> None: ...
    @staticmethod
    def checkRectangular(longArray: typing.List[typing.List[int]]) -> None: ...
    @staticmethod
    def concatenate(*doubleArray: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def convolve(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def cosAngle(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float:
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
    def distance(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def distance(intArray: typing.List[int], intArray2: typing.List[int]) -> float: ...
    @typing.overload
    @staticmethod
    def distance1(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def distance1(intArray: typing.List[int], intArray2: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def distanceInf(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    @staticmethod
    def distanceInf(intArray: typing.List[int], intArray2: typing.List[int]) -> int: ...
    @staticmethod
    def ebeAdd(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def ebeDivide(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def ebeMultiply(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def ebeSubtract(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(byteArray: typing.List[int], byteArray2: typing.List[int]) -> bool:
        """
            Returns true iff both arguments are null or have same dimensions and all their elements are equal as defined by
            :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (float[]): first array
                y (float[]): second array
        
            Returns:
                true if the values are both null or have same dimension and equal elements.
        
            Returns :code:`true` iff both arguments are :code:`null` or have same dimensions and all their elements are equal as
            defined by :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (double[]): First array.
                y (double[]): Second array.
        
            Returns:
                :code:`true` if the values are both :code:`null` or have same dimension and equal elements.
        
            Returns :code:`true` if both arguments are :code:`null` or have same dimensions and all their elements are equals.
        
            Parameters:
                x (long[]): First array.
                y (long[]): Second array.
        
            Returns:
                :code:`true` if the values are both :code:`null` or have same dimension and equal elements.
        
            Returns :code:`true` if both arguments are :code:`null` or have same dimensions and all their elements are equals.
        
            Parameters:
                x (int[]): First array.
                y (int[]): Second array.
        
            Returns:
                :code:`true` if the values are both :code:`null` or have same dimension and equal elements.
        
            Returns :code:`true` if both arguments are :code:`null` or have same dimensions and all their elements are equals.
        
            Parameters:
                x (byte[]): First array.
                y (byte[]): Second array.
        
            Returns:
                :code:`true` if the values are both :code:`null` or have same dimension and equal elements.
        
            Returns :code:`true` if both arguments are :code:`null` or have same dimensions and all their elements are equals.
        
            Parameters:
                x (short[]): First array.
                y (short[]): Second array.
        
            Returns:
                :code:`true` if the values are both :code:`null` or have same dimension and equal elements.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(floatArray: typing.List[float], floatArray2: typing.List[float]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(intArray: typing.List[int], intArray2: typing.List[int]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(longArray: typing.List[int], longArray2: typing.List[int]) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(shortArray: typing.List[int], shortArray2: typing.List[int]) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> bool:
        """
            Returns true iff both arguments are null or have same dimensions and all their elements are equal as defined by
            :meth:`~org.hipparchus.util.Precision.equalsIncludingNaN`.
        
            Parameters:
                x (float[]): first array
                y (float[]): second array
        
            Returns:
                true if the values are both null or have same dimension and equal elements
        
            Returns :code:`true` iff both arguments are :code:`null` or have same dimensions and all their elements are equal as
            defined by :meth:`~org.hipparchus.util.Precision.equalsIncludingNaN`.
        
            Parameters:
                x (double[]): First array.
                y (double[]): Second array.
        
            Returns:
                :code:`true` if the values are both :code:`null` or have same dimension and equal elements.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(floatArray: typing.List[float], floatArray2: typing.List[float]) -> bool: ...
    _isMonotonic_1__T = typing.TypeVar('_isMonotonic_1__T', bound=java.lang.Comparable)  # <T>
    @typing.overload
    @staticmethod
    def isMonotonic(doubleArray: typing.List[float], orderDirection: 'MathArrays.OrderDirection', boolean: bool) -> bool:
        """
            Check that an array is monotonically increasing or decreasing.
        
            Parameters:
                val (double[]): Values.
                dir (:class:`~org.hipparchus.util.MathArrays.OrderDirection`): Ordering direction.
                strict (boolean): Whether the order should be strict.
        
            Returns:
                :code:`true` if sorted, :code:`false` otherwise.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isMonotonic(tArray: typing.List[_isMonotonic_1__T], orderDirection: 'MathArrays.OrderDirection', boolean: bool) -> bool:
        """
            Check that an array is monotonically increasing or decreasing.
        
            Parameters:
                val (T[]): Values.
                dir (:class:`~org.hipparchus.util.MathArrays.OrderDirection`): Ordering direction.
                strict (boolean): Whether the order should be strict.
        
            Returns:
                :code:`true` if sorted, :code:`false` otherwise.
        
        """
        ...
    @typing.overload
    @staticmethod
    def linearCombination(double: float, double2: float, double3: float, double4: float) -> float:
        """
            Compute a linear combination accurately.
        
            This method computes a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` to high accuracy. It does so by using specific
            multiplication and addition algorithms to preserve accuracy and reduce cancellation effects. It is based on the 2005
            paper ` Accurate Sum and Dot Product <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.1547>` by Takeshi Ogita,
            Siegfried M. Rump, and Shin'ichi Oishi published in SIAM J. Sci. Comput.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (double): second factor of the first term
                a2 (double): first factor of the second term
                b2 (double): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.util.MathArrays.linearCombination`, :meth:`~org.hipparchus.util.MathArrays.linearCombination`
        
            Compute a linear combination accurately.
        
            This method computes a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` to high accuracy. It
            does so by using specific multiplication and addition algorithms to preserve accuracy and reduce cancellation effects.
            It is based on the 2005 paper ` Accurate Sum and Dot Product
            <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.1547>` by Takeshi Ogita, Siegfried M. Rump, and Shin'ichi
            Oishi published in SIAM J. Sci. Comput.
        
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
                :meth:`~org.hipparchus.util.MathArrays.linearCombination`, :meth:`~org.hipparchus.util.MathArrays.linearCombination`
        
            Compute a linear combination accurately.
        
            This method computes a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b
            :sub:`4` to high accuracy. It does so by using specific multiplication and addition algorithms to preserve accuracy and
            reduce cancellation effects. It is based on the 2005 paper ` Accurate Sum and Dot Product
            <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.2.1547>` by Takeshi Ogita, Siegfried M. Rump, and Shin'ichi
            Oishi published in SIAM J. Sci. Comput.
        
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
                :meth:`~org.hipparchus.util.MathArrays.linearCombination`, :meth:`~org.hipparchus.util.MathArrays.linearCombination`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def linearCombination(double: float, double2: float, double3: float, double4: float, double5: float, double6: float) -> float: ...
    @typing.overload
    @staticmethod
    def linearCombination(double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float) -> float: ...
    @typing.overload
    @staticmethod
    def linearCombination(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
    @staticmethod
    def natural(int: int) -> typing.List[int]:
        """
            Returns an array representing the natural number :code:`n`.
        
            Parameters:
                n (int): Natural number.
        
            Returns:
                an array whose entries are the numbers 0, 1, ..., :code:`n`-1. If :code:`n == 0`, the returned array is empty.
        
        
        """
        ...
    @staticmethod
    def normalizeArray(doubleArray: typing.List[float], double2: float) -> typing.List[float]: ...
    @staticmethod
    def safeNorm(doubleArray: typing.List[float]) -> float:
        """
            Returns the Cartesian norm (2-norm), handling both overflow and underflow. Translation of the minpack enorm subroutine.
        
            The redistribution policy for MINPACK is available `here <http://www.netlib.org/minpack/disclaimer>`, for convenience,
            it is reproduced below.
        
                Minpack Copyright Notice (1999) University of Chicago. All rights reserved
        
                Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
                following conditions are met:
        
                  1.  Redistributions of source code must retain the above copyright notice, this list of conditions and the following
                    disclaimer.
                  2.  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
                    disclaimer in the documentation and/or other materials provided with the distribution.
                  3.  The end-user documentation included with the redistribution, if any, must include the following acknowledgment:
                    :code:`This product includes software developed by the University of Chicago, as Operator of Argonne National
                    Laboratory.` Alternately, this acknowledgment may appear in the software itself, if and wherever such third-party
                    acknowledgments normally appear.
                  4.  **WARRANTY DISCLAIMER. THE SOFTWARE IS SUPPLIED "AS IS" WITHOUT WARRANTY OF ANY KIND. THE COPYRIGHT HOLDER, THE UNITED
                    STATES, THE UNITED STATES DEPARTMENT OF ENERGY, AND THEIR EMPLOYEES: (1) DISCLAIM ANY WARRANTIES, EXPRESS OR IMPLIED,
                    INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR
                    NON-INFRINGEMENT, (2) DO NOT ASSUME ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS
                    OF THE SOFTWARE, (3) DO NOT REPRESENT THAT USE OF THE SOFTWARE WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS, (4) DO NOT
                    WARRANT THAT THE SOFTWARE WILL FUNCTION UNINTERRUPTED, THAT IT IS ERROR-FREE OR THAT ANY ERRORS WILL BE CORRECTED.**
                  5.  **LIMITATION OF LIABILITY. IN NO EVENT WILL THE COPYRIGHT HOLDER, THE UNITED STATES, THE UNITED STATES DEPARTMENT OF
                    ENERGY, OR THEIR EMPLOYEES: BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL OR PUNITIVE DAMAGES OF ANY
                    KIND OR NATURE, INCLUDING BUT NOT LIMITED TO LOSS OF PROFITS OR LOSS OF DATA, FOR ANY REASON WHATSOEVER, WHETHER SUCH
                    LIABILITY IS ASSERTED ON THE BASIS OF CONTRACT, TORT (INCLUDING NEGLIGENCE OR STRICT LIABILITY), OR OTHERWISE, EVEN IF
                    ANY OF SAID PARTIES HAS BEEN WARNED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGES.**
        
        
            Parameters:
                v (double[]): Vector of doubles.
        
            Returns:
                the 2-norm of the vector.
        
        
        """
        ...
    @staticmethod
    def scale(double: float, doubleArray: typing.List[float]) -> typing.List[float]:
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
    def scaleInPlace(double: float, doubleArray: typing.List[float]) -> None:
        """
            Multiply each element of an array by a value.
        
            The array is modified in place (no copy is created).
        
            Parameters:
                arr (double): Array to scale
                val (double[]): Scalar
        
        
        """
        ...
    @staticmethod
    def sequence(int: int, int2: int, int3: int) -> typing.List[int]:
        """
            Returns an array of :code:`size` integers starting at :code:`start`, skipping :code:`stride` numbers.
        
            Parameters:
                size (int): Natural number.
                start (int): Natural number.
                stride (int): Natural number.
        
            Returns:
                an array whose entries are the numbers :code:`start, start + stride, ..., start + (size - 1) * stride`. If :code:`size
                == 0`, the returned array is empty.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int]) -> None:
        """
            Shuffle the entries of the given array.
        
            Parameters:
                list (int[]): Array whose entries will be shuffled (in-place).
        
            Also see:
                :meth:`~org.hipparchus.util.MathArrays.shuffle`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int], int2: int, position: 'MathArrays.Position') -> None:
        """
            Shuffle the entries of the given array. The :code:`start` and :code:`pos` parameters select which portion of the array
            is randomized and which is left untouched.
        
            Parameters:
                list (int[]): Array whose entries will be shuffled (in-place).
                start (int): Index at which shuffling begins.
                pos (:class:`~org.hipparchus.util.MathArrays.Position`): Shuffling is performed for index positions between :code:`start` and either the end (if
                    :meth:`~org.hipparchus.util.MathArrays.Position.TAIL`) or the beginning (if
                    :meth:`~org.hipparchus.util.MathArrays.Position.HEAD`) of the array.
        
            Also see:
                :meth:`~org.hipparchus.util.MathArrays.shuffle`
        
            Shuffle the entries of the given array, using the :meth:`~org.hipparchus.util.https:.en.wikipedia.org.wiki.Fisher`
            algorithm. The :code:`start` and :code:`pos` parameters select which portion of the array is randomized and which is
            left untouched.
        
            Parameters:
                list (int[]): Array whose entries will be shuffled (in-place).
                start (int): Index at which shuffling begins.
                pos (:class:`~org.hipparchus.util.MathArrays.Position`): Shuffling is performed for index positions between :code:`start` and either the end (if
                    :meth:`~org.hipparchus.util.MathArrays.Position.TAIL`) or the beginning (if
                    :meth:`~org.hipparchus.util.MathArrays.Position.HEAD`) of the array.
                rng (:class:`~org.hipparchus.random.RandomGenerator`): Random number generator.
        
        """
        ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int], int2: int, position: 'MathArrays.Position', randomGenerator: org.hipparchus.random.RandomGenerator) -> None: ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int], randomGenerator: org.hipparchus.random.RandomGenerator) -> None:
        """
            Shuffle the entries of the given array.
        
            Parameters:
                list (int[]): Array whose entries will be shuffled (in-place).
                rng (:class:`~org.hipparchus.random.RandomGenerator`): Random number generator.
        
            Also see:
                :meth:`~org.hipparchus.util.MathArrays.shuffle`
        
        """
        ...
    @typing.overload
    @staticmethod
    def sortInPlace(doubleArray: typing.List[float], *doubleArray2: typing.List[float]) -> None: ...
    @typing.overload
    @staticmethod
    def sortInPlace(doubleArray: typing.List[float], orderDirection: 'MathArrays.OrderDirection', *doubleArray2: typing.List[float]) -> None: ...
    @staticmethod
    def unique(doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Returns an array consisting of the unique values in :code:`data`. The return array is sorted in descending order. Empty
            arrays are allowed, but null arrays result in NullPointerException. Infinities are allowed. NaN values are allowed with
            maximum sort order - i.e., if there are NaN values in :code:`data`, :code:`Double.NaN` will be the first element of the
            output array, even if the array also contains :code:`Double.POSITIVE_INFINITY`.
        
            Parameters:
                data (double[]): array to scan
        
            Returns:
                descending list of values included in the input array
        
            Raises:
                :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if data is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def verifyValues(doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, int2: int) -> bool: ...
    @typing.overload
    @staticmethod
    def verifyValues(doubleArray: typing.List[float], doubleArray2: typing.List[float], int: int, int2: int, boolean: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def verifyValues(doubleArray: typing.List[float], int: int, int2: int) -> bool: ...
    @typing.overload
    @staticmethod
    def verifyValues(doubleArray: typing.List[float], int: int, int2: int, boolean: bool) -> bool: ...
    class Function:
        @typing.overload
        def evaluate(self, doubleArray: typing.List[float]) -> float: ...
        @typing.overload
        def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
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
        def values() -> typing.List['MathArrays.OrderDirection']: ...
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
        def values() -> typing.List['MathArrays.Position']: ...

_MathUtils__FieldSumAndResidual__T = typing.TypeVar('_MathUtils__FieldSumAndResidual__T', bound=org.hipparchus.FieldElement)  # <T>
class MathUtils:
    """
    public final class MathUtils extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Miscellaneous utility functions.
    
        Also see:
            :class:`~org.hipparchus.util.ArithmeticUtils`, :class:`~org.hipparchus.util.Precision`,
            :class:`~org.hipparchus.util.MathArrays`
    """
    TWO_PI: typing.ClassVar[float] = ...
    """
    public static final double TWO_PI
    
        \(2\pi\)
    
        Also see:
            :meth:`~constant`
    
    
    """
    PI_SQUARED: typing.ClassVar[float] = ...
    """
    public static final double PI_SQUARED
    
        \(\pi^2\)
    
        Also see:
            :meth:`~constant`
    
    
    """
    SEMI_PI: typing.ClassVar[float] = ...
    """
    public static final double SEMI_PI
    
        \(\pi/2\).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def checkDimension(int: int, int2: int) -> None:
        """
            Checks that the given dimensions match.
        
            Parameters:
                dimension (int): the first dimension.
                otherDimension (int): the second dimension.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if length != otherLength.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkFinite(double: float) -> None: ...
    @typing.overload
    @staticmethod
    def checkFinite(doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    @staticmethod
    def checkNotNull(object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkNotNull(object: typing.Any, localizable: org.hipparchus.exception.Localizable, *object2: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkRangeInclusive(double: float, double2: float, double3: float) -> None:
        """
            Checks that the given value is strictly within the range [lo, hi].
        
            Parameters:
                value (long): value to be checked.
                lo (long): the lower bound (inclusive).
                hi (long): the upper bound (inclusive).
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`value` is strictly outside [lo, hi].
        
            Checks that the given value is strictly within the range [lo, hi].
        
            Parameters:
                value (double): value to be checked.
                lo (double): the lower bound (inclusive).
                hi (double): the upper bound (inclusive).
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`value` is strictly outside [lo, hi].
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkRangeInclusive(long: int, long2: int, long3: int) -> None: ...
    @typing.overload
    @staticmethod
    def copySign(byte: int, byte2: int) -> int: ...
    @typing.overload
    @staticmethod
    def copySign(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def copySign(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def copySign(short: int, short2: int) -> int: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
            Returns :code:`true` if the values are equal according to semantics of
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Parameters:
                x (double): Value
                y (double): Value
        
            Returns:
                :code:`Double.valueOf(x).equals(Double.valueOf(y))`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def hash(double: float) -> int:
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
    def hash(doubleArray: typing.List[float]) -> int: ...
    _max__T = typing.TypeVar('_max__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def max(t: _max__T, t2: _max__T) -> _max__T:
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
    def min(t: _min__T, t2: _min__T) -> _min__T:
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
    def normalizeAngle(double: float, double2: float) -> float:
        """
            Normalize an angle in a 2π wide interval around a center value.
        
            This method has three main uses:
        
              - normalize an angle between 0 and 2π:
        
        
        :code:`a = MathUtils.normalizeAngle(a, FastMath.PI);`
              - normalize an angle between -π and +π
        
        
        :code:`a = MathUtils.normalizeAngle(a, 0.0);`
              - compute the angle between two defining angular positions:
        
        
        :code:`angle = MathUtils.normalizeAngle(end, start) - start;`
        
        
            Note that due to numerical accuracy and since π cannot be represented exactly, the result interval is *closed*, it
            cannot be half-closed as would be more satisfactory in a purely mathematical view.
        
            Parameters:
                a (double): angle to normalize
                center (double): center of the desired 2π interval for the result
        
            Returns:
                a-2kπ with integer k and center-π <= a-2kπ <= center+π
        
        """
        ...
    @typing.overload
    @staticmethod
    def normalizeAngle(t: _normalizeAngle_1__T, t2: _normalizeAngle_1__T) -> _normalizeAngle_1__T:
        """
            Normalize an angle in a 2π wide interval around a center value.
        
            This method has three main uses:
        
              - normalize an angle between 0 and 2π:
        
        
        :code:`a = MathUtils.normalizeAngle(a, FastMath.PI);`
              - normalize an angle between -π and +π
        
        
        :code:`a = MathUtils.normalizeAngle(a, zero);`
              - compute the angle between two defining angular positions:
        
        
        :code:`angle = MathUtils.normalizeAngle(end, start).subtract(start);`
        
        
            Note that due to numerical accuracy and since π cannot be represented exactly, the result interval is *closed*, it
            cannot be half-closed as would be more satisfactory in a purely mathematical view.
        
            Parameters:
                a (T): angle to normalize
                center (T): center of the desired 2π interval for the result
        
            Returns:
                a-2kπ with integer k and center-π <= a-2kπ <= center+π
        
        
        """
        ...
    @staticmethod
    def reduce(double: float, double2: float, double3: float) -> float:
        """
        
            Reduce :code:`|a - offset|` to the primary interval :code:`[0, |period|)`.
        
            Specifically, the value returned is
        
        
            :code:`a - |period| * floor((a - offset) / |period|) - offset`.
        
            If any of the parameters are :code:`NaN` or infinite, the result is :code:`NaN`.
        
            Parameters:
                a (double): Value to reduce.
                period (double): Period.
                offset (double): Value that will be mapped to :code:`0`.
        
            Returns:
                the value, within the interval :code:`[0 |period|)`, that corresponds to :code:`a`.
        
        
        """
        ...
    _twoSum_0__T = typing.TypeVar('_twoSum_0__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def twoSum(t: _twoSum_0__T, t2: _twoSum_0__T) -> 'MathUtils.FieldSumAndResidual'[_twoSum_0__T]:
        """
            Sums :code:`a` and :code:`b` using Møller's 2Sum algorithm.
        
            References:
        
              - Møller, Ole. "Quasi double-precision in floating point addition." BIT 5, 37–50 (1965).
              - Shewchuk, Richard J. "Adaptive Precision Floating-Point Arithmetic and Fast Robust Geometric Predicates." Discrete &
                Computational Geometry 18, 305–363 (1997).
              - :class:`~org.hipparchus.util.https:.en.wikipedia.org.wiki.2Sum`
        
        
            Parameters:
                a (T): first summand
                b (T): second summand
        
            Returns:
                sum and residual error in the sum
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def twoSum(double: float, double2: float) -> 'MathUtils.SumAndResidual':
        """
            Sums :code:`a` and :code:`b` using Møller's 2Sum algorithm.
        
            References:
        
              - Møller, Ole. "Quasi double-precision in floating point addition." BIT 5, 37–50 (1965).
              - Shewchuk, Richard J. "Adaptive Precision Floating-Point Arithmetic and Fast Robust Geometric Predicates." Discrete &
                Computational Geometry 18, 305–363 (1997).
              - :class:`~org.hipparchus.util.https:.en.wikipedia.org.wiki.2Sum`
        
        
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
    public class MultidimensionalCounter extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable?is`<:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Integer?is`>
    
        Converter between unidimensional storage structure and multidimensional conceptual structure. This utility will convert
        from indices in a multidimensional structure to the corresponding index in a one-dimensional array. For example,
        assuming that the ranges (in 3 dimensions) of indices are 2, 4 and 3, the following correspondences, between 3-tuples
        indices and unidimensional indices, will hold:
    
          - (0, 0, 0) corresponds to 0
          - (0, 0, 1) corresponds to 1
          - (0, 0, 2) corresponds to 2
          - (0, 1, 0) corresponds to 3
          - ...
          - (1, 0, 0) corresponds to 12
          - ...
          - (1, 3, 2) corresponds to 23
    """
    def __init__(self, *int: int): ...
    def getCount(self, *int: int) -> int: ...
    def getCounts(self, int: int) -> typing.List[int]: ...
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
    def getSizes(self) -> typing.List[int]:
        """
            Get the number of multidimensional counter slots in each dimension.
        
            Returns:
                the sizes of the multidimensional counter in each dimension.
        
        
        """
        ...
    def iterator(self) -> 'MultidimensionalCounter.Iterator':
        """
            Create an iterator over this counter.
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable.html?is` in
                interface :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Iterable?is`
        
            Returns:
                the iterator.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    class Iterator(java.util.Iterator[int]):
        @typing.overload
        def getCount(self) -> int: ...
        @typing.overload
        def getCount(self, int: int) -> int: ...
        def getCounts(self) -> typing.List[int]: ...
        def hasNext(self) -> bool: ...
        def next(self) -> int: ...
        def remove(self) -> None: ...

class OpenIntToDoubleHashMap(java.io.Serializable):
    """
    public class OpenIntToDoubleHashMap extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Open addressed map from int to double.
    
        This class provides a dedicated map from integers to doubles with a much smaller memory overhead than standard
        :code:`java.util.Map`.
    
        This class is not synchronized. The specialized iterators returned by
        :meth:`~org.hipparchus.util.OpenIntToDoubleHashMap.iterator` are fail-fast: they throw a
        :code:`ConcurrentModificationException` when they detect the map has been modified during iteration.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, openIntToDoubleHashMap: 'OpenIntToDoubleHashMap'): ...
    def containsKey(self, int: int) -> bool:
        """
            Check if a value is associated with a key.
        
            Parameters:
                key (int): key to check
        
            Returns:
                true if a value is associated with key
        
        
        """
        ...
    def get(self, int: int) -> float:
        """
            Get the stored value associated with the given key
        
            Parameters:
                key (int): key associated with the data
        
            Returns:
                data associated with the key
        
        
        """
        ...
    def iterator(self) -> 'OpenIntToDoubleHashMap.Iterator':
        """
            Get an iterator over map elements.
        
            The specialized iterators returned are fail-fast: they throw a :code:`ConcurrentModificationException` when they detect
            the map has been modified during iteration.
        
            Returns:
                iterator over the map elements
        
        
        """
        ...
    def put(self, int: int, double: float) -> float:
        """
            Put a value associated with a key in the map.
        
            Parameters:
                key (int): key to which value is associated
                value (double): value to put in the map
        
            Returns:
                previous value associated with the key
        
        
        """
        ...
    def remove(self, int: int) -> float:
        """
            Remove the value associated with a key.
        
            Parameters:
                key (int): key to which the value is associated
        
            Returns:
                removed value
        
        
        """
        ...
    def size(self) -> int:
        """
            Get the number of elements stored in the map.
        
            Returns:
                number of elements stored in the map
        
        
        """
        ...
    class Iterator:
        def advance(self) -> None: ...
        def hasNext(self) -> bool: ...
        def key(self) -> int: ...
        def value(self) -> float: ...

_OpenIntToFieldHashMap__T = typing.TypeVar('_OpenIntToFieldHashMap__T', bound=org.hipparchus.FieldElement)  # <T>
class OpenIntToFieldHashMap(java.io.Serializable, typing.Generic[_OpenIntToFieldHashMap__T]):
    """
    public class OpenIntToFieldHashMap<T extends :class:`~org.hipparchus.FieldElement`<T>> extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Open addressed map from int to FieldElement.
    
        This class provides a dedicated map from integers to FieldElements with a much smaller memory overhead than standard
        :code:`java.util.Map`.
    
        This class is not synchronized. The specialized iterators returned by
        :meth:`~org.hipparchus.util.OpenIntToFieldHashMap.iterator` are fail-fast: they throw a
        :code:`ConcurrentModificationException` when they detect the map has been modified during iteration.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T], int: int, t: _OpenIntToFieldHashMap__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_OpenIntToFieldHashMap__T], t: _OpenIntToFieldHashMap__T): ...
    @typing.overload
    def __init__(self, openIntToFieldHashMap: 'OpenIntToFieldHashMap'[_OpenIntToFieldHashMap__T]): ...
    def containsKey(self, int: int) -> bool:
        """
            Check if a value is associated with a key.
        
            Parameters:
                key (int): key to check
        
            Returns:
                true if a value is associated with key
        
        
        """
        ...
    def get(self, int: int) -> _OpenIntToFieldHashMap__T:
        """
            Get the stored value associated with the given key
        
            Parameters:
                key (int): key associated with the data
        
            Returns:
                data associated with the key
        
        
        """
        ...
    def iterator(self) -> 'OpenIntToFieldHashMap.Iterator':
        """
            Get an iterator over map elements.
        
            The specialized iterators returned are fail-fast: they throw a :code:`ConcurrentModificationException` when they detect
            the map has been modified during iteration.
        
            Returns:
                iterator over the map elements
        
        
        """
        ...
    def put(self, int: int, t: _OpenIntToFieldHashMap__T) -> _OpenIntToFieldHashMap__T:
        """
            Put a value associated with a key in the map.
        
            Parameters:
                key (int): key to which value is associated
                value (:class:`~org.hipparchus.util.OpenIntToFieldHashMap`): value to put in the map
        
            Returns:
                previous value associated with the key
        
        
        """
        ...
    def remove(self, int: int) -> _OpenIntToFieldHashMap__T:
        """
            Remove the value associated with a key.
        
            Parameters:
                key (int): key to which the value is associated
        
            Returns:
                removed value
        
        
        """
        ...
    def size(self) -> int:
        """
            Get the number of elements stored in the map.
        
            Returns:
                number of elements stored in the map
        
        
        """
        ...
    class Iterator:
        def advance(self) -> None: ...
        def hasNext(self) -> bool: ...
        def key(self) -> int: ...
        def value(self) -> _OpenIntToFieldHashMap__T: ...

_Pair__K = typing.TypeVar('_Pair__K')  # <K>
_Pair__V = typing.TypeVar('_Pair__V')  # <V>
class Pair(typing.Generic[_Pair__K, _Pair__V]):
    """
    public class Pair<K, V> extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Generic pair.
    
        Although the instances of this class are immutable, it is impossible to ensure that the references passed to the
        constructor will not be modified by the caller.
    """
    @typing.overload
    def __init__(self, k: _Pair__K, v: _Pair__V): ...
    @typing.overload
    def __init__(self, pair: 'Pair'[_Pair__K, _Pair__V]): ...
    _create__K = typing.TypeVar('_create__K')  # <K>
    _create__V = typing.TypeVar('_create__V')  # <V>
    @staticmethod
    def create(k: _create__K, v: _create__V) -> 'Pair'[_create__K, _create__V]:
        """
            Convenience factory method that calls the :meth:`~org.hipparchus.util.Pair.%3Cinit%3E`.
        
            Parameters:
                k (K): First element of the pair.
                v (V): Second element of the pair.
        
            Returns:
                a new :code:`Pair` containing :code:`k` and :code:`v`.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Compare the specified object with this entry for equality.
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Parameters:
                o (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`): Object.
        
            Returns:
                :code:`true` if the given object is also a map entry and the two entries represent the same mapping.
        
        
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
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                the hash code value.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...

class PivotingStrategy(java.lang.Enum['PivotingStrategy']):
    """
    public enum PivotingStrategy extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.hipparchus.util.PivotingStrategy`>
    
        A strategy to pick a pivoting index of an array for doing partitioning.
    """
    CENTRAL: typing.ClassVar['PivotingStrategy'] = ...
    MEDIAN_OF_3: typing.ClassVar['PivotingStrategy'] = ...
    def pivotIndex(self, doubleArray: typing.List[float], int: int, int2: int) -> int: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PivotingStrategy':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['PivotingStrategy']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (PivotingStrategy c : PivotingStrategy.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Precision:
    """
    public class Precision extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utilities for comparing numbers.
    """
    EPSILON: typing.ClassVar[float] = ...
    """
    public static final double EPSILON
    
        Largest double-precision floating-point number such that :code:`1 + EPSILON` is numerically equal to 1. This value is an
        upper bound on the relative error due to rounding real numbers to double precision floating-point numbers.
    
        In IEEE 754 arithmetic, this is 2 :sup:`-53` .
    
        Also see:
            `Machine epsilon <http://en.wikipedia.org/wiki/Machine_epsilon>`
    
    
    """
    SAFE_MIN: typing.ClassVar[float] = ...
    """
    public static final double SAFE_MIN
    
        Safe minimum, such that :code:`1 / SAFE_MIN` does not overflow.
    
    
        In IEEE 754 arithmetic, this is also the smallest normalized number 2 :sup:`-1022` .
    
    """
    @typing.overload
    @staticmethod
    def compareTo(double: float, double2: float, double3: float) -> int:
        """
            Compares two numbers given some amount of allowed error.
        
            Parameters:
                x (double): the first number
                y (double): the second number
                eps (double): the amount of error to allow when checking for equality
        
            Returns:
        
                  - 0 if :meth:`~org.hipparchus.util.Precision.equals`
                  - < 0 if !:meth:`~org.hipparchus.util.Precision.equals` &&amp; x < y
                  - > 0 if !:meth:`~org.hipparchus.util.Precision.equals` &&amp; x > y or either argument is NaN
        
        
            Compares two numbers given some amount of allowed error. Two float numbers are considered equal if there are
            :code:`(maxUlps - 1)` (or fewer) floating point numbers between them, i.e. two adjacent floating point numbers are
            considered equal. Adapted from ` Bruce Dawson
            <http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/>`. Returns :code:`false` if
            either of the arguments is NaN.
        
            Parameters:
                x (double): first value
                y (double): second value
                maxUlps (int): :code:`(maxUlps - 1)` is the number of floating point values between :code:`x` and :code:`y`.
        
            Returns:
        
                  - 0 if :meth:`~org.hipparchus.util.Precision.equals`
                  - < 0 if !:meth:`~org.hipparchus.util.Precision.equals` &&amp; x < y
                  - > 0 if !:meth:`~org.hipparchus.util.Precision.equals` &&amp; x > y or either argument is NaN
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def compareTo(double: float, double2: float, int: int) -> int: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool:
        """
            Returns true iff they are equal as defined by :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (float): first value
                y (float): second value
        
            Returns:
                :code:`true` if the values are equal.
        
            Returns true if the arguments are equal or within the range of allowed error (inclusive). Returns :code:`false` if
            either of the arguments is NaN.
        
            Parameters:
                x (float): first value
                y (float): second value
                eps (float): the amount of absolute error to allow.
        
            Returns:
                :code:`true` if the values are equal or within range of each other.
        
            Returns true if the arguments are equal or within the range of allowed error (inclusive). Two float numbers are
            considered equal if there are :code:`(maxUlps - 1)` (or fewer) floating point numbers between them, i.e. two adjacent
            floating point numbers are considered equal. Adapted from ` Bruce Dawson
            <http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/>`. Returns :code:`false` if
            either of the arguments is NaN.
        
            Parameters:
                x (float): first value
                y (float): second value
                maxUlps (int): :code:`(maxUlps - 1)` is the number of floating point values between :code:`x` and :code:`y`.
        
            Returns:
                :code:`true` if there are fewer than :code:`maxUlps` floating point values between :code:`x` and :code:`y`.
        
            Returns true iff they are equal as defined by :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (double): first value
                y (double): second value
        
            Returns:
                :code:`true` if the values are equal.
        
            Returns :code:`true` if there is no double value strictly between the arguments or the difference between them is within
            the range of allowed error (inclusive). Returns :code:`false` if either of the arguments is NaN.
        
            Parameters:
                x (double): First value.
                y (double): Second value.
                eps (double): Amount of allowed absolute error.
        
            Returns:
                :code:`true` if the values are two adjacent floating point numbers or they are within range of each other.
        
            Returns true if the arguments are equal or within the range of allowed error (inclusive).
        
            Two float numbers are considered equal if there are :code:`(maxUlps - 1)` (or fewer) floating point numbers between
            them, i.e. two adjacent floating point numbers are considered equal.
        
            Adapted from ` Bruce Dawson
            <http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/>`. Returns :code:`false` if
            either of the arguments is NaN.
        
            Parameters:
                x (double): first value
                y (double): second value
                maxUlps (int): :code:`(maxUlps - 1)` is the number of floating point values between :code:`x` and :code:`y`.
        
            Returns:
                :code:`true` if there are fewer than :code:`maxUlps` floating point values between :code:`x` and :code:`y`.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float, double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(float: float, float2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(float: float, float2: float, float3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(float: float, float2: float, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(double: float, double2: float) -> bool:
        """
            Returns true if both arguments are NaN or they are equal as defined by :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (float): first value
                y (float): second value
        
            Returns:
                :code:`true` if the values are equal or both are NaN.
        
            Returns true if the arguments are both NaN, are equal, or are within the range of allowed error (inclusive).
        
            Parameters:
                x (float): first value
                y (float): second value
                eps (float): the amount of absolute error to allow.
        
            Returns:
                :code:`true` if the values are equal or within range of each other, or both are NaN.
        
            Returns true if the arguments are both NaN or if they are equal as defined by
            :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (float): first value
                y (float): second value
                maxUlps (int): :code:`(maxUlps - 1)` is the number of floating point values between :code:`x` and :code:`y`.
        
            Returns:
                :code:`true` if both arguments are NaN or if there are less than :code:`maxUlps` floating point values between :code:`x`
                and :code:`y`.
        
            Returns true if the arguments are both NaN or they are equal as defined by
            :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (double): first value
                y (double): second value
        
            Returns:
                :code:`true` if the values are equal or both are NaN.
        
            Returns true if the arguments are both NaN, are equal or are within the range of allowed error (inclusive).
        
            Parameters:
                x (double): first value
                y (double): second value
                eps (double): the amount of absolute error to allow.
        
            Returns:
                :code:`true` if the values are equal or within range of each other, or both are NaN.
        
            Returns true if both arguments are NaN or if they are equal as defined by :meth:`~org.hipparchus.util.Precision.equals`.
        
            Parameters:
                x (double): first value
                y (double): second value
                maxUlps (int): :code:`(maxUlps - 1)` is the number of floating point values between :code:`x` and :code:`y`.
        
            Returns:
                :code:`true` if both arguments are NaN or if there are less than :code:`maxUlps` floating point values between :code:`x`
                and :code:`y`.
        
        
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
    def equalsIncludingNaN(float: float, float2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(float: float, float2: float, float3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(float: float, float2: float, int: int) -> bool: ...
    @staticmethod
    def equalsWithRelativeTolerance(double: float, double2: float, double3: float) -> bool:
        """
            Returns :code:`true` if there is no double value strictly between the arguments or the relative difference between them
            is less than or equal to the given tolerance. Returns :code:`false` if either of the arguments is NaN.
        
            Parameters:
                x (double): First value.
                y (double): Second value.
                eps (double): Amount of allowed relative error.
        
            Returns:
                :code:`true` if the values are two adjacent floating point numbers or they are within range of each other.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isMathematicalInteger(double: float) -> bool:
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
    def isMathematicalInteger(float: float) -> bool: ...
    @staticmethod
    def representableDelta(double: float, double2: float) -> float:
        """
            Computes a number :code:`delta` close to :code:`originalDelta` with the property that
        
            .. code-block: java
            
            
               x + delta - x
             
            is exactly machine-representable. This is useful when computing numerical derivatives, in order to reduce roundoff
            errors.
        
            Parameters:
                x (double): Value.
                originalDelta (double): Offset value.
        
            Returns:
                a number :code:`delta` so that :code:`x + delta` and :code:`x` differ by a representable floating number.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def round(double: float, int: int) -> float:
        """
            Rounds the given value to the specified number of decimal places. The value is rounded using the
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal.html?is` method.
        
            Parameters:
                x (double): Value to round.
                scale (int): Number of digits to the right of the decimal point.
        
            Returns:
                the rounded value.
        
            Rounds the given value to the specified number of decimal places. The value is rounded using the given method which is
            any method defined in :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal?is`. If
            :code:`x` is infinite or :code:`NaN`, then the value of :code:`x` is returned unchanged, regardless of the other
            parameters.
        
            Parameters:
                x (double): Value to round.
                scale (int): Number of digits to the right of the decimal point.
                roundingMethod (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.RoundingMode?is`): Rounding method as defined in
                    :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal?is`.
        
            Returns:
                the rounded value.
        
            Raises:
                :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.ArithmeticException?is`: if :code:`roundingMethod == ROUND_UNNECESSARY` and the specified scaling operation would require rounding.
                :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if :code:`roundingMethod` does not represent a valid rounding mode.
        
            Rounds the given value to the specified number of decimal places. The value is rounded using the
            :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal.html?is` method.
        
            Parameters:
                x (float): Value to round.
                scale (int): Number of digits to the right of the decimal point.
        
            Returns:
                the rounded value.
        
        public static float round (float x, int scale, :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.RoundingMode?is` roundingMethod) throws :class:`~org.hipparchus.exception.MathRuntimeException`, :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Rounds the given value to the specified number of decimal places. The value is rounded using the given method which is
            any method defined in :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal?is`.
        
            Parameters:
                x (float): Value to round.
                scale (int): Number of digits to the right of the decimal point.
                roundingMethod (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.RoundingMode?is`): Rounding method as defined in
                    :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.math.BigDecimal?is`.
        
            Returns:
                the rounded value.
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if an exact operation is required but result is not exact
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`roundingMethod` is not a valid rounding method.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def round(double: float, int: int, roundingMode: java.math.RoundingMode) -> float: ...
    @typing.overload
    @staticmethod
    def round(float: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def round(float: float, int: int, roundingMode: java.math.RoundingMode) -> float: ...

class ResizableDoubleArray(java.io.Serializable):
    """
    public class ResizableDoubleArray extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        A variable length primitive double array implementation that automatically handles expanding and contracting its
        internal storage array as elements are added and removed.
    
        The internal storage array starts with capacity determined by the :code:`initialCapacity` property, which can be set by
        the constructor. The default initial capacity is 16. Adding elements using
        :meth:`~org.hipparchus.util.ResizableDoubleArray.addElement` appends elements to the end of the array. When there are no
        open entries at the end of the internal storage array, the array is expanded. The size of the expanded array depends on
        the :code:`expansionMode` and :code:`expansionFactor` properties. The :code:`expansionMode` determines whether the size
        of the array is multiplied by the :code:`expansionFactor`
        (:meth:`~org.hipparchus.util.ResizableDoubleArray.ExpansionMode.MULTIPLICATIVE`) or if the expansion is additive
        (:meth:`~org.hipparchus.util.ResizableDoubleArray.ExpansionMode.ADDITIVE` -- :code:`expansionFactor` storage locations
        added). The default :code:`expansionMode` is :code:`MULTIPLICATIVE` and the default :code:`expansionFactor` is 2.
    
        The :meth:`~org.hipparchus.util.ResizableDoubleArray.addElementRolling` method adds a new element to the end of the
        internal storage array and adjusts the "usable window" of the internal array forward by one position (effectively making
        what was the second element the first, and so on). Repeated activations of this method (or activation of
        :meth:`~org.hipparchus.util.ResizableDoubleArray.discardFrontElements`) will effectively orphan the storage locations at
        the beginning of the internal storage array. To reclaim this storage, each time one of these methods is activated, the
        size of the internal storage array is compared to the number of addressable elements (the :code:`numElements` property)
        and if the difference is too large, the internal array is contracted to size :code:`numElements + 1`. The determination
        of when the internal storage array is "too large" depends on the :code:`expansionMode` and :code:`contractionFactor`
        properties. If the :code:`expansionMode` is :code:`MULTIPLICATIVE`, contraction is triggered when the ratio between
        storage array length and :code:`numElements` exceeds :code:`contractionFactor.` If the :code:`expansionMode` is
        :code:`ADDITIVE`, the number of excess storage locations is compared to :code:`contractionFactor`.
    
        To avoid cycles of expansions and contractions, the :code:`expansionFactor` must not exceed the
        :code:`contractionFactor`. Constructors and mutators for both of these properties enforce this requirement, throwing a
        :code:`MathIllegalArgumentException` if it is violated.
    
        **Note:** this class is **NOT** thread-safe.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, expansionMode: 'ResizableDoubleArray.ExpansionMode', *double3: float): ...
    @typing.overload
    def __init__(self, resizableDoubleArray: 'ResizableDoubleArray'): ...
    def addElement(self, double: float) -> None:
        """
            Adds an element to the end of this expandable array.
        
            Parameters:
                value (double): Value to be added to end of array.
        
        
        """
        ...
    def addElementRolling(self, double: float) -> float:
        """
            Adds an element to the end of the array and removes the first element in the array. Returns the discarded first element.
        
            The effect is similar to a push operation in a FIFO queue.
        
            Example: If the array contains the elements 1, 2, 3, 4 (in that order) and addElementRolling(5) is invoked, the result
            is an array containing the entries 2, 3, 4, 5 and the value returned is 1.
        
            Parameters:
                value (double): Value to be added to the array.
        
            Returns:
                the value which has been discarded or "pushed" out of the array by this rolling insert.
        
        
        """
        ...
    def addElements(self, doubleArray: typing.List[float]) -> None:
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
    def compute(self, function: MathArrays.Function) -> float:
        """
            Performs an operation on the addressable elements of the array.
        
            Parameters:
                f (:class:`~org.hipparchus.util.MathArrays.Function`): Function to be applied on this array.
        
            Returns:
                the result.
        
        
        """
        ...
    def contract(self) -> None:
        """
            Contracts the storage array to the (size of the element set) + 1 - to avoid a zero length array. This function also
            resets the startIndex to zero.
        
        """
        ...
    def copy(self) -> 'ResizableDoubleArray':
        """
            Returns a copy of the ResizableDoubleArray. Does not contract before the copy, so the returned object is an exact copy
            of this.
        
            Returns:
                a new ResizableDoubleArray with the same data and configuration properties as this
        
        
        """
        ...
    def discardFrontElements(self, int: int) -> None: ...
    def discardMostRecentElements(self, int: int) -> None: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns true iff object is a ResizableDoubleArray with the same properties as this and an identical internal storage
            array.
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Parameters:
                object (:class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`): object to be compared for equality with this
        
            Returns:
                true iff object is a ResizableDoubleArray with the same data and properties as this
        
        
        """
        ...
    def getCapacity(self) -> int:
        """
            Gets the currently allocated size of the internal data structure used for storing elements. This is not to be confused
            with :meth:`~org.hipparchus.util.ResizableDoubleArray.getNumElements`.
        
            Returns:
                the length of the internal array.
        
        
        """
        ...
    def getContractionCriterion(self) -> float:
        """
            The contraction criterion defines when the internal array will contract to store only the number of elements in the
            element array.
        
            If the :code:`expansionMode` is :code:`MULTIPLICATIVE`, contraction is triggered when the ratio between storage array
            length and :code:`numElements` exceeds :code:`contractionFactor`. If the :code:`expansionMode` is :code:`ADDITIVE`, the
            number of excess storage locations is compared to :code:`contractionFactor`.
        
            Returns:
                the contraction criterion used to reclaim memory.
        
        
        """
        ...
    def getElement(self, int: int) -> float:
        """
            Returns the element at the specified index.
        
            Parameters:
                index (int): index to fetch a value from
        
            Returns:
                value stored at the specified index
        
            Raises:
                :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.ArrayIndexOutOfBoundsException?is`: if :code:`index` is less than zero or is greater than :code:`getNumElements() - 1`.
        
        
        """
        ...
    def getElements(self) -> typing.List[float]:
        """
            Returns a double array containing the elements of this ResizableArray.
        
            This method returns a copy, not a reference to the underlying array, so that changes made to the returned array have no
            effect on this ResizableArray.
        
            Returns:
                the double array.
        
        
        """
        ...
    def getExpansionFactor(self) -> float:
        """
            The expansion factor controls the size of a new array when an array needs to be expanded.
        
            The :code:`expansionMode` determines whether the size of the array is multiplied by the :code:`expansionFactor`
            (MULTIPLICATIVE) or if the expansion is additive (ADDITIVE -- :code:`expansionFactor` storage locations added). The
            default :code:`expansionMode` is MULTIPLICATIVE and the default :code:`expansionFactor` is 2.0.
        
            Returns:
                the expansion factor of this expandable double array
        
        
        """
        ...
    def getExpansionMode(self) -> 'ResizableDoubleArray.ExpansionMode':
        """
            The expansion mode determines whether the internal storage array grows additively or multiplicatively when it is
            expanded.
        
            Returns:
                the expansion mode.
        
        
        """
        ...
    def getNumElements(self) -> int:
        """
            Returns the number of elements currently in the array. Please note that this is different from the length of the
            internal storage array.
        
            Returns:
                the number of elements.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Returns a hash code consistent with equals.
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                the hash code representing this :code:`ResizableDoubleArray`.
        
        
        """
        ...
    def setElement(self, int: int, double: float) -> None:
        """
            Sets the element at the specified index.
        
            If the specified index is greater than :code:`getNumElements() - 1`, the :code:`numElements` property is increased to
            :code:`index +1` and additional storage is allocated (if necessary) for the new element and all (uninitialized) elements
            between the new element and the previous end of the array).
        
            Parameters:
                index (int): index to store a value in
                value (double): value to store at the specified index
        
            Raises:
                :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.ArrayIndexOutOfBoundsException?is`: if :code:`index < 0`.
        
        
        """
        ...
    def setNumElements(self, int: int) -> None: ...
    def substituteMostRecentElement(self, double: float) -> float: ...
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
        def values() -> typing.List['ResizableDoubleArray.ExpansionMode']: ...

class RosenNumberPartitionIterator(java.util.Iterator[typing.List[int]]):
    """
    public class RosenNumberPartitionIterator extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator?is`<int[]>
    
        An iterator that generates all partitions of :code:`n` elements, into :code:`k` parts containing the number of elements
        in each part, based on Rosen's algorithm.
    
        This is a copy of the class (with slight edits) with the same name from the
        :class:`~org.hipparchus.util.https:.github.com.axkr.symja_android_library`. The original file was published under the
        terms of the GPLV3 license, but the Hipparchus project was :meth:`~org.hipparchus.util.https:.github.com.Hipparchus` to
        include it relicensed to Apache V2.
    
        See Kenneth H. Rosen, Discrete Mathematics and Its Applications, 2nd edition (NY: McGraw-Hill, 1991), pp. 284-286
    """
    def __init__(self, int: int, int2: int): ...
    def hasNext(self) -> bool:
        """
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator.html?is` in
                interface :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator?is`
        
            Also see:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator.html?is`
        
        
        """
        ...
    def next(self) -> typing.List[int]:
        """
        
            Specified by:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator.html?is` in
                interface :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator?is`
        
            Also see:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.util.Iterator.html?is`
        
        
        """
        ...
    def reset(self) -> None:
        """
            Reset this iterator to the start condition.
        
        """
        ...

class RyuDouble:
    """
    public final class RyuDouble extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        An implementation of Ryū for double.
    
        Ryū generates the shortest decimal representation of a floating point number that maintains round-trip safety. That is,
        a correct parser can recover the exact original number. Ryū is very fast (about 10 time faster than
        :code:`Double.toString()`).
    
        Also see:
            :class:`~org.hipparchus.util.https:.dl.acm.org.citation.cfm?doid=3296979.3192369`
    """
    DEFAULT_LOW_EXP: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_LOW_EXP
    
        Default low switch level to scientific notation.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_HIGH_EXP: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_HIGH_EXP
    
        Default high switch level to scientific notation.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    @staticmethod
    def doubleToString(double: float) -> str:
        """
            Convert a double to shortest string representation, preserving full accuracy.
        
            This implementation uses the same specifications as :code:`Double.toString()`, i.e. it uses scientific notation if for
            numbers smaller than 10⁻³ or larger than 10⁺⁷, and decimal notion in between. That is it call
            :meth:`~org.hipparchus.util.RyuDouble.doubleToString`.
        
            Parameters:
                value (double): double number to convert
        
            Returns:
                shortest string representation
        
            Also see:
                :meth:`~org.hipparchus.util.RyuDouble.doubleToString`, :meth:`~org.hipparchus.util.RyuDouble.DEFAULT_LOW_EXP`,
                :meth:`~org.hipparchus.util.RyuDouble.DEFAULT_HIGH_EXP`
        
            Convert a double to shortest string representation, preserving full accuracy.
        
            Number inside of the interval [10 :sup:`lowExp` , 10 :sup:`highExp` ] are represented using decimal notation, numbers
            outside of this range are represented using scientific notation.
        
            Parameters:
                value (double): double number to convert
                lowExp (int): lowest decimal exponent for which decimal notation can be used
                highExp (int): highest decimal exponent for which decimal notation can be used
        
            Returns:
                shortest string representation
        
            Also see:
                :meth:`~org.hipparchus.util.RyuDouble.doubleToString`, :meth:`~org.hipparchus.util.RyuDouble.DEFAULT_LOW_EXP`,
                :meth:`~org.hipparchus.util.RyuDouble.DEFAULT_HIGH_EXP`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def doubleToString(double: float, int: int, int2: int) -> str: ...

class SinCos:
    """
    public class SinCos extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Holder for both sine and cosine values.
    
        This class is a simple container, it does not provide any computational method.
    
        Since:
            1.3
    
        Also see:
            :meth:`~org.hipparchus.util.FastMath.sinCos`
    """
    def cos(self) -> float:
        """
            Get the value of the cosine.
        
            Returns:
                value of the cosine
        
        
        """
        ...
    @staticmethod
    def difference(sinCos: 'SinCos', sinCos2: 'SinCos') -> 'SinCos':
        """
            Compute sine and cosine of angles difference.
        
            Parameters:
                scAlpha (:class:`~org.hipparchus.util.SinCos`): \((\sin \alpha, \cos \alpha)\)
                scBeta (:class:`~org.hipparchus.util.SinCos`): \((\sin \beta, \cos \beta)\)
        
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
    def sum(sinCos: 'SinCos', sinCos2: 'SinCos') -> 'SinCos':
        """
            Compute sine and cosine of angles sum.
        
            Parameters:
                scAlpha (:class:`~org.hipparchus.util.SinCos`): \((\sin \alpha, \cos \alpha)\)
                scBeta (:class:`~org.hipparchus.util.SinCos`): \((\sin \beta, \cos \beta)\)
        
            Returns:
                \((\sin \alpha+\beta, \cos \alpha+\beta)\)
        
            Since:
                1.8
        
        
        """
        ...

class SinhCosh:
    """
    public class SinhCosh extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Holder for both hyperbolic sine and hyperbolic cosine values.
    
        This class is a simple container, it does not provide any computational method.
    
        Since:
            2.0
    
        Also see:
            :meth:`~org.hipparchus.util.FastMath.sinhCosh`
    """
    def cosh(self) -> float:
        """
            Get the value of the hyperbolic cosine.
        
            Returns:
                value of the hyperbolic cosine
        
        
        """
        ...
    @staticmethod
    def difference(sinhCosh: 'SinhCosh', sinhCosh2: 'SinhCosh') -> 'SinhCosh':
        """
            Compute hyperbolic sine and hyperbolic cosine of angles difference.
        
            Parameters:
                schAlpha (:class:`~org.hipparchus.util.SinhCosh`): \((\sinh \alpha, \cosh \alpha)\)
                schBeta (:class:`~org.hipparchus.util.SinhCosh`): \((\sinh \beta, \cosh \beta)\)
        
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
    def sum(sinhCosh: 'SinhCosh', sinhCosh2: 'SinhCosh') -> 'SinhCosh':
        """
            Compute hyperbolic sine and hyperbolic cosine of angles sum.
        
            Parameters:
                schAlpha (:class:`~org.hipparchus.util.SinhCosh`): \((\sinh \alpha, \cosh \alpha)\)
                schBeta (:class:`~org.hipparchus.util.SinhCosh`): \((\sinh \beta, \cosh \beta)\)
        
            Returns:
                \((\sinh \alpha+\beta, \cosh \alpha+\beta)\)
        
        
        """
        ...

class Tuple(org.hipparchus.CalculusFieldElement['Tuple']):
    """
    public class Tuple extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.util.Tuple`>
    
        This class allows to perform the same computation of all components of a Tuple at once.
    
        Since:
            1.2
    """
    def __init__(self, *double: float): ...
    def abs(self) -> 'Tuple':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'Tuple':
        """
            Arc cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'Tuple':
        """
            Inverse hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'Tuple':
        """
            Compute this + a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Tuple`): element to add
        
            Returns:
                a new element representing this + a
        
            '+' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.add` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
        
        """
        ...
    @typing.overload
    def add(self, tuple: 'Tuple') -> 'Tuple': ...
    def asin(self) -> 'Tuple':
        """
            Arc sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'Tuple':
        """
            Inverse hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'Tuple':
        """
            Arc tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atan(this)
        
        
        """
        ...
    def atan2(self, tuple: 'Tuple') -> 'Tuple':
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
                x (:class:`~org.hipparchus.util.Tuple`): second argument of the arc tangent
        
            Returns:
        
        """
        ...
    def atanh(self) -> 'Tuple':
        """
            Inverse hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'Tuple':
        """
            Cubic root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cbrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'Tuple':
        """
            Get the smallest whole number larger than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ceil(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'Tuple':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (:class:`~org.hipparchus.util.Tuple`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, tuple: 'Tuple') -> 'Tuple': ...
    def cos(self) -> 'Tuple':
        """
            Cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'Tuple':
        """
            Hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'Tuple':
        """
            Compute this ÷ a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Tuple`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
            '÷' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.divide` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
        
        """
        ...
    @typing.overload
    def divide(self, tuple: 'Tuple') -> 'Tuple': ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def exp(self) -> 'Tuple':
        """
            Exponential.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'Tuple':
        """
            Exponential minus 1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.expm1` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'Tuple':
        """
            Get the largest whole number smaller than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getComponent(self, int: int) -> float:
        """
            Get one component of the tuple.
        
            Parameters:
                index (int): index of the component, between 0 and :meth:`~org.hipparchus.util.Tuple.getDimension` - 1
        
            Returns:
                value of the component
        
        
        """
        ...
    def getComponents(self) -> typing.List[float]:
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
    def getField(self) -> org.hipparchus.Field['Tuple']: ...
    def getPi(self) -> 'Tuple':
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
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def hypot(self, tuple: 'Tuple') -> 'Tuple':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2`  +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.hypot` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                y (:class:`~org.hipparchus.util.Tuple`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, tuple: 'Tuple', double2: float, tuple2: 'Tuple') -> 'Tuple':
        """
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Tuple`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Tuple`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Tuple`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Tuple`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Tuple`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Tuple`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Tuple`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Tuple`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Tuple`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Tuple`): second factor of the second term
                a3 (:class:`~org.hipparchus.util.Tuple`): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Tuple`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Tuple`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Tuple`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Tuple`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Tuple`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Tuple`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Tuple`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Tuple`): second factor of the second term
                a3 (:class:`~org.hipparchus.util.Tuple`): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Tuple`): second factor of the third term
                a4 (:class:`~org.hipparchus.util.Tuple`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.util.Tuple`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Tuple`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Tuple`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Tuple`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.util.Tuple`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, tuple: 'Tuple', double2: float, tuple2: 'Tuple', double3: float, tuple3: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, double: float, tuple: 'Tuple', double2: float, tuple2: 'Tuple', double3: float, tuple3: 'Tuple', double4: float, tuple4: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], tupleArray: typing.List['Tuple']) -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, tuple: 'Tuple', tuple2: 'Tuple', tuple3: 'Tuple', tuple4: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, tuple: 'Tuple', tuple2: 'Tuple', tuple3: 'Tuple', tuple4: 'Tuple', tuple5: 'Tuple', tuple6: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, tuple: 'Tuple', tuple2: 'Tuple', tuple3: 'Tuple', tuple4: 'Tuple', tuple5: 'Tuple', tuple6: 'Tuple', tuple7: 'Tuple', tuple8: 'Tuple') -> 'Tuple': ...
    @typing.overload
    def linearCombination(self, tupleArray: typing.List['Tuple'], tupleArray2: typing.List['Tuple']) -> 'Tuple': ...
    def log(self) -> 'Tuple':
        """
            Natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'Tuple':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'Tuple':
        """
            Shifted natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log1p` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Tuple':
        """
            Compute this × a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Tuple`): element to multiply
        
            Returns:
                a new element representing this × a
        
            Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} =
            \sum_{i=1}^n \mathrm{this} \]
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
            '×' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
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
            Returns the additive inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'Tuple':
        """
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                value (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'Tuple':
        """
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
            Integer power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                e (:class:`~org.hipparchus.util.Tuple`): exponent
        
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
            Returns the multiplicative inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.reciprocal` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'Tuple':
        """
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Tuple`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, tuple: 'Tuple') -> 'Tuple': ...
    def rint(self) -> 'Tuple':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'Tuple':
        """
            N :sup:`th` root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rootN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): order of the root
        
            Returns:
                n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, int: int) -> 'Tuple':
        """
            Multiply the instance by a power of 2.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.scalb` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power of 2
        
            Returns:
                this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> 'Tuple':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'Tuple':
        """
            Sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> FieldSinCos['Tuple']: ...
    def sinh(self) -> 'Tuple':
        """
            Hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> FieldSinhCosh['Tuple']: ...
    def sqrt(self) -> 'Tuple':
        """
            Square root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'Tuple':
        """
            Compute this - a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Tuple`): element to subtract
        
            Returns:
                a new element representing this - a
        
            '-' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.subtract` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
        
        """
        ...
    @typing.overload
    def subtract(self, tuple: 'Tuple') -> 'Tuple': ...
    def tan(self) -> 'Tuple':
        """
            Tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'Tuple':
        """
            Hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> 'Tuple':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'Tuple':
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toRadians` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def ulp(self) -> 'Tuple':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ulp(this)
        
        
        """
        ...

class UnscentedTransformProvider:
    """
    public interface UnscentedTransformProvider
    
        Provider for unscented transform.
    
        Since:
            2.2
    """
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
    def unscentedTransform(self, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[org.hipparchus.linear.RealVector]:
        """
            Perform the unscented transform from a state and its covariance.
        
            Parameters:
                state (:class:`~org.hipparchus.linear.RealVector`): process state
                covariance (:class:`~org.hipparchus.linear.RealMatrix`): covariance associated with the process state
        
            Returns:
                an array containing the sigma points of the unscented transform
        
        
        """
        ...

class AbstractUnscentedTransform(UnscentedTransformProvider):
    """
    public abstract class AbstractUnscentedTransform extends :class:`~org.hipparchus.util.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.hipparchus.util.UnscentedTransformProvider`
    
        Base class for unscented transform providers.
    
        Since:
            2.2
    """
    def __init__(self, int: int): ...
    def unscentedTransform(self, realVector: org.hipparchus.linear.RealVector, realMatrix: org.hipparchus.linear.RealMatrix) -> typing.List[org.hipparchus.linear.RealVector]:
        """
            Perform the unscented transform from a state and its covariance.
        
            Let n be the state dimension and Si be the ith row of the covariance matrix square root. The returned array is organized
            as follow. Element 0 contains the process state, also called the mean state. Elements from 1 to n contain the process
            state + Si. Finally, elements from n + 1 to 2n contain the process state - Si
        
            Specified by:
                :meth:`~org.hipparchus.util.UnscentedTransformProvider.unscentedTransform` in
                interface :class:`~org.hipparchus.util.UnscentedTransformProvider`
        
            Parameters:
                state (:class:`~org.hipparchus.linear.RealVector`): process state
                covariance (:class:`~org.hipparchus.linear.RealMatrix`): covariance associated with the process state
        
            Returns:
                an array containing the sigma points of the unscented transform
        
        
        """
        ...

class JulierUnscentedTransform(AbstractUnscentedTransform):
    """
    public class JulierUnscentedTransform extends :class:`~org.hipparchus.util.AbstractUnscentedTransform`
    
        Unscented transform as defined by Julier and Uhlmann.
    
        The unscented transform uses three parameters: alpha, beta and kappa. Alpha determines the spread of the sigma points
        around the process state, kappa is a secondary scaling parameter, and beta is used to incorporate prior knowledge of the
        distribution of the process state.
    
        The Julier transform is a particular case of :class:`~org.hipparchus.util.MerweUnscentedTransform` with alpha = 1 and
        beta = 0.
    
        Since:
            2.2
    
        Also see:
            "S. J. Julier and J. K. Uhlmann. A New Extension of the Kalman Filter to Nonlinear Systems. Proc. SPIE 3068, Signal
            Processing, Sensor Fusion, and Target Recognition VI, 182 (July 28, 1997)"
    """
    DEFAULT_KAPPA: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_KAPPA
    
        Default value for kappa, (0.0, see reference).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
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
    public class MerweUnscentedTransform extends :class:`~org.hipparchus.util.AbstractUnscentedTransform`
    
        Unscented transform as defined by Merwe and Wan.
    
        The unscented transform uses three parameters: alpha, beta and kappa. Alpha determines the spread of the sigma points
        around the process state, kappa is a secondary scaling parameter, and beta is used to incorporate prior knowledge of the
        distribution of the process state.
    
        Since:
            2.2
    
        Also see:
            "E. A. Wan and R. Van der Merwe, The unscented Kalman filter for nonlinear estimation, in Proc. Symp. Adaptive Syst.
            Signal Process., Commun. Contr., Lake Louise, AB, Canada, Oct. 2000."
    """
    DEFAULT_ALPHA: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ALPHA
    
        Default value for alpha (0.5, see reference).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_BETA: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_BETA
    
        Default value for beta (2.0, see reference).
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_KAPPA: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_KAPPA
    
        Default value for kappa, (0.0, see reference).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.util")``.

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
