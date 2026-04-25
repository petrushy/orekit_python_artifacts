
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.orekit.files.rinex.utils
import org.orekit.gnss
import org.orekit.time
import typing



class RinexBaseHeader:
    """
    Base container for Rinex headers.
    
    Since:
        12.0
    """
    def getCreationDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for the creation date.
        
        Returns:
            the creation date
        
        
        """
        ...
    def getCreationDateComponents(self) -> org.orekit.time.DateTimeComponents:
        """
        Getter for the creation date of the file as a string.
        
        Returns:
            the creation date
        
        
        """
        ...
    def getCreationTimeZone(self) -> str:
        """
        Getter for the creation time zone of the file as a string.
        
        Returns:
            the creation time zone as a string
        
        
        """
        ...
    def getDoi(self) -> str:
        """
        Getter for the Digital Object Information.
        
        Returns:
            the Digital Object Information
        
        Since:
            12.0
        
        
        """
        ...
    def getFileType(self) -> org.orekit.files.rinex.utils.RinexFileType:
        """
        Get the file type.
        
        Returns:
            file type
        
        
        """
        ...
    def getFormatVersion(self) -> float:
        """
        Getter for the format version.
        
        Returns:
            the format version
        
        
        """
        ...
    def getLicense(self) -> str:
        """
        Getter for the license of use.
        
        Returns:
            the license of use
        
        Since:
            12.0
        
        
        """
        ...
    def getProgramName(self) -> str:
        """
        Getter for the program name.
        
        Returns:
            the program name
        
        
        """
        ...
    def getRunByName(self) -> str:
        """
        Getter for the run/by name.
        
        Returns:
            the run/by name
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
        Getter for the satellite system.
        
        Not specified for RINEX 2.X versions (value is null).
        
        Returns:
            the satellite system
        
        
        """
        ...
    def getStationInformation(self) -> str:
        """
        Getter for the station information.
        
        Returns:
            the station information
        
        Since:
            12.0
        
        
        """
        ...
    def setCreationDate(self, creationDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Setter for the creation date.
        
        Parameters:
            creationDate (AbsoluteDate): the creation date to set
        
        
        """
        ...
    def setCreationDateComponents(self, creationDateComponents: org.orekit.time.DateTimeComponents) -> None:
        """
        Setter for the creation date as a string.
        
        Parameters:
            creationDateComponents (DateTimeComponents): the creation date to set
        
        
        """
        ...
    def setCreationTimeZone(self, creationTimeZone: str) -> None:
        """
        Setter for the creation time zone.
        
        Parameters:
            creationTimeZone (String): the creation time zone to set
        
        
        """
        ...
    def setDoi(self, doi: str) -> None:
        """
        Setter for the Digital Object Information.
        
        Parameters:
            doi (String): the Digital Object Information to set
        
        Since:
            12.0
        
        
        """
        ...
    def setFormatVersion(self, formatVersion: float) -> None:
        """
        Setter for the format version.
        
        Parameters:
            formatVersion (double): the format version to set
        
        
        """
        ...
    def setLicense(self, license: str) -> None:
        """
        Setter for the license of use.
        
        Parameters:
            license (String): the license of use
        
        Since:
            12.0
        
        
        """
        ...
    def setProgramName(self, programName: str) -> None:
        """
        Setter for the program name.
        
        Parameters:
            programName (String): the program name to set
        
        
        """
        ...
    def setRunByName(self, runByName: str) -> None:
        """
        Setter for the run/by name.
        
        Parameters:
            runByName (String): the run/by name to set
        
        
        """
        ...
    def setSatelliteSystem(self, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> None:
        """
        Setter for the satellite system.
        
        Parameters:
            satelliteSystem (SatelliteSystem): the satellite system to set
        
        
        """
        ...
    def setStationInformation(self, stationInformation: str) -> None:
        """
        Setter for the station information.
        
        Parameters:
            stationInformation (String): the station information to set
        
        Since:
            12.0
        
        
        """
        ...

class RinexComment:
    """
    Container for comment in RINEX file.
    
    Since:
        12.0
    """
    def __init__(self, lineNumber: int, text: str):
        """
        Simple constructor.
        
        Parameters:
            lineNumber (int): line number
            text (String): text
        
        
        """
        ...
    def getLineNumber(self) -> int:
        """
        Get the line number.
        
        Returns:
            line number
        
        
        """
        ...
    def getText(self) -> str:
        """
        Get the text.
        
        Returns:
            text
        
        
        """
        ...

class RinexLabels(java.lang.Enum['RinexLabels']):
    """
    Labels for Rinex files.
    
    Since:
        12.0
    """
    VERSION: typing.ClassVar['RinexLabels'] = ...
    PROGRAM: typing.ClassVar['RinexLabels'] = ...
    COMMENT: typing.ClassVar['RinexLabels'] = ...
    MARKER_NAME: typing.ClassVar['RinexLabels'] = ...
    MARKER_NUMBER: typing.ClassVar['RinexLabels'] = ...
    MARKER_TYPE: typing.ClassVar['RinexLabels'] = ...
    OBSERVER_AGENCY: typing.ClassVar['RinexLabels'] = ...
    REC_NB_TYPE_VERS: typing.ClassVar['RinexLabels'] = ...
    ANT_NB_TYPE: typing.ClassVar['RinexLabels'] = ...
    APPROX_POSITION_XYZ: typing.ClassVar['RinexLabels'] = ...
    ANTENNA_DELTA_H_E_N: typing.ClassVar['RinexLabels'] = ...
    ANTENNA_DELTA_X_Y_Z: typing.ClassVar['RinexLabels'] = ...
    ANTENNA_PHASE_CENTER: typing.ClassVar['RinexLabels'] = ...
    ANTENNA_B_SIGHT_XYZ: typing.ClassVar['RinexLabels'] = ...
    ANTENNA_ZERODIR_AZI: typing.ClassVar['RinexLabels'] = ...
    ANTENNA_ZERODIR_XYZ: typing.ClassVar['RinexLabels'] = ...
    WAVELENGTH_FACT_L1_2: typing.ClassVar['RinexLabels'] = ...
    OBS_SCALE_FACTOR: typing.ClassVar['RinexLabels'] = ...
    CENTER_OF_MASS_XYZ: typing.ClassVar['RinexLabels'] = ...
    DOI: typing.ClassVar['RinexLabels'] = ...
    LICENSE: typing.ClassVar['RinexLabels'] = ...
    STATION_INFORMATION: typing.ClassVar['RinexLabels'] = ...
    NB_TYPES_OF_OBSERV: typing.ClassVar['RinexLabels'] = ...
    SYS_NB_TYPES_OF_OBSERV: typing.ClassVar['RinexLabels'] = ...
    SIGNAL_STRENGTH_UNIT: typing.ClassVar['RinexLabels'] = ...
    INTERVAL: typing.ClassVar['RinexLabels'] = ...
    TIME_OF_FIRST_OBS: typing.ClassVar['RinexLabels'] = ...
    TIME_OF_LAST_OBS: typing.ClassVar['RinexLabels'] = ...
    RCV_CLOCK_OFFS_APPL: typing.ClassVar['RinexLabels'] = ...
    SYS_DCBS_APPLIED: typing.ClassVar['RinexLabels'] = ...
    SYS_PCVS_APPLIED: typing.ClassVar['RinexLabels'] = ...
    SYS_SCALE_FACTOR: typing.ClassVar['RinexLabels'] = ...
    SYS_PHASE_SHIFT: typing.ClassVar['RinexLabels'] = ...
    GLONASS_SLOT_FRQ_NB: typing.ClassVar['RinexLabels'] = ...
    GLONASS_COD_PHS_BIS: typing.ClassVar['RinexLabels'] = ...
    LEAP_SECONDS: typing.ClassVar['RinexLabels'] = ...
    NB_OF_SATELLITES: typing.ClassVar['RinexLabels'] = ...
    PRN_NB_OF_OBS: typing.ClassVar['RinexLabels'] = ...
    END: typing.ClassVar['RinexLabels'] = ...
    def getLabel(self) -> str:
        """
        Get the first label.
        
        Returns:
            first label
        
        
        """
        ...
    def matches(self, label: str) -> bool:
        """
        Check if label matches.
        
        Parameters:
            label (String): label to check
        
        Returns:
            true if label matches one of the allowed label
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'RinexLabels':
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
    def values() -> typing.MutableSequence['RinexLabels']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RinexLabels c : RinexLabels.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.section")``.

    RinexBaseHeader: typing.Type[RinexBaseHeader]
    RinexComment: typing.Type[RinexComment]
    RinexLabels: typing.Type[RinexLabels]
