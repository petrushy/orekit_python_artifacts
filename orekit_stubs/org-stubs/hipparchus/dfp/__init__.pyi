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
    def add(self, double: float) -> org.hipparchus.FieldElement: ...
    @typing.overload
    def add(self, dfp: 'Dfp') -> 'Dfp': ...
    def asin(self) -> 'Dfp': ...
    def asinh(self) -> 'Dfp': ...
    def atan(self) -> 'Dfp': ...
    def atan2(self, dfp: 'Dfp') -> 'Dfp': ...
    def atanh(self) -> 'Dfp': ...
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
    def divide(self, double: float) -> org.hipparchus.FieldElement: ...
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
    def multiply(self, double: float) -> org.hipparchus.FieldElement: ...
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
    def sinh(self) -> 'Dfp': ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['Dfp']: ...
    def sqrt(self) -> 'Dfp': ...
    def square(self) -> 'Dfp': ...
    def strictlyNegative(self) -> bool: ...
    def strictlyPositive(self) -> bool: ...
    @typing.overload
    def subtract(self, double: float) -> org.hipparchus.FieldElement: ...
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
    FLAG_INVALID: typing.ClassVar[int] = ...
    FLAG_DIV_ZERO: typing.ClassVar[int] = ...
    FLAG_OVERFLOW: typing.ClassVar[int] = ...
    FLAG_UNDERFLOW: typing.ClassVar[int] = ...
    FLAG_INEXACT: typing.ClassVar[int] = ...
    def __init__(self, int: int): ...
    def clearIEEEFlags(self) -> None: ...
    @staticmethod
    def computeExp(dfp: Dfp, dfp2: Dfp) -> Dfp: ...
    @staticmethod
    def computeLn(dfp: Dfp, dfp2: Dfp, dfp3: Dfp) -> Dfp: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDegToRad(self) -> Dfp: ...
    def getE(self) -> Dfp: ...
    def getESplit(self) -> typing.List[Dfp]: ...
    def getExtendedField(self, int: int, boolean: bool) -> 'DfpField': ...
    def getIEEEFlags(self) -> int: ...
    def getLn10(self) -> Dfp: ...
    def getLn2(self) -> Dfp: ...
    def getLn2Split(self) -> typing.List[Dfp]: ...
    def getLn5(self) -> Dfp: ...
    def getLn5Split(self) -> typing.List[Dfp]: ...
    def getOne(self) -> Dfp: ...
    def getPi(self) -> Dfp: ...
    def getPiSplit(self) -> typing.List[Dfp]: ...
    def getRadToDeg(self) -> Dfp: ...
    def getRadixDigits(self) -> int: ...
    def getRoundingMode(self) -> 'DfpField.RoundingMode': ...
    def getRuntimeClass(self) -> typing.Type[Dfp]: ...
    def getSqr2(self) -> Dfp: ...
    def getSqr2Reciprocal(self) -> Dfp: ...
    def getSqr2Split(self) -> typing.List[Dfp]: ...
    def getSqr3(self) -> Dfp: ...
    def getSqr3Reciprocal(self) -> Dfp: ...
    def getTwo(self) -> Dfp: ...
    def getZero(self) -> Dfp: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def newDfp(self) -> Dfp: ...
    @typing.overload
    def newDfp(self, byte: int) -> Dfp: ...
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
    def setIEEEFlags(self, int: int) -> None: ...
    def setIEEEFlagsBits(self, int: int) -> None: ...
    def setRoundingMode(self, roundingMode: 'DfpField.RoundingMode') -> None: ...
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
    @staticmethod
    def acos(dfp: Dfp) -> Dfp: ...
    @staticmethod
    def asin(dfp: Dfp) -> Dfp: ...
    @staticmethod
    def atan(dfp: Dfp) -> Dfp: ...
    @staticmethod
    def cos(dfp: Dfp) -> Dfp: ...
    @staticmethod
    def exp(dfp: Dfp) -> Dfp: ...
    @staticmethod
    def log(dfp: Dfp) -> Dfp: ...
    @typing.overload
    @staticmethod
    def pow(dfp: Dfp, int: int) -> Dfp: ...
    @typing.overload
    @staticmethod
    def pow(dfp: Dfp, dfp2: Dfp) -> Dfp: ...
    @staticmethod
    def sin(dfp: Dfp) -> Dfp: ...
    @staticmethod
    def tan(dfp: Dfp) -> Dfp: ...

class DfpDec(Dfp):
    def __init__(self, dfp: Dfp): ...
    @typing.overload
    def newInstance(self, dfpField: DfpField, roundingMode: DfpField.RoundingMode) -> Dfp: ...
    @typing.overload
    def newInstance(self) -> Dfp: ...
    @typing.overload
    def newInstance(self, byte: int) -> Dfp: ...
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
    def nextAfter(self, dfp: Dfp) -> Dfp: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.dfp")``.

    Dfp: typing.Type[Dfp]
    DfpDec: typing.Type[DfpDec]
    DfpField: typing.Type[DfpField]
    DfpMath: typing.Type[DfpMath]
