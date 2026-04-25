
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import org.orekit.data
import org.orekit.files.general
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class STKEphemerisFile(org.orekit.files.general.EphemerisFile[org.orekit.utils.TimeStampedPVCoordinates, 'STKEphemerisFile.STKEphemerisSegment']):
    """
    STK ephemeris file.
    
    Since:
        12.0
    """
    def __init__(self, stkVersion: str, satelliteId: str, ephemeris: 'STKEphemerisFile.STKEphemeris'):
        """
        Constructs a STKEphemerisFile instance.
        
        Parameters:
            stkVersion (String): STK version string (example: "stk.v.11.0")
            satelliteId (String): satellite id
            ephemeris (STKEphemeris): ephemeris
        
        
        """
        ...
    def getSTKVersion(self) -> str:
        """
        Returns the STK version string.
        
        Returns:
            STK version string
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'STKEphemerisFile.STKEphemeris']:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        STK ephemeris files define ephemeris for a single satellite, so the returned map will have a single entry.
        
        Specified by: getSatellites in interface EphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...
    class STKCoordinateSystem(java.lang.Enum['STKEphemerisFile.STKCoordinateSystem']):
        ICRF: typing.ClassVar['STKEphemerisFile.STKCoordinateSystem'] = ...
        J2000: typing.ClassVar['STKEphemerisFile.STKCoordinateSystem'] = ...
        INERTIAL: typing.ClassVar['STKEphemerisFile.STKCoordinateSystem'] = ...
        FIXED: typing.ClassVar['STKEphemerisFile.STKCoordinateSystem'] = ...
        TRUE_OF_DATE: typing.ClassVar['STKEphemerisFile.STKCoordinateSystem'] = ...
        MEAN_OF_DATE: typing.ClassVar['STKEphemerisFile.STKCoordinateSystem'] = ...
        TEME_OF_DATE: typing.ClassVar['STKEphemerisFile.STKCoordinateSystem'] = ...
        @staticmethod
        def parse(string: str) -> 'STKEphemerisFile.STKCoordinateSystem': ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'STKEphemerisFile.STKCoordinateSystem': ...
        @staticmethod
        def values() -> typing.MutableSequence['STKEphemerisFile.STKCoordinateSystem']: ...
    class STKEphemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, 'STKEphemerisFile.STKEphemerisSegment']):
        def __init__(self, string: str, double: float, list: java.util.List['STKEphemerisFile.STKEphemerisSegment']): ...
        def getId(self) -> str: ...
        def getMu(self) -> float: ...
        def getSegments(self) -> java.util.List['STKEphemerisFile.STKEphemerisSegment']: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...
    class STKEphemerisSegment(org.orekit.files.general.EphemerisFile.EphemerisSegment[org.orekit.utils.TimeStampedPVCoordinates]):
        def __init__(self, double: float, frame: org.orekit.frames.Frame, int: int, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, list: java.util.List[org.orekit.utils.TimeStampedPVCoordinates]): ...
        def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter: ...
        def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]: ...
        def getFrame(self) -> org.orekit.frames.Frame: ...
        def getInterpolationSamples(self) -> int: ...
        def getMu(self) -> float: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...

class STKEphemerisFileParser(org.orekit.files.general.EphemerisFileParser[STKEphemerisFile]):
    """
    Parser of STKEphemerisFiles.
    
    The STK ephemeris file format specification is quite extensive and this implementation does not attempt (nor is it possible, given the lack of an STK scenario to provide context) to support all possible variations of the format. The following keywords are recognized (case-insensitive):
    
    Any keyword in the format specification which is not explicitly named in the above table is not recognized and will cause a parse exception. Those keywords that are listed above as recognized but not supported are simply ignored.
    
    The following ephemeris formats are recognized and supported:
    
      - EphemerisTimePos
      - EphemerisTimePosVel
      - EphemerisTimePosVelAcc
    
    Any ephemeris format in the format specification which is not explicitly named in the above list is not recognized and will cause an exception.
    
    Since:
        12.0
    """
    def __init__(self, satelliteId: str, mu: float, utc: org.orekit.time.UTCScale, frameMapping: typing.Union[java.util.Map[STKEphemerisFile.STKCoordinateSystem, org.orekit.frames.Frame], typing.Mapping[STKEphemerisFile.STKCoordinateSystem, org.orekit.frames.Frame]]):
        """
        Constructs a STKEphemerisFileParser instance.
        
        Parameters:
            satelliteId (String): satellite id for satellites parsed by the parser
            mu (double): gravitational parameter (m^3/s^2)
            utc (UTCScale): UTC scale for parsed dates
            frameMapping (Map<STKCoordinateSystem, Frame> frameMapping): mapping from STK coordinate system to Orekit frame
        
        
        """
        ...
    def parse(self, source: org.orekit.data.DataSource) -> STKEphemerisFile:
        """
        Description copied from interface: parse Parse an ephemeris file from a data source.
        
        Specified by: parse in interface EphemerisFileParser
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed ephemeris file.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.stk")``.

    STKEphemerisFile: typing.Type[STKEphemerisFile]
    STKEphemerisFileParser: typing.Type[STKEphemerisFileParser]
