
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.files.rinex
import org.orekit.files.rinex.section
import org.orekit.time
import typing



class RinexUtils:
    """
    Utilities for RINEX various messages files.
    
    Since:
        12.0
    """
    LABEL_INDEX: typing.ClassVar[int] = ...
    """
    Index of label in header lines.
    
    Also see:
        constant
    
    
    """
    @staticmethod
    def convert2DigitsYear(yy: int) -> int:
        """
        Convert a 2 digits year to a complete year.
        
        Parameters:
            yy (int): year between 0 and 99
        
        Returns:
            complete year
        
        Since:
            12.0
        
        
        """
        ...
    @staticmethod
    def getLabel(line: str) -> str:
        """
        Get the trimmed label from a header line.
        
        Parameters:
            line (String): header line to parse
        
        Returns:
            trimmed label
        
        
        """
        ...
    @staticmethod
    def matchesLabel(line: str, label: str) -> bool:
        """
        Check if a header line matches an expected label.
        
        Parameters:
            line (String): header line to check
            label (String): expected label
        
        Returns:
            true if line matches expected label
        
        
        """
        ...
    @staticmethod
    def parseComment(lineNumber: int, line: str, rinexFile: org.orekit.files.rinex.RinexFile[typing.Any]) -> None:
        """
        Parse a comment.
        
        Parameters:
            lineNumber (int): line number
            line (String): line to parse
            rinexFile (RinexFile<?> rinexFile): rinex file
        
        
        """
        ...
    @staticmethod
    def parseDouble(line: str, startIndex: int, size: int) -> float:
        """
        Parse a double value.
        
        Parameters:
            line (String): line to parse
            startIndex (int): start index
            size (int): size of the value
        
        Returns:
            the parsed value
        
        
        """
        ...
    @staticmethod
    def parseInt(line: str, startIndex: int, size: int) -> int:
        """
        Parse an integer value.
        
        Parameters:
            line (String): line to parse
            startIndex (int): start index
            size (int): size of the value
        
        Returns:
            the parsed value
        
        
        """
        ...
    @staticmethod
    def parseProgramRunByDate(line: str, lineNumber: int, name: str, timeScales: org.orekit.time.TimeScales, header: org.orekit.files.rinex.section.RinexBaseHeader) -> None:
        """
        Parse program, run/by and date.
        
        Parameters:
            line (String): line to parse
            lineNumber (int): line number
            name (String): file name (for error message generation)
            timeScales (TimeScales): the set of time scales used for parsing dates.
            header (RinexBaseHeader): header to fill with parsed data
        
        
        """
        ...
    @staticmethod
    def parseString(line: str, startIndex: int, size: int) -> str:
        """
        Parse a string value.
        
        Parameters:
            line (String): line to parse
            startIndex (int): start index
            size (int): size of the value
        
        Returns:
            the parsed value
        
        
        """
        ...
    @staticmethod
    def parseVersionFileTypeSatelliteSystem(line: str, name: str, header: org.orekit.files.rinex.section.RinexBaseHeader, *supportedVersions: float) -> None:
        """
        Parse version, file type and satellite system.
        
        Parameters:
            line (String): line to parse
            name (String): file name (for error message generation)
            header (RinexBaseHeader): header to fill with parsed data
            supportedVersions (double...): supported versions
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.utils.parsing")``.

    RinexUtils: typing.Type[RinexUtils]
