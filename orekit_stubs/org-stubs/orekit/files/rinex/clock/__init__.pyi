
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import java.util.function
import org.orekit.data
import org.orekit.files.rinex
import org.orekit.frames
import org.orekit.gnss
import org.orekit.time
import org.orekit.utils
import typing



class RinexClock:
    """
    Represents a parsed clock file from the IGS.
    
    A time system should be specified in the file. However, if it is not, default time system will be chosen regarding the satellite system. If it is mixed or not specified, default time system will be UTC.
    
    Some fields might be null after parsing. It is expected because of the numerous kind of data that can be stored in clock data file.
    
    Caution, files with missing information in header can lead to wrong data dates and station positions. It is advised to check the correctness and format compliance of the clock file to be parsed. Some values such as file time scale still can be set by user.
    
    Since:
        11.0
    
    Also see:
        txt,
        txt,
        txt
    """
    def __init__(self, frameBuilder: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]]):
        """
        Constructor.
        
        Parameters:
            frameBuilder (Function<? super String, ? extends Frame> frameBuilder): for constructing a reference frame from the identifier
        
        
        """
        ...
    def addAppliedDCBS(self, appliedDCBS: org.orekit.files.rinex.AppliedDCBS) -> None:
        """
        Add an applied differencial code bias corrections.
        
        Parameters:
            appliedDCBS (AppliedDCBS): the applied differencial code bias corrections to add
        
        
        """
        ...
    def addAppliedPCVS(self, appliedPCVS: org.orekit.files.rinex.AppliedPCVS) -> None:
        """
        Add an applied phase center variations.
        
        Parameters:
            appliedPCVS (AppliedPCVS): the phase center variations to add
        
        
        """
        ...
    def addClockData(self, id: str, clockDataLine: 'RinexClock.ClockDataLine') -> None:
        """
        Add a clock data line to a specified receiver/satellite.
        
        Parameters:
            id (String): the satellite system to add observation type
            clockDataLine (ClockDataLine): the clock data line to add
        
        
        """
        ...
    def addClockDataType(self, clockDataType: 'RinexClock.ClockDataType') -> None:
        """
        Add a clock data types.
        
        Parameters:
            clockDataType (ClockDataType): the clock data types to add
        
        
        """
        ...
    def addComment(self, comment: str) -> None:
        """
        Add a comment line.
        
        Parameters:
            comment (String): the comment line to add
        
        
        """
        ...
    def addReceiver(self, receiver: 'RinexClock.Receiver') -> None:
        """
        Add a new receiver to the list of stored receivers.
        
        Parameters:
            receiver (Receiver): the receiver
        
        
        """
        ...
    def addReferenceClockList(self, referenceClockList: java.util.List['RinexClock.ReferenceClock'], startDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Add a list of reference clocks which will be used after a specified date. If the reference map has not been already created, it will be.
        
        Parameters:
            referenceClockList (List<ReferenceClock> referenceClockList): the reference clock list
            startDate (AbsoluteDate): the date the list will be valid after.
        
        
        """
        ...
    def addSatellite(self, satId: str) -> None:
        """
        Add a new satellite with a given identifier to the list of stored satellites.
        
        Parameters:
            satId (String): the satellite identifier
        
        
        """
        ...
    def addSystemObservationType(self, satSystem: org.orekit.gnss.SatelliteSystem, observationType: org.orekit.gnss.ObservationType) -> None:
        """
        Add an observation type for a specified satellite system.
        
        Parameters:
            satSystem (SatelliteSystem): the satellite system to add observation type
            observationType (ObservationType): the system observation type to set
        
        
        """
        ...
    def extractClockModel(self, name: str, nbInterpolationPoints: int) -> org.orekit.time.SampledClockModel:
        """
        Extract the clock model.
        
        Parameters:
            name (String): receiver/satellite name
            nbInterpolationPoints (int): number of points to use in interpolation
        
        Returns:
            extracted clock model
        
        Since:
            12.1
        
        
        """
        ...
    def getAgencyName(self) -> str:
        """
        Getter for the agency name.
        
        Returns:
            the agencyName
        
        
        """
        ...
    def getAnalysisCenterID(self) -> str:
        """
        Getter for the analysis center ID.
        
        Returns:
            the analysis center ID
        
        
        """
        ...
    def getAnalysisCenterName(self) -> str:
        """
        Getter for the analysis center name.
        
        Returns:
            the analysis center name
        
        
        """
        ...
    def getClockData(self) -> java.util.Map[str, java.util.List['RinexClock.ClockDataLine']]:
        """
        Getter for an unmodifiable map of clock data.
        
        Returns:
            the clock data
        
        
        """
        ...
    def getClockDataTypes(self) -> java.util.List['RinexClock.ClockDataType']:
        """
        Getter for the different clock data types.
        
        Returns:
            the list of the different clock data types
        
        
        """
        ...
    def getComments(self) -> str:
        """
        Getter for the comments.
        
        Returns:
            the comments
        
        
        """
        ...
    def getCreationDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for the creation date.
        
        Returns:
            the creation date
        
        
        """
        ...
    def getCreationDateString(self) -> str:
        """
        Getter for the creation date of the file as a string.
        
        Returns:
            the creation date as a string
        
        
        """
        ...
    def getCreationTimeString(self) -> str:
        """
        Getter for the creation time of the file as a string.
        
        Returns:
            the creation time as a string
        
        
        """
        ...
    def getCreationTimeZoneString(self) -> str:
        """
        Getter for the creation time zone of the file as a string.
        
        Returns:
            the creation time zone as a string
        
        
        """
        ...
    def getEarliestEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get earliest epoch from the getClockData.
        
        Returns:
            earliest epoch from the getClockData, or
            FUTURE_INFINITY if no data has been added
        
        Since:
            12.1
        
        
        """
        ...
    def getExternalClockReference(self) -> str:
        """
        Getter for the external clock reference.
        
        Returns:
            the external clock reference
        
        
        """
        ...
    def getFormatVersion(self) -> float:
        """
        Getter for the format version.
        
        Returns:
            the format version
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame for the station positions.
        
        Returns:
            the reference frame for station positions
        
        
        """
        ...
    def getFrameName(self) -> str:
        """
        Getter for the frame name.
        
        Returns:
            the frame name
        
        
        """
        ...
    def getLatestEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get latest epoch from the getClockData.
        
        Returns:
            latest epoch from the getClockData, or
            PAST_INFINITY if no data has been added
        
        Since:
            12.1
        
        
        """
        ...
    def getListAppliedDCBS(self) -> java.util.List[org.orekit.files.rinex.AppliedDCBS]:
        """
        Getter for the applied differential code bias corrections.
        
        Returns:
            the list of applied differential code bias corrections
        
        
        """
        ...
    def getListAppliedPCVS(self) -> java.util.List[org.orekit.files.rinex.AppliedPCVS]:
        """
        Getter for the applied phase center variations.
        
        Returns:
            the list of the applied phase center variations
        
        
        """
        ...
    def getNumberOfClockDataTypes(self) -> int:
        """
        Get the number of different clock data types in the file.
        
        Returns:
            the number of different clock data types
        
        
        """
        ...
    def getNumberOfLeapSeconds(self) -> int:
        """
        Getter for the number of leap seconds.
        
        Returns:
            the number of leap seconds
        
        
        """
        ...
    def getNumberOfLeapSecondsGNSS(self) -> int:
        """
        Getter for the number of leap second for GNSS time scales.
        
        Returns:
            the number of leap seconds for GNSS time scales
        
        
        """
        ...
    def getNumberOfReceivers(self) -> int:
        """
        Get the number of receivers that are considered in the file.
        
        Returns:
            the number of receivers that are considered in the file
        
        
        """
        ...
    def getNumberOfSatellites(self) -> int:
        """
        Get the number of satellites that are considered in the file.
        
        Returns:
            the number of satellites that are considered in the file
        
        
        """
        ...
    def getProgramName(self) -> str:
        """
        Getter for the program name.
        
        Returns:
            the program name
        
        
        """
        ...
    def getReceivers(self) -> java.util.List['RinexClock.Receiver']:
        """
        Getter for the receivers.
        
        Returns:
            the list of the receivers
        
        
        """
        ...
    def getReferenceClocks(self) -> org.orekit.utils.TimeSpanMap[java.util.List['RinexClock.ReferenceClock']]:
        """
        Getter for the reference clocks.
        
        Returns:
            the time span map of the different refence clocks
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
        Getter for the satellite system.
        
        Returns:
            the satellite system
        
        
        """
        ...
    def getSatellites(self) -> java.util.List[str]:
        """
        Getter for the satellites.
        
        Returns:
            the list of the satellites
        
        
        """
        ...
    def getStationIdentifier(self) -> str:
        """
        Getter for the station identifier.
        
        Returns:
            the station identifier
        
        
        """
        ...
    def getStationName(self) -> str:
        """
        Getter for the station name.
        
        Returns:
            the station name
        
        
        """
        ...
    def getSystemObservationTypes(self) -> java.util.Map[org.orekit.gnss.SatelliteSystem, java.util.List[org.orekit.gnss.ObservationType]]:
        """
        Getter for the different observation type for each satellite system.
        
        Returns:
            the map of the different observation type per satellite system
        
        
        """
        ...
    def getTimeScale(self) -> org.orekit.time.TimeScale:
        """
        Getter for the data time scale.
        
        Returns:
            the data time scale
        
        
        """
        ...
    def getTimeSystem(self) -> org.orekit.gnss.TimeSystem:
        """
        Getter for the file time system.
        
        Returns:
            the file time system
        
        
        """
        ...
    def getTotalNumberOfDataLines(self) -> int:
        """
        Get the total number of complete data lines in the file.
        
        Returns:
            the total number of complete data lines in the file
        
        
        """
        ...
    def numberOfObsTypes(self, system: org.orekit.gnss.SatelliteSystem) -> int:
        """
        Get the number of observation types for a given system.
        
        Parameters:
            system (SatelliteSystem): the satellite system to consider
        
        Returns:
            the number of observation types for a given system
        
        
        """
        ...
    def setAgencyName(self, agencyName: str) -> None:
        """
        Setter for the agency name.
        
        Parameters:
            agencyName (String): the agency name to set
        
        
        """
        ...
    def setAnalysisCenterID(self, analysisCenterID: str) -> None:
        """
        Setter for the analysis center ID.
        
        Parameters:
            analysisCenterID (String): the analysis center ID to set
        
        
        """
        ...
    def setAnalysisCenterName(self, analysisCenterName: str) -> None:
        """
        Setter for the analysis center name.
        
        Parameters:
            analysisCenterName (String): the analysis center name to set
        
        
        """
        ...
    def setCreationDate(self, creationDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Setter for the creation date.
        
        Parameters:
            creationDate (AbsoluteDate): the creation date to set
        
        
        """
        ...
    def setCreationDateString(self, creationDateString: str) -> None:
        """
        Setter for the creation date as a string.
        
        Parameters:
            creationDateString (String): the creation date as a string to set
        
        
        """
        ...
    def setCreationTimeString(self, creationTimeString: str) -> None:
        """
        Setter for the creation time as a string.
        
        Parameters:
            creationTimeString (String): the creation time as a string to set
        
        
        """
        ...
    def setCreationTimeZoneString(self, creationTimeZoneString: str) -> None:
        """
        Setter for the creation time zone.
        
        Parameters:
            creationTimeZoneString (String): the creation time zone as a string to set
        
        
        """
        ...
    def setExternalClockReference(self, externalClockReference: str) -> None:
        """
        Setter for the external clock reference.
        
        Parameters:
            externalClockReference (String): the external clock reference to set
        
        
        """
        ...
    def setFormatVersion(self, formatVersion: float) -> None:
        """
        Setter for the format version.
        
        Parameters:
            formatVersion (double): the format version to set
        
        
        """
        ...
    def setFrameName(self, frameName: str) -> None:
        """
        Setter for the frame name.
        
        Parameters:
            frameName (String): the frame name to set
        
        
        """
        ...
    def setNumberOfLeapSeconds(self, numberOfLeapSeconds: int) -> None:
        """
        Setter for the number of leap seconds.
        
        Parameters:
            numberOfLeapSeconds (int): the number of leap seconds to set
        
        
        """
        ...
    def setNumberOfLeapSecondsGNSS(self, numberOfLeapSecondsGNSS: int) -> None:
        """
        Setter for the number of leap seconds for GNSS time scales.
        
        Parameters:
            numberOfLeapSecondsGNSS (int): the number of leap seconds for GNSS time scales to set
        
        
        """
        ...
    def setProgramName(self, programName: str) -> None:
        """
        Setter for the program name.
        
        Parameters:
            programName (String): the program name to set
        
        
        """
        ...
    def setSatelliteSystem(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> None:
        """
        Setter for the satellite system.
        
        Parameters:
            satelliteSystem (SatelliteSystem): the satellite system to set
        
        
        """
        ...
    def setStationIdentifier(self, stationIdentifier: str) -> None:
        """
        Setter for the station identifier.
        
        Parameters:
            stationIdentifier (String): the station identifier to set
        
        
        """
        ...
    def setStationName(self, stationName: str) -> None:
        """
        Setter for the station name.
        
        Parameters:
            stationName (String): the station name to set
        
        
        """
        ...
    def setTimeScale(self, timeScale: org.orekit.time.TimeScale) -> None:
        """
        Setter for the data time scale.
        
        Parameters:
            timeScale (TimeScale): the data time scale to set
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.gnss.TimeSystem) -> None:
        """
        Setter for the file time system.
        
        Parameters:
            timeSystem (TimeSystem): the file time system to set
        
        
        """
        ...
    @staticmethod
    def splice(clocks: typing.Union[java.util.Collection['RinexClock'], typing.Sequence['RinexClock'], typing.Set['RinexClock']], maxGap: float) -> 'RinexClock':
        """
        Splice several Rinex clock files together.
        
        Splicing Rinex clock files is intended to be used when continuous computation covering more than one file is needed. The metadata (version number, agency, …) will be retrieved from the earliest file only. Receivers and satellites will be merged from all files. Some receivers or satellites may be missing in some files… Once sorted (which is done internally), if the gap between segments from two files is larger than maxGap, then an error will be triggered.
        
        The spliced file only contains the receivers and satellites that were present in all files. Receivers and satellites present in some files and absent from other files are silently dropped.
        
        Depending on producer, successive clock files either have a gap between the last entry of one file and the first entry of the next file (for example, files with a 5 minutes epoch interval may end at 23:55 and the next file start at 00:00), or both files have one point exactly at the splicing date (i.e. 24:00 one day and 00:00 next day). In the later case, the last point of the early file is dropped, and the first point of the late file takes precedence, hence only one point remains in the spliced file; this design choice is made to enforce continuity and regular interpolation.
        
        Parameters:
            clocks (Collection<RinexClock> clocks): clock files to merge
            maxGap (double): maximum time gap between files
        
        Returns:
            merged clock file
        
        Since:
            12.1
        
        
        """
        ...
    class ClockDataLine:
        def __init__(self, rinexClock: 'RinexClock', clockDataType: 'RinexClock.ClockDataType', string: str, dateComponents: org.orekit.time.DateComponents, timeComponents: org.orekit.time.TimeComponents, int: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
        def getClockAcceleration(self) -> float: ...
        def getClockAccelerationSigma(self) -> float: ...
        def getClockBias(self) -> float: ...
        def getClockBiasSigma(self) -> float: ...
        def getClockRate(self) -> float: ...
        def getClockRateSigma(self) -> float: ...
        def getDataType(self) -> 'RinexClock.ClockDataType': ...
        @typing.overload
        def getEpoch(self) -> org.orekit.time.AbsoluteDate: ...
        @typing.overload
        def getEpoch(self, timeScale: org.orekit.time.TimeScale) -> org.orekit.time.AbsoluteDate: ...
        def getName(self) -> str: ...
        def getNumberOfValues(self) -> int: ...
    class ClockDataType(java.lang.Enum['RinexClock.ClockDataType']):
        AR: typing.ClassVar['RinexClock.ClockDataType'] = ...
        AS: typing.ClassVar['RinexClock.ClockDataType'] = ...
        CR: typing.ClassVar['RinexClock.ClockDataType'] = ...
        DR: typing.ClassVar['RinexClock.ClockDataType'] = ...
        MS: typing.ClassVar['RinexClock.ClockDataType'] = ...
        def getKey(self) -> str: ...
        @staticmethod
        def parseClockDataType(string: str) -> 'RinexClock.ClockDataType': ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'RinexClock.ClockDataType': ...
        @staticmethod
        def values() -> typing.MutableSequence['RinexClock.ClockDataType']: ...
    class Receiver:
        def __init__(self, string: str, string2: str, double: float, double2: float, double3: float): ...
        def getDesignator(self) -> str: ...
        def getReceiverIdentifier(self) -> str: ...
        def getX(self) -> float: ...
        def getY(self) -> float: ...
        def getZ(self) -> float: ...
    class ReferenceClock:
        def __init__(self, string: str, string2: str, double: float, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
        def getClockConstraint(self) -> float: ...
        def getClockID(self) -> str: ...
        def getEndDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getReferenceName(self) -> str: ...
        def getStartDate(self) -> org.orekit.time.AbsoluteDate: ...

class RinexClockParser:
    """
    A parser for the clock file from the IGS. This parser handles versions 2.0 to 3.04 of the RINEX clock files.
    
    It is able to manage some mistakes in file writing and format compliance such as wrong date format, misplaced header blocks or missing information.
    
    A time system should be specified in the file. However, if it is not, default time system will be chosen regarding the satellite system. If it is mixed or not specified, default time system will be UTC.
    
    Caution, files with missing information in header can lead to wrong data dates and station positions. It is advised to check the correctness and format compliance of the clock file to be parsed.
    
    Since:
        11.0
    
    Also see:
        txt,
        txt,
        txt
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]]): ...
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]], function2: typing.Union[java.util.function.Function[str, org.orekit.gnss.ObservationType], typing.Callable[[str], org.orekit.gnss.ObservationType]], timeScales: org.orekit.time.TimeScales): ...
    @typing.overload
    def parse(self, reader: java.io.BufferedReader, fileName: str) -> RinexClock:
        """
        Parse an IGS clock file from a stream.
        
        Parameters:
            reader (BufferedReader): containing the clock file
            fileName (String): file name
        
        Returns:
            a parsed IGS clock file
        
        Also see:
            parse,
            parse,
            parse
        
        """
        ...
    @typing.overload
    def parse(self, inputStream: java.io.InputStream) -> RinexClock:
        """
        Parse an IGS clock file from an input stream using the UTF-8 charset.
        
        This method creates a BufferedReader from the stream and as such this method may read more data than necessary from stream and the additional data will be lost. The other parse methods do not have this issue.
        
        Parameters:
            stream (InputStream): to read the IGS clock file from
        
        Returns:
            a parsed IGS clock file
        
        Also see:
            parse,
            parse,
            parse
        
        Parse an IGS clock file from a file on the local file system.
        
        Parameters:
            fileName (String): file name
        
        Returns:
            a parsed IGS clock file
        
        Also see:
            parse,
            parse,
            parse
        
        Parse an IGS clock file from a DataSource.
        
        Parameters:
            source (DataSource): source for clock file
        
        Returns:
            a parsed IGS clock file
        
        Since:
            12.1
        
        Also see:
            parse,
            parse,
            parse
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> RinexClock: ...
    @typing.overload
    def parse(self, dataSource: org.orekit.data.DataSource) -> RinexClock: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.clock")``.

    RinexClock: typing.Type[RinexClock]
    RinexClockParser: typing.Type[RinexClockParser]
