
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
    public class Acm extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata`, :class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmData`>> implements :class:`~org.orekit.files.general.AttitudeEphemerisFile`<:class:`~org.orekit.utils.TimeStampedAngularCoordinates`, :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeStateHistory`>
    
        This class gathers the informations present in the Attitude Comprehensive Message (ACM).
    
        Since:
            12.0
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ROOT
    
        Root element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` FORMAT_VERSION_KEY
    
        Key for format version.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ATT_LINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ATT_LINE
    
        Attitude line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    COV_LINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` COV_LINE
    
        Covariance line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNKNOWN_OBJECT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` UNKNOWN_OBJECT
    
        Default name for unknown object.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, admHeader: org.orekit.files.ccsds.ndm.adm.AdmHeader, list: java.util.List[org.orekit.files.ccsds.section.Segment['AcmMetadata', 'AcmData']], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...
    def getData(self) -> 'AcmData':
        """
            Get the data from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`.
        
            Returns:
                data from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`
        
        
        """
        ...
    def getMetadata(self) -> 'AcmMetadata':
        """
            Get the metadata from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`.
        
            Returns:
                metadata from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'AcmSatelliteEphemeris']: ...

class AcmData(org.orekit.files.ccsds.section.Data):
    """
    public class AcmData extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Data container for Attitude Comprehensive Messages.
    
        Since:
            12.0
    """
    def __init__(self, list: java.util.List['AttitudeStateHistory'], attitudePhysicalProperties: 'AttitudePhysicalProperties', list2: java.util.List['AttitudeCovarianceHistory'], list3: java.util.List['AttitudeManeuver'], attitudeDetermination: 'AttitudeDetermination', userDefined: org.orekit.files.ccsds.ndm.odm.UserDefined): ...
    def getAttitudeBlocks(self) -> java.util.List['AttitudeStateHistory']: ...
    def getAttitudeDeterminationBlock(self) -> 'AttitudeDetermination':
        """
            Get attitude determination logical block.
        
            Returns:
                attitude determination logical block (may be null)
        
        
        """
        ...
    def getCovarianceBlocks(self) -> java.util.List['AttitudeCovarianceHistory']: ...
    def getManeuverBlocks(self) -> java.util.List['AttitudeManeuver']: ...
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
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AcmDataSubStructureKey(java.lang.Enum['AcmDataSubStructureKey']):
    """
    public enum AcmDataSubStructureKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmDataSubStructureKey`>
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, acmParser: 'AcmParser') -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                parser (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmParser`): ACM file parser
        
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
    def valueOf(string: str) -> 'AcmDataSubStructureKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AcmDataSubStructureKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AcmDataSubStructureKey c : AcmDataSubStructureKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AcmElements(java.lang.Enum['AcmElements']):
    """
    public enum AcmElements extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmElements`>
    
        Data elements types used in CCSDS :class:`~org.orekit.files.ccsds.ndm.adm.acm.Acm`.
    
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
    def valueOf(string: str) -> 'AcmElements':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AcmElements']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AcmElements c : AcmElements.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AcmMetadata(org.orekit.files.ccsds.ndm.adm.AdmMetadata):
    """
    public class AcmMetadata extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`
    
        Meta-data for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata`.
    
        Since:
            12.0
    """
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def getAcmDataElements(self) -> java.util.List[AcmElements]: ...
    def getCatalogName(self) -> str:
        """
            Get the specification of satellite catalog source.
        
            Returns:
                specification of satellite catalog source
        
        
        """
        ...
    def getEpochT0(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the epoch to which *all* relative times are referenced in data blocks.
        
            Returns:
                epoch to which *all* relative times are referenced in data blocks
        
        
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
            Get the difference (TAI – UTC) in seconds incorporated at epoch
            :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getNextLeapEpoch`.
        
            Returns:
                difference (TAI – UTC) in seconds incorporated at epoch
                :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getNextLeapEpoch`
        
        
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
            Get the difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getEpochT0`.
        
            Returns:
                difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getEpochT0`
        
        
        """
        ...
    def setAcmDataElements(self, list: java.util.List[AcmElements]) -> None: ...
    def setCatalogName(self, string: str) -> None:
        """
            Set the specification of satellite catalog source.
        
            Parameters:
                catalogName (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): specification of satellite catalog source
        
        
        """
        ...
    def setEpochT0(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the epoch to which *all* relative times are referenced in data blocks.
        
            Parameters:
                epochT0 (:class:`~org.orekit.time.AbsoluteDate`): epoch to which *all* relative times are referenced in data blocks
        
        
        """
        ...
    def setInternationalDesignator(self, string: str) -> None:
        """
            Set the international designator for the object.
        
            Parameters:
                internationalDesignator (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): international designator for the object
        
        
        """
        ...
    def setNextLeapEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the epoch of next leap second.
        
            Parameters:
                nextLeapEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of next leap second
        
        
        """
        ...
    def setNextLeapTaimutc(self, double: float) -> None:
        """
            Set the difference (TAI – UTC) in seconds incorporated at epoch
            :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getNextLeapEpoch`.
        
            Parameters:
                nextLeapTaimutc (double): difference (TAI – UTC) in seconds incorporated at epoch
                    :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getNextLeapEpoch`
        
        
        """
        ...
    def setObjectDesignator(self, string: str) -> None:
        """
            Set the unique satellite identification designator for the object.
        
            Parameters:
                objectDesignator (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): unique satellite identification designator for the object
        
        
        """
        ...
    def setOdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Orbit Data Message linked to this Attitude Data Message.
        
            Parameters:
                odmMessageLink (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Unique identifier of Orbit Data Message linked to this Attitude Data Message
        
        
        """
        ...
    def setOriginatorAddress(self, string: str) -> None:
        """
            Set the address of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorAddress (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorEmail(self, string: str) -> None:
        """
            Set the email address of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorEmail (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): email address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPOC(self, string: str) -> None:
        """
            Set the programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPOC (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPhone(self, string: str) -> None:
        """
            Set the phone number of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPhone (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): phone number of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPosition(self, string: str) -> None:
        """
            Set the position of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPosition (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): position of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time of the earliest data contained in the OCM.
        
            Parameters:
                startTime (:class:`~org.orekit.time.AbsoluteDate`): time of the earliest data contained in the OCM
        
        
        """
        ...
    def setStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time of the latest data contained in the OCM.
        
            Parameters:
                stopTime (:class:`~org.orekit.time.AbsoluteDate`): time of the latest data contained in the OCM
        
        
        """
        ...
    def setTaimutcT0(self, double: float) -> None:
        """
            Set the difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getEpochT0`.
        
            Parameters:
                taimutcT0 (double): difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata.getEpochT0`
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata.validate` in
                class :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AcmMetadataKey(java.lang.Enum['AcmMetadataKey']):
    """
    public enum AcmMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, acmMetadata: AcmMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'AcmMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AcmMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AcmMetadataKey c : AcmMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AcmParser(org.orekit.files.ccsds.ndm.adm.AdmParser[Acm, 'AcmParser'], org.orekit.files.general.AttitudeEphemerisFileParser[Acm]):
    """
    public class AcmParser extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmParser`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.Acm`, :class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmParser`> implements :class:`~org.orekit.files.general.AttitudeEphemerisFileParser`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.Acm`>
    
        A parser for the CCSDS ACM (Attitude Comprehensive Message).
    
        Since:
            12.0
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, functionArray: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
    def build(self) -> Acm:
        """
            Build the file from parsed entries.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.build` in
                interface :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Returns:
                parsed file
        
        
        """
        ...
    def finalizeData(self) -> bool:
        """
            Finalize data after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeData` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
            Finalize header after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
            Finalize metadata after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeMetadata` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def getHeader(self) -> org.orekit.files.ccsds.ndm.adm.AdmHeader:
        """
            Get file header to fill.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.getHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                file header to fill
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]: ...
    def inData(self) -> bool:
        """
            Acknowledge data parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inData` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
            Acknowledge header parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
            Acknowledge metada parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inMetadata` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> Acm:
        """
            Parse an attitude ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFileParser.parse` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed attitude ephemeris file.
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
            Prepare data for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareData` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
            Prepare header for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
            Prepare metadata for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareMetadata` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.reset` in
                interface :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class AcmSatelliteEphemeris(org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, 'AttitudeStateHistory']):
    """
    public class AcmSatelliteEphemeris extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`<:class:`~org.orekit.utils.TimeStampedAngularCoordinates`, :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeStateHistory`>
    
        ACM ephemeris blocks for a single satellite.
    
        Since:
            11.0
    """
    def __init__(self, string: str, list: java.util.List['AttitudeStateHistory']): ...
    def getId(self) -> str:
        """
            Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris.getId` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`
        
            Returns:
                the satellite's ID, never :code:`null`.
        
        
        """
        ...
    def getSegments(self) -> java.util.List['AttitudeStateHistory']: ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of the ephemeris.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris.getStart` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`
        
            Returns:
                ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of the ephemeris.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris.getStop` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`
        
            Returns:
                ephemeris end date.
        
        
        """
        ...

class AcmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.adm.AdmHeader, org.orekit.files.ccsds.section.Segment[AcmMetadata, AcmData], Acm]):
    """
    public class AcmWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmMetadata`, :class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmData`>, :class:`~org.orekit.files.ccsds.ndm.adm.acm.Acm`>
    
        Writer for CCSDS Attitude Comprehensive Message.
    
        Since:
            12.0
    """
    CCSDS_ACM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_ACM_VERS
    
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
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...

class AttitudeCovariance(org.orekit.time.TimeStamped):
    """
    public class AttitudeCovariance extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Covariance entry.
    
        Since:
            12.0
    """
    def __init__(self, attitudeCovarianceType: 'AttitudeCovarianceType', absoluteDate: org.orekit.time.AbsoluteDate, stringArray: typing.Union[typing.List[str], jpype.JArray], int: int): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
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
    public class AttitudeCovarianceHistory extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Covariance history.
    
        Since:
            12.0
    """
    def __init__(self, attitudeCovarianceHistoryMetadata: 'AttitudeCovarianceHistoryMetadata', list: java.util.List[AttitudeCovariance]): ...
    def getCovariances(self) -> java.util.List[AttitudeCovariance]: ...
    def getMetadata(self) -> 'AttitudeCovarianceHistoryMetadata':
        """
            Get metadata.
        
            Returns:
                metadata
        
        
        """
        ...

class AttitudeCovarianceHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class AttitudeCovarianceHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for covariance history.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            12.0
    """
    def __init__(self): ...
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
    def setCovBasis(self, string: str) -> None:
        """
            Set basis of this covariance time history data.
        
            Parameters:
                covBasis (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): basis of this covariance time history data
        
        
        """
        ...
    def setCovBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this covariance is based.
        
            Parameters:
                covBasisID (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of the orbit determination or simulation upon which this covariance is based
        
        
        """
        ...
    def setCovID(self, string: str) -> None:
        """
            Set covariance identification number.
        
            Parameters:
                covID (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): covariance identification number
        
        
        """
        ...
    def setCovPrevID(self, string: str) -> None:
        """
            Set identification number of previous covariance.
        
            Parameters:
                covPrevID (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of previous covariance
        
        
        """
        ...
    def setCovReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame of the covariance.
        
            Parameters:
                covReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setCovType(self, attitudeCovarianceType: 'AttitudeCovarianceType') -> None:
        """
            Set covariance element set type.
        
            Parameters:
                covType (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeCovarianceType`): covariance element set type
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AttitudeCovarianceHistoryMetadataKey(java.lang.Enum['AttitudeCovarianceHistoryMetadataKey']):
    """
    public enum AttitudeCovarianceHistoryMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeCovarianceHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeCovarianceHistoryMetadata` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, attitudeCovarianceHistoryMetadata: AttitudeCovarianceHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeCovarianceHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'AttitudeCovarianceHistoryMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeCovarianceHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeCovarianceHistoryMetadataKey c : AttitudeCovarianceHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeCovarianceType(java.lang.Enum['AttitudeCovarianceType']):
    """
    public enum AttitudeCovarianceType extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeCovarianceType`>
    
        Attitude covariance set type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.adm.acm.Acm`.
    
        Since:
            12.0
    """
    ANGLE: typing.ClassVar['AttitudeCovarianceType'] = ...
    ANGLE_GYROBIAS: typing.ClassVar['AttitudeCovarianceType'] = ...
    ANGLE_ANGVEL: typing.ClassVar['AttitudeCovarianceType'] = ...
    QUATERNION: typing.ClassVar['AttitudeCovarianceType'] = ...
    QUATERNION_GYROBIAS: typing.ClassVar['AttitudeCovarianceType'] = ...
    QUATERNION_ANGVEL: typing.ClassVar['AttitudeCovarianceType'] = ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AttitudeCovarianceType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeCovarianceType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeCovarianceType c : AttitudeCovarianceType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeDetermination(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class AttitudeDetermination extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Attitude determination data.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            12.0
    """
    def __init__(self): ...
    def addSensor(self, attitudeDeterminationSensor: 'AttitudeDeterminationSensor') -> None:
        """
            Add a sensor used.
        
            Parameters:
                sensor (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeDeterminationSensor`): sensor to add
        
        
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
            Get number of states for :meth:`~org.orekit.files.ccsds.definitions.AdMethodType.EKF`,
            :meth:`~org.orekit.files.ccsds.definitions.AdMethodType.BATCH` or
            :meth:`~org.orekit.files.ccsds.definitions.AdMethodType.FILTER_SMOOTHER`.
        
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
            Get process noise standard deviation if :code:`rateStates` is
            :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.ANGVEL`.
        
            Returns:
                process noise standard deviation if :code:`rateStates` is
                :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.ANGVEL`
        
        
        """
        ...
    def getRateStates(self) -> 'RateElementsType':
        """
            Get attitude rate states.
        
            Returns:
                attitude rate states
        
        
        """
        ...
    def getSensorsUsed(self) -> java.util.List['AttitudeDeterminationSensor']: ...
    def getSigmaU(self) -> float:
        """
            Get rate random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`.
        
            Returns:
                rate random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`
        
        
        """
        ...
    def getSigmaV(self) -> float:
        """
            Get angle random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`.
        
            Returns:
                angle random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`
        
        
        """
        ...
    def getSource(self) -> str:
        """
            Get source of attitude estimate.
        
            Returns:
                source of attitude estimate
        
        
        """
        ...
    def setAttitudeStates(self, attitudeElementsType: 'AttitudeElementsType') -> None:
        """
            Set attitude states.
        
            Parameters:
                attitudeStates (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeElementsType`): attitude states
        
        
        """
        ...
    def setCovarianceType(self, attitudeCovarianceType: AttitudeCovarianceType) -> None:
        """
            Set type of attitude error state.
        
            Parameters:
                covarianceType (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeCovarianceType`): type of attitude error state
        
        
        """
        ...
    def setEulerRotSeq(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
            Set the rotation order for Euler angles.
        
            Parameters:
                eulerRotSeq (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): rotation order for Euler angles
        
        
        """
        ...
    def setId(self, string: str) -> None:
        """
            Set identification number.
        
            Parameters:
                id (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number
        
        
        """
        ...
    def setMethod(self, adMethodType: org.orekit.files.ccsds.definitions.AdMethodType) -> None:
        """
            Set attitude determination method.
        
            Parameters:
                method (:class:`~org.orekit.files.ccsds.definitions.AdMethodType`): attitude determination method
        
        
        """
        ...
    def setNbStates(self, int: int) -> None:
        """
            Set number of states for :meth:`~org.orekit.files.ccsds.definitions.AdMethodType.EKF`,
            :meth:`~org.orekit.files.ccsds.definitions.AdMethodType.BATCH` or
            :meth:`~org.orekit.files.ccsds.definitions.AdMethodType.FILTER_SMOOTHER`.
        
            Parameters:
                nbStates (int): number of states
        
        
        """
        ...
    def setPrevId(self, string: str) -> None:
        """
            Set identification of previous orbit determination.
        
            Parameters:
                prevId (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification of previous orbit determination
        
        
        """
        ...
    def setRateProcessNoiseStdDev(self, double: float) -> None:
        """
            Set process noise standard deviation if :code:`rateStates` is
            :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.ANGVEL`.
        
            Parameters:
                rateProcessNoiseStdDev (double): process noise standard deviation if :code:`rateStates` is
                    :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.ANGVEL`
        
        
        """
        ...
    def setRateStates(self, rateElementsType: 'RateElementsType') -> None:
        """
            Set attitude rate states.
        
            Parameters:
                rateStates (:class:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType`): attitude rate states
        
        
        """
        ...
    def setSigmaU(self, double: float) -> None:
        """
            Set rate random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`.
        
            Parameters:
                sigmaU (double): rate random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`
        
        
        """
        ...
    def setSigmaV(self, double: float) -> None:
        """
            Set angle random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`.
        
            Parameters:
                sigmaV (double): angle random walk if :code:`rateStates` is :meth:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType.GYRO_BIAS`
        
        
        """
        ...
    def setSource(self, string: str) -> None:
        """
            Set source of attitude estimate.
        
            Parameters:
                source (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): source of attitude estimate
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AttitudeDeterminationKey(java.lang.Enum['AttitudeDeterminationKey']):
    """
    public enum AttitudeDeterminationKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeDeterminationKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeDetermination` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, acmParser: AcmParser, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, attitudeDetermination: AttitudeDetermination) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                parser (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AcmParser`): ACM file parser
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeDetermination`): container to fill
        
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
    def valueOf(string: str) -> 'AttitudeDeterminationKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeDeterminationKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeDeterminationKey c : AttitudeDeterminationKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeDeterminationSensor(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class AttitudeDeterminationSensor extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Attitude determination sensor data.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            12.0
    """
    def __init__(self): ...
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
    def setNbSensorNoiseCovariance(self, int: int) -> None:
        """
            Set number of noise elements for sensor.
        
            Parameters:
                n (int): number of noise elements for sensor
        
        
        """
        ...
    def setSensorFrequency(self, double: float) -> None:
        """
            Set frequency of sensor data for sensor.
        
            Parameters:
                frequency (double): frequency of sensor data for sensor
        
        
        """
        ...
    def setSensorNoiseCovariance(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Set standard deviation of sensor noise for sensor.
        
            Parameters:
                stddev (double[]): standard deviation of sensor noise
        
        
        """
        ...
    def setSensorNumber(self, int: int) -> None:
        """
            Set number of the sensor.
        
            Parameters:
                sensorNumber (int): number of the sensor
        
        
        """
        ...
    def setSensorUsed(self, string: str) -> None:
        """
            Set sensor used.
        
            Parameters:
                sensorUsed (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): sensor used
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AttitudeDeterminationSensorKey(java.lang.Enum['AttitudeDeterminationSensorKey']):
    """
    public enum AttitudeDeterminationSensorKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeDeterminationSensorKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeDetermination` sensor entries.
    
        Since:
            12.0
    """
    SENSOR_NUMBER: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    SENSOR_USED: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    NUMBER_SENSOR_NOISE_COVARIANCE: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    SENSOR_NOISE_STDDEV: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    SENSOR_FREQUENCY: typing.ClassVar['AttitudeDeterminationSensorKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, attitudeDeterminationSensor: AttitudeDeterminationSensor) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeDeterminationSensor`): container to fill
        
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
    def valueOf(string: str) -> 'AttitudeDeterminationSensorKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeDeterminationSensorKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeDeterminationSensorKey c : AttitudeDeterminationSensorKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeElementsType(java.lang.Enum['AttitudeElementsType']):
    """
    public enum AttitudeElementsType extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeElementsType`>
    
        Attitude element set type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.adm.acm.Acm`.
    
        Since:
            12.0
    """
    QUATERNION: typing.ClassVar['AttitudeElementsType'] = ...
    EULER_ANGLES: typing.ClassVar['AttitudeElementsType'] = ...
    DCM: typing.ClassVar['AttitudeElementsType'] = ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def toRotation(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Convert to rotation.
        
            Parameters:
                order (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): rotation order for Euler angles
                elements (double[]): elements values in SI units
        
            Returns:
                rotation
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum.html?is` in
                class :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AttitudeElementsType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeElementsType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeElementsType c : AttitudeElementsType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeManeuver(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class AttitudeManeuver extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Maneuver entry.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            12.0
    """
    def __init__(self): ...
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
            Get reference frame for :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeManeuver.getTargetMomentum`.
        
            Returns:
                reference frame for :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeManeuver.getTargetMomentum`
        
        
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
    def setActuatorUsed(self, string: str) -> None:
        """
            Set actuator used.
        
            Parameters:
                actuatorUsed (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): actuator used
        
        
        """
        ...
    def setBeginTime(self, double: float) -> None:
        """
            Set start time of actual maneuver, relative to t₀.
        
            Parameters:
                beginTime (double): start time of actual maneuver, relative to t₀
        
        
        """
        ...
    def setDuration(self, double: float) -> None:
        """
            Set duration.
        
            Parameters:
                duration (double): duration
        
        
        """
        ...
    def setEndTime(self, double: float) -> None:
        """
            Set end time of actual maneuver, relative to t₀.
        
            Parameters:
                endTime (double): end time of actual maneuver, relative to t₀
        
        
        """
        ...
    def setID(self, string: str) -> None:
        """
            Set maneuver identification number.
        
            Parameters:
                manId (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): maneuver identification number
        
        
        """
        ...
    def setManPurpose(self, string: str) -> None:
        """
            Set purpose of maneuver.
        
            Parameters:
                manPurpose (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): purpose of maneuver
        
        
        """
        ...
    def setPrevID(self, string: str) -> None:
        """
            Set identification number of previous maneuver.
        
            Parameters:
                prevID (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of previous maneuver
        
        
        """
        ...
    def setTargetAttitude(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation) -> None:
        """
            Set target attitude (if purpose is attitude adjustment).
        
            Parameters:
                targetAttitude (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Rotation?is`): target attitude
        
        
        """
        ...
    def setTargetMomFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame for :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeManeuver.getTargetMomentum`.
        
            Parameters:
                targetMomFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): reference frame for :meth:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeManeuver.getTargetMomentum`
        
        
        """
        ...
    def setTargetMomentum(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set target momentum (if purpose is momentum desaturation).
        
            Parameters:
                targetMomentum (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): target momentum
        
        
        """
        ...
    def setTargetSpinRate(self, double: float) -> None:
        """
            Set target spin rate (if purpose is spin rate adjustment).
        
            Parameters:
                targetSpinRate (double): target spin rate
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AttitudeManeuverKey(java.lang.Enum['AttitudeManeuverKey']):
    """
    public enum AttitudeManeuverKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeManeuverKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeManeuver` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, attitudeManeuver: AttitudeManeuver) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                data (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeManeuver`): data to fill
        
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
    def valueOf(string: str) -> 'AttitudeManeuverKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeManeuverKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeManeuverKey c : AttitudeManeuverKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudePhysicalProperties(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class AttitudePhysicalProperties extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Spacecraft physical properties.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            12.0
    """
    def __init__(self): ...
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
    def setCenterOfPressure(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set the location of center of pressure.
        
            Parameters:
                centerOfPressure (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): location of center of pressure
        
        
        """
        ...
    def setCenterOfPressureReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame for center of pressure.
        
            Parameters:
                centerOfPressureReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): reference frame for center of pressure
        
        
        """
        ...
    def setDragCoefficient(self, double: float) -> None:
        """
            Set the the drag coefficient.
        
            Parameters:
                dragCoefficient (double): the drag coefficient
        
        
        """
        ...
    def setDryMass(self, double: float) -> None:
        """
            Set the mass without propellant.
        
            Parameters:
                dryMass (double): mass without propellant
        
        
        """
        ...
    def setInertiaMatrixEntry(self, int: int, int2: int, double: float) -> None:
        """
            Set an entry in the inertia matrix.
        
            Both I(j, k) and I(k, j) are set.
        
            Parameters:
                j (int): row index (must be between 0 and 3 (inclusive)
                k (int): column index (must be between 0 and 3 (inclusive)
                entry (double): value of the matrix entry
        
        
        """
        ...
    def setInertiaReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame for inertia.
        
            Parameters:
                inertiaReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): reference frame for inertia
        
        
        """
        ...
    def setWetMass(self, double: float) -> None:
        """
            Set the total mass at T₀.
        
            Parameters:
                wetMass (double): total mass at T₀
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AttitudePhysicalPropertiesKey(java.lang.Enum['AttitudePhysicalPropertiesKey']):
    """
    public enum AttitudePhysicalPropertiesKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudePhysicalPropertiesKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudePhysicalProperties` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, attitudePhysicalProperties: AttitudePhysicalProperties) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                data (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudePhysicalProperties`): data to fill
        
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
    def valueOf(string: str) -> 'AttitudePhysicalPropertiesKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudePhysicalPropertiesKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudePhysicalPropertiesKey c : AttitudePhysicalPropertiesKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeState(org.orekit.time.TimeStamped):
    """
    public class AttitudeState extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Attitude state entry.
    
        Since:
            12.0
    """
    def __init__(self, attitudeElementsType: AttitudeElementsType, rateElementsType: 'RateElementsType', absoluteDate: org.orekit.time.AbsoluteDate, stringArray: typing.Union[typing.List[str], jpype.JArray], int: int): ...
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
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
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
    def toAngular(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
            Convert to angular coordinates.
        
            Parameters:
                order (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): rotation order for Euler angles
        
            Returns:
                angular coordinates
        
        
        """
        ...

class AttitudeStateHistory(org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment[org.orekit.utils.TimeStampedAngularCoordinates]):
    """
    public class AttitudeStateHistory extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`<:class:`~org.orekit.utils.TimeStampedAngularCoordinates`>
    
        Attitude state history.
    
        Since:
            12.0
    """
    def __init__(self, attitudeStateHistoryMetadata: 'AttitudeStateHistoryMetadata', list: java.util.List[AttitudeState]): ...
    def getAngularCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider:
        """
            Get the attitude provider for this attitude ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getAttitudeProvider` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                the attitude provider for this attitude ephemeris segment.
        
        
        """
        ...
    def getAttitudeStates(self) -> java.util.List[AttitudeState]: ...
    def getAvailableDerivatives(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
            Get which derivatives of angular data are available in this attitude ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getAvailableDerivatives` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                a value indicating if the file contains rotation and/or rotation rate and/or acceleration data.
        
        
        """
        ...
    def getInterpolationMethod(self) -> str:
        """
            Get the interpolation method to be used.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getInterpolationMethod` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                the interpolation method
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of samples to use in interpolation.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getInterpolationSamples` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
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
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getReferenceFrame` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                the reference frame from which attitude is defined
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of this ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getStart` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of this ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getStop` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                ephemeris segment end date.
        
        
        """
        ...

class AttitudeStateHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class AttitudeStateHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for attitude state history.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            12.0
    """
    def __init__(self): ...
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
    def setAttBasis(self, string: str) -> None:
        """
            Set basis of this attitude state time history data.
        
            Parameters:
                attBasis (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): basis of this attitude state time history data
        
        
        """
        ...
    def setAttBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this attitude is based.
        
            Parameters:
                attBasisID (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of the orbit determination or simulation upon which this attitude is based
        
        
        """
        ...
    def setAttID(self, string: str) -> None:
        """
            Set attitude identification number.
        
            Parameters:
                attID (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): attitude identification number
        
        
        """
        ...
    def setAttPrevID(self, string: str) -> None:
        """
            Set identification number of previous attitude.
        
            Parameters:
                attPrevID (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of previous attitude
        
        
        """
        ...
    def setAttitudeType(self, attitudeElementsType: AttitudeElementsType) -> None:
        """
            Set attitude element set type.
        
            Parameters:
                attitudeType (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeElementsType`): attitude element set type
        
        
        """
        ...
    def setEulerRotSeq(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
            Set the rotation order for Euler angles.
        
            Parameters:
                eulerRotSeq (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): rotation order for Euler angles
        
        
        """
        ...
    def setNbStates(self, int: int) -> None:
        """
            Set the number of data states included (attitude components plus rates components).
        
            Parameters:
                nbStates (int): number of data states included (attitude components plus rates components)
        
        
        """
        ...
    def setRateType(self, rateElementsType: 'RateElementsType') -> None:
        """
            Set attitude rate element set type.
        
            Parameters:
                rateType (:class:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType`): attitude rate element set type
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AttitudeStateHistoryMetadataKey(java.lang.Enum['AttitudeStateHistoryMetadataKey']):
    """
    public enum AttitudeStateHistoryMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeStateHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeStateHistoryMetadata` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, attitudeStateHistoryMetadata: AttitudeStateHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.acm.AttitudeStateHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'AttitudeStateHistoryMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeStateHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeStateHistoryMetadataKey c : AttitudeStateHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RateElementsType(java.lang.Enum['RateElementsType']):
    """
    public enum RateElementsType extends :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.acm.RateElementsType`>
    
        Attitude rate element set type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.adm.acm.Acm`.
    
        Since:
            12.0
    """
    ANGVEL: typing.ClassVar['RateElementsType'] = ...
    Q_DOT: typing.ClassVar['RateElementsType'] = ...
    EULER_RATE: typing.ClassVar['RateElementsType'] = ...
    GYRO_BIAS: typing.ClassVar['RateElementsType'] = ...
    NONE: typing.ClassVar['RateElementsType'] = ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def toAngular(self, absoluteDate: org.orekit.time.AbsoluteDate, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, rotation2: org.hipparchus.geometry.euclidean.threed.Rotation, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
            Convert to angyla coordinates.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                order (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): rotation order for Euler angles
                rotation (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Rotation?is`): rotation
                first (int): index of the first element to consider
                elements (double[]): elements values in SI units
        
            Returns:
                rotation
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum.html?is` in
                class :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RateElementsType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.acm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['RateElementsType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
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
