
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import datetime
import java.io
import java.lang
import java.time
import java.util
import java.util.concurrent
import java.util.function
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss
import org.orekit.utils
import typing



class ChronologicalComparator(java.util.Comparator['TimeStamped'], java.io.Serializable):
    """
    Comparator for TimeStamped instance.
    
    Also see:
        AbsoluteDate, TimeStamped, serialized
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def compare(self, timeStamped1: typing.Union['TimeStamped', typing.Callable], timeStamped2: typing.Union['TimeStamped', typing.Callable]) -> int:
        """
        Compare two time-stamped instances.
        
        Specified by: Comparator in interface Comparator
        
        Parameters:
            timeStamped1 (TimeStamped): first time-stamped instance
            timeStamped2 (TimeStamped): second time-stamped instance
        
        Returns:
            a negative integer, zero, or a positive integer as the first instance is before, simultaneous, or after the second one.
        
        
        """
        ...

class ClockModel:
    """
    Offset clock model.
    
    Since:
        12.1
    """
    _getOffset_1__T = typing.TypeVar('_getOffset_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, date: 'AbsoluteDate') -> 'ClockOffset':
        """
        Get the clock offset at date.
        
        Parameters:
            date (AbsoluteDate): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        """
        ...
    @typing.overload
    def getOffset(self, date: 'FieldAbsoluteDate'[_getOffset_1__T]) -> 'FieldClockOffset'[_getOffset_1__T]:
        """
        Get the clock offset at date.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        
        """
        ...
    def getValidityEnd(self) -> 'AbsoluteDate':
        """
        Get validity end.
        
        Returns:
            model validity end
        
        
        """
        ...
    def getValidityStart(self) -> 'AbsoluteDate':
        """
        Get validity start.
        
        Returns:
            model validity start
        
        
        """
        ...

class DateComponents(java.io.Serializable, java.lang.Comparable['DateComponents']):
    """
    Class representing a date broken up as year, month and day components.
    
    This class uses the astronomical convention for calendars, which is also the convention used by Date: a year zero is present between years -1 and +1, and 10 days are missing in 1582. The calendar used around these special dates are:
    
      - up to 0000-12-31 : proleptic julian calendar
      - from 0001-01-01 to 1582-10-04: julian calendar
      - from 1582-10-15: gregorian calendar
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        TimeComponents, DateTimeComponents, serialized
    """
    JULIAN_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for julian dates: -4712-01-01.
    
    Both Date and DateComponents classes follow the astronomical conventions and consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be seen in other documents or programs that obey a different convention (for example the convcal utility).
    """
    MODIFIED_JULIAN_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for modified julian dates: 1858-11-17.
    """
    FIFTIES_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for 1950 dates: 1950-01-01.
    """
    CCSDS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01.
    """
    GALILEO_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for Galileo System Time: 1999-08-22.
    """
    GPS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for GPS weeks: 1980-01-06.
    """
    QZSS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for QZSS weeks: 1980-01-06.
    """
    NAVIC_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for NavIC weeks: 1999-08-22.
    """
    BEIDOU_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for BeiDou weeks: 2006-01-01.
    """
    GLONASS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Reference epoch for GLONASS four-year interval number: 1996-01-01.
    """
    J2000_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    J2000.0 Reference epoch: 2000-01-01.
    """
    JAVA_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Java Reference epoch: 1970-01-01.
    """
    MAX_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Maximum supported date.
    
    This is date 5881610-07-11 which corresponds to MAX_VALUE days after J2000_EPOCH.
    
    Since:
        9.0
    
    
    """
    MIN_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    Maximum supported date.
    
    This is date -5877490-03-03, which corresponds to MIN_VALUE days before J2000_EPOCH.
    
    Since:
        9.0
    
    
    """
    JD_TO_MJD: typing.ClassVar[float] = ...
    """
    Offset between julian day epoch and modified julian day epoch.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, int: int, month: 'Month', int2: int): ...
    @typing.overload
    def __init__(self, dateComponents: 'DateComponents', int: int): ...
    def compareTo(self, dateComponents: 'DateComponents') -> int:
        """
        Specified by: Comparable in interface Comparable
        
        
        """
        ...
    @staticmethod
    def createFromWeekComponents(wYear: int, week: int, dayOfWeek: int) -> 'DateComponents':
        """
        Build a date from week components.
        
        The calendar week number is a number between 1 and 52 or 53 depending on the year. Week 1 is defined by ISO as the one that includes the first Thursday of a year. Week 1 may therefore start the previous year and week 52 or 53 may end in the next year. As an example calendar date 1995-01-01 corresponds to week date 1994-W52-7 (i.e. Sunday in the last week of 1994 is in fact the first day of year 1995). This date would beAnother example is calendar date 1996-12-31 which corresponds to week date 1997-W01-2 (i.e. Tuesday in the first week of 1997 is in fact the last day of year 1996).
        
        Parameters:
            wYear (int): year associated to week numbering
            week (int): week number in year, from 1 to 52 or 53
            dayOfWeek (int): day of week, from 1 (Monday) to 7 (Sunday)
        
        Returns:
            a builded date
        
        Raises:
            IllegalArgumentException: if inconsistent arguments are given (parameters out of range, week 53 on a 52 weeks year ...)
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getCalendarWeek(self) -> int:
        """
        Get the calendar week number.
        
        The calendar week number is a number between 1 and 52 or 53 depending on the year. Week 1 is defined by ISO as the one that includes the first Thursday of a year. Week 1 may therefore start the previous year and week 52 or 53 may end in the next year. As an example calendar date 1995-01-01 corresponds to week date 1994-W52-7 (i.e. Sunday in the last week of 1994 is in fact the first day of year 1995). Another example is calendar date 1996-12-31 which corresponds to week date 1997-W01-2 (i.e. Tuesday in the first week of 1997 is in fact the last day of year 1996).
        
        Returns:
            calendar week number
        
        
        """
        ...
    def getDay(self) -> int:
        """
        Get the day.
        
        Returns:
            day number from 1 to 31
        
        
        """
        ...
    def getDayOfWeek(self) -> int:
        """
        Get the day of week.
        
        Day of week is a number between 1 (Monday) and 7 (Sunday).
        
        Returns:
            day of week
        
        
        """
        ...
    def getDayOfYear(self) -> int:
        """
        Get the day number in year.
        
        Day number in year is between 1 (January 1st) and either 365 or 366 inclusive depending on year.
        
        Returns:
            day number in year
        
        
        """
        ...
    def getJ2000Day(self) -> int:
        """
        Get the day number with respect to J2000 epoch.
        
        Returns:
            day number with respect to J2000 epoch
        
        
        """
        ...
    def getMJD(self) -> int:
        """
        Get the modified julian day.
        
        Returns:
            modified julian day
        
        
        """
        ...
    def getMonth(self) -> int:
        """
        Get the month.
        
        Returns:
            month number from 1 to 12
        
        
        """
        ...
    def getMonthEnum(self) -> 'Month':
        """
        Get the month as an enumerate.
        
        Returns:
            month as an enumerate
        
        
        """
        ...
    def getYear(self) -> int:
        """
        Get the year number.
        
        Returns:
            year number (may be 0 or negative for BC years)
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @staticmethod
    def parseDate(string: str) -> 'DateComponents':
        """
        Parse a string in ISO-8601 format to build a date.
        
        The supported formats are:
        
          - basic format calendar date: YYYYMMDD
          - extended format calendar date: YYYY-MM-DD
          - basic format ordinal date: YYYYDDD
          - extended format ordinal date: YYYY-DDD
          - basic format week date: YYYYWwwD
          - extended format week date: YYYY-Www-D
        
        As shown by the list above, only the complete representations defined in section 4.1 of ISO-8601 standard are supported, neither expended representations nor representations with reduced accuracy are supported.
        
        Parsing a single integer as a julian day is not supported as it may be ambiguous with either the basic format calendar date or the basic format ordinal date depending on the number of digits.
        
        Parameters:
            string (String): string to parse
        
        Returns:
            a parsed date
        
        Raises:
            IllegalArgumentException: if string cannot be parsed
        
        
        """
        ...
    def toString(self) -> str:
        """
        Get a string representation (ISO-8601) of the date.
        
        Overrides: Object in class Object
        
        Returns:
            string representation of the date.
        
        
        """
        ...

class DateTimeComponents(java.io.Serializable, java.lang.Comparable['DateTimeComponents']):
    """
    Holder for date and time components.
    
    This class is a simple holder with no processing methods.
    
    Instance of this class are guaranteed to be immutable.
    
    Also see:
        AbsoluteDate, DateComponents,
        TimeComponents, serialized
    """
    JULIAN_EPOCH: typing.ClassVar['DateTimeComponents'] = ...
    """
    The Julian Epoch.
    
    Also see:
        getJulianEpoch
    
    
    """
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, timeOffset: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, int: int, month: 'Month', int2: int): ...
    @typing.overload
    def __init__(self, int: int, month: 'Month', int2: int, int3: int, int4: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, month: 'Month', int2: int, int3: int, int4: int, timeOffset: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, timeComponents: 'TimeComponents'): ...
    @typing.overload
    def __init__(self, dateTimeComponents: 'DateTimeComponents', double: float): ...
    @typing.overload
    def __init__(self, dateTimeComponents: 'DateTimeComponents', long: int, timeUnit: java.util.concurrent.TimeUnit): ...
    @typing.overload
    def __init__(self, dateTimeComponents: 'DateTimeComponents', timeOffset: 'TimeOffset'): ...
    def compareTo(self, dateTimeComponents: 'DateTimeComponents') -> int:
        """
        Specified by: Comparable in interface Comparable
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getDate(self) -> DateComponents:
        """
        Get the date component.
        
        Returns:
            date component
        
        
        """
        ...
    def getTime(self) -> 'TimeComponents':
        """
        Get the time component.
        
        Returns:
            time component
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @typing.overload
    def offsetFrom(self, dateTimeComponents: 'DateTimeComponents') -> float:
        """
        Compute the seconds offset between two instances.
        
        Parameters:
            dateTime (DateTimeComponents): dateTime to subtract from the instance
        
        Returns:
            offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Compute the seconds offset between two instances.
        
        Parameters:
            dateTime (DateTimeComponents): dateTime to subtract from the instance
            timeUnit (TimeUnit): the desired TimeUnit
        
        Returns:
            offset in the given timeunit between the two instants (positive if the instance is posterior to the argument), rounded
            to the nearest integer
            TimeUnit
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def offsetFrom(self, dateTimeComponents: 'DateTimeComponents', timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    @staticmethod
    def parseDateTime(string: str) -> 'DateTimeComponents':
        """
        Parse a string in ISO-8601 format to build a date/time.
        
        The supported formats are all date formats supported by parseDate and all time formats supported by parseTime separated by the standard time separator 'T', or date components only (in which case a 00:00:00 hour is implied). Typical examples are 2000-01-01T12:00:00Z or 1976W186T210000.
        
        Parameters:
            string (String): string to parse
        
        Returns:
            a parsed date/time
        
        Raises:
            IllegalArgumentException: if string cannot be parsed
        
        
        """
        ...
    def roundIfNeeded(self, minuteDuration: int, fractionDigits: int) -> 'DateTimeComponents':
        """
        Round this date-time to the given precision if needed to prevent rounding up to an invalid seconds number. This is useful, for example, when writing custom date-time formatting methods so one does not, e.g., end up with "60.0" seconds during a normal minute when the value of seconds is . This method will instead round up the minute, hour, day, month, and year as needed.
        
        Parameters:
            minuteDuration (int): 59, 60, 61, or 62 seconds depending on the date being close to a leap second introduction and the magnitude of the leap
                second.
            fractionDigits (int): the number of decimal digits after the decimal point in the seconds number that will be printed. This date-time is
                rounded to fractionDigits after the decimal point if necessary to prevent rounding up to minuteDuration.
                fractionDigits must be greater than or equal to .
        
        Returns:
            a date-time within 5 * 10**-fractionDigits seconds of this, and with a seconds number that will not round up
            to minuteDuration when rounded to fractionDigits after the decimal point.
        
        Since:
            11.3
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
        Return a string representation of this pair.
        
        The format used is ISO8601 including the UTC offset.
        
        Overrides: Object in class Object
        
        Returns:
            string representation of this pair
        
        """
        ...
    @typing.overload
    def toString(self, int: int) -> str:
        """
        Return a string representation of this date-time, rounded to millisecond precision.
        
        The format used is ISO8601 including the UTC offset.
        
        Parameters:
            minuteDuration (int): 60, 61, or 62 seconds depending on the date being close to a leap second introduction and the magnitude of the leap
                second.
        
        Returns:
            string representation of this date, time, and UTC offset
        
        Also see:
            toString
        
        Return a string representation of this date-time, rounded to the given precision.
        
        The format used is ISO8601 including the UTC offset.
        
        Parameters:
            minuteDuration (int): 59, 60, 61, or 62 seconds depending on the date being close to a leap second introduction and the magnitude of the leap
                second.
            fractionDigits (int): the number of digits to include after the decimal point in the string representation of the seconds. The date and time
                is first rounded as necessary. fractionDigits must be greater than or equal to .
        
        Returns:
            string representation of this date, time, and UTC offset
        
        Since:
            11.0
        
        Also see:
            toStringRfc3339,
            toStringWithoutUtcOffset,
            toStringWithoutUtcOffset
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, int2: int) -> str: ...
    def toStringRfc3339(self) -> str:
        """
        Represent the given date and time as a string according to the format in RFC 3339. RFC3339 is a restricted subset of ISO 8601 with a well defined grammar. This method includes enough precision to represent the point in time without rounding up to the next minute.
        
        RFC3339 is unable to represent BC years, years of 10000 or more, time zone offsets of 100 hours or more, or NaN. In these cases the value returned from this method will not be valid RFC3339 format.
        
        Returns:
            RFC 3339 format string.
        
        Also see:
            rfc3339, toStringRfc3339,
            toString,
            toStringWithoutUtcOffset
        
        
        """
        ...
    @typing.overload
    def toStringWithoutUtcOffset(self) -> str:
        """
        Get a string representation of the date-time without the offset from UTC. The format used is ISO6801, except without the offset from UTC.
        
        Returns:
            a string representation of the date-time.
        
        Also see:
            toStringWithoutUtcOffset,
            toString, toStringRfc3339
        
        """
        ...
    @typing.overload
    def toStringWithoutUtcOffset(self, minuteDuration: int, fractionDigits: int) -> str:
        """
        Return a string representation of this date-time, rounded to the given precision.
        
        The format used is ISO8601 without the UTC offset.
        
        Parameters:
            minuteDuration (int): 59, 60, 61, or 62 seconds depending on the date being close to a leap second introduction and the magnitude of the leap
                second.
            fractionDigits (int): the number of digits to include after the decimal point in the string representation of the seconds. The date and time
                are first rounded as necessary. fractionDigits must be greater than or equal to .
        
        Returns:
            string representation of this date, time, and UTC offset
        
        Since:
            11.1
        
        Also see:
            toStringRfc3339,
            toStringWithoutUtcOffset,
            toString
        
        
        """
        ...

class DatesSelector:
    """
    Interface for selecting dates within an interval.
    
    This interface is mainly useful for AbstractScheduler measurements Generator.
    
    Since:
        9.3
    
    Also see:
        AbstractScheduler,
        Generator
    """
    def selectDates(self, start: 'AbsoluteDate', end: 'AbsoluteDate') -> java.util.List['AbsoluteDate']:
        """
        Select dates within an interval.
        
        The start and end date may be either in direct or reverse chronological order. The list is produced in the same order as start and end, i.e. direct chronological order if start is earlier than end or reverse chronological order if start is later than end.
        
        The ordering (direct or reverse chronological order) should not be changed between calls, otherwise unpredictable results may occur.
        
        Parameters:
            start (AbsoluteDate): interval start
            end (AbsoluteDate): interval end
        
        Returns:
            selected dates within this interval
        
        
        """
        ...

_FieldChronologicalComparator__KK = typing.TypeVar('_FieldChronologicalComparator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldChronologicalComparator(java.util.Comparator['FieldTimeStamped'[_FieldChronologicalComparator__KK]], java.io.Serializable, typing.Generic[_FieldChronologicalComparator__KK]):
    """
    Comparator for FieldTimeStamped instance.
    
    Also see:
        FieldAbsoluteDate, FieldTimeStamped, serialized
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def compare(self, timeStamped1: typing.Union['FieldTimeStamped'[_FieldChronologicalComparator__KK], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]], timeStamped2: typing.Union['FieldTimeStamped'[_FieldChronologicalComparator__KK], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> int:
        """
        Compare two time-stamped instances.
        
        Specified by: Comparator in interface Comparator
        
        Parameters:
            timeStamped1 (FieldTimeStamped<FieldChronologicalComparator> timeStamped1): first time-stamped instance
            timeStamped2 (FieldTimeStamped<FieldChronologicalComparator> timeStamped2): second time-stamped instance
        
        Returns:
            a negative integer, zero, or a positive integer as the first instance is before, simultaneous, or after the second one.
        
        
        """
        ...

_FieldTimeInterpolator__T = typing.TypeVar('_FieldTimeInterpolator__T', bound='FieldTimeStamped')  # <T>
_FieldTimeInterpolator__KK = typing.TypeVar('_FieldTimeInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldTimeInterpolator(typing.Generic[_FieldTimeInterpolator__T, _FieldTimeInterpolator__KK]):
    """
    This interface represents objects that can interpolate a time stamped value with respect to time.
    
    Also see:
        FieldAbsoluteDate, FieldTimeStamped,
        CalculusFieldElement
    """
    def getExtrapolationThreshold(self) -> float:
        """
        Get the extrapolation threshold.
        
        Returns:
            get the extrapolation threshold.
        
        
        """
        ...
    def getNbInterpolationPoints(self) -> int:
        """
        Get the number of interpolation points. In the specific case where this interpolator contains multiple sub-interpolators, this method will return the maximum number of interpolation points required among all sub-interpolators.
        
        Returns:
            the number of interpolation points
        
        Since:
            12.0.1
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List['FieldTimeInterpolator'['FieldTimeStamped'[_FieldTimeInterpolator__KK], _FieldTimeInterpolator__KK]]:
        """
        Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldTimeInterpolator__KK], collection: typing.Union[java.util.Collection[_FieldTimeInterpolator__T], typing.Sequence[_FieldTimeInterpolator__T], typing.Set[_FieldTimeInterpolator__T]]) -> _FieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldTimeInterpolator__KK], stream: java.util.stream.Stream[_FieldTimeInterpolator__T]) -> _FieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: 'AbsoluteDate', collection: typing.Union[java.util.Collection[_FieldTimeInterpolator__T], typing.Sequence[_FieldTimeInterpolator__T], typing.Set[_FieldTimeInterpolator__T]]) -> _FieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: 'AbsoluteDate', stream: java.util.stream.Stream[_FieldTimeInterpolator__T]) -> _FieldTimeInterpolator__T: ...

_FieldTimeStamped__T = typing.TypeVar('_FieldTimeStamped__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTimeStamped(typing.Generic[_FieldTimeStamped__T]):
    """
    This interface represents objects that have a AbsoluteDate date attached to them.
    
    Classes implementing this interface can be stored chronologically in sorted sets using ChronologicalComparator as the underlying comparator. An example using for Orbit instances is given here:
    
    
         SortedSet<Orbit> sortedOrbits =
             new TreeSet<Orbit>(new ChronologicalComparator());
         sortedOrbits.add(orbit1);
         sortedOrbits.add(orbit2);
         ...
     
    
    This interface is also the base interface used to TimeStampedCache series of time-dependent objects for interpolation in a thread-safe manner.
    
    Also see:
        AbsoluteDate, ChronologicalComparator,
        TimeStampedCache
    """
    @typing.overload
    def durationFrom(self, timeStamped: typing.Union['FieldTimeStamped'[_FieldTimeStamped__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> _FieldTimeStamped__T:
        """
        Compute the physically elapsed duration between two instants.
        
        Parameters:
            timeStamped (TimeStamped): instant to subtract from the instance
        
        Returns:
            offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Since:
            131
        
        Also see:
            durationFrom
        
        
        """
        ...
    @typing.overload
    def durationFrom(self, timeStamped: typing.Union['TimeStamped', typing.Callable]) -> _FieldTimeStamped__T: ...
    def getDate(self) -> 'FieldAbsoluteDate'[_FieldTimeStamped__T]:
        """
        Get the date.
        
        Returns:
            date attached to the object
        
        
        """
        ...

class Month(java.lang.Enum['Month']):
    """
    Enumerate representing a calendar month.
    
    This enum is mainly useful to parse data files that use month names like Jan or JAN or January or numbers like 1 or 01. It handles month numbers as well as three letters abbreviation and full names, independently of capitalization.
    
    Also see:
        DateComponents
    """
    JANUARY: typing.ClassVar['Month'] = ...
    FEBRUARY: typing.ClassVar['Month'] = ...
    MARCH: typing.ClassVar['Month'] = ...
    APRIL: typing.ClassVar['Month'] = ...
    MAY: typing.ClassVar['Month'] = ...
    JUNE: typing.ClassVar['Month'] = ...
    JULY: typing.ClassVar['Month'] = ...
    AUGUST: typing.ClassVar['Month'] = ...
    SEPTEMBER: typing.ClassVar['Month'] = ...
    OCTOBER: typing.ClassVar['Month'] = ...
    NOVEMBER: typing.ClassVar['Month'] = ...
    DECEMBER: typing.ClassVar['Month'] = ...
    def getCapitalizedAbbreviation(self) -> str:
        """
        Get the capitalized three letters abbreviation.
        
        Returns:
            capitalized three letters abbreviation
        
        
        """
        ...
    def getCapitalizedName(self) -> str:
        """
        Get the capitalized full name.
        
        Returns:
            capitalized full name
        
        
        """
        ...
    def getLowerCaseAbbreviation(self) -> str:
        """
        Get the lower case three letters abbreviation.
        
        Returns:
            lower case three letters abbreviation
        
        
        """
        ...
    def getLowerCaseName(self) -> str:
        """
        Get the lower case full name.
        
        Returns:
            lower case full name
        
        
        """
        ...
    @staticmethod
    def getMonth(number: int) -> 'Month':
        """
        Get the month corresponding to a number.
        
        Parameters:
            number (int): month number
        
        Returns:
            the month corresponding to the string
        
        Raises:
            IllegalArgumentException: if the string does not correspond to a month
        
        
        """
        ...
    def getNumber(self) -> int:
        """
        Get the month number.
        
        Returns:
            month number between 1 and 12
        
        
        """
        ...
    def getUpperCaseAbbreviation(self) -> str:
        """
        Get the upper case three letters abbreviation.
        
        Returns:
            upper case three letters abbreviation
        
        
        """
        ...
    def getUpperCaseName(self) -> str:
        """
        Get the upper case full name.
        
        Returns:
            upper case full name
        
        
        """
        ...
    @staticmethod
    def parseMonth(s: str) -> 'Month':
        """
        Parse the string to get the month.
        
        The string can be either the month number, the full name or the three letter abbreviation. The parsing ignore the case of the specified string and trims surrounding blanks.
        
        Parameters:
            s (String): string to parse
        
        Returns:
            the month corresponding to the string
        
        Raises:
            IllegalArgumentException: if the string does not correspond to a month
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'Month':
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
    def values() -> typing.MutableSequence['Month']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (Month c : Month.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OffsetModel(java.io.Serializable):
    """
    TAI UTC offset model.
    
    Since:
        7.1
    
    Also see:
        UTCTAIOffsetsLoader, serialized
    """
    @typing.overload
    def __init__(self, dateComponents: DateComponents, int: int): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, int: int, timeOffset: 'TimeOffset', int2: int): ...
    def getMJDRef(self) -> int:
        """
        Get the reference date of the linear model as a modified julian day.
        
        Returns:
            reference date of the linear model as a modified julian day
        
        
        """
        ...
    def getOffset(self) -> 'TimeOffset':
        """
        Offset at reference date in seconds (TAI minus UTC).
        
        Returns:
            offset at reference date in seconds (TAI minus UTC)
        
        
        """
        ...
    def getSlope(self) -> int:
        """
        Offset slope in nanoseconds per UTC second (TAI minus UTC / dUTC).
        
        Returns:
            offset slope in nanoseconds per UTC second (TAI minus UTC / dUTC)
        
        
        """
        ...
    def getStart(self) -> DateComponents:
        """
        Get the date of the offset start.
        
        Returns:
            date of the offset start
        
        
        """
        ...

class TimeComponents(java.io.Serializable, java.lang.Comparable['TimeComponents']):
    """
    Class representing a time within the day broken up as hour, minute and second components.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        DateComponents, DateTimeComponents, serialized
    """
    H00: typing.ClassVar['TimeComponents'] = ...
    """
    Constant for commonly used hour 00:00:00.
    """
    H12: typing.ClassVar['TimeComponents'] = ...
    """
    Constant for commonly used hour 12:00:00.
    """
    NaN: typing.ClassVar['TimeComponents'] = ...
    """
    Constant for NaN time.
    
    Since:
        13.0
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, int3: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, timeOffset: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, int: int, int2: int, timeOffset: 'TimeOffset', int3: int): ...
    @typing.overload
    def __init__(self, timeOffset: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, timeOffset: 'TimeOffset', timeOffset2: 'TimeOffset', int: int): ...
    def compareTo(self, timeComponents: 'TimeComponents') -> int:
        """
        Specified by: Comparable in interface Comparable
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def formatUtcOffset(self) -> str:
        """
        Get the UTC offset as a string in ISO8601 format. For example, +00:00.
        
        Returns:
            the UTC offset as a string.
        
        Also see:
            toStringWithoutUtcOffset, toString
        
        
        """
        ...
    def getHour(self) -> int:
        """
        Get the hour number.
        
        Returns:
            hour number from 0 to 23
        
        
        """
        ...
    def getMinute(self) -> int:
        """
        Get the minute number.
        
        Returns:
            minute minute number from 0 to 59
        
        
        """
        ...
    def getMinutesFromUTC(self) -> int:
        """
        Get the offset between the specified date and UTC.
        
        The offset is always an integral number of minutes, as per ISO-8601 standard.
        
        Returns:
            offset in minutes between the specified date and UTC
        
        Since:
            7.2
        
        
        """
        ...
    def getSecond(self) -> float:
        """
        Get the seconds number.
        
        Returns:
            second second number from 0.0 to 61.0 (excluded). Note that 60 ≤ second < 61 only occurs during a leap second.
        
        
        """
        ...
    def getSecondsInLocalDay(self) -> float:
        """
        Get the second number within the local day, without applying the getMinutesFromUTC.
        
        Returns:
            second number from 0.0 to Constants.JULIAN_DAY
        
        Since:
            7.2
        
        Also see:
            getSplitSecondsInLocalDay,
            getSecondsInUTCDay
        
        
        """
        ...
    def getSecondsInUTCDay(self) -> float:
        """
        Get the second number within the UTC day, applying the getMinutesFromUTC.
        
        Returns:
            second number from getMinutesFromUTC to Constants.JULIAN_DAY
            getMinutesFromUTC
        
        Since:
            7.2
        
        Also see:
            getSplitSecondsInUTCDay,
            getSecondsInLocalDay
        
        
        """
        ...
    def getSplitSecond(self) -> 'TimeOffset':
        """
        Get the seconds number.
        
        Returns:
            second second number from 0.0 to 61.0 (excluded). Note that 60 ≤ second < 61 only occurs during a leap second.
        
        
        """
        ...
    def getSplitSecondsInLocalDay(self) -> 'TimeOffset':
        """
        Get the second number within the local day, without applying the getMinutesFromUTC.
        
        Returns:
            second number from 0.0 to Constants.JULIAN_DAY
        
        Since:
            13.0
        
        Also see:
            getSecondsInLocalDay,
            getSplitSecondsInUTCDay
        
        
        """
        ...
    def getSplitSecondsInUTCDay(self) -> 'TimeOffset':
        """
        Get the second number within the UTC day, applying the getMinutesFromUTC.
        
        Returns:
            second number from getMinutesFromUTC to Constants.JULIAN_DAY
            getMinutesFromUTC
        
        Since:
            13.0
        
        Also see:
            getSecondsInUTCDay,
            getSplitSecondsInLocalDay
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @staticmethod
    def parseTime(string: str) -> 'TimeComponents':
        """
        Parse a string in ISO-8601 format to build a time.
        
        The supported formats are:
        
          - basic and extended format local time: hhmmss, hh:mm:ss (with optional decimals in seconds)
          - optional UTC time: hhmmssZ, hh:mm:ssZ
          - optional signed hours UTC offset: hhmmss+HH, hhmmss-HH, hh:mm:ss+HH, hh:mm:ss-HH
          - optional signed basic hours and minutes UTC offset: hhmmss+HHMM, hhmmss-HHMM, hh:mm:ss+HHMM, hh:mm:ss-HHMM
          - optional signed extended hours and minutes UTC offset: hhmmss+HH:MM, hhmmss-HH:MM, hh:mm:ss+HH:MM, hh:mm:ss-HH:MM
        
        As shown by the list above, only the complete representations defined in section 4.2 of ISO-8601 standard are supported, neither expended representations nor representations with reduced accuracy are supported.
        
        Parameters:
            string (String): string to parse
        
        Returns:
            a parsed time
        
        Raises:
            IllegalArgumentException: if string cannot be parsed
        
        
        """
        ...
    def toString(self) -> str:
        """
        Get a string representation of the time including the offset from UTC.
        
        Overrides: Object in class Object
        
        Returns:
            string representation of the time in an ISO 8601 like format including the UTC offset.
        
        Also see:
            toStringWithoutUtcOffset,
            formatUtcOffset
        
        
        """
        ...
    def toStringWithoutUtcOffset(self) -> str:
        """
        Get a string representation of the time without the offset from UTC.
        
        Returns:
            a string representation of the time in an ISO 8601 like format.
        
        Also see:
            formatUtcOffset, toString
        
        
        """
        ...
    def wrapIfNeeded(self, minuteDuration: int, fractionDigits: int) -> 'TimeComponents':
        """
        Round this time to the given precision if needed to prevent rounding up to an invalid seconds number. This is useful, for example, when writing custom date-time formatting methods so one does not, e.g., end up with "60.0" seconds during a normal minute when the value of seconds is . This method will instead round up the minute, hour, day, month, and year as needed.
        
        Parameters:
            minuteDuration (int): 59, 60, 61, or 62 seconds depending on the date being close to a leap second introduction and the magnitude of the leap
                second.
            fractionDigits (int): the number of decimal digits after the decimal point in the seconds number that will be printed. This date-time is
                rounded to fractionDigits after the decimal point if necessary to prevent rounding up to minuteDuration.
                fractionDigits must be greater than or equal to .
        
        Returns:
            the instance itself if no rounding was needed, or a time within 5 * 10**-fractionDigits seconds of this, and
            with a seconds number that will not round up to minuteDuration when rounded to fractionDigits after the
            decimal point
        
        Since:
            13.0
        
        
        """
        ...

_TimeInterpolator__T = typing.TypeVar('_TimeInterpolator__T', bound='TimeStamped')  # <T>
class TimeInterpolator(typing.Generic[_TimeInterpolator__T]):
    """
    This interface represents objects that can interpolate a time stamped value with respect to time.
    
    Also see:
        AbsoluteDate, TimeStamped
    """
    def getExtrapolationThreshold(self) -> float:
        """
        Get the extrapolation threshold.
        
        Returns:
            get the extrapolation threshold
        
        
        """
        ...
    def getNbInterpolationPoints(self) -> int:
        """
        Get the number of interpolation points. In the specific case where this interpolator contains multiple sub-interpolators, this method will return the maximum number of interpolation points required among all sub-interpolators.
        
        Returns:
            the number of interpolation points
        
        Since:
            12.0.1
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List['TimeInterpolator'['TimeStamped']]:
        """
        Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: 'AbsoluteDate', collection: typing.Union[java.util.Collection[_TimeInterpolator__T], typing.Sequence[_TimeInterpolator__T], typing.Set[_TimeInterpolator__T]]) -> _TimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: 'AbsoluteDate', stream: java.util.stream.Stream[_TimeInterpolator__T]) -> _TimeInterpolator__T: ...

class TimeInterval:
    """
    Interface representing a closed time interval i.e. [a, b], possibly of infinite length.
    
    Since:
        13.1
    
    Also see:
        AbsoluteDate
    """
    @typing.overload
    def contains(self, timeInterval: 'TimeInterval') -> bool:
        """
        Method returning true if and only if the dated input is contained within the closed interval.
        
        Parameters:
            timeStamped (TimeStamped): time stamped object
        
        Returns:
            boolean on inclusion
        
        Method returning true if and only if input (also a closed time interval) contains the instance.
        
        Parameters:
            interval (TimeInterval): time interval
        
        Returns:
            boolean on inclusion
        
        
        """
        ...
    @typing.overload
    def contains(self, timeStamped: typing.Union['TimeStamped', typing.Callable]) -> bool: ...
    def duration(self) -> float:
        """
        Computes the interval length in seconds.
        
        Returns:
            duration
        
        
        """
        ...
    def getEndDate(self) -> 'AbsoluteDate':
        """
        Getter for the right end of the interval.
        
        Returns:
            right end
        
        
        """
        ...
    def getStartDate(self) -> 'AbsoluteDate':
        """
        Getter for the left end of the interval.
        
        Returns:
            left end
        
        
        """
        ...
    def intersects(self, interval: 'TimeInterval') -> bool:
        """
        Method returning true if and only if input (also a closed time interval) intersects the instance.
        
        Parameters:
            interval (TimeInterval): time interval
        
        Returns:
            boolean on intersection
        
        
        """
        ...
    @staticmethod
    def of(date: 'AbsoluteDate', otherDate: 'AbsoluteDate') -> 'TimeInterval':
        """
        Create instance from two dates in arbitrary order.
        
        Parameters:
            date (AbsoluteDate): date
            otherDate (AbsoluteDate): other date
        
        Returns:
            time interval
        
        
        """
        ...

class TimeOffset(java.lang.Comparable['TimeOffset'], java.io.Serializable):
    """
    This class represents a time range split into seconds and attoseconds.
    
    Instances of this class may either be interpreted as offsets from a reference date, or they may be interpreted as durations. Negative values represent dates earlier than the reference date in the first interpretation, and negative durations in the second interpretation.
    
    The whole number of seconds is stored as signed primitive long, so the range of dates that can be represented is ±292 billion years. The fractional part within the second is stored as non-negative primitive long with fixed precision at a resolution of one attosecond (10⁻¹⁸s). The choice of attoseconds allows to represent exactly all important offsets (between TT and TAI, or between UTC and TAI during the linear eras), as well as all times converted from standard Java Instant, Date or TimeUnit classes. It also allows simple computation as adding or subtracting a few values in attoseconds that are less than one second does not overflow (a primitive long could hold any values between ±9.22s in attoseconds so simple additions and subtractions followed by handling a carry to bring the value back between 0 and 10¹⁸ is straightforward). There are also special encodings (internally using negative longs in the fractional part) to represent NaN, POSITIVE_INFINITY and NEGATIVE_INFINITY.
    
    Since:
        13.0
    
    Also see:
        AbsoluteDate, FieldAbsoluteDate, serialized
    """
    ZERO: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 0.
    """
    ATTOSECOND: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 attosecond.
    """
    FEMTOSECOND: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 femtosecond.
    """
    PICOSECOND: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 picosecond.
    """
    NANOSECOND: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 nanosecond.
    """
    MICROSECOND: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 microsecond.
    """
    MILLISECOND: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 millisecond.
    """
    SECOND: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 second.
    """
    MINUTE: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 minute.
    """
    HOUR: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 hour.
    """
    DAY: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 day.
    """
    DAY_WITH_POSITIVE_LEAP: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing 1 day that includes an additional leap second.
    """
    NaN: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing a NaN.
    """
    NEGATIVE_INFINITY: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing negative infinity.
    """
    POSITIVE_INFINITY: typing.ClassVar['TimeOffset'] = ...
    """
    Split time representing positive infinity.
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, long: int, timeUnit: java.util.concurrent.TimeUnit): ...
    @typing.overload
    def __init__(self, long: int, long2: int): ...
    @typing.overload
    def __init__(self, long: int, timeOffset: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, long: int, timeOffset: 'TimeOffset', long2: int, timeOffset2: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, long: int, timeOffset: 'TimeOffset', long2: int, timeOffset2: 'TimeOffset', long3: int, timeOffset3: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, long: int, timeOffset: 'TimeOffset', long2: int, timeOffset2: 'TimeOffset', long3: int, timeOffset3: 'TimeOffset', long4: int, timeOffset4: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, long: int, timeOffset: 'TimeOffset', long2: int, timeOffset2: 'TimeOffset', long3: int, timeOffset3: 'TimeOffset', long4: int, timeOffset4: 'TimeOffset', long5: int, timeOffset5: 'TimeOffset'): ...
    @typing.overload
    def __init__(self, *timeOffset: 'TimeOffset'): ...
    def add(self, t: 'TimeOffset') -> 'TimeOffset':
        """
        Build a time by adding two times.
        
        Parameters:
            t (TimeOffset): time to add
        
        Returns:
            this+t
        
        
        """
        ...
    def compareTo(self, other: 'TimeOffset') -> int:
        """
        Compare the instance with another one.
        
        Not that in order to be consistent with Double, NaN is considered equal to itself and greater than positive infinity.
        
        Specified by: Comparable in interface Comparable
        
        Parameters:
            other (TimeOffset): other time to compare the instance to
        
        Returns:
            a negative integer, zero, or a positive integer if applying this time to reference date would result in a date being
            before, simultaneous, or after the date obtained by applying the other time to the same reference date.
        
        
        """
        ...
    def divide(self, q: int) -> 'TimeOffset':
        """
        Divide the instance by a positive constant.
        
        Parameters:
            q (int): division factor (must be strictly positive)
        
        Returns:
            this ÷ q
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getAttoSeconds(self) -> int:
        """
        Get the normalized attoseconds part of the time.
        
        The normalized attoseconds is always between 0L and 1000000000000000000L for finite ranges. Note that it may reach 1000000000000000000L if for example the time is less than 1 attosecond before a whole second. It is negative for isNaN or isInfinite times.
        
        Returns:
            normalized attoseconds part of the time
        
        
        """
        ...
    def getRoundedOffset(self, fractionDigits: int) -> 'TimeOffset':
        """
        Round to specified accuracy.
        
        For simplicity of implementation, the tiebreaking rule applied here is to round half towards positive infinity. This implies that rounding to 3 fraction digits an offset of exactly 2.0025s implies adding 0.0005s so the rounded value becomes 2.003s, whereas rounding to 3 fraction digits an offset of exactly -2.0025s also implies adding 0.0005s so the rounded value becomes -2.002s.
        
        Parameters:
            fractionDigits (int): the number of decimal digits after the decimal point in the seconds number
        
        Returns:
            rounded time offset
        
        Since:
            13.0.3
        
        
        """
        ...
    def getRoundedTime(self, unit: java.util.concurrent.TimeUnit) -> int:
        """
        Get the time in some unit.
        
        Parameters:
            unit (TimeUnit): time unit
        
        Returns:
            time in this unit, rounded to the closest long, returns arbitrarily
            Long for
            isNaN
        
        
        """
        ...
    def getSeconds(self) -> int:
        """
        Get the normalized seconds part of the time.
        
        Returns:
            normalized seconds part of the time (may be negative)
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def isFinite(self) -> bool:
        """
        Check if time is finite (i.e. neither isNaN nor isInfinite.
        
        Returns:
            true if time is finite
        
        Also see:
            isNaN, isInfinite,
            isNegativeInfinity, isPositiveInfinity
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Check if time is infinity.
        
        Returns:
            true if time is infinity
        
        Also see:
            isFinite, isNaN,
            isNegativeInfinity, isPositiveInfinity
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Check if time is NaN.
        
        Returns:
            true if time is NaN
        
        Also see:
            isFinite, isInfinite,
            isNegativeInfinity, isPositiveInfinity
        
        
        """
        ...
    def isNegativeInfinity(self) -> bool:
        """
        Check if time is negative infinity.
        
        Returns:
            true if time is negative infinity
        
        Also see:
            isFinite, isNaN,
            isInfinite, isPositiveInfinity
        
        
        """
        ...
    def isPositiveInfinity(self) -> bool:
        """
        Check if time is positive infinity.
        
        Returns:
            true if time is positive infinity
        
        Also see:
            isFinite, isNaN,
            isInfinite, isNegativeInfinity
        
        
        """
        ...
    def isZero(self) -> bool:
        """
        check if the time is zero.
        
        Returns:
            true if the time is zero
        
        
        """
        ...
    def multiply(self, p: int) -> 'TimeOffset':
        """
        Multiply the instance by a positive or zero constant.
        
        Parameters:
            p (long): multiplication factor (must be positive)
        
        Returns:
            this ⨉ p
        
        
        """
        ...
    def negate(self) -> 'TimeOffset':
        """
        Negate the instance.
        
        Returns:
            new instance corresponding to opposite time
        
        
        """
        ...
    @staticmethod
    def parse(s: str) -> 'TimeOffset':
        """
        Parse a string to produce an accurate split time.
        
        This method is more accurate than parsing the string as a double and then calling because it reads the before separator and after separator parts in decimal, hence avoiding problems like for example 0.1 not being an exact IEEE754 number.
        
        Parameters:
            s (String): string to parse
        
        Returns:
            parsed split time
        
        
        """
        ...
    def subtract(self, t: 'TimeOffset') -> 'TimeOffset':
        """
        Build a time by subtracting one time from the instance.
        
        Parameters:
            t (TimeOffset): time to subtract
        
        Returns:
            this-t
        
        
        """
        ...
    def toDouble(self) -> float:
        """
        Get the time collapsed into a single double.
        
        Beware that lots of accuracy is lost when combining getSeconds and getAttoSeconds into a single double.
        
        Returns:
            time as a single double
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class TimeScalarFunction:
    """
    This interface represents a scalar function of time.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, date: 'AbsoluteDate') -> float:
        """
        Compute a function of time.
        
        Parameters:
            date (AbsoluteDate): date
        
        Returns:
            value of the function
        
        """
        ...
    @typing.overload
    def value(self, date: 'FieldAbsoluteDate'[_value_1__T]) -> _value_1__T:
        """
        Compute a function of time.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
        
        Returns:
            value of the function
        
        
        """
        ...

class TimeScale:
    """
    Interface for time scales.
    
    This is the interface representing all time scales. Time scales are related to each other by some offsets that may be discontinuous (for example the UTCScale with respect to the TAIScale).
    
    Also see:
        AbsoluteDate
    """
    _getLeap_0__T = typing.TypeVar('_getLeap_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLeap(self, date: 'FieldAbsoluteDate'[_getLeap_0__T]) -> _getLeap_0__T:
        """
        Get the value of the previous leap.
        
        This method will return 0.0 for all time scales that do not implement leap seconds.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            value of the previous leap
        
        Since:
            9.0
        
        
        """
        ...
    @typing.overload
    def getLeap(self, date: 'AbsoluteDate') -> TimeOffset:
        """
        Get the value of the previous leap.
        
        This method will return 0 for all time scales that do not implement leap seconds.
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            value of the previous leap
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _insideLeap_1__T = typing.TypeVar('_insideLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def insideLeap(self, date: 'AbsoluteDate') -> bool:
        """
        Check if date is within a leap second introduction in this time scale.
        
        This method will return false for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale.
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            true if time is within a leap second introduction
        
        """
        ...
    @typing.overload
    def insideLeap(self, date: 'FieldAbsoluteDate'[_insideLeap_1__T]) -> bool:
        """
        Check if date is within a leap second introduction in this time scale.
        
        This method will return false for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            true if time is within a leap second introduction
        
        Since:
            9.0
        
        
        """
        ...
    _minuteDuration_1__T = typing.TypeVar('_minuteDuration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def minuteDuration(self, date: 'AbsoluteDate') -> int:
        """
        Check length of the current minute in this time scale.
        
        This method will return 60 for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale, and 61 for time scales that do implement leap second when the current date is within the last minute before the leap, or during the leap itself.
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            60 or 61 depending on leap seconds introduction
        
        """
        ...
    @typing.overload
    def minuteDuration(self, date: 'FieldAbsoluteDate'[_minuteDuration_1__T]) -> int:
        """
        Check length of the current minute in this time scale.
        
        This method will return 60 for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale, and 61 for time scales that do implement leap second when the current date is within the last minute before the leap, or during the leap itself.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            60 or 61 depending on leap seconds introduction
        
        Since:
            9.0
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Since:
            9.0
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: 'AbsoluteDate') -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def offsetToTAI(self, date: DateComponents, time: TimeComponents) -> TimeOffset:
        """
        Get the offset to convert locations from instance to TAIScale.
        
        Parameters:
            date (DateComponents): date location in the time scale
            time (TimeComponents): time location in the time scale
        
        Returns:
            offset in seconds to add to a location in instance time scale to get a location in TAIScale
            time scale
        
        Also see:
            offsetFromTAI
        
        
        """
        ...

class TimeScales:
    """
    A collection of TimeScales. This interface defines methods for obtaining instances of many common time scales.
    
    Since:
        10.1
    
    Also see:
        TimeScalesFactory, TimeScale,
        LazyLoadedTimeScales, of
    """
    def createBesselianEpoch(self, besselianEpoch: float) -> 'AbsoluteDate':
        """
        Build an instance corresponding to a Besselian Epoch (BE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date as:
        
         BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
        
        This method reverts the formula above and computes an AbsoluteDate from the Besselian Epoch.
        
        Parameters:
            besselianEpoch (double): Besselian epoch, like 1950 for defining the classical reference B1950.0
        
        Returns:
            a new instant
        
        Also see:
            createJulianEpoch
        
        
        """
        ...
    def createJulianEpoch(self, julianEpoch: float) -> 'AbsoluteDate':
        """
        Build an instance corresponding to a Julian Epoch (JE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
        
         JE = 2000.0 + (JED - 2451545.0) / 365.25
        
        This method reverts the formula above and computes an AbsoluteDate from the Julian Epoch.
        
        Parameters:
            julianEpoch (double): Julian epoch, like 2000.0 for defining the classical reference J2000.0
        
        Returns:
            a new instant
        
        Also see:
            getJ2000Epoch, createBesselianEpoch
        
        
        """
        ...
    def getBDT(self) -> 'BDTScale':
        """
        Get the BeiDou Navigation Satellite System time scale.
        
        Returns:
            BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    def getBeidouEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for BeiDou weeks: 2006-01-01T00:00:00 UTC.
        
        Returns:
            Beidou Epoch
        
        
        """
        ...
    def getCcsdsEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (not UTC).
        
        Returns:
            CCSDS Epoch
        
        
        """
        ...
    def getFiftiesEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
        
        Returns:
            Fifties Epoch
        
        
        """
        ...
    def getFutureInfinity(self) -> 'AbsoluteDate':
        """
        Dummy date at infinity in the future direction.
        
        Returns:
            the latest date.
        
        
        """
        ...
    def getGLONASS(self) -> 'GLONASSScale':
        """
        Get the GLObal NAvigation Satellite System time scale.
        
        Returns:
            GLObal NAvigation Satellite System time scale
        
        
        """
        ...
    def getGMST(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> 'GMSTScale':
        """
        Get the Greenwich Mean Sidereal Time scale.
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Greenwich Mean Sidereal Time scale
        
        Since:
            7.0
        
        
        """
        ...
    def getGPS(self) -> 'GPSScale':
        """
        Get the Global Positioning System scale.
        
        Returns:
            Global Positioning System scale
        
        
        """
        ...
    def getGST(self) -> 'GalileoScale':
        """
        Get the Galileo System Time scale.
        
        Returns:
            Galileo System Time scale
        
        
        """
        ...
    def getGalileoEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for Galileo System Time: 1999-08-22T00:00:00 GST.
        
        Returns:
            Galileo Epoch
        
        
        """
        ...
    def getGlonassEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for GLONASS four-year interval number: 1996-01-01T00:00:00 GLONASS time.
        
        By convention, TGLONASS = UTC + 3 hours.
        
        Returns:
            GLONASS Epoch
        
        
        """
        ...
    def getGpsEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
        
        Returns:
            GPS Epoch
        
        
        """
        ...
    def getJ2000Epoch(self) -> 'AbsoluteDate':
        """
        J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (not UTC).
        
        Returns:
            J2000 Epoch
        
        Also see:
            createJulianEpoch, createBesselianEpoch
        
        
        """
        ...
    def getJavaEpoch(self) -> 'AbsoluteDate':
        """
        Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
        
        Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587, UTC-TAI = 8.000082s
        
        Returns:
            Java Epoch
        
        
        """
        ...
    def getJulianEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
        
        Both Date and DateComponents classes follow the astronomical conventions and consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be seen in other documents or programs that obey a different convention (for example the convcal utility).
        
        Returns:
            Julian epoch.
        
        
        """
        ...
    def getModifiedJulianEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
        
        Returns:
            Modified Julian Epoch
        
        
        """
        ...
    def getNavIC(self) -> 'NavicScale':
        """
        Get the Navigation with Indian Constellation time scale.
        
        Returns:
            Navigation with Indian Constellation time scale
        
        
        """
        ...
    def getNavicEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for NavIC weeks: 1999-08-22T00:00:00 NavIC time.
        
        Returns:
            NavIC Epoch
        
        
        """
        ...
    def getPastInfinity(self) -> 'AbsoluteDate':
        """
        Dummy date at infinity in the past direction.
        
        Returns:
            the earliest date.
        
        
        """
        ...
    def getQZSS(self) -> 'QZSSScale':
        """
        Get the Quasi-Zenith Satellite System time scale.
        
        Returns:
            Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    def getQzssEpoch(self) -> 'AbsoluteDate':
        """
        Reference epoch for QZSS weeks: 1980-01-06T00:00:00 QZSS time.
        
        Returns:
            QZSS Epoch
        
        
        """
        ...
    def getTAI(self) -> 'TAIScale':
        """
        Get the International Atomic Time scale.
        
        Returns:
            International Atomic Time scale
        
        
        """
        ...
    def getTCB(self) -> 'TCBScale':
        """
        Get the Barycentric Coordinate Time scale.
        
        Returns:
            Barycentric Coordinate Time scale
        
        
        """
        ...
    def getTCG(self) -> 'TCGScale':
        """
        Get the Geocentric Coordinate Time scale.
        
        Returns:
            Geocentric Coordinate Time scale
        
        
        """
        ...
    def getTDB(self) -> 'TDBScale':
        """
        Get the Barycentric Dynamic Time scale.
        
        Returns:
            Barycentric Dynamic Time scale
        
        
        """
        ...
    def getTT(self) -> 'TTScale':
        """
        Get the Terrestrial Time scale.
        
        Returns:
            Terrestrial Time scale
        
        
        """
        ...
    def getUT1(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> 'UT1Scale':
        """
        Get the Universal Time 1 scale.
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Universal Time 1 scale
        
        Also see:
            getUTC, getEOPHistory
        
        
        """
        ...
    def getUTC(self) -> 'UTCScale':
        """
        Get the Universal Time Coordinate scale.
        
        Returns:
            Universal Time Coordinate scale
        
        
        """
        ...
    @staticmethod
    def of(utcMinusTai: typing.Union[java.util.Collection[OffsetModel], typing.Sequence[OffsetModel], typing.Set[OffsetModel]], eopSupplier: typing.Union[java.util.function.BiFunction[org.orekit.utils.IERSConventions, 'TimeScales', java.util.Collection[org.orekit.frames.EOPEntry]], typing.Callable[[org.orekit.utils.IERSConventions, 'TimeScales'], java.util.Collection[org.orekit.frames.EOPEntry]]]) -> 'TimeScales':
        """
        Create a set of time scales where all the data is loaded from the given functions.
        
        Parameters:
            utcMinusTai (Collection<? extends OffsetModel> utcMinusTai): offsets used to compute UTC. If the pre-1972 linear offsets are missing they will be added.
            eopSupplier (BiFunction<? super IERSConventions, ? super TimeScales, ? extends Collection<? extends EOPEntry>>): function to retrieve the EOP data. Since the EOP have to be reloaded every time a different
                IERSConventions is requested this function may be called multiple times. The requested
                conventions and the created time scales are passed as arguments. Attempting to call
                getUT1 or getGMST on the time scales argument
                may result in unbounded recursion. To ignore EOP corrections this function should return an empty collection.
        
        Returns:
            a set of time scales based on the given data.
        
        Also see:
            Parser, Parser
        
        
        """
        ...

class TimeScalesFactory(java.io.Serializable):
    """
    Factory for predefined time scales.
    
    This is a utility class, so its constructor is private.
    
    Also see:
        TimeScales, LazyLoadedTimeScales, serialized
    """
    @staticmethod
    def addDefaultUTCTAIOffsetsLoaders() -> None:
        """
        Add the default loaders for UTC-TAI offsets history files (both IERS and USNO).
        
        The default loaders are TAIUTCDatFilesLoader that looks for a file named dat that must be in USNO format and UTCTAIHistoryFilesLoader that looks fir a file named history that must be in the IERS format. The UTCTAIBulletinAFilesLoader is not added by default as it is not recommended. USNO warned us that the TAI-UTC data present in bulletin A was for convenience only and was not reliable, there have been errors in several bulletins regarding these data.
        
        Since:
            7.1
        
        Also see:
            `USNO tai-utc.dat file <http://maia.usno.navy.mil/ser7/tai-utc.dat>`, `IERS UTC-TAI.history file
            <http://hpiers.obspm.fr/eoppc/bul/bulc/UTC-TAI.history>`, TAIUTCDatFilesLoader,
            UTCTAIHistoryFilesLoader, getUTC,
            clearUTCTAIOffsetsLoaders
        
        
        """
        ...
    @staticmethod
    def addUTCTAIOffsetsLoader(loader: typing.Union['UTCTAIOffsetsLoader', typing.Callable]) -> None:
        """
        Add a loader for UTC-TAI offsets history files.
        
        Parameters:
            loader (UTCTAIOffsetsLoader): custom loader to add
        
        Since:
            7.1
        
        Also see:
            TAIUTCDatFilesLoader, UTCTAIHistoryFilesLoader,
            UTCTAIBulletinAFilesLoader, getUTC,
            clearUTCTAIOffsetsLoaders
        
        
        """
        ...
    @staticmethod
    def clearUTCTAIOffsetsLoaders() -> None:
        """
        Clear loaders for UTC-TAI offsets history files.
        
        Since:
            7.1
        
        Also see:
            getUTC, addUTCTAIOffsetsLoader,
            addDefaultUTCTAIOffsetsLoaders
        
        
        """
        ...
    @staticmethod
    def getBDT() -> 'BDTScale':
        """
        Get the BeiDou Navigation Satellite System time scale.
        
        Returns:
            BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    @staticmethod
    def getGLONASS() -> 'GLONASSScale':
        """
        Get the GLObal NAvigation Satellite System time scale.
        
        Returns:
            GLObal NAvigation Satellite System time scale
        
        
        """
        ...
    @staticmethod
    def getGMST(conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> 'GMSTScale':
        """
        Get the Greenwich Mean Sidereal Time scale.
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Greenwich Mean Sidereal Time scale
        
        Since:
            7.0
        
        
        """
        ...
    @staticmethod
    def getGPS() -> 'GPSScale':
        """
        Get the Global Positioning System scale.
        
        Returns:
            Global Positioning System scale
        
        
        """
        ...
    @staticmethod
    def getGST() -> 'GalileoScale':
        """
        Get the Galileo System Time scale.
        
        Returns:
            Galileo System Time scale
        
        
        """
        ...
    @staticmethod
    def getNavIC() -> 'NavicScale':
        """
        Get the Navigation with Indian Constellation time scale.
        
        Returns:
            Navigation with Indian Constellation time scale
        
        
        """
        ...
    @staticmethod
    def getQZSS() -> 'QZSSScale':
        """
        Get the Quasi-Zenith Satellite System time scale.
        
        Returns:
            Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    @staticmethod
    def getTAI() -> 'TAIScale':
        """
        Get the International Atomic Time scale.
        
        Returns:
            International Atomic Time scale
        
        
        """
        ...
    @staticmethod
    def getTCB() -> 'TCBScale':
        """
        Get the Barycentric Coordinate Time scale.
        
        Returns:
            Barycentric Coordinate Time scale
        
        
        """
        ...
    @staticmethod
    def getTCG() -> 'TCGScale':
        """
        Get the Geocentric Coordinate Time scale.
        
        Returns:
            Geocentric Coordinate Time scale
        
        
        """
        ...
    @staticmethod
    def getTDB() -> 'TDBScale':
        """
        Get the Barycentric Dynamic Time scale.
        
        Returns:
            Barycentric Dynamic Time scale
        
        
        """
        ...
    @staticmethod
    def getTT() -> 'TTScale':
        """
        Get the Terrestrial Time scale.
        
        Returns:
            Terrestrial Time scale
        
        
        """
        ...
    @staticmethod
    def getTimeScales() -> 'LazyLoadedTimeScales':
        """
        Get the instance of TimeScales that is called by all of the static methods in this class.
        
        Returns:
            the time scales used by this factory.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getUT1(eOPHistory: org.orekit.frames.EOPHistory) -> 'UT1Scale': ...
    @typing.overload
    @staticmethod
    def getUT1(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'UT1Scale': ...
    @staticmethod
    def getUTC() -> 'UTCScale':
        """
        Get the Universal Time Coordinate scale.
        
        If no UTCTAIOffsetsLoader has been added by calling addUTCTAIOffsetsLoader or if clearUTCTAIOffsetsLoaders has been called afterwards, the addDefaultUTCTAIOffsetsLoaders method will be called automatically.
        
        Returns:
            Universal Time Coordinate scale
        
        Also see:
            addDefaultUTCTAIOffsetsLoaders
        
        
        """
        ...

_TimeShiftable__T = typing.TypeVar('_TimeShiftable__T', bound='TimeShiftable')  # <T>
class TimeShiftable(typing.Generic[_TimeShiftable__T]):
    """
    This interface represents objects that can be shifted in time.
    """
    @typing.overload
    def shiftedBy(self, double: float) -> _TimeShiftable__T:
        """
        Get a time-shifted instance.
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        Get a time-shifted instance.
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: TimeOffset) -> _TimeShiftable__T: ...

class TimeStamped:
    """
    This interface represents objects that have a AbsoluteDate date attached to them.
    
    Classes implementing this interface can be stored chronologically in sorted sets using ChronologicalComparator as the underlying comparator. An example using for Orbit instances is given here:
    
    
         SortedSet<Orbit> sortedOrbits =
             new TreeSet<Orbit>(new ChronologicalComparator());
         sortedOrbits.add(orbit1);
         sortedOrbits.add(orbit2);
         ...
     
    
    This interface is also the base interface used to TimeStampedCache series of time-dependent objects for interpolation in a thread-safe manner.
    
    Also see:
        AbsoluteDate, ChronologicalComparator,
        TimeStampedCache
    """
    def durationFrom(self, other: typing.Union['TimeStamped', typing.Callable]) -> float:
        """
        Compute the physically elapsed duration between two instants.
        
        The returned duration is the number of seconds physically elapsed between the two instants, measured in a regular time scale with respect to surface of the Earth (i.e either the TAIScale, the TTScale or the GPSScale). It is the only method that gives a duration with a physical meaning.
        
        Parameters:
            other (TimeStamped): instant to subtract from the instance
        
        Returns:
            offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Since:
            12.0
        
        Also see:
            durationFrom
        
        
        """
        ...
    def getDate(self) -> 'AbsoluteDate':
        """
        Get the date.
        
        Returns:
            date attached to the object
        
        
        """
        ...

class TimeVectorFunction:
    """
    This interface represents a multi-valued function of time.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, date: 'AbsoluteDate') -> typing.MutableSequence[float]:
        """
        Compute a function of time.
        
        Parameters:
            date (AbsoluteDate): date
        
        Returns:
            value of the function
        
        """
        ...
    @typing.overload
    def value(self, date: 'FieldAbsoluteDate'[_value_1__T]) -> typing.MutableSequence[_value_1__T]:
        """
        Compute a function of time.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
        
        Returns:
            value of the function
        
        
        """
        ...

class UTCTAIOffsetsLoader:
    """
    Interface for loading UTC-TAI offsets data files.
    
    Since:
        7.1
    """
    def loadOffsets(self) -> java.util.List[OffsetModel]:
        """
        Load UTC-TAI offsets entries.
        
        Returns:
            sorted UTC-TAI offsets entries (if the linear offsets used prior to 1972 are missing, they will be inserted
            automatically)
        
        
        """
        ...
    class Parser:
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class AGILeapSecondFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    Loader for UTC-TAI extracted from LeapSecond file from AGI.
    
    This class is immutable and hence thread-safe
    
    Since:
        10.3
    
    Also see:
        dat
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default supported files name pattern.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]:
        """
        Load UTC-TAI offsets entries.
        
        Specified by: loadOffsets in interface UTCTAIOffsetsLoader
        
        Returns:
            sorted UTC-TAI offsets entries (if the linear offsets used prior to 1972 are missing, they will be inserted
            automatically)
        
        
        """
        ...
    class Parser(UTCTAIOffsetsLoader.Parser):
        def __init__(self): ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class AbsoluteDate(TimeOffset, TimeStamped, TimeShiftable['AbsoluteDate'], java.lang.Comparable[TimeOffset], java.io.Serializable):
    """
    This class represents a specific instant in time.
    
    Instances of this class are considered to be absolute in the sense that each one represent the occurrence of some event and can be compared to other instances or located in any TimeScale. In other words the different locations of an event with respect to two different time scales (say TAIScale and UTCScale for example) are simply different perspective related to a single object. Only one AbsoluteDate instance is needed, both representations being available from this single instance by specifying the time scales as parameter when calling the ad-hoc methods.
    
    Since an instance is not bound to a specific time-scale, all methods related to the location of the date within some time scale require to provide the time scale as an argument. It is therefore possible to define a date in one time scale and to use it in another one. An example of such use is to read a date from a file in UTC and write it in another file in TAI. This can be done as follows:
    
    
       DateTimeComponents utcComponents = readNextDate();
       AbsoluteDate date = new AbsoluteDate(utcComponents, TimeScalesFactory.getUTC());
       writeNextDate(date.getComponents(TimeScalesFactory.getTAI()));
     
    
    Two complementary views are available:
    
      - 
        location view (mainly for input/output or conversions)
    
        locations represent the coordinate of one event with respect to a TimeScale. The related
        methods are , parseCCSDSCalendarSegmentedTimeCode, toDate,
        toString, toString, and
        timeScalesOffset.
      - 
        offset view (mainly for physical computation)
    
        offsets represent either the flow of time between two events (two instances of the class) or durations. They are counted in seconds, are continuous and could be measured using only a virtually perfect stopwatch. The related methods are , parseCCSDSUnsegmentedTimeCode, parseCCSDSDaySegmentedTimeCode, durationFrom, compareTo, equals and hashCode.
    
    A few reference epochs which are commonly used in space systems have been defined. These epochs can be used as the basis for offset computation. The supported epochs are: JULIAN_EPOCH, MODIFIED_JULIAN_EPOCH, FIFTIES_EPOCH, CCSDS_EPOCH, GALILEO_EPOCH, GPS_EPOCH, QZSS_EPOCH J2000_EPOCH, JAVA_EPOCH. There are also two factory methods createJulianEpoch and createBesselianEpoch that can be used to compute other reference epochs like J1900.0 or B1950.0. In addition to these reference epochs, two other constants are defined for convenience: PAST_INFINITY and FUTURE_INFINITY, which can be used either as dummy dates when a date is not yet initialized, or for initialization of loops searching for a min or max date.
    
    Instances of the AbsoluteDate class are guaranteed to be immutable.
    
    Also see:
        TimeScale, TimeStamped,
        ChronologicalComparator, serialized
    """
    JULIAN_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
    
    Both Date and DateComponents classes follow the astronomical conventions and consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be seen in other documents or programs that obey a different convention (for example the convcal utility).
    
    This constant uses the getDefault.
    
    Also see:
        getJulianEpoch
    
    
    """
    MODIFIED_JULIAN_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
    
    This constant uses the getDefault.
    
    Also see:
        getModifiedJulianEpoch
    
    
    """
    FIFTIES_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
    
    This constant uses the getDefault.
    
    Also see:
        getFiftiesEpoch
    
    
    """
    CCSDS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (not UTC).
    
    This constant uses the getDefault.
    
    Also see:
        getCcsdsEpoch
    
    
    """
    GALILEO_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for Galileo System Time: 1999-08-22T00:00:00 GST.
    
    This constant uses the getDefault.
    
    Also see:
        getGalileoEpoch
    
    
    """
    GPS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
    
    This constant uses the getDefault.
    
    Also see:
        getGpsEpoch
    
    
    """
    QZSS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for QZSS weeks: 1980-01-06T00:00:00 QZSS time.
    
    This constant uses the getDefault.
    
    Also see:
        getQzssEpoch
    
    
    """
    NAVIC_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for NavIC weeks: 1999-08-22T00:00:00 NavIC time.
    
    This constant uses the getDefault.
    
    Also see:
        getNavicEpoch
    
    
    """
    BEIDOU_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for BeiDou weeks: 2006-01-01T00:00:00 UTC.
    
    This constant uses the getDefault.
    
    Also see:
        getBeidouEpoch
    
    
    """
    GLONASS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Reference epoch for GLONASS four-year interval number: 1996-01-01T00:00:00 GLONASS time.
    
    By convention, TGLONASS = UTC + 3 hours.
    
    This constant uses the getDefault.
    
    Also see:
        getGlonassEpoch
    
    
    """
    J2000_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (not UTC).
    
    This constant uses the getDefault.
    
    Also see:
        createJulianEpoch, createBesselianEpoch,
        getJ2000Epoch
    
    
    """
    JAVA_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
    
    Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587, UTC-TAI = 8.000082s
    
    This constant uses the getDefault.
    
    Also see:
        getJavaEpoch
    
    
    """
    ARBITRARY_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    An arbitrary finite date. Uses when a non-null date is needed but its value doesn't matter.
    """
    PAST_INFINITY: typing.ClassVar['AbsoluteDate'] = ...
    """
    Dummy date at infinity in the past direction.
    
    Also see:
        getPastInfinity
    
    
    """
    FUTURE_INFINITY: typing.ClassVar['AbsoluteDate'] = ...
    """
    Dummy date at infinity in the future direction.
    
    Also see:
        getFutureInfinity
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, timeOffset: TimeOffset, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, month: Month, int2: int, int3: int, int4: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, month: Month, int2: int, int3: int, int4: int, timeOffset: TimeOffset, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, month: Month, int2: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, string: str, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, instant: typing.Union[java.time.Instant, datetime.datetime]): ...
    @typing.overload
    def __init__(self, instant: typing.Union[java.time.Instant, datetime.datetime], timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, instant: typing.Union[java.time.Instant, datetime.datetime], uTCScale: 'UTCScale'): ...
    @typing.overload
    def __init__(self, date: java.util.Date, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, absoluteDate: 'AbsoluteDate', double: float): ...
    @typing.overload
    def __init__(self, absoluteDate: 'AbsoluteDate', double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, absoluteDate: 'AbsoluteDate', long: int, timeUnit: java.util.concurrent.TimeUnit): ...
    @typing.overload
    def __init__(self, absoluteDate: 'AbsoluteDate', timeOffset: TimeOffset): ...
    @typing.overload
    def __init__(self, absoluteDate: 'AbsoluteDate', timeOffset: TimeOffset, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, timeComponents: TimeComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, dateTimeComponents: DateTimeComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, timeOffset: TimeOffset): ...
    def accurateDurationFrom(self, instant: 'AbsoluteDate') -> TimeOffset:
        """
        Compute the physically elapsed duration between two instants.
        
        The returned duration is the number of seconds physically elapsed between the two instants, measured in a regular time scale with respect to surface of the Earth (i.e either the TAIScale, the TTScale or the GPSScale). It is the only method that gives a duration with a physical meaning.
        
        This method gives the same result (with less computation) as calling offsetFrom with a second argument set to one of the regular scales cited above.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (AbsoluteDate): instant to subtract from the instance
        
        Returns:
            offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Since:
            13.0
        
        Also see:
            durationFrom, offsetFrom,
            
        
        
        """
        ...
    def accurateOffsetFrom(self, instant: 'AbsoluteDate', timeScale: TimeScale) -> TimeOffset:
        """
        Compute the apparent clock offset between two instant in the perspective of a specific TimeScale.
        
        The offset is the number of seconds counted in the given time scale between the locations of the two instants, with all time scale irregularities removed (i.e. considering all days are exactly 86400 seconds long). This method will give a result that may not have a physical meaning if the time scale is irregular. For example since a leap second was introduced at the end of 2005, the apparent clock offset between 2005-12-31T23:59:59 and 2006-01-01T00:00:00 is 1 second and is the value this method will return. On the other hand, the physical duration of the corresponding time interval as returned by the durationFrom method is 2 seconds.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (AbsoluteDate): instant to subtract from the instance
            timeScale (TimeScale): time scale with respect to which the offset should be computed
        
        Returns:
            apparent clock offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Since:
            13.0
        
        Also see:
            durationFrom, offsetFrom,
            
        
        
        """
        ...
    @staticmethod
    def createBesselianEpoch(besselianEpoch: float) -> 'AbsoluteDate':
        """
        Build an instance corresponding to a Besselian Epoch (BE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date as:
        
         BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
        
        This method reverts the formula above and computes an AbsoluteDate from the Besselian Epoch.
        
        This method uses the getDefault.
        
        Parameters:
            besselianEpoch (double): Besselian epoch, like 1950 for defining the classical reference B1950.0
        
        Returns:
            a new instant
        
        Also see:
            createJulianEpoch, createBesselianEpoch
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createJDDate(int: int, double: float, timeScale: TimeScale) -> 'AbsoluteDate':
        """
        Build an instance corresponding to a Julian Day date.
        
        Parameters:
            jd (int): Julian day
            secondsSinceNoon (double): seconds in the Julian day (BEWARE, Julian days start at noon, so 0.0 is noon)
            timeScale (TimeScale): time scale in which the seconds in day are defined
        
        Returns:
            a new instant
        
        Build an instance corresponding to a Julian Day date.
        
        This function should be preferred to createMJDDate when the target time scale has a non-constant offset with respect to TAI.
        
        The idea is to introduce a pivot time scale that is close to the target time scale but has a constant bias with TAI.
        
        For example, to get a date from an MJD in TDB time scale, it's advised to use the TT time scale as a pivot scale. TT is very close to TDB and has constant offset to TAI.
        
        Parameters:
            jd (int): Julian day
            secondsSinceNoon (double): seconds in the Julian day (BEWARE, Julian days start at noon, so 0.0 is noon)
            timeScale (TimeScale): timescale in which the seconds in day are defined
            pivotTimeScale (TimeScale): pivot timescale used as intermediate timescale
        
        Returns:
            a new instant
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createJDDate(int: int, double: float, timeScale: TimeScale, timeScale2: TimeScale) -> 'AbsoluteDate': ...
    @staticmethod
    def createJulianEpoch(julianEpoch: float) -> 'AbsoluteDate':
        """
        Build an instance corresponding to a Julian Epoch (JE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
        
         JE = 2000.0 + (JED - 2451545.0) / 365.25
        
        This method reverts the formula above and computes an AbsoluteDate from the Julian Epoch.
        
        This method uses the getDefault.
        
        Parameters:
            julianEpoch (double): Julian epoch, like 2000.0 for defining the classical reference J2000.0
        
        Returns:
            a new instant
        
        Also see:
            J2000_EPOCH, createBesselianEpoch,
            createJulianEpoch
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createMJDDate(int: int, double: float, timeScale: TimeScale) -> 'AbsoluteDate': ...
    @typing.overload
    @staticmethod
    def createMJDDate(int: int, timeOffset: TimeOffset, timeScale: TimeScale) -> 'AbsoluteDate': ...
    @staticmethod
    def createMedian(date1: 'AbsoluteDate', date2: 'AbsoluteDate') -> 'AbsoluteDate':
        """
        Create an instance as the median data between two existing instances.
        
        Parameters:
            date1 (AbsoluteDate): first instance
            date2 (AbsoluteDate): second instance
        
        Returns:
            median date between first and second instance
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def durationFrom(self, timeStamped: typing.Union[TimeStamped, typing.Callable]) -> float:
        """
        Compute the physically elapsed duration between two instants.
        
        The returned duration is the number of seconds physically elapsed between the two instants, measured in a regular time scale with respect to surface of the Earth (i.e either the TAIScale, the TTScale or the GPSScale). It is the only method that gives a duration with a physical meaning.
        
        This method gives the same result (with less computation) as calling offsetFrom with a second argument set to one of the regular scales cited above.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (AbsoluteDate): instant to subtract from the instance
        
        Returns:
            offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Also see:
            accurateDurationFrom, offsetFrom,
            
        
        Compute the physically elapsed duration between two instants.
        
        The returned duration is the duration physically elapsed between the two instants, using the given time unit and rounded to the nearest integer, measured in a regular time scale with respect to surface of the Earth (i.e either the TAIScale, the TTScale or the GPSScale). It is the only method that gives a duration with a physical meaning.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (AbsoluteDate): instant to subtract from the instance
            timeUnit (TimeUnit): TimeUnit precision for the
                offset
        
        Returns:
            offset in the given timeunit between the two instants (positive if the instance is posterior to the argument), rounded
            to the nearest integer
            TimeUnit
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def durationFrom(self, absoluteDate: 'AbsoluteDate') -> float: ...
    @typing.overload
    def durationFrom(self, absoluteDate: 'AbsoluteDate', timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    @typing.overload
    def getComponents(self, int: int) -> DateTimeComponents:
        """
        Split the instance into date/time components.
        
        Parameters:
            timeScale (TimeScale): time scale to use
        
        Returns:
            date/time components
        
        Split the instance into date/time components for a local time.
        
        This method uses the getDefault.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC)
        
        Returns:
            date/time components
        
        Since:
            7.2
        
        Also see:
            getComponents
        
        Split the instance into date/time components for a local time.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC)
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            date/time components
        
        Since:
            10.1
        
        Split the instance into date/time components for a time zone.
        
        This method uses the getDefault.
        
        Parameters:
            timeZone (TimeZone): time zone
        
        Returns:
            date/time components
        
        Since:
            7.2
        
        Also see:
            getComponents
        
        Split the instance into date/time components for a time zone.
        
        Parameters:
            timeZone (TimeZone): time zone
            utc (TimeScale): time scale used to computed date and time components.
        
        Returns:
            date/time components
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getComponents(self, int: int, timeScale: TimeScale) -> DateTimeComponents: ...
    @typing.overload
    def getComponents(self, timeZone: java.util.TimeZone) -> DateTimeComponents: ...
    @typing.overload
    def getComponents(self, timeZone: java.util.TimeZone, timeScale: TimeScale) -> DateTimeComponents: ...
    @typing.overload
    def getComponents(self, timeScale: TimeScale) -> DateTimeComponents: ...
    def getDate(self) -> 'AbsoluteDate':
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getDayOfYear(self, utc: TimeScale) -> float:
        """
        Get day of year, preserving continuity as much as possible.
        
        This is a continuous extension of the integer value returned by getComponentsgetDategetDayOfYear. In order to have it remain as close as possible to its integer counterpart, day 1.0 is considered to occur on January 1st at noon.
        
        Continuity is preserved from day to day within a year, but of course there is a discontinuity at year change, where it switches from 365.49999… (or 366.49999… on leap years) to 0.5
        
        Parameters:
            utc (TimeScale): time scale to compute date components
        
        Returns:
            day of year, with day 1.0 occurring on January first at noon
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def getJD(self) -> float:
        """
        Return the given date as a Julian Date expressed in UTC.
        
        Returns:
            double representation of the given date as Julian Date.
        
        Since:
            12.2
        
        """
        ...
    @typing.overload
    def getJD(self, ts: TimeScale) -> float:
        """
        Return the given date as a Julian Date expressed in given timescale.
        
        Parameters:
            ts (TimeScale): time scale
        
        Returns:
            double representation of the given date as Julian Date.
        
        Since:
            12.2
        
        
        """
        ...
    @typing.overload
    def getMJD(self) -> float:
        """
        Return the given date as a Modified Julian Date expressed in UTC.
        
        Returns:
            double representation of the given date as Modified Julian Date.
        
        Since:
            12.2
        
        """
        ...
    @typing.overload
    def getMJD(self, ts: TimeScale) -> float:
        """
        Return the given date as a Modified Julian Date expressed in given timescale.
        
        Parameters:
            ts (TimeScale): time scale
        
        Returns:
            double representation of the given date as Modified Julian Date.
        
        Since:
            12.2
        
        
        """
        ...
    def isAfter(self, other: typing.Union[TimeStamped, typing.Callable]) -> bool:
        """
        Check if the instance represents a time that is strictly after another.
        
        Parameters:
            other (TimeStamped): the instant to compare this date to
        
        Returns:
            true if the instance is strictly after the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isAfterOrEqualTo
        
        
        """
        ...
    def isAfterOrEqualTo(self, other: typing.Union[TimeStamped, typing.Callable]) -> bool:
        """
        Check if the instance represents a time that is after or equal to another.
        
        Parameters:
            other (TimeStamped): the instant to compare this date to
        
        Returns:
            true if the instance is after (or equal to) the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isAfterOrEqualTo
        
        
        """
        ...
    def isBefore(self, other: typing.Union[TimeStamped, typing.Callable]) -> bool:
        """
        Check if the instance represents a time that is strictly before another.
        
        Parameters:
            other (TimeStamped): the instant to compare this date to
        
        Returns:
            true if the instance is strictly before the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBeforeOrEqualTo
        
        
        """
        ...
    def isBeforeOrEqualTo(self, other: typing.Union[TimeStamped, typing.Callable]) -> bool:
        """
        Check if the instance represents a time that is before or equal to another.
        
        Parameters:
            other (TimeStamped): the instant to compare this date to
        
        Returns:
            true if the instance is before (or equal to) the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBefore
        
        
        """
        ...
    def isBetween(self, boundary: typing.Union[TimeStamped, typing.Callable], otherBoundary: typing.Union[TimeStamped, typing.Callable]) -> bool:
        """
        Check if the instance represents a time that is strictly between two others representing the boundaries of a time span. The two boundaries can be provided in any order: in other words, whether boundary represents a time that is before or after otherBoundary will not change the result of this method.
        
        Parameters:
            boundary (TimeStamped): one end of the time span
            otherBoundary (TimeStamped): the other end of the time span
        
        Returns:
            true if the instance is strictly between the two arguments when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBetweenOrEqualTo
        
        
        """
        ...
    def isBetweenOrEqualTo(self, boundary: typing.Union[TimeStamped, typing.Callable], otherBoundary: typing.Union[TimeStamped, typing.Callable]) -> bool:
        """
        Check if the instance represents a time that is between two others representing the boundaries of a time span, or equal to one of them. The two boundaries can be provided in any order: in other words, whether boundary represents a time that is before or after otherBoundary will not change the result of this method.
        
        Parameters:
            boundary (TimeStamped): one end of the time span
            otherBoundary (TimeStamped): the other end of the time span
        
        Returns:
            true if the instance is between the two arguments (or equal to at least one of them) when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBetween
        
        
        """
        ...
    def isCloseTo(self, other: typing.Union[TimeStamped, typing.Callable], tolerance: float) -> bool:
        """
        Check if the instance time is close to another.
        
        Parameters:
            other (TimeStamped): the instant to compare this date to
            tolerance (double): the separation, in seconds, under which the two instants will be considered close to each other
        
        Returns:
            true if the duration between the instance and the argument is strictly below the tolerance
        
        Since:
            10.1
        
        Also see:
            isEqualTo
        
        
        """
        ...
    def isEqualTo(self, other: typing.Union[TimeStamped, typing.Callable]) -> bool:
        """
        Check if the instance represents the same time as another.
        
        Parameters:
            other (TimeStamped): the instant to compare this date to
        
        Returns:
            true if the instance and the argument refer to the same instant
        
        Since:
            10.1
        
        Also see:
            isCloseTo
        
        
        """
        ...
    def offsetFrom(self, instant: 'AbsoluteDate', timeScale: TimeScale) -> float:
        """
        Compute the apparent clock offset between two instant in the perspective of a specific TimeScale.
        
        The offset is the number of seconds counted in the given time scale between the locations of the two instants, with all time scale irregularities removed (i.e. considering all days are exactly 86400 seconds long). This method will give a result that may not have a physical meaning if the time scale is irregular. For example since a leap second was introduced at the end of 2005, the apparent clock offset between 2005-12-31T23:59:59 and 2006-01-01T00:00:00 is 1 second and is the value this method will return. On the other hand, the physical duration of the corresponding time interval as returned by the durationFrom method is 2 seconds.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (AbsoluteDate): instant to subtract from the instance
            timeScale (TimeScale): time scale with respect to which the offset should be computed
        
        Returns:
            apparent clock offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Also see:
            durationFrom, accurateOffsetFrom,
            
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSCalendarSegmentedTimeCode(byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> 'AbsoluteDate':
        """
        CCSDS Calendar Segmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in November 2010
        
        Parameters:
            preambleField (byte): field specifying the format, often not transmitted in data interfaces, as it is constant for a given data interface
            timeField (byte[]): byte array containing the time code
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            an instance corresponding to the specified date
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSCalendarSegmentedTimeCode(byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], timeScale: TimeScale) -> 'AbsoluteDate': ...
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], dateComponents: DateComponents) -> 'AbsoluteDate':
        """
        CCSDS Day Segmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in November 2010
        
        Parameters:
            preambleField (byte): field specifying the format, often not transmitted in data interfaces, as it is constant for a given data interface
            timeField (byte[]): byte array containing the time code
            agencyDefinedEpoch (DateComponents): reference epoch, ignored if the preamble field specifies the CCSDS_EPOCH is used
                (and hence may be null in this case)
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            an instance corresponding to the specified date
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], dateComponents: DateComponents, timeScale: TimeScale) -> 'AbsoluteDate': ...
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(byte: int, byte2: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], absoluteDate: 'AbsoluteDate') -> 'AbsoluteDate':
        """
        CCSDS Unsegmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in November 2010
        
        If the date to be parsed is formatted using version 3 of the standard (CCSDS 301.0-B-3 published in 2002) or if the extension of the preamble field introduced in version 4 of the standard is not used, then the preambleField2 parameter can be set to 0.
        
        Parameters:
            preambleField1 (byte): first byte of the field specifying the format, often not transmitted in data interfaces, as it is constant for a given
                data interface
            preambleField2 (byte): second byte of the field specifying the format (added in revision 4 of the CCSDS standard in 2010), often not
                transmitted in data interfaces, as it is constant for a given data interface (value ignored if presence not signaled in
                preambleField1)
            timeField (byte[]): byte array containing the time code
            agencyDefinedEpoch (AbsoluteDate): reference epoch, ignored if the preamble field specifies the CCSDS_EPOCH is used
                (and hence may be null in this case, but then ccsdsEpoch must be non-null)
            ccsdsEpoch (AbsoluteDate): reference epoch, ignored if the preamble field specifies the agency epoch is used (and hence may be null in this case,
                but then agencyDefinedEpoch must be non-null).
        
        Returns:
            an instance corresponding to the specified date
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(byte: int, byte2: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], absoluteDate: 'AbsoluteDate', absoluteDate2: 'AbsoluteDate') -> 'AbsoluteDate': ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'AbsoluteDate':
        """
        Get a time-shifted instance.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        Get a time-shifted instance.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        Get a time-shifted date.
        
        Calling this method is equivalent to call new AbsoluteDate(this, shift, timeUnit).
        
        Parameters:
            dt (long): time shift in time units
            timeUnit (TimeUnit): TimeUnit of the shift
        
        Returns:
            a new date, shifted with respect to instance (which is immutable)
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> 'AbsoluteDate': ...
    @typing.overload
    def shiftedBy(self, timeOffset: TimeOffset) -> 'AbsoluteDate': ...
    def timeScalesOffset(self, scale1: TimeScale, scale2: TimeScale) -> float:
        """
        Compute the offset between two time scales at the current instant.
        
        The offset is defined as l₁-l₂ where l₁ is the location of the instant in the scale1 time scale and l₂ is the location of the instant in the scale2 time scale.
        
        Parameters:
            scale1 (TimeScale): first time scale
            scale2 (TimeScale): second time scale
        
        Returns:
            offset in seconds between the two time scales at the current instant
        
        
        """
        ...
    def toDate(self, timeScale: TimeScale) -> java.util.Date:
        """
        Convert the instance to a Java Date.
        
        Conversion to the Date class induces a loss of precision because the Date class does not provide sub-millisecond information. Java Dates are considered to be locations in some times scales.
        
        Parameters:
            timeScale (TimeScale): time scale to use
        
        Returns:
            a Date instance representing the
            location of the instant in the time scale
        
        
        """
        ...
    @typing.overload
    def toInstant(self) -> java.time.Instant:
        """
        Convert the instance to a Java Instant. Nanosecond precision is preserved during this conversion
        
        Returns:
            a Instant instance representing the
            location of the instant in the utc time scale
        
        Since:
            12.1
        
        """
        ...
    @typing.overload
    def toInstant(self, timeScales: TimeScales) -> java.time.Instant:
        """
        Convert the instance to a Java Instant. Nanosecond precision is preserved during this conversion
        
        Parameters:
            timeScales (TimeScales): the timescales to use
        
        Returns:
            a Instant instance representing the
            location of the instant in the utc time scale
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
        Get a String representation of the instant location with up to 18 digits of precision for the seconds value.
        
        Since this method is used in exception messages and error handling every effort is made to return some representation of the instant. If UTC is available from the default data context then it is used to format the string in UTC. If not then TAI is used. Finally if the prior attempts fail this method falls back to converting this class's internal representation to a string.
        
        This method uses the getDefault.
        
        Overrides: toString in class TimeOffset
        
        Returns:
            a string representation of the instance, in ISO-8601 format if UTC is available from the default data context.
        
        Also see:
            toString, toStringRfc3339,
            toString
        
        """
        ...
    @typing.overload
    def toString(self, int: int) -> str:
        """
        Get a String representation of the instant location in ISO-8601 format without the UTC offset and with up to 16 digits of precision for the seconds value.
        
        Parameters:
            timeScale (TimeScale): time scale to use
        
        Returns:
            a string representation of the instance.
        
        Also see:
            toStringRfc3339, toString
        
        Get a String representation of the instant location for a local time.
        
        This method uses the getDefault.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC).
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Since:
            7.2
        
        Also see:
            toString
        
        Get a String representation of the instant location for a local time.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC).
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Since:
            10.1
        
        Also see:
            getComponents, toString
        
        Get a String representation of the instant location for a time zone.
        
        This method uses the getDefault.
        
        Parameters:
            timeZone (TimeZone): time zone
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Since:
            7.2
        
        Also see:
            toString
        
        Get a String representation of the instant location for a time zone.
        
        Parameters:
            timeZone (TimeZone): time zone
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Since:
            10.1
        
        Also see:
            getComponents, toString
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, timeScale: TimeScale) -> str: ...
    @typing.overload
    def toString(self, timeZone: java.util.TimeZone) -> str: ...
    @typing.overload
    def toString(self, timeZone: java.util.TimeZone, timeScale: TimeScale) -> str: ...
    @typing.overload
    def toString(self, timeScale: TimeScale) -> str: ...
    def toStringRfc3339(self, utc: TimeScale) -> str:
        """
        Represent the given date as a string according to the format in RFC 3339. RFC3339 is a restricted subset of ISO 8601 with a well defined grammar. Enough digits are included in the seconds value to avoid rounding up to the next minute.
        
        This method is different than toString in that it includes a "Z" at the end to indicate the time zone and enough precision to represent the point in time without rounding up to the next minute.
        
        RFC3339 is unable to represent BC years, years of 10000 or more, time zone offsets of 100 hours or more, or NaN. In these cases the value returned from this method will not be valid RFC3339 format.
        
        Parameters:
            utc (TimeScale): time scale.
        
        Returns:
            RFC 3339 format string.
        
        Also see:
            rfc3339,
            toStringRfc3339, toString,
            getComponents
        
        
        """
        ...
    def toStringWithoutUtcOffset(self, timeScale: TimeScale, fractionDigits: int) -> str:
        """
        Return a string representation of this date-time, rounded to the given precision.
        
        The format used is ISO8601 without the UTC offset.
        
        Calling getUTC(), 3) will emulate the behavior of toString in Orekit 10 and earlier. Note this method is more accurate as it correctly handles rounding during leap seconds.
        
        Parameters:
            timeScale (TimeScale): to use to compute components.
            fractionDigits (int): the number of digits to include after the decimal point in the string representation of the seconds. The date and time
                is first rounded as necessary. fractionDigits must be greater than or equal to .
        
        Returns:
            string representation of this date, time, and UTC offset
        
        Since:
            11.1
        
        Also see:
            toString, toStringRfc3339,
            toString,
            toStringWithoutUtcOffset
        
        
        """
        ...

_AbstractFieldTimeInterpolator__T = typing.TypeVar('_AbstractFieldTimeInterpolator__T', bound=FieldTimeStamped)  # <T>
_AbstractFieldTimeInterpolator__KK = typing.TypeVar('_AbstractFieldTimeInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class AbstractFieldTimeInterpolator(FieldTimeInterpolator[_AbstractFieldTimeInterpolator__T, _AbstractFieldTimeInterpolator__KK], typing.Generic[_AbstractFieldTimeInterpolator__T, _AbstractFieldTimeInterpolator__KK]):
    """
    Abstract class for time interpolator.
    """
    DEFAULT_EXTRAPOLATION_THRESHOLD_SEC: typing.ClassVar[float] = ...
    """
    Default extrapolation time threshold: 1ms.
    
    Also see:
        constant
    
    
    """
    DEFAULT_INTERPOLATION_POINTS: typing.ClassVar[int] = ...
    """
    Default number of interpolation points.
    
    Also see:
        constant
    
    
    """
    def __init__(self, interpolationPoints: int, extrapolationThreshold: float):
        """
        Constructor.
        
        Parameters:
            interpolationPoints (int): number of interpolation points
            extrapolationThreshold (double): extrapolation threshold beyond which the propagation will fail
        
        
        """
        ...
    _checkInterpolatorCompatibilityWithSampleSize__T = typing.TypeVar('_checkInterpolatorCompatibilityWithSampleSize__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def checkInterpolatorCompatibilityWithSampleSize(interpolator: FieldTimeInterpolator[FieldTimeStamped[_checkInterpolatorCompatibilityWithSampleSize__T], _checkInterpolatorCompatibilityWithSampleSize__T], sampleSize: int) -> None:
        """
        Method checking if given interpolator is compatible with given sample size.
        
        Parameters:
            interpolator (FieldTimeInterpolator<? extends FieldTimeStamped<T>, T> interpolator): interpolator
            sampleSize (int): sample size
        
        
        """
        ...
    _getCentralDate_0__KK = typing.TypeVar('_getCentralDate_0__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
    _getCentralDate_1__T = typing.TypeVar('_getCentralDate_1__T', bound=FieldTimeStamped)  # <T>
    _getCentralDate_1__KK = typing.TypeVar('_getCentralDate_1__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
    @typing.overload
    @staticmethod
    def getCentralDate(date: 'FieldAbsoluteDate'[_getCentralDate_0__KK], minDate: 'FieldAbsoluteDate'[_getCentralDate_0__KK], maxDate: 'FieldAbsoluteDate'[_getCentralDate_0__KK], threshold: float) -> 'FieldAbsoluteDate'[_getCentralDate_0__KK]:
        """
        Get the central date to use to find neighbors while taking into account extrapolation threshold.
        
        Parameters:
            date (FieldAbsoluteDate<KK> date): interpolation date
            minDate (FieldAbsoluteDate<KK> minDate): earliest date in the sample.
            maxDate (FieldAbsoluteDate<KK> maxDate): latest date in the sample.
            threshold (double): extrapolation threshold
        
        Returns:
            central date to use to find neighbors
        
        Since:
            12.0.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getCentralDate(date: 'FieldAbsoluteDate'[_getCentralDate_1__KK], cachedSamples: org.orekit.utils.ImmutableFieldTimeStampedCache[_getCentralDate_1__T, _getCentralDate_1__KK], threshold: float) -> 'FieldAbsoluteDate'[_getCentralDate_1__KK]:
        """
        Get the central date to use to find neighbors while taking into account extrapolation threshold.
        
        Parameters:
            date (FieldAbsoluteDate<KK> date): interpolation date
            cachedSamples (ImmutableFieldTimeStampedCache<T, KK> cachedSamples): cached samples
            threshold (double): extrapolation threshold
        
        Returns:
            central date to use to find neighbors
        
        Since:
            12.0.1
        
        """
        ...
    def getExtrapolationThreshold(self) -> float:
        """
        Get the extrapolation threshold.
        
        Specified by: getExtrapolationThreshold in interface FieldTimeInterpolator
        
        Returns:
            get the extrapolation threshold.
        
        
        """
        ...
    def getInternalNbInterpolationPoints(self) -> int: ...
    def getNbInterpolationPoints(self) -> int:
        """
        Get the number of interpolation points. In the specific case where this interpolator contains multiple sub-interpolators, this method will return the maximum number of interpolation points required among all sub-interpolators.
        
        Specified by: getNbInterpolationPoints in interface FieldTimeInterpolator
        
        Returns:
            the number of interpolation points
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[FieldTimeInterpolator[FieldTimeStamped[_AbstractFieldTimeInterpolator__KK], _AbstractFieldTimeInterpolator__KK]]:
        """
        Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Specified by: getSubInterpolators in interface FieldTimeInterpolator
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, collection: typing.Union[java.util.Collection[_AbstractFieldTimeInterpolator__T], typing.Sequence[_AbstractFieldTimeInterpolator__T], typing.Set[_AbstractFieldTimeInterpolator__T]]) -> _AbstractFieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, stream: java.util.stream.Stream[_AbstractFieldTimeInterpolator__T]) -> _AbstractFieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_AbstractFieldTimeInterpolator__KK], collection: typing.Union[java.util.Collection[_AbstractFieldTimeInterpolator__T], typing.Sequence[_AbstractFieldTimeInterpolator__T], typing.Set[_AbstractFieldTimeInterpolator__T]]) -> _AbstractFieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_AbstractFieldTimeInterpolator__KK], stream: java.util.stream.Stream[_AbstractFieldTimeInterpolator__T]) -> _AbstractFieldTimeInterpolator__T: ...
    class InterpolationData:
        def getField(self) -> org.hipparchus.Field[_AbstractFieldTimeInterpolator__KK]: ...
        def getInterpolationDate(self) -> 'FieldAbsoluteDate'[_AbstractFieldTimeInterpolator__KK]: ...
        def getNeighborList(self) -> java.util.List[_AbstractFieldTimeInterpolator__T]: ...
        def getOne(self) -> _AbstractFieldTimeInterpolator__KK: ...
        def getZero(self) -> _AbstractFieldTimeInterpolator__KK: ...

_AbstractTimeInterpolator__T = typing.TypeVar('_AbstractTimeInterpolator__T', bound=TimeStamped)  # <T>
class AbstractTimeInterpolator(TimeInterpolator[_AbstractTimeInterpolator__T], typing.Generic[_AbstractTimeInterpolator__T]):
    """
    Abstract class for time interpolator.
    """
    DEFAULT_EXTRAPOLATION_THRESHOLD_SEC: typing.ClassVar[float] = ...
    """
    Default extrapolation time threshold: 1ms.
    
    Also see:
        constant
    
    
    """
    DEFAULT_INTERPOLATION_POINTS: typing.ClassVar[int] = ...
    """
    Default number of interpolation points.
    
    Also see:
        constant
    
    
    """
    def __init__(self, interpolationPoints: int, extrapolationThreshold: float):
        """
        Constructor.
        
        Parameters:
            interpolationPoints (int): number of interpolation points
            extrapolationThreshold (double): extrapolation threshold beyond which the propagation will fail
        
        
        """
        ...
    @staticmethod
    def checkInterpolatorCompatibilityWithSampleSize(interpolator: TimeInterpolator[TimeStamped], sampleSize: int) -> None:
        """
        Method checking if given interpolator is compatible with given sample size.
        
        Parameters:
            interpolator (TimeInterpolator<? extends TimeStamped> interpolator): interpolator
            sampleSize (int): sample size
        
        
        """
        ...
    _getCentralDate_1__T = typing.TypeVar('_getCentralDate_1__T', bound=TimeStamped)  # <T>
    @typing.overload
    @staticmethod
    def getCentralDate(date: AbsoluteDate, minDate: AbsoluteDate, maxDate: AbsoluteDate, threshold: float) -> AbsoluteDate:
        """
        Get the central date to use to find neighbors while taking into account extrapolation threshold.
        
        Parameters:
            date (AbsoluteDate): interpolation date
            minDate (AbsoluteDate): earliest date in the sample.
            maxDate (AbsoluteDate): latest date in the sample.
            threshold (double): extrapolation threshold
        
        Returns:
            central date to use to find neighbors
        
        Since:
            12.0.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getCentralDate(date: AbsoluteDate, cachedSamples: org.orekit.utils.ImmutableTimeStampedCache[_getCentralDate_1__T], threshold: float) -> AbsoluteDate:
        """
        Get the central date to use to find neighbors while taking into account extrapolation threshold.
        
        Parameters:
            date (AbsoluteDate): interpolation date
            cachedSamples (ImmutableTimeStampedCache<T> cachedSamples): cached samples
            threshold (double): extrapolation threshold
        
        Returns:
            central date to use to find neighbors
        
        Since:
            12.0.1
        
        """
        ...
    def getExtrapolationThreshold(self) -> float:
        """
        Get the extrapolation threshold.
        
        Specified by: getExtrapolationThreshold in interface TimeInterpolator
        
        Returns:
            get the extrapolation threshold
        
        
        """
        ...
    def getInternalNbInterpolationPoints(self) -> int: ...
    def getNbInterpolationPoints(self) -> int:
        """
        Get the number of interpolation points. In the specific case where this interpolator contains multiple sub-interpolators, this method will return the maximum number of interpolation points required among all sub-interpolators.
        
        Specified by: getNbInterpolationPoints in interface TimeInterpolator
        
        Returns:
            the number of interpolation points
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[TimeInterpolator[TimeStamped]]:
        """
        Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Specified by: getSubInterpolators in interface TimeInterpolator
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, collection: typing.Union[java.util.Collection[_AbstractTimeInterpolator__T], typing.Sequence[_AbstractTimeInterpolator__T], typing.Set[_AbstractTimeInterpolator__T]]) -> _AbstractTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, stream: java.util.stream.Stream[_AbstractTimeInterpolator__T]) -> _AbstractTimeInterpolator__T: ...
    class InterpolationData:
        def getInterpolationDate(self) -> AbsoluteDate: ...
        def getNeighborList(self) -> java.util.List[_AbstractTimeInterpolator__T]: ...

class AbstractTimeScales(TimeScales):
    """
    Abstract base class for TimeScales that implements some common functionality.
    
    Since:
        10.1
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def createBesselianEpoch(self, besselianEpoch: float) -> AbsoluteDate:
        """
        Description copied from interface: createBesselianEpoch Build an instance corresponding to a Besselian Epoch (BE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date as:
        
         BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
        
        This method reverts the formula above and computes an AbsoluteDate from the Besselian Epoch.
        
        Specified by: createBesselianEpoch in interface TimeScales
        
        Parameters:
            besselianEpoch (double): Besselian epoch, like 1950 for defining the classical reference B1950.0
        
        Returns:
            a new instant
        
        Also see:
            createJulianEpoch
        
        
        """
        ...
    def createJulianEpoch(self, julianEpoch: float) -> AbsoluteDate:
        """
        Description copied from interface: createJulianEpoch Build an instance corresponding to a Julian Epoch (JE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
        
         JE = 2000.0 + (JED - 2451545.0) / 365.25
        
        This method reverts the formula above and computes an AbsoluteDate from the Julian Epoch.
        
        Specified by: createJulianEpoch in interface TimeScales
        
        Parameters:
            julianEpoch (double): Julian epoch, like 2000.0 for defining the classical reference J2000.0
        
        Returns:
            a new instant
        
        Also see:
            getJ2000Epoch, createBesselianEpoch
        
        
        """
        ...
    def getBeidouEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getBeidouEpoch Reference epoch for BeiDou weeks: 2006-01-01T00:00:00 UTC.
        
        Specified by: getBeidouEpoch in interface TimeScales
        
        Returns:
            Beidou Epoch
        
        
        """
        ...
    def getCcsdsEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getCcsdsEpoch Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (not UTC).
        
        Specified by: getCcsdsEpoch in interface TimeScales
        
        Returns:
            CCSDS Epoch
        
        
        """
        ...
    def getFiftiesEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getFiftiesEpoch Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
        
        Specified by: getFiftiesEpoch in interface TimeScales
        
        Returns:
            Fifties Epoch
        
        
        """
        ...
    def getFutureInfinity(self) -> AbsoluteDate:
        """
        Description copied from interface: getFutureInfinity Dummy date at infinity in the future direction.
        
        Specified by: getFutureInfinity in interface TimeScales
        
        Returns:
            the latest date.
        
        
        """
        ...
    def getGMST(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> 'GMSTScale':
        """
        Description copied from interface: getGMST Get the Greenwich Mean Sidereal Time scale.
        
        Specified by: getGMST in interface TimeScales
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Greenwich Mean Sidereal Time scale
        
        
        """
        ...
    def getGalileoEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getGalileoEpoch Reference epoch for Galileo System Time: 1999-08-22T00:00:00 GST.
        
        Specified by: getGalileoEpoch in interface TimeScales
        
        Returns:
            Galileo Epoch
        
        
        """
        ...
    def getGlonassEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getGlonassEpoch Reference epoch for GLONASS four-year interval number: 1996-01-01T00:00:00 GLONASS time.
        
        By convention, TGLONASS = UTC + 3 hours.
        
        Specified by: getGlonassEpoch in interface TimeScales
        
        Returns:
            GLONASS Epoch
        
        
        """
        ...
    def getGpsEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getGpsEpoch Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
        
        Specified by: getGpsEpoch in interface TimeScales
        
        Returns:
            GPS Epoch
        
        
        """
        ...
    def getJ2000Epoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getJ2000Epoch J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (not UTC).
        
        Specified by: getJ2000Epoch in interface TimeScales
        
        Returns:
            J2000 Epoch
        
        Also see:
            createJulianEpoch, createBesselianEpoch
        
        
        """
        ...
    def getJavaEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getJavaEpoch Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
        
        Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587, UTC-TAI = 8.000082s
        
        Specified by: getJavaEpoch in interface TimeScales
        
        Returns:
            Java Epoch
        
        
        """
        ...
    def getJulianEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getJulianEpoch Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
        
        Both Date and DateComponents classes follow the astronomical conventions and consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be seen in other documents or programs that obey a different convention (for example the convcal utility).
        
        Specified by: getJulianEpoch in interface TimeScales
        
        Returns:
            Julian epoch.
        
        
        """
        ...
    def getModifiedJulianEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getModifiedJulianEpoch Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
        
        Specified by: getModifiedJulianEpoch in interface TimeScales
        
        Returns:
            Modified Julian Epoch
        
        
        """
        ...
    def getNavicEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getNavicEpoch Reference epoch for NavIC weeks: 1999-08-22T00:00:00 NavIC time.
        
        Specified by: getNavicEpoch in interface TimeScales
        
        Returns:
            NavIC Epoch
        
        
        """
        ...
    def getPastInfinity(self) -> AbsoluteDate:
        """
        Description copied from interface: getPastInfinity Dummy date at infinity in the past direction.
        
        Specified by: getPastInfinity in interface TimeScales
        
        Returns:
            the earliest date.
        
        
        """
        ...
    def getQzssEpoch(self) -> AbsoluteDate:
        """
        Description copied from interface: getQzssEpoch Reference epoch for QZSS weeks: 1980-01-06T00:00:00 QZSS time.
        
        Specified by: getQzssEpoch in interface TimeScales
        
        Returns:
            QZSS Epoch
        
        
        """
        ...
    def getUT1(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'UT1Scale':
        """
        Get the Universal Time 1 scale.
        
        As this method allow associating any history with the time scale, it may involve large data sets. So this method does not cache the resulting UT1Scale instance, a new instance will be returned each time. In order to avoid wasting memory, calling getUT1 with the single enumerate corresponding to the conventions may be a better solution. This method is made available only for expert use.
        
        Parameters:
            history (EOPHistory): EOP parameters providing dUT1 (may be null if no correction is desired)
        
        Returns:
            Universal Time 1 scale
        
        Also see:
            getUT1
        
        public UT1Scale getUT1 (IERSConventions conventions, boolean simpleEOP)
        
        Description copied from interface: getUT1 Get the Universal Time 1 scale.
        
        Specified by: getUT1 in interface TimeScales
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Universal Time 1 scale
        
        Also see:
            getUTC, getEOPHistory
        
        
        """
        ...

class AggregatedClockModel(ClockModel):
    """
    Offset clock model aggregating several other clock models.
    
    Since:
        12.1
    """
    def __init__(self, models: org.orekit.utils.TimeSpanMap[ClockModel]):
        """
        Simple constructor.
        
        Parameters:
            models (TimeSpanMap<ClockModel> models): underlying clock models
        
        
        """
        ...
    def getModels(self) -> org.orekit.utils.TimeSpanMap[ClockModel]:
        """
        Get the underlying models.
        
        Returns:
            underlying models
        
        
        """
        ...
    _getOffset_1__T = typing.TypeVar('_getOffset_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, date: AbsoluteDate) -> 'ClockOffset':
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (AbsoluteDate): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        """
        ...
    @typing.overload
    def getOffset(self, date: 'FieldAbsoluteDate'[_getOffset_1__T]) -> 'FieldClockOffset'[_getOffset_1__T]:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        
        """
        ...
    def getValidityEnd(self) -> AbsoluteDate:
        """
        Get validity end.
        
        Specified by: getValidityEnd in interface ClockModel
        
        Returns:
            model validity end
        
        
        """
        ...
    def getValidityStart(self) -> AbsoluteDate:
        """
        Get validity start.
        
        Specified by: getValidityStart in interface ClockModel
        
        Returns:
            model validity start
        
        
        """
        ...

class BurstSelector(DatesSelector):
    """
    Selector generating high rate bursts of dates separated by some rest period.
    
    The dates can be aligned to whole steps in some time scale. So for example if a rest period of 3600s is used and the alignment time scale is set to getUTC, the earliest date of each burst will occur at whole hours in UTC time.
    
    BEWARE! This class stores internally the last selected dates, so it is neither reusable across several EventBasedScheduler or ContinuousScheduler schedulers, nor thread-safe. A separate selector should be used for each scheduler and for each thread in multi-threading context.
    
    Since:
        9.3
    """
    def __init__(self, maxBurstSize: int, highRateStep: float, burstPeriod: float, alignmentTimeScale: TimeScale):
        """
        Simple constructor.
        
        The burstPeriod ignores the duration of the burst itself. This means that if burst of maxBurstSize=256 dates each separated by highRateStep=100ms should be selected with burstPeriod=300s, then the first burst would contain 256 dates from t0 to 5s and the second burst would start at t0+300s, not at 5s.
        
        If alignment to some time scale is needed, it applies only to the first date in each burst.
        
        Parameters:
            maxBurstSize (int): maximum number of selected dates in a burst
            highRateStep (double): step between two consecutive dates within a burst (s)
            burstPeriod (double): period between the start of each burst (s)
            alignmentTimeScale (TimeScale): alignment time scale for first date in burst (null is alignment is not needed)
        
        
        """
        ...
    def selectDates(self, start: AbsoluteDate, end: AbsoluteDate) -> java.util.List[AbsoluteDate]:
        """
        Select dates within an interval.
        
        The start and end date may be either in direct or reverse chronological order. The list is produced in the same order as start and end, i.e. direct chronological order if start is earlier than end or reverse chronological order if start is later than end.
        
        The ordering (direct or reverse chronological order) should not be changed between calls, otherwise unpredictable results may occur.
        
        Specified by: selectDates in interface DatesSelector
        
        Parameters:
            start (AbsoluteDate): interval start
            end (AbsoluteDate): interval end
        
        Returns:
            selected dates within this interval
        
        
        """
        ...

class ClockOffset(TimeStamped):
    """
    Container for time stamped clock offset.
    
    Since:
        12.1
    """
    def __init__(self, date: AbsoluteDate, offset: float, rate: float, acceleration: float):
        """
        Simple constructor.
        
        Parameters:
            date (AbsoluteDate): date
            offset (double): clock offset
            rate (double): clock rate (can be set to NaN if unknown)
            acceleration (double): clock acceleration (can be set to NaN if unknown)
        
        
        """
        ...
    def getAcceleration(self) -> float:
        """
        Get acceleration.
        
        Returns:
            acceleration (NaN if unknown)
        
        
        """
        ...
    def getDate(self) -> AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getOffset(self) -> float:
        """
        Get offset.
        
        Returns:
            offset
        
        
        """
        ...
    def getRate(self) -> float:
        """
        Get rate.
        
        Returns:
            rate (NaN if unknown)
        
        
        """
        ...

class ClockTimeScale(TimeScale):
    """
    Time scale with clock offset from another time scale.
    
    Since:
        12.1
    """
    def __init__(self, name: str, reference: TimeScale, clockModel: ClockModel):
        """
        Simple constructor.
        
        Parameters:
            name (String): name of the time scale
            reference (TimeScale): reference time scale
            clockModel (ClockModel): clock offset model
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...

class ConstantOffsetTimeScale(TimeScale):
    """
    Base class for time scales with constant offset with respect to to TAI.
    
    Since:
        12.1
    """
    def __init__(self, name: str, offset: TimeOffset):
        """
        Simple constructor.
        
        Parameters:
            name (String): name of the time scale
            offset (TimeOffset): offset from TAI
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def offsetToTAI(self, date: DateComponents, time: TimeComponents) -> TimeOffset:
        """
        Get the offset to convert locations from instance to TAIScale.
        
        Specified by: offsetToTAI in interface TimeScale
        
        Parameters:
            date (DateComponents): date location in the time scale
            time (TimeComponents): time location in the time scale
        
        Returns:
            offset in seconds to add to a location in instance time scale to get a location in TAIScale
            time scale
        
        Also see:
            offsetFromTAI
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

_FieldClockOffset__T = typing.TypeVar('_FieldClockOffset__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldClockOffset(FieldTimeStamped[_FieldClockOffset__T], typing.Generic[_FieldClockOffset__T]):
    """
    Container for time stamped clock offset.
    
    Since:
        12.1
    """
    def __init__(self, date: 'FieldAbsoluteDate'[_FieldClockOffset__T], offset: _FieldClockOffset__T, rate: _FieldClockOffset__T, acceleration: _FieldClockOffset__T):
        """
        Simple constructor.
        
        Parameters:
            date (FieldAbsoluteDate<FieldClockOffset> date): date
            offset (FieldClockOffset): clock offset
            rate (FieldClockOffset): clock rate (can be set to null if unknown)
            acceleration (FieldClockOffset): clock acceleration (can be set to null if unknown)
        
        
        """
        ...
    def getAcceleration(self) -> _FieldClockOffset__T:
        """
        Get acceleration.
        
        Returns:
            acceleration (null if unknown)
        
        
        """
        ...
    def getDate(self) -> 'FieldAbsoluteDate'[_FieldClockOffset__T]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getOffset(self) -> _FieldClockOffset__T:
        """
        Get offset.
        
        Returns:
            offset
        
        
        """
        ...
    def getRate(self) -> _FieldClockOffset__T:
        """
        Get rate.
        
        Returns:
            rate (null if unknown)
        
        
        """
        ...

_FieldTimeShiftable__T = typing.TypeVar('_FieldTimeShiftable__T', bound='FieldTimeShiftable')  # <T>
_FieldTimeShiftable__KK = typing.TypeVar('_FieldTimeShiftable__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldTimeShiftable(TimeShiftable[_FieldTimeShiftable__T], typing.Generic[_FieldTimeShiftable__T, _FieldTimeShiftable__KK]):
    """
    This interface represents objects that can be shifted in time.
    
    Since:
        9.0
    """
    @typing.overload
    def shiftedBy(self, dt: _FieldTimeShiftable__KK) -> _FieldTimeShiftable__T:
        """
        Get a time-shifted instance.
        
        Parameters:
            dt (FieldTimeShiftable): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> _FieldTimeShiftable__T: ...
    @typing.overload
    def shiftedBy(self, timeOffset: TimeOffset) -> _FieldTimeShiftable__T: ...

_FieldTimeStampedPair__F = typing.TypeVar('_FieldTimeStampedPair__F', bound=FieldTimeStamped)  # <F>
_FieldTimeStampedPair__S = typing.TypeVar('_FieldTimeStampedPair__S', bound=FieldTimeStamped)  # <S>
_FieldTimeStampedPair__KK = typing.TypeVar('_FieldTimeStampedPair__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldTimeStampedPair(FieldTimeStamped[_FieldTimeStampedPair__KK], typing.Generic[_FieldTimeStampedPair__F, _FieldTimeStampedPair__S, _FieldTimeStampedPair__KK]):
    """
    Pair of time stamped values being defined at the same date.
    
    Also see:
        FieldTimeStamped
    """
    DEFAULT_DATE_EQUALITY_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default date equality threshold of 1 ns.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, f: _FieldTimeStampedPair__F, s2: _FieldTimeStampedPair__S): ...
    @typing.overload
    def __init__(self, f: _FieldTimeStampedPair__F, s2: _FieldTimeStampedPair__S, double: float): ...
    def getDate(self) -> 'FieldAbsoluteDate'[_FieldTimeStampedPair__KK]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFirst(self) -> _FieldTimeStampedPair__F:
        """
        Get first time stamped value.
        
        Returns:
            first time stamped value
        
        
        """
        ...
    def getSecond(self) -> _FieldTimeStampedPair__S:
        """
        Get second time stamped value.
        
        Returns:
            second time stamped value
        
        
        """
        ...

class FixedStepSelector(DatesSelector):
    """
    Selector generating a continuous stream of dates separated by a constant step.
    
    The dates can be aligned to whole steps in some time scale. So for example if a step of 60s is used and the alignment time scale is set to getUTC, dates will be selected at whole minutes in UTC time.
    
    BEWARE! This class stores internally the last selected dates, so it is neither reusable across several EventBasedScheduler or ContinuousScheduler schedulers, nor thread-safe. A separate selector should be used for each scheduler and for each thread in multi-threading context.
    
    Since:
        9.3
    """
    def __init__(self, step: float, alignmentTimeScale: TimeScale):
        """
        Simple constructor.
        
        Parameters:
            step (double): step between two consecutive dates (s)
            alignmentTimeScale (TimeScale): alignment time scale (null is alignment is not needed)
        
        
        """
        ...
    def selectDates(self, start: AbsoluteDate, end: AbsoluteDate) -> java.util.List[AbsoluteDate]:
        """
        Select dates within an interval.
        
        The start and end date may be either in direct or reverse chronological order. The list is produced in the same order as start and end, i.e. direct chronological order if start is earlier than end or reverse chronological order if start is later than end.
        
        The ordering (direct or reverse chronological order) should not be changed between calls, otherwise unpredictable results may occur.
        
        Specified by: selectDates in interface DatesSelector
        
        Parameters:
            start (AbsoluteDate): interval start
            end (AbsoluteDate): interval end
        
        Returns:
            selected dates within this interval
        
        
        """
        ...

class GLONASSDate(TimeStamped):
    """
    Container for date in GLONASS form.
    
    Since:
        10.0
    
    Also see:
        AbsoluteDate, "GLONASS Interface Control Document v1.0, 2016"
    """
    @typing.overload
    def __init__(self, int: int, int2: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, timeScale: TimeScale): ...
    def getDate(self) -> AbsoluteDate:
        """
        Description copied from interface: getDate Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getDayNumber(self) -> int:
        """
        Get the number of the current day in a four year interval.
        
        Returns:
            the number of the current day in a four year interval
        
        
        """
        ...
    def getGMST(self) -> float:
        """
        Get the Greenwich Mean Sidereal Time.
        
        Returns:
            the Greenwich Mean Sidereal Time (rad)
        
        
        """
        ...
    def getIntervalNumber(self) -> int:
        """
        Get the number of the current four year interval.
        
        Returns:
            the number of the current four year interval
        
        
        """
        ...
    def getJD0(self) -> float:
        """
        Get the current Julian date JD0.
        
        Returns:
            the current date JD0
        
        
        """
        ...
    def getSecInDay(self) -> float:
        """
        Get the number of seconds since N :sub:`a` start.
        
        Returns:
            number of seconds since N :sub:`a` start
        
        
        """
        ...

class GLONASSScale(TimeScale):
    """
    GLONASS time scale.
    
    By convention, TGLONASS = UTC + 3 hours.
    
    The time scale is defined in ` Global Navigation Sattelite System GLONASS - Interface Control document <http://www.spacecorp.ru/upload/iblock/1c4/cgs-aaixymyt%205.1%20ENG%20v%202014.02.18w.pdf>`, version 5.1 2008 (the typo in the title is in the original document title).
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    _getLeap_0__T = typing.TypeVar('_getLeap_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLeap(self, date: 'FieldAbsoluteDate'[_getLeap_0__T]) -> _getLeap_0__T:
        """
        Get the value of the previous leap.
        
        This method will return 0.0 for all time scales that do not implement leap seconds.
        
        Specified by: getLeap in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            value of the previous leap
        
        
        """
        ...
    @typing.overload
    def getLeap(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the value of the previous leap.
        
        This method will return 0 for all time scales that do not implement leap seconds.
        
        Specified by: getLeap in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            value of the previous leap
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _insideLeap_1__T = typing.TypeVar('_insideLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def insideLeap(self, date: AbsoluteDate) -> bool:
        """
        Check if date is within a leap second introduction in this time scale.
        
        This method will return false for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale.
        
        Specified by: insideLeap in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            true if time is within a leap second introduction
        
        """
        ...
    @typing.overload
    def insideLeap(self, date: 'FieldAbsoluteDate'[_insideLeap_1__T]) -> bool:
        """
        Check if date is within a leap second introduction in this time scale.
        
        This method will return false for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale.
        
        Specified by: insideLeap in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            true if time is within a leap second introduction
        
        
        """
        ...
    _minuteDuration_1__T = typing.TypeVar('_minuteDuration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def minuteDuration(self, date: AbsoluteDate) -> int:
        """
        Check length of the current minute in this time scale.
        
        This method will return 60 for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale, and 61 for time scales that do implement leap second when the current date is within the last minute before the leap, or during the leap itself.
        
        Specified by: minuteDuration in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            60 or 61 depending on leap seconds introduction
        
        """
        ...
    @typing.overload
    def minuteDuration(self, date: 'FieldAbsoluteDate'[_minuteDuration_1__T]) -> int:
        """
        Check length of the current minute in this time scale.
        
        This method will return 60 for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale, and 61 for time scales that do implement leap second when the current date is within the last minute before the leap, or during the leap itself.
        
        Specified by: minuteDuration in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            60 or 61 depending on leap seconds introduction
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def offsetToTAI(self, date: DateComponents, time: TimeComponents) -> TimeOffset:
        """
        Get the offset to convert locations from instance to TAIScale.
        
        Specified by: offsetToTAI in interface TimeScale
        
        Parameters:
            date (DateComponents): date location in the time scale
            time (TimeComponents): time location in the time scale
        
        Returns:
            offset in seconds to add to a location in instance time scale to get a location in TAIScale
            time scale
        
        Also see:
            offsetFromTAI
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class GMSTScale(TimeScale):
    """
    Greenwich Mean Sidereal Time.
    
    The Greenwich Mean Sidereal Time is the hour angle between the meridian of Greenwich and mean equinox of date at 0h UT1.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Since:
        5.1
    
    Also see:
        AbsoluteDate
    """
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class GNSSDate(java.io.Serializable, TimeStamped):
    """
    Container for date in GNSS form.
    
    This class can be used to handle GPS, GALILEO, BEIDOU and QZSS dates.
    
    Also see:
        AbsoluteDate, serialized
    """
    @typing.overload
    def __init__(self, int: int, double: float, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, int: int, double: float, satelliteSystem: org.orekit.gnss.SatelliteSystem, dateComponents: DateComponents, timeScales: TimeScales): ...
    @typing.overload
    def __init__(self, int: int, double: float, satelliteSystem: org.orekit.gnss.SatelliteSystem, timeScales: TimeScales): ...
    @typing.overload
    def __init__(self, int: int, timeOffset: TimeOffset, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, int: int, timeOffset: TimeOffset, satelliteSystem: org.orekit.gnss.SatelliteSystem, dateComponents: DateComponents, timeScales: TimeScales): ...
    @typing.overload
    def __init__(self, int: int, timeOffset: TimeOffset, satelliteSystem: org.orekit.gnss.SatelliteSystem, timeScales: TimeScales): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, satelliteSystem: org.orekit.gnss.SatelliteSystem, timeScales: TimeScales): ...
    def getDate(self) -> AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getMilliInWeek(self) -> float:
        """
        Get the number of milliseconds since week start.
        
        Returns:
            number of milliseconds since week start
        
        
        """
        ...
    @staticmethod
    def getRolloverReference() -> DateComponents:
        """
        Get the reference date ensuring continuity across GNSS week rollover.
        
        Returns:
            reference reference date for GNSS week rollover
        
        Since:
            9.3.1
        
        Also see:
            setRolloverReference, 
        
        
        """
        ...
    def getSecondsInWeek(self) -> float:
        """
        Get the number of seconds since week start.
        
        Returns:
            number of seconds since week start
        
        Since:
            12.0
        
        
        """
        ...
    def getSplitSecondsInWeek(self) -> TimeOffset:
        """
        Get the number of seconds since week start.
        
        Returns:
            number of seconds since week start
        
        Since:
            13.0
        
        
        """
        ...
    def getWeekNumber(self) -> int:
        """
        Get the week number since the GNSS reference epoch.
        
        The week number returned here has been fixed for GNSS week rollover, i.e. it may be larger than the corresponding week cycle of the constellation.
        
        Returns:
            week number since the GNSS reference epoch
        
        
        """
        ...
    @staticmethod
    def setRolloverReference(reference: DateComponents) -> None:
        """
        Set a reference date for ensuring continuity across GNSS week rollover.
        
        Instance created using the  constructor and with a week number between 0 and the constellation week cycle (cycleW) after this method has been called will fix the week number to ensure they correspond to dates between reference - cycleW / 2 weeks and reference + cycleW / 2 weeks.
        
        If this method is never called, a default reference date for rollover will be set using the date of the last known EOP entry retrieved from getEOPHistory time scale.
        
        Parameters:
            reference (DateComponents): reference date for GNSS week rollover
        
        Since:
            9.3.1
        
        Also see:
            getRolloverReference, 
        
        
        """
        ...
    class GNSSDateType(java.lang.Enum['GNSSDate.GNSSDateType']):
        GPS: typing.ClassVar['GNSSDate.GNSSDateType'] = ...
        GALILEO: typing.ClassVar['GNSSDate.GNSSDateType'] = ...
        QZSS: typing.ClassVar['GNSSDate.GNSSDateType'] = ...
        BEIDOU: typing.ClassVar['GNSSDate.GNSSDateType'] = ...
        NAVIC: typing.ClassVar['GNSSDate.GNSSDateType'] = ...
        SBAS: typing.ClassVar['GNSSDate.GNSSDateType'] = ...
        def getRollOverCycle(self) -> int: ...
        @staticmethod
        def getRollOverWeek(satelliteSystem: org.orekit.gnss.SatelliteSystem) -> int: ...
        def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'GNSSDate.GNSSDateType': ...
        @staticmethod
        def values() -> typing.MutableSequence['GNSSDate.GNSSDateType']: ...

class PerfectClockModel(ClockModel):
    """
    Clock model for perfect clock with constant zero offset.
    
    Since:
        12.1
    """
    def __init__(self): ...
    _getOffset_1__T = typing.TypeVar('_getOffset_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, date: AbsoluteDate) -> ClockOffset:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (AbsoluteDate): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        """
        ...
    @typing.overload
    def getOffset(self, date: 'FieldAbsoluteDate'[_getOffset_1__T]) -> FieldClockOffset[_getOffset_1__T]:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        
        """
        ...
    def getValidityEnd(self) -> AbsoluteDate:
        """
        Get validity end.
        
        Specified by: getValidityEnd in interface ClockModel
        
        Returns:
            model validity end
        
        
        """
        ...
    def getValidityStart(self) -> AbsoluteDate:
        """
        Get validity start.
        
        Specified by: getValidityStart in interface ClockModel
        
        Returns:
            model validity start
        
        
        """
        ...

class PythonClockModel(ClockModel):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getOffset_1__T = typing.TypeVar('_getOffset_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, date: AbsoluteDate) -> ClockOffset:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (AbsoluteDate): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        """
        ...
    @typing.overload
    def getOffset(self, date: 'FieldAbsoluteDate'[_getOffset_1__T]) -> FieldClockOffset[_getOffset_1__T]:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        
        """
        ...
    def getValidityEnd(self) -> AbsoluteDate:
        """
        Get validity end.
        
        Specified by: getValidityEnd in interface ClockModel
        
        Returns:
            model validity end
        
        
        """
        ...
    def getValidityStart(self) -> AbsoluteDate:
        """
        Get validity start.
        
        Specified by: getValidityStart in interface ClockModel
        
        Returns:
            model validity start
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonDatesSelector(DatesSelector):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def selectDates(self, start: AbsoluteDate, end: AbsoluteDate) -> java.util.List[AbsoluteDate]:
        """
        Select dates within an interval. Extension point for Python.
        
        The start and end date may be either in direct or reverse chronological order. The list is produced in the same order as start and end, i.e. direct chronological order if start is earlier than end or reverse chronological order if start is later than end.
        
        The ordering (direct or reverse chronological order) should not be changed between calls, otherwise unpredictable results may occur.
        
        Specified by: selectDates in interface DatesSelector
        
        Parameters:
            start (AbsoluteDate): interval start
            end (AbsoluteDate): interval end
        
        Returns:
            selected dates within this interval
        
        
        """
        ...

_PythonFieldTimeInterpolator__T = typing.TypeVar('_PythonFieldTimeInterpolator__T', bound=FieldTimeInterpolator)  # <T>
_PythonFieldTimeInterpolator__KK = typing.TypeVar('_PythonFieldTimeInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class PythonFieldTimeInterpolator(FieldTimeInterpolator[_PythonFieldTimeInterpolator__T, _PythonFieldTimeInterpolator__KK], typing.Generic[_PythonFieldTimeInterpolator__T, _PythonFieldTimeInterpolator__KK]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getExtrapolationThreshold(self) -> float:
        """
        Description copied from interface: getExtrapolationThreshold Get the extrapolation threshold.
        
        Specified by: getExtrapolationThreshold in interface FieldTimeInterpolator
        
        Returns:
            get the extrapolation threshold.
        
        
        """
        ...
    def getNbInterpolationPoints(self) -> int:
        """
        Description copied from interface: getNbInterpolationPoints Get the number of interpolation points. In the specific case where this interpolator contains multiple sub-interpolators, this method will return the maximum number of interpolation points required among all sub-interpolators.
        
        Specified by: getNbInterpolationPoints in interface FieldTimeInterpolator
        
        Returns:
            the number of interpolation points
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[FieldTimeInterpolator[FieldTimeStamped[_PythonFieldTimeInterpolator__KK], _PythonFieldTimeInterpolator__KK]]:
        """
        Description copied from interface: getSubInterpolators Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Specified by: getSubInterpolators in interface FieldTimeInterpolator
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, collection: typing.Union[java.util.Collection[_PythonFieldTimeInterpolator__T], typing.Sequence[_PythonFieldTimeInterpolator__T], typing.Set[_PythonFieldTimeInterpolator__T]]) -> _PythonFieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, stream: java.util.stream.Stream[_PythonFieldTimeInterpolator__T]) -> _PythonFieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_PythonFieldTimeInterpolator__KK], collection: typing.Union[java.util.Collection[_PythonFieldTimeInterpolator__T], typing.Sequence[_PythonFieldTimeInterpolator__T], typing.Set[_PythonFieldTimeInterpolator__T]]) -> _PythonFieldTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_PythonFieldTimeInterpolator__KK], stream: java.util.stream.Stream[_PythonFieldTimeInterpolator__T]) -> _PythonFieldTimeInterpolator__T: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldTimeStamped__T = typing.TypeVar('_PythonFieldTimeStamped__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldTimeStamped(FieldTimeStamped[_PythonFieldTimeStamped__T], typing.Generic[_PythonFieldTimeStamped__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDate(self) -> 'FieldAbsoluteDate'[_PythonFieldTimeStamped__T]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonParser(UTCTAIOffsetsLoader.Parser):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def parse(self, input: java.io.InputStream, name: str) -> java.util.List[OffsetModel]:
        """
        Parse leap seconds from the input stream.
        
        Specified by: parse in interface Parser
        
        Parameters:
            input (InputStream): stream to parse.
            name (String): of the input stream to use in error messages.
        
        Returns:
            parsed UTC-TAI offsets.
        
        Raises:
            IOException: if input throws one during parsing.
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

_PythonTimeInterpolator__T = typing.TypeVar('_PythonTimeInterpolator__T', bound=TimeInterpolator)  # <T>
class PythonTimeInterpolator(TimeInterpolator[_PythonTimeInterpolator__T], typing.Generic[_PythonTimeInterpolator__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getExtrapolationThreshold(self) -> float:
        """
        Get the extrapolation threshold.
        
        Specified by: getExtrapolationThreshold in interface TimeInterpolator
        
        Returns:
            get the extrapolation threshold
        
        
        """
        ...
    def getNbInterpolationPoints(self) -> int:
        """
        Get the number of interpolation points. In the specific case where this interpolator contains multiple sub-interpolators, this method will return the maximum number of interpolation points required among all sub-interpolators.
        
        Specified by: getNbInterpolationPoints in interface TimeInterpolator
        
        Returns:
            the number of interpolation points
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[TimeInterpolator[TimeStamped]]:
        """
        Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Specified by: getSubInterpolators in interface TimeInterpolator
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, collection: typing.Union[java.util.Collection[_PythonTimeInterpolator__T], typing.Sequence[_PythonTimeInterpolator__T], typing.Set[_PythonTimeInterpolator__T]]) -> _PythonTimeInterpolator__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, stream: java.util.stream.Stream[_PythonTimeInterpolator__T]) -> _PythonTimeInterpolator__T: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonTimeInterval(TimeInterval):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEndDate(self) -> AbsoluteDate:
        """
        Description copied from interface: getEndDate Getter for the right end of the interval.
        
        Specified by: getEndDate in interface TimeInterval
        
        Returns:
            right end
        
        
        """
        ...
    def getStartDate(self) -> AbsoluteDate:
        """
        Description copied from interface: getStartDate Getter for the left end of the interval.
        
        Specified by: getStartDate in interface TimeInterval
        
        Returns:
            left end
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonTimeScalarFunction(TimeScalarFunction):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, date: AbsoluteDate) -> float:
        """
        Compute a function of time.
        
        Specified by: value in interface TimeScalarFunction
        
        Parameters:
            date (AbsoluteDate): date
        
        Returns:
            value of the function
        
        """
        ...
    @typing.overload
    def value(self, date: 'FieldAbsoluteDate'[_value_1__T]) -> _value_1__T:
        """
        Compute a function of time.
        
        Specified by: value in interface TimeScalarFunction
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
        
        Returns:
            value of the function
        
        
        """
        ...

class PythonTimeScale(TimeScale):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonTimeScales(TimeScales):
    def __init__(self): ...
    def createBesselianEpoch(self, besselianEpoch: float) -> AbsoluteDate:
        """
        Build an instance corresponding to a Besselian Epoch (BE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date as:
        
         BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
        
        This method reverts the formula above and computes an AbsoluteDate from the Besselian Epoch.
        
        Specified by: createBesselianEpoch in interface TimeScales
        
        Parameters:
            besselianEpoch (double): Besselian epoch, like 1950 for defining the classical reference B1950.0
        
        Returns:
            a new instant
        
        Also see:
            createJulianEpoch
        
        
        """
        ...
    def createJulianEpoch(self, julianEpoch: float) -> AbsoluteDate:
        """
        Build an instance corresponding to a Julian Epoch (JE).
        
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
        
         JE = 2000.0 + (JED - 2451545.0) / 365.25
        
        This method reverts the formula above and computes an AbsoluteDate from the Julian Epoch.
        
        Specified by: createJulianEpoch in interface TimeScales
        
        Parameters:
            julianEpoch (double): Julian epoch, like 2000.0 for defining the classical reference J2000.0
        
        Returns:
            a new instant
        
        Also see:
            getJ2000Epoch, createBesselianEpoch
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBDT(self) -> 'BDTScale':
        """
        Get the BeiDou Navigation Satellite System time scale.
        
        Specified by: getBDT in interface TimeScales
        
        Returns:
            BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    def getBeidouEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for BeiDou weeks: 2006-01-01T00:00:00 UTC.
        
        Specified by: getBeidouEpoch in interface TimeScales
        
        Returns:
            Beidou Epoch
        
        
        """
        ...
    def getCcsdsEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (not UTC).
        
        Specified by: getCcsdsEpoch in interface TimeScales
        
        Returns:
            CCSDS Epoch
        
        
        """
        ...
    def getFiftiesEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
        
        Specified by: getFiftiesEpoch in interface TimeScales
        
        Returns:
            Fifties Epoch
        
        
        """
        ...
    def getFutureInfinity(self) -> AbsoluteDate:
        """
        Dummy date at infinity in the future direction.
        
        Specified by: getFutureInfinity in interface TimeScales
        
        Returns:
            the latest date.
        
        
        """
        ...
    def getGLONASS(self) -> GLONASSScale:
        """
        Get the GLObal NAvigation Satellite System time scale.
        
        Specified by: getGLONASS in interface TimeScales
        
        Returns:
            GLObal NAvigation Satellite System time scale
        
        
        """
        ...
    def getGMST(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> GMSTScale:
        """
        Get the Greenwich Mean Sidereal Time scale.
        
        Specified by: getGMST in interface TimeScales
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Greenwich Mean Sidereal Time scale
        
        
        """
        ...
    def getGPS(self) -> 'GPSScale':
        """
        Get the Global Positioning System scale.
        
        Specified by: getGPS in interface TimeScales
        
        Returns:
            Global Positioning System scale
        
        
        """
        ...
    def getGST(self) -> 'GalileoScale':
        """
        Get the Galileo System Time scale.
        
        Specified by: getGST in interface TimeScales
        
        Returns:
            Galileo System Time scale
        
        
        """
        ...
    def getGalileoEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for Galileo System Time: 1999-08-22T00:00:00 GST.
        
        Specified by: getGalileoEpoch in interface TimeScales
        
        Returns:
            Galileo Epoch
        
        
        """
        ...
    def getGlonassEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for GLONASS four-year interval number: 1996-01-01T00:00:00 GLONASS time.
        
        By convention, TGLONASS = UTC + 3 hours.
        
        Specified by: getGlonassEpoch in interface TimeScales
        
        Returns:
            GLONASS Epoch
        
        
        """
        ...
    def getGpsEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
        
        Specified by: getGpsEpoch in interface TimeScales
        
        Returns:
            GPS Epoch
        
        
        """
        ...
    def getJ2000Epoch(self) -> AbsoluteDate:
        """
        J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (not UTC).
        
        Specified by: getJ2000Epoch in interface TimeScales
        
        Returns:
            J2000 Epoch
        
        Also see:
            createJulianEpoch, createBesselianEpoch
        
        
        """
        ...
    def getJavaEpoch(self) -> AbsoluteDate:
        """
        Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
        
        Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587, UTC-TAI = 8.000082s
        
        Specified by: getJavaEpoch in interface TimeScales
        
        Returns:
            Java Epoch
        
        
        """
        ...
    def getJulianEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
        
        Both Date and DateComponents classes follow the astronomical conventions and consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be seen in other documents or programs that obey a different convention (for example the convcal utility).
        
        Specified by: getJulianEpoch in interface TimeScales
        
        Returns:
            Julian epoch.
        
        
        """
        ...
    def getModifiedJulianEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
        
        Specified by: getModifiedJulianEpoch in interface TimeScales
        
        Returns:
            Modified Julian Epoch
        
        
        """
        ...
    def getNavIC(self) -> 'NavicScale':
        """
        Get the Navigation with Indian Constellation time scale.
        
        Specified by: getNavIC in interface TimeScales
        
        Returns:
            Navigation with Indian Constellation time scale
        
        
        """
        ...
    def getNavicEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for NavIC weeks: 1999-08-22T00:00:00 NavIC time.
        
        Specified by: getNavicEpoch in interface TimeScales
        
        Returns:
            NavIC Epoch
        
        
        """
        ...
    def getPastInfinity(self) -> AbsoluteDate:
        """
        Dummy date at infinity in the past direction.
        
        Specified by: getPastInfinity in interface TimeScales
        
        Returns:
            the earliest date.
        
        
        """
        ...
    def getQZSS(self) -> 'QZSSScale':
        """
        Get the Quasi-Zenith Satellite System time scale.
        
        Specified by: getQZSS in interface TimeScales
        
        Returns:
            Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    def getQzssEpoch(self) -> AbsoluteDate:
        """
        Reference epoch for QZSS weeks: 1980-01-06T00:00:00 QZSS time.
        
        Specified by: getQzssEpoch in interface TimeScales
        
        Returns:
            QZSS Epoch
        
        
        """
        ...
    def getTAI(self) -> 'TAIScale':
        """
        Get the International Atomic Time scale.
        
        Specified by: getTAI in interface TimeScales
        
        Returns:
            International Atomic Time scale
        
        
        """
        ...
    def getTCB(self) -> 'TCBScale':
        """
        Get the Barycentric Coordinate Time scale.
        
        Specified by: getTCB in interface TimeScales
        
        Returns:
            Barycentric Coordinate Time scale
        
        
        """
        ...
    def getTCG(self) -> 'TCGScale':
        """
        Get the Geocentric Coordinate Time scale.
        
        Specified by: getTCG in interface TimeScales
        
        Returns:
            Geocentric Coordinate Time scale
        
        
        """
        ...
    def getTDB(self) -> 'TDBScale':
        """
        Get the Barycentric Dynamic Time scale.
        
        Specified by: getTDB in interface TimeScales
        
        Returns:
            Barycentric Dynamic Time scale
        
        
        """
        ...
    def getTT(self) -> 'TTScale':
        """
        Get the Terrestrial Time scale.
        
        Specified by: getTT in interface TimeScales
        
        Returns:
            Terrestrial Time scale
        
        
        """
        ...
    def getUT1(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> 'UT1Scale':
        """
        Get the Universal Time 1 scale.
        
        Specified by: getUT1 in interface TimeScales
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Universal Time 1 scale
        
        Also see:
            getUTC, getEOPHistory
        
        
        """
        ...
    def getUTC(self) -> 'UTCScale':
        """
        Get the Universal Time Coordinate scale.
        
        Specified by: getUTC in interface TimeScales
        
        Returns:
            Universal Time Coordinate scale
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

_PythonTimeShiftable__T = typing.TypeVar('_PythonTimeShiftable__T', bound=TimeShiftable)  # <T>
class PythonTimeShiftable(TimeShiftable[_PythonTimeShiftable__T], typing.Generic[_PythonTimeShiftable__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def shiftedBy(self, dt: TimeOffset) -> _PythonTimeShiftable__T:
        """
        Get a time-shifted instance.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> _PythonTimeShiftable__T: ...

class PythonTimeStamped(TimeStamped):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDate(self) -> AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonTimeVectorFunction(TimeVectorFunction):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, date: AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Compute a function of time.
        
        Specified by: value in interface TimeVectorFunction
        
        Parameters:
            date (AbsoluteDate): date
        
        Returns:
            value of the function
        
        """
        ...
    @typing.overload
    def value(self, date: 'FieldAbsoluteDate'[_value_1__T]) -> typing.MutableSequence[_value_1__T]:
        """
        Compute a function of time.
        
        Specified by: value in interface TimeVectorFunction
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
        
        Returns:
            value of the function
        
        
        """
        ...

class PythonUTCTAIOffsetsLoader(UTCTAIOffsetsLoader):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def loadOffsets(self) -> java.util.List[OffsetModel]:
        """
        Load UTC-TAI offsets entries.
        
        Specified by: loadOffsets in interface UTCTAIOffsetsLoader
        
        Returns:
            sorted UTC-TAI offsets entries (if the linear offsets used prior to 1972 are missing, they will be inserted
            automatically)
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class SampledClockModel(ClockModel):
    """
    Offset clock model backed up by a sample.
    
    Since:
        12.1
    """
    def __init__(self, sample: java.util.List[ClockOffset], nbInterpolationPoints: int):
        """
        Simple constructor.
        
        Parameters:
            sample (List<ClockOffset> sample): clock offsets sample
            nbInterpolationPoints (int): number of points to use in interpolation
        
        
        """
        ...
    def getCache(self) -> org.orekit.utils.ImmutableTimeStampedCache[ClockOffset]:
        """
        Get the clock offsets cache.
        
        Returns:
            clock offsets cache
        
        
        """
        ...
    _getOffset_1__T = typing.TypeVar('_getOffset_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, date: AbsoluteDate) -> ClockOffset:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (AbsoluteDate): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        """
        ...
    @typing.overload
    def getOffset(self, date: 'FieldAbsoluteDate'[_getOffset_1__T]) -> FieldClockOffset[_getOffset_1__T]:
        """
        Get the clock offset at date.
        
        Specified by: getOffset in interface ClockModel
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which offset is requested
        
        Returns:
            clock offset at specified date
        
        
        """
        ...
    def getValidityEnd(self) -> AbsoluteDate:
        """
        Get validity end.
        
        Specified by: getValidityEnd in interface ClockModel
        
        Returns:
            model validity end
        
        
        """
        ...
    def getValidityStart(self) -> AbsoluteDate:
        """
        Get validity start.
        
        Specified by: getValidityStart in interface ClockModel
        
        Returns:
            model validity start
        
        
        """
        ...

class SatelliteClockScale(TimeScale):
    """
    Scale for on-board clock.
    
    Since:
        11.0
    """
    def __init__(self, name: str, epoch: AbsoluteDate, epochScale: TimeScale, countAtEpoch: float, drift: float):
        """
        Create a linear model for satellite clock.
        
        Beware that we specify the model using its drift with respect to flow of time. For a perfect clock without any drift, the clock count would be one tick every SI second. A clock that is fast, say for example it generates 1000001 ticks every 1000000 SI second, would have a rate of 1.000001 tick per SI second and hence a drift of 1.0e-6 tick per SI second. In this constructor we use the drift (1.0e-6 in the previous example) rather than the rate (1.000001 in the previous example) to specify the clock. The rationale is that for clocks that are intended to be used for representing absolute time, the drift is expected to be small (much smaller that 1.0e-6 for a good clock), so using drift is numerically more stable than using rate and risking catastrophic cancellation when subtracting 1.0 in the internal computation.
        
        Despite what is explained in the previous paragraph, this class can handle spacecraft clocks that are not intended to be synchronized with SI seconds, for example clocks that ticks at 10 Hz. In such cases the drift would need to be set at 10.0 - 1.0 = 9.0, which is not intuitive. For these clocks, the methods countAtDate and dateAtCount and perhaps offsetFromTAI are still useful, whereas offsetToTAI is probably not really meaningful.
        
        Parameters:
            name (String): of the scale
            epoch (AbsoluteDate): reference epoch
            epochScale (TimeScale): time scale in which the epoch was defined
            countAtEpoch (double): clock count at epoch
            drift (double): clock drift rate (i.e. clock count change per SI second minus 1.0)
        
        
        """
        ...
    def countAtDate(self, date: AbsoluteDate) -> float:
        """
        Compute clock count corresponding to some date.
        
        Parameters:
            date (AbsoluteDate): date
        
        Returns:
            clock count at date
        
        
        """
        ...
    def dateAtCount(self, count: float) -> AbsoluteDate:
        """
        Compute date corresponding to some clock count.
        
        Parameters:
            count (double): clock count
        
        Returns:
            date at count
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def offsetToTAI(self, date: DateComponents, time: TimeComponents) -> TimeOffset:
        """
        Get the offset to convert locations from instance to TAIScale.
        
        Specified by: offsetToTAI in interface TimeScale
        
        Parameters:
            date (DateComponents): date location in the time scale
            time (TimeComponents): time location in the time scale
        
        Returns:
            offset in seconds to add to a location in instance time scale to get a location in TAIScale
            time scale
        
        Also see:
            offsetFromTAI
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class TAIUTCDatFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    Loader for UTC-TAI extracted from tai-utc.dat file from USNO.
    
    This class is immutable and hence thread-safe
    
    Since:
        7.1
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default supported files name pattern.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]:
        """
        Load UTC-TAI offsets entries.
        
        Specified by: loadOffsets in interface UTCTAIOffsetsLoader
        
        Returns:
            sorted UTC-TAI offsets entries (if the linear offsets used prior to 1972 are missing, they will be inserted
            automatically)
        
        
        """
        ...
    class Parser(UTCTAIOffsetsLoader.Parser):
        def __init__(self): ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class TCBScale(TimeScale):
    """
    Barycentric Coordinate Time.
    
    Coordinate time at the center of mass of the Solar System. This time scale depends linearly from TDBScale.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class TCGScale(TimeScale):
    """
    Geocentric Coordinate Time.
    
    Coordinate time at the center of mass of the Earth. This time scale depends linearly from TTScale.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class TDBScale(TimeScale):
    """
    Barycentric Dynamic Time.
    
    Time used to take account of time dilation when calculating orbits of planets, asteroids, comets and interplanetary spacecraft in the Solar system. It was based on a Dynamical time scale but was not well defined and not rigorously correct as a relativistic time scale. It was subsequently deprecated in favour of Barycentric Coordinate Time (TCB), but at the 2006 General Assembly of the International Astronomical Union TDB was rehabilitated by making it a specific fixed linear transformation of TCB.
    
    By convention, TDB = TT + 0.001658 sin(g) + 0.000014 sin(2g)seconds where g = 357.53 + 0.9856003 (JD - 2451545) degrees.
    """
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class TimeStampedDouble(TimeStamped):
    """
    Class that associates a double with a date.
    
    Also see:
        AbsoluteDate
    """
    @typing.overload
    def __init__(self, double: float, absoluteDate: AbsoluteDate): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, double: float): ...
    def getDate(self) -> AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Get value.
        
        Returns:
            value
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

_TimeStampedField__KK = typing.TypeVar('_TimeStampedField__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class TimeStampedField(FieldTimeStamped[_TimeStampedField__KK], typing.Generic[_TimeStampedField__KK]):
    """
    Class that associates a field with a date.
    
    Also see:
        FieldAbsoluteDate,
        CalculusFieldElement
    """
    @typing.overload
    def __init__(self, kK: _TimeStampedField__KK, absoluteDate: AbsoluteDate): ...
    @typing.overload
    def __init__(self, kK: _TimeStampedField__KK, fieldAbsoluteDate: 'FieldAbsoluteDate'[_TimeStampedField__KK]): ...
    def getDate(self) -> 'FieldAbsoluteDate'[_TimeStampedField__KK]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getValue(self) -> _TimeStampedField__KK:
        """
        Get value.
        
        Returns:
            value
        
        
        """
        ...

_TimeStampedPair__K = typing.TypeVar('_TimeStampedPair__K', bound=TimeStamped)  # <K>
_TimeStampedPair__V = typing.TypeVar('_TimeStampedPair__V', bound=TimeStamped)  # <V>
class TimeStampedPair(TimeStamped, typing.Generic[_TimeStampedPair__K, _TimeStampedPair__V]):
    """
    Pair of time stamped values being defined at the same date.
    
    Also see:
        TimeStamped
    """
    DEFAULT_DATE_EQUALITY_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default date equality threshold of 1 ns.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, k: _TimeStampedPair__K, v: _TimeStampedPair__V): ...
    @typing.overload
    def __init__(self, k: _TimeStampedPair__K, v: _TimeStampedPair__V, double: float): ...
    @staticmethod
    def checkDatesConsistency(firstDate: AbsoluteDate, secondDate: AbsoluteDate, dateEqualityThreshold: float) -> None:
        """
        Check date consistency.
        
        Parameters:
            firstDate (AbsoluteDate): first date
            secondDate (AbsoluteDate): second date
            dateEqualityThreshold (double): threshold below which dates are considered equal
        
        
        """
        ...
    def getDate(self) -> AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFirst(self) -> _TimeStampedPair__K:
        """
        Get first time stamped value.
        
        Returns:
            first time stamped value
        
        
        """
        ...
    def getSecond(self) -> _TimeStampedPair__V:
        """
        Get second time stamped value.
        
        Returns:
            second time stamped value
        
        
        """
        ...

class UT1Scale(TimeScale):
    """
    Universal Time 1.
    
    UT1 is a time scale directly linked to the actual rotation of the Earth. It is an irregular scale, reflecting Earth irregular rotation rate. The offset between UT1 and UTCScale is found in the Earth Orientation Parameters published by IERS.
    
    Since:
        5.1
    
    Also see:
        AbsoluteDate
    """
    def getEOPHistory(self) -> org.orekit.frames.EOPHistory:
        """
        Get the EOP history.
        
        Returns:
            eop history (may be null)
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    def getUTCScale(self) -> 'UTCScale':
        """
        Get the associated UTC scale.
        
        Returns:
            associated UTC scale.
        
        Since:
            9.1
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class UTCScale(TimeScale):
    """
    Coordinated Universal Time.
    
    UTC is related to TAI using step adjustments from time to time according to IERS (International Earth Rotation Service) rules. Before 1972, these adjustments were piecewise linear offsets. Since 1972, these adjustments are piecewise constant offsets, which require introduction of leap seconds.
    
    Leap seconds are always inserted as additional seconds at the last minute of the day, pushing the next day forward. Such minutes are therefore more than 60 seconds long. In theory, there may be seconds removal instead of seconds insertion, but up to now (2010) it has never been used. As an example, when a one second leap was introduced at the end of 2005, the UTC time sequence was 2005-12-31T23:59:59 UTC, followed by 2005-12-31T23:59:60 UTC, followed by 2006-01-01T00:00:00 UTC.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    def getBaseOffsets(self) -> java.util.Collection[OffsetModel]:
        """
        Get the base offsets.
        
        Returns:
            base offsets (may lack the pre-1975 offsets)
        
        Since:
            12.0
        
        
        """
        ...
    def getFirstKnownLeapSecond(self) -> AbsoluteDate:
        """
        Get the date of the first known leap second.
        
        Returns:
            date of the first known leap second
        
        
        """
        ...
    def getLastKnownLeapSecond(self) -> AbsoluteDate:
        """
        Get the date of the last known leap second.
        
        Returns:
            date of the last known leap second
        
        
        """
        ...
    _getLeap_0__T = typing.TypeVar('_getLeap_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLeap(self, date: 'FieldAbsoluteDate'[_getLeap_0__T]) -> _getLeap_0__T:
        """
        Get the value of the previous leap.
        
        This method will return 0.0 for all time scales that do not implement leap seconds.
        
        Specified by: getLeap in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            value of the previous leap
        
        
        """
        ...
    @typing.overload
    def getLeap(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the value of the previous leap.
        
        This method will return 0 for all time scales that do not implement leap seconds.
        
        Specified by: getLeap in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            value of the previous leap
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name time scale.
        
        Specified by: getName in interface TimeScale
        
        Returns:
            name of the time scale
        
        
        """
        ...
    def getUTCTAIOffsets(self) -> java.util.List['UTCTAIOffset']:
        """
        Returns the UTC-TAI offsets underlying this UTC scale.
        
        Modifications to the returned list will not affect this UTC scale instance.
        
        Returns:
            new non-null modifiable list of UTC-TAI offsets time-sorted from earliest to latest
        
        
        """
        ...
    _insideLeap_1__T = typing.TypeVar('_insideLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def insideLeap(self, date: AbsoluteDate) -> bool:
        """
        Check if date is within a leap second introduction in this time scale.
        
        This method will return false for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale.
        
        Specified by: insideLeap in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            true if time is within a leap second introduction
        
        """
        ...
    @typing.overload
    def insideLeap(self, date: 'FieldAbsoluteDate'[_insideLeap_1__T]) -> bool:
        """
        Check if date is within a leap second introduction in this time scale.
        
        This method will return false for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale.
        
        Specified by: insideLeap in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            true if time is within a leap second introduction
        
        
        """
        ...
    _minuteDuration_1__T = typing.TypeVar('_minuteDuration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def minuteDuration(self, date: AbsoluteDate) -> int:
        """
        Check length of the current minute in this time scale.
        
        This method will return 60 for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale, and 61 for time scales that do implement leap second when the current date is within the last minute before the leap, or during the leap itself.
        
        Specified by: minuteDuration in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): date to check
        
        Returns:
            60 or 61 depending on leap seconds introduction
        
        """
        ...
    @typing.overload
    def minuteDuration(self, date: 'FieldAbsoluteDate'[_minuteDuration_1__T]) -> int:
        """
        Check length of the current minute in this time scale.
        
        This method will return 60 for all time scales that do not implement leap seconds, even if the date corresponds to a leap second in UTCScale, and 61 for time scales that do implement leap second when the current date is within the last minute before the leap, or during the leap itself.
        
        Specified by: minuteDuration in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date to check
        
        Returns:
            60 or 61 depending on leap seconds introduction
        
        
        """
        ...
    _offsetFromTAI_0__T = typing.TypeVar('_offsetFromTAI_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, date: 'FieldAbsoluteDate'[_offsetFromTAI_0__T]) -> _offsetFromTAI_0__T:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (FieldAbsoluteDate<T> date): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, date: AbsoluteDate) -> TimeOffset:
        """
        Get the offset to convert locations from TAIScale to instance.
        
        Specified by: offsetFromTAI in interface TimeScale
        
        Parameters:
            date (AbsoluteDate): conversion date
        
        Returns:
            offset in seconds to add to a location in TAIScale time scale to get a location in instance
            time scale
        
        Also see:
            offsetToTAI
        
        """
        ...
    def offsetToTAI(self, date: DateComponents, time: TimeComponents) -> TimeOffset:
        """
        Get the offset to convert locations from instance to TAIScale.
        
        Specified by: offsetToTAI in interface TimeScale
        
        Parameters:
            date (DateComponents): date location in the time scale
            time (TimeComponents): time location in the time scale
        
        Returns:
            offset in seconds to add to a location in instance time scale to get a location in TAIScale
            time scale
        
        Also see:
            offsetFromTAI
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class UTCTAIBulletinAFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    Loader for UTC-TAI extracted from bulletin A files.
    
    This class is a modified version of BulletinAFileLoader that only parses the TAI-UTC header line and checks the UT1-UTC column for discontinuities.
    
    Note that extracting UTC-TAI from bulletin A files is NOT recommended. There are known issues in some past bulletin A (for example bulletina-xix-001.txt from 2006-01-05 has a wrong year for last leap second and bulletina-xxi-053.txt from 2008-12-31 has an off by one value for TAI-UTC on MJD 54832). This is a known problem, and the Earth Orientation Department at USNO told us this TAI-UTC data was only provided as a convenience and this data should rather be sourced from other official files. As the bulletin A files are a record of past publications, they cannot modify archived bulletins, hence the errors above will remain forever. This UTC-TAI loader should therefore be used with great care.
    
    This class is immutable and hence thread-safe
    
    Since:
        7.1
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]:
        """
        Load UTC-TAI offsets entries.
        
        Specified by: loadOffsets in interface UTCTAIOffsetsLoader
        
        Returns:
            sorted UTC-TAI offsets entries (if the linear offsets used prior to 1972 are missing, they will be inserted
            automatically)
        
        
        """
        ...

class UTCTAIHistoryFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    Loader for UTC versus TAI history files.
    
    UTC versus TAI history files contain UTCTAIOffset data since.
    
    The UTC versus TAI history files are recognized thanks to their base names, which must match the pattern history (or gz for gzip-compressed files)
    
    Only one history file must be present in the IERS directories hierarchy.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]:
        """
        Load UTC-TAI offsets entries.
        
        Specified by: loadOffsets in interface UTCTAIOffsetsLoader
        
        Returns:
            sorted UTC-TAI offsets entries (if the linear offsets used prior to 1972 are missing, they will be inserted
            automatically)
        
        
        """
        ...
    class Parser(UTCTAIOffsetsLoader.Parser):
        def __init__(self): ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class UTCTAIOffset(TimeStamped, java.io.Serializable):
    """
    Offset between UTCScale and TAIScale time scales.
    
    The UTCScale and TAIScale time scales are two scales offset with respect to each other. The TAIScale scale is continuous whereas the UTCScale includes some discontinuity when leap seconds are introduced by the `International Earth Rotation Service <http://www.iers.org/>` (IERS).
    
    This class represents the offset between the two scales that is valid between two leap seconds occurrences. It handles both the linear offsets used from 1961-01-01 to 1971-12-31 and the constant integer offsets used since 1972-01-01.
    
    Also see:
        UTCScale, UTCTAIHistoryFilesLoader, serialized
    """
    def getDate(self) -> AbsoluteDate:
        """
        Get the date of the start of the leap.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date of the start of the leap
        
        Also see:
            getValidityStart
        
        
        """
        ...
    def getLeap(self) -> TimeOffset:
        """
        Get the value of the leap at offset validity start.
        
        Returns:
            value of the leap at offset validity start
        
        
        """
        ...
    def getMJD(self) -> int:
        """
        Get the date of the start of the leap as Modified Julian Day.
        
        Returns:
            date of the start of the leap as Modified Julian Day
        
        
        """
        ...
    _getOffset_0__T = typing.TypeVar('_getOffset_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, date: 'FieldAbsoluteDate'[_getOffset_0__T]) -> _getOffset_0__T:
        """
        Get the TAI - UTC offset in seconds.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which the offset is requested
        
        Returns:
            TAI - UTC offset in seconds.
        
        Since:
            9.0
        
        """
        ...
    @typing.overload
    def getOffset(self, absoluteDate: AbsoluteDate) -> TimeOffset:
        """
        Get the TAI - UTC offset in seconds.
        
        Parameters:
            date (AbsoluteDate): date at which the offset is requested
        
        Returns:
            TAI - UTC offset in seconds.
        
        Get the TAI - UTC offset in seconds.
        
        Parameters:
            date (DateComponents): date components (in UTC) at which the offset is requested
            time (TimeComponents): time components (in UTC) at which the offset is requested
        
        Returns:
            TAI - UTC offset in seconds.
        
        
        """
        ...
    @typing.overload
    def getOffset(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> TimeOffset: ...
    def getValidityStart(self) -> AbsoluteDate:
        """
        Get the start time of validity for this offset.
        
        The start of the validity of the offset is getLeap seconds after the start of the leap itself.
        
        Returns:
            start of validity date
        
        Also see:
            getDate
        
        
        """
        ...

class BDTScale(ConstantOffsetTimeScale):
    """
    Beidou system time scale.
    
    By convention, BDT = UTC on January 1st 2006.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    ...

class ClockOffsetHermiteInterpolator(AbstractTimeInterpolator[ClockOffset]):
    """
    bHermite interpolator of time stamped clock offsets.
    
    Since:
        12.1
    
        class:`~org.orekit.time.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, TimeInterpolator
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...

_FieldAbsoluteDate__T = typing.TypeVar('_FieldAbsoluteDate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbsoluteDate(FieldTimeStamped[_FieldAbsoluteDate__T], FieldTimeShiftable['FieldAbsoluteDate'[_FieldAbsoluteDate__T], _FieldAbsoluteDate__T], java.lang.Comparable['FieldAbsoluteDate'[_FieldAbsoluteDate__T]], typing.Generic[_FieldAbsoluteDate__T]):
    """
    This class represents a specific instant in time.
    
    Instances of this class are considered to be absolute in the sense that each one represent the occurrence of some event and can be compared to other instances or located in any TimeScale. In other words the different locations of an event with respect to two different time scales (say TAIScale and UTCScale for example) are simply different perspective related to a single object. Only one FieldAbsoluteDate<T> instance is needed, both representations being available from this single instance by specifying the time scales as parameter when calling the ad-hoc methods.
    
    Since an instance is not bound to a specific time-scale, all methods related to the location of the date within some time scale require to provide the time scale as an argument. It is therefore possible to define a date in one time scale and to use it in another one. An example of such use is to read a date from a file in UTC and write it in another file in TAI. This can be done as follows:
    
    
       DateTimeComponents utcComponents = readNextDate();
       FieldAbsoluteDate<T> date = new FieldAbsoluteDate<>(utcComponents, TimeScalesFactory.getUTC());
       writeNextDate(date.getComponents(TimeScalesFactory.getTAI()));
     
    
    Two complementary views are available:
    
      - 
        location view (mainly for input/output or conversions)
    
        locations represent the coordinate of one event with respect to a TimeScale. The related
        methods are , createGPSDate,
        parseCCSDSCalendarSegmentedTimeCode,
        toDate, toString,
        toString, and timeScalesOffset.
      - 
        offset view (mainly for physical computation)
    
        offsets represent either the flow of time between two events (two instances of the class) or durations. They are counted in seconds, are continuous and could be measured using only a virtually perfect stopwatch. The related methods are , parseCCSDSUnsegmentedTimeCode, parseCCSDSDaySegmentedTimeCode, durationFrom, compareTo, equals and hashCode.
    
    A few reference epochs which are commonly used in space systems have been defined. These epochs can be used as the basis for offset computation. The supported epochs are: getJulianEpoch, getModifiedJulianEpoch, getFiftiesEpoch, getCCSDSEpoch, getGalileoEpoch, getGPSEpoch, getJ2000Epoch, getJavaEpoch. There are also two factory methods createJulianEpoch and createBesselianEpoch that can be used to compute other reference epochs like J1900.0 or B1950.0. In addition to these reference epochs, two other constants are defined for convenience: getPastInfinity and getFutureInfinity, which can be used either as dummy dates when a date is not yet initialized, or for initialization of loops searching for a min or max date.
    
    Instances of the FieldAbsoluteDate<T> class are guaranteed to be immutable.
    
    Also see:
        TimeScale, TimeStamped,
        ChronologicalComparator
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, int2: int, int3: int, int4: int, int5: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, int2: int, int3: int, int4: int, int5: int, timeOffset: TimeOffset, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, int2: int, int3: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, month: Month, int2: int, int3: int, int4: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, month: Month, int2: int, int3: int, int4: int, timeOffset: TimeOffset, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, month: Month, int2: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], string: str, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], instant: typing.Union[java.time.Instant, datetime.datetime]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], instant: typing.Union[java.time.Instant, datetime.datetime], timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], instant: typing.Union[java.time.Instant, datetime.datetime], uTCScale: UTCScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], date: java.util.Date, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], absoluteDate: AbsoluteDate): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], dateComponents: DateComponents, timeComponents: TimeComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], dateComponents: DateComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], dateTimeComponents: DateTimeComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, long: int, timeUnit: java.util.concurrent.TimeUnit, field: org.hipparchus.Field[_FieldAbsoluteDate__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, t: _FieldAbsoluteDate__T): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], double: float): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], long: int, timeUnit: java.util.concurrent.TimeUnit): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], t: _FieldAbsoluteDate__T): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], timeOffset: TimeOffset): ...
    def compareTo(self, other: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]) -> int:
        """
        Compare the instance with another date.
        
        Specified by: Comparable in interface Comparable
        
        Parameters:
            other (FieldAbsoluteDate<FieldAbsoluteDate> other): other date to compare the instance to
        
        Returns:
            a negative integer, zero, or a positive integer as this date is before, simultaneous, or after the specified date.
        
        
        """
        ...
    _createBesselianEpoch_0__T = typing.TypeVar('_createBesselianEpoch_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _createBesselianEpoch_1__T = typing.TypeVar('_createBesselianEpoch_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createBesselianEpoch(t: _createBesselianEpoch_0__T) -> 'FieldAbsoluteDate'[_createBesselianEpoch_0__T]:
        """
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date as:
        
         BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
        
        This method reverts the formula above and computes an FieldAbsoluteDate<T> from the Besselian Epoch.
        
        Parameters:
            besselianEpoch (T): Besselian epoch, like 1950 for defining the classical reference B1950.0
            timeScales (TimeScales): used in the computation.
        
        Returns:
            a new instant
        
        Since:
            10.1
        
        Also see:
            createJulianEpoch, createBesselianEpoch
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createBesselianEpoch(t: _createBesselianEpoch_1__T, timeScales: TimeScales) -> 'FieldAbsoluteDate'[_createBesselianEpoch_1__T]: ...
    _createGPSDate_0__T = typing.TypeVar('_createGPSDate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _createGPSDate_1__T = typing.TypeVar('_createGPSDate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createGPSDate(int: int, t: _createGPSDate_0__T) -> 'FieldAbsoluteDate'[_createGPSDate_0__T]:
        """
        Build an instance corresponding to a GPS date.
        
        GPS dates are provided as a week number starting at getGPSEpoch and as a number of milliseconds since week start.
        
        Parameters:
            weekNumber (int): week number since getGPSEpoch
            milliInWeek (T): number of milliseconds since week start
            gps (TimeScale): GPS time scale.
        
        Returns:
            a new instant
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createGPSDate(int: int, t: _createGPSDate_1__T, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_createGPSDate_1__T]: ...
    _createJDDate_0__T = typing.TypeVar('_createJDDate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _createJDDate_1__T = typing.TypeVar('_createJDDate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createJDDate(int: int, t: _createJDDate_0__T, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_createJDDate_0__T]:
        """
        Build an instance corresponding to a Julian Day date.
        
        Parameters:
            jd (int): Julian day
            secondsSinceNoon (T): seconds in the Julian day (BEWARE, Julian days start at noon, so 0.0 is noon)
            timeScale (TimeScale): time scale in which the seconds in day are defined
        
        Returns:
            a new instant
        
        Build an instance corresponding to a Julian Day date.
        
        This function should be preferred to createJDDate when the target time scale has a non-constant offset with respect to TAI.
        
        The idea is to introduce a pivot time scale that is close to the target time scale but has a constant bias with TAI.
        
        For example, to get a date from an MJD in TDB time scale, it's advised to use the TT time scale as a pivot scale. TT is very close to TDB and has constant offset to TAI.
        
        Parameters:
            jd (int): Julian day
            secondsSinceNoon (T): seconds in the Julian day (BEWARE, Julian days start at noon, so 0.0 is noon)
            timeScale (TimeScale): time scale in which the seconds in day are defined
            pivotTimeScale (TimeScale): pivot timescale used as intermediate timescale
        
        Returns:
            a new instant
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createJDDate(int: int, t: _createJDDate_1__T, timeScale: TimeScale, timeScale2: TimeScale) -> 'FieldAbsoluteDate'[_createJDDate_1__T]: ...
    _createJulianEpoch_0__T = typing.TypeVar('_createJulianEpoch_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _createJulianEpoch_1__T = typing.TypeVar('_createJulianEpoch_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createJulianEpoch(t: _createJulianEpoch_0__T) -> 'FieldAbsoluteDate'[_createJulianEpoch_0__T]:
        """
        According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`, Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as: 0) / 365
        
        This method reverts the formula above and computes an FieldAbsoluteDate<T> from the Julian Epoch.
        
        Parameters:
            julianEpoch (T): Julian epoch, like 2000.0 for defining the classical reference J2000.0
            timeScales (TimeScales): used in the computation.
        
        Returns:
            a new instant
        
        Since:
            10.1
        
        Also see:
            getJ2000Epoch,
            createBesselianEpoch, createJulianEpoch
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createJulianEpoch(t: _createJulianEpoch_1__T, timeScales: TimeScales) -> 'FieldAbsoluteDate'[_createJulianEpoch_1__T]: ...
    _createMJDDate__T = typing.TypeVar('_createMJDDate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def createMJDDate(mjd: int, secondsInDay: _createMJDDate__T, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_createMJDDate__T]:
        """
        Build an instance corresponding to a Modified Julian Day date.
        
        Parameters:
            mjd (int): modified Julian day
            secondsInDay (T): seconds in the day
            timeScale (TimeScale): time scale in which the seconds in day are defined
        
        Returns:
            a new instant
        
        
        """
        ...
    _createMedian__T = typing.TypeVar('_createMedian__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def createMedian(date1: 'FieldAbsoluteDate'[_createMedian__T], date2: 'FieldAbsoluteDate'[_createMedian__T]) -> 'FieldAbsoluteDate'[_createMedian__T]:
        """
        Create an instance as the median data between two existing instances.
        
        Parameters:
            date1 (FieldAbsoluteDate<T> date1): first instance
            date2 (FieldAbsoluteDate<T> date2): second instance
        
        Returns:
            median date between first and second instance
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def durationFrom(self, fieldTimeStamped: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> _FieldAbsoluteDate__T:
        """
        Compute the physically elapsed duration between two instants.
        
        The returned duration is the number of seconds physically elapsed between the two instants, measured in a regular time scale with respect to surface of the Earth (i.e either the TAIScale, the TTScale or the GPSScale). It is the only method that gives a duration with a physical meaning.
        
        This method gives the same result (with less computation) as calling offsetFrom with a second argument set to one of the regular scales cited above.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (AbsoluteDate): instant to subtract from the instance
        
        Returns:
            offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Also see:
            offsetFrom, 
        
        Compute the physically elapsed duration between two instants.
        
        The returned duration is the number of seconds physically elapsed between the two instants, measured in a regular time scale with respect to surface of the Earth (i.e either the TAIScale, the TTScale or the GPSScale). It is the only method that gives a duration with a physical meaning.
        
        This method gives the same result (with less computation) as calling offsetFrom with a second argument set to one of the regular scales cited above.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (AbsoluteDate): instant to subtract from the instance
            timeUnit (TimeUnit): TimeUnit precision for the
                offset
        
        Returns:
            offset in the given timeunit between the two instants (positive if the instance is posterior to the argument), rounded
            to the nearest integer
            TimeUnit
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def durationFrom(self, timeStamped: typing.Union[TimeStamped, typing.Callable]) -> _FieldAbsoluteDate__T: ...
    @typing.overload
    def durationFrom(self, absoluteDate: AbsoluteDate) -> _FieldAbsoluteDate__T: ...
    @typing.overload
    def durationFrom(self, absoluteDate: AbsoluteDate, timeUnit: java.util.concurrent.TimeUnit) -> _FieldAbsoluteDate__T: ...
    @typing.overload
    def durationFrom(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]) -> _FieldAbsoluteDate__T: ...
    @typing.overload
    def durationFrom(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], timeUnit: java.util.concurrent.TimeUnit) -> _FieldAbsoluteDate__T: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Check if the instance represents the same time as another instance.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): other date
        
        Returns:
            true if the instance and the other date refer to the same instant with same Field and addendum
        
        
        """
        ...
    _getArbitraryEpoch__T = typing.TypeVar('_getArbitraryEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getArbitraryEpoch(field: org.hipparchus.Field[_getArbitraryEpoch__T]) -> 'FieldAbsoluteDate'[_getArbitraryEpoch__T]:
        """
        Get an arbitrary date. Useful when a non-null date is needed but its values does not matter.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            an arbitrary date.
        
        
        """
        ...
    _getCCSDSEpoch__T = typing.TypeVar('_getCCSDSEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getCCSDSEpoch(field: org.hipparchus.Field[_getCCSDSEpoch__T]) -> 'FieldAbsoluteDate'[_getCCSDSEpoch__T]:
        """
        Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4).
        
        This method uses the getDefault. 1958-01-01T00:00:00 International Atomic Time (not UTC).
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the reference epoch for CCSDS Time Code Format as a FieldAbsoluteDate
        
        Also see:
            CCSDS_EPOCH, getCcsdsEpoch
        
        
        """
        ...
    @typing.overload
    def getComponents(self, int: int) -> DateTimeComponents:
        """
        Split the instance into date/time components.
        
        Parameters:
            timeScale (TimeScale): time scale to use
        
        Returns:
            date/time components
        
        Split the instance into date/time components for a local time.
        
        This method uses the getDefault.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC)
        
        Returns:
            date/time components
        
        Also see:
            getComponents
        
        Split the instance into date/time components for a local time.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC)
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            date/time components
        
        Since:
            10.1
        
        Split the instance into date/time components for a time zone.
        
        This method uses the getDefault.
        
        Parameters:
            timeZone (TimeZone): time zone
        
        Returns:
            date/time components
        
        Also see:
            getComponents
        
        Split the instance into date/time components for a time zone.
        
        Parameters:
            timeZone (TimeZone): time zone
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            date/time components
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getComponents(self, int: int, timeScale: TimeScale) -> DateTimeComponents: ...
    @typing.overload
    def getComponents(self, timeZone: java.util.TimeZone) -> DateTimeComponents: ...
    @typing.overload
    def getComponents(self, timeZone: java.util.TimeZone, timeScale: TimeScale) -> DateTimeComponents: ...
    @typing.overload
    def getComponents(self, timeScale: TimeScale) -> DateTimeComponents: ...
    def getDate(self) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getDayOfYear(self, utc: TimeScale) -> _FieldAbsoluteDate__T:
        """
        Get day of year, preserving continuity as much as possible.
        
        This is a continuous extension of the integer value returned by getComponentsgetDategetDayOfYear. In order to have it remain as close as possible to its integer counterpart, day 1.0 is considered to occur on January 1st at noon.
        
        Continuity is preserved from day to day within a year, but of course there is a discontinuity at year change, where it switches from 365.49999… (or 366.49999… on leap years) to 0.5
        
        Parameters:
            utc (TimeScale): time scale to compute date components
        
        Returns:
            day of year, with day 1.0 occurring on January first at noon
        
        Since:
            13.0
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldAbsoluteDate__T]:
        """
        Get the field.
        
        Returns:
            field instance.
        
        
        """
        ...
    _getFiftiesEpoch__T = typing.TypeVar('_getFiftiesEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getFiftiesEpoch(field: org.hipparchus.Field[_getFiftiesEpoch__T]) -> 'FieldAbsoluteDate'[_getFiftiesEpoch__T]:
        """
        Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
        
        This method uses the getDefault.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the reference epoch for 1950 dates as a FieldAbsoluteDate
        
        Also see:
            FIFTIES_EPOCH, getFiftiesEpoch
        
        
        """
        ...
    _getFutureInfinity__T = typing.TypeVar('_getFutureInfinity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getFutureInfinity(field: org.hipparchus.Field[_getFutureInfinity__T]) -> 'FieldAbsoluteDate'[_getFutureInfinity__T]:
        """
        Dummy date at infinity in the future direction.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            a dummy date at infinity in the future direction as a FieldAbsoluteDate
        
        Also see:
            FUTURE_INFINITY, getFutureInfinity
        
        
        """
        ...
    _getGPSEpoch__T = typing.TypeVar('_getGPSEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getGPSEpoch(field: org.hipparchus.Field[_getGPSEpoch__T]) -> 'FieldAbsoluteDate'[_getGPSEpoch__T]:
        """
        Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
        
        This method uses the getDefault.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the reference epoch for GPS weeks as a FieldAbsoluteDate
        
        Also see:
            GPS_EPOCH, getGpsEpoch
        
        
        """
        ...
    _getGalileoEpoch__T = typing.TypeVar('_getGalileoEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getGalileoEpoch(field: org.hipparchus.Field[_getGalileoEpoch__T]) -> 'FieldAbsoluteDate'[_getGalileoEpoch__T]:
        """
        Reference epoch for Galileo System Time: 1999-08-22T00:00:00 UTC.
        
        This method uses the getDefault.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the reference epoch for Galileo System Time as a FieldAbsoluteDate
        
        Also see:
            GALILEO_EPOCH, getGalileoEpoch
        
        
        """
        ...
    _getJ2000Epoch__T = typing.TypeVar('_getJ2000Epoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getJ2000Epoch(field: org.hipparchus.Field[_getJ2000Epoch__T]) -> 'FieldAbsoluteDate'[_getJ2000Epoch__T]:
        """
        J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (not UTC).
        
        This method uses the getDefault.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the J2000.0 reference epoch as a FieldAbsoluteDate
        
        Also see:
            createJulianEpoch, J2000_EPOCH,
            getJ2000Epoch
        
        
        """
        ...
    @typing.overload
    def getJD(self) -> _FieldAbsoluteDate__T:
        """
        Return the given date as a Julian Date expressed in UTC.
        
        Returns:
            double representation of the given date as Julian Date.
        
        Since:
            12.2
        
        """
        ...
    @typing.overload
    def getJD(self, ts: TimeScale) -> _FieldAbsoluteDate__T:
        """
        Return the given date as a Julian Date expressed in given timescale.
        
        Parameters:
            ts (TimeScale): time scale
        
        Returns:
            double representation of the given date as Julian Date.
        
        Since:
            12.2
        
        
        """
        ...
    _getJavaEpoch__T = typing.TypeVar('_getJavaEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getJavaEpoch(field: org.hipparchus.Field[_getJavaEpoch__T]) -> 'FieldAbsoluteDate'[_getJavaEpoch__T]:
        """
        Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
        
        This method uses the getDefault.
        
        Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587, UTC-TAI = 8.000082s
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the Java reference epoch as a FieldAbsoluteDate
        
        Also see:
            JAVA_EPOCH, getJavaEpoch
        
        
        """
        ...
    _getJulianEpoch__T = typing.TypeVar('_getJulianEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getJulianEpoch(field: org.hipparchus.Field[_getJulianEpoch__T]) -> 'FieldAbsoluteDate'[_getJulianEpoch__T]:
        """
        Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
        
        Both Date and DateComponents classes follow the astronomical conventions and consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be seen in other documents or programs that obey a different convention (for example the convcal utility).
        
        This method uses the getDefault.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the reference epoch for julian dates as a FieldAbsoluteDate
        
        Also see:
            JULIAN_EPOCH, getJulianEpoch
        
        
        """
        ...
    @typing.overload
    def getMJD(self) -> _FieldAbsoluteDate__T:
        """
        Return the given date as a Modified Julian Date expressed in UTC.
        
        Returns:
            double representation of the given date as Modified Julian Date.
        
        Since:
            12.2
        
        """
        ...
    @typing.overload
    def getMJD(self, ts: TimeScale) -> _FieldAbsoluteDate__T:
        """
        Return the given date as a Modified Julian Date expressed in given timescale.
        
        Parameters:
            ts (TimeScale): time scale
        
        Returns:
            double representation of the given date as Modified Julian Date.
        
        Since:
            12.2
        
        
        """
        ...
    _getModifiedJulianEpoch__T = typing.TypeVar('_getModifiedJulianEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getModifiedJulianEpoch(field: org.hipparchus.Field[_getModifiedJulianEpoch__T]) -> 'FieldAbsoluteDate'[_getModifiedJulianEpoch__T]:
        """
        Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
        
        This method uses the getDefault.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            the reference epoch for modified julian dates as a FieldAbsoluteDate
        
        Also see:
            MODIFIED_JULIAN_EPOCH, getModifiedJulianEpoch
        
        
        """
        ...
    _getPastInfinity__T = typing.TypeVar('_getPastInfinity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getPastInfinity(field: org.hipparchus.Field[_getPastInfinity__T]) -> 'FieldAbsoluteDate'[_getPastInfinity__T]:
        """
        Dummy date at infinity in the past direction.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            a dummy date at infinity in the past direction as a FieldAbsoluteDate
        
        Also see:
            PAST_INFINITY, getPastInfinity
        
        
        """
        ...
    def hasZeroField(self) -> bool:
        """
        Check if the Field is semantically equal to zero.
        
        Using FieldElement
        
        Returns:
            true the Field is semantically equal to zero
        
        Since:
            12.0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashcode for this date.
        
        Overrides: Object in class Object
        
        Returns:
            hashcode
        
        
        """
        ...
    def isAfter(self, other: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> bool:
        """
        Check if the instance represents a time that is strictly after another.
        
        Parameters:
            other (FieldTimeStamped<FieldAbsoluteDate> other): the instant to compare this date to
        
        Returns:
            true if the instance is strictly after the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isAfterOrEqualTo
        
        
        """
        ...
    def isAfterOrEqualTo(self, other: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> bool:
        """
        Check if the instance represents a time that is after or equal to another.
        
        Parameters:
            other (FieldTimeStamped<FieldAbsoluteDate> other): the instant to compare this date to
        
        Returns:
            true if the instance is after (or equal to) the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isAfterOrEqualTo
        
        
        """
        ...
    def isBefore(self, other: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> bool:
        """
        Check if the instance represents a time that is strictly before another.
        
        Parameters:
            other (FieldTimeStamped<FieldAbsoluteDate> other): the instant to compare this date to
        
        Returns:
            true if the instance is strictly before the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBeforeOrEqualTo
        
        
        """
        ...
    def isBeforeOrEqualTo(self, other: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> bool:
        """
        Check if the instance represents a time that is before or equal to another.
        
        Parameters:
            other (FieldTimeStamped<FieldAbsoluteDate> other): the instant to compare this date to
        
        Returns:
            true if the instance is before (or equal to) the argument when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBefore
        
        
        """
        ...
    def isBetween(self, boundary: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]], otherBoundary: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> bool:
        """
        Check if the instance represents a time that is strictly between two others representing the boundaries of a time span. The two boundaries can be provided in any order: in other words, whether boundary represents a time that is before or after otherBoundary will not change the result of this method.
        
        Parameters:
            boundary (FieldTimeStamped<FieldAbsoluteDate> boundary): one end of the time span
            otherBoundary (FieldTimeStamped<FieldAbsoluteDate> otherBoundary): the other end of the time span
        
        Returns:
            true if the instance is strictly between the two arguments when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBetweenOrEqualTo
        
        
        """
        ...
    def isBetweenOrEqualTo(self, boundary: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]], otherBoundary: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> bool:
        """
        Check if the instance represents a time that is between two others representing the boundaries of a time span, or equal to one of them. The two boundaries can be provided in any order: in other words, whether boundary represents a time that is before or after otherBoundary will not change the result of this method.
        
        Parameters:
            boundary (FieldTimeStamped<FieldAbsoluteDate> boundary): one end of the time span
            otherBoundary (FieldTimeStamped<FieldAbsoluteDate> otherBoundary): the other end of the time span
        
        Returns:
            true if the instance is between the two arguments (or equal to at least one of them) when ordering chronologically
        
        Since:
            10.1
        
        Also see:
            isBetween
        
        
        """
        ...
    def isCloseTo(self, other: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]], tolerance: float) -> bool:
        """
        Check if the instance time is close to another.
        
        Parameters:
            other (FieldTimeStamped<FieldAbsoluteDate> other): the instant to compare this date to
            tolerance (double): the separation, in seconds, under which the two instants will be considered close to each other
        
        Returns:
            true if the duration between the instance and the argument is strictly below the tolerance
        
        Since:
            10.1
        
        Also see:
            isEqualTo
        
        
        """
        ...
    def isEqualTo(self, other: typing.Union[FieldTimeStamped[_FieldAbsoluteDate__T], typing.Callable[[], 'FieldAbsoluteDate'[org.hipparchus.CalculusFieldElement]]]) -> bool:
        """
        Check if the instance represents the same time as another.
        
        Parameters:
            other (FieldTimeStamped<FieldAbsoluteDate> other): the instant to compare this date to
        
        Returns:
            true if the instance and the argument refer to the same instant
        
        Since:
            10.1
        
        Also see:
            isCloseTo
        
        
        """
        ...
    def offsetFrom(self, instant: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], timeScale: TimeScale) -> _FieldAbsoluteDate__T:
        """
        Compute the apparent clock offset between two instant in the perspective of a specific TimeScale.
        
        The offset is the number of seconds counted in the given time scale between the locations of the two instants, with all time scale irregularities removed (i.e. considering all days are exactly 86400 seconds long). This method will give a result that may not have a physical meaning if the time scale is irregular. For example since a leap second was introduced at the end of 2005, the apparent offset between 2005-12-31T23:59:59 and 2006-01-01T00:00:00 is 1 second, but the physical duration of the corresponding time interval as returned by the durationFrom method is 2 seconds.
        
        This method is the reverse of the  constructor.
        
        Parameters:
            instant (FieldAbsoluteDate<FieldAbsoluteDate> instant): instant to subtract from the instance
            timeScale (TimeScale): time scale with respect to which the offset should be computed
        
        Returns:
            apparent clock offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
        Also see:
            durationFrom, 
        
        
        """
        ...
    @typing.overload
    def parseCCSDSCalendarSegmentedTimeCode(self, byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    @typing.overload
    def parseCCSDSCalendarSegmentedTimeCode(self, byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], timeScale: TimeScale) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    _parseCCSDSDaySegmentedTimeCode_0__T = typing.TypeVar('_parseCCSDSDaySegmentedTimeCode_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _parseCCSDSDaySegmentedTimeCode_1__T = typing.TypeVar('_parseCCSDSDaySegmentedTimeCode_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(field: org.hipparchus.Field[_parseCCSDSDaySegmentedTimeCode_0__T], byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], dateComponents: DateComponents) -> 'FieldAbsoluteDate'[_parseCCSDSDaySegmentedTimeCode_0__T]:
        """
        CCSDS Day Segmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in November 2010
        
        Parameters:
            field (Field<T> field): field for the components
            preambleField (byte): field specifying the format, often not transmitted in data interfaces, as it is constant for a given data interface
            timeField (byte[]): byte array containing the time code
            agencyDefinedEpoch (DateComponents): reference epoch, ignored if the preamble field specifies the getCCSDSEpoch is
                used (and hence may be null in this case)
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            an instance corresponding to the specified date
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(field: org.hipparchus.Field[_parseCCSDSDaySegmentedTimeCode_1__T], byte: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], dateComponents: DateComponents, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_parseCCSDSDaySegmentedTimeCode_1__T]: ...
    _parseCCSDSUnsegmentedTimeCode_0__T = typing.TypeVar('_parseCCSDSUnsegmentedTimeCode_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _parseCCSDSUnsegmentedTimeCode_1__T = typing.TypeVar('_parseCCSDSUnsegmentedTimeCode_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(preambleField1: int, preambleField2: int, timeField: typing.Union[typing.List[int], jpype.JArray, bytes], agencyDefinedEpoch: 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_0__T], ccsdsEpoch: 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_0__T]) -> 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_0__T]:
        """
        CCSDS Unsegmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in November 2010
        
        If the date to be parsed is formatted using version 3 of the standard (CCSDS 301.0-B-3 published in 2002) or if the extension of the preamble field introduced in version 4 of the standard is not used, then the preambleField2 parameter can be set to 0.
        
        Parameters:
            preambleField1 (byte): first byte of the field specifying the format, often not transmitted in data interfaces, as it is constant for a given
                data interface
            preambleField2 (byte): second byte of the field specifying the format (added in revision 4 of the CCSDS standard in 2010), often not
                transmitted in data interfaces, as it is constant for a given data interface (value ignored if presence not signaled in
                preambleField1)
            timeField (byte[]): byte array containing the time code
            agencyDefinedEpoch (FieldAbsoluteDate<T> agencyDefinedEpoch): reference epoch, ignored if the preamble field specifies the CCSDS_EPOCH is used
                (and hence may be null in this case, but then ccsdsEpoch must be non-null)
            ccsdsEpoch (FieldAbsoluteDate<T> ccsdsEpoch): reference epoch, ignored if the preamble field specifies the agency epoch is used (and hence may be null in this case,
                but then agencyDefinedEpoch must be non-null).
        
        Returns:
            an instance corresponding to the specified date
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(field: org.hipparchus.Field[_parseCCSDSUnsegmentedTimeCode_1__T], byte: int, byte2: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], fieldAbsoluteDate: 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_1__T]) -> 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_1__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    @typing.overload
    def shiftedBy(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAbsoluteDate__T) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    @typing.overload
    def shiftedBy(self, timeOffset: TimeOffset) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    def timeScalesOffset(self, scale1: TimeScale, scale2: TimeScale) -> _FieldAbsoluteDate__T:
        """
        Compute the offset between two time scales at the current instant.
        
        The offset is defined as l₁-l₂ where l₁ is the location of the instant in the scale1 time scale and l₂ is the location of the instant in the scale2 time scale.
        
        Parameters:
            scale1 (TimeScale): first time scale
            scale2 (TimeScale): second time scale
        
        Returns:
            offset in seconds between the two time scales at the current instant
        
        
        """
        ...
    def toAbsoluteDate(self) -> AbsoluteDate:
        """
        Transform the FieldAbsoluteDate in an AbsoluteDate.
        
        Returns:
            AbsoluteDate of the FieldObject
        
        
        """
        ...
    def toDate(self, timeScale: TimeScale) -> java.util.Date:
        """
        Convert the instance to a Java Date.
        
        Conversion to the Date class induces a loss of precision because the Date class does not provide sub-millisecond information. Java Dates are considered to be locations in some times scales.
        
        Parameters:
            timeScale (TimeScale): time scale to use
        
        Returns:
            a Date instance representing the
            location of the instant in the time scale
        
        
        """
        ...
    def toFUD1Field(self) -> 'FieldAbsoluteDate'[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1[_FieldAbsoluteDate__T]]:
        """
        Creates Field date with offset as univariate derivative of first order, with a unit linear coefficient in time.
        
        Returns:
            univariate derivative 1 date
        
        Since:
            13.1
        
        
        """
        ...
    def toFUD2Field(self) -> 'FieldAbsoluteDate'[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldAbsoluteDate__T]]:
        """
        Creates Field date with offset as univariate derivative of second order, with a unit linear coefficient in time.
        
        Returns:
            univariate derivative 2 date
        
        Since:
            12.2
        
        
        """
        ...
    @typing.overload
    def toInstant(self) -> java.time.Instant:
        """
        Convert the instance to a Java Instant. Nanosecond precision is preserved during this conversion
        
        Returns:
            a Instant instance representing the
            location of the instant in the utc time scale
        
        Since:
            12.1
        
        """
        ...
    @typing.overload
    def toInstant(self, timeScales: TimeScales) -> java.time.Instant:
        """
        Convert the instance to a Java Instant. Nanosecond precision is preserved during this conversion
        
        Parameters:
            timeScales (TimeScales): the timescales to use
        
        Returns:
            a Instant instance representing the
            location of the instant in the utc time scale
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
        Get a String representation of the instant location with up to 16 digits of precision for the seconds value.
        
        Since this method is used in exception messages and error handling every effort is made to return some representation of the instant. If UTC is available from the default data context then it is used to format the string in UTC. If not then TAI is used. Finally if the prior attempts fail this method falls back to converting this class's internal representation to a string.
        
        This method uses the getDefault.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of the instance, in ISO-8601 format if UTC is available from the default data context.
        
        Also see:
            toString, toString,
            toString
        
        """
        ...
    @typing.overload
    def toString(self, int: int) -> str:
        """
        Get a String representation of the instant location in ISO-8601 format without the UTC offset and with up to 16 digits of precision for the seconds value.
        
        Parameters:
            timeScale (TimeScale): time scale to use
        
        Returns:
            a string representation of the instance.
        
        Also see:
            toString
        
        Get a String representation of the instant location for a local time.
        
        This method uses the getDefault.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC).
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Also see:
            toString
        
        Get a String representation of the instant location for a local time.
        
        Parameters:
            minutesFromUTC (int): offset in minutes from UTC (positive Eastwards UTC, negative Westward UTC).
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Since:
            10.1
        
        Get a String representation of the instant location for a time zone.
        
        This method uses the getDefault.
        
        Parameters:
            timeZone (TimeZone): time zone
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Also see:
            toString
        
        Get a String representation of the instant location for a time zone.
        
        Parameters:
            timeZone (TimeZone): time zone
            utc (TimeScale): time scale used to compute date and time components.
        
        Returns:
            string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, timeScale: TimeScale) -> str: ...
    @typing.overload
    def toString(self, timeZone: java.util.TimeZone) -> str: ...
    @typing.overload
    def toString(self, timeZone: java.util.TimeZone, timeScale: TimeScale) -> str: ...
    @typing.overload
    def toString(self, timeScale: TimeScale) -> str: ...
    def toStringWithoutUtcOffset(self, timeScale: TimeScale, fractionDigits: int) -> str:
        """
        Return a string representation of this date-time, rounded to the given precision.
        
        The format used is ISO8601 without the UTC offset.
        
        Parameters:
            timeScale (TimeScale): to use to compute components.
            fractionDigits (int): the number of digits to include after the decimal point in the string representation of the seconds. The date and time
                is first rounded as necessary. fractionDigits must be greater than or equal to .
        
        Returns:
            string representation of this date, time, and UTC offset
        
        Since:
            12.2
        
        Also see:
            toString, toString,
            toStringWithoutUtcOffset
        
        
        """
        ...

_FieldClockOffsetHermiteInterpolator__T = typing.TypeVar('_FieldClockOffsetHermiteInterpolator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldClockOffsetHermiteInterpolator(AbstractFieldTimeInterpolator[FieldClockOffset[_FieldClockOffsetHermiteInterpolator__T], _FieldClockOffsetHermiteInterpolator__T], typing.Generic[_FieldClockOffsetHermiteInterpolator__T]):
    """
    bHermite interpolator of time stamped clock offsets.
    
    Since:
        12.1
    
        class:`~org.orekit.time.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, TimeInterpolator
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...

class GPSScale(ConstantOffsetTimeScale):
    """
    GPS time scale.
    
    By convention, TGPS = TAI - 19 s.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    ...

class GalileoScale(ConstantOffsetTimeScale):
    """
    Galileo system time scale.
    
    By convention, TGST = UTC + 13s at Galileo epoch (1999-08-22T00:00:00Z).
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Galileo System Time and GPS time are very close scales. Without any errors, they should be identical. The offset between these two scales is the GGTO, it depends on the clocks used to realize the time scales. It is of the order of a few tens nanoseconds. This class does not implement this offset, so it is virtually identical to the GPSScale.
    
    Also see:
        AbsoluteDate
    """
    ...

class LazyLoadedTimeScales(AbstractTimeScales):
    """
    An implementation of TimeScales that loads auxiliary data, leap seconds and UT1-UTC, when it is first accessed. The list of loaders may be modified before the first data access.
    
    Since:
        10.1
    
    Also see:
        TimeScalesFactory
    """
    def __init__(self, lazyLoadedEop: org.orekit.frames.LazyLoadedEop):
        """
        Create a new set of time scales with the given sources of auxiliary data. This constructor uses the same DataProvidersManager for the default EOP loaders and the default leap second loaders.
        
        Parameters:
            lazyLoadedEop (LazyLoadedEop): loads Earth Orientation Parameters for getUT1.
        
        
        """
        ...
    def addDefaultUTCTAIOffsetsLoaders(self) -> None:
        """
        Add the default loaders for UTC-TAI offsets history files (both IERS and USNO).
        
        The default loaders are TAIUTCDatFilesLoader that looks for a file named dat that must be in USNO format, UTCTAIHistoryFilesLoader that looks for a file named history that must be in the IERS format and AGILeapSecondFilesLoader that looks for a files named dat that must be in AGI format. The UTCTAIBulletinAFilesLoader isnot added by default as it is not recommended. USNO warned us that the TAI-UTC data present in bulletin A was for convenience only and was not reliable, there have been errors in several bulletins regarding these data.
        
        Since:
            7.1
        
        Also see:
            `USNO tai-utc.dat file <http://maia.usno.navy.mil/ser7/tai-utc.dat>`, `IERS UTC-TAI.history file
            <http://hpiers.obspm.fr/eoppc/bul/bulc/UTC-TAI.history>`, TAIUTCDatFilesLoader,
            UTCTAIHistoryFilesLoader, AGILeapSecondFilesLoader,
            getUTC,
            clearUTCTAIOffsetsLoaders
        
        
        """
        ...
    def addUTCTAIOffsetsLoader(self, loader: typing.Union[UTCTAIOffsetsLoader, typing.Callable]) -> None:
        """
        Add a loader for UTC-TAI offsets history files.
        
        Parameters:
            loader (UTCTAIOffsetsLoader): custom loader to add
        
        Since:
            7.1
        
        Also see:
            TAIUTCDatFilesLoader, UTCTAIHistoryFilesLoader,
            UTCTAIBulletinAFilesLoader, getUTC,
            clearUTCTAIOffsetsLoaders
        
        
        """
        ...
    def clearUTCTAIOffsetsLoaders(self) -> None:
        """
        Clear loaders for UTC-TAI offsets history files.
        
        Since:
            7.1
        
        Also see:
            getUTC,
            addUTCTAIOffsetsLoader,
            addDefaultUTCTAIOffsetsLoaders
        
        
        """
        ...
    def getBDT(self) -> BDTScale:
        """
        Description copied from interface: getBDT Get the BeiDou Navigation Satellite System time scale.
        
        Returns:
            BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    def getGLONASS(self) -> GLONASSScale:
        """
        Description copied from interface: getGLONASS Get the GLObal NAvigation Satellite System time scale.
        
        Returns:
            GLObal NAvigation Satellite System time scale
        
        
        """
        ...
    def getGMST(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> GMSTScale:
        """
        Description copied from interface: getGMST Get the Greenwich Mean Sidereal Time scale.
        
        Specified by: getGMST in interface TimeScales
        
        Overrides: getGMST in class AbstractTimeScales
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Greenwich Mean Sidereal Time scale
        
        
        """
        ...
    def getGPS(self) -> GPSScale:
        """
        Description copied from interface: getGPS Get the Global Positioning System scale.
        
        Returns:
            Global Positioning System scale
        
        
        """
        ...
    def getGST(self) -> GalileoScale:
        """
        Description copied from interface: getGST Get the Galileo System Time scale.
        
        Returns:
            Galileo System Time scale
        
        
        """
        ...
    def getNavIC(self) -> 'NavicScale':
        """
        Description copied from interface: getNavIC Get the Navigation with Indian Constellation time scale.
        
        Returns:
            Navigation with Indian Constellation time scale
        
        
        """
        ...
    def getQZSS(self) -> 'QZSSScale':
        """
        Description copied from interface: getQZSS Get the Quasi-Zenith Satellite System time scale.
        
        Returns:
            Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    def getTAI(self) -> 'TAIScale':
        """
        Description copied from interface: getTAI Get the International Atomic Time scale.
        
        Returns:
            International Atomic Time scale
        
        
        """
        ...
    def getTCB(self) -> TCBScale:
        """
        Description copied from interface: getTCB Get the Barycentric Coordinate Time scale.
        
        Returns:
            Barycentric Coordinate Time scale
        
        
        """
        ...
    def getTCG(self) -> TCGScale:
        """
        Description copied from interface: getTCG Get the Geocentric Coordinate Time scale.
        
        Returns:
            Geocentric Coordinate Time scale
        
        
        """
        ...
    def getTDB(self) -> TDBScale:
        """
        Description copied from interface: getTDB Get the Barycentric Dynamic Time scale.
        
        Returns:
            Barycentric Dynamic Time scale
        
        
        """
        ...
    def getTT(self) -> 'TTScale':
        """
        Description copied from interface: getTT Get the Terrestrial Time scale.
        
        Returns:
            Terrestrial Time scale
        
        
        """
        ...
    @typing.overload
    def getUT1(self, eOPHistory: org.orekit.frames.EOPHistory) -> UT1Scale:
        """
        Description copied from interface: getUT1 Get the Universal Time 1 scale.
        
        Specified by: getUT1 in interface TimeScales
        
        Overrides: getUT1 in class AbstractTimeScales
        
        Parameters:
            conventions (IERSConventions): IERS conventions for which EOP parameters will provide dUT1
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Universal Time 1 scale
        
        Also see:
            getUTC, getEOPHistory
        
        Get the Universal Time 1 scale.
        
        As this method allow associating any history with the time scale, it may involve large data sets. So this method does not cache the resulting UT1Scale instance, a new instance will be returned each time. In order to avoid wasting memory, calling getUT1 with the single enumerate corresponding to the conventions may be a better solution. This method is made available only for expert use.
        
        Overrides: getUT1 in class AbstractTimeScales
        
        Parameters:
            history (EOPHistory): EOP parameters providing dUT1 (may be null if no correction is desired)
        
        Returns:
            Universal Time 1 scale
        
        Also see:
            getUT1
        
        
        """
        ...
    @typing.overload
    def getUT1(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> UT1Scale: ...
    def getUTC(self) -> UTCScale:
        """
        Description copied from interface: getUTC Get the Universal Time Coordinate scale.
        
        Returns:
            Universal Time Coordinate scale
        
        
        """
        ...

class NavicScale(ConstantOffsetTimeScale):
    """
    NavIC time scale (also called IRNWT for IRNSS NetWork Time).
    
    By convention, TNAVIC = TAI - 19 s.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    ...

class PythonAbstractTimeScales(AbstractTimeScales):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBDT(self) -> BDTScale:
        """
        Get the BeiDou Navigation Satellite System time scale.
        
        Returns:
            BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    def getEopHistory(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> org.orekit.frames.EOPHistory:
        """
        Get the EOP history for the given conventions.
        
        Specified by: getEopHistory in class AbstractTimeScales
        
        Parameters:
            conventions (IERSConventions): to use in computing the EOP history.
            simpleEOP (boolean): whether to ignore some small tidal effects.
        
        Returns:
            EOP history.
        
        
        """
        ...
    def getGLONASS(self) -> GLONASSScale:
        """
        Get the GLObal NAvigation Satellite System time scale.
        
        Returns:
            GLObal NAvigation Satellite System time scale
        
        
        """
        ...
    def getGPS(self) -> GPSScale:
        """
        Get the Global Positioning System scale.
        
        Returns:
            Global Positioning System scale
        
        
        """
        ...
    def getGST(self) -> GalileoScale:
        """
        Get the Galileo System Time scale.
        
        Returns:
            Galileo System Time scale
        
        
        """
        ...
    def getNavIC(self) -> NavicScale:
        """
        Get the Navigation with Indian Constellation time scale.
        
        Returns:
            Navigation with Indian Constellation time scale
        
        
        """
        ...
    def getQZSS(self) -> 'QZSSScale':
        """
        Get the Quasi-Zenith Satellite System time scale.
        
        Returns:
            Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    def getTAI(self) -> 'TAIScale':
        """
        Get the International Atomic Time scale.
        
        Returns:
            International Atomic Time scale
        
        
        """
        ...
    def getTCB(self) -> TCBScale:
        """
        Get the Barycentric Coordinate Time scale.
        
        Returns:
            Barycentric Coordinate Time scale
        
        
        """
        ...
    def getTCG(self) -> TCGScale:
        """
        Get the Geocentric Coordinate Time scale.
        
        Returns:
            Geocentric Coordinate Time scale
        
        
        """
        ...
    def getTDB(self) -> TDBScale:
        """
        Get the Barycentric Dynamic Time scale.
        
        Returns:
            Barycentric Dynamic Time scale
        
        
        """
        ...
    def getTT(self) -> 'TTScale':
        """
        Get the Terrestrial Time scale.
        
        Returns:
            Terrestrial Time scale
        
        
        """
        ...
    @typing.overload
    def getUT1(self, history: org.orekit.frames.EOPHistory) -> UT1Scale:
        """
        Get the Universal Time 1 scale.
        
        As this method allow associating any history with the time scale, it may involve large data sets. So this method does not cache the resulting UT1Scale instance, a new instance will be returned each time. In order to avoid wasting memory, calling getUT1 with the single enumerate corresponding to the conventions may be a better solution. This method is made available only for expert use.
        
        Overrides: getUT1 in class AbstractTimeScales
        
        Parameters:
            history (EOPHistory): EOP parameters providing dUT1 (may be null if no correction is desired)
        
        Returns:
            Universal Time 1 scale
        
        Also see:
            getUT1
        
        
        """
        ...
    @typing.overload
    def getUT1(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> UT1Scale: ...
    def getUTC(self) -> UTCScale:
        """
        Get the Universal Time Coordinate scale.
        
        Returns:
            Universal Time Coordinate scale
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

_PythonFieldTimeShiftable__T = typing.TypeVar('_PythonFieldTimeShiftable__T', bound=FieldTimeShiftable)  # <T>
_PythonFieldTimeShiftable__KK = typing.TypeVar('_PythonFieldTimeShiftable__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class PythonFieldTimeShiftable(FieldTimeShiftable[_PythonFieldTimeShiftable__T, _PythonFieldTimeShiftable__KK], typing.Generic[_PythonFieldTimeShiftable__T, _PythonFieldTimeShiftable__KK]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: TimeOffset) -> _PythonFieldTimeShiftable__T:
        """
        Get a time-shifted instance.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        Get a time-shifted instance. Calls the ShiftedByType Python extension method
        
        Specified by: shiftedBy in interface FieldTimeShiftable
        
        Parameters:
            dt (PythonFieldTimeShiftable): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> _PythonFieldTimeShiftable__T: ...
    @typing.overload
    def shiftedBy(self, kK: _PythonFieldTimeShiftable__KK) -> _PythonFieldTimeShiftable__T: ...

class QZSSScale(ConstantOffsetTimeScale):
    """
    QZSS time scale.
    
    By convention, TQZSS = TAI - 19 s.
    
    The time scale is defined in ` Quasi-Zenith Satellite System Navigation Service - Interface Specification for QZSS <http://qzss.go.jp/en/technical/download/pdf/ps-is-qzss/is-qzss-pnt-003.pdf?t=1549268771755>` version 1.6, 2014.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    ...

class TAIScale(ConstantOffsetTimeScale):
    """
    International Atomic Time.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    ...

class TTScale(ConstantOffsetTimeScale):
    """
    Terrestrial Time as defined by IAU(1991) recommendation IV.
    
    Coordinate time at the surface of the Earth. IT is the successor of Ephemeris Time TE.
    
    By convention, TT = TAI + 32.184 s.
    
    This is intended to be accessed thanks to TimeScales, so there is no public constructor.
    
    Also see:
        AbsoluteDate
    """
    ...

class TimeStampedDoubleAndDerivative(TimeStampedDouble):
    """
    Class that associates a double, its time derivative with a date.
    
    Since:
        12.1
    """
    @typing.overload
    def __init__(self, double: float, double2: float, absoluteDate: AbsoluteDate): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, double: float, double2: float): ...
    def getDerivative(self) -> float:
        """
        Get time derivative.
        
        Returns:
            time derivative
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: toString in class TimeStampedDouble
        
        
        """
        ...

class TimeStampedDoubleAndDerivativeHermiteInterpolator(AbstractTimeInterpolator[TimeStampedDoubleAndDerivative]):
    """
    Hermite interpolator of time stamped double value.
    
        class:`~org.orekit.time.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, TimeInterpolator
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...

class TimeStampedDoubleHermiteInterpolator(AbstractTimeInterpolator[TimeStampedDouble]):
    """
    Hermite interpolator of time stamped double value.
    
        class:`~org.orekit.time.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, TimeInterpolator
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...

_TimeStampedFieldHermiteInterpolator__KK = typing.TypeVar('_TimeStampedFieldHermiteInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class TimeStampedFieldHermiteInterpolator(AbstractFieldTimeInterpolator[TimeStampedField[_TimeStampedFieldHermiteInterpolator__KK], _TimeStampedFieldHermiteInterpolator__KK], typing.Generic[_TimeStampedFieldHermiteInterpolator__KK]):
    """
    Hermite interpolator of time stamped field value.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
        class:`~org.orekit.time.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.FieldHermiteInterpolator?is`, FieldTimeInterpolator
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.time")``.

    AGILeapSecondFilesLoader: typing.Type[AGILeapSecondFilesLoader]
    AbsoluteDate: typing.Type[AbsoluteDate]
    AbstractFieldTimeInterpolator: typing.Type[AbstractFieldTimeInterpolator]
    AbstractTimeInterpolator: typing.Type[AbstractTimeInterpolator]
    AbstractTimeScales: typing.Type[AbstractTimeScales]
    AggregatedClockModel: typing.Type[AggregatedClockModel]
    BDTScale: typing.Type[BDTScale]
    BurstSelector: typing.Type[BurstSelector]
    ChronologicalComparator: typing.Type[ChronologicalComparator]
    ClockModel: typing.Type[ClockModel]
    ClockOffset: typing.Type[ClockOffset]
    ClockOffsetHermiteInterpolator: typing.Type[ClockOffsetHermiteInterpolator]
    ClockTimeScale: typing.Type[ClockTimeScale]
    ConstantOffsetTimeScale: typing.Type[ConstantOffsetTimeScale]
    DateComponents: typing.Type[DateComponents]
    DateTimeComponents: typing.Type[DateTimeComponents]
    DatesSelector: typing.Type[DatesSelector]
    FieldAbsoluteDate: typing.Type[FieldAbsoluteDate]
    FieldChronologicalComparator: typing.Type[FieldChronologicalComparator]
    FieldClockOffset: typing.Type[FieldClockOffset]
    FieldClockOffsetHermiteInterpolator: typing.Type[FieldClockOffsetHermiteInterpolator]
    FieldTimeInterpolator: typing.Type[FieldTimeInterpolator]
    FieldTimeShiftable: typing.Type[FieldTimeShiftable]
    FieldTimeStamped: typing.Type[FieldTimeStamped]
    FieldTimeStampedPair: typing.Type[FieldTimeStampedPair]
    FixedStepSelector: typing.Type[FixedStepSelector]
    GLONASSDate: typing.Type[GLONASSDate]
    GLONASSScale: typing.Type[GLONASSScale]
    GMSTScale: typing.Type[GMSTScale]
    GNSSDate: typing.Type[GNSSDate]
    GPSScale: typing.Type[GPSScale]
    GalileoScale: typing.Type[GalileoScale]
    LazyLoadedTimeScales: typing.Type[LazyLoadedTimeScales]
    Month: typing.Type[Month]
    NavicScale: typing.Type[NavicScale]
    OffsetModel: typing.Type[OffsetModel]
    PerfectClockModel: typing.Type[PerfectClockModel]
    PythonAbstractTimeScales: typing.Type[PythonAbstractTimeScales]
    PythonClockModel: typing.Type[PythonClockModel]
    PythonDatesSelector: typing.Type[PythonDatesSelector]
    PythonFieldTimeInterpolator: typing.Type[PythonFieldTimeInterpolator]
    PythonFieldTimeShiftable: typing.Type[PythonFieldTimeShiftable]
    PythonFieldTimeStamped: typing.Type[PythonFieldTimeStamped]
    PythonParser: typing.Type[PythonParser]
    PythonTimeInterpolator: typing.Type[PythonTimeInterpolator]
    PythonTimeInterval: typing.Type[PythonTimeInterval]
    PythonTimeScalarFunction: typing.Type[PythonTimeScalarFunction]
    PythonTimeScale: typing.Type[PythonTimeScale]
    PythonTimeScales: typing.Type[PythonTimeScales]
    PythonTimeShiftable: typing.Type[PythonTimeShiftable]
    PythonTimeStamped: typing.Type[PythonTimeStamped]
    PythonTimeVectorFunction: typing.Type[PythonTimeVectorFunction]
    PythonUTCTAIOffsetsLoader: typing.Type[PythonUTCTAIOffsetsLoader]
    QZSSScale: typing.Type[QZSSScale]
    SampledClockModel: typing.Type[SampledClockModel]
    SatelliteClockScale: typing.Type[SatelliteClockScale]
    TAIScale: typing.Type[TAIScale]
    TAIUTCDatFilesLoader: typing.Type[TAIUTCDatFilesLoader]
    TCBScale: typing.Type[TCBScale]
    TCGScale: typing.Type[TCGScale]
    TDBScale: typing.Type[TDBScale]
    TTScale: typing.Type[TTScale]
    TimeComponents: typing.Type[TimeComponents]
    TimeInterpolator: typing.Type[TimeInterpolator]
    TimeInterval: typing.Type[TimeInterval]
    TimeOffset: typing.Type[TimeOffset]
    TimeScalarFunction: typing.Type[TimeScalarFunction]
    TimeScale: typing.Type[TimeScale]
    TimeScales: typing.Type[TimeScales]
    TimeScalesFactory: typing.Type[TimeScalesFactory]
    TimeShiftable: typing.Type[TimeShiftable]
    TimeStamped: typing.Type[TimeStamped]
    TimeStampedDouble: typing.Type[TimeStampedDouble]
    TimeStampedDoubleAndDerivative: typing.Type[TimeStampedDoubleAndDerivative]
    TimeStampedDoubleAndDerivativeHermiteInterpolator: typing.Type[TimeStampedDoubleAndDerivativeHermiteInterpolator]
    TimeStampedDoubleHermiteInterpolator: typing.Type[TimeStampedDoubleHermiteInterpolator]
    TimeStampedField: typing.Type[TimeStampedField]
    TimeStampedFieldHermiteInterpolator: typing.Type[TimeStampedFieldHermiteInterpolator]
    TimeStampedPair: typing.Type[TimeStampedPair]
    TimeVectorFunction: typing.Type[TimeVectorFunction]
    UT1Scale: typing.Type[UT1Scale]
    UTCScale: typing.Type[UTCScale]
    UTCTAIBulletinAFilesLoader: typing.Type[UTCTAIBulletinAFilesLoader]
    UTCTAIHistoryFilesLoader: typing.Type[UTCTAIHistoryFilesLoader]
    UTCTAIOffset: typing.Type[UTCTAIOffset]
    UTCTAIOffsetsLoader: typing.Type[UTCTAIOffsetsLoader]
