
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class AngleType(java.lang.Enum['AngleType']):
    """
    Antenna geometry represented in the angle date.
    
    Since:
        11.0
    """
    AZEL: typing.ClassVar['AngleType'] = ...
    RADEC: typing.ClassVar['AngleType'] = ...
    XEYN: typing.ClassVar['AngleType'] = ...
    XSYE: typing.ClassVar['AngleType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AngleType':
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
    def values() -> typing.MutableSequence['AngleType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AngleType c : AngleType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CorrectionApplied(java.lang.Enum['CorrectionApplied']):
    """
    Indicator for corrections application.
    
    Since:
        11.0
    """
    YES: typing.ClassVar['CorrectionApplied'] = ...
    NO: typing.ClassVar['CorrectionApplied'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'CorrectionApplied':
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
    def values() -> typing.MutableSequence['CorrectionApplied']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CorrectionApplied c : CorrectionApplied.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DataQuality(java.lang.Enum['DataQuality']):
    """
    Quality of the data.
    
    Since:
        11.0
    """
    RAW: typing.ClassVar['DataQuality'] = ...
    VALIDATED: typing.ClassVar['DataQuality'] = ...
    DEGRADED: typing.ClassVar['DataQuality'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'DataQuality':
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
    def values() -> typing.MutableSequence['DataQuality']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (DataQuality c : DataQuality.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IntegrationReference(java.lang.Enum['IntegrationReference']):
    """
    Relationship between time tag and integration interval.
    
    Since:
        11.0
    """
    START: typing.ClassVar['IntegrationReference'] = ...
    MIDDLE: typing.ClassVar['IntegrationReference'] = ...
    END: typing.ClassVar['IntegrationReference'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'IntegrationReference':
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
    def values() -> typing.MutableSequence['IntegrationReference']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (IntegrationReference c : IntegrationReference.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Observation:
    """
    The Observation class contains the data from an observation line.
    
    It is not an Orekit object yet. It is a simple container holding:
    
      - a keyword, the type of the observation;
      - a timetag, the epoch of the observation;
      - a measurement, the value of the observation.
    
    WARNING. The same class handles many different measurements types (range, Doppler, clocks, pressure, power to noise ratio…). Since Orekit 11.0, it uses only SI units, so angular measurements have already been converted in radians, range has been converted in meters (according to the getRangeUnits, Doppler has been converted to meters per second. Up to Orekit 10.x, the measurements were raw measurements as read in the TDM.
    """
    def __init__(self, type: 'ObservationType', epoch: org.orekit.time.AbsoluteDate, measurement: float):
        """
        Simple constructor.
        
        Parameters:
            type (ObservationType): type of the observation
            epoch (AbsoluteDate): the timetag
            measurement (double): the measurement (in SI units, converted from TDM)
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for the epoch.
        
        Returns:
            the epoch
        
        
        """
        ...
    def getMeasurement(self) -> float:
        """
        Getter for the measurement.
        
        Returns:
            the measurement (in SI units, converted from TDM)
        
        
        """
        ...
    def getType(self) -> 'ObservationType':
        """
        Get the type of observation.
        
        Returns:
            type of observation
        
        
        """
        ...

class ObservationType(java.lang.Enum['ObservationType']):
    """
    Keys for Observation entries.
    
    Since:
        11.0
    """
    CARRIER_POWER: typing.ClassVar['ObservationType'] = ...
    DOPPLER_COUNT: typing.ClassVar['ObservationType'] = ...
    DOPPLER_INSTANTANEOUS: typing.ClassVar['ObservationType'] = ...
    DOPPLER_INTEGRATED: typing.ClassVar['ObservationType'] = ...
    PC_N0: typing.ClassVar['ObservationType'] = ...
    PR_N0: typing.ClassVar['ObservationType'] = ...
    RECEIVE_PHASE_CT_1: typing.ClassVar['ObservationType'] = ...
    RECEIVE_PHASE_CT_2: typing.ClassVar['ObservationType'] = ...
    RECEIVE_PHASE_CT_3: typing.ClassVar['ObservationType'] = ...
    RECEIVE_PHASE_CT_4: typing.ClassVar['ObservationType'] = ...
    RECEIVE_PHASE_CT_5: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_PHASE_CT_1: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_PHASE_CT_2: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_PHASE_CT_3: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_PHASE_CT_4: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_PHASE_CT_5: typing.ClassVar['ObservationType'] = ...
    RANGE: typing.ClassVar['ObservationType'] = ...
    RECEIVE_FREQ_1: typing.ClassVar['ObservationType'] = ...
    RECEIVE_FREQ_2: typing.ClassVar['ObservationType'] = ...
    RECEIVE_FREQ_3: typing.ClassVar['ObservationType'] = ...
    RECEIVE_FREQ_4: typing.ClassVar['ObservationType'] = ...
    RECEIVE_FREQ_5: typing.ClassVar['ObservationType'] = ...
    RECEIVE_FREQ: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_1: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_2: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_3: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_4: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_5: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_RATE_1: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_RATE_2: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_RATE_3: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_RATE_4: typing.ClassVar['ObservationType'] = ...
    TRANSMIT_FREQ_RATE_5: typing.ClassVar['ObservationType'] = ...
    DOR: typing.ClassVar['ObservationType'] = ...
    VLBI_DELAY: typing.ClassVar['ObservationType'] = ...
    ANGLE_1: typing.ClassVar['ObservationType'] = ...
    ANGLE_2: typing.ClassVar['ObservationType'] = ...
    MAG: typing.ClassVar['ObservationType'] = ...
    RCS: typing.ClassVar['ObservationType'] = ...
    CLOCK_BIAS: typing.ClassVar['ObservationType'] = ...
    CLOCK_DRIFT: typing.ClassVar['ObservationType'] = ...
    STEC: typing.ClassVar['ObservationType'] = ...
    TROPO_DRY: typing.ClassVar['ObservationType'] = ...
    TROPO_WET: typing.ClassVar['ObservationType'] = ...
    PRESSURE: typing.ClassVar['ObservationType'] = ...
    RHUMIDITY: typing.ClassVar['ObservationType'] = ...
    TEMPERATURE: typing.ClassVar['ObservationType'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, ruConverter: 'RangeUnitsConverter', metadata: 'TdmMetadata', observationsBlock: 'ObservationsBlock') -> bool:
        """
        Process an observation line.
        
        Parameters:
            token (ParseToken): parse token
            context (ContextBinding): context binding
            ruConverter (RangeUnitsConverter): converter for RU (may be null)
            metadata (TdmMetadata): metadata for current block
            observationsBlock (ObservationsBlock): observation block to fill
        
        Returns:
            true if token was accepted
        
        
        """
        ...
    def rawToSI(self, ruConverter: 'RangeUnitsConverter', metadata: 'TdmMetadata', date: org.orekit.time.AbsoluteDate, rawValue: float) -> float:
        """
        Convert a measurement to SI units.
        
        Parameters:
            ruConverter (RangeUnitsConverter): converter for RU (may be null)
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            rawValue (double): measurement raw value
        
        Returns:
            measurement in SI units
        
        
        """
        ...
    def siToRaw(self, ruConverter: 'RangeUnitsConverter', metadata: 'TdmMetadata', date: org.orekit.time.AbsoluteDate, siValue: float) -> float:
        """
        Convert a measurement from SI units.
        
        Parameters:
            ruConverter (RangeUnitsConverter): converter for RU (may be null)
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            siValue (double): measurement value in SI units
        
        Returns:
            measurement raw value
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ObservationType':
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
    def values() -> typing.MutableSequence['ObservationType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ObservationType c : ObservationType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ObservationsBlock(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    The Observations Block class contain metadata and the list of observation data lines.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    The reason for which the observations have been separated into blocks is that the different data blocks in a TDM file usually refers to different types of observations. An observation block is associated with a TDM metadata object and contains a list of observations. At this level, an observation is not an Orekit object, it is a custom object containing:
    
      - a keyword, the type of the observation;
      - a timetag, the date of the observation;
      - a measurement, the value of the observation.
    """
    def __init__(self):
        """
        ObservationsBlock constructor.
        """
        ...
    @typing.overload
    def addObservation(self, observation: Observation) -> None:
        """
        Adds an observation data line.
        
        Parameters:
            observation (Observation): the observation to add to the list
        
        Adds an observation data line.
        
        Parameters:
            type (ObservationType): type of the observation
            epoch (AbsoluteDate): the timetag
            measurement (double): the measurement
        
        
        """
        ...
    @typing.overload
    def addObservation(self, type: ObservationType, epoch: org.orekit.time.AbsoluteDate, measurement: float) -> None: ...
    def getObservations(self) -> java.util.List[Observation]:
        """
        Get the list of Observations data lines.
        
        Returns:
            a reference to the internal list of Observations data lines
        
        
        """
        ...
    def setObservations(self, observations: java.util.List[Observation]) -> None:
        """
        Set the list of Observations Data Lines.
        
        Parameters:
            observations (List<Observation> observations): the list of Observations Data Lines to set
        
        
        """
        ...

class RangeMode(java.lang.Enum['RangeMode']):
    """
    Type of range tones.
    
    Since:
        11.0
    """
    COHERENT: typing.ClassVar['RangeMode'] = ...
    CONSTANT: typing.ClassVar['RangeMode'] = ...
    ONE_WAY: typing.ClassVar['RangeMode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'RangeMode':
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
    def values() -> typing.MutableSequence['RangeMode']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RangeMode c : RangeMode.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RangeUnits(java.lang.Enum['RangeUnits']):
    """
    Units of the range observable.
    
    Since:
        11.0
    """
    km: typing.ClassVar['RangeUnits'] = ...
    s: typing.ClassVar['RangeUnits'] = ...
    RU: typing.ClassVar['RangeUnits'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'RangeUnits':
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
    def values() -> typing.MutableSequence['RangeUnits']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RangeUnits c : RangeUnits.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RangeUnitsConverter:
    """
    Interface for converting RU to meters.
    
    Implementations of this interface must be provided by user when dealing with Tdm that include range observations in RU. These units are intended for mission-specific measurements and must be described in an Interface Control Document.
    
    Since:
        11.0
    """
    def metersToRu(self, metadata: 'TdmMetadata', date: org.orekit.time.AbsoluteDate, range: float) -> float:
        """
        Convert a range expressed in meters.
        
        Parameters:
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            range (double): range value in meters
        
        Returns:
            range range value in RU
        
        
        """
        ...
    def ruToMeters(self, metadata: 'TdmMetadata', date: org.orekit.time.AbsoluteDate, range: float) -> float:
        """
        Convert a range expressed in RU.
        
        Parameters:
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            range (double): range value in RU
        
        Returns:
            range range value in meters
        
        
        """
        ...

class Tdm(org.orekit.files.ccsds.ndm.NdmConstituent['TdmHeader', org.orekit.files.ccsds.section.Segment['TdmMetadata', ObservationsBlock]]):
    """
    This class stores all the information of the CCSDS Tracking Data Message parsed by TDMParser or TDMXMLParser.
    
    It contains the header and a list of Observations Blocks each containing TDM metadata and a list of observation data lines.
    
    At this level the observations are not Orekit objects but custom object containing a keyword (type of observation), a timetag (date of the observation) and a measurement (value of the observation).
    
    It is up to the user to convert these observations to Orekit tracking object (Range, Angular, TurnAroundRange etc...).
    
    References:
    
    pdf ("Tracking Data Message", Blue Book, Version 1.0, November 2007).
    
    Since:
        9.0
    """
    ROOT: typing.ClassVar[str] = ...
    """
    Root element for XML files.
    
    Also see:
        constant
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    Key for format version.
    
    Also see:
        constant
    
    
    """
    def __init__(self, header: 'TdmHeader', segments: java.util.List[org.orekit.files.ccsds.section.Segment['TdmMetadata', ObservationsBlock]], conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext):
        """
        Simple constructor.
        
        Parameters:
            header (TdmHeader): file header
            segments (List<Segment<TdmMetadata, ObservationsBlock>>): file segments
            conventions (IERSConventions): IERS conventions
            dataContext (DataContext): used for creating frames, time scales, etc.
        
        
        """
        ...

class TdmDataKey(java.lang.Enum['TdmDataKey']):
    """
    Keys for Observation entries, except the measurements themselves.
    
    Since:
        11.0
    """
    observation: typing.ClassVar['TdmDataKey'] = ...
    COMMENT: typing.ClassVar['TdmDataKey'] = ...
    EPOCH: typing.ClassVar['TdmDataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, observationsBlock: ObservationsBlock) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            observationsBlock (ObservationsBlock): observation block to fill
        
        Returns:
            true if token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'TdmDataKey':
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
    def values() -> typing.MutableSequence['TdmDataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (TdmDataKey c : TdmDataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TdmHeader(org.orekit.files.ccsds.section.Header):
    """
    Header of a CCSDS Tracking Data Message.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...

class TdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    The TDMMetadata class gathers the meta-data present in the Tracking Data Message (TDM).
    
    References:
    
    pdf. §3.3 ("Tracking Data Message", Blue Book, Version 1.0, November 2007).
    
    Since:
        9.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def addEphemerisName(self, participantNumber: int, ephemerisName: str) -> None:
        """
        Adds an ephemeris name to the list.
        
        Parameters:
            participantNumber (int): the number of the participant
            ephemerisName (String): name of the ephemeris for the participant
        
        
        """
        ...
    def addParticipant(self, participantNumber: int, participant: str) -> None:
        """
        Adds a participant to the list.
        
        Parameters:
            participantNumber (int): the number of the participant to add
            participant (String): the name of the participant to add
        
        
        """
        ...
    def addReceiveDelay(self, participantNumber: int, receiveDelay: float) -> None:
        """
        Adds a receive delay to the list.
        
        Parameters:
            participantNumber (int): the number of the participants for which the receive delay is given
            receiveDelay (double): the receive delay value to add
        
        
        """
        ...
    def addTransmitDelay(self, participantNumber: int, transmitDelay: float) -> None:
        """
        Adds a transmit delay to the list.
        
        Parameters:
            participantNumber (int): the number of the participants for which the transmit delay is given
            transmitDelay (double): the transmit delay value to add
        
        
        """
        ...
    def getAngleType(self) -> AngleType:
        """
        Getter for angleType.
        
        Returns:
            the angleType
        
        
        """
        ...
    def getCorrectionAberrationDiurnal(self) -> float:
        """
        Getter for the diurnal aberration correction.
        
        Returns:
            the diurnal aberration correction in radians
        
        
        """
        ...
    def getCorrectionAberrationYearly(self) -> float:
        """
        Getter for the yearly aberration correction.
        
        Returns:
            the yearly aberration correction in radians
        
        
        """
        ...
    def getCorrectionAngle1(self) -> float:
        """
        Getter for the correctionAngle1.
        
        Returns:
            the correctionAngle1 (in radians)
        
        
        """
        ...
    def getCorrectionAngle2(self) -> float:
        """
        Getter for the correctionAngle2.
        
        Returns:
            the correctionAngle2 (in radians)
        
        
        """
        ...
    def getCorrectionDoppler(self) -> float:
        """
        Getter for the correctionDoppler.
        
        Returns:
            the correctionDoppler (in m/s)
        
        
        """
        ...
    def getCorrectionMagnitude(self) -> float:
        """
        Getter for the magnitude correction.
        
        Returns:
            the magnitude correction
        
        
        """
        ...
    def getCorrectionRange(self, converter: RangeUnitsConverter) -> float:
        """
        Getter for the raw correction for range in meters.
        
        Parameters:
            converter (RangeUnitsConverter): converter to use if getRangeUnits are set to
                RU
        
        Returns:
            the raw correction for range in meters
        
        
        """
        ...
    def getCorrectionRcs(self) -> float:
        """
        Getter for the radar cross section correction.
        
        Returns:
            the radar cross section correction in m²
        
        
        """
        ...
    def getCorrectionReceive(self) -> float:
        """
        Getter for the correctionReceive.
        
        Returns:
            the correctionReceive (in TDM units, without conversion)
        
        
        """
        ...
    def getCorrectionTransmit(self) -> float:
        """
        Getter for the correctionTransmit.
        
        Returns:
            the correctionTransmit (in TDM units, without conversion)
        
        
        """
        ...
    def getCorrectionsApplied(self) -> CorrectionApplied:
        """
        Getter for the correctionApplied.
        
        Returns:
            the correctionApplied (in TDM units, without conversion)
        
        
        """
        ...
    def getDataQuality(self) -> DataQuality:
        """
        Getter for the dataQuality.
        
        Returns:
            the dataQuality
        
        
        """
        ...
    def getDataTypes(self) -> java.util.List[ObservationType]:
        """
        Getter for the data types in the data section.
        
        Returns:
            data types in the data section
        
        
        """
        ...
    def getDopplerCountBias(self) -> float:
        """
        Get the Doppler count bias.
        
        Returns:
            the Doppler count bias in Hz
        
        
        """
        ...
    def getDopplerCountScale(self) -> float:
        """
        Get the Doppler count scale.
        
        Returns:
            the Doppler count scale
        
        
        """
        ...
    def getEphemerisNames(self) -> java.util.Map[int, str]:
        """
        Getter for external ephemeris names for participants.
        
        Returns:
            external ephemeris names for participants
        
        
        """
        ...
    def getFreqOffset(self) -> float:
        """
        Getter for the freqOffset.
        
        Returns:
            the freqOffset
        
        
        """
        ...
    def getIntegrationInterval(self) -> float:
        """
        Getter for the integrationInterval.
        
        Returns:
            the integrationInterval
        
        
        """
        ...
    def getIntegrationRef(self) -> IntegrationReference:
        """
        Getter for the integrationRef.
        
        Returns:
            the integrationRef
        
        
        """
        ...
    def getInterpolationDegree(self) -> int:
        """
        Get the interpolation degree.
        
        Returns:
            the interpolation degree
        
        
        """
        ...
    def getInterpolationMethod(self) -> str:
        """
        Get the interpolation method to be used.
        
        Returns:
            the interpolation method
        
        
        """
        ...
    def getMode(self) -> 'TrackingMode':
        """
        Getter for the mode.
        
        Returns:
            the mode
        
        
        """
        ...
    def getParticipants(self) -> java.util.Map[int, str]:
        """
        Getter for the participants.
        
        Returns:
            the participants
        
        
        """
        ...
    def getPath(self) -> typing.MutableSequence[int]:
        """
        Getter for the path.
        
        Returns:
            the path
        
        
        """
        ...
    def getPath1(self) -> typing.MutableSequence[int]:
        """
        Getter for the path1.
        
        Returns:
            the path1
        
        
        """
        ...
    def getPath2(self) -> typing.MutableSequence[int]:
        """
        Getter for the path2.
        
        Returns:
            the path2
        
        
        """
        ...
    def getRadecFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame used right ascension and declination measurements.
        
        Note that CCSDS 503 says "The origin (center) of the reference frame is assumed to be at the antenna reference point", but since the TDM does not provide the location of the antenna reference point the returned frame is not centered at the antenna reference point. Therefore, only the orientation of the returned frame is significant.
        
        Returns:
            Orientation of the frame used for RADEC observations.
        
        Since:
            13.1.5
        
        Also see:
            getReferenceFrame
        
        
        """
        ...
    def getRangeMode(self) -> RangeMode:
        """
        Getter for the rangeMode.
        
        Returns:
            the rangeMode
        
        
        """
        ...
    def getRangeModulus(self, converter: RangeUnitsConverter) -> float:
        """
        Getter for the range modulus in meters.
        
        Parameters:
            converter (RangeUnitsConverter): converter to use if getRangeUnits are set to
                RU
        
        Returns:
            the range modulus in meters
        
        
        """
        ...
    def getRangeUnits(self) -> RangeUnits:
        """
        Getter for the rangeUnits.
        
        Returns:
            the rangeUnits
        
        
        """
        ...
    def getRawCorrectionRange(self) -> float:
        """
        Getter for the raw correction for range.
        
        Returns:
            the raw correction for range (in getRangeUnits)
        
        
        """
        ...
    def getRawRangeModulus(self) -> float:
        """
        Getter for the raw range modulus.
        
        Returns:
            the raw range modulus in range units
        
        
        """
        ...
    def getReceiveBand(self) -> str:
        """
        Getter for the receiveBand.
        
        Returns:
            the receiveBand
        
        
        """
        ...
    def getReceiveDelays(self) -> java.util.Map[int, float]:
        """
        Getter for receiveDelays.
        
        Returns:
            the receiveDelays
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get the the value of REFERENCE_FRAME as an Orekit Frame.
        
        Returns:
            The reference frame specified by the REFERENCE_FRAME keyword.
        
        Also see:
            getRadecFrame
        
        
        """
        ...
    def getStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for the startTime.
        
        Returns:
            the startTime
        
        
        """
        ...
    def getStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for the stopTime.
        
        Returns:
            the stopTime
        
        
        """
        ...
    def getTimetagRef(self) -> 'TimetagReference':
        """
        Getter for the timetagRef.
        
        Returns:
            the timetagRef
        
        
        """
        ...
    def getTrackId(self) -> str:
        """
        Getter for the tracking data identifier.
        
        Returns:
            tracking data identifier
        
        
        """
        ...
    def getTransmitBand(self) -> str:
        """
        Getter for the transmitBand.
        
        Returns:
            the transmitBand
        
        
        """
        ...
    def getTransmitDelays(self) -> java.util.Map[int, float]:
        """
        Getter for the transmitDelays.
        
        Returns:
            the transmitDelays
        
        
        """
        ...
    def getTurnaroundDenominator(self) -> int:
        """
        Getter for the turnaroundDenominator.
        
        Returns:
            the turnaroundDenominator
        
        
        """
        ...
    def getTurnaroundNumerator(self) -> int:
        """
        Getter for the turnaroundNumerator.
        
        Returns:
            the turnaroundNumerator
        
        
        """
        ...
    def hasDopplerCountRollover(self) -> bool:
        """
        Check if there is a Doppler count rollover.
        
        Returns:
            true if there is a Doppler count rollover
        
        
        """
        ...
    def setAngleType(self, angleType: AngleType) -> None:
        """
        Setter for the angleType.
        
        Parameters:
            angleType (AngleType): the angleType to set
        
        
        """
        ...
    def setCorrectionAberrationDiurnal(self, correctionAberrationDiurnal: float) -> None:
        """
        Setter for the diurnal aberration correction.
        
        Parameters:
            correctionAberrationDiurnal (double): the diurnal aberration correction in radians to set
        
        
        """
        ...
    def setCorrectionAberrationYearly(self, correctionAberrationYearly: float) -> None:
        """
        Setter for the yearly aberration correction.
        
        Parameters:
            correctionAberrationYearly (double): the yearly aberration correction in radians to set
        
        
        """
        ...
    def setCorrectionAngle1(self, correctionAngle1: float) -> None:
        """
        Setter for the correctionAngle1.
        
        Parameters:
            correctionAngle1 (double): the correctionAngle1 to set (in radians)
        
        
        """
        ...
    def setCorrectionAngle2(self, correctionAngle2: float) -> None:
        """
        Setter for the correctionAngle2.
        
        Parameters:
            correctionAngle2 (double): the correctionAngle2 to set (in radians)
        
        
        """
        ...
    def setCorrectionDoppler(self, correctionDoppler: float) -> None:
        """
        Setter for the correctionDoppler.
        
        Parameters:
            correctionDoppler (double): the correctionDoppler to set (in m/s)
        
        
        """
        ...
    def setCorrectionMagnitude(self, correctionMagnitude: float) -> None:
        """
        Setter for the magnitude correction.
        
        Parameters:
            correctionMagnitude (double): the magnitude correction to set
        
        
        """
        ...
    def setCorrectionRcs(self, correctionRcs: float) -> None:
        """
        Setter for the radar cross section correction.
        
        Parameters:
            correctionRcs (double): the radar cross section correction in m² to set
        
        
        """
        ...
    def setCorrectionReceive(self, correctionReceive: float) -> None:
        """
        Setter for the correctionReceive.
        
        Parameters:
            correctionReceive (double): the correctionReceive to set (in TDM units, without conversion)
        
        
        """
        ...
    def setCorrectionTransmit(self, correctionTransmit: float) -> None:
        """
        Setter for the correctionTransmit.
        
        Parameters:
            correctionTransmit (double): the correctionTransmit to set (in TDM units, without conversion)
        
        
        """
        ...
    def setCorrectionsApplied(self, correctionsApplied: CorrectionApplied) -> None:
        """
        Setter for the correctionApplied.
        
        Parameters:
            correctionsApplied (CorrectionApplied): the correctionApplied to set (in TDM units, without conversion)
        
        
        """
        ...
    def setDataQuality(self, dataQuality: DataQuality) -> None:
        """
        Setter for the dataQuality.
        
        Parameters:
            dataQuality (DataQuality): the dataQuality to set
        
        
        """
        ...
    def setDataTypes(self, dataTypes: java.util.List[ObservationType]) -> None:
        """
        Setter for the data types in the data section.
        
        Parameters:
            dataTypes (List<ObservationType> dataTypes): data types in the data section
        
        
        """
        ...
    def setDopplerCountBias(self, dopplerCountBias: float) -> None:
        """
        Set the Doppler count bias.
        
        Parameters:
            dopplerCountBias (double): Doppler count bias in Hz to set
        
        
        """
        ...
    def setDopplerCountRollover(self, dopplerCountRollover: bool) -> None:
        """
        Set the indicator for Doppler count rollover.
        
        Parameters:
            dopplerCountRollover (boolean): indicator for Doppler count rollover
        
        
        """
        ...
    def setDopplerCountScale(self, dopplerCountScale: float) -> None:
        """
        Set the Doppler count Scale.
        
        Parameters:
            dopplerCountScale (double): Doppler count scale to set
        
        
        """
        ...
    def setEphemerisNames(self, ephemerisNames: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]]) -> None:
        """
        Setter for the external ephemeris names for participants.
        
        Parameters:
            ephemerisNames (Map<Integer, String> ephemerisNames): external ephemeris names for participants
        
        
        """
        ...
    def setFreqOffset(self, freqOffset: float) -> None:
        """
        Setter for the freqOffset.
        
        Parameters:
            freqOffset (double): the freqOffset to set
        
        
        """
        ...
    def setIntegrationInterval(self, integrationInterval: float) -> None:
        """
        Setter for the integrationInterval.
        
        Parameters:
            integrationInterval (double): the integrationInterval to set
        
        
        """
        ...
    def setIntegrationRef(self, integrationRef: IntegrationReference) -> None:
        """
        Setter for the integrationRef.
        
        Parameters:
            integrationRef (IntegrationReference): the integrationRef to set
        
        
        """
        ...
    def setInterpolationDegree(self, interpolationDegree: int) -> None:
        """
        Set the interpolation degree.
        
        Parameters:
            interpolationDegree (int): the interpolation degree to be set
        
        
        """
        ...
    def setInterpolationMethod(self, interpolationMethod: str) -> None:
        """
        Set the interpolation method to be used.
        
        Parameters:
            interpolationMethod (String): the interpolation method to be set
        
        
        """
        ...
    def setMode(self, mode: 'TrackingMode') -> None:
        """
        Setter for the mode.
        
        Parameters:
            mode (TrackingMode): the mode to set
        
        
        """
        ...
    def setParticipants(self, participants: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]]) -> None:
        """
        Setter for the participants.
        
        Parameters:
            participants (Map<Integer, String> participants): the participants to set
        
        
        """
        ...
    def setPath(self, path: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
        Setter for the path.
        
        Parameters:
            path (int[]): the path to set
        
        
        """
        ...
    def setPath1(self, path1: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
        Setter for the path1.
        
        Parameters:
            path1 (int[]): the path1 to set
        
        
        """
        ...
    def setPath2(self, path2: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
        Setter for the path2.
        
        Parameters:
            path2 (int[]): the path2 to set
        
        
        """
        ...
    def setRangeMode(self, rangeMode: RangeMode) -> None:
        """
        Setter for the rangeMode.
        
        Parameters:
            rangeMode (RangeMode): the rangeMode to set
        
        
        """
        ...
    def setRangeUnits(self, rangeUnits: RangeUnits) -> None:
        """
        Setter for the rangeUnits.
        
        Parameters:
            rangeUnits (RangeUnits): the rangeUnits to set
        
        
        """
        ...
    def setRawCorrectionRange(self, rawCorrectionRange: float) -> None:
        """
        Setter for the raw correction for range.
        
        Parameters:
            rawCorrectionRange (double): the raw correction for range to set (in getRangeUnits)
        
        
        """
        ...
    def setRawRangeModulus(self, rawRangeModulus: float) -> None:
        """
        Setter for the raw range modulus.
        
        Parameters:
            rawRangeModulus (double): the raw range modulus to set
        
        
        """
        ...
    def setReceiveBand(self, receiveBand: str) -> None:
        """
        Setter for the receiveBand.
        
        Parameters:
            receiveBand (String): the receiveBand to set
        
        
        """
        ...
    def setReceiveDelays(self, receiveDelays: typing.Union[java.util.Map[int, float], typing.Mapping[int, float]]) -> None:
        """
        Setter for the receiveDelays.
        
        Parameters:
            receiveDelays (Map<Integer, Double> receiveDelays): the receiveDelays to set
        
        
        """
        ...
    def setReferenceFrame(self, referenceFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set the reference frame in which data are given: used for RADEC tracking data.
        
        Parameters:
            referenceFrame (FrameFacade): the reference frame to be set
        
        
        """
        ...
    def setStartTime(self, startTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Setter for the startTime.
        
        Parameters:
            startTime (AbsoluteDate): the startTime to set
        
        
        """
        ...
    def setStopTime(self, stopTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Setter for the stopTime.
        
        Parameters:
            stopTime (AbsoluteDate): the stopTime to set
        
        
        """
        ...
    def setTimetagRef(self, timetagRef: 'TimetagReference') -> None:
        """
        Setter for the timetagRef.
        
        Parameters:
            timetagRef (TimetagReference): the timetagRef to set
        
        
        """
        ...
    def setTrackId(self, trackId: str) -> None:
        """
        Setter for the tracking data identifier.
        
        Parameters:
            trackId (String): tracking data identifier
        
        
        """
        ...
    def setTransmitBand(self, transmitBand: str) -> None:
        """
        Setter for the transmitBand.
        
        Parameters:
            transmitBand (String): the transmitBand to set
        
        
        """
        ...
    def setTransmitDelays(self, transmitDelays: typing.Union[java.util.Map[int, float], typing.Mapping[int, float]]) -> None:
        """
        Setter for the transmitDelays.
        
        Parameters:
            transmitDelays (Map<Integer, Double> transmitDelays): the transmitDelays to set
        
        
        """
        ...
    def setTurnaroundDenominator(self, turnaroundDenominator: int) -> None:
        """
        Setter for the turnaroundDenominator.
        
        Parameters:
            turnaroundDenominator (int): the turnaroundDenominator to set
        
        
        """
        ...
    def setTurnaroundNumerator(self, turnaroundNumerator: int) -> None:
        """
        Setter for the turnaroundNumerator.
        
        Parameters:
            turnaroundNumerator (int): the turnaroundNumerator to set
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class Metadata
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class TdmMetadataKey(java.lang.Enum['TdmMetadataKey']):
    """
    Keys for TdmMetadata entries.
    
    Since:
        11.0
    """
    TRACK_ID: typing.ClassVar['TdmMetadataKey'] = ...
    DATA_TYPES: typing.ClassVar['TdmMetadataKey'] = ...
    START_TIME: typing.ClassVar['TdmMetadataKey'] = ...
    STOP_TIME: typing.ClassVar['TdmMetadataKey'] = ...
    PARTICIPANT_1: typing.ClassVar['TdmMetadataKey'] = ...
    PARTICIPANT_2: typing.ClassVar['TdmMetadataKey'] = ...
    PARTICIPANT_3: typing.ClassVar['TdmMetadataKey'] = ...
    PARTICIPANT_4: typing.ClassVar['TdmMetadataKey'] = ...
    PARTICIPANT_5: typing.ClassVar['TdmMetadataKey'] = ...
    MODE: typing.ClassVar['TdmMetadataKey'] = ...
    PATH: typing.ClassVar['TdmMetadataKey'] = ...
    PATH_1: typing.ClassVar['TdmMetadataKey'] = ...
    PATH_2: typing.ClassVar['TdmMetadataKey'] = ...
    EPHEMERIS_NAME_1: typing.ClassVar['TdmMetadataKey'] = ...
    EPHEMERIS_NAME_2: typing.ClassVar['TdmMetadataKey'] = ...
    EPHEMERIS_NAME_3: typing.ClassVar['TdmMetadataKey'] = ...
    EPHEMERIS_NAME_4: typing.ClassVar['TdmMetadataKey'] = ...
    EPHEMERIS_NAME_5: typing.ClassVar['TdmMetadataKey'] = ...
    TRANSMIT_BAND: typing.ClassVar['TdmMetadataKey'] = ...
    RECEIVE_BAND: typing.ClassVar['TdmMetadataKey'] = ...
    TURNAROUND_NUMERATOR: typing.ClassVar['TdmMetadataKey'] = ...
    TURNAROUND_DENOMINATOR: typing.ClassVar['TdmMetadataKey'] = ...
    TIMETAG_REF: typing.ClassVar['TdmMetadataKey'] = ...
    INTEGRATION_INTERVAL: typing.ClassVar['TdmMetadataKey'] = ...
    INTEGRATION_REF: typing.ClassVar['TdmMetadataKey'] = ...
    FREQ_OFFSET: typing.ClassVar['TdmMetadataKey'] = ...
    RANGE_MODE: typing.ClassVar['TdmMetadataKey'] = ...
    RANGE_MODULUS: typing.ClassVar['TdmMetadataKey'] = ...
    RANGE_UNITS: typing.ClassVar['TdmMetadataKey'] = ...
    ANGLE_TYPE: typing.ClassVar['TdmMetadataKey'] = ...
    REFERENCE_FRAME: typing.ClassVar['TdmMetadataKey'] = ...
    INTERPOLATION: typing.ClassVar['TdmMetadataKey'] = ...
    INTERPOLATION_DEGREE: typing.ClassVar['TdmMetadataKey'] = ...
    DOPPLER_COUNT_BIAS: typing.ClassVar['TdmMetadataKey'] = ...
    DOPPLER_COUNT_SCALE: typing.ClassVar['TdmMetadataKey'] = ...
    DOPPLER_COUNT_ROLLOVER: typing.ClassVar['TdmMetadataKey'] = ...
    TRANSMIT_DELAY_1: typing.ClassVar['TdmMetadataKey'] = ...
    TRANSMIT_DELAY_2: typing.ClassVar['TdmMetadataKey'] = ...
    TRANSMIT_DELAY_3: typing.ClassVar['TdmMetadataKey'] = ...
    TRANSMIT_DELAY_4: typing.ClassVar['TdmMetadataKey'] = ...
    TRANSMIT_DELAY_5: typing.ClassVar['TdmMetadataKey'] = ...
    RECEIVE_DELAY_1: typing.ClassVar['TdmMetadataKey'] = ...
    RECEIVE_DELAY_2: typing.ClassVar['TdmMetadataKey'] = ...
    RECEIVE_DELAY_3: typing.ClassVar['TdmMetadataKey'] = ...
    RECEIVE_DELAY_4: typing.ClassVar['TdmMetadataKey'] = ...
    RECEIVE_DELAY_5: typing.ClassVar['TdmMetadataKey'] = ...
    DATA_QUALITY: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_ANGLE_1: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_ANGLE_2: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_DOPPLER: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_MAG: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_RANGE: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_RCS: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_RECEIVE: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_TRANSMIT: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_ABERRATION_YEARLY: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTION_ABERRATION_DIURNAL: typing.ClassVar['TdmMetadataKey'] = ...
    CORRECTIONS_APPLIED: typing.ClassVar['TdmMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: TdmMetadata) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (TdmMetadata): container to fill
        
        Returns:
            true if token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'TdmMetadataKey':
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
    def values() -> typing.MutableSequence['TdmMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (TdmMetadataKey c : TdmMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[TdmHeader, Tdm, 'TdmParser']):
    """
    Class for CCSDS Tracking Data Message parsers.
    
    Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until the message is complete and the parseMessage method has returned. This implies that parsers should not be used in a multi-thread context. The recommended way to use parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
    References:
    
      - pdf ("Tracking Data Message", Blue Book,
        Issue 1, November 2007)
      - pdf ("XML Specification for Navigation
        Data Message", Blue Book, Issue 1, December 2010)
    
    
    Since:
        9.0
    """
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, converter: RangeUnitsConverter, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, converter: RangeUnitsConverter, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray], frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def build(self) -> Tdm:
        """
        Build the file from parsed entries.
        
        Returns:
            parsed file
        
        
        """
        ...
    def finalizeData(self) -> bool:
        """
        Finalize data after parsing.
        
        Specified by: finalizeData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
        Finalize header after parsing.
        
        Specified by: finalizeHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
        Finalize metadata after parsing.
        
        Specified by: finalizeMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def getHeader(self) -> TdmHeader:
        """
        Get file header to fill.
        
        Specified by: getHeader in class AbstractConstituentParser
        
        Returns:
            file header to fill
        
        
        """
        ...
    def inData(self) -> bool:
        """
        Acknowledge data parsing has started.
        
        Specified by: inData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
        Acknowledge header parsing has started.
        
        Specified by: inHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
        Acknowledge metada parsing has started.
        
        Specified by: inMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
        Prepare data for parsing.
        
        Specified by: prepareData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
        Prepare header for parsing.
        
        Specified by: prepareHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
        Prepare metadata for parsing.
        
        Specified by: prepareMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
        Reset parser to initial state before parsing.
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...

class TdmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[TdmHeader, org.orekit.files.ccsds.section.Segment[TdmMetadata, ObservationsBlock], Tdm]):
    """
    Writer for CCSDS Tracking Data Message.
    
    Since:
        11.0
    """
    CCSDS_TDM_VERS: typing.ClassVar[float] = ...
    """
    Version number implemented.
    
    Also see:
        constant
    
    
    """
    KVN_PADDING_WIDTH: typing.ClassVar[int] = ...
    """
    Padding width for aligning the '=' sign.
    
    Also see:
        constant
    
    
    """
    def __init__(self, conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, converter: RangeUnitsConverter):
        """
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildTdmWriter.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            dataContext (DataContext): used to retrieve frames, time scales, etc.
            converter (RangeUnitsConverter): converter for RU (may be null if there are no range observations in
                RU)
        
        
        """
        ...

class TimetagReference(java.lang.Enum['TimetagReference']):
    """
    Reference for time tag.
    
    Since:
        11.0
    """
    TRANSMIT: typing.ClassVar['TimetagReference'] = ...
    RECEIVE: typing.ClassVar['TimetagReference'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'TimetagReference':
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
    def values() -> typing.MutableSequence['TimetagReference']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (TimetagReference c : TimetagReference.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TrackingMode(java.lang.Enum['TrackingMode']):
    """
    Tracking mode.
    
    Since:
        11.0
    """
    SEQUENTIAL: typing.ClassVar['TrackingMode'] = ...
    SINGLE_DIFF: typing.ClassVar['TrackingMode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'TrackingMode':
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
    def values() -> typing.MutableSequence['TrackingMode']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (TrackingMode c : TrackingMode.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IdentityConverter(RangeUnitsConverter):
    """
    Identity converter for Range Units.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def metersToRu(self, metadata: TdmMetadata, date: org.orekit.time.AbsoluteDate, range: float) -> float:
        """
        Convert a range expressed in meters.
        
        Specified by: metersToRu in interface RangeUnitsConverter
        
        Parameters:
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            range (double): range value in meters
        
        Returns:
            range range value in RU
        
        
        """
        ...
    def ruToMeters(self, metadata: TdmMetadata, date: org.orekit.time.AbsoluteDate, range: float) -> float:
        """
        Convert a range expressed in RU.
        
        Specified by: ruToMeters in interface RangeUnitsConverter
        
        Parameters:
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            range (double): range value in RU
        
        Returns:
            range range value in meters
        
        
        """
        ...

class PythonRangeUnitsConverter(RangeUnitsConverter):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def metersToRu(self, metadata: TdmMetadata, date: org.orekit.time.AbsoluteDate, range: float) -> float:
        """
        Convert a range expressed in meters.
        
        Specified by: metersToRu in interface RangeUnitsConverter
        
        Parameters:
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            range (double): range value in meters
        
        Returns:
            range range value in RU
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def ruToMeters(self, metadata: TdmMetadata, date: org.orekit.time.AbsoluteDate, range: float) -> float:
        """
        Convert a range expressed in RU.
        
        Specified by: ruToMeters in interface RangeUnitsConverter
        
        Parameters:
            metadata (TdmMetadata): metadata corresponding to the observation
            date (AbsoluteDate): observation date
            range (double): range value in RU
        
        Returns:
            range range value in meters
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.tdm")``.

    AngleType: typing.Type[AngleType]
    CorrectionApplied: typing.Type[CorrectionApplied]
    DataQuality: typing.Type[DataQuality]
    IdentityConverter: typing.Type[IdentityConverter]
    IntegrationReference: typing.Type[IntegrationReference]
    Observation: typing.Type[Observation]
    ObservationType: typing.Type[ObservationType]
    ObservationsBlock: typing.Type[ObservationsBlock]
    PythonRangeUnitsConverter: typing.Type[PythonRangeUnitsConverter]
    RangeMode: typing.Type[RangeMode]
    RangeUnits: typing.Type[RangeUnits]
    RangeUnitsConverter: typing.Type[RangeUnitsConverter]
    Tdm: typing.Type[Tdm]
    TdmDataKey: typing.Type[TdmDataKey]
    TdmHeader: typing.Type[TdmHeader]
    TdmMetadata: typing.Type[TdmMetadata]
    TdmMetadataKey: typing.Type[TdmMetadataKey]
    TdmParser: typing.Type[TdmParser]
    TdmWriter: typing.Type[TdmWriter]
    TimetagReference: typing.Type[TimetagReference]
    TrackingMode: typing.Type[TrackingMode]
