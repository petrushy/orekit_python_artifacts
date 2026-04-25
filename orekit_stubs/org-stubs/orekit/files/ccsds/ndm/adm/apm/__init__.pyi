
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.hipparchus.complex
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.attitudes
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.adm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class AngularVelocity(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for Attitude Parameter Message data lines.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getAngVelX(self) -> float:
        """
        Get the angular velocity around X axis (rad/s).
        
        Returns:
            angular velocity around X axis (rad/s)
        
        
        """
        ...
    def getAngVelY(self) -> float:
        """
        Get the angular velocity around Y axis (rad/s).
        
        Returns:
            angular velocity around Y axis (rad/s)
        
        
        """
        ...
    def getAngVelZ(self) -> float:
        """
        Get the angular velocity around Z axis (rad/s).
        
        Returns:
            angular velocity around Z axis (rad/s)
        
        
        """
        ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints:
        """
        Get the endpoints (i.e. frames A, B and their relationship).
        
        Returns:
            endpoints
        
        
        """
        ...
    def getFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get frame in which angular velocities are specified.
        
        Returns:
            frame in which angular velocities are specified
        
        
        """
        ...
    def setAngVelX(self, angVelX: float) -> None:
        """
        Set the angular velocity around X axis (rad/s).
        
        Parameters:
            angVelX (double): angular velocity around X axis (rad/s)
        
        
        """
        ...
    def setAngVelY(self, angVelY: float) -> None:
        """
        Set the angular velocity around Y axis (rad/s).
        
        Parameters:
            angVelY (double): angular velocity around Y axis (rad/s)
        
        
        """
        ...
    def setAngVelZ(self, angVelZ: float) -> None:
        """
        Set the angular velocity around Z axis (rad/s).
        
        Parameters:
            angVelZ (double): angular velocity around Z axis (rad/s)
        
        
        """
        ...
    def setFrame(self, frame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set frame in which angular velocities are specified.
        
        Parameters:
            frame (FrameFacade): frame in which angular velocities are specified
        
        
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

class AngularVelocityKey(java.lang.Enum['AngularVelocityKey']):
    """
    Keys for AngularVelocity entries.
    
    Since:
        12.0
    """
    COMMENT: typing.ClassVar['AngularVelocityKey'] = ...
    REF_FRAME_A: typing.ClassVar['AngularVelocityKey'] = ...
    REF_FRAME_B: typing.ClassVar['AngularVelocityKey'] = ...
    ANGVEL_FRAME: typing.ClassVar['AngularVelocityKey'] = ...
    ANGVEL_X: typing.ClassVar['AngularVelocityKey'] = ...
    ANGVEL_Y: typing.ClassVar['AngularVelocityKey'] = ...
    ANGVEL_Z: typing.ClassVar['AngularVelocityKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AngularVelocity) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AngularVelocity): container to fill
        
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
    def valueOf(name: str) -> 'AngularVelocityKey':
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
    def values() -> typing.MutableSequence['AngularVelocityKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AngularVelocityKey c : AngularVelocityKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Apm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.adm.AdmHeader, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, 'ApmData']]):
    """
    This class stores all the information of the Attitude Parameter Message (APM) File parsed by APMParser. It contains the header and the metadata and a the data lines.
    
    Since:
        10.2
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
    def __init__(self, header: org.orekit.files.ccsds.ndm.adm.AdmHeader, segments: java.util.List[org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, 'ApmData']], conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext):
        """
        Simple constructor.
        
        Parameters:
            header (AdmHeader): file header
            segments (List<Segment<AdmMetadata, ApmData>>): file segments
            conventions (IERSConventions): IERS conventions
            dataContext (DataContext): used for creating frames, time scales, etc.
        
        
        """
        ...
    def getAttitude(self, frame: org.orekit.frames.Frame, pvProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]) -> org.orekit.attitudes.Attitude:
        """
        Get the attitude.
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined, (may be null if attitude is not orbit-relative and one
                wants attitude in the same frame as used in the attitude message)
            pvProvider (PVCoordinatesProvider): provider for spacecraft position and velocity (may be null if attitude is not orbit-relative)
        
        Returns:
            attitude
        
        
        """
        ...
    def getData(self) -> 'ApmData':
        """
        Get the file data.
        
        Returns:
            file data
        
        
        """
        ...
    def getMetadata(self) -> org.orekit.files.ccsds.ndm.adm.AdmMetadata:
        """
        Get the file metadata.
        
        Returns:
            file metadata
        
        
        """
        ...

class ApmData(org.orekit.files.ccsds.section.Data):
    """
    Container for Attitude Parameter Message data.
    
    Since:
        10.2
    """
    def __init__(self, commentsBlock: org.orekit.files.ccsds.section.CommentsContainer, epoch: org.orekit.time.AbsoluteDate, quaternionBlock: 'ApmQuaternion', eulerBlock: 'Euler', angularVelocityBlock: AngularVelocity, spinStabilizedBlock: 'SpinStabilized', inertia: 'Inertia'):
        """
        Simple constructor.
        
        Parameters:
            commentsBlock (CommentsContainer): general comments block
            epoch (AbsoluteDate): epoch of the data
            quaternionBlock (ApmQuaternion): quaternion logical block (may be null in ADM V2 or later)
            eulerBlock (Euler): Euler angles logicial block (may be null)
            angularVelocityBlock (AngularVelocity): angular velocity block (may be null)
            spinStabilizedBlock (SpinStabilized): spin-stabilized logical block (may be null)
            inertia (Inertia): inertia logical block (may be null)
        
        
        """
        ...
    def addManeuver(self, maneuver: 'Maneuver') -> None:
        """
        Add a maneuver.
        
        Parameters:
            maneuver (Maneuver): maneuver to be set
        
        
        """
        ...
    def getAngularVelocityBlock(self) -> AngularVelocity:
        """
        Get the angular velocity logical block.
        
        Returns:
            angular velocity block (may be null)
        
        Since:
            12.0
        
        
        """
        ...
    def getAttitude(self, frame: org.orekit.frames.Frame, pvProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]) -> org.orekit.attitudes.Attitude:
        """
        Get the attitude.
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined, (may be null if attitude is not orbit-relative and one
                wants attitude in the same frame as used in the attitude message)
            pvProvider (PVCoordinatesProvider): provider for spacecraft position and velocity (may be null if attitude is not orbit-relative)
        
        Returns:
            attitude
        
        Since:
            12.0
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]:
        """
        Get the comments.
        
        Returns:
            comments
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the epoch of the data.
        
        Returns:
            epoch the epoch
        
        Since:
            12.0
        
        
        """
        ...
    def getEulerBlock(self) -> 'Euler':
        """
        Get the Euler angles logical block.
        
        Returns:
            Euler angles block (may be null)
        
        
        """
        ...
    def getInertiaBlock(self) -> 'Inertia':
        """
        Get the inertia logical block.
        
        Returns:
            inertia block (may be null)
        
        
        """
        ...
    def getManeuver(self, index: int) -> 'Maneuver':
        """
        Get a maneuver.
        
        Parameters:
            index (int): maneuver index, counting from 0
        
        Returns:
            maneuver
        
        
        """
        ...
    def getManeuvers(self) -> java.util.List['Maneuver']:
        """
        Get a list of all maneuvers.
        
        Returns:
            unmodifiable list of all maneuvers.
        
        
        """
        ...
    def getNbManeuvers(self) -> int:
        """
        Get the number of maneuvers present in the APM.
        
        Returns:
            the number of maneuvers
        
        
        """
        ...
    def getQuaternionBlock(self) -> 'ApmQuaternion':
        """
        Get the quaternion logical block.
        
        Returns:
            quaternion block
        
        
        """
        ...
    def getSpinStabilizedBlock(self) -> 'SpinStabilized':
        """
        Get the spin-stabilized logical block.
        
        Returns:
            spin-stabilized block (may be null)
        
        
        """
        ...
    def hasManeuvers(self) -> bool:
        """
        Get boolean testing whether the APM contains at least one maneuver.
        
        Returns:
            true if APM contains at least one maneuver false otherwise
        
        
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

class ApmParser(org.orekit.files.ccsds.ndm.adm.AdmParser[Apm, 'ApmParser']):
    """
    A parser for the CCSDS APM (Attitude Parameter Message).
    
    Since:
        10.2
    """
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]):
        """
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildApmParser.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
            dataContext (DataContext): used to retrieve frames, time scales, etc.
            missionReferenceDate (AbsoluteDate): reference date for Mission Elapsed Time or Mission Relative Time time systems (may be null if time system is absolute)
            parsedUnitsBehavior (ParsedUnitsBehavior): behavior to adopt for handling parsed units
            filters (Function<ParseToken, List<ParseToken>>[]): filters to apply to parse tokens
        
        Since:
            12.0
        
        
        """
        ...
    def build(self) -> Apm:
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
    def getHeader(self) -> org.orekit.files.ccsds.ndm.adm.AdmHeader:
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

class ApmQuaternion(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for Attitude Parameter Message quaternion logical block.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        10.2
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints:
        """
        Get the endpoints (i.e. frames A, B and their relationship).
        
        Returns:
            endpoints
        
        
        """
        ...
    def getQuaternion(self) -> org.hipparchus.complex.Quaternion:
        """
        Get the quaternion.
        
        Returns:
            quaternion
        
        
        """
        ...
    def getQuaternionDot(self) -> org.hipparchus.complex.Quaternion:
        """
        Get the quaternion derivative.
        
        Returns:
            quaternion derivative
        
        
        """
        ...
    def hasRates(self) -> bool:
        """
        Check if the logical block includes rates.
        
        Returns:
            true if logical block includes rates
        
        
        """
        ...
    def setQ(self, index: int, value: float) -> None:
        """
        Set quaternion component.
        
        Parameters:
            index (int): component index (0 is scalar part)
            value (double): quaternion component
        
        
        """
        ...
    def setQDot(self, index: int, derivative: float) -> None:
        """
        Set quaternion derivative component.
        
        Parameters:
            index (int): component index (0 is scalar part)
            derivative (double): quaternion derivative component
        
        
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

class ApmQuaternionKey(java.lang.Enum['ApmQuaternionKey']):
    """
    Keys for ApmQuaternion entries.
    
    Since:
        10.2
    """
    quaternion: typing.ClassVar['ApmQuaternionKey'] = ...
    quaternionRate: typing.ClassVar['ApmQuaternionKey'] = ...
    quaternionDot: typing.ClassVar['ApmQuaternionKey'] = ...
    COMMENT: typing.ClassVar['ApmQuaternionKey'] = ...
    EPOCH: typing.ClassVar['ApmQuaternionKey'] = ...
    Q_FRAME_A: typing.ClassVar['ApmQuaternionKey'] = ...
    REF_FRAME_A: typing.ClassVar['ApmQuaternionKey'] = ...
    Q_FRAME_B: typing.ClassVar['ApmQuaternionKey'] = ...
    REF_FRAME_B: typing.ClassVar['ApmQuaternionKey'] = ...
    Q_DIR: typing.ClassVar['ApmQuaternionKey'] = ...
    QC: typing.ClassVar['ApmQuaternionKey'] = ...
    Q1: typing.ClassVar['ApmQuaternionKey'] = ...
    Q2: typing.ClassVar['ApmQuaternionKey'] = ...
    Q3: typing.ClassVar['ApmQuaternionKey'] = ...
    QC_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    Q1_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    Q2_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    Q3_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: ApmQuaternion, epochSetter: typing.Union[org.orekit.files.ccsds.utils.lexical.ParseToken.DateConsumer, typing.Callable]) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (ApmQuaternion): container to fill
            epochSetter (DateConsumer): setter for the epoch (used only in ADM V1 XML files)
        
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
    def valueOf(name: str) -> 'ApmQuaternionKey':
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
    def values() -> typing.MutableSequence['ApmQuaternionKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ApmQuaternionKey c : ApmQuaternionKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ApmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.adm.AdmHeader, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, ApmData], Apm]):
    """
    Writer for CCSDS Orbit Parameter Message.
    
    Since:
        11.0
    """
    CCSDS_APM_VERS: typing.ClassVar[float] = ...
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
    def __init__(self, conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate):
        """
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildApmWriter.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            dataContext (DataContext): used to retrieve frames, time scales, etc.
            missionReferenceDate (AbsoluteDate): reference date for Mission Elapsed Time or Mission Relative Time time systems
        
        
        """
        ...

class Euler(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for Euler entries.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        10.2
    """
    def __init__(self):
        """
        Simple constructor.
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
        Get the rotation order of Euler angles.
        
        Returns:
            rotation order
        
        
        """
        ...
    def getRotationAngles(self) -> typing.MutableSequence[float]:
        """
        Get the coordinates of the Euler angles.
        
        Returns:
            rotation angles (rad)
        
        
        """
        ...
    def getRotationRates(self) -> typing.MutableSequence[float]:
        """
        Get the rates of the Euler angles.
        
        Returns:
            rotation rates (rad/s)
        
        
        """
        ...
    def hasAngles(self) -> bool:
        """
        Check if the logical block includes angles.
        
        This can be false only for ADM V1, as angles are mandatory since ADM V2.
        
        Returns:
            true if logical block includes angles
        
        Since:
            12.0
        
        
        """
        ...
    def hasRates(self) -> bool:
        """
        Check if the logical block includes rates.
        
        Returns:
            true if logical block includes rates
        
        
        """
        ...
    def isSpacecraftBodyRate(self) -> bool:
        """
        Check if rates are specified in spacecraft body frame.
        
        validate must have been initialized properly to non-null values before this method is called, otherwise NullPointerException will be thrown.
        
        Returns:
            true if rates are specified in spacecraft body frame
        
        
        """
        ...
    def rateFrameIsA(self) -> bool:
        """
        Check if rates are specified in getFrameA.
        
        Returns:
            true if rates are specified in getFrameA
        
        
        """
        ...
    def setEulerRotSeq(self, eulerRotSeq: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
        Set the rotation order for Euler angles.
        
        Parameters:
            eulerRotSeq (RotationOrder): order to be set
        
        
        """
        ...
    def setInRotationAngles(self, inRotationAngles: bool) -> None:
        """
        Set flag for rotation angle parsing.
        
        Parameters:
            inRotationAngles (boolean): if true, we are in the rotationAngles part of XML files
        
        
        """
        ...
    def setIndexedRotationAngle(self, axis: int, angle: float) -> None:
        """
        Set the Euler angle about axis.
        
        Parameters:
            axis (int): rotation axis
            angle (double): angle to set (rad)
        
        Since:
            12.0
        
        
        """
        ...
    def setIndexedRotationRate(self, axis: int, rate: float) -> None:
        """
        Set the rate of Euler angle about axis.
        
        Parameters:
            axis (int): rotation axis
            rate (double): angle rate to set (rad/s)
        
        Since:
            12.0
        
        
        """
        ...
    def setLabeledRotationAngle(self, axis: str, angle: float) -> None:
        """
        Set the Euler angle about axis.
        
        Parameters:
            axis (char): rotation axis
            angle (double): angle to set (rad)
        
        
        """
        ...
    def setLabeledRotationRate(self, axis: str, rate: float) -> None:
        """
        Set the rate of Euler angle about axis.
        
        Parameters:
            axis (char): rotation axis
            rate (double): angle rate to set (rad/s)
        
        
        """
        ...
    def setRateFrameIsA(self, rateFrameIsA: bool) -> None:
        """
        Set the frame in which rates are specified.
        
        Parameters:
            rateFrameIsA (boolean): if true, rates are specified in getFrameA
        
        
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

class EulerKey(java.lang.Enum['EulerKey']):
    """
    Keys for ApmData entries.
    
    Since:
        10.2
    """
    rotationAngles: typing.ClassVar['EulerKey'] = ...
    rotationRates: typing.ClassVar['EulerKey'] = ...
    COMMENT: typing.ClassVar['EulerKey'] = ...
    EULER_FRAME_A: typing.ClassVar['EulerKey'] = ...
    REF_FRAME_A: typing.ClassVar['EulerKey'] = ...
    EULER_FRAME_B: typing.ClassVar['EulerKey'] = ...
    REF_FRAME_B: typing.ClassVar['EulerKey'] = ...
    EULER_DIR: typing.ClassVar['EulerKey'] = ...
    EULER_ROT_SEQ: typing.ClassVar['EulerKey'] = ...
    RATE_FRAME: typing.ClassVar['EulerKey'] = ...
    X_ANGLE: typing.ClassVar['EulerKey'] = ...
    Y_ANGLE: typing.ClassVar['EulerKey'] = ...
    Z_ANGLE: typing.ClassVar['EulerKey'] = ...
    X_RATE: typing.ClassVar['EulerKey'] = ...
    Y_RATE: typing.ClassVar['EulerKey'] = ...
    Z_RATE: typing.ClassVar['EulerKey'] = ...
    ANGLE_1: typing.ClassVar['EulerKey'] = ...
    ANGLE_2: typing.ClassVar['EulerKey'] = ...
    ANGLE_3: typing.ClassVar['EulerKey'] = ...
    ANGLE_1_DOT: typing.ClassVar['EulerKey'] = ...
    ANGLE_2_DOT: typing.ClassVar['EulerKey'] = ...
    ANGLE_3_DOT: typing.ClassVar['EulerKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: Euler) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (Euler): container to fill
        
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
    def valueOf(name: str) -> 'EulerKey':
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
    def values() -> typing.MutableSequence['EulerKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (EulerKey c : EulerKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Inertia(org.orekit.files.ccsds.ndm.CommonPhysicalProperties):
    """
    Inertia.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get frame in which inertia is specified.
        
        Returns:
            frame in which inertia is specified
        
        
        """
        ...
    def getInertiaMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the inertia matrix.
        
        Returns:
            the inertia matrix
        
        
        """
        ...
    def setFrame(self, frame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set frame in which inertia is specified.
        
        Parameters:
            frame (FrameFacade): frame in which inertia is specified
        
        
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
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommonPhysicalProperties
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class InertiaKey(java.lang.Enum['InertiaKey']):
    """
    Keys for Inertia entries.
    
    Since:
        12.0
    """
    COMMENT: typing.ClassVar['InertiaKey'] = ...
    INERTIA_REF_FRAME: typing.ClassVar['InertiaKey'] = ...
    I11: typing.ClassVar['InertiaKey'] = ...
    IXX: typing.ClassVar['InertiaKey'] = ...
    I22: typing.ClassVar['InertiaKey'] = ...
    IYY: typing.ClassVar['InertiaKey'] = ...
    I33: typing.ClassVar['InertiaKey'] = ...
    IZZ: typing.ClassVar['InertiaKey'] = ...
    I12: typing.ClassVar['InertiaKey'] = ...
    IXY: typing.ClassVar['InertiaKey'] = ...
    I13: typing.ClassVar['InertiaKey'] = ...
    IXZ: typing.ClassVar['InertiaKey'] = ...
    I23: typing.ClassVar['InertiaKey'] = ...
    IYZ: typing.ClassVar['InertiaKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, data: Inertia) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            data (Inertia): data to fill
        
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
    def valueOf(name: str) -> 'InertiaKey':
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
    def values() -> typing.MutableSequence['InertiaKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (InertiaKey c : InertiaKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Maneuver(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Maneuver in an APM file.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        10.2
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getDeltaMass(self) -> float:
        """
        Get mass change during maneuver.
        
        Returns:
            mass change during maneuver (kg, negative)
        
        Since:
            12.0
        
        
        """
        ...
    def getDuration(self) -> float:
        """
        Get duration (value is 0 for impulsive maneuver).
        
        Returns:
            duration (value is 0 for impulsive maneuver)
        
        
        """
        ...
    def getEpochStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get epoch start.
        
        Returns:
            epoch start
        
        
        """
        ...
    def getFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get Coordinate system for the torque vector.
        
        Returns:
            coordinate system for the torque vector
        
        
        """
        ...
    def getTorque(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the torque vector (N.m).
        
        Returns:
            torque vector
        
        
        """
        ...
    def setDeltaMass(self, deltaMass: float) -> None:
        """
        Set mass change during maneuver.
        
        Parameters:
            deltaMass (double): mass change during maneuver (kg)
        
        Since:
            12.0
        
        
        """
        ...
    def setDuration(self, duration: float) -> None:
        """
        Set duration (value is 0 for impulsive maneuver).
        
        Parameters:
            duration (double): duration (value is 0 for impulsive maneuver)
        
        
        """
        ...
    def setEpochStart(self, epochStart: org.orekit.time.AbsoluteDate) -> None:
        """
        Set epoch start.
        
        Parameters:
            epochStart (AbsoluteDate): epoch start
        
        
        """
        ...
    def setFrame(self, frame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set Coordinate system for the torque vector.
        
        Parameters:
            frame (FrameFacade): coordinate system for the torque vector
        
        
        """
        ...
    def setTorque(self, index: int, value: float) -> None:
        """
        Set the torque vector (N.m).
        
        Parameters:
            index (int): vector component index (counting from 0)
            value (double): component value
        
        
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

class ManeuverKey(java.lang.Enum['ManeuverKey']):
    """
    Keys for Maneuver entries.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['ManeuverKey'] = ...
    MAN_EPOCH_START: typing.ClassVar['ManeuverKey'] = ...
    MAN_DURATION: typing.ClassVar['ManeuverKey'] = ...
    MAN_REF_FRAME: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_1: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_X: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_2: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_Y: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_3: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_Z: typing.ClassVar['ManeuverKey'] = ...
    MAN_DELTA_MASS: typing.ClassVar['ManeuverKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: Maneuver) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (Maneuver): container to fill
        
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
    def valueOf(name: str) -> 'ManeuverKey':
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
    def values() -> typing.MutableSequence['ManeuverKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ManeuverKey c : ManeuverKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SpinStabilized(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for Attitude Parameter Message data lines.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        10.2
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints:
        """
        Get the endpoints (i.e. frames A, B and their relationship).
        
        Returns:
            endpoints
        
        
        """
        ...
    def getMomentumAlpha(self) -> float:
        """
        Get the right ascension of angular momentum vector (rad).
        
        Returns:
            the right ascension of angular momentum vector
        
        Since:
            12.0
        
        
        """
        ...
    def getMomentumDelta(self) -> float:
        """
        Get the declination of the angular momentum vector (rad).
        
        Returns:
            the declination of the angular momentum vector (rad).
        
        Since:
            12.0
        
        
        """
        ...
    def getNutation(self) -> float:
        """
        Get the nutation angle of spin axis (rad).
        
        Returns:
            the nutation angle of spin axis
        
        
        """
        ...
    def getNutationPeriod(self) -> float:
        """
        Get the body nutation period of the spin axis (s).
        
        Returns:
            the body nutation period of the spin axis
        
        
        """
        ...
    def getNutationPhase(self) -> float:
        """
        Get the inertial nutation phase (rad).
        
        Returns:
            the inertial nutation phase
        
        
        """
        ...
    def getNutationVel(self) -> float:
        """
        Get the angular velocity of spin vector around angular momentum vector.
        
        Returns:
            angular velocity of spin vector around angular momentum vector (rad/s)
        
        Since:
            12.0
        
        
        """
        ...
    def getSpinAlpha(self) -> float:
        """
        Get the right ascension of spin axis vector (rad).
        
        Returns:
            the right ascension of spin axis vector
        
        
        """
        ...
    def getSpinAngle(self) -> float:
        """
        Get the phase of the satellite about the spin axis (rad).
        
        Returns:
            the phase of the satellite about the spin axis
        
        
        """
        ...
    def getSpinAngleVel(self) -> float:
        """
        Get the angular velocity of satellite around spin axis (rad/s).
        
        Returns:
            the angular velocity of satellite around spin axis
        
        
        """
        ...
    def getSpinDelta(self) -> float:
        """
        Get the declination of the spin axis vector (rad).
        
        Returns:
            the declination of the spin axis vector (rad).
        
        
        """
        ...
    def hasMomentum(self) -> bool:
        """
        Check if the logical block includes momentum.
        
        Returns:
            true if logical block includes momentum
        
        Since:
            12.0
        
        
        """
        ...
    def hasNutation(self) -> bool:
        """
        Check if the logical block includes nutation.
        
        Returns:
            true if logical block includes nutation
        
        Since:
            12.0
        
        
        """
        ...
    def setMomentumAlpha(self, momentumAlpha: float) -> None:
        """
        Set the right ascension of angular momentum vector (rad).
        
        Parameters:
            momentumAlpha (double): value to be set
        
        Since:
            12.0
        
        
        """
        ...
    def setMomentumDelta(self, momentumDelta: float) -> None:
        """
        Set the declination of the angular momentum vector (rad).
        
        Parameters:
            momentumDelta (double): value to be set
        
        Since:
            12.0
        
        
        """
        ...
    def setNutation(self, nutation: float) -> None:
        """
        Set the nutation angle of spin axis (rad).
        
        Parameters:
            nutation (double): the nutation angle to be set
        
        
        """
        ...
    def setNutationPeriod(self, period: float) -> None:
        """
        Set the body nutation period of the spin axis (s).
        
        Parameters:
            period (double): the nutation period to be set
        
        
        """
        ...
    def setNutationPhase(self, nutationPhase: float) -> None:
        """
        Set the inertial nutation phase (rad).
        
        Parameters:
            nutationPhase (double): the nutation phase to be set
        
        
        """
        ...
    def setNutationVel(self, nutationVel: float) -> None:
        """
        Set the angular velocity of spin vector around angular momentum vector.
        
        Parameters:
            nutationVel (double): angular velocity of spin vector around angular momentum vector (rad/s)
        
        Since:
            12.0
        
        
        """
        ...
    def setSpinAlpha(self, spinAlpha: float) -> None:
        """
        Set the right ascension of spin axis vector (rad).
        
        Parameters:
            spinAlpha (double): value to be set
        
        
        """
        ...
    def setSpinAngle(self, spinAngle: float) -> None:
        """
        Set the phase of the satellite about the spin axis (rad).
        
        Parameters:
            spinAngle (double): value to be set
        
        
        """
        ...
    def setSpinAngleVel(self, spinAngleVel: float) -> None:
        """
        Set the angular velocity of satellite around spin axis (rad/s).
        
        Parameters:
            spinAngleVel (double): value to be set
        
        
        """
        ...
    def setSpinDelta(self, spinDelta: float) -> None:
        """
        Set the declination of the spin axis vector (rad).
        
        Parameters:
            spinDelta (double): value to be set
        
        
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

class SpinStabilizedKey(java.lang.Enum['SpinStabilizedKey']):
    """
    Keys for SpinStabilized entries.
    
    Since:
        10.2
    """
    COMMENT: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_FRAME_A: typing.ClassVar['SpinStabilizedKey'] = ...
    REF_FRAME_A: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_FRAME_B: typing.ClassVar['SpinStabilizedKey'] = ...
    REF_FRAME_B: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_DIR: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_ALPHA: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_DELTA: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_ANGLE: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_ANGLE_VEL: typing.ClassVar['SpinStabilizedKey'] = ...
    NUTATION: typing.ClassVar['SpinStabilizedKey'] = ...
    NUTATION_PER: typing.ClassVar['SpinStabilizedKey'] = ...
    NUTATION_PHASE: typing.ClassVar['SpinStabilizedKey'] = ...
    MOMENTUM_ALPHA: typing.ClassVar['SpinStabilizedKey'] = ...
    MOMENTUM_DELTA: typing.ClassVar['SpinStabilizedKey'] = ...
    NUTATION_VEL: typing.ClassVar['SpinStabilizedKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: SpinStabilized) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (SpinStabilized): container to fill
        
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
    def valueOf(name: str) -> 'SpinStabilizedKey':
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
    def values() -> typing.MutableSequence['SpinStabilizedKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SpinStabilizedKey c : SpinStabilizedKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.adm.apm")``.

    AngularVelocity: typing.Type[AngularVelocity]
    AngularVelocityKey: typing.Type[AngularVelocityKey]
    Apm: typing.Type[Apm]
    ApmData: typing.Type[ApmData]
    ApmParser: typing.Type[ApmParser]
    ApmQuaternion: typing.Type[ApmQuaternion]
    ApmQuaternionKey: typing.Type[ApmQuaternionKey]
    ApmWriter: typing.Type[ApmWriter]
    Euler: typing.Type[Euler]
    EulerKey: typing.Type[EulerKey]
    Inertia: typing.Type[Inertia]
    InertiaKey: typing.Type[InertiaKey]
    Maneuver: typing.Type[Maneuver]
    ManeuverKey: typing.Type[ManeuverKey]
    SpinStabilized: typing.Type[SpinStabilized]
    SpinStabilizedKey: typing.Type[SpinStabilizedKey]
