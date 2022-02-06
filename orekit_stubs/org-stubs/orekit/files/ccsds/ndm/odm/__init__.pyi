import java.lang
import java.util
import java.util.function
import org.hipparchus.linear
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
    public class CartesianCovariance extends :class:`~org.orekit.files.ccsds.section.CommentsContainer` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Container for OPM/OMM/OCM Cartesian covariance matrix.
    
        Since:
            6.1
    """
    def __init__(self, supplier: typing.Union[java.util.function.Supplier[org.orekit.files.ccsds.definitions.FrameFacade], typing.Callable[[], org.orekit.files.ccsds.definitions.FrameFacade]]): ...
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
    def getReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get the reference frame.
        
            Returns:
                The reference frame specified by the :code:`COV_REF_FRAME` keyword or inherited from metadata
        
        
        """
        ...
    def setCovarianceMatrixEntry(self, int: int, int2: int, double: float) -> None:
        """
            Set an entry in the Position/Velocity covariance matrix.
        
            Both m(j, k) and m(k, j) are set.
        
            Parameters:
                j (int): row index (must be between 0 and 5 (inclusive)
                k (int): column index (must be between 0 and 5 (inclusive)
                entry (double): value of the matrix entry
        
        
        """
        ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set matrix epoch.
        
            Parameters:
                epoch (:class:`~org.orekit.time.AbsoluteDate`): matrix epoch
        
        
        """
        ...
    def setReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set the reference frame in which data are given.
        
            Parameters:
                referenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
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

class CartesianCovarianceKey(java.lang.Enum['CartesianCovarianceKey']):
    """
    public enum CartesianCovarianceKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.CartesianCovarianceKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.CartesianCovariance` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, cartesianCovariance: CartesianCovariance) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.CartesianCovariance`): container to fill
        
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
    def valueOf(string: str) -> 'CartesianCovarianceKey':
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
    def values() -> typing.List['CartesianCovarianceKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CartesianCovarianceKey c : CartesianCovarianceKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CartesianCovarianceWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class CartesianCovarianceWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for covariance matrix data.
    
        Since:
            11.0
    """
    def __init__(self, string: str, string2: str, cartesianCovariance: CartesianCovariance): ...

class CommonMetadataKey(java.lang.Enum['CommonMetadataKey']):
    """
    public enum CommonMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.CommonMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.CommonMetadata` entries.
    
        Since:
            11.0
    """
    OBJECT_ID: typing.ClassVar['CommonMetadataKey'] = ...
    CENTER_NAME: typing.ClassVar['CommonMetadataKey'] = ...
    REF_FRAME: typing.ClassVar['CommonMetadataKey'] = ...
    REF_FRAME_EPOCH: typing.ClassVar['CommonMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, commonMetadata: 'CommonMetadata') -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.CommonMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'CommonMetadataKey':
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
    def values() -> typing.List['CommonMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CommonMetadataKey c : CommonMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CommonMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class CommonMetadataWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for Common metadata for CCSDS Orbit Parameter/Ephemeris/Mean Messages.
    
        Since:
            11.0
    """
    def __init__(self, commonMetadata: 'CommonMetadata', timeConverter: org.orekit.files.ccsds.definitions.TimeConverter): ...

class KeplerianElements(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    public class KeplerianElements extends :class:`~org.orekit.files.ccsds.section.CommentsContainer` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Container for Keplerian elements.
    
        Since:
            6.1
    """
    def __init__(self): ...
    def generateKeplerianOrbit(self, frame: org.orekit.frames.Frame) -> org.orekit.orbits.KeplerianOrbit:
        """
            Generate a keplerian orbit.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): inertial frame for orbit
        
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
    def getAnomalyType(self) -> org.orekit.orbits.PositionAngle:
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
    def setA(self, double: float) -> None:
        """
            Set the orbit semi-major axis.
        
            Parameters:
                a (double): the semi-major axis to be set
        
        
        """
        ...
    def setAnomaly(self, double: float) -> None:
        """
            Set the orbit anomaly.
        
            Parameters:
                anomaly (double): the anomaly to be set
        
        
        """
        ...
    def setAnomalyType(self, positionAngle: org.orekit.orbits.PositionAngle) -> None:
        """
            Set the type of anomaly.
        
            Parameters:
                anomalyType (:class:`~org.orekit.orbits.PositionAngle`): the type of anomaly to be set
        
        
        """
        ...
    def setE(self, double: float) -> None:
        """
            Set the orbit eccentricity.
        
            Parameters:
                e (double): the eccentricity to be set
        
        
        """
        ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of state vector, Keplerian elements and covariance matrix data.
        
            Parameters:
                epoch (:class:`~org.orekit.time.AbsoluteDate`): the epoch to be set
        
        
        """
        ...
    def setI(self, double: float) -> None:
        """
            Set the orbit inclination.
        
            Parameters:
                i (double): the inclination to be set
        
        
        """
        ...
    def setMeanMotion(self, double: float) -> None:
        """
            Set the orbit mean motion.
        
            Parameters:
                motion (double): the mean motion to be set
        
        
        """
        ...
    def setMu(self, double: float) -> None:
        """
            Set the gravitational coefficient.
        
            Parameters:
                mu (double): the coefficient to be set
        
        
        """
        ...
    def setPa(self, double: float) -> None:
        """
            Set the orbit argument of pericenter.
        
            Parameters:
                pa (double): the argument of pericenter to be set
        
        
        """
        ...
    def setRaan(self, double: float) -> None:
        """
            Set the orbit right ascension of ascending node.
        
            Parameters:
                raan (double): the right ascension of ascending node to be set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            We check neither semi-major axis nor mean motion here, they must be checked separately in OPM and OMM parsers
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class KeplerianElementsKey(java.lang.Enum['KeplerianElementsKey']):
    """
    public enum KeplerianElementsKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.KeplerianElementsKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.KeplerianElements` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, keplerianElements: KeplerianElements) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.KeplerianElements`): container to fill
        
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
    def valueOf(string: str) -> 'KeplerianElementsKey':
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
    def values() -> typing.List['KeplerianElementsKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (KeplerianElementsKey c : KeplerianElementsKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    public class OdmMetadata extends :class:`~org.orekit.files.ccsds.section.Metadata`
    
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
    def setObjectName(self, string: str) -> None:
        """
            Set the spacecraft name for which the orbit state is provided.
        
            Parameters:
                objectName (String): the spacecraft name to be set
        
        
        """
        ...

class OdmMetadataKey(java.lang.Enum['OdmMetadataKey']):
    """
    public enum OdmMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.OdmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.OdmMetadata` entries.
    
        Since:
            11.0
    """
    OBJECT_NAME: typing.ClassVar['OdmMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, odmMetadata: OdmMetadata) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.OdmMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'OdmMetadataKey':
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
    def values() -> typing.List['OdmMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OdmMetadataKey c : OdmMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_OdmParser__T = typing.TypeVar('_OdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_OdmParser__P = typing.TypeVar('_OdmParser__P', bound='OdmParser')  # <P>
class OdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[_OdmParser__T, _OdmParser__P], typing.Generic[_OdmParser__T, _OdmParser__P]):
    """
    public abstract class OdmParser<T extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<?,?>,P extends OdmParser<T,?>> extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<T,P>
    
        Common parser for Orbit Parameter/Ephemeris/Mean/Comprehensive Messages.
    
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
    def getSelectedMu(self) -> float:
        """
            Select the gravitational coefficient to use. In order of decreasing priority, finalMU is set equal to:
        
              1.  the coefficient parsed in the file,
              2.  the coefficient set by the user with the parser's method setMu,
              3.  the coefficient created from the knowledge of the central body.
        
        
            Returns:
                selected gravitational coefficient
        
        
        """
        ...

class SpacecraftParameters(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    public class SpacecraftParameters extends :class:`~org.orekit.files.ccsds.section.CommentsContainer` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Container for spacecraft parameters.
    
        Since:
            6.1
    """
    def __init__(self): ...
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
    def setDragArea(self, double: float) -> None:
        """
            Set the drag area.
        
            Parameters:
                dragArea (double): the area to be set
        
        
        """
        ...
    def setDragCoeff(self, double: float) -> None:
        """
            Set the drag coefficient.
        
            Parameters:
                dragCoeff (double): the coefficient to be set
        
        
        """
        ...
    def setMass(self, double: float) -> None:
        """
            Set the spacecraft mass.
        
            Parameters:
                mass (double): the spacecraft mass to be set
        
        
        """
        ...
    def setSolarRadArea(self, double: float) -> None:
        """
            Set the solar radiation pressure area.
        
            Parameters:
                solarRadArea (double): the area to be set
        
        
        """
        ...
    def setSolarRadCoeff(self, double: float) -> None:
        """
            Get the solar radiation pressure coefficient.
        
            Parameters:
                solarRadCoeff (double): the coefficient to be set
        
        
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
    public enum SpacecraftParametersKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.SpacecraftParametersKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.SpacecraftParameters` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['SpacecraftParametersKey'] = ...
    MASS: typing.ClassVar['SpacecraftParametersKey'] = ...
    SOLAR_RAD_AREA: typing.ClassVar['SpacecraftParametersKey'] = ...
    SOLAR_RAD_COEFF: typing.ClassVar['SpacecraftParametersKey'] = ...
    DRAG_AREA: typing.ClassVar['SpacecraftParametersKey'] = ...
    DRAG_COEFF: typing.ClassVar['SpacecraftParametersKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, spacecraftParameters: SpacecraftParameters) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.SpacecraftParameters`): container to fill
        
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

class SpacecraftParametersWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class SpacecraftParametersWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for spacecraft parameters data.
    
        Since:
            11.0
    """
    def __init__(self, string: str, string2: str, spacecraftParameters: SpacecraftParameters): ...

class StateVector(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class StateVector extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for state vector data.
    
        Since:
            11.0
    """
    def __init__(self): ...
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
    def setA(self, int: int, double: float) -> None:
        """
            Set acceleration component.
        
            Parameters:
                index (int): component index (counting from 0)
                value (double): acceleration component
        
        
        """
        ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of state vector, Keplerian elements and covariance matrix data.
        
            Parameters:
                epoch (:class:`~org.orekit.time.AbsoluteDate`): the epoch to be set
        
        
        """
        ...
    def setP(self, int: int, double: float) -> None:
        """
            Set position component.
        
            Parameters:
                index (int): component index (counting from 0)
                value (double): position component
        
        
        """
        ...
    def setV(self, int: int, double: float) -> None:
        """
            Set velocity component.
        
            Parameters:
                index (int): component index (counting from 0)
                value (double): velocity component
        
        
        """
        ...
    def toTimeStampedPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Convert to :class:`~org.orekit.utils.TimeStampedPVCoordinates`.
        
            Returns:
                a new :class:`~org.orekit.utils.TimeStampedPVCoordinates`
        
        
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

class StateVectorKey(java.lang.Enum['StateVectorKey']):
    """
    public enum StateVectorKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.StateVectorKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.StateVector` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, stateVector: StateVector) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.StateVector`): container to fill
        
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
    def valueOf(string: str) -> 'StateVectorKey':
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
    def values() -> typing.List['StateVectorKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (StateVectorKey c : StateVectorKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StateVectorWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class StateVectorWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for state vector data.
    
        Since:
            11.0
    """
    def __init__(self, string: str, string2: str, stateVector: StateVector, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter): ...

class UserDefined(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class UserDefined extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for user defined data.
    
        Since:
            11.0
    """
    USER_DEFINED_XML_TAG: typing.ClassVar[str] = ...
    """
    public static final String USER_DEFINED_XML_TAG
    
        Tag name for user defined parameters keys.
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_DEFINED_XML_ATTRIBUTE: typing.ClassVar[str] = ...
    """
    public static final String USER_DEFINED_XML_ATTRIBUTE
    
        Attribute name for user defined parameters keys.
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_DEFINED_PREFIX: typing.ClassVar[str] = ...
    """
    public static final String USER_DEFINED_PREFIX
    
        Prefix for user defined parameters keys.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def addEntry(self, string: str, string2: str) -> None:
        """
            Add a key/value entry.
        
            Parameters:
                key (String): parameter key, with the :meth:`~org.orekit.files.ccsds.ndm.odm.UserDefined.USER_DEFINED_PREFIX` stripped away
                value (String): parameter value
        
        
        """
        ...
    def getParameters(self) -> java.util.Map[str, str]:
        """
            Get all user defined parameters.
        
            The :meth:`~org.orekit.files.ccsds.ndm.odm.UserDefined.USER_DEFINED_PREFIX` has been stripped away from the keys.
        
            Returns:
                unmodifiable view of the map containing all user defined parameters
        
        
        """
        ...

class UserDefinedWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class UserDefinedWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for user defined parameters data.
    
        Since:
            11.0
    """
    def __init__(self, string: str, string2: str, userDefined: UserDefined): ...

class CommonMetadata(OdmMetadata):
    """
    public class CommonMetadata extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmMetadata`
    
        Common metadata for Orbit Parameter/Ephemeris/Mean Messages.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def finalizeMetadata(self, contextBinding: org.orekit.files.ccsds.utils.ContextBinding) -> None:
        """
            Finalize the metadata.
        
            ODM standard enforces :code:`TIME_SYSTEM` to appear *after* :code:`REF_FRAME_EPOCH`, despite it is needed to interpret
            it. We have to wait until parsing end to finalize this date.
        
        
            Parameters:
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
        
        
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
            Get the reference frame in which data are given: used for state vector and Keplerian elements data (and for the
            covariance reference frame if none is given).
        
            Returns:
                the reference frame
        
        
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
            Get the value of :code:`REF_FRAME` as an Orekit :class:`~org.orekit.frames.Frame`. The :code:`CENTER_NAME` key word has
            not been applied yet, so the returned frame may not correspond to the reference frame of the data in the file.
        
            Returns:
                The reference frame specified by the :code:`REF_FRAME` keyword.
        
            Also see:
                :meth:`~org.orekit.files.ccsds.ndm.odm.CommonMetadata.getFrame`
        
        
        """
        ...
    def setCenter(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
            Set the origin of reference frame.
        
            Parameters:
                center (:class:`~org.orekit.files.ccsds.definitions.BodyFacade`): origin of reference frame to be set
        
        
        """
        ...
    def setFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of reference frame, if not intrinsic to the definition of the reference frame.
        
            Parameters:
                frameEpoch (:class:`~org.orekit.time.AbsoluteDate`): the epoch of reference frame to be set
        
        
        """
        ...
    def setFrameEpochString(self, string: str) -> None:
        """
            Set epoch of reference frame, if not intrinsic to the definition of the reference frame.
        
            Parameters:
                frameEpochString (String): the epoch of reference frame to be set
        
        
        """
        ...
    def setObjectID(self, string: str) -> None:
        """
            Set the spacecraft ID for which the orbit state is provided.
        
            Parameters:
                objectID (String): the spacecraft ID to be set
        
        
        """
        ...
    def setReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set the reference frame in which data are given: used for state vector and Keplerian elements data (and for the
            covariance reference frame if none is given).
        
            Parameters:
                referenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
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

_PythonOdmParser__T = typing.TypeVar('_PythonOdmParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonOdmParser__P = typing.TypeVar('_PythonOdmParser__P', bound=OdmParser)  # <P>
class PythonOdmParser(OdmParser[_PythonOdmParser__T, _PythonOdmParser__P], typing.Generic[_PythonOdmParser__T, _PythonOdmParser__P]):
    """
    public class PythonOdmParser<T extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<?,?>,P extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmParser`<T,?>> extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmParser`<T,P>
    """
    def build(self) -> _PythonOdmParser__T:
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm")``.

    CartesianCovariance: typing.Type[CartesianCovariance]
    CartesianCovarianceKey: typing.Type[CartesianCovarianceKey]
    CartesianCovarianceWriter: typing.Type[CartesianCovarianceWriter]
    CommonMetadata: typing.Type[CommonMetadata]
    CommonMetadataKey: typing.Type[CommonMetadataKey]
    CommonMetadataWriter: typing.Type[CommonMetadataWriter]
    KeplerianElements: typing.Type[KeplerianElements]
    KeplerianElementsKey: typing.Type[KeplerianElementsKey]
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
