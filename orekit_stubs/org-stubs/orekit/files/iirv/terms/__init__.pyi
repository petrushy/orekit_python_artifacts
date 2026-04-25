
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
    Three-character checksum to validate message.
    
    Calculated by summing the decimal equivalent of the preceding characters in the line, counting spaces as 0 and negative signs as 1:
    
      - 0 through 9 = face value
      - Minus (-) = 1
      - ASCII Space = 0
    
    Valid Values: 000-999
    
    Since:
        13.0
    """
    CHECK_SUM_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    CHECK_SUM_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...
    @staticmethod
    def computeChecksum(input: str) -> int:
        """
        Computes the sum of the decimal equivalent of characters in the line, counting spaces as 0 and negative signs as 1.
        
        Parameters:
            input (String): input string to compute checksum from
        
        Returns:
            computed checksum integer value
        
        
        """
        ...
    @staticmethod
    def fromIIRVTerms(*terms: org.orekit.files.iirv.terms.base.IIRVVectorTerm[typing.Any]) -> 'CheckSumTerm':
        """
        Constructs an IIRV checksum from a series of IIRVTerm instances.
        
        Parameters:
            terms (IIRVVectorTerm<?>...): IIRVTerms to compute checksum
        
        Returns:
            newly created CheckSum instance
        
        
        """
        ...
    def validateAgainstLineString(self, line: str) -> bool:
        """
        Validate the checksum from a line based on the object's checksum integer value.
        
        Parameters:
            line (String): string line of an IIRV message (including checksum as the final three characters)
        
        Returns:
            true if the extracted checksum value matches this object's integer value
        
        
        """
        ...
    @staticmethod
    def validateLineCheckSum(line: str) -> bool:
        """
        Validate a line's embedded checksum value.
        
        Parameters:
            line (String): string line of an IIRV message (including checksum as the final three characters)
        
        Returns:
            true if the derived and embedded checksum values are equal
        
        
        """
        ...

class CoordinateSystemTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
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
    Geocentric True-of-Date Rotating (GTOD) CoordinateSystemTerm.
    
    Also known as True of Date Rotating frame (TDR) or Greenwich Rotating Coordinate frame (GCR).
    """
    GEOCENTRIC_MEAN_B1950: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    Geocentric mean of 1950.0 (B1950.0) CoordinateSystemTerm.
    """
    HELIOCENTRIC_B1950: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    Heliocentric B1950.0 CoordinateSystemTerm.
    """
    JPL_RESERVED_1: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    Reserved for JPL use (non-GSFC) CoordinateSystemTerm.
    """
    JPL_RESERVED_2: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    Reserved for JPL use (non-GSFC) CoordinateSystemTerm.
    """
    GEOCENTRIC_MEAN_OF_J2000: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    Geocentric mean of 2000.0 (J2000.0) CoordinateSystemTerm.
    """
    HELIOCENTRIC_J2000: typing.ClassVar['CoordinateSystemTerm'] = ...
    """
    Heliocentric J2000.0 CoordinateSystemTerm.
    """
    COORDINATE_SYSTEM_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    COORDINATE_SYSTEM_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Returns the Frame specified within the IIRV using the getDefault.
        
        Returns:
            coordinate system
        
        
        """
        ...
    @typing.overload
    def getFrame(self, context: org.orekit.data.DataContext) -> org.orekit.frames.Frame:
        """
        Returns the Frame specified within the IIRV.
        
        Parameters:
            context (DataContext): data context used to retrieve frames
        
        Returns:
            coordinate system
        
        """
        ...

class CrossSectionalAreaTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    5-character average satellite cross-sectional area in square meters with a resolution to the nearest hundredth of a square meter.
    
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
    CrossSectionalAreaTerm contains all zeros when not used.
    """
    CROSS_SECTIONAL_AREA_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    CROSS_SECTIONAL_AREA_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class DataSourceTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
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
    Nominal/planning DataSource.
    """
    REAL_TIME: typing.ClassVar['DataSourceTerm'] = ...
    """
    Real-time DataSource.
    """
    OFFLINE: typing.ClassVar['DataSourceTerm'] = ...
    """
    Off-line DataSource.
    """
    OFFLINE_MEAN: typing.ClassVar['DataSourceTerm'] = ...
    """
    Off-line/mean DataSource.
    """
    DATA_SOURCE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    DATA_SOURCE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class DayOfYearTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    3-character integer representing the day of the year.
    
    Valid values: 001-366 (365 + 1 for leap year)
    
    Since:
        13.0
    """
    DAY_OF_YEAR_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    DAY_OF_YEAR_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, uTCScale: org.orekit.time.UTCScale): ...
    def getDateComponents(self, year: int) -> org.orekit.time.DateComponents:
        """
        Returns the DateComponents instance that corresponds this term's value.
        
        Parameters:
            year (int): year to associated with the created date components
        
        Returns:
            the date components associated with this term
        
        
        """
        ...

class DragCoefficientTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    4-character dimensionless drag coefficient.
    
    Assumed decimal point is two places from the right. Must contain all zeros if not used.
    
    Units: dimensionless
    
    Valid values:
    
      - 0 to 99.99
      - "xxxx", x: Any integer 0-9
    
    
    Since:
        13.0
    """
    UNUSED: typing.ClassVar['DragCoefficientTerm'] = ...
    """
    DragCoefficientTerm contains all zeros when not used.
    """
    DRAG_COEFFICIENT_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    DRAG_COEFFICIENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class IIRVTermUtils:
    """
    Utilities class for IIRVVectorTerm subclasses.
    
    Since:
        13.0
    """
    @staticmethod
    def addPadding(string: str, c: str, size: int, addPaddingToLeft: bool) -> str:
        """
        Add padding characters to a string.
        
        Parameters:
            string (String): string to pad
            c (char): padding character
            size (int): desired size
            addPaddingToLeft (boolean): if true, the resulting string is right justified (i.e. the padding character is added to the left of the string)
        
        Returns:
            padded String
        
        
        """
        ...
    @staticmethod
    def iirvTermsToLineString(*terms: org.orekit.files.iirv.terms.base.IIRVVectorTerm[typing.Any]) -> str:
        """
        Converts a list of IIRVVectorTerm instances to a String for a single line of an IIRVVector.
        
        Parameters:
            terms (IIRVVectorTerm<?>...): terms to parse/convert
        
        Returns:
            String containing each of the inputted terms
        
        
        """
        ...
    @staticmethod
    def iirvTermsToLineStringSplitByTerm(delimiter: str, *terms: org.orekit.files.iirv.terms.base.IIRVVectorTerm[typing.Any]) -> str:
        """
        Converts a list of IIRVVectorTerm instances to a String for a single line of an IIRVVector, where each term in the line is split by a specified delimiter.
        
        For real IIRV vector, the deliminator is always empty; it is only used when creating human-readable forms to more readily identify specific terms within a given message.
        
        Parameters:
            delimiter (String): delimiter to insert between each IIRV vector term
            terms (IIRVVectorTerm<?>...): terms to parse/convert
        
        Returns:
            String containing each of the inputted terms
        
        
        """
        ...

class MassTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    8-character mass of the satellite in kilograms with a resolution to the nearest tenth of a kilogram; assumed decimal point is one place from the right. Must contain all zeros if not used.
    
    Units: kg
    
    Valid values:
    
    
    
      - 0 to 999.99
      - [String]: Any integer 0-9 for characters 1-8
    
    
    Since:
        13.0
    """
    UNUSED: typing.ClassVar['MassTerm'] = ...
    """
    MassTerm contains all zeros when not used.
    """
    MASS_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    MASS_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class MessageClassTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    2-character IIRV message class.
    
    Valid values:
    
      - 10 = IIRV (nominal)
      - 15 = IIRV (inflight update)
    
    
    Since:
        13.0
    """
    NOMINAL: typing.ClassVar['MessageClassTerm'] = ...
    """
    Nominal MessageClass.
    """
    INFLIGHT_UPDATE: typing.ClassVar['MessageClassTerm'] = ...
    """
    Inflight update MessageClass.
    """
    MESSAGE_CLASS_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    Length of the term (number of characters).
    
    Also see:
        constant
    
    
    """
    MESSAGE_CLASS_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class MessageEndConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    5-character immutable end of the message: "ITERM".
    
    Valid values: ITERM
    
    Since:
        13.0
    """
    MESSAGE_END_TERM_STRING: typing.ClassVar[str] = ...
    """
    End of the message is always "ITERM".
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Constructor.
        
        See
        """
        ...

class MessageIDTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    A unique 7-character number used to reference the IIRV message.
    
    Valid values: 0000000 to 9999999
    
    Since:
        13.0
    """
    MESSAGE_ID_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    MESSAGE_ID_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class MessageSourceTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    1-character source of the message (Default = "0").
    
    Since:
        13.0
    """
    DEFAULT: typing.ClassVar['MessageSourceTerm'] = ...
    """
    Default value for the message source is "0".
    """
    MESSAGE_SOURCE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the message source term within the IIRV vector.
    
    Also see:
        constant
    
    
    """
    MESSAGE_SOURCE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    def __init__(self, value: str):
        """
        Constructor.
        
        See
        
        Parameters:
            value (String): value of message source term
        
        
        """
        ...

class MessageStartConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    5-character start of the message, always is "GIIRV".
    
    Valid values: GIIRV
    
    Since:
        13.0
    """
    MESSAGE_START_TERM_STRING: typing.ClassVar[str] = ...
    """
    Start of the message is always "GIIRV".
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Constructor.
        
        See
        """
        ...

class MessageTypeTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    2-character type of this message.
    
    Valid values: Any letter, number or, ASCII space
    
    Since:
        13.0
    """
    DEFAULT: typing.ClassVar['MessageTypeTerm'] = ...
    """
    Default value: "03" (operations data message).
    """
    MESSAGE_TYPE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the message type term within the IIRV vector.
    
    Also see:
        constant
    
    
    """
    MESSAGE_TYPE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    def __init__(self, value: str):
        """
        Constructor.
        
        See
        
        Parameters:
            value (String): value of the message type term
        
        
        """
        ...

class OriginIdentificationTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    1-character alphabetic character indicating originator of message.
    
    See RoutingIndicatorTerm for the related four-character routing indicator
    
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
    NASA Goddard Space Flight Center (GSFC) OriginIdentification.
    """
    WLP: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    Wallops Island tracking radars (WLP) OriginIdentification.
    """
    ETR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    NASA/USFC Eastern Test Range (ETR) OriginIdentification.
    """
    JPL: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    NASA Jet Propulsion Laboratory (JPL) OriginIdentification.
    """
    WTR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    NASA/USFC Western Test Range (WTR) OriginIdentification.
    """
    JSC: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    NASA Johnson Space Center (JSC) OriginIdentification.
    """
    PMR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    Navy Pacific Missile Range (PMR) OriginIdentification.
    """
    CSTC: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    Air Force Satellite Control Facility (CSTC) OriginIdentification.
    """
    KMR: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    Army Kwajalein Missile Range (KMR) OriginIdentification.
    """
    CNES: typing.ClassVar['OriginIdentificationTerm'] = ...
    """
    French Space Agency National Centre for Space Studies (CNES) OriginIdentification.
    """
    ORIGIN_IDENTIFICATION_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the origin identification term within the IIRV vector.
    
    Also see:
        constant
    
    
    """
    ORIGIN_IDENTIFICATION_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    def __init__(self, value: str):
        """
        Constructor.
        
        See
        
        Parameters:
            value (String): value of the origin ID term
        
        
        """
        ...

class OriginatorRoutingIndicatorTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    4-character originating routing indicator.
    
    Valid values: GCQU, GAQD
    
    Since:
        13.0
    """
    GCQU: typing.ClassVar['OriginatorRoutingIndicatorTerm'] = ...
    """
    GCQU OriginatorRoutingIndicator.
    """
    GAQD: typing.ClassVar['OriginatorRoutingIndicatorTerm'] = ...
    """
    GAQD OriginatorRoutingIndicator.
    """
    ORIGINATOR_ROUTING_INDICATOR_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    ORIGINATOR_ROUTING_INDICATOR_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    def __init__(self, value: str):
        """
        Constructor.
        
        See
        
        Parameters:
            value (String): value of the originator routing indicator term (dimensionless)
        
        
        """
        ...

class PositionVectorComponentTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
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
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    POSITION_VECTOR_COMPONENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class RoutingIndicatorTerm(org.orekit.files.iirv.terms.base.StringValuedIIRVTerm):
    """
    4-character destination routing indicator that specifies the site for which the message was generated.
    
    See OriginIdentificationTerm for the related alphabetic character
    
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
    NASA Goddard Space Flight Center (GSFC) RoutingIndicator.
    """
    WLP: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    Wallops Island tracking radars (WLP) RoutingIndicator.
    """
    ETR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    NASA/USFC Eastern Test Range (ETR) RoutingIndicator.
    """
    JPL: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    NASA Jet Propulsion Laboratory (JPL) RoutingIndicator.
    """
    WTR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    NASA/USFC Western Test Range (WTR) RoutingIndicator.
    """
    JSC: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    NASA Johnson Space Center (JSC) RoutingIndicator.
    """
    PMR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    Navy Pacific Missile Range (PMR) RoutingIndicator.
    """
    CSTC: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    Air Force Satellite Control Facility (CSTC) RoutingIndicator.
    """
    KMR: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    Army Kwajalein Missile Range (KMR) RoutingIndicator.
    """
    CNES: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    French Space Agency National Centre for Space Studies (CNES) RoutingIndicator.
    """
    MANY: typing.ClassVar['RoutingIndicatorTerm'] = ...
    """
    Message originated from more than one of the above stations RoutingIndicator.
    """
    ROUTING_INDICATOR_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    ROUTING_INDICATOR_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    def __init__(self, value: str):
        """
        Constructor.
        
        See
        
        Parameters:
            value (String): value of the routing indicator term
        
        
        """
        ...

class SequenceNumberTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    3-character sequence number counter that is incremented for each vector in a set of vector data on a per-station per transmission basis.
    
    Valid values: 000-999.
    
    Since:
        13.0
    """
    SEQUENCE_NUMBER_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    MAX_SEQUENCE_NUMBER: typing.ClassVar[int] = ...
    """
    Maximum value of an IIRV sequence number.
    
    Also see:
        constant
    
    
    """
    SEQUENCE_NUMBER_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term (integer 000-999).
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class SolarReflectivityCoefficientTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
    8-character dimensionless solar reflectivity coefficient.
    
    s = "-" for negative sign or blank for positive sign, assumed decimal point is six places from the right. May contain all zeros if not used.
    
    Units: dimensionless
    
    Valid values
    
      - -99.99999 to 99.99999
      - "sxxxxxxx: s: ' ' (ASCII space) or '-', x: Any integer 0-9
    
    
    Since:
        13.0
    """
    UNUSED: typing.ClassVar['SolarReflectivityCoefficientTerm'] = ...
    """
    SolarReflectivityCoefficientTerm contains all zeros when not used.
    """
    SOLAR_REFLECTIVITY_COEFFICIENT_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    SOLAR_REFLECTIVITY_COEFFICIENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    N_CHARS_AFTER_DECIMAL_PLACE: typing.ClassVar[int] = ...
    """
    Number of characters before the end of the string the decimal place occurs.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, string: str): ...

class SpareConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    IIRV spare character (ASCII space).
    
    Since:
        13.0
    """
    SPARE_TERM_STRING: typing.ClassVar[str] = ...
    """
    IIRV spare character (ASCII space).
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Constructor.
        
        See
        """
        ...

class SupportIdCodeTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    4-character mission-specific support identification code (SIC).
    
    Valid values: 0000-9999.
    
    Since:
        13.0
    """
    SUPPORT_ID_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    SUPPORT_ID_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term (0000-9999).
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class TransferTypeConstantTerm(org.orekit.files.iirv.terms.base.ConstantValuedIIRVTerm):
    """
    1-character type of transfer (constant).
    
    Valid values: 1 (Interrange)
    
    Since:
        13.0
    """
    TRANSFER_TYPE_TERM_STRING: typing.ClassVar[str] = ...
    """
    Start of the message is always "1" denoting an interrange message type.
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Constructor.
        
        See
        """
        ...

class VectorEpochTerm(org.orekit.files.iirv.terms.base.IIRVVectorTerm[org.orekit.time.TimeComponents]):
    """
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
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    VECTOR_EPOCH_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    String in the form "hhmmsssss":
    
      - hh is 00 to 23: (0[0-9]|1[0-9]|2[0-3])
      - mm is 00 to 59: ([0-5][0-9])
      - sssss is 00000 to 599999: ([0-5][0-9]{4})
    
    
    Also see:
        constant
    
    
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
    def toEncodedString(self, value: org.orekit.time.TimeComponents) -> str:
        """
        Convert an IIRV term value into the encoded String representation, as it would appear in the IIRV message.
        
        Specified by: toEncodedString in class IIRVVectorTerm
        
        Parameters:
            value (TimeComponents): Value of the term
        
        Returns:
            Encoded String representing of the inputted IIRV term it appears in the IIRV message
        
        
        """
        ...
    @typing.overload
    def toEncodedString(self) -> str: ...

class VectorTypeTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
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
    Free flight (routine on-orbit) VectorType.
    """
    FORCED: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Forced VectorType.
    """
    SPARE3: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Spare VectorType: 3.
    """
    MANEUVER_IGNITION: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Maneuver ignition VectorType.
    """
    MANEUVER_CUTOFF: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Maneuver cutoff VectorType.
    """
    REENTRY: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Reentry VectorType.
    """
    POWERED_FLIGHT: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Powered flight VectorType.
    """
    STATIONARY: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Stationary VectorType.
    """
    SPARE9: typing.ClassVar['VectorTypeTerm'] = ...
    """
    Spare VectorType: 9.
    """
    VECTOR_TYPE_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    VECTOR_TYPE_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class VehicleIdCodeTerm(org.orekit.files.iirv.terms.base.LongValuedIIRVTerm):
    """
    2-character body number/vehicle identification code (VIC).
    
    Valid values: 01-99.
    
    Since:
        13.0
    """
    DEFAULT: typing.ClassVar['VehicleIdCodeTerm'] = ...
    """
    Default VIC set to 1.
    """
    VEHICLE_ID_TERM_LENGTH: typing.ClassVar[int] = ...
    """
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    VEHICLE_ID_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression to check that vehicle identification codes are 01-99 (00 is not a valid entry).
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int): ...

class VelocityVectorComponentTerm(org.orekit.files.iirv.terms.base.DoubleValuedIIRVTerm):
    """
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
    The length of the IIRV term within the message.
    
    Also see:
        constant
    
    
    """
    VELOCITY_VECTOR_COMPONENT_TERM_PATTERN: typing.ClassVar[str] = ...
    """
    Regular expression that ensures the validity of string values for this term.
    
    Also see:
        constant
    
    
    """
    N_CHARS_AFTER_DECIMAL_PLACE: typing.ClassVar[int] = ...
    """
    Number of characters before the end of the string the decimal place occurs.
    
    Also see:
        constant
    
    
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
