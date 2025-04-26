
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.function
import jpype
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.adm
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



class Aem(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.adm.AdmHeader, 'AemSegment'], org.orekit.files.general.AttitudeEphemerisFile[org.orekit.utils.TimeStampedAngularCoordinates, 'AemSegment']):
    """
    public class Aem extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemSegment`> implements :class:`~org.orekit.files.general.AttitudeEphemerisFile`<:class:`~org.orekit.utils.TimeStampedAngularCoordinates`, :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemSegment`>
    
        This class stores all the information of the Attitude Ephemeris Message (AEM) File parsed by AEMParser. It contains the
        header and a list of Attitude Ephemerides Blocks each containing metadata and a list of attitude ephemerides data lines.
    
        Since:
            10.2
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ROOT
    
        Root element for XML files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` FORMAT_VERSION_KEY
    
        Key for format version.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, admHeader: org.orekit.files.ccsds.ndm.adm.AdmHeader, list: java.util.List['AemSegment'], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...
    def getSatellites(self) -> java.util.Map[str, 'AemSatelliteEphemeris']: ...

class AemData(org.orekit.files.ccsds.section.CommentsContainer, org.orekit.files.ccsds.section.Data):
    """
    public class AemData extends :class:`~org.orekit.files.ccsds.section.CommentsContainer` implements :class:`~org.orekit.files.ccsds.section.Data`
    
        The Attitude Ephemerides data blocks class contain list of attitude data points.
    
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
    def addData(self, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> bool:
        """
            Add a data point.
        
            Parameters:
                data (:class:`~org.orekit.utils.TimeStampedAngularCoordinates`): data point to add
        
            Returns:
                always return :code:`true`
        
        
        """
        ...
    def getAngularCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]: ...

class AemMetadata(org.orekit.files.ccsds.ndm.adm.AdmMetadata):
    """
    public class AemMetadata extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`
    
        This class gathers the meta-data present in the Attitude Data Message (ADM).
    
        Since:
            10.2
    """
    def __init__(self, int: int): ...
    def getAttitudeType(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeType:
        """
            Get the format of the data lines in the message.
        
            Returns:
                the format of the data lines in the message
        
        
        """
        ...
    def getEndpoints(self) -> org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints:
        """
            Get the endpoints (i.e. frames A, B and their relationship).
        
            Returns:
                endpoints
        
        
        """
        ...
    def getEulerRotSeq(self) -> org.hipparchus.geometry.euclidean.threed.RotationOrder:
        """
            Get the rotation order of Euler angles.
        
            Returns:
                rotation order
        
        
        """
        ...
    def getFrameAngvelFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get frame in which angular velocities are specified.
        
            Returns:
                frame in which angular velocities are specified
        
            Since:
                12.0
        
        
        """
        ...
    def getInterpolationDegree(self) -> int:
        """
            Get the interpolation degree.
        
            Returns:
                the interpolation degree
        
        
        """
        ...
    def getInterpolationMethod(self) -> str:
        """
            Get the interpolation method to be used.
        
            Returns:
                the interpolation method
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of samples to use in interpolation.
        
            Returns:
                the number of points to use for interpolation.
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of this ephemeris segment.
        
            Returns:
                ephemeris segment start date.
        
        
        """
        ...
    def getStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start of total time span covered by attitude data.
        
            Returns:
                the start time
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of this ephemeris segment.
        
            Returns:
                ephemeris segment end date.
        
        
        """
        ...
    def getStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get end of total time span covered by attitude data.
        
            Returns:
                the stop time
        
        
        """
        ...
    def getUseableStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start of useable time span covered by attitude data.
        
            Returns:
                the useable start time
        
        
        """
        ...
    def getUseableStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get end of useable time span covered by ephemerides data.
        
            Returns:
                the useable stop time
        
        
        """
        ...
    def isFirst(self) -> bool:
        """
            Get the flag for the placement of the quaternion QC in the attitude data.
        
            Returns:
                true if QC is the first element in the attitude data, false if not initialized
        
        
        """
        ...
    def isSpacecraftBodyRate(self) -> bool:
        """
            Check if rates are specified in spacecraft body frame.
        
            :meth:`~org.orekit.files.ccsds.ndm.adm.aem.AemMetadata.validate` must have been initialized properly to non-null values
            before this method is called, otherwise :code:`NullPointerException` will be thrown.
        
            Returns:
                true if rates are specified in spacecraft body frame
        
        
        """
        ...
    def rateFrameIsA(self) -> bool:
        """
            Check if rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA`.
        
            Returns:
                true if rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA`
        
        
        """
        ...
    def setAngvelFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set frame in which angular velocities are specified.
        
            Parameters:
                angvelFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): frame in which angular velocities are specified
        
            Since:
                12.0
        
        
        """
        ...
    def setAttitudeType(self, attitudeType: org.orekit.files.ccsds.ndm.adm.AttitudeType) -> None:
        """
            Set the format of the data lines in the message.
        
            Parameters:
                type (:class:`~org.orekit.files.ccsds.ndm.adm.AttitudeType`): format to be set
        
        
        """
        ...
    def setEulerRotSeq(self, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder) -> None:
        """
            Set the rotation order for Euler angles.
        
            Parameters:
                eulerRotSeq (:class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.RotationOrder?is`): order to be set
        
        
        """
        ...
    def setInterpolationDegree(self, int: int) -> None:
        """
            Set the interpolation degree.
        
            Parameters:
                interpolationDegree (int): the interpolation degree to be set
        
        
        """
        ...
    def setInterpolationMethod(self, string: str) -> None:
        """
            Set the interpolation method to be used.
        
            Parameters:
                interpolationMethod (:class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the interpolation method to be set
        
        
        """
        ...
    def setIsFirst(self, boolean: bool) -> None:
        """
            Set the flag for the placement of the quaternion QC in the attitude data.
        
            Parameters:
                isFirst (boolean): true if QC is the first element in the attitude data
        
        
        """
        ...
    def setRateFrameIsA(self, boolean: bool) -> None:
        """
            Set the frame in which rates are specified.
        
            Parameters:
                rateFrameIsA (boolean): if true, rates are specified in :meth:`~org.orekit.files.ccsds.ndm.adm.AttitudeEndpoints.getFrameA`
        
        
        """
        ...
    def setStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set start of total time span covered by attitude data.
        
            Parameters:
                startTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def setStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set end of total time span covered by attitude data.
        
            Parameters:
                stopTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def setUseableStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set start of useable time span covered by attitude data.
        
            Parameters:
                useableStartTime (:class:`~org.orekit.time.AbsoluteDate`): the time to be set
        
        
        """
        ...
    def setUseableStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set end of useable time span covered by ephemerides data.
        
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
                :meth:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata.validate` in
                class :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadata`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AemMetadataKey(java.lang.Enum['AemMetadataKey']):
    """
    public enum AemMetadataKey extends :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.aem.AemMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemMetadata` entries.
    
        Additional container are also listed in :class:`~org.orekit.files.ccsds.ndm.adm.AdmMetadataKey`.
    
        Since:
            11.0
    """
    REF_FRAME_A: typing.ClassVar['AemMetadataKey'] = ...
    REF_FRAME_B: typing.ClassVar['AemMetadataKey'] = ...
    ATTITUDE_DIR: typing.ClassVar['AemMetadataKey'] = ...
    START_TIME: typing.ClassVar['AemMetadataKey'] = ...
    STOP_TIME: typing.ClassVar['AemMetadataKey'] = ...
    USEABLE_START_TIME: typing.ClassVar['AemMetadataKey'] = ...
    USEABLE_STOP_TIME: typing.ClassVar['AemMetadataKey'] = ...
    ATTITUDE_TYPE: typing.ClassVar['AemMetadataKey'] = ...
    QUATERNION_TYPE: typing.ClassVar['AemMetadataKey'] = ...
    EULER_ROT_SEQ: typing.ClassVar['AemMetadataKey'] = ...
    RATE_FRAME: typing.ClassVar['AemMetadataKey'] = ...
    ANGVEL_FRAME: typing.ClassVar['AemMetadataKey'] = ...
    INTERPOLATION_METHOD: typing.ClassVar['AemMetadataKey'] = ...
    INTERPOLATION_DEGREE: typing.ClassVar['AemMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, aemMetadata: AemMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.adm.aem.AemMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'AemMetadataKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AemMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AemMetadataKey c : AemMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AemParser(org.orekit.files.ccsds.ndm.adm.AdmParser[Aem, 'AemParser'], org.orekit.files.general.AttitudeEphemerisFileParser[Aem]):
    """
    public class AemParser extends :class:`~org.orekit.files.ccsds.ndm.adm.AdmParser`<:class:`~org.orekit.files.ccsds.ndm.adm.aem.Aem`, :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemParser`> implements :class:`~org.orekit.files.general.AttitudeEphemerisFileParser`<:class:`~org.orekit.files.ccsds.ndm.adm.aem.Aem`>
    
        A parser for the CCSDS AEM (Attitude Ephemeris Message).
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            10.2
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, absoluteDate: org.orekit.time.AbsoluteDate, int: int, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, functionArray: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
    def build(self) -> Aem:
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
    def getHeader(self) -> org.orekit.files.ccsds.ndm.adm.AdmHeader:
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
    def parse(self, dataSource: org.orekit.data.DataSource) -> Aem:
        """
            Parse an attitude ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFileParser.parse` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFileParser`
        
            Parameters:
                source (:class:`~org.orekit.data.DataSource`): source providing the data to parse
        
            Returns:
                a parsed attitude ephemeris file.
        
        
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

class AemSatelliteEphemeris(org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, 'AemSegment']):
    """
    public class AemSatelliteEphemeris extends :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`<:class:`~org.orekit.utils.TimeStampedAngularCoordinates`, :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemSegment`>
    
        AEM ephemeris blocks for a single satellite.
    """
    def __init__(self, string: str, list: java.util.List['AemSegment']): ...
    def getId(self) -> str:
        """
            Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris.getId` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`
        
            Returns:
                the satellite's ID, never :code:`null`.
        
        
        """
        ...
    def getSegments(self) -> java.util.List['AemSegment']: ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of the ephemeris.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris.getStart` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`
        
            Returns:
                ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of the ephemeris.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris.getStop` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris`
        
            Returns:
                ephemeris end date.
        
        
        """
        ...

class AemSegment(org.orekit.files.ccsds.section.Segment[AemMetadata, AemData], org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment[org.orekit.utils.TimeStampedAngularCoordinates]):
    """
    public class AemSegment extends :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.adm.aem.AemMetadata`, :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemData`> implements :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`<:class:`~org.orekit.utils.TimeStampedAngularCoordinates`>
    
        This class stores the metadata and data for one attitude segment.
    
        Since:
            11.0
    """
    def __init__(self, aemMetadata: AemMetadata, aemData: AemData): ...
    def getAngularCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.BoundedAttitudeProvider:
        """
            Get the attitude provider for this attitude ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getAttitudeProvider` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                the attitude provider for this attitude ephemeris segment.
        
        
        """
        ...
    def getAvailableDerivatives(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
            Get which derivatives of angular data are available in this attitude ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getAvailableDerivatives` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                a value indicating if the file contains rotation and/or rotation rate and/or acceleration data.
        
        
        """
        ...
    def getInterpolationMethod(self) -> str:
        """
            Get the interpolation method to be used.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getInterpolationMethod` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                the interpolation method
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of samples to use in interpolation.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getInterpolationSamples` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                the number of points to use for interpolation.
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame from which attitude is defined.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getReferenceFrame` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                the reference frame from which attitude is defined
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of this ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getStart` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of this ephemeris segment.
        
            Specified by:
                :meth:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment.getStop` in
                interface :class:`~org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment`
        
            Returns:
                ephemeris segment end date.
        
        
        """
        ...

class AemWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.adm.AdmHeader, AemSegment, Aem]):
    """
    public class AemWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.ndm.adm.AdmHeader`, :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemSegment`, :class:`~org.orekit.files.ccsds.ndm.adm.aem.Aem`>
    
        A writer for Attitude Ephemeris Messsage (AEM) files.
    
        Metadata
    ----------
    
    
        The AEM header and metadata used by this writer are described in the following tables. Many metadata items are optional
        or have default values so they do not need to be specified. At a minimum the user must supply those values that are
        required and for which no default exits: :meth:`~org.orekit.files.ccsds.ndm.adm.AdmMetadataKey.OBJECT_NAME`,
        :meth:`~org.orekit.files.ccsds.ndm.adm.AdmCommonMetadataKey.OBJECT_ID`,
        :meth:`~org.orekit.files.ccsds.ndm.adm.aem.AemMetadataKey.START_TIME` and
        :meth:`~org.orekit.files.ccsds.ndm.adm.aem.AemMetadataKey.STOP_TIME`. The usage column in the table indicates where the
        metadata item is used, either in the AEM header or in the metadata section at the start of an AEM attitude segment.
    
        The AEM header for the whole AEM file is set when calling
        :meth:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter.writeHeader`, the entries are defined in table 4-2
        of the ADM standard.
    
        The AEM metadata for the AEM file is set when calling
        :meth:`~org.orekit.files.ccsds.ndm.adm.aem.AemWriter.writeSegmentContent`, the entries are defined in tables 4-3, 4-4
        and annex A of the ADM standard.
    
        The :meth:`~org.orekit.files.ccsds.section.MetadataKey.TIME_SYSTEM` must be constant for the whole file and is used to
        interpret all dates except :meth:`~org.orekit.files.ccsds.section.HeaderKey.CREATION_DATE` which is always in
        :meth:`~org.orekit.files.ccsds.definitions.TimeSystem.UTC`. The guessing algorithm is not guaranteed to work so it is
        recommended to provide values for :meth:`~org.orekit.files.ccsds.ndm.adm.AdmMetadataKey.CENTER_NAME` and
        :meth:`~org.orekit.files.ccsds.section.MetadataKey.TIME_SYSTEM` to avoid any bugs associated with incorrect guesses.
    
        Standardized values for :meth:`~org.orekit.files.ccsds.section.MetadataKey.TIME_SYSTEM` are GMST, GPS, MET, MRT, SCLK,
        TAI, TCB, TDB, TT, UT1, and UTC. Standardized values for reference frames are EME2000, GTOD, ICRF, ITRF2000, ITRF-93,
        ITRF-97, LVLH, RTN, QSW, TOD, TNW, NTW and RSW. Additionally ITRF followed by a four digit year may be used.
    
        Since:
            10.2
    """
    CCSDS_AEM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_AEM_VERS
    
        Version number implemented.
    
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

class AttitudeEntryKey(java.lang.Enum['AttitudeEntryKey']):
    """
    public enum AttitudeEntryKey extends :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.files.ccsds.ndm.adm.aem.AttitudeEntryKey`>
    
        Keys for :code:`attitude entries` in XML messages.
    
        Since:
            11.0
    """
    quaternionState: typing.ClassVar['AttitudeEntryKey'] = ...
    quaternionEphemeris: typing.ClassVar['AttitudeEntryKey'] = ...
    quaternionDerivative: typing.ClassVar['AttitudeEntryKey'] = ...
    quaternionEulerRate: typing.ClassVar['AttitudeEntryKey'] = ...
    quaternionAngVel: typing.ClassVar['AttitudeEntryKey'] = ...
    eulerAngle: typing.ClassVar['AttitudeEntryKey'] = ...
    eulerAngleRate: typing.ClassVar['AttitudeEntryKey'] = ...
    eulerAngleDerivative: typing.ClassVar['AttitudeEntryKey'] = ...
    eulerAngleAngVel: typing.ClassVar['AttitudeEntryKey'] = ...
    spin: typing.ClassVar['AttitudeEntryKey'] = ...
    spinNutation: typing.ClassVar['AttitudeEntryKey'] = ...
    spinNutationMom: typing.ClassVar['AttitudeEntryKey'] = ...
    quaternion: typing.ClassVar['AttitudeEntryKey'] = ...
    quaternionRate: typing.ClassVar['AttitudeEntryKey'] = ...
    quaternionDot: typing.ClassVar['AttitudeEntryKey'] = ...
    rotationAngles: typing.ClassVar['AttitudeEntryKey'] = ...
    rotationRates: typing.ClassVar['AttitudeEntryKey'] = ...
    angVel: typing.ClassVar['AttitudeEntryKey'] = ...
    EPOCH: typing.ClassVar['AttitudeEntryKey'] = ...
    Q1: typing.ClassVar['AttitudeEntryKey'] = ...
    Q2: typing.ClassVar['AttitudeEntryKey'] = ...
    Q3: typing.ClassVar['AttitudeEntryKey'] = ...
    QC: typing.ClassVar['AttitudeEntryKey'] = ...
    Q1_DOT: typing.ClassVar['AttitudeEntryKey'] = ...
    Q2_DOT: typing.ClassVar['AttitudeEntryKey'] = ...
    Q3_DOT: typing.ClassVar['AttitudeEntryKey'] = ...
    QC_DOT: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGVEL_X: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGVEL_Y: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGVEL_Z: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGLE_1: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGLE_2: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGLE_3: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGLE_1_DOT: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGLE_2_DOT: typing.ClassVar['AttitudeEntryKey'] = ...
    ANGLE_3_DOT: typing.ClassVar['AttitudeEntryKey'] = ...
    X_ANGLE: typing.ClassVar['AttitudeEntryKey'] = ...
    Y_ANGLE: typing.ClassVar['AttitudeEntryKey'] = ...
    Z_ANGLE: typing.ClassVar['AttitudeEntryKey'] = ...
    X_RATE: typing.ClassVar['AttitudeEntryKey'] = ...
    Y_RATE: typing.ClassVar['AttitudeEntryKey'] = ...
    Z_RATE: typing.ClassVar['AttitudeEntryKey'] = ...
    SPIN_ALPHA: typing.ClassVar['AttitudeEntryKey'] = ...
    SPIN_DELTA: typing.ClassVar['AttitudeEntryKey'] = ...
    SPIN_ANGLE: typing.ClassVar['AttitudeEntryKey'] = ...
    SPIN_ANGLE_VEL: typing.ClassVar['AttitudeEntryKey'] = ...
    NUTATION: typing.ClassVar['AttitudeEntryKey'] = ...
    NUTATION_PER: typing.ClassVar['AttitudeEntryKey'] = ...
    NUTATION_PHASE: typing.ClassVar['AttitudeEntryKey'] = ...
    MOMENTUM_ALPHA: typing.ClassVar['AttitudeEntryKey'] = ...
    MOMENTUM_DELTA: typing.ClassVar['AttitudeEntryKey'] = ...
    NUTATION_VEL: typing.ClassVar['AttitudeEntryKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, attitudeEntry: 'AttitudeEntry') -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (org.orekit.files.ccsds.ndm.adm.aem.AttitudeEntry): container to fill
        
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
    def valueOf(string: str) -> 'AttitudeEntryKey':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AttitudeEntryKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AttitudeEntryKey c : AttitudeEntryKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AttitudeWriter(org.orekit.files.general.AttitudeEphemerisFileWriter):
    """
    public class AttitudeWriter extends :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.general.AttitudeEphemerisFileWriter`
    
        An :class:`~org.orekit.files.general.AttitudeEphemerisFileWriter` generating
        :class:`~org.orekit.files.ccsds.ndm.adm.aem.Aem` files.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, aemWriter: AemWriter, admHeader: org.orekit.files.ccsds.ndm.adm.AdmHeader, aemMetadata: AemMetadata, fileFormat: org.orekit.files.ccsds.utils.FileFormat, string: str, double: float, int: int): ...
    @typing.overload
    def __init__(self, aemWriter: AemWriter, admHeader: org.orekit.files.ccsds.ndm.adm.AdmHeader, aemMetadata: AemMetadata, fileFormat: org.orekit.files.ccsds.utils.FileFormat, string: str, double: float, int: int, formatter: org.orekit.utils.Formatter): ...
    _write_0__C = typing.TypeVar('_write_0__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
    _write_0__S = typing.TypeVar('_write_0__S', bound=org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment)  # <S>
    _write_1__C = typing.TypeVar('_write_1__C', bound=org.orekit.utils.TimeStampedAngularCoordinates)  # <C>
    _write_1__S = typing.TypeVar('_write_1__S', bound=org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment)  # <S>
    @typing.overload
    def write(self, string: str, attitudeEphemerisFile: typing.Union[org.orekit.files.general.AttitudeEphemerisFile[_write_0__C, _write_0__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment]]]]) -> None: ...
    @typing.overload
    def write(self, appendable: java.lang.Appendable, attitudeEphemerisFile: typing.Union[org.orekit.files.general.AttitudeEphemerisFile[_write_1__C, _write_1__S], typing.Callable[[], java.util.Map[str, org.orekit.files.general.AttitudeEphemerisFile.SatelliteAttitudeEphemeris[org.orekit.utils.TimeStampedAngularCoordinates, org.orekit.files.general.AttitudeEphemerisFile.AttitudeEphemerisSegment]]]]) -> None: ...

class StreamingAemWriter(java.lang.AutoCloseable):
    """
    public class StreamingAemWriter extends :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.docs.oracle.com.javase.8.docs.api.java.lang.AutoCloseable?is`
    
        A writer for AEM files.
    
        Each instance corresponds to a single AEM file.
    
        This class can be used as a step handler for a :class:`~org.orekit.propagation.Propagator`.
    
        .. code-block: java
        
         Propagator propagator = ...; // pre-configured propagator
         AEMWriter  aemWriter  = ...; // pre-configured writer
           try (Generator out = ...;  // set-up output stream
                StreamingAemWriter sw = new StreamingAemWriter(out, aemWriter)) { // set-up streaming writer
        
             // write segment 1
             propagator.getMultiplexer().add(step, sw.newSegment());
             propagator.propagate(startDate1, stopDate1);
        
             ...
        
             // write segment n
             propagator.getMultiplexer().clear();
             propagator.getMultiplexer().add(step, sw.newSegment());
             propagator.propagate(startDateN, stopDateN);
        
           }
         
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.files.ccsds.ndm.adm.aem.https:.public.ccsds.org.Pubs.504x0b1c1.pdf`,
            :class:`~org.orekit.files.ccsds.ndm.adm.aem.AemWriter`
    """
    def __init__(self, generator: org.orekit.files.ccsds.utils.generation.Generator, aemWriter: AemWriter, admHeader: org.orekit.files.ccsds.ndm.adm.AdmHeader, aemMetadata: AemMetadata): ...
    def close(self) -> None: ...
    def newSegment(self) -> 'StreamingAemWriter.SegmentWriter':
        """
            Create a writer for a new AEM attitude ephemeris segment.
        
            The returned writer can only write a single attitude ephemeris segment in an AEM. This method must be called to create a
            writer for each attitude ephemeris segment.
        
            Returns:
                a new AEM segment writer, ready for use.
        
        
        """
        ...
    class SegmentWriter(org.orekit.propagation.sampling.OrekitFixedStepHandler):
        def __init__(self, streamingAemWriter: 'StreamingAemWriter'): ...
        def finish(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def handleStep(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> None: ...

class AttitudeEntry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.adm.aem")``.

    Aem: typing.Type[Aem]
    AemData: typing.Type[AemData]
    AemMetadata: typing.Type[AemMetadata]
    AemMetadataKey: typing.Type[AemMetadataKey]
    AemParser: typing.Type[AemParser]
    AemSatelliteEphemeris: typing.Type[AemSatelliteEphemeris]
    AemSegment: typing.Type[AemSegment]
    AemWriter: typing.Type[AemWriter]
    AttitudeEntry: typing.Type[AttitudeEntry]
    AttitudeEntryKey: typing.Type[AttitudeEntryKey]
    AttitudeWriter: typing.Type[AttitudeWriter]
    StreamingAemWriter: typing.Type[StreamingAemWriter]
