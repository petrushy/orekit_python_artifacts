
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
    public class AngularVelocity extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for Attitude Parameter Message data lines.
    
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
    def setAngVelX(self, double: float) -> None:
        """
            Set the angular velocity around X axis (rad/s).
        
            Parameters:
                angVelX (double): angular velocity around X axis (rad/s)
        
        
        """
        ...
    def setAngVelY(self, double: float) -> None:
        """
            Set the angular velocity around Y axis (rad/s).
        
            Parameters:
                angVelY (double): angular velocity around Y axis (rad/s)
        
        
        """
        ...
    def setAngVelZ(self, double: float) -> None:
        """
            Set the angular velocity around Z axis (rad/s).
        
            Parameters:
                angVelZ (double): angular velocity around Z axis (rad/s)
        
        
        """
        ...
    def setFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set frame in which angular velocities are specified.
        
            Parameters:
                frame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): frame in which angular velocities are specified
        
        
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

class AngularVelocityKey(java.lang.Enum['AngularVelocityKey']):
    """
    public enum AngularVelocityKey extends :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.AngularVelocityKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.AngularVelocity` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, angularVelocity: AngularVelocity) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.apm.AngularVelocity`): container to fill
        
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
    def valueOf(string: str) -> 'AngularVelocityKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AngularVelocityKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AngularVelocityKey c : AngularVelocityKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Apm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.adm.AdmHeader, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, 'ApmData']]):
    """
    public class Apm extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`, :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmData`>>
    
        This class stores all the information of the Attitude Parameter Message (APM) File parsed by APMParser. It contains the
        header and the metadata and a the data lines.
    
        Since:
            10.2
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ROOT
    
        Root element for XML files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` FORMAT_VERSION_KEY
    
        Key for format version.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, admHeader: org.orekit.files.ccsds.ndm.adm.AdmHeader, list: java.util.List[org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, 'ApmData']], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...
    def getAttitude(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]) -> org.orekit.attitudes.Attitude:
        """
            Get the attitude.
        
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
    public class ApmData extends :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Container for Attitude Parameter Message data.
    
        Since:
            10.2
    """
    def __init__(self, commentsContainer: org.orekit.files.ccsds.section.CommentsContainer, absoluteDate: org.orekit.time.AbsoluteDate, apmQuaternion: 'ApmQuaternion', euler: 'Euler', angularVelocity: AngularVelocity, spinStabilized: 'SpinStabilized', inertia: 'Inertia'): ...
    def addManeuver(self, maneuver: 'Maneuver') -> None:
        """
            Add a maneuver.
        
            Parameters:
                maneuver (:class:`~org.orekit.files.ccsds.ndm.adm.apm.Maneuver`): maneuver to be set
        
        
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
    def getAttitude(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable]) -> org.orekit.attitudes.Attitude:
        """
            Get the attitude.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined, (may be null if attitude is *not* orbit-relative and one
                    wants attitude in the same frame as used in the attitude message)
                pvProvider (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for spacecraft position and velocity (may be null if attitude is *not* orbit-relative)
        
            Returns:
                attitude
        
            Since:
                12.0
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]: ...
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
    public class ApmParser extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmParser`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.Apm`, :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmParser`>
    
        A parser for the CCSDS APM (Attitude Parameter Message).
    
        Since:
            10.2
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, functionArray: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
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
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class ApmQuaternion(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class ApmQuaternion extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for Attitude Parameter Message quaternion logical block.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            10.2
    """
    def __init__(self): ...
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
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class ApmQuaternionKey(java.lang.Enum['ApmQuaternionKey']):
    """
    public enum ApmQuaternionKey extends :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternionKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternion` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, apmQuaternion: ApmQuaternion, dateConsumer: typing.Union[org.orekit.files.ccsds.utils.lexical.ParseToken.DateConsumer, typing.Callable]) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmQuaternion`): container to fill
                epochSetter (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken.DateConsumer`): setter for the epoch (used only in ADM V1 XML files)
        
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
                name (:class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['ApmQuaternionKey']:
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

class ApmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.adm.AdmHeader, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.adm.AdmMetadata, ApmData], Apm]):
    """
    public class ApmWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`, :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmData`>, :class:`~org.orekit.files.ccsds.ndm.adm.apm.Apm`>
    
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

class Euler(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class Euler extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for :class:`~org.orekit.files.ccsds.ndm.adm.apm.Euler` entries.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            10.2
    """
    def __init__(self): ...
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
        
            :meth:`~org.orekit.files.ccsds.ndm.adm.apm.Euler.validate` must have been initialized properly to non-null values before
            this method is called, otherwise :code:`NullPointerException` will be thrown.
        
            Returns:
                true if rates are specified in spacecraft body frame
        
        
        """
        ...
    def rateFrameIsA(self) -> bool:
        """
            Check if rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA`.
        
            Returns:
                true if rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA`
        
        
        """
        ...
    def setEulerRotSeq(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
            Set the rotation order for Euler angles.
        
            Parameters:
                eulerRotSeq (:class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): order to be set
        
        
        """
        ...
    def setInRotationAngles(self, boolean: bool) -> None:
        """
            Set flag for rotation angle parsing.
        
            Parameters:
                inRotationAngles (boolean): if true, we are in the rotationAngles part of XML files
        
        
        """
        ...
    def setIndexedRotationAngle(self, int: int, double: float) -> None:
        """
            Set the Euler angle about axis.
        
            Parameters:
                axis (int): rotation axis
                angle (double): angle to set (rad)
        
            Since:
                12.0
        
        
        """
        ...
    def setIndexedRotationRate(self, int: int, double: float) -> None:
        """
            Set the rate of Euler angle about axis.
        
            Parameters:
                axis (int): rotation axis
                rate (double): angle rate to set (rad/s)
        
            Since:
                12.0
        
        
        """
        ...
    def setLabeledRotationAngle(self, char: str, double: float) -> None:
        """
            Set the Euler angle about axis.
        
            Parameters:
                axis (char): rotation axis
                angle (double): angle to set (rad)
        
        
        """
        ...
    def setLabeledRotationRate(self, char: str, double: float) -> None:
        """
            Set the rate of Euler angle about axis.
        
            Parameters:
                axis (char): rotation axis
                rate (double): angle rate to set (rad/s)
        
        
        """
        ...
    def setRateFrameIsA(self, boolean: bool) -> None:
        """
            Set the frame in which rates are specified.
        
            Parameters:
                rateFrameIsA (boolean): if true, rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA`
        
        
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

class EulerKey(java.lang.Enum['EulerKey']):
    """
    public enum EulerKey extends :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.EulerKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmData` entries.
    
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
                name (:class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['EulerKey']:
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

class Inertia(org.orekit.files.ccsds.ndm.CommonPhysicalProperties):
    """
    public class Inertia extends :class:`~org.orekit.files.ccsds.ndm.CommonPhysicalProperties`
    
        Inertia.
    
        Since:
            12.0
    """
    def __init__(self): ...
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
    def setFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set frame in which inertia is specified.
        
            Parameters:
                frame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): frame in which inertia is specified
        
        
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
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.CommonPhysicalProperties.validate` in
                class :class:`~org.orekit.files.ccsds.ndm.CommonPhysicalProperties`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class InertiaKey(java.lang.Enum['InertiaKey']):
    """
    public enum InertiaKey extends :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.InertiaKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.Inertia` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, inertia: Inertia) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                data (:class:`~org.orekit.files.ccsds.ndm.adm.apm.Inertia`): data to fill
        
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
    def valueOf(string: str) -> 'InertiaKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['InertiaKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (InertiaKey c : InertiaKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Maneuver(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class Maneuver extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Maneuver in an APM file.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            10.2
    """
    def __init__(self): ...
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
    def setDeltaMass(self, double: float) -> None:
        """
            Set mass change during maneuver.
        
            Parameters:
                deltaMass (double): mass change during maneuver (kg)
        
            Since:
                12.0
        
        
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
    def setFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set Coordinate system for the torque vector.
        
            Parameters:
                frame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): coordinate system for the torque vector
        
        
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
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class ManeuverKey(java.lang.Enum['ManeuverKey']):
    """
    public enum ManeuverKey extends :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.ManeuverKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.Maneuver` entries.
    
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
                name (:class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['ManeuverKey']:
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

class SpinStabilized(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class SpinStabilized extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for Attitude Parameter Message data lines.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    
        Since:
            10.2
    """
    def __init__(self): ...
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
    def setMomentumAlpha(self, double: float) -> None:
        """
            Set the right ascension of angular momentum vector (rad).
        
            Parameters:
                momentumAlpha (double): value to be set
        
            Since:
                12.0
        
        
        """
        ...
    def setMomentumDelta(self, double: float) -> None:
        """
            Set the declination of the angular momentum vector (rad).
        
            Parameters:
                momentumDelta (double): value to be set
        
            Since:
                12.0
        
        
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
    def setNutationVel(self, double: float) -> None:
        """
            Set the angular velocity of spin vector around angular momentum vector.
        
            Parameters:
                nutationVel (double): angular velocity of spin vector around angular momentum vector (rad/s)
        
            Since:
                12.0
        
        
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
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate` in
                class :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class SpinStabilizedKey(java.lang.Enum['SpinStabilizedKey']):
    """
    public enum SpinStabilizedKey extends :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.apm.SpinStabilizedKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.apm.SpinStabilized` entries.
    
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
                name (:class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.apm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['SpinStabilizedKey']:
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
