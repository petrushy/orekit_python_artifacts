import java.io
import java.lang
import java.time
import java.time.chrono
import java.time.format
import java.util
import java.util.function
import typing



class IsoFields:
    DAY_OF_QUARTER: typing.ClassVar['TemporalField'] = ...
    QUARTER_OF_YEAR: typing.ClassVar['TemporalField'] = ...
    WEEK_OF_WEEK_BASED_YEAR: typing.ClassVar['TemporalField'] = ...
    WEEK_BASED_YEAR: typing.ClassVar['TemporalField'] = ...
    WEEK_BASED_YEARS: typing.ClassVar['TemporalUnit'] = ...
    QUARTER_YEARS: typing.ClassVar['TemporalUnit'] = ...

class JulianFields:
    JULIAN_DAY: typing.ClassVar['TemporalField'] = ...
    MODIFIED_JULIAN_DAY: typing.ClassVar['TemporalField'] = ...
    RATA_DIE: typing.ClassVar['TemporalField'] = ...

class TemporalAccessor:
    def get(self, temporalField: 'TemporalField') -> int: ...
    def getLong(self, temporalField: 'TemporalField') -> int: ...
    def isSupported(self, temporalField: 'TemporalField') -> bool: ...
    _query__R = typing.TypeVar('_query__R')  # <R>
    def query(self, temporalQuery: typing.Union['TemporalQuery'[_query__R], typing.Callable[['TemporalAccessor'], _query__R]]) -> _query__R: ...
    def range(self, temporalField: 'TemporalField') -> 'ValueRange': ...

class TemporalAdjuster:
    def adjustInto(self, temporal: 'Temporal') -> 'Temporal': ...

class TemporalAdjusters:
    @staticmethod
    def dayOfWeekInMonth(int: int, dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @staticmethod
    def firstDayOfMonth() -> TemporalAdjuster: ...
    @staticmethod
    def firstDayOfNextMonth() -> TemporalAdjuster: ...
    @staticmethod
    def firstDayOfNextYear() -> TemporalAdjuster: ...
    @staticmethod
    def firstDayOfYear() -> TemporalAdjuster: ...
    @staticmethod
    def firstInMonth(dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @staticmethod
    def lastDayOfMonth() -> TemporalAdjuster: ...
    @staticmethod
    def lastDayOfYear() -> TemporalAdjuster: ...
    @staticmethod
    def lastInMonth(dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @staticmethod
    def next(dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @staticmethod
    def nextOrSame(dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @staticmethod
    def ofDateAdjuster(unaryOperator: typing.Union[java.util.function.UnaryOperator[java.time.LocalDate], typing.Callable]) -> TemporalAdjuster: ...
    @staticmethod
    def previous(dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...
    @staticmethod
    def previousOrSame(dayOfWeek: java.time.DayOfWeek) -> TemporalAdjuster: ...

class TemporalAmount:
    def addTo(self, temporal: 'Temporal') -> 'Temporal': ...
    def get(self, temporalUnit: 'TemporalUnit') -> int: ...
    def getUnits(self) -> java.util.List['TemporalUnit']: ...
    def subtractFrom(self, temporal: 'Temporal') -> 'Temporal': ...

class TemporalField:
    _adjustInto__R = typing.TypeVar('_adjustInto__R', bound='Temporal')  # <R>
    def adjustInto(self, r: _adjustInto__R, long: int) -> _adjustInto__R: ...
    def getBaseUnit(self) -> 'TemporalUnit': ...
    def getDisplayName(self, locale: java.util.Locale) -> str: ...
    def getFrom(self, temporalAccessor: TemporalAccessor) -> int: ...
    def getRangeUnit(self) -> 'TemporalUnit': ...
    def isDateBased(self) -> bool: ...
    def isSupportedBy(self, temporalAccessor: TemporalAccessor) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def range(self) -> 'ValueRange': ...
    def rangeRefinedBy(self, temporalAccessor: TemporalAccessor) -> 'ValueRange': ...
    def resolve(self, map: typing.Union[java.util.Map['TemporalField', int], typing.Mapping['TemporalField', int]], temporalAccessor: TemporalAccessor, resolverStyle: java.time.format.ResolverStyle) -> TemporalAccessor: ...
    def toString(self) -> str: ...

class TemporalQueries:
    @staticmethod
    def chronology() -> 'TemporalQuery'[java.time.chrono.Chronology]: ...
    @staticmethod
    def localDate() -> 'TemporalQuery'[java.time.LocalDate]: ...
    @staticmethod
    def localTime() -> 'TemporalQuery'[java.time.LocalTime]: ...
    @staticmethod
    def offset() -> 'TemporalQuery'[java.time.ZoneOffset]: ...
    @staticmethod
    def precision() -> 'TemporalQuery'['TemporalUnit']: ...
    @staticmethod
    def zone() -> 'TemporalQuery'[java.time.ZoneId]: ...
    @staticmethod
    def zoneId() -> 'TemporalQuery'[java.time.ZoneId]: ...

_TemporalQuery__R = typing.TypeVar('_TemporalQuery__R')  # <R>
class TemporalQuery(typing.Generic[_TemporalQuery__R]):
    def queryFrom(self, temporalAccessor: TemporalAccessor) -> _TemporalQuery__R: ...

class TemporalUnit:
    _addTo__R = typing.TypeVar('_addTo__R', bound='Temporal')  # <R>
    def addTo(self, r: _addTo__R, long: int) -> _addTo__R: ...
    def between(self, temporal: 'Temporal', temporal2: 'Temporal') -> int: ...
    def getDuration(self) -> java.time.Duration: ...
    def isDateBased(self) -> bool: ...
    def isDurationEstimated(self) -> bool: ...
    def isSupportedBy(self, temporal: 'Temporal') -> bool: ...
    def isTimeBased(self) -> bool: ...
    def toString(self) -> str: ...

class UnsupportedTemporalTypeException(java.time.DateTimeException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...

class ValueRange(java.io.Serializable):
    def checkValidIntValue(self, long: int, temporalField: TemporalField) -> int: ...
    def checkValidValue(self, long: int, temporalField: TemporalField) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getLargestMinimum(self) -> int: ...
    def getMaximum(self) -> int: ...
    def getMinimum(self) -> int: ...
    def getSmallestMaximum(self) -> int: ...
    def hashCode(self) -> int: ...
    def isFixed(self) -> bool: ...
    def isIntValue(self) -> bool: ...
    def isValidIntValue(self, long: int) -> bool: ...
    def isValidValue(self, long: int) -> bool: ...
    @typing.overload
    @staticmethod
    def of(long: int, long2: int) -> 'ValueRange': ...
    @typing.overload
    @staticmethod
    def of(long: int, long2: int, long3: int) -> 'ValueRange': ...
    @typing.overload
    @staticmethod
    def of(long: int, long2: int, long3: int, long4: int) -> 'ValueRange': ...
    def toString(self) -> str: ...

class WeekFields(java.io.Serializable):
    ISO: typing.ClassVar['WeekFields'] = ...
    SUNDAY_START: typing.ClassVar['WeekFields'] = ...
    WEEK_BASED_YEARS: typing.ClassVar[TemporalUnit] = ...
    def dayOfWeek(self) -> TemporalField: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getFirstDayOfWeek(self) -> java.time.DayOfWeek: ...
    def getMinimalDaysInFirstWeek(self) -> int: ...
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def of(dayOfWeek: java.time.DayOfWeek, int: int) -> 'WeekFields': ...
    @typing.overload
    @staticmethod
    def of(locale: java.util.Locale) -> 'WeekFields': ...
    def toString(self) -> str: ...
    def weekBasedYear(self) -> TemporalField: ...
    def weekOfMonth(self) -> TemporalField: ...
    def weekOfWeekBasedYear(self) -> TemporalField: ...
    def weekOfYear(self) -> TemporalField: ...

class ChronoField(java.lang.Enum['ChronoField'], TemporalField):
    NANO_OF_SECOND: typing.ClassVar['ChronoField'] = ...
    NANO_OF_DAY: typing.ClassVar['ChronoField'] = ...
    MICRO_OF_SECOND: typing.ClassVar['ChronoField'] = ...
    MICRO_OF_DAY: typing.ClassVar['ChronoField'] = ...
    MILLI_OF_SECOND: typing.ClassVar['ChronoField'] = ...
    MILLI_OF_DAY: typing.ClassVar['ChronoField'] = ...
    SECOND_OF_MINUTE: typing.ClassVar['ChronoField'] = ...
    SECOND_OF_DAY: typing.ClassVar['ChronoField'] = ...
    MINUTE_OF_HOUR: typing.ClassVar['ChronoField'] = ...
    MINUTE_OF_DAY: typing.ClassVar['ChronoField'] = ...
    HOUR_OF_AMPM: typing.ClassVar['ChronoField'] = ...
    CLOCK_HOUR_OF_AMPM: typing.ClassVar['ChronoField'] = ...
    HOUR_OF_DAY: typing.ClassVar['ChronoField'] = ...
    CLOCK_HOUR_OF_DAY: typing.ClassVar['ChronoField'] = ...
    AMPM_OF_DAY: typing.ClassVar['ChronoField'] = ...
    DAY_OF_WEEK: typing.ClassVar['ChronoField'] = ...
    ALIGNED_DAY_OF_WEEK_IN_MONTH: typing.ClassVar['ChronoField'] = ...
    ALIGNED_DAY_OF_WEEK_IN_YEAR: typing.ClassVar['ChronoField'] = ...
    DAY_OF_MONTH: typing.ClassVar['ChronoField'] = ...
    DAY_OF_YEAR: typing.ClassVar['ChronoField'] = ...
    EPOCH_DAY: typing.ClassVar['ChronoField'] = ...
    ALIGNED_WEEK_OF_MONTH: typing.ClassVar['ChronoField'] = ...
    ALIGNED_WEEK_OF_YEAR: typing.ClassVar['ChronoField'] = ...
    MONTH_OF_YEAR: typing.ClassVar['ChronoField'] = ...
    PROLEPTIC_MONTH: typing.ClassVar['ChronoField'] = ...
    YEAR_OF_ERA: typing.ClassVar['ChronoField'] = ...
    YEAR: typing.ClassVar['ChronoField'] = ...
    ERA: typing.ClassVar['ChronoField'] = ...
    INSTANT_SECONDS: typing.ClassVar['ChronoField'] = ...
    OFFSET_SECONDS: typing.ClassVar['ChronoField'] = ...
    _adjustInto__R = typing.TypeVar('_adjustInto__R', bound='Temporal')  # <R>
    def adjustInto(self, r: _adjustInto__R, long: int) -> _adjustInto__R: ...
    def checkValidIntValue(self, long: int) -> int: ...
    def checkValidValue(self, long: int) -> int: ...
    def getBaseUnit(self) -> TemporalUnit: ...
    def getDisplayName(self, locale: java.util.Locale) -> str: ...
    def getFrom(self, temporalAccessor: TemporalAccessor) -> int: ...
    def getRangeUnit(self) -> TemporalUnit: ...
    def isDateBased(self) -> bool: ...
    def isSupportedBy(self, temporalAccessor: TemporalAccessor) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def range(self) -> ValueRange: ...
    def rangeRefinedBy(self, temporalAccessor: TemporalAccessor) -> ValueRange: ...
    def toString(self) -> str: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ChronoField': ...
    @staticmethod
    def values() -> typing.List['ChronoField']: ...

class ChronoUnit(java.lang.Enum['ChronoUnit'], TemporalUnit):
    NANOS: typing.ClassVar['ChronoUnit'] = ...
    MICROS: typing.ClassVar['ChronoUnit'] = ...
    MILLIS: typing.ClassVar['ChronoUnit'] = ...
    SECONDS: typing.ClassVar['ChronoUnit'] = ...
    MINUTES: typing.ClassVar['ChronoUnit'] = ...
    HOURS: typing.ClassVar['ChronoUnit'] = ...
    HALF_DAYS: typing.ClassVar['ChronoUnit'] = ...
    DAYS: typing.ClassVar['ChronoUnit'] = ...
    WEEKS: typing.ClassVar['ChronoUnit'] = ...
    MONTHS: typing.ClassVar['ChronoUnit'] = ...
    YEARS: typing.ClassVar['ChronoUnit'] = ...
    DECADES: typing.ClassVar['ChronoUnit'] = ...
    CENTURIES: typing.ClassVar['ChronoUnit'] = ...
    MILLENNIA: typing.ClassVar['ChronoUnit'] = ...
    ERAS: typing.ClassVar['ChronoUnit'] = ...
    FOREVER: typing.ClassVar['ChronoUnit'] = ...
    _addTo__R = typing.TypeVar('_addTo__R', bound='Temporal')  # <R>
    def addTo(self, r: _addTo__R, long: int) -> _addTo__R: ...
    def between(self, temporal: 'Temporal', temporal2: 'Temporal') -> int: ...
    def getDuration(self) -> java.time.Duration: ...
    def isDateBased(self) -> bool: ...
    def isDurationEstimated(self) -> bool: ...
    def isSupportedBy(self, temporal: 'Temporal') -> bool: ...
    def isTimeBased(self) -> bool: ...
    def toString(self) -> str: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ChronoUnit': ...
    @staticmethod
    def values() -> typing.List['ChronoUnit']: ...

class Temporal(TemporalAccessor):
    @typing.overload
    def isSupported(self, temporalUnit: TemporalUnit) -> bool: ...
    @typing.overload
    def isSupported(self, temporalField: TemporalField) -> bool: ...
    @typing.overload
    def minus(self, temporalAmount: TemporalAmount) -> 'Temporal': ...
    @typing.overload
    def minus(self, long: int, temporalUnit: TemporalUnit) -> 'Temporal': ...
    @typing.overload
    def plus(self, long: int, temporalUnit: TemporalUnit) -> 'Temporal': ...
    @typing.overload
    def plus(self, temporalAmount: TemporalAmount) -> 'Temporal': ...
    def until(self, temporal: 'Temporal', temporalUnit: TemporalUnit) -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.time.temporal")``.

    ChronoField: typing.Type[ChronoField]
    ChronoUnit: typing.Type[ChronoUnit]
    IsoFields: typing.Type[IsoFields]
    JulianFields: typing.Type[JulianFields]
    Temporal: typing.Type[Temporal]
    TemporalAccessor: typing.Type[TemporalAccessor]
    TemporalAdjuster: typing.Type[TemporalAdjuster]
    TemporalAdjusters: typing.Type[TemporalAdjusters]
    TemporalAmount: typing.Type[TemporalAmount]
    TemporalField: typing.Type[TemporalField]
    TemporalQueries: typing.Type[TemporalQueries]
    TemporalQuery: typing.Type[TemporalQuery]
    TemporalUnit: typing.Type[TemporalUnit]
    UnsupportedTemporalTypeException: typing.Type[UnsupportedTemporalTypeException]
    ValueRange: typing.Type[ValueRange]
    WeekFields: typing.Type[WeekFields]