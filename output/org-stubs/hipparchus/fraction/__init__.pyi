import java.io
import java.lang
import java.math
import java.text
import java.util
import org
import org.hipparchus
import typing



class BigFraction(java.lang.Number, org.hipparchus.FieldElement['BigFraction'], java.lang.Comparable['BigFraction'], java.io.Serializable):
    TWO: typing.ClassVar['BigFraction'] = ...
    ONE: typing.ClassVar['BigFraction'] = ...
    ZERO: typing.ClassVar['BigFraction'] = ...
    MINUS_ONE: typing.ClassVar['BigFraction'] = ...
    FOUR_FIFTHS: typing.ClassVar['BigFraction'] = ...
    ONE_FIFTH: typing.ClassVar['BigFraction'] = ...
    ONE_HALF: typing.ClassVar['BigFraction'] = ...
    ONE_QUARTER: typing.ClassVar['BigFraction'] = ...
    ONE_THIRD: typing.ClassVar['BigFraction'] = ...
    THREE_FIFTHS: typing.ClassVar['BigFraction'] = ...
    THREE_QUARTERS: typing.ClassVar['BigFraction'] = ...
    TWO_FIFTHS: typing.ClassVar['BigFraction'] = ...
    TWO_QUARTERS: typing.ClassVar['BigFraction'] = ...
    TWO_THIRDS: typing.ClassVar['BigFraction'] = ...
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
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def __init__(self, long: int, long2: int): ...
    def abs(self) -> 'BigFraction': ...
    @typing.overload
    def add(self, int: int) -> 'BigFraction': ...
    @typing.overload
    def add(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def add(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def add(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    @typing.overload
    def bigDecimalValue(self) -> java.math.BigDecimal: ...
    @typing.overload
    def bigDecimalValue(self, int: int) -> java.math.BigDecimal: ...
    @typing.overload
    def bigDecimalValue(self, int: int, int2: int) -> java.math.BigDecimal: ...
    def compareTo(self, bigFraction: 'BigFraction') -> int: ...
    @typing.overload
    def divide(self, int: int) -> 'BigFraction': ...
    @typing.overload
    def divide(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def divide(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def divide(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    def doubleValue(self) -> float: ...
    def equals(self, object: typing.Any) -> bool: ...
    def floatValue(self) -> float: ...
    def getDenominator(self) -> java.math.BigInteger: ...
    def getDenominatorAsInt(self) -> int: ...
    def getDenominatorAsLong(self) -> int: ...
    def getField(self) -> 'BigFractionField': ...
    def getNumerator(self) -> java.math.BigInteger: ...
    def getNumeratorAsInt(self) -> int: ...
    def getNumeratorAsLong(self) -> int: ...
    def getReal(self) -> float: ...
    @staticmethod
    def getReducedFraction(int: int, int2: int) -> 'BigFraction': ...
    def hashCode(self) -> int: ...
    def intValue(self) -> int: ...
    def isInteger(self) -> bool: ...
    def longValue(self) -> int: ...
    @typing.overload
    def multiply(self, int: int) -> 'BigFraction': ...
    @typing.overload
    def multiply(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def multiply(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def multiply(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    def negate(self) -> 'BigFraction': ...
    def percentageValue(self) -> float: ...
    @typing.overload
    def pow(self, double: float) -> float: ...
    @typing.overload
    def pow(self, int: int) -> 'BigFraction': ...
    @typing.overload
    def pow(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def pow(self, long: int) -> 'BigFraction': ...
    def reciprocal(self) -> 'BigFraction': ...
    def reduce(self) -> 'BigFraction': ...
    def signum(self) -> int: ...
    @typing.overload
    def subtract(self, int: int) -> 'BigFraction': ...
    @typing.overload
    def subtract(self, bigInteger: java.math.BigInteger) -> 'BigFraction': ...
    @typing.overload
    def subtract(self, long: int) -> 'BigFraction': ...
    @typing.overload
    def subtract(self, bigFraction: 'BigFraction') -> 'BigFraction': ...
    def toString(self) -> str: ...

class BigFractionField(org.hipparchus.Field[BigFraction], java.io.Serializable):
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def getInstance() -> 'BigFractionField': ...
    def getOne(self) -> BigFraction: ...
    def getRuntimeClass(self) -> typing.Type[BigFraction]: ...
    def getZero(self) -> BigFraction: ...
    def hashCode(self) -> int: ...

class Fraction(java.lang.Number, org.hipparchus.FieldElement['Fraction'], java.lang.Comparable['Fraction'], java.io.Serializable):
    TWO: typing.ClassVar['Fraction'] = ...
    ONE: typing.ClassVar['Fraction'] = ...
    ZERO: typing.ClassVar['Fraction'] = ...
    FOUR_FIFTHS: typing.ClassVar['Fraction'] = ...
    ONE_FIFTH: typing.ClassVar['Fraction'] = ...
    ONE_HALF: typing.ClassVar['Fraction'] = ...
    ONE_QUARTER: typing.ClassVar['Fraction'] = ...
    ONE_THIRD: typing.ClassVar['Fraction'] = ...
    THREE_FIFTHS: typing.ClassVar['Fraction'] = ...
    THREE_QUARTERS: typing.ClassVar['Fraction'] = ...
    TWO_FIFTHS: typing.ClassVar['Fraction'] = ...
    TWO_QUARTERS: typing.ClassVar['Fraction'] = ...
    TWO_THIRDS: typing.ClassVar['Fraction'] = ...
    MINUS_ONE: typing.ClassVar['Fraction'] = ...
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
    def abs(self) -> 'Fraction': ...
    @typing.overload
    def add(self, int: int) -> 'Fraction': ...
    @typing.overload
    def add(self, fraction: 'Fraction') -> 'Fraction': ...
    def compareTo(self, fraction: 'Fraction') -> int: ...
    @typing.overload
    def divide(self, int: int) -> 'Fraction': ...
    @typing.overload
    def divide(self, fraction: 'Fraction') -> 'Fraction': ...
    def doubleValue(self) -> float: ...
    def equals(self, object: typing.Any) -> bool: ...
    def floatValue(self) -> float: ...
    def getDenominator(self) -> int: ...
    def getField(self) -> 'FractionField': ...
    def getNumerator(self) -> int: ...
    def getReal(self) -> float: ...
    @staticmethod
    def getReducedFraction(int: int, int2: int) -> 'Fraction': ...
    def hashCode(self) -> int: ...
    def intValue(self) -> int: ...
    def isInteger(self) -> bool: ...
    def longValue(self) -> int: ...
    @typing.overload
    def multiply(self, int: int) -> 'Fraction': ...
    @typing.overload
    def multiply(self, fraction: 'Fraction') -> 'Fraction': ...
    def negate(self) -> 'Fraction': ...
    def percentageValue(self) -> float: ...
    def reciprocal(self) -> 'Fraction': ...
    def signum(self) -> int: ...
    @typing.overload
    def subtract(self, int: int) -> 'Fraction': ...
    @typing.overload
    def subtract(self, fraction: 'Fraction') -> 'Fraction': ...
    def toString(self) -> str: ...

class FractionField(org.hipparchus.Field[Fraction], java.io.Serializable):
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def getInstance() -> 'FractionField': ...
    def getOne(self) -> Fraction: ...
    def getRuntimeClass(self) -> typing.Type[Fraction]: ...
    def getZero(self) -> Fraction: ...
    def hashCode(self) -> int: ...

class BigFractionFormat(org.hipparchus.fraction.AbstractFormat, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, bigFraction: BigFraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def formatBigFraction(bigFraction: BigFraction) -> str: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    @typing.overload
    @staticmethod
    def getImproperInstance() -> 'BigFractionFormat': ...
    @typing.overload
    @staticmethod
    def getImproperInstance(locale: java.util.Locale) -> 'BigFractionFormat': ...
    @typing.overload
    @staticmethod
    def getProperInstance() -> 'BigFractionFormat': ...
    @typing.overload
    @staticmethod
    def getProperInstance(locale: java.util.Locale) -> 'BigFractionFormat': ...
    @typing.overload
    def parse(self, string: str) -> BigFraction: ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> BigFraction: ...

class FractionFormat(org.hipparchus.fraction.AbstractFormat):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, fraction: Fraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def formatFraction(fraction: Fraction) -> str: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    @typing.overload
    @staticmethod
    def getImproperInstance() -> 'FractionFormat': ...
    @typing.overload
    @staticmethod
    def getImproperInstance(locale: java.util.Locale) -> 'FractionFormat': ...
    @typing.overload
    @staticmethod
    def getProperInstance() -> 'FractionFormat': ...
    @typing.overload
    @staticmethod
    def getProperInstance(locale: java.util.Locale) -> 'FractionFormat': ...
    @typing.overload
    def parse(self, string: str) -> Fraction: ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Fraction: ...

class ProperBigFractionFormat(BigFractionFormat):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat, numberFormat3: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, bigFraction: BigFraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    def getWholeFormat(self) -> java.text.NumberFormat: ...
    @typing.overload
    def parse(self, string: str) -> BigFraction: ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> BigFraction: ...

class ProperFractionFormat(FractionFormat):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat, numberFormat2: java.text.NumberFormat, numberFormat3: java.text.NumberFormat): ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, fraction: Fraction, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    def getWholeFormat(self) -> java.text.NumberFormat: ...
    @typing.overload
    def parse(self, string: str) -> Fraction: ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> Fraction: ...

class AbstractFormat: ...


class __module_protocol__(typing.Protocol):
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
