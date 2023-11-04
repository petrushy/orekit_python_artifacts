import java.lang
import java.util
import java.util.function
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.bodies
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.ndm.odm.oem
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.general
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.sampling
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class EphemerisOcmWriter(org.orekit.files.general.EphemerisFileWriter):
    """
    public class EphemerisOcmWriter extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFileWriter`
    
        An :class:`~org.orekit.files.general.EphemerisFileWriter` generating :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`
        files.
    
        This writer is intended to write only trajectory state history blocks. It does not writes physical properties,
        covariance data, maneuver data, perturbations parameters, orbit determination or user-defined parameters. If these
        blocks are needed, then :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmWriter` must be used as it handles all OCM data
        blocks.
    
        The trajectory blocks metadata identifiers (:code:`TRAJ_ID`, :code:`TRAJ_PREV_ID`, :code:`TRAJ_NEXT_ID`) are updated
        automatically using :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.incrementTrajID`, so users
        should generally only set :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.setTrajID` in the
        template.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmWriter`, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.StreamingOcmWriter`
    """
    def __init__(self, ocmWriter: 'OcmWriter', odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, ocmMetadata: 'OcmMetadata', trajectoryStateHistoryMetadata: 'TrajectoryStateHistoryMetadata', fileFormat: org.orekit.files.ccsds.utils.FileFormat, string: str, double: float, int: int): ...
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    @typing.overload
    def write(self, string: str, ephemerisFile: org.orekit.files.general.EphemerisFile[_write_0__C, _write_0__S]) -> None: ...
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: org.orekit.files.general.EphemerisFile[_write_1__C, _write_1__S]) -> None: ...

class ManBasis(java.lang.Enum['ManBasis']):
    """
    public enum ManBasis extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManBasis`>
    
        Basis of maneuver used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    CANDIDATE: typing.ClassVar['ManBasis'] = ...
    PLANNED: typing.ClassVar['ManBasis'] = ...
    ANTICIPATED: typing.ClassVar['ManBasis'] = ...
    DETERMINED_TLM: typing.ClassVar['ManBasis'] = ...
    DETERMINED_OD: typing.ClassVar['ManBasis'] = ...
    SIMULATED: typing.ClassVar['ManBasis'] = ...
    OTHER: typing.ClassVar['ManBasis'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ManBasis':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['ManBasis']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ManBasis c : ManBasis.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ManeuverFieldType(java.lang.Enum['ManeuverFieldType']):
    """
    public enum ManeuverFieldType extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverFieldType`>
    
        Maneuver field type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    TIME_ABSOLUTE: typing.ClassVar['ManeuverFieldType'] = ...
    TIME_RELATIVE: typing.ClassVar['ManeuverFieldType'] = ...
    MAN_DURA: typing.ClassVar['ManeuverFieldType'] = ...
    DELTA_MASS: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_X: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_Y: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_Z: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_INTERP: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_MAG_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DV_X: typing.ClassVar['ManeuverFieldType'] = ...
    DV_Y: typing.ClassVar['ManeuverFieldType'] = ...
    DV_Z: typing.ClassVar['ManeuverFieldType'] = ...
    DV_MAG_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DV_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    THR_X: typing.ClassVar['ManeuverFieldType'] = ...
    THR_Y: typing.ClassVar['ManeuverFieldType'] = ...
    THR_Z: typing.ClassVar['ManeuverFieldType'] = ...
    THR_EFFIC: typing.ClassVar['ManeuverFieldType'] = ...
    THR_INTERP: typing.ClassVar['ManeuverFieldType'] = ...
    THR_ISP: typing.ClassVar['ManeuverFieldType'] = ...
    THR_MAG_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    THR_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_ID: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_X: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_Y: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_Z: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_MASS: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_RATIO: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_CDA: typing.ClassVar['ManeuverFieldType'] = ...
    def checkUnit(self, unit: org.orekit.utils.units.Unit) -> None:
        """
            Check if parsed unit is compatible with field type.
        
            Parameters:
                parsedUnit (:class:`~org.orekit.utils.units.Unit`): unit to check
        
        
        """
        ...
    def getUnit(self) -> org.orekit.utils.units.Unit:
        """
            Get the field unit.
        
            Returns:
                field unit
        
        
        """
        ...
    def isTime(self) -> bool:
        """
            Check if a field is a time field.
        
            Returns:
                true if field is a time field
        
        
        """
        ...
    def outputField(self, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, orbitManeuver: 'OrbitManeuver') -> str:
        """
            Output one maneuver field.
        
            Parameters:
                converter (:class:`~org.orekit.files.ccsds.definitions.TimeConverter`): converter for dates
                maneuver (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuver`): maneuver containing the field to output
        
            Returns:
                output field
        
        
        """
        ...
    def process(self, string: str, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, orbitManeuver: 'OrbitManeuver', int: int, string2: str) -> None:
        """
            Process one field.
        
            Parameters:
                field (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): field to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                maneuver (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuver`): maneuver to fill
                lineNumber (int): line number at which the field occurs
                fileName (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the file in which the field occurs
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ManeuverFieldType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['ManeuverFieldType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ManeuverFieldType c : ManeuverFieldType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ObjectType(java.lang.Enum['ObjectType']):
    """
    public enum ObjectType extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ObjectType`>
    
        Object type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    PAYLOAD: typing.ClassVar['ObjectType'] = ...
    ROCKET_BODY: typing.ClassVar['ObjectType'] = ...
    DEBRIS: typing.ClassVar['ObjectType'] = ...
    UNKNOWN: typing.ClassVar['ObjectType'] = ...
    OTHER: typing.ClassVar['ObjectType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ObjectType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['ObjectType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ObjectType c : ObjectType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Ocm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.odm.OdmHeader, org.orekit.files.ccsds.section.Segment['OcmMetadata', 'OcmData']], org.orekit.files.general.EphemerisFile[org.orekit.utils.TimeStampedPVCoordinates, 'TrajectoryStateHistory']):
    """
    public class Ocm extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.odm.OdmHeader`, :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmData`>> implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistory`>
    
        This class gathers the informations present in the Orbit Comprehensive Message (OCM).
    
        Since:
            11.0
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ROOT
    
        Root element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` FORMAT_VERSION_KEY
    
        Key for format version.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRAJ_LINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TRAJ_LINE
    
        Trajectory line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    COV_LINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` COV_LINE
    
        Covariance line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAN_LINE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MAN_LINE
    
        Maneuver line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNKNOWN_OBJECT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` UNKNOWN_OBJECT
    
        Default name for unknown object.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, list: java.util.List[org.orekit.files.ccsds.section.Segment['OcmMetadata', 'OcmData']], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, double: float): ...
    def getData(self) -> 'OcmData':
        """
            Get the data from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`.
        
            Returns:
                data from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`
        
        
        """
        ...
    def getMetadata(self) -> 'OcmMetadata':
        """
            Get the metadata from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`.
        
            Returns:
                metadata from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OcmSatelliteEphemeris']: ...

class OcmData(org.orekit.files.ccsds.section.Data):
    """
    public class OcmData extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Data container for Orbit Comprehensive Messages.
    
        Since:
            11.0
    """
    def __init__(self, list: java.util.List['TrajectoryStateHistory'], orbitPhysicalProperties: 'OrbitPhysicalProperties', list2: java.util.List['OrbitCovarianceHistory'], list3: java.util.List['OrbitManeuverHistory'], perturbations: 'Perturbations', orbitDetermination: 'OrbitDetermination', userDefined: org.orekit.files.ccsds.ndm.odm.UserDefined): ...
    def getCovarianceBlocks(self) -> java.util.List['OrbitCovarianceHistory']: ...
    def getManeuverBlocks(self) -> java.util.List['OrbitManeuverHistory']: ...
    def getOrbitDeterminationBlock(self) -> 'OrbitDetermination':
        """
            Get orbit determination logical block.
        
            Returns:
                orbit determination logical block (may be null)
        
        
        """
        ...
    def getPerturbationsBlock(self) -> 'Perturbations':
        """
            Get perturbations logical block.
        
            Returns:
                perturbations logical block (may be null)
        
        
        """
        ...
    def getPhysicBlock(self) -> 'OrbitPhysicalProperties':
        """
            Get physical properties logical block.
        
            Returns:
                physical properties logical block (may be null)
        
        
        """
        ...
    def getTrajectoryBlocks(self) -> java.util.List['TrajectoryStateHistory']: ...
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

class OcmDataSubStructureKey(java.lang.Enum['OcmDataSubStructureKey']):
    """
    public enum OcmDataSubStructureKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmDataSubStructureKey`>
    
        Keywords for OCM data sub-structure.
    
        Since:
            11.0
    """
    TRAJ: typing.ClassVar['OcmDataSubStructureKey'] = ...
    traj: typing.ClassVar['OcmDataSubStructureKey'] = ...
    PHYS: typing.ClassVar['OcmDataSubStructureKey'] = ...
    phys: typing.ClassVar['OcmDataSubStructureKey'] = ...
    COV: typing.ClassVar['OcmDataSubStructureKey'] = ...
    cov: typing.ClassVar['OcmDataSubStructureKey'] = ...
    MAN: typing.ClassVar['OcmDataSubStructureKey'] = ...
    man: typing.ClassVar['OcmDataSubStructureKey'] = ...
    PERT: typing.ClassVar['OcmDataSubStructureKey'] = ...
    pert: typing.ClassVar['OcmDataSubStructureKey'] = ...
    OD: typing.ClassVar['OcmDataSubStructureKey'] = ...
    od: typing.ClassVar['OcmDataSubStructureKey'] = ...
    USER: typing.ClassVar['OcmDataSubStructureKey'] = ...
    user: typing.ClassVar['OcmDataSubStructureKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, ocmParser: 'OcmParser') -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                parser (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmParser`): OCM file parser
        
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
    def valueOf(string: str) -> 'OcmDataSubStructureKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OcmDataSubStructureKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OcmDataSubStructureKey c : OcmDataSubStructureKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OcmElements(java.lang.Enum['OcmElements']):
    """
    public enum OcmElements extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmElements`>
    
        Data elements types used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            12.0
    """
    ORB: typing.ClassVar['OcmElements'] = ...
    PHYS: typing.ClassVar['OcmElements'] = ...
    COV: typing.ClassVar['OcmElements'] = ...
    MAN: typing.ClassVar['OcmElements'] = ...
    PERT: typing.ClassVar['OcmElements'] = ...
    OD: typing.ClassVar['OcmElements'] = ...
    USER: typing.ClassVar['OcmElements'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OcmElements':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OcmElements']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OcmElements c : OcmElements.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OcmMetadata(org.orekit.files.ccsds.ndm.odm.OdmMetadata):
    """
    public class OcmMetadata extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmMetadata`
    
        Meta-data for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`.
    
        Since:
            11.0
    """
    DEFAULT_SCLK_OFFSET_AT_EPOCH: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_SCLK_OFFSET_AT_EPOCH
    
        Default value for SCLK_OFFSET_AT_EPOCH.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_SCLK_SEC_PER_SI_SEC: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_SCLK_SEC_PER_SI_SEC
    
        Default value for SCLK_SEC_PER_SI_SEC.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def copy(self, double: float) -> 'OcmMetadata':
        """
            Copy the instance, making sure mandatory fields have been initialized.
        
            Message ID, previous/next references, start and stop times are not copied.
        
            Parameters:
                version (double): format version
        
            Returns:
                a new copy
        
            Since:
                12.0
        
        
        """
        ...
    def getAdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Attitude Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Attitude Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getAlternateNames(self) -> java.util.List[str]: ...
    def getCatalogName(self) -> str:
        """
            Get the specification of satellite catalog source.
        
            Returns:
                specification of satellite catalog source
        
        
        """
        ...
    def getCdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Conjunction Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Conjunction Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getCelestialSource(self) -> str:
        """
            Get the source and version of celestial body (e.g. Sun/Earth/Planetary).
        
            Returns:
                source and version of celestial body (e.g. Sun/Earth/Planetary)
        
        
        """
        ...
    def getConstellation(self) -> str:
        """
            Get the name of the constellation this space object belongs to.
        
            Returns:
                name of the constellation this space object belongs to
        
        
        """
        ...
    def getCountry(self) -> str:
        """
            Get the name of the country where the space object owner is based.
        
            Returns:
                name of the country where the space object owner is based
        
        
        """
        ...
    def getEopSource(self) -> str:
        """
            Get the source and version of Earth Orientation Parameters.
        
            Returns:
                source and version of Earth Orientation Parameters
        
        
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
    def getInterpMethodEOP(self) -> str:
        """
            Get the interpolation method for Earth Orientation Parameters.
        
            Returns:
                interpolation method for Earth Orientation Parameters
        
        
        """
        ...
    def getNextLeapEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the epoch of next leap second.
        
            Returns:
                epoch of next leap second
        
            Since:
                11.2
        
        
        """
        ...
    def getNextLeapTaimutc(self) -> float:
        """
            Get the difference (TAI – UTC) in seconds incorporated at epoch
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getNextLeapEpoch`.
        
            Returns:
                difference (TAI – UTC) in seconds incorporated at epoch
                :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getNextLeapEpoch`
        
            Since:
                11.2
        
        
        """
        ...
    def getNextMessageEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the creation date of next message from a given originator.
        
            Returns:
                creation date of next message from a given originator
        
        
        """
        ...
    def getNextMessageID(self) -> str:
        """
            Get the unique ID identifying next message from a given originator.
        
            Returns:
                unique ID identifying next message from a given originator
        
        
        """
        ...
    def getObjectDesignator(self) -> str:
        """
            Get the unique satellite identification designator for the object.
        
            Returns:
                unique satellite identification designator for the object.
        
        
        """
        ...
    def getObjectType(self) -> ObjectType:
        """
            Get the type of object.
        
            Returns:
                type of object
        
        
        """
        ...
    def getOcmDataElements(self) -> java.util.List[OcmElements]: ...
    def getOperator(self) -> str:
        """
            Get the operator of the space object.
        
            Returns:
                operator of the space object
        
        
        """
        ...
    def getOpsStatus(self) -> 'OpsStatus':
        """
            Get the operational status.
        
            Returns:
                operational status
        
        
        """
        ...
    def getOrbitCategory(self) -> 'OrbitCategory':
        """
            Get the orbit category.
        
            Returns:
                orbit category
        
        
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
        
            Since:
                11.2
        
        
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
    def getOwner(self) -> str:
        """
            Get the owner of the space object.
        
            Returns:
                owner of the space object
        
        
        """
        ...
    def getPreviousMessageEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the creation date of previous message from a given originator.
        
            Returns:
                creation date of previous message from a given originator
        
        
        """
        ...
    def getPreviousMessageID(self) -> str:
        """
            Get the unique ID identifying previous message from a given originator.
        
            Returns:
                unique ID identifying previous message from a given originator
        
        
        """
        ...
    def getPrmMessageLink(self) -> str:
        """
            Get the Unique identifier of Pointing Request Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Pointing Request Message linked to this Orbit Data Message
        
        
        """
        ...
    def getRdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Reentry Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Reentry Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getSclkOffsetAtEpoch(self) -> float:
        """
            Get the spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Returns:
                spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def getSclkSecPerSISec(self) -> float:
        """
            Get the number of spacecraft clock seconds occurring during one SI second.
        
            Returns:
                number of spacecraft clock seconds occurring during one SI second
        
        
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
            Get the difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Returns:
                difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def getTdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Tracking Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Tracking Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getTechAddress(self) -> str:
        """
            Get the address of Technical Point Of Contact at originator.
        
            Returns:
                address of Technical Point Of Contact at originator
        
        
        """
        ...
    def getTechEmail(self) -> str:
        """
            Get the email address of Technical Point Of Contact at originator.
        
            Returns:
                email address of Technical Point Of Contact at originator
        
            Since:
                11.2
        
        
        """
        ...
    def getTechOrg(self) -> str:
        """
            Get the creating agency or operator.
        
            Returns:
                creating agency or operator
        
        
        """
        ...
    def getTechPOC(self) -> str:
        """
            Get the Technical Point Of Contact at originator.
        
            Returns:
                Technical Point Of Contact at originator
        
        
        """
        ...
    def getTechPhone(self) -> str:
        """
            Get the phone number of Technical Point Of Contact at originator.
        
            Returns:
                phone number of Technical Point Of Contact at originator
        
        
        """
        ...
    def getTechPosition(self) -> str:
        """
            Get the position of Technical Point Of Contact at originator.
        
            Returns:
                position of Technical Point Of Contact at originator
        
        
        """
        ...
    def getTimeSpan(self) -> float:
        """
            Get the span of time in seconds that the OCM covers.
        
            Returns:
                span of time in seconds that the OCM covers
        
        
        """
        ...
    def getUt1mutcT0(self) -> float:
        """
            Get the difference (UT1 – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Returns:
                difference (UT1 – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def setAdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Attitude Data Message linked to this Orbit Data Message.
        
            Parameters:
                admMessageLink (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Unique identifier of Attitude Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setAlternateNames(self, list: java.util.List[str]) -> None: ...
    def setCatalogName(self, string: str) -> None:
        """
            Set the specification of satellite catalog source.
        
            Parameters:
                catalogName (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): specification of satellite catalog source
        
        
        """
        ...
    def setCdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Conjunction Data Message linked to this Orbit Data Message.
        
            Parameters:
                cdmMessageLink (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Unique identifier of Conjunction Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setCelestialSource(self, string: str) -> None:
        """
            Set the source and version of celestial body (e.g. Sun/Earth/Planetary).
        
            Parameters:
                celestialSource (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): source and version of celestial body (e.g. Sun/Earth/Planetary)
        
        
        """
        ...
    def setConstellation(self, string: str) -> None:
        """
            Set the name of the constellation this space object belongs to.
        
            Parameters:
                constellation (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the constellation this space object belongs to
        
        
        """
        ...
    def setCountry(self, string: str) -> None:
        """
            Set the name of the country where the space object owner is based.
        
            Parameters:
                country (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the country where the space object owner is based
        
        
        """
        ...
    def setEopSource(self, string: str) -> None:
        """
            Set the source and version of Earth Orientation Parameters.
        
            Parameters:
                eopSource (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): source and version of Earth Orientation Parameters
        
        
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
                internationalDesignator (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): international designator for the object
        
        
        """
        ...
    def setInterpMethodEOP(self, string: str) -> None:
        """
            Set the interpolation method for Earth Orientation Parameters.
        
            Parameters:
                interpMethodEOP (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): interpolation method for Earth Orientation Parameters
        
        
        """
        ...
    def setNextLeapEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the epoch of next leap second.
        
            Parameters:
                nextLeapEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of next leap second
        
            Since:
                11.2
        
        
        """
        ...
    def setNextLeapTaimutc(self, double: float) -> None:
        """
            Set the difference (TAI – UTC) in seconds incorporated at epoch
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getNextLeapEpoch`.
        
            Parameters:
                nextLeapTaimutc (double): difference (TAI – UTC) in seconds incorporated at epoch
                    :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getNextLeapEpoch`
        
            Since:
                11.2
        
        
        """
        ...
    def setNextMessageEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the creation date of next message from a given originator.
        
            Parameters:
                nextMessageEpoch (:class:`~org.orekit.time.AbsoluteDate`): creation date of next message from a given originator
        
        
        """
        ...
    def setNextMessageID(self, string: str) -> None:
        """
            Set the unique ID identifying next message from a given originator.
        
            Parameters:
                nextMessageID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): unique ID identifying next message from a given originator
        
        
        """
        ...
    def setObjectDesignator(self, string: str) -> None:
        """
            Set the unique satellite identification designator for the object.
        
            Parameters:
                objectDesignator (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): unique satellite identification designator for the object
        
        
        """
        ...
    def setObjectType(self, objectType: ObjectType) -> None:
        """
            Set the type of object.
        
            Parameters:
                objectType (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ObjectType`): type of object
        
        
        """
        ...
    def setOcmDataElements(self, list: java.util.List[OcmElements]) -> None: ...
    def setOperator(self, string: str) -> None:
        """
            Set the operator of the space object.
        
            Parameters:
                operator (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): operator of the space object
        
        
        """
        ...
    def setOpsStatus(self, opsStatus: 'OpsStatus') -> None:
        """
            Set the operational status.
        
            Parameters:
                opsStatus (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OpsStatus`): operational status
        
        
        """
        ...
    def setOrbitCategory(self, orbitCategory: 'OrbitCategory') -> None:
        """
            Set the orbit category.
        
            Parameters:
                orbitCategory (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCategory`): orbit category
        
        
        """
        ...
    def setOriginatorAddress(self, string: str) -> None:
        """
            Set the address of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorAddress (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorEmail(self, string: str) -> None:
        """
            Set the email address of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorEmail (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): email address of Programmatic Point Of Contact at originator
        
            Since:
                11.2
        
        
        """
        ...
    def setOriginatorPOC(self, string: str) -> None:
        """
            Set the programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPOC (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPhone(self, string: str) -> None:
        """
            Set the phone number of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPhone (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): phone number of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPosition(self, string: str) -> None:
        """
            Set the position of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPosition (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): position of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOwner(self, string: str) -> None:
        """
            Set the owner of the space object.
        
            Parameters:
                owner (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): owner of the space object
        
        
        """
        ...
    def setPreviousMessageEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the creation date of previous message from a given originator.
        
            Parameters:
                previousMessageEpoch (:class:`~org.orekit.time.AbsoluteDate`): creation date of previous message from a given originator
        
        
        """
        ...
    def setPreviousMessageID(self, string: str) -> None:
        """
            Set the unique ID identifying previous message from a given originator.
        
            Parameters:
                previousMessageID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): unique ID identifying previous message from a given originator
        
        
        """
        ...
    def setPrmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Pointing Request Message linked to this Orbit Data Message.
        
            Parameters:
                prmMessageLink (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Unique identifier of Pointing Request Message linked to this Orbit Data Message
        
        
        """
        ...
    def setRdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Reentry Data Message linked to this Orbit Data Message.
        
            Parameters:
                rdmMessageLink (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Unique identifier of Reentry Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setSclkOffsetAtEpoch(self, double: float) -> None:
        """
            Set the spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Parameters:
                sclkOffsetAtEpoch (double): spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def setSclkSecPerSISec(self, double: float) -> None:
        """
            Set the number of spacecraft clock seconds occurring during one SI second.
        
            Parameters:
                secClockPerSISec (double): number of spacecraft clock seconds occurring during one SI second
        
        
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
            Set the difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Parameters:
                taimutcT0 (double): difference (TAI – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def setTdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Tracking Data Message linked to this Orbit Data Message.
        
            Parameters:
                tdmMessageLink (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Unique identifier of Tracking Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setTechAddress(self, string: str) -> None:
        """
            Set the address of Technical Point Of Contact at originator.
        
            Parameters:
                techAddress (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): address of Technical Point Of Contact at originator
        
        
        """
        ...
    def setTechEmail(self, string: str) -> None:
        """
            Set the email address of Technical Point Of Contact at originator.
        
            Parameters:
                techEmail (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): email address of Technical Point Of Contact at originator
        
            Since:
                11.2
        
        
        """
        ...
    def setTechOrg(self, string: str) -> None:
        """
            Set the creating agency or operator.
        
            Parameters:
                techOrg (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): creating agency or operator
        
        
        """
        ...
    def setTechPOC(self, string: str) -> None:
        """
            Set the Technical Point Of Contact at originator.
        
            Parameters:
                techPOC (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Technical Point Of Contact at originator
        
        
        """
        ...
    def setTechPhone(self, string: str) -> None:
        """
            Set the phone number of Technical Point Of Contact at originator.
        
            Parameters:
                techPhone (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): phone number of Technical Point Of Contact at originator
        
        
        """
        ...
    def setTechPosition(self, string: str) -> None:
        """
            Set the position of Technical Point Of Contact at originator.
        
            Parameters:
                techPosition (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): position of Technical Point Of Contact at originator
        
        
        """
        ...
    def setTimeSpan(self, double: float) -> None:
        """
            Set the span of time in seconds that the OCM covers.
        
            Parameters:
                timeSpan (double): span of time in seconds that the OCM covers
        
        
        """
        ...
    def setUt1mutcT0(self, double: float) -> None:
        """
            Set the difference (UT1 – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Parameters:
                ut1mutcT0 (double): difference (UT1 – UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
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

class OcmMetadataKey(java.lang.Enum['OcmMetadataKey']):
    """
    public enum OcmMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata` entries.
    
        Since:
            11.0
    """
    INTERNATIONAL_DESIGNATOR: typing.ClassVar['OcmMetadataKey'] = ...
    CATALOG_NAME: typing.ClassVar['OcmMetadataKey'] = ...
    OBJECT_DESIGNATOR: typing.ClassVar['OcmMetadataKey'] = ...
    ALTERNATE_NAMES: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_POC: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_POSITION: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_PHONE: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_EMAIL: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_ADDRESS: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_ORG: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_POC: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_POSITION: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_PHONE: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_EMAIL: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_ADDRESS: typing.ClassVar['OcmMetadataKey'] = ...
    PREVIOUS_MESSAGE_ID: typing.ClassVar['OcmMetadataKey'] = ...
    NEXT_MESSAGE_ID: typing.ClassVar['OcmMetadataKey'] = ...
    ADM_MSG_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    CDM_MSG_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    PRM_MSG_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    RDM_MSG_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    TDM_MSG_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    OPERATOR: typing.ClassVar['OcmMetadataKey'] = ...
    OWNER: typing.ClassVar['OcmMetadataKey'] = ...
    COUNTRY: typing.ClassVar['OcmMetadataKey'] = ...
    CONSTELLATION: typing.ClassVar['OcmMetadataKey'] = ...
    OBJECT_TYPE: typing.ClassVar['OcmMetadataKey'] = ...
    EPOCH_TZERO: typing.ClassVar['OcmMetadataKey'] = ...
    OPS_STATUS: typing.ClassVar['OcmMetadataKey'] = ...
    ORBIT_CATEGORY: typing.ClassVar['OcmMetadataKey'] = ...
    OCM_DATA_ELEMENTS: typing.ClassVar['OcmMetadataKey'] = ...
    SCLK_OFFSET_AT_EPOCH: typing.ClassVar['OcmMetadataKey'] = ...
    SCLK_SEC_PER_SI_SEC: typing.ClassVar['OcmMetadataKey'] = ...
    PREVIOUS_MESSAGE_EPOCH: typing.ClassVar['OcmMetadataKey'] = ...
    NEXT_MESSAGE_EPOCH: typing.ClassVar['OcmMetadataKey'] = ...
    START_TIME: typing.ClassVar['OcmMetadataKey'] = ...
    STOP_TIME: typing.ClassVar['OcmMetadataKey'] = ...
    TIME_SPAN: typing.ClassVar['OcmMetadataKey'] = ...
    TAIMUTC_AT_TZERO: typing.ClassVar['OcmMetadataKey'] = ...
    NEXT_LEAP_EPOCH: typing.ClassVar['OcmMetadataKey'] = ...
    NEXT_LEAP_TAIMUTC: typing.ClassVar['OcmMetadataKey'] = ...
    UT1MUTC_AT_TZERO: typing.ClassVar['OcmMetadataKey'] = ...
    EOP_SOURCE: typing.ClassVar['OcmMetadataKey'] = ...
    INTERP_METHOD_EOP: typing.ClassVar['OcmMetadataKey'] = ...
    CELESTIAL_SOURCE: typing.ClassVar['OcmMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, ocmMetadata: OcmMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'OcmMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OcmMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OcmMetadataKey c : OcmMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OcmParser(org.orekit.files.ccsds.ndm.odm.OdmParser[Ocm, 'OcmParser'], org.orekit.files.general.EphemerisFileParser[Ocm]):
    """
    public class OcmParser extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmParser`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmParser`> implements :class:`~org.orekit.files.general.EphemerisFileParser`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`>
    
        A parser for the CCSDS OCM (Orbit Comprehensive Message).
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            11.0
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, double: float, double2: float, boolean: bool, dataContext: org.orekit.data.DataContext, double3: float, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, functionArray: typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]]): ...
    def build(self) -> Ocm:
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
    def getHeader(self) -> org.orekit.files.ccsds.ndm.odm.OdmHeader:
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
    def parse(self, dataSource: org.orekit.data.DataSource) -> Ocm:
        """
            Parse an ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFileParser.parse` in
                interface :class:`~org.orekit.files.general.EphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed ephemeris file.
        
        
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

class OcmSatelliteEphemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, 'TrajectoryStateHistory']):
    """
    public class OcmSatelliteEphemeris extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistory`>
    
        OCM ephemeris blocks for a single satellite.
    
        Since:
            11.0
    """
    def __init__(self, string: str, double: float, list: java.util.List['TrajectoryStateHistory']): ...
    def getId(self) -> str:
        """
            Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getId` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the satellite's ID, never :code:`null`.
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getMu` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getPropagator`, in
                m³/s².
        
        
        """
        ...
    def getSegments(self) -> java.util.List['TrajectoryStateHistory']: ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStart` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStop` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris end date.
        
        
        """
        ...

class OcmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.odm.OdmHeader, org.orekit.files.ccsds.section.Segment[OcmMetadata, OcmData], Ocm]):
    """
    public class OcmWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.ndm.odm.OdmHeader`, :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmData`>, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`>
    
        Writer for CCSDS Orbit Comprehensive Message.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.odm.ocm.EphemerisOcmWriter`,
            :class:`~org.orekit.files.ccsds.ndm.odm.ocm.StreamingOcmWriter`
    """
    CCSDS_OCM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_OCM_VERS
    
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
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, double: float, double2: float, dataContext: org.orekit.data.DataContext): ...
    def getEquatorialRadius(self) -> float:
        """
            Get the central body equatorial radius.
        
            Returns:
                central body equatorial radius
        
            Since:
                12.0
        
        
        """
        ...
    def getFlattening(self) -> float:
        """
            Get the central body flattening.
        
            Returns:
                central body flattening
        
            Since:
                12.0
        
        
        """
        ...

class OpsStatus(java.lang.Enum['OpsStatus']):
    """
    public enum OpsStatus extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OpsStatus`>
    
        Operational status used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    OPERATIONAL: typing.ClassVar['OpsStatus'] = ...
    NONOPERATIONAL: typing.ClassVar['OpsStatus'] = ...
    PARTIALLY_OPERATIONAL: typing.ClassVar['OpsStatus'] = ...
    BACKUP: typing.ClassVar['OpsStatus'] = ...
    STANBY: typing.ClassVar['OpsStatus'] = ...
    EXTENDED_MISSION: typing.ClassVar['OpsStatus'] = ...
    REENTRY_MODE: typing.ClassVar['OpsStatus'] = ...
    DECAYED: typing.ClassVar['OpsStatus'] = ...
    UNKNOWN: typing.ClassVar['OpsStatus'] = ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum.html?is` in
                class :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OpsStatus':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OpsStatus']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OpsStatus c : OpsStatus.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitCategory(java.lang.Enum['OrbitCategory']):
    """
    public enum OrbitCategory extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCategory`>
    
        Orbit category used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    EGO: typing.ClassVar['OrbitCategory'] = ...
    ESO: typing.ClassVar['OrbitCategory'] = ...
    GHO: typing.ClassVar['OrbitCategory'] = ...
    GEO: typing.ClassVar['OrbitCategory'] = ...
    GSO: typing.ClassVar['OrbitCategory'] = ...
    GTO: typing.ClassVar['OrbitCategory'] = ...
    HAO: typing.ClassVar['OrbitCategory'] = ...
    HEO: typing.ClassVar['OrbitCategory'] = ...
    IGO: typing.ClassVar['OrbitCategory'] = ...
    LEO: typing.ClassVar['OrbitCategory'] = ...
    LMO: typing.ClassVar['OrbitCategory'] = ...
    MEO: typing.ClassVar['OrbitCategory'] = ...
    MGO: typing.ClassVar['OrbitCategory'] = ...
    NSO: typing.ClassVar['OrbitCategory'] = ...
    UFO: typing.ClassVar['OrbitCategory'] = ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum.html?is` in
                class :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OrbitCategory':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OrbitCategory']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OrbitCategory c : OrbitCategory.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitCovariance(org.orekit.time.TimeStamped):
    """
    public class OrbitCovariance extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Covariance entry.
    
        Since:
            11.0
    """
    def __init__(self, orbitElementsType: 'OrbitElementsType', ordering: 'Ordering', absoluteDate: org.orekit.time.AbsoluteDate, stringArray: typing.List[str], int: int): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the covariance matrix.
        
            Returns:
                covariance matrix
        
        
        """
        ...
    def getType(self) -> 'OrbitElementsType':
        """
            Get the type of the elements.
        
            Returns:
                type of the elements
        
        
        """
        ...

class OrbitCovarianceHistory:
    """
    public class OrbitCovarianceHistory extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Covariance history.
    
        Since:
            11.0
    """
    def __init__(self, orbitCovarianceHistoryMetadata: 'OrbitCovarianceHistoryMetadata', list: java.util.List[OrbitCovariance]): ...
    def getCovariances(self) -> java.util.List[OrbitCovariance]: ...
    def getMetadata(self) -> 'OrbitCovarianceHistoryMetadata':
        """
            Get metadata.
        
            Returns:
                metadata
        
        
        """
        ...

class OrbitCovarianceHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class OrbitCovarianceHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for covariance history.
    
        Since:
            11.0
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate): ...
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
    def getCovConfidence(self) -> float:
        """
            Get the measure of confidence in covariance error matching reality.
        
            Returns:
                measure of confidence in covariance error matching reality
        
        
        """
        ...
    def getCovFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovarianceHistoryMetadata.getCovReferenceFrame`.
        
            Returns:
                epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovarianceHistoryMetadata.getCovReferenceFrame`
        
        
        """
        ...
    def getCovID(self) -> str:
        """
            Get covariance identification number.
        
            Returns:
                covariance identification number
        
        
        """
        ...
    def getCovNextID(self) -> str:
        """
            Get identification number of next covariance.
        
            Returns:
                identification number of next covariance
        
        
        """
        ...
    def getCovOrdering(self) -> 'Ordering':
        """
            Get covariance ordering.
        
            Returns:
                covariance ordering
        
        
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
    def getCovScaleMax(self) -> float:
        """
            Get the maximum scale factor to apply to achieve realism.
        
            Returns:
                maximum scale factor to apply to achieve realism
        
        
        """
        ...
    def getCovScaleMin(self) -> float:
        """
            Get the minimum scale factor to apply to achieve realism.
        
            Returns:
                minimum scale factor to apply to achieve realism
        
        
        """
        ...
    def getCovType(self) -> 'OrbitElementsType':
        """
            Get covariance element set type.
        
            Returns:
                covariance element set type
        
        
        """
        ...
    def getCovUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def setCovBasis(self, string: str) -> None:
        """
            Set basis of this covariance time history data.
        
            Parameters:
                covBasis (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): basis of this covariance time history data
        
        
        """
        ...
    def setCovBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this covariance is based.
        
            Parameters:
                covBasisID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of the orbit determination or simulation upon which this covariance is based
        
        
        """
        ...
    def setCovConfidence(self, double: float) -> None:
        """
            Set the measure of confidence in covariance error matching reality.
        
            Parameters:
                covConfidence (double): measure of confidence in covariance error matching reality
        
        
        """
        ...
    def setCovFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovarianceHistoryMetadata.getCovReferenceFrame`.
        
            Parameters:
                covFrameEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovarianceHistoryMetadata.getCovReferenceFrame`
        
        
        """
        ...
    def setCovID(self, string: str) -> None:
        """
            Set covariance identification number.
        
            Parameters:
                covID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): covariance identification number
        
        
        """
        ...
    def setCovNextID(self, string: str) -> None:
        """
            Set identification number of next covariance.
        
            Parameters:
                covNextID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of next covariance
        
        
        """
        ...
    def setCovOrdering(self, ordering: 'Ordering') -> None:
        """
            Set covariance ordering.
        
            Parameters:
                covOrdering (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ordering`): covariance ordering
        
        
        """
        ...
    def setCovPrevID(self, string: str) -> None:
        """
            Set identification number of previous covariance.
        
            Parameters:
                covPrevID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of previous covariance
        
        
        """
        ...
    def setCovReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame of the covariance.
        
            Parameters:
                covReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setCovScaleMax(self, double: float) -> None:
        """
            Set the maximum scale factor to apply to achieve realism.
        
            Parameters:
                covScaleMax (double): maximum scale factor to apply to achieve realism
        
        
        """
        ...
    def setCovScaleMin(self, double: float) -> None:
        """
            Set the minimum scale factor to apply to achieve realism.
        
            Parameters:
                covScaleMin (double): minimum scale factor to apply to achieve realism
        
        
        """
        ...
    def setCovType(self, orbitElementsType: 'OrbitElementsType') -> None:
        """
            Set covariance element set type.
        
            Parameters:
                covType (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitElementsType`): covariance element set type
        
        
        """
        ...
    def setCovUnits(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
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

class OrbitCovarianceHistoryMetadataKey(java.lang.Enum['OrbitCovarianceHistoryMetadataKey']):
    """
    public enum OrbitCovarianceHistoryMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovarianceHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovarianceHistoryMetadata` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_ID: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_PREV_ID: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_NEXT_ID: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_BASIS: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_BASIS_ID: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_REF_FRAME: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_FRAME_EPOCH: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_SCALE_MIN: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_SCALE_MAX: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_CONFIDENCE: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_TYPE: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_ORDERING: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    COV_UNITS: typing.ClassVar['OrbitCovarianceHistoryMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, orbitCovarianceHistoryMetadata: OrbitCovarianceHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovarianceHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'OrbitCovarianceHistoryMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OrbitCovarianceHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OrbitCovarianceHistoryMetadataKey c : OrbitCovarianceHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitDetermination(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class OrbitDetermination extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Orbit determination data.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getActualOdSpan(self) -> float:
        """
            Get actual time span used for the OD of the object.
        
            Returns:
                actual time span used for the OD of the object
        
        
        """
        ...
    def getConfidence(self) -> float:
        """
            Get confidence metric.
        
            Returns:
                confidence metric
        
        
        """
        ...
    def getConsiderN(self) -> int:
        """
            Get number of consider parameters.
        
            Returns:
                number of consider parameters
        
        
        """
        ...
    def getConsiderParameters(self) -> java.util.List[str]: ...
    def getDataTypes(self) -> java.util.List[str]: ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get time tag for orbit determination solved-for state.
        
            Returns:
                time tag for orbit determination solved-for state
        
        
        """
        ...
    def getEpochEigenInt(self) -> float:
        """
            Get positional error ellipsoid 1σ intermediate eigenvalue at the epoch of OD.
        
            Returns:
                positional error ellipsoid 1σ intermediate eigenvalue at the epoch of OD
        
        
        """
        ...
    def getEpochEigenMaj(self) -> float:
        """
            Get positional error ellipsoid 1σ major eigenvalue at the epoch of OD.
        
            Returns:
                positional error ellipsoid 1σ major eigenvalue at the epoch of OD
        
        
        """
        ...
    def getEpochEigenMin(self) -> float:
        """
            Get positional error ellipsoid 1σ minor eigenvalue at the epoch of OD.
        
            Returns:
                positional error ellipsoid 1σ minor eigenvalue at the epoch of OD
        
        
        """
        ...
    def getGdop(self) -> float:
        """
            Get generalize Dilution Of Precision.
        
            Returns:
                generalize Dilution Of Precision
        
        
        """
        ...
    def getId(self) -> str:
        """
            Get identification number.
        
            Returns:
                identification number
        
        
        """
        ...
    def getMaxPredictedEigenMaj(self) -> float:
        """
            Get maximum predicted major eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM.
        
            Returns:
                maximum predicted major eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def getMaximumObsGap(self) -> float:
        """
            Get maximum time between observations in the OD of the object.
        
            Returns:
                maximum time between observations in the OD of the object
        
        
        """
        ...
    def getMethod(self) -> org.orekit.files.ccsds.definitions.OdMethodFacade:
        """
            Get orbit determination method.
        
            Returns:
                orbit determination method
        
        
        """
        ...
    def getMinPredictedEigenMin(self) -> float:
        """
            Get minimum predicted minor eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM.
        
            Returns:
                minimum predicted v eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def getObsAvailable(self) -> int:
        """
            Get number of observations available within the actual OD span.
        
            Returns:
                number of observations available within the actual OD span
        
        
        """
        ...
    def getObsUsed(self) -> int:
        """
            Get number of observations accepted within the actual OD span.
        
            Returns:
                number of observations accepted within the actual OD span
        
        
        """
        ...
    def getPrevId(self) -> str:
        """
            Get identification of previous orbit determination.
        
            Returns:
                identification of previous orbit determination
        
        
        """
        ...
    def getRecommendedOdSpan(self) -> float:
        """
            Get time span of observation recommended for the OD of the object.
        
            Returns:
                time span of observation recommended for the OD of the object
        
        
        """
        ...
    def getSedr(self) -> float:
        """
            Get Specific Energy Dissipation Rate.
        
            Returns:
                Specific Energy Dissipation Rate
        
            Since:
                12.0
        
        
        """
        ...
    def getSensors(self) -> java.util.List[str]: ...
    def getSensorsN(self) -> int:
        """
            Get number of sensors used.
        
            Returns:
                number of sensors used
        
        
        """
        ...
    def getSolveN(self) -> int:
        """
            Get number of solved-for states.
        
            Returns:
                number of solved-for states
        
        
        """
        ...
    def getSolveStates(self) -> java.util.List[str]: ...
    def getTimeSinceFirstObservation(self) -> float:
        """
            Get time elapsed between first accepted observation on epoch.
        
            Returns:
                time elapsed between first accepted observation on epoch
        
        
        """
        ...
    def getTimeSinceLastObservation(self) -> float:
        """
            Get time elapsed between last accepted observation on epoch.
        
            Returns:
                time elapsed between last accepted observation on epoch
        
        
        """
        ...
    def getTracksAvailable(self) -> int:
        """
            Get number of sensors tracks available for the OD within the actual OD span.
        
            Returns:
                number of sensors tracks available for the OD within the actual OD span
        
        
        """
        ...
    def getTracksUsed(self) -> int:
        """
            Get number of sensors tracks accepted for the OD within the actual OD span.
        
            Returns:
                number of sensors tracks accepted for the OD within the actual OD span
        
        
        """
        ...
    def getWeightedRms(self) -> float:
        """
            Get weighted RMS residual ratio.
        
            Returns:
                weighted RMS residual ratio
        
        
        """
        ...
    def setActualOdSpan(self, double: float) -> None:
        """
            Set actual time span used for the OD of the object.
        
            Parameters:
                actualOdSpan (double): actual time span used for the OD of the object
        
        
        """
        ...
    def setConfidence(self, double: float) -> None:
        """
            Set confidence metric.
        
            Parameters:
                confidence (double): confidence metric
        
        
        """
        ...
    def setConsiderN(self, int: int) -> None:
        """
            Set number of consider parameters.
        
            Parameters:
                considerN (int): number of consider parameters
        
        
        """
        ...
    def setConsiderParameters(self, list: java.util.List[str]) -> None: ...
    def setDataTypes(self, list: java.util.List[str]) -> None: ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set time tag for orbit determination solved-for state.
        
            Parameters:
                epoch (:class:`~org.orekit.time.AbsoluteDate`): time tag for orbit determination solved-for state
        
        
        """
        ...
    def setEpochEigenInt(self, double: float) -> None:
        """
            Set positional error ellipsoid 1σ intermediate eigenvalue at the epoch of OD.
        
            Parameters:
                epochEigenInt (double): positional error ellipsoid 1σ intermediate eigenvalue at the epoch of OD
        
        
        """
        ...
    def setEpochEigenMaj(self, double: float) -> None:
        """
            Set positional error ellipsoid 1σ major eigenvalue at the epoch of OD.
        
            Parameters:
                epochEigenMaj (double): positional error ellipsoid 1σ major eigenvalue at the epoch of OD
        
        
        """
        ...
    def setEpochEigenMin(self, double: float) -> None:
        """
            Set positional error ellipsoid 1σ minor eigenvalue at the epoch of OD.
        
            Parameters:
                epochEigenMin (double): positional error ellipsoid 1σ minor eigenvalue at the epoch of OD
        
        
        """
        ...
    def setGdop(self, double: float) -> None:
        """
            Set generalize Dilution Of Precision.
        
            Parameters:
                gdop (double): generalize Dilution Of Precision
        
        
        """
        ...
    def setId(self, string: str) -> None:
        """
            Set identification number.
        
            Parameters:
                id (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number
        
        
        """
        ...
    def setMaxPredictedEigenMaj(self, double: float) -> None:
        """
            Set maximum predicted major eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM.
        
            Parameters:
                maxPredictedEigenMaj (double): maximum predicted major eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def setMaximumObsGap(self, double: float) -> None:
        """
            Set maximum time between observations in the OD of the object.
        
            Parameters:
                maximumObsGap (double): maximum time between observations in the OD of the object
        
        
        """
        ...
    def setMethod(self, odMethodFacade: org.orekit.files.ccsds.definitions.OdMethodFacade) -> None:
        """
            Set orbit determination method.
        
            Parameters:
                method (:class:`~org.orekit.files.ccsds.definitions.OdMethodFacade`): orbit determination method
        
        
        """
        ...
    def setMinPredictedEigenMin(self, double: float) -> None:
        """
            Set minimum predicted minor eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM.
        
            Parameters:
                minPredictedEigenMin (double): minimum predicted minor eigenvalue of 1σ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def setObsAvailable(self, int: int) -> None:
        """
            Set number of observations available within the actual OD span.
        
            Parameters:
                obsAvailable (int): number of observations available within the actual OD span
        
        
        """
        ...
    def setObsUsed(self, int: int) -> None:
        """
            Set number of observations accepted within the actual OD span.
        
            Parameters:
                obsUsed (int): number of observations accepted within the actual OD span
        
        
        """
        ...
    def setPrevId(self, string: str) -> None:
        """
            Set identification of previous orbit determination.
        
            Parameters:
                prevId (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification of previous orbit determination
        
        
        """
        ...
    def setRecommendedOdSpan(self, double: float) -> None:
        """
            Set time span of observation recommended for the OD of the object.
        
            Parameters:
                recommendedOdSpan (double): time span of observation recommended for the OD of the object
        
        
        """
        ...
    def setSedr(self, double: float) -> None:
        """
            Set Specific Energy Dissipation Rate.
        
            Parameters:
                sedr (double): Specific Energy Dissipation Rate (W/kg)
        
            Since:
                12.0
        
        
        """
        ...
    def setSensors(self, list: java.util.List[str]) -> None: ...
    def setSensorsN(self, int: int) -> None:
        """
            Set number of sensors used.
        
            Parameters:
                sensorsN (int): number of sensors used
        
        
        """
        ...
    def setSolveN(self, int: int) -> None:
        """
            Set number of solved-for states.
        
            Parameters:
                solveN (int): number of solved-for states
        
        
        """
        ...
    def setSolveStates(self, list: java.util.List[str]) -> None: ...
    def setTimeSinceFirstObservation(self, double: float) -> None:
        """
            Set time elapsed between first accepted observation on epoch.
        
            Parameters:
                timeSinceFirstObservation (double): time elapsed between first accepted observation on epoch
        
        
        """
        ...
    def setTimeSinceLastObservation(self, double: float) -> None:
        """
            Set time elapsed between last accepted observation on epoch.
        
            Parameters:
                timeSinceLastObservation (double): time elapsed between last accepted observation on epoch
        
        
        """
        ...
    def setTracksAvailable(self, int: int) -> None:
        """
            Set number of sensors tracks available for the OD within the actual OD span.
        
            Parameters:
                tracksAvailable (int): number of sensors tracks available for the OD within the actual OD span
        
        
        """
        ...
    def setTracksUsed(self, int: int) -> None:
        """
            Set number of sensors tracks accepted for the OD within the actual OD span.
        
            Parameters:
                tracksUsed (int): number of sensors tracks accepted for the OD within the actual OD span
        
        
        """
        ...
    def setWeightedRms(self, double: float) -> None:
        """
            Set weighted RMS residual ratio.
        
            Parameters:
                weightedRms (double): weighted RMS residual ratio
        
        
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

class OrbitDeterminationKey(java.lang.Enum['OrbitDeterminationKey']):
    """
    public enum OrbitDeterminationKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitDeterminationKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitDetermination` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_ID: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_PREV_ID: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_METHOD: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH: typing.ClassVar['OrbitDeterminationKey'] = ...
    DAYS_SINCE_FIRST_OBS: typing.ClassVar['OrbitDeterminationKey'] = ...
    DAYS_SINCE_LAST_OBS: typing.ClassVar['OrbitDeterminationKey'] = ...
    RECOMMENDED_OD_SPAN: typing.ClassVar['OrbitDeterminationKey'] = ...
    ACTUAL_OD_SPAN: typing.ClassVar['OrbitDeterminationKey'] = ...
    OBS_AVAILABLE: typing.ClassVar['OrbitDeterminationKey'] = ...
    OBS_USED: typing.ClassVar['OrbitDeterminationKey'] = ...
    TRACKS_AVAILABLE: typing.ClassVar['OrbitDeterminationKey'] = ...
    TRACKS_USED: typing.ClassVar['OrbitDeterminationKey'] = ...
    MAXIMUM_OBS_GAP: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH_EIGMAJ: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH_EIGINT: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH_EIGMIN: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_MAX_PRED_EIGMAJ: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_MIN_PRED_EIGMIN: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_CONFIDENCE: typing.ClassVar['OrbitDeterminationKey'] = ...
    GDOP: typing.ClassVar['OrbitDeterminationKey'] = ...
    SOLVE_N: typing.ClassVar['OrbitDeterminationKey'] = ...
    SOLVE_STATES: typing.ClassVar['OrbitDeterminationKey'] = ...
    CONSIDER_N: typing.ClassVar['OrbitDeterminationKey'] = ...
    CONSIDER_PARAMS: typing.ClassVar['OrbitDeterminationKey'] = ...
    SEDR: typing.ClassVar['OrbitDeterminationKey'] = ...
    SENSORS_N: typing.ClassVar['OrbitDeterminationKey'] = ...
    SENSORS: typing.ClassVar['OrbitDeterminationKey'] = ...
    WEIGHTED_RMS: typing.ClassVar['OrbitDeterminationKey'] = ...
    DATA_TYPES: typing.ClassVar['OrbitDeterminationKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, orbitDetermination: OrbitDetermination) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitDetermination`): container to fill
        
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
    def valueOf(string: str) -> 'OrbitDeterminationKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OrbitDeterminationKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OrbitDeterminationKey c : OrbitDeterminationKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitElementsType(java.lang.Enum['OrbitElementsType']):
    """
    public enum OrbitElementsType extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitElementsType`>
    
        Orbit element set type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.sanaregistry.org.r.orbital_elements`
    """
    ADBARV: typing.ClassVar['OrbitElementsType'] = ...
    CARTP: typing.ClassVar['OrbitElementsType'] = ...
    CARTPV: typing.ClassVar['OrbitElementsType'] = ...
    CARTPVA: typing.ClassVar['OrbitElementsType'] = ...
    DELAUNAY: typing.ClassVar['OrbitElementsType'] = ...
    DELAUNAYMOD: typing.ClassVar['OrbitElementsType'] = ...
    EIGVAL3EIGVEC3: typing.ClassVar['OrbitElementsType'] = ...
    EQUINOCTIAL: typing.ClassVar['OrbitElementsType'] = ...
    EQUINOCTIALMOD: typing.ClassVar['OrbitElementsType'] = ...
    GEODETIC: typing.ClassVar['OrbitElementsType'] = ...
    KEPLERIAN: typing.ClassVar['OrbitElementsType'] = ...
    KEPLERIANMEAN: typing.ClassVar['OrbitElementsType'] = ...
    LDBARV: typing.ClassVar['OrbitElementsType'] = ...
    ONSTATION: typing.ClassVar['OrbitElementsType'] = ...
    POINCARE: typing.ClassVar['OrbitElementsType'] = ...
    def getUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def toCartesian(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double2: float) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Convert to Cartesian coordinates.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): elements date
                elements (double[]): elements values in SI units
                body (:class:`~org.orekit.bodies.OneAxisEllipsoid`): central body (may be null if type is *not* :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitElementsType.GEODETIC`)
                mu (double): gravitational parameter in m³/s²
        
            Returns:
                Cartesian coordinates
        
        
        """
        ...
    def toRawElements(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> typing.List[float]:
        """
            Convert to raw elements array.
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): Cartesian coordinates
                frame (:class:`~org.orekit.frames.Frame`): inertial frame where elements are defined
                body (:class:`~org.orekit.bodies.OneAxisEllipsoid`): central body (may be null if type is *not* :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitElementsType.GEODETIC`)
                mu (double): gravitational parameter in m³/s²
        
            Returns:
                elements elements values in SI units
        
            Since:
                12.0
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum.html?is` in
                class :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OrbitElementsType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OrbitElementsType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OrbitElementsType c : OrbitElementsType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitManeuver(org.orekit.time.TimeStamped):
    """
    public class OrbitManeuver extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Maneuver entry.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get acceleration.
        
            Returns:
                acceleration
        
        
        """
        ...
    def getAccelerationDirectionSigma(self) -> float:
        """
            Get one σ angular off-nominal acceleration direction.
        
            Returns:
                one σ angular off-nominal acceleration direction
        
        
        """
        ...
    def getAccelerationInterpolation(self) -> org.orekit.files.ccsds.definitions.OnOff:
        """
            Get interpolation mode between current and next acceleration line.
        
            Returns:
                interpolation mode between current and next acceleration line
        
        
        """
        ...
    def getAccelerationMagnitudeSigma(self) -> float:
        """
            Get one σ percent error on acceleration magnitude.
        
            Returns:
                one σ percent error on acceleration magnitude
        
        
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
    def getDeltaMass(self) -> float:
        """
            Get mass change.
        
            Returns:
                mass change
        
        
        """
        ...
    def getDeployDirSigma(self) -> float:
        """
            Get one σ angular off-nominal deployment vector direction.
        
            Returns:
                one σ angular off-nominal deployment vector direction
        
        
        """
        ...
    def getDeployDv(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get velocity increment of deployed "child" object.
        
            Returns:
                velocity increment of deployed "child" object
        
        
        """
        ...
    def getDeployDvCda(self) -> float:
        """
            Get typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object.
        
            Returns:
                typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object
        
        
        """
        ...
    def getDeployDvRatio(self) -> float:
        """
            Get ratio of child-to-host ΔV vectors.
        
            Returns:
                ratio of child-to-host ΔV vectors
        
        
        """
        ...
    def getDeployDvSigma(self) -> float:
        """
            Get one σ percent error on deployment ΔV magnitude.
        
            Returns:
                one σ percent error on deployment ΔV magnitude
        
        
        """
        ...
    def getDeployId(self) -> str:
        """
            Get identifier of resulting "child" object deployed from this host.
        
            Returns:
                identifier of resulting "child" object deployed from this host
        
        
        """
        ...
    def getDeployMass(self) -> float:
        """
            Get decrement in host mass as a result of deployment.
        
            Returns:
                decrement in host mass as a result of deployment (shall be ≤ 0)
        
        
        """
        ...
    def getDuration(self) -> float:
        """
            Get duration.
        
            Returns:
                duration
        
        
        """
        ...
    def getDv(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get velocity increment.
        
            Returns:
                velocity increment
        
        
        """
        ...
    def getDvDirSigma(self) -> float:
        """
            Get one σ angular off-nominal ΔV direction.
        
            Returns:
                one σ angular off-nominal ΔV direction
        
        
        """
        ...
    def getDvMagSigma(self) -> float:
        """
            Get one σ percent error on ΔV magnitude.
        
            Returns:
                one σ percent error on ΔV magnitude
        
        
        """
        ...
    def getThrust(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get thrust.
        
            Returns:
                thrust
        
        
        """
        ...
    def getThrustDirectionSigma(self) -> float:
        """
            Get one σ angular off-nominal thrust direction.
        
            Returns:
                one σ angular off-nominal thrust direction
        
        
        """
        ...
    def getThrustEfficiency(self) -> float:
        """
            Get thrust efficiency η.
        
            Returns:
                thrust efficiency η (typically between 0.0 and 1.0)
        
        
        """
        ...
    def getThrustInterpolation(self) -> org.orekit.files.ccsds.definitions.OnOff:
        """
            Get interpolation mode between current and next thrust line.
        
            Returns:
                interpolation mode between current and next thrust line
        
        
        """
        ...
    def getThrustIsp(self) -> float:
        """
            Get thrust specific impulse.
        
            Returns:
                thrust specific impulse
        
        
        """
        ...
    def getThrustMagnitudeSigma(self) -> float:
        """
            Get one σ percent error on thrust magnitude.
        
            Returns:
                one σ percent error on thrust magnitude
        
        
        """
        ...
    def setAcceleration(self, int: int, double: float) -> None:
        """
            Set acceleration component.
        
            Parameters:
                i (int): component index
                ai (double): i :sup:`th` component of acceleration
        
        
        """
        ...
    def setAccelerationDirectionSigma(self, double: float) -> None:
        """
            Set one σ angular off-nominal acceleration direction.
        
            Parameters:
                accelerationDirectionSigma (double): one σ angular off-nominal acceleration direction
        
        
        """
        ...
    def setAccelerationInterpolation(self, onOff: org.orekit.files.ccsds.definitions.OnOff) -> None:
        """
            Set interpolation mode between current and next acceleration line.
        
            Parameters:
                accelerationInterpolation (:class:`~org.orekit.files.ccsds.definitions.OnOff`): interpolation mode between current and next acceleration line
        
        
        """
        ...
    def setAccelerationMagnitudeSigma(self, double: float) -> None:
        """
            Set one σ percent error on acceleration magnitude.
        
            Parameters:
                accelerationMagnitudeSigma (double): one σ percent error on acceleration magnitude
        
        
        """
        ...
    def setDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): maneuver date
        
        
        """
        ...
    def setDeltaMass(self, double: float) -> None:
        """
            Set mass change.
        
            Parameters:
                deltaMass (double): mass change
        
        
        """
        ...
    def setDeployDirSigma(self, double: float) -> None:
        """
            Set one σ angular off-nominal deployment vector direction.
        
            Parameters:
                deployDirSigma (double): one σ angular off-nominal deployment vector direction
        
        
        """
        ...
    def setDeployDv(self, int: int, double: float) -> None:
        """
            Set velocity increment component of deployed "child" object.
        
            Parameters:
                i (int): component index
                deployDvi (double): i :sup:`th` component of velocity increment of deployed "child" object
        
        
        """
        ...
    def setDeployDvCda(self, double: float) -> None:
        """
            Set typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object.
        
            Parameters:
                deployDvCda (double): typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object
        
        
        """
        ...
    def setDeployDvRatio(self, double: float) -> None:
        """
            Set ratio of child-to-host ΔV vectors.
        
            Parameters:
                deployDvRatio (double): ratio of child-to-host ΔV vectors
        
        
        """
        ...
    def setDeployDvSigma(self, double: float) -> None:
        """
            Set one σ percent error on deployment ΔV magnitude.
        
            Parameters:
                deployDvSigma (double): one σ percent error on deployment ΔV magnitude
        
        
        """
        ...
    def setDeployId(self, string: str) -> None:
        """
            Set identifier of resulting "child" object deployed from this host.
        
            Parameters:
                deployId (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identifier of resulting "child" object deployed from this host
        
        
        """
        ...
    def setDeployMass(self, double: float) -> None:
        """
            Set decrement in host mass as a result of deployment.
        
            Parameters:
                deployMass (double): decrement in host mass as a result of deployment (shall be ≤ 0)
        
        
        """
        ...
    def setDuration(self, double: float) -> None:
        """
            Set duration.
        
            Parameters:
                duration (double): duration
        
        
        """
        ...
    def setDv(self, int: int, double: float) -> None:
        """
            Set velocity increment component.
        
            Parameters:
                i (int): component index
                dVi (double): i :sup:`th` component of velocity increment
        
        
        """
        ...
    def setDvDirSigma(self, double: float) -> None:
        """
            Set one σ angular off-nominal ΔV direction.
        
            Parameters:
                dvDirSigma (double): one σ angular off-nominal ΔV direction
        
        
        """
        ...
    def setDvMagSigma(self, double: float) -> None:
        """
            Set one σ percent error on ΔV magnitude.
        
            Parameters:
                dvMagSigma (double): one σ percent error on ΔV magnitude
        
        
        """
        ...
    def setThrust(self, int: int, double: float) -> None:
        """
            Set thrust component.
        
            Parameters:
                i (int): component index
                ti (double): i :sup:`th` component of thrust
        
        
        """
        ...
    def setThrustDirectionSigma(self, double: float) -> None:
        """
            Set one σ angular off-nominal thrust direction.
        
            Parameters:
                thrustDirectionSigma (double): one σ angular off-nominal thrust direction
        
        
        """
        ...
    def setThrustEfficiency(self, double: float) -> None:
        """
            Set thrust efficiency η.
        
            Parameters:
                thrustEfficiency (double): thrust efficiency η (typically between 0.0 and 1.0)
        
        
        """
        ...
    def setThrustInterpolation(self, onOff: org.orekit.files.ccsds.definitions.OnOff) -> None:
        """
            Set interpolation mode between current and next thrust line.
        
            Parameters:
                thrustInterpolation (:class:`~org.orekit.files.ccsds.definitions.OnOff`): interpolation mode between current and next thrust line
        
        
        """
        ...
    def setThrustIsp(self, double: float) -> None:
        """
            Set thrust specific impulse.
        
            Parameters:
                thrustIsp (double): thrust specific impulse
        
        
        """
        ...
    def setThrustMagnitudeSigma(self, double: float) -> None:
        """
            Set one σ percent error on thrust magnitude.
        
            Parameters:
                thrustMagnitudeSigma (double): one σ percent error on thrust magnitude
        
        
        """
        ...

class OrbitManeuverHistory:
    """
    public class OrbitManeuverHistory extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Maneuver history.
    
        Since:
            11.0
    """
    def __init__(self, orbitManeuverHistoryMetadata: 'OrbitManeuverHistoryMetadata', list: java.util.List[OrbitManeuver]): ...
    def getManeuvers(self) -> java.util.List[OrbitManeuver]: ...
    def getMetadata(self) -> 'OrbitManeuverHistoryMetadata':
        """
            Get metadata.
        
            Returns:
                metadata
        
        
        """
        ...

class OrbitManeuverHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class OrbitManeuverHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for maneuver history.
    
        Since:
            11.0
    """
    DEFAULT_DC_TYPE: typing.ClassVar[org.orekit.files.ccsds.definitions.DutyCycleType] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.definitions.DutyCycleType` DEFAULT_DC_TYPE
    
        Default duty cycle type.
    
        Since:
            12.0
    
    
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def getDcBodyFrame(self) -> org.orekit.files.ccsds.definitions.SpacecraftBodyFrame:
        """
            Get spacecraft body frame in which
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyTrigger` is specified.
        
            Returns:
                spacecraft body frame in which :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyTrigger`
                is specified
        
        
        """
        ...
    def getDcBodyTrigger(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyFrame` for triggering
            duty cycle.
        
            Returns:
                direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyFrame` for triggering duty
                cycle
        
        
        """
        ...
    def getDcExecStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start time of initial duty cycle-based maneuver execution.
        
            Returns:
                start time of initial duty cycle-based maneuver execution
        
        
        """
        ...
    def getDcExecStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end time of final duty cycle-based maneuver execution.
        
            Returns:
                end time of final duty cycle-based maneuver execution
        
        
        """
        ...
    def getDcMaxCycles(self) -> int:
        """
            Get the maximum number of "ON" duty cycles.
        
            Returns:
                maximum number of "ON" duty cycles (-1 if not set)
        
        
        """
        ...
    def getDcMinCycles(self) -> int:
        """
            Get the minimum number of "ON" duty cycles.
        
            Returns:
                minimum number of "ON" duty cycles (-1 if not set)
        
        
        """
        ...
    def getDcPhaseStartAngle(self) -> float:
        """
            Get phase angle of pulse start.
        
            Returns:
                phase angle of pulse start
        
        
        """
        ...
    def getDcPhaseStopAngle(self) -> float:
        """
            Get phase angle of pulse stop.
        
            Returns:
                phase angle of pulse stop
        
        
        """
        ...
    def getDcRefDir(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get reference direction for triggering duty cycle.
        
            Returns:
                reference direction for triggering duty cycle
        
        
        """
        ...
    def getDcRefTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get duty cycle thrust reference time.
        
            Returns:
                duty cycle thrust reference time
        
        
        """
        ...
    def getDcTimePulseDuration(self) -> float:
        """
            Get duty cycle pulse "ON" duration.
        
            Returns:
                duty cycle pulse "ON" duration
        
        
        """
        ...
    def getDcTimePulsePeriod(self) -> float:
        """
            Get duty cycle elapsed time between start of a pulse and start of next pulse.
        
            Returns:
                duty cycle elapsed time between start of a pulse and start of next pulse
        
        
        """
        ...
    def getDcType(self) -> org.orekit.files.ccsds.definitions.DutyCycleType:
        """
            Get type of duty cycle.
        
            Returns:
                type of duty cycle
        
        
        """
        ...
    def getDcWindowClose(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end time of duty cycle-based maneuver window.
        
            Returns:
                end time of duty cycle-based maneuver window
        
        
        """
        ...
    def getDcWindowOpen(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start time of duty cycle-based maneuver window.
        
            Returns:
                start time of duty cycle-based maneuver window
        
        
        """
        ...
    def getGravitationalAssist(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
            Get the origin of gravitational assist.
        
            Returns:
                the origin of gravitational assist.
        
        
        """
        ...
    def getManBasis(self) -> ManBasis:
        """
            Get basis of this maneuver history data.
        
            Returns:
                basis of this maneuver history data
        
        
        """
        ...
    def getManBasisID(self) -> str:
        """
            Get identification number of the orbit determination or simulation upon which this maneuver is based.
        
            Returns:
                identification number of the orbit determination or simulation upon which this maneuver is based
        
        
        """
        ...
    def getManComposition(self) -> java.util.List[ManeuverFieldType]: ...
    def getManDeviceID(self) -> str:
        """
            Get identifier of the device used for this maneuver.
        
            Returns:
                identifier of the device used for this maneuver
        
        
        """
        ...
    def getManFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getManReferenceFrame`.
        
            Returns:
                epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getManReferenceFrame`
        
        
        """
        ...
    def getManID(self) -> str:
        """
            Get maneuver identification number.
        
            Returns:
                maneuver identification number
        
        
        """
        ...
    def getManNextEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start time of next maneuver.
        
            Returns:
                start time of next maneuver
        
        
        """
        ...
    def getManNextID(self) -> str:
        """
            Get identification number of next maneuver.
        
            Returns:
                identification number of next maneuver
        
        
        """
        ...
    def getManPredSource(self) -> str:
        """
            Get prediction source on which this maneuver is based.
        
            Returns:
                prediction source on which this maneuver is based
        
        
        """
        ...
    def getManPrevEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get completion time of previous maneuver.
        
            Returns:
                completion time of previous maneuver
        
        
        """
        ...
    def getManPrevID(self) -> str:
        """
            Get identification number of previous maneuver.
        
            Returns:
                identification number of previous maneuver
        
        
        """
        ...
    def getManPurpose(self) -> java.util.List[str]: ...
    def getManReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get reference frame of the maneuver.
        
            Returns:
                reference frame of the maneuver
        
        
        """
        ...
    def getManUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def setDcBodyFrame(self, spacecraftBodyFrame: org.orekit.files.ccsds.definitions.SpacecraftBodyFrame) -> None:
        """
            Set spacecraft body frame in which
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyTrigger` is specified.
        
            Parameters:
                dcBodyFrame (:class:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame`): spacecraft body frame in which :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyTrigger`
                    is specified
        
        
        """
        ...
    def setDcBodyTrigger(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyFrame` for triggering
            duty cycle.
        
            Parameters:
                dcBodyTrigger (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getDcBodyFrame` for triggering duty
                    cycle
        
        
        """
        ...
    def setDcExecStart(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start time of initial duty cycle-based maneuver execution.
        
            Parameters:
                dcExecStart (:class:`~org.orekit.time.AbsoluteDate`): start time of initial duty cycle-based maneuver execution
        
        
        """
        ...
    def setDcExecStop(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the end time of final duty cycle-based maneuver execution.
        
            Parameters:
                dcExecStop (:class:`~org.orekit.time.AbsoluteDate`): end time of final duty cycle-based maneuver execution
        
        
        """
        ...
    def setDcMaxCycles(self, int: int) -> None:
        """
            Set the maximum number of "ON" duty cycles.
        
            Parameters:
                dcMaxCycles (int): maximum number of "ON" duty cycles
        
        
        """
        ...
    def setDcMinCycles(self, int: int) -> None:
        """
            Set the minimum number of "ON" duty cycles.
        
            Parameters:
                dcMinCycles (int): minimum number of "ON" duty cycles
        
        
        """
        ...
    def setDcPhaseStartAngle(self, double: float) -> None:
        """
            Set phase angle of pulse start.
        
            Parameters:
                dcPhaseStartAngle (double): phase angle of pulse start
        
        
        """
        ...
    def setDcPhaseStopAngle(self, double: float) -> None:
        """
            Set phase angle of pulse stop.
        
            Parameters:
                dcPhaseStopAngle (double): phase angle of pulse stop
        
        
        """
        ...
    def setDcRefDir(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set reference direction for triggering duty cycle.
        
            Parameters:
                dcRefDir (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): reference direction for triggering duty cycle
        
        
        """
        ...
    def setDcRefTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set duty cycle thrust reference time.
        
            Parameters:
                dcRefTime (:class:`~org.orekit.time.AbsoluteDate`): duty cycle thrust reference time
        
        
        """
        ...
    def setDcTimePulseDuration(self, double: float) -> None:
        """
            Set duty cycle pulse "ON" duration.
        
            Parameters:
                dcTimePulseDuration (double): duty cycle pulse "ON" duration
        
        
        """
        ...
    def setDcTimePulsePeriod(self, double: float) -> None:
        """
            Set duty cycle elapsed time between start of a pulse and start of next pulse.
        
            Parameters:
                dcTimePulsePeriod (double): duty cycle elapsed time between start of a pulse and start of next pulse
        
        
        """
        ...
    def setDcType(self, dutyCycleType: org.orekit.files.ccsds.definitions.DutyCycleType) -> None:
        """
            Set type of duty cycle.
        
            Parameters:
                dcType (:class:`~org.orekit.files.ccsds.definitions.DutyCycleType`): type of duty cycle
        
        
        """
        ...
    def setDcWindowClose(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the end time of duty cycle-based maneuver window.
        
            Parameters:
                dcWindowClose (:class:`~org.orekit.time.AbsoluteDate`): end time of duty cycle-based maneuver window
        
        
        """
        ...
    def setDcWindowOpen(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start time of duty cycle-based maneuver window.
        
            Parameters:
                dcWindowOpen (:class:`~org.orekit.time.AbsoluteDate`): start time of duty cycle-based maneuver window
        
        
        """
        ...
    def setGravitationalAssist(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
            Set the origin of gravitational assist.
        
            Parameters:
                gravitationalAssist (:class:`~org.orekit.files.ccsds.definitions.BodyFacade`): origin of gravitational assist to be set
        
        
        """
        ...
    def setManBasis(self, manBasis: ManBasis) -> None:
        """
            Set basis of this maneuver history data.
        
            Parameters:
                manBasis (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManBasis`): basis of this maneuver history data
        
        
        """
        ...
    def setManBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this maneuver is based.
        
            Parameters:
                manBasisID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of the orbit determination or simulation upon which this maneuver is based
        
        
        """
        ...
    def setManComposition(self, list: java.util.List[ManeuverFieldType]) -> None: ...
    def setManDeviceID(self, string: str) -> None:
        """
            Set identifier of the device used for this maneuver.
        
            Parameters:
                manDeviceID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identifier of the device used for this maneuver
        
        
        """
        ...
    def setManFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getManReferenceFrame`.
        
            Parameters:
                manFrameEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata.getManReferenceFrame`
        
        
        """
        ...
    def setManID(self, string: str) -> None:
        """
            Set maneuver identification number.
        
            Parameters:
                manID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): maneuver identification number
        
        
        """
        ...
    def setManNextEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set start time of next maneuver.
        
            Parameters:
                manNextEpoch (:class:`~org.orekit.time.AbsoluteDate`): start time of next maneuver
        
        
        """
        ...
    def setManNextID(self, string: str) -> None:
        """
            Set identification number of next maneuver.
        
            Parameters:
                manNextID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of next maneuver
        
        
        """
        ...
    def setManPredSource(self, string: str) -> None:
        """
            Set prediction source on which this maneuver is based.
        
            Parameters:
                manPredSource (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): prediction source on which this maneuver is based
        
        
        """
        ...
    def setManPrevEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set completion time of previous maneuver.
        
            Parameters:
                manPrevEpoch (:class:`~org.orekit.time.AbsoluteDate`): completion time of previous maneuver
        
        
        """
        ...
    def setManPrevID(self, string: str) -> None:
        """
            Set identification number of previous maneuver.
        
            Parameters:
                manPrevID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of previous maneuver
        
        
        """
        ...
    def setManPurpose(self, list: java.util.List[str]) -> None: ...
    def setManReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame of the maneuver.
        
            Parameters:
                manReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setManUnits(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
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

class OrbitManeuverHistoryMetadataKey(java.lang.Enum['OrbitManeuverHistoryMetadataKey']):
    """
    public enum OrbitManeuverHistoryMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_ID: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_PREV_ID: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_NEXT_ID: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_BASIS: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_BASIS_ID: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_DEVICE_ID: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_PREV_EPOCH: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_NEXT_EPOCH: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_PURPOSE: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_PRED_SOURCE: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_REF_FRAME: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_FRAME_EPOCH: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    GRAV_ASSIST_NAME: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_TYPE: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_WIN_OPEN: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_WIN_CLOSE: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_MIN_CYCLES: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_MAX_CYCLES: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_EXEC_START: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_EXEC_STOP: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_REF_TIME: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_TIME_PULSE_DURATION: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_TIME_PULSE_PERIOD: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_REF_DIR: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_BODY_FRAME: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_BODY_TRIGGER: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_PA_START_ANGLE: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    DC_PA_STOP_ANGLE: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_COMPOSITION: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    MAN_UNITS: typing.ClassVar['OrbitManeuverHistoryMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, orbitManeuverHistoryMetadata: OrbitManeuverHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitManeuverHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'OrbitManeuverHistoryMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OrbitManeuverHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OrbitManeuverHistoryMetadataKey c : OrbitManeuverHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitPhysicalProperties(org.orekit.files.ccsds.ndm.CommonPhysicalProperties):
    """
    public class OrbitPhysicalProperties extends :class:`~org.orekit.files.ccsds.ndm.CommonPhysicalProperties`
    
        Spacecraft physical properties.
    
        Since:
            11.0
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def getAttitudeActuatorType(self) -> str:
        """
            Get the type of actuator for attitude control.
        
            Returns:
                type of actuator for attitude control
        
        
        """
        ...
    def getAttitudeControlAccuracy(self) -> float:
        """
            Get the accuracy of attitude control.
        
            Returns:
                accuracy of attitude control
        
        
        """
        ...
    def getAttitudeControlMode(self) -> str:
        """
            Get the attitude control mode.
        
            Returns:
                attitude control mode
        
        
        """
        ...
    def getAttitudeKnowledgeAccuracy(self) -> float:
        """
            Get the accuracy of attitude knowledge.
        
            Returns:
                accuracy of attitude knowledge
        
        
        """
        ...
    def getAttitudePointingAccuracy(self) -> float:
        """
            Get the overall accuracy of spacecraft to maintain attitude.
        
            Returns:
                overall accuracy of spacecraft to maintain attitude
        
        
        """
        ...
    def getBolDv(self) -> float:
        """
            Get the total ΔV capability at beginning of life.
        
            Returns:
                total ΔV capability at beginning of life
        
        
        """
        ...
    def getBusModel(self) -> str:
        """
            Get the bus model name.
        
            Returns:
                bus model name
        
        
        """
        ...
    def getDockedWith(self) -> java.util.List[str]: ...
    def getDragCoefficient(self) -> float:
        """
            Get the nominal drag coefficient.
        
            Returns:
                the nominal drag coefficient
        
        
        """
        ...
    def getDragConstantArea(self) -> float:
        """
            Get the attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB.
        
            Returns:
                attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def getDragUncertainty(self) -> float:
        """
            Get the drag coefficient 1σ uncertainty.
        
            Returns:
                drag coefficient 1σ uncertainty (in %)
        
        
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
    def getInitialWetMass(self) -> float:
        """
            Get the total mass at beginning of life.
        
            Returns:
                total mass at beginning of life
        
        
        """
        ...
    def getManeuversFrequency(self) -> float:
        """
            Get the average frequency of orbit or attitude maneuvers (in SI units, hence per second).
        
            Returns:
                average frequency of orbit or attitude maneuvers (in SI units, hence per second).
        
        
        """
        ...
    def getManeuversPerYear(self) -> float:
        """
            Get the average number of orbit or attitude maneuvers per year.
        
            Returns:
                average number of orbit or attitude maneuvers per year.
        
        
        """
        ...
    def getManufacturer(self) -> str:
        """
            Get manufacturer name.
        
            Returns:
                manufacturer name
        
        
        """
        ...
    def getMaxAreaForCollisionProbability(self) -> float:
        """
            Get the maximum cross-sectional area for collision probability estimation purposes.
        
            Returns:
                maximum cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def getMaxThrust(self) -> float:
        """
            Get the maximum composite thrust the spacecraft can accomplish.
        
            Returns:
                maximum composite thrust the spacecraft can accomplish
        
        
        """
        ...
    def getMinAreaForCollisionProbability(self) -> float:
        """
            Get the minimum cross-sectional area for collision probability estimation purposes.
        
            Returns:
                minimum cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def getRemainingDv(self) -> float:
        """
            Get the total ΔV remaining for spacecraft.
        
            Returns:
                total ΔV remaining for spacecraft
        
        
        """
        ...
    def getSrpCoefficient(self) -> float:
        """
            Get the nominal SRP coefficient.
        
            Returns:
                nominal SRP coefficient
        
        
        """
        ...
    def getSrpConstantArea(self) -> float:
        """
            Get the attitude-independent SRP area, not already into attitude-dependent area along OEB.
        
            Returns:
                attitude-independent SRP area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def getSrpUncertainty(self) -> float:
        """
            Get the SRP coefficient 1σ uncertainty.
        
            Returns:
                SRP coefficient 1σ uncertainty
        
        
        """
        ...
    def getTypAreaForCollisionProbability(self) -> float:
        """
            Get the typical (50th percentile) cross-sectional area for collision probability estimation purposes.
        
            Returns:
                typical (50th percentile) cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def getWetMass(self) -> float:
        """
            Get the total mass at T₀.
        
            Returns:
                total mass at T₀
        
        
        """
        ...
    def setAttitudeActuatorType(self, string: str) -> None:
        """
            Set the type of actuator for attitude control.
        
            Parameters:
                attitudeActuatorType (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): type of actuator for attitude control
        
        
        """
        ...
    def setAttitudeControlAccuracy(self, double: float) -> None:
        """
            Set the accuracy of attitude control.
        
            Parameters:
                attitudeControlAccuracy (double): accuracy of attitude control
        
        
        """
        ...
    def setAttitudeControlMode(self, string: str) -> None:
        """
            Set the attitude control mode.
        
            Parameters:
                attitudeControlMode (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): attitude control mode
        
        
        """
        ...
    def setAttitudeKnowledgeAccuracy(self, double: float) -> None:
        """
            Set the accuracy of attitude knowledge.
        
            Parameters:
                attitudeKnowledgeAccuracy (double): accuracy of attitude knowledge
        
        
        """
        ...
    def setAttitudePointingAccuracy(self, double: float) -> None:
        """
            Set the overall accuracy of spacecraft to maintain attitude.
        
            Parameters:
                attitudePointingAccuracy (double): overall accuracy of spacecraft to maintain attitude
        
        
        """
        ...
    def setBolDv(self, double: float) -> None:
        """
            Set the total ΔV capability at beginning of life.
        
            Parameters:
                bolDv (double): total ΔV capability at beginning of life
        
        
        """
        ...
    def setBusModel(self, string: str) -> None:
        """
            Set the bus model name.
        
            Parameters:
                busModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): bus model name
        
        
        """
        ...
    def setDockedWith(self, list: java.util.List[str]) -> None: ...
    def setDragCoefficient(self, double: float) -> None:
        """
            Set the the nominal drag coefficient.
        
            Parameters:
                dragCoefficient (double): the nominal drag coefficient
        
        
        """
        ...
    def setDragConstantArea(self, double: float) -> None:
        """
            Set the attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB.
        
            Parameters:
                dragConstantArea (double): attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def setDragUncertainty(self, double: float) -> None:
        """
            Set the drag coefficient 1σ uncertainty.
        
            Parameters:
                dragUncertainty (double): drag coefficient 1σ uncertainty (in %)
        
        
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
    def setInitialWetMass(self, double: float) -> None:
        """
            Set the total mass at beginning of life.
        
            Parameters:
                initialWetMass (double): total mass at beginning of life
        
        
        """
        ...
    def setManeuversFrequency(self, double: float) -> None:
        """
            Set the average frequency of orbit or attitude maneuvers (in SI units, hence per second).
        
            Parameters:
                maneuversFrequency (double): average frequency of orbit or attitude (in SI units, hence per second).
        
        
        """
        ...
    def setManufacturer(self, string: str) -> None:
        """
            Set manufacturer name.
        
            Parameters:
                manufacturer (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): manufacturer name
        
        
        """
        ...
    def setMaxAreaForCollisionProbability(self, double: float) -> None:
        """
            Set the maximum cross-sectional area for collision probability estimation purposes.
        
            Parameters:
                maxAreaForCollisionProbability (double): maximum cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def setMaxThrust(self, double: float) -> None:
        """
            Set the maximum composite thrust the spacecraft can accomplish.
        
            Parameters:
                maxThrust (double): maximum composite thrust the spacecraft can accomplish
        
        
        """
        ...
    def setMinAreaForCollisionProbability(self, double: float) -> None:
        """
            Set the minimum cross-sectional area for collision probability estimation purposes.
        
            Parameters:
                minAreaForCollisionProbability (double): minimum cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def setRemainingDv(self, double: float) -> None:
        """
            Set the total ΔV remaining for spacecraft.
        
            Parameters:
                remainingDv (double): total ΔV remaining for spacecraft
        
        
        """
        ...
    def setSrpCoefficient(self, double: float) -> None:
        """
            Set the nominal SRP coefficient.
        
            Parameters:
                srpCoefficient (double): nominal SRP coefficient
        
        
        """
        ...
    def setSrpConstantArea(self, double: float) -> None:
        """
            Set the attitude-independent SRP area, not already into attitude-dependent area along OEB.
        
            Parameters:
                srpConstantArea (double): attitude-independent SRP area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def setSrpUncertainty(self, double: float) -> None:
        """
            Set the SRP coefficient 1σ uncertainty.
        
            Parameters:
                srpUncertainty (double): SRP coefficient 1σ uncertainty.
        
        
        """
        ...
    def setTypAreaForCollisionProbability(self, double: float) -> None:
        """
            Get the typical (50th percentile) cross-sectional area for collision probability estimation purposes.
        
            Parameters:
                typAreaForCollisionProbability (double): typical (50th percentile) cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def setWetMass(self, double: float) -> None:
        """
            Set the total mass at T₀.
        
            Parameters:
                wetMass (double): total mass at T₀
        
        
        """
        ...

class OrbitPhysicalPropertiesKey(java.lang.Enum['OrbitPhysicalPropertiesKey']):
    """
    public enum OrbitPhysicalPropertiesKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitPhysicalPropertiesKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitPhysicalProperties` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    MANUFACTURER: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    BUS_MODEL: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    DOCKED_WITH: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    DRAG_CONST_AREA: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    DRAG_COEFF_NOM: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    DRAG_UNCERTAINTY: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    INITIAL_WET_MASS: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    WET_MASS: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    DRY_MASS: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_PARENT_FRAME: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_PARENT_FRAME_EPOCH: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_Q1: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_Q2: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_Q3: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_QC: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_MAX: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_INT: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    OEB_MIN: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    AREA_ALONG_OEB_MAX: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    AREA_ALONG_OEB_INT: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    AREA_ALONG_OEB_MIN: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    AREA_MIN_FOR_PC: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    AREA_MAX_FOR_PC: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    AREA_TYP_FOR_PC: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    RCS: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    RCS_MIN: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    RCS_MAX: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    SRP_CONST_AREA: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    SOLAR_RAD_COEFF: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    SOLAR_RAD_UNCERTAINTY: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    VM_ABSOLUTE: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    VM_APPARENT_MIN: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    VM_APPARENT: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    VM_APPARENT_MAX: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    REFLECTANCE: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    ATT_CONTROL_MODE: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    ATT_ACTUATOR_TYPE: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    ATT_KNOWLEDGE: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    ATT_CONTROL: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    ATT_POINTING: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    AVG_MANEUVER_FREQ: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    MAX_THRUST: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    DV_BOL: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    DV_REMAINING: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    IXX: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    IYY: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    IZZ: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    IXY: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    IXZ: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    IYZ: typing.ClassVar['OrbitPhysicalPropertiesKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, orbitPhysicalProperties: OrbitPhysicalProperties) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                data (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitPhysicalProperties`): data to fill
        
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
    def valueOf(string: str) -> 'OrbitPhysicalPropertiesKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['OrbitPhysicalPropertiesKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OrbitPhysicalPropertiesKey c : OrbitPhysicalPropertiesKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Ordering(java.lang.Enum['Ordering']):
    """
    public enum Ordering extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ordering`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCovariance` elements ordering.
    
        Since:
            11.0
    """
    LTM: typing.ClassVar['Ordering'] = ...
    UTM: typing.ClassVar['Ordering'] = ...
    FULL: typing.ClassVar['Ordering'] = ...
    LTMWCC: typing.ClassVar['Ordering'] = ...
    UTMWCC: typing.ClassVar['Ordering'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Ordering':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['Ordering']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (Ordering c : Ordering.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Perturbations(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class Perturbations extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Perturbation parameters.
    
        Since:
            11.0
    """
    def __init__(self, celestialBodies: org.orekit.bodies.CelestialBodies): ...
    def getAlbedoGridSize(self) -> int:
        """
            Get albedo grid size.
        
            Returns:
                albedo grid size
        
        
        """
        ...
    def getAlbedoModel(self) -> str:
        """
            Get albedo model.
        
            Returns:
                albedo model
        
        
        """
        ...
    def getAtmosphericModel(self) -> str:
        """
            Get name of atmospheric model.
        
            Returns:
                name of atmospheric model
        
        
        """
        ...
    def getCentralBodyRotation(self) -> float:
        """
            Get central body angular rotation rate.
        
            Returns:
                central body angular rotation rate
        
        
        """
        ...
    def getEquatorialRadius(self) -> float:
        """
            Get oblate spheroid equatorial radius of central body.
        
            Returns:
                oblate spheroid equatorial radius of central body
        
        
        """
        ...
    def getFixedF10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7
        
        
        """
        ...
    def getFixedF10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7
        
        
        """
        ...
    def getFixedGeomagneticAp(self) -> float:
        """
            Get fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aₚ.
        
            Returns:
                fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aₚ
        
        
        """
        ...
    def getFixedGeomagneticDst(self) -> float:
        """
            Get fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst.
        
            Returns:
                fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst
        
        
        """
        ...
    def getFixedGeomagneticKp(self) -> float:
        """
            Get fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kₚ.
        
            Returns:
                fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kₚ
        
        
        """
        ...
    def getFixedM10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux daily proxy M10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux daily proxy M10.7
        
        
        """
        ...
    def getFixedM10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7
        
        
        """
        ...
    def getFixedS10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux daily proxy S10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux daily proxy S10.7
        
        
        """
        ...
    def getFixedS10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7
        
        
        """
        ...
    def getFixedY10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux daily proxy Y10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux daily proxy Y10.7
        
        
        """
        ...
    def getFixedY10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7
        
        
        """
        ...
    def getGm(self) -> float:
        """
            Get gravitational coefficient of attracting body.
        
            Returns:
                gravitational coefficient of attracting body
        
        
        """
        ...
    def getGravityDegree(self) -> int:
        """
            Get degree of the gravity model.
        
            Returns:
                degree of the gravity model
        
        
        """
        ...
    def getGravityModel(self) -> str:
        """
            Get gravity model name.
        
            Returns:
                gravity model name
        
        
        """
        ...
    def getGravityOrder(self) -> int:
        """
            Get order of the gravity model.
        
            Returns:
                order of the gravity model
        
        
        """
        ...
    def getInterpMethodSW(self) -> str:
        """
            Get the interpolation method for Space Weather data.
        
            Returns:
                interpolation method for Space Weather data
        
        
        """
        ...
    def getNBodyPerturbations(self) -> java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]: ...
    def getOblateFlattening(self) -> float:
        """
            Get central body oblate spheroid oblateness.
        
            Returns:
                central body oblate spheroid oblateness
        
        
        """
        ...
    def getOceanTidesModel(self) -> str:
        """
            Get ocean tides model.
        
            Returns:
                ocean tides model
        
        
        """
        ...
    def getReductionTheory(self) -> str:
        """
            Get reduction theory used for precession and nutation modeling.
        
            Returns:
                reduction theory used for precession and nutation modeling
        
        
        """
        ...
    def getShadowBodies(self) -> java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]: ...
    def getShadowModel(self) -> 'ShadowModel':
        """
            Get shadow model used for solar radiation pressure.
        
            Returns:
                shadow model used for solar radiation pressure
        
        
        """
        ...
    def getSolidTidesModel(self) -> str:
        """
            Get solid tides model.
        
            Returns:
                solid tides model
        
        
        """
        ...
    def getSpaceWeatherEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the Space Weather data.
        
            Returns:
                epoch of the Space Weather data
        
        
        """
        ...
    def getSpaceWeatherSource(self) -> str:
        """
            Get Space Weather data source.
        
            Returns:
                Space Weather data source
        
        
        """
        ...
    def getSrpModel(self) -> str:
        """
            Get Solar Radiation Pressure model.
        
            Returns:
                Solar Radiation Pressure model
        
        
        """
        ...
    def setAlbedoGridSize(self, int: int) -> None:
        """
            Set albedo grid size.
        
            Parameters:
                albedoGridSize (int): albedo grid size
        
        
        """
        ...
    def setAlbedoModel(self, string: str) -> None:
        """
            Set albedo model.
        
            Parameters:
                albedoModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): albedo model
        
        
        """
        ...
    def setAtmosphericModel(self, string: str) -> None:
        """
            Set name of atmospheric model.
        
            Parameters:
                atmosphericModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of atmospheric model
        
        
        """
        ...
    def setCentralBodyRotation(self, double: float) -> None:
        """
            Set central body angular rotation rate.
        
            Parameters:
                centralBodyRotation (double): central body angular rotation rate
        
        
        """
        ...
    def setEquatorialRadius(self, double: float) -> None:
        """
            Set oblate spheroid equatorial radius of central body.
        
            Parameters:
                equatorialRadius (double): oblate spheroid equatorial radius of central body
        
        
        """
        ...
    def setFixedF10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7.
        
            Parameters:
                fixedF10P7 (double): fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7
        
        
        """
        ...
    def setFixedF10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7.
        
            Parameters:
                fixedF10P7Mean (double): fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7
        
        
        """
        ...
    def setFixedGeomagneticAp(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aₚ.
        
            Parameters:
                fixedGeomagneticAp (double): fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aₚ
        
        
        """
        ...
    def setFixedGeomagneticDst(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst.
        
            Parameters:
                fixedGeomagneticDst (double): fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst
        
        
        """
        ...
    def setFixedGeomagneticKp(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kₚ.
        
            Parameters:
                fixedGeomagneticKp (double): fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kₚ
        
        
        """
        ...
    def setFixedM10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux daily proxy M10.7.
        
            Parameters:
                fixedM10P7 (double): fixed (time invariant) value of the Solar Flux daily proxy M10.7
        
        
        """
        ...
    def setFixedM10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7.
        
            Parameters:
                fixedM10P7Mean (double): fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7
        
        
        """
        ...
    def setFixedS10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux daily proxy S10.7.
        
            Parameters:
                fixedS10P7 (double): fixed (time invariant) value of the Solar Flux daily proxy S10.7
        
        
        """
        ...
    def setFixedS10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7.
        
            Parameters:
                fixedS10P7Mean (double): fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7
        
        
        """
        ...
    def setFixedY10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux daily proxy Y10.7.
        
            Parameters:
                fixedY10P7 (double): fixed (time invariant) value of the Solar Flux daily proxy Y10.7
        
        
        """
        ...
    def setFixedY10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7.
        
            Parameters:
                fixedY10P7Mean (double): fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7
        
        
        """
        ...
    def setGm(self, double: float) -> None:
        """
            Set gravitational coefficient of attracting body.
        
            Parameters:
                gm (double): gravitational coefficient of attracting body
        
        
        """
        ...
    def setGravityModel(self, string: str, int: int, int2: int) -> None:
        """
            Set gravity model.
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the model
                degree (int): degree of the model
                order (int): order of the model
        
        
        """
        ...
    def setInterpMethodSW(self, string: str) -> None:
        """
            Set the interpolation method for Space Weather data.
        
            Parameters:
                interpMethodSW (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): interpolation method for Space Weather data
        
        
        """
        ...
    def setNBodyPerturbations(self, list: java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]) -> None: ...
    def setOblateFlattening(self, double: float) -> None:
        """
            Set central body oblate spheroid oblateness.
        
            Parameters:
                oblateFlattening (double): central body oblate spheroid oblateness
        
        
        """
        ...
    def setOceanTidesModel(self, string: str) -> None:
        """
            Set ocean tides model.
        
            Parameters:
                oceanTidesModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): ocean tides model
        
        
        """
        ...
    def setReductionTheory(self, string: str) -> None:
        """
            Set reduction theory used for precession and nutation modeling.
        
            Parameters:
                reductionTheory (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): reduction theory used for precession and nutation modeling
        
        
        """
        ...
    def setShadowBodies(self, list: java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]) -> None: ...
    def setShadowModel(self, shadowModel: 'ShadowModel') -> None:
        """
            Set shadow model used for solar radiation pressure.
        
            Parameters:
                shadowModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ShadowModel`): shadow model used for solar radiation pressure
        
        
        """
        ...
    def setSolidTidesModel(self, string: str) -> None:
        """
            Set solid tides model.
        
            Parameters:
                solidTidesModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): solid tides model
        
        
        """
        ...
    def setSpaceWeatherEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the Space Weather data.
        
            Parameters:
                spaceWeatherEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the Space Weather data
        
        
        """
        ...
    def setSpaceWeatherSource(self, string: str) -> None:
        """
            Set Space Weather data source.
        
            Parameters:
                spaceWeatherSource (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Space Weather data source
        
        
        """
        ...
    def setSrpModel(self, string: str) -> None:
        """
            Set Solar Radiation Pressure model.
        
            Parameters:
                srpModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Solar Radiation Pressure model
        
        
        """
        ...

class PerturbationsKey(java.lang.Enum['PerturbationsKey']):
    """
    public enum PerturbationsKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.PerturbationsKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Perturbations` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['PerturbationsKey'] = ...
    ATMOSPHERIC_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    GRAVITY_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    EQUATORIAL_RADIUS: typing.ClassVar['PerturbationsKey'] = ...
    GM: typing.ClassVar['PerturbationsKey'] = ...
    N_BODY_PERTURBATIONS: typing.ClassVar['PerturbationsKey'] = ...
    CENTRAL_BODY_ROTATION: typing.ClassVar['PerturbationsKey'] = ...
    OBLATE_FLATTENING: typing.ClassVar['PerturbationsKey'] = ...
    OCEAN_TIDES_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    SOLID_TIDES_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    REDUCTION_THEORY: typing.ClassVar['PerturbationsKey'] = ...
    ALBEDO_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    ALBEDO_GRID_SIZE: typing.ClassVar['PerturbationsKey'] = ...
    SHADOW_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    SHADOW_BODIES: typing.ClassVar['PerturbationsKey'] = ...
    SRP_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    SW_DATA_SOURCE: typing.ClassVar['PerturbationsKey'] = ...
    SW_DATA_EPOCH: typing.ClassVar['PerturbationsKey'] = ...
    SW_INTERP_METHOD: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_GEOMAG_KP: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_GEOMAG_AP: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_GEOMAG_DST: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_F10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_F10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_M10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_M10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_S10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_S10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_Y10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_Y10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, perturbations: Perturbations) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Perturbations`): container to fill
        
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
    def valueOf(string: str) -> 'PerturbationsKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['PerturbationsKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PerturbationsKey c : PerturbationsKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ShadowModel(java.lang.Enum['ShadowModel']):
    """
    public enum ShadowModel extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ShadowModel`>
    
        Shadow model for solar radiation pressure.
    
        Since:
            11.0
    """
    NONE: typing.ClassVar['ShadowModel'] = ...
    CYLINDRICAL: typing.ClassVar['ShadowModel'] = ...
    CONE: typing.ClassVar['ShadowModel'] = ...
    DUAL_CONE: typing.ClassVar['ShadowModel'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ShadowModel':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['ShadowModel']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ShadowModel c : ShadowModel.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StreamingOcmWriter(java.lang.AutoCloseable):
    """
    public class StreamingOcmWriter extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable?is`
    
        A writer for OCM files.
    
        Each instance corresponds to a single Orbit Comprehensive Message. A new OCM ephemeris trajectory state history block is
        started by calling :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.StreamingOcmWriter.newBlock`.
    
        This writer is intended to write only trajectory state history blocks. It does not writes physical properties,
        covariance data, maneuver data, perturbations parameters, orbit determination or user-defined parameters. If these
        blocks are needed, then :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmWriter` must be used as it handles all OCM data
        blocks.
    
        The trajectory blocks metadata identifiers (:code:`TRAJ_ID`, :code:`TRAJ_PREV_ID`, :code:`TRAJ_NEXT_ID`) are updated
        automatically using :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.incrementTrajID`, so users
        should generally only set :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.setTrajID` in the
        template.
    
        The blocks returned by this class can be used as step handlers for a :class:`~org.orekit.propagation.Propagator`.
    
        .. code-block: java
        
         Propagator propagator = ...; // pre-configured propagator
         OCMWriter  ocmWriter  = ...; // pre-configured writer
           try (Generator out = ...;  // set-up output stream
                StreamingOcmWriter sw = new StreamingOcmWriter(out, ocmWriter, header, metadata, template)) { // set-up streaming writer
        
             // write block 1
             propagator.getMultiplexer().add(step, sw.newBlock());
             propagator.propagate(startDate1, stopDate1);
        
             ...
        
             // write block n
             propagator.getMultiplexer().clear();
             propagator.getMultiplexer().add(step, sw.newBlock());
             propagator.propagate(startDateN, stopDateN);
        
           }
         
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmWriter`, :class:`~org.orekit.files.ccsds.ndm.odm.ocm.EphemerisOcmWriter`
    """
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, ocmWriter: OcmWriter, odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, ocmMetadata: OcmMetadata, trajectoryStateHistoryMetadata: 'TrajectoryStateHistoryMetadata'): ...
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, ocmWriter: OcmWriter, odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, ocmMetadata: OcmMetadata, trajectoryStateHistoryMetadata: 'TrajectoryStateHistoryMetadata', boolean: bool): ...
    def close(self) -> None: ...
    def newBlock(self) -> 'StreamingOcmWriter.BlockWriter':
        """
            Create a writer for a new OCM trajectory state history block.
        
            The returned writer can only write a single trajectory state history block in an OCM. This method must be called to
            create a writer for each trajectory state history block.
        
            Returns:
                a new OCM trajectory state history block writer, ready for use.
        
        
        """
        ...
    class BlockWriter(org.orekit.propagation.sampling.OrekitFixedStepHandler):
        def __init__(self, streamingOcmWriter: 'StreamingOcmWriter'): ...
        def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def handleStep(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> None: ...

class TrajectoryState(org.orekit.time.TimeStamped):
    """
    public class TrajectoryState extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        Trajectory state entry.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, orbitElementsType: OrbitElementsType, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, orbitElementsType: OrbitElementsType, absoluteDate: org.orekit.time.AbsoluteDate, stringArray: typing.List[str], int: int, list: java.util.List[org.orekit.utils.units.Unit]): ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get which derivatives of position are available in this state.
        
            Returns:
                a value indicating if the file contains velocity and/or acceleration
        
        
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
    def getElements(self) -> typing.List[float]:
        """
            Get trajectory elements.
        
            Returns:
                trajectory elements
        
        
        """
        ...
    def getType(self) -> OrbitElementsType:
        """
            Get the type of the elements.
        
            Returns:
                type of the elements
        
        
        """
        ...
    def toCartesian(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Convert to Cartesian coordinates.
        
            Parameters:
                body (:class:`~org.orekit.bodies.OneAxisEllipsoid`): central body (may be null if :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryState.getType` is *not*
                    :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitElementsType.GEODETIC`)
                mu (double): gravitational parameter in m³/s²
        
            Returns:
                Cartesian coordinates
        
        
        """
        ...

class TrajectoryStateHistory(org.orekit.files.general.EphemerisFile.EphemerisSegment[org.orekit.utils.TimeStampedPVCoordinates]):
    """
    public class TrajectoryStateHistory extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`>
    
        Trajectory state history.
    
        Since:
            11.0
    """
    def __init__(self, trajectoryStateHistoryMetadata: 'TrajectoryStateHistoryMetadata', list: java.util.List[TrajectoryState], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get which derivatives of position are available in this ephemeris segment.
        
            While :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates` always returns position, velocity,
            and acceleration the return value from this method indicates which of those are in the ephemeris file and are actually
            valid.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getAvailableDerivatives` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                a value indicating if the file contains velocity and/or acceleration data.
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
            Get central body.
        
            Returns:
                central body
        
            Since:
                12.0
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame for this ephemeris segment. The defining frame for
            :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the reference frame for this segment. Never :code:`null`.
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of samples to use in interpolation.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getInterpolationSamples` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the number of points to use for interpolation.
        
        
        """
        ...
    def getMetadata(self) -> 'TrajectoryStateHistoryMetadata':
        """
            Get metadata.
        
            Returns:
                metadata
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getMu` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getPropagator`, in
                m³/s².
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStart` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStop` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment end date.
        
        
        """
        ...
    def getTrajectoryStates(self) -> java.util.List[TrajectoryState]: ...

class TrajectoryStateHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class TrajectoryStateHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for trajectory state history.
    
        Since:
            11.0
    """
    DEFAULT_INTERPOLATION_METHOD: typing.ClassVar[org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod` DEFAULT_INTERPOLATION_METHOD
    
        Default interpolation method.
    
        Since:
            12.0
    
    
    """
    DEFAULT_INTERPOLATION_DEGREE: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_INTERPOLATION_DEGREE
    
        Default interpolation degree.
    
        Since:
            12.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, dataContext: org.orekit.data.DataContext): ...
    def copy(self, double: float) -> 'TrajectoryStateHistoryMetadata':
        """
            Copy the instance, making sure mandatory fields have been initialized.
        
            Dates and orbit counter are not copied.
        
            Parameters:
                version (double): format version
        
            Returns:
                a new copy
        
            Since:
                12.0
        
        
        """
        ...
    def getCenter(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
            Get the origin of reference frame.
        
            Returns:
                the origin of reference frame.
        
        
        """
        ...
    def getInterpolationDegree(self) -> int:
        """
            Get the interpolation degree.
        
            Returns:
                the interpolation degree
        
        
        """
        ...
    def getInterpolationMethod(self) -> org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod:
        """
            Get the interpolation method to be used.
        
            Returns:
                the interpolation method
        
        
        """
        ...
    def getOrbAveraging(self) -> str:
        """
            Get type of averaging (Osculating, mean Brouwer, other.
        
            Returns:
                type of averaging (Osculating, mean Brouwer, other)
        
        
        """
        ...
    def getOrbRevNum(self) -> int:
        """
            Get the integer orbit revolution number.
        
            Returns:
                integer orbit revolution number (-1 if not set)
        
        
        """
        ...
    def getOrbRevNumBasis(self) -> int:
        """
            Get the basis for orbit revolution number.
        
            This specifies if first launch/deployment is on orbit 0 or 1.
        
            Returns:
                basis for orbit revolution number (-1 if not set)
        
        
        """
        ...
    def getPropagator(self) -> str:
        """
            Get the orbit propagator used to generate this trajectory.
        
            Returns:
                orbit propagator used to generate this trajectory
        
            Since:
                11.2
        
        
        """
        ...
    def getTrajBasis(self) -> str:
        """
            Get basis of this trajectory state time history data.
        
            Returns:
                basis of this trajectory state time history data
        
        
        """
        ...
    def getTrajBasisID(self) -> str:
        """
            Get identification number of the orbit determination or simulation upon which this trajectory is based.
        
            Returns:
                identification number of the orbit determination or simulation upon which this trajectory is based
        
        
        """
        ...
    def getTrajFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`.
        
            Returns:
                epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`
        
        
        """
        ...
    def getTrajID(self) -> str:
        """
            Get trajectory identification number.
        
            Returns:
                trajectory identification number
        
        
        """
        ...
    def getTrajNextID(self) -> str:
        """
            Get identification number of next trajectory.
        
            Returns:
                identification number of next trajectory
        
        
        """
        ...
    def getTrajPrevID(self) -> str:
        """
            Get identification number of previous trajectory.
        
            Returns:
                identification number of previous trajectory
        
        
        """
        ...
    def getTrajReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get reference frame of the trajectory.
        
            Returns:
                reference frame of the trajectory
        
        
        """
        ...
    def getTrajType(self) -> OrbitElementsType:
        """
            Get trajectory element set type.
        
            Returns:
                trajectory element set type
        
        
        """
        ...
    def getTrajUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def getUseableStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Returns:
                the useable start time
        
        
        """
        ...
    def getUseableStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get end of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Returns:
                the useable stop time
        
        
        """
        ...
    @staticmethod
    def incrementTrajID(string: str) -> str:
        """
            Increments a trajectory ID.
        
            The trajectory blocks metadata contains three identifiers (:code:`TRAJ_ID`, :code:`TRAJ_PREV_ID`, :code:`TRAJ_NEXT_ID`)
            that link the various blocks together. This helper method allows to update one identifier based on the value of another
            identifier. The update is performed by looking for an integer suffix at the end of the :code:`original` identifier and
            incrementing it by one, taking care to use at least the same number of digits. If for example the original identifier is
            set to :code:`trajectory 037`, then the updated identifier will be :code:`trajectory 038`.
        
            This helper function is intended to be used by ephemeris generators like
            :class:`~org.orekit.files.ccsds.ndm.odm.ocm.EphemerisOcmWriter` and
            :class:`~org.orekit.files.ccsds.ndm.odm.ocm.StreamingOcmWriter`, allowing users to call only
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.setTrajBasisID` in the trajectory metadata
            template. The ephemeris generators call
            :code:`template.setTrajNextID(TrajectoryStateHistoryMetadata.incrementTrajID(template.getTrajID()))` before generating
            each trajectory block and call both :code:`template.setTrajPrevID(template.getTrajID()))` and
            :code:`template.setTrajID(template.getTrajNextID()))` after having generated each block.
        
            Parameters:
                original (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): original ID (may be null)
        
            Returns:
                incremented ID, or null if original was null
        
        
        """
        ...
    def setCenter(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
            Set the origin of reference frame.
        
            Parameters:
                center (:class:`~org.orekit.files.ccsds.definitions.BodyFacade`): origin of reference frame to be set
        
        
        """
        ...
    def setInterpolationDegree(self, int: int) -> None:
        """
            Set the interpolation degree.
        
            Parameters:
                interpolationDegree (int): the interpolation degree to be set
        
        
        """
        ...
    def setInterpolationMethod(self, interpolationMethod: org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod) -> None:
        """
            Set the interpolation method to be used.
        
            Parameters:
                interpolationMethod (:class:`~org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod`): the interpolation method to be set
        
        
        """
        ...
    def setOrbAveraging(self, string: str) -> None:
        """
            Set type of averaging (Osculating, mean Brouwer, other.
        
            Parameters:
                orbAveraging (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): type of averaging (Osculating, mean Brouwer, other).
        
        
        """
        ...
    def setOrbRevNum(self, int: int) -> None:
        """
            Set the integer orbit revolution number.
        
            Parameters:
                orbRevNum (int): integer orbit revolution number
        
        
        """
        ...
    def setOrbRevNumBasis(self, int: int) -> None:
        """
            Set the basis for orbit revolution number.
        
            This specifies if first launch/deployment is on orbit 0 or 1.
        
            Parameters:
                orbRevNumBasis (int): basis for orbit revolution number
        
        
        """
        ...
    def setPropagator(self, string: str) -> None:
        """
            Set the orbit propagator used to generate this trajectory.
        
            Parameters:
                propagator (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): orbit propagator used to generate this trajectory
        
            Since:
                11.2
        
        
        """
        ...
    def setTrajBasis(self, string: str) -> None:
        """
            Set basis of this trajectory state time history data.
        
            Parameters:
                trajBasis (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): basis of this trajectory state time history data
        
        
        """
        ...
    def setTrajBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this trajectory is based.
        
            Parameters:
                trajBasisID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of the orbit determination or simulation upon which this trajectory is based
        
        
        """
        ...
    def setTrajFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`.
        
            Parameters:
                trajFrameEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`
        
        
        """
        ...
    def setTrajID(self, string: str) -> None:
        """
            Set trajectory identification number.
        
            Parameters:
                trajID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): trajectory identification number
        
        
        """
        ...
    def setTrajNextID(self, string: str) -> None:
        """
            Set identification number of next trajectory.
        
            Parameters:
                trajNextID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of next trajectory
        
        
        """
        ...
    def setTrajPrevID(self, string: str) -> None:
        """
            Set identification number of previous trajectory.
        
            Parameters:
                trajPrevID (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): identification number of previous trajectory
        
        
        """
        ...
    def setTrajReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame of the trajectory.
        
            Parameters:
                trajReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setTrajType(self, orbitElementsType: OrbitElementsType) -> None:
        """
            Set trajectory element set type.
        
            Parameters:
                trajType (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitElementsType`): trajectory element set type
        
        
        """
        ...
    def setTrajUnits(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
    def setUseableStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set start of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Parameters:
                useableStartTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def setUseableStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set end of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Parameters:
                useableStopTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
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

class TrajectoryStateHistoryMetadataKey(java.lang.Enum['TrajectoryStateHistoryMetadataKey']):
    """
    public enum TrajectoryStateHistoryMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_PREV_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_NEXT_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_BASIS: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_BASIS_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    INTERPOLATION: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    INTERPOLATION_DEGREE: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    PROPAGATOR: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    CENTER_NAME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_REF_FRAME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_FRAME_EPOCH: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    USEABLE_START_TIME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    USEABLE_STOP_TIME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    ORB_REVNUM: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    ORB_REVNUM_BASIS: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    ORB_AVERAGING: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_TYPE: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_UNITS: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, trajectoryStateHistoryMetadata: TrajectoryStateHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'TrajectoryStateHistoryMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.ocm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['TrajectoryStateHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (TrajectoryStateHistoryMetadataKey c : TrajectoryStateHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm.ocm")``.

    EphemerisOcmWriter: typing.Type[EphemerisOcmWriter]
    ManBasis: typing.Type[ManBasis]
    ManeuverFieldType: typing.Type[ManeuverFieldType]
    ObjectType: typing.Type[ObjectType]
    Ocm: typing.Type[Ocm]
    OcmData: typing.Type[OcmData]
    OcmDataSubStructureKey: typing.Type[OcmDataSubStructureKey]
    OcmElements: typing.Type[OcmElements]
    OcmMetadata: typing.Type[OcmMetadata]
    OcmMetadataKey: typing.Type[OcmMetadataKey]
    OcmParser: typing.Type[OcmParser]
    OcmSatelliteEphemeris: typing.Type[OcmSatelliteEphemeris]
    OcmWriter: typing.Type[OcmWriter]
    OpsStatus: typing.Type[OpsStatus]
    OrbitCategory: typing.Type[OrbitCategory]
    OrbitCovariance: typing.Type[OrbitCovariance]
    OrbitCovarianceHistory: typing.Type[OrbitCovarianceHistory]
    OrbitCovarianceHistoryMetadata: typing.Type[OrbitCovarianceHistoryMetadata]
    OrbitCovarianceHistoryMetadataKey: typing.Type[OrbitCovarianceHistoryMetadataKey]
    OrbitDetermination: typing.Type[OrbitDetermination]
    OrbitDeterminationKey: typing.Type[OrbitDeterminationKey]
    OrbitElementsType: typing.Type[OrbitElementsType]
    OrbitManeuver: typing.Type[OrbitManeuver]
    OrbitManeuverHistory: typing.Type[OrbitManeuverHistory]
    OrbitManeuverHistoryMetadata: typing.Type[OrbitManeuverHistoryMetadata]
    OrbitManeuverHistoryMetadataKey: typing.Type[OrbitManeuverHistoryMetadataKey]
    OrbitPhysicalProperties: typing.Type[OrbitPhysicalProperties]
    OrbitPhysicalPropertiesKey: typing.Type[OrbitPhysicalPropertiesKey]
    Ordering: typing.Type[Ordering]
    Perturbations: typing.Type[Perturbations]
    PerturbationsKey: typing.Type[PerturbationsKey]
    ShadowModel: typing.Type[ShadowModel]
    StreamingOcmWriter: typing.Type[StreamingOcmWriter]
    TrajectoryState: typing.Type[TrajectoryState]
    TrajectoryStateHistory: typing.Type[TrajectoryStateHistory]
    TrajectoryStateHistoryMetadata: typing.Type[TrajectoryStateHistoryMetadata]
    TrajectoryStateHistoryMetadataKey: typing.Type[TrajectoryStateHistoryMetadataKey]
