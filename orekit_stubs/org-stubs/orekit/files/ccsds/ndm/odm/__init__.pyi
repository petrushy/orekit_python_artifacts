
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.hipparchus.linear
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm.ocm
import org.orekit.files.ccsds.ndm.odm.oem
import org.orekit.files.ccsds.ndm.odm.omm
import org.orekit.files.ccsds.ndm.odm.opm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.frames
import org.orekit.orbits
import org.orekit.time
import org.orekit.utils
import typing



class CartesianCovariance(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    Container for OPM/OMM/OCM Cartesian covariance matrix.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        6.1
    """
    @typing.overload
    def __init__(self, defaultFrameSupplier: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.definitions.FrameFacade], typing.Callable[[], org.orekit.files.ccsds.definitions.FrameFacade]]): ...
    @typing.overload
    def __init__(self, defaultFrameSupplier: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.definitions.FrameFacade], typing.Callable[[], org.orekit.files.ccsds.definitions.FrameFacade]], frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def getCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the Position/Velocity covariance matrix.
        
        Returns:
            the Position/Velocity covariance matrix
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get matrix epoch.
        
        Returns:
            matrix epoch
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which this covariance matrix is defined. Note that only the orientation of the returned frame is significant, the position of the returned frame is irrelevant and should be ignored.
        
        Returns:
            Orekit frame for this covariance matrix.
        
        Since:
            13.1.5
        
        Also see:
            getReferenceFrame,
            getFrameMapper
        
        
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
    def getReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get the reference frame.
        
        Returns:
            The reference frame specified by the COV_REF_FRAME keyword or inherited from metadata
        
        
        """
        ...
    def setCovarianceMatrixEntry(self, j: int, k: int, entry: float) -> None:
        """
        Set an entry in the Position/Velocity covariance matrix.
        
        Both m(j, k) and m(k, j) are set.
        
        Parameters:
            j (int): row index (must be between 0 and 5 (inclusive)
            k (int): column index (must be between 0 and 5 (inclusive)
            entry (double): value of the matrix entry
        
        
        """
        ...
    def setEpoch(self, epoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set matrix epoch.
        
        Parameters:
            epoch (AbsoluteDate): matrix epoch
        
        
        """
        ...
    def setReferenceFrame(self, referenceFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set the reference frame in which data are given.
        
        Parameters:
            referenceFrame (FrameFacade): the reference frame to be set
        
        
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

class CartesianCovarianceKey(java.lang.Enum['CartesianCovarianceKey']):
    """
    Keys for CartesianCovariance entries.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['CartesianCovarianceKey'] = ...
    EPOCH: typing.ClassVar['CartesianCovarianceKey'] = ...
    COV_REF_FRAME: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CX_DOT_X_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_X_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CY_DOT_Y_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_X: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Y: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Z: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_X_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Y_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    CZ_DOT_Z_DOT: typing.ClassVar['CartesianCovarianceKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: CartesianCovariance) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (CartesianCovariance): container to fill
        
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
    def valueOf(name: str) -> 'CartesianCovarianceKey':
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
    def values() -> typing.MutableSequence['CartesianCovarianceKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CartesianCovarianceKey c : CartesianCovarianceKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CartesianCovarianceWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for covariance matrix data.
    
    Since:
        11.0
    """
    def __init__(self, xmlTag: str, kvnTag: str, covariance: CartesianCovariance):
        """
        Create a writer.
        
        Parameters:
            xmlTag (String): name of the XML tag surrounding the section
            kvnTag (String): name of the KVN tag surrounding the section (may be null)
            covariance (CartesianCovariance): covariance matrix to write
        
        
        """
        ...

class CommonMetadataKey(java.lang.Enum['CommonMetadataKey']):
    """
    Keys for OdmCommonMetadata entries.
    
    Since:
        11.0
    """
    OBJECT_ID: typing.ClassVar['CommonMetadataKey'] = ...
    CENTER_NAME: typing.ClassVar['CommonMetadataKey'] = ...
    REF_FRAME: typing.ClassVar['CommonMetadataKey'] = ...
    REF_FRAME_EPOCH: typing.ClassVar['CommonMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: 'OdmCommonMetadata') -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (OdmCommonMetadata): container to fill
        
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
    def valueOf(name: str) -> 'CommonMetadataKey':
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
    def values() -> typing.MutableSequence['CommonMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CommonMetadataKey c : CommonMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CommonMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for Common metadata for CCSDS Orbit Parameter/Ephemeris/Mean Messages.
    
    Since:
        11.0
    """
    def __init__(self, metadata: 'OdmCommonMetadata', timeConverter: org.orekit.files.ccsds.definitions.TimeConverter):
        """
        Simple constructor.
        
        Parameters:
            metadata (OdmCommonMetadata): metadata to write
            timeConverter (TimeConverter): converter for dates
        
        
        """
        ...

class KeplerianElements(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    Container for Keplerian elements.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        6.1
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def generateKeplerianOrbit(self, frame: org.orekit.frames.Frame) -> org.orekit.orbits.KeplerianOrbit:
        """
        Generate a keplerian orbit.
        
        Parameters:
            frame (Frame): inertial frame for orbit
        
        Returns:
            generated orbit
        
        
        """
        ...
    def getA(self) -> float:
        """
        Get the orbit semi-major axis.
        
        Returns:
            the orbit semi-major axis
        
        
        """
        ...
    def getAnomaly(self) -> float:
        """
        Get the orbit anomaly.
        
        Returns:
            the orbit anomaly
        
        
        """
        ...
    def getAnomalyType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get the type of anomaly (true or mean).
        
        Returns:
            the type of anomaly
        
        
        """
        ...
    def getE(self) -> float:
        """
        Get the orbit eccentricity.
        
        Returns:
            the orbit eccentricity
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get epoch of state vector, Keplerian elements and covariance matrix data.
        
        Returns:
            epoch the epoch
        
        
        """
        ...
    def getI(self) -> float:
        """
        Get the orbit inclination.
        
        Returns:
            the orbit inclination
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
        Get the orbit mean motion.
        
        Returns:
            the orbit mean motion
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the gravitational coefficient.
        
        Returns:
            gravitational coefficient
        
        
        """
        ...
    def getPa(self) -> float:
        """
        Get the orbit argument of pericenter.
        
        Returns:
            the orbit argument of pericenter
        
        
        """
        ...
    def getRaan(self) -> float:
        """
        Get the orbit right ascension of ascending node.
        
        Returns:
            the orbit right ascension of ascending node
        
        
        """
        ...
    def setA(self, a: float) -> None:
        """
        Set the orbit semi-major axis.
        
        Parameters:
            a (double): the semi-major axis to be set
        
        
        """
        ...
    def setAnomaly(self, anomaly: float) -> None:
        """
        Set the orbit anomaly.
        
        Parameters:
            anomaly (double): the anomaly to be set
        
        
        """
        ...
    def setAnomalyType(self, anomalyType: org.orekit.orbits.PositionAngleType) -> None:
        """
        Set the type of anomaly.
        
        Parameters:
            anomalyType (PositionAngleType): the type of anomaly to be set
        
        
        """
        ...
    def setE(self, e: float) -> None:
        """
        Set the orbit eccentricity.
        
        Parameters:
            e (double): the eccentricity to be set
        
        
        """
        ...
    def setEpoch(self, epoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set epoch of state vector, Keplerian elements and covariance matrix data.
        
        Parameters:
            epoch (AbsoluteDate): the epoch to be set
        
        
        """
        ...
    def setI(self, i: float) -> None:
        """
        Set the orbit inclination.
        
        Parameters:
            i (double): the inclination to be set
        
        
        """
        ...
    def setMeanMotion(self, motion: float) -> None:
        """
        Set the orbit mean motion.
        
        Parameters:
            motion (double): the mean motion to be set
        
        
        """
        ...
    def setMu(self, mu: float) -> None:
        """
        Set the gravitational coefficient.
        
        Parameters:
            mu (double): the coefficient to be set
        
        
        """
        ...
    def setPa(self, pa: float) -> None:
        """
        Set the orbit argument of pericenter.
        
        Parameters:
            pa (double): the argument of pericenter to be set
        
        
        """
        ...
    def setRaan(self, raan: float) -> None:
        """
        Set the orbit right ascension of ascending node.
        
        Parameters:
            raan (double): the right ascension of ascending node to be set
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        We check neither semi-major axis nor mean motion here, they must be checked separately in OPM and OMM parsers
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class KeplerianElementsKey(java.lang.Enum['KeplerianElementsKey']):
    """
    Keys for KeplerianElements entries.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['KeplerianElementsKey'] = ...
    EPOCH: typing.ClassVar['KeplerianElementsKey'] = ...
    SEMI_MAJOR_AXIS: typing.ClassVar['KeplerianElementsKey'] = ...
    MEAN_MOTION: typing.ClassVar['KeplerianElementsKey'] = ...
    ECCENTRICITY: typing.ClassVar['KeplerianElementsKey'] = ...
    INCLINATION: typing.ClassVar['KeplerianElementsKey'] = ...
    RA_OF_ASC_NODE: typing.ClassVar['KeplerianElementsKey'] = ...
    ARG_OF_PERICENTER: typing.ClassVar['KeplerianElementsKey'] = ...
    TRUE_ANOMALY: typing.ClassVar['KeplerianElementsKey'] = ...
    MEAN_ANOMALY: typing.ClassVar['KeplerianElementsKey'] = ...
    GM: typing.ClassVar['KeplerianElementsKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: KeplerianElements) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (KeplerianElements): container to fill
        
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
    def valueOf(name: str) -> 'KeplerianElementsKey':
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
    def values() -> typing.MutableSequence['KeplerianElementsKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (KeplerianElementsKey c : KeplerianElementsKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OdmHeader(org.orekit.files.ccsds.section.Header):
    """
    Header of a CCSDS Orbit Data Message.
    
    Since:
        12.0
    """
    def __init__(self):
        """
        Constructor.
        """
        ...

class OdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    This class gathers the meta-data present in the Orbital Data Message (ODM).
    
    Since:
        6.1
    """
    def getObjectName(self) -> str:
        """
        Get the spacecraft name for which the orbit state is provided.
        
        Returns:
            the spacecraft name
        
        
        """
        ...
    def setObjectName(self, objectName: str) -> None:
        """
        Set the spacecraft name for which the orbit state is provided.
        
        Parameters:
            objectName (String): the spacecraft name to be set
        
        
        """
        ...

class OdmMetadataKey(java.lang.Enum['OdmMetadataKey']):
    """
    Keys for OdmMetadata entries.
    
    Since:
        11.0
    """
    OBJECT_NAME: typing.ClassVar['OdmMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: OdmMetadata) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (OdmMetadata): container to fill
        
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
    def valueOf(name: str) -> 'OdmMetadataKey':
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
    def values() -> typing.MutableSequence['OdmMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (OdmMetadataKey c : OdmMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_OdmParser__T = typing.TypeVar('_OdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_OdmParser__P = typing.TypeVar('_OdmParser__P', bound='OdmParser')  # <P>
class OdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[OdmHeader, _OdmParser__T, _OdmParser__P], typing.Generic[_OdmParser__T, _OdmParser__P]):
    """
    Common parser for Orbit Parameter/Ephemeris/Mean/Comprehensive Messages.
    
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
    def getSelectedMu(self) -> float:
        """
        Select the gravitational coefficient to use. In order of decreasing priority, finalMU is set equal to:
        
          1.  the coefficient parsed in the file, 2.  the coefficient set by the user with the parser's method setMu, 3.  the coefficient created from the knowledge of the central body.
        
        
        Returns:
            selected gravitational coefficient
        
        
        """
        ...

class SpacecraftParameters(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    Container for spacecraft parameters.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        6.1
    """
    def __init__(self):
        """
        Create an empty state data set.
        """
        ...
    def getDragArea(self) -> float:
        """
        Get the drag area.
        
        Returns:
            the drag area
        
        
        """
        ...
    def getDragCoeff(self) -> float:
        """
        Get the drag coefficient.
        
        Returns:
            the drag coefficient
        
        
        """
        ...
    def getMass(self) -> float:
        """
        Get the spacecraft mass.
        
        Returns:
            the spacecraft mass
        
        
        """
        ...
    def getSolarRadArea(self) -> float:
        """
        Get the solar radiation pressure area.
        
        Returns:
            the solar radiation pressure area
        
        
        """
        ...
    def getSolarRadCoeff(self) -> float:
        """
        Get the solar radiation pressure coefficient.
        
        Returns:
            the solar radiation pressure coefficient
        
        
        """
        ...
    def setDragArea(self, dragArea: float) -> None:
        """
        Set the drag area.
        
        Parameters:
            dragArea (double): the area to be set
        
        
        """
        ...
    def setDragCoeff(self, dragCoeff: float) -> None:
        """
        Set the drag coefficient.
        
        Parameters:
            dragCoeff (double): the coefficient to be set
        
        
        """
        ...
    def setMass(self, mass: float) -> None:
        """
        Set the spacecraft mass.
        
        Parameters:
            mass (double): the spacecraft mass to be set
        
        
        """
        ...
    def setSolarRadArea(self, solarRadArea: float) -> None:
        """
        Set the solar radiation pressure area.
        
        Parameters:
            solarRadArea (double): the area to be set
        
        
        """
        ...
    def setSolarRadCoeff(self, solarRadCoeff: float) -> None:
        """
        Get the solar radiation pressure coefficient.
        
        Parameters:
            solarRadCoeff (double): the coefficient to be set
        
        
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

class SpacecraftParametersKey(java.lang.Enum['SpacecraftParametersKey']):
    """
    Keys for SpacecraftParameters entries.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['SpacecraftParametersKey'] = ...
    MASS: typing.ClassVar['SpacecraftParametersKey'] = ...
    SOLAR_RAD_AREA: typing.ClassVar['SpacecraftParametersKey'] = ...
    SOLAR_RAD_COEFF: typing.ClassVar['SpacecraftParametersKey'] = ...
    DRAG_AREA: typing.ClassVar['SpacecraftParametersKey'] = ...
    DRAG_COEFF: typing.ClassVar['SpacecraftParametersKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: SpacecraftParameters) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (SpacecraftParameters): container to fill
        
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
    def valueOf(name: str) -> 'SpacecraftParametersKey':
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
    def values() -> typing.MutableSequence['SpacecraftParametersKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SpacecraftParametersKey c : SpacecraftParametersKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SpacecraftParametersWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for spacecraft parameters data.
    
    Since:
        11.0
    """
    def __init__(self, xmlTag: str, kvnTag: str, spacecraftParameters: SpacecraftParameters):
        """
        Create a writer.
        
        Parameters:
            xmlTag (String): name of the XML tag surrounding the section
            kvnTag (String): name of the KVN tag surrounding the section (may be null)
            spacecraftParameters (SpacecraftParameters): spacecraft parameters to write
        
        
        """
        ...

class StateVector(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for state vector data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Create an empty data set.
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get epoch of state vector, Keplerian elements and covariance matrix data.
        
        Returns:
            epoch the epoch
        
        
        """
        ...
    def hasAcceleration(self) -> bool:
        """
        Check if state contains acceleration data.
        
        Returns:
            true is state contains acceleration data
        
        
        """
        ...
    def setA(self, index: int, value: float) -> None:
        """
        Set acceleration component.
        
        Parameters:
            index (int): component index (counting from 0)
            value (double): acceleration component
        
        
        """
        ...
    def setEpoch(self, epoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set epoch of state vector, Keplerian elements and covariance matrix data.
        
        Parameters:
            epoch (AbsoluteDate): the epoch to be set
        
        
        """
        ...
    def setP(self, index: int, value: float) -> None:
        """
        Set position component.
        
        Parameters:
            index (int): component index (counting from 0)
            value (double): position component
        
        
        """
        ...
    def setV(self, index: int, value: float) -> None:
        """
        Set velocity component.
        
        Parameters:
            index (int): component index (counting from 0)
            value (double): velocity component
        
        
        """
        ...
    def toTimeStampedPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Convert to TimeStampedPVCoordinates.
        
        Returns:
            a new TimeStampedPVCoordinates
        
        
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

class StateVectorKey(java.lang.Enum['StateVectorKey']):
    """
    Keys for StateVector entries.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['StateVectorKey'] = ...
    EPOCH: typing.ClassVar['StateVectorKey'] = ...
    X: typing.ClassVar['StateVectorKey'] = ...
    Y: typing.ClassVar['StateVectorKey'] = ...
    Z: typing.ClassVar['StateVectorKey'] = ...
    X_DOT: typing.ClassVar['StateVectorKey'] = ...
    Y_DOT: typing.ClassVar['StateVectorKey'] = ...
    Z_DOT: typing.ClassVar['StateVectorKey'] = ...
    X_DDOT: typing.ClassVar['StateVectorKey'] = ...
    Y_DDOT: typing.ClassVar['StateVectorKey'] = ...
    Z_DDOT: typing.ClassVar['StateVectorKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: StateVector) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (StateVector): container to fill
        
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
    def valueOf(name: str) -> 'StateVectorKey':
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
    def values() -> typing.MutableSequence['StateVectorKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (StateVectorKey c : StateVectorKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StateVectorWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for state vector data.
    
    Since:
        11.0
    """
    def __init__(self, xmlTag: str, kvnTag: str, stateVector: StateVector, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter):
        """
        Create a writer.
        
        Parameters:
            xmlTag (String): name of the XML tag surrounding the section
            kvnTag (String): name of the KVN tag surrounding the section (may be null)
            stateVector (StateVector): state vector to write
            timeConverter (TimeConverter): converter for dates
        
        
        """
        ...

class UserDefined(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for user defined data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        11.0
    """
    USER_DEFINED_XML_TAG: typing.ClassVar[str] = ...
    """
    Tag name for user defined parameters keys.
    
    Also see:
        constant
    
    
    """
    USER_DEFINED_XML_ATTRIBUTE: typing.ClassVar[str] = ...
    """
    Attribute name for user defined parameters keys.
    
    Also see:
        constant
    
    
    """
    USER_DEFINED_PREFIX: typing.ClassVar[str] = ...
    """
    Prefix for user defined parameters keys.
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Create an empty data set.
        """
        ...
    def addEntry(self, key: str, value: str) -> None:
        """
        Add a key/value entry.
        
        Parameters:
            key (String): parameter key, with the USER_DEFINED_PREFIX stripped away
            value (String): parameter value
        
        
        """
        ...
    def getParameters(self) -> java.util.Map[str, str]:
        """
        Get all user defined parameters.
        
        The USER_DEFINED_PREFIX has been stripped away from the keys.
        
        Returns:
            unmodifiable view of the map containing all user defined parameters
        
        
        """
        ...

class UserDefinedWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for user defined parameters data.
    
    Since:
        11.0
    """
    def __init__(self, xmlTag: str, kvnTag: str, userDefined: UserDefined):
        """
        Create a writer.
        
        Parameters:
            xmlTag (String): name of the XML tag surrounding the section
            kvnTag (String): name of the KVN tag surrounding the section (may be null)
            userDefined (UserDefined): user defined parameters to write
        
        
        """
        ...

class OdmCommonMetadata(OdmMetadata):
    """
    Common metadata for Orbit Parameter/Ephemeris/Mean Messages.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def finalizeMetadata(self, context: org.orekit.files.ccsds.utils.ContextBinding) -> None:
        """
        Finalize the metadata.
        
        ODM standard enforces TIME_SYSTEM to appear after REF_FRAME_EPOCH, despite it is needed to interpret it. We have to wait until parsing end to finalize this date.
        
        Parameters:
            context (ContextBinding): context binding
        
        
        """
        ...
    def getCenter(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
        Get the origin of reference frame.
        
        Returns:
            the origin of reference frame.
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame in which data are given: used for state vector and Keplerian elements data (and for the covariance reference frame if none is given).
        
        Returns:
            the reference frame
        
        Also see:
            getFrameMapper
        
        
        """
        ...
    def getFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get epoch of reference frame, if not intrinsic to the definition of the reference frame.
        
        Returns:
            epoch of reference frame
        
        
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
        Get the spacecraft ID for which the orbit state is provided.
        
        Returns:
            the spacecraft ID
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get the value of REF_FRAME as an Orekit Frame. The CENTER_NAME key word has not been applied yet, so the returned frame may not correspond to the reference frame of the data in the file.
        
        Returns:
            The reference frame specified by the REF_FRAME keyword.
        
        Also see:
            getFrame
        
        
        """
        ...
    def setCenter(self, center: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
        Set the origin of reference frame.
        
        Parameters:
            center (BodyFacade): origin of reference frame to be set
        
        
        """
        ...
    def setFrameEpoch(self, frameEpoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set epoch of reference frame, if not intrinsic to the definition of the reference frame.
        
        Parameters:
            frameEpoch (AbsoluteDate): the epoch of reference frame to be set
        
        
        """
        ...
    def setFrameEpochString(self, frameEpochString: str) -> None:
        """
        Set epoch of reference frame, if not intrinsic to the definition of the reference frame.
        
        Parameters:
            frameEpochString (String): the epoch of reference frame to be set
        
        
        """
        ...
    def setObjectID(self, objectID: str) -> None:
        """
        Set the spacecraft ID for which the orbit state is provided.
        
        Parameters:
            objectID (String): the spacecraft ID to be set
        
        
        """
        ...
    def setReferenceFrame(self, referenceFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set the reference frame in which data are given: used for state vector and Keplerian elements data (and for the covariance reference frame if none is given).
        
        Parameters:
            referenceFrame (FrameFacade): the reference frame to be set
        
        
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

_PythonOdmParser__T = typing.TypeVar('_PythonOdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonOdmParser__P = typing.TypeVar('_PythonOdmParser__P', bound=OdmParser)  # <P>
class PythonOdmParser(OdmParser[_PythonOdmParser__T, _PythonOdmParser__P], typing.Generic[_PythonOdmParser__T, _PythonOdmParser__P]):
    def __init__(self, root: str, formatVersionKey: str, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate, mu: float, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]):
        """
        Complete constructor.
        
        Parameters:
            root (String): root element for XML files
            formatVersionKey (String): key for format version
            conventions (IERSConventions): IERS Conventions
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
            dataContext (DataContext): used to retrieve frames and time scales
            missionReferenceDate (AbsoluteDate): reference date for Mission Elapsed Time or Mission Relative Time time systems
            mu (double): gravitational coefficient
            parsedUnitsBehavior (ParsedUnitsBehavior): behavior to adopt for handling parsed units
            filters (Function<ParseToken, List<ParseToken>>[]): filters to apply to parse tokens
        
        Since:
            12.0
        
        
        """
        ...
    def build(self) -> _PythonOdmParser__T:
        """
        Build the file from parsed entries.
        
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
    def getFileFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
        Get the file format.
        
        Specified by: getFileFormat in interface MessageParser
        
        Overrides: getFileFormat in class AbstractMessageParser
        
        Returns:
            file format
        
        
        """
        ...
    def getHeader(self) -> OdmHeader:
        """
        Get file header to fill.
        
        Specified by: getHeader in class AbstractConstituentParser
        
        Returns:
            file header to fill
        
        
        """
        ...
    def getMuSet(self) -> float:
        """
        Get the gravitational coefficient set at construction.
        
        Overrides: getMuSet in class OdmParser
        
        Returns:
            gravitational coefficient set at construction
        
        
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
    def setMuCreated(self, muCreated: float) -> None:
        """
        Set the gravitational coefficient created from the knowledge of the central body.
        
        Overrides: setMuCreated in class OdmParser
        
        Parameters:
            muCreated (double): the coefficient to be set
        
        
        """
        ...
    def setMuParsed(self, muParsed: float) -> None:
        """
        Set the gravitational coefficient parsed in the ODM File.
        
        Overrides: setMuParsed in class OdmParser
        
        Parameters:
            muParsed (double): the coefficient to be set
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm")``.

    CartesianCovariance: typing.Type[CartesianCovariance]
    CartesianCovarianceKey: typing.Type[CartesianCovarianceKey]
    CartesianCovarianceWriter: typing.Type[CartesianCovarianceWriter]
    CommonMetadataKey: typing.Type[CommonMetadataKey]
    CommonMetadataWriter: typing.Type[CommonMetadataWriter]
    KeplerianElements: typing.Type[KeplerianElements]
    KeplerianElementsKey: typing.Type[KeplerianElementsKey]
    OdmCommonMetadata: typing.Type[OdmCommonMetadata]
    OdmHeader: typing.Type[OdmHeader]
    OdmMetadata: typing.Type[OdmMetadata]
    OdmMetadataKey: typing.Type[OdmMetadataKey]
    OdmParser: typing.Type[OdmParser]
    PythonOdmParser: typing.Type[PythonOdmParser]
    SpacecraftParameters: typing.Type[SpacecraftParameters]
    SpacecraftParametersKey: typing.Type[SpacecraftParametersKey]
    SpacecraftParametersWriter: typing.Type[SpacecraftParametersWriter]
    StateVector: typing.Type[StateVector]
    StateVectorKey: typing.Type[StateVectorKey]
    StateVectorWriter: typing.Type[StateVectorWriter]
    UserDefined: typing.Type[UserDefined]
    UserDefinedWriter: typing.Type[UserDefinedWriter]
    ocm: org.orekit.files.ccsds.ndm.odm.ocm.__module_protocol__
    oem: org.orekit.files.ccsds.ndm.odm.oem.__module_protocol__
    omm: org.orekit.files.ccsds.ndm.odm.omm.__module_protocol__
    opm: org.orekit.files.ccsds.ndm.odm.opm.__module_protocol__
