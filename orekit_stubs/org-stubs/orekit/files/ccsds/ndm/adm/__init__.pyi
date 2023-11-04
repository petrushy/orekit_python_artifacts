import java.lang
import java.util
import java.util.function
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.adm.acm
import org.orekit.files.ccsds.ndm.adm.aem
import org.orekit.files.ccsds.ndm.adm.apm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class AdmCommonMetadataKey(java.lang.Enum['AdmCommonMetadataKey']):
    """
    public enum AdmCommonMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmCommonMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata` entries.
    
        Since:
            12.0
    """
    OBJECT_ID: typing.ClassVar['AdmCommonMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, admMetadata: 'AdmMetadata') -> bool:
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
    def valueOf(string: str) -> 'AdmCommonMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['AdmCommonMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AdmCommonMetadataKey c : AdmCommonMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdmCommonMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class AdmCommonMetadataWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for Common metadata for CCSDS Attitude Parameter/Ephemeris Messages.
    
        Since:
            11.0
    """
    def __init__(self, admMetadata: 'AdmMetadata'): ...

class AdmHeader(org.orekit.files.ccsds.section.Header):
    """
    public class AdmHeader extends :class:`~org.orekit.files.ccsds.section.Header`
    
        Header of a CCSDS Attitude Data Message.
    
        Since:
            12.0
    """
    def __init__(self): ...

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
                objectID (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the spacecraft ID to be set
        
        
        """
        ...
    def setObjectName(self, string: str) -> None:
        """
            Set the spacecraft name for which the attitude data are provided.
        
            Parameters:
                objectName (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the spacecraft name to be set
        
        
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
    public enum AdmMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata` entries.
    
        Since:
            11.0
    """
    OBJECT_NAME: typing.ClassVar['AdmMetadataKey'] = ...
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
                name (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
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

_AdmParser__T = typing.TypeVar('_AdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_AdmParser__P = typing.TypeVar('_AdmParser__P', bound=org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser)  # <P>
class AdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[AdmHeader, _AdmParser__T, _AdmParser__P], typing.Generic[_AdmParser__T, _AdmParser__P]):
    """
    public abstract class AdmParser<T extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, ?>, P extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, T, ?>> extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, T, P>
    
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

class AttitudeEndpoints(org.orekit.attitudes.AttitudeBuilder):
    """
    public class AttitudeEndpoints extends :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.attitudes.AttitudeBuilder`
    
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
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` A2B
    
        Constant for A → B diraction.
    
        Also see:
            :meth:`~constant`
    
    
    """
    B2A: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` B2A
    
        Constant for A ← B direction.
    
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
                aKey (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<?> aKey): key for frame A
                bKey (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<?> bKey): key for frame B
        
        
        """
        ...
    def checkMandatoryEntriesExceptExternalFrame(self, double: float, enum: java.lang.Enum[typing.Any], enum2: java.lang.Enum[typing.Any], enum3: java.lang.Enum[typing.Any]) -> None:
        """
            Check is mandatory entries *except external frame* have been initialized.
        
            Either frame A or frame B must be initialized with a :class:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame`.
        
            This method should throw an exception if some mandatory entry is missing
        
            Parameters:
                version (double): format version
                aKey (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<?> aKey): key for frame A
                bKey (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<?> bKey): key for frame B
                dirKey (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<?> dirKey): key for direction
        
        
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
            Check if rotation direction is from :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA` to
            :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameB`.
        
            Returns:
                true if rotation direction is from :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA` to
                :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameB`
        
        
        """
        ...
    def isCompatibleWith(self, attitudeEndpoints: 'AttitudeEndpoints') -> bool:
        """
            Check if a endpoint is compatible with another one.
        
            Endpoins are compatible if they refer o the same frame names, in the same order and in the same direction.
        
            Parameters:
                other (:class:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints`): other endpoints to check against
        
            Returns:
                true if both endpoints are compatible with each other
        
        
        """
        ...
    def isExternal2SpacecraftBody(self) -> bool:
        """
            Check if attitude is from external frame to spacecraft body frame.
        
            :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.checkMandatoryEntriesExceptExternalFrame` must have been
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
                a2b (boolean): if true, rotation is from :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA` to
                    :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameB`
        
        
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
                :meth:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...

class AttitudeType(java.lang.Enum['AttitudeType']):
    """
    public enum AttitudeType extends :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.AttitudeType`>
    
        Enumerate for ADM attitude type.
    
        Since:
            10.2
    """
    QUATERNION: typing.ClassVar['AttitudeType'] = ...
    QUATERNION_DERIVATIVE: typing.ClassVar['AttitudeType'] = ...
    QUATERNION_EULER_RATES: typing.ClassVar['AttitudeType'] = ...
    QUATERNION_ANGVEL: typing.ClassVar['AttitudeType'] = ...
    EULER_ANGLE: typing.ClassVar['AttitudeType'] = ...
    EULER_ANGLE_DERIVATIVE: typing.ClassVar['AttitudeType'] = ...
    EULER_ANGLE_ANGVEL: typing.ClassVar['AttitudeType'] = ...
    SPIN: typing.ClassVar['AttitudeType'] = ...
    SPIN_NUTATION: typing.ClassVar['AttitudeType'] = ...
    SPIN_NUTATION_MOMENTUM: typing.ClassVar['AttitudeType'] = ...
    def build(self, boolean: bool, boolean2: bool, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, boolean3: bool, absoluteDate: org.orekit.time.AbsoluteDate, *double: float) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
            Get the angular coordinates corresponding to the attitude data.
        
            Parameters:
                isFirst (boolean): if true the first quaternion component is the scalar component
                isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
                eulerRotSequence (:class:`~org.orekit.files.ccsds.ndm.adm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): sequance of Euler angles
                isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
                date (:class:`~org.orekit.time.AbsoluteDate`): entry date
                components (double...): entry components with SI units, semantic depends on attitude type
        
            Returns:
                the angular coordinates, using :class:`~org.orekit.attitudes.Attitude` convention (i.e. from inertial frame to
                spacecraft frame)
        
        
        """
        ...
    def createDataFields(self, boolean: bool, boolean2: bool, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, boolean3: bool, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> typing.List[str]:
        """
            Get the attitude data fields corresponding to the attitude type.
        
            This method returns the components in CCSDS units (i.e. degrees, degrees per seconds…).
        
            Parameters:
                isFirst (boolean): if true the first quaternion component is the scalar component
                isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
                eulerRotSequence (:class:`~org.orekit.files.ccsds.ndm.adm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): sequance of Euler angles
                isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
                attitude (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): angular coordinates, using :class:`~org.orekit.attitudes.Attitude` convention (i.e. from inertial frame to spacecraft
                    frame)
        
            Returns:
                the attitude data in CCSDS units
        
        
        """
        ...
    def generateData(self, boolean: bool, boolean2: bool, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, boolean3: bool, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> typing.List[float]:
        """
            Generate the attitude data corresponding to the attitude type.
        
            This method returns the components in SI units.
        
            Parameters:
                isFirst (boolean): if true the first quaternion component is the scalar component
                isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
                eulerRotSequence (:class:`~org.orekit.files.ccsds.ndm.adm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): sequance of Euler angles
                isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
                attitude (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): angular coordinates, using :class:`~org.orekit.attitudes.Attitude` convention (i.e. from inertial frame to spacecraft
                    frame)
        
            Returns:
                the attitude data in CCSDS units
        
            Since:
                12.0
        
        
        """
        ...
    def getAngularDerivativesFilter(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
            Get the angular derivative filter corresponding to the attitude data.
        
            Returns:
                the angular derivative filter corresponding to the attitude data
        
        
        """
        ...
    def getName(self, double: float) -> str:
        """
            Get the type name for a given format version.
        
            Parameters:
                formatVersion (double): format version
        
            Returns:
                type name
        
            Since:
                12.0
        
        
        """
        ...
    def parse(self, boolean: bool, boolean2: bool, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, boolean3: bool, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, stringArray: typing.List[str]) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
            Get the angular coordinates corresponding to the attitude data.
        
            This method assumes the text fields are in CCSDS units and will convert to SI units.
        
            Parameters:
                isFirst (boolean): if true the first quaternion component is the scalar component
                isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
                eulerRotSequence (:class:`~org.orekit.files.ccsds.ndm.adm.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): sequance of Euler angles
                isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                fields (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`[]): raw data fields
        
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
                typeSpecification (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): unnormalized type name
        
            Returns:
                parsed type
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum.html?is` in
                class :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`
        
        
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
                name (:class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
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
    public class RotationXmlTokenBuilder extends :class:`~org.orekit.files.ccsds.ndm.adm.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder`
    
        Builder for rotation angles and rates.
    
        Instances of this class are immutable.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def buildTokens(self, boolean: bool, boolean2: bool, string: str, string2: str, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]], int: int, string3: str) -> java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]: ...

_PythonAdmParser__T = typing.TypeVar('_PythonAdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonAdmParser__P = typing.TypeVar('_PythonAdmParser__P', bound=org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser)  # <P>
class PythonAdmParser(AdmParser[_PythonAdmParser__T, _PythonAdmParser__P], typing.Generic[_PythonAdmParser__T, _PythonAdmParser__P]):
    """
    public class PythonAdmParser<T extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, ?>, P extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, T, ?>> extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmParser`<T, P>
    """
    def __init__(self, string: str, string2: str, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, functionArray: typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]]): ...
    def build(self) -> _PythonAdmParser__T:
        """
            Description copied from interface: :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.build`
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
    def getHeader(self) -> AdmHeader:
        """
            Description copied from class: :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.getHeader`
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

    AdmCommonMetadataKey: typing.Type[AdmCommonMetadataKey]
    AdmCommonMetadataWriter: typing.Type[AdmCommonMetadataWriter]
    AdmHeader: typing.Type[AdmHeader]
    AdmMetadata: typing.Type[AdmMetadata]
    AdmMetadataKey: typing.Type[AdmMetadataKey]
    AdmParser: typing.Type[AdmParser]
    AttitudeEndpoints: typing.Type[AttitudeEndpoints]
    AttitudeType: typing.Type[AttitudeType]
    PythonAdmParser: typing.Type[PythonAdmParser]
    RotationXmlTokenBuilder: typing.Type[RotationXmlTokenBuilder]
    acm: org.orekit.files.ccsds.ndm.adm.acm.__module_protocol__
    aem: org.orekit.files.ccsds.ndm.adm.aem.__module_protocol__
    apm: org.orekit.files.ccsds.ndm.adm.apm.__module_protocol__
