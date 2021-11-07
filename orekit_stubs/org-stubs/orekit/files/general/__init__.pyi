import java.lang
import java.util
import org.orekit.attitudes
import org.orekit.bodies
import org.orekit.data
import org.orekit.files.general.class-use
import org.orekit.frames
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



_AttitudeEphemerisFile__AttitudeEphemerisSegment__C = typing.TypeVar('_AttitudeEphemerisFile__AttitudeEphemerisSegment__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
_AttitudeEphemerisFile__SatelliteAttitudeEphemeris__C = typing.TypeVar('_AttitudeEphemerisFile__SatelliteAttitudeEphemeris__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
_AttitudeEphemerisFile__SatelliteAttitudeEphemeris__S = typing.TypeVar('_AttitudeEphemerisFile__SatelliteAttitudeEphemeris__S', bound='AttitudeEphemerisFile.AttitudeEphemerisSegment')  # <S>
_AttitudeEphemerisFile__C = typing.TypeVar('_AttitudeEphemerisFile__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
_AttitudeEphemerisFile__S = typing.TypeVar('_AttitudeEphemerisFile__S', bound='AttitudeEphemerisFile.AttitudeEphemerisSegment')  # <S>
class AttitudeEphemerisFile(typing.Generic[_AttitudeEphemerisFile__C, _AttitudeEphemerisFile__S]):
    """
    public interface AttitudeEphemerisFile<C extends :class:`~org.orekit.utils.TimeStampedAngularCoordinates`,S extends :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`<C>>
    
        An interface for accessing the data stored in an attitude ephemeris file.
    
        An :class:`~org.orekit.files.general.AttitudeEphemerisFile` consists of one or more satellites each with a unique ID
        within the file. The ephemeris for each satellite consists of one or more segments.
    
        Some attitude ephemeris file formats may supply additional information that is not available via this interface. In
        those cases it is recommended that the parser return a subclass of this interface to provide access to the additional
        information.
    
        Since:
            10.3
    
        Also see:
            :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`,
            :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
    """
    def getSatellites(self) -> java.util.Map[str, 'AttitudeEphemerisFile.SatelliteAttitudeEphemeris'[_AttitudeEphemerisFile__C, _AttitudeEphemerisFile__S]]: ...
    class AttitudeEphemerisSegment(typing.Generic[_AttitudeEphemerisFile__AttitudeEphemerisSegment__C]):
        def getAngularCoordinates(self) -> java.util.List[_AttitudeEphemerisFile__AttitudeEphemerisSegment__C]: ...
        def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider: ...
        def getAvailableDerivatives(self) -> org.orekit.utils.AngularDerivativesFilter: ...
        def getInterpolationMethod(self) -> str: ...
        def getInterpolationSamples(self) -> int: ...
        def getReferenceFrame(self) -> org.orekit.frames.Frame: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...
    class SatelliteAttitudeEphemeris(typing.Generic[_AttitudeEphemerisFile__SatelliteAttitudeEphemeris__C, _AttitudeEphemerisFile__SatelliteAttitudeEphemeris__S]):
        def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider: ...
        def getId(self) -> str: ...
        def getSegments(self) -> java.util.List[_AttitudeEphemerisFile__SatelliteAttitudeEphemeris__S]: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...

_AttitudeEphemerisFileParser__T = typing.TypeVar('_AttitudeEphemerisFileParser__T', bound=AttitudeEphemerisFile)  # <T>
class AttitudeEphemerisFileParser(typing.Generic[_AttitudeEphemerisFileParser__T]):
    """
    public interface AttitudeEphemerisFileParser<T extends :class:`~org.orekit.files.general.AttitudeEphemerisFile`<?,?>>
    
        Parse an ephemeris file.
    
        Since:
            10.3
    """
    def parse(self, dataSource: org.orekit.data.DataSource) -> _AttitudeEphemerisFileParser__T:
        """
            Parse an attitude ephemeris file from a data source.
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed attitude ephemeris file.
        
        
        """
        ...

class AttitudeEphemerisFileWriter:
    """
    public interface AttitudeEphemerisFileWriter
    
        An interface for writing out ephemeris files to disk.
    
        An :class:`~org.orekit.files.general.AttitudeEphemerisFile` consists of one or more satellites each an ID unique within
        the file. The ephemeris for each satellite consists of one or more segments.
    
        Ephemeris file formats may have additional settings that need to be configured to be compliant with their formats.
    
        Since:
            10.3
    """
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=AttitudeEphemerisFile.AttitudeEphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=AttitudeEphemerisFile.AttitudeEphemerisSegment)  # <S>
    @typing.overload
    def write(self, appendable: java.lang.Appendable, attitudeEphemerisFile: AttitudeEphemerisFile[_write_0__C, _write_0__S]) -> None: ...
    @typing.overload
    def write(self, string: str, attitudeEphemerisFile: AttitudeEphemerisFile[_write_1__C, _write_1__S]) -> None: ...

_EphemerisFile__EphemerisSegment__C = typing.TypeVar('_EphemerisFile__EphemerisSegment__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
_EphemerisFile__SatelliteEphemeris__C = typing.TypeVar('_EphemerisFile__SatelliteEphemeris__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
_EphemerisFile__SatelliteEphemeris__S = typing.TypeVar('_EphemerisFile__SatelliteEphemeris__S', bound='EphemerisFile.EphemerisSegment')  # <S>
_EphemerisFile__C = typing.TypeVar('_EphemerisFile__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
_EphemerisFile__S = typing.TypeVar('_EphemerisFile__S', bound='EphemerisFile.EphemerisSegment')  # <S>
class EphemerisFile(typing.Generic[_EphemerisFile__C, _EphemerisFile__S]):
    """
    public interface EphemerisFile<C extends :class:`~org.orekit.utils.TimeStampedPVCoordinates`,S extends :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`<C>>
    
        An interface for accessing the data stored in an ephemeris file and using the data to create a working
        :class:`~org.orekit.propagation.Propagator`.
    
        An :class:`~org.orekit.files.general.EphemerisFile` consists of one or more satellites each with a unique ID within the
        file. The ephemeris for each satellite consists of one or more segments.
    
        Some ephemeris file formats may supply additional information that is not available via this interface. In those cases
        it is recommended that the parser return a subclass of this interface to provide access to the additional information.
    
        Also see:
            :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`,
            :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
    """
    def getSatellites(self) -> java.util.Map[str, 'EphemerisFile.SatelliteEphemeris'[_EphemerisFile__C, _EphemerisFile__S]]: ...
    class EphemerisSegment(typing.Generic[_EphemerisFile__EphemerisSegment__C]):
        def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter: ...
        def getCoordinates(self) -> java.util.List[_EphemerisFile__EphemerisSegment__C]: ...
        def getFrame(self) -> org.orekit.frames.Frame: ...
        def getInertialFrame(self) -> org.orekit.frames.Frame: ...
        def getInterpolationSamples(self) -> int: ...
        def getMu(self) -> float: ...
        def getPropagator(self) -> org.orekit.propagation.BoundedPropagator: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...
    class SatelliteEphemeris(typing.Generic[_EphemerisFile__SatelliteEphemeris__C, _EphemerisFile__SatelliteEphemeris__S]):
        def getId(self) -> str: ...
        def getMu(self) -> float: ...
        def getPropagator(self) -> org.orekit.propagation.BoundedPropagator: ...
        def getSegments(self) -> java.util.List[_EphemerisFile__SatelliteEphemeris__S]: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...

_EphemerisFileParser__T = typing.TypeVar('_EphemerisFileParser__T', bound=EphemerisFile)  # <T>
class EphemerisFileParser(typing.Generic[_EphemerisFileParser__T]):
    """
    public interface EphemerisFileParser<T extends :class:`~org.orekit.files.general.EphemerisFile`<?,?>>
    
        Parse an ephemeris file.
    """
    def parse(self, dataSource: org.orekit.data.DataSource) -> _EphemerisFileParser__T:
        """
            Parse an ephemeris file from a data source.
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed ephemeris file.
        
        
        """
        ...

class EphemerisFileWriter:
    """
    public interface EphemerisFileWriter
    
        An interface for writing out ephemeris files to disk.
    
        An :class:`~org.orekit.files.general.EphemerisFile` consists of one or more satellites each an ID unique within the
        file. The ephemeris for each satellite consists of one or more segments.
    
        Ephemeris file formats may have additional settings that need to be configured to be compliant with their formats.
    
        Since:
            9.0
    """
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=EphemerisFile.EphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=EphemerisFile.EphemerisSegment)  # <S>
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: EphemerisFile[_write_0__C, _write_0__S]) -> None: ...
    @typing.overload
    def write(self, string: str, ephemerisFile: EphemerisFile[_write_1__C, _write_1__S]) -> None: ...

class OrekitAttitudeEphemerisFile(AttitudeEphemerisFile[org.orekit.utils.TimeStampedAngularCoordinates, 'OrekitAttitudeEphemerisFile.OrekitAttitudeEphemerisSegment']):
    """
    public class OrekitAttitudeEphemerisFile extends :class:`~org.orekit.files.general.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.AttitudeEphemerisFile`<:class:`~org.orekit.utils.TimeStampedAngularCoordinates`,:class:`~org.orekit.files.general.OrekitAttitudeEphemerisFile.OrekitAttitudeEphemerisSegment`>
    
        A class for encapsulating Orekit propagators within an :class:`~org.orekit.files.general.AttitudeEphemerisFile`
        complaint object that makes for easy serialization to external ephemeris formats like AEM.
    
        Since:
            10.3
    """
    def __init__(self): ...
    def addSatellite(self, string: str) -> 'OrekitAttitudeEphemerisFile.OrekitSatelliteAttitudeEphemeris':
        """
            Adds a new satellite to this object.
        
            Parameters:
                id (:class:`~org.orekit.files.general.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): ID to use for this satellite
        
            Returns:
                the new satellite object
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OrekitAttitudeEphemerisFile.OrekitSatelliteAttitudeEphemeris']: ...
    class OrekitAttitudeEphemerisSegment(AttitudeEphemerisFile.AttitudeEphemerisSegment[org.orekit.utils.TimeStampedAngularCoordinates]):
        def __init__(self, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], string: str, int: int, frame: org.orekit.frames.Frame, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
        def getAngularCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]: ...
        def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider: ...
        def getAvailableDerivatives(self) -> org.orekit.utils.AngularDerivativesFilter: ...
        def getInterpolationMethod(self) -> str: ...
        def getInterpolationSamples(self) -> int: ...
        def getReferenceFrame(self) -> org.orekit.frames.Frame: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...
    class OrekitSatelliteAttitudeEphemeris(AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, 'OrekitAttitudeEphemerisFile.OrekitAttitudeEphemerisSegment']):
        DEFAULT_INTERPOLATION_METHOD: typing.ClassVar[str] = ...
        DEFAULT_INTERPOLATION_SIZE: typing.ClassVar[int] = ...
        def __init__(self, string: str): ...
        def addNewSegment(self, list: java.util.List[org.orekit.propagation.SpacecraftState], string: str, int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter) -> 'OrekitAttitudeEphemerisFile.OrekitAttitudeEphemerisSegment': ...
        def getId(self) -> str: ...
        def getSegments(self) -> java.util.List['OrekitAttitudeEphemerisFile.OrekitAttitudeEphemerisSegment']: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...

class OrekitEphemerisFile(EphemerisFile[org.orekit.utils.TimeStampedPVCoordinates, 'OrekitEphemerisFile.OrekitEphemerisSegment']):
    """
    public class OrekitEphemerisFile extends :class:`~org.orekit.files.general.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`,:class:`~org.orekit.files.general.OrekitEphemerisFile.OrekitEphemerisSegment`>
    
        A class for encapsulating Orekit propagators within an :class:`~org.orekit.files.general.EphemerisFile` complaint object
        that makes for easy serialization to external ephemeris formats like OEM.
    
        Since:
            9.0
    """
    def __init__(self): ...
    def addSatellite(self, string: str) -> 'OrekitEphemerisFile.OrekitSatelliteEphemeris':
        """
            Adds a new satellite to this object.
        
            Parameters:
                id (:class:`~org.orekit.files.general.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): ID to use for this satellite
        
            Returns:
                the new satellite object
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OrekitEphemerisFile.OrekitSatelliteEphemeris']: ...
    class OrekitEphemerisSegment(EphemerisFile.EphemerisSegment[org.orekit.utils.TimeStampedPVCoordinates]):
        def __init__(self, list: java.util.List[org.orekit.utils.TimeStampedPVCoordinates], frame: org.orekit.frames.Frame, double: float, int: int): ...
        def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter: ...
        def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]: ...
        def getFrame(self) -> org.orekit.frames.Frame: ...
        def getInertialFrame(self) -> org.orekit.frames.Frame: ...
        def getInterpolationSamples(self) -> int: ...
        def getMu(self) -> float: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...
    class OrekitSatelliteEphemeris(EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, 'OrekitEphemerisFile.OrekitEphemerisSegment']):
        DEFAULT_INTERPOLATION_SIZE: typing.ClassVar[int] = ...
        def __init__(self, string: str): ...
        @typing.overload
        def addNewSegment(self, list: java.util.List[org.orekit.propagation.SpacecraftState]) -> 'OrekitEphemerisFile.OrekitEphemerisSegment': ...
        @typing.overload
        def addNewSegment(self, list: java.util.List[org.orekit.propagation.SpacecraftState], int: int) -> 'OrekitEphemerisFile.OrekitEphemerisSegment': ...
        @typing.overload
        def addNewSegment(self, list: java.util.List[org.orekit.propagation.SpacecraftState], celestialBody: org.orekit.bodies.CelestialBody, int: int) -> 'OrekitEphemerisFile.OrekitEphemerisSegment': ...
        @typing.overload
        def addNewSegment(self, list: java.util.List[org.orekit.propagation.SpacecraftState], celestialBody: org.orekit.bodies.CelestialBody, int: int, timeScale: org.orekit.time.TimeScale) -> 'OrekitEphemerisFile.OrekitEphemerisSegment': ...
        def getId(self) -> str: ...
        def getMu(self) -> float: ...
        def getSegments(self) -> java.util.List['OrekitEphemerisFile.OrekitEphemerisSegment']: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.general")``.

    AttitudeEphemerisFile: typing.Type[AttitudeEphemerisFile]
    AttitudeEphemerisFileParser: typing.Type[AttitudeEphemerisFileParser]
    AttitudeEphemerisFileWriter: typing.Type[AttitudeEphemerisFileWriter]
    EphemerisFile: typing.Type[EphemerisFile]
    EphemerisFileParser: typing.Type[EphemerisFileParser]
    EphemerisFileWriter: typing.Type[EphemerisFileWriter]
    OrekitAttitudeEphemerisFile: typing.Type[OrekitAttitudeEphemerisFile]
    OrekitEphemerisFile: typing.Type[OrekitEphemerisFile]
    class-use: org.orekit.files.general.class-use.__module_protocol__
