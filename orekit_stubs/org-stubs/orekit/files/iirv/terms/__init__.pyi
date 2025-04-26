
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.data
import org.orekit.files.iirv.terms.base
import org.orekit.frames
import org.orekit.time
import typing



class CheckSumTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class CheckSumTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        Three-character checksum to validate message.
    
        Calculated by summing the decimal equivalent of the preceding characters in the line, counting spaces as 0 and negative
        signs as 1:
    
          - 0 through 9 = face value
          - Minus (-) = 1
          - ASCII Space = 0
    
    
        Valid Values: 000-999
    
        Since:
            13.0
    """
    CHECK_SUM_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int CHECK_SUM_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CHECK_SUM_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CHECK_SUM_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...
    @staticmethod
    def computeChecksum(string: str) -> int:
        """
            Computes the sum of the decimal equivalent of characters in the line, counting spaces as 0 and negative signs as 1.
        
            Parameters:
                input (:class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): input string to compute checksum from
        
            Returns:
                computed checksum integer value
        
        
        """
        ...
    @staticmethod
    def fromIIRVTerms(*iIRVVectorTerm: org.orekit.files.iirv.terms.base.IIRVVectorTerm[typing.Any]) -> 'CheckSumTerm': ...
    def validateAgainstLineString(self, string: str) -> bool:
        """
            Validate the checksum from a line based on the object's checksum integer value.
        
            Parameters:
                line (:class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string line of an IIRV message (including checksum as the final three characters)
        
            Returns:
                true if the extracted checksum value matches this object's integer value
        
        
        """
        ...
    @staticmethod
    def validateLineCheckSum(string: str) -> bool:
        """
            Validate a line's embedded checksum value.
        
            Parameters:
                line (:class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string line of an IIRV message (including checksum as the final three characters)
        
            Returns:
                true if the derived and embedded checksum values are equal
        
        
        """
        ...

class CoordinateSystemTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class CoordinateSystemTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        1-character representing the coordinate system associated with the state variables.
    
        Valid values:
    
          - 1 = Geocentric True-of-Date Rotating
          - 2 = Geocentric mean of 1950.0 (B1950.0)
          - 3 = Heliocentric B1950.0
          - 4 = Reserved for JPL use (non-GSFC)
          - 5 = Reserved for JPL use (non-GSFC)
          - 6 = Geocentric mean of 2000.0 (J2000.0)
          - 7 = Heliocentric J2000.0
    
    
        Since:
            13.0
    """
    GEOCENTRIC_TRUE_OF_DATE_ROTATING: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CoordinateSystemTerm` GEOCENTRIC_TRUE_OF_DATE_ROTATING
    
        Geocentric True-of-Date Rotating (GTOD) CoordinateSystemTerm.
    
        Also known as True of Date Rotating frame (TDR) or Greenwich Rotating Coordinate frame (GCR).
    
    """
    GEOCENTRIC_MEAN_B1950: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CoordinateSystemTerm` GEOCENTRIC_MEAN_B1950
    
        Geocentric mean of 1950.0 (B1950.0) CoordinateSystemTerm.
    
    """
    HELIOCENTRIC_B1950: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CoordinateSystemTerm` HELIOCENTRIC_B1950
    
        Heliocentric B1950.0 CoordinateSystemTerm.
    
    """
    JPL_RESERVED_1: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CoordinateSystemTerm` JPL_RESERVED_1
    
        Reserved for JPL use (non-GSFC) CoordinateSystemTerm.
    
    """
    JPL_RESERVED_2: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CoordinateSystemTerm` JPL_RESERVED_2
    
        Reserved for JPL use (non-GSFC) CoordinateSystemTerm.
    
    """
    GEOCENTRIC_MEAN_OF_J2000: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CoordinateSystemTerm` GEOCENTRIC_MEAN_OF_J2000
    
        Geocentric mean of 2000.0 (J2000.0) CoordinateSystemTerm.
    
    """
    HELIOCENTRIC_J2000: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CoordinateSystemTerm` HELIOCENTRIC_J2000
    
        Heliocentric J2000.0 CoordinateSystemTerm.
    
    """
    COORDINATE_SYSTEM_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int COORDINATE_SYSTEM_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    COORDINATE_SYSTEM_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` COORDINATE_SYSTEM_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Returns the :class:`~org.orekit.frames.Frame` specified within the IIRV using the
            :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                coordinate system
        
        
        """
        ...
    @typing.overload
    def getFrame(self, dataContext: org.orekit.data.DataContext) -> org.orekit.frames.Frame:
        """
            Returns the :class:`~org.orekit.frames.Frame` specified within the IIRV.
        
            Parameters:
                context (:class:`~org.orekit.data.DataContext`): data context used to retrieve frames
        
            Returns:
                coordinate system
        
        """
        ...

class CrossSectionalAreaTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    public class CrossSectionalAreaTerm extends :class:`~org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm`
    
        5-character average satellite cross-sectional area in square meters with a resolution to the nearest hundredth of a
        square meter.
    
        Assumed decimal point is two places from the right. Must contain all zeros if not used.
    
        Units: m^2
    
        Valid values:
    
    
    
          - 0 to 999.99
          - [String]: Any integer 0-9 for characters 1-5
    
    
        Since:
            13.0
    """
    UNUSED: typing.ClassVar['CrossSectionalAreaTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.CrossSectionalAreaTerm` UNUSED
    
        CrossSectionalAreaTerm contains all zeros when not used.
    
    """
    CROSS_SECTIONAL_AREA_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int CROSS_SECTIONAL_AREA_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CROSS_SECTIONAL_AREA_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CROSS_SECTIONAL_AREA_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class DataSourceTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class DataSourceTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        Source of the data message.
    
        Valid values:
    
          - 1 = Nominal/planning
          - 2 = Real-time
          - 3 = Off-line
          - 4 = Off-line/mean
    
    
    
        Since:
            13.0
    """
    NOMINAL: typing.ClassVar['DataSourceTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.DataSourceTerm` NOMINAL
    
        Nominal/planning DataSource.
    
    """
    REAL_TIME: typing.ClassVar['DataSourceTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.DataSourceTerm` REAL_TIME
    
        Real-time DataSource.
    
    """
    OFFLINE: typing.ClassVar['DataSourceTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.DataSourceTerm` OFFLINE
    
        Off-line DataSource.
    
    """
    OFFLINE_MEAN: typing.ClassVar['DataSourceTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.DataSourceTerm` OFFLINE_MEAN
    
        Off-line/mean DataSource.
    
    """
    DATA_SOURCE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int DATA_SOURCE_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATA_SOURCE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DATA_SOURCE_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class DayOfYearTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class DayOfYearTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        3-character integer representing the day of the year.
    
        Valid values: 001-366 (365 + 1 for leap year)
    
        Since:
            13.0
    """
    DAY_OF_YEAR_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int DAY_OF_YEAR_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DAY_OF_YEAR_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DAY_OF_YEAR_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, uTCScale: org.orekit.time.UTCScale): ...
    def getDateComponents(self, int: int) -> org.orekit.time.DateComponents:
        """
            Returns the :class:`~org.orekit.time.DateComponents` instance that corresponds this term's value.
        
            Parameters:
                year (int): year to associated with the created date components
        
            Returns:
                the date components associated with this term
        
        
        """
        ...

class DragCoefficientTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    public class DragCoefficientTerm extends :class:`~org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm`
    
        4-character dimensionless drag coefficient.
    
        Assumed decimal point is two places from the right. Must contain all zeros if not used.
    
        Units: dimensionless
    
        Valid values:
    
          - 0 to 99.99
          - ":code:`xxxx`", :code:`x`: Any integer 0-9
    
    
        Since:
            13.0
    """
    UNUSED: typing.ClassVar['DragCoefficientTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.DragCoefficientTerm` UNUSED
    
        DragCoefficientTerm contains all zeros when not used.
    
    """
    DRAG_COEFFICIENT_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int DRAG_COEFFICIENT_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DRAG_COEFFICIENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DRAG_COEFFICIENT_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class IIRVTermUtils:
    """
    public final class IIRVTermUtils extends :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utilities class for :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm` subclasses.
    
        Since:
            13.0
    """
    @staticmethod
    def addPadding(string: str, char: str, int: int, boolean: bool) -> str:
        """
            Add padding characters to a string.
        
            Parameters:
                string (:class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string to pad
                c (char): padding character
                size (int): desired size
                addPaddingToLeft (boolean): if true, the resulting string is right justified (i.e. the padding character is added to the left of the string)
        
            Returns:
                padded String
        
        
        """
        ...
    @staticmethod
    def iirvTermsToLineString(*iIRVVectorTerm: org.orekit.files.iirv.terms.base.IIRVVectorTerm[typing.Any]) -> str: ...
    @staticmethod
    def iirvTermsToLineStringSplitByTerm(string: str, *iIRVVectorTerm: org.orekit.files.iirv.terms.base.IIRVVectorTerm[typing.Any]) -> str: ...

class MassTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    public class MassTerm extends :class:`~org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm`
    
        8-character mass of the satellite in kilograms with a resolution to the nearest tenth of a kilogram; assumed decimal
        point is one place from the right. Must contain all zeros if not used.
    
        Units: kg
    
        Valid values:
    
    
    
          - 0 to 999.99
          - [String]: Any integer 0-9 for characters 1-8
    
    
        Since:
            13.0
    """
    UNUSED: typing.ClassVar['MassTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.MassTerm` UNUSED
    
        MassTerm contains all zeros when not used.
    
    """
    MASS_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int MASS_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MASS_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MASS_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class MessageClassTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class MessageClassTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        2-character IIRV message class.
    
        Valid values:
    
          - 10 = IIRV (nominal)
          - 15 = IIRV (inflight update)
    
    
        Since:
            13.0
    """
    NOMINAL: typing.ClassVar['MessageClassTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.MessageClassTerm` NOMINAL
    
        Nominal MessageClass.
    
    """
    INFLIGHT_UPDATE: typing.ClassVar['MessageClassTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.MessageClassTerm` INFLIGHT_UPDATE
    
        Inflight update MessageClass.
    
    """
    MESSAGE_CLASS_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int MESSAGE_CLASS_TERM_LENGTH
    
        Length of the term (number of characters).
    
        Also see:
            :meth:`~constant`
    
    
    """
    MESSAGE_CLASS_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MESSAGE_CLASS_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class MessageEndConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    public class MessageEndConstantTerm extends :class:`~org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm`
    
        5-character immutable end of the message: "ITERM".
    
        Valid values: ITERM
    
        Since:
            13.0
    """
    MESSAGE_END_TERM_STRING: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MESSAGE_END_TERM_STRING
    
        End of the message is always "ITERM".
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class MessageIDTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class MessageIDTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        A unique 7-character number used to reference the IIRV message.
    
        Valid values: 0000000 to 9999999
    
        Since:
            13.0
    """
    MESSAGE_ID_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int MESSAGE_ID_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MESSAGE_ID_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MESSAGE_ID_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class MessageSourceTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    public class MessageSourceTerm extends :class:`~org.orekit.files.iirv.terms.base.StringValuedIIRVTerm`
    
        1-character source of the message (Default = "0").
    
        Since:
            13.0
    """
    DEFAULT: typing.ClassVar['MessageSourceTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.MessageSourceTerm` DEFAULT
    
        Default value for the message source is "0".
    
    """
    MESSAGE_SOURCE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int MESSAGE_SOURCE_TERM_LENGTH
    
        The length of the message source term within the IIRV vector.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MESSAGE_SOURCE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MESSAGE_SOURCE_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str): ...

class MessageStartConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    public class MessageStartConstantTerm extends :class:`~org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm`
    
        5-character start of the message, always is "GIIRV".
    
        Valid values: GIIRV
    
        Since:
            13.0
    """
    MESSAGE_START_TERM_STRING: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MESSAGE_START_TERM_STRING
    
        Start of the message is always "GIIRV".
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class MessageTypeTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    public class MessageTypeTerm extends :class:`~org.orekit.files.iirv.terms.base.StringValuedIIRVTerm`
    
        2-character type of this message.
    
        Valid values: Any letter, number or, ASCII space
    
        Since:
            13.0
    """
    DEFAULT: typing.ClassVar['MessageTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.MessageTypeTerm` DEFAULT
    
        Default value: "03" (operations data message).
    
    """
    MESSAGE_TYPE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int MESSAGE_TYPE_TERM_LENGTH
    
        The length of the message type term within the IIRV vector.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MESSAGE_TYPE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MESSAGE_TYPE_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str): ...

class OriginIdentificationTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    public class OriginIdentificationTerm extends :class:`~org.orekit.files.iirv.terms.base.StringValuedIIRVTerm`
    
        1-character alphabetic character indicating originator of message.
    
        See :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` for the related four-character routing indicator
    
        Valid values:
    
          - ASCII space = GSFC
          - Z = WLP
          - E = ETR
          - L = JPL
          - W = WTR
          - J = JSC
          - P = PMR
          - A = CSTC
          - K = KMR
          - C = CNES
    
    
        Since:
            13.0
    """
    GSFC: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` GSFC
    
        NASA Goddard Space Flight Center (GSFC) OriginIdentification.
    
    """
    WLP: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` WLP
    
        Wallops Island tracking radars (WLP) OriginIdentification.
    
    """
    ETR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` ETR
    
        NASA/USFC Eastern Test Range (ETR) OriginIdentification.
    
    """
    JPL: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` JPL
    
        NASA Jet Propulsion Laboratory (JPL) OriginIdentification.
    
    """
    WTR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` WTR
    
        NASA/USFC Western Test Range (WTR) OriginIdentification.
    
    """
    JSC: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` JSC
    
        NASA Johnson Space Center (JSC) OriginIdentification.
    
    """
    PMR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` PMR
    
        Navy Pacific Missile Range (PMR) OriginIdentification.
    
    """
    CSTC: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` CSTC
    
        Air Force Satellite Control Facility (CSTC) OriginIdentification.
    
    """
    KMR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` KMR
    
        Army Kwajalein Missile Range (KMR) OriginIdentification.
    
    """
    CNES: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` CNES
    
        French Space Agency National Centre for Space Studies (CNES) OriginIdentification.
    
    """
    ORIGIN_IDENTIFICATION_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int ORIGIN_IDENTIFICATION_TERM_LENGTH
    
        The length of the origin identification term within the IIRV vector.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ORIGIN_IDENTIFICATION_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ORIGIN_IDENTIFICATION_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str): ...

class OriginatorRoutingIndicatorTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    public class OriginatorRoutingIndicatorTerm extends :class:`~org.orekit.files.iirv.terms.base.StringValuedIIRVTerm`
    
        4-character originating routing indicator.
    
        Valid values: GCQU, GAQD
    
        Since:
            13.0
    """
    GCQU: typing.ClassVar['OriginatorRoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginatorRoutingIndicatorTerm` GCQU
    
        GCQU OriginatorRoutingIndicator.
    
    """
    GAQD: typing.ClassVar['OriginatorRoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.OriginatorRoutingIndicatorTerm` GAQD
    
        GAQD OriginatorRoutingIndicator.
    
    """
    ORIGINATOR_ROUTING_INDICATOR_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int ORIGINATOR_ROUTING_INDICATOR_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ORIGINATOR_ROUTING_INDICATOR_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ORIGINATOR_ROUTING_INDICATOR_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str): ...

class PositionVectorComponentTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class PositionVectorComponentTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        13-character signed component of a position vector.
    
        Units: m
    
        Valid values:
    
          - Character 1: ' ' or '-'
          - Character 2-12: Any integer 0-9
    
    
        Since:
            13.0
    """
    POSITION_VECTOR_COMPONENT_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int POSITION_VECTOR_COMPONENT_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    POSITION_VECTOR_COMPONENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` POSITION_VECTOR_COMPONENT_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class RoutingIndicatorTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    public class RoutingIndicatorTerm extends :class:`~org.orekit.files.iirv.terms.base.StringValuedIIRVTerm`
    
        4-character destination routing indicator that specifies the site for which the message was generated.
    
        See :class:`~org.orekit.files.iirv.terms.OriginIdentificationTerm` for the related alphabetic character
    
        Valid values:
    
          - GSFC = NASA Goddard Space Flight Center
          - WLP = Wallops Island tracking radars
          - ETR = NASA/USFC Eastern Test Range
          - JPL = NASA Jet Propulsion Laboratory
          - WTR = NASA/USFC Western Test Range
          - JSC = NASA Johnson Space Center
          - PMR = Navy Pacific Missile Range
          - CSTC = Air Force Satellite Control Facility
          - KMR = Army Kwajalein Missile Range
          - CNES = French Space Agency National Centre for Space Studies (CNES)
          - MANY = Message originated from more than one of the above stations
    
    
        Since:
            13.0
    """
    GSFC: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` GSFC
    
        NASA Goddard Space Flight Center (GSFC) RoutingIndicator.
    
    """
    WLP: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` WLP
    
        Wallops Island tracking radars (WLP) RoutingIndicator.
    
    """
    ETR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` ETR
    
        NASA/USFC Eastern Test Range (ETR) RoutingIndicator.
    
    """
    JPL: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` JPL
    
        NASA Jet Propulsion Laboratory (JPL) RoutingIndicator.
    
    """
    WTR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` WTR
    
        NASA/USFC Western Test Range (WTR) RoutingIndicator.
    
    """
    JSC: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` JSC
    
        NASA Johnson Space Center (JSC) RoutingIndicator.
    
    """
    PMR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` PMR
    
        Navy Pacific Missile Range (PMR) RoutingIndicator.
    
    """
    CSTC: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` CSTC
    
        Air Force Satellite Control Facility (CSTC) RoutingIndicator.
    
    """
    KMR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` KMR
    
        Army Kwajalein Missile Range (KMR) RoutingIndicator.
    
    """
    CNES: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` CNES
    
        French Space Agency National Centre for Space Studies (CNES) RoutingIndicator.
    
    """
    MANY: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.RoutingIndicatorTerm` MANY
    
        Message originated from more than one of the above stations RoutingIndicator.
    
    """
    ROUTING_INDICATOR_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int ROUTING_INDICATOR_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROUTING_INDICATOR_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ROUTING_INDICATOR_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str): ...

class SequenceNumberTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class SequenceNumberTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        3-character sequence number counter that is incremented for each vector in a set of vector data on a per-station per
        transmission basis.
    
        Valid values: 000-999.
    
        Since:
            13.0
    """
    SEQUENCE_NUMBER_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int SEQUENCE_NUMBER_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX_SEQUENCE_NUMBER: typing.ClassVar[int] = ...
    """
    public static final int MAX_SEQUENCE_NUMBER
    
        Maximum value of an IIRV sequence number.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SEQUENCE_NUMBER_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SEQUENCE_NUMBER_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term (integer 000-999).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class SolarReflectivityCoefficientTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    public class SolarReflectivityCoefficientTerm extends :class:`~org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm`
    
        8-character dimensionless solar reflectivity coefficient.
    
        s = "-" for negative sign or blank for positive sign, assumed decimal point is six places from the right. May contain
        all zeros if not used.
    
        Units: dimensionless
    
        Valid values
    
          - -99.99999 to 99.99999
          - ":code:`sxxxxxxx`: :code:`s`: ' ' (ASCII space) or '-', :code:`x`: Any integer 0-9
    
    
        Since:
            13.0
    """
    UNUSED: typing.ClassVar['SolarReflectivityCoefficientTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.SolarReflectivityCoefficientTerm` UNUSED
    
        SolarReflectivityCoefficientTerm contains all zeros when not used.
    
    """
    SOLAR_REFLECTIVITY_COEFFICIENT_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int SOLAR_REFLECTIVITY_COEFFICIENT_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SOLAR_REFLECTIVITY_COEFFICIENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SOLAR_REFLECTIVITY_COEFFICIENT_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    N_CHARS_AFTER_DECIMAL_PLACE: typing.ClassVar[int] = ...
    """
    public static final int N_CHARS_AFTER_DECIMAL_PLACE
    
        Number of characters before the end of the string the decimal place occurs.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class SpareConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    public class SpareConstantTerm extends :class:`~org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm`
    
        IIRV spare character (ASCII space).
    
        Since:
            13.0
    """
    SPARE_TERM_STRING: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SPARE_TERM_STRING
    
        IIRV spare character (ASCII space).
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class SupportIdCodeTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class SupportIdCodeTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        4-character mission-specific support identification code (SIC).
    
        Valid values: 0000-9999.
    
        Since:
            13.0
    """
    SUPPORT_ID_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int SUPPORT_ID_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SUPPORT_ID_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SUPPORT_ID_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term (0000-9999).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class TransferTypeConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    public class TransferTypeConstantTerm extends :class:`~org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm`
    
        1-character type of transfer (constant).
    
        Valid values: 1 (Interrange)
    
        Since:
            13.0
    """
    TRANSFER_TYPE_TERM_STRING: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TRANSFER_TYPE_TERM_STRING
    
        Start of the message is always "1" denoting an interrange message type.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class VectorEpochTerm(org.orekit.files.iirv.terms.base.IIRVVectorTerm[org.orekit.time.TimeComponents]):
    """
    public class VectorEpochTerm extends :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`<:class:`~org.orekit.time.TimeComponents`>
    
        Vector epoch in UTC with resolution to nearest millisecond.
    
        Valid values:
    
        hhmmsssss where:
    
          - hh = 00 to 23
          - mm = 00 to 59
          - sssss = 00000 to 59999 (milliseconds, implied decimal point three places from right)
    
    
        Since:
            13.0
    """
    VECTOR_EPOCH_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int VECTOR_EPOCH_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VECTOR_EPOCH_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` VECTOR_EPOCH_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        String in the form "hhmmsssss":
    
          - hh is 00 to 23: (0[0-9]|1[0-9]|2[0-3])
          - mm is 00 to 59: ([0-5][0-9])
          - sssss is 00000 to 599999: ([0-5][0-9]{4})
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, uTCScale: org.orekit.time.UTCScale): ...
    @typing.overload
    def __init__(self, timeComponents: org.orekit.time.TimeComponents): ...
    def hh(self) -> str:
        """
            Gets the two-character hour of the vector epoch.
        
            Returns:
                hh: hour of the vector epoch
        
        
        """
        ...
    def mm(self) -> str:
        """
            Gets the two-character minute of the vector epoch.
        
            Returns:
                mm: minute of the vector epoch
        
        
        """
        ...
    def ss(self) -> str:
        """
            Gets the two-character second of the vector epoch.
        
            Returns:
                ss: second of the vector epoch
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self, timeComponents: org.orekit.time.TimeComponents) -> str:
        """
            Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
            Specified by:
                :meth:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm.toEncodedString` in
                class :class:`~org.orekit.files.iirv.terms.base.IIRVVectorTerm`
        
            Parameters:
                value (:class:`~org.orekit.time.TimeComponents`): Value of the term
        
            Returns:
                Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...

class VectorTypeTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class VectorTypeTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        1-character type of vector specified in the message.
    
        Valid values:
    
          - 1 = Free flight (routine on-orbit)
          - 2 = Forced (special orbit update)
          - 3 = Spare
          - 4 = Maneuver ignition
          - 5 = Maneuver cutoff
          - 6 = Reentry
          - 7 = Powered flight
          - 8 = Stationary
          - 9 = Spare
    
    
        Since:
            13.0
    """
    FREE_FLIGHT: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` FREE_FLIGHT
    
        Free flight (routine on-orbit) VectorType.
    
    """
    FORCED: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` FORCED
    
        Forced VectorType.
    
    """
    SPARE3: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` SPARE3
    
        Spare VectorType: 3.
    
    """
    MANEUVER_IGNITION: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` MANEUVER_IGNITION
    
        Maneuver ignition VectorType.
    
    """
    MANEUVER_CUTOFF: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` MANEUVER_CUTOFF
    
        Maneuver cutoff VectorType.
    
    """
    REENTRY: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` REENTRY
    
        Reentry VectorType.
    
    """
    POWERED_FLIGHT: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` POWERED_FLIGHT
    
        Powered flight VectorType.
    
    """
    STATIONARY: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` STATIONARY
    
        Stationary VectorType.
    
    """
    SPARE9: typing.ClassVar['VectorTypeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VectorTypeTerm` SPARE9
    
        Spare VectorType: 9.
    
    """
    VECTOR_TYPE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int VECTOR_TYPE_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VECTOR_TYPE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` VECTOR_TYPE_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class VehicleIdCodeTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    public class VehicleIdCodeTerm extends :class:`~org.orekit.files.iirv.terms.base.LongValuedIIRVTerm`
    
        2-character body number/vehicle identification code (VIC).
    
        Valid values: 01-99.
    
        Since:
            13.0
    """
    DEFAULT: typing.ClassVar['VehicleIdCodeTerm'] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.VehicleIdCodeTerm` DEFAULT
    
        Default VIC set to 1.
    
    """
    VEHICLE_ID_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int VEHICLE_ID_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VEHICLE_ID_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` VEHICLE_ID_TERM_PATTERN
    
        Regular expression to check that vehicle identification codes are 01-99 (00 is not a valid entry).
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class VelocityVectorComponentTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    public class VelocityVectorComponentTerm extends :class:`~org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm`
    
        13-character signed component of a velocity vector.
    
        Units: m/s
    
        Assumed decimal places is three places from the right
    
        Valid values:
    
          - Character 1: ' ' or '-'
          - Character 2-12: Any integer 0-9
    
    
        Since:
            13.0
    """
    VELOCITY_VECTOR_COMPONENT_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int VELOCITY_VECTOR_COMPONENT_TERM_LENGTH
    
        The length of the IIRV term within the message.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VELOCITY_VECTOR_COMPONENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.iirv.terms.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` VELOCITY_VECTOR_COMPONENT_TERM_PATTERN
    
        Regular expression that ensures the validity of string values for this term.
    
        Also see:
            :meth:`~constant`
    
    
    """
    N_CHARS_AFTER_DECIMAL_PLACE: typing.ClassVar[int] = ...
    """
    public static final int N_CHARS_AFTER_DECIMAL_PLACE
    
        Number of characters before the end of the string the decimal place occurs.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.iirv.terms")``.

    CheckSumTerm: typing.Type[CheckSumTerm]
    CoordinateSystemTerm: typing.Type[CoordinateSystemTerm]
    CrossSectionalAreaTerm: typing.Type[CrossSectionalAreaTerm]
    DataSourceTerm: typing.Type[DataSourceTerm]
    DayOfYearTerm: typing.Type[DayOfYearTerm]
    DragCoefficientTerm: typing.Type[DragCoefficientTerm]
    IIRVTermUtils: typing.Type[IIRVTermUtils]
    MassTerm: typing.Type[MassTerm]
    MessageClassTerm: typing.Type[MessageClassTerm]
    MessageEndConstantTerm: typing.Type[MessageEndConstantTerm]
    MessageIDTerm: typing.Type[MessageIDTerm]
    MessageSourceTerm: typing.Type[MessageSourceTerm]
    MessageStartConstantTerm: typing.Type[MessageStartConstantTerm]
    MessageTypeTerm: typing.Type[MessageTypeTerm]
    OriginIdentificationTerm: typing.Type[OriginIdentificationTerm]
    OriginatorRoutingIndicatorTerm: typing.Type[OriginatorRoutingIndicatorTerm]
    PositionVectorComponentTerm: typing.Type[PositionVectorComponentTerm]
    RoutingIndicatorTerm: typing.Type[RoutingIndicatorTerm]
    SequenceNumberTerm: typing.Type[SequenceNumberTerm]
    SolarReflectivityCoefficientTerm: typing.Type[SolarReflectivityCoefficientTerm]
    SpareConstantTerm: typing.Type[SpareConstantTerm]
    SupportIdCodeTerm: typing.Type[SupportIdCodeTerm]
    TransferTypeConstantTerm: typing.Type[TransferTypeConstantTerm]
    VectorEpochTerm: typing.Type[VectorEpochTerm]
    VectorTypeTerm: typing.Type[VectorTypeTerm]
    VehicleIdCodeTerm: typing.Type[VehicleIdCodeTerm]
    VelocityVectorComponentTerm: typing.Type[VelocityVectorComponentTerm]
    base: org.orekit.files.iirv.terms.base.__module_protocol__
