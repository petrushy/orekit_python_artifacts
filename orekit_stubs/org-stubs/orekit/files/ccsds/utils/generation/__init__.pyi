
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class Generator(java.lang.AutoCloseable):
    """
    Generation interface for CCSDS messages.
    
    Since:
        11.0
    """
    def close(self) -> None:
        """
        Close the generator.
        
        Specified by: meth:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable.html?is` in interface AutoCloseable
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def dateToCalendarString(self, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate) -> str:
        """
        Convert a date to calendar string value with high precision.
        
        Parameters:
            converter (TimeConverter): converter for dates
            date (AbsoluteDate): date to write
        
        Returns:
            date as a calendar string
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def dateToString(self, year: int, month: int, day: int, hour: int, minute: int, seconds: float) -> str:
        """
        Convert a date to string value with high precision.
        
        Parameters:
            year (int): year
            month (int): month
            day (int): day
            hour (int): hour
            minute (int): minute
            seconds (double): seconds
        
        Returns:
            date as a string
        
        
        """
        ...
    @typing.overload
    def dateToString(self, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate) -> str:
        """
        Convert a date to string value with high precision.
        
        Parameters:
            converter (TimeConverter): converter for dates
            date (AbsoluteDate): date to write
        
        Returns:
            date as a string (may be either a relative date or a calendar date)
        
        """
        ...
    def doubleToString(self, value: float) -> str:
        """
        Convert a double to string value with high precision.
        
        We don't want to loose internal accuracy when writing doubles but we also don't want to have ugly representations like STEP = 1.25000000000000000 so we try a few simple formats first and fall back to scientific notation if it doesn't work.
        
        Parameters:
            value (double): value to format
        
        Returns:
            formatted value, with all original value accuracy preserved, or null if value is null or NaN
        
        
        """
        ...
    def endMessage(self, root: str) -> None:
        """
        End CCSDS message.
        
        Parameters:
            root (String): root element for XML files
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def enterSection(self, name: str) -> None:
        """
        Enter into a new section.
        
        Parameters:
            name (String): section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def exitSection(self) -> str:
        """
        Exit last section.
        
        Returns:
            section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
        Get the generated file format.
        
        Returns:
            generated file format
        
        
        """
        ...
    def getFormatter(self) -> org.orekit.utils.Formatter:
        """
        Used to format dates and doubles to string.
        
        Returns:
            formatter
        
        
        """
        ...
    def getOutputName(self) -> str:
        """
        Get the name of the output (for error messages).
        
        Returns:
            name of the output
        
        
        """
        ...
    def newLine(self) -> None:
        """
        Finish current line.
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def siToCcsdsName(self, siName: str) -> str:
        """
        Convert a SI unit name to a CCSDS name.
        
        Parameters:
            siName (String): si unit name
        
        Returns:
            CCSDS name for the unit
        
        
        """
        ...
    def startMessage(self, root: str, messageTypeKey: str, version: float) -> None:
        """
        Start CCSDS message.
        
        Parameters:
            messageTypeKey (String): key for message type
            root (String): root element for XML files
            version (double): format version
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def unitsListToString(self, units: java.util.List[org.orekit.utils.units.Unit]) -> str:
        """
        Convert a list of units to a bracketed string.
        
        Parameters:
            units (List<Unit> units): lists to output (may be null or empty)
        
        Returns:
            bracketed string (null if units list is null or empty)
        
        
        """
        ...
    def writeComments(self, comments: java.util.List[str]) -> None:
        """
        Write comment lines.
        
        Parameters:
            comments (List<String> comments): comments to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    @typing.overload
    def writeEntry(self, key: str, value: str, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: int, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: java.lang.Enum[typing.Any], mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: str, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: java.util.List[str], mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate, forceCalendar: bool, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: int, mandatory: bool) -> None: ...
    @typing.overload
    def writeRawData(self, data: str) -> None: ...
    @typing.overload
    def writeRawData(self, data: typing.Union[java.lang.CharSequence, str]) -> None: ...

_MessageWriter__H = typing.TypeVar('_MessageWriter__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_MessageWriter__S = typing.TypeVar('_MessageWriter__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
_MessageWriter__F = typing.TypeVar('_MessageWriter__F', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <F>
class MessageWriter(typing.Generic[_MessageWriter__H, _MessageWriter__S, _MessageWriter__F]):
    """
    Interface for writing Navigation Data Message (NDM) files.
    
    Since:
        11.0
    """
    def getFormatVersionKey(self) -> str:
        """
        Get key for format version.
        
        Returns:
            key for format version
        
        Since:
            12.0
        
        
        """
        ...
    def getRoot(self) -> str:
        """
        Get root element for XML files.
        
        Returns:
            root element for XML files
        
        Since:
            12.0
        
        
        """
        ...
    def getVersion(self) -> float:
        """
        Get current format version.
        
        Returns:
            current format version
        
        Since:
            12.0
        
        
        """
        ...
    def writeFooter(self, generator: Generator) -> None:
        """
        Write footer for the file.
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeHeader(self, generator: Generator, header: _MessageWriter__H) -> None:
        """
        Write header for the file.
        
        Parameters:
            generator (Generator): generator to use for producing output
            header (MessageWriter): header to write (creation date and originator will be added if missing)
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeMessage(self, generator: Generator, message: _MessageWriter__F) -> None:
        """
        Write one complete message.
        
        Parameters:
            generator (Generator): generator to use for producing output
            message (MessageWriter): message to write
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeSegment(self, generator: Generator, segment: _MessageWriter__S) -> None:
        """
        Write one segment.
        
        Parameters:
            generator (Generator): generator to use for producing output
            segment (MessageWriter): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class AbstractGenerator(Generator):
    """
    Base class for both Key-Value Notation and eXtended Markup Language generators for CCSDS messages.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self, output: java.lang.Appendable, outputName: str, maxRelativeOffset: float, writeUnits: bool): ...
    @typing.overload
    def __init__(self, output: java.lang.Appendable, outputName: str, maxRelativeOffset: float, writeUnits: bool, formatter: org.orekit.utils.Formatter): ...
    def close(self) -> None:
        """
        Close the generator.
        
        Specified by: meth:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable.html?is` in interface AutoCloseable
        
        Specified by: close in interface Generator
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def dateToCalendarString(self, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate) -> str:
        """
        Convert a date to calendar string value with high precision.
        
        Specified by: dateToCalendarString in interface Generator
        
        Parameters:
            converter (TimeConverter): converter for dates
            date (AbsoluteDate): date to write
        
        Returns:
            date as a calendar string
        
        
        """
        ...
    @typing.overload
    def dateToString(self, year: int, month: int, day: int, hour: int, minute: int, seconds: float) -> str:
        """
        Convert a date to string value with high precision.
        
        Specified by: dateToString in interface Generator
        
        Parameters:
            year (int): year
            month (int): month
            day (int): day
            hour (int): hour
            minute (int): minute
            seconds (double): seconds
        
        Returns:
            date as a string
        
        
        """
        ...
    @typing.overload
    def dateToString(self, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate) -> str:
        """
        Convert a date to string value with high precision.
        
        Specified by: dateToString in interface Generator
        
        Parameters:
            converter (TimeConverter): converter for dates
            date (AbsoluteDate): date to write
        
        Returns:
            date as a string (may be either a relative date or a calendar date)
        
        """
        ...
    def doubleToString(self, value: float) -> str:
        """
        Convert a double to string value with high precision.
        
        We don't want to loose internal accuracy when writing doubles but we also don't want to have ugly representations like STEP = 1.25000000000000000 so we try a few simple formats first and fall back to scientific notation if it doesn't work.
        
        Specified by: doubleToString in interface Generator
        
        Parameters:
            value (double): value to format
        
        Returns:
            formatted value, with all original value accuracy preserved, or null if value is null or NaN
        
        
        """
        ...
    def enterSection(self, name: str) -> None:
        """
        Enter into a new section.
        
        Specified by: enterSection in interface Generator
        
        Parameters:
            name (String): section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def exitSection(self) -> str:
        """
        Exit last section.
        
        Specified by: exitSection in interface Generator
        
        Returns:
            section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def getFormatter(self) -> org.orekit.utils.Formatter:
        """
        Used to format dates and doubles to string.
        
        Specified by: getFormatter in interface Generator
        
        Returns:
            formatter
        
        
        """
        ...
    def getOutputName(self) -> str:
        """
        Get the name of the output (for error messages).
        
        Specified by: getOutputName in interface Generator
        
        Returns:
            name of the output
        
        
        """
        ...
    def newLine(self) -> None:
        """
        Finish current line.
        
        Specified by: newLine in interface Generator
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def siToCcsdsName(self, siName: str) -> str:
        """
        Convert a SI unit name to a CCSDS name.
        
        Specified by: siToCcsdsName in interface Generator
        
        Parameters:
            siName (String): si unit name
        
        Returns:
            CCSDS name for the unit
        
        
        """
        ...
    def unitsListToString(self, units: java.util.List[org.orekit.utils.units.Unit]) -> str:
        """
        Convert a list of units to a bracketed string.
        
        Specified by: unitsListToString in interface Generator
        
        Parameters:
            units (List<Unit> units): lists to output (may be null or empty)
        
        Returns:
            bracketed string (null if units list is null or empty)
        
        
        """
        ...
    @typing.overload
    def writeEntry(self, key: str, value: str, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: int, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: str, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: int, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: java.lang.Enum[typing.Any], mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: java.util.List[str], mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate, forceCalendar: bool, mandatory: bool) -> None: ...
    @typing.overload
    def writeRawData(self, data: str) -> None: ...
    @typing.overload
    def writeRawData(self, data: typing.Union[java.lang.CharSequence, str]) -> None: ...
    def writeUnits(self, unit: org.orekit.utils.units.Unit) -> bool:
        """
        Check if unit must be written.
        
        Parameters:
            unit (Unit): entry unit
        
        Returns:
            true if units must be written
        
        
        """
        ...

_AbstractMessageWriter__H = typing.TypeVar('_AbstractMessageWriter__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_AbstractMessageWriter__S = typing.TypeVar('_AbstractMessageWriter__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
_AbstractMessageWriter__F = typing.TypeVar('_AbstractMessageWriter__F', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <F>
class AbstractMessageWriter(MessageWriter[_AbstractMessageWriter__H, _AbstractMessageWriter__S, _AbstractMessageWriter__F], typing.Generic[_AbstractMessageWriter__H, _AbstractMessageWriter__S, _AbstractMessageWriter__F]):
    """
    Base class for Navigation Data Message (NDM) files.
    
    Since:
        11.0
    """
    DEFAULT_ORIGINATOR: typing.ClassVar[str] = ...
    """
    Default value for ORIGINATOR.
    
    Also see:
        constant
    
    
    """
    def __init__(self, root: str, formatVersionKey: str, defaultVersion: float, context: org.orekit.files.ccsds.utils.ContextBinding):
        """
        Constructor used to create a new NDM writer configured with the necessary parameters to successfully fill in all required fields that aren't part of a standard object.
        
        If creation date and originator are not present in header, built-in defaults will be used
        
        Parameters:
            root (String): root element for XML files
            formatVersionKey (String): key for format version
            defaultVersion (double): default format version
            context (ContextBinding): context binding (may be reset for each segment)
        
        
        """
        ...
    def getContext(self) -> org.orekit.files.ccsds.utils.ContextBinding:
        """
        Get the current context.
        
        Returns:
            current context
        
        
        """
        ...
    def getDefaultVersion(self) -> float:
        """
        Get the default format version.
        
        Returns:
            default format version
        
        
        """
        ...
    def getFormatVersionKey(self) -> str:
        """
        Get key for format version.
        
        Specified by: getFormatVersionKey in interface MessageWriter
        
        Returns:
            key for format version
        
        
        """
        ...
    def getRoot(self) -> str:
        """
        Get root element for XML files.
        
        Specified by: getRoot in interface MessageWriter
        
        Returns:
            root element for XML files
        
        
        """
        ...
    def getTimeConverter(self) -> org.orekit.files.ccsds.definitions.TimeConverter:
        """
        Get the current time converter.
        
        Returns:
            current time converter
        
        
        """
        ...
    def getVersion(self) -> float:
        """
        Get current format version.
        
        Specified by: getVersion in interface MessageWriter
        
        Returns:
            current format version
        
        
        """
        ...
    def setContext(self, context: org.orekit.files.ccsds.utils.ContextBinding) -> None:
        """
        Reset context binding.
        
        Parameters:
            context (ContextBinding): context binding to use
        
        
        """
        ...
    def writeFooter(self, generator: Generator) -> None:
        """
        Write footer for the file.
        
        Specified by: writeFooter in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeHeader(self, generator: Generator, header: _AbstractMessageWriter__H) -> None:
        """
        Write header for the file.
        
        Specified by: writeHeader in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            header (AbstractMessageWriter): header to write (creation date and originator will be added if missing)
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeSegment(self, generator: Generator, segment: _AbstractMessageWriter__S) -> None:
        """
        Write one segment.
        
        Specified by: writeSegment in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            segment (AbstractMessageWriter): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class PythonGenerator(Generator):
    def __init__(self): ...
    def close(self) -> None:
        """
        Close the generator.
        
        Specified by: meth:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable.html?is` in interface AutoCloseable
        
        Specified by: close in interface Generator
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def dateToCalendarString(self, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate) -> str:
        """
        Convert a date to calendar string value with high precision.
        
        Specified by: dateToCalendarString in interface Generator
        
        Parameters:
            converter (TimeConverter): converter for dates
            date (AbsoluteDate): date to write
        
        Returns:
            date as a calendar string
        
        
        """
        ...
    @typing.overload
    def dateToString(self, year: int, month: int, day: int, hour: int, minute: int, seconds: float) -> str:
        """
        Convert a date to string value with high precision.
        
        Specified by: dateToString in interface Generator
        
        Parameters:
            year (int): year
            month (int): month
            day (int): day
            hour (int): hour
            minute (int): minute
            seconds (double): seconds
        
        Returns:
            date as a string
        
        
        """
        ...
    @typing.overload
    def dateToString(self, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate) -> str:
        """
        Convert a date to string value with high precision.
        
        Specified by: dateToString in interface Generator
        
        Parameters:
            converter (TimeConverter): converter for dates
            date (AbsoluteDate): date to write
        
        Returns:
            date as a string (may be either a relative date or a calendar date)
        
        """
        ...
    def doubleToString(self, value: float) -> str:
        """
        Convert a double to string value with high precision.
        
        We don't want to loose internal accuracy when writing doubles but we also don't want to have ugly representations like STEP = 1.25000000000000000 so we try a few simple formats first and fall back to scientific notation if it doesn't work.
        
        Specified by: doubleToString in interface Generator
        
        Parameters:
            value (double): value to format
        
        Returns:
            formatted value, with all original value accuracy preserved, or null if value is null or NaN
        
        
        """
        ...
    def endMessage(self, root: str) -> None:
        """
        End CCSDS message.
        
        Specified by: endMessage in interface Generator
        
        Parameters:
            root (String): root element for XML files
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def enterSection(self, name: str) -> None:
        """
        Enter into a new section.
        
        Specified by: enterSection in interface Generator
        
        Parameters:
            name (String): section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def exitSection(self) -> str:
        """
        Exit last section.
        
        Specified by: exitSection in interface Generator
        
        Returns:
            section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
        Get the generated file format.
        
        Specified by: getFormat in interface Generator
        
        Returns:
            generated file format
        
        
        """
        ...
    def getFormatter(self) -> org.orekit.utils.Formatter:
        """
        Used to format dates and doubles to string.
        
        Specified by: getFormatter in interface Generator
        
        Returns:
            formatter
        
        
        """
        ...
    def getOutputName(self) -> str:
        """
        Get the name of the output (for error messages).
        
        Specified by: getOutputName in interface Generator
        
        Returns:
            name of the output
        
        
        """
        ...
    def newLine(self) -> None:
        """
        Finish current line.
        
        Specified by: newLine in interface Generator
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...
    def siToCcsdsName(self, siName: str) -> str:
        """
        Convert a SI unit name to a CCSDS name.
        
        Specified by: siToCcsdsName in interface Generator
        
        Parameters:
            siName (String): si unit name
        
        Returns:
            CCSDS name for the unit
        
        
        """
        ...
    def startMessage(self, root: str, messageTypeKey: str, version: float) -> None:
        """
        Start CCSDS message.
        
        Specified by: startMessage in interface Generator
        
        Parameters:
            root (String): root element for XML files
            messageTypeKey (String): key for message type
            version (double): format version
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def unitsListToString(self, units: java.util.List[org.orekit.utils.units.Unit]) -> str:
        """
        Convert a list of units to a bracketed string.
        
        Specified by: unitsListToString in interface Generator
        
        Parameters:
            units (List<Unit> units): lists to output (may be null or empty)
        
        Returns:
            bracketed string (null if units list is null or empty)
        
        
        """
        ...
    def writeComments(self, comments: java.util.List[str]) -> None:
        """
        Write comment lines.
        
        Specified by: writeComments in interface Generator
        
        Parameters:
            comments (List<String> comments): comments to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    @typing.overload
    def writeEntry(self, key: str, value: int, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: str, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: int, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: java.lang.Enum[typing.Any], mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: str, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: java.util.List[str], mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, converter: org.orekit.files.ccsds.definitions.TimeConverter, date: org.orekit.time.AbsoluteDate, forceCalendar: bool, mandatory: bool) -> None: ...
    @typing.overload
    def writeRawData(self, data: str) -> None: ...
    @typing.overload
    def writeRawData(self, data: typing.Union[java.lang.CharSequence, str]) -> None: ...

_PythonMessageWriter__H = typing.TypeVar('_PythonMessageWriter__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_PythonMessageWriter__S = typing.TypeVar('_PythonMessageWriter__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
_PythonMessageWriter__F = typing.TypeVar('_PythonMessageWriter__F', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <F>
class PythonMessageWriter(MessageWriter[_PythonMessageWriter__H, _PythonMessageWriter__S, _PythonMessageWriter__F], typing.Generic[_PythonMessageWriter__H, _PythonMessageWriter__S, _PythonMessageWriter__F]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFormatVersionKey(self) -> str:
        """
        Description copied from interface: getFormatVersionKey Get key for format version.
        
        Specified by: getFormatVersionKey in interface MessageWriter
        
        Returns:
            key for format version
        
        
        """
        ...
    def getRoot(self) -> str:
        """
        Description copied from interface: getRoot Get root element for XML files.
        
        Specified by: getRoot in interface MessageWriter
        
        Returns:
            root element for XML files
        
        
        """
        ...
    def getVersion(self) -> float:
        """
        Description copied from interface: getVersion Get current format version.
        
        Specified by: getVersion in interface MessageWriter
        
        Returns:
            current format version
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...
    def writeFooter(self, generator: Generator) -> None:
        """
        Write footer for the file.
        
        Specified by: writeFooter in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeHeader(self, generator: Generator, header: _PythonMessageWriter__H) -> None:
        """
        Write header for the file.
        
        Specified by: writeHeader in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            header (PythonMessageWriter): header to write (creation date and originator will be added if missing)
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeSegment(self, generator: Generator, segment: _PythonMessageWriter__S) -> None:
        """
        Write one segment.
        
        Specified by: writeSegment in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            segment (PythonMessageWriter): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class KvnGenerator(AbstractGenerator):
    """
    Generator for Key-Value Notation CCSDS messages.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self, output: java.lang.Appendable, paddingWidth: int, outputName: str, maxRelativeOffset: float, unitsColumn: int): ...
    @typing.overload
    def __init__(self, output: java.lang.Appendable, paddingWidth: int, outputName: str, maxRelativeOffset: float, unitsColumn: int, formatter: org.orekit.utils.Formatter): ...
    def endMessage(self, root: str) -> None:
        """
        End CCSDS message.
        
        Parameters:
            root (String): root element for XML files
        
        
        """
        ...
    def enterSection(self, name: str) -> None:
        """
        Enter into a new section.
        
        Specified by: enterSection in interface Generator
        
        Overrides: enterSection in class AbstractGenerator
        
        Parameters:
            name (String): section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def exitSection(self) -> str:
        """
        Exit last section.
        
        Specified by: exitSection in interface Generator
        
        Overrides: exitSection in class AbstractGenerator
        
        Returns:
            section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
        Get the generated file format.
        
        Returns:
            generated file format
        
        
        """
        ...
    def startMessage(self, root: str, messageTypeKey: str, version: float) -> None:
        """
        Start CCSDS message.
        
        Parameters:
            root (String): root element for XML files
            messageTypeKey (String): key for message type
            version (double): format version
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def writeComments(self, comments: java.util.List[str]) -> None:
        """
        Write comment lines.
        
        Parameters:
            comments (List<String> comments): comments to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    @typing.overload
    def writeEntry(self, string: str, integer: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, char: str, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, enum: java.lang.Enum[typing.Any], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, list: java.util.List[str], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool, boolean2: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: str, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...

class PythonAbstractGenerator(AbstractGenerator):
    @typing.overload
    def __init__(self, output: java.lang.Appendable, outputName: str, maxRelativeOffset: float, writeUnits: bool): ...
    @typing.overload
    def __init__(self, output: java.lang.Appendable, outputName: str, maxRelativeOffset: float, writeUnits: bool, formatter: org.orekit.utils.Formatter): ...
    def endMessage(self, root: str) -> None:
        """
        End CCSDS message.
        
        Parameters:
            root (String): root element for XML files
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
        Get the generated file format.
        
        Returns:
            generated file format
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def startMessage(self, root: str, messageTypeKey: str, version: float) -> None:
        """
        Start CCSDS message.
        
        Parameters:
            root (String): root element for XML files
            messageTypeKey (String): key for message type
            version (double): format version
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def writeComments(self, comments: java.util.List[str]) -> None:
        """
        Write comment lines.
        
        Parameters:
            comments (List<String> comments): comments to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    @typing.overload
    def writeEntry(self, string: str, integer: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: str, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, char: str, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, enum: java.lang.Enum[typing.Any], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, list: java.util.List[str], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool, boolean2: bool) -> None: ...

_PythonAbstractMessageWriter__H = typing.TypeVar('_PythonAbstractMessageWriter__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_PythonAbstractMessageWriter__S = typing.TypeVar('_PythonAbstractMessageWriter__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
_PythonAbstractMessageWriter__F = typing.TypeVar('_PythonAbstractMessageWriter__F', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <F>
class PythonAbstractMessageWriter(AbstractMessageWriter[_PythonAbstractMessageWriter__H, _PythonAbstractMessageWriter__S, _PythonAbstractMessageWriter__F], typing.Generic[_PythonAbstractMessageWriter__H, _PythonAbstractMessageWriter__S, _PythonAbstractMessageWriter__F]):
    def __init__(self, root: str, formatVersionKey: str, defaultVersion: float, context: org.orekit.files.ccsds.utils.ContextBinding):
        """
        Constructor used to create a new NDM writer configured with the necessary parameters to successfully fill in all required fields that aren't part of a standard object.
        
        If creation date and originator are not present in header, built-in defaults will be used
        
        Parameters:
            root (String): root element for XML files
            formatVersionKey (String): key for format version
            defaultVersion (double): default format version
            context (ContextBinding): context binding (may be reset for each segment)
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def writeSegmentContent(self, generator: Generator, formatVersion: float, segment: _PythonAbstractMessageWriter__S) -> None:
        """
        Write one segment content (without XML wrapping).
        
        Specified by: writeSegmentContent in class AbstractMessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            formatVersion (double): format version to use
            segment (PythonAbstractMessageWriter): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class XmlGenerator(AbstractGenerator):
    """
    Generator for eXtended Markup Language CCSDS messages.
    
    Since:
        11.0
    """
    DEFAULT_INDENT: typing.ClassVar[int] = ...
    """
    Default number of space for each indentation level.
    
    Also see:
        constant
    
    
    """
    UNITS: typing.ClassVar[str] = ...
    """
    Name of the units attribute.
    
    Also see:
        constant
    
    
    """
    NDM_XML_V3_SCHEMA_LOCATION: typing.ClassVar[str] = ...
    """
    NDM/XML version 3 location.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, output: java.lang.Appendable, indentation: int, outputName: str, maxRelativeOffset: float, writeUnits: bool, schemaLocation: str): ...
    @typing.overload
    def __init__(self, output: java.lang.Appendable, indentation: int, outputName: str, maxRelativeOffset: float, writeUnits: bool, schemaLocation: str, formatter: org.orekit.utils.Formatter): ...
    def endMessage(self, root: str) -> None:
        """
        End CCSDS message.
        
        Parameters:
            root (String): root element for XML files
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def enterSection(self, name: str) -> None:
        """
        Enter into a new section.
        
        Specified by: enterSection in interface Generator
        
        Overrides: enterSection in class AbstractGenerator
        
        Parameters:
            name (String): section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def exitSection(self) -> str:
        """
        Exit last section.
        
        Specified by: exitSection in interface Generator
        
        Overrides: exitSection in class AbstractGenerator
        
        Returns:
            section name
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
        Get the generated file format.
        
        Returns:
            generated file format
        
        
        """
        ...
    def startMessage(self, root: str, messageTypeKey: str, version: float) -> None:
        """
        Start CCSDS message.
        
        Parameters:
            root (String): root element for XML files
            messageTypeKey (String): key for message type
            version (double): format version
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def writeComments(self, comments: java.util.List[str]) -> None:
        """
        Write comment lines.
        
        Parameters:
            comments (List<String> comments): comments to write
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    @typing.overload
    def writeEntry(self, string: str, integer: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, char: str, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: float, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, enum: java.lang.Enum[typing.Any], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, list: java.util.List[str], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool, boolean2: bool) -> None: ...
    @typing.overload
    def writeEntry(self, key: str, value: str, unit: org.orekit.utils.units.Unit, mandatory: bool) -> None: ...
    def writeOneAttributeElement(self, name: str, value: str, attributeName: str, attributeValue: str) -> None:
        """
        Write an element with one attribute.
        
        Parameters:
            name (String): tag name
            value (String): element value
            attributeName (String): attribute name
            attributeValue (String): attribute value
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...
    def writeTwoAttributesElement(self, name: str, value: str, attribute1Name: str, attribute1Value: str, attribute2Name: str, attribute2Value: str) -> None:
        """
        Write an element with two attributes.
        
        Parameters:
            name (String): tag name
            value (String): element value
            attribute1Name (String): attribute 1 name
            attribute1Value (String): attribute 1 value
            attribute2Name (String): attribute 2 name
            attribute2Value (String): attribute 2 value
        
        Raises:
            IOException: if an I/O error occurs.
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils.generation")``.

    AbstractGenerator: typing.Type[AbstractGenerator]
    AbstractMessageWriter: typing.Type[AbstractMessageWriter]
    Generator: typing.Type[Generator]
    KvnGenerator: typing.Type[KvnGenerator]
    MessageWriter: typing.Type[MessageWriter]
    PythonAbstractGenerator: typing.Type[PythonAbstractGenerator]
    PythonAbstractMessageWriter: typing.Type[PythonAbstractMessageWriter]
    PythonGenerator: typing.Type[PythonGenerator]
    PythonMessageWriter: typing.Type[PythonMessageWriter]
    XmlGenerator: typing.Type[XmlGenerator]
