import java.io
import java.lang
import java.util
import java.util.function
import java.util.stream
import org.hipparchus
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss
import org.orekit.utils
import typing



class ChronologicalComparator(java.util.Comparator['TimeStamped'], java.io.Serializable):
    """
    public class ChronologicalComparator extends Object implements Comparator<:class:`~org.orekit.time.TimeStamped`>, Serializable
    
        Comparator for :class:`~org.orekit.time.TimeStamped` instance.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :class:`~org.orekit.time.TimeStamped`, :meth:`~serialized`
    """
    def __init__(self): ...
    def compare(self, timeStamped: 'TimeStamped', timeStamped2: 'TimeStamped') -> int:
        """
            Compare two time-stamped instances.
        
            Specified by:
                 in interface 
        
            Parameters:
                timeStamped1 (:class:`~org.orekit.time.TimeStamped`): first time-stamped instance
                timeStamped2 (:class:`~org.orekit.time.TimeStamped`): second time-stamped instance
        
            Returns:
                a negative integer, zero, or a positive integer as the first instance is before, simultaneous, or after the second one.
        
        
        """
        ...

class DateComponents(java.io.Serializable, java.lang.Comparable['DateComponents']):
    """
    public class DateComponents extends Object implements Serializable, Comparable<:class:`~org.orekit.time.DateComponents`>
    
        Class representing a date broken up as year, month and day components.
    
        This class uses the astronomical convention for calendars, which is also the convention used by :code:`java.util.Date`:
        a year zero is present between years -1 and +1, and 10 days are missing in 1582. The calendar used around these special
        dates are:
    
          - up to 0000-12-31 : proleptic julian calendar
          - from 0001-01-01 to 1582-10-04: julian calendar
          - from 1582-10-15: gregorian calendar
    
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.time.TimeComponents`, :class:`~org.orekit.time.DateTimeComponents`, :meth:`~serialized`
    """
    JULIAN_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` JULIAN_EPOCH
    
        Reference epoch for julian dates: -4712-01-01.
    
        Both :code:`java.util.Date` and :class:`~org.orekit.time.DateComponents` classes follow the astronomical conventions and
        consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be
        seen in other documents or programs that obey a different convention (for example the :code:`convcal` utility).
    
    """
    MODIFIED_JULIAN_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` MODIFIED_JULIAN_EPOCH
    
        Reference epoch for modified julian dates: 1858-11-17.
    
    """
    FIFTIES_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` FIFTIES_EPOCH
    
        Reference epoch for 1950 dates: 1950-01-01.
    
    """
    CCSDS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` CCSDS_EPOCH
    
        Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01.
    
    """
    GALILEO_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` GALILEO_EPOCH
    
        Reference epoch for Galileo System Time: 1999-08-22.
    
    """
    GPS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` GPS_EPOCH
    
        Reference epoch for GPS weeks: 1980-01-06.
    
    """
    QZSS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` QZSS_EPOCH
    
        Reference epoch for QZSS weeks: 1980-01-06.
    
    """
    IRNSS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` IRNSS_EPOCH
    
        Reference epoch for IRNSS weeks: 1999-08-22.
    
    """
    BEIDOU_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` BEIDOU_EPOCH
    
        Reference epoch for BeiDou weeks: 2006-01-01.
    
    """
    GLONASS_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` GLONASS_EPOCH
    
        Reference epoch for GLONASS four-year interval number: 1996-01-01.
    
    """
    J2000_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` J2000_EPOCH
    
        J2000.0 Reference epoch: 2000-01-01.
    
    """
    JAVA_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` JAVA_EPOCH
    
        Java Reference epoch: 1970-01-01.
    
    """
    MAX_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` MAX_EPOCH
    
        Maximum supported date.
    
        This is date 5881610-07-11 which corresponds to :code:`Integer.MAX_VALUE` days after
        :meth:`~org.orekit.time.DateComponents.J2000_EPOCH`.
    
        Since:
            9.0
    
    
    """
    MIN_EPOCH: typing.ClassVar['DateComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateComponents` MIN_EPOCH
    
        Maximum supported date.
    
        This is date -5877490-03-03, which corresponds to :code:`Integer.MIN_VALUE` days before
        :meth:`~org.orekit.time.DateComponents.J2000_EPOCH`.
    
        Since:
            9.0
    
    
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
        
            Specified by:
                 in interface 
        
        
        """
        ...
    @staticmethod
    def createFromWeekComponents(int: int, int2: int, int3: int) -> 'DateComponents': ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getCalendarWeek(self) -> int:
        """
            Get the calendar week number.
        
            The calendar week number is a number between 1 and 52 or 53 depending on the year. Week 1 is defined by ISO as the one
            that includes the first Thursday of a year. Week 1 may therefore start the previous year and week 52 or 53 may end in
            the next year. As an example calendar date 1995-01-01 corresponds to week date 1994-W52-7 (i.e. Sunday in the last week
            of 1994 is in fact the first day of year 1995). Another example is calendar date 1996-12-31 which corresponds to week
            date 1997-W01-2 (i.e. Tuesday in the first week of 1997 is in fact the last day of year 1996).
        
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
        
            Overrides:
                 in class 
        
        
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
        
        
            As shown by the list above, only the complete representations defined in section 4.1 of ISO-8601 standard are supported,
            neither expended representations nor representations with reduced accuracy are supported.
        
            Parsing a single integer as a julian day is *not* supported as it may be ambiguous with either the basic format calendar
            date or the basic format ordinal date depending on the number of digits.
        
            Parameters:
                string (String): string to parse
        
            Returns:
                a parsed date
        
            Raises:
                : if string cannot be parsed
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a string representation (ISO-8601) of the date.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of the date.
        
        
        """
        ...

class DateTimeComponents(java.io.Serializable, java.lang.Comparable['DateTimeComponents']):
    """
    public class DateTimeComponents extends Object implements Serializable, Comparable<:class:`~org.orekit.time.DateTimeComponents`>
    
        Holder for date and time components.
    
        This class is a simple holder with no processing methods.
    
        Instance of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :class:`~org.orekit.time.DateComponents`,
            :class:`~org.orekit.time.TimeComponents`, :meth:`~serialized`
    """
    JULIAN_EPOCH: typing.ClassVar['DateTimeComponents'] = ...
    """
    public static final :class:`~org.orekit.time.DateTimeComponents` JULIAN_EPOCH
    
        The Julian Epoch.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getJulianEpoch`
    
    
    """
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, month: 'Month', int2: int): ...
    @typing.overload
    def __init__(self, int: int, month: 'Month', int2: int, int3: int, int4: int, double: float): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, timeComponents: 'TimeComponents'): ...
    @typing.overload
    def __init__(self, dateTimeComponents: 'DateTimeComponents', double: float): ...
    def compareTo(self, dateTimeComponents: 'DateTimeComponents') -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
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
        
            Overrides:
                 in class 
        
        
        """
        ...
    def offsetFrom(self, dateTimeComponents: 'DateTimeComponents') -> float:
        """
            Compute the seconds offset between two instances.
        
            Parameters:
                dateTime (:class:`~org.orekit.time.DateTimeComponents`): dateTime to subtract from the instance
        
            Returns:
                offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
            Also see:
                :meth:`~org.orekit.time.DateTimeComponents.DateTimeComponents`
        
        
        """
        ...
    @staticmethod
    def parseDateTime(string: str) -> 'DateTimeComponents':
        """
            Parse a string in ISO-8601 format to build a date/time.
        
            The supported formats are all date formats supported by :meth:`~org.orekit.time.DateComponents.parseDate` and all time
            formats supported by :meth:`~org.orekit.time.TimeComponents.parseTime` separated by the standard time separator 'T', or
            date components only (in which case a 00:00:00 hour is implied). Typical examples are 2000-01-01T12:00:00Z or
            1976W186T210000.
        
            Parameters:
                string (String): string to parse
        
            Returns:
                a parsed date/time
        
            Raises:
                : if string cannot be parsed
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Return a string representation of this pair.
        
            The format used is ISO8601 including the UTC offset.
        
            Overrides:
                 in class 
        
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
                :meth:`~org.orekit.time.DateTimeComponents.toString`
        
            Return a string representation of this date-time, rounded to the given precision.
        
            The format used is ISO8601 including the UTC offset.
        
            Parameters:
                minuteDuration (int): 59, 60, 61, or 62 seconds depending on the date being close to a leap second introduction and the magnitude of the leap
                    second.
                fractionDigits (int): the number of digits to include after the decimal point in the string representation of the seconds. The date and time
                    is first rounded as necessary. :code:`fractionDigits` must be greater than or equal to :code:`0`.
        
            Returns:
                string representation of this date, time, and UTC offset
        
            Since:
                11.0
        
            Also see:
                :meth:`~org.orekit.time.DateTimeComponents.toStringRfc3339`,
                :meth:`~org.orekit.time.DateTimeComponents.toStringWithoutUtcOffset`,
                :meth:`~org.orekit.time.DateTimeComponents.toStringWithoutUtcOffset`
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, int2: int) -> str: ...
    def toStringRfc3339(self) -> str:
        """
            Represent the given date and time as a string according to the format in RFC 3339. RFC3339 is a restricted subset of ISO
            8601 with a well defined grammar. This method includes enough precision to represent the point in time without rounding
            up to the next minute.
        
            RFC3339 is unable to represent BC years, years of 10000 or more, time zone offsets of 100 hours or more, or NaN. In
            these cases the value returned from this method will not be valid RFC3339 format.
        
            Returns:
                RFC 3339 format string.
        
            Also see:
                RFC 3339, :meth:`~org.orekit.time.AbsoluteDate.toStringRfc3339`, :meth:`~org.orekit.time.DateTimeComponents.toString`,
                :meth:`~org.orekit.time.DateTimeComponents.toStringWithoutUtcOffset`
        
        
        """
        ...
    @typing.overload
    def toStringWithoutUtcOffset(self) -> str:
        """
            Get a string representation of the date-time without the offset from UTC. The format used is ISO6801, except without the
            offset from UTC.
        
            Returns:
                a string representation of the date-time.
        
            Also see:
                :meth:`~org.orekit.time.DateTimeComponents.toStringWithoutUtcOffset`,
                :meth:`~org.orekit.time.DateTimeComponents.toString`, :meth:`~org.orekit.time.DateTimeComponents.toStringRfc3339`
        
        """
        ...
    @typing.overload
    def toStringWithoutUtcOffset(self, int: int, int2: int) -> str:
        """
            Return a string representation of this date-time, rounded to the given precision.
        
            The format used is ISO8601 without the UTC offset.
        
            Parameters:
                minuteDuration (int): 59, 60, 61, or 62 seconds depending on the date being close to a leap second introduction and the magnitude of the leap
                    second.
                fractionDigits (int): the number of digits to include after the decimal point in the string representation of the seconds. The date and time
                    is first rounded as necessary. :code:`fractionDigits` must be greater than or equal to :code:`0`.
        
            Returns:
                string representation of this date, time, and UTC offset
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.time.DateTimeComponents.toStringRfc3339`,
                :meth:`~org.orekit.time.DateTimeComponents.toStringWithoutUtcOffset`,
                :meth:`~org.orekit.time.DateTimeComponents.toString`
        
        
        """
        ...

class DatesSelector:
    """
    public interface DatesSelector
    
        Interface for selecting dates within an interval.
    
        This interface is mainly useful for :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`
        measurements :class:`~org.orekit.estimation.measurements.generation.Generator`.
    
        Since:
            9.3
    
        Also see:
            :class:`~org.orekit.estimation.measurements.generation.AbstractScheduler`,
            :class:`~org.orekit.estimation.measurements.generation.Generator`
    """
    def selectDates(self, absoluteDate: 'AbsoluteDate', absoluteDate2: 'AbsoluteDate') -> java.util.List['AbsoluteDate']: ...

_FieldTimeInterpolable__T = typing.TypeVar('_FieldTimeInterpolable__T', bound='FieldTimeInterpolable')  # <T>
_FieldTimeInterpolable__KK = typing.TypeVar('_FieldTimeInterpolable__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldTimeInterpolable(typing.Generic[_FieldTimeInterpolable__T, _FieldTimeInterpolable__KK]):
    """
    public interface FieldTimeInterpolable<T extends FieldTimeInterpolable<T,KK>,KK extends CalculusFieldElement<KK>>
    
        This interface represents objects that can be interpolated in time.
    """
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldTimeInterpolable__KK], stream: java.util.stream.Stream[_FieldTimeInterpolable__T]) -> _FieldTimeInterpolable__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldTimeInterpolable__KK], collection: typing.Union[java.util.Collection[_FieldTimeInterpolable__T], typing.Sequence[_FieldTimeInterpolable__T], typing.Set[_FieldTimeInterpolable__T]]) -> _FieldTimeInterpolable__T: ...

_FieldTimeShiftable__T = typing.TypeVar('_FieldTimeShiftable__T', bound=FieldTimeInterpolable)  # <T>
_FieldTimeShiftable__KK = typing.TypeVar('_FieldTimeShiftable__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldTimeShiftable(typing.Generic[_FieldTimeShiftable__T, _FieldTimeShiftable__KK]):
    """
    public interface FieldTimeShiftable<T extends :class:`~org.orekit.time.FieldTimeInterpolable`<T,KK>,KK extends CalculusFieldElement<KK>>
    
        This interface represents objects that can be shifted in time.
    
        Since:
            9.0
    """
    @typing.overload
    def shiftedBy(self, double: float) -> _FieldTimeShiftable__T:
        """
            Get a time-shifted instance.
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
            Get a time-shifted instance.
        
            Parameters:
                dt (:class:`~org.orekit.time.FieldTimeShiftable`): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, kK: _FieldTimeShiftable__KK) -> _FieldTimeShiftable__T: ...

_FieldTimeStamped__T = typing.TypeVar('_FieldTimeStamped__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTimeStamped(typing.Generic[_FieldTimeStamped__T]):
    """
    public interface FieldTimeStamped<T extends CalculusFieldElement<T>>
    
        This interface represents objects that have a :class:`~org.orekit.time.AbsoluteDate` date attached to them.
    
        Classes implementing this interface can be stored chronologically in sorted sets using
        :class:`~org.orekit.time.ChronologicalComparator` as the underlying comparator. An example using for
        :class:`~org.orekit.orbits.Orbit` instances is given here:
    
        .. code-block: java
        
        
             SortedSet<Orbit> sortedOrbits =
                 new TreeSet<Orbit>(new ChronologicalComparator());
             sortedOrbits.add(orbit1);
             sortedOrbits.add(orbit2);
             ...
         
    
        This interface is also the base interface used to :class:`~org.orekit.utils.TimeStampedCache` series of time-dependent
        objects for interpolation in a thread-safe manner.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :class:`~org.orekit.time.ChronologicalComparator`,
            :class:`~org.orekit.utils.TimeStampedCache`
    """
    def getDate(self) -> 'FieldAbsoluteDate'[_FieldTimeStamped__T]: ...

class Month(java.lang.Enum['Month']):
    """
    public enum Month extends Enum<:class:`~org.orekit.time.Month`>
    
        Enumerate representing a calendar month.
    
        This enum is mainly useful to parse data files that use month names like Jan or JAN or January or numbers like 1 or 01.
        It handles month numbers as well as three letters abbreviation and full names, independently of capitalization.
    
        Also see:
            :class:`~org.orekit.time.DateComponents`
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
    def getMonth(int: int) -> 'Month':
        """
            Get the month corresponding to a number.
        
            Parameters:
                number (int): month number
        
            Returns:
                the month corresponding to the string
        
            Raises:
                : if the string does not correspond to a month
        
        
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
    def parseMonth(string: str) -> 'Month':
        """
            Parse the string to get the month.
        
            The string can be either the month number, the full name or the three letter abbreviation. The parsing ignore the case
            of the specified string and trims surrounding blanks.
        
            Parameters:
                s (String): string to parse
        
            Returns:
                the month corresponding to the string
        
            Raises:
                : if the string does not correspond to a month
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Month':
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
    def values() -> typing.List['Month']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (Month c : Month.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OffsetModel:
    """
    public class OffsetModel extends Object
    
        TAI UTC offset model.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.time.UTCTAIOffsetsLoader`
    """
    @typing.overload
    def __init__(self, dateComponents: DateComponents, int: int): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, int: int, double: float, double2: float): ...
    def getMJDRef(self) -> int:
        """
            Get the reference date of the linear model as a modified julian day.
        
            Returns:
                reference date of the linear model as a modified julian day
        
        
        """
        ...
    def getOffset(self) -> float:
        """
            Offset at reference date in seconds (TAI minus UTC).
        
            Returns:
                offset at reference date in seconds (TAI minus UTC)
        
        
        """
        ...
    def getSlope(self) -> float:
        """
            Offset slope in seconds per UTC day (TAI minus UTC / dUTC).
        
            Returns:
                offset slope in seconds per UTC day (TAI minus UTC / dUTC)
        
        
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
    public class TimeComponents extends Object implements Serializable, Comparable<:class:`~org.orekit.time.TimeComponents`>
    
        Class representing a time within the day broken up as hour, minute and second components.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.time.DateComponents`, :class:`~org.orekit.time.DateTimeComponents`, :meth:`~serialized`
    """
    H00: typing.ClassVar['TimeComponents'] = ...
    """
    public static final :class:`~org.orekit.time.TimeComponents` H00
    
        Constant for commonly used hour 00:00:00.
    
    """
    H12: typing.ClassVar['TimeComponents'] = ...
    """
    public static final :class:`~org.orekit.time.TimeComponents` H12
    
        Constant for commonly used hour 12:00:00.
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, int3: int): ...
    def compareTo(self, timeComponents: 'TimeComponents') -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def formatUtcOffset(self) -> str:
        """
            Get the UTC offset as a string in ISO8601 format. For example, :code:`+00:00`.
        
            Returns:
                the UTC offset as a string.
        
            Also see:
                :meth:`~org.orekit.time.TimeComponents.toStringWithoutUtcOffset`, :meth:`~org.orekit.time.TimeComponents.toString`
        
        
        """
        ...
    @staticmethod
    def fromSeconds(int: int, double: float, double2: float, int2: int) -> 'TimeComponents':
        """
            Build a time from the second number within the day.
        
            The seconds past midnight is the sum :code:`secondInDayA + secondInDayB + leap`. The two parameters are used for
            increased accuracy. Only the first part of the sum (:code:`secondInDayA + secondInDayB`) is used to compute the hours
            and minutes. The third parameter (:code:`leap`) is added directly to the second value
            (:meth:`~org.orekit.time.TimeComponents.getSecond`) to implement leap seconds. These three quantities must satisfy the
            following constraints. This first guarantees the hour and minute are valid, the second guarantees the second is valid.
        
            .. code-block: java
            
            
                  0 <= secondInDayA + secondInDayB < 86400
                 :code:`0 <= (secondInDayA + secondInDayB) % 60 + leap <= minuteDuration`
                 :code:`0 <= leap <= minuteDuration - 60                        if minuteDuration >= 60`
                 :code:`0 >= leap >= minuteDuration - 60                        if minuteDuration <  60`
             
        
            If the seconds of minute (:meth:`~org.orekit.time.TimeComponents.getSecond`) computed from :code:`secondInDayA +
            secondInDayB + leap` is greater than or equal to :code:`60 + leap` then the second of minute will be set to
            :code:`FastMath.nextDown(60 + leap)`. This prevents rounding to an invalid seconds of minute number when the input
            values have greater precision than a :code:`double`.
        
            This constructor is always in UTC (i.e. :meth:`~org.orekit.time.TimeComponents.getMinutesFromUTC`).
        
            If :code:`secondsInDayB` or :code:`leap` is NaN then the hour and minute will be determined from :code:`secondInDayA`
            and the second of minute will be NaN.
        
            Parameters:
                secondInDayA (int): first part of the second number.
                secondInDayB (double): last part of the second number.
                leap (double): magnitude of the leap second if this point in time is during a leap second, otherwise :code:`0.0`. This value is not
                    used to compute hours and minutes, but it is added to the computed second of minute.
                minuteDuration (int): number of seconds in the current minute, normally :code:`60`.
        
            Returns:
                new time components for the specified time.
        
            Raises:
                :class:`~org.orekit.errors.OrekitIllegalArgumentException`: if the inequalities above do not hold.
        
            Since:
                10.2
        
        
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
            Get the second number within the local day, *without* applying the
            :meth:`~org.orekit.time.TimeComponents.getMinutesFromUTC`.
        
            Returns:
                second number from 0.0 to Constants.JULIAN_DAY
        
            Since:
                7.2
        
            Also see:
                :meth:`~org.orekit.time.TimeComponents.getSecondsInUTCDay`
        
        
        """
        ...
    def getSecondsInUTCDay(self) -> float:
        """
            Get the second number within the UTC day, applying the :meth:`~org.orekit.time.TimeComponents.getMinutesFromUTC`.
        
            Returns:
                second number from :meth:`~org.orekit.time.TimeComponents.getMinutesFromUTC` to Constants.JULIAN_DAY
                :meth:`~org.orekit.time.TimeComponents.getMinutesFromUTC`
        
            Since:
                7.2
        
            Also see:
                :meth:`~org.orekit.time.TimeComponents.getSecondsInLocalDay`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
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
        
        
            As shown by the list above, only the complete representations defined in section 4.2 of ISO-8601 standard are supported,
            neither expended representations nor representations with reduced accuracy are supported.
        
            Parameters:
                string (String): string to parse
        
            Returns:
                a parsed time
        
            Raises:
                : if string cannot be parsed
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a string representation of the time including the offset from UTC.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of the time in an ISO 8601 like format including the UTC offset.
        
            Also see:
                :meth:`~org.orekit.time.TimeComponents.toStringWithoutUtcOffset`,
                :meth:`~org.orekit.time.TimeComponents.formatUtcOffset`
        
        
        """
        ...
    def toStringWithoutUtcOffset(self) -> str:
        """
            Get a string representation of the time without the offset from UTC.
        
            Returns:
                a string representation of the time in an ISO 8601 like format.
        
            Also see:
                :meth:`~org.orekit.time.TimeComponents.formatUtcOffset`, :meth:`~org.orekit.time.TimeComponents.toString`
        
        
        """
        ...

_TimeInterpolable__T = typing.TypeVar('_TimeInterpolable__T', bound='TimeInterpolable')  # <T>
class TimeInterpolable(typing.Generic[_TimeInterpolable__T]):
    """
    public interface TimeInterpolable<T extends TimeInterpolable<T>>
    
        This interface represents objects that can be interpolated in time.
    """
    @typing.overload
    def interpolate(self, absoluteDate: 'AbsoluteDate', stream: java.util.stream.Stream[_TimeInterpolable__T]) -> _TimeInterpolable__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: 'AbsoluteDate', collection: typing.Union[java.util.Collection[_TimeInterpolable__T], typing.Sequence[_TimeInterpolable__T], typing.Set[_TimeInterpolable__T]]) -> _TimeInterpolable__T: ...

class TimeScalarFunction:
    """
    public interface TimeScalarFunction
    
        This interface represents a scalar function of time.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, absoluteDate: 'AbsoluteDate') -> float:
        """
            Compute a function of time.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
        
            Returns:
                value of the function
        
        """
        ...
    @typing.overload
    def value(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_value_1__T]) -> _value_1__T:
        """
            Compute a function of time.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
        
            Returns:
                value of the function
        
        
        """
        ...

class TimeScale(java.io.Serializable):
    """
    public interface TimeScale extends Serializable
    
        Interface for time scales.
    
        This is the interface representing all time scales. Time scales are related to each other by some offsets that may be
        discontinuous (for example the :class:`~org.orekit.time.UTCScale` with respect to the
        :class:`~org.orekit.time.TAIScale`).
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`
    """
    _getLeap_1__T = typing.TypeVar('_getLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLeap(self, absoluteDate: 'AbsoluteDate') -> float:
        """
            Get the value of the previous leap.
        
            This method will return 0.0 for all time scales that do *not* implement leap seconds.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                value of the previous leap
        
        """
        ...
    @typing.overload
    def getLeap(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_getLeap_1__T]) -> _getLeap_1__T:
        """
            Get the value of the previous leap.
        
            This method will return 0.0 for all time scales that do *not* implement leap seconds.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                value of the previous leap
        
            Since:
                9.0
        
        
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
    def insideLeap(self, absoluteDate: 'AbsoluteDate') -> bool:
        """
            Check if date is within a leap second introduction *in this time scale*.
        
            This method will return false for all time scales that do *not* implement leap seconds, even if the date corresponds to
            a leap second in :class:`~org.orekit.time.UTCScale`.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                true if time is within a leap second introduction
        
        """
        ...
    @typing.overload
    def insideLeap(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_insideLeap_1__T]) -> bool:
        """
            Check if date is within a leap second introduction *in this time scale*.
        
            This method will return false for all time scales that do *not* implement leap seconds, even if the date corresponds to
            a leap second in :class:`~org.orekit.time.UTCScale`.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                true if time is within a leap second introduction
        
            Since:
                9.0
        
        
        """
        ...
    _minuteDuration_1__T = typing.TypeVar('_minuteDuration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def minuteDuration(self, absoluteDate: 'AbsoluteDate') -> int:
        """
            Check length of the current minute *in this time scale*.
        
            This method will return 60 for all time scales that do *not* implement leap seconds, even if the date corresponds to a
            leap second in :class:`~org.orekit.time.UTCScale`, and 61 for time scales that do implement leap second when the current
            date is within the last minute before the leap, or during the leap itself.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                60 or 61 depending on leap seconds introduction
        
        """
        ...
    @typing.overload
    def minuteDuration(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_minuteDuration_1__T]) -> int:
        """
            Check length of the current minute *in this time scale*.
        
            This method will return 60 for all time scales that do *not* implement leap seconds, even if the date corresponds to a
            leap second in :class:`~org.orekit.time.UTCScale`, and 61 for time scales that do implement leap second when the current
            date is within the last minute before the leap, or during the leap itself.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                60 or 61 depending on leap seconds introduction
        
            Since:
                9.0
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: 'AbsoluteDate') -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...

class TimeScales:
    """
    public interface TimeScales
    
        A collection of :class:`~org.orekit.time.TimeScale`s. This interface defines methods for obtaining instances of many
        common time scales.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.time.TimeScalesFactory`, :class:`~org.orekit.time.TimeScale`,
            :class:`~org.orekit.time.LazyLoadedTimeScales`, :meth:`~org.orekit.time.TimeScales.of`
    """
    def createBesselianEpoch(self, double: float) -> 'AbsoluteDate':
        """
            Build an instance corresponding to a Besselian Epoch (BE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date
            as:
        
            .. code-block: java
            
            
             BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
             
        
            This method reverts the formula above and computes an :code:`AbsoluteDate` from the Besselian Epoch.
        
            Parameters:
                besselianEpoch (double): Besselian epoch, like 1950 for defining the classical reference B1950.0
        
            Returns:
                a new instant
        
            Also see:
                :meth:`~org.orekit.time.TimeScales.createJulianEpoch`
        
        
        """
        ...
    def createJulianEpoch(self, double: float) -> 'AbsoluteDate':
        """
            Build an instance corresponding to a Julian Epoch (JE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
        
            .. code-block: java
            
            
             JE = 2000.0 + (JED - 2451545.0) / 365.25
             
        
            This method reverts the formula above and computes an :code:`AbsoluteDate` from the Julian Epoch.
        
            Parameters:
                julianEpoch (double): Julian epoch, like 2000.0 for defining the classical reference J2000.0
        
            Returns:
                a new instant
        
            Also see:
                :meth:`~org.orekit.time.TimeScales.getJ2000Epoch`, :meth:`~org.orekit.time.TimeScales.createBesselianEpoch`
        
        
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
            Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (*not* UTC).
        
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
    def getGMST(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'GMSTScale':
        """
            Get the Greenwich Mean Sidereal Time scale.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
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
    def getIRNSS(self) -> 'IRNSSScale':
        """
            Get the Indian Regional Navigation Satellite System time scale.
        
            Returns:
                Indian Regional Navigation Satellite System time scale
        
        
        """
        ...
    def getIrnssEpoch(self) -> 'AbsoluteDate':
        """
            Reference epoch for IRNSS weeks: 1999-08-22T00:00:00 IRNSS time.
        
            Returns:
                IRNSS Epoch
        
        
        """
        ...
    def getJ2000Epoch(self) -> 'AbsoluteDate':
        """
            J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (*not* UTC).
        
            Returns:
                J2000 Epoch
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.createJulianEpoch`, :meth:`~org.orekit.time.AbsoluteDate.createBesselianEpoch`
        
        
        """
        ...
    def getJavaEpoch(self) -> 'AbsoluteDate':
        """
            Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
        
            Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587,
            UTC-TAI = 8.000082s
        
            Returns:
                Java Epoch
        
        
        """
        ...
    def getJulianEpoch(self) -> 'AbsoluteDate':
        """
            Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
        
            Both :code:`java.util.Date` and :class:`~org.orekit.time.DateComponents` classes follow the astronomical conventions and
            consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be
            seen in other documents or programs that obey a different convention (for example the :code:`convcal` utility).
        
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
    def getUT1(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'UT1Scale':
        """
            Get the Universal Time 1 scale.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Universal Time 1 scale
        
            Also see:
                :meth:`~org.orekit.time.TimeScales.getUTC`, :meth:`~org.orekit.frames.Frames.getEOPHistory`
        
        
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
    def of(collection: typing.Union[java.util.Collection[OffsetModel], typing.Sequence[OffsetModel], typing.Set[OffsetModel]], biFunction: typing.Union[java.util.function.BiFunction[org.orekit.utils.IERSConventions, 'TimeScales', java.util.Collection[org.orekit.frames.EOPEntry]], typing.Callable[[org.orekit.utils.IERSConventions, 'TimeScales'], java.util.Collection[org.orekit.frames.EOPEntry]]]) -> 'TimeScales': ...

class TimeScalesFactory(java.io.Serializable):
    """
    public class TimeScalesFactory extends Object implements Serializable
    
        Factory for predefined time scales.
    
        This is a utility class, so its constructor is private.
    
        Also see:
            :class:`~org.orekit.time.TimeScales`, :class:`~org.orekit.time.LazyLoadedTimeScales`, :meth:`~serialized`
    """
    @staticmethod
    def addDefaultUTCTAIOffsetsLoaders() -> None: ...
    @staticmethod
    def addUTCTAIOffsetsLoader(uTCTAIOffsetsLoader: 'UTCTAIOffsetsLoader') -> None: ...
    @staticmethod
    def clearUTCTAIOffsetsLoaders() -> None: ...
    @staticmethod
    def getBDT() -> 'BDTScale': ...
    @staticmethod
    def getGLONASS() -> 'GLONASSScale': ...
    @staticmethod
    def getGMST(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'GMSTScale': ...
    @staticmethod
    def getGPS() -> 'GPSScale': ...
    @staticmethod
    def getGST() -> 'GalileoScale': ...
    @staticmethod
    def getIRNSS() -> 'IRNSSScale': ...
    @staticmethod
    def getQZSS() -> 'QZSSScale': ...
    @staticmethod
    def getTAI() -> 'TAIScale': ...
    @staticmethod
    def getTCB() -> 'TCBScale': ...
    @staticmethod
    def getTCG() -> 'TCGScale': ...
    @staticmethod
    def getTDB() -> 'TDBScale': ...
    @staticmethod
    def getTT() -> 'TTScale': ...
    @staticmethod
    def getTimeScales() -> 'LazyLoadedTimeScales': ...
    @typing.overload
    @staticmethod
    def getUT1(eOPHistory: org.orekit.frames.EOPHistory) -> 'UT1Scale': ...
    @typing.overload
    @staticmethod
    def getUT1(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'UT1Scale': ...
    @staticmethod
    def getUTC() -> 'UTCScale': ...

_TimeShiftable__T = typing.TypeVar('_TimeShiftable__T', bound='TimeShiftable')  # <T>
class TimeShiftable(typing.Generic[_TimeShiftable__T]):
    """
    public interface TimeShiftable<T extends TimeShiftable<T>>
    
        This interface represents objects that can be shifted in time.
    """
    def shiftedBy(self, double: float) -> _TimeShiftable__T:
        """
            Get a time-shifted instance.
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...

class TimeStamped:
    """
    public interface TimeStamped
    
        This interface represents objects that have a :class:`~org.orekit.time.AbsoluteDate` date attached to them.
    
        Classes implementing this interface can be stored chronologically in sorted sets using
        :class:`~org.orekit.time.ChronologicalComparator` as the underlying comparator. An example using for
        :class:`~org.orekit.orbits.Orbit` instances is given here:
    
        .. code-block: java
        
        
             SortedSet<Orbit> sortedOrbits =
                 new TreeSet<Orbit>(new ChronologicalComparator());
             sortedOrbits.add(orbit1);
             sortedOrbits.add(orbit2);
             ...
         
    
        This interface is also the base interface used to :class:`~org.orekit.utils.TimeStampedCache` series of time-dependent
        objects for interpolation in a thread-safe manner.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :class:`~org.orekit.time.ChronologicalComparator`,
            :class:`~org.orekit.utils.TimeStampedCache`
    """
    def getDate(self) -> 'AbsoluteDate':
        """
            Get the date.
        
            Returns:
                date attached to the object
        
        
        """
        ...

class TimeVectorFunction:
    """
    public interface TimeVectorFunction
    
        This interface represents a multi-valued function of time.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, absoluteDate: 'AbsoluteDate') -> typing.List[float]:
        """
            Compute a function of time.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
        
            Returns:
                value of the function
        
        """
        ...
    @typing.overload
    def value(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_value_1__T]) -> typing.List[_value_1__T]:
        """
            Compute a function of time.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
        
            Returns:
                value of the function
        
        
        """
        ...

class UTCTAIOffsetsLoader:
    """
    public interface UTCTAIOffsetsLoader
    
        Interface for loading UTC-TAI offsets data files.
    
        Since:
            7.1
    """
    def loadOffsets(self) -> java.util.List[OffsetModel]: ...
    class Parser:
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class AGILeapSecondFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    public class AGILeapSecondFilesLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.time.UTCTAIOffsetsLoader`
    
        Loader for UTC-TAI extracted from LeapSecond file from AGI.
    
        This class is immutable and hence thread-safe
    
        Since:
            10.3
    
        Also see:
            LeapSecond.dat
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_SUPPORTED_NAMES
    
        Default supported files name pattern.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]: ...
    class Parser(UTCTAIOffsetsLoader.Parser):
        def __init__(self): ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class AbsoluteDate(TimeStamped, TimeShiftable['AbsoluteDate'], java.lang.Comparable['AbsoluteDate'], java.io.Serializable):
    """
    public class AbsoluteDate extends Object implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.time.AbsoluteDate`>, Comparable<:class:`~org.orekit.time.AbsoluteDate`>, Serializable
    
        This class represents a specific instant in time.
    
        Instances of this class are considered to be absolute in the sense that each one represent the occurrence of some event
        and can be compared to other instances or located in *any* :class:`~org.orekit.time.TimeScale`. In other words the
        different locations of an event with respect to two different time scales (say :class:`~org.orekit.time.TAIScale` and
        :class:`~org.orekit.time.UTCScale` for example) are simply different perspective related to a single object. Only one
        :code:`AbsoluteDate` instance is needed, both representations being available from this single instance by specifying
        the time scales as parameter when calling the ad-hoc methods.
    
        Since an instance is not bound to a specific time-scale, all methods related to the location of the date within some
        time scale require to provide the time scale as an argument. It is therefore possible to define a date in one time scale
        and to use it in another one. An example of such use is to read a date from a file in UTC and write it in another file
        in TAI. This can be done as follows:
    
        .. code-block: java
        
        
           DateTimeComponents utcComponents = readNextDate();
           AbsoluteDate date = new AbsoluteDate(utcComponents, TimeScalesFactory.getUTC());
           writeNextDate(date.getComponents(TimeScalesFactory.getTAI()));
         
    
        Two complementary views are available:
    
          - 
            location view (mainly for input/output or conversions)
    
            locations represent the coordinate of one event with respect to a :class:`~org.orekit.time.TimeScale`. The related
            methods are :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate`, :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate`,
            :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate`, :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate`, null,
            :meth:`~org.orekit.time.AbsoluteDate.toDate`, :meth:`~org.orekit.time.AbsoluteDate.toString`,
            :meth:`~org.orekit.time.AbsoluteDate.toString`, and :meth:`~org.orekit.time.AbsoluteDate.timeScalesOffset`.
          - 
            offset view (mainly for physical computation)
    
            offsets represent either the flow of time between two events (two instances of the class) or durations. They are counted
            in seconds, are continuous and could be measured using only a virtually perfect stopwatch. The related methods are
            :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate`, null, null, :meth:`~org.orekit.time.AbsoluteDate.durationFrom`,
            :meth:`~org.orekit.time.AbsoluteDate.compareTo`, :meth:`~org.orekit.time.AbsoluteDate.equals` and
            :meth:`~org.orekit.time.AbsoluteDate.hashCode`.
    
    
        A few reference epochs which are commonly used in space systems have been defined. These epochs can be used as the basis
        for offset computation. The supported epochs are: :meth:`~org.orekit.time.AbsoluteDate.JULIAN_EPOCH`,
        :meth:`~org.orekit.time.AbsoluteDate.MODIFIED_JULIAN_EPOCH`, :meth:`~org.orekit.time.AbsoluteDate.FIFTIES_EPOCH`,
        :meth:`~org.orekit.time.AbsoluteDate.CCSDS_EPOCH`, :meth:`~org.orekit.time.AbsoluteDate.GALILEO_EPOCH`,
        :meth:`~org.orekit.time.AbsoluteDate.GPS_EPOCH`, :meth:`~org.orekit.time.AbsoluteDate.QZSS_EPOCH`
        :meth:`~org.orekit.time.AbsoluteDate.J2000_EPOCH`, :meth:`~org.orekit.time.AbsoluteDate.JAVA_EPOCH`. There are also two
        factory methods :meth:`~org.orekit.time.AbsoluteDate.createJulianEpoch` and
        :meth:`~org.orekit.time.AbsoluteDate.createBesselianEpoch` that can be used to compute other reference epochs like
        J1900.0 or B1950.0. In addition to these reference epochs, two other constants are defined for convenience:
        :meth:`~org.orekit.time.AbsoluteDate.PAST_INFINITY` and :meth:`~org.orekit.time.AbsoluteDate.FUTURE_INFINITY`, which can
        be used either as dummy dates when a date is not yet initialized, or for initialization of loops searching for a min or
        max date.
    
        Instances of the :code:`AbsoluteDate` class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.time.TimeScale`, :class:`~org.orekit.time.TimeStamped`,
            :class:`~org.orekit.time.ChronologicalComparator`, :meth:`~serialized`
    """
    JULIAN_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` JULIAN_EPOCH
    
        Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
    
        Both :code:`java.util.Date` and :class:`~org.orekit.time.DateComponents` classes follow the astronomical conventions and
        consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be
        seen in other documents or programs that obey a different convention (for example the :code:`convcal` utility).
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getJulianEpoch`
    
    
    """
    MODIFIED_JULIAN_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` MODIFIED_JULIAN_EPOCH
    
        Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getModifiedJulianEpoch`
    
    
    """
    FIFTIES_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` FIFTIES_EPOCH
    
        Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getFiftiesEpoch`
    
    
    """
    CCSDS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` CCSDS_EPOCH
    
        Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (*not* UTC).
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getCcsdsEpoch`
    
    
    """
    GALILEO_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` GALILEO_EPOCH
    
        Reference epoch for Galileo System Time: 1999-08-22T00:00:00 GST.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getGalileoEpoch`
    
    
    """
    GPS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` GPS_EPOCH
    
        Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getGpsEpoch`
    
    
    """
    QZSS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` QZSS_EPOCH
    
        Reference epoch for QZSS weeks: 1980-01-06T00:00:00 QZSS time.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getQzssEpoch`
    
    
    """
    IRNSS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` IRNSS_EPOCH
    
        Reference epoch for IRNSS weeks: 1999-08-22T00:00:00 IRNSS time.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getIrnssEpoch`
    
    
    """
    BEIDOU_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` BEIDOU_EPOCH
    
        Reference epoch for BeiDou weeks: 2006-01-01T00:00:00 UTC.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getBeidouEpoch`
    
    
    """
    GLONASS_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` GLONASS_EPOCH
    
        Reference epoch for GLONASS four-year interval number: 1996-01-01T00:00:00 GLONASS time.
    
        By convention, TGLONASS = UTC + 3 hours.
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getGlonassEpoch`
    
    
    """
    J2000_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` J2000_EPOCH
    
        J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (*not* UTC).
    
        Also see:
            :meth:`~org.orekit.time.AbsoluteDate.createJulianEpoch`, :meth:`~org.orekit.time.AbsoluteDate.createBesselianEpoch`,
            :meth:`~org.orekit.time.TimeScales.getJ2000Epoch`
    
    
    """
    JAVA_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    :class:`~org.orekit.annotation.DefaultDataContext` public static final :class:`~org.orekit.time.AbsoluteDate` JAVA_EPOCH
    
        Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
    
        Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587,
        UTC-TAI = 8.000082s
    
        This constant uses the :meth:`~org.orekit.data.DataContext.getDefault`.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getJavaEpoch`
    
    
    """
    ARBITRARY_EPOCH: typing.ClassVar['AbsoluteDate'] = ...
    """
    public static final :class:`~org.orekit.time.AbsoluteDate` ARBITRARY_EPOCH
    
        An arbitrary finite date. Uses when a non-null date is needed but its value doesn't matter.
    
    """
    PAST_INFINITY: typing.ClassVar['AbsoluteDate'] = ...
    """
    public static final :class:`~org.orekit.time.AbsoluteDate` PAST_INFINITY
    
        Dummy date at infinity in the past direction.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getPastInfinity`
    
    
    """
    FUTURE_INFINITY: typing.ClassVar['AbsoluteDate'] = ...
    """
    public static final :class:`~org.orekit.time.AbsoluteDate` FUTURE_INFINITY
    
        Dummy date at infinity in the future direction.
    
        Also see:
            :meth:`~org.orekit.time.TimeScales.getFutureInfinity`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, month: Month, int2: int, int3: int, int4: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, int: int, month: Month, int2: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, string: str, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, date: java.util.Date, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, absoluteDate: 'AbsoluteDate', double: float): ...
    @typing.overload
    def __init__(self, absoluteDate: 'AbsoluteDate', double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, timeComponents: TimeComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, dateComponents: DateComponents, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, dateTimeComponents: DateTimeComponents, timeScale: TimeScale): ...
    def compareTo(self, absoluteDate: 'AbsoluteDate') -> int:
        """
            Compare the instance with another date.
        
            Specified by:
                 in interface 
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): other date to compare the instance to
        
            Returns:
                a negative integer, zero, or a positive integer as this date is before, simultaneous, or after the specified date.
        
        
        """
        ...
    @staticmethod
    def createBesselianEpoch(double: float) -> 'AbsoluteDate': ...
    @staticmethod
    def createJDDate(int: int, double: float, timeScale: TimeScale) -> 'AbsoluteDate':
        """
            Build an instance corresponding to a Julian Day date.
        
            Parameters:
                jd (int): Julian day
                secondsSinceNoon (double): seconds in the Julian day (BEWARE, Julian days start at noon, so 0.0 is noon)
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale in which the seconds in day are defined
        
            Returns:
                a new instant
        
        
        """
        ...
    @staticmethod
    def createJulianEpoch(double: float) -> 'AbsoluteDate': ...
    @staticmethod
    def createMJDDate(int: int, double: float, timeScale: TimeScale) -> 'AbsoluteDate': ...
    def durationFrom(self, absoluteDate: 'AbsoluteDate') -> float:
        """
            Compute the physically elapsed duration between two instants.
        
            The returned duration is the number of seconds physically elapsed between the two instants, measured in a regular time
            scale with respect to surface of the Earth (i.e either the :class:`~org.orekit.time.TAIScale`, the
            :class:`~org.orekit.time.TTScale` or the :class:`~org.orekit.time.GPSScale`). It is the only method that gives a
            duration with a physical meaning.
        
            This method gives the same result (with less computation) as calling :meth:`~org.orekit.time.AbsoluteDate.offsetFrom`
            with a second argument set to one of the regular scales cited above.
        
            This method is the reverse of the :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate` constructor.
        
            Parameters:
                instant (:class:`~org.orekit.time.AbsoluteDate`): instant to subtract from the instance
        
            Returns:
                offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.offsetFrom`, :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Check if the instance represents the same time as another instance.
        
            Overrides:
                 in class 
        
            Parameters:
                date (Object): other date
        
            Returns:
                true if the instance and the other date refer to the same instant
        
        
        """
        ...
    @typing.overload
    def getComponents(self, int: int) -> DateTimeComponents:
        """
            Split the instance into date/time components.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale to use
        
            Returns:
                date/time components
        
            Split the instance into date/time components for a local time.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC)
        
            Returns:
                date/time components
        
            Since:
                7.2
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.getComponents`
        
            Split the instance into date/time components for a local time.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC)
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                date/time components
        
            Since:
                10.1
        
            Split the instance into date/time components for a time zone.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                timeZone (TimeZone): time zone
        
            Returns:
                date/time components
        
            Since:
                7.2
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.getComponents`
        
            Split the instance into date/time components for a time zone.
        
            Parameters:
                timeZone (TimeZone): time zone
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to computed date and time components.
        
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
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashcode for this date.
        
            Overrides:
                 in class 
        
            Returns:
                hashcode
        
        
        """
        ...
    def isAfter(self, timeStamped: TimeStamped) -> bool:
        """
            Check if the instance represents a time that is strictly after another.
        
            Parameters:
                other (:class:`~org.orekit.time.TimeStamped`): the instant to compare this date to
        
            Returns:
                true if the instance is strictly after the argument when ordering chronologically
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isAfterOrEqualTo`
        
        
        """
        ...
    def isAfterOrEqualTo(self, timeStamped: TimeStamped) -> bool:
        """
            Check if the instance represents a time that is after or equal to another.
        
            Parameters:
                other (:class:`~org.orekit.time.TimeStamped`): the instant to compare this date to
        
            Returns:
                true if the instance is after (or equal to) the argument when ordering chronologically
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isAfterOrEqualTo`
        
        
        """
        ...
    def isBefore(self, timeStamped: TimeStamped) -> bool:
        """
            Check if the instance represents a time that is strictly before another.
        
            Parameters:
                other (:class:`~org.orekit.time.TimeStamped`): the instant to compare this date to
        
            Returns:
                true if the instance is strictly before the argument when ordering chronologically
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isBeforeOrEqualTo`
        
        
        """
        ...
    def isBeforeOrEqualTo(self, timeStamped: TimeStamped) -> bool:
        """
            Check if the instance represents a time that is before or equal to another.
        
            Parameters:
                other (:class:`~org.orekit.time.TimeStamped`): the instant to compare this date to
        
            Returns:
                true if the instance is before (or equal to) the argument when ordering chronologically
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isBefore`
        
        
        """
        ...
    def isBetween(self, timeStamped: TimeStamped, timeStamped2: TimeStamped) -> bool:
        """
            Check if the instance represents a time that is strictly between two others representing the boundaries of a time span.
            The two boundaries can be provided in any order: in other words, whether :code:`boundary` represents a time that is
            before or after :code:`otherBoundary` will not change the result of this method.
        
            Parameters:
                boundary (:class:`~org.orekit.time.TimeStamped`): one end of the time span
                otherBoundary (:class:`~org.orekit.time.TimeStamped`): the other end of the time span
        
            Returns:
                true if the instance is strictly between the two arguments when ordering chronologically
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isBetweenOrEqualTo`
        
        
        """
        ...
    def isBetweenOrEqualTo(self, timeStamped: TimeStamped, timeStamped2: TimeStamped) -> bool:
        """
            Check if the instance represents a time that is between two others representing the boundaries of a time span, or equal
            to one of them. The two boundaries can be provided in any order: in other words, whether :code:`boundary` represents a
            time that is before or after :code:`otherBoundary` will not change the result of this method.
        
            Parameters:
                boundary (:class:`~org.orekit.time.TimeStamped`): one end of the time span
                otherBoundary (:class:`~org.orekit.time.TimeStamped`): the other end of the time span
        
            Returns:
                true if the instance is between the two arguments (or equal to at least one of them) when ordering chronologically
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isBetween`
        
        
        """
        ...
    def isCloseTo(self, timeStamped: TimeStamped, double: float) -> bool:
        """
            Check if the instance time is close to another.
        
            Parameters:
                other (:class:`~org.orekit.time.TimeStamped`): the instant to compare this date to
                tolerance (double): the separation, in seconds, under which the two instants will be considered close to each other
        
            Returns:
                true if the duration between the instance and the argument is strictly below the tolerance
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isEqualTo`
        
        
        """
        ...
    def isEqualTo(self, timeStamped: TimeStamped) -> bool:
        """
            Check if the instance represents the same time as another.
        
            Parameters:
                other (:class:`~org.orekit.time.TimeStamped`): the instant to compare this date to
        
            Returns:
                true if the instance and the argument refer to the same instant
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.isCloseTo`
        
        
        """
        ...
    def offsetFrom(self, absoluteDate: 'AbsoluteDate', timeScale: TimeScale) -> float:
        """
            Compute the apparent clock offset between two instant *in the perspective of a specific
            :class:`~org.orekit.time.TimeScale`*.
        
            The offset is the number of seconds counted in the given time scale between the locations of the two instants, with all
            time scale irregularities removed (i.e. considering all days are exactly 86400 seconds long). This method will give a
            result that may not have a physical meaning if the time scale is irregular. For example since a leap second was
            introduced at the end of 2005, the apparent offset between 2005-12-31T23:59:59 and 2006-01-01T00:00:00 is 1 second, but
            the physical duration of the corresponding time interval as returned by the
            :meth:`~org.orekit.time.AbsoluteDate.durationFrom` method is 2 seconds.
        
            This method is the reverse of the :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate` constructor.
        
            Parameters:
                instant (:class:`~org.orekit.time.AbsoluteDate`): instant to subtract from the instance
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale with respect to which the offset should be computed
        
            Returns:
                apparent clock offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.durationFrom`, :meth:`~org.orekit.time.AbsoluteDate.AbsoluteDate`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSCalendarSegmentedTimeCode(byte: int, byteArray: typing.List[int]) -> 'AbsoluteDate':
        """
            Build an instance from a CCSDS Calendar Segmented Time Code (CCS).
        
            CCSDS Calendar Segmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in
            November 2010
        
            Parameters:
                preambleField (byte): field specifying the format, often not transmitted in data interfaces, as it is constant for a given data interface
                timeField (byte[]): byte array containing the time code
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                an instance corresponding to the specified date
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSCalendarSegmentedTimeCode(byte: int, byteArray: typing.List[int], timeScale: TimeScale) -> 'AbsoluteDate': ...
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(byte: int, byteArray: typing.List[int], dateComponents: DateComponents) -> 'AbsoluteDate':
        """
            Build an instance from a CCSDS Day Segmented Time Code (CDS).
        
            CCSDS Day Segmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in
            November 2010
        
            Parameters:
                preambleField (byte): field specifying the format, often not transmitted in data interfaces, as it is constant for a given data interface
                timeField (byte[]): byte array containing the time code
                agencyDefinedEpoch (:class:`~org.orekit.time.DateComponents`): reference epoch, ignored if the preamble field specifies the :meth:`~org.orekit.time.AbsoluteDate.CCSDS_EPOCH` is used
                    (and hence may be null in this case)
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                an instance corresponding to the specified date
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(byte: int, byteArray: typing.List[int], dateComponents: DateComponents, timeScale: TimeScale) -> 'AbsoluteDate': ...
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(byte: int, byte2: int, byteArray: typing.List[int], absoluteDate: 'AbsoluteDate') -> 'AbsoluteDate':
        """
            Build an instance from a CCSDS Unsegmented Time Code (CUC).
        
            CCSDS Unsegmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in November
            2010
        
            If the date to be parsed is formatted using version 3 of the standard (CCSDS 301.0-B-3 published in 2002) or if the
            extension of the preamble field introduced in version 4 of the standard is not used, then the :code:`preambleField2`
            parameter can be set to 0.
        
            Parameters:
                preambleField1 (byte): first byte of the field specifying the format, often not transmitted in data interfaces, as it is constant for a given
                    data interface
                preambleField2 (byte): second byte of the field specifying the format (added in revision 4 of the CCSDS standard in 2010), often not
                    transmitted in data interfaces, as it is constant for a given data interface (value ignored if presence not signaled in
                    :code:`preambleField1`)
                timeField (byte[]): byte array containing the time code
                agencyDefinedEpoch (:class:`~org.orekit.time.AbsoluteDate`): reference epoch, ignored if the preamble field specifies the :meth:`~org.orekit.time.AbsoluteDate.CCSDS_EPOCH` is used
                    (and hence may be null in this case)
                ccsdsEpoch (:class:`~org.orekit.time.AbsoluteDate`): reference epoch, ignored if the preamble field specifies the agency epoch is used.
        
            Returns:
                an instance corresponding to the specified date
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(byte: int, byte2: int, byteArray: typing.List[int], absoluteDate: 'AbsoluteDate', absoluteDate2: 'AbsoluteDate') -> 'AbsoluteDate': ...
    def shiftedBy(self, double: float) -> 'AbsoluteDate':
        """
            Get a time-shifted date.
        
            Calling this method is equivalent to call :code:`new AbsoluteDate(this, dt)`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new date, shifted with respect to instance (which is immutable)
        
            Also see:
                :meth:`~org.orekit.utils.PVCoordinates.shiftedBy`, :meth:`~org.orekit.attitudes.Attitude.shiftedBy`,
                :meth:`~org.orekit.orbits.Orbit.shiftedBy`, :meth:`~org.orekit.propagation.SpacecraftState.shiftedBy`
        
        
        """
        ...
    def timeScalesOffset(self, timeScale: TimeScale, timeScale2: TimeScale) -> float:
        """
            Compute the offset between two time scales at the current instant.
        
            The offset is defined as *lÃ¢â€šï¿½-lÃ¢â€šâ€š* where *lÃ¢â€šï¿½* is the location of the instant in the :code:`scale1`
            time scale and *lÃ¢â€šâ€š* is the location of the instant in the :code:`scale2` time scale.
        
            Parameters:
                scale1 (:class:`~org.orekit.time.TimeScale`): first time scale
                scale2 (:class:`~org.orekit.time.TimeScale`): second time scale
        
            Returns:
                offset in seconds between the two time scales at the current instant
        
        
        """
        ...
    def toDate(self, timeScale: TimeScale) -> java.util.Date:
        """
            Convert the instance to a Java null.
        
            Conversion to the Date class induces a loss of precision because the Date class does not provide sub-millisecond
            information. Java Dates are considered to be locations in some times scales.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale to use
        
            Returns:
                a null instance representing the location of the instant in the time scale
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a String representation of the instant location with up to 16 digits of precision for the seconds value.
        
            Since this method is used in exception messages and error handling every effort is made to return some representation of
            the instant. If UTC is available from the default data context then it is used to format the string in UTC. If not then
            TAI is used. Finally if the prior attempts fail this method falls back to converting this class's internal
            representation to a string.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the instance, in ISO-8601 format if UTC is available from the default data context.
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.toString`, :meth:`~org.orekit.time.AbsoluteDate.toStringRfc3339`,
                :meth:`~org.orekit.time.DateTimeComponents.toString`
        
        """
        ...
    @typing.overload
    def toString(self, int: int) -> str:
        """
            Get a String representation of the instant location in ISO-8601 format without the UTC offset and with up to 16 digits
            of precision for the seconds value.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale to use
        
            Returns:
                a string representation of the instance.
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.toStringRfc3339`, :meth:`~org.orekit.time.DateTimeComponents.toString`
        
            Get a String representation of the instant location for a local time.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC).
        
            Returns:
                string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
            Since:
                7.2
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.toString`
        
            Get a String representation of the instant location for a local time.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC).
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.getComponents`, :meth:`~org.orekit.time.DateTimeComponents.toString`
        
            Get a String representation of the instant location for a time zone.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                timeZone (TimeZone): time zone
        
            Returns:
                string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
            Since:
                7.2
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.toString`
        
            Get a String representation of the instant location for a time zone.
        
            Parameters:
                timeZone (TimeZone): time zone
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.getComponents`, :meth:`~org.orekit.time.DateTimeComponents.toString`
        
        
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
    def toStringRfc3339(self, timeScale: TimeScale) -> str:
        """
            Represent the given date as a string according to the format in RFC 3339. RFC3339 is a restricted subset of ISO 8601
            with a well defined grammar. Enough digits are included in the seconds value to avoid rounding up to the next minute.
        
            This method is different than :meth:`~org.orekit.time.AbsoluteDate.toString` in that it includes a :code:`"Z"` at the
            end to indicate the time zone and enough precision to represent the point in time without rounding up to the next
            minute.
        
            RFC3339 is unable to represent BC years, years of 10000 or more, time zone offsets of 100 hours or more, or NaN. In
            these cases the value returned from this method will not be valid RFC3339 format.
        
            Parameters:
                utc (:class:`~org.orekit.time.TimeScale`): time scale.
        
            Returns:
                RFC 3339 format string.
        
            Also see:
                RFC 3339, :meth:`~org.orekit.time.DateTimeComponents.toStringRfc3339`, :meth:`~org.orekit.time.AbsoluteDate.toString`,
                :meth:`~org.orekit.time.AbsoluteDate.getComponents`
        
        
        """
        ...
    def toStringWithoutUtcOffset(self, timeScale: TimeScale, int: int) -> str:
        """
            Return a string representation of this date-time, rounded to the given precision.
        
            The format used is ISO8601 without the UTC offset.
        
            Calling :code:`toStringWithoutUtcOffset(DataContext.getDefault().getTimeScales().getUTC(), 3)` will emulate the behavior
            of :meth:`~org.orekit.time.AbsoluteDate.toString` in Orekit 10 and earlier. Note this method is more accurate as it
            correctly handles rounding during leap seconds.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): to use to compute components.
                fractionDigits (int): the number of digits to include after the decimal point in the string representation of the seconds. The date and time
                    is first rounded as necessary. :code:`fractionDigits` must be greater than or equal to :code:`0`.
        
            Returns:
                string representation of this date, time, and UTC offset
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.toString`, :meth:`~org.orekit.time.AbsoluteDate.toStringRfc3339`,
                :meth:`~org.orekit.time.DateTimeComponents.toString`,
                :meth:`~org.orekit.time.DateTimeComponents.toStringWithoutUtcOffset`
        
        
        """
        ...

class AbstractTimeScales(TimeScales):
    """
    public abstract class AbstractTimeScales extends Object implements :class:`~org.orekit.time.TimeScales`
    
        Abstract base class for :class:`~org.orekit.time.TimeScales` that implements some common functionality.
    
        Since:
            10.1
    """
    def __init__(self): ...
    def createBesselianEpoch(self, double: float) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.createBesselianEpoch`
            Build an instance corresponding to a Besselian Epoch (BE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date
            as:
        
            .. code-block: java
            
            
             BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
             
        
            This method reverts the formula above and computes an :code:`AbsoluteDate` from the Besselian Epoch.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.createBesselianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                besselianEpoch (double): Besselian epoch, like 1950 for defining the classical reference B1950.0
        
            Returns:
                a new instant
        
            Also see:
                :meth:`~org.orekit.time.TimeScales.createJulianEpoch`
        
        
        """
        ...
    def createJulianEpoch(self, double: float) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.createJulianEpoch`
            Build an instance corresponding to a Julian Epoch (JE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
        
            .. code-block: java
            
            
             JE = 2000.0 + (JED - 2451545.0) / 365.25
             
        
            This method reverts the formula above and computes an :code:`AbsoluteDate` from the Julian Epoch.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.createJulianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                julianEpoch (double): Julian epoch, like 2000.0 for defining the classical reference J2000.0
        
            Returns:
                a new instant
        
            Also see:
                :meth:`~org.orekit.time.TimeScales.getJ2000Epoch`, :meth:`~org.orekit.time.TimeScales.createBesselianEpoch`
        
        
        """
        ...
    def getBeidouEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getBeidouEpoch`
            Reference epoch for BeiDou weeks: 2006-01-01T00:00:00 UTC.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getBeidouEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Beidou Epoch
        
        
        """
        ...
    def getCcsdsEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getCcsdsEpoch`
            Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (*not* UTC).
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getCcsdsEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                CCSDS Epoch
        
        
        """
        ...
    def getFiftiesEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getFiftiesEpoch`
            Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getFiftiesEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Fifties Epoch
        
        
        """
        ...
    def getFutureInfinity(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getFutureInfinity`
            Dummy date at infinity in the future direction.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getFutureInfinity` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                the latest date.
        
        
        """
        ...
    def getGMST(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'GMSTScale':
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGMST`
            Get the Greenwich Mean Sidereal Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGMST` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Greenwich Mean Sidereal Time scale
        
        
        """
        ...
    def getGalileoEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGalileoEpoch`
            Reference epoch for Galileo System Time: 1999-08-22T00:00:00 GST.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGalileoEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Galileo Epoch
        
        
        """
        ...
    def getGlonassEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGlonassEpoch`
            Reference epoch for GLONASS four-year interval number: 1996-01-01T00:00:00 GLONASS time.
        
            By convention, TGLONASS = UTC + 3 hours.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGlonassEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                GLONASS Epoch
        
        
        """
        ...
    def getGpsEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGpsEpoch`
            Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGpsEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                GPS Epoch
        
        
        """
        ...
    def getIrnssEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getIrnssEpoch`
            Reference epoch for IRNSS weeks: 1999-08-22T00:00:00 IRNSS time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getIrnssEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                IRNSS Epoch
        
        
        """
        ...
    def getJ2000Epoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getJ2000Epoch`
            J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (*not* UTC).
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getJ2000Epoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                J2000 Epoch
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.createJulianEpoch`, :meth:`~org.orekit.time.AbsoluteDate.createBesselianEpoch`
        
        
        """
        ...
    def getJavaEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getJavaEpoch`
            Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
        
            Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587,
            UTC-TAI = 8.000082s
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getJavaEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Java Epoch
        
        
        """
        ...
    def getJulianEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getJulianEpoch`
            Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
        
            Both :code:`java.util.Date` and :class:`~org.orekit.time.DateComponents` classes follow the astronomical conventions and
            consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be
            seen in other documents or programs that obey a different convention (for example the :code:`convcal` utility).
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getJulianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Julian epoch.
        
        
        """
        ...
    def getModifiedJulianEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getModifiedJulianEpoch`
            Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getModifiedJulianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Modified Julian Epoch
        
        
        """
        ...
    def getPastInfinity(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getPastInfinity`
            Dummy date at infinity in the past direction.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getPastInfinity` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                the earliest date.
        
        
        """
        ...
    def getQzssEpoch(self) -> AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getQzssEpoch`
            Reference epoch for QZSS weeks: 1980-01-06T00:00:00 QZSS time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getQzssEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                QZSS Epoch
        
        
        """
        ...
    def getUT1(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'UT1Scale':
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getUT1`
            Get the Universal Time 1 scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getUT1` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Universal Time 1 scale
        
            Also see:
                :meth:`~org.orekit.time.TimeScales.getUTC`, :meth:`~org.orekit.frames.Frames.getEOPHistory`
        
        
        """
        ...

class BDTScale(TimeScale):
    """
    public class BDTScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Beidou system time scale.
    
        By convention, BDT = UTC on January 1st 2006.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class BurstSelector(DatesSelector):
    """
    public class BurstSelector extends Object implements :class:`~org.orekit.time.DatesSelector`
    
        Selector generating high rate bursts of dates separated by some rest period.
    
        The dates can be aligned to whole steps in some time scale. So for example if a rest period of 3600s is used and the
        alignment time scale is set to :meth:`~org.orekit.time.TimeScales.getUTC`, the earliest date of each burst will occur at
        whole hours in UTC time.
    
        BEWARE! This class stores internally the last selected dates, so it is *neither* reusable across several
        :class:`~org.orekit.estimation.measurements.generation.EventBasedScheduler` or
        :class:`~org.orekit.estimation.measurements.generation.ContinuousScheduler` schedulers, *nor* thread-safe. A separate
        selector should be used for each scheduler and for each thread in multi-threading context.
    
        Since:
            9.3
    """
    def __init__(self, int: int, double: float, double2: float, timeScale: TimeScale): ...
    def selectDates(self, absoluteDate: AbsoluteDate, absoluteDate2: AbsoluteDate) -> java.util.List[AbsoluteDate]: ...

_FieldAbsoluteDate__T = typing.TypeVar('_FieldAbsoluteDate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbsoluteDate(FieldTimeStamped[_FieldAbsoluteDate__T], TimeShiftable['FieldAbsoluteDate'[_FieldAbsoluteDate__T]], java.lang.Comparable['FieldAbsoluteDate'[_FieldAbsoluteDate__T]], typing.Generic[_FieldAbsoluteDate__T]):
    """
    public class FieldAbsoluteDate<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.time.FieldTimeStamped`<T>, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.time.FieldAbsoluteDate`<T>>, Comparable<:class:`~org.orekit.time.FieldAbsoluteDate`<T>>
    
        This class represents a specific instant in time.
    
        Instances of this class are considered to be absolute in the sense that each one represent the occurrence of some event
        and can be compared to other instances or located in *any* :class:`~org.orekit.time.TimeScale`. In other words the
        different locations of an event with respect to two different time scales (say :class:`~org.orekit.time.TAIScale` and
        :class:`~org.orekit.time.UTCScale` for example) are simply different perspective related to a single object. Only one
        :code:`FieldAbsoluteDate<T>` instance is needed, both representations being available from this single instance by
        specifying the time scales as parameter when calling the ad-hoc methods.
    
        Since an instance is not bound to a specific time-scale, all methods related to the location of the date within some
        time scale require to provide the time scale as an argument. It is therefore possible to define a date in one time scale
        and to use it in another one. An example of such use is to read a date from a file in UTC and write it in another file
        in TAI. This can be done as follows:
    
        .. code-block: java
        
        
           DateTimeComponents utcComponents = readNextDate();
           FieldAbsoluteDate<T> date = new FieldAbsoluteDate<>(utcComponents, TimeScalesFactory.getUTC());
           writeNextDate(date.getComponents(TimeScalesFactory.getTAI()));
         
    
        Two complementary views are available:
    
          - 
            location view (mainly for input/output or conversions)
    
            locations represent the coordinate of one event with respect to a :class:`~org.orekit.time.TimeScale`. The related
            methods are :meth:`~org.orekit.time.FieldAbsoluteDate.FieldAbsoluteDate`,
            :meth:`~org.orekit.time.FieldAbsoluteDate.FieldAbsoluteDate`,
            :meth:`~org.orekit.time.FieldAbsoluteDate.FieldAbsoluteDate`,
            :meth:`~org.orekit.time.FieldAbsoluteDate.FieldAbsoluteDate`, :meth:`~org.orekit.time.FieldAbsoluteDate.createGPSDate`,
            null, :meth:`~org.orekit.time.FieldAbsoluteDate.toDate`, :meth:`~org.orekit.time.FieldAbsoluteDate.toString`,
            :meth:`~org.orekit.time.FieldAbsoluteDate.toString`, and :meth:`~org.orekit.time.FieldAbsoluteDate.timeScalesOffset`.
          - 
            offset view (mainly for physical computation)
    
            offsets represent either the flow of time between two events (two instances of the class) or durations. They are counted
            in seconds, are continuous and could be measured using only a virtually perfect stopwatch. The related methods are
            :meth:`~org.orekit.time.FieldAbsoluteDate.FieldAbsoluteDate`, null, null,
            :meth:`~org.orekit.time.FieldAbsoluteDate.durationFrom`, :meth:`~org.orekit.time.FieldAbsoluteDate.compareTo`,
            :meth:`~org.orekit.time.FieldAbsoluteDate.equals` and :meth:`~org.orekit.time.FieldAbsoluteDate.hashCode`.
    
    
        A few reference epochs which are commonly used in space systems have been defined. These epochs can be used as the basis
        for offset computation. The supported epochs are: :meth:`~org.orekit.time.FieldAbsoluteDate.getJulianEpoch`,
        :meth:`~org.orekit.time.FieldAbsoluteDate.getModifiedJulianEpoch`,
        :meth:`~org.orekit.time.FieldAbsoluteDate.getFiftiesEpoch`, :meth:`~org.orekit.time.FieldAbsoluteDate.getCCSDSEpoch`,
        :meth:`~org.orekit.time.FieldAbsoluteDate.getGalileoEpoch`, :meth:`~org.orekit.time.FieldAbsoluteDate.getGPSEpoch`,
        :meth:`~org.orekit.time.FieldAbsoluteDate.getJ2000Epoch`, :meth:`~org.orekit.time.FieldAbsoluteDate.getJavaEpoch`. There
        are also two factory methods :meth:`~org.orekit.time.FieldAbsoluteDate.createJulianEpoch` and
        :meth:`~org.orekit.time.FieldAbsoluteDate.createBesselianEpoch` that can be used to compute other reference epochs like
        J1900.0 or B1950.0. In addition to these reference epochs, two other constants are defined for convenience:
        :meth:`~org.orekit.time.FieldAbsoluteDate.getPastInfinity` and
        :meth:`~org.orekit.time.FieldAbsoluteDate.getFutureInfinity`, which can be used either as dummy dates when a date is not
        yet initialized, or for initialization of loops searching for a min or max date.
    
        Instances of the :code:`FieldAbsoluteDate<T>` class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.time.TimeScale`, :class:`~org.orekit.time.TimeStamped`,
            :class:`~org.orekit.time.ChronologicalComparator`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, int2: int, int3: int, int4: int, int5: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, int2: int, int3: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, month: Month, int2: int, int3: int, int4: int, double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], int: int, month: Month, int2: int, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsoluteDate__T], string: str, timeScale: TimeScale): ...
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
    def __init__(self, absoluteDate: AbsoluteDate, t: _FieldAbsoluteDate__T): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], double: float): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], double: float, timeScale: TimeScale): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], t: _FieldAbsoluteDate__T): ...
    def compareTo(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]) -> int: ...
    _createBesselianEpoch_0__T = typing.TypeVar('_createBesselianEpoch_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _createBesselianEpoch_1__T = typing.TypeVar('_createBesselianEpoch_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createBesselianEpoch(t: _createBesselianEpoch_0__T) -> 'FieldAbsoluteDate'[_createBesselianEpoch_0__T]:
        """
            Build an instance corresponding to a Besselian Epoch (BE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date
            as:
        
            .. code-block: java
            
            
             BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
             
        
            This method reverts the formula above and computes an :code:`FieldAbsoluteDate<T>` from the Besselian Epoch.
        
            Parameters:
                besselianEpoch (T): Besselian epoch, like 1950 for defining the classical reference B1950.0
                timeScales (:class:`~org.orekit.time.TimeScales`): used in the computation.
        
            Returns:
                a new instant
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.FieldAbsoluteDate.createJulianEpoch`, :meth:`~org.orekit.time.TimeScales.createBesselianEpoch`
        
        
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
        
            GPS dates are provided as a week number starting at :meth:`~org.orekit.time.FieldAbsoluteDate.getGPSEpoch` and as a
            number of milliseconds since week start.
        
            Parameters:
                weekNumber (int): week number since :meth:`~org.orekit.time.FieldAbsoluteDate.getGPSEpoch`
                milliInWeek (T): number of milliseconds since week start
                gps (:class:`~org.orekit.time.TimeScale`): GPS time scale.
        
            Returns:
                a new instant
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createGPSDate(int: int, t: _createGPSDate_1__T, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_createGPSDate_1__T]: ...
    _createJDDate__T = typing.TypeVar('_createJDDate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def createJDDate(int: int, t: _createJDDate__T, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_createJDDate__T]:
        """
            Build an instance corresponding to a Julian Day date.
        
            Parameters:
                jd (int): Julian day
                secondsSinceNoon (T): seconds in the Julian day (BEWARE, Julian days start at noon, so 0.0 is noon)
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale in which the seconds in day are defined
        
            Returns:
                a new instant
        
        
        """
        ...
    _createJulianEpoch_0__T = typing.TypeVar('_createJulianEpoch_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _createJulianEpoch_1__T = typing.TypeVar('_createJulianEpoch_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createJulianEpoch(t: _createJulianEpoch_0__T) -> 'FieldAbsoluteDate'[_createJulianEpoch_0__T]:
        """
            Build an instance corresponding to a Julian Epoch (JE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
            :code:`JE = 2000.0 + (JED - 2451545.0) / 365.25`
        
            This method reverts the formula above and computes an :code:`FieldAbsoluteDate<T>` from the Julian Epoch.
        
            Parameters:
                julianEpoch (T): Julian epoch, like 2000.0 for defining the classical reference J2000.0
                timeScales (:class:`~org.orekit.time.TimeScales`): used in the computation.
        
            Returns:
                a new instant
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.time.FieldAbsoluteDate.getJ2000Epoch`,
                :meth:`~org.orekit.time.FieldAbsoluteDate.createBesselianEpoch`, :meth:`~org.orekit.time.TimeScales.createJulianEpoch`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createJulianEpoch(t: _createJulianEpoch_1__T, timeScales: TimeScales) -> 'FieldAbsoluteDate'[_createJulianEpoch_1__T]: ...
    _createMJDDate__T = typing.TypeVar('_createMJDDate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def createMJDDate(int: int, t: _createMJDDate__T, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_createMJDDate__T]:
        """
            Build an instance corresponding to a Modified Julian Day date.
        
            Parameters:
                mjd (int): modified Julian day
                secondsInDay (T): seconds in the day
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale in which the seconds in day are defined
        
            Returns:
                a new instant
        
        
        """
        ...
    @typing.overload
    def durationFrom(self, absoluteDate: AbsoluteDate) -> _FieldAbsoluteDate__T:
        """
            Compute the physically elapsed duration between two instants.
        
            The returned duration is the number of seconds physically elapsed between the two instants, measured in a regular time
            scale with respect to surface of the Earth (i.e either the :class:`~org.orekit.time.TAIScale`, the
            :class:`~org.orekit.time.TTScale` or the :class:`~org.orekit.time.GPSScale`). It is the only method that gives a
            duration with a physical meaning.
        
            This method gives the same result (with less computation) as calling
            :meth:`~org.orekit.time.FieldAbsoluteDate.offsetFrom` with a second argument set to one of the regular scales cited
            above.
        
            This method is the reverse of the :meth:`~org.orekit.time.FieldAbsoluteDate.FieldAbsoluteDate` constructor.
        
            Parameters:
                instant (:class:`~org.orekit.time.AbsoluteDate`): instant to subtract from the instance
        
            Returns:
                offset in seconds between the two instants (positive if the instance is posterior to the argument)
        
            Also see:
                :meth:`~org.orekit.time.FieldAbsoluteDate.offsetFrom`, :meth:`~org.orekit.time.FieldAbsoluteDate.FieldAbsoluteDate`
        
        
        """
        ...
    @typing.overload
    def durationFrom(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]) -> _FieldAbsoluteDate__T: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Check if the instance represents the same time as another instance.
        
            Overrides:
                 in class 
        
            Parameters:
                date (Object): other date
        
            Returns:
                true if the instance and the other date refer to the same instant
        
        
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
    def getCCSDSEpoch(field: org.hipparchus.Field[_getCCSDSEpoch__T]) -> 'FieldAbsoluteDate'[_getCCSDSEpoch__T]: ...
    @typing.overload
    def getComponents(self, int: int) -> DateTimeComponents:
        """
            Split the instance into date/time components.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale to use
        
            Returns:
                date/time components
        
            Split the instance into date/time components for a local time.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC)
        
            Returns:
                date/time components
        
            Also see:
                :meth:`~org.orekit.time.FieldAbsoluteDate.getComponents`
        
            Split the instance into date/time components for a local time.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC)
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                date/time components
        
            Since:
                10.1
        
            Split the instance into date/time components for a time zone.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                timeZone (TimeZone): time zone
        
            Returns:
                date/time components
        
            Also see:
                :meth:`~org.orekit.time.FieldAbsoluteDate.getComponents`
        
            Split the instance into date/time components for a time zone.
        
            Parameters:
                timeZone (TimeZone): time zone
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
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
    def getDate(self) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    def getField(self) -> org.hipparchus.Field[_FieldAbsoluteDate__T]: ...
    _getFiftiesEpoch__T = typing.TypeVar('_getFiftiesEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getFiftiesEpoch(field: org.hipparchus.Field[_getFiftiesEpoch__T]) -> 'FieldAbsoluteDate'[_getFiftiesEpoch__T]: ...
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
                :meth:`~org.orekit.time.AbsoluteDate.FUTURE_INFINITY`, :meth:`~org.orekit.time.TimeScales.getFutureInfinity`
        
        
        """
        ...
    _getGPSEpoch__T = typing.TypeVar('_getGPSEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getGPSEpoch(field: org.hipparchus.Field[_getGPSEpoch__T]) -> 'FieldAbsoluteDate'[_getGPSEpoch__T]: ...
    _getGalileoEpoch__T = typing.TypeVar('_getGalileoEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getGalileoEpoch(field: org.hipparchus.Field[_getGalileoEpoch__T]) -> 'FieldAbsoluteDate'[_getGalileoEpoch__T]: ...
    _getJ2000Epoch__T = typing.TypeVar('_getJ2000Epoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getJ2000Epoch(field: org.hipparchus.Field[_getJ2000Epoch__T]) -> 'FieldAbsoluteDate'[_getJ2000Epoch__T]: ...
    _getJavaEpoch__T = typing.TypeVar('_getJavaEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getJavaEpoch(field: org.hipparchus.Field[_getJavaEpoch__T]) -> 'FieldAbsoluteDate'[_getJavaEpoch__T]: ...
    _getJulianEpoch__T = typing.TypeVar('_getJulianEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getJulianEpoch(field: org.hipparchus.Field[_getJulianEpoch__T]) -> 'FieldAbsoluteDate'[_getJulianEpoch__T]: ...
    _getModifiedJulianEpoch__T = typing.TypeVar('_getModifiedJulianEpoch__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getModifiedJulianEpoch(field: org.hipparchus.Field[_getModifiedJulianEpoch__T]) -> 'FieldAbsoluteDate'[_getModifiedJulianEpoch__T]: ...
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
                :meth:`~org.orekit.time.AbsoluteDate.PAST_INFINITY`, :meth:`~org.orekit.time.TimeScales.getPastInfinity`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashcode for this date.
        
            Overrides:
                 in class 
        
            Returns:
                hashcode
        
        
        """
        ...
    def isAfter(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T]) -> bool: ...
    def isAfterOrEqualTo(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T]) -> bool: ...
    def isBefore(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T]) -> bool: ...
    def isBeforeOrEqualTo(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T]) -> bool: ...
    def isBetween(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T], fieldTimeStamped2: FieldTimeStamped[_FieldAbsoluteDate__T]) -> bool: ...
    def isBetweenOrEqualTo(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T], fieldTimeStamped2: FieldTimeStamped[_FieldAbsoluteDate__T]) -> bool: ...
    def isCloseTo(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T], double: float) -> bool: ...
    def isEqualTo(self, fieldTimeStamped: FieldTimeStamped[_FieldAbsoluteDate__T]) -> bool: ...
    def offsetFrom(self, fieldAbsoluteDate: 'FieldAbsoluteDate'[_FieldAbsoluteDate__T], timeScale: TimeScale) -> _FieldAbsoluteDate__T: ...
    @typing.overload
    def parseCCSDSCalendarSegmentedTimeCode(self, byte: int, byteArray: typing.List[int]) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    @typing.overload
    def parseCCSDSCalendarSegmentedTimeCode(self, byte: int, byteArray: typing.List[int], timeScale: TimeScale) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    _parseCCSDSDaySegmentedTimeCode_0__T = typing.TypeVar('_parseCCSDSDaySegmentedTimeCode_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _parseCCSDSDaySegmentedTimeCode_1__T = typing.TypeVar('_parseCCSDSDaySegmentedTimeCode_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(field: org.hipparchus.Field[_parseCCSDSDaySegmentedTimeCode_0__T], byte: int, byteArray: typing.List[int], dateComponents: DateComponents) -> 'FieldAbsoluteDate'[_parseCCSDSDaySegmentedTimeCode_0__T]:
        """
            Build an instance from a CCSDS Day Segmented Time Code (CDS).
        
            CCSDS Day Segmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in
            November 2010
        
            Parameters:
                field (Field<T> field): field for the components
                preambleField (byte): field specifying the format, often not transmitted in data interfaces, as it is constant for a given data interface
                timeField (byte[]): byte array containing the time code
                agencyDefinedEpoch (:class:`~org.orekit.time.DateComponents`): reference epoch, ignored if the preamble field specifies the :meth:`~org.orekit.time.FieldAbsoluteDate.getCCSDSEpoch` is
                    used (and hence may be null in this case)
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                an instance corresponding to the specified date
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSDaySegmentedTimeCode(field: org.hipparchus.Field[_parseCCSDSDaySegmentedTimeCode_1__T], byte: int, byteArray: typing.List[int], dateComponents: DateComponents, timeScale: TimeScale) -> 'FieldAbsoluteDate'[_parseCCSDSDaySegmentedTimeCode_1__T]: ...
    _parseCCSDSUnsegmentedTimeCode_0__T = typing.TypeVar('_parseCCSDSUnsegmentedTimeCode_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _parseCCSDSUnsegmentedTimeCode_1__T = typing.TypeVar('_parseCCSDSUnsegmentedTimeCode_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(field: org.hipparchus.Field[_parseCCSDSUnsegmentedTimeCode_0__T], byte: int, byte2: int, byteArray: typing.List[int], fieldAbsoluteDate: 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_0__T]) -> 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_0__T]:
        """
            Build an instance from a CCSDS Unsegmented Time Code (CUC).
        
            CCSDS Unsegmented Time Code is defined in the blue book: CCSDS Time Code Format (CCSDS 301.0-B-4) published in November
            2010
        
            If the date to be parsed is formatted using version 3 of the standard (CCSDS 301.0-B-3 published in 2002) or if the
            extension of the preamble field introduced in version 4 of the standard is not used, then the :code:`preambleField2`
            parameter can be set to 0.
        
            Parameters:
                field (Field<T> field): field for the components
                preambleField1 (byte): first byte of the field specifying the format, often not transmitted in data interfaces, as it is constant for a given
                    data interface
                preambleField2 (byte): second byte of the field specifying the format (added in revision 4 of the CCSDS standard in 2010), often not
                    transmitted in data interfaces, as it is constant for a given data interface (value ignored if presence not signaled in
                    :code:`preambleField1`)
                timeField (byte[]): byte array containing the time code
                agencyDefinedEpoch (:class:`~org.orekit.time.FieldAbsoluteDate`<T> agencyDefinedEpoch): reference epoch, ignored if the preamble field specifies the CCSDS reference epoch is used (and hence may be null in
                    this case)
                ccsdsEpoch (:class:`~org.orekit.time.FieldAbsoluteDate`<T> ccsdsEpoch): reference epoch, ignored if the preamble field specifies the agency epoch is used.
        
            Returns:
                an instance corresponding to the specified date
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseCCSDSUnsegmentedTimeCode(field: org.hipparchus.Field[_parseCCSDSUnsegmentedTimeCode_1__T], byte: int, byte2: int, byteArray: typing.List[int], fieldAbsoluteDate: 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_1__T], fieldAbsoluteDate2: 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_1__T]) -> 'FieldAbsoluteDate'[_parseCCSDSUnsegmentedTimeCode_1__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAbsoluteDate__T) -> 'FieldAbsoluteDate'[_FieldAbsoluteDate__T]: ...
    def timeScalesOffset(self, timeScale: TimeScale, timeScale2: TimeScale) -> _FieldAbsoluteDate__T:
        """
            Compute the offset between two time scales at the current instant.
        
            The offset is defined as *lÃ¢â€šï¿½-lÃ¢â€šâ€š* where *lÃ¢â€šï¿½* is the location of the instant in the :code:`scale1`
            time scale and *lÃ¢â€šâ€š* is the location of the instant in the :code:`scale2` time scale.
        
            Parameters:
                scale1 (:class:`~org.orekit.time.TimeScale`): first time scale
                scale2 (:class:`~org.orekit.time.TimeScale`): second time scale
        
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
            Convert the instance to a Java null.
        
            Conversion to the Date class induces a loss of precision because the Date class does not provide sub-millisecond
            information. Java Dates are considered to be locations in some times scales.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale to use
        
            Returns:
                a null instance representing the location of the instant in the time scale
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Get a String representation of the instant location with up to 16 digits of precision for the seconds value.
        
            Since this method is used in exception messages and error handling every effort is made to return some representation of
            the instant. If UTC is available from the default data context then it is used to format the string in UTC. If not then
            TAI is used. Finally if the prior attempts fail this method falls back to converting this class's internal
            representation to a string.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of the instance, in ISO-8601 format if UTC is available from the default data context.
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.toString`, :meth:`~org.orekit.time.FieldAbsoluteDate.toString`,
                :meth:`~org.orekit.time.DateTimeComponents.toString`
        
        """
        ...
    @typing.overload
    def toString(self, int: int) -> str:
        """
            Get a String representation of the instant location in ISO-8601 format without the UTC offset and with up to 16 digits
            of precision for the seconds value.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale to use
        
            Returns:
                a string representation of the instance.
        
            Also see:
                :meth:`~org.orekit.time.DateTimeComponents.toString`
        
            Get a String representation of the instant location for a local time.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC).
        
            Returns:
                string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
            Also see:
                :meth:`~org.orekit.time.FieldAbsoluteDate.toString`
        
            Get a String representation of the instant location for a local time.
        
            Parameters:
                minutesFromUTC (int): offset in *minutes* from UTC (positive Eastwards UTC, negative Westward UTC).
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
            Returns:
                string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
            Since:
                10.1
        
            Get a String representation of the instant location for a time zone.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                timeZone (TimeZone): time zone
        
            Returns:
                string representation of the instance, in ISO-8601 format with milliseconds accuracy
        
            Also see:
                :meth:`~org.orekit.time.FieldAbsoluteDate.toString`
        
            Get a String representation of the instant location for a time zone.
        
            Parameters:
                timeZone (TimeZone): time zone
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to compute date and time components.
        
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

class FixedStepSelector(DatesSelector):
    """
    public class FixedStepSelector extends Object implements :class:`~org.orekit.time.DatesSelector`
    
        Selector generating a continuous stream of dates separated by a constant step.
    
        The dates can be aligned to whole steps in some time scale. So for example if a step of 60s is used and the alignment
        time scale is set to :meth:`~org.orekit.time.TimeScales.getUTC`, dates will be selected at whole minutes in UTC time.
    
        BEWARE! This class stores internally the last selected dates, so it is *neither* reusable across several
        :class:`~org.orekit.estimation.measurements.generation.EventBasedScheduler` or
        :class:`~org.orekit.estimation.measurements.generation.ContinuousScheduler` schedulers, *nor* thread-safe. A separate
        selector should be used for each scheduler and for each thread in multi-threading context.
    
        Since:
            9.3
    """
    def __init__(self, double: float, timeScale: TimeScale): ...
    def selectDates(self, absoluteDate: AbsoluteDate, absoluteDate2: AbsoluteDate) -> java.util.List[AbsoluteDate]: ...

class GLONASSDate(java.io.Serializable, TimeStamped):
    """
    public class GLONASSDate extends Object implements Serializable, :class:`~org.orekit.time.TimeStamped`
    
        Container for date in GLONASS form.
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, "GLONASS Interface Control Document v1.0, 2016", :meth:`~serialized`
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
            Description copied from interface: :meth:`~org.orekit.time.TimeStamped.getDate`
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
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
    public class GLONASSScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        GLONASS time scale.
    
        By convention, TGLONASS = UTC + 3 hours.
    
        The time scale is defined in ` Global Navigation Sattelite System GLONASS - Interface Control document
        <http://www.spacecorp.ru/upload/iblock/1c4/cgs-aaixymyt%205.1%20ENG%20v%202014.02.18w.pdf>`, version 5.1 2008 (the typo
        in the title is in the original document title).
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    _getLeap_1__T = typing.TypeVar('_getLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLeap(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the value of the previous leap.
        
            This method will return 0.0 for all time scales that do *not* implement leap seconds.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                value of the previous leap
        
        """
        ...
    @typing.overload
    def getLeap(self, fieldAbsoluteDate: FieldAbsoluteDate[_getLeap_1__T]) -> _getLeap_1__T:
        """
            Get the value of the previous leap.
        
            This method will return 0.0 for all time scales that do *not* implement leap seconds.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                value of the previous leap
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _insideLeap_1__T = typing.TypeVar('_insideLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def insideLeap(self, absoluteDate: AbsoluteDate) -> bool:
        """
            Check if date is within a leap second introduction *in this time scale*.
        
            This method will return false for all time scales that do *not* implement leap seconds, even if the date corresponds to
            a leap second in :class:`~org.orekit.time.UTCScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.insideLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                true if time is within a leap second introduction
        
        """
        ...
    @typing.overload
    def insideLeap(self, fieldAbsoluteDate: FieldAbsoluteDate[_insideLeap_1__T]) -> bool:
        """
            Check if date is within a leap second introduction *in this time scale*.
        
            This method will return false for all time scales that do *not* implement leap seconds, even if the date corresponds to
            a leap second in :class:`~org.orekit.time.UTCScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.insideLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                true if time is within a leap second introduction
        
        
        """
        ...
    _minuteDuration_1__T = typing.TypeVar('_minuteDuration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def minuteDuration(self, absoluteDate: AbsoluteDate) -> int:
        """
            Check length of the current minute *in this time scale*.
        
            This method will return 60 for all time scales that do *not* implement leap seconds, even if the date corresponds to a
            leap second in :class:`~org.orekit.time.UTCScale`, and 61 for time scales that do implement leap second when the current
            date is within the last minute before the leap, or during the leap itself.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.minuteDuration` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                60 or 61 depending on leap seconds introduction
        
        """
        ...
    @typing.overload
    def minuteDuration(self, fieldAbsoluteDate: FieldAbsoluteDate[_minuteDuration_1__T]) -> int:
        """
            Check length of the current minute *in this time scale*.
        
            This method will return 60 for all time scales that do *not* implement leap seconds, even if the date corresponds to a
            leap second in :class:`~org.orekit.time.UTCScale`, and 61 for time scales that do implement leap second when the current
            date is within the last minute before the leap, or during the leap itself.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.minuteDuration` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                60 or 61 depending on leap seconds introduction
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class GMSTScale(TimeScale):
    """
    public class GMSTScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Greenwich Mean Sidereal Time.
    
        The Greenwich Mean Sidereal Time is the hour angle between the meridian of Greenwich and mean equinox of date at 0h UT1.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Since:
            5.1
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class GNSSDate(java.io.Serializable, TimeStamped):
    """
    public class GNSSDate extends Object implements Serializable, :class:`~org.orekit.time.TimeStamped`
    
        Container for date in GNSS form.
    
        This class can be used to handle :meth:`~org.orekit.gnss.SatelliteSystem.GPS`,
        :meth:`~org.orekit.gnss.SatelliteSystem.GALILEO`, :meth:`~org.orekit.gnss.SatelliteSystem.BEIDOU` and
        :meth:`~org.orekit.gnss.SatelliteSystem.QZSS` dates.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, int: int, double: float, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, int: int, double: float, satelliteSystem: org.orekit.gnss.SatelliteSystem, timeScales: TimeScales): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, satelliteSystem: org.orekit.gnss.SatelliteSystem): ...
    @typing.overload
    def __init__(self, absoluteDate: AbsoluteDate, satelliteSystem: org.orekit.gnss.SatelliteSystem, timeScales: TimeScales): ...
    def getDate(self) -> AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
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
                :meth:`~org.orekit.time.GNSSDate.setRolloverReference`, :meth:`~org.orekit.time.GNSSDate.GNSSDate`
        
        
        """
        ...
    def getWeekNumber(self) -> int:
        """
            Get the week number since the GNSS reference epoch.
        
            The week number returned here has been fixed for GNSS week rollover, i.e. it may be larger than the corresponding week
            cycle of the constellation.
        
            Returns:
                week number since since the GNSS reference epoch
        
        
        """
        ...
    @staticmethod
    def setRolloverReference(dateComponents: DateComponents) -> None:
        """
            Set a reference date for ensuring continuity across GNSS week rollover.
        
            Instance created using the :meth:`~org.orekit.time.GNSSDate.GNSSDate` constructor and with a week number between 0 and
            the constellation week cycle (cycleW) after this method has been called will fix the week number to ensure they
            correspond to dates between :code:`reference - cycleW / 2 weeks` and :code:`reference + cycleW / 2 weeks`.
        
            If this method is never called, a default reference date for rollover will be set using the date of the last known EOP
            entry retrieved from :meth:`~org.orekit.time.UT1Scale.getEOPHistory` time scale.
        
            Parameters:
                reference (:class:`~org.orekit.time.DateComponents`): reference date for GNSS week rollover
        
            Since:
                9.3.1
        
            Also see:
                :meth:`~org.orekit.time.GNSSDate.getRolloverReference`, :meth:`~org.orekit.time.GNSSDate.GNSSDate`
        
        
        """
        ...

class GPSScale(TimeScale):
    """
    public class GPSScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        GPS time scale.
    
        By convention, TGPS = TAI - 19 s.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class GalileoScale(TimeScale):
    """
    public class GalileoScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Galileo system time scale.
    
        By convention, TGST = UTC + 13s at Galileo epoch (1999-08-22T00:00:00Z).
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Galileo System Time and GPS time are very close scales. Without any errors, they should be identical. The offset between
        these two scales is the GGTO, it depends on the clocks used to realize the time scales. It is of the order of a few tens
        nanoseconds. This class does not implement this offset, so it is virtually identical to the
        :class:`~org.orekit.time.GPSScale`.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class IRNSSScale(TimeScale):
    """
    public class IRNSSScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        IRNSS time scale (also called IRNWT for IRNSS NetWork Time).
    
        By convention, TIRNSS = TAI - 19 s.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class PythonDatesSelector(DatesSelector):
    """
    public class PythonDatesSelector extends Object implements :class:`~org.orekit.time.DatesSelector`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
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
    def selectDates(self, absoluteDate: AbsoluteDate, absoluteDate2: AbsoluteDate) -> java.util.List[AbsoluteDate]: ...

_PythonFieldTimeInterpolable__T = typing.TypeVar('_PythonFieldTimeInterpolable__T', bound=FieldTimeInterpolable)  # <T>
_PythonFieldTimeInterpolable__KK = typing.TypeVar('_PythonFieldTimeInterpolable__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class PythonFieldTimeInterpolable(FieldTimeInterpolable[_PythonFieldTimeInterpolable__T, _PythonFieldTimeInterpolable__KK], typing.Generic[_PythonFieldTimeInterpolable__T, _PythonFieldTimeInterpolable__KK]):
    """
    public class PythonFieldTimeInterpolable<T extends :class:`~org.orekit.time.FieldTimeInterpolable`<T,KK>,KK extends CalculusFieldElement<KK>> extends Object implements :class:`~org.orekit.time.FieldTimeInterpolable`<T,KK>
    """
    def __init__(self): ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: FieldAbsoluteDate[_PythonFieldTimeInterpolable__KK], collection: typing.Union[java.util.Collection[_PythonFieldTimeInterpolable__T], typing.Sequence[_PythonFieldTimeInterpolable__T], typing.Set[_PythonFieldTimeInterpolable__T]]) -> _PythonFieldTimeInterpolable__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: FieldAbsoluteDate[_PythonFieldTimeInterpolable__KK], stream: java.util.stream.Stream[_PythonFieldTimeInterpolable__T]) -> _PythonFieldTimeInterpolable__T: ...

_PythonFieldTimeShiftable__T = typing.TypeVar('_PythonFieldTimeShiftable__T', bound=FieldTimeInterpolable)  # <T>
_PythonFieldTimeShiftable__KK = typing.TypeVar('_PythonFieldTimeShiftable__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class PythonFieldTimeShiftable(FieldTimeShiftable[_PythonFieldTimeShiftable__T, _PythonFieldTimeShiftable__KK], typing.Generic[_PythonFieldTimeShiftable__T, _PythonFieldTimeShiftable__KK]):
    """
    public class PythonFieldTimeShiftable<T extends :class:`~org.orekit.time.FieldTimeInterpolable`<T,KK>,KK extends CalculusFieldElement<KK>> extends Object implements :class:`~org.orekit.time.FieldTimeShiftable`<T,KK>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
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
    def shiftedBy(self, double: float) -> _PythonFieldTimeShiftable__T:
        """
            Get a time-shifted instance.
        
            Specified by:
                :meth:`~org.orekit.time.FieldTimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.FieldTimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
            Get a time-shifted instance. Calls the ShiftedByType Python extension method
        
            Specified by:
                :meth:`~org.orekit.time.FieldTimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.FieldTimeShiftable`
        
            Parameters:
                dt (:class:`~org.orekit.time.PythonFieldTimeShiftable`): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, kK: _PythonFieldTimeShiftable__KK) -> _PythonFieldTimeShiftable__T: ...
    def shiftedBy_KK(self, kK: _PythonFieldTimeShiftable__KK) -> _PythonFieldTimeShiftable__T:
        """
            Get a time-shifted instance. The Python extension method.
        
            Parameters:
                dt (:class:`~org.orekit.time.PythonFieldTimeShiftable`): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...

_PythonFieldTimeStamped__T = typing.TypeVar('_PythonFieldTimeStamped__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldTimeStamped(FieldTimeStamped[_PythonFieldTimeStamped__T], typing.Generic[_PythonFieldTimeStamped__T]):
    """
    public class PythonFieldTimeStamped<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.time.FieldTimeStamped`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getDate(self) -> FieldAbsoluteDate[_PythonFieldTimeStamped__T]: ...
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
    """
    public class PythonParser extends Object implements :class:`~org.orekit.time.UTCTAIOffsetsLoader.Parser`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...
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

_PythonTimeInterpolable__T = typing.TypeVar('_PythonTimeInterpolable__T', bound=TimeInterpolable)  # <T>
class PythonTimeInterpolable(TimeInterpolable[_PythonTimeInterpolable__T], typing.Generic[_PythonTimeInterpolable__T]):
    """
    public class PythonTimeInterpolable<T extends :class:`~org.orekit.time.TimeInterpolable`<T>> extends Object implements :class:`~org.orekit.time.TimeInterpolable`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, collection: typing.Union[java.util.Collection[_PythonTimeInterpolable__T], typing.Sequence[_PythonTimeInterpolable__T], typing.Set[_PythonTimeInterpolable__T]]) -> _PythonTimeInterpolable__T: ...
    @typing.overload
    def interpolate(self, absoluteDate: AbsoluteDate, stream: java.util.stream.Stream[_PythonTimeInterpolable__T]) -> _PythonTimeInterpolable__T: ...
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
    """
    public class PythonTimeScalarFunction extends Object implements :class:`~org.orekit.time.TimeScalarFunction`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
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
    def value(self, absoluteDate: AbsoluteDate) -> float:
        """
            Compute a function of time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScalarFunction.value` in interface :class:`~org.orekit.time.TimeScalarFunction`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
        
            Returns:
                value of the function
        
        """
        ...
    @typing.overload
    def value(self, fieldAbsoluteDate: FieldAbsoluteDate[_value_1__T]) -> _value_1__T:
        """
            Compute a function of time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScalarFunction.value` in interface :class:`~org.orekit.time.TimeScalarFunction`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
        
            Returns:
                value of the function
        
        
        """
        ...
    _value_F__T = typing.TypeVar('_value_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value_F(self, fieldAbsoluteDate: FieldAbsoluteDate[_value_F__T]) -> _value_F__T:
        """
            Compute a function of time.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
        
            Returns:
                value of the function
        
        
        """
        ...

class PythonTimeScale(TimeScale):
    """
    public class PythonTimeScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    _offsetFromTAI_F__T = typing.TypeVar('_offsetFromTAI_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def offsetFromTAI_F(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_F__T]) -> _offsetFromTAI_F__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
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
    """
    public class PythonTimeScales extends Object implements :class:`~org.orekit.time.TimeScales`
    """
    def __init__(self): ...
    def createBesselianEpoch(self, double: float) -> AbsoluteDate:
        """
            Build an instance corresponding to a Besselian Epoch (BE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Besselian Epoch is related to Julian Ephemeris Date
            as:
        
            .. code-block: java
            
            
             BE = 1900.0 + (JED - 2415020.31352) / 365.242198781
             
        
            This method reverts the formula above and computes an :code:`AbsoluteDate` from the Besselian Epoch.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.createBesselianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                besselianEpoch (double): Besselian epoch, like 1950 for defining the classical reference B1950.0
        
            Returns:
                a new instant
        
            Also see:
                :meth:`~org.orekit.time.PythonTimeScales.createJulianEpoch`
        
        
        """
        ...
    def createJulianEpoch(self, double: float) -> AbsoluteDate:
        """
            Build an instance corresponding to a Julian Epoch (JE).
        
            According to Lieske paper: ` Precession Matrix Based on IAU (1976) System of Astronomical Constants
            <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26A....73..282L&amp;defaultprint=YES&amp;filetype=.pdf.>`,
            Astronomy and Astrophysics, vol. 73, no. 3, Mar. 1979, p. 282-284, Julian Epoch is related to Julian Ephemeris Date as:
        
            .. code-block: java
            
            
             JE = 2000.0 + (JED - 2451545.0) / 365.25
             
        
            This method reverts the formula above and computes an :code:`AbsoluteDate` from the Julian Epoch.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.createJulianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                julianEpoch (double): Julian epoch, like 2000.0 for defining the classical reference J2000.0
        
            Returns:
                a new instant
        
            Also see:
                :meth:`~org.orekit.time.PythonTimeScales.getJ2000Epoch`, :meth:`~org.orekit.time.PythonTimeScales.createBesselianEpoch`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getBDT(self) -> BDTScale:
        """
            Get the BeiDou Navigation Satellite System time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getBDT` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    def getBeidouEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for BeiDou weeks: 2006-01-01T00:00:00 UTC.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getBeidouEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Beidou Epoch
        
        
        """
        ...
    def getCcsdsEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for CCSDS Time Code Format (CCSDS 301.0-B-4): 1958-01-01T00:00:00 International Atomic Time (*not* UTC).
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getCcsdsEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                CCSDS Epoch
        
        
        """
        ...
    def getFiftiesEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for 1950 dates: 1950-01-01T00:00:00 Terrestrial Time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getFiftiesEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Fifties Epoch
        
        
        """
        ...
    def getFutureInfinity(self) -> AbsoluteDate:
        """
            Dummy date at infinity in the future direction.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getFutureInfinity` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                the latest date.
        
        
        """
        ...
    def getGLONASS(self) -> GLONASSScale:
        """
            Get the GLObal NAvigation Satellite System time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGLONASS` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                GLObal NAvigation Satellite System time scale
        
        
        """
        ...
    def getGMST(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> GMSTScale:
        """
            Get the Greenwich Mean Sidereal Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGMST` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Greenwich Mean Sidereal Time scale
        
            Since:
                7.0
        
        
        """
        ...
    def getGPS(self) -> GPSScale:
        """
            Get the Global Positioning System scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGPS` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Global Positioning System scale
        
        
        """
        ...
    def getGST(self) -> GalileoScale:
        """
            Get the Galileo System Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGST` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Galileo System Time scale
        
        
        """
        ...
    def getGalileoEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for Galileo System Time: 1999-08-22T00:00:00 GST.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGalileoEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Galileo Epoch
        
        
        """
        ...
    def getGlonassEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for GLONASS four-year interval number: 1996-01-01T00:00:00 GLONASS time.
        
            By convention, TGLONASS = UTC + 3 hours.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGlonassEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                GLONASS Epoch
        
        
        """
        ...
    def getGpsEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for GPS weeks: 1980-01-06T00:00:00 GPS time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGpsEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                GPS Epoch
        
        
        """
        ...
    def getIRNSS(self) -> IRNSSScale:
        """
            Get the Indian Regional Navigation Satellite System time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getIRNSS` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Indian Regional Navigation Satellite System time scale
        
        
        """
        ...
    def getIrnssEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for IRNSS weeks: 1999-08-22T00:00:00 IRNSS time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getIrnssEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                IRNSS Epoch
        
        
        """
        ...
    def getJ2000Epoch(self) -> AbsoluteDate:
        """
            J2000.0 Reference epoch: 2000-01-01T12:00:00 Terrestrial Time (*not* UTC).
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getJ2000Epoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                J2000 Epoch
        
            Also see:
                :meth:`~org.orekit.time.AbsoluteDate.createJulianEpoch`, :meth:`~org.orekit.time.AbsoluteDate.createBesselianEpoch`
        
        
        """
        ...
    def getJavaEpoch(self) -> AbsoluteDate:
        """
            Java Reference epoch: 1970-01-01T00:00:00 Universal Time Coordinate.
        
            Between 1968-02-01 and 1972-01-01, UTC-TAI = 4.213 170 0s + (MJD - 39 126) x 0.002 592s. As on 1970-01-01 MJD = 40587,
            UTC-TAI = 8.000082s
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getJavaEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Java Epoch
        
        
        """
        ...
    def getJulianEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for julian dates: -4712-01-01T12:00:00 Terrestrial Time.
        
            Both :code:`java.util.Date` and :class:`~org.orekit.time.DateComponents` classes follow the astronomical conventions and
            consider a year 0 between years -1 and +1, hence this reference date lies in year -4712 and not in year -4713 as can be
            seen in other documents or programs that obey a different convention (for example the :code:`convcal` utility).
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getJulianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Julian epoch.
        
        
        """
        ...
    def getModifiedJulianEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for modified julian dates: 1858-11-17T00:00:00 Terrestrial Time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getModifiedJulianEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Modified Julian Epoch
        
        
        """
        ...
    def getPastInfinity(self) -> AbsoluteDate:
        """
            Dummy date at infinity in the past direction.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getPastInfinity` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                the earliest date.
        
        
        """
        ...
    def getQZSS(self) -> 'QZSSScale':
        """
            Get the Quasi-Zenith Satellite System time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getQZSS` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    def getQzssEpoch(self) -> AbsoluteDate:
        """
            Reference epoch for QZSS weeks: 1980-01-06T00:00:00 QZSS time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getQzssEpoch` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                QZSS Epoch
        
        
        """
        ...
    def getTAI(self) -> 'TAIScale':
        """
            Get the International Atomic Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getTAI` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                International Atomic Time scale
        
        
        """
        ...
    def getTCB(self) -> 'TCBScale':
        """
            Get the Barycentric Coordinate Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getTCB` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Barycentric Coordinate Time scale
        
        
        """
        ...
    def getTCG(self) -> 'TCGScale':
        """
            Get the Geocentric Coordinate Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getTCG` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Geocentric Coordinate Time scale
        
        
        """
        ...
    def getTDB(self) -> 'TDBScale':
        """
            Get the Barycentric Dynamic Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getTDB` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Barycentric Dynamic Time scale
        
        
        """
        ...
    def getTT(self) -> 'TTScale':
        """
            Get the Terrestrial Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getTT` in interface :class:`~org.orekit.time.TimeScales`
        
            Returns:
                Terrestrial Time scale
        
        
        """
        ...
    def getUT1(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'UT1Scale':
        """
            Get the Universal Time 1 scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getUT1` in interface :class:`~org.orekit.time.TimeScales`
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Universal Time 1 scale
        
            Also see:
                :meth:`~org.orekit.time.PythonTimeScales.getUTC`
        
        
        """
        ...
    def getUTC(self) -> 'UTCScale':
        """
            Get the Universal Time Coordinate scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getUTC` in interface :class:`~org.orekit.time.TimeScales`
        
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
    """
    public class PythonTimeShiftable<T extends :class:`~org.orekit.time.TimeShiftable`<T>> extends Object implements :class:`~org.orekit.time.TimeShiftable`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
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
    def shiftedBy(self, double: float) -> _PythonTimeShiftable__T:
        """
            Get a time-shifted instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...

class PythonTimeStamped(TimeStamped):
    """
    public class PythonTimeStamped extends Object implements :class:`~org.orekit.time.TimeStamped`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getDate(self) -> AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
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
    """
    public class PythonTimeVectorFunction extends Object implements :class:`~org.orekit.time.TimeVectorFunction`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
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
    def value(self, absoluteDate: AbsoluteDate) -> typing.List[float]:
        """
            Compute a function of time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeVectorFunction.value` in interface :class:`~org.orekit.time.TimeVectorFunction`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
        
            Returns:
                value of the function
        
        """
        ...
    @typing.overload
    def value(self, fieldAbsoluteDate: FieldAbsoluteDate[_value_1__T]) -> typing.List[_value_1__T]:
        """
            Compute a function of time.
        
            Specified by:
                :meth:`~org.orekit.time.TimeVectorFunction.value` in interface :class:`~org.orekit.time.TimeVectorFunction`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
        
            Returns:
                value of the function
        
        
        """
        ...
    _value_F__T = typing.TypeVar('_value_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def value_F(self, fieldAbsoluteDate: FieldAbsoluteDate[_value_F__T]) -> typing.List[_value_F__T]:
        """
            Compute a function of time.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
        
            Returns:
                value of the function
        
        
        """
        ...

class PythonUTCTAIOffsetsLoader(UTCTAIOffsetsLoader):
    """
    public class PythonUTCTAIOffsetsLoader extends Object implements :class:`~org.orekit.time.UTCTAIOffsetsLoader`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def loadOffsets(self) -> java.util.List[OffsetModel]: ...
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

class QZSSScale(TimeScale):
    """
    public class QZSSScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        QZSS time scale.
    
        By convention, TQZSS = TAI - 19 s.
    
        The time scale is defined in ` Quasi-Zenith Satellite System Navigation Service - Interface Specification for QZSS
        <http://qzss.go.jp/en/technical/download/pdf/ps-is-qzss/is-qzss-pnt-003.pdf?t=1549268771755>` version 1.6, 2014.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SatelliteClockScale(TimeScale):
    """
    public class SatelliteClockScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Scale for on-board clock.
    
        Since:
            11.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, absoluteDate: AbsoluteDate, timeScale: TimeScale, double: float, double2: float): ...
    def countAtDate(self, absoluteDate: AbsoluteDate) -> float:
        """
            Compute clock count corresponding to some date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
        
            Returns:
                clock count at :code:`date`
        
        
        """
        ...
    def dateAtCount(self, double: float) -> AbsoluteDate:
        """
            Compute date corresponding to some clock count.
        
            Parameters:
                count (double): clock count
        
            Returns:
                date at :code:`count`
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TAIScale(TimeScale):
    """
    public class TAIScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        International Atomic Time.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                taiTime (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TAIUTCDatFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    public class TAIUTCDatFilesLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.time.UTCTAIOffsetsLoader`
    
        Loader for UTC-TAI extracted from tai-utc.dat file from USNO.
    
        This class is immutable and hence thread-safe
    
        Since:
            7.1
    """
    DEFAULT_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_SUPPORTED_NAMES
    
        Default supported files name pattern.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]: ...
    class Parser(UTCTAIOffsetsLoader.Parser):
        def __init__(self): ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class TCBScale(TimeScale):
    """
    public class TCBScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Barycentric Coordinate Time.
    
        Coordinate time at the center of mass of the Solar System. This time scale depends linearly from
        :class:`~org.orekit.time.TDBScale`.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TCGScale(TimeScale):
    """
    public class TCGScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Geocentric Coordinate Time.
    
        Coordinate time at the center of mass of the Earth. This time scale depends linearly from
        :class:`~org.orekit.time.TTScale`.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TDBScale(TimeScale):
    """
    public class TDBScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Barycentric Dynamic Time.
    
        Time used to take account of time dilation when calculating orbits of planets, asteroids, comets and interplanetary
        spacecraft in the Solar system. It was based on a Dynamical time scale but was not well defined and not rigorously
        correct as a relativistic time scale. It was subsequently deprecated in favour of Barycentric Coordinate Time (TCB), but
        at the 2006 General Assembly of the International Astronomical Union TDB was rehabilitated by making it a specific fixed
        linear transformation of TCB.
    
        By convention, TDB = TT + 0.001658 sin(g) + 0.000014 sin(2g)seconds where g = 357.53 + 0.9856003 (JD - 2451545) degrees.
    
        Also see:
            :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TTScale(TimeScale):
    """
    public class TTScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Terrestrial Time as defined by IAU(1991) recommendation IV.
    
        Coordinate time at the surface of the Earth. IT is the successor of Ephemeris Time TE.
    
        By convention, TT = TAI + 32.184 s.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UT1Scale(TimeScale):
    """
    public class UT1Scale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Universal Time 1.
    
        UT1 is a time scale directly linked to the actual rotation of the Earth. It is an irregular scale, reflecting Earth
        irregular rotation rate. The offset between UT1 and :class:`~org.orekit.time.UTCScale` is found in the Earth Orientation
        Parameters published by IERS.
    
        Since:
            5.1
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
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
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
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
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UTCScale(TimeScale):
    """
    public class UTCScale extends Object implements :class:`~org.orekit.time.TimeScale`
    
        Coordinated Universal Time.
    
        UTC is related to TAI using step adjustments from time to time according to IERS (International Earth Rotation Service)
        rules. Before 1972, these adjustments were piecewise linear offsets. Since 1972, these adjustments are piecewise
        constant offsets, which require introduction of leap seconds.
    
        Leap seconds are always inserted as additional seconds at the last minute of the day, pushing the next day forward. Such
        minutes are therefore more than 60 seconds long. In theory, there may be seconds removal instead of seconds insertion,
        but up to now (2010) it has never been used. As an example, when a one second leap was introduced at the end of 2005,
        the UTC time sequence was 2005-12-31T23:59:59 UTC, followed by 2005-12-31T23:59:60 UTC, followed by 2006-01-01T00:00:00
        UTC.
    
        This is intended to be accessed thanks to :class:`~org.orekit.time.TimeScales`, so there is no public constructor.
    
        Also see:
            :class:`~org.orekit.time.AbsoluteDate`, :meth:`~serialized`
    """
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
    _getLeap_1__T = typing.TypeVar('_getLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLeap(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the value of the previous leap.
        
            This method will return 0.0 for all time scales that do *not* implement leap seconds.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                value of the previous leap
        
        """
        ...
    @typing.overload
    def getLeap(self, fieldAbsoluteDate: FieldAbsoluteDate[_getLeap_1__T]) -> _getLeap_1__T:
        """
            Get the value of the previous leap.
        
            This method will return 0.0 for all time scales that do *not* implement leap seconds.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                value of the previous leap
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.getName` in interface :class:`~org.orekit.time.TimeScale`
        
            Returns:
                name of the time scale
        
        
        """
        ...
    def getUTCTAIOffsets(self) -> java.util.List['UTCTAIOffset']: ...
    _insideLeap_1__T = typing.TypeVar('_insideLeap_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def insideLeap(self, absoluteDate: AbsoluteDate) -> bool:
        """
            Check if date is within a leap second introduction *in this time scale*.
        
            This method will return false for all time scales that do *not* implement leap seconds, even if the date corresponds to
            a leap second in :class:`~org.orekit.time.UTCScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.insideLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                true if time is within a leap second introduction
        
        """
        ...
    @typing.overload
    def insideLeap(self, fieldAbsoluteDate: FieldAbsoluteDate[_insideLeap_1__T]) -> bool:
        """
            Check if date is within a leap second introduction *in this time scale*.
        
            This method will return false for all time scales that do *not* implement leap seconds, even if the date corresponds to
            a leap second in :class:`~org.orekit.time.UTCScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.insideLeap` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                true if time is within a leap second introduction
        
        
        """
        ...
    _minuteDuration_1__T = typing.TypeVar('_minuteDuration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def minuteDuration(self, absoluteDate: AbsoluteDate) -> int:
        """
            Check length of the current minute *in this time scale*.
        
            This method will return 60 for all time scales that do *not* implement leap seconds, even if the date corresponds to a
            leap second in :class:`~org.orekit.time.UTCScale`, and 61 for time scales that do implement leap second when the current
            date is within the last minute before the leap, or during the leap itself.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.minuteDuration` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date to check
        
            Returns:
                60 or 61 depending on leap seconds introduction
        
        """
        ...
    @typing.overload
    def minuteDuration(self, fieldAbsoluteDate: FieldAbsoluteDate[_minuteDuration_1__T]) -> int:
        """
            Check length of the current minute *in this time scale*.
        
            This method will return 60 for all time scales that do *not* implement leap seconds, even if the date corresponds to a
            leap second in :class:`~org.orekit.time.UTCScale`, and 61 for time scales that do implement leap second when the current
            date is within the last minute before the leap, or during the leap itself.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.minuteDuration` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date to check
        
            Returns:
                60 or 61 depending on leap seconds introduction
        
        
        """
        ...
    _offsetFromTAI_1__T = typing.TypeVar('_offsetFromTAI_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def offsetFromTAI(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        """
        ...
    @typing.overload
    def offsetFromTAI(self, fieldAbsoluteDate: FieldAbsoluteDate[_offsetFromTAI_1__T]) -> _offsetFromTAI_1__T:
        """
            Get the offset to convert locations from :class:`~org.orekit.time.TAIScale` to instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): conversion date
        
            Returns:
                offset in seconds to add to a location in *:class:`~org.orekit.time.TAIScale` time scale* to get a location in *instance
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI`
        
        
        """
        ...
    def offsetToTAI(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float:
        """
            Get the offset to convert locations from instance to :class:`~org.orekit.time.TAIScale`.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScale.offsetToTAI` in interface :class:`~org.orekit.time.TimeScale`
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date location in the time scale
                time (:class:`~org.orekit.time.TimeComponents`): time location in the time scale
        
            Returns:
                offset in seconds to add to a location in *instance time scale* to get a location in *:class:`~org.orekit.time.TAIScale`
                time scale*
        
            Also see:
                :meth:`~org.orekit.time.TimeScale.offsetFromTAI`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UTCTAIBulletinAFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    public class UTCTAIBulletinAFilesLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.time.UTCTAIOffsetsLoader`
    
        Loader for UTC-TAI extracted from bulletin A files.
    
        This class is a modified version of :code:`BulletinAFileLoader` that only parses the TAI-UTC header line and checks the
        UT1-UTC column for discontinuities.
    
        Note that extracting UTC-TAI from bulletin A files is *NOT* recommended. There are known issues in some past bulletin A
        (for example bulletina-xix-001.txt from 2006-01-05 has a wrong year for last leap second and bulletina-xxi-053.txt from
        2008-12-31 has an off by one value for TAI-UTC on MJD 54832). This is a known problem, and the Earth Orientation
        Department at USNO told us this TAI-UTC data was only provided as a convenience and this data should rather be sourced
        from other official files. As the bulletin A files are a record of past publications, they cannot modify archived
        bulletins, hence the errors above will remain forever. This UTC-TAI loader should therefore be used with great care.
    
        This class is immutable and hence thread-safe
    
        Since:
            7.1
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]: ...

class UTCTAIHistoryFilesLoader(org.orekit.data.AbstractSelfFeedingLoader, UTCTAIOffsetsLoader):
    """
    public class UTCTAIHistoryFilesLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.time.UTCTAIOffsetsLoader`
    
        Loader for UTC versus TAI history files.
    
        UTC versus TAI history files contain :class:`~org.orekit.time.UTCTAIOffset` data since.
    
        The UTC versus TAI history files are recognized thanks to their base names, which must match the pattern
        :code:`UTC-TAI.history` (or :code:`UTC-TAI.history.gz` for gzip-compressed files)
    
        Only one history file must be present in the IERS directories hierarchy.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def loadOffsets(self) -> java.util.List[OffsetModel]: ...
    class Parser(UTCTAIOffsetsLoader.Parser):
        def __init__(self): ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[OffsetModel]: ...

class UTCTAIOffset(TimeStamped, java.io.Serializable):
    """
    public class UTCTAIOffset extends Object implements :class:`~org.orekit.time.TimeStamped`, Serializable
    
        Offset between :class:`~org.orekit.time.UTCScale` and :class:`~org.orekit.time.TAIScale` time scales.
    
        The :class:`~org.orekit.time.UTCScale` and :class:`~org.orekit.time.TAIScale` time scales are two scales offset with
        respect to each other. The :class:`~org.orekit.time.TAIScale` scale is continuous whereas the
        :class:`~org.orekit.time.UTCScale` includes some discontinuity when leap seconds are introduced by the `International
        Earth Rotation Service <http://www.iers.org/>` (IERS).
    
        This class represents the offset between the two scales that is valid between two leap seconds occurrences. It handles
        both the linear offsets used from 1961-01-01 to 1971-12-31 and the constant integer offsets used since 1972-01-01.
    
        Also see:
            :class:`~org.orekit.time.UTCScale`, :class:`~org.orekit.time.UTCTAIHistoryFilesLoader`, :meth:`~serialized`
    """
    def getDate(self) -> AbsoluteDate:
        """
            Get the date of the start of the leap.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date of the start of the leap
        
            Also see:
                :meth:`~org.orekit.time.UTCTAIOffset.getValidityStart`
        
        
        """
        ...
    def getLeap(self) -> float:
        """
            Get the value of the leap at offset validity start (in seconds).
        
            Returns:
                value of the leap at offset validity start (in seconds)
        
        
        """
        ...
    def getMJD(self) -> int:
        """
            Get the date of the start of the leap as Modified Julian Day.
        
            Returns:
                date of the start of the leap as Modified Julian Day
        
        
        """
        ...
    _getOffset_2__T = typing.TypeVar('_getOffset_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getOffset(self, absoluteDate: AbsoluteDate) -> float:
        """
            Get the TAI - UTC offset in seconds.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the offset is requested
        
            Returns:
                TAI - UTC offset in seconds.
        
            Get the TAI - UTC offset in seconds.
        
            Parameters:
                date (:class:`~org.orekit.time.DateComponents`): date components (in UTC) at which the offset is requested
                time (:class:`~org.orekit.time.TimeComponents`): time components (in UTC) at which the offset is requested
        
            Returns:
                TAI - UTC offset in seconds.
        
        
        """
        ...
    @typing.overload
    def getOffset(self, dateComponents: DateComponents, timeComponents: TimeComponents) -> float: ...
    @typing.overload
    def getOffset(self, fieldAbsoluteDate: FieldAbsoluteDate[_getOffset_2__T]) -> _getOffset_2__T:
        """
            Get the TAI - UTC offset in seconds.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which the offset is requested
        
            Returns:
                TAI - UTC offset in seconds.
        
            Since:
                9.0
        
        """
        ...
    def getValidityStart(self) -> AbsoluteDate:
        """
            Get the start time of validity for this offset.
        
            The start of the validity of the offset is :meth:`~org.orekit.time.UTCTAIOffset.getLeap` seconds after the start of the
            leap itself.
        
            Returns:
                start of validity date
        
            Also see:
                :meth:`~org.orekit.time.UTCTAIOffset.getDate`
        
        
        """
        ...

class LazyLoadedTimeScales(AbstractTimeScales):
    """
    public class LazyLoadedTimeScales extends :class:`~org.orekit.time.AbstractTimeScales`
    
        An implementation of :class:`~org.orekit.time.TimeScales` that loads auxiliary data, leap seconds and UT1-UTC, when it
        is first accessed. The list of loaders may be modified before the first data access.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.time.TimeScalesFactory`
    """
    def __init__(self, lazyLoadedEop: org.orekit.frames.LazyLoadedEop): ...
    def addDefaultUTCTAIOffsetsLoaders(self) -> None:
        """
            Add the default loaders for UTC-TAI offsets history files (both IERS and USNO).
        
            The default loaders are :class:`~org.orekit.time.TAIUTCDatFilesLoader` that looks for a file named :code:`tai-utc.dat`
            that must be in USNO format, :class:`~org.orekit.time.UTCTAIHistoryFilesLoader` that looks for a file named
            :code:`UTC-TAI.history` that must be in the IERS format and :class:`~org.orekit.time.AGILeapSecondFilesLoader` that
            looks for a files named :code:`LeapSecond.dat` that must be in AGI format. The
            :class:`~org.orekit.time.UTCTAIBulletinAFilesLoader` is*not* added by default as it is not recommended. USNO warned us
            that the TAI-UTC data present in bulletin A was for convenience only and was not reliable, there have been errors in
            several bulletins regarding these data.
        
            Since:
                7.1
        
            Also see:
                `USNO tai-utc.dat file <http://maia.usno.navy.mil/ser7/tai-utc.dat>`, `IERS UTC-TAI.history file
                <http://hpiers.obspm.fr/eoppc/bul/bulc/UTC-TAI.history>`, :class:`~org.orekit.time.TAIUTCDatFilesLoader`,
                :class:`~org.orekit.time.UTCTAIHistoryFilesLoader`, :class:`~org.orekit.time.AGILeapSecondFilesLoader`,
                :meth:`~org.orekit.time.LazyLoadedTimeScales.getUTC`,
                :meth:`~org.orekit.time.LazyLoadedTimeScales.clearUTCTAIOffsetsLoaders`
        
        
        """
        ...
    def addUTCTAIOffsetsLoader(self, uTCTAIOffsetsLoader: UTCTAIOffsetsLoader) -> None:
        """
            Add a loader for UTC-TAI offsets history files.
        
            Parameters:
                loader (:class:`~org.orekit.time.UTCTAIOffsetsLoader`): custom loader to add
        
            Since:
                7.1
        
            Also see:
                :class:`~org.orekit.time.TAIUTCDatFilesLoader`, :class:`~org.orekit.time.UTCTAIHistoryFilesLoader`,
                :class:`~org.orekit.time.UTCTAIBulletinAFilesLoader`, :meth:`~org.orekit.time.LazyLoadedTimeScales.getUTC`,
                :meth:`~org.orekit.time.LazyLoadedTimeScales.clearUTCTAIOffsetsLoaders`
        
        
        """
        ...
    def clearUTCTAIOffsetsLoaders(self) -> None:
        """
            Clear loaders for UTC-TAI offsets history files.
        
            Since:
                7.1
        
            Also see:
                :meth:`~org.orekit.time.LazyLoadedTimeScales.getUTC`,
                :meth:`~org.orekit.time.LazyLoadedTimeScales.addUTCTAIOffsetsLoader`,
                :meth:`~org.orekit.time.LazyLoadedTimeScales.addDefaultUTCTAIOffsetsLoaders`
        
        
        """
        ...
    def getBDT(self) -> BDTScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getBDT`
            Get the BeiDou Navigation Satellite System time scale.
        
            Returns:
                BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    def getGLONASS(self) -> GLONASSScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGLONASS`
            Get the GLObal NAvigation Satellite System time scale.
        
            Returns:
                GLObal NAvigation Satellite System time scale
        
        
        """
        ...
    def getGMST(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> GMSTScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGMST`
            Get the Greenwich Mean Sidereal Time scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getGMST` in interface :class:`~org.orekit.time.TimeScales`
        
            Overrides:
                :meth:`~org.orekit.time.AbstractTimeScales.getGMST` in class :class:`~org.orekit.time.AbstractTimeScales`
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Greenwich Mean Sidereal Time scale
        
        
        """
        ...
    def getGPS(self) -> GPSScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGPS`
            Get the Global Positioning System scale.
        
            Returns:
                Global Positioning System scale
        
        
        """
        ...
    def getGST(self) -> GalileoScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getGST`
            Get the Galileo System Time scale.
        
            Returns:
                Galileo System Time scale
        
        
        """
        ...
    def getIRNSS(self) -> IRNSSScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getIRNSS`
            Get the Indian Regional Navigation Satellite System time scale.
        
            Returns:
                Indian Regional Navigation Satellite System time scale
        
        
        """
        ...
    def getQZSS(self) -> QZSSScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getQZSS`
            Get the Quasi-Zenith Satellite System time scale.
        
            Returns:
                Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    def getTAI(self) -> TAIScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getTAI`
            Get the International Atomic Time scale.
        
            Returns:
                International Atomic Time scale
        
        
        """
        ...
    def getTCB(self) -> TCBScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getTCB`
            Get the Barycentric Coordinate Time scale.
        
            Returns:
                Barycentric Coordinate Time scale
        
        
        """
        ...
    def getTCG(self) -> TCGScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getTCG`
            Get the Geocentric Coordinate Time scale.
        
            Returns:
                Geocentric Coordinate Time scale
        
        
        """
        ...
    def getTDB(self) -> TDBScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getTDB`
            Get the Barycentric Dynamic Time scale.
        
            Returns:
                Barycentric Dynamic Time scale
        
        
        """
        ...
    def getTT(self) -> TTScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getTT`
            Get the Terrestrial Time scale.
        
            Returns:
                Terrestrial Time scale
        
        
        """
        ...
    @typing.overload
    def getUT1(self, eOPHistory: org.orekit.frames.EOPHistory) -> UT1Scale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getUT1`
            Get the Universal Time 1 scale.
        
            Specified by:
                :meth:`~org.orekit.time.TimeScales.getUT1` in interface :class:`~org.orekit.time.TimeScales`
        
            Overrides:
                :meth:`~org.orekit.time.AbstractTimeScales.getUT1` in class :class:`~org.orekit.time.AbstractTimeScales`
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions for which EOP parameters will provide dUT1
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Universal Time 1 scale
        
            Also see:
                :meth:`~org.orekit.time.TimeScales.getUTC`, :meth:`~org.orekit.frames.Frames.getEOPHistory`
        
            Get the Universal Time 1 scale.
        
            As this method allow associating any history with the time scale, it may involve large data sets. So this method does
            *not* cache the resulting :class:`~org.orekit.time.UT1Scale` instance, a new instance will be returned each time. In
            order to avoid wasting memory, calling :meth:`~org.orekit.time.AbstractTimeScales.getUT1` with the single enumerate
            corresponding to the conventions may be a better solution. This method is made available only for expert use.
        
            Overrides:
                :meth:`~org.orekit.time.AbstractTimeScales.getUT1` in class :class:`~org.orekit.time.AbstractTimeScales`
        
            Parameters:
                history (:class:`~org.orekit.frames.EOPHistory`): EOP parameters providing dUT1 (may be null if no correction is desired)
        
            Returns:
                Universal Time 1 scale
        
            Also see:
                :meth:`~org.orekit.time.AbstractTimeScales.getUT1`
        
        
        """
        ...
    @typing.overload
    def getUT1(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> UT1Scale: ...
    def getUTC(self) -> UTCScale:
        """
            Description copied from interface: :meth:`~org.orekit.time.TimeScales.getUTC`
            Get the Universal Time Coordinate scale.
        
            Returns:
                Universal Time Coordinate scale
        
        
        """
        ...

class PythonAbstractTimeScales(AbstractTimeScales):
    """
    public class PythonAbstractTimeScales extends :class:`~org.orekit.time.AbstractTimeScales`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getBDT(self) -> BDTScale:
        """
            Get the BeiDou Navigation Satellite System time scale.
        
            Returns:
                BeiDou Navigation Satellite System time scale
        
        
        """
        ...
    def getEopHistory(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> org.orekit.frames.EOPHistory:
        """
            Get the EOP history for the given conventions.
        
            Specified by:
                :meth:`~org.orekit.time.AbstractTimeScales.getEopHistory` in class :class:`~org.orekit.time.AbstractTimeScales`
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): to use in computing the EOP history.
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
    def getIRNSS(self) -> IRNSSScale:
        """
            Get the Indian Regional Navigation Satellite System time scale.
        
            Returns:
                Indian Regional Navigation Satellite System time scale
        
        
        """
        ...
    def getQZSS(self) -> QZSSScale:
        """
            Get the Quasi-Zenith Satellite System time scale.
        
            Returns:
                Quasi-Zenith Satellite System time scale
        
        
        """
        ...
    def getTAI(self) -> TAIScale:
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
    def getTT(self) -> TTScale:
        """
            Get the Terrestrial Time scale.
        
            Returns:
                Terrestrial Time scale
        
        
        """
        ...
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.time")``.

    AGILeapSecondFilesLoader: typing.Type[AGILeapSecondFilesLoader]
    AbsoluteDate: typing.Type[AbsoluteDate]
    AbstractTimeScales: typing.Type[AbstractTimeScales]
    BDTScale: typing.Type[BDTScale]
    BurstSelector: typing.Type[BurstSelector]
    ChronologicalComparator: typing.Type[ChronologicalComparator]
    DateComponents: typing.Type[DateComponents]
    DateTimeComponents: typing.Type[DateTimeComponents]
    DatesSelector: typing.Type[DatesSelector]
    FieldAbsoluteDate: typing.Type[FieldAbsoluteDate]
    FieldTimeInterpolable: typing.Type[FieldTimeInterpolable]
    FieldTimeShiftable: typing.Type[FieldTimeShiftable]
    FieldTimeStamped: typing.Type[FieldTimeStamped]
    FixedStepSelector: typing.Type[FixedStepSelector]
    GLONASSDate: typing.Type[GLONASSDate]
    GLONASSScale: typing.Type[GLONASSScale]
    GMSTScale: typing.Type[GMSTScale]
    GNSSDate: typing.Type[GNSSDate]
    GPSScale: typing.Type[GPSScale]
    GalileoScale: typing.Type[GalileoScale]
    IRNSSScale: typing.Type[IRNSSScale]
    LazyLoadedTimeScales: typing.Type[LazyLoadedTimeScales]
    Month: typing.Type[Month]
    OffsetModel: typing.Type[OffsetModel]
    PythonAbstractTimeScales: typing.Type[PythonAbstractTimeScales]
    PythonDatesSelector: typing.Type[PythonDatesSelector]
    PythonFieldTimeInterpolable: typing.Type[PythonFieldTimeInterpolable]
    PythonFieldTimeShiftable: typing.Type[PythonFieldTimeShiftable]
    PythonFieldTimeStamped: typing.Type[PythonFieldTimeStamped]
    PythonParser: typing.Type[PythonParser]
    PythonTimeInterpolable: typing.Type[PythonTimeInterpolable]
    PythonTimeScalarFunction: typing.Type[PythonTimeScalarFunction]
    PythonTimeScale: typing.Type[PythonTimeScale]
    PythonTimeScales: typing.Type[PythonTimeScales]
    PythonTimeShiftable: typing.Type[PythonTimeShiftable]
    PythonTimeStamped: typing.Type[PythonTimeStamped]
    PythonTimeVectorFunction: typing.Type[PythonTimeVectorFunction]
    PythonUTCTAIOffsetsLoader: typing.Type[PythonUTCTAIOffsetsLoader]
    QZSSScale: typing.Type[QZSSScale]
    SatelliteClockScale: typing.Type[SatelliteClockScale]
    TAIScale: typing.Type[TAIScale]
    TAIUTCDatFilesLoader: typing.Type[TAIUTCDatFilesLoader]
    TCBScale: typing.Type[TCBScale]
    TCGScale: typing.Type[TCGScale]
    TDBScale: typing.Type[TDBScale]
    TTScale: typing.Type[TTScale]
    TimeComponents: typing.Type[TimeComponents]
    TimeInterpolable: typing.Type[TimeInterpolable]
    TimeScalarFunction: typing.Type[TimeScalarFunction]
    TimeScale: typing.Type[TimeScale]
    TimeScales: typing.Type[TimeScales]
    TimeScalesFactory: typing.Type[TimeScalesFactory]
    TimeShiftable: typing.Type[TimeShiftable]
    TimeStamped: typing.Type[TimeStamped]
    TimeVectorFunction: typing.Type[TimeVectorFunction]
    UT1Scale: typing.Type[UT1Scale]
    UTCScale: typing.Type[UTCScale]
    UTCTAIBulletinAFilesLoader: typing.Type[UTCTAIBulletinAFilesLoader]
    UTCTAIHistoryFilesLoader: typing.Type[UTCTAIHistoryFilesLoader]
    UTCTAIOffset: typing.Type[UTCTAIOffset]
    UTCTAIOffsetsLoader: typing.Type[UTCTAIOffsetsLoader]
