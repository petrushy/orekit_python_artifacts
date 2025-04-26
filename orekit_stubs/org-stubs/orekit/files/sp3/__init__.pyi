
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.data
import org.orekit.files.general
import org.orekit.frames
import org.orekit.gnss
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class DataUsed(java.lang.Enum['DataUsed']):
    """
    public enum DataUsed extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.sp3.DataUsed`>
    
        Enumerate for data used.
    
        Since:
            12.0
    """
    UNDIFFERENTIATED_CARRIER_PHASE: typing.ClassVar['DataUsed'] = ...
    CHANGE_IN_UNDIFFERENTIATED_CARRIER_PHASE: typing.ClassVar['DataUsed'] = ...
    TWO_RECEIVER_ONE_SATELLITE_CARRIER_PHASE: typing.ClassVar['DataUsed'] = ...
    CHANGE_IN_TWO_RECEIVER_ONE_SATELLITE_CARRIER_PHASE: typing.ClassVar['DataUsed'] = ...
    TWO_RECEIVER_TWO_SATELLITE_CARRIER_PHASE: typing.ClassVar['DataUsed'] = ...
    CHANGE_IN_TWO_RECEIVER_TWO_SATELLITE_CARRIER_PHASE: typing.ClassVar['DataUsed'] = ...
    UNDIFFERENTIATED_CODE_PHASE: typing.ClassVar['DataUsed'] = ...
    CHANGE_IN_UNDIFFERENTIATED_CODE_PHASE: typing.ClassVar['DataUsed'] = ...
    TWO_RECEIVER_ONE_SATELLITE_CODE_PHASE: typing.ClassVar['DataUsed'] = ...
    CHANGE_IN_TWO_RECEIVER_ONE_SATELLITE_CODE_PHASE: typing.ClassVar['DataUsed'] = ...
    TWO_RECEIVER_TWO_SATELLITE_CODE_PHASE: typing.ClassVar['DataUsed'] = ...
    CHANGE_IN_TWO_RECEIVER_TWO_SATELLITE_CODE_PHASE: typing.ClassVar['DataUsed'] = ...
    SATELLITE_LASER_RANGING: typing.ClassVar['DataUsed'] = ...
    MIXED: typing.ClassVar['DataUsed'] = ...
    ORBIT: typing.ClassVar['DataUsed'] = ...
    def getKey(self) -> str:
        """
            Get the key for the data used.
        
            Returns:
                key for the data used
        
        
        """
        ...
    @staticmethod
    def parse(string: str, string2: str, char: str) -> 'DataUsed':
        """
            Parse the string to get the data used.
        
            Parameters:
                s (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string to parse
                fileName (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): file name to generate the error message
                version (char): format version
        
            Returns:
                the data used corresponding to the string
        
            Raises:
                :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if the string does not correspond to a data used
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DataUsed':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['DataUsed']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (DataUsed c : DataUsed.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class NsgfV00Filter(org.orekit.data.DataFilter):
    """
    public class NsgfV00Filter extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.data.DataFilter`
    
        Filter for some non-official files from CDDIS.
    
        Some files produced by UKRI/NERC/British Geological Survey Space Geodesy Facility (SGF) claim to be SP3c but are really
        SP3d since they have more than 4 comments lines. This filter can be used to parse them.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.files.sp3.https:.forum.orekit.org.t.solved`
    """
    DEFAULT_V00_PATTERN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_V00_PATTERN
    
        Default regular expression for NSGF V00 files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, function: typing.Union[java.util.function.Function[str, str], typing.Callable[[str], str]]): ...
    def filter(self, dataSource: org.orekit.data.DataSource) -> org.orekit.data.DataSource: ...

class SP3(org.orekit.files.general.EphemerisFile['SP3Coordinate', 'SP3Segment']):
    """
    public class SP3 extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.files.sp3.SP3Coordinate`, :class:`~org.orekit.files.sp3.SP3Segment`>
    
        Represents a parsed SP3 orbit file.
    """
    @typing.overload
    def __init__(self, double: float, int: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, sP3Header: 'SP3Header', double: float, int: int, frame: org.orekit.frames.Frame): ...
    def addSatellite(self, string: str) -> None:
        """
            Add a new satellite with a given identifier to the list of stored satellites.
        
            Parameters:
                satId (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the satellite identifier
        
        
        """
        ...
    @staticmethod
    def changeFrame(sP3: 'SP3', frame: org.orekit.frames.Frame) -> 'SP3':
        """
            Change the frame of an SP3 file.
        
            Parameters:
                original (:class:`~org.orekit.files.sp3.SP3`): original SP3 file
                newFrame (:class:`~org.orekit.frames.Frame`): frame to use for the changed SP3 file
        
            Returns:
                changed SP3 file
        
            Since:
                12.1
        
        
        """
        ...
    def containsSatellite(self, string: str) -> bool:
        """
            Tests whether a satellite with the given id is contained in this orbit file.
        
            Parameters:
                satId (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the satellite id
        
            Returns:
                :code:`true` if the satellite is contained in the file, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    def getEphemeris(self, int: int) -> 'SP3Ephemeris':
        """
            Get an ephemeris.
        
            Parameters:
                index (int): index of the satellite
        
            Returns:
                satellite ephemeris
        
            Since:
                12.0
        
            Get an ephemeris.
        
            Parameters:
                satId (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): satellite identifier
        
            Returns:
                satellite ephemeris, or null if not found
        
            Since:
                12.0
        
        
        """
        ...
    @typing.overload
    def getEphemeris(self, string: str) -> 'SP3Ephemeris': ...
    def getHeader(self) -> 'SP3Header':
        """
            Get the header.
        
            Returns:
                header
        
            Since:
                12.0
        
        
        """
        ...
    def getSatelliteCount(self) -> int:
        """
            Get the number of satellites contained in this orbit file.
        
            Returns:
                the number of satellites
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'SP3Ephemeris']: ...
    @staticmethod
    def splice(collection: typing.Union[java.util.Collection['SP3'], typing.Sequence['SP3'], typing.Set['SP3']]) -> 'SP3': ...
    def validate(self, boolean: bool, string: str) -> None: ...

class SP3Coordinate(org.orekit.utils.TimeStampedPVCoordinates):
    """
    public class SP3Coordinate extends :class:`~org.orekit.utils.TimeStampedPVCoordinates`
    
        A single record of position clock and possibly derivatives in an SP3 file.
    
        Since:
            12.0
    """
    DUMMY: typing.ClassVar['SP3Coordinate'] = ...
    """
    public static final :class:`~org.orekit.files.sp3.SP3Coordinate` DUMMY
    
        Dummy coordinate with all fields set to 0.0.
    
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float, double3: float, double4: float, boolean: bool, boolean2: bool, boolean3: bool, boolean4: bool): ...
    def getClockAccuracy(self) -> float:
        """
            Get the clock accuracy.
        
            Returns:
                clock accuracy in s (:code:`Double.NaN` if not known).
        
        
        """
        ...
    def getClockCorrection(self) -> float:
        """
            Get the clock correction value.
        
            Returns:
                the clock correction in s.
        
        
        """
        ...
    def getClockRateAccuracy(self) -> float:
        """
            Get the clock rate accuracy.
        
            Returns:
                clock rate accuracy in s/s (:code:`Double.NaN` if not known).
        
        
        """
        ...
    def getClockRateChange(self) -> float:
        """
            Get the clock rate.
        
            Returns:
                the clock rate of change in s/s.
        
        
        """
        ...
    def getPositionAccuracy(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position accuracy.
        
            Returns:
                position accuracy in m (null if not known).
        
        
        """
        ...
    def getVelocityAccuracy(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the velocity accuracy.
        
            Returns:
                velocity accuracy in m/s (null if not known).
        
        
        """
        ...
    def hasClockEvent(self) -> bool:
        """
            Get clock event flag.
        
            Returns:
                true if clock event flag is set
        
        
        """
        ...
    def hasClockPrediction(self) -> bool:
        """
            Get clock prediction flag.
        
            Returns:
                true if clock prediction flag is set
        
        
        """
        ...
    def hasOrbitManeuverEvent(self) -> bool:
        """
            Get orbit maneuver event flag.
        
            Returns:
                true if orbit maneuver event flag is set
        
        
        """
        ...
    def hasOrbitPrediction(self) -> bool:
        """
            Get orbit prediction flag.
        
            Returns:
                true if orbit prediction flag is set
        
        
        """
        ...

class SP3CoordinateHermiteInterpolator(org.orekit.time.AbstractTimeInterpolator[SP3Coordinate]):
    """
    public class SP3CoordinateHermiteInterpolator extends :class:`~org.orekit.time.AbstractTimeInterpolator`<:class:`~org.orekit.files.sp3.SP3Coordinate`>
    
        Interpolator for :class:`~org.orekit.files.sp3.SP3Coordinate`.
    
        As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points
        (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and
        numerical problems (including NaN appearing).
    
        If some clock or clock rate are present in the SP3 files as default values (999999.999999), then they are replaced by
        :code:`Double.NaN` during parsing, so the interpolation will exhibit NaNs, but the positions will be properly
        interpolated.
    
        Since:
            12.0
    
        Also see:
            
            class:`~org.orekit.files.sp3.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`,
            :class:`~org.orekit.files.sp3.SP3Coordinate`
    """
    def __init__(self, int: int, double: float, boolean: bool): ...

class SP3Ephemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[SP3Coordinate, 'SP3Segment']):
    """
    public class SP3Ephemeris extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`<:class:`~org.orekit.files.sp3.SP3Coordinate`, :class:`~org.orekit.files.sp3.SP3Segment`>
    
        Single satellite ephemeris from an :class:`~org.orekit.files.sp3.SP3` file.
    
        Since:
            12.0
    """
    def __init__(self, string: str, double: float, frame: org.orekit.frames.Frame, int: int, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter): ...
    def addCoordinate(self, sP3Coordinate: SP3Coordinate, double: float) -> None:
        """
            Adds a new P/V coordinate.
        
            Parameters:
                coord (:class:`~org.orekit.files.sp3.SP3Coordinate`): the P/V coordinate of the satellite
                maxGap (double): maximum gap between segments
        
        
        """
        ...
    def extractClockModel(self) -> org.orekit.time.AggregatedClockModel:
        """
            Extract the clock model.
        
            There are always 2n+1 :meth:`~org.orekit.time.AggregatedClockModel.getModels` underlying clock models when there are n
            :meth:`~org.orekit.files.sp3.SP3Ephemeris.getSegments` in the ephemeris. This happens because there are spans with
            :code:`null` data before the first segment, between all regular segments and after last segment.
        
            Returns:
                extracted clock model
        
            Since:
                12.1
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get the available derivatives.
        
            Returns:
                available derivatives
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame.
        
            Returns:
                reference frame
        
        
        """
        ...
    def getId(self) -> str:
        """
            Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getId` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the satellite's ID, never :code:`null`.
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of points to use for interpolation.
        
            Returns:
                number of points to use for interpolation
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getMu` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getPropagator`, in
                m³/s².
        
        
        """
        ...
    def getSegments(self) -> java.util.List['SP3Segment']: ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStart` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStop` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris end date.
        
        
        """
        ...

class SP3FileType(java.lang.Enum['SP3FileType']):
    """
    public enum SP3FileType extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.sp3.SP3FileType`>
    
        File type indicator.
    
        Since:
            12.0
    """
    GPS: typing.ClassVar['SP3FileType'] = ...
    MIXED: typing.ClassVar['SP3FileType'] = ...
    GLONASS: typing.ClassVar['SP3FileType'] = ...
    LEO: typing.ClassVar['SP3FileType'] = ...
    GALILEO: typing.ClassVar['SP3FileType'] = ...
    SBAS: typing.ClassVar['SP3FileType'] = ...
    NAVIC: typing.ClassVar['SP3FileType'] = ...
    COMPASS: typing.ClassVar['SP3FileType'] = ...
    QZSS: typing.ClassVar['SP3FileType'] = ...
    UNDEFINED: typing.ClassVar['SP3FileType'] = ...
    def getKey(self) -> str:
        """
            Get the key for the file type.
        
            Returns:
                key for the file type
        
        
        """
        ...
    @staticmethod
    def parse(string: str) -> 'SP3FileType':
        """
            Parse the string to get the data used.
        
            Parameters:
                s (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string to parse
        
            Returns:
                the file type corresponding to the string
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SP3FileType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['SP3FileType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SP3FileType c : SP3FileType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SP3Header:
    """
    public class SP3Header extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Header for SP3 files.
    
        Since:
            12.0
    """
    SP3_FRAME_CENTER_STRING: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SP3_FRAME_CENTER_STRING
    
        String representation of the center of ephemeris coordinate system.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def addComment(self, string: str) -> None:
        """
            Add a comment.
        
            Parameters:
                comment (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): comment to add
        
        
        """
        ...
    def addSatId(self, string: str) -> None:
        """
            Add a satellite identifier.
        
            Parameters:
                satId (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): satellite identifier
        
        
        """
        ...
    def getAccuracy(self, string: str) -> float:
        """
            Get the formal accuracy.
        
            The accuracy is limited by the SP3 standard to be a power of 2 in mm. The value returned here is in meters.
        
            Parameters:
                satId (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): satellite identifier
        
            Returns:
                magnitude of one standard deviation, in m.
        
        
        """
        ...
    def getAgency(self) -> str:
        """
            Returns the agency that prepared this SP3 file.
        
            Returns:
                the agency
        
        
        """
        ...
    def getClockBase(self) -> float:
        """
            Get the base for clock/clock-rate accuracy.
        
            Returns:
                base for clock/clock-rate accuracy
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]: ...
    def getCoordinateSystem(self) -> str:
        """
            Returns the coordinate system of the entries in this orbit file.
        
            Returns:
                the coordinate system
        
        
        """
        ...
    def getDataUsed(self) -> java.util.List[DataUsed]: ...
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
    def getFilter(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get the derivatives filter.
        
            Returns:
                filter with available derivatives
        
        
        """
        ...
    def getGpsWeek(self) -> int:
        """
            Returns the GPS week as contained in the SP3 file.
        
            Returns:
                the GPS week of the SP3 file
        
        
        """
        ...
    def getModifiedJulianDay(self) -> int:
        """
            Returns the modified julian day for this SP3 file.
        
            Returns:
                the modified julian day
        
        
        """
        ...
    def getNumberOfEpochs(self) -> int:
        """
            Returns the number of epochs contained in this orbit file.
        
            Returns:
                the number of epochs
        
        
        """
        ...
    def getOrbitType(self) -> 'SP3OrbitType':
        """
            Returns the :class:`~org.orekit.files.sp3.SP3OrbitType` for this SP3 file.
        
            Returns:
                the orbit type
        
        
        """
        ...
    def getOrbitTypeKey(self) -> str:
        """
            Returns the orbit type key for this SP3 file.
        
            Returns:
                the orbit type key
        
        
        """
        ...
    def getPosVelBase(self) -> float:
        """
            Get the base for position/velocity accuracy.
        
            Returns:
                base for position/velocity accuracy
        
        
        """
        ...
    def getSatIds(self) -> java.util.List[str]: ...
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
    def getType(self) -> SP3FileType:
        """
            Returns the :class:`~org.orekit.files.sp3.SP3FileType` associated with this SP3 file.
        
            Returns:
                the file type for this SP3 file
        
        
        """
        ...
    def getVersion(self) -> str:
        """
            Get the file version.
        
            Returns:
                file version
        
        
        """
        ...
    def setAccuracy(self, int: int, double: float) -> None:
        """
            Set the accuracy.
        
            Parameters:
                index (int): satellite index in :meth:`~org.orekit.files.sp3.SP3Header.getSatIds`
                accuracy (double): in m
        
        
        """
        ...
    def setAgency(self, string: str) -> None:
        """
            Set the agency string for this SP3 file.
        
            Parameters:
                agencyStr (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the agency string to be set
        
        
        """
        ...
    def setClockBase(self, double: float) -> None:
        """
            Set the base for clock/clock-rate accuracy.
        
            Parameters:
                clockBase (double): base for clock/clock-rate accuracy
        
        
        """
        ...
    def setCoordinateSystem(self, string: str) -> None:
        """
            Set the coordinate system used for the orbit entries.
        
            Parameters:
                system (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the coordinate system to be set
        
        
        """
        ...
    def setDataUsed(self, list: java.util.List[DataUsed]) -> None: ...
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
    def setModifiedJulianDay(self, int: int) -> None:
        """
            Set the modified julian day for this SP3 file.
        
            Parameters:
                day (int): the modified julian day to be set
        
        
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
                oTypeKey (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the orbit type key to be set
        
        
        """
        ...
    def setPosVelBase(self, double: float) -> None:
        """
            Set the base for position/velocity accuracy.
        
            Parameters:
                posVelBase (double): base for position/velocity accuracy
        
        
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
    def setType(self, sP3FileType: SP3FileType) -> None:
        """
            Set the file type for this SP3 file.
        
            Parameters:
                fileType (:class:`~org.orekit.files.sp3.SP3FileType`): the file type to be set
        
        
        """
        ...
    def setVersion(self, char: str) -> None:
        """
            Set the file version.
        
            Parameters:
                version (char): file version
        
        
        """
        ...

class SP3OrbitType(java.lang.Enum['SP3OrbitType']):
    """
    public enum SP3OrbitType extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.sp3.SP3OrbitType`>
    
        Orbit type indicator.
    """
    FIT: typing.ClassVar['SP3OrbitType'] = ...
    EXT: typing.ClassVar['SP3OrbitType'] = ...
    BCT: typing.ClassVar['SP3OrbitType'] = ...
    HLM: typing.ClassVar['SP3OrbitType'] = ...
    OTHER: typing.ClassVar['SP3OrbitType'] = ...
    @staticmethod
    def parseType(string: str) -> 'SP3OrbitType':
        """
            Parse a string to get the type.
        
            Parameters:
                s (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): string to parse
        
            Returns:
                the type corresponding to the string
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SP3OrbitType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['SP3OrbitType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SP3OrbitType c : SP3OrbitType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SP3Parser(org.orekit.files.general.EphemerisFileParser[SP3]):
    """
    public class SP3Parser extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFileParser`<:class:`~org.orekit.files.sp3.SP3`>
    
        A parser for the SP3 orbit file format. It supports all formats from sp3-a to sp3-d.
    
        **Note:** this parser is thread-safe, so calling :meth:`~org.orekit.files.sp3.SP3Parser.parse` from different threads is
        allowed.
    
        Also see:
            :class:`~org.orekit.files.sp3.https:.files.igs.org.pub.data.format.sp3_docu.txt`,
            :class:`~org.orekit.files.sp3.https:.files.igs.org.pub.data.format.sp3c.txt`,
            :class:`~org.orekit.files.sp3.https:.files.igs.org.pub.data.format.sp3d.pdf`
    """
    DEFAULT_INTERPOLATION_SAMPLES: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_INTERPOLATION_SAMPLES
    
        Default number of samples to use when interpolating SP3 coordinates.
    
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
                :meth:`~org.orekit.files.general.EphemerisFileParser.parse` in
                interface :class:`~org.orekit.files.general.EphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed ephemeris file.
        
        
        """
        ...

class SP3Segment(org.orekit.files.general.EphemerisFile.EphemerisSegment[SP3Coordinate]):
    """
    public class SP3Segment extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`<:class:`~org.orekit.files.sp3.SP3Coordinate`>
    
        One segment of an :class:`~org.orekit.files.sp3.SP3Ephemeris`.
    
        Since:
            12.0
    """
    def __init__(self, double: float, frame: org.orekit.frames.Frame, int: int, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter): ...
    def addCoordinate(self, sP3Coordinate: SP3Coordinate) -> None:
        """
            Adds a new P/V coordinate.
        
            Parameters:
                coord (:class:`~org.orekit.files.sp3.SP3Coordinate`): the P/V coordinate of the satellite
        
        
        """
        ...
    def extractClockModel(self) -> org.orekit.time.ClockModel:
        """
            Extract the clock model.
        
            If some clock or clock rate are present in the SP3 files as default values (999999.999999), then they filtered out here
            when building the clock model, so interpolation will work if at least there are some remaining regular values.
        
            Returns:
                extracted clock model
        
            Since:
                12.1
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get which derivatives of position are available in this ephemeris segment.
        
            While :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates` always returns position, velocity,
            and acceleration the return value from this method indicates which of those are in the ephemeris file and are actually
            valid.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getAvailableDerivatives` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                a value indicating if the file contains velocity and/or acceleration data.
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[SP3Coordinate]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame for this ephemeris segment. The defining frame for
            :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the reference frame for this segment. Never :code:`null`.
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of samples to use in interpolation.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getInterpolationSamples` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the number of points to use for interpolation.
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getMu` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getPropagator`, in
                m³/s².
        
        
        """
        ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.BoundedPropagator:
        """
            View this ephemeris segment as a propagator.
        
            In order to view the ephemeris for this satellite as a :class:`~org.orekit.propagation.Propagator` several conditions
            must be met. An Orekit :class:`~org.orekit.frames.Frame` must be constructable from the frame specification in the
            ephemeris file. This condition is met when :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame`
            return normally. Additionally, :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getMu` must return a
            valid value. If these conditions are not met an :class:`~org.orekit.errors.OrekitException` may be thrown by this method
            or by one of the methods of the returned :class:`~org.orekit.propagation.Propagator`.
        
            The :class:`~org.orekit.attitudes.AttitudeProvider` used is a :class:`~org.orekit.attitudes.FrameAlignedProvider`
            aligned with the :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getInertialFrame`
        
            Each call to this method creates a new propagator.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getPropagator` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                a propagator for this ephemeris segment.
        
        """
        ...
    @typing.overload
    def getPropagator(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> org.orekit.propagation.BoundedPropagator:
        """
            View this ephemeris segment as a propagator.
        
            In order to view the ephemeris for this satellite as a :class:`~org.orekit.propagation.Propagator` several conditions
            must be met. An Orekit :class:`~org.orekit.frames.Frame` must be constructable from the frame specification in the
            ephemeris file. This condition is met when :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame`
            return normally. Additionally, :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getMu` must return a
            valid value. If these conditions are not met an :class:`~org.orekit.errors.OrekitException` may be thrown by this method
            or by one of the methods of the returned :class:`~org.orekit.propagation.Propagator`.
        
            Each call to this method creates a new propagator.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getPropagator` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): provider for attitude computation
        
            Returns:
                a propagator for this ephemeris segment.
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStart` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStop` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment end date.
        
        
        """
        ...

class SP3Utils:
    """
    public class SP3Utils extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Constants for SP3 files.
    
        Since:
            12.0
    """
    DEFAULT_CLOCK_VALUE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_CLOCK_VALUE
    
        Bad or absent clock values are to be set to 999999.999999.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_CLOCK_RATE_VALUE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_CLOCK_RATE_VALUE
    
        Bad or absent clock rate values are to be set to 999999.999999.
    
        Also see:
            :meth:`~constant`
    
    
    """
    POS_VEL_BASE_ACCURACY: typing.ClassVar[float] = ...
    """
    public static final double POS_VEL_BASE_ACCURACY
    
        Base for general position/velocity accuracy.
    
        Also see:
            :meth:`~constant`
    
    
    """
    POSITION_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` POSITION_UNIT
    
        Position unit.
    
    """
    POSITION_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` POSITION_ACCURACY_UNIT
    
        Position accuracy unit.
    
    """
    VELOCITY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` VELOCITY_UNIT
    
        Velocity unit.
    
    """
    VELOCITY_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` VELOCITY_ACCURACY_UNIT
    
        Velocity accuracy unit.
    
    """
    CLOCK_ADDITIONAL_STATE: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CLOCK_ADDITIONAL_STATE
    
        Additional state name for clock.
    
        Since:
            12.1
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLOCK_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` CLOCK_UNIT
    
        Clock unit.
    
    """
    CLOCK_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` CLOCK_ACCURACY_UNIT
    
        Clock accuracy unit.
    
    """
    CLOCK_RATE_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` CLOCK_RATE_UNIT
    
        Clock rate unit.
    
    """
    CLOCK_RATE_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` CLOCK_RATE_ACCURACY_UNIT
    
        Clock rate accuracy unit.
    
    """
    @staticmethod
    def indexAccuracy(unit: org.orekit.utils.units.Unit, double: float, double2: float) -> int:
        """
            Convert an accuracy from SI units.
        
            Parameters:
                unit (:class:`~org.orekit.utils.units.Unit`): accuracy unit
                base (double): base
                accuracy (double): in SI units
        
            Returns:
                accuracyIndex index of accuracy
        
        
        """
        ...
    @staticmethod
    def siAccuracy(unit: org.orekit.utils.units.Unit, double: float, int: int) -> float:
        """
            Convert an accuracy to SI units.
        
            Parameters:
                unit (:class:`~org.orekit.utils.units.Unit`): accuracy unit
                base (double): base
                accuracyIndex (int): index of accuracy
        
            Returns:
                accuracy in SI units
        
        
        """
        ...

class SP3Writer:
    """
    public class SP3Writer extends :class:`~org.orekit.files.sp3.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Writer for SP3 file.
    
        Since:
            12.0
    """
    def __init__(self, appendable: java.lang.Appendable, string: str, timeScales: org.orekit.time.TimeScales): ...
    def write(self, sP3: SP3) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.sp3")``.

    DataUsed: typing.Type[DataUsed]
    NsgfV00Filter: typing.Type[NsgfV00Filter]
    SP3: typing.Type[SP3]
    SP3Coordinate: typing.Type[SP3Coordinate]
    SP3CoordinateHermiteInterpolator: typing.Type[SP3CoordinateHermiteInterpolator]
    SP3Ephemeris: typing.Type[SP3Ephemeris]
    SP3FileType: typing.Type[SP3FileType]
    SP3Header: typing.Type[SP3Header]
    SP3OrbitType: typing.Type[SP3OrbitType]
    SP3Parser: typing.Type[SP3Parser]
    SP3Segment: typing.Type[SP3Segment]
    SP3Utils: typing.Type[SP3Utils]
    SP3Writer: typing.Type[SP3Writer]
