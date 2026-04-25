
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
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



class Maneuver(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Maneuver in an OPM file.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        6.1
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def completed(self) -> bool:
        """
        Check if maneuver has been completed.
        
        Returns:
            true if maneuver has been completed
        
        
        """
        ...
    def getDV(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get velocity increment.
        
        Returns:
            velocity increment
        
        
        """
        ...
    def getDeltaMass(self) -> float:
        """
        Get mass change during maneuver (value is < 0).
        
        Returns:
            mass change during maneuver (value is < 0)
        
        
        """
        ...
    def getDuration(self) -> float:
        """
        Get duration (value is 0 for impulsive maneuver).
        
        Returns:
            duration (value is 0 for impulsive maneuver)
        
        
        """
        ...
    def getEpochIgnition(self) -> org.orekit.time.AbsoluteDate:
        """
        Get epoch ignition.
        
        Returns:
            epoch ignition
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get Coordinate system for velocity increment vector.
        
        Returns:
            coordinate system for velocity increment vector
        
        
        """
        ...
    def setDV(self, i: int, dVi: float) -> None:
        """
        Set velocity increment component.
        
        Parameters:
            i (int): component index
            dVi (double): velocity increment component
        
        
        """
        ...
    def setDeltaMass(self, deltaMass: float) -> None:
        """
        Set mass change during maneuver (value is < 0).
        
        Parameters:
            deltaMass (double): mass change during maneuver (value is < 0)
        
        
        """
        ...
    def setDuration(self, duration: float) -> None:
        """
        Set duration (value is 0 for impulsive maneuver).
        
        Parameters:
            duration (double): duration (value is 0 for impulsive maneuver)
        
        
        """
        ...
    def setEpochIgnition(self, epochIgnition: org.orekit.time.AbsoluteDate) -> None:
        """
        Set epoch ignition.
        
        Parameters:
            epochIgnition (AbsoluteDate): epoch ignition
        
        
        """
        ...
    def setReferenceFrame(self, referenceFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set Coordinate system for velocity increment vector.
        
        Parameters:
            referenceFrame (FrameFacade): coordinate system for velocity increment vector
        
        
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

class ManeuverKey(java.lang.Enum['ManeuverKey']):
    """
    Keys for Maneuver entries.
    
    Since:
        11.0
    """
    COMMENT: typing.ClassVar['ManeuverKey'] = ...
    MAN_EPOCH_IGNITION: typing.ClassVar['ManeuverKey'] = ...
    MAN_REF_FRAME: typing.ClassVar['ManeuverKey'] = ...
    MAN_DURATION: typing.ClassVar['ManeuverKey'] = ...
    MAN_DELTA_MASS: typing.ClassVar['ManeuverKey'] = ...
    MAN_DV_1: typing.ClassVar['ManeuverKey'] = ...
    MAN_DV_2: typing.ClassVar['ManeuverKey'] = ...
    MAN_DV_3: typing.ClassVar['ManeuverKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: Maneuver) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (Maneuver): container to fill
        
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
    def valueOf(name: str) -> 'ManeuverKey':
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
    def values() -> typing.MutableSequence['ManeuverKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ManeuverKey c : ManeuverKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Opm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.ndm.odm.OdmHeader, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata, 'OpmData']], org.orekit.time.TimeStamped):
    """
    This class gathers the informations present in the Orbital Parameter Message (OPM).
    
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
    def __init__(self, header: org.orekit.files.ccsds.ndm.odm.OdmHeader, segments: java.util.List[org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata, 'OpmData']], conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, mu: float):
        """
        Simple constructor.
        
        Parameters:
            header (OdmHeader): file header
            segments (List<Segment<OdmCommonMetadata, OpmData>>): file segments
            conventions (IERSConventions): IERS conventions
            dataContext (DataContext): used for creating frames, time scales, etc.
            mu (double): gravitational coefficient to use for building Cartesian/Keplerian orbits
        
        
        """
        ...
    def generateCartesianOrbit(self) -> org.orekit.orbits.CartesianOrbit:
        """
        Generate a Cartesian orbit.
        
        Returns:
            generated orbit
        
        
        """
        ...
    def generateKeplerianOrbit(self) -> org.orekit.orbits.KeplerianOrbit:
        """
        Generate a keplerian orbit.
        
        Returns:
            generated orbit
        
        
        """
        ...
    def generateSpacecraftState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Generate spacecraft state from the CartesianOrbit generated by generateCartesianOrbit.
        
        Returns:
            the spacecraft state of the OPM
        
        
        """
        ...
    def getData(self) -> 'OpmData':
        """
        Get the file data.
        
        Returns:
            file data
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getManeuver(self, index: int) -> Maneuver:
        """
        Get a maneuver.
        
        Parameters:
            index (int): maneuver index, counting from 0
        
        Returns:
            maneuver
        
        
        """
        ...
    def getManeuvers(self) -> java.util.List[Maneuver]:
        """
        Get a list of all maneuvers.
        
        Returns:
            unmodifiable list of all maneuvers.
        
        
        """
        ...
    def getMetadata(self) -> org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata:
        """
        Get the file metadata.
        
        Returns:
            file metadata
        
        
        """
        ...
    def getNbManeuvers(self) -> int:
        """
        Get the number of maneuvers present in the OPM.
        
        Returns:
            the number of maneuvers
        
        
        """
        ...
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the position/velocity coordinates contained in the OPM.
        
        Returns:
            the position/velocity coordinates contained in the OPM
        
        
        """
        ...
    def hasManeuvers(self) -> bool:
        """
        check whether the OPM contains at least one maneuver.
        
        Returns:
            true if OPM contains at least one maneuver false otherwise
        
        
        """
        ...

class OpmData(org.orekit.files.ccsds.section.Data):
    """
    Container for Orbit Parameter Message data.
    
    Since:
        11.0
    """
    def __init__(self, stateVectorBlock: org.orekit.files.ccsds.ndm.odm.StateVector, keplerianElementsBlock: org.orekit.files.ccsds.ndm.odm.KeplerianElements, spacecraftParametersBlock: org.orekit.files.ccsds.ndm.odm.SpacecraftParameters, covarianceBlock: org.orekit.files.ccsds.ndm.odm.CartesianCovariance, maneuverBlocks: java.util.List[Maneuver], userDefinedBlock: org.orekit.files.ccsds.ndm.odm.UserDefined, mass: float):
        """
        Simple constructor.
        
        Parameters:
            stateVectorBlock (StateVector): state vector logical block
            keplerianElementsBlock (KeplerianElements): Keplerian elements logical block (may be null)
            spacecraftParametersBlock (SpacecraftParameters): spacecraft parameters logical block (may be null)
            covarianceBlock (CartesianCovariance): covariance matrix logical block (may be null)
            maneuverBlocks (List<Maneuver> maneuverBlocks): maneuvers block list
            userDefinedBlock (UserDefined): user-defined logical block
            mass (double): mass (always defined, even if there is no spacecraftParameters block
        
        
        """
        ...
    def getCovarianceBlock(self) -> org.orekit.files.ccsds.ndm.odm.CartesianCovariance:
        """
        Get the covariance matrix logical block.
        
        Returns:
            covariance matrix block (may be null)
        
        
        """
        ...
    def getKeplerianElementsBlock(self) -> org.orekit.files.ccsds.ndm.odm.KeplerianElements:
        """
        Get the Keplerian elements logical block.
        
        Returns:
            Keplerian elements block (may be null)
        
        
        """
        ...
    def getManeuver(self, index: int) -> Maneuver:
        """
        Get a maneuver.
        
        Parameters:
            index (int): maneuver index, counting from 0
        
        Returns:
            maneuver
        
        
        """
        ...
    def getManeuvers(self) -> java.util.List[Maneuver]:
        """
        Get a list of all maneuvers.
        
        Returns:
            unmodifiable list of all maneuvers.
        
        
        """
        ...
    def getMass(self) -> float:
        """
        Get the mass.
        
        Returns:
            mass
        
        
        """
        ...
    def getNbManeuvers(self) -> int:
        """
        Get the number of maneuvers present in the APM.
        
        Returns:
            the number of maneuvers
        
        
        """
        ...
    def getSpacecraftParametersBlock(self) -> org.orekit.files.ccsds.ndm.odm.SpacecraftParameters:
        """
        Get the spacecraft parameters logical block.
        
        Returns:
            spacecraft parameters block (may be null)
        
        
        """
        ...
    def getStateVectorBlock(self) -> org.orekit.files.ccsds.ndm.odm.StateVector:
        """
        Get the state vector logical block.
        
        Returns:
            state vector block
        
        
        """
        ...
    def getUserDefinedBlock(self) -> org.orekit.files.ccsds.ndm.odm.UserDefined:
        """
        Get the user defined parameters logical block.
        
        Returns:
            user defined parameters block (may be null)
        
        
        """
        ...
    def hasManeuvers(self) -> bool:
        """
        Get boolean testing whether the APM contains at least one maneuver.
        
        Returns:
            true if APM contains at least one maneuver false otherwise
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class OpmParser(org.orekit.files.ccsds.ndm.odm.OdmParser[Opm, 'OpmParser']):
    """
    A parser for the CCSDS OPM (Orbit Parameter Message).
    
    Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until the message is complete and the parseMessage method has returned. This implies that parsers should not be used in a multi-thread context. The recommended way to use parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
    Since:
        6.1
    """
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, missionReferenceDate: org.orekit.time.AbsoluteDate, mu: float, defaultMass: float, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]):
        """
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildOpmParser.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
            dataContext (DataContext): used to retrieve frames, time scales, etc.
            missionReferenceDate (AbsoluteDate): reference date for Mission Elapsed Time or Mission Relative Time time systems
            mu (double): gravitational coefficient
            defaultMass (double): default mass to use if there are no spacecraft parameters block logical block in the file
            parsedUnitsBehavior (ParsedUnitsBehavior): behavior to adopt for handling parsed units
            filters (Function<ParseToken, List<ParseToken>>[]): filters to apply to parse tokens
        
        Since:
            12.0
        
        
        """
        ...
    def build(self) -> Opm:
        """
        Build the file from parsed entries.
        
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
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]:
        """
        Get the non-default token builders for special XML elements.
        
        Specified by: getSpecialXmlElementsBuilders in interface MessageParser
        
        Overrides: getSpecialXmlElementsBuilders in class AbstractMessageParser
        
        Returns:
            map of token builders for special XML elements (keyed by XML element name)
        
        
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
        
        Parameters:
            fileFormat (FileFormat): format of the file ready to be parsed
        
        
        """
        ...

class OpmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.ndm.odm.OdmHeader, org.orekit.files.ccsds.section.Segment[org.orekit.files.ccsds.ndm.odm.OdmCommonMetadata, OpmData], Opm]):
    """
    Writer for CCSDS Orbit Parameter Message.
    
    Since:
        11.0
    """
    CCSDS_OPM_VERS: typing.ClassVar[float] = ...
    """
    Version number implemented.
    
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
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildOpmWriter.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            dataContext (DataContext): used to retrieve frames, time scales, etc.
            missionReferenceDate (AbsoluteDate): reference date for Mission Elapsed Time or Mission Relative Time time systems
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm.opm")``.

    Maneuver: typing.Type[Maneuver]
    ManeuverKey: typing.Type[ManeuverKey]
    Opm: typing.Type[Opm]
    OpmData: typing.Type[OpmData]
    OpmParser: typing.Type[OpmParser]
    OpmWriter: typing.Type[OpmWriter]
