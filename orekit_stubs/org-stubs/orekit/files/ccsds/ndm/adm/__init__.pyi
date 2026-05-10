
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
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
    Keys for AdmMetadata entries.
    
    Since:
        12.0
    """
    OBJECT_ID: typing.ClassVar['AdmCommonMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: 'AdmMetadata') -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AdmMetadata): container to fill
        
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
    def valueOf(name: str) -> 'AdmCommonMetadataKey':
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
    def values() -> typing.MutableSequence['AdmCommonMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AdmCommonMetadataKey c : AdmCommonMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdmCommonMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for Common metadata for CCSDS Attitude Parameter/Ephemeris Messages.
    
    Since:
        11.0
    """
    def __init__(self, metadata: 'AdmMetadata'):
        """
        Simple constructor.
        
        Parameters:
            metadata (AdmMetadata): metadata to write
        
        
        """
        ...

class AdmHeader(org.orekit.files.ccsds.section.Header):
    """
    Header of a CCSDS Attitude Data Message.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...

class AdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    This class gathers the meta-data present in the Attitude Data Message (ADM).
    
    Since:
        10.2
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def getCenter(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
        Get the body at origin of reference frame.
        
        Returns:
            the body at origin of reference frame.
        
        
        """
        ...
    def getHasCreatableBody(self) -> bool:
        """
        Get boolean testing whether the body corresponding to the centerName attribute can be created through the CelestialBodies.
        
        Returns:
            true if CelestialBody can be created from centerName false otherwise
        
        
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
    def setCenter(self, center: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
        Set the body at origin of reference frame.
        
        Parameters:
            center (BodyFacade): body at origin of reference frame
        
        
        """
        ...
    def setObjectID(self, objectID: str) -> None:
        """
        Set the spacecraft ID for which the attitude data are provided.
        
        Parameters:
            objectID (String): the spacecraft ID to be set
        
        
        """
        ...
    def setObjectName(self, objectName: str) -> None:
        """
        Set the spacecraft name for which the attitude data are provided.
        
        Parameters:
            objectName (String): the spacecraft name to be set
        
        
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

class AdmMetadataKey(java.lang.Enum['AdmMetadataKey']):
    """
    Keys for AdmMetadata entries.
    
    Since:
        11.0
    """
    OBJECT_NAME: typing.ClassVar['AdmMetadataKey'] = ...
    CENTER_NAME: typing.ClassVar['AdmMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AdmMetadata) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AdmMetadata): container to fill
        
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
    def valueOf(name: str) -> 'AdmMetadataKey':
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
    def values() -> typing.MutableSequence['AdmMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
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
    Base class for Attitude Data Message parsers.
    
    Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until the message is complete and the parseMessage method has returned. This implies that parsers should not be used in a multi-thread context. The recommended way to use parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
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
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]:
        """
        Get the non-default token builders for special XML elements.
        
        Specified by: getSpecialXmlElementsBuilders in interface MessageParser
        
        Overrides: getSpecialXmlElementsBuilders in class AbstractMessageParser
        
        Returns:
            map of token builders for special XML elements (keyed by XML element name)
        
        
        """
        ...

class AttitudeEndpoints(org.orekit.attitudes.AttitudeBuilder):
    """
    Endpoints for attitude definition.
    
    This class provides a bridge between two different views of attitude definition. In both views, there is an external frame, based on either celestial body or orbit-relative and there is a spacecraft body frame.
    
      - CCSDS ADM view: frames are labeled as A and B but nothing tells which is which and attitude can be defined in any
        direction
      - Attitude view: attitude is always from external to spacecraft body
    
    
    Since:
        11.0
    """
    A2B: typing.ClassVar[str] = ...
    """
    Constant for A → B diraction.
    
    Also see:
        constant
    
    
    """
    B2A: typing.ClassVar[str] = ...
    """
    Constant for A ← B direction.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], rawAttitude: org.orekit.utils.TimeStampedAngularCoordinates) -> org.orekit.attitudes.Attitude:
        """
        Build a filtered attitude.
        
        Specified by: build in interface AttitudeBuilder
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (PVCoordinatesProvider): provider for spacecraft position and velocity
            rawAttitude (TimeStampedAngularCoordinates): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], rawAttitude: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> org.orekit.attitudes.FieldAttitude[_build_1__T]:
        """
        Build a filtered attitude.
        
        Specified by: build in interface AttitudeBuilder
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for spacecraft position and velocity
            rawAttitude (TimeStampedFieldAngularCoordinates<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        
        """
        ...
    def checkExternalFrame(self, aKey: java.lang.Enum[typing.Any], bKey: java.lang.Enum[typing.Any]) -> None:
        """
        Check external frame is properly initialized.
        
        Parameters:
            aKey (Enum<?> aKey): key for frame A
            bKey (Enum<?> bKey): key for frame B
        
        
        """
        ...
    def checkMandatoryEntriesExceptExternalFrame(self, version: float, aKey: java.lang.Enum[typing.Any], bKey: java.lang.Enum[typing.Any], dirKey: java.lang.Enum[typing.Any]) -> None:
        """
        Check is mandatory entries except external frame have been initialized.
        
        Either frame A or frame B must be initialized with a SpacecraftBodyFrame.
        
        This method should throw an exception if some mandatory entry is missing
        
        Parameters:
            version (double): format version
            aKey (Enum<?> aKey): key for frame A
            bKey (Enum<?> bKey): key for frame B
            dirKey (Enum<?> dirKey): key for direction
        
        
        """
        ...
    def getExternal(self) -> org.orekit.frames.Frame:
        """
        Get the external reference frame. Only the orientation is significant.
        
        Returns:
            the external frame.
        
        Since:
            13.1.5
        
        Also see:
            getExternalFrame
        
        
        """
        ...
    def getExternalFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get the external frame.
        
        Returns:
            external frame
        
        Also see:
            getExternal
        
        
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
    def getFrameMapper(self) -> org.orekit.files.ccsds.definitions.CcsdsFrameMapper:
        """
        Get the mapping between a CCSDS frame and a Frame.
        
        Returns:
            the frame mapper.
        
        Since:
            13.1.5
        
        
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
        Check if rotation direction is from getFrameA to getFrameB.
        
        Returns:
            true if rotation direction is from getFrameA to
            getFrameB
        
        
        """
        ...
    def isCompatibleWith(self, other: 'AttitudeEndpoints') -> bool:
        """
        Check if a endpoint is compatible with another one.
        
        Endpoins are compatible if they refer o the same frame names, in the same order and in the same direction.
        
        Parameters:
            other (AttitudeEndpoints): other endpoints to check against
        
        Returns:
            true if both endpoints are compatible with each other
        
        
        """
        ...
    def isExternal2SpacecraftBody(self) -> bool:
        """
        Check if attitude is from external frame to spacecraft body frame.
        
        checkMandatoryEntriesExceptExternalFrame must have been initialized properly to non-null values before this method is called, otherwise NullPointerException will be thrown.
        
        Returns:
            true if attitude is from external frame to spacecraft body frame
        
        
        """
        ...
    def setA2b(self, a2b: bool) -> None:
        """
        Set rotation direction.
        
        Parameters:
            a2b (boolean): if true, rotation is from getFrameA to
                getFrameB
        
        
        """
        ...
    def setFrameA(self, frameA: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set frame A.
        
        Parameters:
            frameA (FrameFacade): frame A
        
        
        """
        ...
    def setFrameB(self, frameB: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set frame B.
        
        Parameters:
            frameB (FrameFacade): frame B
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class AttitudeType(java.lang.Enum['AttitudeType']):
    """
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
    def build(self, isFirst: bool, isExternal2SpacecraftBody: bool, eulerRotSequence: org.hipparchus.geometry.euclidean.threed.RotationOrder, isSpacecraftBodyRate: bool, date: org.orekit.time.AbsoluteDate, *components: float) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
        Get the angular coordinates corresponding to the attitude data.
        
        Parameters:
            isFirst (boolean): if true the first quaternion component is the scalar component
            isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
            eulerRotSequence (RotationOrder): sequance of Euler angles
            isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
            date (AbsoluteDate): entry date
            components (double...): entry components with SI units, semantic depends on attitude type
        
        Returns:
            the angular coordinates, using Attitude convention (i.e. from inertial frame to
            spacecraft frame)
        
        
        """
        ...
    @typing.overload
    def createDataFields(self, isFirst: bool, isExternal2SpacecraftBody: bool, eulerRotSequence: org.hipparchus.geometry.euclidean.threed.RotationOrder, isSpacecraftBodyRate: bool, attitude: org.orekit.utils.TimeStampedAngularCoordinates) -> typing.MutableSequence[str]:
        """
        Get the attitude data fields corresponding to the attitude type.
        
        This method returns the components in CCSDS units (i.e. degrees, degrees per seconds…).
        
        Parameters:
            isFirst (boolean): if true the first quaternion component is the scalar component
            isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
            eulerRotSequence (RotationOrder): sequance of Euler angles
            isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
            attitude (TimeStampedAngularCoordinates): angular coordinates, using Attitude convention
            formatter (Formatter): used to format doubles and dates (i.e. from inertial frame to spacecraft frame)
        
        Returns:
            the attitude data in CCSDS units
        
        Get the attitude data fields corresponding to the attitude type.
        
        This method returns the components in CCSDS units (i.e. degrees, degrees per seconds…).
        
        Parameters:
            isFirst (boolean): if true the first quaternion component is the scalar component
            isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
            eulerRotSequence (RotationOrder): sequance of Euler angles
            isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
            attitude (TimeStampedAngularCoordinates): angular coordinates, using Attitude convention (i.e. from inertial frame to spacecraft
                frame)
        
        Returns:
            the attitude data in CCSDS units
        
        
        """
        ...
    @typing.overload
    def createDataFields(self, isFirst: bool, isExternal2SpacecraftBody: bool, eulerRotSequence: org.hipparchus.geometry.euclidean.threed.RotationOrder, isSpacecraftBodyRate: bool, attitude: org.orekit.utils.TimeStampedAngularCoordinates, formatter: org.orekit.utils.Formatter) -> typing.MutableSequence[str]: ...
    def generateData(self, isFirst: bool, isExternal2SpacecraftBody: bool, eulerRotSequence: org.hipparchus.geometry.euclidean.threed.RotationOrder, isSpacecraftBodyRate: bool, attitude: org.orekit.utils.TimeStampedAngularCoordinates) -> typing.MutableSequence[float]:
        """
        Generate the attitude data corresponding to the attitude type.
        
        This method returns the components in SI units.
        
        Parameters:
            isFirst (boolean): if true the first quaternion component is the scalar component
            isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
            eulerRotSequence (RotationOrder): sequance of Euler angles
            isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
            attitude (TimeStampedAngularCoordinates): angular coordinates, using Attitude convention (i.e. from inertial frame to spacecraft
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
    def getName(self, formatVersion: float) -> str:
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
    def parse(self, isFirst: bool, isExternal2SpacecraftBody: bool, eulerRotSequence: org.hipparchus.geometry.euclidean.threed.RotationOrder, isSpacecraftBodyRate: bool, context: org.orekit.files.ccsds.utils.ContextBinding, fields: typing.Union[typing.List[str], jpype.JArray]) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
        Get the angular coordinates corresponding to the attitude data.
        
        This method assumes the text fields are in CCSDS units and will convert to SI units.
        
        Parameters:
            isFirst (boolean): if true the first quaternion component is the scalar component
            isExternal2SpacecraftBody (boolean): true attitude is from external frame to spacecraft body frame
            eulerRotSequence (RotationOrder): sequance of Euler angles
            isSpacecraftBodyRate (boolean): if true Euler rates are specified in spacecraft body frame
            context (ContextBinding): context binding
            fields (String[]): raw data fields
        
        Returns:
            the angular coordinates, using Attitude convention (i.e. from inertial frame to
            spacecraft frame)
        
        
        """
        ...
    @staticmethod
    def parseType(typeSpecification: str) -> 'AttitudeType':
        """
        Parse an attitude type.
        
        Parameters:
            typeSpecification (String): unnormalized type name
        
        Returns:
            parsed type
        
        
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
    def valueOf(name: str) -> 'AttitudeType':
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
    def values() -> typing.MutableSequence['AttitudeType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AttitudeType c : AttitudeType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RotationXmlTokenBuilder(org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder):
    """
    Builder for rotation angles and rates.
    
    Instances of this class are immutable.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def buildTokens(self, startTag: bool, isLeaf: bool, qName: str, content: str, attributes: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]], lineNumber: int, fileName: str) -> java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]:
        """
        Create a list of parse tokens.
        
        Specified by: buildTokens in interface XmlTokenBuilder
        
        Parameters:
            startTag (boolean): if true we are parsing the start tag from an XML element
            isLeaf (boolean): if true and startTag is false, we are processing the end tag of a leaf XML element
            qName (String): element qualified name
            content (String): element content
            attributes (Map<String, String> attributes): element attributes
            lineNumber (int): number of the line in the CCSDS data message
            fileName (String): name of the file
        
        Returns:
            list of parse tokens
        
        
        """
        ...

_PythonAdmParser__T = typing.TypeVar('_PythonAdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonAdmParser__P = typing.TypeVar('_PythonAdmParser__P', bound=org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser)  # <P>
class PythonAdmParser(AdmParser[_PythonAdmParser__T, _PythonAdmParser__P], typing.Generic[_PythonAdmParser__T, _PythonAdmParser__P]):
    def __init__(self, root: str, formatVersionKey: str, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]):
        """
        Complete constructor.
        
        Parameters:
            root (String): root element for XML files
            formatVersionKey (String): key for format version
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
    def build(self) -> _PythonAdmParser__T:
        """
        Description copied from interface: build Build the file from parsed entries.
        
        Returns:
            parsed file
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def getHeader(self) -> AdmHeader:
        """
        Description copied from class: getHeader Get file header to fill.
        
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
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
        Reset parser to initial state before parsing.
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...


class __module_protocol__(Protocol):
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
