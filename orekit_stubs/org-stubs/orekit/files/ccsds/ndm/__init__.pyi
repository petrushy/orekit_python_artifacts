
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.hipparchus.complex
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm.adm
import org.orekit.files.ccsds.ndm.adm.acm
import org.orekit.files.ccsds.ndm.adm.aem
import org.orekit.files.ccsds.ndm.adm.apm
import org.orekit.files.ccsds.ndm.cdm
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
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



_AbstractBuilder__T = typing.TypeVar('_AbstractBuilder__T', bound='AbstractBuilder')  # <T>
class AbstractBuilder(typing.Generic[_AbstractBuilder__T]):
    """
    Abstract builder for all NdmConstituent files parsers/writers.
    
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
    def getEquatorialRadius(self) -> float:
        """
        Get the central body equatorial radius.
        
        Returns:
            central body equatorial radius
        
        
        """
        ...
    def getFlattening(self) -> float:
        """
        Get the central body flattening.
        
        Returns:
            central body flattening
        
        
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
        Get the converter for RU.
        
        Returns:
            converter for RU
        
        
        """
        ...
    def withConventions(self, newConventions: org.orekit.utils.IERSConventions) -> _AbstractBuilder__T:
        """
        Set up IERS conventions.
        
        Parameters:
            newConventions (IERSConventions): IERS Conventions
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withDataContext(self, newDataContext: org.orekit.data.DataContext) -> _AbstractBuilder__T:
        """
        Set up data context used to retrieve frames, time scales, etc..
        
        Parameters:
            newDataContext (DataContext): data context used to retrieve frames, time scales, etc.
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withEquatorialRadius(self, newEquatorialRadius: float) -> _AbstractBuilder__T:
        """
        Set up the central body equatorial radius.
        
        Parameters:
            newEquatorialRadius (double): central body equatorial radius
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withFlattening(self, newFlattening: float) -> _AbstractBuilder__T:
        """
        Set up the central body flattening.
        
        Parameters:
            newFlattening (double): central body flattening
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withMissionReferenceDate(self, newMissionReferenceDate: org.orekit.time.AbsoluteDate) -> _AbstractBuilder__T:
        """
        Set up mission reference date or Mission Elapsed Time or Mission Relative Time time systems.
        
        The mission reference date is used only by AemParser and ApmParser, and by OpmParser, OmmParser and OemParser up to version 2.0 of ODM (starting with version 3.0 of ODM, both MET and MRT time system have been withdrawn from the standard).
        
        Parameters:
            newMissionReferenceDate (AbsoluteDate): mission reference date or Mission Elapsed Time or Mission Relative Time time systems
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withRangeUnitsConverter(self, newRangeUnitsConverter: org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter) -> _AbstractBuilder__T:
        """
        Set up the converter for RU.
        
        Parameters:
            newRangeUnitsConverter (RangeUnitsConverter): converter for RU
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...

class CommonPhysicalProperties(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for common physical properties for both OrbitPhysicalProperties and AdditionalParameters.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        11.3
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def getFrameMapper(self) -> org.orekit.files.ccsds.definitions.CcsdsFrameMapper:
        """
        Get the mapping between a CCSDS frame and a Frame.
        
        Returns:
            the frame mapper.
        
        Since:
            13.1.5
        
        
        """
        ...
    def getMaxRcs(self) -> float:
        """
        Get the maximum radar cross-section.
        
        Returns:
            maximum radar cross-section
        
        
        """
        ...
    def getMinRcs(self) -> float:
        """
        Get the minimum radar cross-section.
        
        Returns:
            minimum radar cross-section
        
        
        """
        ...
    def getOebAreaAlongIntermediate(self) -> float:
        """
        Get the cross-sectional area of Optimally Enclosing Box when viewed along the intermediate OEB direction.
        
        Returns:
            cross-sectional area of Optimally Enclosing Box when viewed along the intermediate OEB direction.
        
        
        """
        ...
    def getOebAreaAlongMax(self) -> float:
        """
        Get the cross-sectional area of Optimally Enclosing Box when viewed along the maximum OEB direction.
        
        Returns:
            cross-sectional area of Optimally Enclosing Box when viewed along the maximum OEB direction.
        
        
        """
        ...
    def getOebAreaAlongMin(self) -> float:
        """
        Get the cross-sectional area of Optimally Enclosing Box when viewed along the minimum OEB direction.
        
        Returns:
            cross-sectional area of Optimally Enclosing Box when viewed along the minimum OEB direction.
        
        
        """
        ...
    def getOebIntermediate(self) -> float:
        """
        Get the intermediate physical dimension of the OEB.
        
        Returns:
            intermediate physical dimension of the OEB.
        
        
        """
        ...
    def getOebMax(self) -> float:
        """
        Get the maximum physical dimension of the OEB.
        
        Returns:
            maximum physical dimension of the OEB.
        
        
        """
        ...
    def getOebMin(self) -> float:
        """
        Get the minimum physical dimension of the OEB.
        
        Returns:
            dimensions the minimum physical dimension of the OEB.
        
        
        """
        ...
    def getOebParent(self) -> org.orekit.frames.Frame:
        """
        Get the frame OEB parent frame. Note that only the orientation of the returned frame is significant, the position of the returned frame is irrelevant and should be ignored.
        
        Returns:
            Orekit frame for this covariance history.
        
        Since:
            13.1.5
        
        Also see:
            getOebParentFrame,
            getOebParentFrameEpoch,
            getFrameMapper
        
        
        """
        ...
    def getOebParentFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get the Optimally Enclosing Box parent reference frame.
        
        Returns:
            Optimally Enclosing Box parent reference frame
        
        
        """
        ...
    def getOebParentFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the Optimally Enclosing Box parent reference frame epoch.
        
        Returns:
            Optimally Enclosing Box parent reference frame epoch
        
        
        """
        ...
    def getOebQ(self) -> org.hipparchus.complex.Quaternion:
        """
        Get the quaternion defining Optimally Enclosing Box.
        
        Returns:
            quaternion defining Optimally Enclosing Box
        
        
        """
        ...
    def getRcs(self) -> float:
        """
        Get the typical (50th percentile) radar cross-section.
        
        Returns:
            typical (50th percentile) radar cross-section
        
        
        """
        ...
    def getReflectance(self) -> float:
        """
        Get the typical (50th percentile) coefficient of reflectance.
        
        Returns:
            typical (50th percentile) coefficient of reflectance
        
        
        """
        ...
    def getVmAbsolute(self) -> float:
        """
        Get the typical (50th percentile) visual magnitude.
        
        Returns:
            typical (50th percentile) visual magnitude
        
        
        """
        ...
    def getVmApparent(self) -> float:
        """
        Get the typical (50th percentile) apparent visual magnitude.
        
        Returns:
            typical (50th percentile) apparent visual magnitude
        
        
        """
        ...
    def getVmApparentMax(self) -> float:
        """
        Get the maximum apparent visual magnitude.
        
        Returns:
            maximum apparent visual magnitude
        
        
        """
        ...
    def getVmApparentMin(self) -> float:
        """
        Get the minimum apparent visual magnitude.
        
        Returns:
            minimum apparent visual magnitude
        
        
        """
        ...
    def setMaxRcs(self, maxRcs: float) -> None:
        """
        Set the maximum radar cross-section.
        
        Parameters:
            maxRcs (double): maximum radar cross-section
        
        
        """
        ...
    def setMinRcs(self, minRcs: float) -> None:
        """
        Set the minimum radar cross-section.
        
        Parameters:
            minRcs (double): minimum radar cross-section
        
        
        """
        ...
    def setOebAreaAlongIntermediate(self, oebAreaAlongIntermediate: float) -> None:
        """
        Set the cross-sectional area of Optimally Enclosing Box when viewed along the intermediate OEB direction.
        
        Parameters:
            oebAreaAlongIntermediate (double): cross-sectional area of Optimally Enclosing Box when viewed along the intermediate OEB direction.
        
        
        """
        ...
    def setOebAreaAlongMax(self, oebAreaAlongMax: float) -> None:
        """
        Set the cross-sectional area of Optimally Enclosing Box when viewed along the maximum OEB direction.
        
        Parameters:
            oebAreaAlongMax (double): cross-sectional area of Optimally Enclosing Box when viewed along the maximum OEB direction.
        
        
        """
        ...
    def setOebAreaAlongMin(self, oebAreaAlongMin: float) -> None:
        """
        Set the cross-sectional area of Optimally Enclosing Box when viewed along the minimum OEB direction.
        
        Parameters:
            oebAreaAlongMin (double): cross-sectional area of Optimally Enclosing Box when viewed along the minimum OEB direction.
        
        
        """
        ...
    def setOebIntermediate(self, oebIntermediate: float) -> None:
        """
        Set the intermediate physical dimension of the OEB.
        
        Parameters:
            oebIntermediate (double): intermediate physical dimension of the OEB.
        
        
        """
        ...
    def setOebMax(self, oebMax: float) -> None:
        """
        Set the maximum physical dimension of the OEB.
        
        Parameters:
            oebMax (double): maximum physical dimension of the OEB.
        
        
        """
        ...
    def setOebMin(self, oebMin: float) -> None:
        """
        Set the minimum physical dimension of the OEB.
        
        Parameters:
            oebMin (double): the minimum physical dimension of the OEB.
        
        
        """
        ...
    def setOebParentFrame(self, oebParentFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set the Optimally Enclosing Box parent reference frame.
        
        Parameters:
            oebParentFrame (FrameFacade): Optimally Enclosing Box parent reference frame
        
        
        """
        ...
    def setOebParentFrameEpoch(self, oebParentFrameEpoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the Optimally Enclosing Box parent reference frame epoch.
        
        Parameters:
            oebParentFrameEpoch (AbsoluteDate): Optimally Enclosing Box parent reference frame epoch
        
        
        """
        ...
    def setOebQ(self, i: int, qI: float) -> None:
        """
        set the component of quaternion defining Optimally Enclosing Box.
        
        Parameters:
            i (int): index of the component
            qI (double): component of quaternion defining Optimally Enclosing Box
        
        
        """
        ...
    def setRcs(self, rcs: float) -> None:
        """
        Set the typical (50th percentile) radar cross-section.
        
        Parameters:
            rcs (double): typical (50th percentile) radar cross-section
        
        
        """
        ...
    def setReflectance(self, reflectance: float) -> None:
        """
        Set the typical (50th percentile) coefficient of reflectance.
        
        Parameters:
            reflectance (double): typical (50th percentile) coefficient of reflectance
        
        
        """
        ...
    def setVmAbsolute(self, vmAbsolute: float) -> None:
        """
        Set the typical (50th percentile) visual magnitude.
        
        Parameters:
            vmAbsolute (double): typical (50th percentile) visual magnitude
        
        
        """
        ...
    def setVmApparent(self, vmApparent: float) -> None:
        """
        Set the typical (50th percentile) apparent visual magnitude.
        
        Parameters:
            vmApparent (double): typical (50th percentile) apparent visual magnitude
        
        
        """
        ...
    def setVmApparentMax(self, vmApparentMax: float) -> None:
        """
        Set the maximum apparent visual magnitude.
        
        Parameters:
            vmApparentMax (double): maximum apparent visual magnitude
        
        
        """
        ...
    def setVmApparentMin(self, vmApparentMin: float) -> None:
        """
        Set the minimum apparent visual magnitude.
        
        Parameters:
            vmApparentMin (double): minimum apparent visual magnitude
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommentsContainer
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class Ndm:
    """
    CCSDS Navigation Data Message. This class is a container for comments and NdmConstituent.
    
    Since:
        11.0
    """
    def __init__(self, comments: java.util.List[str], constituents: java.util.List['NdmConstituent'[typing.Any, typing.Any]]):
        """
        Simple constructor.
        
        Parameters:
            comments (List<String> comments): file comments
            constituents (List<NdmConstituent<?, ?>>): constituents of the message
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]:
        """
        Get an unmodifiable view of the comments.
        
        Returns:
            unmodifiable view of the comment
        
        
        """
        ...
    def getConstituents(self) -> java.util.List['NdmConstituent'[typing.Any, typing.Any]]:
        """
        Get an unmodifiable view of the constituents.
        
        Returns:
            unmodifiable view of the constituents
        
        
        """
        ...

_NdmConstituent__H = typing.TypeVar('_NdmConstituent__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_NdmConstituent__S = typing.TypeVar('_NdmConstituent__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
class NdmConstituent(typing.Generic[_NdmConstituent__H, _NdmConstituent__S]):
    """
    Constituents of a CCSDS Navigation Data Message. Constituents may be Attitude Data Message (ADM), Orbit Data Message (ODM), Tracking Data Message (TDM)… Each constituent has its own header and a list of segments.
    
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
    def getSegments(self) -> java.util.List[_NdmConstituent__S]:
        """
        Get the segments.
        
        Returns:
            segments
        
        Since:
            11.0
        
        
        """
        ...
    def setHeader(self, header: _NdmConstituent__H) -> None:
        """
        Set the header.
        
        Parameters:
            header (NdmConstituent): the header
        
        
        """
        ...
    def setSegments(self, segments: java.util.List[_NdmConstituent__S]) -> None:
        """
        Set the segments.
        
        Parameters:
            segments (List<NdmConstituent> segments): the segments
        
        
        """
        ...
    def validate(self) -> None:
        """
        Validate the file message for required and forbidden entries.
        
        This method throws an exception if file does not meet format requirements. The requirements may depend on format version, which is found in header.
        """
        ...

class NdmParser(org.orekit.files.ccsds.utils.parsing.AbstractMessageParser[Ndm]):
    """
    A parser for the CCSDS NDM (Navigation Data Message).
    
    Since:
        11.0
    """
    def __init__(self, builder: 'ParserBuilder', filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]):
        """
        Simple constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildNdmParser.
        
        Parameters:
            builder (ParserBuilder): builder for the constituents parsers
            filters (Function<ParseToken, List<ParseToken>>[]): filters to apply to parse tokens
        
        Since:
            12.0
        
        
        """
        ...
    def addComment(self, comment: str) -> bool:
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
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]:
        """
        Get the non-default token builders for special XML elements.
        
        Specified by: getSpecialXmlElementsBuilders in interface MessageParser
        
        Overrides: getSpecialXmlElementsBuilders in class AbstractMessageParser
        
        Returns:
            map of token builders for special XML elements (keyed by XML element name)
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
        Reset parser to initial state before parsing.
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...

class NdmWriter:
    """
    Writer for CCSDS Navigation Data Message.
    
    Since:
        11.0
    """
    def __init__(self, builder: 'WriterBuilder'):
        """
        Simple constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildNdmWriter.
        
        Parameters:
            builder (WriterBuilder): builder for the constituents parsers
        
        
        """
        ...
    def writeComment(self, generator: org.orekit.files.ccsds.utils.generation.Generator, comment: str) -> None:
        """
        Write a comment line.
        
        Comments allows comments only before constituents, so attempting to add comments after the first constituent has been written will produce an exception.
        
        Parameters:
            generator (Generator): generator to use for producing output
            comment (String): comment line to write
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    _writeConstituent__H = typing.TypeVar('_writeConstituent__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
    _writeConstituent__S = typing.TypeVar('_writeConstituent__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
    _writeConstituent__F = typing.TypeVar('_writeConstituent__F', bound=NdmConstituent)  # <F>
    def writeConstituent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, constituent: _writeConstituent__F) -> None:
        """
        Write a constituent.
        
        Parameters:
            generator (Generator): generator to use for producing output
            constituent (F): constituent
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeMessage(self, generator: org.orekit.files.ccsds.utils.generation.Generator, message: Ndm) -> None:
        """
        Write one complete message.
        
        Parameters:
            generator (Generator): generator to use for producing output
            message (Ndm): message to write
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...

class ParsedUnitsBehavior(java.lang.Enum['ParsedUnitsBehavior']):
    """
    Behavior adopted for units that have been parsed from a CCSDS message.
    
    Since:
        11.0
    """
    IGNORE_PARSED: typing.ClassVar['ParsedUnitsBehavior'] = ...
    CONVERT_COMPATIBLE: typing.ClassVar['ParsedUnitsBehavior'] = ...
    STRICT_COMPLIANCE: typing.ClassVar['ParsedUnitsBehavior'] = ...
    def select(self, message: org.orekit.utils.units.Unit, standard: org.orekit.utils.units.Unit) -> org.orekit.utils.units.Unit:
        """
        Select the unit to use for interpreting parsed value.
        
        Parameters:
            message (Unit): unit parsed in the CCSDS message
            standard (Unit): unit mandated by the standard
        
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
    def valueOf(name: str) -> 'ParsedUnitsBehavior':
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
    def values() -> typing.MutableSequence['ParsedUnitsBehavior']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ParsedUnitsBehavior c : ParsedUnitsBehavior.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ParserBuilder(AbstractBuilder['ParserBuilder']):
    """
    Builder for all NdmConstituent files parsers.
    
    This builder can be used for building all CCSDS Messages parsers types. It is particularly useful in multi-threaded context as parsers cannot be shared between threads and thus several independent parsers must be built in this case.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def buildAcmParser(self) -> org.orekit.files.ccsds.ndm.adm.acm.AcmParser:
        """
        Build a parser for Acm.
        
        Returns:
            a new parser
        
        Since:
            12.0
        
        
        """
        ...
    def buildAemParser(self) -> org.orekit.files.ccsds.ndm.adm.aem.AemParser:
        """
        Build a parser for Aem.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildApmParser(self) -> org.orekit.files.ccsds.ndm.adm.apm.ApmParser:
        """
        Build a parser for Apm.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildCdmParser(self) -> org.orekit.files.ccsds.ndm.cdm.CdmParser:
        """
        Build a parser for Cdm.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildNdmParser(self) -> NdmParser:
        """
        Build a parser for Ndm.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildOcmParser(self) -> org.orekit.files.ccsds.ndm.odm.ocm.OcmParser:
        """
        Build a parser for Ocm.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildOemParser(self) -> org.orekit.files.ccsds.ndm.odm.oem.OemParser:
        """
        Build a parser for Oem.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildOmmParser(self) -> org.orekit.files.ccsds.ndm.odm.omm.OmmParser:
        """
        Build a parser for Omm.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildOpmParser(self) -> org.orekit.files.ccsds.ndm.odm.opm.OpmParser:
        """
        Build a parser for Opm.
        
        Returns:
            a new parser
        
        
        """
        ...
    def buildTdmParser(self) -> org.orekit.files.ccsds.ndm.tdm.TdmParser:
        """
        Build a parser for Tdm.
        
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
    def getFilters(self) -> typing.MutableSequence[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]]:
        """
        Get the filters to apply to parse tokens.
        
        Returns:
            filters to apply to parse tokens
        
        Since:
            12.0
        
        
        """
        ...
    def getFrameMapper(self) -> org.orekit.files.ccsds.definitions.CcsdsFrameMapper:
        """
        Get the mapping between CCSDS NDM center and frame and a Frame.
        
        Returns:
            the frame mapper.
        
        Since:
            13.1.5
        
        
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
    def withDefaultInterpolationDegree(self, newDefaultInterpolationDegree: int) -> 'ParserBuilder':
        """
        Set up the default interpolation degree.
        
        The default interpolation degree is used only by AemParser and OemParser.
        
        Parameters:
            newDefaultInterpolationDegree (int): default interpolation degree
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withDefaultMass(self, newDefaultMass: float) -> 'ParserBuilder':
        """
        Set up the default mass.
        
        The default mass is used only by OpmParser.
        
        Parameters:
            newDefaultMass (double): default mass
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withFilter(self, filter: typing.Union[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]], typing.Callable[[org.orekit.files.ccsds.utils.lexical.ParseToken], java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]]) -> 'ParserBuilder':
        """
        Add a filter for parsed tokens.
        
        This filter allows to change parsed tokens. This method can be called several times, once for each filter to set up. The filters are always applied in the order they were set. There are several use cases for this feature.
        
        The first use case is to allow parsing malformed CCSDS messages with some known discrepancies that can be fixed. One real life example (the one that motivated the development of this feature) is OMM files in XML format that add an empty OBJECT_ID. This could be fixed by setting a filter as follows:
        
        
         Omm omm = new ParserBuilder().
                   withFilter(token -> {
                                  if ("OBJECT_ID".equals(token.getName()) &&amp;
                                      (token.getRawContent() == null || token.getRawContent().isEmpty())) {
                                      // replace null/empty entries with "unknown"
                                      return Collections.singletonList(new ParseToken(token.getType(), token.getName(),
                                                                                      "unknown", token.getUnits(),
                                                                                      token.getLineNumber(), token.getFileName()));
                                  } else {
                                      return Collections.singletonList(token);
                                  }
                             }).
                   buildOmmParser().
                   parseMessage(message);
         
        
        A second use case is to remove unwanted data. For example in order to remove all user-defined data one could use:
        
        
         Omm omm = new ParserBuilder().
                   withFilter(token -> {
                                  if (token.getName().startsWith("USER_DEFINED")) {
                                      return Collections.emptyList();
                                  } else {
                                      return Collections.singletonList(token);
                                  }
                             }).
                   buildOmmmParser().
                   parseMessage(message);
         
        
        A third use case is to add data not originally present in the file. For example in order to add a generated ODM V3 message id to an ODM V2 message that lacks it, one could do:
        
        
         final String myMessageId = ...; // this could be computed from a counter, or a SHA256 digest, or some metadata
         Omm omm = new ParserBuilder()
                   withFilter(token -> {
                                  if ("CCSDS_OMM_VERS".equals(token.getName())) {
                                      // enforce ODM V3
                                      return Collections.singletonList(new ParseToken(token.getType(), token.getName(),
                                                                                      "3.0", token.getUnits(),
                                                                                      token.getLineNumber(), token.getFileName()));
                                  } else {
                                      return Collections.singletonList(token);
                                  }
                              }).
                   withFilter(token -> {
                                  if ("ORIGINATOR".equals(token.getName())) {
                                      // add generated message ID after ORIGINATOR entry
                                      return Arrays.asList(token,
                                                           new ParseToken(TokenType.ENTRY, "MESSAGE_ID",
                                                                          myMessageId, null,
                                                                          -1, token.getFileName()));
                                  } else {
                                      return Collections.singletonList(token);
                                  }
                              }).
                   buildOmmmParser().
                   parseMessage(message);
         
        
        Parameters:
            filter (Function<ParseToken, List<ParseToken>>): token filter to add
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        Since:
            12.0
        
        
        """
        ...
    def withFrameMapper(self, newFrameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper) -> 'ParserBuilder':
        """
        Set the mapping between CCSDS NDM center and frame and a Frame.
        
        Parameters:
            newFrameMapper (CcsdsFrameMapper): the frame mapper.
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        Since:
            13.1.5
        
        
        """
        ...
    def withMu(self, newMu: float) -> 'ParserBuilder':
        """
        Set up the gravitational coefficient.
        
        Parameters:
            newMu (double): gravitational coefficient
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withParsedUnitsBehavior(self, newParsedUnitsBehavior: ParsedUnitsBehavior) -> 'ParserBuilder':
        """
        Set up the behavior to adopt for handling parsed units.
        
        Parameters:
            newParsedUnitsBehavior (ParsedUnitsBehavior): behavior to adopt for handling parsed units
        
        Returns:
            a new builder with updated configuration (the instance is not changed)
        
        
        """
        ...
    def withSimpleEOP(self, newSimpleEOP: bool) -> 'ParserBuilder':
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
    def __init__(self, conventions: org.orekit.utils.IERSConventions, equatorialRadius: float, flattening: float, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate, rangeUnitsConverter: org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter):
        """
        Complete constructor.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            dataContext (double): used to retrieve frames, time scales, etc.
            missionReferenceDate (double): reference date for Mission Elapsed Time or Mission Relative Time time systems
            rangeUnitsConverter (DataContext): converter for RU
        
        
        """
        ...
    def create(self, newConventions: org.orekit.utils.IERSConventions, newEquatorialRadius: float, newFlattening: float, newDataContext: org.orekit.data.DataContext, newMissionReferenceDate: org.orekit.time.AbsoluteDate, newRangeUnitsConverter: org.orekit.files.ccsds.ndm.tdm.RangeUnitsConverter) -> _PythonAbstractBuilder__T:
        """
        Build an instance.
        
        Specified by: create in class AbstractBuilder
        
        Parameters:
            newConventions (IERSConventions): IERS Conventions
            newEquatorialRadius (double): central body equatorial radius
            newFlattening (double): central body flattening
            newDataContext (DataContext): used to retrieve frames, time scales, etc.
            newMissionReferenceDate (AbsoluteDate): reference date for Mission Elapsed Time or Mission Relative Time time systems
            newRangeUnitsConverter (RangeUnitsConverter): converter for RU
        
        Returns:
            new instance
        
        
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

_PythonNdmConstituent__H = typing.TypeVar('_PythonNdmConstituent__H', bound=org.orekit.files.ccsds.section.Header)  # <H>
_PythonNdmConstituent__S = typing.TypeVar('_PythonNdmConstituent__S', bound=org.orekit.files.ccsds.section.Segment)  # <S>
class PythonNdmConstituent(NdmConstituent[_PythonNdmConstituent__H, _PythonNdmConstituent__S], typing.Generic[_PythonNdmConstituent__H, _PythonNdmConstituent__S]):
    def __init__(self, header: _PythonNdmConstituent__H, segments: java.util.List[_PythonNdmConstituent__S], conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext):
        """
        Constructor.
        
        Parameters:
            header (PythonNdmConstituent): file header
            segments (List<PythonNdmConstituent> segments): file segments
            conventions (IERSConventions): IERS conventions
            dataContext (DataContext): used for creating frames, time scales, etc.
        
        
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
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
        Get IERS conventions.
        
        Overrides: getConventions in class NdmConstituent
        
        Returns:
            IERS conventions
        
        
        """
        ...
    def getDataContext(self) -> org.orekit.data.DataContext:
        """
        Get the data context.
        
        Overrides: getDataContext in class NdmConstituent
        
        Returns:
            the data context used for creating frames, time scales, etc.
        
        
        """
        ...
    def getHeader(self) -> _PythonNdmConstituent__H:
        """
        Get the header.
        
        Overrides: getHeader in class NdmConstituent
        
        Returns:
            header
        
        Since:
            11.0
        
        
        """
        ...
    def getSegments(self) -> java.util.List[_PythonNdmConstituent__S]:
        """
        Get the segments.
        
        Overrides: getSegments in class NdmConstituent
        
        Returns:
            segments
        
        Since:
            11.0
        
        
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
    def validate(self) -> None:
        """
        Validate the file message for required and forbidden entries.
        
        This method throws an exception if file does not meet format requirements. The requirements may depend on format version, which is found in header.
        
        Overrides: validate in class NdmConstituent
        
        
        """
        ...

class WriterBuilder(AbstractBuilder['WriterBuilder']):
    """
    Builder for all NdmConstituent files writers.
    
    This builder can be used for building all CCSDS Messages writers types. It is particularly useful in multi-threaded context as writers cannot be shared between threads and thus several independent writers must be built in this case.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def buildAcmWriter(self) -> org.orekit.files.ccsds.ndm.adm.acm.AcmWriter:
        """
        Build a writer for Acm.
        
        Returns:
            a new writer
        
        Since:
            12.0
        
        
        """
        ...
    def buildAemWriter(self) -> org.orekit.files.ccsds.ndm.adm.aem.AemWriter:
        """
        Build a writer for Aem.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildApmWriter(self) -> org.orekit.files.ccsds.ndm.adm.apm.ApmWriter:
        """
        Build a writer for Apm.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildCdmWriter(self) -> org.orekit.files.ccsds.ndm.cdm.CdmWriter:
        """
        Build a writer for Cdm.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildNdmWriter(self) -> NdmWriter:
        """
        Build a writer for Ndm.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildOcmWriter(self) -> org.orekit.files.ccsds.ndm.odm.ocm.OcmWriter:
        """
        Build a writer for Ocm.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildOemWriter(self) -> org.orekit.files.ccsds.ndm.odm.oem.OemWriter:
        """
        Build a writer for Oem.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildOmmWriter(self) -> org.orekit.files.ccsds.ndm.odm.omm.OmmWriter:
        """
        Build a writer for Omm.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildOpmWriter(self) -> org.orekit.files.ccsds.ndm.odm.opm.OpmWriter:
        """
        Build a writer for Opm.
        
        Returns:
            a new writer
        
        
        """
        ...
    def buildTdmWriter(self) -> org.orekit.files.ccsds.ndm.tdm.TdmWriter:
        """
        Build a writer for Tdm.
        
        Returns:
            a new writer
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm")``.

    AbstractBuilder: typing.Type[AbstractBuilder]
    CommonPhysicalProperties: typing.Type[CommonPhysicalProperties]
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
    cdm: org.orekit.files.ccsds.ndm.cdm.__module_protocol__
    odm: org.orekit.files.ccsds.ndm.odm.__module_protocol__
    tdm: org.orekit.files.ccsds.ndm.tdm.__module_protocol__
