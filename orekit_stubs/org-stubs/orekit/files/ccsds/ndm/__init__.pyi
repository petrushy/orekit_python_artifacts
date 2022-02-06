import java.lang
import java.util
import org.orekit.data
import org.orekit.files.ccsds.ndm.adm
import org.orekit.files.ccsds.ndm.adm.aem
import org.orekit.files.ccsds.ndm.adm.apm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.ndm.odm.ocm
import org.orekit.files.ccsds.ndm.odm.oem
import org.orekit.files.ccsds.ndm.odm.omm
import org.orekit.files.ccsds.ndm.odm.opm
import org.orekit.files.ccsds.ndm.tdm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



_AbstractBuilder__T = typing.TypeVar('_AbstractBuilder__T', bound='AbstractBuilder')  # <T>
class AbstractBuilder(typing.Generic[_AbstractBuilder__T]):
    """
    public abstract class AbstractBuilder<T extends AbstractBuilder<T>> extends Object
    
        Abstract builder for all :class:`~org.orekit.files.ccsds.ndm.NdmConstituent` files parsers/writers.
    
        Since:
            11.0
    """
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
            Get the IERS conventions.
        
            Returns:
                IERS conventions
        
        
        """
        ...
    def getDataContext(self) -> org.orekit.data.DataContext:
        """
            Get the data context.
        
            Returns:
                data context used to retrieve frames, time scales, etc.
        
        
        """
        ...
    def getMissionReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the mission reference date or Mission Elapsed Time or Mission Relative Time time systems.
        
            Returns:
                mission reference date
        
        
        """
        ...
    def getRangeUnitsConverter(self) -> org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter:
        """
            Get the converter for :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`.
        
            Returns:
                converter for :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
        
        """
        ...
    def withConventions(self, iERSConventions: org.orekit.utils.IERSConventions) -> _AbstractBuilder__T:
        """
            Set up IERS conventions.
        
            Parameters:
                newConventions (:class:`~org.orekit.utils.IERSConventions`): IERS Conventions
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withDataContext(self, dataContext: org.orekit.data.DataContext) -> _AbstractBuilder__T:
        """
            Set up data context used to retrieve frames, time scales, etc..
        
            Parameters:
                newDataContext (:class:`~org.orekit.data.DataContext`): data context used to retrieve frames, time scales, etc.
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withMissionReferenceDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> _AbstractBuilder__T:
        """
            Set up mission reference date or Mission Elapsed Time or Mission Relative Time time systems.
        
            The mission reference date is used only by :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemParser` and
            :class:`~org.orekit.files.ccsds.ndm.adm.apm.ApmParser`, and by :class:`~org.orekit.files.ccsds.ndm.odm.opm.OpmParser`,
            :class:`~org.orekit.files.ccsds.ndm.odm.omm.OmmParser` and :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemParser` up to
            version 2.0 of ODM (starting with version 3.0 of ODM, both MET and MRT time system have been withdrawn from the
            standard).
        
            Parameters:
                newMissionReferenceDate (:class:`~org.orekit.time.AbsoluteDate`): mission reference date or Mission Elapsed Time or Mission Relative Time time systems
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withRangeUnitsConverter(self, rangeUnitsConverter: org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter) -> _AbstractBuilder__T:
        """
            Set up the converter for :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`.
        
            Parameters:
                newRangeUnitsConverter (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`): converter for :meth:`~org.orekit.files.ccsds.ndm.tdm.RangeUnits.RU`
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...

class Ndm:
    """
    public class Ndm extends Object
    
        CCSDS Navigation Data Message. This class is a container for comments and
        :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`.
    
        Since:
            11.0
    """
    def __init__(self, list: java.util.List[str], list2: java.util.List['NdmConstituent'[typing.Any, typing.Any]]): ...
    def getComments(self) -> java.util.List[str]:
        """
            Get an unmodifiable view of the comments.
        
            Returns:
                unmodifiable view of the comment
        
        
        """
        ...
    def getConstituents(self) -> java.util.List['NdmConstituent'[typing.Any, typing.Any]]: ...

_NdmConstituent__H = typing.TypeVar('_NdmConstituent__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_NdmConstituent__S = typing.TypeVar('_NdmConstituent__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
class NdmConstituent(typing.Generic[_NdmConstituent__H, _NdmConstituent__S]):
    """
    public abstract class NdmConstituent<H extends :class:`~org.orekit.files.ccsds.section.Header`,S extends :class:`~org.orekit.files.ccsds.section.Segment`<?,?>> extends Object
    
        Constituents of a CCSDS Navigation Data Message. Constituents may be Attitude Data Message (ADM), Orbit Data Message
        (ODM), Tracking Data Message (TDM)Ã¢â‚¬Â¦ Each constituent has its own header and a list of segments.
    
        Since:
            10.2
    """
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
            Get IERS conventions.
        
            Returns:
                IERS conventions
        
        
        """
        ...
    def getDataContext(self) -> org.orekit.data.DataContext:
        """
            Get the data context.
        
            Returns:
                the data context used for creating frames, time scales, etc.
        
        
        """
        ...
    def getHeader(self) -> _NdmConstituent__H:
        """
            Get the header.
        
            Returns:
                header
        
            Since:
                11.0
        
        
        """
        ...
    def getSegments(self) -> java.util.List[_NdmConstituent__S]: ...
    def validate(self) -> None:
        """
            Validate the file message for required and forbidden entries.
        
            This method throws an exception if file does not meet format requirements. The requirements may depend on format
            version, which is found in header.
        
        """
        ...

class NdmParser(org.orekit.files.ccsds.utils.parsing.AbstractMessageParser[Ndm]):
    """
    public class NdmParser extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser`<:class:`~org.orekit.files.ccsds.ndm.Ndm`>
    
        A parser for the CCSDS NDM (Navigation Data Message).
    
        Since:
            11.0
    """
    def __init__(self, parserBuilder: 'ParserBuilder'): ...
    def addComment(self, string: str) -> bool:
        """
            Add comment.
        
            Comments are accepted only at start. Once other content is stored in the same section, comments are refused.
        
            Parameters:
                comment (String): comment line
        
            Returns:
                true if comment was accepted
        
        
        """
        ...
    def build(self) -> Ndm:
        """
            Build the file from parsed entries.
        
            Returns:
                parsed file
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]: ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class NdmWriter:
    """
    public class NdmWriter extends Object
    
        Writer for CCSDS Navigation Data Message.
    
        Since:
            11.0
    """
    def __init__(self, writerBuilder: 'WriterBuilder'): ...
    def writeComment(self, generator: org.orekit.files.ccsds.utils.generation.Generator, string: str) -> None: ...
    _writeConstituent__H = typing.TypeVar('_writeConstituent__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
    _writeConstituent__S = typing.TypeVar('_writeConstituent__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
    _writeConstituent__F = typing.TypeVar('_writeConstituent__F', bound=NdmConstituent)  # <F>
    def writeConstituent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, f: _writeConstituent__F) -> None: ...
    def writeMessage(self, generator: org.orekit.files.ccsds.utils.generation.Generator, ndm: Ndm) -> None: ...

class ParsedUnitsBehavior(java.lang.Enum['ParsedUnitsBehavior']):
    """
    public enum ParsedUnitsBehavior extends Enum<:class:`~org.orekit.files.ccsds.ndm.ParsedUnitsBehavior`>
    
        Behavior adopted for units that have been parsed from a CCSDS message.
    
        Since:
            11.0
    """
    IGNORE_PARSED: typing.ClassVar['ParsedUnitsBehavior'] = ...
    CONVERT_COMPATIBLE: typing.ClassVar['ParsedUnitsBehavior'] = ...
    STRICT_COMPLIANCE: typing.ClassVar['ParsedUnitsBehavior'] = ...
    def select(self, unit: org.orekit.utils.units.Unit, unit2: org.orekit.utils.units.Unit) -> org.orekit.utils.units.Unit:
        """
            Select the unit to use for interpreting parsed value.
        
            Parameters:
                message (:class:`~org.orekit.utils.units.Unit`): unit parsed in the CCSDS message
                standard (:class:`~org.orekit.utils.units.Unit`): unit mandated by the standard
        
            Returns:
                selected unit
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ParsedUnitsBehavior':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['ParsedUnitsBehavior']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ParsedUnitsBehavior c : ParsedUnitsBehavior.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ParserBuilder(AbstractBuilder['ParserBuilder']):
    """
    public class ParserBuilder extends :class:`~org.orekit.files.ccsds.ndm.AbstractBuilder`<:class:`~org.orekit.files.ccsds.ndm.ParserBuilder`>
    
        Builder for all :class:`~org.orekit.files.ccsds.ndm.NdmConstituent` files parsers.
    
        This builder can be used for building all CCSDS Messages parsers types. It is particularly useful in multi-threaded
        context as parsers cannot be shared between threads and thus several independent parsers must be built in this case.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def buildAemParser(self) -> org.orekit.files.ccsds.ndm.adm.aem.AemParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.adm.aem.Aem`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def buildApmParser(self) -> org.orekit.files.ccsds.ndm.adm.apm.ApmParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.adm.apm.Apm`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def buildNdmParser(self) -> NdmParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.Ndm`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def buildOcmParser(self) -> org.orekit.files.ccsds.ndm.odm.ocm.OcmParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def buildOemParser(self) -> org.orekit.files.ccsds.ndm.odm.oem.OemParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.odm.oem.Oem`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def buildOmmParser(self) -> org.orekit.files.ccsds.ndm.odm.omm.OmmParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.odm.omm.Omm`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def buildOpmParser(self) -> org.orekit.files.ccsds.ndm.odm.opm.OpmParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.odm.opm.Opm`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def buildTdmParser(self) -> org.orekit.files.ccsds.ndm.tdm.TdmParser:
        """
            Build a parser for :class:`~org.orekit.files.ccsds.ndm.tdm.Tdm`.
        
            Returns:
                a new parser
        
        
        """
        ...
    def getDefaultInterpolationDegree(self) -> int:
        """
            Get the default interpolation degree.
        
            Returns:
                default interpolation degree
        
        
        """
        ...
    def getDefaultMass(self) -> float:
        """
            Get the default mass.
        
            Returns:
                default mass
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the gravitational coefficient.
        
            Returns:
                gravitational coefficient
        
        
        """
        ...
    def getParsedUnitsBehavior(self) -> ParsedUnitsBehavior:
        """
            Get the behavior to adopt for handling parsed units.
        
            Returns:
                behavior to adopt for handling parsed units
        
        
        """
        ...
    def isSimpleEOP(self) -> bool:
        """
            Check if tidal effects are ignored when interpolating EOP.
        
            Returns:
                true if tidal effects are ignored when interpolating EOP
        
        
        """
        ...
    def withDefaultInterpolationDegree(self, int: int) -> 'ParserBuilder':
        """
            Set up the default interpolation degree.
        
            The default interpolation degree is used only by :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemParser` and
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemParser`.
        
            Parameters:
                newDefaultInterpolationDegree (int): default interpolation degree
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withDefaultMass(self, double: float) -> 'ParserBuilder':
        """
            Set up the default mass.
        
            The default mass is used only by :class:`~org.orekit.files.ccsds.ndm.odm.opm.OpmParser`.
        
            Parameters:
                newDefaultMass (double): default mass
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withMu(self, double: float) -> 'ParserBuilder':
        """
            Set up the gravitational coefficient.
        
            Parameters:
                newMu (double): gravitational coefficient
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withParsedUnitsBehavior(self, parsedUnitsBehavior: ParsedUnitsBehavior) -> 'ParserBuilder':
        """
            Set up the behavior to adopt for handling parsed units.
        
            Parameters:
                newParsedUnitsBehavior (:class:`~org.orekit.files.ccsds.ndm.ParsedUnitsBehavior`): behavior to adopt for handling parsed units
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withSimpleEOP(self, boolean: bool) -> 'ParserBuilder':
        """
            Set up flag for ignoring tidal effects when interpolating EOP.
        
            Parameters:
                newSimpleEOP (boolean): true if tidal effects are ignored when interpolating EOP
        
            Returns:
                a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...

_PythonAbstractBuilder__T = typing.TypeVar('_PythonAbstractBuilder__T', bound=AbstractBuilder)  # <T>
class PythonAbstractBuilder(AbstractBuilder[_PythonAbstractBuilder__T], typing.Generic[_PythonAbstractBuilder__T]):
    """
    public class PythonAbstractBuilder<T extends :class:`~org.orekit.files.ccsds.ndm.AbstractBuilder`<T>> extends :class:`~org.orekit.files.ccsds.ndm.AbstractBuilder`<T>
    """
    def create(self, iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate, rangeUnitsConverter: org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter) -> _PythonAbstractBuilder__T:
        """
            Build an instance.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.ndm.AbstractBuilder.create`Â in
                classÂ :class:`~org.orekit.files.ccsds.ndm.AbstractBuilder`
        
            Parameters:
                newConventions (:class:`~org.orekit.utils.IERSConventions`): IERS Conventions
                newDataContext (:class:`~org.orekit.data.DataContext`): used to retrieve frames, time scales, etc.
                newMissionReferenceDate (:class:`~org.orekit.time.AbsoluteDate`): reference date for Mission Elapsed Time or Mission Relative Time time systems
                newRangeUnitsConverter (:class:`~org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter`): converter for :code:`Range Units`
        
            Returns:
                new instance
        
        
        """
        ...
    def finalize(self) -> None: ...
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

_PythonNdmConstituent__H = typing.TypeVar('_PythonNdmConstituent__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_PythonNdmConstituent__S = typing.TypeVar('_PythonNdmConstituent__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
class PythonNdmConstituent(NdmConstituent[_PythonNdmConstituent__H, _PythonNdmConstituent__S], typing.Generic[_PythonNdmConstituent__H, _PythonNdmConstituent__S]):
    """
    public class PythonNdmConstituent<H extends :class:`~org.orekit.files.ccsds.section.Header`,S extends :class:`~org.orekit.files.ccsds.section.Segment`<?,?>> extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<H,S>
    """
    def finalize(self) -> None: ...
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
            Get IERS conventions.
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getConventions`Â in
                classÂ :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`
        
            Returns:
                IERS conventions
        
        
        """
        ...
    def getDataContext(self) -> org.orekit.data.DataContext:
        """
            Get the data context.
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getDataContext`Â in
                classÂ :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`
        
            Returns:
                the data context used for creating frames, time scales, etc.
        
        
        """
        ...
    def getHeader(self) -> _PythonNdmConstituent__H:
        """
            Get the header.
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`
        
            Returns:
                header
        
            Since:
                11.0
        
        
        """
        ...
    def getSegments(self) -> java.util.List[_PythonNdmConstituent__S]: ...
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
    def validate(self) -> None:
        """
            Validate the file message for required and forbidden entries.
        
            This method throws an exception if file does not meet format requirements. The requirements may depend on format
            version, which is found in header.
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`
        
        
        """
        ...

class WriterBuilder(AbstractBuilder['WriterBuilder']):
    """
    public class WriterBuilder extends :class:`~org.orekit.files.ccsds.ndm.AbstractBuilder`<:class:`~org.orekit.files.ccsds.ndm.WriterBuilder`>
    
        Builder for all :class:`~org.orekit.files.ccsds.ndm.NdmConstituent` files writers.
    
        This builder can be used for building all CCSDS Messages writers types. It is particularly useful in multi-threaded
        context as writers cannot be shared between threads and thus several independent writers must be built in this case.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def buildAemWriter(self) -> org.orekit.files.ccsds.ndm.adm.aem.AemWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.adm.aem.Aem`.
        
            Returns:
                a new writer
        
        
        """
        ...
    def buildApmWriter(self) -> org.orekit.files.ccsds.ndm.adm.apm.ApmWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.adm.apm.Apm`.
        
            Returns:
                a new writer
        
        
        """
        ...
    def buildNdmWriter(self) -> NdmWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.Ndm`.
        
            Returns:
                a new writer
        
        
        """
        ...
    def buildOcmWriter(self) -> org.orekit.files.ccsds.ndm.odm.ocm.OcmWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
        
            Returns:
                a new writer
        
        
        """
        ...
    def buildOemWriter(self) -> org.orekit.files.ccsds.ndm.odm.oem.OemWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.odm.oem.Oem`.
        
            Returns:
                a new writer
        
        
        """
        ...
    def buildOmmWriter(self) -> org.orekit.files.ccsds.ndm.odm.omm.OmmWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.odm.omm.Omm`.
        
            Returns:
                a new writer
        
        
        """
        ...
    def buildOpmWriter(self) -> org.orekit.files.ccsds.ndm.odm.opm.OpmWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.odm.opm.Opm`.
        
            Returns:
                a new writer
        
        
        """
        ...
    def buildTdmWriter(self) -> org.orekit.files.ccsds.ndm.tdm.TdmWriter:
        """
            Build a writer for :class:`~org.orekit.files.ccsds.ndm.tdm.Tdm`.
        
            Returns:
                a new writer
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm")``.

    AbstractBuilder: typing.Type[AbstractBuilder]
    Ndm: typing.Type[Ndm]
    NdmConstituent: typing.Type[NdmConstituent]
    NdmParser: typing.Type[NdmParser]
    NdmWriter: typing.Type[NdmWriter]
    ParsedUnitsBehavior: typing.Type[ParsedUnitsBehavior]
    ParserBuilder: typing.Type[ParserBuilder]
    PythonAbstractBuilder: typing.Type[PythonAbstractBuilder]
    PythonNdmConstituent: typing.Type[PythonNdmConstituent]
    WriterBuilder: typing.Type[WriterBuilder]
    adm: org.orekit.files.ccsds.ndm.adm.__module_protocol__
    odm: org.orekit.files.ccsds.ndm.odm.__module_protocol__
    tdm: org.orekit.files.ccsds.ndm.tdm.__module_protocol__
