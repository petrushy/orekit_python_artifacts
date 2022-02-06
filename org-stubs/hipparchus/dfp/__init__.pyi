import java.lang
import org.hipparchus
import org.hipparchus.util
import typing



class Dfp(org.hipparchus.CalculusFieldElement['Dfp']):
    RADIX: typing.ClassVar[int] = ...
    MIN_EXP: typing.ClassVar[int] = ...
    MAX_EXP: typing.ClassVar[int] = ...
    ERR_SCALE: typing.ClassVar[int] = ...
    FINITE: typing.ClassVar[int] = ...
    INFINITE: typing.ClassVar[int] = ...
    SNAN: typing.ClassVar[int] = ...
    QNAN: typing.ClassVar[int] = ...
    def __init__(self, dfp: 'Dfp'): ...
    def abs(self) -> 'Dfp': ...
    def acos(self) -> 'Dfp': ...
    def acosh(self) -> 'Dfp': ...
    @typing.overload
    def add(self, double: float) -> 'Dfp': ...
    @typing.overload
    def add(self, dfp: 'Dfp') -> 'Dfp': ...
    def asin(self) -> 'Dfp': ...
    def asinh(self) -> 'Dfp': ...
    def atan(self) -> 'Dfp': ...
    def atan2(self, dfp: 'Dfp') -> 'Dfp': ...
    def atanh(self) -> 'Dfp': ...
    def cbrt(self) -> 'Dfp': ...
    def ceil(self) -> 'Dfp': ...
    def classify(self) -> int: ...
    @typing.overload
    def copySign(self, double: float) -> 'Dfp': ...
    @typing.overload
    def copySign(self, dfp: 'Dfp') -> 'Dfp': ...
    @staticmethod
    def copysign(dfp: 'Dfp', dfp2: 'Dfp') -> 'Dfp': ...
    def cos(self) -> 'Dfp': ...
    def cosh(self) -> 'Dfp': ...
    @typing.overload
    def divide(self, double: float) -> 'Dfp': ...
    @typing.overload
    def divide(self, int: int) -> 'Dfp': ...
    @typing.overload
    def divide(self, dfp: 'Dfp') -> 'Dfp': ...
    def dotrap(self, int: int, string: str, dfp: 'Dfp', dfp2: 'Dfp') -> 'Dfp': ...
    def equals(self, object: typing.Any) -> bool: ...
    def exp(self) -> 'Dfp': ...
    def expm1(self) -> 'Dfp': ...
    def floor(self) -> 'Dfp': ...
    def getExponent(self) -> int: ...
    def getField(self) -> 'DfpField': ...
    def getOne(self) -> 'Dfp': ...
    def getPi(self) -> 'Dfp': ...
    def getRadixDigits(self) -> int: ...
    def getReal(self) -> float: ...
    def getTwo(self) -> 'Dfp': ...
    def getZero(self) -> 'Dfp': ...
    def greaterThan(self, dfp: 'Dfp') -> bool: ...
    def hashCode(self) -> int: ...
    def hypot(self, dfp: 'Dfp') -> 'Dfp': ...
    def intLog10(self) -> int: ...
    def intValue(self) -> int: ...
    def isInfinite(self) -> bool: ...
    def isNaN(self) -> bool: ...
    def isZero(self) -> bool: ...
    def lessThan(self, dfp: 'Dfp') -> bool: ...
    @typing.overload
    def linearCombination(self, double: float, dfp: 'Dfp', double2: float, dfp2: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, double: float, dfp: 'Dfp', double2: float, dfp2: 'Dfp', double3: float, dfp3: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, double: float, dfp: 'Dfp', double2: float, dfp2: 'Dfp', double3: float, dfp3: 'Dfp', double4: float, dfp4: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], dfpArray: typing.List['Dfp']) -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfp: 'Dfp', dfp2: 'Dfp', dfp3: 'Dfp', dfp4: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfp: 'Dfp', dfp2: 'Dfp', dfp3: 'Dfp', dfp4: 'Dfp', dfp5: 'Dfp', dfp6: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfp: 'Dfp', dfp2: 'Dfp', dfp3: 'Dfp', dfp4: 'Dfp', dfp5: 'Dfp', dfp6: 'Dfp', dfp7: 'Dfp', dfp8: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfpArray: typing.List['Dfp'], dfpArray2: typing.List['Dfp']) -> 'Dfp': ...
    def log(self) -> 'Dfp': ...
    def log10(self) -> 'Dfp': ...
    def log10K(self) -> int: ...
    def log1p(self) -> 'Dfp': ...
    @typing.overload
    def multiply(self, double: float) -> 'Dfp': ...
    @typing.overload
    def multiply(self, int: int) -> 'Dfp': ...
    @typing.overload
    def multiply(self, dfp: 'Dfp') -> 'Dfp': ...
    def negate(self) -> 'Dfp': ...
    def negativeOrNull(self) -> bool: ...
    @typing.overload
    def newInstance(self) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, byte: int) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, byte: int, byte2: int) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, double: float) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, int: int) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, string: str) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, long: int) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, dfp: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def newInstance(self, dfpField: 'DfpField', roundingMode: 'DfpField.RoundingMode') -> 'Dfp': ...
    def nextAfter(self, dfp: 'Dfp') -> 'Dfp': ...
    def positiveOrNull(self) -> bool: ...
    @typing.overload
    def pow(self, double: float) -> 'Dfp': ...
    @typing.overload
    def pow(self, int: int) -> 'Dfp': ...
    @typing.overload
    def pow(self, dfp: 'Dfp') -> 'Dfp': ...
    def power10(self, int: int) -> 'Dfp': ...
    def power10K(self, int: int) -> 'Dfp': ...
    def reciprocal(self) -> 'Dfp': ...
    @typing.overload
    def remainder(self, double: float) -> 'Dfp': ...
    @typing.overload
    def remainder(self, dfp: 'Dfp') -> 'Dfp': ...
    def rint(self) -> 'Dfp': ...
    def rootN(self, int: int) -> 'Dfp': ...
    def scalb(self, int: int) -> 'Dfp': ...
    def sign(self) -> 'Dfp': ...
    def sin(self) -> 'Dfp': ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['Dfp']: ...
    def sinh(self) -> 'Dfp': ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['Dfp']: ...
    def sqrt(self) -> 'Dfp': ...
    def strictlyNegative(self) -> bool: ...
    def strictlyPositive(self) -> bool: ...
    @typing.overload
    def subtract(self, double: float) -> 'Dfp': ...
    @typing.overload
    def subtract(self, dfp: 'Dfp') -> 'Dfp': ...
    def tan(self) -> 'Dfp': ...
    def tanh(self) -> 'Dfp': ...
    def toDegrees(self) -> 'Dfp': ...
    def toDouble(self) -> float: ...
    def toRadians(self) -> 'Dfp': ...
    def toSplitDouble(self) -> typing.List[float]: ...
    def toString(self) -> str: ...
    def ulp(self) -> 'Dfp': ...
    def unequal(self, dfp: 'Dfp') -> bool: ...

class DfpField(org.hipparchus.Field[Dfp]):
    """
    public class DfpField extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.dfp.Dfp`>
    
        Field for Decimal floating point instances.
    """
    FLAG_INVALID: typing.ClassVar[int] = ...
    """
    public static final int FLAG_INVALID
    
        IEEE 854-1987 flag for invalid operation.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLAG_DIV_ZERO: typing.ClassVar[int] = ...
    """
    public static final int FLAG_DIV_ZERO
    
        IEEE 854-1987 flag for division by zero.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLAG_OVERFLOW: typing.ClassVar[int] = ...
    """
    public static final int FLAG_OVERFLOW
    
        IEEE 854-1987 flag for overflow.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLAG_UNDERFLOW: typing.ClassVar[int] = ...
    """
    public static final int FLAG_UNDERFLOW
    
        IEEE 854-1987 flag for underflow.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLAG_INEXACT: typing.ClassVar[int] = ...
    """
    public static final int FLAG_INEXACT
    
        IEEE 854-1987 flag for inexact result.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, int: int): ...
    def clearIEEEFlags(self) -> None:
        """
            Clears the IEEE 854 status flags.
        
            Also see:
                :meth:`~org.hipparchus.dfp.DfpField.getIEEEFlags`, :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlags`,
                :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlagsBits`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        """
        ...
    @staticmethod
    def computeExp(dfp: Dfp, dfp2: Dfp) -> Dfp:
        """
            Compute exp(a).
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number for which we want the exponential
                one (:class:`~org.hipparchus.dfp.Dfp`): constant with value 1 at desired precision
        
            Returns:
                exp(a)
        
        
        """
        ...
    @staticmethod
    def computeLn(dfp: Dfp, dfp2: Dfp, dfp3: Dfp) -> Dfp:
        """
            Compute ln(a). Let f(x) = ln(x), We know that f'(x) = 1/x, thus from Taylor's theorem we have: ----- n+1 n f(x) = \ (-1)
            (x - 1) / ---------------- for 1 <= n <= infinity ----- n or 2 3 4 (x-1) (x-1) (x-1) ln(x) = (x-1) - ----- + ------ -
            ------ + ... 2 3 4 alternatively, 2 3 4 x x x ln(x+1) = x - - + - - - + ... 2 3 4 This series can be used to compute
            ln(x), but it converges too slowly. If we substitute -x for x above, we get 2 3 4 x x x ln(1-x) = -x - - - - - - + ... 2
            3 4 Note that all terms are now negative. Because the even powered ones absorbed the sign. Now, subtract the series
            above from the previous one to get ln(x+1) - ln(1-x). Note the even terms cancel out leaving only the odd ones 3 5 7 2x
            2x 2x ln(x+1) - ln(x-1) = 2x + --- + --- + ---- + ... 3 5 7 By the property of logarithms that ln(a) - ln(b) = ln (a/b)
            we have: 3 5 7 x+1 / x x x \ ln ----- = 2 * | x + ---- + ---- + ---- + ... | x-1 \ 3 5 7 / But now we want to find
            ln(a), so we need to find the value of x such that a = (x+1)/(x-1). This is easily solved to find that x = (a-1)/(a+1).
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number for which we want the exponential
                one (:class:`~org.hipparchus.dfp.Dfp`): constant with value 1 at desired precision
                two (:class:`~org.hipparchus.dfp.Dfp`): constant with value 2 at desired precision
        
            Returns:
                ln(a)
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Two fields are considered equals if they have the same number of radix digits and the same rounding mode.
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getDegToRad(self) -> Dfp:
        """
            Get the degrees to radians conversion factor.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` for degrees to radians conversion factor
        
        
        """
        ...
    def getE(self) -> Dfp:
        """
            Get the constant e.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value e
        
        
        """
        ...
    def getESplit(self) -> typing.List[Dfp]:
        """
            Get the constant e split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value e split in two pieces
        
        
        """
        ...
    def getExtendedField(self, int: int, boolean: bool) -> 'DfpField':
        """
            Get extended field for accuracy conversion.
        
            Parameters:
                digitsFactor (int): multiplication factor for number of digits
                computeConstants (boolean): if true, the transcendental constants for the given precision must be computed (setting this flag to false is RESERVED
                    for the internal recursive call)
        
            Returns:
                field with extended precision
        
            Since:
                1.7
        
        
        """
        ...
    def getIEEEFlags(self) -> int:
        """
            Get the IEEE 854 status flags.
        
            Returns:
                IEEE 854 status flags
        
            Also see:
                :meth:`~org.hipparchus.dfp.DfpField.clearIEEEFlags`, :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlags`,
                :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlagsBits`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        """
        ...
    def getLn10(self) -> Dfp:
        """
            Get the constant ln(10).
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(10)
        
        
        """
        ...
    def getLn2(self) -> Dfp:
        """
            Get the constant ln(2).
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(2)
        
        
        """
        ...
    def getLn2Split(self) -> typing.List[Dfp]:
        """
            Get the constant ln(2) split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(2) split in two pieces
        
        
        """
        ...
    def getLn5(self) -> Dfp:
        """
            Get the constant ln(5).
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(5)
        
        
        """
        ...
    def getLn5Split(self) -> typing.List[Dfp]:
        """
            Get the constant ln(5) split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(5) split in two pieces
        
        
        """
        ...
    def getOne(self) -> Dfp:
        """
            Get the constant 1.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value 1
        
        
        """
        ...
    def getPi(self) -> Dfp:
        """
            Get the constant π.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value π
        
        
        """
        ...
    def getPiSplit(self) -> typing.List[Dfp]:
        """
            Get the constant π split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value π split in two pieces
        
        
        """
        ...
    def getRadToDeg(self) -> Dfp:
        """
            Get the radians to degrees conversion factor.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` for radians to degrees conversion factor
        
        
        """
        ...
    def getRadixDigits(self) -> int:
        """
            Get the number of radix digits of the :class:`~org.hipparchus.dfp.Dfp` instances built by this factory.
        
            Returns:
                number of radix digits
        
        
        """
        ...
    def getRoundingMode(self) -> 'DfpField.RoundingMode':
        """
            Get the current rounding mode.
        
            Returns:
                current rounding mode
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Dfp]: ...
    def getSqr2(self) -> Dfp:
        """
            Get the constant √2.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √2
        
        
        """
        ...
    def getSqr2Reciprocal(self) -> Dfp:
        """
            Get the constant √2 / 2.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √2 / 2
        
        
        """
        ...
    def getSqr2Split(self) -> typing.List[Dfp]:
        """
            Get the constant √2 split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √2 split in two pieces
        
        
        """
        ...
    def getSqr3(self) -> Dfp:
        """
            Get the constant √3.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √3
        
        
        """
        ...
    def getSqr3Reciprocal(self) -> Dfp:
        """
            Get the constant √3 / 3.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √3 / 3
        
        
        """
        ...
    def getTwo(self) -> Dfp:
        """
            Get the constant 2.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value 2
        
        
        """
        ...
    def getZero(self) -> Dfp:
        """
            Get the constant 0.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getZero` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value 0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def newDfp(self) -> Dfp:
        """
            Makes a :class:`~org.hipparchus.dfp.Dfp` with a value of 0.
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with a value of 0
        
        """
        ...
    @typing.overload
    def newDfp(self, byte: int) -> Dfp:
        """
            Create an instance from a byte value.
        
            Parameters:
                x (byte): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Create an instance from an int value.
        
            Parameters:
                x (int): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Create an instance from a long value.
        
            Parameters:
                x (long): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Create an instance from a double value.
        
            Parameters:
                x (double): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Copy constructor.
        
            Parameters:
                d (:class:`~org.hipparchus.dfp.Dfp`): instance to copy
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as d
        
            Create a :class:`~org.hipparchus.dfp.Dfp` given a String representation.
        
            Parameters:
                s (String): string representation of the instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` parsed from specified string
        
            Creates a :class:`~org.hipparchus.dfp.Dfp` with a non-finite value.
        
            Parameters:
                sign (byte): sign of the Dfp to create
                nans (byte): code of the value, must be one of :meth:`~org.hipparchus.dfp.Dfp.INFINITE`, :meth:`~org.hipparchus.dfp.Dfp.SNAN`,
                    :meth:`~org.hipparchus.dfp.Dfp.QNAN`
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with a non-finite value
        
        
        """
        ...
    @typing.overload
    def newDfp(self, byte: int, byte2: int) -> Dfp: ...
    @typing.overload
    def newDfp(self, double: float) -> Dfp: ...
    @typing.overload
    def newDfp(self, int: int) -> Dfp: ...
    @typing.overload
    def newDfp(self, string: str) -> Dfp: ...
    @typing.overload
    def newDfp(self, long: int) -> Dfp: ...
    @typing.overload
    def newDfp(self, dfp: Dfp) -> Dfp: ...
    def setIEEEFlags(self, int: int) -> None:
        """
            Sets the IEEE 854 status flags.
        
            Parameters:
                flags (int): desired value for the flags
        
            Also see:
                :meth:`~org.hipparchus.dfp.DfpField.getIEEEFlags`, :meth:`~org.hipparchus.dfp.DfpField.clearIEEEFlags`,
                :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlagsBits`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        """
        ...
    def setIEEEFlagsBits(self, int: int) -> None:
        """
            Sets some bits in the IEEE 854 status flags, without changing the already set bits.
        
            Calling this method is equivalent to call :code:`setIEEEFlags(getIEEEFlags() | bits)`
        
            Parameters:
                bits (int): bits to set
        
            Also see:
                :meth:`~org.hipparchus.dfp.DfpField.getIEEEFlags`, :meth:`~org.hipparchus.dfp.DfpField.clearIEEEFlags`,
                :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlags`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`,
                :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`, :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        """
        ...
    def setRoundingMode(self, roundingMode: 'DfpField.RoundingMode') -> None:
        """
            Set the rounding mode. If not set, the default value is
            :meth:`~org.hipparchus.dfp.DfpField.RoundingMode.ROUND_HALF_EVEN`.
        
            Parameters:
                mode (:class:`~org.hipparchus.dfp.DfpField.RoundingMode`): desired rounding mode Note that the rounding mode is common to all :class:`~org.hipparchus.dfp.Dfp` instances belonging
                    to the current :class:`~org.hipparchus.dfp.DfpField` in the system and will affect all future calculations.
        
        
        """
        ...
    class RoundingMode(java.lang.Enum['DfpField.RoundingMode']):
        ROUND_DOWN: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_UP: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_UP: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_DOWN: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_EVEN: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_ODD: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_CEIL: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_FLOOR: typing.ClassVar['DfpField.RoundingMode'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'DfpField.RoundingMode': ...
        @staticmethod
        def values() -> typing.List['DfpField.RoundingMode']: ...

class DfpMath:
    """
    public class DfpMath extends Object
    
        Mathematical routines for use with :class:`~org.hipparchus.dfp.Dfp`. The constants are defined in
        :class:`~org.hipparchus.dfp.DfpField`
    """
    @staticmethod
    def acos(dfp: Dfp) -> Dfp:
        """
            computes the arc-cosine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which arc-cosine is desired
        
            Returns:
                acos(a)
        
        
        """
        ...
    @staticmethod
    def asin(dfp: Dfp) -> Dfp:
        """
            computes the arc-sine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which arc-sine is desired
        
            Returns:
                asin(a)
        
        
        """
        ...
    @staticmethod
    def atan(dfp: Dfp) -> Dfp:
        """
            computes the arc tangent of the argument Uses the typical taylor series but may reduce arguments using the following
            identity tan(x+y) = (tan(x) + tan(y)) / (1 - tan(x)*tan(y)) since tan(PI/8) = sqrt(2)-1, atan(x) = atan( (x - sqrt(2) +
            1) / (1+x*sqrt(2) - x) + PI/8.0
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which arc-tangent is desired
        
            Returns:
                atan(a)
        
        
        """
        ...
    @staticmethod
    def cos(dfp: Dfp) -> Dfp:
        """
            computes the cosine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which cosine is desired
        
            Returns:
                cos(a)
        
        
        """
        ...
    @staticmethod
    def exp(dfp: Dfp) -> Dfp:
        """
            Computes e to the given power. a is broken into two parts, such that a = n+m where n is an integer. We use pow() to
            compute e :sup:`n` and a Taylor series to compute e :sup:`m` . We return e* :sup:`n` Ã— e :sup:`m`
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): power at which e should be raised
        
            Returns:
                e :sup:`a`
        
        
        """
        ...
    @staticmethod
    def log(dfp: Dfp) -> Dfp:
        """
            Returns the natural logarithm of a. a is first split into three parts such that a = (10000^h)(2^j)k. ln(a) is computed
            by ln(a) = ln(5)*h + ln(2)*(h+j) + ln(k) k is in the range 2/3 < k < 4/3 and is passed on to a series expansion.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which logarithm is requested
        
            Returns:
                log(a)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def pow(dfp: Dfp, int: int) -> Dfp:
        """
            Raises base to the power a by successive squaring.
        
            Parameters:
                base (:class:`~org.hipparchus.dfp.Dfp`): number to raise
                a (int): power
        
            Returns:
                base :sup:`a`
        
            Computes x to the y power.
        
            Uses the following method:
        
        
              1.  Set u = rint(y), v = y-u
              2.  Compute a = v * ln(x)
              3.  Compute b = rint( a/ln(2) )
              4.  Compute c = a - b*ln(2)
              5.  x :sup:`y` = x :sup:`u` * 2 :sup:`b` * e :sup:`c`
        
            if |y| > 1e8, then we compute by exp(y*ln(x))
        
            **Special Cases**
        
        
              - if y is 0.0 or -0.0 then result is 1.0
              - if y is 1.0 then result is x
              - if y is NaN then result is NaN
              - if x is NaN and y is not zero then result is NaN
              - if |x| > 1.0 and y is +Infinity then result is +Infinity
              - if |x| < 1.0 and y is -Infinity then result is +Infinity
              - if |x| > 1.0 and y is -Infinity then result is +0
              - if |x| < 1.0 and y is +Infinity then result is +0
              - if |x| = 1.0 and y is +/-Infinity then result is NaN
              - if x = +0 and y > 0 then result is +0
              - if x = +Inf and y < 0 then result is +0
              - if x = +0 and y < 0 then result is +Inf
              - if x = +Inf and y > 0 then result is +Inf
              - if x = -0 and y > 0, finite, not odd integer then result is +0
              - if x = -0 and y < 0, finite, and odd integer then result is -Inf
              - if x = -Inf and y > 0, finite, and odd integer then result is -Inf
              - if x = -0 and y < 0, not finite odd integer then result is +Inf
              - if x = -Inf and y > 0, not finite odd integer then result is +Inf
              - if x < 0 and y > 0, finite, and odd integer then result is -(|x| :sup:`y` )
              - if x < 0 and y > 0, finite, and not integer then result is NaN
        
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): base to be raised
                y (:class:`~org.hipparchus.dfp.Dfp`): power to which base should be raised
        
            Returns:
                x :sup:`y`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def pow(dfp: Dfp, dfp2: Dfp) -> Dfp: ...
    @staticmethod
    def sin(dfp: Dfp) -> Dfp:
        """
            computes the sine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which sine is desired
        
            Returns:
                sin(a)
        
        
        """
        ...
    @staticmethod
    def tan(dfp: Dfp) -> Dfp:
        """
            computes the tangent of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which tangent is desired
        
            Returns:
                tan(a)
        
        
        """
        ...

class DfpDec(Dfp):
    """
    public class DfpDec extends :class:`~org.hipparchus.dfp.Dfp`
    
        Subclass of :class:`~org.hipparchus.dfp.Dfp` which hides the radix-10000 artifacts of the superclass. This should give
        outward appearances of being a decimal number with DIGITS*4-3 decimal digits. This class can be subclassed to appear to
        be an arbitrary number of decimal digits less than DIGITS*4-3.
    """
    def __init__(self, dfp: Dfp): ...
    @typing.overload
    def newInstance(self, dfpField: DfpField, roundingMode: DfpField.RoundingMode) -> Dfp:
        """
            Creates an instance with a non-finite value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                sign (byte): sign of the Dfp to create
                nans (byte): code of the value, must be one of :meth:`~org.hipparchus.dfp.Dfp.INFINITE`, :meth:`~org.hipparchus.dfp.Dfp.SNAN`,
                    :meth:`~org.hipparchus.dfp.Dfp.QNAN`
        
            Returns:
                a new instance with a non-finite value
        
        
        """
        ...
    @typing.overload
    def newInstance(self) -> Dfp:
        """
            Create an instance with a value of 0. Use this internally in preference to constructors to facilitate subclasses
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Returns:
                a new instance with a value of 0
        
        """
        ...
    @typing.overload
    def newInstance(self, byte: int) -> Dfp:
        """
            Create an instance from a byte value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (byte): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance from an int value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (int): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance from a long value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (long): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
            Create an instance by copying an existing one. Use this internally in preference to constructors to facilitate
            subclasses.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                d (:class:`~org.hipparchus.dfp.Dfp`): instance to copy
        
            Returns:
                a new instance with the same value as d
        
            Create an instance from a String representation. Use this internally in preference to constructors to facilitate
            subclasses.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                s (String): string representation of the instance
        
            Returns:
                a new instance parsed from specified string
        
        """
        ...
    @typing.overload
    def newInstance(self, byte: int, byte2: int) -> Dfp: ...
    @typing.overload
    def newInstance(self, double: float) -> Dfp: ...
    @typing.overload
    def newInstance(self, int: int) -> Dfp: ...
    @typing.overload
    def newInstance(self, string: str) -> Dfp: ...
    @typing.overload
    def newInstance(self, long: int) -> Dfp: ...
    @typing.overload
    def newInstance(self, dfp: Dfp) -> Dfp: ...
    def nextAfter(self, dfp: Dfp) -> Dfp:
        """
            Returns the next number greater than this one in the direction of x. If this==x then simply returns this.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.nextAfter` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): direction where to look at
        
            Returns:
                closest number next to instance in the direction of x
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.dfp")``.

    Dfp: typing.Type[Dfp]
    DfpDec: typing.Type[DfpDec]
    DfpField: typing.Type[DfpField]
    DfpMath: typing.Type[DfpMath]
