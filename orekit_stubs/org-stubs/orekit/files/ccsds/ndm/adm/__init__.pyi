import java.lang
import java.util
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.adm.aem
import org.orekit.files.ccsds.ndm.adm.apm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import org.xml.sax
import typing



class AdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    public class AdmMetadata extends :class:`~org.orekit.files.ccsds.section.Metadata`
    
        This class gathers the meta-data present in the Attitude Data Message (ADM).
    
        Since:
            10.2
    """
    def __init__(self): ...
    def getCenter(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
            Get the body at origin of reference frame.
        
            Returns:
                the body at origin of reference frame.
        
        
        """
        ...
    def getHasCreatableBody(self) -> bool:
        """
            Get boolean testing whether the body corresponding to the centerName attribute can be created through the
            :class:`~org.orekit.bodies.CelestialBodies`.
        
            Returns:
                true if :class:`~org.orekit.bodies.CelestialBody` can be created from centerName false otherwise
        
        
        """
        ...
    def getLaunchNumber(self) -> int:
        """
            Get the launch number.
        
            Returns:
                launch number
        
        
        """
        ...
    def getLaunchPiece(self) -> str:
        """
            Get the piece of launch.
        
            Returns:
                piece of launch
        
        
        """
        ...
    def getLaunchYear(self) -> int:
        """
            Get the launch year.
        
            Returns:
                launch year
        
        
        """
        ...
    def getObjectID(self) -> str:
        """
            Get the spacecraft ID for which the attitude data are provided.
        
            Returns:
                the spacecraft ID
        
        
        """
        ...
    def getObjectName(self) -> str:
        """
            Get the spacecraft name for which the attitude data are provided.
        
            Returns:
                the spacecraft name
        
        
        """
        ...
    def setCenter(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
            Set the body at origin of reference frame.
        
            Parameters:
                center (:class:`~org.orekit.files.ccsds.definitions.BodyFacade`): body at origin of reference frame
        
        
        """
        ...
    def setObjectID(self, string: str) -> None:
        """
            Set the spacecraft ID for which the attitude data are provided.
        
            Parameters:
                objectID (String): the spacecraft ID to be set
        
        
        """
        ...
    def setObjectName(self, string: str) -> None:
        """
            Set the spacecraft name for which the attitude data are provided.
        
            Parameters:
                objectName (String): the spacecraft name to be set
        
        
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

class AdmMetadataKey(java.lang.Enum['AdmMetadataKey']):
    """
    public enum AdmMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata` entries.
    
        Since:
            11.0
    """
    OBJECT_NAME: typing.ClassVar['AdmMetadataKey'] = ...
    OBJECT_ID: typing.ClassVar['AdmMetadataKey'] = ...
    CENTER_NAME: typing.ClassVar['AdmMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, admMetadata: AdmMetadata) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'AdmMetadataKey':
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
    def values() -> typing.List['AdmMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (AdmMetadataKey c : AdmMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdmMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class AdmMetadataWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for Common metadata for CCSDS Attitude Parameter/Ephemeris Messages.
    
        Since:
            11.0
    """
    def __init__(self, admMetadata: AdmMetadata): ...

_AdmParser__T = typing.TypeVar('_AdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_AdmParser__P = typing.TypeVar('_AdmParser__P', bound=org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser)  # <P>
class AdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[_AdmParser__T, _AdmParser__P], typing.Generic[_AdmParser__T, _AdmParser__P]):
    """
    public abstract class AdmParser<T extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<?,?>,P extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<T,?>> extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<T,P>
    
        Base class for Attitude Data Message parsers.
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            11.0
    """
    def getMissionReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get reference date for Mission Elapsed Time and Mission Relative Time time systems.
        
            Returns:
                the reference date
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]: ...
    @staticmethod
    def processRotationOrder(parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, rotationOrderConsumer: 'AdmParser.RotationOrderConsumer') -> bool:
        """
            Process a CCSDS Euler angles sequence as a null.
        
            Parameters:
                sequence (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): Euler angles sequence token
                consumer (:class:`~org.orekit.files.ccsds.ndm.adm.AdmParser.RotationOrderConsumer`): consumer of the rotation order
        
            Returns:
                always return :code:`true`
        
        
        """
        ...
    class RotationOrderConsumer:
        def accept(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None: ...

class AttitudeEndoints(org.orekit.attitudes.AttitudeBuilder):
    """
    public class AttitudeEndoints extends Object implements :class:`~org.orekit.attitudes.AttitudeBuilder`
    
        Endpoints for attitude definition.
    
        This class provides a bridge between two different views of attitude definition. In both views, there is an external
        frame, based on either celestial body or orbit-relative and there is a spacecraft body frame.
    
          - CCSDS ADM view: frames are labeled as A and B but nothing tells which is which and attitude can be defined in any
            direction
          - :class:`~org.orekit.attitudes.Attitude` view: attitude is always from external to spacecraft body
    
    
        Since:
            11.0
    """
    A2B: typing.ClassVar[str] = ...
    """
    public static final String A2B
    
        Constant for A â†’ B diraction.
    
        Also see:
            :meth:`~constant`
    
    
    """
    B2A: typing.ClassVar[str] = ...
    """
    public static final String B2A
    
        Constant for A â†� B direction.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> org.orekit.attitudes.Attitude:
        """
            Build a filtered attitude.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeBuilder.build` in interface :class:`~org.orekit.attitudes.AttitudeBuilder`
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.PVCoordinatesProvider`): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> org.orekit.attitudes.FieldAttitude[_build_1__T]:
        """
            Build a filtered attitude.
        
            Specified by:
                :meth:`~org.orekit.attitudes.AttitudeBuilder.build` in interface :class:`~org.orekit.attitudes.AttitudeBuilder`
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): reference frame with respect to which attitude must be defined
                pvProv (:class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T> pvProv): provider for spacecraft position and velocity
                rawAttitude (:class:`~org.orekit.utils.TimeStampedFieldAngularCoordinates`<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
            Returns:
                filtered attitude
        
        
        """
        ...
    def checkExternalFrame(self, enum: java.lang.Enum[typing.Any], enum2: java.lang.Enum[typing.Any]) -> None:
        """
            Check external frame is properly initialized.
        
            Parameters:
                aKey (Enum<?> aKey): key for frame A
                bKey (Enum<?> bKey): key for frame B
        
        
        """
        ...
    def checkMandatoryEntriesExceptExternalFrame(self, enum: java.lang.Enum[typing.Any], enum2: java.lang.Enum[typing.Any], enum3: java.lang.Enum[typing.Any]) -> None:
        """
            Check is mandatory entries *except external frame* have been initialized.
        
            Either frame A or frame B must be initialized with a :class:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame`.
        
            This method should throw an exception if some mandatory entry is missing
        
            Parameters:
                aKey (Enum<?> aKey): key for frame A
                bKey (Enum<?> bKey): key for frame B
                dirKey (Enum<?> dirKey): key for direction
        
        
        """
        ...
    def getExternalFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get the external frame.
        
            Returns:
                external frame
        
        
        """
        ...
    def getFrameA(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get frame A.
        
            Returns:
                frame A
        
        
        """
        ...
    def getFrameB(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get frame B.
        
            Returns:
                frame B
        
        
        """
        ...
    def getSpacecraftBodyFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get the spacecraft body frame.
        
            Returns:
                spacecraft body frame
        
        
        """
        ...
    def isA2b(self) -> bool:
        """
            Check if rotation direction is from :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameA` to
            :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameB`.
        
            Returns:
                true if rotation direction is from :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameA` to
                :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameB`
        
        
        """
        ...
    def isCompatibleWith(self, attitudeEndoints: 'AttitudeEndoints') -> bool:
        """
            Check if a endpoint is compatible with another one.
        
            Endpoins are compatible if they refer o the same frame names, in the same order and in the same direction.
        
            Parameters:
                other (:class:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints`): other endpoints to check against
        
            Returns:
                true if both endpoints are compatible with each other
        
        
        """
        ...
    def isExternal2SpacecraftBody(self) -> bool:
        """
            Check if attitude is from external frame to spacecraft body frame.
        
            :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.checkMandatoryEntriesExceptExternalFrame` must have been
            initialized properly to non-null values before this method is called, otherwise :code:`NullPointerException` will be
            thrown.
        
            Returns:
                true if attitude is from external frame to spacecraft body frame
        
        
        """
        ...
    def setA2b(self, boolean: bool) -> None:
        """
            Set rotation direction.
        
            Parameters:
                a2b (boolean): if true, rotation is from :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameA` to
                    :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndoints.getFrameB`
        
        
        """
        ...
    def setFrameA(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set frame A.
        
            Parameters:
                frameA (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): frame A
        
        
        """
        ...
    def setFrameB(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set frame B.
        
            Parameters:
                frameB (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): frame B
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class AttitudeType(java.lang.Enum['AttitudeType']):
    """
    public enum AttitudeType extends Enum<:class:`~org.orekit.files.ccsds.ndm.adm.AttitudeType`>
    
        Enumerate for ADM attitude type.
    
        Since:
            10.2
    """
    QUATERNION: typing.ClassVar['AttitudeType'] = ...
    QUATERNION_DERIVATIVE: typing.ClassVar['AttitudeType'] = ...
    QUATERNION_RATE: typing.ClassVar['AttitudeType'] = ...
    EULER_ANGLE: typing.ClassVar['AttitudeType'] = ...
    EULER_ANGLE_RATE: typing.ClassVar['AttitudeType'] = ...
    SPIN: typing.ClassVar['AttitudeType'] = ...
    SPIN_NUTATION: typing.ClassVar['AttitudeType'] = ...
    def build(self, boolean: bool, boolean2: bool, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, boolean3: bool, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
            Get the angular coordinates corresponding to the attitude data.
        
            Parameters:
                isFirst (boolean): if true the first quaternion component is the scalar component
                isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
                eulerRotSequence (RotationOrder): sequance of Euler angles
                isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
                date (:class:`~org.orekit.time.AbsoluteDate`): entry date
                components (double...): entry components with CCSDS units (i.e. angles *must* still be in degrees here), semantic depends on attitude type
        
            Returns:
                the angular coordinates, using :class:`~org.orekit.attitudes.Attitude` convention (i.e. from inertial frame to
                spacecraft frame)
        
        
        """
        ...
    def createDataFields(self, boolean: bool, boolean2: bool, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, boolean3: bool, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> typing.List[str]:
        """
            Get the attitude data fields corresponding to the attitude type.
        
            This method returns the components in CCSDS units (i.e. degrees, degrees per secondsâ€¦).
        
            Parameters:
                isFirst (boolean): if true the first quaternion component is the scalar component
                isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
                eulerRotSequence (RotationOrder): sequance of Euler angles
                isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
                attitude (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): angular coordinates, using :class:`~org.orekit.attitudes.Attitude` convention (i.e. from inertial frame to spacecraft
                    frame)
        
            Returns:
                the attitude data in CCSDS units
        
        
        """
        ...
    def getAngularDerivativesFilter(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
            Get the angular derivative filter corresponding to the attitude data.
        
            Returns:
                the angular derivative filter corresponding to the attitude data
        
        
        """
        ...
    def parse(self, boolean: bool, boolean2: bool, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, boolean3: bool, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, stringArray: typing.List[str]) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
            Get the angular coordinates corresponding to the attitude data.
        
            This method assumes the text fields are in CCSDS units and will convert to SI units.
        
            Parameters:
                isFirst (boolean): if true the first quaternion component is the scalar component
                isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
                eulerRotSequence (RotationOrder): sequance of Euler angles
                isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                fields (String[]): raw data fields
        
            Returns:
                the angular coordinates, using :class:`~org.orekit.attitudes.Attitude` convention (i.e. from inertial frame to
                spacecraft frame)
        
        
        """
        ...
    @staticmethod
    def parseType(string: str) -> 'AttitudeType':
        """
            Parse an attitude type.
        
            Parameters:
                type (String): unnormalized type name
        
            Returns:
                parsed type
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AttitudeType':
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
    def values() -> typing.List['AttitudeType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (AttitudeType c : AttitudeType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RotationXmlTokenBuilder(org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder):
    """
    public class RotationXmlTokenBuilder extends Object implements :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder`
    
        Builder for rotation angles and rates.
    
        Instances of this class are immutable.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def buildTokens(self, boolean: bool, string: str, string2: str, attributes: org.xml.sax.Attributes, int: int, string3: str) -> java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]: ...

_PythonAdmParser__T = typing.TypeVar('_PythonAdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonAdmParser__P = typing.TypeVar('_PythonAdmParser__P', bound=org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser)  # <P>
class PythonAdmParser(AdmParser[_PythonAdmParser__T, _PythonAdmParser__P], typing.Generic[_PythonAdmParser__T, _PythonAdmParser__P]):
    """
    public class PythonAdmParser<T extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<?,?>,P extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<T,?>> extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmParser`<T,P>
    """
    def build(self) -> _PythonAdmParser__T:
        """
            Build the file from parsed entries.
        
            Returns:
                parsed file
        
        
        """
        ...
    def finalize(self) -> None: ...
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
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.adm")``.

    AdmMetadata: typing.Type[AdmMetadata]
    AdmMetadataKey: typing.Type[AdmMetadataKey]
    AdmMetadataWriter: typing.Type[AdmMetadataWriter]
    AdmParser: typing.Type[AdmParser]
    AttitudeEndoints: typing.Type[AttitudeEndoints]
    AttitudeType: typing.Type[AttitudeType]
    PythonAdmParser: typing.Type[PythonAdmParser]
    RotationXmlTokenBuilder: typing.Type[RotationXmlTokenBuilder]
    aem: org.orekit.files.ccsds.ndm.adm.aem.__module_protocol__
    apm: org.orekit.files.ccsds.ndm.adm.apm.__module_protocol__
