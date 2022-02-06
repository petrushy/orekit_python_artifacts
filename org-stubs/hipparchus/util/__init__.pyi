import decimal
import java.io
import java.lang
import java.math
import java.text
import java.util
import org.hipparchus
import org.hipparchus.exception
import org.hipparchus.random
import typing



class ArithmeticUtils:
    @typing.overload
    @staticmethod
    def addAndCheck(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def addAndCheck(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def divideUnsigned(int: int, int2: int) -> int: ...
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
    def isPowerOfTwo(long: int) -> bool: ...
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
    def remainderUnsigned(int: int, int2: int) -> int: ...
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
    public class BigReal extends Object implements :class:`~org.hipparchus.FieldElement`<:class:`~org.hipparchus.util.BigReal`>, Comparable<:class:`~org.hipparchus.util.BigReal`>, Serializable
    
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
                 in interface 
        
        
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
                 in class 
        
        
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
                 in class 
        
        
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
        
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
        
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
                roundingMode (RoundingMode): rounding mode for decimal divisions
        
        
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
    public class BigRealField extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.util.BigReal`>, Serializable
    
        Representation of real numbers with arbitrary precision field.
    
        This class is a singleton.
    
        Also see:
            :class:`~org.hipparchus.util.BigReal`, :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
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
            equalities a Ã— e :sub:`1` = e :sub:`1` Ã— a = a hold.
        
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
                 in class 
        
        
        """
        ...

class Combinations(java.lang.Iterable[typing.List[int]]):
    def __init__(self, int: int, int2: int): ...
    def comparator(self) -> java.util.Comparator[typing.List[int]]: ...
    def getK(self) -> int: ...
    def getN(self) -> int: ...
    def iterator(self) -> java.util.Iterator[typing.List[int]]: ...

class CombinatoricsUtils:
    """
    public final class CombinatoricsUtils extends Object
    
        Combinatorial utilities.
    """
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
                an null over the k-sets in n.
        
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
    @staticmethod
    def stirlingS2(int: int, int2: int) -> int: ...
    class FactorialLog:
        @staticmethod
        def create() -> 'CombinatoricsUtils.FactorialLog': ...
        def value(self, int: int) -> float: ...
        def withCache(self, int: int) -> 'CombinatoricsUtils.FactorialLog': ...

class CompositeFormat:
    """
    public class CompositeFormat extends Object
    
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
            Create a default number format. The default number format is based on null with the only customizing that the maximum
            number of fraction digits is set to 10.
        
            Returns:
                the default number format.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDefaultNumberFormat(locale: java.util.Locale) -> java.text.NumberFormat:
        """
            Create a default number format. The default number format is based on null with the only customizing that the maximum
            number of fraction digits is set to 10.
        
            Parameters:
                locale (Locale): the specific locale used by the format.
        
            Returns:
                the default number format specific to the given locale.
        
        
        """
        ...
    @staticmethod
    def parseAndIgnoreWhitespace(string: str, parsePosition: java.text.ParsePosition) -> None:
        """
            Parses :code:`source` until a non-whitespace character is found.
        
            Parameters:
                source (String): the string to parse
                pos (ParsePosition): input/output parsing parameter. On output, :code:`pos` holds the index of the next non-whitespace character.
        
        
        """
        ...
    @staticmethod
    def parseFixedstring(string: str, string2: str, parsePosition: java.text.ParsePosition) -> bool:
        """
            Parse :code:`source` for an expected fixed string.
        
            Parameters:
                source (String): the string to parse
                expected (String): expected string
                pos (ParsePosition): input/output parsing parameter.
        
            Returns:
                true if the expected string was there
        
        
        """
        ...
    @staticmethod
    def parseNextCharacter(string: str, parsePosition: java.text.ParsePosition) -> str:
        """
            Parses :code:`source` until a non-whitespace character is found.
        
            Parameters:
                source (String): the string to parse
                pos (ParsePosition): input/output parsing parameter.
        
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
                source (String): the string to parse
                format (NumberFormat): the number format used to parse normal, numeric values.
                pos (ParsePosition): input/output parsing parameter.
        
            Returns:
                the parsed number.
        
        
        """
        ...

class ContinuedFraction:
    """
    public abstract class ContinuedFraction extends Object
    
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

class Decimal64(java.lang.Number, org.hipparchus.CalculusFieldElement['Decimal64'], java.lang.Comparable['Decimal64']):
    """
    public class Decimal64 extends Number implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.util.Decimal64`>, Comparable<:class:`~org.hipparchus.util.Decimal64`>
    
        This class wraps a :code:`double` value in an object. It is similar to the standard class null, while also implementing
        the :class:`~org.hipparchus.CalculusFieldElement` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ZERO: typing.ClassVar['Decimal64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Decimal64` ZERO
    
        The constant value of :code:`0d` as a :code:`Decimal64`.
    
    """
    ONE: typing.ClassVar['Decimal64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Decimal64` ONE
    
        The constant value of :code:`1d` as a :code:`Decimal64`.
    
    """
    PI: typing.ClassVar['Decimal64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Decimal64` PI
    
        The constant value of Ï€ as a :code:`Decimal64`.
    
    """
    NEGATIVE_INFINITY: typing.ClassVar['Decimal64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Decimal64` NEGATIVE_INFINITY
    
        The constant value of null as a :code:`Decimal64`.
    
    """
    POSITIVE_INFINITY: typing.ClassVar['Decimal64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Decimal64` POSITIVE_INFINITY
    
        The constant value of null as a :code:`Decimal64`.
    
    """
    NAN: typing.ClassVar['Decimal64'] = ...
    """
    public static final :class:`~org.hipparchus.util.Decimal64` NAN
    
        The constant value of null as a :code:`Decimal64`.
    
    """
    def __init__(self, double: float): ...
    def abs(self) -> 'Decimal64':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'Decimal64':
        """
            Arc cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'Decimal64':
        """
            Inverse hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'Decimal64':
        """
            Compute this + a. The current implementation strictly enforces :code:`this.add(a).equals(new
            Decimal64(this.doubleValue() + a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Decimal64`): element to add
        
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
    def add(self, decimal64: 'Decimal64') -> 'Decimal64': ...
    def asin(self) -> 'Decimal64':
        """
            Arc sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'Decimal64':
        """
            Inverse hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'Decimal64':
        """
            Arc tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atan(this)
        
        
        """
        ...
    def atan2(self, decimal64: 'Decimal64') -> 'Decimal64':
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
                x (:class:`~org.hipparchus.util.Decimal64`): second argument of the arc tangent
        
            Returns:
        
        """
        ...
    def atanh(self) -> 'Decimal64':
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
                 in class 
        
        
        """
        ...
    def cbrt(self) -> 'Decimal64':
        """
            Cubic root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cbrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'Decimal64':
        """
            Get the smallest whole number larger than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ceil(this)
        
        
        """
        ...
    def compareTo(self, decimal64: 'Decimal64') -> int:
        """
            The current implementation returns the same value as
            :code:`new Double(this.doubleValue()).compareTo(new Double(o.doubleValue()))`
        
            Specified by:
                 in interface 
        
            Also see:
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'Decimal64':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (:class:`~org.hipparchus.util.Decimal64`): the sign for the returned value
        
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
    def copySign(self, decimal64: 'Decimal64') -> 'Decimal64': ...
    def cos(self) -> 'Decimal64':
        """
            Cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'Decimal64':
        """
            Hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'Decimal64':
        """
            Compute this Ã· a. The current implementation strictly enforces :code:`this.divide(a).equals(new
            Decimal64(this.doubleValue() / a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Decimal64`): element to divide by
        
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
    def divide(self, decimal64: 'Decimal64') -> 'Decimal64': ...
    def doubleValue(self) -> float:
        """
        
            Specified by:
                 in class 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def exp(self) -> 'Decimal64':
        """
            Exponential.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'Decimal64':
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
                 in class 
        
        
        """
        ...
    def floor(self) -> 'Decimal64':
        """
            Get the largest whole number smaller than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['Decimal64']: ...
    def getPi(self) -> 'Decimal64':
        """
            Get the Archimedes constant Ï€.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant Ï€
        
        
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
                 in class 
        
            Also see:
        
        
        """
        ...
    def hypot(self, decimal64: 'Decimal64') -> 'Decimal64':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2` Â +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.hypot` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                y (:class:`~org.hipparchus.util.Decimal64`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    def intValue(self) -> int:
        """
            The current implementation performs casting to a :code:`int`.
        
            Specified by:
                 in class 
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Returns :code:`true` if :code:`this` double precision number is infinite (null or null).
        
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
    def linearCombination(self, double: float, decimal64: 'Decimal64', double2: float, decimal642: 'Decimal64') -> 'Decimal64':
        """
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Decimal64`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Decimal64`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Decimal64`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Decimal64`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Decimal64`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Decimal64`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Decimal64`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Decimal64`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Decimal64`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Decimal64`): second factor of the second term
                a3 (:class:`~org.hipparchus.util.Decimal64`): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Decimal64`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Decimal64`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Decimal64`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Decimal64`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.util.Decimal64`): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Decimal64`): second factor of the first term
                a2 (:class:`~org.hipparchus.util.Decimal64`): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Decimal64`): second factor of the second term
                a3 (:class:`~org.hipparchus.util.Decimal64`): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Decimal64`): second factor of the third term
                a4 (:class:`~org.hipparchus.util.Decimal64`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.util.Decimal64`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.util.Decimal64`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.util.Decimal64`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.util.Decimal64`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.util.Decimal64`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, decimal64: 'Decimal64', double2: float, decimal642: 'Decimal64', double3: float, decimal643: 'Decimal64') -> 'Decimal64': ...
    @typing.overload
    def linearCombination(self, double: float, decimal64: 'Decimal64', double2: float, decimal642: 'Decimal64', double3: float, decimal643: 'Decimal64', double4: float, decimal644: 'Decimal64') -> 'Decimal64': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], decimal64Array: typing.List['Decimal64']) -> 'Decimal64': ...
    @typing.overload
    def linearCombination(self, decimal64: 'Decimal64', decimal642: 'Decimal64', decimal643: 'Decimal64', decimal644: 'Decimal64') -> 'Decimal64': ...
    @typing.overload
    def linearCombination(self, decimal64: 'Decimal64', decimal642: 'Decimal64', decimal643: 'Decimal64', decimal644: 'Decimal64', decimal645: 'Decimal64', decimal646: 'Decimal64') -> 'Decimal64': ...
    @typing.overload
    def linearCombination(self, decimal64: 'Decimal64', decimal642: 'Decimal64', decimal643: 'Decimal64', decimal644: 'Decimal64', decimal645: 'Decimal64', decimal646: 'Decimal64', decimal647: 'Decimal64', decimal648: 'Decimal64') -> 'Decimal64': ...
    @typing.overload
    def linearCombination(self, decimal64Array: typing.List['Decimal64'], decimal64Array2: typing.List['Decimal64']) -> 'Decimal64': ...
    def log(self) -> 'Decimal64':
        """
            Natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'Decimal64':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'Decimal64':
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
                 in class 
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Decimal64':
        """
            Compute this Ã— a. The current implementation strictly enforces :code:`this.multiply(a).equals(new
            Decimal64(this.doubleValue() * a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Decimal64`): element to multiply
        
            Returns:
                a new element representing this × a
        
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
            The current implementation strictly enforces :code:`this.multiply(n).equals(new Decimal64(n * this.doubleValue()))`.
        
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
    def multiply(self, int: int) -> 'Decimal64': ...
    @typing.overload
    def multiply(self, decimal64: 'Decimal64') -> 'Decimal64': ...
    def negate(self) -> 'Decimal64':
        """
            Returns the additive inverse of :code:`this` element. The current implementation strictly enforces
            :code:`this.negate().equals(new Decimal64(-this.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'Decimal64':
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
    def pow(self, double: float) -> 'Decimal64':
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
                e (:class:`~org.hipparchus.util.Decimal64`): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'Decimal64': ...
    @typing.overload
    def pow(self, decimal64: 'Decimal64') -> 'Decimal64': ...
    def reciprocal(self) -> 'Decimal64':
        """
            Returns the multiplicative inverse of :code:`this` element. The current implementation strictly enforces
            :code:`this.reciprocal().equals(new Decimal64(1.0 / this.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.reciprocal` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'Decimal64':
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
                a (:class:`~org.hipparchus.util.Decimal64`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, decimal64: 'Decimal64') -> 'Decimal64': ...
    def rint(self) -> 'Decimal64':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'Decimal64':
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
    def scalb(self, int: int) -> 'Decimal64':
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
                 in class 
        
        
        """
        ...
    def sign(self) -> 'Decimal64':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'Decimal64':
        """
            Sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> 'FieldSinCos'['Decimal64']: ...
    def sinh(self) -> 'Decimal64':
        """
            Hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> 'FieldSinhCosh'['Decimal64']: ...
    def sqrt(self) -> 'Decimal64':
        """
            Square root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'Decimal64':
        """
            Compute this - a. The current implementation strictly enforces :code:`this.subtract(a).equals(new
            Decimal64(this.doubleValue() - a.doubleValue()))`.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.util.Decimal64`): element to subtract
        
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
    def subtract(self, decimal64: 'Decimal64') -> 'Decimal64': ...
    def tan(self) -> 'Decimal64':
        """
            Tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'Decimal64':
        """
            Hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> 'Decimal64':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'Decimal64':
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
                 in class 
        
            Also see:
        
        
        """
        ...
    def ulp(self) -> 'Decimal64':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ulp(this)
        
        
        """
        ...

class Decimal64Field(org.hipparchus.Field[Decimal64], java.io.Serializable):
    """
    public class Decimal64Field extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.util.Decimal64`>, Serializable
    
        The field of double precision floating-point numbers.
    
        Also see:
            :class:`~org.hipparchus.util.Decimal64`, :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'Decimal64Field':
        """
            Returns the unique instance of this class.
        
            Returns:
                the unique instance of this class
        
        
        """
        ...
    def getOne(self) -> Decimal64:
        """
            Get the multiplicative identity of the field.
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a Ã— e :sub:`1` = e :sub:`1` Ã— a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Decimal64]: ...
    def getZero(self) -> Decimal64:
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
                 in class 
        
        
        """
        ...

class FastMath:
    PI: typing.ClassVar[float] = ...
    E: typing.ClassVar[float] = ...
    _IEEEremainder_1__T = typing.TypeVar('_IEEEremainder_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _IEEEremainder_2__T = typing.TypeVar('_IEEEremainder_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def IEEEremainder(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def IEEEremainder(t: _IEEEremainder_1__T, double: float) -> _IEEEremainder_1__T: ...
    @typing.overload
    @staticmethod
    def IEEEremainder(t: _IEEEremainder_2__T, t2: _IEEEremainder_2__T) -> _IEEEremainder_2__T: ...
    _abs_4__T = typing.TypeVar('_abs_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def abs(double: float) -> float: ...
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
    def abs(t: _abs_4__T) -> _abs_4__T: ...
    @typing.overload
    @staticmethod
    def absExact(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def absExact(long: int) -> int: ...
    _acos_1__T = typing.TypeVar('_acos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def acos(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def acos(t: _acos_1__T) -> _acos_1__T: ...
    _acosh_1__T = typing.TypeVar('_acosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def acosh(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def acosh(t: _acosh_1__T) -> _acosh_1__T: ...
    @typing.overload
    @staticmethod
    def addExact(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def addExact(long: int, long2: int) -> int: ...
    _asin_1__T = typing.TypeVar('_asin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def asin(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def asin(t: _asin_1__T) -> _asin_1__T: ...
    _asinh_1__T = typing.TypeVar('_asinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def asinh(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def asinh(t: _asinh_1__T) -> _asinh_1__T: ...
    _atan_1__T = typing.TypeVar('_atan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def atan(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def atan(t: _atan_1__T) -> _atan_1__T: ...
    _atan2_1__T = typing.TypeVar('_atan2_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def atan2(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def atan2(t: _atan2_1__T, t2: _atan2_1__T) -> _atan2_1__T: ...
    _atanh_1__T = typing.TypeVar('_atanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def atanh(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def atanh(t: _atanh_1__T) -> _atanh_1__T: ...
    _cbrt_1__T = typing.TypeVar('_cbrt_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def cbrt(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def cbrt(t: _cbrt_1__T) -> _cbrt_1__T: ...
    _ceil_1__T = typing.TypeVar('_ceil_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def ceil(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def ceil(t: _ceil_1__T) -> _ceil_1__T: ...
    _copySign_2__T = typing.TypeVar('_copySign_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _copySign_3__T = typing.TypeVar('_copySign_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def copySign(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def copySign(float: float, float2: float) -> float: ...
    @typing.overload
    @staticmethod
    def copySign(t: _copySign_2__T, double: float) -> _copySign_2__T: ...
    @typing.overload
    @staticmethod
    def copySign(t: _copySign_3__T, t2: _copySign_3__T) -> _copySign_3__T: ...
    _cos_1__T = typing.TypeVar('_cos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def cos(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def cos(t: _cos_1__T) -> _cos_1__T: ...
    _cosh_1__T = typing.TypeVar('_cosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def cosh(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def cosh(t: _cosh_1__T) -> _cosh_1__T: ...
    @typing.overload
    @staticmethod
    def decrementExact(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def decrementExact(long: int) -> int: ...
    _exp_1__T = typing.TypeVar('_exp_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def exp(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def exp(t: _exp_1__T) -> _exp_1__T: ...
    _expm1_1__T = typing.TypeVar('_expm1_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def expm1(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def expm1(t: _expm1_1__T) -> _expm1_1__T: ...
    _floor_1__T = typing.TypeVar('_floor_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def floor(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def floor(t: _floor_1__T) -> _floor_1__T: ...
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
    def floorMod(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorMod(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def floorMod(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def fma(double: float, double2: float, double3: float) -> float: ...
    @typing.overload
    @staticmethod
    def fma(float: float, float2: float, float3: float) -> float: ...
    @typing.overload
    @staticmethod
    def getExponent(double: float) -> int: ...
    @typing.overload
    @staticmethod
    def getExponent(float: float) -> int: ...
    _hypot_1__T = typing.TypeVar('_hypot_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def hypot(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def hypot(t: _hypot_1__T, t2: _hypot_1__T) -> _hypot_1__T: ...
    @typing.overload
    @staticmethod
    def incrementExact(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def incrementExact(long: int) -> int: ...
    _log_2__T = typing.TypeVar('_log_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def log(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def log(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def log(t: _log_2__T) -> _log_2__T: ...
    _log10_1__T = typing.TypeVar('_log10_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def log10(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def log10(t: _log10_1__T) -> _log10_1__T: ...
    _log1p_1__T = typing.TypeVar('_log1p_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def log1p(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def log1p(t: _log1p_1__T) -> _log1p_1__T: ...
    _max_4__T = typing.TypeVar('_max_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _max_5__T = typing.TypeVar('_max_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def max(double: float, double2: float) -> float: ...
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
    def max(t: _max_4__T, double: float) -> _max_4__T: ...
    @typing.overload
    @staticmethod
    def max(t: _max_5__T, t2: _max_5__T) -> _max_5__T: ...
    _min_4__T = typing.TypeVar('_min_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _min_5__T = typing.TypeVar('_min_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def min(double: float, double2: float) -> float: ...
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
    def min(t: _min_4__T, double: float) -> _min_4__T: ...
    @typing.overload
    @staticmethod
    def min(t: _min_5__T, t2: _min_5__T) -> _min_5__T: ...
    @typing.overload
    @staticmethod
    def multiplyExact(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def multiplyExact(long: int, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def multiplyExact(long: int, long2: int) -> int: ...
    @staticmethod
    def multiplyFull(int: int, int2: int) -> int: ...
    @staticmethod
    def multiplyHigh(long: int, long2: int) -> int: ...
    @typing.overload
    @staticmethod
    def negateExact(int: int) -> int: ...
    @typing.overload
    @staticmethod
    def negateExact(long: int) -> int: ...
    @typing.overload
    @staticmethod
    def nextAfter(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextAfter(float: float, double: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextDown(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextDown(float: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextUp(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def nextUp(float: float) -> float: ...
    _norm__T = typing.TypeVar('_norm__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def norm(t: _norm__T) -> float: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_4__T = typing.TypeVar('_pow_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_5__T = typing.TypeVar('_pow_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def pow(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def pow(double: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def pow(double: float, long: int) -> float: ...
    @typing.overload
    @staticmethod
    def pow(t: _pow_3__T, double: float) -> _pow_3__T: ...
    @typing.overload
    @staticmethod
    def pow(t: _pow_4__T, int: int) -> _pow_4__T: ...
    @typing.overload
    @staticmethod
    def pow(t: _pow_5__T, t2: _pow_5__T) -> _pow_5__T: ...
    @staticmethod
    def random() -> float: ...
    _rint_1__T = typing.TypeVar('_rint_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rint(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def rint(t: _rint_1__T) -> _rint_1__T: ...
    _round_2__T = typing.TypeVar('_round_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def round(float: float) -> int: ...
    @typing.overload
    @staticmethod
    def round(double: float) -> int: ...
    @typing.overload
    @staticmethod
    def round(t: _round_2__T) -> int: ...
    _scalb_2__T = typing.TypeVar('_scalb_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def scalb(double: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def scalb(float: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def scalb(t: _scalb_2__T, int: int) -> _scalb_2__T: ...
    _sign__T = typing.TypeVar('_sign__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def sign(t: _sign__T) -> _sign__T: ...
    @typing.overload
    @staticmethod
    def signum(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def signum(float: float) -> float: ...
    _sin_1__T = typing.TypeVar('_sin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sin(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def sin(t: _sin_1__T) -> _sin_1__T: ...
    _sinCos_0__T = typing.TypeVar('_sinCos_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sinCos(t: _sinCos_0__T) -> 'FieldSinCos'[_sinCos_0__T]: ...
    @typing.overload
    @staticmethod
    def sinCos(double: float) -> 'SinCos': ...
    _sinh_1__T = typing.TypeVar('_sinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sinh(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def sinh(t: _sinh_1__T) -> _sinh_1__T: ...
    _sinhCosh_0__T = typing.TypeVar('_sinhCosh_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sinhCosh(t: _sinhCosh_0__T) -> 'FieldSinhCosh'[_sinhCosh_0__T]: ...
    @typing.overload
    @staticmethod
    def sinhCosh(double: float) -> 'SinhCosh': ...
    _sqrt_1__T = typing.TypeVar('_sqrt_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def sqrt(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def sqrt(t: _sqrt_1__T) -> _sqrt_1__T: ...
    @typing.overload
    @staticmethod
    def subtractExact(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def subtractExact(long: int, long2: int) -> int: ...
    _tan_1__T = typing.TypeVar('_tan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tan(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def tan(t: _tan_1__T) -> _tan_1__T: ...
    _tanh_1__T = typing.TypeVar('_tanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tanh(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def tanh(t: _tanh_1__T) -> _tanh_1__T: ...
    _toDegrees_1__T = typing.TypeVar('_toDegrees_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def toDegrees(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def toDegrees(t: _toDegrees_1__T) -> _toDegrees_1__T: ...
    @staticmethod
    def toIntExact(long: int) -> int: ...
    _toRadians_1__T = typing.TypeVar('_toRadians_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def toRadians(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def toRadians(t: _toRadians_1__T) -> _toRadians_1__T: ...
    _ulp_2__T = typing.TypeVar('_ulp_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def ulp(double: float) -> float: ...
    @typing.overload
    @staticmethod
    def ulp(float: float) -> float: ...
    @typing.overload
    @staticmethod
    def ulp(t: _ulp_2__T) -> _ulp_2__T: ...

_FieldSinCos__T = typing.TypeVar('_FieldSinCos__T')  # <T>
class FieldSinCos(typing.Generic[_FieldSinCos__T]):
    """
    public class FieldSinCos<T> extends Object
    
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
    public class FieldSinhCosh<T> extends Object
    
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
    public class FieldTuple<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.util.FieldTuple`<T>>
    
        This class allows to perform the same computation of all components of a Tuple at once.
    
        Since:
            1.2
    """
    def __init__(self, tArray: typing.List[_FieldTuple__T]): ...
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
                 in class 
        
        
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
                 in class 
        
        
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
    public class Incrementor extends Object
    
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
    public class IterationEvent extends EventObject
    
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
    public interface IterationListener extends EventListener
    
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
    public class IterationManager extends Object
    
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
    public class KthSelector extends Object implements Serializable
    
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
    _buildArray_0__T = typing.TypeVar('_buildArray_0__T', bound=org.hipparchus.FieldElement)  # <T>
    _buildArray_1__T = typing.TypeVar('_buildArray_1__T', bound=org.hipparchus.FieldElement)  # <T>
    _buildArray_2__T = typing.TypeVar('_buildArray_2__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def buildArray(field: org.hipparchus.Field[_buildArray_0__T], int: int) -> typing.List[_buildArray_0__T]: ...
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
    def checkEqualLength(doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(intArray: typing.List[int], intArray2: typing.List[int], boolean: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(tArray: typing.List[_checkEqualLength_2__T], tArray2: typing.List[_checkEqualLength_2__T], boolean: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(intArray: typing.List[int], intArray2: typing.List[int]) -> None: ...
    @typing.overload
    @staticmethod
    def checkEqualLength(tArray: typing.List[_checkEqualLength_5__T], tArray2: typing.List[_checkEqualLength_5__T]) -> None: ...
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
    def concatenate(doubleArray: typing.List[typing.List[float]]) -> typing.List[float]: ...
    @staticmethod
    def convolve(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def cosAngle(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> float: ...
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
    def equals(byteArray: typing.List[int], byteArray2: typing.List[int]) -> bool: ...
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
    def equalsIncludingNaN(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> bool: ...
    @typing.overload
    @staticmethod
    def equalsIncludingNaN(floatArray: typing.List[float], floatArray2: typing.List[float]) -> bool: ...
    _isMonotonic_1__T = typing.TypeVar('_isMonotonic_1__T', bound=java.lang.Comparable)  # <T>
    @typing.overload
    @staticmethod
    def isMonotonic(doubleArray: typing.List[float], orderDirection: 'MathArrays.OrderDirection', boolean: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def isMonotonic(tArray: typing.List[_isMonotonic_1__T], orderDirection: 'MathArrays.OrderDirection', boolean: bool) -> bool: ...
    @typing.overload
    @staticmethod
    def linearCombination(double: float, double2: float, double3: float, double4: float) -> float: ...
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
    def natural(int: int) -> typing.List[int]: ...
    @staticmethod
    def normalizeArray(doubleArray: typing.List[float], double2: float) -> typing.List[float]: ...
    @staticmethod
    def safeNorm(doubleArray: typing.List[float]) -> float: ...
    @staticmethod
    def scale(double: float, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def scaleInPlace(double: float, doubleArray: typing.List[float]) -> None: ...
    @staticmethod
    def sequence(int: int, int2: int, int3: int) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int]) -> None: ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int], int2: int, position: 'MathArrays.Position') -> None: ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int], int2: int, position: 'MathArrays.Position', randomGenerator: org.hipparchus.random.RandomGenerator) -> None: ...
    @typing.overload
    @staticmethod
    def shuffle(intArray: typing.List[int], randomGenerator: org.hipparchus.random.RandomGenerator) -> None: ...
    @typing.overload
    @staticmethod
    def sortInPlace(doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]]) -> None: ...
    @typing.overload
    @staticmethod
    def sortInPlace(doubleArray: typing.List[float], orderDirection: 'MathArrays.OrderDirection', doubleArray2: typing.List[typing.List[float]]) -> None: ...
    @staticmethod
    def unique(doubleArray: typing.List[float]) -> typing.List[float]: ...
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
    TWO_PI: typing.ClassVar[float] = ...
    PI_SQUARED: typing.ClassVar[float] = ...
    SEMI_PI: typing.ClassVar[float] = ...
    @staticmethod
    def checkDimension(int: int, int2: int) -> None: ...
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
    def checkNotNull(object: typing.Any, localizable: org.hipparchus.exception.Localizable, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def checkRangeInclusive(double: float, double2: float, double3: float) -> None: ...
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
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def hash(double: float) -> int: ...
    @typing.overload
    @staticmethod
    def hash(doubleArray: typing.List[float]) -> int: ...
    _max__T = typing.TypeVar('_max__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def max(t: _max__T, t2: _max__T) -> _max__T: ...
    _min__T = typing.TypeVar('_min__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def min(t: _min__T, t2: _min__T) -> _min__T: ...
    _normalizeAngle_1__T = typing.TypeVar('_normalizeAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def normalizeAngle(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def normalizeAngle(t: _normalizeAngle_1__T, t2: _normalizeAngle_1__T) -> _normalizeAngle_1__T: ...
    @staticmethod
    def reduce(double: float, double2: float, double3: float) -> float: ...
    _twoSum_0__T = typing.TypeVar('_twoSum_0__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def twoSum(t: _twoSum_0__T, t2: _twoSum_0__T) -> 'MathUtils.FieldSumAndResidual'[_twoSum_0__T]: ...
    @typing.overload
    @staticmethod
    def twoSum(double: float, double2: float) -> 'MathUtils.SumAndResidual': ...
    class FieldSumAndResidual(typing.Generic[_MathUtils__FieldSumAndResidual__T]):
        def getResidual(self) -> _MathUtils__FieldSumAndResidual__T: ...
        def getSum(self) -> _MathUtils__FieldSumAndResidual__T: ...
    class SumAndResidual:
        def getResidual(self) -> float: ...
        def getSum(self) -> float: ...

class MultidimensionalCounter(java.lang.Iterable[int]):
    """
    public class MultidimensionalCounter extends Object implements Iterable<Integer>
    
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
    def __init__(self, intArray: typing.List[int]): ...
    def getCount(self, intArray: typing.List[int]) -> int: ...
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
                 in interface 
        
            Returns:
                the iterator.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
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
    public class OpenIntToDoubleHashMap extends Object implements Serializable
    
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
    public class OpenIntToFieldHashMap<T extends :class:`~org.hipparchus.FieldElement`<T>> extends Object implements Serializable
    
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
    public class Pair<K,V> extends Object
    
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
            Convenience factory method that calls the :meth:`~org.hipparchus.util.Pair.Pair`.
        
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
                 in class 
        
            Parameters:
                o (Object): Object.
        
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
                 in class 
        
            Returns:
                the hash code value.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class PivotingStrategy(java.lang.Enum['PivotingStrategy']):
    """
    public enum PivotingStrategy extends Enum<:class:`~org.hipparchus.util.PivotingStrategy`>
    
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
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
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
    EPSILON: typing.ClassVar[float] = ...
    SAFE_MIN: typing.ClassVar[float] = ...
    @typing.overload
    @staticmethod
    def compareTo(double: float, double2: float, double3: float) -> int: ...
    @typing.overload
    @staticmethod
    def compareTo(double: float, double2: float, int: int) -> int: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
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
    def equalsIncludingNaN(double: float, double2: float) -> bool: ...
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
    def equalsWithRelativeTolerance(double: float, double2: float, double3: float) -> bool: ...
    @typing.overload
    @staticmethod
    def isMathematicalInteger(double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def isMathematicalInteger(float: float) -> bool: ...
    @staticmethod
    def representableDelta(double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def round(double: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def round(double: float, int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def round(float: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def round(float: float, int: int, int2: int) -> float: ...

class ResizableDoubleArray(java.io.Serializable):
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
    def __init__(self, int: int, double: float, double2: float, expansionMode: 'ResizableDoubleArray.ExpansionMode', doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, resizableDoubleArray: 'ResizableDoubleArray'): ...
    def addElement(self, double: float) -> None: ...
    def addElementRolling(self, double: float) -> float: ...
    def addElements(self, doubleArray: typing.List[float]) -> None: ...
    def clear(self) -> None: ...
    def compute(self, function: MathArrays.Function) -> float: ...
    def contract(self) -> None: ...
    def copy(self) -> 'ResizableDoubleArray': ...
    def discardFrontElements(self, int: int) -> None: ...
    def discardMostRecentElements(self, int: int) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCapacity(self) -> int: ...
    def getContractionCriterion(self) -> float: ...
    def getElement(self, int: int) -> float: ...
    def getElements(self) -> typing.List[float]: ...
    def getExpansionFactor(self) -> float: ...
    def getExpansionMode(self) -> 'ResizableDoubleArray.ExpansionMode': ...
    def getNumElements(self) -> int: ...
    def hashCode(self) -> int: ...
    def setElement(self, int: int, double: float) -> None: ...
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

class RyuDouble:
    DEFAULT_LOW_EXP: typing.ClassVar[int] = ...
    DEFAULT_HIGH_EXP: typing.ClassVar[int] = ...
    @typing.overload
    @staticmethod
    def doubleToString(double: float) -> str: ...
    @typing.overload
    @staticmethod
    def doubleToString(double: float, int: int, int2: int) -> str: ...

class SinCos:
    """
    public class SinCos extends Object
    
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
    public class SinhCosh extends Object
    
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
    public class Tuple extends Object implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.util.Tuple`>
    
        This class allows to perform the same computation of all components of a Tuple at once.
    
        Since:
            1.2
    """
    def __init__(self, doubleArray: typing.List[float]): ...
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
                 in class 
        
        
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
            Get the Archimedes constant Ï€.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant Ï€
        
        
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
                 in class 
        
        
        """
        ...
    def hypot(self, tuple: 'Tuple') -> 'Tuple':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2` Â +*y* :sup:`2` )
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
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
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
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
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
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
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
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
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
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
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
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
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
        
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.util")``.

    ArithmeticUtils: typing.Type[ArithmeticUtils]
    BigReal: typing.Type[BigReal]
    BigRealField: typing.Type[BigRealField]
    Combinations: typing.Type[Combinations]
    CombinatoricsUtils: typing.Type[CombinatoricsUtils]
    CompositeFormat: typing.Type[CompositeFormat]
    ContinuedFraction: typing.Type[ContinuedFraction]
    Decimal64: typing.Type[Decimal64]
    Decimal64Field: typing.Type[Decimal64Field]
    FastMath: typing.Type[FastMath]
    FieldSinCos: typing.Type[FieldSinCos]
    FieldSinhCosh: typing.Type[FieldSinhCosh]
    FieldTuple: typing.Type[FieldTuple]
    Incrementor: typing.Type[Incrementor]
    IterationEvent: typing.Type[IterationEvent]
    IterationListener: typing.Type[IterationListener]
    IterationManager: typing.Type[IterationManager]
    KthSelector: typing.Type[KthSelector]
    MathArrays: typing.Type[MathArrays]
    MathUtils: typing.Type[MathUtils]
    MultidimensionalCounter: typing.Type[MultidimensionalCounter]
    OpenIntToDoubleHashMap: typing.Type[OpenIntToDoubleHashMap]
    OpenIntToFieldHashMap: typing.Type[OpenIntToFieldHashMap]
    Pair: typing.Type[Pair]
    PivotingStrategy: typing.Type[PivotingStrategy]
    Precision: typing.Type[Precision]
    ResizableDoubleArray: typing.Type[ResizableDoubleArray]
    RyuDouble: typing.Type[RyuDouble]
    SinCos: typing.Type[SinCos]
    SinhCosh: typing.Type[SinhCosh]
    Tuple: typing.Type[Tuple]
