import java.util
import org.orekit.data
import org.orekit.gnss
import org.orekit.propagation.analytical.gnss.data
import org.orekit.time
import typing



class RinexNavigation:
    """
    public class RinexNavigation extends Object
    
        Represents a parsed RINEX navigation messages files.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def addBeidouNavigationMessage(self, beidouNavigationMessage: org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage) -> None:
        """
            Add a Beidou navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage`): message to add
        
        
        """
        ...
    def addComment(self, string: str) -> None:
        """
            Add a comment line.
        
            Parameters:
                comment (String): the comment line to add
        
        
        """
        ...
    def addGPSNavigationMessage(self, gPSNavigationMessage: org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage) -> None:
        """
            Add a GPS navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage`): message to add
        
        
        """
        ...
    def addGalileoNavigationMessage(self, galileoNavigationMessage: org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage) -> None:
        """
            Add a Galileo navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage`): message to add
        
        
        """
        ...
    def addGlonassNavigationMessage(self, gLONASSNavigationMessage: org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage) -> None:
        """
            Add a Glonass navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage`): message to add
        
        
        """
        ...
    def addIRNSSNavigationMessage(self, iRNSSNavigationMessage: org.orekit.propagation.analytical.gnss.data.IRNSSNavigationMessage) -> None:
        """
            Add a IRNSS navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.IRNSSNavigationMessage`): message to add
        
        
        """
        ...
    def addQZSSNavigationMessage(self, qZSSNavigationMessage: org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage) -> None:
        """
            Add a QZSS navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage`): message to add
        
        
        """
        ...
    def addSBASNavigationMessage(self, sBASNavigationMessage: org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage) -> None:
        """
            Add a SBAS navigation message to the list.
        
            Parameters:
                message (:class:`~org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage`): message to add
        
        
        """
        ...
    def addTimeSystemCorrections(self, timeSystemCorrection: 'RinexNavigation.TimeSystemCorrection') -> None:
        """
            Add a time system correction to the list.
        
            Parameters:
                timeSystemCorrection (:class:`~org.orekit.gnss.navigation.RinexNavigation.TimeSystemCorrection`): the element to add
        
        
        """
        ...
    def getAgencyName(self) -> str:
        """
            Getter for the agency name.
        
            Returns:
                the agencyName
        
        
        """
        ...
    @typing.overload
    def getBeidouNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage]: ...
    @typing.overload
    def getBeidouNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage]]: ...
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
    def getFileType(self) -> str:
        """
            Get the file type.
        
            Returns:
                'N' for navigation data.
        
        
        """
        ...
    def getFormatVersion(self) -> float:
        """
            Getter for the format version.
        
            Returns:
                the format version
        
        
        """
        ...
    @typing.overload
    def getGPSNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage]: ...
    @typing.overload
    def getGPSNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage]]: ...
    @typing.overload
    def getGalileoNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage]: ...
    @typing.overload
    def getGalileoNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage]]: ...
    @typing.overload
    def getGlonassNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage]: ...
    @typing.overload
    def getGlonassNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage]]: ...
    @typing.overload
    def getIRNSSNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.IRNSSNavigationMessage]: ...
    @typing.overload
    def getIRNSSNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.IRNSSNavigationMessage]]: ...
    def getIonosphericCorrectionType(self) -> str:
        """
            Getter for the ionospheric correction type.
        
            Only the three first characters are given (e.g. GAL, GPS, QZS, BDS, or IRN)
        
            Returns:
                the ionospheric correction type
        
        
        """
        ...
    def getKlobucharAlpha(self) -> typing.List[float]:
        """
            Get the "alpha" ionospheric parameters.
        
            They are used to initialize the :class:`~org.orekit.models.earth.ionosphere.KlobucharIonoModel`.
        
            Returns:
                the "alpha" ionospheric parameters
        
        
        """
        ...
    def getKlobucharBeta(self) -> typing.List[float]:
        """
            Get the "beta" ionospheric parameters.
        
            They are used to initialize the :class:`~org.orekit.models.earth.ionosphere.KlobucharIonoModel`.
        
            Returns:
                the "beta" ionospheric parameters
        
        
        """
        ...
    def getNeQuickAlpha(self) -> typing.List[float]:
        """
            Get the "alpha" ionospheric parameters.
        
            They are used to initialize the :class:`~org.orekit.models.earth.ionosphere.NeQuickModel`.
        
            Returns:
                the "alpha" ionospheric parameters
        
        
        """
        ...
    def getNumberOfLeapSeconds(self) -> int:
        """
            Getter for the current number of leap seconds.
        
            Returns:
                the current number of leap seconds
        
        
        """
        ...
    def getProgramName(self) -> str:
        """
            Getter for the program name.
        
            Returns:
                the program name
        
        
        """
        ...
    @typing.overload
    def getQZSSNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage]: ...
    @typing.overload
    def getQZSSNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage]]: ...
    @typing.overload
    def getSBASNavigationMessages(self, string: str) -> java.util.List[org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage]: ...
    @typing.overload
    def getSBASNavigationMessages(self) -> java.util.Map[str, java.util.List[org.orekit.propagation.analytical.gnss.data.SBASNavigationMessage]]: ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
            Getter for the satellite system.
        
            Not specified for RINEX 2.X versions (value is null).
        
            Returns:
                the satellite system
        
        
        """
        ...
    def getTimeSystemCorrections(self) -> java.util.List['RinexNavigation.TimeSystemCorrection']: ...
    def setAgencyName(self, string: str) -> None:
        """
            Setter for the agency name.
        
            Parameters:
                agencyName (String): the agency name to set
        
        
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
                creationDateString (String): the creation date as a string to set
        
        
        """
        ...
    def setCreationTimeString(self, string: str) -> None:
        """
            Setter for the creation time as a string.
        
            Parameters:
                creationTimeString (String): the creation time as a string to set
        
        
        """
        ...
    def setCreationTimeZoneString(self, string: str) -> None:
        """
            Setter for the creation time zone.
        
            Parameters:
                creationTimeZoneString (String): the creation time zone as a string to set
        
        
        """
        ...
    def setFileType(self, string: str) -> None:
        """
            Setter for the file type.
        
            Parameters:
                fileType (String): must be 'N' for navigation data
        
        
        """
        ...
    def setFormatVersion(self, double: float) -> None:
        """
            Setter for the format version.
        
            Parameters:
                formatVersion (double): the format version to set
        
        
        """
        ...
    def setIonosphericCorrectionType(self, string: str) -> None:
        """
            Setter for the ionospheric correction type.
        
            Parameters:
                ionosphericCorrectionType (String): the ionospheric correction type to set
        
        
        """
        ...
    def setKlobucharAlpha(self, doubleArray: typing.List[float]) -> None:
        """
            Set the "alpha" ionspheric parameters.
        
            Parameters:
                klobucharAlpha (double[]): the "alpha" ionspheric parameters to set
        
        
        """
        ...
    def setKlobucharBeta(self, doubleArray: typing.List[float]) -> None:
        """
            Set the "beta" ionospheric parameters.
        
            Parameters:
                klobucharBeta (double[]): the "beta" ionospheric parameters to set
        
        
        """
        ...
    def setNeQuickAlpha(self, doubleArray: typing.List[float]) -> None:
        """
            Set the "alpha" ionospheric parameters.
        
            Parameters:
                neQuickAlpha (double[]): the "alpha" ionospheric parameters to set
        
        
        """
        ...
    def setNumberOfLeapSeconds(self, int: int) -> None:
        """
            Setter for the current number of leap seconds.
        
            Parameters:
                numberOfLeapSeconds (int): the number of leap seconds to set
        
        
        """
        ...
    def setProgramName(self, string: str) -> None:
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
                satelliteSystem (:class:`~org.orekit.gnss.SatelliteSystem`): the satellite system to set
        
        
        """
        ...
    class TimeSystemCorrection:
        def __init__(self, string: str, double: float, double2: float, int: int, int2: int): ...
        def getTimeSystemCorrectionA0(self) -> float: ...
        def getTimeSystemCorrectionA1(self) -> float: ...
        def getTimeSystemCorrectionSecOfWeek(self) -> int: ...
        def getTimeSystemCorrectionType(self) -> str: ...
        def getTimeSystemCorrectionWeekNumber(self) -> int: ...

class RinexNavigationParser:
    """
    public class RinexNavigationParser extends Object
    
        Parser for RINEX navigation messages files.
    
        This parser handles RINEX version from 3.01 to 3.05. It is not adapted for RINEX 2.10 and 2.11 versions.
    
        Since:
            11.0
    
        Also see:
            3.01 navigation messages file format, 3.02 navigation messages file format, 3.03 navigation messages file format, 3.04
            navigation messages file format, 3.05 navigation messages file format
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, timeScales: org.orekit.time.TimeScales): ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> RinexNavigation: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.navigation")``.

    RinexNavigation: typing.Type[RinexNavigation]
    RinexNavigationParser: typing.Type[RinexNavigationParser]
