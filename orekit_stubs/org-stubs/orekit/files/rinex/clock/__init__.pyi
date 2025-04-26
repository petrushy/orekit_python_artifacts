
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
    public class RinexClock extends :class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Represents a parsed clock file from the IGS.
    
        A time system should be specified in the file. However, if it is not, default time system will be chosen regarding the
        satellite system. If it is mixed or not specified, default time system will be UTC.
    
        Some fields might be null after parsing. It is expected because of the numerous kind of data that can be stored in clock
        data file.
    
        Caution, files with missing information in header can lead to wrong data dates and station positions. It is advised to
        check the correctness and format compliance of the clock file to be parsed. Some values such as file time scale still
        can be set by user.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.rinex.clock.https:.files.igs.org.pub.data.format.rinex_clock300.txt`,
            :class:`~org.orekit.files.rinex.clock.https:.files.igs.org.pub.data.format.rinex_clock302.txt`,
            :class:`~org.orekit.files.rinex.clock.https:.files.igs.org.pub.data.format.rinex_clock304.txt`
    """
    def __init__(self, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]]): ...
    def addAppliedDCBS(self, appliedDCBS: org.orekit.files.rinex.AppliedDCBS) -> None:
        """
            Add an applied differencial code bias corrections.
        
            Parameters:
                appliedDCBS (:class:`~org.orekit.files.rinex.AppliedDCBS`): the applied differencial code bias corrections to add
        
        
        """
        ...
    def addAppliedPCVS(self, appliedPCVS: org.orekit.files.rinex.AppliedPCVS) -> None:
        """
            Add an applied phase center variations.
        
            Parameters:
                appliedPCVS (:class:`~org.orekit.files.rinex.AppliedPCVS`): the phase center variations to add
        
        
        """
        ...
    def addClockData(self, string: str, clockDataLine: 'RinexClock.ClockDataLine') -> None:
        """
            Add a clock data line to a specified receiver/satellite.
        
            Parameters:
                id (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the satellite system to add observation type
                clockDataLine (:class:`~org.orekit.files.rinex.clock.RinexClock.ClockDataLine`): the clock data line to add
        
        
        """
        ...
    def addClockDataType(self, clockDataType: 'RinexClock.ClockDataType') -> None:
        """
            Add a clock data types.
        
            Parameters:
                clockDataType (:class:`~org.orekit.files.rinex.clock.RinexClock.ClockDataType`): the clock data types to add
        
        
        """
        ...
    def addComment(self, string: str) -> None:
        """
            Add a comment line.
        
            Parameters:
                comment (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the comment line to add
        
        
        """
        ...
    def addReceiver(self, receiver: 'RinexClock.Receiver') -> None:
        """
            Add a new receiver to the list of stored receivers.
        
            Parameters:
                receiver (:class:`~org.orekit.files.rinex.clock.RinexClock.Receiver`): the receiver
        
        
        """
        ...
    def addReferenceClockList(self, list: java.util.List['RinexClock.ReferenceClock'], absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def addSatellite(self, string: str) -> None:
        """
            Add a new satellite with a given identifier to the list of stored satellites.
        
            Parameters:
                satId (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the satellite identifier
        
        
        """
        ...
    def addSystemObservationType(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, observationType: org.orekit.gnss.ObservationType) -> None:
        """
            Add an observation type for a specified satellite system.
        
            Parameters:
                satSystem (:class:`~org.orekit.gnss.SatelliteSystem`): the satellite system to add observation type
                observationType (:class:`~org.orekit.gnss.ObservationType`): the system observation type to set
        
        
        """
        ...
    def extractClockModel(self, string: str, int: int) -> org.orekit.time.SampledClockModel:
        """
            Extract the clock model.
        
            Parameters:
                name (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): receiver/satellite name
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
    def getClockData(self) -> java.util.Map[str, java.util.List['RinexClock.ClockDataLine']]: ...
    def getClockDataTypes(self) -> java.util.List['RinexClock.ClockDataType']: ...
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
            Get earliest epoch from the :meth:`~org.orekit.files.rinex.clock.RinexClock.getClockData`.
        
            Returns:
                earliest epoch from the :meth:`~org.orekit.files.rinex.clock.RinexClock.getClockData`, or
                :meth:`~org.orekit.time.AbsoluteDate.FUTURE_INFINITY` if no data has been added
        
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
            Get latest epoch from the :meth:`~org.orekit.files.rinex.clock.RinexClock.getClockData`.
        
            Returns:
                latest epoch from the :meth:`~org.orekit.files.rinex.clock.RinexClock.getClockData`, or
                :meth:`~org.orekit.time.AbsoluteDate.PAST_INFINITY` if no data has been added
        
            Since:
                12.1
        
        
        """
        ...
    def getListAppliedDCBS(self) -> java.util.List[org.orekit.files.rinex.AppliedDCBS]: ...
    def getListAppliedPCVS(self) -> java.util.List[org.orekit.files.rinex.AppliedPCVS]: ...
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
    def getReceivers(self) -> java.util.List['RinexClock.Receiver']: ...
    def getReferenceClocks(self) -> org.orekit.utils.TimeSpanMap[java.util.List['RinexClock.ReferenceClock']]: ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Getter for the satellite system.
        
            Returns:
                the satellite system
        
        
        """
        ...
    def getSatellites(self) -> java.util.List[str]: ...
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
    def getSystemObservationTypes(self) -> java.util.Map[org.orekit.gnss.SatelliteSystem, java.util.List[org.orekit.gnss.ObservationType]]: ...
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
    def numberOfObsTypes(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> int:
        """
            Get the number of observation types for a given system.
        
            Parameters:
                system (:class:`~org.orekit.gnss.SatelliteSystem`): the satellite system to consider
        
            Returns:
                the number of observation types for a given system
        
        
        """
        ...
    def setAgencyName(self, string: str) -> None:
        """
            Setter for the agency name.
        
            Parameters:
                agencyName (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the agency name to set
        
        
        """
        ...
    def setAnalysisCenterID(self, string: str) -> None:
        """
            Setter for the analysis center ID.
        
            Parameters:
                analysisCenterID (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the analysis center ID to set
        
        
        """
        ...
    def setAnalysisCenterName(self, string: str) -> None:
        """
            Setter for the analysis center name.
        
            Parameters:
                analysisCenterName (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the analysis center name to set
        
        
        """
        ...
    def setCreationDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Setter for the creation date.
        
            Parameters:
                creationDate (:class:`~org.orekit.time.AbsoluteDate`): the creation date to set
        
        
        """
        ...
    def setCreationDateString(self, string: str) -> None:
        """
            Setter for the creation date as a string.
        
            Parameters:
                creationDateString (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the creation date as a string to set
        
        
        """
        ...
    def setCreationTimeString(self, string: str) -> None:
        """
            Setter for the creation time as a string.
        
            Parameters:
                creationTimeString (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the creation time as a string to set
        
        
        """
        ...
    def setCreationTimeZoneString(self, string: str) -> None:
        """
            Setter for the creation time zone.
        
            Parameters:
                creationTimeZoneString (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the creation time zone as a string to set
        
        
        """
        ...
    def setExternalClockReference(self, string: str) -> None:
        """
            Setter for the external clock reference.
        
            Parameters:
                externalClockReference (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the external clock reference to set
        
        
        """
        ...
    def setFormatVersion(self, double: float) -> None:
        """
            Setter for the format version.
        
            Parameters:
                formatVersion (double): the format version to set
        
        
        """
        ...
    def setFrameName(self, string: str) -> None:
        """
            Setter for the frame name.
        
            Parameters:
                frameName (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the frame name to set
        
        
        """
        ...
    def setNumberOfLeapSeconds(self, int: int) -> None:
        """
            Setter for the number of leap seconds.
        
            Parameters:
                numberOfLeapSeconds (int): the number of leap seconds to set
        
        
        """
        ...
    def setNumberOfLeapSecondsGNSS(self, int: int) -> None:
        """
            Setter for the number of leap seconds for GNSS time scales.
        
            Parameters:
                numberOfLeapSecondsGNSS (int): the number of leap seconds for GNSS time scales to set
        
        
        """
        ...
    def setProgramName(self, string: str) -> None:
        """
            Setter for the program name.
        
            Parameters:
                programName (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the program name to set
        
        
        """
        ...
    def setSatelliteSystem(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> None:
        """
            Setter for the satellite system.
        
            Parameters:
                satelliteSystem (:class:`~org.orekit.gnss.SatelliteSystem`): the satellite system to set
        
        
        """
        ...
    def setStationIdentifier(self, string: str) -> None:
        """
            Setter for the station identifier.
        
            Parameters:
                stationIdentifier (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the station identifier to set
        
        
        """
        ...
    def setStationName(self, string: str) -> None:
        """
            Setter for the station name.
        
            Parameters:
                stationName (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the station name to set
        
        
        """
        ...
    def setTimeScale(self, timeScale: org.orekit.time.TimeScale) -> None:
        """
            Setter for the data time scale.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): the data time scale to set
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.gnss.TimeSystem) -> None:
        """
            Setter for the file time system.
        
            Parameters:
                timeSystem (:class:`~org.orekit.gnss.TimeSystem`): the file time system to set
        
        
        """
        ...
    @staticmethod
    def splice(collection: typing.Union[java.util.Collection['RinexClock'], typing.Sequence['RinexClock'], typing.Set['RinexClock']], double: float) -> 'RinexClock': ...
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
    public class RinexClockParser extends :class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        A parser for the clock file from the IGS. This parser handles versions 2.0 to 3.04 of the RINEX clock files.
    
        It is able to manage some mistakes in file writing and format compliance such as wrong date format, misplaced header
        blocks or missing information.
    
        A time system should be specified in the file. However, if it is not, default time system will be chosen regarding the
        satellite system. If it is mixed or not specified, default time system will be UTC.
    
        Caution, files with missing information in header can lead to wrong data dates and station positions. It is advised to
        check the correctness and format compliance of the clock file to be parsed.
    
        Since:
            11.0
    
        Also see:
            :class:`~org.orekit.files.rinex.clock.https:.files.igs.org.pub.data.format.rinex_clock300.txt`,
            :class:`~org.orekit.files.rinex.clock.https:.files.igs.org.pub.data.format.rinex_clock302.txt`,
            :class:`~org.orekit.files.rinex.clock.https:.files.igs.org.pub.data.format.rinex_clock304.txt`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]]): ...
    @typing.overload
    def __init__(self, function: typing.Union[java.util.function.Function[str, org.orekit.frames.Frame], typing.Callable[[str], org.orekit.frames.Frame]], function2: typing.Union[java.util.function.Function[str, org.orekit.gnss.ObservationType], typing.Callable[[str], org.orekit.gnss.ObservationType]], timeScales: org.orekit.time.TimeScales): ...
    @typing.overload
    def parse(self, bufferedReader: java.io.BufferedReader, string: str) -> RinexClock:
        """
            Parse an IGS clock file from a stream.
        
            Parameters:
                reader (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.io.BufferedReader?is`): containing the clock file
                fileName (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): file name
        
            Returns:
                a parsed IGS clock file
        
            Also see:
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`
        
        """
        ...
    @typing.overload
    def parse(self, inputStream: java.io.InputStream) -> RinexClock:
        """
            Parse an IGS clock file from an input stream using the UTF-8 charset.
        
            This method creates a
            :class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.io.BufferedReader?is` from the
            stream and as such this method may read more data than necessary from :code:`stream` and the additional data will be
            lost. The other parse methods do not have this issue.
        
            Parameters:
                stream (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.io.InputStream?is`): to read the IGS clock file from
        
            Returns:
                a parsed IGS clock file
        
            Also see:
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`
        
            Parse an IGS clock file from a file on the local file system.
        
            Parameters:
                fileName (:class:`~org.orekit.files.rinex.clock.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): file name
        
            Returns:
                a parsed IGS clock file
        
            Also see:
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`
        
            Parse an IGS clock file from a :class:`~org.orekit.data.DataSource`.
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source for clock file
        
            Returns:
                a parsed IGS clock file
        
            Since:
                12.1
        
            Also see:
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`,
                :meth:`~org.orekit.files.rinex.clock.RinexClockParser.parse`
        
        
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
