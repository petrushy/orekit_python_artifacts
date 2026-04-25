
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.gnss.antenna
import org.orekit.gnss.attitude
import org.orekit.gnss.metric
import org.orekit.gnss.rflink
import org.orekit.propagation
import org.orekit.propagation.analytical.gnss.data
import org.orekit.time
import org.orekit.utils
import typing



class DOP:
    """
    This class is a container for the result of a single DOP computation.
    
    Since:
        8.0
    
    Also see:
        `Dilution of precision <http://en.wikipedia.org/wiki/Dilution_of_precision_%28GPS%29>`
    """
    def __init__(self, location: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate, gnssNb: int, gdop: float, pdop: float, hdop: float, vdop: float, tdop: float):
        """
        Constructor.
        
        Parameters:
            location (GeodeticPoint): location with respect to the Earth where DOP was calculated
            date (AbsoluteDate): date when all DOP was calculated
            gnssNb (int): number of GNSS satellites taken into account for DOP computation
            gdop (double): the geometric dilution of precision
            pdop (double): the position dilution of precision
            hdop (double): the horizontal dilution of precision
            vdop (double): the vertical dilution of precision
            tdop (double): the time dilution of precision
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the calculation date of the DOP.
        
        Returns:
            the calculation date of the DOP
        
        
        """
        ...
    def getGdop(self) -> float:
        """
        Gets the geometric dilution of precision.
        
        Returns:
            the GDOP
        
        
        """
        ...
    def getGnssNb(self) -> int:
        """
        Gets the number of GNSS satellites taken into account for DOP computation.
        
        Returns:
            the number of GNSS satellites taken into account for DOP computation
        
        
        """
        ...
    def getHdop(self) -> float:
        """
        Gets the horizontal dilution of precision.
        
        Returns:
            the HDOP
        
        
        """
        ...
    def getLocation(self) -> org.orekit.bodies.GeodeticPoint:
        """
        Gets the location with respect to the Earth where DOP was calculated.
        
        Returns:
            the location with respect to the Earth where DOP was calculated
        
        
        """
        ...
    def getPdop(self) -> float:
        """
        Gets the position dilution of precision.
        
        Returns:
            the PDOP
        
        
        """
        ...
    def getTdop(self) -> float:
        """
        Gets the time dilution of precision.
        
        Returns:
            the TDOP
        
        
        """
        ...
    def getVdop(self) -> float:
        """
        Gets the vertical dilution of precision.
        
        Returns:
            the VDOP
        
        
        """
        ...

class DOPComputer:
    """
    This class aims at computing the dilution of precision.
    
    Since:
        8.0
    
    Also see:
        `Dilution of precision <http://en.wikipedia.org/wiki/Dilution_of_precision_%28GPS%29>`
    """
    DOP_MIN_ELEVATION: typing.ClassVar[float] = ...
    """
    Minimum elevation : 0°.
    
    Also see:
        constant
    
    
    """
    def compute(self, date: org.orekit.time.AbsoluteDate, gnss: java.util.List[org.orekit.propagation.Propagator]) -> DOP:
        """
        Compute the DOP at a given date for a set of GNSS spacecrafts.
        
        Four GNSS spacecraft at least are needed to compute the DOP. If less than 4 propagators are provided, an exception will be thrown. If less than 4 spacecrafts are visible at the date, all DOP values will be set to Double.
        
        Parameters:
            date (AbsoluteDate): the computation date
            gnss (List<Propagator> gnss): the propagators for GNSS spacecraft involved in the DOP computation
        
        Returns:
            the DOP at the location
        
        
        """
        ...
    @staticmethod
    def create(shape: org.orekit.bodies.OneAxisEllipsoid, location: org.orekit.bodies.GeodeticPoint) -> 'DOPComputer':
        """
        Creates a DOP computer for one location.
        
        A minimum elevation of 0° is taken into account to compute visibility between the location and the GNSS spacecrafts.
        
        Parameters:
            shape (OneAxisEllipsoid): the body shape on which the location is defined
            location (GeodeticPoint): the point of interest
        
        Returns:
            a configured DOP computer
        
        
        """
        ...
    def getElevationMask(self) -> org.orekit.utils.ElevationMask:
        """
        Get the elevation mask.
        
        Returns:
            the elevation mask
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
        Get the minimum elevation.
        
        Returns:
            the minimum elevation (rad)
        
        
        """
        ...
    def withElevationMask(self, newElevationMask: org.orekit.utils.ElevationMask) -> 'DOPComputer':
        """
        Set the elevation mask.
        
        This will override the min elevation if it has been configured as such previously.
        
        Parameters:
            newElevationMask (ElevationMask): elevation mask to use for the computation
        
        Returns:
            a new detector with updated configuration (the instance is not changed)
        
        Also see:
            getElevationMask
        
        
        """
        ...
    def withMinElevation(self, newMinElevation: float) -> 'DOPComputer':
        """
        Set the minimum elevation.
        
        This will override an elevation mask if it has been configured as such previously.
        
        Parameters:
            newMinElevation (double): minimum elevation for visibility (rad)
        
        Returns:
            a new DOP computer with updated configuration (the instance is not changed)
        
        Also see:
            getMinElevation
        
        
        """
        ...

class IGSUtils:
    """
    Utility for IGS files.
    
    Since:
        12.1
    """
    @staticmethod
    def frameName(frame: org.orekit.frames.Frame) -> str:
        """
        Guess a frame name.
        
        If the frame is not compatible with guessFrame, an exception will be triggered
        
        Parameters:
            frame (Frame): frame from which we want the name
        
        Returns:
            name compatible with guessFrame
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def guessFrame(string: str) -> org.orekit.frames.Frame:
        """
        Default string to Frame conversion for SP3Parser or RinexClockParser.
        
        Various frame names are supported:
        
          - IER##, ITR##, ITRF##, IGS##, IGb##, or SLR##, where ## is a two digits number, the number will be used to build the
            appropriate ITRFVersion
          - GCRF (left or right justified) for GCRF inertial frame
          - EME00 or EME2K for EME2000 inertial frame
          - for all other names (for example if name is UNDEF or WGS84), then a default getITRF
            frame will be selected
        
        Note that using inertial frames in classical products like SP3 files is non-standard, it is supported by Orekit, but may not be supported by other programs, so they should be used with caution when writing files.
        
        Parameters:
            frames (Frames): frames factory
            name (String): of the frame.
        
        Returns:
            guessed frame
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def guessFrame(frames: org.orekit.frames.Frames, string: str) -> org.orekit.frames.Frame: ...

class MeasurementType(java.lang.Enum['MeasurementType']):
    """
    Enumerate for measurement type.
    
    Since:
        9.2
    """
    PSEUDO_RANGE: typing.ClassVar['MeasurementType'] = ...
    CARRIER_PHASE: typing.ClassVar['MeasurementType'] = ...
    DOPPLER: typing.ClassVar['MeasurementType'] = ...
    SIGNAL_STRENGTH: typing.ClassVar['MeasurementType'] = ...
    COMBINED_RANGE_PHASE: typing.ClassVar['MeasurementType'] = ...
    TWO_WAY_TIME_TRANSFER: typing.ClassVar['MeasurementType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'MeasurementType':
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
    def values() -> typing.MutableSequence['MeasurementType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (MeasurementType c : MeasurementType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ObservationTimeScale(java.lang.Enum['ObservationTimeScale']):
    """
    Observation time scales.
    
    Since:
        12.0
    """
    GPS: typing.ClassVar['ObservationTimeScale'] = ...
    GAL: typing.ClassVar['ObservationTimeScale'] = ...
    GLO: typing.ClassVar['ObservationTimeScale'] = ...
    QZS: typing.ClassVar['ObservationTimeScale'] = ...
    BDT: typing.ClassVar['ObservationTimeScale'] = ...
    IRN: typing.ClassVar['ObservationTimeScale'] = ...
    def getTimeScale(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScale:
        """
        Get time scale.
        
        Parameters:
            timeScales (TimeScales): time scales factory
        
        Returns:
            time scale
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ObservationTimeScale':
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
    def values() -> typing.MutableSequence['ObservationTimeScale']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ObservationTimeScale c : ObservationTimeScale.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ObservationType:
    """
    Observation Types for GNSS measurements.
    
    Since:
        13.0
    """
    def getMeasurementType(self) -> MeasurementType:
        """
        Get the measurement type.
        
        Returns:
            measurement type
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the observation type.
        
        Returns:
            name of the observation type
        
        
        """
        ...
    def getSignal(self, system: 'SatelliteSystem') -> 'GnssSignal':
        """
        Get the signal for a specified satellite system.
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            signal for the satellite system, or null if satellite system not compatible
        
        
        """
        ...
    def getSignalCode(self) -> 'SignalCode':
        """
        Get the signal code.
        
        Returns:
            signal code
        
        
        """
        ...

class RadioWave:
    """
    Top level interface for radio waves.
    
    Since:
        12.1
    """
    ONE_MILLI_HERTZ: typing.ClassVar[float] = ...
    """
    Default 1MHz tolerance for closeTo.
    
    Since:
        13.0
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def closeTo(self, radioWave: typing.Union['RadioWave', typing.Callable]) -> bool:
        """
        Check if two radio waves are closer than ONE_MILLI_HERTZ.
        
        Parameters:
            other (RadioWave): other radio wave to check against instance
        
        Returns:
            true if radio waves are closer than ONE_MILLI_HERTZ
        
        Since:
            13.0
        
        Also see:
            closeTo
        
        Check if two radio waves are closer than tolerance.
        
        Parameters:
            other (RadioWave): other radio wave to check against instance
            tolerance (double): frequency tolerance in Hz
        
        Returns:
            true if radio waves are closer than tolerance
        
        Since:
            13.0
        
        Also see:
            ONE_MILLI_HERTZ, closeTo
        
        
        """
        ...
    @typing.overload
    def closeTo(self, radioWave: typing.Union['RadioWave', typing.Callable], double: float) -> bool: ...
    def getFrequency(self) -> float:
        """
        Get the value of the frequency in Hz.
        
        Returns:
            value of the frequency in Hz
        
        Also see:
            getWavelength
        
        
        """
        ...
    def getWavelength(self) -> float:
        """
        Get the wavelength in meters.
        
        Returns:
            wavelength in meters
        
        Also see:
            getFrequency
        
        
        """
        ...

class SEMParser(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader):
    """
    This class reads SEM almanac files and provides GPSAlmanac.
    
    The definition of a SEM almanac comes from the `U.S. COAST GUARD NAVIGATION CENTER <http://www.navcen.uscg.gov/?pageName=gpsSem>`.
    
    The format of the files holding SEM almanacs is not precisely specified, so the parsing rules have been deduced from the downloadable files at `NAVCEN <http://www.navcen.uscg.gov/?pageName=gpsAlmanacs>` and at SEM.
    
    Since:
        8.0
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales): ...
    def getAlmanacs(self) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GPSAlmanac]:
        """
        Gets all the GPSAlmanac read from the file.
        
        Returns:
            the list of GPSAlmanac from the file
        
        
        """
        ...
    def getPRNNumbers(self) -> java.util.List[int]:
        """
        Gets the PRN numbers of all the GPSAlmanac read from the file.
        
        Returns:
            the PRN numbers of all the GPSAlmanac read from the file
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
        Description copied from class: getSupportedNames Get the supported names regular expression.
        
        Overrides: getSupportedNames in class AbstractSelfFeedingLoader
        
        Returns:
            the supported names.
        
        Also see:
            feed
        
        
        """
        ...
    @typing.overload
    def loadData(self) -> None:
        """
        Loads almanacs.
        
        The almanacs already loaded in the instance will be discarded and replaced by the newly loaded data.
        
        This feature is useful when the file selection is already set up by the DataProvidersManager configuration. public void loadData (InputStream input, String name) throws IOException, ParseException, OrekitException
        
        Description copied from interface: loadData Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...
    @typing.overload
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def stillAcceptsData(self) -> bool:
        """
        Description copied from interface: stillAcceptsData Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
        Returns:
            true while the loader still accepts new data
        
        
        """
        ...

class SatInSystem:
    """
    Container for satellite system and PRN.
    
    Since:
        12.0
    """
    ANY_PRN: typing.ClassVar[int] = ...
    """
    Value representing all PRNs in the system.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, satelliteSystem: 'SatelliteSystem', int: int): ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getPRN(self) -> int:
        """
        Get the Pseudo Random Number of the satellite.
        
        Returns:
            Pseudo Random Number of the satellite, or ANY_PRN to represent any PRN in the
            system
        
        
        """
        ...
    def getSystem(self) -> 'SatelliteSystem':
        """
        Get the system this satellite belongs to.
        
        Returns:
            system this satellite belongs to
        
        
        """
        ...
    def getTwoDigitsRinexPRN(self) -> int:
        """
        Get a 2-digits Pseudo Random Number for RINEX files.
        
        Returns:
            2-digits Pseudo Random Number for RINEX files
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class SatelliteSystem(java.lang.Enum['SatelliteSystem']):
    """
    Enumerate for satellite system.
    
    Since:
        9.2
    """
    USER_DEFINED_A: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_B: typing.ClassVar['SatelliteSystem'] = ...
    BEIDOU: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_D: typing.ClassVar['SatelliteSystem'] = ...
    GALILEO: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_F: typing.ClassVar['SatelliteSystem'] = ...
    GPS: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_H: typing.ClassVar['SatelliteSystem'] = ...
    NAVIC: typing.ClassVar['SatelliteSystem'] = ...
    QZSS: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_K: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_L: typing.ClassVar['SatelliteSystem'] = ...
    MIXED: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_N: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_O: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_P: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_Q: typing.ClassVar['SatelliteSystem'] = ...
    GLONASS: typing.ClassVar['SatelliteSystem'] = ...
    SBAS: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_T: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_U: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_V: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_W: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_X: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_Y: typing.ClassVar['SatelliteSystem'] = ...
    USER_DEFINED_Z: typing.ClassVar['SatelliteSystem'] = ...
    def getKey(self) -> str:
        """
        Get the key for the system.
        
        Returns:
            key for the system
        
        
        """
        ...
    def getObservationTimeScale(self) -> ObservationTimeScale:
        """
        Get observation time scale for satellite system.
        
        Returns:
            observation time scale, null if there are not
        
        Since:
            12.0
        
        
        """
        ...
    @staticmethod
    def parseSatelliteSystem(s: str) -> 'SatelliteSystem':
        """
        Parse a string to get the satellite system.
        
        The string first character must be the satellite system.
        
        Parameters:
            s (String): string to parse
        
        Returns:
            the satellite system
        
        Raises:
            OrekitIllegalArgumentException: if the string does not correspond to a satellite system key
        
        
        """
        ...
    @staticmethod
    def parseSatelliteSystemWithGPSDefault(s: str) -> 'SatelliteSystem':
        """
        Parse a string to get the satellite system.
        
        The string first character must be the satellite system, or empty to get GPS as default
        
        Parameters:
            s (String): string to parse
        
        Returns:
            the satellite system
        
        Since:
            12.0
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'SatelliteSystem':
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
    def values() -> typing.MutableSequence['SatelliteSystem']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SatelliteSystem c : SatelliteSystem.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SignalCode(java.lang.Enum['SignalCode']):
    """
    Enumerate for satellite signal code.
    
    Since:
        10.1
    """
    A: typing.ClassVar['SignalCode'] = ...
    B: typing.ClassVar['SignalCode'] = ...
    C: typing.ClassVar['SignalCode'] = ...
    D: typing.ClassVar['SignalCode'] = ...
    E: typing.ClassVar['SignalCode'] = ...
    I: typing.ClassVar['SignalCode'] = ...
    L: typing.ClassVar['SignalCode'] = ...
    M: typing.ClassVar['SignalCode'] = ...
    N: typing.ClassVar['SignalCode'] = ...
    P: typing.ClassVar['SignalCode'] = ...
    Q: typing.ClassVar['SignalCode'] = ...
    S: typing.ClassVar['SignalCode'] = ...
    W: typing.ClassVar['SignalCode'] = ...
    X: typing.ClassVar['SignalCode'] = ...
    Y: typing.ClassVar['SignalCode'] = ...
    Z: typing.ClassVar['SignalCode'] = ...
    CODELESS: typing.ClassVar['SignalCode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'SignalCode':
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
    def values() -> typing.MutableSequence['SignalCode']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SignalCode c : SignalCode.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TimeSystem(java.lang.Enum['TimeSystem']):
    """
    Enumerate for the time systems used in navigation files.
    
    Since:
        11.0
    """
    GPS: typing.ClassVar['TimeSystem'] = ...
    GLONASS: typing.ClassVar['TimeSystem'] = ...
    GALILEO: typing.ClassVar['TimeSystem'] = ...
    TAI: typing.ClassVar['TimeSystem'] = ...
    UTC: typing.ClassVar['TimeSystem'] = ...
    QZSS: typing.ClassVar['TimeSystem'] = ...
    BEIDOU: typing.ClassVar['TimeSystem'] = ...
    NAVIC: typing.ClassVar['TimeSystem'] = ...
    SBAS: typing.ClassVar['TimeSystem'] = ...
    GMT: typing.ClassVar['TimeSystem'] = ...
    UNKNOWN: typing.ClassVar['TimeSystem'] = ...
    def getKey(self) -> str:
        """
        Get the 3 letters key of the time system.
        
        Returns:
            3 letters key
        
        Since:
            12.0
        
        
        """
        ...
    def getOneLetterCode(self) -> str:
        """
        Get the one letter code.
        
        Returns:
            one letter code (may be null for non-GNSS time systems)
        
        Since:
            12.2
        
        
        """
        ...
    def getTimeScale(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScale:
        """
        Get the time scale corresponding to time system.
        
        Parameters:
            timeScales (TimeScales): the set of time scales to use
        
        Returns:
            the time scale corresponding to time system in the set of time scales
        
        
        """
        ...
    def getTwoLettersCode(self) -> str:
        """
        Get the two letters code.
        
        Returns:
            two letters code (may be null for non-GNSS time systems)
        
        Since:
            12.2
        
        
        """
        ...
    @staticmethod
    def parseOneLetterCode(code: str) -> 'TimeSystem':
        """
        Parse a string to get the time system.
        
        The string must be the one letters code of the time system. The one letter code is the RINEX GNSS system flag.
        
        Parameters:
            code (String): string to parse
        
        Returns:
            the time system
        
        Raises:
            OrekitIllegalArgumentException: if the string does not correspond to a time system key
        
        
        """
        ...
    @staticmethod
    def parseTimeSystem(s: str) -> 'TimeSystem':
        """
        Parse a string to get the time system.
        
        The string must be the time system.
        
        Parameters:
            s (String): string to parse
        
        Returns:
            the time system
        
        Raises:
            OrekitIllegalArgumentException: if the string does not correspond to a time system key
        
        
        """
        ...
    @staticmethod
    def parseTwoLettersCode(code: str) -> 'TimeSystem':
        """
        Parse a string to get the time system.
        
        The string must be the two letters code of the time system.
        
        Parameters:
            code (String): string to parse
        
        Returns:
            the time system
        
        Raises:
            OrekitIllegalArgumentException: if the string does not correspond to a time system key
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'TimeSystem':
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
    def values() -> typing.MutableSequence['TimeSystem']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (TimeSystem c : TimeSystem.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class YUMAParser(org.orekit.data.AbstractSelfFeedingLoader, org.orekit.data.DataLoader):
    """
    This class reads Yuma almanac files and provides GPSAlmanac.
    
    The definition of a Yuma almanac comes from the `U.S. COAST GUARD NAVIGATION CENTER <http://www.navcen.uscg.gov/?pageName=gpsYuma>`.
    
    The format of the files holding Yuma almanacs is not precisely specified, so the parsing rules have been deduced from the downloadable files at `NAVCEN <http://www.navcen.uscg.gov/?pageName=gpsAlmanacs>` and at Yuma.
    
    Since:
        8.0
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales): ...
    def getAlmanacs(self) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GPSAlmanac]:
        """
        Gets all the GPSAlmanac read from the file.
        
        Returns:
            the list of GPSAlmanac from the file
        
        
        """
        ...
    def getPRNNumbers(self) -> java.util.List[int]:
        """
        Gets the PRN numbers of all the GPSAlmanac read from the file.
        
        Returns:
            the PRN numbers of all the GPSAlmanac read from the file
        
        
        """
        ...
    def getSupportedNames(self) -> str:
        """
        Description copied from class: getSupportedNames Get the supported names regular expression.
        
        Overrides: getSupportedNames in class AbstractSelfFeedingLoader
        
        Returns:
            the supported names.
        
        Also see:
            feed
        
        
        """
        ...
    @typing.overload
    def loadData(self) -> None:
        """
        Loads almanacs.
        
        The almanacs already loaded in the instance will be discarded and replaced by the newly loaded data.
        
        This feature is useful when the file selection is already set up by the DataProvidersManager configuration. public void loadData (InputStream input, String name) throws IOException, ParseException, OrekitException
        
        Description copied from interface: loadData Load data from a stream.
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): data input stream
            name (String): name of the file (or zip entry)
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed or if some loader specific error occurs
            OrekitException: 
        
        """
        ...
    @typing.overload
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def stillAcceptsData(self) -> bool:
        """
        Description copied from interface: stillAcceptsData Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
        Returns:
            true while the loader still accepts new data
        
        
        """
        ...

class GnssSignal(RadioWave):
    """
    Intermediate level interface for radio waves related to GNSS common frequency.
    
    Since:
        12.1
    """
    F0: typing.ClassVar[float] = ...
    """
    Common frequency F0 in Hz (10.23 MHz).
    
    Also see:
        constant
    
    
    """
    def getName(self) -> str:
        """
        Get the RINEX name for the frequency.
        
        Returns:
            RINEX name for the frequency
        
        
        """
        ...
    def getRatio(self) -> float:
        """
        Get the ratio f/f0, where F0 is the common frequency.
        
        Returns:
            ratio f/f0, where F0 is the common frequency
        
        Also see:
            F0, getFrequency
        
        
        """
        ...
    def getSatelliteSystem(self) -> SatelliteSystem:
        """
        Get the satellite system for which this frequency is defined.
        
        Returns:
            satellite system for which this frequency is defined
        
        
        """
        ...

class PredefinedObservationType(java.lang.Enum['PredefinedObservationType'], ObservationType):
    """
    Enumerate for all the Observation Types for Rinex 2 and 3. For Rinex 2, there is an two-character enumerate composed of the Observation Code (C,P,L,D,S) and the Frequency code (1,2,5,6,7,8). For Rinex 3 there is a three-character enumerate composed of the Observation Code (C,L,D,S), the frequency code (1,2,5,6,7,8) and a final attribute depending on the tracking mode or channel.
    """
    C1: typing.ClassVar['PredefinedObservationType'] = ...
    C2: typing.ClassVar['PredefinedObservationType'] = ...
    C5: typing.ClassVar['PredefinedObservationType'] = ...
    C6: typing.ClassVar['PredefinedObservationType'] = ...
    C7: typing.ClassVar['PredefinedObservationType'] = ...
    C8: typing.ClassVar['PredefinedObservationType'] = ...
    P1: typing.ClassVar['PredefinedObservationType'] = ...
    P2: typing.ClassVar['PredefinedObservationType'] = ...
    L1: typing.ClassVar['PredefinedObservationType'] = ...
    L2: typing.ClassVar['PredefinedObservationType'] = ...
    L5: typing.ClassVar['PredefinedObservationType'] = ...
    L6: typing.ClassVar['PredefinedObservationType'] = ...
    L7: typing.ClassVar['PredefinedObservationType'] = ...
    L8: typing.ClassVar['PredefinedObservationType'] = ...
    LA: typing.ClassVar['PredefinedObservationType'] = ...
    LB: typing.ClassVar['PredefinedObservationType'] = ...
    LC: typing.ClassVar['PredefinedObservationType'] = ...
    LD: typing.ClassVar['PredefinedObservationType'] = ...
    D1: typing.ClassVar['PredefinedObservationType'] = ...
    D2: typing.ClassVar['PredefinedObservationType'] = ...
    D5: typing.ClassVar['PredefinedObservationType'] = ...
    D6: typing.ClassVar['PredefinedObservationType'] = ...
    D7: typing.ClassVar['PredefinedObservationType'] = ...
    D8: typing.ClassVar['PredefinedObservationType'] = ...
    S1: typing.ClassVar['PredefinedObservationType'] = ...
    S2: typing.ClassVar['PredefinedObservationType'] = ...
    S5: typing.ClassVar['PredefinedObservationType'] = ...
    S6: typing.ClassVar['PredefinedObservationType'] = ...
    S7: typing.ClassVar['PredefinedObservationType'] = ...
    S8: typing.ClassVar['PredefinedObservationType'] = ...
    C1A: typing.ClassVar['PredefinedObservationType'] = ...
    C1B: typing.ClassVar['PredefinedObservationType'] = ...
    C1C: typing.ClassVar['PredefinedObservationType'] = ...
    C1D: typing.ClassVar['PredefinedObservationType'] = ...
    C1E: typing.ClassVar['PredefinedObservationType'] = ...
    C1I: typing.ClassVar['PredefinedObservationType'] = ...
    C1L: typing.ClassVar['PredefinedObservationType'] = ...
    C1M: typing.ClassVar['PredefinedObservationType'] = ...
    C1P: typing.ClassVar['PredefinedObservationType'] = ...
    C1Q: typing.ClassVar['PredefinedObservationType'] = ...
    C1R: typing.ClassVar['PredefinedObservationType'] = ...
    C1S: typing.ClassVar['PredefinedObservationType'] = ...
    C1W: typing.ClassVar['PredefinedObservationType'] = ...
    C1X: typing.ClassVar['PredefinedObservationType'] = ...
    C1Y: typing.ClassVar['PredefinedObservationType'] = ...
    C1Z: typing.ClassVar['PredefinedObservationType'] = ...
    C2C: typing.ClassVar['PredefinedObservationType'] = ...
    C2D: typing.ClassVar['PredefinedObservationType'] = ...
    C2I: typing.ClassVar['PredefinedObservationType'] = ...
    C2L: typing.ClassVar['PredefinedObservationType'] = ...
    C2M: typing.ClassVar['PredefinedObservationType'] = ...
    C2P: typing.ClassVar['PredefinedObservationType'] = ...
    C2Q: typing.ClassVar['PredefinedObservationType'] = ...
    C2R: typing.ClassVar['PredefinedObservationType'] = ...
    C2S: typing.ClassVar['PredefinedObservationType'] = ...
    C2W: typing.ClassVar['PredefinedObservationType'] = ...
    C2X: typing.ClassVar['PredefinedObservationType'] = ...
    C2Y: typing.ClassVar['PredefinedObservationType'] = ...
    C3I: typing.ClassVar['PredefinedObservationType'] = ...
    C3Q: typing.ClassVar['PredefinedObservationType'] = ...
    C3X: typing.ClassVar['PredefinedObservationType'] = ...
    C4A: typing.ClassVar['PredefinedObservationType'] = ...
    C4B: typing.ClassVar['PredefinedObservationType'] = ...
    C4X: typing.ClassVar['PredefinedObservationType'] = ...
    C5A: typing.ClassVar['PredefinedObservationType'] = ...
    C5B: typing.ClassVar['PredefinedObservationType'] = ...
    C5C: typing.ClassVar['PredefinedObservationType'] = ...
    C5D: typing.ClassVar['PredefinedObservationType'] = ...
    C5I: typing.ClassVar['PredefinedObservationType'] = ...
    C5P: typing.ClassVar['PredefinedObservationType'] = ...
    C5Q: typing.ClassVar['PredefinedObservationType'] = ...
    C5X: typing.ClassVar['PredefinedObservationType'] = ...
    C5Z: typing.ClassVar['PredefinedObservationType'] = ...
    C6A: typing.ClassVar['PredefinedObservationType'] = ...
    C6B: typing.ClassVar['PredefinedObservationType'] = ...
    C6C: typing.ClassVar['PredefinedObservationType'] = ...
    C6D: typing.ClassVar['PredefinedObservationType'] = ...
    C6E: typing.ClassVar['PredefinedObservationType'] = ...
    C6I: typing.ClassVar['PredefinedObservationType'] = ...
    C6L: typing.ClassVar['PredefinedObservationType'] = ...
    C6P: typing.ClassVar['PredefinedObservationType'] = ...
    C6Q: typing.ClassVar['PredefinedObservationType'] = ...
    C6S: typing.ClassVar['PredefinedObservationType'] = ...
    C6X: typing.ClassVar['PredefinedObservationType'] = ...
    C6Z: typing.ClassVar['PredefinedObservationType'] = ...
    C7D: typing.ClassVar['PredefinedObservationType'] = ...
    C7I: typing.ClassVar['PredefinedObservationType'] = ...
    C7P: typing.ClassVar['PredefinedObservationType'] = ...
    C7Q: typing.ClassVar['PredefinedObservationType'] = ...
    C7X: typing.ClassVar['PredefinedObservationType'] = ...
    C7Z: typing.ClassVar['PredefinedObservationType'] = ...
    C8D: typing.ClassVar['PredefinedObservationType'] = ...
    C8I: typing.ClassVar['PredefinedObservationType'] = ...
    C8P: typing.ClassVar['PredefinedObservationType'] = ...
    C8Q: typing.ClassVar['PredefinedObservationType'] = ...
    C8X: typing.ClassVar['PredefinedObservationType'] = ...
    C9A: typing.ClassVar['PredefinedObservationType'] = ...
    C9B: typing.ClassVar['PredefinedObservationType'] = ...
    C9C: typing.ClassVar['PredefinedObservationType'] = ...
    C9X: typing.ClassVar['PredefinedObservationType'] = ...
    C0: typing.ClassVar['PredefinedObservationType'] = ...
    CA: typing.ClassVar['PredefinedObservationType'] = ...
    CB: typing.ClassVar['PredefinedObservationType'] = ...
    CC: typing.ClassVar['PredefinedObservationType'] = ...
    CD: typing.ClassVar['PredefinedObservationType'] = ...
    D1A: typing.ClassVar['PredefinedObservationType'] = ...
    D1B: typing.ClassVar['PredefinedObservationType'] = ...
    D1C: typing.ClassVar['PredefinedObservationType'] = ...
    D1D: typing.ClassVar['PredefinedObservationType'] = ...
    D1E: typing.ClassVar['PredefinedObservationType'] = ...
    D1I: typing.ClassVar['PredefinedObservationType'] = ...
    D1L: typing.ClassVar['PredefinedObservationType'] = ...
    D1M: typing.ClassVar['PredefinedObservationType'] = ...
    D1N: typing.ClassVar['PredefinedObservationType'] = ...
    D1P: typing.ClassVar['PredefinedObservationType'] = ...
    D1R: typing.ClassVar['PredefinedObservationType'] = ...
    D1S: typing.ClassVar['PredefinedObservationType'] = ...
    D1W: typing.ClassVar['PredefinedObservationType'] = ...
    D1X: typing.ClassVar['PredefinedObservationType'] = ...
    D1Y: typing.ClassVar['PredefinedObservationType'] = ...
    D1Z: typing.ClassVar['PredefinedObservationType'] = ...
    D2C: typing.ClassVar['PredefinedObservationType'] = ...
    D2D: typing.ClassVar['PredefinedObservationType'] = ...
    D2I: typing.ClassVar['PredefinedObservationType'] = ...
    D2L: typing.ClassVar['PredefinedObservationType'] = ...
    D2M: typing.ClassVar['PredefinedObservationType'] = ...
    D2N: typing.ClassVar['PredefinedObservationType'] = ...
    D2P: typing.ClassVar['PredefinedObservationType'] = ...
    D2Q: typing.ClassVar['PredefinedObservationType'] = ...
    D2R: typing.ClassVar['PredefinedObservationType'] = ...
    D2S: typing.ClassVar['PredefinedObservationType'] = ...
    D2W: typing.ClassVar['PredefinedObservationType'] = ...
    D2X: typing.ClassVar['PredefinedObservationType'] = ...
    D2Y: typing.ClassVar['PredefinedObservationType'] = ...
    D3I: typing.ClassVar['PredefinedObservationType'] = ...
    D3Q: typing.ClassVar['PredefinedObservationType'] = ...
    D3X: typing.ClassVar['PredefinedObservationType'] = ...
    D4A: typing.ClassVar['PredefinedObservationType'] = ...
    D4B: typing.ClassVar['PredefinedObservationType'] = ...
    D4X: typing.ClassVar['PredefinedObservationType'] = ...
    D5A: typing.ClassVar['PredefinedObservationType'] = ...
    D5B: typing.ClassVar['PredefinedObservationType'] = ...
    D5C: typing.ClassVar['PredefinedObservationType'] = ...
    D5D: typing.ClassVar['PredefinedObservationType'] = ...
    D5I: typing.ClassVar['PredefinedObservationType'] = ...
    D5P: typing.ClassVar['PredefinedObservationType'] = ...
    D5Q: typing.ClassVar['PredefinedObservationType'] = ...
    D5X: typing.ClassVar['PredefinedObservationType'] = ...
    D5Z: typing.ClassVar['PredefinedObservationType'] = ...
    D6A: typing.ClassVar['PredefinedObservationType'] = ...
    D6B: typing.ClassVar['PredefinedObservationType'] = ...
    D6C: typing.ClassVar['PredefinedObservationType'] = ...
    D6D: typing.ClassVar['PredefinedObservationType'] = ...
    D6E: typing.ClassVar['PredefinedObservationType'] = ...
    D6I: typing.ClassVar['PredefinedObservationType'] = ...
    D6L: typing.ClassVar['PredefinedObservationType'] = ...
    D6P: typing.ClassVar['PredefinedObservationType'] = ...
    D6Q: typing.ClassVar['PredefinedObservationType'] = ...
    D6S: typing.ClassVar['PredefinedObservationType'] = ...
    D6X: typing.ClassVar['PredefinedObservationType'] = ...
    D6Z: typing.ClassVar['PredefinedObservationType'] = ...
    D7D: typing.ClassVar['PredefinedObservationType'] = ...
    D7I: typing.ClassVar['PredefinedObservationType'] = ...
    D7P: typing.ClassVar['PredefinedObservationType'] = ...
    D7Q: typing.ClassVar['PredefinedObservationType'] = ...
    D7X: typing.ClassVar['PredefinedObservationType'] = ...
    D7Z: typing.ClassVar['PredefinedObservationType'] = ...
    D8D: typing.ClassVar['PredefinedObservationType'] = ...
    D8I: typing.ClassVar['PredefinedObservationType'] = ...
    D8P: typing.ClassVar['PredefinedObservationType'] = ...
    D8Q: typing.ClassVar['PredefinedObservationType'] = ...
    D8X: typing.ClassVar['PredefinedObservationType'] = ...
    D9A: typing.ClassVar['PredefinedObservationType'] = ...
    D9B: typing.ClassVar['PredefinedObservationType'] = ...
    D9C: typing.ClassVar['PredefinedObservationType'] = ...
    D9X: typing.ClassVar['PredefinedObservationType'] = ...
    D0: typing.ClassVar['PredefinedObservationType'] = ...
    DA: typing.ClassVar['PredefinedObservationType'] = ...
    DB: typing.ClassVar['PredefinedObservationType'] = ...
    DC: typing.ClassVar['PredefinedObservationType'] = ...
    DD: typing.ClassVar['PredefinedObservationType'] = ...
    L1A: typing.ClassVar['PredefinedObservationType'] = ...
    L1B: typing.ClassVar['PredefinedObservationType'] = ...
    L1C: typing.ClassVar['PredefinedObservationType'] = ...
    L1D: typing.ClassVar['PredefinedObservationType'] = ...
    L1E: typing.ClassVar['PredefinedObservationType'] = ...
    L1I: typing.ClassVar['PredefinedObservationType'] = ...
    L1L: typing.ClassVar['PredefinedObservationType'] = ...
    L1M: typing.ClassVar['PredefinedObservationType'] = ...
    L1N: typing.ClassVar['PredefinedObservationType'] = ...
    L1P: typing.ClassVar['PredefinedObservationType'] = ...
    L1R: typing.ClassVar['PredefinedObservationType'] = ...
    L1S: typing.ClassVar['PredefinedObservationType'] = ...
    L1W: typing.ClassVar['PredefinedObservationType'] = ...
    L1X: typing.ClassVar['PredefinedObservationType'] = ...
    L1Y: typing.ClassVar['PredefinedObservationType'] = ...
    L1Z: typing.ClassVar['PredefinedObservationType'] = ...
    L2C: typing.ClassVar['PredefinedObservationType'] = ...
    L2D: typing.ClassVar['PredefinedObservationType'] = ...
    L2I: typing.ClassVar['PredefinedObservationType'] = ...
    L2L: typing.ClassVar['PredefinedObservationType'] = ...
    L2M: typing.ClassVar['PredefinedObservationType'] = ...
    L2N: typing.ClassVar['PredefinedObservationType'] = ...
    L2P: typing.ClassVar['PredefinedObservationType'] = ...
    L2Q: typing.ClassVar['PredefinedObservationType'] = ...
    L2R: typing.ClassVar['PredefinedObservationType'] = ...
    L2S: typing.ClassVar['PredefinedObservationType'] = ...
    L2W: typing.ClassVar['PredefinedObservationType'] = ...
    L2X: typing.ClassVar['PredefinedObservationType'] = ...
    L2Y: typing.ClassVar['PredefinedObservationType'] = ...
    L3I: typing.ClassVar['PredefinedObservationType'] = ...
    L3Q: typing.ClassVar['PredefinedObservationType'] = ...
    L3X: typing.ClassVar['PredefinedObservationType'] = ...
    L4A: typing.ClassVar['PredefinedObservationType'] = ...
    L4B: typing.ClassVar['PredefinedObservationType'] = ...
    L4X: typing.ClassVar['PredefinedObservationType'] = ...
    L5A: typing.ClassVar['PredefinedObservationType'] = ...
    L5B: typing.ClassVar['PredefinedObservationType'] = ...
    L5C: typing.ClassVar['PredefinedObservationType'] = ...
    L5D: typing.ClassVar['PredefinedObservationType'] = ...
    L5I: typing.ClassVar['PredefinedObservationType'] = ...
    L5P: typing.ClassVar['PredefinedObservationType'] = ...
    L5Q: typing.ClassVar['PredefinedObservationType'] = ...
    L5X: typing.ClassVar['PredefinedObservationType'] = ...
    L5Z: typing.ClassVar['PredefinedObservationType'] = ...
    L6A: typing.ClassVar['PredefinedObservationType'] = ...
    L6B: typing.ClassVar['PredefinedObservationType'] = ...
    L6C: typing.ClassVar['PredefinedObservationType'] = ...
    L6D: typing.ClassVar['PredefinedObservationType'] = ...
    L6E: typing.ClassVar['PredefinedObservationType'] = ...
    L6I: typing.ClassVar['PredefinedObservationType'] = ...
    L6L: typing.ClassVar['PredefinedObservationType'] = ...
    L6P: typing.ClassVar['PredefinedObservationType'] = ...
    L6Q: typing.ClassVar['PredefinedObservationType'] = ...
    L6S: typing.ClassVar['PredefinedObservationType'] = ...
    L6X: typing.ClassVar['PredefinedObservationType'] = ...
    L6Z: typing.ClassVar['PredefinedObservationType'] = ...
    L7D: typing.ClassVar['PredefinedObservationType'] = ...
    L7I: typing.ClassVar['PredefinedObservationType'] = ...
    L7P: typing.ClassVar['PredefinedObservationType'] = ...
    L7Q: typing.ClassVar['PredefinedObservationType'] = ...
    L7X: typing.ClassVar['PredefinedObservationType'] = ...
    L7Z: typing.ClassVar['PredefinedObservationType'] = ...
    L8D: typing.ClassVar['PredefinedObservationType'] = ...
    L8I: typing.ClassVar['PredefinedObservationType'] = ...
    L8P: typing.ClassVar['PredefinedObservationType'] = ...
    L8Q: typing.ClassVar['PredefinedObservationType'] = ...
    L8X: typing.ClassVar['PredefinedObservationType'] = ...
    L9A: typing.ClassVar['PredefinedObservationType'] = ...
    L9B: typing.ClassVar['PredefinedObservationType'] = ...
    L9C: typing.ClassVar['PredefinedObservationType'] = ...
    L9X: typing.ClassVar['PredefinedObservationType'] = ...
    L0: typing.ClassVar['PredefinedObservationType'] = ...
    S1A: typing.ClassVar['PredefinedObservationType'] = ...
    S1B: typing.ClassVar['PredefinedObservationType'] = ...
    S1C: typing.ClassVar['PredefinedObservationType'] = ...
    S1D: typing.ClassVar['PredefinedObservationType'] = ...
    S1E: typing.ClassVar['PredefinedObservationType'] = ...
    S1I: typing.ClassVar['PredefinedObservationType'] = ...
    S1L: typing.ClassVar['PredefinedObservationType'] = ...
    S1M: typing.ClassVar['PredefinedObservationType'] = ...
    S1N: typing.ClassVar['PredefinedObservationType'] = ...
    S1P: typing.ClassVar['PredefinedObservationType'] = ...
    S1R: typing.ClassVar['PredefinedObservationType'] = ...
    S1S: typing.ClassVar['PredefinedObservationType'] = ...
    S1W: typing.ClassVar['PredefinedObservationType'] = ...
    S1X: typing.ClassVar['PredefinedObservationType'] = ...
    S1Y: typing.ClassVar['PredefinedObservationType'] = ...
    S1Z: typing.ClassVar['PredefinedObservationType'] = ...
    S2C: typing.ClassVar['PredefinedObservationType'] = ...
    S2D: typing.ClassVar['PredefinedObservationType'] = ...
    S2I: typing.ClassVar['PredefinedObservationType'] = ...
    S2L: typing.ClassVar['PredefinedObservationType'] = ...
    S2M: typing.ClassVar['PredefinedObservationType'] = ...
    S2N: typing.ClassVar['PredefinedObservationType'] = ...
    S2P: typing.ClassVar['PredefinedObservationType'] = ...
    S2Q: typing.ClassVar['PredefinedObservationType'] = ...
    S2R: typing.ClassVar['PredefinedObservationType'] = ...
    S2S: typing.ClassVar['PredefinedObservationType'] = ...
    S2W: typing.ClassVar['PredefinedObservationType'] = ...
    S2X: typing.ClassVar['PredefinedObservationType'] = ...
    S2Y: typing.ClassVar['PredefinedObservationType'] = ...
    S3I: typing.ClassVar['PredefinedObservationType'] = ...
    S3Q: typing.ClassVar['PredefinedObservationType'] = ...
    S3X: typing.ClassVar['PredefinedObservationType'] = ...
    S4A: typing.ClassVar['PredefinedObservationType'] = ...
    S4B: typing.ClassVar['PredefinedObservationType'] = ...
    S4X: typing.ClassVar['PredefinedObservationType'] = ...
    S5A: typing.ClassVar['PredefinedObservationType'] = ...
    S5B: typing.ClassVar['PredefinedObservationType'] = ...
    S5C: typing.ClassVar['PredefinedObservationType'] = ...
    S5D: typing.ClassVar['PredefinedObservationType'] = ...
    S5I: typing.ClassVar['PredefinedObservationType'] = ...
    S5P: typing.ClassVar['PredefinedObservationType'] = ...
    S5Q: typing.ClassVar['PredefinedObservationType'] = ...
    S5X: typing.ClassVar['PredefinedObservationType'] = ...
    S5Z: typing.ClassVar['PredefinedObservationType'] = ...
    S6A: typing.ClassVar['PredefinedObservationType'] = ...
    S6B: typing.ClassVar['PredefinedObservationType'] = ...
    S6C: typing.ClassVar['PredefinedObservationType'] = ...
    S6D: typing.ClassVar['PredefinedObservationType'] = ...
    S6E: typing.ClassVar['PredefinedObservationType'] = ...
    S6I: typing.ClassVar['PredefinedObservationType'] = ...
    S6L: typing.ClassVar['PredefinedObservationType'] = ...
    S6P: typing.ClassVar['PredefinedObservationType'] = ...
    S6Q: typing.ClassVar['PredefinedObservationType'] = ...
    S6S: typing.ClassVar['PredefinedObservationType'] = ...
    S6X: typing.ClassVar['PredefinedObservationType'] = ...
    S6Z: typing.ClassVar['PredefinedObservationType'] = ...
    S7D: typing.ClassVar['PredefinedObservationType'] = ...
    S7I: typing.ClassVar['PredefinedObservationType'] = ...
    S7P: typing.ClassVar['PredefinedObservationType'] = ...
    S7Q: typing.ClassVar['PredefinedObservationType'] = ...
    S7X: typing.ClassVar['PredefinedObservationType'] = ...
    S7Z: typing.ClassVar['PredefinedObservationType'] = ...
    S8D: typing.ClassVar['PredefinedObservationType'] = ...
    S8I: typing.ClassVar['PredefinedObservationType'] = ...
    S8P: typing.ClassVar['PredefinedObservationType'] = ...
    S8Q: typing.ClassVar['PredefinedObservationType'] = ...
    S8X: typing.ClassVar['PredefinedObservationType'] = ...
    S9A: typing.ClassVar['PredefinedObservationType'] = ...
    S9B: typing.ClassVar['PredefinedObservationType'] = ...
    S9C: typing.ClassVar['PredefinedObservationType'] = ...
    S9X: typing.ClassVar['PredefinedObservationType'] = ...
    S0: typing.ClassVar['PredefinedObservationType'] = ...
    SA: typing.ClassVar['PredefinedObservationType'] = ...
    SB: typing.ClassVar['PredefinedObservationType'] = ...
    SC: typing.ClassVar['PredefinedObservationType'] = ...
    SD: typing.ClassVar['PredefinedObservationType'] = ...
    def getMeasurementType(self) -> MeasurementType:
        """
        Get the measurement type.
        
        Specified by: getMeasurementType in interface ObservationType
        
        Returns:
            measurement type
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the observation type.
        
        Specified by: getName in interface ObservationType
        
        Returns:
            name of the observation type
        
        
        """
        ...
    def getSignal(self, system: SatelliteSystem) -> GnssSignal:
        """
        Get the signal for a specified satellite system.
        
        Specified by: getSignal in interface ObservationType
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            signal for the satellite system, or null if satellite system not compatible
        
        
        """
        ...
    def getSignalCode(self) -> SignalCode:
        """
        Get the signal code.
        
        Specified by: getSignalCode in interface ObservationType
        
        Returns:
            signal code
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'PredefinedObservationType':
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
    def values() -> typing.MutableSequence['PredefinedObservationType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (PredefinedObservationType c : PredefinedObservationType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PythonObservationType(ObservationType):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getMeasurementType(self) -> MeasurementType:
        """
        Get the measurement type.
        
        Specified by: getMeasurementType in interface ObservationType
        
        Returns:
            measurement type
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the observation type.
        
        Specified by: getName in interface ObservationType
        
        Returns:
            name of the observation type
        
        
        """
        ...
    def getSignal(self, system: SatelliteSystem) -> GnssSignal:
        """
        Get the signal for a specified satellite system.
        
        Specified by: getSignal in interface ObservationType
        
        Parameters:
            system (SatelliteSystem): satellite system
        
        Returns:
            signal for the satellite system, or null if satellite system not compatible
        
        
        """
        ...
    def getSignalCode(self) -> SignalCode:
        """
        Get the signal code.
        
        Specified by: getSignalCode in interface ObservationType
        
        Returns:
            signal code
        
        
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

class PythonRadioWave(RadioWave):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFrequency(self) -> float:
        """
        Description copied from interface: getFrequency Get the value of the frequency in Hz.
        
        Specified by: getFrequency in interface RadioWave
        
        Returns:
            value of the frequency in Hz
        
        Also see:
            getWavelength
        
        
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

class PredefinedGnssSignal(java.lang.Enum['PredefinedGnssSignal'], GnssSignal):
    """
    Enumerate for GNSS predefined signals.
    
    Since:
        9.2
    """
    G01: typing.ClassVar['PredefinedGnssSignal'] = ...
    G02: typing.ClassVar['PredefinedGnssSignal'] = ...
    G05: typing.ClassVar['PredefinedGnssSignal'] = ...
    R01: typing.ClassVar['PredefinedGnssSignal'] = ...
    R02: typing.ClassVar['PredefinedGnssSignal'] = ...
    R03: typing.ClassVar['PredefinedGnssSignal'] = ...
    R04: typing.ClassVar['PredefinedGnssSignal'] = ...
    R06: typing.ClassVar['PredefinedGnssSignal'] = ...
    E01: typing.ClassVar['PredefinedGnssSignal'] = ...
    E05: typing.ClassVar['PredefinedGnssSignal'] = ...
    E07: typing.ClassVar['PredefinedGnssSignal'] = ...
    E08: typing.ClassVar['PredefinedGnssSignal'] = ...
    E06: typing.ClassVar['PredefinedGnssSignal'] = ...
    C01: typing.ClassVar['PredefinedGnssSignal'] = ...
    C02: typing.ClassVar['PredefinedGnssSignal'] = ...
    C05: typing.ClassVar['PredefinedGnssSignal'] = ...
    C06: typing.ClassVar['PredefinedGnssSignal'] = ...
    C07: typing.ClassVar['PredefinedGnssSignal'] = ...
    C08: typing.ClassVar['PredefinedGnssSignal'] = ...
    B01: typing.ClassVar['PredefinedGnssSignal'] = ...
    B02: typing.ClassVar['PredefinedGnssSignal'] = ...
    B03: typing.ClassVar['PredefinedGnssSignal'] = ...
    B1C: typing.ClassVar['PredefinedGnssSignal'] = ...
    B1A: typing.ClassVar['PredefinedGnssSignal'] = ...
    B2A: typing.ClassVar['PredefinedGnssSignal'] = ...
    B2B: typing.ClassVar['PredefinedGnssSignal'] = ...
    B08: typing.ClassVar['PredefinedGnssSignal'] = ...
    B3A: typing.ClassVar['PredefinedGnssSignal'] = ...
    J01: typing.ClassVar['PredefinedGnssSignal'] = ...
    J02: typing.ClassVar['PredefinedGnssSignal'] = ...
    J05: typing.ClassVar['PredefinedGnssSignal'] = ...
    J06: typing.ClassVar['PredefinedGnssSignal'] = ...
    I01: typing.ClassVar['PredefinedGnssSignal'] = ...
    I05: typing.ClassVar['PredefinedGnssSignal'] = ...
    I09: typing.ClassVar['PredefinedGnssSignal'] = ...
    S01: typing.ClassVar['PredefinedGnssSignal'] = ...
    S05: typing.ClassVar['PredefinedGnssSignal'] = ...
    def getFrequency(self) -> float:
        """
        Get the value of the frequency in Hz.
        
        Specified by: getFrequency in interface RadioWave
        
        Returns:
            value of the frequency in Hz
        
        Also see:
            getWavelength
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the RINEX name for the frequency.
        
        Specified by: getName in interface GnssSignal
        
        Returns:
            RINEX name for the frequency
        
        
        """
        ...
    def getRatio(self) -> float:
        """
        Get the ratio f/f0, where F0 is the common frequency.
        
        Specified by: getRatio in interface GnssSignal
        
        Returns:
            ratio f/f0, where F0 is the common frequency
        
        Also see:
            F0, getFrequency
        
        
        """
        ...
    def getSatelliteSystem(self) -> SatelliteSystem:
        """
        Get the satellite system for which this frequency is defined.
        
        Specified by: getSatelliteSystem in interface GnssSignal
        
        Returns:
            satellite system for which this frequency is defined
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'PredefinedGnssSignal':
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
    def values() -> typing.MutableSequence['PredefinedGnssSignal']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (PredefinedGnssSignal c : PredefinedGnssSignal.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PythonGnssSignal(GnssSignal):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFrequency(self) -> float:
        """
        Get the value of the frequency in Hz.
        
        Specified by: getFrequency in interface RadioWave
        
        Returns:
            value of the frequency in Hz
        
        Also see:
            getWavelength
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the RINEX name for the frequency.
        
        Specified by: getName in interface GnssSignal
        
        Returns:
            RINEX name for the frequency
        
        
        """
        ...
    def getRatio(self) -> float:
        """
        Get the ratio f/f0, where F0 is the common frequency.
        
        Specified by: getRatio in interface GnssSignal
        
        Returns:
            ratio f/f0, where F0 is the common frequency
        
        Also see:
            F0, getFrequency
        
        
        """
        ...
    def getSatelliteSystem(self) -> SatelliteSystem:
        """
        Get the satellite system for which this frequency is defined.
        
        Specified by: getSatelliteSystem in interface GnssSignal
        
        Returns:
            satellite system for which this frequency is defined
        
        
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss")``.

    DOP: typing.Type[DOP]
    DOPComputer: typing.Type[DOPComputer]
    GnssSignal: typing.Type[GnssSignal]
    IGSUtils: typing.Type[IGSUtils]
    MeasurementType: typing.Type[MeasurementType]
    ObservationTimeScale: typing.Type[ObservationTimeScale]
    ObservationType: typing.Type[ObservationType]
    PredefinedGnssSignal: typing.Type[PredefinedGnssSignal]
    PredefinedObservationType: typing.Type[PredefinedObservationType]
    PythonGnssSignal: typing.Type[PythonGnssSignal]
    PythonObservationType: typing.Type[PythonObservationType]
    PythonRadioWave: typing.Type[PythonRadioWave]
    RadioWave: typing.Type[RadioWave]
    SEMParser: typing.Type[SEMParser]
    SatInSystem: typing.Type[SatInSystem]
    SatelliteSystem: typing.Type[SatelliteSystem]
    SignalCode: typing.Type[SignalCode]
    TimeSystem: typing.Type[TimeSystem]
    YUMAParser: typing.Type[YUMAParser]
    antenna: org.orekit.gnss.antenna.__module_protocol__
    attitude: org.orekit.gnss.attitude.__module_protocol__
    metric: org.orekit.gnss.metric.__module_protocol__
    rflink: org.orekit.gnss.rflink.__module_protocol__
