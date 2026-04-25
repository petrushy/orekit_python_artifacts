
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
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
    An interface for accessing the data stored in an attitude ephemeris file.
    
    An AttitudeEphemerisFile consists of one or more satellites each with a unique ID within the file. The ephemeris for each satellite consists of one or more segments.
    
    Some attitude ephemeris file formats may supply additional information that is not available via this interface. In those cases it is recommended that the parser return a subclass of this interface to provide access to the additional information.
    
    Since:
        10.3
    
    Also see:
        SatelliteAttitudeEphemeris,
        AttitudeEphemerisSegment
    """
    def getSatellites(self) -> java.util.Map[str, 'AttitudeEphemerisFile.SatelliteAttitudeEphemeris'[_AttitudeEphemerisFile__C, _AttitudeEphemerisFile__S]]:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...
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
    Parse an ephemeris file.
    
    Since:
        10.3
    """
    def parse(self, source: org.orekit.data.DataSource) -> _AttitudeEphemerisFileParser__T:
        """
        Parse an attitude ephemeris file from a data source.
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed attitude ephemeris file.
        
        
        """
        ...

class AttitudeEphemerisFileWriter:
    """
    An interface for writing out ephemeris files to disk.
    
    An AttitudeEphemerisFile consists of one or more satellites each an ID unique within the file. The ephemeris for each satellite consists of one or more segments.
    
    Ephemeris file formats may have additional settings that need to be configured to be compliant with their formats.
    
    Since:
        10.3
    """
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=AttitudeEphemerisFile.AttitudeEphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=AttitudeEphemerisFile.AttitudeEphemerisSegment)  # <S>
    @typing.overload
    def write(self, appendable: java.lang.Appendable, attitudeEphemerisFile: typing.Union[AttitudeEphemerisFile[_write_0__C, _write_0__S], typing.Callable[[], java.util.Map[str, AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, AttitudeEphemerisFile.AttitudeEphemerisSegment]]]]) -> None: ...
    @typing.overload
    def write(self, string: str, attitudeEphemerisFile: typing.Union[AttitudeEphemerisFile[_write_1__C, _write_1__S], typing.Callable[[], java.util.Map[str, AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, AttitudeEphemerisFile.AttitudeEphemerisSegment]]]]) -> None: ...

_EphemerisFile__EphemerisSegment__C = typing.TypeVar('_EphemerisFile__EphemerisSegment__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
_EphemerisFile__SatelliteEphemeris__C = typing.TypeVar('_EphemerisFile__SatelliteEphemeris__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
_EphemerisFile__SatelliteEphemeris__S = typing.TypeVar('_EphemerisFile__SatelliteEphemeris__S', bound='EphemerisFile.EphemerisSegment')  # <S>
_EphemerisFile__C = typing.TypeVar('_EphemerisFile__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
_EphemerisFile__S = typing.TypeVar('_EphemerisFile__S', bound='EphemerisFile.EphemerisSegment')  # <S>
class EphemerisFile(typing.Generic[_EphemerisFile__C, _EphemerisFile__S]):
    """
    An interface for accessing the data stored in an ephemeris file and using the data to create a working Propagator.
    
    An EphemerisFile consists of one or more satellites each with a unique ID within the file. The ephemeris for each satellite consists of one or more segments.
    
    Some ephemeris file formats may supply additional information that is not available via this interface. In those cases it is recommended that the parser return a subclass of this interface to provide access to the additional information.
    
    Also see:
        SatelliteEphemeris,
        EphemerisSegment
    """
    def getSatellites(self) -> java.util.Map[str, 'EphemerisFile.SatelliteEphemeris'[_EphemerisFile__C, _EphemerisFile__S]]:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...
    class EphemerisSegment(typing.Generic[_EphemerisFile__EphemerisSegment__C]):
        def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter: ...
        def getCoordinates(self) -> java.util.List[_EphemerisFile__EphemerisSegment__C]: ...
        def getFrame(self) -> org.orekit.frames.Frame: ...
        def getInertialFrame(self) -> org.orekit.frames.Frame: ...
        def getInterpolationSamples(self) -> int: ...
        def getMu(self) -> float: ...
        @typing.overload
        def getPropagator(self) -> org.orekit.propagation.BoundedPropagator: ...
        @typing.overload
        def getPropagator(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> org.orekit.propagation.BoundedPropagator: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...
    class SatelliteEphemeris(typing.Generic[_EphemerisFile__SatelliteEphemeris__C, _EphemerisFile__SatelliteEphemeris__S]):
        def getId(self) -> str: ...
        def getMu(self) -> float: ...
        @typing.overload
        def getPropagator(self) -> org.orekit.propagation.BoundedPropagator: ...
        @typing.overload
        def getPropagator(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> org.orekit.propagation.BoundedPropagator: ...
        def getSegments(self) -> java.util.List[_EphemerisFile__SatelliteEphemeris__S]: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...

_EphemerisFileParser__T = typing.TypeVar('_EphemerisFileParser__T', bound=EphemerisFile)  # <T>
class EphemerisFileParser(typing.Generic[_EphemerisFileParser__T]):
    """
    Parse an ephemeris file.
    """
    def parse(self, source: org.orekit.data.DataSource) -> _EphemerisFileParser__T:
        """
        Parse an ephemeris file from a data source.
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed ephemeris file.
        
        
        """
        ...

class EphemerisFileWriter:
    """
    An interface for writing out ephemeris files to disk.
    
    An EphemerisFile consists of one or more satellites each an ID unique within the file. The ephemeris for each satellite consists of one or more segments.
    
    Ephemeris file formats may have additional settings that need to be configured to be compliant with their formats.
    
    Since:
        9.0
    """
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=EphemerisFile.EphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=EphemerisFile.EphemerisSegment)  # <S>
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: typing.Union[EphemerisFile[_write_0__C, _write_0__S], typing.Callable[[], java.util.Map[str, EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, EphemerisFile.EphemerisSegment]]]]) -> None: ...
    @typing.overload
    def write(self, string: str, ephemerisFile: typing.Union[EphemerisFile[_write_1__C, _write_1__S], typing.Callable[[], java.util.Map[str, EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, EphemerisFile.EphemerisSegment]]]]) -> None: ...

_EphemerisSegmentPropagator__C = typing.TypeVar('_EphemerisSegmentPropagator__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
class EphemerisSegmentPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator, org.orekit.propagation.BoundedPropagator, typing.Generic[_EphemerisSegmentPropagator__C]):
    """
    A Propagator based on a EphemerisSegment.
    
    The getPVCoordinates is implemented without using the propagate methods so using this class as a PVCoordinatesProvider still behaves as expected when the ephemeris file did not have a valid gravitational parameter.
    """
    def __init__(self, ephemeris: EphemerisFile.EphemerisSegment[_EphemerisSegmentPropagator__C], attitudeProvider: org.orekit.attitudes.AttitudeProvider):
        """
        Create a Propagator from an ephemeris segment.
        
        Parameters:
            ephemeris (EphemerisSegment<EphemerisSegmentPropagator> ephemeris): segment containing the data for this propagator.
            attitudeProvider (AttitudeProvider): provider for attitude computation
        
        
        """
        ...
    def getInitialState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Description copied from class: getInitialState Get the propagator initial state.
        
        Specified by: getInitialState in interface Propagator
        
        Overrides: getInitialState in class AbstractPropagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getMaxDate Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getMinDate Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Description copied from interface: getPVCoordinates Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface Propagator
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from interface: getPosition Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface Propagator
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Description copied from class: propagateOrbit Extrapolate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Description copied from class: resetInitialState Reset the propagator initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...

class OrekitAttitudeEphemerisFile(AttitudeEphemerisFile[org.orekit.utils.TimeStampedAngularCoordinates, 'OrekitAttitudeEphemerisFile.OrekitAttitudeEphemerisSegment']):
    """
    A class for encapsulating Orekit propagators within an AttitudeEphemerisFile complaint object that makes for easy serialization to external ephemeris formats like AEM.
    
    Since:
        10.3
    """
    def __init__(self):
        """
        Standard default constructor.
        """
        ...
    def addSatellite(self, id: str) -> 'OrekitAttitudeEphemerisFile.OrekitSatelliteAttitudeEphemeris':
        """
        Adds a new satellite to this object.
        
        Parameters:
            id (String): ID to use for this satellite
        
        Returns:
            the new satellite object
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OrekitAttitudeEphemerisFile.OrekitSatelliteAttitudeEphemeris']:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Specified by: getSatellites in interface AttitudeEphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...
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
    A class for encapsulating Orekit propagators within an EphemerisFile complaint object that makes for easy serialization to external ephemeris formats like OEM.
    
    Since:
        9.0
    """
    def __init__(self):
        """
        Standard default constructor.
        """
        ...
    def addSatellite(self, id: str) -> 'OrekitEphemerisFile.OrekitSatelliteEphemeris':
        """
        Adds a new satellite to this object.
        
        Parameters:
            id (String): ID to use for this satellite
        
        Returns:
            the new satellite object
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OrekitEphemerisFile.OrekitSatelliteEphemeris']:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Specified by: getSatellites in interface EphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...
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

class PythonAttitudeEphemerisFile(AttitudeEphemerisFile):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, AttitudeEphemerisFile.SatelliteAttitudeEphemeris]:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Specified by: getSatellites in interface AttitudeEphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
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

class PythonAttitudeEphemerisFileParser(AttitudeEphemerisFileParser):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def parse(self, source: org.orekit.data.DataSource) -> AttitudeEphemerisFile[typing.Any, typing.Any]:
        """
        Parse an attitude ephemeris file from a data source.
        
        Specified by: parse in interface AttitudeEphemerisFileParser
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed attitude ephemeris file.
        
        
        """
        ...
    def parse_BS(self, reader: java.io.BufferedReader, fileName: str) -> AttitudeEphemerisFile:
        """
        Parse an attitude ephemeris file from a stream.
        
        Parameters:
            reader (BufferedReader): containing the ephemeris file.
            fileName (String): to use in error messages.
        
        Returns:
            a parsed ephemeris file.
        
        Raises:
            IOException: if reader throws one.
        
        
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

class PythonAttitudeEphemerisFileWriter(AttitudeEphemerisFileWriter):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=AttitudeEphemerisFile.AttitudeEphemerisSegment)  # <S>
    @typing.overload
    def write(self, string: str, attitudeEphemerisFile: typing.Union[AttitudeEphemerisFile[_write_0__C, _write_0__S], typing.Callable[[], java.util.Map[str, AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, AttitudeEphemerisFile.AttitudeEphemerisSegment]]]]) -> None: ...
    @typing.overload
    def write(self, appendable: java.lang.Appendable, attitudeEphemerisFile: typing.Union[AttitudeEphemerisFile, typing.Callable]) -> None: ...

class PythonAttitudeEphemerisSegment(AttitudeEphemerisFile.AttitudeEphemerisSegment):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAngularCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]:
        """
        Get an unmodifiable list of attitude data lines.
        
        Specified by: getAngularCoordinates in interface AttitudeEphemerisSegment
        
        Returns:
            a list of attitude data
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider:
        """
        Get the attitude provider for this attitude ephemeris segment.
        
        Specified by: getAttitudeProvider in interface AttitudeEphemerisSegment
        
        Returns:
            the attitude provider for this attitude ephemeris segment.
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
        Get which derivatives of angular data are available in this attitude ephemeris segment.
        
        Specified by: getAvailableDerivatives in interface AttitudeEphemerisSegment
        
        Returns:
            a value indicating if the file contains rotation and/or rotation rate and/or acceleration data.
        
        
        """
        ...
    def getInterpolationMethod(self) -> str:
        """
        Get the interpolation method to be used.
        
        Specified by: getInterpolationMethod in interface AttitudeEphemerisSegment
        
        Returns:
            the interpolation method
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
        Get the number of samples to use in interpolation.
        
        Specified by: getInterpolationSamples in interface AttitudeEphemerisSegment
        
        Returns:
            the number of points to use for interpolation.
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame from which attitude is defined.
        
        Specified by: getReferenceFrame in interface AttitudeEphemerisSegment
        
        Returns:
            the reference frame from which attitude is defined
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of this ephemeris segment.
        
        Specified by: getStart in interface AttitudeEphemerisSegment
        
        Returns:
            ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of this ephemeris segment.
        
        Specified by: getStop in interface AttitudeEphemerisSegment
        
        Returns:
            ephemeris segment end date.
        
        
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

class PythonEphemerisFile(EphemerisFile):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, EphemerisFile.SatelliteEphemeris]:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Specified by: getSatellites in interface EphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
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

class PythonEphemerisFileParser(EphemerisFileParser):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def parse(self, source: org.orekit.data.DataSource) -> EphemerisFile[typing.Any, typing.Any]:
        """
        Parse an ephemeris file from a data source.
        
        Specified by: parse in interface EphemerisFileParser
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed ephemeris file.
        
        
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

class PythonEphemerisFileWriter(EphemerisFileWriter):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: typing.Union[EphemerisFile, typing.Callable]) -> None: ...
    @typing.overload
    def write(self, string: str, ephemerisFile: typing.Union[EphemerisFile, typing.Callable]) -> None: ...

class PythonSatelliteAttitudeEphemeris(AttitudeEphemerisFile.SatelliteAttitudeEphemeris):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider:
        """
        Get the attitude provider corresponding to this ephemeris, combining data from all getSegments.
        
        Specified by: getAttitudeProvider in interface SatelliteAttitudeEphemeris
        
        Returns:
            an attitude provider for all the data in this attitude ephemeris file.
        
        
        """
        ...
    def getId(self) -> str:
        """
        Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
        Specified by: getId in interface SatelliteAttitudeEphemeris
        
        Returns:
            the satellite's ID, never null.
        
        
        """
        ...
    def getSegments(self) -> java.util.List[AttitudeEphemerisFile.AttitudeEphemerisSegment]:
        """
        Get the segments of the attitude ephemeris.
        
        Attitude ephemeris segments are typically used to split an ephemeris around discontinuous events.
        
        Specified by: getSegments in interface SatelliteAttitudeEphemeris
        
        Returns:
            the segments contained in the attitude ephemeris file for this satellite.
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of the ephemeris.
        
        Specified by: getStart in interface SatelliteAttitudeEphemeris
        
        Returns:
            ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of the ephemeris.
        
        Specified by: getStop in interface SatelliteAttitudeEphemeris
        
        Returns:
            ephemeris end date.
        
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.general")``.

    AttitudeEphemerisFile: typing.Type[AttitudeEphemerisFile]
    AttitudeEphemerisFileParser: typing.Type[AttitudeEphemerisFileParser]
    AttitudeEphemerisFileWriter: typing.Type[AttitudeEphemerisFileWriter]
    EphemerisFile: typing.Type[EphemerisFile]
    EphemerisFileParser: typing.Type[EphemerisFileParser]
    EphemerisFileWriter: typing.Type[EphemerisFileWriter]
    EphemerisSegmentPropagator: typing.Type[EphemerisSegmentPropagator]
    OrekitAttitudeEphemerisFile: typing.Type[OrekitAttitudeEphemerisFile]
    OrekitEphemerisFile: typing.Type[OrekitEphemerisFile]
    PythonAttitudeEphemerisFile: typing.Type[PythonAttitudeEphemerisFile]
    PythonAttitudeEphemerisFileParser: typing.Type[PythonAttitudeEphemerisFileParser]
    PythonAttitudeEphemerisFileWriter: typing.Type[PythonAttitudeEphemerisFileWriter]
    PythonAttitudeEphemerisSegment: typing.Type[PythonAttitudeEphemerisSegment]
    PythonEphemerisFile: typing.Type[PythonEphemerisFile]
    PythonEphemerisFileParser: typing.Type[PythonEphemerisFileParser]
    PythonEphemerisFileWriter: typing.Type[PythonEphemerisFileWriter]
    PythonSatelliteAttitudeEphemeris: typing.Type[PythonSatelliteAttitudeEphemeris]
