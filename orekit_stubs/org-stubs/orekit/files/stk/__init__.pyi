
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
    public class STKEphemerisFile extends :class:`~org.orekit.files.stk.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`, :class:`~org.orekit.files.stk.STKEphemerisFile.STKEphemerisSegment`>
    
        STK ephemeris file.
    
        Since:
            12.0
    """
    def __init__(self, string: str, string2: str, sTKEphemeris: 'STKEphemerisFile.STKEphemeris'): ...
    def getSTKVersion(self) -> str:
        """
            Returns the STK version string.
        
            Returns:
                STK version string
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'STKEphemerisFile.STKEphemeris']: ...
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
    public class STKEphemerisFileParser extends :class:`~org.orekit.files.stk.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFileParser`<:class:`~org.orekit.files.stk.STKEphemerisFile`>
    
        Parser of :class:`~org.orekit.files.stk.STKEphemerisFile`s.
    
        The STK ephemeris file format specification is quite extensive and this implementation does not attempt (nor is it
        possible, given the lack of an STK scenario to provide context) to support all possible variations of the format. The
        following keywords are recognized (case-insensitive):
    
        Any keyword in the format specification which is not explicitly named in the above table is not recognized and will
        cause a parse exception. Those keywords that are listed above as recognized but not supported are simply ignored.
    
        The following ephemeris formats are recognized and supported:
    
          - EphemerisTimePos
          - EphemerisTimePosVel
          - EphemerisTimePosVelAcc
    
        Any ephemeris format in the format specification which is not explicitly named in the above list is not recognized and
        will cause an exception.
    
        Since:
            12.0
    """
    def __init__(self, string: str, double: float, uTCScale: org.orekit.time.UTCScale, map: typing.Union[java.util.Map[STKEphemerisFile.STKCoordinateSystem, org.orekit.frames.Frame], typing.Mapping[STKEphemerisFile.STKCoordinateSystem, org.orekit.frames.Frame]]): ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> STKEphemerisFile:
        """
            Description copied from interface: :meth:`~org.orekit.files.general.EphemerisFileParser.parse`
            Parse an ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFileParser.parse` in
                interface :class:`~org.orekit.files.general.EphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed ephemeris file.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.stk")``.

    STKEphemerisFile: typing.Type[STKEphemerisFile]
    STKEphemerisFileParser: typing.Type[STKEphemerisFileParser]
