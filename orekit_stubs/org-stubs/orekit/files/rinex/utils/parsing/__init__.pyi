
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
    public class RinexUtils extends :class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utilities for RINEX various messages files.
    
        Since:
            12.0
    """
    LABEL_INDEX: typing.ClassVar[int] = ...
    """
    public static final int LABEL_INDEX
    
        Index of label in header lines.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def convert2DigitsYear(int: int) -> int:
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
    def getLabel(string: str) -> str:
        """
            Get the trimmed label from a header line.
        
            Parameters:
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): header line to parse
        
            Returns:
                trimmed label
        
        
        """
        ...
    @staticmethod
    def matchesLabel(string: str, string2: str) -> bool:
        """
            Check if a header line matches an expected label.
        
            Parameters:
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): header line to check
                label (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): expected label
        
            Returns:
                true if line matches expected label
        
        
        """
        ...
    @staticmethod
    def parseComment(int: int, string: str, rinexFile: org.orekit.files.rinex.RinexFile[typing.Any]) -> None:
        """
            Parse a comment.
        
            Parameters:
                lineNumber (int): line number
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): line to parse
                rinexFile (:class:`~org.orekit.files.rinex.RinexFile`<?> rinexFile): rinex file
        
        
        """
        ...
    @staticmethod
    def parseDouble(string: str, int: int, int2: int) -> float:
        """
            Parse a double value.
        
            Parameters:
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): line to parse
                startIndex (int): start index
                size (int): size of the value
        
            Returns:
                the parsed value
        
        
        """
        ...
    @staticmethod
    def parseInt(string: str, int: int, int2: int) -> int:
        """
            Parse an integer value.
        
            Parameters:
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): line to parse
                startIndex (int): start index
                size (int): size of the value
        
            Returns:
                the parsed value
        
        
        """
        ...
    @staticmethod
    def parseProgramRunByDate(string: str, int: int, string2: str, timeScales: org.orekit.time.TimeScales, rinexBaseHeader: org.orekit.files.rinex.section.RinexBaseHeader) -> None:
        """
            Parse program, run/by and date.
        
            Parameters:
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): line to parse
                lineNumber (int): line number
                name (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): file name (for error message generation)
                timeScales (:class:`~org.orekit.time.TimeScales`): the set of time scales used for parsing dates.
                header (:class:`~org.orekit.files.rinex.section.RinexBaseHeader`): header to fill with parsed data
        
        
        """
        ...
    @staticmethod
    def parseString(string: str, int: int, int2: int) -> str:
        """
            Parse a string value.
        
            Parameters:
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): line to parse
                startIndex (int): start index
                size (int): size of the value
        
            Returns:
                the parsed value
        
        
        """
        ...
    @staticmethod
    def parseVersionFileTypeSatelliteSystem(string: str, string2: str, rinexBaseHeader: org.orekit.files.rinex.section.RinexBaseHeader, *double: float) -> None:
        """
            Parse version, file type and satellite system.
        
            Parameters:
                line (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): line to parse
                name (:class:`~org.orekit.files.rinex.utils.parsing.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): file name (for error message generation)
                header (:class:`~org.orekit.files.rinex.section.RinexBaseHeader`): header to fill with parsed data
                supportedVersions (double...): supported versions
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex.utils.parsing")``.

    RinexUtils: typing.Type[RinexUtils]
