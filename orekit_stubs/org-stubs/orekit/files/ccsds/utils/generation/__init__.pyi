import java.lang
import java.util
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation.class-use
import org.orekit.time
import org.orekit.utils.units
import typing



class Generator(java.lang.AutoCloseable):
    """
    public interface Generator extends :class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable?is`
    
        Generation interface for CCSDS messages.
    
        Since:
            11.0
    """
    def close(self) -> None: ...
    @typing.overload
    def dateToString(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str:
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
    def dateToString(self, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate) -> str:
        """
            Convert a date to string value with high precision.
        
            Parameters:
                converter (:class:`~org.orekit.files.ccsds.definitions.TimeConverter`): converter for dates
                date (:class:`~org.orekit.time.AbsoluteDate`): date to write
        
            Returns:
                date as a string
        
        """
        ...
    def doubleToString(self, double: float) -> str:
        """
            Convert a double to string value with high precision.
        
            We don't want to loose internal accuracy when writing doubles but we also don't want to have ugly representations like
            STEP = 1.25000000000000000 so we try a few simple formats first and fall back to scientific notation if it doesn't work.
        
            Parameters:
                value (double): value to format
        
            Returns:
                formatted value, with all original value accuracy preserved, or null if value is null or :code:`Double.NaN`
        
        
        """
        ...
    def endMessage(self, string: str) -> None: ...
    def enterSection(self, string: str) -> None: ...
    def exitSection(self) -> str: ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
            Get the generated file format.
        
            Returns:
                generated file format
        
        
        """
        ...
    def getOutputName(self) -> str:
        """
            Get the name of the output (for error messages).
        
            Returns:
                name of the output
        
        
        """
        ...
    def newLine(self) -> None: ...
    def siToCcsdsName(self, string: str) -> str:
        """
            Convert a SI unit name to a CCSDS name.
        
            Parameters:
                siName (:class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): si unit name
        
            Returns:
                CCSDS name for the unit
        
        
        """
        ...
    def startMessage(self, string: str, string2: str, double: float) -> None: ...
    def unitsListToString(self, list: java.util.List[org.orekit.utils.units.Unit]) -> str: ...
    def writeComments(self, list: java.util.List[str]) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, char: str, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, enum: java.lang.Enum[typing.Any], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, string2: str, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, list: java.util.List[str], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> None: ...
    @typing.overload
    def writeRawData(self, char: str) -> None: ...
    @typing.overload
    def writeRawData(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> None: ...

_MessageWriter__H = typing.TypeVar('_MessageWriter__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_MessageWriter__S = typing.TypeVar('_MessageWriter__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
_MessageWriter__F = typing.TypeVar('_MessageWriter__F', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <F>
class MessageWriter(typing.Generic[_MessageWriter__H, _MessageWriter__S, _MessageWriter__F]):
    """
    public interface MessageWriter<H extends :class:`~org.orekit.files.ccsds.section.Header`,S extends :class:`~org.orekit.files.ccsds.section.Segment`<?,?>,F extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<H,S>>
    
        Interface for writing Navigation Data Message (NDM) files.
    
        Since:
            11.0
    """
    def writeFooter(self, generator: Generator) -> None: ...
    def writeHeader(self, generator: Generator, h: _MessageWriter__H) -> None: ...
    def writeMessage(self, generator: Generator, f: _MessageWriter__F) -> None: ...
    def writeSegment(self, generator: Generator, s2: _MessageWriter__S) -> None: ...

class AbstractGenerator(Generator):
    """
    public abstract class AbstractGenerator extends :class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.utils.generation.Generator`
    
        Base class for both Key-Value Notation and eXtended Markup Language generators for CCSDS messages.
    
        Since:
            11.0
    """
    def __init__(self, appendable: java.lang.Appendable, string: str, boolean: bool): ...
    def close(self) -> None: ...
    @typing.overload
    def dateToString(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str:
        """
            Convert a date to string value with high precision.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.generation.Generator.dateToString` in
                interface :class:`~org.orekit.files.ccsds.utils.generation.Generator`
        
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
    def dateToString(self, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate) -> str:
        """
            Convert a date to string value with high precision.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.generation.Generator.dateToString` in
                interface :class:`~org.orekit.files.ccsds.utils.generation.Generator`
        
            Parameters:
                converter (:class:`~org.orekit.files.ccsds.definitions.TimeConverter`): converter for dates
                date (:class:`~org.orekit.time.AbsoluteDate`): date to write
        
            Returns:
                date as a string
        
        """
        ...
    def doubleToString(self, double: float) -> str:
        """
            Convert a double to string value with high precision.
        
            We don't want to loose internal accuracy when writing doubles but we also don't want to have ugly representations like
            STEP = 1.25000000000000000 so we try a few simple formats first and fall back to scientific notation if it doesn't work.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.generation.Generator.doubleToString` in
                interface :class:`~org.orekit.files.ccsds.utils.generation.Generator`
        
            Parameters:
                value (double): value to format
        
            Returns:
                formatted value, with all original value accuracy preserved, or null if value is null or :code:`Double.NaN`
        
        
        """
        ...
    def enterSection(self, string: str) -> None: ...
    def exitSection(self) -> str: ...
    def getOutputName(self) -> str:
        """
            Get the name of the output (for error messages).
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.generation.Generator.getOutputName` in
                interface :class:`~org.orekit.files.ccsds.utils.generation.Generator`
        
            Returns:
                name of the output
        
        
        """
        ...
    def newLine(self) -> None: ...
    def siToCcsdsName(self, string: str) -> str:
        """
            Convert a SI unit name to a CCSDS name.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.generation.Generator.siToCcsdsName` in
                interface :class:`~org.orekit.files.ccsds.utils.generation.Generator`
        
            Parameters:
                siName (:class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): si unit name
        
            Returns:
                CCSDS name for the unit
        
        
        """
        ...
    def unitsListToString(self, list: java.util.List[org.orekit.utils.units.Unit]) -> str: ...
    @typing.overload
    def writeEntry(self, string: str, string2: str, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, char: str, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, enum: java.lang.Enum[typing.Any], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, list: java.util.List[str], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> None: ...
    @typing.overload
    def writeRawData(self, char: str) -> None: ...
    @typing.overload
    def writeRawData(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> None: ...
    def writeUnits(self, unit: org.orekit.utils.units.Unit) -> bool:
        """
            Check if unit must be written.
        
            Parameters:
                unit (:class:`~org.orekit.utils.units.Unit`): entry unit
        
            Returns:
                true if units must be written
        
        
        """
        ...

_AbstractMessageWriter__H = typing.TypeVar('_AbstractMessageWriter__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_AbstractMessageWriter__S = typing.TypeVar('_AbstractMessageWriter__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
_AbstractMessageWriter__F = typing.TypeVar('_AbstractMessageWriter__F', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <F>
class AbstractMessageWriter(MessageWriter[_AbstractMessageWriter__H, _AbstractMessageWriter__S, _AbstractMessageWriter__F], typing.Generic[_AbstractMessageWriter__H, _AbstractMessageWriter__S, _AbstractMessageWriter__F]):
    """
    public abstract class AbstractMessageWriter<H extends :class:`~org.orekit.files.ccsds.section.Header`,S extends :class:`~org.orekit.files.ccsds.section.Segment`<?,?>,F extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<H,S>> extends :class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.utils.generation.MessageWriter`<H,S,F>
    
        Base class for Navigation Data Message (NDM) files.
    
        Since:
            11.0
    """
    DEFAULT_ORIGINATOR: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_ORIGINATOR
    
        Default value for :meth:`~org.orekit.files.ccsds.section.HeaderKey.ORIGINATOR`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, string2: str, double: float, contextBinding: org.orekit.files.ccsds.utils.ContextBinding): ...
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
    def getTimeConverter(self) -> org.orekit.files.ccsds.definitions.TimeConverter:
        """
            Get the current time converter.
        
            Returns:
                current time converter
        
        
        """
        ...
    def setContext(self, contextBinding: org.orekit.files.ccsds.utils.ContextBinding) -> None:
        """
            Reset context binding.
        
            Parameters:
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding to use
        
        
        """
        ...
    def writeFooter(self, generator: Generator) -> None: ...
    def writeHeader(self, generator: Generator, h: _AbstractMessageWriter__H) -> None: ...
    def writeSegment(self, generator: Generator, s2: _AbstractMessageWriter__S) -> None: ...
    def writeSegmentContent(self, generator: Generator, double: float, s2: _AbstractMessageWriter__S) -> None: ...

class KvnGenerator(AbstractGenerator):
    """
    public class KvnGenerator extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractGenerator`
    
        Generator for Key-Value Notation CCSDS messages.
    
        Since:
            11.0
    """
    def __init__(self, appendable: java.lang.Appendable, int: int, string: str, int2: int): ...
    def endMessage(self, string: str) -> None:
        """
            End CCSDS message.
        
            Parameters:
                root (:class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): root element for XML files
        
        
        """
        ...
    def enterSection(self, string: str) -> None: ...
    def exitSection(self) -> str: ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
            Get the generated file format.
        
            Returns:
                generated file format
        
        
        """
        ...
    def startMessage(self, string: str, string2: str, double: float) -> None: ...
    def writeComments(self, list: java.util.List[str]) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, char: str, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, enum: java.lang.Enum[typing.Any], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, list: java.util.List[str], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, string2: str, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...

class XmlGenerator(AbstractGenerator):
    """
    public class XmlGenerator extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractGenerator`
    
        Generator for eXtended Markup Language CCSDS messages.
    
        Since:
            11.0
    """
    DEFAULT_INDENT: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_INDENT
    
        Default number of space for each indentation level.
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNITS: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.utils.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` UNITS
    
        Name of the units attribute.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, appendable: java.lang.Appendable, int: int, string: str, boolean: bool): ...
    def endMessage(self, string: str) -> None: ...
    def enterSection(self, string: str) -> None: ...
    def exitSection(self) -> str: ...
    def getFormat(self) -> org.orekit.files.ccsds.utils.FileFormat:
        """
            Get the generated file format.
        
            Returns:
                generated file format
        
        
        """
        ...
    def startMessage(self, string: str, string2: str, double: float) -> None: ...
    def writeComments(self, list: java.util.List[str]) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, char: str, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, double: float, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, enum: java.lang.Enum[typing.Any], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, list: java.util.List[str], boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> None: ...
    @typing.overload
    def writeEntry(self, string: str, string2: str, unit: org.orekit.utils.units.Unit, boolean: bool) -> None: ...
    def writeOneAttributeElement(self, string: str, string2: str, string3: str, string4: str) -> None: ...
    def writeTwoAttributesElement(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils.generation")``.

    AbstractGenerator: typing.Type[AbstractGenerator]
    AbstractMessageWriter: typing.Type[AbstractMessageWriter]
    Generator: typing.Type[Generator]
    KvnGenerator: typing.Type[KvnGenerator]
    MessageWriter: typing.Type[MessageWriter]
    XmlGenerator: typing.Type[XmlGenerator]
    class-use: org.orekit.files.ccsds.utils.generation.class-use.__module_protocol__
