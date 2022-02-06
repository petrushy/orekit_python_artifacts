import java.lang
import java.util
import org.hipparchus.complex
import org.hipparchus.geometry.euclidean.threed
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



class Apm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, 'ApmData']]):
    """
    public class Apm extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.section.Header`,:class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`,:class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmData`>>
    
        This class stores all the information of the Attitude Parameter Message (APM) File parsed by APMParser. It contains the
        header and the metadata and a the data lines.
    
        Since:
            10.2
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
    def __init__(self, header: org.orekit.files.ccsds.section.Header, list: java.util.List[org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, 'ApmData']], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...
    def getAttitude(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider) -> org.orekit.attitudes.Attitude:
        """
            Get the attitude.
        
            The orientation part of the attitude is always extracted from the file mandatory
            :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternion`. The rotation rate part of the attitude is extracted from the
            :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternion` if rate is available there, or from the
            :class:`~org.orekit.files.ccsds.ndm.adm.apm.Euler` if rate is missing from quaternion logical block but available in
            Euler logical block.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined, (may be null if attitude is *not* orbit-relative and one
                    wants attitude in the same frame as used in the attitude message)
                pvProvider (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for spacecraft position and velocity (may be null if attitude is *not* orbit-relative)
        
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
    public class ApmData extends Object implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Container for Attitude Parameter Message data.
    
        Since:
            10.2
    """
    def __init__(self, commentsContainer: org.orekit.files.ccsds.section.CommentsContainer, apmQuaternion: 'ApmQuaternion', euler: 'Euler', spinStabilized: 'SpinStabilized', spacecraftParameters: 'SpacecraftParameters'): ...
    def addManeuver(self, maneuver: 'Maneuver') -> None:
        """
            Add a maneuver.
        
            Parameters:
                maneuver (:class:`~org.orekit.files.ccsds.ndm.adm.apm.Maneuver`): maneuver to be set
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]:
        """
            Get the comments.
        
            Returns:
                comments
        
        
        """
        ...
    def getEulerBlock(self) -> 'Euler':
        """
            Get the Euler angles logical block.
        
            Returns:
                Euler angles block (may be null)
        
        
        """
        ...
    def getManeuver(self, int: int) -> 'Maneuver':
        """
            Get a maneuver.
        
            Parameters:
                index (int): maneuver index, counting from 0
        
            Returns:
                maneuver
        
        
        """
        ...
    def getManeuvers(self) -> java.util.List['Maneuver']: ...
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
    def getSpacecraftParametersBlock(self) -> 'SpacecraftParameters':
        """
            Get the spacecraft parameters logical block.
        
            Returns:
                spacecraft parameters block (may be null)
        
        
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

class ApmParser(org.orekit.files.ccsds.ndm.adm.AdmParser[Apm, 'ApmParser']):
    """
    public class ApmParser extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmParser`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.Apm`,:class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmParser`>
    
        A parser for the CCSDS APM (Attitude Parameter Message).
    
        Since:
            10.2
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior): ...
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

class ApmQuaternion(org.orekit.files.ccsds.section.Section):
    """
    public class ApmQuaternion extends Object implements :class:`~org.orekit.files.ccsds.section.Section`
    
        Container for Attitude Parameter Message quaternion logical block.
    
        Since:
            10.2
    """
    def __init__(self): ...
    def getAttitude(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider) -> org.orekit.attitudes.Attitude:
        """
            Get the attitude.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined (may be null if attitude is *not* orbit-relative and one
                    wants attitude in the same frame as used in the attitude message)
                pvProvider (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for spacecraft position and velocity (may be null if attitude is *not* orbit-relative)
        
            Returns:
                attitude
        
        
        """
        ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndoints:
        """
            Get the endpoints (i.e. frames A, B and their relationship).
        
            Returns:
                endpoints
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the epoch of the data.
        
            Returns:
                epoch the epoch
        
        
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
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the epoch of the data.
        
            Parameters:
                epoch (:class:`~org.orekit.time.AbsoluteDate`): the epoch to be set
        
        
        """
        ...
    def setQ(self, int: int, double: float) -> None:
        """
            Set quaternion component.
        
            Parameters:
                index (int): component index (0 is scalar part)
                value (double): quaternion component
        
        
        """
        ...
    def setQDot(self, int: int, double: float) -> None:
        """
            Set quaternion derivative component.
        
            Parameters:
                index (int): component index (0 is scalar part)
                derivative (double): quaternion derivative component
        
        
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

class ApmQuaternionKey(java.lang.Enum['ApmQuaternionKey']):
    """
    public enum ApmQuaternionKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternionKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternion` entries.
    
        Since:
            10.2
    """
    quaternion: typing.ClassVar['ApmQuaternionKey'] = ...
    quaternionRate: typing.ClassVar['ApmQuaternionKey'] = ...
    EPOCH: typing.ClassVar['ApmQuaternionKey'] = ...
    Q_FRAME_A: typing.ClassVar['ApmQuaternionKey'] = ...
    Q_FRAME_B: typing.ClassVar['ApmQuaternionKey'] = ...
    Q_DIR: typing.ClassVar['ApmQuaternionKey'] = ...
    QC: typing.ClassVar['ApmQuaternionKey'] = ...
    Q1: typing.ClassVar['ApmQuaternionKey'] = ...
    Q2: typing.ClassVar['ApmQuaternionKey'] = ...
    Q3: typing.ClassVar['ApmQuaternionKey'] = ...
    QC_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    Q1_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    Q2_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    Q3_DOT: typing.ClassVar['ApmQuaternionKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, apmQuaternion: ApmQuaternion) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternion`): container to fill
        
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
    def valueOf(string: str) -> 'ApmQuaternionKey':
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
    def values() -> typing.List['ApmQuaternionKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ApmQuaternionKey c : ApmQuaternionKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ApmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, ApmData], Apm]):
    """
    public class ApmWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.section.Header`,:class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`,:class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmData`>,:class:`~org.orekit.files.ccsds.ndm.adm.apm.Apm`>
    
        Writer for CCSDS Orbit Parameter Message.
    
        Since:
            11.0
    """
    CCSDS_APM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_APM_VERS
    
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
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate): ...
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, segment: org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, ApmData]) -> None: ...

class Euler(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class Euler extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for :class:`~org.orekit.files.ccsds.ndm.adm.apm.Euler` entries.
    
        Since:
            10.2
    """
    def __init__(self): ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndoints:
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
    def getRotationAngles(self) -> typing.List[float]:
        """
            Get the coordinates of the Euler angles (rad).
        
            Returns:
                rotation angles
        
        
        """
        ...
    def getRotationRates(self) -> typing.List[float]:
        """
            Get the rates of the Euler angles (rad/s).
        
            Returns:
                rotation rates
        
        
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
        
            :meth:`~org.orekit.files.ccsds.ndm.adm.apm.Euler.validate` must have been initialized properly to non-null values before
            this method is called, otherwise :code:`NullPointerException` will be thrown.
        
            Returns:
                true if rates are specified in spacecraft body frame
        
        
        """
        ...
    def rateFrameIsA(self) -> bool:
        """
            Check if rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameA`.
        
            Returns:
                true if rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameA`
        
        
        """
        ...
    def setEulerRotSeq(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
            Set the rotation order for Euler angles.
        
            Parameters:
                eulerRotSeq (RotationOrder): order to be set
        
        
        """
        ...
    def setInRotationAngles(self, boolean: bool) -> None:
        """
            Set flag for rotation angle parsing.
        
            Parameters:
                inRotationAngles (boolean): if true, we are in the rotationAngles part of XML files
        
        
        """
        ...
    def setRateFrameIsA(self, boolean: bool) -> None:
        """
            Set the frame in which rates are specified.
        
            Parameters:
                rateFrameIsA (boolean): if true, rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameA`
        
        
        """
        ...
    def setRotationAngle(self, char: str, double: float) -> None:
        """
            Set the Euler angle about (rad).
        
            Parameters:
                axis (char): rotation axis
                angle (double): angle to set
        
        
        """
        ...
    def setRotationRate(self, char: str, double: float) -> None:
        """
            Set the rate of Euler angle (rad/s).
        
            Parameters:
                axis (char): rotation axis
                rate (double): angle rate to set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class EulerKey(java.lang.Enum['EulerKey']):
    """
    public enum EulerKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.adm.apm.EulerKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmData` entries.
    
        Since:
            10.2
    """
    rotationAngles: typing.ClassVar['EulerKey'] = ...
    rotationRates: typing.ClassVar['EulerKey'] = ...
    COMMENT: typing.ClassVar['EulerKey'] = ...
    EULER_FRAME_A: typing.ClassVar['EulerKey'] = ...
    EULER_FRAME_B: typing.ClassVar['EulerKey'] = ...
    EULER_DIR: typing.ClassVar['EulerKey'] = ...
    EULER_ROT_SEQ: typing.ClassVar['EulerKey'] = ...
    RATE_FRAME: typing.ClassVar['EulerKey'] = ...
    X_ANGLE: typing.ClassVar['EulerKey'] = ...
    Y_ANGLE: typing.ClassVar['EulerKey'] = ...
    Z_ANGLE: typing.ClassVar['EulerKey'] = ...
    X_RATE: typing.ClassVar['EulerKey'] = ...
    Y_RATE: typing.ClassVar['EulerKey'] = ...
    Z_RATE: typing.ClassVar['EulerKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, euler: Euler) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.apm.Euler`): container to fill
        
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
    def valueOf(string: str) -> 'EulerKey':
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
    def values() -> typing.List['EulerKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (EulerKey c : EulerKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Maneuver(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class Maneuver extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Maneuver in an APM file.
    
        Since:
            10.2
    """
    def __init__(self): ...
    def completed(self) -> bool:
        """
            Check if maneuver has been completed.
        
            Returns:
                true if maneuver has been completed
        
        
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
    def getRefFrameString(self) -> str:
        """
            Get Coordinate system for the torque vector, for absolute frames.
        
            Returns:
                coordinate system for the torque vector, for absolute frames
        
        
        """
        ...
    def getTorque(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the torque vector (N.m).
        
            Returns:
                torque vector
        
        
        """
        ...
    def setDuration(self, double: float) -> None:
        """
            Set duration (value is 0 for impulsive maneuver).
        
            Parameters:
                duration (double): duration (value is 0 for impulsive maneuver)
        
        
        """
        ...
    def setEpochStart(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch start.
        
            Parameters:
                epochStart (:class:`~org.orekit.time.AbsoluteDate`): epoch start
        
        
        """
        ...
    def setRefFrameString(self, string: str) -> None:
        """
            Set Coordinate system for the torque vector, for absolute frames.
        
            Parameters:
                refFrameString (String): coordinate system for the torque vector, for absolute frames
        
        
        """
        ...
    def setTorque(self, int: int, double: float) -> None:
        """
            Set the torque vector (N.m).
        
            Parameters:
                index (int): vector component index (counting from 0)
                value (double): component value
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class ManeuverKey(java.lang.Enum['ManeuverKey']):
    """
    public enum ManeuverKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.adm.apm.ManeuverKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.Maneuver` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['ManeuverKey'] = ...
    MAN_EPOCH_START: typing.ClassVar['ManeuverKey'] = ...
    MAN_DURATION: typing.ClassVar['ManeuverKey'] = ...
    MAN_REF_FRAME: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_1: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_2: typing.ClassVar['ManeuverKey'] = ...
    MAN_TOR_3: typing.ClassVar['ManeuverKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, maneuver: Maneuver) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.apm.Maneuver`): container to fill
        
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
    def valueOf(string: str) -> 'ManeuverKey':
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
    def values() -> typing.List['ManeuverKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ManeuverKey c : ManeuverKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SpacecraftParameters(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class SpacecraftParameters extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for spacecraft parameters data.
    
        Since:
            10.2
    """
    def __init__(self): ...
    def getI11(self) -> float:
        """
            Get the moment of Inertia about the 1-axis (N.mÂ²).
        
            Returns:
                the moment of Inertia about the 1-axis.
        
        
        """
        ...
    def getI12(self) -> float:
        """
            Get the moment of Inertia about the 1 and 2 axes (N.mÂ²).
        
            Returns:
                the moment of Inertia about the 1 and 2 axes.
        
        
        """
        ...
    def getI13(self) -> float:
        """
            Get the moment of Inertia about the 1 and 3 axes (N.mÂ²).
        
            Returns:
                the moment of Inertia about the 1 and 3 axes.
        
        
        """
        ...
    def getI22(self) -> float:
        """
            Get the moment of Inertia about the 2-axis (N.mÂ²).
        
            Returns:
                the moment of Inertia about the 2-axis.
        
        
        """
        ...
    def getI23(self) -> float:
        """
            Get the moment of Inertia about the 2 and 3 axes (N.mÂ²).
        
            Returns:
                the moment of Inertia about the 2 and 3 axes.
        
        
        """
        ...
    def getI33(self) -> float:
        """
            Get the moment of Inertia about the 3-axis (N.mÂ²).
        
            Returns:
                the moment of Inertia about the 3-axis.
        
        
        """
        ...
    def getInertiaReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get the coordinate system for the inertia tensor.
        
            Returns:
                the coordinate system for the inertia tensor
        
        
        """
        ...
    def setI11(self, double: float) -> None:
        """
            Set the moment of Inertia about the 1-axis (N.mÂ²).
        
            Parameters:
                i11 (double): moment of Inertia about the 1-axis
        
        
        """
        ...
    def setI12(self, double: float) -> None:
        """
            Set the moment of Inertia about the 1 and 2 axes (N.mÂ²).
        
            Parameters:
                i12 (double): moment of Inertia about the 1 and 2 axes
        
        
        """
        ...
    def setI13(self, double: float) -> None:
        """
            Set the moment of Inertia about the 1 and 3 axes (N.mÂ²).
        
            Parameters:
                i13 (double): moment of Inertia about the 1 and 3 axes
        
        
        """
        ...
    def setI22(self, double: float) -> None:
        """
            Set the moment of Inertia about the 2-axis (N.mÂ²).
        
            Parameters:
                i22 (double): moment of Inertia about the 2-axis
        
        
        """
        ...
    def setI23(self, double: float) -> None:
        """
            Set the moment of Inertia about the 2 and 3 axes (N.mÂ²).
        
            Parameters:
                i23 (double): moment of Inertia about the 2 and 3 axes
        
        
        """
        ...
    def setI33(self, double: float) -> None:
        """
            Set the moment of Inertia about the 3-axis (N.mÂ²).
        
            Parameters:
                i33 (double): moment of Inertia about the 3-axis
        
        
        """
        ...
    def setInertiaReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set the coordinate system for the inertia tensor.
        
            Parameters:
                inertiaReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): frame to be set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class SpacecraftParametersKey(java.lang.Enum['SpacecraftParametersKey']):
    """
    public enum SpacecraftParametersKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.adm.apm.SpacecraftParametersKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.SpacecraftParameters` entries.
    
        Since:
            10.2
    """
    COMMENT: typing.ClassVar['SpacecraftParametersKey'] = ...
    INERTIA_REF_FRAME: typing.ClassVar['SpacecraftParametersKey'] = ...
    I11: typing.ClassVar['SpacecraftParametersKey'] = ...
    I22: typing.ClassVar['SpacecraftParametersKey'] = ...
    I33: typing.ClassVar['SpacecraftParametersKey'] = ...
    I12: typing.ClassVar['SpacecraftParametersKey'] = ...
    I13: typing.ClassVar['SpacecraftParametersKey'] = ...
    I23: typing.ClassVar['SpacecraftParametersKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, spacecraftParameters: SpacecraftParameters) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.apm.SpacecraftParameters`): container to fill
        
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
    def valueOf(string: str) -> 'SpacecraftParametersKey':
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
    def values() -> typing.List['SpacecraftParametersKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (SpacecraftParametersKey c : SpacecraftParametersKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SpinStabilized(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class SpinStabilized extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for Attitude Parameter Message data lines.
    
        Since:
            10.2
    """
    def __init__(self): ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndoints:
        """
            Get the endpoints (i.e. frames A, B and their relationship).
        
            Returns:
                endpoints
        
        
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
    def setNutation(self, double: float) -> None:
        """
            Set the nutation angle of spin axis (rad).
        
            Parameters:
                nutation (double): the nutation angle to be set
        
        
        """
        ...
    def setNutationPeriod(self, double: float) -> None:
        """
            Set the body nutation period of the spin axis (s).
        
            Parameters:
                period (double): the nutation period to be set
        
        
        """
        ...
    def setNutationPhase(self, double: float) -> None:
        """
            Set the inertial nutation phase (rad).
        
            Parameters:
                nutationPhase (double): the nutation phase to be set
        
        
        """
        ...
    def setSpinAlpha(self, double: float) -> None:
        """
            Set the right ascension of spin axis vector (rad).
        
            Parameters:
                spinAlpha (double): value to be set
        
        
        """
        ...
    def setSpinAngle(self, double: float) -> None:
        """
            Set the phase of the satellite about the spin axis (rad).
        
            Parameters:
                spinAngle (double): value to be set
        
        
        """
        ...
    def setSpinAngleVel(self, double: float) -> None:
        """
            Set the angular velocity of satellite around spin axis (rad/s).
        
            Parameters:
                spinAngleVel (double): value to be set
        
        
        """
        ...
    def setSpinDelta(self, double: float) -> None:
        """
            Set the declination of the spin axis vector (rad).
        
            Parameters:
                spinDelta (double): value to be set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class SpinStabilizedKey(java.lang.Enum['SpinStabilizedKey']):
    """
    public enum SpinStabilizedKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.adm.apm.SpinStabilizedKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.SpinStabilized` entries.
    
        Since:
            10.2
    """
    COMMENT: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_FRAME_A: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_FRAME_B: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_DIR: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_ALPHA: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_DELTA: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_ANGLE: typing.ClassVar['SpinStabilizedKey'] = ...
    SPIN_ANGLE_VEL: typing.ClassVar['SpinStabilizedKey'] = ...
    NUTATION: typing.ClassVar['SpinStabilizedKey'] = ...
    NUTATION_PER: typing.ClassVar['SpinStabilizedKey'] = ...
    NUTATION_PHASE: typing.ClassVar['SpinStabilizedKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, spinStabilized: SpinStabilized) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.apm.SpinStabilized`): container to fill
        
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
    def valueOf(string: str) -> 'SpinStabilizedKey':
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
    def values() -> typing.List['SpinStabilizedKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (SpinStabilizedKey c : SpinStabilizedKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.adm.apm")``.

    Apm: typing.Type[Apm]
    ApmData: typing.Type[ApmData]
    ApmParser: typing.Type[ApmParser]
    ApmQuaternion: typing.Type[ApmQuaternion]
    ApmQuaternionKey: typing.Type[ApmQuaternionKey]
    ApmWriter: typing.Type[ApmWriter]
    Euler: typing.Type[Euler]
    EulerKey: typing.Type[EulerKey]
    Maneuver: typing.Type[Maneuver]
    ManeuverKey: typing.Type[ManeuverKey]
    SpacecraftParameters: typing.Type[SpacecraftParameters]
    SpacecraftParametersKey: typing.Type[SpacecraftParametersKey]
    SpinStabilized: typing.Type[SpinStabilized]
    SpinStabilizedKey: typing.Type[SpinStabilizedKey]
