import java.lang
import java.util
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.time
import org.orekit.utils
import typing



class AngleType(java.lang.Enum['AngleType']):
    """
    public enum AngleType extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.AngleType`>
    
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
    def valueOf(string: str) -> 'AngleType':
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
    def values() -> typing.List['AngleType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (AngleType c : AngleType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CorrectionApplied(java.lang.Enum['CorrectionApplied']):
    """
    public enum CorrectionApplied extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.CorrectionApplied`>
    
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
    def valueOf(string: str) -> 'CorrectionApplied':
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
    def values() -> typing.List['CorrectionApplied']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CorrectionApplied c : CorrectionApplied.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DataQuality(java.lang.Enum['DataQuality']):
    """
    public enum DataQuality extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.DataQuality`>
    
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
    def valueOf(string: str) -> 'DataQuality':
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
    def values() -> typing.List['DataQuality']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (DataQuality c : DataQuality.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IntegrationReference(java.lang.Enum['IntegrationReference']):
    """
    public enum IntegrationReference extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.IntegrationReference`>
    
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
    def valueOf(string: str) -> 'IntegrationReference':
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
    def values() -> typing.List['IntegrationReference']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (IntegrationReference c : IntegrationReference.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Observation:
    """
    public class Observation extends Object
    
        The Observation class contains the data from an observation line.
    
        It is not an Orekit object yet. It is a simple container holding:
    
          - a keyword, the type of the observation;
          - a timetag, the epoch of the observation;
          - a measurement, the value of the observation.
    
    
        WARNING. The same class handles many different measurements types (range, Doppler, clocks, pressure, power to noise
        ratioÃ¢â‚¬Â¦). Since Orekit 11.0, it uses only SI units, so angular measurements have already been converted in radians,
        range has been converted in meters (according to the :meth:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata.getRangeUnits`,
        Doppler has been converted to meters per second. Up to Orekit 10.x, the measurements were raw measurements as read in
        the TDM.
    """
    def __init__(self, observationType: 'ObservationType', absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
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
    public enum ObservationType extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.ObservationType`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.tdm.Observation` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, rangeUnitsConverter: 'RangeUnitsConverter', tdmMetadata: 'TdmMetadata', observationsBlock: 'ObservationsBlock') -> bool:
        """
            Process an observation line.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): parse token
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                ruConverter (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`): converter for :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU` (may be null)
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata for current block
                observationsBlock (:class:`~org.orekit.files.ccsds.ndm.tdm.ObservationsBlock`): observation block to fill
        
            Returns:
                true if token was accepted
        
        
        """
        ...
    def rawToSI(self, rangeUnitsConverter: 'RangeUnitsConverter', tdmMetadata: 'TdmMetadata', absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a measurement to SI units.
        
            Parameters:
                ruConverter (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`): converter for :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU` (may be null)
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
                rawValue (double): measurement raw value
        
            Returns:
                measurement in SI units
        
        
        """
        ...
    def siToRaw(self, rangeUnitsConverter: 'RangeUnitsConverter', tdmMetadata: 'TdmMetadata', absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a measurement from SI units.
        
            Parameters:
                ruConverter (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`): converter for :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU` (may be null)
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
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
    def valueOf(string: str) -> 'ObservationType':
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
    def values() -> typing.List['ObservationType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ObservationType c : ObservationType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ObservationsBlock(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    public class ObservationsBlock extends :class:`~org.orekit.files.ccsds.section.CommentsContainer` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        The Observations Block class contain metadata and the list of observation data lines.
    
        The reason for which the observations have been separated into blocks is that the different data blocks in a TDM file
        usually refers to different types of observations.
    
        An observation block is associated with a TDM metadata object and contains a list of observations.
    
        At this level, an observation is not an Orekit object, it is a custom object containing:
    
        - a keyword, the type of the observation;
    
        - a timetag, the date of the observation;
    
        - a measurement, the value of the observation.
    """
    def __init__(self): ...
    @typing.overload
    def addObservation(self, observation: Observation) -> None:
        """
            Adds an observation data line.
        
            Parameters:
                observation (:class:`~org.orekit.files.ccsds.ndm.tdm.Observation`): the observation to add to the list
        
            Adds an observation data line.
        
            Parameters:
                type (:class:`~org.orekit.files.ccsds.ndm.tdm.ObservationType`): type of the observation
                epoch (:class:`~org.orekit.time.AbsoluteDate`): the timetag
                measurement (double): the measurement
        
        
        """
        ...
    @typing.overload
    def addObservation(self, observationType: ObservationType, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> None: ...
    def getObservations(self) -> java.util.List[Observation]: ...
    def setObservations(self, list: java.util.List[Observation]) -> None: ...

class RangeMode(java.lang.Enum['RangeMode']):
    """
    public enum RangeMode extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.RangeMode`>
    
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
    def valueOf(string: str) -> 'RangeMode':
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
    def values() -> typing.List['RangeMode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (RangeMode c : RangeMode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RangeUnits(java.lang.Enum['RangeUnits']):
    """
    public enum RangeUnits extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits`>
    
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
    def valueOf(string: str) -> 'RangeUnits':
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
    def values() -> typing.List['RangeUnits']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (RangeUnits c : RangeUnits.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RangeUnitsConverter:
    """
    public interface RangeUnitsConverter
    
        Interface for converting :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU` to meters.
    
        Implementations of this interface must be provided by user when dealing with
        :class:`~org.orekit.files.ccsds.ndm.tdm.Tdm` that include range observations in
        :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`. These units are intended for mission-specific measurements and
        must be described in an Interface Control Document.
    
        Since:
            11.0
    """
    def metersToRu(self, tdmMetadata: 'TdmMetadata', absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a range expressed in meters.
        
            Parameters:
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
                range (double): range value in meters
        
            Returns:
                range range value in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
        
        """
        ...
    def ruToMeters(self, tdmMetadata: 'TdmMetadata', absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a range expressed in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`.
        
            Parameters:
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
                range (double): range value in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
            Returns:
                range range value in meters
        
        
        """
        ...

class Tdm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment['TdmMetadata', ObservationsBlock]]):
    """
    public class Tdm extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.section.Header`,:class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`,:class:`~org.orekit.files.ccsds.ndm.tdm.ObservationsBlock`>>
    
        This class stores all the information of the CCSDS Tracking Data Message parsed by TDMParser or TDMXMLParser.
    
        It contains the header and a list of Observations Blocks each containing TDM metadata and a list of observation data
        lines.
    
        At this level the observations are not Orekit objects but custom object containing a keyword (type of observation), a
        timetag (date of the observation) and a measurement (value of the observation).
    
        It is up to the user to convert these observations to Orekit tracking object (Range, Angular, TurnAroundRange etc...).
    
        References:
    
        CCSDS 503.0-B-1 recommended standard ("Tracking Data Message", Blue Book, Version 1.0, November 2007).
    
        Since:
            9.0
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final String ROOT
    
        Root element for XML files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    public static final String FORMAT_VERSION_KEY
    
        Key for format version.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, header: org.orekit.files.ccsds.section.Header, list: java.util.List[org.orekit.files.ccsds.section.Segment['TdmMetadata', ObservationsBlock]], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...

class TdmDataKey(java.lang.Enum['TdmDataKey']):
    """
    public enum TdmDataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.TdmDataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.tdm.Observation` entries, except the measurements themselves.
    
        Since:
            11.0
    """
    observation: typing.ClassVar['TdmDataKey'] = ...
    COMMENT: typing.ClassVar['TdmDataKey'] = ...
    EPOCH: typing.ClassVar['TdmDataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, observationsBlock: ObservationsBlock) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                observationsBlock (:class:`~org.orekit.files.ccsds.ndm.tdm.ObservationsBlock`): observation block to fill
        
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
    def valueOf(string: str) -> 'TdmDataKey':
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
    def values() -> typing.List['TdmDataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TdmDataKey c : TdmDataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    public class TdmMetadata extends :class:`~org.orekit.files.ccsds.section.Metadata`
    
        The TDMMetadata class gathers the meta-data present in the Tracking Data Message (TDM).
    
        References:
    
        CCSDS 503.0-B-1 recommended standard. Â§3.3 ("Tracking Data Message", Blue Book, Version 1.0, November 2007).
    
        Since:
            9.0
    """
    def __init__(self): ...
    def addEphemerisName(self, int: int, string: str) -> None:
        """
            Adds an ephemeris name to the list.
        
            Parameters:
                participantNumber (int): the number of the participant
                ephemerisName (String): name of the ephemeris for the participant
        
        
        """
        ...
    def addParticipant(self, int: int, string: str) -> None:
        """
            Adds a participant to the list.
        
            Parameters:
                participantNumber (int): the number of the participant to add
                participant (String): the name of the participant to add
        
        
        """
        ...
    def addReceiveDelay(self, int: int, double: float) -> None:
        """
            Adds a receive delay to the list.
        
            Parameters:
                participantNumber (int): the number of the participants for which the receive delay is given
                receiveDelay (double): the receive delay value to add
        
        
        """
        ...
    def addTransmitDelay(self, int: int, double: float) -> None:
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
    def getCorrectionRange(self, rangeUnitsConverter: RangeUnitsConverter) -> float:
        """
            Getter for the raw correction for range in meters.
        
            Parameters:
                converter (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`): converter to use if :meth:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata.getRangeUnits` are set to
                    :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
            Returns:
                the raw correction for range in meters
        
        
        """
        ...
    def getCorrectionRcs(self) -> float:
        """
            Getter for the radar cross section correction.
        
            Returns:
                the radar cross section correction in mÂ²
        
        
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
    def getDataTypes(self) -> java.util.List[ObservationType]: ...
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
    def getPath(self) -> typing.List[int]:
        """
            Getter for the path.
        
            Returns:
                the path
        
        
        """
        ...
    def getPath1(self) -> typing.List[int]:
        """
            Getter for the path1.
        
            Returns:
                the path1
        
        
        """
        ...
    def getPath2(self) -> typing.List[int]:
        """
            Getter for the path2.
        
            Returns:
                the path2
        
        
        """
        ...
    def getRangeMode(self) -> RangeMode:
        """
            Getter for the rangeMode.
        
            Returns:
                the rangeMode
        
        
        """
        ...
    def getRangeModulus(self, rangeUnitsConverter: RangeUnitsConverter) -> float:
        """
            Getter for the range modulus in meters.
        
            Parameters:
                converter (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`): converter to use if :meth:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata.getRangeUnits` are set to
                    :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
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
                the raw correction for range (in :meth:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata.getRangeUnits`)
        
        
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
            Get the the value of :code:`REFERENCE_FRAME` as an Orekit :class:`~org.orekit.frames.Frame`.
        
            Returns:
                The reference frame specified by the :code:`REFERENCE_FRAME` keyword.
        
        
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
                angleType (:class:`~org.orekit.files.ccsds.ndm.tdm.AngleType`): the angleType to set
        
        
        """
        ...
    def setCorrectionAberrationDiurnal(self, double: float) -> None:
        """
            Setter for the diurnal aberration correction.
        
            Parameters:
                correctionAberrationDiurnal (double): the diurnal aberration correction in radians to set
        
        
        """
        ...
    def setCorrectionAberrationYearly(self, double: float) -> None:
        """
            Setter for the yearly aberration correction.
        
            Parameters:
                correctionAberrationYearly (double): the yearly aberration correction in radians to set
        
        
        """
        ...
    def setCorrectionAngle1(self, double: float) -> None:
        """
            Setter for the correctionAngle1.
        
            Parameters:
                correctionAngle1 (double): the correctionAngle1 to set (in radians)
        
        
        """
        ...
    def setCorrectionAngle2(self, double: float) -> None:
        """
            Setter for the correctionAngle2.
        
            Parameters:
                correctionAngle2 (double): the correctionAngle2 to set (in radians)
        
        
        """
        ...
    def setCorrectionDoppler(self, double: float) -> None:
        """
            Setter for the correctionDoppler.
        
            Parameters:
                correctionDoppler (double): the correctionDoppler to set (in m/s)
        
        
        """
        ...
    def setCorrectionMagnitude(self, double: float) -> None:
        """
            Setter for the magnitude correction.
        
            Parameters:
                correctionMagnitude (double): the magnitude correction to set
        
        
        """
        ...
    def setCorrectionRcs(self, double: float) -> None:
        """
            Setter for the radar cross section correction.
        
            Parameters:
                correctionRcs (double): the radar cross section correction in mÂ² to set
        
        
        """
        ...
    def setCorrectionReceive(self, double: float) -> None:
        """
            Setter for the correctionReceive.
        
            Parameters:
                correctionReceive (double): the correctionReceive to set (in TDM units, without conversion)
        
        
        """
        ...
    def setCorrectionTransmit(self, double: float) -> None:
        """
            Setter for the correctionTransmit.
        
            Parameters:
                correctionTransmit (double): the correctionTransmit to set (in TDM units, without conversion)
        
        
        """
        ...
    def setCorrectionsApplied(self, correctionApplied: CorrectionApplied) -> None:
        """
            Setter for the correctionApplied.
        
            Parameters:
                correctionsApplied (:class:`~org.orekit.files.ccsds.ndm.tdm.CorrectionApplied`): the correctionApplied to set (in TDM units, without conversion)
        
        
        """
        ...
    def setDataQuality(self, dataQuality: DataQuality) -> None:
        """
            Setter for the dataQuality.
        
            Parameters:
                dataQuality (:class:`~org.orekit.files.ccsds.ndm.tdm.DataQuality`): the dataQuality to set
        
        
        """
        ...
    def setDataTypes(self, list: java.util.List[ObservationType]) -> None: ...
    def setDopplerCountBias(self, double: float) -> None:
        """
            Set the Doppler count bias.
        
            Parameters:
                dopplerCountBias (double): Doppler count bias in Hz to set
        
        
        """
        ...
    def setDopplerCountRollover(self, boolean: bool) -> None:
        """
            Set the indicator for Doppler count rollover.
        
            Parameters:
                dopplerCountRollover (boolean): indicator for Doppler count rollover
        
        
        """
        ...
    def setDopplerCountScale(self, double: float) -> None:
        """
            Set the Doppler count Scale.
        
            Parameters:
                dopplerCountScale (double): Doppler count scale to set
        
        
        """
        ...
    def setEphemerisNames(self, map: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]]) -> None:
        """
            Setter for the external ephemeris names for participants.
        
            Parameters:
                ephemerisNames (Map<Integer,String> ephemerisNames): external ephemeris names for participants
        
        
        """
        ...
    def setFreqOffset(self, double: float) -> None:
        """
            Setter for the freqOffset.
        
            Parameters:
                freqOffset (double): the freqOffset to set
        
        
        """
        ...
    def setIntegrationInterval(self, double: float) -> None:
        """
            Setter for the integrationInterval.
        
            Parameters:
                integrationInterval (double): the integrationInterval to set
        
        
        """
        ...
    def setIntegrationRef(self, integrationReference: IntegrationReference) -> None:
        """
            Setter for the integrationRef.
        
            Parameters:
                integrationRef (:class:`~org.orekit.files.ccsds.ndm.tdm.IntegrationReference`): the integrationRef to set
        
        
        """
        ...
    def setInterpolationDegree(self, int: int) -> None:
        """
            Set the interpolation degree.
        
            Parameters:
                interpolationDegree (int): the interpolation degree to be set
        
        
        """
        ...
    def setInterpolationMethod(self, string: str) -> None:
        """
            Set the interpolation method to be used.
        
            Parameters:
                interpolationMethod (String): the interpolation method to be set
        
        
        """
        ...
    def setMode(self, trackingMode: 'TrackingMode') -> None:
        """
            Setter for the mode.
        
            Parameters:
                mode (:class:`~org.orekit.files.ccsds.ndm.tdm.TrackingMode`): the mode to set
        
        
        """
        ...
    def setParticipants(self, map: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]]) -> None:
        """
            Setter for the participants.
        
            Parameters:
                participants (Map<Integer,String> participants): the participants to set
        
        
        """
        ...
    def setPath(self, intArray: typing.List[int]) -> None:
        """
            Setter for the path.
        
            Parameters:
                path (int[]): the path to set
        
        
        """
        ...
    def setPath1(self, intArray: typing.List[int]) -> None:
        """
            Setter for the path1.
        
            Parameters:
                path1 (int[]): the path1 to set
        
        
        """
        ...
    def setPath2(self, intArray: typing.List[int]) -> None:
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
                rangeMode (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeMode`): the rangeMode to set
        
        
        """
        ...
    def setRangeUnits(self, rangeUnits: RangeUnits) -> None:
        """
            Setter for the rangeUnits.
        
            Parameters:
                rangeUnits (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits`): the rangeUnits to set
        
        
        """
        ...
    def setRawCorrectionRange(self, double: float) -> None:
        """
            Setter for the raw correction for range.
        
            Parameters:
                rawCorrectionRange (double): the raw correction for range to set (in :meth:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata.getRangeUnits`)
        
        
        """
        ...
    def setRawRangeModulus(self, double: float) -> None:
        """
            Setter for the raw range modulus.
        
            Parameters:
                rawRangeModulus (double): the raw range modulus to set
        
        
        """
        ...
    def setReceiveBand(self, string: str) -> None:
        """
            Setter for the receiveBand.
        
            Parameters:
                receiveBand (String): the receiveBand to set
        
        
        """
        ...
    def setReceiveDelays(self, map: typing.Union[java.util.Map[int, float], typing.Mapping[int, float]]) -> None:
        """
            Setter for the receiveDelays.
        
            Parameters:
                receiveDelays (Map<Integer,Double> receiveDelays): the receiveDelays to set
        
        
        """
        ...
    def setReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set the reference frame in which data are given: used for RADEC tracking data.
        
            Parameters:
                referenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the startTime.
        
            Parameters:
                startTime (:class:`~org.orekit.time.AbsoluteDate`): the startTime to set
        
        
        """
        ...
    def setStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the stopTime.
        
            Parameters:
                stopTime (:class:`~org.orekit.time.AbsoluteDate`): the stopTime to set
        
        
        """
        ...
    def setTimetagRef(self, timetagReference: 'TimetagReference') -> None:
        """
            Setter for the timetagRef.
        
            Parameters:
                timetagRef (:class:`~org.orekit.files.ccsds.ndm.tdm.TimetagReference`): the timetagRef to set
        
        
        """
        ...
    def setTrackId(self, string: str) -> None:
        """
            Setter for the tracking data identifier.
        
            Parameters:
                trackId (String): tracking data identifier
        
        
        """
        ...
    def setTransmitBand(self, string: str) -> None:
        """
            Setter for the transmitBand.
        
            Parameters:
                transmitBand (String): the transmitBand to set
        
        
        """
        ...
    def setTransmitDelays(self, map: typing.Union[java.util.Map[int, float], typing.Mapping[int, float]]) -> None:
        """
            Setter for the transmitDelays.
        
            Parameters:
                transmitDelays (Map<Integer,Double> transmitDelays): the transmitDelays to set
        
        
        """
        ...
    def setTurnaroundDenominator(self, int: int) -> None:
        """
            Setter for the turnaroundDenominator.
        
            Parameters:
                turnaroundDenominator (int): the turnaroundDenominator to set
        
        
        """
        ...
    def setTurnaroundNumerator(self, int: int) -> None:
        """
            Setter for the turnaroundNumerator.
        
            Parameters:
                turnaroundNumerator (int): the turnaroundNumerator to set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.Metadata.validate` in class :class:`~org.orekit.files.ccsds.section.Metadata`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class TdmMetadataKey(java.lang.Enum['TdmMetadataKey']):
    """
    public enum TdmMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, tdmMetadata: TdmMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'TdmMetadataKey':
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
    def values() -> typing.List['TdmMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TdmMetadataKey c : TdmMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[Tdm, 'TdmParser']):
    """
    public class TdmParser extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<:class:`~org.orekit.files.ccsds.ndm.tdm.Tdm`,:class:`~org.orekit.files.ccsds.ndm.tdm.TdmParser`>
    
        Class for CCSDS Tracking Data Message parsers.
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        References:
    
        - CCSDS 503.0-B-1 recommended standard ("Tracking Data Message", Blue Book, Issue 1, November 2007).
    
        - CCSDS 505.0-B-1 recommended standard ("XML Specification for Navigation Data Message", Blue Book, Issue 1, December
        2010).
    
    
        Since:
            9.0
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, rangeUnitsConverter: RangeUnitsConverter): ...
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
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeData`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
            Finalize header after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
            Finalize metadata after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeMetadata`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def getHeader(self) -> org.orekit.files.ccsds.section.Header:
        """
            Get file header to fill.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.getHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                file header to fill
        
        
        """
        ...
    def inData(self) -> bool:
        """
            Acknowledge data parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inData`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
            Acknowledge header parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
            Acknowledge metada parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inMetadata`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
            Prepare data for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareData`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
            Prepare header for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
            Prepare metadata for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareMetadata`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class TdmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment[TdmMetadata, ObservationsBlock], Tdm]):
    """
    public class TdmWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.section.Header`,:class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`,:class:`~org.orekit.files.ccsds.ndm.tdm.ObservationsBlock`>,:class:`~org.orekit.files.ccsds.ndm.tdm.Tdm`>
    
        Writer for CCSDS Tracking Data Message.
    
        Since:
            11.0
    """
    CCSDS_TDM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_TDM_VERS
    
        Version number implemented.
    
        Also see:
            :meth:`~constant`
    
    
    """
    KVN_PADDING_WIDTH: typing.ClassVar[int] = ...
    """
    public static final int KVN_PADDING_WIDTH
    
        Padding width for aligning the '=' sign.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, rangeUnitsConverter: RangeUnitsConverter): ...
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, segment: org.orekit.files.ccsds.section.Segment[TdmMetadata, ObservationsBlock]) -> None: ...

class TimetagReference(java.lang.Enum['TimetagReference']):
    """
    public enum TimetagReference extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.TimetagReference`>
    
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
    def valueOf(string: str) -> 'TimetagReference':
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
    def values() -> typing.List['TimetagReference']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TimetagReference c : TimetagReference.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TrackingMode(java.lang.Enum['TrackingMode']):
    """
    public enum TrackingMode extends Enum<:class:`~org.orekit.files.ccsds.ndm.tdm.TrackingMode`>
    
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
    def valueOf(string: str) -> 'TrackingMode':
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
    def values() -> typing.List['TrackingMode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TrackingMode c : TrackingMode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IdentityConverter(RangeUnitsConverter):
    """
    public class IdentityConverter extends Object implements :class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`
    
        Identity converter for Range Units.
    
    
        Since:
            11.0
    """
    def __init__(self): ...
    def metersToRu(self, tdmMetadata: TdmMetadata, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a range expressed in meters.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter.metersToRu`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`
        
            Parameters:
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
                range (double): range value in meters
        
            Returns:
                range range value in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
        
        """
        ...
    def ruToMeters(self, tdmMetadata: TdmMetadata, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a range expressed in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter.ruToMeters`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`
        
            Parameters:
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
                range (double): range value in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
            Returns:
                range range value in meters
        
        
        """
        ...

class PythonRangeUnitsConverter(RangeUnitsConverter):
    """
    public class PythonRangeUnitsConverter extends Object implements :class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def metersToRu(self, tdmMetadata: TdmMetadata, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a range expressed in meters.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter.metersToRu`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`
        
            Parameters:
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
                range (double): range value in meters
        
            Returns:
                range range value in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
        
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
    def ruToMeters(self, tdmMetadata: TdmMetadata, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> float:
        """
            Convert a range expressed in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter.ruToMeters`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`
        
            Parameters:
                metadata (:class:`~org.orekit.files.ccsds.ndm.tdm.TdmMetadata`): metadata corresponding to the observation
                date (:class:`~org.orekit.time.AbsoluteDate`): observation date
                range (double): range value in :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
            Returns:
                range range value in meters
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
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
    TdmMetadata: typing.Type[TdmMetadata]
    TdmMetadataKey: typing.Type[TdmMetadataKey]
    TdmParser: typing.Type[TdmParser]
    TdmWriter: typing.Type[TdmWriter]
    TimetagReference: typing.Type[TimetagReference]
    TrackingMode: typing.Type[TrackingMode]
