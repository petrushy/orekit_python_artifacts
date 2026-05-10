
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
    def parse(s: str, fileName: str, version: str) -> 'DataUsed':
        """
        Parse the string to get the data used.
        
        Parameters:
            s (String): string to parse
            fileName (String): file name to generate the error message
            version (char): format version
        
        Returns:
            the data used corresponding to the string
        
        Raises:
            IllegalArgumentException: if the string does not correspond to a data used
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'DataUsed':
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
    def values() -> typing.MutableSequence['DataUsed']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (DataUsed c : DataUsed.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class NsgfV00Filter(org.orekit.data.DataFilter):
    """
    Filter for some non-official files from CDDIS.
    
    Some files produced by UKRI/NERC/British Geological Survey Space Geodesy Facility (SGF) claim to be SP3c but are really SP3d since they have more than 4 comments lines. This filter can be used to parse them.
    
    Since:
        12.1
    
    Also see:
        solved
    """
    DEFAULT_V00_PATTERN: typing.ClassVar[str] = ...
    """
    Default regular expression for NSGF V00 files.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, nameRegexp: str, renaming: typing.Union[java.util.function.Function[str, str], typing.Callable[[str], str]]): ...
    def filter(self, original: org.orekit.data.DataSource) -> org.orekit.data.DataSource:
        """
        Filter the data source.
        
        Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
        A filter must never openStreamOnce the DataSource by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it is the upper layer that will decide to open (or not) the returned value and that a DataSource can be opened only once; this is the core principle of lazy-opening provided by DataSource.
        
        Beware that as the DataProvidersManager will attempt to pile all filters in a stack as long as their implementation of this method returns a value different from the original parameter. This implies that the filter, must perform some checks to see if it must be applied or not. If for example there is a need for a deciphering filter to be applied once to all data, then the filter should for example check for a suffix in the getName and create a new filtered DataSource instance only if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering filters being built, until a stack overflow or memory exhaustion exception occurs.
        
        Specified by: filter in interface DataFilter
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            filtered data source, or original if this filter does not apply to this data source
        
        Raises:
            IOException: if filtered stream cannot be created
        
        
        """
        ...

class SP3(org.orekit.files.general.EphemerisFile['SP3Coordinate', 'SP3Segment']):
    """
    Represents a parsed SP3 orbit file.
    """
    @typing.overload
    def __init__(self, mu: float, interpolationSamples: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, header: 'SP3Header', mu: float, interpolationSamples: int, frame: org.orekit.frames.Frame): ...
    def addSatellite(self, satId: str) -> None:
        """
        Add a new satellite with a given identifier to the list of stored satellites.
        
        Parameters:
            satId (String): the satellite identifier
        
        
        """
        ...
    @staticmethod
    def changeFrame(original: 'SP3', newFrame: org.orekit.frames.Frame) -> 'SP3':
        """
        Change the frame of an SP3 file.
        
        Parameters:
            original (SP3): original SP3 file
            newFrame (Frame): frame to use for the changed SP3 file
        
        Returns:
            changed SP3 file
        
        Since:
            12.1
        
        
        """
        ...
    def containsSatellite(self, satId: str) -> bool:
        """
        Tests whether a satellite with the given id is contained in this orbit file.
        
        Parameters:
            satId (String): the satellite id
        
        Returns:
            true if the satellite is contained in the file, false otherwise
        
        
        """
        ...
    @typing.overload
    def getEphemeris(self, index: int) -> 'SP3Ephemeris':
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
            satId (String): satellite identifier
        
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
    def getSatellites(self) -> java.util.Map[str, 'SP3Ephemeris']:
        """
        Description copied from interface: getSatellites Get the loaded ephemeris for each satellite in the file.
        
        Specified by: getSatellites in interface EphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...
    @staticmethod
    def splice(sp3: typing.Union[java.util.Collection['SP3'], typing.Sequence['SP3'], typing.Set['SP3']]) -> 'SP3':
        """
        Splice several SP3 files together.
        
        Splicing SP3 files is intended to be used when continuous computation covering more than one file is needed. The files should all have the exact same metadata: getType, getTimeSystem, getCoordinateSystem, except for satellite accuracy which can be different from one file to the next one, and some satellites may be missing in some files… Once sorted (which is done internally), if the gap between segments from two file is at most getEpochInterval, then the segments are merged as one segment, otherwise the segments are kept separated.
        
        The spliced file only contains the satellites that were present in all files. Satellites present in some files and absent from other files are silently dropped.
        
        Depending on producer, successive SP3 files either have a gap between the last entry of one file and the first entry of the next file (for example files with a 5 minutes epoch interval may end at 23:55 and the next file start at 00:00), or both files have one point exactly at the splicing date (i.e. 24:00 one day and 00:00 next day). In the later case, the last point of the early file is dropped and the first point of the late file takes precedence, hence only one point remains in the spliced file ; this design choice is made to enforce continuity and regular interpolation.
        
        Parameters:
            sp3 (Collection<SP3> sp3): SP3 files to merge
        
        Returns:
            merged SP3
        
        Since:
            12.0
        
        
        """
        ...
    def validate(self, parsing: bool, fileName: str) -> None:
        """
        Check file is valid.
        
        Parameters:
            parsing (boolean): if true, we are parsing an existing file, and are more lenient in order to accept some common errors (like between 86
                and 99 satellites in SP3a, SP3b or SP3c files)
            fileName (String): file name to generate the error message
        
        Raises:
            OrekitException: if file is not valid
        
        
        """
        ...

class SP3Coordinate(org.orekit.utils.TimeStampedPVCoordinates):
    """
    A single record of position clock and possibly derivatives in an SP3 file.
    
    Since:
        12.0
    """
    DUMMY: typing.ClassVar['SP3Coordinate'] = ...
    """
    Dummy coordinate with all fields set to 0.0.
    """
    def __init__(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, positionAccuracy: org.hipparchus.geometry.euclidean.threed.Vector3D, velocity: org.hipparchus.geometry.euclidean.threed.Vector3D, velocityAccuracy: org.hipparchus.geometry.euclidean.threed.Vector3D, clock: float, clockAccuracy: float, clockRate: float, clockRateAccuracy: float, clockEvent: bool, clockPrediction: bool, orbitManeuverEvent: bool, orbitPrediction: bool):
        """
        Create a coordinate with position and velocity.
        
        Parameters:
            date (AbsoluteDate): of validity.
            position (Vector3D): of the satellite.
            positionAccuracy (Vector3D): of the satellite (null if not known).
            velocity (Vector3D): of the satellite.
            velocityAccuracy (Vector3D): of the satellite (null if not known).
            clock (double): correction in s.
            clockAccuracy (double): correction in s (NaN if not known).
            clockRate (double): in s / s.
            clockRateAccuracy (double): in s / s (NaN if not known).
            clockEvent (boolean): clock event flag
            clockPrediction (boolean): clock prediction flag
            orbitManeuverEvent (boolean): orbit maneuver event flag
            orbitPrediction (boolean): flag
        
        
        """
        ...
    def getClockAccuracy(self) -> float:
        """
        Get the clock accuracy.
        
        Returns:
            clock accuracy in s (NaN if not known).
        
        
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
            clock rate accuracy in s/s (NaN if not known).
        
        
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
    Interpolator for SP3Coordinate.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid and numerical problems (including NaN appearing).
    
    If some clock or clock rate are present in the SP3 files as default values (999999.999999), then they are replaced by NaN during parsing, so the interpolation will exhibit NaNs, but the positions will be properly interpolated.
    
    Since:
        12.0
    
        class:`~org.orekit.files.sp3.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, SP3Coordinate
    """
    def __init__(self, interpolationPoints: int, extrapolationThreshold: float, useRates: bool):
        """
        Constructor.
        
        As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid and numerical problems (including NaN appearing).
        
        Parameters:
            interpolationPoints (int): number of interpolation points
            extrapolationThreshold (double): extrapolation threshold beyond which the propagation will fail
            useRates (boolean): if true, use velocity and clock rates for interpolation
        
        
        """
        ...

class SP3Ephemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[SP3Coordinate, 'SP3Segment']):
    """
    Single satellite ephemeris from an SP3 file.
    
    Since:
        12.0
    """
    def __init__(self, id: str, mu: float, frame: org.orekit.frames.Frame, interpolationSamples: int, filter: org.orekit.utils.CartesianDerivativesFilter):
        """
        Create an ephemeris for a single satellite.
        
        Parameters:
            id (String): of the satellite.
            mu (double): standard gravitational parameter to use for creating Orbit from the ephemeris data.
            frame (Frame): reference frame
            interpolationSamples (int): number of points to use for interpolation
            filter (CartesianDerivativesFilter): available derivatives
        
        
        """
        ...
    def addCoordinate(self, coord: SP3Coordinate, maxGap: float) -> None:
        """
        Adds a new P/V coordinate.
        
        Parameters:
            coord (SP3Coordinate): the P/V coordinate of the satellite
            maxGap (double): maximum gap between segments
        
        
        """
        ...
    def extractClockModel(self) -> org.orekit.time.AggregatedClockModel:
        """
        Extract the clock model.
        
        There are always 2n+1 getModels underlying clock models when there are n getSegments in the ephemeris. This happens because there are spans with null data before the first segment, between all regular segments and after last segment.
        
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
        
        Specified by: getId in interface SatelliteEphemeris
        
        Returns:
            the satellite's ID, never null.
        
        
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
        
        Specified by: getMu in interface SatelliteEphemeris
        
        Returns:
            the gravitational parameter used in getPropagator, in
            m³/s².
        
        
        """
        ...
    def getSegments(self) -> java.util.List['SP3Segment']:
        """
        Get the segments of the ephemeris.
        
        Ephemeris segments are typically used to split an ephemeris around discontinuous events, such as maneuvers.
        
        Specified by: getSegments in interface SatelliteEphemeris
        
        Returns:
            the segments contained in the ephemeris file for this satellite.
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of the ephemeris.
        
        The date returned by this method is equivalent to getMinDate().
        
        Specified by: getStart in interface SatelliteEphemeris
        
        Returns:
            ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of the ephemeris.
        
        The date returned by this method is equivalent to getMaxDate().
        
        Specified by: getStop in interface SatelliteEphemeris
        
        Returns:
            ephemeris end date.
        
        
        """
        ...

class SP3FileType(java.lang.Enum['SP3FileType']):
    """
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
    def parse(s: str) -> 'SP3FileType':
        """
        Parse the string to get the data used.
        
        Parameters:
            s (String): string to parse
        
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
    def valueOf(name: str) -> 'SP3FileType':
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
    def values() -> typing.MutableSequence['SP3FileType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SP3FileType c : SP3FileType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SP3Header:
    """
    Header for SP3 files.
    
    Since:
        12.0
    """
    SP3_FRAME_CENTER_STRING: typing.ClassVar[str] = ...
    """
    String representation of the center of ephemeris coordinate system.
    
    Also see:
        constant
    
    
    """
    def __init__(self):
        """
        Create a new SP3 header.
        """
        ...
    def addComment(self, comment: str) -> None:
        """
        Add a comment.
        
        Parameters:
            comment (String): comment to add
        
        
        """
        ...
    def addSatId(self, satId: str) -> None:
        """
        Add a satellite identifier.
        
        Parameters:
            satId (String): satellite identifier
        
        
        """
        ...
    def getAccuracy(self, satId: str) -> float:
        """
        Get the formal accuracy.
        
        The accuracy is limited by the SP3 standard to be a power of 2 in mm. The value returned here is in meters.
        
        Parameters:
            satId (String): satellite identifier
        
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
    def getComments(self) -> java.util.List[str]:
        """
        Get the comments.
        
        Returns:
            an unmodifiable view of comments
        
        
        """
        ...
    def getCoordinateSystem(self) -> str:
        """
        Returns the coordinate system of the entries in this orbit file.
        
        Returns:
            the coordinate system
        
        
        """
        ...
    def getDataUsed(self) -> java.util.List[DataUsed]:
        """
        Returns the data used indicator from the SP3 file.
        
        Returns:
            the data used indicator
        
        
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
        Returns the SP3OrbitType for this SP3 file.
        
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
    def getSatIds(self) -> java.util.List[str]:
        """
        Get the satellite identifiers.
        
        Returns:
            satellites identifiers
        
        
        """
        ...
    def getSecondsOfWeek(self) -> float:
        """
        Returns the seconds of the GPS week as contained in the SP3 file.
        
        Returns:
            the seconds of the GPS week
        
        
        """
        ...
    def getTimeSystem(self) -> org.orekit.gnss.TimeSystem:
        """
        Returns the TimeSystem used to time-stamp position entries.
        
        Returns:
            the TimeSystem of the orbit file
        
        
        """
        ...
    def getType(self) -> SP3FileType:
        """
        Returns the SP3FileType associated with this SP3 file.
        
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
    def setAccuracy(self, index: int, accuracy: float) -> None:
        """
        Set the accuracy.
        
        Parameters:
            index (int): satellite index in getSatIds
            accuracy (double): in m
        
        
        """
        ...
    def setAgency(self, agencyStr: str) -> None:
        """
        Set the agency string for this SP3 file.
        
        Parameters:
            agencyStr (String): the agency string to be set
        
        
        """
        ...
    def setClockBase(self, clockBase: float) -> None:
        """
        Set the base for clock/clock-rate accuracy.
        
        Parameters:
            clockBase (double): base for clock/clock-rate accuracy
        
        
        """
        ...
    def setCoordinateSystem(self, system: str) -> None:
        """
        Set the coordinate system used for the orbit entries.
        
        Parameters:
            system (String): the coordinate system to be set
        
        
        """
        ...
    def setDataUsed(self, dataUsed: java.util.List[DataUsed]) -> None:
        """
        Set the data used indicator for this SP3 file.
        
        Parameters:
            dataUsed (List<DataUsed> dataUsed): the data used indicator to be set
        
        
        """
        ...
    def setDayFraction(self, fraction: float) -> None:
        """
        Set the day fraction for this SP3 file.
        
        Parameters:
            fraction (double): the day fraction to be set
        
        
        """
        ...
    def setEpoch(self, time: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the epoch of the SP3 file.
        
        Parameters:
            time (AbsoluteDate): the epoch to be set
        
        
        """
        ...
    def setEpochInterval(self, interval: float) -> None:
        """
        Set the epoch interval for this SP3 file.
        
        Parameters:
            interval (double): the interval between orbit entries
        
        
        """
        ...
    def setFilter(self, filter: org.orekit.utils.CartesianDerivativesFilter) -> None:
        """
        Set the derivatives filter.
        
        Parameters:
            filter (CartesianDerivativesFilter): that indicates which derivatives of position are available.
        
        
        """
        ...
    def setGpsWeek(self, week: int) -> None:
        """
        Set the GPS week of the SP3 file.
        
        Parameters:
            week (int): the GPS week to be set
        
        
        """
        ...
    def setModifiedJulianDay(self, day: int) -> None:
        """
        Set the modified julian day for this SP3 file.
        
        Parameters:
            day (int): the modified julian day to be set
        
        
        """
        ...
    def setNumberOfEpochs(self, epochCount: int) -> None:
        """
        Set the number of epochs as contained in the SP3 file.
        
        Parameters:
            epochCount (int): the number of epochs to be set
        
        
        """
        ...
    def setOrbitTypeKey(self, oTypeKey: str) -> None:
        """
        Set the orbit type key for this SP3 file.
        
        Parameters:
            oTypeKey (String): the orbit type key to be set
        
        
        """
        ...
    def setPosVelBase(self, posVelBase: float) -> None:
        """
        Set the base for position/velocity accuracy.
        
        Parameters:
            posVelBase (double): base for position/velocity accuracy
        
        
        """
        ...
    def setSecondsOfWeek(self, seconds: float) -> None:
        """
        Set the seconds of the GPS week for this SP3 file.
        
        Parameters:
            seconds (double): the seconds to be set
        
        
        """
        ...
    def setTimeSystem(self, system: org.orekit.gnss.TimeSystem) -> None:
        """
        Set the time system used in this SP3 file.
        
        Parameters:
            system (TimeSystem): the time system to be set
        
        
        """
        ...
    def setType(self, fileType: SP3FileType) -> None:
        """
        Set the file type for this SP3 file.
        
        Parameters:
            fileType (SP3FileType): the file type to be set
        
        
        """
        ...
    def setVersion(self, version: str) -> None:
        """
        Set the file version.
        
        Parameters:
            version (char): file version
        
        
        """
        ...

class SP3OrbitType(java.lang.Enum['SP3OrbitType']):
    """
    Orbit type indicator.
    """
    FIT: typing.ClassVar['SP3OrbitType'] = ...
    EXT: typing.ClassVar['SP3OrbitType'] = ...
    BCT: typing.ClassVar['SP3OrbitType'] = ...
    HLM: typing.ClassVar['SP3OrbitType'] = ...
    OTHER: typing.ClassVar['SP3OrbitType'] = ...
    @staticmethod
    def parseType(s: str) -> 'SP3OrbitType':
        """
        Parse a string to get the type.
        
        Parameters:
            s (String): string to parse
        
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
    def valueOf(name: str) -> 'SP3OrbitType':
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
    def values() -> typing.MutableSequence['SP3OrbitType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SP3OrbitType c : SP3OrbitType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SP3Parser(org.orekit.files.general.EphemerisFileParser[SP3]):
    """
    A parser for the SP3 orbit file format. It supports all formats from sp3-a to sp3-d.
    
    Note: this parser is thread-safe, so calling parse from different threads is allowed.
    
    Also see:
        txt,
        txt,
        pdf
    """
    DEFAULT_INTERPOLATION_SAMPLES: typing.ClassVar[int] = ...
    """
    Default number of samples to use when interpolating SP3 coordinates.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, mu: float, interpolationSamples: int, frameBuilder: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]]): ...
    @typing.overload
    def __init__(self, mu: float, interpolationSamples: int, frameBuilder: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]], timeScales: org.orekit.time.TimeScales): ...
    def parse(self, source: org.orekit.data.DataSource) -> SP3:
        """
        Description copied from interface: parse Parse an ephemeris file from a data source.
        
        Specified by: parse in interface EphemerisFileParser
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed ephemeris file.
        
        
        """
        ...

class SP3Segment(org.orekit.files.general.EphemerisFile.EphemerisSegment[SP3Coordinate]):
    """
    One segment of an SP3Ephemeris.
    
    Since:
        12.0
    """
    def __init__(self, mu: float, frame: org.orekit.frames.Frame, interpolationSamples: int, filter: org.orekit.utils.CartesianDerivativesFilter):
        """
        Simple constructor.
        
        Parameters:
            mu (double): standard gravitational parameter to use for creating Orbit from the ephemeris data.
            frame (Frame): reference frame
            interpolationSamples (int): number of points to use for interpolation
            filter (CartesianDerivativesFilter): available derivatives
        
        
        """
        ...
    def addCoordinate(self, coord: SP3Coordinate) -> None:
        """
        Adds a new P/V coordinate.
        
        Parameters:
            coord (SP3Coordinate): the P/V coordinate of the satellite
        
        
        """
        ...
    def extractClockModel(self) -> org.orekit.time.ClockModel:
        """
        Extract the clock model.
        
        If some clock or clock rate are present in the SP3 files as default values (999999.999999), then they filtered out here when building the clock model, so interpolation will work if at least there are some remaining regular values.
        
        Returns:
            extracted clock model
        
        Since:
            12.1
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
        Get which derivatives of position are available in this ephemeris segment.
        
        While getCoordinates always returns position, velocity, and acceleration the return value from this method indicates which of those are in the ephemeris file and are actually valid.
        
        Specified by: getAvailableDerivatives in interface EphemerisSegment
        
        Returns:
            a value indicating if the file contains velocity and/or acceleration data.
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[SP3Coordinate]:
        """
        Get the coordinates for this ephemeris segment in getFrame.
        
        Specified by: getCoordinates in interface EphemerisSegment
        
        Returns:
            a list of state vectors in chronological order. The coordinates are not necessarily evenly spaced in time. The value of
            getAvailableDerivatives indicates if the velocity or
            accelerations were specified in the file. Any position, velocity, or acceleration coordinates that are not specified in
            the ephemeris file are zero in the returned values.
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame for this ephemeris segment. The defining frame for getCoordinates.
        
        Specified by: getFrame in interface EphemerisSegment
        
        Returns:
            the reference frame for this segment. Never null.
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
        Get the number of samples to use in interpolation.
        
        Specified by: getInterpolationSamples in interface EphemerisSegment
        
        Returns:
            the number of points to use for interpolation.
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the standard gravitational parameter for the satellite.
        
        Specified by: getMu in interface EphemerisSegment
        
        Returns:
            the gravitational parameter used in getPropagator, in
            m³/s².
        
        
        """
        ...
    @typing.overload
    def getPropagator(self) -> org.orekit.propagation.BoundedPropagator:
        """
        View this ephemeris segment as a propagator.
        
        In order to view the ephemeris for this satellite as a Propagator several conditions must be met. An Orekit Frame must be constructable from the frame specification in the ephemeris file. This condition is met when getFrame return normally. Additionally, getMu must return a valid value. If these conditions are not met an OrekitException may be thrown by this method or by one of the methods of the returned Propagator.
        
        The AttitudeProvider used is a FrameAlignedProvider aligned with the getInertialFrame
        
        Each call to this method creates a new propagator.
        
        Specified by: getPropagator in interface EphemerisSegment
        
        Returns:
            a propagator for this ephemeris segment.
        
        """
        ...
    @typing.overload
    def getPropagator(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> org.orekit.propagation.BoundedPropagator:
        """
        View this ephemeris segment as a propagator.
        
        In order to view the ephemeris for this satellite as a Propagator several conditions must be met. An Orekit Frame must be constructable from the frame specification in the ephemeris file. This condition is met when getFrame return normally. Additionally, getMu must return a valid value. If these conditions are not met an OrekitException may be thrown by this method or by one of the methods of the returned Propagator.
        
        Each call to this method creates a new propagator.
        
        Specified by: getPropagator in interface EphemerisSegment
        
        Parameters:
            attitudeProvider (AttitudeProvider): provider for attitude computation
        
        Returns:
            a propagator for this ephemeris segment.
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of this ephemeris segment.
        
        The date returned by this method is equivalent to getMinDate().
        
        Specified by: getStart in interface EphemerisSegment
        
        Returns:
            ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of this ephemeris segment.
        
        The date returned by this method is equivalent to getMaxDate().
        
        Specified by: getStop in interface EphemerisSegment
        
        Returns:
            ephemeris segment end date.
        
        
        """
        ...

class SP3Utils:
    """
    Constants for SP3 files.
    
    Since:
        12.0
    """
    DEFAULT_CLOCK_VALUE: typing.ClassVar[float] = ...
    """
    Bad or absent clock values are to be set to 999999.999999.
    
    Also see:
        constant
    
    
    """
    DEFAULT_CLOCK_RATE_VALUE: typing.ClassVar[float] = ...
    """
    Bad or absent clock rate values are to be set to 999999.999999.
    
    Also see:
        constant
    
    
    """
    POS_VEL_BASE_ACCURACY: typing.ClassVar[float] = ...
    """
    Base for general position/velocity accuracy.
    
    Also see:
        constant
    
    
    """
    POSITION_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Position unit.
    """
    POSITION_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Position accuracy unit.
    """
    VELOCITY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Velocity unit.
    """
    VELOCITY_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Velocity accuracy unit.
    """
    CLOCK_ADDITIONAL_STATE: typing.ClassVar[str] = ...
    """
    Additional state name for clock.
    
    Since:
        12.1
    
    Also see:
        constant
    
    
    """
    CLOCK_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Clock unit.
    """
    CLOCK_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Clock accuracy unit.
    """
    CLOCK_RATE_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Clock rate unit.
    """
    CLOCK_RATE_ACCURACY_UNIT: typing.ClassVar[org.orekit.utils.units.Unit] = ...
    """
    Clock rate accuracy unit.
    """
    @staticmethod
    def indexAccuracy(unit: org.orekit.utils.units.Unit, base: float, accuracy: float) -> int:
        """
        Convert an accuracy from SI units.
        
        Parameters:
            unit (Unit): accuracy unit
            base (double): base
            accuracy (double): in SI units
        
        Returns:
            index of accuracy
        
        
        """
        ...
    @staticmethod
    def siAccuracy(unit: org.orekit.utils.units.Unit, base: float, accuracyIndex: int) -> float:
        """
        Convert an accuracy to SI units.
        
        Parameters:
            unit (Unit): accuracy unit
            base (double): base
            accuracyIndex (int): index of accuracy
        
        Returns:
            accuracy in SI units
        
        
        """
        ...

class SP3Writer:
    """
    Writer for SP3 file.
    
    Since:
        12.0
    """
    def __init__(self, output: java.lang.Appendable, outputName: str, timeScales: org.orekit.time.TimeScales):
        """
        Simple constructor.
        
        Parameters:
            output (Appendable): destination of generated output
            outputName (String): output name for error messages
            timeScales (TimeScales): set of time scales used for parsing dates
        
        
        """
        ...
    def write(self, sp3: SP3) -> None:
        """
        Write a SP3 file.
        
        Parameters:
            sp3 (SP3): SP3 file to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...


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
