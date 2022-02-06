import java.lang
import java.util
import java.util.function
import org.hipparchus.geometry.euclidean.threed
import org.orekit.data
import org.orekit.files.general
import org.orekit.frames
import org.orekit.gnss
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



class SP3(org.orekit.files.general.EphemerisFile['SP3.SP3Coordinate', 'SP3.SP3Ephemeris']):
    """
    public class SP3 extends Object implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.files.sp3.SP3.SP3Coordinate`,:class:`~org.orekit.files.sp3.SP3.SP3Ephemeris`>
    
        Represents a parsed SP3 orbit file.
    """
    SP3_FRAME_CENTER_STRING: typing.ClassVar[str] = ...
    """
    public static final String SP3_FRAME_CENTER_STRING
    
        String representation of the center of ephemeris coordinate system.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, double: float, int: int, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]]): ...
    def addSatellite(self, string: str) -> None:
        """
            Add a new satellite with a given identifier to the list of stored satellites.
        
            Parameters:
                satId (String): the satellite identifier
        
        
        """
        ...
    def addSatelliteCoordinate(self, string: str, sP3Coordinate: 'SP3.SP3Coordinate') -> None:
        """
            Adds a new P/V coordinate for a given satellite.
        
            Parameters:
                satId (String): the satellite identifier
                coord (:class:`~org.orekit.files.sp3.SP3.SP3Coordinate`): the P/V coordinate of the satellite
        
        
        """
        ...
    def containsSatellite(self, string: str) -> bool:
        """
            Tests whether a satellite with the given id is contained in this orbit file.
        
            Parameters:
                satId (String): the satellite id
        
            Returns:
                :code:`true` if the satellite is contained in the file, :code:`false` otherwise
        
        
        """
        ...
    def getAccuracy(self, int: int) -> float:
        """
            Get the formal accuracy for a satellite.
        
            Parameters:
                index (int): is the index of the satellite.
        
            Returns:
                accuracy of the satellite, in m.
        
        
        """
        ...
    def getAgency(self) -> str:
        """
            Returns the agency that prepared this SP3 file.
        
            Returns:
                the agency
        
        
        """
        ...
    def getCoordinateSystem(self) -> str:
        """
            Returns the coordinate system of the entries in this orbit file.
        
            Returns:
                the coordinate system
        
        
        """
        ...
    def getDataUsed(self) -> str:
        """
            Returns the data used indicator from the SP3 file.
        
            Returns:
                the data used indicator (unparsed)
        
        
        """
        ...
    def getDayFraction(self) -> float:
        """
            Returns the day fraction for this SP3 file.
        
            Returns:
                the day fraction
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Returns the start epoch of the orbit file.
        
            Returns:
                the start epoch
        
        
        """
        ...
    def getEpochInterval(self) -> float:
        """
            Returns the time interval between epochs (in seconds).
        
            Returns:
                the time interval between epochs
        
        
        """
        ...
    def getGpsWeek(self) -> int:
        """
            Returns the GPS week as contained in the SP3 file.
        
            Returns:
                the GPS week of the SP3 file
        
        
        """
        ...
    def getJulianDay(self) -> int:
        """
            Returns the julian day for this SP3 file.
        
            Returns:
                the julian day
        
        
        """
        ...
    def getNumberOfEpochs(self) -> int:
        """
            Returns the number of epochs contained in this orbit file.
        
            Returns:
                the number of epochs
        
        
        """
        ...
    def getOrbitType(self) -> 'SP3.SP3OrbitType':
        """
            Returns the :class:`~org.orekit.files.sp3.SP3.SP3OrbitType` for this SP3 file.
        
            Returns:
                the orbit type
        
        
        """
        ...
    def getOrbitTypeKey(self) -> str:
        """
            Returns the orbit type key for this SP3 file.
        
            Returns:
                the orbit type key
        
            Since:
                9.3
        
        
        """
        ...
    def getSatelliteCount(self) -> int:
        """
            Get the number of satellites contained in this orbit file.
        
            Returns:
                the number of satellites
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'SP3.SP3Ephemeris']: ...
    def getSecondsOfWeek(self) -> float:
        """
            Returns the seconds of the GPS week as contained in the SP3 file.
        
            Returns:
                the seconds of the GPS week
        
        
        """
        ...
    def getTimeSystem(self) -> org.orekit.gnss.TimeSystem:
        """
            Returns the :class:`~org.orekit.gnss.TimeSystem` used to time-stamp position entries.
        
            Returns:
                the :class:`~org.orekit.gnss.TimeSystem` of the orbit file
        
        
        """
        ...
    def getType(self) -> 'SP3.SP3FileType':
        """
            Returns the :class:`~org.orekit.files.sp3.SP3.SP3FileType` associated with this SP3 file.
        
            Returns:
                the file type for this SP3 file
        
        
        """
        ...
    def setAccuracy(self, int: int, double: float) -> None:
        """
            Set the formal accuracy for a satellite.
        
            Parameters:
                index (int): is the index of the satellite.
                accuracy (double): of the satellite, in m.
        
        
        """
        ...
    def setAgency(self, string: str) -> None:
        """
            Set the agency string for this SP3 file.
        
            Parameters:
                agencyStr (String): the agency string to be set
        
        
        """
        ...
    def setCoordinateSystem(self, string: str) -> None:
        """
            Set the coordinate system used for the orbit entries.
        
            Parameters:
                system (String): the coordinate system to be set
        
        
        """
        ...
    def setDataUsed(self, string: str) -> None:
        """
            Set the data used indicator for this SP3 file.
        
            Parameters:
                data (String): the data used indicator to be set
        
        
        """
        ...
    def setDayFraction(self, double: float) -> None:
        """
            Set the day fraction for this SP3 file.
        
            Parameters:
                fraction (double): the day fraction to be set
        
        
        """
        ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the epoch of the SP3 file.
        
            Parameters:
                time (:class:`~org.orekit.time.AbsoluteDate`): the epoch to be set
        
        
        """
        ...
    def setEpochInterval(self, double: float) -> None:
        """
            Set the epoch interval for this SP3 file.
        
            Parameters:
                interval (double): the interval between orbit entries
        
        
        """
        ...
    def setFilter(self, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter) -> None:
        """
            Set the derivatives filter.
        
            Parameters:
                filter (:class:`~org.orekit.utils.CartesianDerivativesFilter`): that indicates which derivatives of position are available.
        
        
        """
        ...
    def setGpsWeek(self, int: int) -> None:
        """
            Set the GPS week of the SP3 file.
        
            Parameters:
                week (int): the GPS week to be set
        
        
        """
        ...
    def setJulianDay(self, int: int) -> None:
        """
            Set the julian day for this SP3 file.
        
            Parameters:
                day (int): the julian day to be set
        
        
        """
        ...
    def setNumberOfEpochs(self, int: int) -> None:
        """
            Set the number of epochs as contained in the SP3 file.
        
            Parameters:
                epochCount (int): the number of epochs to be set
        
        
        """
        ...
    def setOrbitTypeKey(self, string: str) -> None:
        """
            Set the orbit type key for this SP3 file.
        
            Parameters:
                oTypeKey (String): the orbit type key to be set
        
            Since:
                9.3
        
        
        """
        ...
    def setSecondsOfWeek(self, double: float) -> None:
        """
            Set the seconds of the GPS week for this SP3 file.
        
            Parameters:
                seconds (double): the seconds to be set
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.gnss.TimeSystem) -> None:
        """
            Set the time system used in this SP3 file.
        
            Parameters:
                system (:class:`~org.orekit.gnss.TimeSystem`): the time system to be set
        
        
        """
        ...
    def setType(self, sP3FileType: 'SP3.SP3FileType') -> None:
        """
            Set the file type for this SP3 file.
        
            Parameters:
                fileType (:class:`~org.orekit.files.sp3.SP3.SP3FileType`): the file type to be set
        
        
        """
        ...
    class SP3Coordinate(org.orekit.utils.TimeStampedPVCoordinates):
        @typing.overload
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
        @typing.overload
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float): ...
        def getClockCorrection(self) -> float: ...
        def getClockRateChange(self) -> float: ...
    class SP3Ephemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris['SP3.SP3Coordinate', 'SP3.SP3Ephemeris'], org.orekit.files.general.EphemerisFile.EphemerisSegment['SP3.SP3Coordinate']):
        def __init__(self, sP3: 'SP3', string: str): ...
        def getAccuracy(self) -> float: ...
        def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter: ...
        def getCoordinates(self) -> java.util.List['SP3.SP3Coordinate']: ...
        def getFrame(self) -> org.orekit.frames.Frame: ...
        def getId(self) -> str: ...
        def getInterpolationSamples(self) -> int: ...
        def getMu(self) -> float: ...
        def getPropagator(self) -> org.orekit.propagation.BoundedPropagator: ...
        def getSegments(self) -> java.util.List['SP3.SP3Ephemeris']: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStop(self) -> org.orekit.time.AbsoluteDate: ...
        def setAccuracy(self, double: float) -> None: ...
    class SP3FileType(java.lang.Enum['SP3.SP3FileType']):
        GPS: typing.ClassVar['SP3.SP3FileType'] = ...
        MIXED: typing.ClassVar['SP3.SP3FileType'] = ...
        GLONASS: typing.ClassVar['SP3.SP3FileType'] = ...
        LEO: typing.ClassVar['SP3.SP3FileType'] = ...
        GALILEO: typing.ClassVar['SP3.SP3FileType'] = ...
        SBAS: typing.ClassVar['SP3.SP3FileType'] = ...
        IRNSS: typing.ClassVar['SP3.SP3FileType'] = ...
        COMPASS: typing.ClassVar['SP3.SP3FileType'] = ...
        QZSS: typing.ClassVar['SP3.SP3FileType'] = ...
        UNDEFINED: typing.ClassVar['SP3.SP3FileType'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SP3.SP3FileType': ...
        @staticmethod
        def values() -> typing.List['SP3.SP3FileType']: ...
    class SP3OrbitType(java.lang.Enum['SP3.SP3OrbitType']):
        FIT: typing.ClassVar['SP3.SP3OrbitType'] = ...
        EXT: typing.ClassVar['SP3.SP3OrbitType'] = ...
        BCT: typing.ClassVar['SP3.SP3OrbitType'] = ...
        HLM: typing.ClassVar['SP3.SP3OrbitType'] = ...
        OTHER: typing.ClassVar['SP3.SP3OrbitType'] = ...
        @staticmethod
        def parseType(string: str) -> 'SP3.SP3OrbitType': ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SP3.SP3OrbitType': ...
        @staticmethod
        def values() -> typing.List['SP3.SP3OrbitType']: ...

class SP3Parser(org.orekit.files.general.EphemerisFileParser[SP3]):
    """
    public class SP3Parser extends Object implements :class:`~org.orekit.files.general.EphemerisFileParser`<:class:`~org.orekit.files.sp3.SP3`>
    
        A parser for the SP3 orbit file format. It supports all formats from sp3-a to sp3-d.
    
        **Note:** this parser is thread-safe, so calling :meth:`~org.orekit.files.sp3.SP3Parser.parse` from different threads is
        allowed.
    
        Also see:
            SP3-a file format, SP3-c file format, SP3-d file format
    """
    DEFAULT_CLOCK_VALUE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_CLOCK_VALUE
    
        Bad or absent clock values are to be set to 999999.999999.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]]): ...
    @typing.overload
    def __init__(self, double: float, int: int, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]], timeScales: org.orekit.time.TimeScales): ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> SP3:
        """
            Description copied from interface: :meth:`~org.orekit.files.general.EphemerisFileParser.parse`
            Parse an ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFileParser.parse`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed ephemeris file.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.sp3")``.

    SP3: typing.Type[SP3]
    SP3Parser: typing.Type[SP3Parser]
