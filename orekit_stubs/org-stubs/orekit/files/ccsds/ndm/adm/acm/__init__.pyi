
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.attitudes
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.adm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.general
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class Acm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.adm.AdmHeader, org.orekit.files.ccsds.section.Segment['AcmMetadata', 'AcmData']], org.orekit.files.general.AttitudeEphemerisFile[org.orekit.utils.TimeStampedAngularCoordinates, 'AttitudeStateHistory']):
    """
    This class gathers the informations present in the Attitude Comprehensive Message (ACM).
    
    Since:
        12.0
    """
    ROOT: typing.ClassVar[str] = ...
    """
    Root element for XML messages.
    
    Also see:
        constant
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    Key for format version.
    
    Also see:
        constant
    
    
    """
    ATT_LINE: typing.ClassVar[str] = ...
    """
    Attitude line element for XML messages.
    
    Also see:
        constant
    
    
    """
    COV_LINE: typing.ClassVar[str] = ...
    """
    Covariance line element for XML messages.
    
    Also see:
        constant
    
    
    """
    UNKNOWN_OBJECT: typing.ClassVar[str] = ...
    """
    Default name for unknown object.
    
    Also see:
        constant
    
    
    """
    def __init__(self, header: org.orekit.files.ccsds.ndm.adm.AdmHeader, segments: java.util.List[org.orekit.files.ccsds.section.Segment['AcmMetadata', 'AcmData']], conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext):
        """
        Simple constructor.
        
        Parameters:
            header (AdmHeader): file header
            segments (List<Segment<AcmMetadata, AcmData>>): ile segments
            conventions (IERSConventions): IERS conventions
            dataContext (DataContext): used for creating frames, time scales, etc.
        
        
        """
        ...
    def getData(self) -> 'AcmData':
        """
        Get the data from the single getSegments.
        
        Returns:
            data from the single getSegments
        
        
        """
        ...
    def getMetadata(self) -> 'AcmMetadata':
        """
        Get the metadata from the single getSegments.
        
        Returns:
            metadata from the single getSegments
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'AcmSatelliteEphemeris']:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Specified by: getSatellites in interface AttitudeEphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...

class AcmData(org.orekit.files.ccsds.section.Data):
    """
    Data container for Attitude Comprehensive Messages.
    
    Since:
        12.0
    """
    def __init__(self, attitudeBlocks: java.util.List['AttitudeStateHistory'], physicBlock: 'AttitudePhysicalProperties', covarianceBlocks: java.util.List['AttitudeCovarianceHistory'], maneuverBlocks: java.util.List['AttitudeManeuver'], attitudeDeterminationBlock: 'AttitudeDetermination', userDefinedBlock: org.orekit.files.ccsds.ndm.odm.UserDefined):
        """
        Simple constructor.
        
        Parameters:
            attitudeBlocks (List<AttitudeStateHistory> attitudeBlocks): attitude state histories logical blocks (may be empty)
            physicBlock (AttitudePhysicalProperties): physical properties logical block (may be null)
            covarianceBlocks (List<AttitudeCovarianceHistory> covarianceBlocks): covariance logical blocks (may be empty)
            maneuverBlocks (List<AttitudeManeuver> maneuverBlocks): maneuvers logical blocks (may be empty)
            attitudeDeterminationBlock (AttitudeDetermination): attitude determination logical block (may be null)
            userDefinedBlock (UserDefined): user defined parameters logical block (may be null)
        
        
        """
        ...
    def getAttitudeBlocks(self) -> java.util.List['AttitudeStateHistory']:
        """
        Get attitude state histories logical blocks.
        
        Returns:
            attitude state histories logical blocks (may be null)
        
        
        """
        ...
    def getAttitudeDeterminationBlock(self) -> 'AttitudeDetermination':
        """
        Get attitude determination logical block.
        
        Returns:
            attitude determination logical block (may be null)
        
        
        """
        ...
    def getCovarianceBlocks(self) -> java.util.List['AttitudeCovarianceHistory']:
        """
        Get covariance logical blocks.
        
        Returns:
            covariance logical blocks (may be null)
        
        
        """
        ...
    def getManeuverBlocks(self) -> java.util.List['AttitudeManeuver']:
        """
        Get maneuvers logical blocks.
        
        Returns:
            maneuvers logical block (may be null)
        
        
        """
        ...
    def getPhysicBlock(self) -> 'AttitudePhysicalProperties':
        """
        Get physical properties logical block.
        
        Returns:
            physical properties logical block (may be null)
        
        
        """
        ...
    def getUserDefinedBlock(self) -> org.orekit.files.ccsds.ndm.odm.UserDefined:
        """
        Get user defined parameters logical block.
        
        Returns:
            user defined parameters logical block (may be null)
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AcmDataSubStructureKey(java.lang.Enum['AcmDataSubStructureKey']):
    """
    Keywords for ACM data sub-structure.
    
    Since:
        12.0
    """
    ATT: typing.ClassVar['AcmDataSubStructureKey'] = ...
    att: typing.ClassVar['AcmDataSubStructureKey'] = ...
    PHYS: typing.ClassVar['AcmDataSubStructureKey'] = ...
    phys: typing.ClassVar['AcmDataSubStructureKey'] = ...
    COV: typing.ClassVar['AcmDataSubStructureKey'] = ...
    cov: typing.ClassVar['AcmDataSubStructureKey'] = ...
    MAN: typing.ClassVar['AcmDataSubStructureKey'] = ...
    man: typing.ClassVar['AcmDataSubStructureKey'] = ...
    AD: typing.ClassVar['AcmDataSubStructureKey'] = ...
    ad: typing.ClassVar['AcmDataSubStructureKey'] = ...
    USER: typing.ClassVar['AcmDataSubStructureKey'] = ...
    user: typing.ClassVar['AcmDataSubStructureKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, parser: 'AcmParser') -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            parser (AcmParser): ACM file parser
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AcmDataSubStructureKey':
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
    def values() -> typing.MutableSequence['AcmDataSubStructureKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AcmDataSubStructureKey c : AcmDataSubStructureKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AcmElements(java.lang.Enum['AcmElements']):
    """
    Data elements types used in CCSDS Acm.
    
    Since:
        12.0
    """
    ATT: typing.ClassVar['AcmElements'] = ...
    PHYS: typing.ClassVar['AcmElements'] = ...
    COV: typing.ClassVar['AcmElements'] = ...
    MAN: typing.ClassVar['AcmElements'] = ...
    AD: typing.ClassVar['AcmElements'] = ...
    USER: typing.ClassVar['AcmElements'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AcmElements':
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
    def values() -> typing.MutableSequence['AcmElements']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AcmElements c : AcmElements.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AcmMetadata(org.orekit.files.ccsds.ndm.adm.AdmMetadata):
    """
    Meta-data for AcmMetadata.
    
    Since:
        12.0
    """
    def __init__(self, dataContext: org.orekit.data.DataContext):
        """
        Create a new meta-data.
        
        Parameters:
            dataContext (DataContext): data context
        
        
        """
        ...
    def getAcmDataElements(self) -> java.util.List[AcmElements]:
        """
        Get the list of elements of information data blocks included in this message.
        
        Returns:
            list of elements of information data blocks included in this message
        
        
        """
        ...
    def getCatalogName(self) -> str:
        """
        Get the specification of satellite catalog source.
        
        Returns:
            specification of satellite catalog source
        
        
        """
        ...
    def getEpochT0(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the epoch to which all relative times are referenced in data blocks.
        
        Returns:
            epoch to which all relative times are referenced in data blocks
        
        
        """
        ...
    def getInternationalDesignator(self) -> str:
        """
        Get the international designator for the object.
        
        Returns:
            international designator for the object
        
        
        """
        ...
    def getNextLeapEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the epoch of next leap second.
        
        Returns:
            epoch of next leap second
        
        
        """
        ...
    def getNextLeapTaimutc(self) -> float:
        """
        Get the difference (TAI – UTC) in seconds incorporated at epoch getNextLeapEpoch.
        
        Returns:
            difference (TAI – UTC) in seconds incorporated at epoch
            getNextLeapEpoch
        
        
        """
        ...
    def getObjectDesignator(self) -> str:
        """
        Get the unique satellite identification designator for the object.
        
        Returns:
            unique satellite identification designator for the object.
        
        
        """
        ...
    def getOdmMessageLink(self) -> str:
        """
        Get the Unique identifier of Orbit Data Message linked to this Attitude Data Message.
        
        Returns:
            Unique identifier of Orbit Data Message linked to this Attitude Data Message
        
        
        """
        ...
    def getOriginatorAddress(self) -> str:
        """
        Get the address of Programmatic Point Of Contact at originator.
        
        Returns:
            address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOriginatorEmail(self) -> str:
        """
        Get the email address of Programmatic Point Of Contact at originator.
        
        Returns:
            email address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOriginatorPOC(self) -> str:
        """
        Get the programmatic Point Of Contact at originator.
        
        Returns:
            programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOriginatorPhone(self) -> str:
        """
        Get the phone number of Programmatic Point Of Contact at originator.
        
        Returns:
            phone number of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOriginatorPosition(self) -> str:
        """
        Get the position of Programmatic Point Of Contact at originator.
        
        Returns:
            position of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def getStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the time of the earliest data contained in the OCM.
        
        Returns:
            time of the earliest data contained in the OCM
        
        
        """
        ...
    def getStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the time of the latest data contained in the OCM.
        
        Returns:
            time of the latest data contained in the OCM
        
        
        """
        ...
    def getTaimutcT0(self) -> float:
        """
        Get the difference (TAI – UTC) in seconds at epoch getEpochT0.
        
        Returns:
            difference (TAI – UTC) in seconds at epoch getEpochT0
        
        
        """
        ...
    def setAcmDataElements(self, acmDataElements: java.util.List[AcmElements]) -> None:
        """
        Set the list of elements of information data blocks included in this message.
        
        Parameters:
            acmDataElements (List<AcmElements> acmDataElements): list of elements of information data blocks included in this message
        
        
        """
        ...
    def setCatalogName(self, catalogName: str) -> None:
        """
        Set the specification of satellite catalog source.
        
        Parameters:
            catalogName (String): specification of satellite catalog source
        
        
        """
        ...
    def setEpochT0(self, epochT0: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the epoch to which all relative times are referenced in data blocks.
        
        Parameters:
            epochT0 (AbsoluteDate): epoch to which all relative times are referenced in data blocks
        
        
        """
        ...
    def setInternationalDesignator(self, internationalDesignator: str) -> None:
        """
        Set the international designator for the object.
        
        Parameters:
            internationalDesignator (String): international designator for the object
        
        
        """
        ...
    def setNextLeapEpoch(self, nextLeapEpoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the epoch of next leap second.
        
        Parameters:
            nextLeapEpoch (AbsoluteDate): epoch of next leap second
        
        
        """
        ...
    def setNextLeapTaimutc(self, nextLeapTaimutc: float) -> None:
        """
        Set the difference (TAI – UTC) in seconds incorporated at epoch getNextLeapEpoch.
        
        Parameters:
            nextLeapTaimutc (double): difference (TAI – UTC) in seconds incorporated at epoch
                getNextLeapEpoch
        
        
        """
        ...
    def setObjectDesignator(self, objectDesignator: str) -> None:
        """
        Set the unique satellite identification designator for the object.
        
        Parameters:
            objectDesignator (String): unique satellite identification designator for the object
        
        
        """
        ...
    def setOdmMessageLink(self, odmMessageLink: str) -> None:
        """
        Set the Unique identifier of Orbit Data Message linked to this Attitude Data Message.
        
        Parameters:
            odmMessageLink (String): Unique identifier of Orbit Data Message linked to this Attitude Data Message
        
        
        """
        ...
    def setOriginatorAddress(self, originatorAddress: str) -> None:
        """
        Set the address of Programmatic Point Of Contact at originator.
        
        Parameters:
            originatorAddress (String): address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorEmail(self, originatorEmail: str) -> None:
        """
        Set the email address of Programmatic Point Of Contact at originator.
        
        Parameters:
            originatorEmail (String): email address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPOC(self, originatorPOC: str) -> None:
        """
        Set the programmatic Point Of Contact at originator.
        
        Parameters:
            originatorPOC (String): programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPhone(self, originatorPhone: str) -> None:
        """
        Set the phone number of Programmatic Point Of Contact at originator.
        
        Parameters:
            originatorPhone (String): phone number of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPosition(self, originatorPosition: str) -> None:
        """
        Set the position of Programmatic Point Of Contact at originator.
        
        Parameters:
            originatorPosition (String): position of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setStartTime(self, startTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the time of the earliest data contained in the OCM.
        
        Parameters:
            startTime (AbsoluteDate): time of the earliest data contained in the OCM
        
        
        """
        ...
    def setStopTime(self, stopTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the time of the latest data contained in the OCM.
        
        Parameters:
            stopTime (AbsoluteDate): time of the latest data contained in the OCM
        
        
        """
        ...
    def setTaimutcT0(self, taimutcT0: float) -> None:
        """
        Set the difference (TAI – UTC) in seconds at epoch getEpochT0.
        
        Parameters:
            taimutcT0 (double): difference (TAI – UTC) in seconds at epoch getEpochT0
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class AdmMetadata
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AcmMetadataKey(java.lang.Enum['AcmMetadataKey']):
    """
    Keys for AcmMetadata entries.
    
    Since:
        12.0
    """
    INTERNATIONAL_DESIGNATOR: typing.ClassVar['AcmMetadataKey'] = ...
    CATALOG_NAME: typing.ClassVar['AcmMetadataKey'] = ...
    OBJECT_DESIGNATOR: typing.ClassVar['AcmMetadataKey'] = ...
    ORIGINATOR_POC: typing.ClassVar['AcmMetadataKey'] = ...
    ORIGINATOR_POSITION: typing.ClassVar['AcmMetadataKey'] = ...
    ORIGINATOR_PHONE: typing.ClassVar['AcmMetadataKey'] = ...
    ORIGINATOR_EMAIL: typing.ClassVar['AcmMetadataKey'] = ...
    ORIGINATOR_ADDRESS: typing.ClassVar['AcmMetadataKey'] = ...
    ODM_MSG_LINK: typing.ClassVar['AcmMetadataKey'] = ...
    EPOCH_TZERO: typing.ClassVar['AcmMetadataKey'] = ...
    ACM_DATA_ELEMENTS: typing.ClassVar['AcmMetadataKey'] = ...
    START_TIME: typing.ClassVar['AcmMetadataKey'] = ...
    STOP_TIME: typing.ClassVar['AcmMetadataKey'] = ...
    TAIMUTC_AT_TZERO: typing.ClassVar['AcmMetadataKey'] = ...
    NEXT_LEAP_EPOCH: typing.ClassVar['AcmMetadataKey'] = ...
    NEXT_LEAP_TAIMUTC: typing.ClassVar['AcmMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AcmMetadata) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AcmMetadata): container to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AcmMetadataKey':
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
    def values() -> typing.MutableSequence['AcmMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AcmMetadataKey c : AcmMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AcmParser(org.orekit.files.ccsds.ndm.adm.AdmParser[Acm, 'AcmParser'], org.orekit.files.general.AttitudeEphemerisFileParser[Acm]):
    """
    A parser for the CCSDS ACM (Attitude Comprehensive Message).
    
    Since:
        12.0
    """
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]):
        """
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildAcmParser.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
            dataContext (DataContext): used to retrieve frames, time scales, etc.
            parsedUnitsBehavior (ParsedUnitsBehavior): behavior to adopt for handling parsed units
            filters (Function<ParseToken, List<ParseToken>>[]): filters to apply to parse tokens
        
        Since:
            12.0
        
        
        """
        ...
    def build(self) -> Acm:
        """
        Build the file from parsed entries.
        
        Specified by: build in interface MessageParser
        
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
    def getHeader(self) -> org.orekit.files.ccsds.ndm.adm.AdmHeader:
        """
        Get file header to fill.
        
        Specified by: getHeader in class AbstractConstituentParser
        
        Returns:
            file header to fill
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]:
        """
        Get the non-default token builders for special XML elements.
        
        Specified by: getSpecialXmlElementsBuilders in interface MessageParser
        
        Overrides: getSpecialXmlElementsBuilders in class AdmParser
        
        Returns:
            map of token builders for special XML elements (keyed by XML element name)
        
        
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
    def parse(self, source: org.orekit.data.DataSource) -> Acm:
        """
        Parse an attitude ephemeris file from a data source.
        
        Specified by: parse in interface AttitudeEphemerisFileParser
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed attitude ephemeris file.
        
        
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
        
        Specified by: reset in interface MessageParser
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...

class AcmSatelliteEphemeris(org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, 'AttitudeStateHistory']):
    """
    ACM ephemeris blocks for a single satellite.
    
    Since:
        11.0
    """
    def __init__(self, name: str, blocks: java.util.List['AttitudeStateHistory']):
        """
        Create a container for the set of ephemeris blocks in the file that pertain to a single satellite.
        
        Parameters:
            name (String): name of the object.
            blocks (List<AttitudeStateHistory> blocks): containing ephemeris data for the satellite.
        
        
        """
        ...
    def getId(self) -> str:
        """
        Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
        Specified by: getId in interface SatelliteAttitudeEphemeris
        
        Returns:
            the satellite's ID, never null.
        
        
        """
        ...
    def getSegments(self) -> java.util.List['AttitudeStateHistory']:
        """
        Get the segments of the attitude ephemeris.
        
        Attitude ephemeris segments are typically used to split an ephemeris around discontinuous events.
        
        Specified by: getSegments in interface SatelliteAttitudeEphemeris
        
        Returns:
            the segments contained in the attitude ephemeris file for this satellite.
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of the ephemeris.
        
        Specified by: getStart in interface SatelliteAttitudeEphemeris
        
        Returns:
            ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of the ephemeris.
        
        Specified by: getStop in interface SatelliteAttitudeEphemeris
        
        Returns:
            ephemeris end date.
        
        
        """
        ...

class AcmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.adm.AdmHeader, org.orekit.files.ccsds.section.Segment[AcmMetadata, AcmData], Acm]):
    """
    Writer for CCSDS Attitude Comprehensive Message.
    
    Since:
        12.0
    """
    CCSDS_ACM_VERS: typing.ClassVar[float] = ...
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
    def __init__(self, conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext):
        """
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildAcmWriter.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            dataContext (DataContext): used to retrieve frames, time scales, etc.
        
        
        """
        ...

class AttitudeCovariance(org.orekit.time.TimeStamped):
    """
    Covariance entry.
    
    Since:
        12.0
    """
    def __init__(self, type: 'AttitudeCovarianceType', date: org.orekit.time.AbsoluteDate, fields: typing.Union[typing.List[str], jpype.JArray], first: int):
        """
        Simple constructor.
        
        Parameters:
            type (AttitudeCovarianceType): type of the elements
            date (AbsoluteDate): entry date
            fields (String[]): matrix diagonal elements
            first (int): index of first field to consider
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getMatrix(self) -> org.hipparchus.linear.DiagonalMatrix:
        """
        Get the covariance matrix.
        
        Returns:
            covariance matrix
        
        
        """
        ...
    def getType(self) -> 'AttitudeCovarianceType':
        """
        Get the type of the elements.
        
        Returns:
            type of the elements
        
        
        """
        ...

class AttitudeCovarianceHistory:
    """
    Covariance history.
    
    Since:
        12.0
    """
    def __init__(self, metadata: 'AttitudeCovarianceHistoryMetadata', covariances: java.util.List[AttitudeCovariance]):
        """
        Simple constructor.
        
        Parameters:
            metadata (AttitudeCovarianceHistoryMetadata): metadata
            covariances (List<AttitudeCovariance> covariances): covariances
        
        
        """
        ...
    def getCovariances(self) -> java.util.List[AttitudeCovariance]:
        """
        Get the covariances.
        
        Returns:
            covariances
        
        
        """
        ...
    def getMetadata(self) -> 'AttitudeCovarianceHistoryMetadata':
        """
        Get metadata.
        
        Returns:
            metadata
        
        
        """
        ...

class AttitudeCovarianceHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Metadata for covariance history.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def getCovBasis(self) -> str:
        """
        Get basis of this covariance time history data.
        
        Returns:
            basis of this covariance time history data
        
        
        """
        ...
    def getCovBasisID(self) -> str:
        """
        Get identification number of the orbit determination or simulation upon which this covariance is based.
        
        Returns:
            identification number of the orbit determination or simulation upon which this covariance is based
        
        
        """
        ...
    def getCovID(self) -> str:
        """
        Get covariance identification number.
        
        Returns:
            covariance identification number
        
        
        """
        ...
    def getCovPrevID(self) -> str:
        """
        Get identification number of previous covariance.
        
        Returns:
            identification number of previous covariance
        
        
        """
        ...
    def getCovReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get reference frame of the covariance.
        
        Returns:
            reference frame of the covariance
        
        
        """
        ...
    def getCovType(self) -> 'AttitudeCovarianceType':
        """
        Get covariance element set type.
        
        Returns:
            covariance element set type
        
        
        """
        ...
    def setCovBasis(self, covBasis: str) -> None:
        """
        Set basis of this covariance time history data.
        
        Parameters:
            covBasis (String): basis of this covariance time history data
        
        
        """
        ...
    def setCovBasisID(self, covBasisID: str) -> None:
        """
        Set identification number of the orbit determination or simulation upon which this covariance is based.
        
        Parameters:
            covBasisID (String): identification number of the orbit determination or simulation upon which this covariance is based
        
        
        """
        ...
    def setCovID(self, covID: str) -> None:
        """
        Set covariance identification number.
        
        Parameters:
            covID (String): covariance identification number
        
        
        """
        ...
    def setCovPrevID(self, covPrevID: str) -> None:
        """
        Set identification number of previous covariance.
        
        Parameters:
            covPrevID (String): identification number of previous covariance
        
        
        """
        ...
    def setCovReferenceFrame(self, covReferenceFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set reference frame of the covariance.
        
        Parameters:
            covReferenceFrame (FrameFacade): the reference frame to be set
        
        
        """
        ...
    def setCovType(self, covType: 'AttitudeCovarianceType') -> None:
        """
        Set covariance element set type.
        
        Parameters:
            covType (AttitudeCovarianceType): covariance element set type
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AttitudeCovarianceHistoryMetadataKey(java.lang.Enum['AttitudeCovarianceHistoryMetadataKey']):
    """
    Keys for AttitudeCovarianceHistoryMetadata entries.
    
    Since:
        12.0
    """
    COMMENT: typing.ClassVar['AttitudeCovarianceHistoryMetadataKey'] = ...
    COV_ID: typing.ClassVar['AttitudeCovarianceHistoryMetadataKey'] = ...
    COV_PREV_ID: typing.ClassVar['AttitudeCovarianceHistoryMetadataKey'] = ...
    COV_BASIS: typing.ClassVar['AttitudeCovarianceHistoryMetadataKey'] = ...
    COV_BASIS_ID: typing.ClassVar['AttitudeCovarianceHistoryMetadataKey'] = ...
    COV_REF_FRAME: typing.ClassVar['AttitudeCovarianceHistoryMetadataKey'] = ...
    COV_TYPE: typing.ClassVar['AttitudeCovarianceHistoryMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AttitudeCovarianceHistoryMetadata) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AttitudeCovarianceHistoryMetadata): container to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudeCovarianceHistoryMetadataKey':
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
    def values() -> typing.MutableSequence['AttitudeCovarianceHistoryMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeCovarianceHistoryMetadataKey c : AttitudeCovarianceHistoryMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeCovarianceType(java.lang.Enum['AttitudeCovarianceType']):
    """
    Attitude covariance set type used in CCSDS Acm.
    
    Since:
        12.0
    """
    ANGLE: typing.ClassVar['AttitudeCovarianceType'] = ...
    ANGLE_GYROBIAS: typing.ClassVar['AttitudeCovarianceType'] = ...
    ANGLE_ANGVEL: typing.ClassVar['AttitudeCovarianceType'] = ...
    QUATERNION: typing.ClassVar['AttitudeCovarianceType'] = ...
    QUATERNION_GYROBIAS: typing.ClassVar['AttitudeCovarianceType'] = ...
    QUATERNION_ANGVEL: typing.ClassVar['AttitudeCovarianceType'] = ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]:
        """
        Get the elements units.
        
        Returns:
            elements units (they correspond to diagonal elements, hence they are already squared)
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudeCovarianceType':
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
    def values() -> typing.MutableSequence['AttitudeCovarianceType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeCovarianceType c : AttitudeCovarianceType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeDetermination(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Attitude determination data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def addSensor(self, sensor: 'AttitudeDeterminationSensor') -> None:
        """
        Add a sensor used.
        
        Parameters:
            sensor (AttitudeDeterminationSensor): sensor to add
        
        
        """
        ...
    def getAttitudeStates(self) -> 'AttitudeElementsType':
        """
        Get attitude states.
        
        Returns:
            attitude states
        
        
        """
        ...
    def getCovarianceType(self) -> AttitudeCovarianceType:
        """
        Get type of attitude error state.
        
        Returns:
            type of attitude error state
        
        
        """
        ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints:
        """
        Get the endpoints (i.e. frames A, B and their relationship).
        
        Returns:
            endpoints
        
        
        """
        ...
    def getEulerRotSeq(self) -> org.hipparchus.geometry.euclidean.threed.RotationOrder:
        """
        Get the rotation order for Euler angles.
        
        Returns:
            rotation order for Euler angles
        
        
        """
        ...
    def getId(self) -> str:
        """
        Get identification number.
        
        Returns:
            identification number
        
        
        """
        ...
    def getMethod(self) -> org.orekit.files.ccsds.definitions.AdMethodType:
        """
        Get attitude determination method.
        
        Returns:
            attitude determination method
        
        
        """
        ...
    def getNbStates(self) -> int:
        """
        Get number of states for EKF, BATCH or FILTER_SMOOTHER.
        
        Returns:
            number of states
        
        
        """
        ...
    def getPrevId(self) -> str:
        """
        Get identification of previous orbit determination.
        
        Returns:
            identification of previous orbit determination
        
        
        """
        ...
    def getRateProcessNoiseStdDev(self) -> float:
        """
        Get process noise standard deviation if rateStates is ANGVEL.
        
        Returns:
            process noise standard deviation if rateStates is
            ANGVEL
        
        
        """
        ...
    def getRateStates(self) -> 'RateElementsType':
        """
        Get attitude rate states.
        
        Returns:
            attitude rate states
        
        
        """
        ...
    def getSensorsUsed(self) -> java.util.List['AttitudeDeterminationSensor']:
        """
        Get sensors used.
        
        Returns:
            sensors used
        
        
        """
        ...
    def getSigmaU(self) -> float:
        """
        Get rate random walk if rateStates is GYRO_BIAS.
        
        Returns:
            rate random walk if rateStates is GYRO_BIAS
        
        
        """
        ...
    def getSigmaV(self) -> float:
        """
        Get angle random walk if rateStates is GYRO_BIAS.
        
        Returns:
            angle random walk if rateStates is GYRO_BIAS
        
        
        """
        ...
    def getSource(self) -> str:
        """
        Get source of attitude estimate.
        
        Returns:
            source of attitude estimate
        
        
        """
        ...
    def setAttitudeStates(self, attitudeStates: 'AttitudeElementsType') -> None:
        """
        Set attitude states.
        
        Parameters:
            attitudeStates (AttitudeElementsType): attitude states
        
        
        """
        ...
    def setCovarianceType(self, covarianceType: AttitudeCovarianceType) -> None:
        """
        Set type of attitude error state.
        
        Parameters:
            covarianceType (AttitudeCovarianceType): type of attitude error state
        
        
        """
        ...
    def setEulerRotSeq(self, eulerRotSeq: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
        Set the rotation order for Euler angles.
        
        Parameters:
            eulerRotSeq (RotationOrder): rotation order for Euler angles
        
        
        """
        ...
    def setId(self, id: str) -> None:
        """
        Set identification number.
        
        Parameters:
            id (String): identification number
        
        
        """
        ...
    def setMethod(self, method: org.orekit.files.ccsds.definitions.AdMethodType) -> None:
        """
        Set attitude determination method.
        
        Parameters:
            method (AdMethodType): attitude determination method
        
        
        """
        ...
    def setNbStates(self, nbStates: int) -> None:
        """
        Set number of states for EKF, BATCH or FILTER_SMOOTHER.
        
        Parameters:
            nbStates (int): number of states
        
        
        """
        ...
    def setPrevId(self, prevId: str) -> None:
        """
        Set identification of previous orbit determination.
        
        Parameters:
            prevId (String): identification of previous orbit determination
        
        
        """
        ...
    def setRateProcessNoiseStdDev(self, rateProcessNoiseStdDev: float) -> None:
        """
        Set process noise standard deviation if rateStates is ANGVEL.
        
        Parameters:
            rateProcessNoiseStdDev (double): process noise standard deviation if rateStates is
                ANGVEL
        
        
        """
        ...
    def setRateStates(self, rateStates: 'RateElementsType') -> None:
        """
        Set attitude rate states.
        
        Parameters:
            rateStates (RateElementsType): attitude rate states
        
        
        """
        ...
    def setSigmaU(self, sigmaU: float) -> None:
        """
        Set rate random walk if rateStates is GYRO_BIAS.
        
        Parameters:
            sigmaU (double): rate random walk if rateStates is GYRO_BIAS
        
        
        """
        ...
    def setSigmaV(self, sigmaV: float) -> None:
        """
        Set angle random walk if rateStates is GYRO_BIAS.
        
        Parameters:
            sigmaV (double): angle random walk if rateStates is GYRO_BIAS
        
        
        """
        ...
    def setSource(self, source: str) -> None:
        """
        Set source of attitude estimate.
        
        Parameters:
            source (String): source of attitude estimate
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AttitudeDeterminationKey(java.lang.Enum['AttitudeDeterminationKey']):
    """
    Keys for AttitudeDetermination entries.
    
    Since:
        12.0
    """
    COMMENT: typing.ClassVar['AttitudeDeterminationKey'] = ...
    AD_ID: typing.ClassVar['AttitudeDeterminationKey'] = ...
    AD_PREV_ID: typing.ClassVar['AttitudeDeterminationKey'] = ...
    AD_METHOD: typing.ClassVar['AttitudeDeterminationKey'] = ...
    ATTITUDE_SOURCE: typing.ClassVar['AttitudeDeterminationKey'] = ...
    EULER_ROT_SEQ: typing.ClassVar['AttitudeDeterminationKey'] = ...
    NUMBER_STATES: typing.ClassVar['AttitudeDeterminationKey'] = ...
    ATTITUDE_STATES: typing.ClassVar['AttitudeDeterminationKey'] = ...
    COV_TYPE: typing.ClassVar['AttitudeDeterminationKey'] = ...
    REF_FRAME_A: typing.ClassVar['AttitudeDeterminationKey'] = ...
    REF_FRAME_B: typing.ClassVar['AttitudeDeterminationKey'] = ...
    RATE_STATES: typing.ClassVar['AttitudeDeterminationKey'] = ...
    SIGMA_U: typing.ClassVar['AttitudeDeterminationKey'] = ...
    SIGMA_V: typing.ClassVar['AttitudeDeterminationKey'] = ...
    RATE_PROCESS_NOISE_STDDEV: typing.ClassVar['AttitudeDeterminationKey'] = ...
    SENSOR: typing.ClassVar['AttitudeDeterminationKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, parser: AcmParser, context: org.orekit.files.ccsds.utils.ContextBinding, container: AttitudeDetermination) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            parser (AcmParser): ACM file parser
            context (ContextBinding): context binding
            container (AttitudeDetermination): container to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudeDeterminationKey':
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
    def values() -> typing.MutableSequence['AttitudeDeterminationKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeDeterminationKey c : AttitudeDeterminationKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeDeterminationSensor(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Attitude determination sensor data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getNbSensorNoiseCovariance(self) -> int:
        """
        Get number of noise elements for sensor.
        
        Returns:
            number of noise elements for sensor
        
        
        """
        ...
    def getSensorFrequency(self) -> float:
        """
        Get frequency of sensor data for sensor.
        
        Returns:
            frequency of sensor data for sensor
        
        
        """
        ...
    def getSensorNoiseCovariance(self) -> typing.MutableSequence[float]:
        """
        Get standard deviation of sensor noise for sensor.
        
        Returns:
            standard deviation of sensor noise for sensor
        
        
        """
        ...
    def getSensorNumber(self) -> int:
        """
        Get number of the sensor.
        
        Returns:
            number of the sensor
        
        
        """
        ...
    def getSensorUsed(self) -> str:
        """
        Get sensor used.
        
        Returns:
            sensor used
        
        
        """
        ...
    def setNbSensorNoiseCovariance(self, n: int) -> None:
        """
        Set number of noise elements for sensor.
        
        Parameters:
            n (int): number of noise elements for sensor
        
        
        """
        ...
    def setSensorFrequency(self, frequency: float) -> None:
        """
        Set frequency of sensor data for sensor.
        
        Parameters:
            frequency (double): frequency of sensor data for sensor
        
        
        """
        ...
    def setSensorNoiseCovariance(self, stddev: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set standard deviation of sensor noise for sensor.
        
        Parameters:
            stddev (double[]): standard deviation of sensor noise
        
        
        """
        ...
    def setSensorNumber(self, sensorNumber: int) -> None:
        """
        Set number of the sensor.
        
        Parameters:
            sensorNumber (int): number of the sensor
        
        
        """
        ...
    def setSensorUsed(self, sensorUsed: str) -> None:
        """
        Set sensor used.
        
        Parameters:
            sensorUsed (String): sensor used
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AttitudeDeterminationSensorKey(java.lang.Enum['AttitudeDeterminationSensorKey']):
    """
    Keys for AttitudeDetermination sensor entries.
    
    Since:
        12.0
    """
    SENSOR_NUMBER: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    SENSOR_USED: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    NUMBER_SENSOR_NOISE_COVARIANCE: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    SENSOR_NOISE_STDDEV: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    SENSOR_FREQUENCY: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AttitudeDeterminationSensor) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AttitudeDeterminationSensor): container to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudeDeterminationSensorKey':
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
    def values() -> typing.MutableSequence['AttitudeDeterminationSensorKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeDeterminationSensorKey c : AttitudeDeterminationSensorKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeElementsType(java.lang.Enum['AttitudeElementsType']):
    """
    Attitude element set type used in CCSDS Acm.
    
    Since:
        12.0
    """
    QUATERNION: typing.ClassVar['AttitudeElementsType'] = ...
    EULER_ANGLES: typing.ClassVar['AttitudeElementsType'] = ...
    DCM: typing.ClassVar['AttitudeElementsType'] = ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]:
        """
        Get the elements units.
        
        Returns:
            elements units
        
        
        """
        ...
    def toRotation(self, order: org.hipparchus.geometry.euclidean.threed.RotationOrder, elements: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Convert to rotation.
        
        Parameters:
            order (RotationOrder): rotation order for Euler angles
            elements (double[]): elements values in SI units
        
        Returns:
            rotation
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Enum in class Enum
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudeElementsType':
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
    def values() -> typing.MutableSequence['AttitudeElementsType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeElementsType c : AttitudeElementsType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeManeuver(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Maneuver entry.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Build an uninitialized maneuver.
        """
        ...
    def getActuatorUsed(self) -> str:
        """
        Get the actuator used.
        
        Returns:
            actuator used
        
        
        """
        ...
    def getBeginTime(self) -> float:
        """
        Get start time of actual maneuver, relative to t₀.
        
        Returns:
            start time of actual maneuver, relative to t₀
        
        
        """
        ...
    def getDuration(self) -> float:
        """
        Get duration.
        
        Returns:
            duration
        
        
        """
        ...
    def getEndTime(self) -> float:
        """
        Get end time of actual maneuver, relative to t₀.
        
        Returns:
            end time of actual maneuver, relative to t₀
        
        
        """
        ...
    def getID(self) -> str:
        """
        Get maneuver identification number.
        
        Returns:
            maneuver identification number
        
        
        """
        ...
    def getManPurpose(self) -> str:
        """
        Get purpose of maneuver.
        
        Returns:
            purpose of maneuver
        
        
        """
        ...
    def getPrevID(self) -> str:
        """
        Get identification number of previous maneuver.
        
        Returns:
            identification number of previous maneuver
        
        
        """
        ...
    def getTargetAttitude(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get target attitude (if purpose is attitude adjustment).
        
        Returns:
            target attitude
        
        
        """
        ...
    def getTargetMomFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get reference frame for getTargetMomentum.
        
        Returns:
            reference frame for getTargetMomentum
        
        
        """
        ...
    def getTargetMomentum(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get target momentum (if purpose is momentum desaturation).
        
        Returns:
            target momentum
        
        
        """
        ...
    def getTargetSpinRate(self) -> float:
        """
        Get target spin rate (if purpose is spin rate adjustment).
        
        Returns:
            target spin rate
        
        
        """
        ...
    def setActuatorUsed(self, actuatorUsed: str) -> None:
        """
        Set actuator used.
        
        Parameters:
            actuatorUsed (String): actuator used
        
        
        """
        ...
    def setBeginTime(self, beginTime: float) -> None:
        """
        Set start time of actual maneuver, relative to t₀.
        
        Parameters:
            beginTime (double): start time of actual maneuver, relative to t₀
        
        
        """
        ...
    def setDuration(self, duration: float) -> None:
        """
        Set duration.
        
        Parameters:
            duration (double): duration
        
        
        """
        ...
    def setEndTime(self, endTime: float) -> None:
        """
        Set end time of actual maneuver, relative to t₀.
        
        Parameters:
            endTime (double): end time of actual maneuver, relative to t₀
        
        
        """
        ...
    def setID(self, manId: str) -> None:
        """
        Set maneuver identification number.
        
        Parameters:
            manId (String): maneuver identification number
        
        
        """
        ...
    def setManPurpose(self, manPurpose: str) -> None:
        """
        Set purpose of maneuver.
        
        Parameters:
            manPurpose (String): purpose of maneuver
        
        
        """
        ...
    def setPrevID(self, prevID: str) -> None:
        """
        Set identification number of previous maneuver.
        
        Parameters:
            prevID (String): identification number of previous maneuver
        
        
        """
        ...
    def setTargetAttitude(self, targetAttitude: org.hipparchus.geometry.euclidean.threed.Rotation) -> None:
        """
        Set target attitude (if purpose is attitude adjustment).
        
        Parameters:
            targetAttitude (Rotation): target attitude
        
        
        """
        ...
    def setTargetMomFrame(self, targetMomFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set reference frame for getTargetMomentum.
        
        Parameters:
            targetMomFrame (FrameFacade): reference frame for getTargetMomentum
        
        
        """
        ...
    def setTargetMomentum(self, targetMomentum: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set target momentum (if purpose is momentum desaturation).
        
        Parameters:
            targetMomentum (Vector3D): target momentum
        
        
        """
        ...
    def setTargetSpinRate(self, targetSpinRate: float) -> None:
        """
        Set target spin rate (if purpose is spin rate adjustment).
        
        Parameters:
            targetSpinRate (double): target spin rate
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AttitudeManeuverKey(java.lang.Enum['AttitudeManeuverKey']):
    """
    Keys for AttitudeManeuver entries.
    
    Since:
        12.0
    """
    COMMENT: typing.ClassVar['AttitudeManeuverKey'] = ...
    MAN_ID: typing.ClassVar['AttitudeManeuverKey'] = ...
    MAN_PREV_ID: typing.ClassVar['AttitudeManeuverKey'] = ...
    MAN_PURPOSE: typing.ClassVar['AttitudeManeuverKey'] = ...
    MAN_BEGIN_TIME: typing.ClassVar['AttitudeManeuverKey'] = ...
    MAN_END_TIME: typing.ClassVar['AttitudeManeuverKey'] = ...
    MAN_DURATION: typing.ClassVar['AttitudeManeuverKey'] = ...
    ACTUATOR_USED: typing.ClassVar['AttitudeManeuverKey'] = ...
    TARGET_MOMENTUM: typing.ClassVar['AttitudeManeuverKey'] = ...
    TARGET_MOM_FRAME: typing.ClassVar['AttitudeManeuverKey'] = ...
    TARGET_ATTITUDE: typing.ClassVar['AttitudeManeuverKey'] = ...
    TARGET_SPINRATE: typing.ClassVar['AttitudeManeuverKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, data: AttitudeManeuver) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            data (AttitudeManeuver): data to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudeManeuverKey':
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
    def values() -> typing.MutableSequence['AttitudeManeuverKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeManeuverKey c : AttitudeManeuverKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudePhysicalProperties(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Spacecraft physical properties.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getCenterOfPressure(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the location of center of pressure.
        
        Returns:
            location of center of pressure
        
        
        """
        ...
    def getCenterOfPressureReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get reference frame for center of pressure.
        
        Returns:
            reference frame for center of pressure
        
        
        """
        ...
    def getDragCoefficient(self) -> float:
        """
        Get the drag coefficient.
        
        Returns:
            the drag coefficient
        
        
        """
        ...
    def getDryMass(self) -> float:
        """
        Get the mass without propellant.
        
        Returns:
            mass without propellant
        
        
        """
        ...
    def getInertiaMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the inertia matrix.
        
        Returns:
            the inertia matrix
        
        
        """
        ...
    def getInertiaReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get reference frame for inertia.
        
        Returns:
            reference frame for inertia
        
        
        """
        ...
    def getWetMass(self) -> float:
        """
        Get the total mass at T₀.
        
        Returns:
            total mass at T₀
        
        
        """
        ...
    def setCenterOfPressure(self, centerOfPressure: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Set the location of center of pressure.
        
        Parameters:
            centerOfPressure (Vector3D): location of center of pressure
        
        
        """
        ...
    def setCenterOfPressureReferenceFrame(self, centerOfPressureReferenceFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set reference frame for center of pressure.
        
        Parameters:
            centerOfPressureReferenceFrame (FrameFacade): reference frame for center of pressure
        
        
        """
        ...
    def setDragCoefficient(self, dragCoefficient: float) -> None:
        """
        Set the the drag coefficient.
        
        Parameters:
            dragCoefficient (double): the drag coefficient
        
        
        """
        ...
    def setDryMass(self, dryMass: float) -> None:
        """
        Set the mass without propellant.
        
        Parameters:
            dryMass (double): mass without propellant
        
        
        """
        ...
    def setInertiaMatrixEntry(self, j: int, k: int, entry: float) -> None:
        """
        Set an entry in the inertia matrix.
        
        Both I(j, k) and I(k, j) are set.
        
        Parameters:
            j (int): row index (must be between 0 and 3 (inclusive)
            k (int): column index (must be between 0 and 3 (inclusive)
            entry (double): value of the matrix entry
        
        
        """
        ...
    def setInertiaReferenceFrame(self, inertiaReferenceFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set reference frame for inertia.
        
        Parameters:
            inertiaReferenceFrame (FrameFacade): reference frame for inertia
        
        
        """
        ...
    def setWetMass(self, wetMass: float) -> None:
        """
        Set the total mass at T₀.
        
        Parameters:
            wetMass (double): total mass at T₀
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AttitudePhysicalPropertiesKey(java.lang.Enum['AttitudePhysicalPropertiesKey']):
    """
    Keys for AttitudePhysicalProperties entries.
    
    Since:
        12.0
    """
    COMMENT: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    DRAG_COEFF: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    WET_MASS: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    DRY_MASS: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    CP_REF_FRAME: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    CP: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    INERTIA_REF_FRAME: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    IXX: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    IYY: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    IZZ: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    IXY: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    IXZ: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    IYZ: typing.ClassVar['AttitudePhysicalPropertiesKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, data: AttitudePhysicalProperties) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            data (AttitudePhysicalProperties): data to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudePhysicalPropertiesKey':
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
    def values() -> typing.MutableSequence['AttitudePhysicalPropertiesKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudePhysicalPropertiesKey c : AttitudePhysicalPropertiesKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeState(org.orekit.time.TimeStamped):
    """
    Attitude state entry.
    
    Since:
        12.0
    """
    def __init__(self, attitudeType: AttitudeElementsType, rateType: 'RateElementsType', date: org.orekit.time.AbsoluteDate, fields: typing.Union[typing.List[str], jpype.JArray], first: int):
        """
        Simple constructor.
        
        Parameters:
            attitudeType (AttitudeElementsType): type of the elements
            rateType (RateElementsType): type of the elements rates (internally changed to NONE if
                null)
            date (AbsoluteDate): entry date
            fields (String[]): trajectory elements
            first (int): index of first field to consider
        
        
        """
        ...
    def getAttitudeType(self) -> AttitudeElementsType:
        """
        Get the type of the elements.
        
        Returns:
            type of the elements
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
        Get which derivatives of position are available in this state.
        
        Returns:
            a value indicating if the file contains rotation rate and/or acceleration
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getElements(self) -> typing.MutableSequence[float]:
        """
        Get attitude elements.
        
        Returns:
            attitude elements
        
        
        """
        ...
    def getRateElementsType(self) -> 'RateElementsType':
        """
        Get the type of the elements rates.
        
        Returns:
            type of the elements rates
        
        
        """
        ...
    def toAngular(self, order: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
        Convert to angular coordinates.
        
        Parameters:
            order (RotationOrder): rotation order for Euler angles
        
        Returns:
            angular coordinates
        
        
        """
        ...

class AttitudeStateHistory(org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment[org.orekit.utils.TimeStampedAngularCoordinates]):
    """
    Attitude state history.
    
    Since:
        12.0
    """
    def __init__(self, metadata: 'AttitudeStateHistoryMetadata', states: java.util.List[AttitudeState]):
        """
        Simple constructor.
        
        Parameters:
            metadata (AttitudeStateHistoryMetadata): metadata
            states (List<AttitudeState> states): attitude states
        
        
        """
        ...
    def getAngularCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]:
        """
        Get an unmodifiable list of attitude data lines.
        
        Specified by: getAngularCoordinates in interface AttitudeEphemerisSegment
        
        Returns:
            a list of attitude data
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider:
        """
        Get the attitude provider for this attitude ephemeris segment.
        
        Specified by: getAttitudeProvider in interface AttitudeEphemerisSegment
        
        Returns:
            the attitude provider for this attitude ephemeris segment.
        
        
        """
        ...
    def getAttitudeStates(self) -> java.util.List[AttitudeState]:
        """
        Get the attitude states.
        
        Returns:
            attitude states
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
        Get which derivatives of angular data are available in this attitude ephemeris segment.
        
        Specified by: getAvailableDerivatives in interface AttitudeEphemerisSegment
        
        Returns:
            a value indicating if the file contains rotation and/or rotation rate and/or acceleration data.
        
        
        """
        ...
    def getInterpolationMethod(self) -> str:
        """
        Get the interpolation method to be used.
        
        Specified by: getInterpolationMethod in interface AttitudeEphemerisSegment
        
        Returns:
            the interpolation method
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
        Get the number of samples to use in interpolation.
        
        Specified by: getInterpolationSamples in interface AttitudeEphemerisSegment
        
        Returns:
            the number of points to use for interpolation.
        
        
        """
        ...
    def getMetadata(self) -> 'AttitudeStateHistoryMetadata':
        """
        Get metadata.
        
        Returns:
            metadata
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame from which attitude is defined.
        
        Specified by: getReferenceFrame in interface AttitudeEphemerisSegment
        
        Returns:
            the reference frame from which attitude is defined
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of this ephemeris segment.
        
        Specified by: getStart in interface AttitudeEphemerisSegment
        
        Returns:
            ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of this ephemeris segment.
        
        Specified by: getStop in interface AttitudeEphemerisSegment
        
        Returns:
            ephemeris segment end date.
        
        
        """
        ...

class AttitudeStateHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Metadata for attitude state history.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getAttBasis(self) -> str:
        """
        Get basis of this attitude state time history data.
        
        Returns:
            basis of this attitude state time history data
        
        
        """
        ...
    def getAttBasisID(self) -> str:
        """
        Get identification number of the orbit determination or simulation upon which this attitude is based.
        
        Returns:
            identification number of the orbit determination or simulation upon which this attitude is based
        
        
        """
        ...
    def getAttID(self) -> str:
        """
        Get attitude identification number.
        
        Returns:
            attitude identification number
        
        
        """
        ...
    def getAttPrevID(self) -> str:
        """
        Get identification number of previous attitude.
        
        Returns:
            identification number of previous attitude
        
        
        """
        ...
    def getAttitudeType(self) -> AttitudeElementsType:
        """
        Get attitude element set type.
        
        Returns:
            attitude element set type
        
        
        """
        ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints:
        """
        Get the endpoints (i.e. frames A, B and their relationship).
        
        Returns:
            endpoints
        
        
        """
        ...
    def getEulerRotSeq(self) -> org.hipparchus.geometry.euclidean.threed.RotationOrder:
        """
        Get the rotation order for Euler angles.
        
        Returns:
            rotation order for Euler angles
        
        
        """
        ...
    def getNbStates(self) -> int:
        """
        Get the number of data states included (attitude components plus rates components).
        
        Returns:
            number of data states included (attitude components plus rates components)
        
        
        """
        ...
    def getRateType(self) -> 'RateElementsType':
        """
        Get attitude rate element set type.
        
        Returns:
            attitude rate element set type
        
        
        """
        ...
    def setAttBasis(self, attBasis: str) -> None:
        """
        Set basis of this attitude state time history data.
        
        Parameters:
            attBasis (String): basis of this attitude state time history data
        
        
        """
        ...
    def setAttBasisID(self, attBasisID: str) -> None:
        """
        Set identification number of the orbit determination or simulation upon which this attitude is based.
        
        Parameters:
            attBasisID (String): identification number of the orbit determination or simulation upon which this attitude is based
        
        
        """
        ...
    def setAttID(self, attID: str) -> None:
        """
        Set attitude identification number.
        
        Parameters:
            attID (String): attitude identification number
        
        
        """
        ...
    def setAttPrevID(self, attPrevID: str) -> None:
        """
        Set identification number of previous attitude.
        
        Parameters:
            attPrevID (String): identification number of previous attitude
        
        
        """
        ...
    def setAttitudeType(self, attitudeType: AttitudeElementsType) -> None:
        """
        Set attitude element set type.
        
        Parameters:
            attitudeType (AttitudeElementsType): attitude element set type
        
        
        """
        ...
    def setEulerRotSeq(self, eulerRotSeq: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
        Set the rotation order for Euler angles.
        
        Parameters:
            eulerRotSeq (RotationOrder): rotation order for Euler angles
        
        
        """
        ...
    def setNbStates(self, nbStates: int) -> None:
        """
        Set the number of data states included (attitude components plus rates components).
        
        Parameters:
            nbStates (int): number of data states included (attitude components plus rates components)
        
        
        """
        ...
    def setRateType(self, rateType: 'RateElementsType') -> None:
        """
        Set attitude rate element set type.
        
        Parameters:
            rateType (RateElementsType): attitude rate element set type
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AttitudeStateHistoryMetadataKey(java.lang.Enum['AttitudeStateHistoryMetadataKey']):
    """
    Keys for AttitudeStateHistoryMetadata entries.
    
    Since:
        12.0
    """
    COMMENT: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    ATT_ID: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    ATT_PREV_ID: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    ATT_BASIS: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    ATT_BASIS_ID: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    REF_FRAME_A: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    REF_FRAME_B: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    EULER_ROT_SEQ: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    NUMBER_STATES: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    ATT_TYPE: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    RATE_TYPE: typing.ClassVar['AttitudeStateHistoryMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AttitudeStateHistoryMetadata) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AttitudeStateHistoryMetadata): container to fill
        
        Returns:
            true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AttitudeStateHistoryMetadataKey':
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
    def values() -> typing.MutableSequence['AttitudeStateHistoryMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeStateHistoryMetadataKey c : AttitudeStateHistoryMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RateElementsType(java.lang.Enum['RateElementsType']):
    """
    Attitude rate element set type used in CCSDS Acm.
    
    Since:
        12.0
    """
    ANGVEL: typing.ClassVar['RateElementsType'] = ...
    Q_DOT: typing.ClassVar['RateElementsType'] = ...
    EULER_RATE: typing.ClassVar['RateElementsType'] = ...
    GYRO_BIAS: typing.ClassVar['RateElementsType'] = ...
    NONE: typing.ClassVar['RateElementsType'] = ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]:
        """
        Get the elements units.
        
        Returns:
            elements units
        
        
        """
        ...
    def toAngular(self, date: org.orekit.time.AbsoluteDate, order: org.hipparchus.geometry.euclidean.threed.RotationOrder, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, first: int, elements: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
        Convert to angyla coordinates.
        
        Parameters:
            date (AbsoluteDate): date
            order (RotationOrder): rotation order for Euler angles
            rotation (Rotation): rotation
            first (int): index of the first element to consider
            elements (double[]): elements values in SI units
        
        Returns:
            rotation
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Enum in class Enum
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'RateElementsType':
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
    def values() -> typing.MutableSequence['RateElementsType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RateElementsType c : RateElementsType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.adm.acm")``.

    Acm: typing.Type[Acm]
    AcmData: typing.Type[AcmData]
    AcmDataSubStructureKey: typing.Type[AcmDataSubStructureKey]
    AcmElements: typing.Type[AcmElements]
    AcmMetadata: typing.Type[AcmMetadata]
    AcmMetadataKey: typing.Type[AcmMetadataKey]
    AcmParser: typing.Type[AcmParser]
    AcmSatelliteEphemeris: typing.Type[AcmSatelliteEphemeris]
    AcmWriter: typing.Type[AcmWriter]
    AttitudeCovariance: typing.Type[AttitudeCovariance]
    AttitudeCovarianceHistory: typing.Type[AttitudeCovarianceHistory]
    AttitudeCovarianceHistoryMetadata: typing.Type[AttitudeCovarianceHistoryMetadata]
    AttitudeCovarianceHistoryMetadataKey: typing.Type[AttitudeCovarianceHistoryMetadataKey]
    AttitudeCovarianceType: typing.Type[AttitudeCovarianceType]
    AttitudeDetermination: typing.Type[AttitudeDetermination]
    AttitudeDeterminationKey: typing.Type[AttitudeDeterminationKey]
    AttitudeDeterminationSensor: typing.Type[AttitudeDeterminationSensor]
    AttitudeDeterminationSensorKey: typing.Type[AttitudeDeterminationSensorKey]
    AttitudeElementsType: typing.Type[AttitudeElementsType]
    AttitudeManeuver: typing.Type[AttitudeManeuver]
    AttitudeManeuverKey: typing.Type[AttitudeManeuverKey]
    AttitudePhysicalProperties: typing.Type[AttitudePhysicalProperties]
    AttitudePhysicalPropertiesKey: typing.Type[AttitudePhysicalPropertiesKey]
    AttitudeState: typing.Type[AttitudeState]
    AttitudeStateHistory: typing.Type[AttitudeStateHistory]
    AttitudeStateHistoryMetadata: typing.Type[AttitudeStateHistoryMetadata]
    AttitudeStateHistoryMetadataKey: typing.Type[AttitudeStateHistoryMetadataKey]
    RateElementsType: typing.Type[RateElementsType]
