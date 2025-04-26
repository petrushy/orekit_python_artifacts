
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.orekit.data
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.general
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.sampling
import org.orekit.time
import org.orekit.utils
import typing



class EphemerisOemWriter(org.orekit.files.general.EphemerisFileWriter):
    """
    public class EphemerisOemWriter extends :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFileWriter`
    
        An :class:`~org.orekit.files.general.EphemerisFileWriter` generating :class:`~org.orekit.files.ccsds.ndm.odm.oem.Oem`
        files.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.public.ccsds.org.Pubs.502x0b2c1.pdf`,
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.public.ccsds.org.Pubs.500x0g4.pdf`,
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.StreamingOemWriter`
    """
    @typing.overload
    def __init__(self, oemWriter: 'OemWriter', odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, oemMetadata: 'OemMetadata', fileFormat: org.orekit.files.ccsds.utils.FileFormat, string: str, double: float, int: int): ...
    @typing.overload
    def __init__(self, oemWriter: 'OemWriter', odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, oemMetadata: 'OemMetadata', fileFormat: org.orekit.files.ccsds.utils.FileFormat, string: str, double: float, int: int, formatter: org.orekit.utils.Formatter): ...
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    @typing.overload
    def write(self, string: str, ephemerisFile: typing.Union[org.orekit.files.general.EphemerisFile[_write_0__C, _write_0__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, org.orekit.files.general.EphemerisFile.EphemerisSegment]]]]) -> None: ...
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: typing.Union[org.orekit.files.general.EphemerisFile[_write_1__C, _write_1__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, org.orekit.files.general.EphemerisFile.EphemerisSegment]]]]) -> None: ...
    _writeSegment__C = typing.TypeVar('_writeSegment__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _writeSegment__S = typing.TypeVar('_writeSegment__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    def writeSegment(self, generator: org.orekit.files.ccsds.utils.generation.Generator, s2: _writeSegment__S) -> None: ...

class InterpolationMethod(java.lang.Enum['InterpolationMethod']):
    """
    public enum InterpolationMethod extends :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod`>
    
        OEM interpolation method.
    """
    HERMITE: typing.ClassVar['InterpolationMethod'] = ...
    LAGRANGE: typing.ClassVar['InterpolationMethod'] = ...
    LINEAR: typing.ClassVar['InterpolationMethod'] = ...
    PROPAGATE: typing.ClassVar['InterpolationMethod'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'InterpolationMethod':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['InterpolationMethod']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (InterpolationMethod c : InterpolationMethod.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Oem(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.odm.OdmHeader, 'OemSegment'], org.orekit.files.general.EphemerisFile[org.orekit.utils.TimeStampedPVCoordinates, 'OemSegment']):
    """
    public class Oem extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.odm.OdmHeader`, :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemSegment`> implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`, :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemSegment`>
    
        This class stores all the information of the OEM File parsed by OEMParser.
    
        It contains the header and a list of Ephemerides Blocks each containing metadata, a list of ephemerides data lines and
        optional covariance matrices (and their metadata).
    
        Since:
            6.1
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ROOT
    
        Root element for XML files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` FORMAT_VERSION_KEY
    
        Key for format version.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, list: java.util.List['OemSegment'], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, double: float): ...
    def checkTimeSystems(self) -> None:
        """
            Check that, according to the CCSDS standard, every OEMBlock has the same time system.
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OemSatelliteEphemeris']: ...

class OemData(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    public class OemData extends :class:`~org.orekit.files.ccsds.section.CommentsContainer` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        The Ephemerides data blocks class contain list of orbital data points.
    
        Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these
        SI units into CCSDS mandatory units. The :class:`~org.orekit.utils.units.Unit` class provides useful
        :meth:`~org.orekit.utils.units.Unit.fromSI` and :meth:`~org.orekit.utils.units.Unit.toSI` methods in case the callers
        already use CCSDS units instead of the API SI units. The general-purpose :class:`~org.orekit.utils.units.Unit` class
        (without an 's') and the CCSDS-specific :class:`~org.orekit.files.ccsds.definitions.Units` class (with an 's') also
        provide some predefined units. These predefined units and the :meth:`~org.orekit.utils.units.Unit.fromSI` and
        :meth:`~org.orekit.utils.units.Unit.toSI` conversion methods are indeed what the parsers and writers use for the
        conversions.
    """
    def __init__(self): ...
    def addCovarianceMatrix(self, cartesianCovariance: org.orekit.files.ccsds.ndm.odm.CartesianCovariance) -> None:
        """
            Add a covariance matrix.
        
            Parameters:
                covarianceMatrix (:class:`~org.orekit.files.ccsds.ndm.odm.CartesianCovariance`): covariance matrix to dd
        
        
        """
        ...
    def addData(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, boolean: bool) -> bool:
        """
            Add a data point.
        
            Parameters:
                data (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): data point to add
                hasAcceleration (boolean): true if the current data point has acceleration data.
        
            Returns:
                always return :code:`true`
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get the derivatives available in the block.
        
            Returns:
                derivatives available in the block
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]: ...
    def getCovarianceMatrices(self) -> java.util.List[org.orekit.files.ccsds.ndm.odm.CartesianCovariance]: ...
    def getEphemeridesDataLines(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]: ...

class OemMetadata(org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata):
    """
    public class OemMetadata extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata`
    
        Metadata for Orbit Ephemeris Messages.
    
        Since:
            11.0
    """
    def __init__(self, int: int): ...
    def getInterpolationDegree(self) -> int:
        """
            Get the interpolation degree.
        
            Returns:
                the interpolation degree
        
        
        """
        ...
    def getInterpolationMethod(self) -> InterpolationMethod:
        """
            Get the interpolation method to be used.
        
            Returns:
                the interpolation method
        
        
        """
        ...
    def getStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start of total time span covered by ephemerides data and covariance data.
        
            Returns:
                the start time
        
        
        """
        ...
    def getStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get end of total time span covered by ephemerides data and covariance data.
        
            Returns:
                the stop time
        
        
        """
        ...
    def getUseableStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Returns:
                the useable start time
        
        
        """
        ...
    def getUseableStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get end of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Returns:
                the useable stop time
        
        
        """
        ...
    def setInterpolationDegree(self, int: int) -> None:
        """
            Set the interpolation degree.
        
            Parameters:
                interpolationDegree (int): the interpolation degree to be set
        
        
        """
        ...
    def setInterpolationMethod(self, interpolationMethod: InterpolationMethod) -> None:
        """
            Set the interpolation method to be used.
        
            Parameters:
                interpolationMethod (:class:`~org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod`): the interpolation method to be set
        
        
        """
        ...
    def setStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set start of total time span covered by ephemerides data and covariance data.
        
            Parameters:
                startTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def setStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set end of total time span covered by ephemerides data and covariance data.
        
            Parameters:
                stopTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def setUseableStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set start of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Parameters:
                useableStartTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def setUseableStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set end of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
            Parameters:
                useableStopTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata.validate` in
                class :class:`~org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class OemMetadataKey(java.lang.Enum['OemMetadataKey']):
    """
    public enum OemMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.odm.oem.OemMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemMetadata` entries.
    
        Since:
            11.0
    """
    START_TIME: typing.ClassVar['OemMetadataKey'] = ...
    STOP_TIME: typing.ClassVar['OemMetadataKey'] = ...
    USEABLE_START_TIME: typing.ClassVar['OemMetadataKey'] = ...
    USEABLE_STOP_TIME: typing.ClassVar['OemMetadataKey'] = ...
    INTERPOLATION: typing.ClassVar['OemMetadataKey'] = ...
    INTERPOLATION_DEGREE: typing.ClassVar['OemMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, oemMetadata: OemMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.oem.OemMetadata`): container to fill
        
            Returns:
                true of token was accepted
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OemMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['OemMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OemMetadataKey c : OemMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OemParser(org.orekit.files.ccsds.ndm.odm.OdmParser[Oem, 'OemParser'], org.orekit.files.general.EphemerisFileParser[Oem]):
    """
    public class OemParser extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmParser`<:class:`~org.orekit.files.ccsds.ndm.odm.oem.Oem`, :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemParser`> implements :class:`~org.orekit.files.general.EphemerisFileParser`<:class:`~org.orekit.files.ccsds.ndm.odm.oem.Oem`>
    
        A parser for the CCSDS OEM (Orbit Ephemeris Message).
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            6.1
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate, double: float, int: int, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, functionArray: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
    def build(self) -> Oem:
        """
            Build the file from parsed entries.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.build` in
                interface :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Returns:
                parsed file
        
        
        """
        ...
    def finalizeData(self) -> bool:
        """
            Finalize data after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeData` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
            Finalize header after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
            Finalize metadata after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeMetadata` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def getHeader(self) -> org.orekit.files.ccsds.ndm.odm.OdmHeader:
        """
            Get file header to fill.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.getHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                file header to fill
        
        
        """
        ...
    def inData(self) -> bool:
        """
            Acknowledge data parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inData` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
            Acknowledge header parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
            Acknowledge metada parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inMetadata` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def parse(self, dataSource: org.orekit.data.DataSource) -> Oem:
        """
            Parse an ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFileParser.parse` in
                interface :class:`~org.orekit.files.general.EphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed ephemeris file.
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
            Prepare data for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareData` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
            Prepare header for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareHeader` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
            Prepare metadata for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareMetadata` in
                class :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.reset` in
                interface :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class OemSatelliteEphemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, 'OemSegment']):
    """
    public class OemSatelliteEphemeris extends :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`, :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemSegment`>
    
        OEM ephemeris blocks for a single satellite.
    
        Since:
            11.0
    """
    def __init__(self, string: str, double: float, list: java.util.List['OemSegment']): ...
    def getId(self) -> str:
        """
            Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getId` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the satellite's ID, never :code:`null`.
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getMu` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getPropagator`, in
                m³/s².
        
        
        """
        ...
    def getSegments(self) -> java.util.List['OemSegment']: ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStart` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStop` in
                interface :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris end date.
        
        
        """
        ...

class OemSegment(org.orekit.files.ccsds.section.Segment[OemMetadata, OemData], org.orekit.files.general.EphemerisFile.EphemerisSegment[org.orekit.utils.TimeStampedPVCoordinates]):
    """
    public class OemSegment extends :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.odm.oem.OemMetadata`, :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemData`> implements :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`>
    
        The Ephemerides Blocks class contain metadata, the list of ephemerides data lines and optional covariance matrices (and
        their metadata). The reason for which the ephemerides have been separated into blocks is that the ephemerides of two
        different blocks are not suited for interpolation.
    """
    def __init__(self, oemMetadata: OemMetadata, oemData: OemData, double: float): ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get which derivatives of position are available in this ephemeris segment.
        
            While :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates` always returns position, velocity,
            and acceleration the return value from this method indicates which of those are in the ephemeris file and are actually
            valid.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getAvailableDerivatives` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                a value indicating if the file contains velocity and/or acceleration data.
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]: ...
    def getCovarianceMatrices(self) -> java.util.List[org.orekit.files.ccsds.ndm.odm.CartesianCovariance]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame for this ephemeris segment. The defining frame for
            :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the reference frame for this segment. Never :code:`null`.
        
        
        """
        ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
            Get the inertial reference frame for this ephemeris segment. Defines the propagation frame for
            :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getPropagator`.
        
            The default implementation returns :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame` if it is
            inertial. Otherwise it returns :meth:`~org.orekit.frames.Frame.getRoot`. Implementors are encouraged to override this
            default implementation if a more suitable inertial frame is available.
        
            This implementation returns :meth:`~org.orekit.files.ccsds.ndm.odm.oem.OemSegment.getFrame` if it is
            :meth:`~org.orekit.frames.Frame.isPseudoInertial`, or its closest :meth:`~org.orekit.frames.Frame.getParent` that is
            pseudo-inertial.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getInertialFrame` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                an reference frame that is inertial, i.e. :meth:`~org.orekit.frames.Frame.isPseudoInertial` is :code:`true`. May be the
                same as :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame` if it is inertial.
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of samples to use in interpolation.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getInterpolationSamples` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the number of points to use for interpolation.
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getMu` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getPropagator`, in
                m³/s².
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStart` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStop` in
                interface :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment end date.
        
        
        """
        ...

class OemWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.odm.OdmHeader, OemSegment, Oem]):
    """
    public class OemWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.ndm.odm.OdmHeader`, :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemSegment`, :class:`~org.orekit.files.ccsds.ndm.odm.oem.Oem`>
    
        A writer for Orbit Ephemeris Message (OEM) files.
    
        Metadata
    ----------
    
    
        The OEM metadata used by this writer is described in the following table. Many metadata items are optional or have
        default values so they do not need to be specified. At a minimum the user must supply those values that are required and
        for which no default exits: :meth:`~org.orekit.files.ccsds.ndm.odm.OdmMetadataKey.OBJECT_NAME`, and
        :meth:`~org.orekit.files.ccsds.ndm.odm.CommonMetadataKey.OBJECT_ID`. The usage column in the table indicates where the
        metadata item is used, either in the OEM header or in the metadata section at the start of an OEM ephemeris segment.
    
        The :meth:`~org.orekit.files.ccsds.section.MetadataKey.TIME_SYSTEM` must be constant for the whole file and is used to
        interpret all dates except :meth:`~org.orekit.files.ccsds.section.HeaderKey.CREATION_DATE` which is always in
        :meth:`~org.orekit.files.ccsds.definitions.TimeSystem.UTC`. The guessing algorithm is not guaranteed to work so it is
        recommended to provide values for :meth:`~org.orekit.files.ccsds.ndm.odm.CommonMetadataKey.CENTER_NAME` and
        :meth:`~org.orekit.files.ccsds.section.MetadataKey.TIME_SYSTEM` to avoid any bugs associated with incorrect guesses.
    
        Standardized values for :meth:`~org.orekit.files.ccsds.section.MetadataKey.TIME_SYSTEM` are GMST, GPS, MET, MRT, SCLK,
        TAI, TCB, TDB, TT, UT1, and UTC. Standardized values for reference frames are EME2000, GTOD, ICRF, ITRF2000, ITRF-93,
        ITRF-97, LVLH, RTN, QSW, TOD, TNW, NTW and RSW. Additionally ITRF followed by a four digit year may be used.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.public.ccsds.org.Pubs.502x0b2c1.pdf`,
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.public.ccsds.org.Pubs.500x0g4.pdf`,
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.StreamingOemWriter`
    """
    CCSDS_OEM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_OEM_VERS
    
        Version number implemented.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_FILE_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` DEFAULT_FILE_NAME
    
        Default file name for error messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    KVN_PADDING_WIDTH: typing.ClassVar[int] = ...
    """
    public static final int KVN_PADDING_WIDTH
    
        Padding width for aligning the '=' sign.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate): ...

class StreamingOemWriter(java.lang.AutoCloseable):
    """
    public class StreamingOemWriter extends :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable?is`
    
        A writer for OEM files.
    
        Each instance corresponds to a single OEM file. A new OEM ephemeris segment is started by calling
        :meth:`~org.orekit.files.ccsds.ndm.odm.oem.StreamingOemWriter.newSegment`.
    
        The segments returned by this class can be used as step handlers for a :class:`~org.orekit.propagation.Propagator`.
    
        .. code-block: java
        
         Propagator propagator = ...; // pre-configured propagator
         OEMWriter  aemWriter  = ...; // pre-configured writer
           try (Generator out = ...;  // set-up output stream
                StreamingOemWriter sw = new StreamingOemWriter(out, oemWriter, header, metadata)) { // set-up streaming writer
        
             // write segment 1
             propagator.getMultiplexer().add(step, sw.newSegment());
             propagator.propagate(startDate1, stopDate1);
        
             ...
        
             // write segment n
             propagator.getMultiplexer().clear();
             propagator.getMultiplexer().add(step, sw.newSegment());
             propagator.propagate(startDateN, stopDateN);
        
           }
         
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.public.ccsds.org.Pubs.502x0b2c1.pdf`,
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.https:.public.ccsds.org.Pubs.500x0g4.pdf`,
            :class:`~org.orekit.files.ccsds.ndm.odm.oem.OemWriter`
    """
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, oemWriter: OemWriter, odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, oemMetadata: OemMetadata): ...
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, oemWriter: OemWriter, odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, oemMetadata: OemMetadata, boolean: bool): ...
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, oemWriter: OemWriter, odmHeader: org.orekit.files.ccsds.ndm.odm.OdmHeader, oemMetadata: OemMetadata, boolean: bool, boolean2: bool): ...
    def close(self) -> None: ...
    def newSegment(self) -> 'StreamingOemWriter.SegmentWriter':
        """
            Create a writer for a new OEM ephemeris segment.
        
            The returned writer can only write a single ephemeris segment in an OEM. This method must be called to create a writer
            for each ephemeris segment.
        
            Returns:
                a new OEM segment writer, ready for use.
        
        
        """
        ...
    class SegmentWriter(org.orekit.propagation.sampling.OrekitFixedStepHandler):
        def __init__(self, streamingOemWriter: 'StreamingOemWriter'): ...
        def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def handleStep(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm.oem")``.

    EphemerisOemWriter: typing.Type[EphemerisOemWriter]
    InterpolationMethod: typing.Type[InterpolationMethod]
    Oem: typing.Type[Oem]
    OemData: typing.Type[OemData]
    OemMetadata: typing.Type[OemMetadata]
    OemMetadataKey: typing.Type[OemMetadataKey]
    OemParser: typing.Type[OemParser]
    OemSatelliteEphemeris: typing.Type[OemSatelliteEphemeris]
    OemSegment: typing.Type[OemSegment]
    OemWriter: typing.Type[OemWriter]
    StreamingOemWriter: typing.Type[StreamingOemWriter]
