
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
import org.orekit.files.ccsds.definitions
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
    An EphemerisFileWriter generating Oem files.
    
    Since:
        9.0
    
    Also see:
        pdf,
        pdf,
        StreamingOemWriter
    """
    @typing.overload
    def __init__(self, writer: 'OemWriter', header: org.orekit.files.ccsds.ndm.odm.OdmHeader, template: 'OemMetadata', fileFormat: org.orekit.files.ccsds.utils.FileFormat, outputName: str, maxRelativeOffset: float, unitsColumn: int): ...
    @typing.overload
    def __init__(self, writer: 'OemWriter', header: org.orekit.files.ccsds.ndm.odm.OdmHeader, template: 'OemMetadata', fileFormat: org.orekit.files.ccsds.utils.FileFormat, outputName: str, maxRelativeOffset: float, unitsColumn: int, formatter: org.orekit.utils.Formatter): ...
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    @typing.overload
    def write(self, appendable: str, ephemerisFile: typing.Union[org.orekit.files.general.EphemerisFile[_write_0__C, _write_0__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, org.orekit.files.general.EphemerisFile.EphemerisSegment]]]]) -> None: ...
    @typing.overload
    def write(self, appendable: java.lang.Appendable, ephemerisFile: typing.Union[org.orekit.files.general.EphemerisFile[_write_1__C, _write_1__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, org.orekit.files.general.EphemerisFile.EphemerisSegment]]]]) -> None: ...
    _writeSegment__C = typing.TypeVar('_writeSegment__C', bound=org.orekit.utils.TimeStampedPVCoordinates)  # <C>
    _writeSegment__S = typing.TypeVar('_writeSegment__S', bound=org.orekit.files.general.EphemerisFile.EphemerisSegment)  # <S>
    def writeSegment(self, generator: org.orekit.files.ccsds.utils.generation.Generator, segment: _writeSegment__S) -> None:
        """
        Write one segment.
        
        Parameters:
            generator (Generator): generator to use for producing output
            segment (S): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class InterpolationMethod(java.lang.Enum['InterpolationMethod']):
    """
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
    def valueOf(name: str) -> 'InterpolationMethod':
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
    def values() -> typing.MutableSequence['InterpolationMethod']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (InterpolationMethod c : InterpolationMethod.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Oem(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.odm.OdmHeader, 'OemSegment'], org.orekit.files.general.EphemerisFile[org.orekit.utils.TimeStampedPVCoordinates, 'OemSegment']):
    """
    This class stores all the information of the OEM File parsed by OEMParser.
    
    It contains the header and a list of Ephemerides Blocks each containing metadata, a list of ephemerides data lines and optional covariance matrices (and their metadata).
    
    Since:
        6.1
    """
    ROOT: typing.ClassVar[str] = ...
    """
    Root element for XML files.
    
    Also see:
        constant
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    Key for format version.
    
    Also see:
        constant
    
    
    """
    def __init__(self, header: org.orekit.files.ccsds.ndm.odm.OdmHeader, segments: java.util.List['OemSegment'], conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, mu: float):
        """
        Simple constructor.
        
        Parameters:
            header (OdmHeader): file header
            segments (List<OemSegment> segments): file segments
            conventions (IERSConventions): IERS conventions
            dataContext (DataContext): used for creating frames, time scales, etc.
            mu (double): gravitational coefficient
        
        
        """
        ...
    def checkTimeSystems(self) -> None:
        """
        Check that, according to the CCSDS standard, every OEMBlock has the same time system.
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OemSatelliteEphemeris']:
        """
        Get the loaded ephemeris for each satellite in the file.
        
        Specified by: getSatellites in interface EphemerisFile
        
        Returns:
            a map from the satellite's ID to the information about that satellite contained in the file.
        
        
        """
        ...

class OemData(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    The Ephemerides data blocks class contain list of orbital data points.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    """
    def __init__(self):
        """
        EphemeridesBlock constructor.
        """
        ...
    def addCovarianceMatrix(self, covarianceMatrix: org.orekit.files.ccsds.ndm.odm.CartesianCovariance) -> None:
        """
        Add a covariance matrix.
        
        Parameters:
            covarianceMatrix (CartesianCovariance): covariance matrix to dd
        
        
        """
        ...
    def addData(self, data: org.orekit.utils.TimeStampedPVCoordinates, hasAcceleration: bool) -> bool:
        """
        Add a data point.
        
        Parameters:
            data (TimeStampedPVCoordinates): data point to add
            hasAcceleration (boolean): true if the current data point has acceleration data.
        
        Returns:
            always return true
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
        Get the derivatives available in the block.
        
        Returns:
            derivatives available in the block
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]:
        """
        Get an unmodifiable view of the data points.
        
        Returns:
            unmodifiable view of the data points
        
        
        """
        ...
    def getCovarianceMatrices(self) -> java.util.List[org.orekit.files.ccsds.ndm.odm.CartesianCovariance]:
        """
        Get an unmodifiable view of Covariance Matrices.
        
        Returns:
            unmodifiable view of Covariance Matrices
        
        
        """
        ...
    def getEphemeridesDataLines(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]:
        """
        Get the list of Ephemerides data lines.
        
        Returns:
            a reference to the internal list of Ephemerides data lines
        
        
        """
        ...

class OemMetadata(org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata):
    """
    Metadata for Orbit Ephemeris Messages.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self, defaultInterpolationDegree: int): ...
    @typing.overload
    def __init__(self, defaultInterpolationDegree: int, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
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
    def setInterpolationDegree(self, interpolationDegree: int) -> None:
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
            interpolationMethod (InterpolationMethod): the interpolation method to be set
        
        
        """
        ...
    def setStartTime(self, startTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set start of total time span covered by ephemerides data and covariance data.
        
        Parameters:
            startTime (AbsoluteDate): the time to be set
        
        
        """
        ...
    def setStopTime(self, stopTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set end of total time span covered by ephemerides data and covariance data.
        
        Parameters:
            stopTime (AbsoluteDate): the time to be set
        
        
        """
        ...
    def setUseableStartTime(self, useableStartTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set start of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
        Parameters:
            useableStartTime (AbsoluteDate): the time to be set
        
        
        """
        ...
    def setUseableStopTime(self, useableStopTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set end of useable time span covered by ephemerides data, it may be necessary to allow for proper interpolation.
        
        Parameters:
            useableStopTime (AbsoluteDate): the time to be set
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class OdmCommonMetadata
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class OemMetadataKey(java.lang.Enum['OemMetadataKey']):
    """
    Keys for OemMetadata entries.
    
    Since:
        11.0
    """
    START_TIME: typing.ClassVar['OemMetadataKey'] = ...
    STOP_TIME: typing.ClassVar['OemMetadataKey'] = ...
    USEABLE_START_TIME: typing.ClassVar['OemMetadataKey'] = ...
    USEABLE_STOP_TIME: typing.ClassVar['OemMetadataKey'] = ...
    INTERPOLATION: typing.ClassVar['OemMetadataKey'] = ...
    INTERPOLATION_DEGREE: typing.ClassVar['OemMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: OemMetadata) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (OemMetadata): container to fill
        
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
    def valueOf(name: str) -> 'OemMetadataKey':
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
    def values() -> typing.MutableSequence['OemMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (OemMetadataKey c : OemMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OemParser(org.orekit.files.ccsds.ndm.odm.OdmParser[Oem, 'OemParser'], org.orekit.files.general.EphemerisFileParser[Oem]):
    """
    A parser for the CCSDS OEM (Orbit Ephemeris Message).
    
    Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until the message is complete and the parseMessage method has returned. This implies that parsers should not be used in a multi-thread context. The recommended way to use parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
    Since:
        6.1
    """
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate, mu: float, defaultInterpolationDegree: int, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate, mu: float, defaultInterpolationDegree: int, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray], frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def build(self) -> Oem:
        """
        Build the file from parsed entries.
        
        Specified by: build in interface MessageParser
        
        Returns:
            parsed file
        
        
        """
        ...
    def finalizeData(self) -> bool:
        """
        Finalize data after parsing.
        
        Specified by: finalizeData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
        Finalize header after parsing.
        
        Specified by: finalizeHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
        Finalize metadata after parsing.
        
        Specified by: finalizeMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def getHeader(self) -> org.orekit.files.ccsds.ndm.odm.OdmHeader:
        """
        Get file header to fill.
        
        Specified by: getHeader in class AbstractConstituentParser
        
        Returns:
            file header to fill
        
        
        """
        ...
    def inData(self) -> bool:
        """
        Acknowledge data parsing has started.
        
        Specified by: inData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
        Acknowledge header parsing has started.
        
        Specified by: inHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
        Acknowledge metada parsing has started.
        
        Specified by: inMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def parse(self, source: org.orekit.data.DataSource) -> Oem:
        """
        Parse an ephemeris file from a data source.
        
        Specified by: parse in interface EphemerisFileParser
        
        Parameters:
            source (DataSource): source providing the data to parse
        
        Returns:
            a parsed ephemeris file.
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
        Prepare data for parsing.
        
        Specified by: prepareData in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
        Prepare header for parsing.
        
        Specified by: prepareHeader in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
        Prepare metadata for parsing.
        
        Specified by: prepareMetadata in class AbstractConstituentParser
        
        Returns:
            true if parser was able to perform the action
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
        Reset parser to initial state before parsing.
        
        Specified by: reset in interface MessageParser
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...

class OemSatelliteEphemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, 'OemSegment']):
    """
    OEM ephemeris blocks for a single satellite.
    
    Since:
        11.0
    """
    def __init__(self, id: str, mu: float, blocks: java.util.List['OemSegment']):
        """
        Create a container for the set of ephemeris blocks in the file that pertain to a single satellite.
        
        Parameters:
            id (String): id of the satellite.
            mu (double): gravitational coefficient to use for building Cartesian/Keplerian orbits
            blocks (List<OemSegment> blocks): containing ephemeris data for the satellite.
        
        
        """
        ...
    def getId(self) -> str:
        """
        Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
        Specified by: getId in interface SatelliteEphemeris
        
        Returns:
            the satellite's ID, never null.
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the standard gravitational parameter for the satellite.
        
        Specified by: getMu in interface SatelliteEphemeris
        
        Returns:
            the gravitational parameter used in getPropagator, in
            m³/s².
        
        
        """
        ...
    def getSegments(self) -> java.util.List['OemSegment']:
        """
        Get the segments of the ephemeris.
        
        Ephemeris segments are typically used to split an ephemeris around discontinuous events, such as maneuvers.
        
        Specified by: getSegments in interface SatelliteEphemeris
        
        Returns:
            the segments contained in the ephemeris file for this satellite.
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of the ephemeris.
        
        The date returned by this method is equivalent to getMinDate().
        
        Specified by: getStart in interface SatelliteEphemeris
        
        Returns:
            ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of the ephemeris.
        
        The date returned by this method is equivalent to getMaxDate().
        
        Specified by: getStop in interface SatelliteEphemeris
        
        Returns:
            ephemeris end date.
        
        
        """
        ...

class OemSegment(org.orekit.files.ccsds.section.Segment[OemMetadata, OemData], org.orekit.files.general.EphemerisFile.EphemerisSegment[org.orekit.utils.TimeStampedPVCoordinates]):
    """
    The Ephemerides Blocks class contain metadata, the list of ephemerides data lines and optional covariance matrices (and their metadata). The reason for which the ephemerides have been separated into blocks is that the ephemerides of two different blocks are not suited for interpolation.
    """
    def __init__(self, metadata: OemMetadata, data: OemData, mu: float):
        """
        Simple constructor.
        
        Parameters:
            metadata (OemMetadata): segment metadata
            data (OemData): segment data
            mu (double): gravitational parameter in m³/s²
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
        Get which derivatives of position are available in this ephemeris segment.
        
        While getCoordinates always returns position, velocity, and acceleration the return value from this method indicates which of those are in the ephemeris file and are actually valid.
        
        Specified by: getAvailableDerivatives in interface EphemerisSegment
        
        Returns:
            a value indicating if the file contains velocity and/or acceleration data.
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]:
        """
        Get the coordinates for this ephemeris segment in getFrame.
        
        Specified by: getCoordinates in interface EphemerisSegment
        
        Returns:
            a list of state vectors in chronological order. The coordinates are not necessarily evenly spaced in time. The value of
            getAvailableDerivatives indicates if the velocity or
            accelerations were specified in the file. Any position, velocity, or acceleration coordinates that are not specified in
            the ephemeris file are zero in the returned values.
        
        
        """
        ...
    def getCovarianceMatrices(self) -> java.util.List[org.orekit.files.ccsds.ndm.odm.CartesianCovariance]:
        """
        Get an unmodifiable view of Covariance Matrices.
        
        Returns:
            unmodifiable view of Covariance Matrices
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame for this ephemeris segment. The defining frame for getCoordinates.
        
        Specified by: getFrame in interface EphemerisSegment
        
        Returns:
            the reference frame for this segment. Never null.
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
        Get the number of samples to use in interpolation.
        
        Specified by: getInterpolationSamples in interface EphemerisSegment
        
        Returns:
            the number of points to use for interpolation.
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the standard gravitational parameter for the satellite.
        
        Specified by: getMu in interface EphemerisSegment
        
        Returns:
            the gravitational parameter used in getPropagator, in
            m³/s².
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start date of this ephemeris segment.
        
        The date returned by this method is equivalent to getMinDate().
        
        Specified by: getStart in interface EphemerisSegment
        
        Returns:
            ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the end date of this ephemeris segment.
        
        The date returned by this method is equivalent to getMaxDate().
        
        Specified by: getStop in interface EphemerisSegment
        
        Returns:
            ephemeris segment end date.
        
        
        """
        ...

class OemWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.odm.OdmHeader, OemSegment, Oem]):
    """
    A writer for Orbit Ephemeris Message (OEM) files.
    
    Metadata ----------
    
    The OEM metadata used by this writer is described in the following table. Many metadata items are optional or have default values so they do not need to be specified. At a minimum the user must supply those values that are required and for which no default exits: OBJECT_NAME, and OBJECT_ID. The usage column in the table indicates where the metadata item is used, either in the OEM header or in the metadata section at the start of an OEM ephemeris segment.
    
    The TIME_SYSTEM must be constant for the whole file and is used to interpret all dates except CREATION_DATE which is always in UTC. The guessing algorithm is not guaranteed to work so it is recommended to provide values for CENTER_NAME and TIME_SYSTEM to avoid any bugs associated with incorrect guesses.
    
    Standardized values for TIME_SYSTEM are GMST, GPS, MET, MRT, SCLK, TAI, TCB, TDB, TT, UT1, and UTC. Standardized values for reference frames are EME2000, GTOD, ICRF, ITRF2000, ITRF-93, ITRF-97, LVLH, RTN, QSW, TOD, TNW, NTW and RSW. Additionally ITRF followed by a four digit year may be used.
    
    Since:
        9.0
    
    Also see:
        pdf,
        pdf,
        StreamingOemWriter
    """
    CCSDS_OEM_VERS: typing.ClassVar[float] = ...
    """
    Version number implemented.
    
    Also see:
        constant
    
    
    """
    DEFAULT_FILE_NAME: typing.ClassVar[str] = ...
    """
    Default file name for error messages.
    
    Also see:
        constant
    
    
    """
    KVN_PADDING_WIDTH: typing.ClassVar[int] = ...
    """
    Padding width for aligning the '=' sign.
    
    Also see:
        constant
    
    
    """
    def __init__(self, conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate):
        """
        Constructor used to create a new OEM writer configured with the necessary parameters to successfully fill in all required fields that aren't part of a standard object.
        
        If the mandatory header entries are not present (or if header is null), built-in defaults will be used
        
        The writer is built from the complete header and partial metadata. The template metadata is used to initialize and independent local copy, that will be updated as new segments are written (with at least the segment start and stop will change, but some other parts may change too). The template argument itself is not changed.
        
        Calling this constructor directly is not recommended. Users should rather use buildOemWriter.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            dataContext (DataContext): used to retrieve frames, time scales, etc.
            missionReferenceDate (AbsoluteDate): reference date for Mission Elapsed Time or Mission Relative Time time systems
        
        Since:
            11.0
        
        Also see:
            DEFAULT_FILE_NAME
        
        
        """
        ...

class StreamingOemWriter(java.lang.AutoCloseable):
    """
    A writer for OEM files.
    
    Each instance corresponds to a single OEM file. A new OEM ephemeris segment is started by calling newSegment.
    
    The segments returned by this class can be used as step handlers for a Propagator.
    
     Propagator propagator = ...; // pre-configured propagator OEMWriter  aemWriter  = ...; // pre-configured writer try (Generator out = ...;  // set-up output stream StreamingOemWriter sw = new StreamingOemWriter(out, oemWriter, header, metadata)) { // set-up streaming writer
    
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
        pdf,
        pdf,
        OemWriter
    """
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, writer: OemWriter, header: org.orekit.files.ccsds.ndm.odm.OdmHeader, template: OemMetadata): ...
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, writer: OemWriter, header: org.orekit.files.ccsds.ndm.odm.OdmHeader, template: OemMetadata, useAttitudeFrame: bool): ...
    @typing.overload
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, writer: OemWriter, header: org.orekit.files.ccsds.ndm.odm.OdmHeader, template: OemMetadata, useAttitudeFrame: bool, includeAcceleration: bool): ...
    def close(self) -> None:
        """
        Specified by: AutoCloseable in interface AutoCloseable
        
        Raises:
            IOException: 
        
        """
        ...
    def newSegment(self) -> 'StreamingOemWriter.SegmentWriter':
        """
        Create a writer for a new OEM ephemeris segment.
        
        The returned writer can only write a single ephemeris segment in an OEM. This method must be called to create a writer for each ephemeris segment.
        
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
