
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
import org.hipparchus.linear
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.ndm.odm.ocm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.ccsds.utils.parsing
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class AdditionalCovarianceMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for the additional covariance metadata (optional).
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getDcpSensitivityVectorPosition(self) -> typing.MutableSequence[float]:
        """
        Get the DCP sensitivity vector (position errors at TCA).
        
        Returns:
            the dcpSensitivityVectorPosition
        
        
        """
        ...
    def getDcpSensitivityVectorVelocity(self) -> typing.MutableSequence[float]:
        """
        Get the DCP sensitivity vector (velocity errors at TCA).
        
        Returns:
            the dcpSensitivityVectorVelocity
        
        
        """
        ...
    def getDensityForecastUncertainty(self) -> float:
        """
        Get the atmospheric density forecast error.
        
        Returns:
            densityForecastUncertainty
        
        
        """
        ...
    def getScreeningDataSource(self) -> str:
        """
        Get the source (or origin) of the specific orbital data for this object.
        
        Returns:
            the screeningDataSource
        
        
        """
        ...
    def getcScaleFactor(self) -> float:
        """
        Get the (median) suggested covariance scale factor.
        
        Returns:
            the cScaleFactor
        
        
        """
        ...
    def getcScaleFactorMax(self) -> float:
        """
        Get the maximum suggested covariance scale factor.
        
        Returns:
            the cScaleFactorMax
        
        
        """
        ...
    def getcScaleFactorMin(self) -> float:
        """
        Get the minimum suggested covariance scale factor.
        
        Returns:
            the cScaleFactorMin
        
        
        """
        ...
    def setDcpSensitivityVectorPosition(self, dcpSensitivityVectorPosition: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the DCP sensitivity vector (position errors at TCA).
        
        Parameters:
            dcpSensitivityVectorPosition (double[]): the dcpSensitivityVectorPosition to set
        
        
        """
        ...
    def setDcpSensitivityVectorVelocity(self, dcpSensitivityVectorVelocity: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the DCP sensitivity vector (velocity errors at TCA).
        
        Parameters:
            dcpSensitivityVectorVelocity (double[]): the dcpSensitivityVectorVelocity to set
        
        
        """
        ...
    def setDensityForecastUncertainty(self, densityForecastUncertainty: float) -> None:
        """
        Set the atmospheric density forecast error.
        
        Parameters:
            densityForecastUncertainty (double): the cScaleFactorMax to set
        
        
        """
        ...
    def setScreeningDataSource(self, screeningDataSource: str) -> None:
        """
        Set the source (or origin) of the specific orbital data for this object.
        
        Parameters:
            screeningDataSource (String): the screeningDataSource to set
        
        
        """
        ...
    def setcScaleFactor(self, cScaleFactor: float) -> None:
        """
        Set the (median) suggested covariance scale factor.
        
        Parameters:
            cScaleFactor (double): the cScaleFactor to set
        
        
        """
        ...
    def setcScaleFactorMax(self, cScaleFactorMax: float) -> None:
        """
        set the maximum suggested covariance scale factor.
        
        Parameters:
            cScaleFactorMax (double): the cScaleFactorMax to set
        
        
        """
        ...
    def setcScaleFactorMin(self, cScaleFactorMin: float) -> None:
        """
        Set the minimum suggested covariance scale factor.
        
        Parameters:
            cScaleFactorMin (double): the cScaleFactorMin to set
        
        
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

class AdditionalCovarianceMetadataKey(java.lang.Enum['AdditionalCovarianceMetadataKey']):
    """
    Keys for AdditionalCovarianceMetadata entries.
    """
    COMMENT: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    DENSITY_FORECAST_UNCERTAINTY: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    CSCALE_FACTOR_MIN: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    CSCALE_FACTOR: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    CSCALE_FACTOR_MAX: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    SCREENING_DATA_SOURCE: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    DCP_SENSITIVITY_VECTOR_POSITION: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    DCP_SENSITIVITY_VECTOR_VELOCITY: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AdditionalCovarianceMetadata) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AdditionalCovarianceMetadata): container to fill
        
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
    def valueOf(name: str) -> 'AdditionalCovarianceMetadataKey':
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
    def values() -> typing.MutableSequence['AdditionalCovarianceMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AdditionalCovarianceMetadataKey c : AdditionalCovarianceMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdditionalParameters(org.orekit.files.ccsds.ndm.CommonPhysicalProperties):
    """
    Container for additional parameters data block.
    
    Since:
        11.2
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def getApoapsisAltitude(self) -> float:
        """
        Get the distance of the furthest point in the objects orbit above the equatorial radius of the central body.
        
        Returns:
            the apoapsisAltitude
        
        
        """
        ...
    def getAreaDRG(self) -> float:
        """
        Get the effective area of the object exposed to atmospheric drag.
        
        Returns:
            the object area (in m²) exposed to atmospheric drag
        
        
        """
        ...
    def getAreaPC(self) -> float:
        """
        Get the actual area of the object.
        
        Returns:
            the object area (in m²)
        
        
        """
        ...
    def getAreaPCMax(self) -> float:
        """
        Get the maximum area of the object to be used to compute the collision probability.
        
        Returns:
            the areaPCMax
        
        
        """
        ...
    def getAreaPCMin(self) -> float:
        """
        Set the minimum area of the object to be used to compute the collision probability.
        
        Returns:
            the areaPCMin
        
        
        """
        ...
    def getAreaSRP(self) -> float:
        """
        Get the effective area of the object exposed to solar radiation pressure.
        
        Returns:
            the object area (in m²) exposed to solar radiation pressure
        
        
        """
        ...
    def getCDAreaOverMass(self) -> float:
        """
        Get the object’s Cd x A/m used to propagate the state vector and covariance to TCA.
        
        Returns:
            the object’s Cd x A/m (in m²/kg)
        
        
        """
        ...
    def getCRAreaOverMass(self) -> float:
        """
        Get the object’s Cr x A/m used to propagate the state vector and covariance to TCA.
        
        Returns:
            the object’s Cr x A/m (in m²/kg)
        
        
        """
        ...
    def getCovConfidence(self) -> float:
        """
        Get the measure of the confidence in the covariance errors matching reality.
        
        Returns:
            the covConfidence
        
        
        """
        ...
    def getCovConfidenceMethod(self) -> str:
        """
        Get the method used for the calculation of COV_CONFIDENCE.
        
        Returns:
            the covConfidenceMethod
        
        
        """
        ...
    def getHbr(self) -> float:
        """
        Get the object hard body radius.
        
        Returns:
            the object hard body radius.
        
        
        """
        ...
    def getInclination(self) -> float:
        """
        Get the angle between the objects orbit plane and the orbit centers equatorial plane.
        
        Returns:
            the inclination
        
        
        """
        ...
    def getMass(self) -> float:
        """
        Get the mass of the object.
        
        Returns:
            the mass (in kg) of the object
        
        
        """
        ...
    def getPeriapsisAltitude(self) -> float:
        """
        Get the distance of the closest point in the objects orbit above the equatorial radius of the central body.
        
        Returns:
            the periapsissAltitude
        
        
        """
        ...
    def getSedr(self) -> float:
        """
        Get the amount of energy being removed from the object’s orbit by atmospheric drag. This value is an average calculated during the OD. SEDR = Specific Energy Dissipation Rate.
        
        Returns:
            the amount of energy (in W/kg) being removed from the object’s orbit by atmospheric drag
        
        
        """
        ...
    def getThrustAcceleration(self) -> float:
        """
        Get the object’s acceleration due to in-track thrust used to propagate the state vector and covariance to TCA.
        
        Returns:
            the object’s acceleration (in m/s²) due to in-track thrust
        
        
        """
        ...
    def setApoapsisAltitude(self, apoapsisAltitude: float) -> None:
        """
        Set the distance of the furthest point in the objects orbit above the equatorial radius of the central body.
        
        Parameters:
            apoapsisAltitude (double): the apoapsisHeight to set
        
        
        """
        ...
    def setAreaDRG(self, areaDRG: float) -> None:
        """
        Set the effective area of the object exposed to atmospheric drag.
        
        Parameters:
            areaDRG (double): area (in m²) value to be set
        
        
        """
        ...
    def setAreaPC(self, areaPC: float) -> None:
        """
        Set the actual area of the object.
        
        Parameters:
            areaPC (double): area (in m²) value to be set
        
        
        """
        ...
    def setAreaPCMax(self, areaPCMax: float) -> None:
        """
        Set the maximum area for the object to be used to compute the collision probability.
        
        Parameters:
            areaPCMax (double): the areaPCMax to set
        
        
        """
        ...
    def setAreaPCMin(self, areaPCMin: float) -> None:
        """
        Get the minimum area of the object to be used to compute the collision probability.
        
        Parameters:
            areaPCMin (double): the areaPCMin to set
        
        
        """
        ...
    def setAreaSRP(self, areaSRP: float) -> None:
        """
        Set the effective area of the object exposed to solar radiation pressure.
        
        Parameters:
            areaSRP (double): area (in m²) to be set
        
        
        """
        ...
    def setCDAreaOverMass(self, CDAreaOverMass: float) -> None:
        """
        Set the object’s Cd x A/m used to propagate the state vector and covariance to TCA.
        
        Parameters:
            CDAreaOverMass (double): object’s Cd x A/m (in m²/kg) value to be set
        
        
        """
        ...
    def setCRAreaOverMass(self, CRAreaOverMass: float) -> None:
        """
        Set the object’s Cr x A/m used to propagate the state vector and covariance to TCA.
        
        Parameters:
            CRAreaOverMass (double): object’s Cr x A/m (in m²/kg) value to be set
        
        
        """
        ...
    def setCovConfidence(self, covConfidence: float) -> None:
        """
        Set the measure of the confidence in the covariance errors matching reality.
        
        Parameters:
            covConfidence (double): the covConfidence to set
        
        
        """
        ...
    def setCovConfidenceMethod(self, covConfidenceMethod: str) -> None:
        """
        Set the method used for the calculation of COV_CONFIDENCE.
        
        Parameters:
            covConfidenceMethod (String): the covConfidenceMethod to set
        
        
        """
        ...
    def setHbr(self, hbr: float) -> None:
        """
        Set the object hard body radius.
        
        Parameters:
            hbr (double): the object hard body radius.
        
        
        """
        ...
    def setInclination(self, inclination: float) -> None:
        """
        Set the angle between the objects orbit plane and the orbit centers equatorial plane.
        
        Parameters:
            inclination (double): the inclination to set
        
        
        """
        ...
    def setMass(self, mass: float) -> None:
        """
        Set the mass of the object.
        
        Parameters:
            mass (double): mass (in kg) of the object to be set
        
        
        """
        ...
    def setPeriapsisAltitude(self, periapsisAltitude: float) -> None:
        """
        Set the distance of the closest point in the objects orbit above the equatorial radius of the central body.
        
        Parameters:
            periapsisAltitude (double): the periapsissHeight to set
        
        
        """
        ...
    def setSedr(self, SEDR: float) -> None:
        """
        Set the amount of energy being removed from the object’s orbit by atmospheric drag. This value is an average calculated during the OD. SEDR = Specific Energy Dissipation Rate.
        
        Parameters:
            SEDR (double): amount of energy (in W/kg) being removed from the object’s orbit by atmospheric drag
        
        
        """
        ...
    def setThrustAcceleration(self, thrustAcceleration: float) -> None:
        """
        Set the object’s acceleration due to in-track thrust used to propagate the state vector and covariance to TCA.
        
        Parameters:
            thrustAcceleration (double): object’s acceleration (in m/s²) due to in-track thrust
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class CommonPhysicalProperties
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class AdditionalParametersKey(java.lang.Enum['AdditionalParametersKey']):
    """
    Keys for AdditionalParameters entries.
    
    Since:
        11.2
    """
    COMMENT: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_PC: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_PC_MIN: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_PC_MAX: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_DRG: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_SRP: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_PARENT_FRAME: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_PARENT_FRAME_EPOCH: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_Q1: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_Q2: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_Q3: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_QC: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_MAX: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_INT: typing.ClassVar['AdditionalParametersKey'] = ...
    OEB_MIN: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_ALONG_OEB_MAX: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_ALONG_OEB_INT: typing.ClassVar['AdditionalParametersKey'] = ...
    AREA_ALONG_OEB_MIN: typing.ClassVar['AdditionalParametersKey'] = ...
    RCS: typing.ClassVar['AdditionalParametersKey'] = ...
    RCS_MIN: typing.ClassVar['AdditionalParametersKey'] = ...
    RCS_MAX: typing.ClassVar['AdditionalParametersKey'] = ...
    VM_ABSOLUTE: typing.ClassVar['AdditionalParametersKey'] = ...
    VM_APPARENT_MIN: typing.ClassVar['AdditionalParametersKey'] = ...
    VM_APPARENT: typing.ClassVar['AdditionalParametersKey'] = ...
    VM_APPARENT_MAX: typing.ClassVar['AdditionalParametersKey'] = ...
    REFLECTANCE: typing.ClassVar['AdditionalParametersKey'] = ...
    MASS: typing.ClassVar['AdditionalParametersKey'] = ...
    HBR: typing.ClassVar['AdditionalParametersKey'] = ...
    CD_AREA_OVER_MASS: typing.ClassVar['AdditionalParametersKey'] = ...
    CR_AREA_OVER_MASS: typing.ClassVar['AdditionalParametersKey'] = ...
    THRUST_ACCELERATION: typing.ClassVar['AdditionalParametersKey'] = ...
    SEDR: typing.ClassVar['AdditionalParametersKey'] = ...
    APOAPSIS_ALTITUDE: typing.ClassVar['AdditionalParametersKey'] = ...
    PERIAPSIS_ALTITUDE: typing.ClassVar['AdditionalParametersKey'] = ...
    INCLINATION: typing.ClassVar['AdditionalParametersKey'] = ...
    COV_CONFIDENCE: typing.ClassVar['AdditionalParametersKey'] = ...
    COV_CONFIDENCE_METHOD: typing.ClassVar['AdditionalParametersKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: AdditionalParameters) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (AdditionalParameters): container to fill
        
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
    def valueOf(name: str) -> 'AdditionalParametersKey':
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
    def values() -> typing.MutableSequence['AdditionalParametersKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AdditionalParametersKey c : AdditionalParametersKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdditionalParametersWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for additional parameters data block for CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    ...

class AltCovarianceType(java.lang.Enum['AltCovarianceType']):
    """
    Flag indicating the type of alternate covariance information provided.
    """
    XYZ: typing.ClassVar['AltCovarianceType'] = ...
    CSIG3EIGVEC3: typing.ClassVar['AltCovarianceType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'AltCovarianceType':
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
    def values() -> typing.MutableSequence['AltCovarianceType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AltCovarianceType c : AltCovarianceType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Cdm(org.orekit.files.ccsds.ndm.NdmConstituent['CdmHeader', 'CdmSegment']):
    """
    This class stores all the information of the Conjunction Data Message (CDM) File parsed by CdmParser. It contains the header and a list of segments each containing metadata and a list of data lines.
    
    Since:
        11.2
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
    def __init__(self, header: 'CdmHeader', segments: java.util.List['CdmSegment'], conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext):
        """
        Simple constructor.
        
        Parameters:
            header (CdmHeader): file header
            segments (List<CdmSegment> segments): file segments
            conventions (IERSConventions): IERS conventions
            dataContext (DataContext): used for creating frames, time scales, etc.
        
        
        """
        ...
    def getDataObject1(self) -> 'CdmData':
        """
        Get the file data.
        
        Returns:
            file data
        
        
        """
        ...
    def getDataObject2(self) -> 'CdmData':
        """
        Get the file data.
        
        Returns:
            file data
        
        
        """
        ...
    def getMetadataObject1(self) -> 'CdmMetadata':
        """
        Get the file metadata.
        
        Returns:
            file metadata
        
        
        """
        ...
    def getMetadataObject2(self) -> 'CdmMetadata':
        """
        Get the file metadata.
        
        Returns:
            file metadata
        
        
        """
        ...
    def getRelativeMetadata(self) -> 'CdmRelativeMetadata':
        """
        Get the file metadata.
        
        Returns:
            file metadata
        
        
        """
        ...
    def getUserDefinedParameters(self) -> org.orekit.files.ccsds.ndm.odm.UserDefined:
        """
        Get user defined parameters.
        
        This method will return null if the user defined block is not present in the CDM
        
        Returns:
            file data
        
        
        """
        ...

class CdmData(org.orekit.files.ccsds.section.Data):
    """
    Container for Conjunction Data Message data.
    
    Since:
        11.2
    """
    @typing.overload
    def __init__(self, commentsBlock: org.orekit.files.ccsds.section.CommentsContainer, ODParametersBlock: 'ODParameters', additionalParametersBlock: AdditionalParameters, stateVectorBlock: 'StateVector', covarianceMatrixBlock: 'RTNCovariance'): ...
    @typing.overload
    def __init__(self, commentsBlock: org.orekit.files.ccsds.section.CommentsContainer, ODParametersBlock: 'ODParameters', additionalParametersBlock: AdditionalParameters, stateVectorBlock: 'StateVector', covarianceMatrixBlock: 'RTNCovariance', additionalCovMetadata: AdditionalCovarianceMetadata): ...
    @typing.overload
    def __init__(self, commentsContainer: org.orekit.files.ccsds.section.CommentsContainer, oDParameters: 'ODParameters', additionalParameters: AdditionalParameters, stateVector: 'StateVector', rTNCovariance: 'RTNCovariance', sigmaEigenvectorsCovariance: 'SigmaEigenvectorsCovariance', additionalCovarianceMetadata: AdditionalCovarianceMetadata): ...
    @typing.overload
    def __init__(self, commentsContainer: org.orekit.files.ccsds.section.CommentsContainer, oDParameters: 'ODParameters', additionalParameters: AdditionalParameters, stateVector: 'StateVector', rTNCovariance: 'RTNCovariance', xYZCovariance: 'XYZCovariance', additionalCovarianceMetadata: AdditionalCovarianceMetadata): ...
    def getAdditionalCovMetadataBlock(self) -> AdditionalCovarianceMetadata:
        """
        Get the additional covariance metadata logical block.
        
        This method will return null if the block is not defined in the CDM.
        
        Returns:
            the additional covariance metadata logical block
        
        
        """
        ...
    def getAdditionalParametersBlock(self) -> AdditionalParameters:
        """
        Get the additional parameters logical block.
        
        Returns:
            additional parameters block (may be null)
        
        
        """
        ...
    def getComments(self) -> java.util.List[str]:
        """
        Get the comments.
        
        Returns:
            comments
        
        
        """
        ...
    def getODParametersBlock(self) -> 'ODParameters':
        """
        Get the OD parameters logical block.
        
        Returns:
            OD parameters block (may be null)
        
        
        """
        ...
    def getRTNCovarianceBlock(self) -> 'RTNCovariance':
        """
        Get the covariance matrix logical block.
        
        The RTN Covariance Matrix is provided in the 9×9 Lower Triangular Form. All parameters of the 6×6 position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        
        Returns:
            covariance matrix block
        
        
        """
        ...
    def getSig3EigVec3CovarianceBlock(self) -> 'SigmaEigenvectorsCovariance':
        """
        Get the Sigma / Eigenvector covariance logical block.
        
        This block is not mandatory and on condition that ALT_COV_TYPE = CSIG3EIGVEC3.
        
        This method will return null if the block is not defined in the CDM.
        
        Returns:
            the Sigma / Eigenvector covariance block
        
        
        """
        ...
    def getStateVectorBlock(self) -> 'StateVector':
        """
        Get the state vector logical block.
        
        Returns:
            state vector block
        
        
        """
        ...
    def getUserDefinedBlock(self) -> org.orekit.files.ccsds.ndm.odm.UserDefined:
        """
        Get the user defined logical block.
        
        This method will return null if the block is not defined in the CDM.
        
        Returns:
            the additional covariance metadata logical block
        
        
        """
        ...
    def getXYZCovarianceBlock(self) -> 'XYZCovariance':
        """
        Get the Covariance Matrix in the XYZ Coordinate Frame (defined by value of ALT_COV_REF_FRAME).
        
        This block is not mandatory and on condition that ALT_COV_TYPE = XYZ.
        
        This method will return null if the block is not defined in the CDM.
        
        Returns:
            XYZ covariance matrix block
        
        
        """
        ...
    def setAdditionalParametersBlock(self, additionalParametersBlock: AdditionalParameters) -> None:
        """
        Set the additional parameters logical block.
        
        Parameters:
            additionalParametersBlock (AdditionalParameters): the additional parameters logical block
        
        
        """
        ...
    def setCovarianceMatrixBlock(self, covarianceMatrixBlock: 'RTNCovariance') -> None:
        """
        Set the additional covariance metadata logical block.
        
        Parameters:
            covarianceMatrixBlock (RTNCovariance): the additional covariance metadata logical block
        
        
        """
        ...
    def setODParametersBlock(self, ODParametersBlock: 'ODParameters') -> None:
        """
        Set the OD parameters logical block.
        
        Parameters:
            ODParametersBlock (ODParameters): the OD Parameters logical block
        
        
        """
        ...
    def setUserDefinedBlock(self, userDefinedBlock: org.orekit.files.ccsds.ndm.odm.UserDefined) -> None:
        """
        Set the user defined logical block.
        
        This block is added at the end of the CDM parsing as common to both Object 1 and 2.
        
        Parameters:
            userDefinedBlock (UserDefined): the user defined block to set
        
        
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

class CdmHeader(org.orekit.files.ccsds.section.Header):
    """
    Header of a CCSDS Conjunction Data Message.
    
    Since:
        11.2
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    def getMessageFor(self) -> str:
        """
        Get the spacecraft name for which the CDM is provided stored in MESSAGE_FOR key.
        
        Returns:
            the spacecraft name for which the CDM is provided.
        
        
        """
        ...
    def setMessageFor(self, spacecraftNames: str) -> None:
        """
        Set the spacecraft name for which the CDM is provided stored in MESSAGE_FOR key.
        
        Parameters:
            spacecraftNames (String): the spacecraft name for which the CDM is provided.
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class Header
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class CdmHeaderKey(java.lang.Enum['CdmHeaderKey']):
    """
    Keywords allowed in CdmHeader.
    
    Since:
        11.2
    """
    MESSAGE_FOR: typing.ClassVar['CdmHeaderKey'] = ...
    CLASSIFICATION: typing.ClassVar['CdmHeaderKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, header: CdmHeader) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            header (CdmHeader): header to fill
        
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
    def valueOf(name: str) -> 'CdmHeaderKey':
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
    def values() -> typing.MutableSequence['CdmHeaderKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CdmHeaderKey c : CdmHeaderKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmHeaderProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    ProcessingState for CdmHeader.
    
    Since:
        11.2
    """
    def __init__(self, parser: 'CdmParser'):
        """
        Simple constructor.
        
        Parameters:
            parser (CdmParser): parser for the complete message
        
        
        """
        ...
    def processToken(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
        Process one token.
        
        Specified by: processToken in interface ProcessingState
        
        Parameters:
            token (ParseToken): token to process
        
        Returns:
            true if token was processed, false otherwise
        
        
        """
        ...

class CdmMessageWriter(org.orekit.files.ccsds.utils.generation.MessageWriter[CdmHeader, 'CdmSegment', Cdm]):
    """
    Cdm message writer.
    
    Since:
        11.2
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
    def writeFooter(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None:
        """
        Write footer for the file.
        
        Specified by: writeFooter in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeHeader(self, generator: org.orekit.files.ccsds.utils.generation.Generator, header: CdmHeader) -> None:
        """
        Write header for the file.
        
        Specified by: writeHeader in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            header (CdmHeader): header to write (creation date and originator will be added if missing)
        
        Raises:
            IOException: if the stream cannot write to stream
        
        
        """
        ...
    def writeRelativeMetadataContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, formatVersion: float, relativeMetadata: 'CdmRelativeMetadata') -> None:
        """
        Write RelativeMetadata part only once after header.
        
        Parameters:
            generator (Generator): generator to use for producing output
            formatVersion (double): format version to use
            relativeMetadata (CdmRelativeMetadata): relative metadata to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...
    def writeSegment(self, generator: org.orekit.files.ccsds.utils.generation.Generator, segment: 'CdmSegment') -> None:
        """
        Write one segment.
        
        Specified by: writeSegment in interface MessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            segment (CdmSegment): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, formatVersion: float, segment: org.orekit.files.ccsds.section.Segment['CdmMetadata', CdmData]) -> None:
        """
        Write one segment content (without XML wrapping).
        
        Parameters:
            generator (Generator): generator to use for producing output
            formatVersion (double): format version to use
            segment (Segment<CdmMetadata, CdmData> segment): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...

class CdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    This class gathers the meta-data present in the Conjunction Data Message (CDM).
    
    Since:
        11.2
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext, frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def getAdmMsgLink(self) -> str:
        """
        Get the unique identifier of Attitude Data Message(s) that are linked (relevant) to this Conjunction Data Message.
        
        Returns:
            the admMsgLink
        
        
        """
        ...
    def getAltCovFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame in which the alternative covariance data is given.
        
        Returns:
            alternative covariance reference frame.
        
        Since:
            13.1.5
        
        Also see:
            getAltCovType,
            getAltCovRefFrame
        
        
        """
        ...
    def getAltCovRefFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get the value of ALT_COV_REF_FRAME as an Orekit Frame.
        
        Returns:
            the reference frame
        
        
        """
        ...
    def getAltCovType(self) -> AltCovarianceType:
        """
        Get the flag indicating the type of alternate covariance information provided.
        
        Returns:
            the altCovType
        
        
        """
        ...
    def getAtmosphericModel(self) -> str:
        """
        Get name of atmospheric model.
        
        Returns:
            name of atmospheric model
        
        
        """
        ...
    def getCatalogName(self) -> str:
        """
        Get the satellite catalog used for the object.
        
        Returns:
            the catalog name
        
        
        """
        ...
    def getCovarianceMethod(self) -> 'CovarianceMethod':
        """
        Get the method name used to calculate covariance during OD.
        
        Returns:
            the name of covariance calculation method
        
        
        """
        ...
    def getCovarianceSource(self) -> str:
        """
        Get the source of the covariance data.
        
        Returns:
            the covarianceSource
        
        
        """
        ...
    def getEarthTides(self) -> org.orekit.files.ccsds.definitions.YesNoUnknown:
        """
        Get Enum YesNoUnknown that indicates if Earth and ocean tides are taken into account or not.
        
        Returns:
            YesNoUnknown
        
        
        """
        ...
    def getEphemName(self) -> str:
        """
        Get the unique name of the external ephemeris used for OD.
        
        Returns:
            the name of ephemeris used
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame in which data are given: used for state vector and Keplerian elements data (and for the covariance reference frame if none is given).
        
        Returns:
            the reference frame
        
        
        """
        ...
    def getGravityDegree(self) -> int:
        """
        Get degree of the gravity model.
        
        Returns:
            degree of the gravity model
        
        
        """
        ...
    def getGravityModel(self) -> str:
        """
        Get gravity model name.
        
        Returns:
            gravity model name
        
        
        """
        ...
    def getGravityOrder(self) -> int:
        """
        Get order of the gravity model.
        
        Returns:
            order of the gravity model
        
        
        """
        ...
    def getInternationalDes(self) -> str:
        """
        Get the international designator for the object.
        
        Returns:
            the international designator
        
        
        """
        ...
    def getIntrackThrust(self) -> org.orekit.files.ccsds.definitions.YesNoUnknown:
        """
        Get Enum YesNoUnknown that indicates if intrack thrust modeling was into account or not.
        
        Returns:
            YesNoUnknown
        
        
        """
        ...
    def getManeuverable(self) -> 'Maneuvrable':
        """
        Get the ability of object to maneuver or not.
        
        Returns:
            the ability to maneuver
        
        
        """
        ...
    def getNBodyPerturbations(self) -> java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]:
        """
        Get n-body perturbation bodies.
        
        Returns:
            n-body perturbation bodies
        
        
        """
        ...
    def getObject(self) -> str:
        """
        Get the object name for which metadata are given.
        
        Returns:
            the object name
        
        
        """
        ...
    def getObjectDesignator(self) -> str:
        """
        Get the object satellite catalog designator for which metadata are given.
        
        Returns:
            the satellite catalog designator for the object
        
        
        """
        ...
    def getObjectName(self) -> str:
        """
        Get the spacecraft name for the object.
        
        Returns:
            the spacecraft name
        
        
        """
        ...
    def getObjectType(self) -> org.orekit.files.ccsds.ndm.odm.ocm.ObjectType:
        """
        Get the type of object.
        
        Returns:
            the object type
        
        
        """
        ...
    def getObsBeforeNextMessage(self) -> org.orekit.files.ccsds.definitions.YesNoUnknown:
        """
        Get the flag indicating whether new tracking observations are anticipated prior to the issue of the next CDM associated with the event specified by CONJUNCTION_ID.
        
        Returns:
            the obsBeforeNextMessage
        
        
        """
        ...
    def getOdmMsgLink(self) -> str:
        """
        Get the unique identifier of Orbit Data Message(s) that are linked (relevant) to this Conjunction Data Message.
        
        Returns:
            the odmMsgLink
        
        
        """
        ...
    def getOperatorContactPosition(self) -> str:
        """
        Get the contact position of the owner / operator of the object.
        
        Returns:
            the contact position
        
        
        """
        ...
    def getOperatorEmail(self) -> str:
        """
        Get the email of the operator of the object.
        
        Returns:
            the operator email
        
        
        """
        ...
    def getOperatorOrganization(self) -> str:
        """
        Get the contact organisation of the object.
        
        Returns:
            the contact organisation
        
        
        """
        ...
    def getOperatorPhone(self) -> str:
        """
        Get the contact phone of the operator of the object.
        
        Returns:
            the operator phone
        
        
        """
        ...
    def getOrbitCenter(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
        Get the central body for object 1 and 2.
        
        Returns:
            the name of the central body
        
        
        """
        ...
    def getRefFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
        Get the value of REF_FRAME as an Orekit Frame. The ORBIT_CENTER key word has not been applied yet, so the returned frame may not correspond to the reference frame of the data in the file.
        
        Returns:
            the reference frame
        
        
        """
        ...
    def getRelativeMetadata(self) -> 'CdmRelativeMetadata':
        """
        Get the relative metadata following header, they are the common metadata for the CDM.
        
        Returns:
            relative metadata
        
        
        """
        ...
    def getSolarRadiationPressure(self) -> org.orekit.files.ccsds.definitions.YesNoUnknown:
        """
        Get Enum YesNoUnknown that indicates if Solar Radiation Pressure is taken into account or not.
        
        Returns:
            YesNoUnknown
        
        
        """
        ...
    def setAdmMsgLink(self, admMsgLink: str) -> None:
        """
        Set the unique identifier of Attitude Data Message(s) that are linked (relevant) to this Conjunction Data Message.
        
        Parameters:
            admMsgLink (String): the admMsgLink to set
        
        
        """
        ...
    def setAltCovRefFrame(self, altCovRefFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set the name of the reference frame in which the alternate covariance data are given.
        
        Parameters:
            altCovRefFrame (FrameFacade): alternate covariance reference frame
        
        
        """
        ...
    def setAltCovType(self, altCovType: AltCovarianceType) -> None:
        """
        Set the flag indicating the type of alternate covariance information provided.
        
        Parameters:
            altCovType (AltCovarianceType): the altCovType to set
        
        
        """
        ...
    def setAtmosphericModel(self, atmosphericModel: str) -> None:
        """
        Set name of atmospheric model.
        
        Parameters:
            atmosphericModel (String): name of atmospheric model
        
        
        """
        ...
    def setCatalogName(self, catalogName: str) -> None:
        """
        Set the satellite catalog name used for object.
        
        Parameters:
            catalogName (String): for the spacecraft to be set
        
        
        """
        ...
    def setCovarianceMethod(self, covarianceMethod: 'CovarianceMethod') -> None:
        """
        Set the method name used to calculate covariance during OD.
        
        Parameters:
            covarianceMethod (CovarianceMethod): method name for covariance calculation
        
        
        """
        ...
    def setCovarianceSource(self, covarianceSource: str) -> None:
        """
        Set the source of the covariance data.
        
        Parameters:
            covarianceSource (String): the covarianceSource to set
        
        
        """
        ...
    def setEarthTides(self, EarthTides: org.orekit.files.ccsds.definitions.YesNoUnknown) -> None:
        """
        Set Enum YesNoUnknown that indicates if Earth and ocean tides are taken into account or not.
        
        Parameters:
            EarthTides (YesNoUnknown): YesNoUnknown
        
        
        """
        ...
    def setEphemName(self, ephemName: str) -> None:
        """
        Set the name of external ephemeris used for OD.
        
        Parameters:
            ephemName (String): me of external ephemeris used
        
        
        """
        ...
    def setGravityModel(self, name: str, degree: int, order: int) -> None:
        """
        Set gravity model.
        
        Parameters:
            name (String): name of the model
            degree (int): degree of the model
            order (int): order of the model
        
        
        """
        ...
    def setInternationalDes(self, internationalDes: str) -> None:
        """
        Set the international designator used for object.
        
        Parameters:
            internationalDes (String): for the object to be set
        
        
        """
        ...
    def setIntrackThrust(self, IntrackThrustModeled: org.orekit.files.ccsds.definitions.YesNoUnknown) -> None:
        """
        Set boolean that indicates if intrack thrust modeling was into account or not.
        
        Parameters:
            IntrackThrustModeled (YesNoUnknown): YesNoUnknown
        
        
        """
        ...
    def setManeuverable(self, maneuverable: 'Maneuvrable') -> None:
        """
        Set the object maneuver ability.
        
        Parameters:
            maneuverable (Maneuvrable): ability to maneuver
        
        
        """
        ...
    def setNBodyPerturbations(self, nBody: java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]) -> None:
        """
        Set n-body perturbation bodies.
        
        Parameters:
            nBody (List<BodyFacade> nBody): n-body perturbation bodies
        
        
        """
        ...
    def setObject(self, object: str) -> None:
        """
        Set the object name for which metadata are given.
        
        Parameters:
            object (String): = object 1 or 2 to be set
        
        
        """
        ...
    def setObjectDesignator(self, objectDesignator: str) -> None:
        """
        Set the satellite designator for the object for which metadata are given.
        
        Parameters:
            objectDesignator (String): for the spacecraft to be set
        
        
        """
        ...
    def setObjectName(self, objectName: str) -> None:
        """
        Set the spacecraft name used for object.
        
        Parameters:
            objectName (String): for the spacecraft to be set
        
        
        """
        ...
    def setObjectType(self, objectType: org.orekit.files.ccsds.ndm.odm.ocm.ObjectType) -> None:
        """
        Set the type of object.
        
        Parameters:
            objectType (ObjectType): type of object
        
        
        """
        ...
    def setObsBeforeNextMessage(self, obsBeforeNextMessage: org.orekit.files.ccsds.definitions.YesNoUnknown) -> None:
        """
        Set the flag indicating whether new tracking observations are anticipated prior to the issue of the next CDM associated with the event specified by CONJUNCTION_ID.
        
        Parameters:
            obsBeforeNextMessage (YesNoUnknown): the obsBeforeNextMessage to set
        
        
        """
        ...
    def setOdmMsgLink(self, odmMsgLink: str) -> None:
        """
        Set the unique identifier of Orbit Data Message(s) that are linked (relevant) to this Conjunction Data Message.
        
        Parameters:
            odmMsgLink (String): the odmMsgLink to set
        
        
        """
        ...
    def setOperatorContactPosition(self, opContact: str) -> None:
        """
        Set the contact position for the object owner / operator.
        
        Parameters:
            opContact (String): for the object to be set
        
        
        """
        ...
    def setOperatorEmail(self, operatorEmail: str) -> None:
        """
        Set the object operator email.
        
        Parameters:
            operatorEmail (String): operator email for the object to be set
        
        
        """
        ...
    def setOperatorOrganization(self, operatorOrganization: str) -> None:
        """
        Set the contact organisation of the object.
        
        Parameters:
            operatorOrganization (String): contact organisation for the object to be set
        
        
        """
        ...
    def setOperatorPhone(self, operatorPhone: str) -> None:
        """
        Set the operator phone of the object.
        
        Parameters:
            operatorPhone (String): contact phone for the object to be set
        
        
        """
        ...
    def setOrbitCenter(self, orbitCenter: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
        Set the central body name for object 1 and 2.
        
        Parameters:
            orbitCenter (BodyFacade): name of the central body
        
        
        """
        ...
    def setRefFrame(self, refFrame: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
        Set the name of the reference frame in which the state vector data are given.
        
        Parameters:
            refFrame (FrameFacade): reference frame
        
        
        """
        ...
    def setRelativeMetadata(self, relativeMetadata: 'CdmRelativeMetadata') -> None:
        """
        Set the relative metadata following header, they are the common metadata for the CDM.
        
        Parameters:
            relativeMetadata (CdmRelativeMetadata): relative metadata
        
        
        """
        ...
    def setSolarRadiationPressure(self, isSolRadPressure: org.orekit.files.ccsds.definitions.YesNoUnknown) -> None:
        """
        Set Enum that indicates if Solar Radiation Pressure is taken into account or not.
        
        Parameters:
            isSolRadPressure (YesNoUnknown): YesNoUnknown
        
        
        """
        ...
    def validate(self, version: float) -> None:
        """
        Check is all mandatory entries have been initialized.
        
        This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
        Specified by: validate in interface Section
        
        Overrides: validate in class Metadata
        
        Parameters:
            version (double): format version
        
        
        """
        ...

class CdmMetadataKey(java.lang.Enum['CdmMetadataKey']):
    """
    Keys for CdmMetadata entries.
    
    Since:
        11.2
    """
    OBJECT: typing.ClassVar['CdmMetadataKey'] = ...
    OBJECT_DESIGNATOR: typing.ClassVar['CdmMetadataKey'] = ...
    CATALOG_NAME: typing.ClassVar['CdmMetadataKey'] = ...
    OBJECT_NAME: typing.ClassVar['CdmMetadataKey'] = ...
    INTERNATIONAL_DESIGNATOR: typing.ClassVar['CdmMetadataKey'] = ...
    OBJECT_TYPE: typing.ClassVar['CdmMetadataKey'] = ...
    OPERATOR_CONTACT_POSITION: typing.ClassVar['CdmMetadataKey'] = ...
    OPERATOR_ORGANIZATION: typing.ClassVar['CdmMetadataKey'] = ...
    OPERATOR_PHONE: typing.ClassVar['CdmMetadataKey'] = ...
    OPERATOR_EMAIL: typing.ClassVar['CdmMetadataKey'] = ...
    ODM_MSG_LINK: typing.ClassVar['CdmMetadataKey'] = ...
    ADM_MSG_LINK: typing.ClassVar['CdmMetadataKey'] = ...
    EPHEMERIS_NAME: typing.ClassVar['CdmMetadataKey'] = ...
    OBS_BEFORE_NEXT_MESSAGE: typing.ClassVar['CdmMetadataKey'] = ...
    COVARIANCE_METHOD: typing.ClassVar['CdmMetadataKey'] = ...
    COVARIANCE_SOURCE: typing.ClassVar['CdmMetadataKey'] = ...
    MANEUVERABLE: typing.ClassVar['CdmMetadataKey'] = ...
    ORBIT_CENTER: typing.ClassVar['CdmMetadataKey'] = ...
    REF_FRAME: typing.ClassVar['CdmMetadataKey'] = ...
    ALT_COV_TYPE: typing.ClassVar['CdmMetadataKey'] = ...
    ALT_COV_REF_FRAME: typing.ClassVar['CdmMetadataKey'] = ...
    GRAVITY_MODEL: typing.ClassVar['CdmMetadataKey'] = ...
    ATMOSPHERIC_MODEL: typing.ClassVar['CdmMetadataKey'] = ...
    N_BODY_PERTURBATIONS: typing.ClassVar['CdmMetadataKey'] = ...
    SOLAR_RAD_PRESSURE: typing.ClassVar['CdmMetadataKey'] = ...
    EARTH_TIDES: typing.ClassVar['CdmMetadataKey'] = ...
    INTRACK_THRUST: typing.ClassVar['CdmMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: CdmMetadata) -> bool:
        """
        Process an token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (CdmMetadata): container to fill
        
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
    def valueOf(name: str) -> 'CdmMetadataKey':
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
    def values() -> typing.MutableSequence['CdmMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CdmMetadataKey c : CdmMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for Metadata for CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    def __init__(self, metadata: CdmMetadata):
        """
        Simple constructor.
        
        Parameters:
            metadata (CdmMetadata): metadata to write
        
        
        """
        ...

class CdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[CdmHeader, Cdm, 'CdmParser']):
    """
    Base class for Conjunction Data Message parsers.
    
    Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until the message is complete and the parseMessage method has returned. This implies that parsers should not be used in a multi-thread context. The recommended way to use parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
    Since:
        11.2
    """
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior, filters: typing.Union[typing.List[java.util.function.Function[org.orekit.files.ccsds.utils.lexical.ParseToken, java.util.List[org.orekit.files.ccsds.utils.lexical.ParseToken]]], jpype.JArray], frameMapper: org.orekit.files.ccsds.definitions.CcsdsFrameMapper): ...
    def build(self) -> Cdm:
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
    def getHeader(self) -> CdmHeader:
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

class CdmRelativeMetadata:
    """
    This class gathers the relative meta-data present in the Conjunction Data Message (CDM).
    
    Since:
        11.2
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def addComment(self, comments: str) -> None:
        """
        Set comment for relative metadata.
        
        Parameters:
            comments (String): to be set
        
        
        """
        ...
    def checkNotNull(self, field: typing.Any, key: java.lang.Enum[typing.Any]) -> None:
        """
        Complain if a field is null.
        
        Parameters:
            field (Object): field to check
            key (Enum<?> key): key associated with the field
        
        
        """
        ...
    def checkScreenVolumeConditions(self) -> None:
        """
        Check screen volume conditions.
        
        The method verifies that all keys are present. Otherwise, an exception is thrown.
        """
        ...
    def getApproachAngle(self) -> float:
        """
        Get the approach angle computed between Objects 1 and 2 in the RTN coordinate frame relative to object 1.
        
        Returns:
            the approachAngle
        
        
        """
        ...
    def getCollisionPercentile(self) -> typing.MutableSequence[int]:
        """
        Get the array of 1 to n elements indicating the percentile(s) for which estimates of the collision probability are provided in the COLLISION_PROBABILITY variable.
        
        Returns:
            the collisionPercentile
        
        
        """
        ...
    def getCollisionProbaMethod(self) -> org.orekit.files.ccsds.definitions.PocMethodFacade:
        """
        Get the method that was used to calculate the collision probability.
        
        Returns:
            method to calculate probability of collision
        
        
        """
        ...
    def getCollisionProbability(self) -> float:
        """
        Get the probability (between 0.0 and 1.0) that Object1 and Object2 will collide.
        
        Returns:
            probability of collision
        
        
        """
        ...
    def getComment(self) -> java.util.List[str]:
        """
        Get comment for relative metadata.
        
        Returns:
            the time system
        
        
        """
        ...
    def getConjunctionId(self) -> str:
        """
        Get the Originator’s ID that uniquely identifies the conjunction to which the message refers.
        
        Returns:
            the conjunction id
        
        
        """
        ...
    def getMahalanobisDistance(self) -> float:
        """
        Get the Mahalanobis Distance. The length of the relative position vector, normalized to one-sigma dispersions of the combined error covariance in the direction of the relative position vector.
        
        Returns:
            the mahalanobisDistance
        
        
        """
        ...
    def getMaxCollisionProbability(self) -> float:
        """
        Get max collision probability.
        
        Returns:
            the max collision probability
        
        
        """
        ...
    def getMaxCollisionProbabilityMethod(self) -> org.orekit.files.ccsds.definitions.PocMethodFacade:
        """
        Get max collision probability method.
        
        Returns:
            the max collision probability method
        
        
        """
        ...
    def getMissDistance(self) -> float:
        """
        Get the norm of relative position vector at TCA.
        
        Returns:
            the miss distance (in m)
        
        
        """
        ...
    def getNextMessageEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get Scheduled UTC epoch of the next CDM associated with the event identified by CONJUNCTION_ID.
        
        Returns:
            the nextMessageEpoch
        
        
        """
        ...
    def getPreviousMessageEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the UTC epoch of the previous CDM issued for the event identified by CONJUNCTION_ID.
        
        Returns:
            the previousMessageEpoch
        
        
        """
        ...
    def getPreviousMessageId(self) -> str:
        """
        Get the ID of previous CDM issued for event identified by CONJUNCTION_ID.
        
        Returns:
            the previousMessageId
        
        
        """
        ...
    def getRelativePosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the Object2’s position vector relative to Object1's at TCA in RTN frame, getX for R component, getY for T component, getZ for N component.
        
        Returns:
            the relative position vector at TCA (in m)
        
        
        """
        ...
    def getRelativeSpeed(self) -> float:
        """
        Get the norm of relative velocity vector at TCA.
        
        Returns:
            the relative speed at TCA (in m/s)
        
        
        """
        ...
    def getRelativeVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the Object2’s velocity vector relative to Object1's at TCA in RTN frame, getX for R component, getY for T component, getZ for N component.
        
        Returns:
            the relative speed vector at TCA (in m/s)
        
        
        """
        ...
    def getScreenEntryTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the time in UTC when Object2 enters the screening volume.
        
        Returns:
            time in UTC when Object2 enters the screening volume
        
        
        """
        ...
    def getScreenExitTime(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the time in UTC when Object2 exits the screening volume.
        
        Returns:
            time in UTC when Object2 exits the screening volume
        
        
        """
        ...
    def getScreenPcThreshold(self) -> float:
        """
        Get the collision probability screening threshold used to identify this conjunction.
        
        Returns:
            the screenPcThreshold
        
        
        """
        ...
    def getScreenType(self) -> 'ScreenType':
        """
        Get the type of screening to be used.
        
        Returns:
            the screenType
        
        
        """
        ...
    def getScreenVolumeFrame(self) -> 'ScreenVolumeFrame':
        """
        Get the name of the Object1 centered reference frame in which the screening volume data are given.
        
        Returns:
            name of screen volume frame
        
        
        """
        ...
    def getScreenVolumeRadius(self) -> float:
        """
        Get the screen volume radius.
        
        Returns:
            the screen volume radius
        
        
        """
        ...
    def getScreenVolumeShape(self) -> 'ScreenVolumeShape':
        """
        Get the shape of the screening volume.
        
        Returns:
            shape of the screening volume
        
        
        """
        ...
    def getScreenVolumeX(self) -> float:
        """
        Get the R or T (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding frame.
        
        Returns:
            first component size of the screening volume (in m)
        
        
        """
        ...
    def getScreenVolumeY(self) -> float:
        """
        Get the T or V (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding frame.
        
        Returns:
            second component size of the screening volume (in m)
        
        
        """
        ...
    def getScreenVolumeZ(self) -> float:
        """
        Get the N component size of the screening volume in the corresponding frame.
        
        Returns:
            third component size of the screening volume (in m)
        
        
        """
        ...
    def getSefiCollisionProbability(self) -> float:
        """
        Get the Space Environment Fragmentation Impact probability.
        
        Returns:
            the Space Environment Fragmentation Impact probability
        
        
        """
        ...
    def getSefiCollisionProbabilityMethod(self) -> org.orekit.files.ccsds.definitions.PocMethodFacade:
        """
        Get the Space Environment Fragmentation Impact probability method.
        
        Returns:
            the Space Environment Fragmentation Impact probability method
        
        
        """
        ...
    def getSefiFragmentationModel(self) -> str:
        """
        Get the Space Environment Fragmentation Impact fragmentation model.
        
        Returns:
            the Space Environment Fragmentation Impact fragmentation model
        
        
        """
        ...
    def getStartScreenPeriod(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start time in UTC of the screening period for the conjunction assessment.
        
        Returns:
            start time in UTC of the screening period
        
        
        """
        ...
    def getStopScreenPeriod(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the stop time in UTC of the screening period for the conjunction assessment.
        
        Returns:
            stop time in UTC of the screening period
        
        
        """
        ...
    def getTca(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date and time in UTC of the closest approach.
        
        Returns:
            time of closest approach
        
        
        """
        ...
    def getTimeSystem(self) -> org.orekit.files.ccsds.definitions.TimeSystem:
        """
        Get the Time System that: for CDM, is used for relative metadata, metadata, OD parameters, state vector. In CDM all date are given in UTC.
        
        Returns:
            the time system
        
        
        """
        ...
    def setApproachAngle(self, approachAngle: float) -> None:
        """
        Set the approach angle computed between Objects 1 and 2 in the RTN coordinate frame relative to object 1.
        
        Parameters:
            approachAngle (double): the approachAngle to set
        
        
        """
        ...
    def setCollisionPercentile(self, collisionPercentile: typing.Union[typing.List[int], jpype.JArray]) -> None:
        """
        Set the array of 1 to n elements indicating the percentile(s) for which estimates of the collision probability are provided in the COLLISION_PROBABILITY variable.
        
        Parameters:
            collisionPercentile (int[]): the collisionPercentile to set
        
        
        """
        ...
    def setCollisionProbaMethod(self, collisionProbaMethod: org.orekit.files.ccsds.definitions.PocMethodFacade) -> None:
        """
        Set the method that was used to calculate the collision probability.
        
        Parameters:
            collisionProbaMethod (PocMethodFacade): method used to calculate probability of collision
        
        
        """
        ...
    def setCollisionProbability(self, collisionProbability: float) -> None:
        """
        Set the probability (between 0.0 and 1.0) that Object1 and Object2 will collide.
        
        Parameters:
            collisionProbability (double): first component size of the screening volume
        
        
        """
        ...
    def setConjunctionId(self, conjunctionId: str) -> None:
        """
        Set the Originator’s ID that uniquely identifies the conjunction to which the message refers.
        
        Parameters:
            conjunctionId (String): the conjunction id to be set
        
        
        """
        ...
    def setMahalanobisDistance(self, mahalanobisDistance: float) -> None:
        """
        Set the Mahalanobis Distance. The length of the relative position vector, normalized to one-sigma dispersions of the combined error covariance in the direction of the relative position vector.
        
        Parameters:
            mahalanobisDistance (double): the mahalanobisDistance to set
        
        
        """
        ...
    def setMaxCollisionProbability(self, maxCollisionProbability: float) -> None:
        """
        Set max collision probability.
        
        Parameters:
            maxCollisionProbability (double): the max collision probability to set
        
        
        """
        ...
    def setMaxCollisionProbabilityMethod(self, pocMethodFacade: org.orekit.files.ccsds.definitions.PocMethodFacade) -> None:
        """
        Set max collision probability method.
        
        Parameters:
            pocMethodFacade (PocMethodFacade): the max collision probability method to set
        
        
        """
        ...
    def setMissDistance(self, missDistance: float) -> None:
        """
        Set the norm of relative position vector at TCA.
        
        Parameters:
            missDistance (double): the miss distance to be set (in m)
        
        
        """
        ...
    def setNextMessageEpoch(self, nextMessageEpoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set Scheduled UTC epoch of the next CDM associated with the event identified by CONJUNCTION_ID.
        
        Parameters:
            nextMessageEpoch (AbsoluteDate): the nextMessageEpoch to set
        
        
        """
        ...
    def setPreviousMessageEpoch(self, previousMessageEpoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the UTC epoch of the previous CDM issued for the event identified by CONJUNCTION_ID.
        
        Parameters:
            previousMessageEpoch (AbsoluteDate): the previousMessageEpoch to set
        
        
        """
        ...
    def setPreviousMessageId(self, previousMessageId: str) -> None:
        """
        Set the ID of previous CDM issued for event identified by CONJUNCTION_ID.
        
        Parameters:
            previousMessageId (String): the previousMessageId to set
        
        
        """
        ...
    def setRelativePositionN(self, relativePositionN: float) -> None:
        """
        Set the N component of Object2’s position relative to Object1’s in RTN frame.
        
        Parameters:
            relativePositionN (double): the N component (in m) of Object2’s position relative to Object1’s
        
        
        """
        ...
    def setRelativePositionR(self, relativePositionR: float) -> None:
        """
        Set the R component of Object2’s position relative to Object1’s in RTN frame.
        
        Parameters:
            relativePositionR (double): the R component (in m) of Object2’s position relative to Object1’s
        
        
        """
        ...
    def setRelativePositionT(self, relativePositionT: float) -> None:
        """
        Set the T component of Object2’s position relative to Object1’s in RTN frame.
        
        Parameters:
            relativePositionT (double): the T component (in m) of Object2’s position relative to Object1’s
        
        
        """
        ...
    def setRelativeSpeed(self, relativeSpeed: float) -> None:
        """
        Set the norm of relative velocity vector at TCA.
        
        Parameters:
            relativeSpeed (double): the relative speed (in m/s) at TCA to be set
        
        
        """
        ...
    def setRelativeVelocityN(self, relativeVelocityN: float) -> None:
        """
        Set the N component of Object2’s velocity relative to Object1’s in RTN frame.
        
        Parameters:
            relativeVelocityN (double): the N component (in m/s) of Object2’s velocity relative to Object1’s
        
        
        """
        ...
    def setRelativeVelocityR(self, relativeVelocityR: float) -> None:
        """
        Set the R component of Object2’s velocity relative to Object1’s in RTN frame.
        
        Parameters:
            relativeVelocityR (double): the R component (in m/s) of Object2’s velocity relative to Object1’s
        
        
        """
        ...
    def setRelativeVelocityT(self, relativeVelocityT: float) -> None:
        """
        Set the T component of Object2’s velocity relative to Object1’s in RTN frame.
        
        Parameters:
            relativeVelocityT (double): the T component (in m/s) of Object2’s velocity relative to Object1’s
        
        
        """
        ...
    def setScreenEntryTime(self, screenEntryTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the time in UTC when Object2 enters the screening volume.
        
        Parameters:
            screenEntryTime (AbsoluteDate): time in UTC when Object2 enters the screening volume
        
        
        """
        ...
    def setScreenExitTime(self, screenExitTime: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the time in UTC when Object2 exits the screening volume.
        
        Parameters:
            screenExitTime (AbsoluteDate): time in UTC when Object2 exits the screening volume
        
        
        """
        ...
    def setScreenPcThreshold(self, screenPcThreshold: float) -> None:
        """
        Set the collision probability screening threshold used to identify this conjunction.
        
        Parameters:
            screenPcThreshold (double): the screenPcThreshold to set
        
        
        """
        ...
    def setScreenType(self, screenType: 'ScreenType') -> None:
        """
        Set the type of screening to be used.
        
        Parameters:
            screenType (ScreenType): the screenType to set
        
        
        """
        ...
    def setScreenVolumeFrame(self, screenVolumeFrame: 'ScreenVolumeFrame') -> None:
        """
        Set the name of the Object1 centered reference frame in which the screening volume data are given.
        
        Parameters:
            screenVolumeFrame (ScreenVolumeFrame): name of screen volume frame
        
        
        """
        ...
    def setScreenVolumeRadius(self, screenVolumeRadius: float) -> None:
        """
        set the screen volume radius.
        
        Parameters:
            screenVolumeRadius (double): the screen volume radius to set
        
        
        """
        ...
    def setScreenVolumeShape(self, screenVolumeShape: 'ScreenVolumeShape') -> None:
        """
        Set the shape of the screening volume.
        
        Parameters:
            screenVolumeShape (ScreenVolumeShape): shape of the screening volume
        
        
        """
        ...
    def setScreenVolumeX(self, screenVolumeX: float) -> None:
        """
        Set the R or T (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding frame.
        
        Parameters:
            screenVolumeX (double): first component size of the screening volume (in m)
        
        
        """
        ...
    def setScreenVolumeY(self, screenVolumeY: float) -> None:
        """
        Set the T or V (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding frame.
        
        Parameters:
            screenVolumeY (double): second component size of the screening volume (in m)
        
        
        """
        ...
    def setScreenVolumeZ(self, screenVolumeZ: float) -> None:
        """
        Set the N component size of the screening volume in the corresponding frame.
        
        Parameters:
            screenVolumeZ (double): third component size of the screening volume (in m)
        
        
        """
        ...
    def setSefiCollisionProbability(self, sefiCollisionProbability: float) -> None:
        """
        Set the Space Environment Fragmentation Impact probability.
        
        Parameters:
            sefiCollisionProbability (double): the Space Environment Fragmentation Impact probability to set
        
        
        """
        ...
    def setSefiCollisionProbabilityMethod(self, pocMethodFacade: org.orekit.files.ccsds.definitions.PocMethodFacade) -> None:
        """
        Set the Space Environment Fragmentation Impact probability method.
        
        Parameters:
            pocMethodFacade (PocMethodFacade): the Space Environment Fragmentation Impact probability method to set
        
        
        """
        ...
    def setSefiFragmentationModel(self, sefiFragmentationModel: str) -> None:
        """
        Set the Space Environment Fragmentation Impact fragmentation model.
        
        Parameters:
            sefiFragmentationModel (String): the Space Environment Fragmentation Impact fragmentation model to set
        
        
        """
        ...
    def setStartScreenPeriod(self, startScreenPeriod: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the start time in UTC of the screening period for the conjunction assessment.
        
        Parameters:
            startScreenPeriod (AbsoluteDate): start time in UTC of the screening period to be set
        
        
        """
        ...
    def setStopScreenPeriod(self, stopScreenPeriod: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the stop time in UTC of the screening period for the conjunction assessment.
        
        Parameters:
            stopScreenPeriod (AbsoluteDate): stop time in UTC of the screening period to be set
        
        
        """
        ...
    def setTca(self, tca: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the date and time in UTC of the closest approach.
        
        Parameters:
            tca (AbsoluteDate): time of closest approach to be set
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.files.ccsds.definitions.TimeSystem) -> None:
        """
        Set the Time System that: for CDM, is used for relative metadata, metadata, OD parameters, state vector. In CDM all date are given in UTC.
        
        Parameters:
            timeSystem (TimeSystem): the time system to be set
        
        
        """
        ...
    def validate(self) -> None:
        """
        Check is all mandatory entries have been initialized.
        """
        ...

class CdmRelativeMetadataKey(java.lang.Enum['CdmRelativeMetadataKey']):
    """
    Keys for CdmRelativeMetadata entries.
    
    Since:
        11.2
    """
    CONJUNCTION_ID: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    TCA: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    MISS_DISTANCE: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    MAHALANOBIS_DISTANCE: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    RELATIVE_SPEED: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    RELATIVE_POSITION_R: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    RELATIVE_POSITION_T: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    RELATIVE_POSITION_N: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    RELATIVE_VELOCITY_R: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    RELATIVE_VELOCITY_T: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    RELATIVE_VELOCITY_N: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    APPROACH_ANGLE: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    START_SCREEN_PERIOD: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    STOP_SCREEN_PERIOD: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_VOLUME_FRAME: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_TYPE: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_VOLUME_SHAPE: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_VOLUME_RADIUS: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_VOLUME_X: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_VOLUME_Y: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_VOLUME_Z: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_ENTRY_TIME: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_EXIT_TIME: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SCREEN_PC_THRESHOLD: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    COLLISION_PERCENTILE: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    COLLISION_PROBABILITY: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    COLLISION_PROBABILITY_METHOD: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    COLLISION_MAX_PROBABILITY: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    COLLISION_MAX_PC_METHOD: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SEFI_COLLISION_PROBABILITY: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SEFI_COLLISION_PROBABILITY_METHOD: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    SEFI_FRAGMENTATION_MODEL: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    PREVIOUS_MESSAGE_ID: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    PREVIOUS_MESSAGE_EPOCH: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    NEXT_MESSAGE_EPOCH: typing.ClassVar['CdmRelativeMetadataKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: CdmRelativeMetadata) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (CdmRelativeMetadata): container to fill
        
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
    def valueOf(name: str) -> 'CdmRelativeMetadataKey':
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
    def values() -> typing.MutableSequence['CdmRelativeMetadataKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CdmRelativeMetadataKey c : CdmRelativeMetadataKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmSegment(org.orekit.files.ccsds.section.Segment[CdmMetadata, CdmData]):
    """
    This class stores the metadata and data for one object.
    
    Since:
        11.2
    """
    def __init__(self, metadata: CdmMetadata, data: CdmData):
        """
        Simple constructor.
        
        Parameters:
            metadata (CdmMetadata): segment metadata
            data (CdmData): segment data
        
        
        """
        ...

class CovarianceMethod(java.lang.Enum['CovarianceMethod']):
    """
    Maneuvrable possibilities used in CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    CALCULATED: typing.ClassVar['CovarianceMethod'] = ...
    DEFAULT: typing.ClassVar['CovarianceMethod'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'CovarianceMethod':
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
    def values() -> typing.MutableSequence['CovarianceMethod']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CovarianceMethod c : CovarianceMethod.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Maneuvrable(java.lang.Enum['Maneuvrable']):
    """
    Maneuvrable possibilities used in CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    YES: typing.ClassVar['Maneuvrable'] = ...
    NO: typing.ClassVar['Maneuvrable'] = ...
    N_A: typing.ClassVar['Maneuvrable'] = ...
    @staticmethod
    def getEnum(keyValue: str) -> 'Maneuvrable':
        """
        Get the enum entry corresponding to the given String.
        
        Parameters:
            keyValue (String): input Sring value
        
        Returns:
            the corresponding enum entry
        
        Raises:
            IllegalArgumentException: if there is no enum entry corresponding to the given String value
        
        
        """
        ...
    def getValue(self) -> str:
        """
        Get the String representation of the enum.
        
        Returns:
            the String representation of the enum
        
        
        """
        ...
    def toString(self) -> str:
        """
        .
        
        Overrides: Enum in class Enum
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'Maneuvrable':
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
    def values() -> typing.MutableSequence['Maneuvrable']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (Maneuvrable c : Maneuvrable.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ODParameters(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for OD parameters data block.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        11.2
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getActualOdSpan(self) -> float:
        """
        Get the actual OD time based on the observations available and the RECOMMENDED_OD_SPAN.
        
        Returns:
            the actual OD time (in days)
        
        
        """
        ...
    def getObsAvailable(self) -> int:
        """
        Get the number of observations available for the OD of the object.
        
        Returns:
            the number of observations available
        
        
        """
        ...
    def getObsUsed(self) -> int:
        """
        Get the number of observations accepted for the OD of the object.
        
        Returns:
            the number of observations used
        
        
        """
        ...
    def getOdEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the epoch of the orbit determination used for this message.
        
        Returns:
            the odEpoch the epoch of the orbit determination used for this message
        
        
        """
        ...
    def getRecommendedOdSpan(self) -> float:
        """
        Get the recommended OD time span calculated for the object.
        
        Returns:
            the recommended OD time span (in days) calculated for the object
        
        
        """
        ...
    def getResidualsAccepted(self) -> float:
        """
        Get the percentage of residuals accepted in the OD of the object (from 0 to 100).
        
        Returns:
            the percentage of residuals accepted in the OD
        
        
        """
        ...
    def getTimeLastObsEnd(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start of a time interval (UTC) that contains the time of the last accepted observation.
        
        Returns:
            the start of a time interval (UTC)
        
        
        """
        ...
    def getTimeLastObsStart(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the start of a time interval (UTC) that contains the time of the last accepted observation.
        
        Returns:
            the start of a time interval (UTC)
        
        
        """
        ...
    def getTracksAvailable(self) -> int:
        """
        Get the number of sensor tracks available for the OD of the object.
        
        Returns:
            the number of sensor tracks available
        
        
        """
        ...
    def getTracksUsed(self) -> int:
        """
        Get the number of sensor tracks used for the OD of the object.
        
        Returns:
            the number of sensor tracks used
        
        
        """
        ...
    def getWeightedRMS(self) -> float:
        """
        Get the weighted Root Mean Square (RMS) of the residuals from a batch least squares OD.
        
        Returns:
            the weighted Root Mean Square (RMS) of the residuals from a batch least squares OD
        
        
        """
        ...
    def setActualOdSpan(self, actualOdSpan: float) -> None:
        """
        Set the actual OD time based on the observations available and the RECOMMENDED_OD_SPAN.
        
        Parameters:
            actualOdSpan (double): the actual OD time (in days)
        
        
        """
        ...
    def setObsAvailable(self, obsAvailable: int) -> None:
        """
        Set the number of observations available for the OD of the object.
        
        Parameters:
            obsAvailable (int): the number of observations available
        
        
        """
        ...
    def setObsUsed(self, obsUsed: int) -> None:
        """
        Set the number of observations accepted for the OD of the object.
        
        Parameters:
            obsUsed (int): the number of observations used
        
        
        """
        ...
    def setOdEpoch(self, odEpoch: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the epoch of the orbit determination used for this message.
        
        Parameters:
            odEpoch (AbsoluteDate): the odEpoch to set
        
        
        """
        ...
    def setRecommendedOdSpan(self, recommendedOdSpan: float) -> None:
        """
        Set the recommended OD time span calculated for the object.
        
        Parameters:
            recommendedOdSpan (double): recommended OD time span (in days) calculated for the object
        
        
        """
        ...
    def setResidualsAccepted(self, residualsAccepted: float) -> None:
        """
        Set the percentage of residuals accepted in the OD of the object (from 0 to 100).
        
        Parameters:
            residualsAccepted (double): the percentage of residuals accepted in the OD to be set
        
        
        """
        ...
    def setTimeLastObsEnd(self, timeLastObsEnd: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the start of a time interval (UTC) that contains the time of the last accepted observation.
        
        Parameters:
            timeLastObsEnd (AbsoluteDate): the start of a time interval (UTC)
        
        
        """
        ...
    def setTimeLastObsStart(self, timeLastObsStart: org.orekit.time.AbsoluteDate) -> None:
        """
        Set the start of a time interval (UTC) that contains the time of the last accepted observation.
        
        Parameters:
            timeLastObsStart (AbsoluteDate): the start of a time interval (UTC)
        
        
        """
        ...
    def setTracksAvailable(self, tracksAvailable: int) -> None:
        """
        Set the number of sensor tracks available for the OD of the object.
        
        Parameters:
            tracksAvailable (int): the number of sensor tracks available
        
        
        """
        ...
    def setTracksUsed(self, tracksUsed: int) -> None:
        """
        Set the number of sensor tracks used for the OD of the object.
        
        Parameters:
            tracksUsed (int): the number of sensor tracks used
        
        
        """
        ...
    def setWeightedRMS(self, WeightedRMS: float) -> None:
        """
        Set the weighted Root Mean Square (RMS) of the residuals from a batch least squares OD.
        
        Parameters:
            WeightedRMS (double): the weighted Root Mean Square (RMS) of the residuals from a batch least squares OD
        
        
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

class ODParametersKey(java.lang.Enum['ODParametersKey']):
    """
    Keys for ODParameters entries.
    
    Since:
        11.2
    """
    COMMENT: typing.ClassVar['ODParametersKey'] = ...
    TIME_LASTOB_START: typing.ClassVar['ODParametersKey'] = ...
    TIME_LASTOB_END: typing.ClassVar['ODParametersKey'] = ...
    RECOMMENDED_OD_SPAN: typing.ClassVar['ODParametersKey'] = ...
    ACTUAL_OD_SPAN: typing.ClassVar['ODParametersKey'] = ...
    OBS_AVAILABLE: typing.ClassVar['ODParametersKey'] = ...
    OBS_USED: typing.ClassVar['ODParametersKey'] = ...
    TRACKS_AVAILABLE: typing.ClassVar['ODParametersKey'] = ...
    TRACKS_USED: typing.ClassVar['ODParametersKey'] = ...
    RESIDUALS_ACCEPTED: typing.ClassVar['ODParametersKey'] = ...
    WEIGHTED_RMS: typing.ClassVar['ODParametersKey'] = ...
    OD_EPOCH: typing.ClassVar['ODParametersKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: ODParameters) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (ODParameters): container to fill
        
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
    def valueOf(name: str) -> 'ODParametersKey':
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
    def values() -> typing.MutableSequence['ODParametersKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ODParametersKey c : ODParametersKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ODParametersWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for OD parameters data block for CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    ...

class RTNCovariance(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for RTN covariance matrix data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    This class has a RealMatrix as attribute which can be access with getRTNCovariaxMatrix method. Beware that there are thus two ways to modify the RTN covariance : setC… (setCrr, setCtr…) which should be prioritized and setEntry(row, col, value).
    
    The RTN Covariance Matrix is provided in the 9×9 Lower Triangular Form. All parameters of the 6×6 position/velocity submatrix are mandatory. The remaining elements will return {code NaN} if not provided.
    
    Since:
        11.2
    """
    def __init__(self):
        """
        Simple constructor. To update matrix value there are 2 ways to modify the RTN covariance : setC... ( setCrr, setCtr ...) which should be prioritized and getRTNCovariaxMatrix.setEntry(row, col, value).
        
        The RTN Covariance Matrix is provided in the 9×9 Lower Triangular Form. All parameters of the 6×6 position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        """
        ...
    def getCdrgdrg(self) -> float:
        """
        Get the object [7,7] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def getCdrgn(self) -> float:
        """
        Get the object [7,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCdrgndot(self) -> float:
        """
        Get the object [7,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCdrgr(self) -> float:
        """
        Get the object [7,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCdrgrdot(self) -> float:
        """
        Get the object [7,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCdrgt(self) -> float:
        """
        Get the object [7,2] in covariance matrix.
        
        Returns:
            the object [7,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCdrgtdot(self) -> float:
        """
        Get the object [7,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCndotn(self) -> float:
        """
        Get the object [6,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCndotndot(self) -> float:
        """
        Get the object [6,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,6] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCndotr(self) -> float:
        """
        Get the object [6,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCndotrdot(self) -> float:
        """
        Get the object [6,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCndott(self) -> float:
        """
        Get the object [6,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCndottdot(self) -> float:
        """
        Get the object [6,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCnn(self) -> float:
        """
        Get the object [3,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [3,3] in covariance matrix (in m²)
        
        
        """
        ...
    def getCnr(self) -> float:
        """
        Get the object [3,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [3,1] in covariance matrix (in m²)
        
        
        """
        ...
    def getCnt(self) -> float:
        """
        Get the object [3,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [3,2] in covariance matrix (in m²)
        
        
        """
        ...
    def getCrdotn(self) -> float:
        """
        Get the object [4, 3] in covariance matrix (with index starting at 1) .
        
        Returns:
            the object [4, 3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCrdotr(self) -> float:
        """
        Get the object [4,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [4,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCrdotrdot(self) -> float:
        """
        Get the object [4, 4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [4, 4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCrdott(self) -> float:
        """
        Get the object [4,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [4,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCrr(self) -> float:
        """
        Get the object [1,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [1,1] in covariance matrix (in m²)
        
        
        """
        ...
    def getCsrpdrg(self) -> float:
        """
        Get the object [8,7] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def getCsrpn(self) -> float:
        """
        Get the object [8,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCsrpndot(self) -> float:
        """
        Get the object [8,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCsrpr(self) -> float:
        """
        Get the object [8,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCsrprdot(self) -> float:
        """
        Get the object [8,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCsrpsrp(self) -> float:
        """
        Get the object [8,8] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,8] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def getCsrpt(self) -> float:
        """
        Get the object [8,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCsrptdot(self) -> float:
        """
        Get the object [8,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCtdotn(self) -> float:
        """
        Get the object [5,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCtdotr(self) -> float:
        """
        Get the object [5, 1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5, 1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCtdotrdot(self) -> float:
        """
        Get the object [5,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCtdott(self) -> float:
        """
        Get the object [5,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCtdottdot(self) -> float:
        """
        Get the object [5,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCthrdrg(self) -> float:
        """
        Get the object [9,7] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,7] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def getCthrn(self) -> float:
        """
        Get the object [9,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,3] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCthrndot(self) -> float:
        """
        Get the object [9,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,6] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def getCthrr(self) -> float:
        """
        Get the object [9,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,1] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCthrrdot(self) -> float:
        """
        Get the object [9,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,4] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def getCthrsrp(self) -> float:
        """
        Get the object [9,8] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,8] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def getCthrt(self) -> float:
        """
        Get the object [9,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,2] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCthrtdot(self) -> float:
        """
        Get the object [9,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,5] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def getCthrthr(self) -> float:
        """
        Get the object [9,9] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,9] in covariance matrix (in m²/s⁴)
        
        
        """
        ...
    def getCtr(self) -> float:
        """
        Get the object [2,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [2,1] in covariance matrix (in m²)
        
        
        """
        ...
    def getCtt(self) -> float:
        """
        Get the object [2,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [2,2] in covariance matrix (in m²)
        
        
        """
        ...
    def getRTNCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the RTN covariance matrix.
        
        The RTN Covariance Matrix is provided in the 9×9 Lower Triangular Form. All parameters of the 6×6 position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        
        Returns:
            the RTN covariance matrix
        
        
        """
        ...
    def setCdrgdrg(self, CDRGDRG: float) -> None:
        """
        Set the object [7,7] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGDRG (double): = object [7,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def setCdrgn(self, CDRGN: float) -> None:
        """
        Set the object [7,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGN (double): = object [7,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCdrgndot(self, CDRGNdot: float) -> None:
        """
        Set the object [7,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGNdot (double): = object [7,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCdrgr(self, CDRGR: float) -> None:
        """
        Set the object [7,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGR (double): = object [7,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCdrgrdot(self, CDRGRdot: float) -> None:
        """
        Set the object [7,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGRdot (double): = object [7,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCdrgt(self, CDRGT: float) -> None:
        """
        Set the object [7,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGT (double): = object [7,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCdrgtdot(self, CDRGTdot: float) -> None:
        """
        Set the object [7,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGTdot (double): = object [7,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCndotn(self, CNdotN: float) -> None:
        """
        Set the object [6,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNdotN (double): = object [6,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCndotndot(self, CNdotNdot: float) -> None:
        """
        Set the object [6,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNdotNdot (double): = object [6,6] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCndotr(self, CNdotR: float) -> None:
        """
        Set the object [6,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNdotR (double): = object [6,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCndotrdot(self, CNdotRdot: float) -> None:
        """
        Set the object [6,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNdotRdot (double): = object [6,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCndott(self, CNdotT: float) -> None:
        """
        Set the object [6,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNdotT (double): = object [6,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCndottdot(self, CNdotTdot: float) -> None:
        """
        Set the object [6,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNdotTdot (double): = object [6,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCnn(self, CNN: float) -> None:
        """
        Set the object [3,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNN (double): = object [3,3] in covariance matrix (in m²)
        
        
        """
        ...
    def setCnr(self, CNR: float) -> None:
        """
        Set the object [3,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNR (double): = object [3,1] in covariance matrix (in m²)
        
        
        """
        ...
    def setCnt(self, CNT: float) -> None:
        """
        Set the object [3,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CNT (double): = object [3,2] in covariance matrix (in m²)
        
        
        """
        ...
    def setCovarianceMatrixEntry(self, j: int, k: int, entry: float) -> None:
        """
        Set an entry in the RTN covariance matrix.
        
        Both m(j, k) and m(k, j) are set.
        
        Parameters:
            j (int): row index (must be between 0 and 5 (inclusive)
            k (int): column index (must be between 0 and 5 (inclusive)
            entry (double): value of the matrix entry
        
        
        """
        ...
    def setCrdotn(self, CRdotN: float) -> None:
        """
        Set the object [4, 3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CRdotN (double): = object [4,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCrdotr(self, CRdotR: float) -> None:
        """
        Set the object [4,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CRdotR (double): = object [4,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCrdotrdot(self, CRdotRdot: float) -> None:
        """
        Set the object [4, 4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CRdotRdot (double): = object [4, 4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCrdott(self, CRdotT: float) -> None:
        """
        Set the object [4, 2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CRdotT (double): = object [4, 2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCrr(self, CRR: float) -> None:
        """
        Set the object [1,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CRR (double): = object [1,1] in covariance matrix (in m²)
        
        
        """
        ...
    def setCsrpdrg(self, CSRPDRG: float) -> None:
        """
        Set the object [8,7] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPDRG (double): = object [8,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def setCsrpn(self, CSRPN: float) -> None:
        """
        Set the object [8,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPN (double): = object [8,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCsrpndot(self, CSRPNdot: float) -> None:
        """
        Set the object [8,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPNdot (double): = object [8,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCsrpr(self, CSRPR: float) -> None:
        """
        Set the object [8,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPR (double): = object [8,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCsrprdot(self, CSRPRdot: float) -> None:
        """
        Set the object [8,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPRdot (double): = object [8,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCsrpsrp(self, CSRPSRP: float) -> None:
        """
        Set the object [8,8] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPSRP (double): = object [8,8] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def setCsrpt(self, CSRPT: float) -> None:
        """
        Set the object [8,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPT (double): = object [8,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCsrptdot(self, CSRPTdot: float) -> None:
        """
        Set the object [8,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPTdot (double): = object [8,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCtdotn(self, CTdotN: float) -> None:
        """
        Set the object [5,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTdotN (double): = object [5,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCtdotr(self, CTdotR: float) -> None:
        """
        Set the object [5,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTdotR (double): = object [5,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCtdotrdot(self, CTdotRdot: float) -> None:
        """
        Set the object [5,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTdotRdot (double): = object [5,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCtdott(self, CTdotT: float) -> None:
        """
        Set the object [5,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTdotT (double): = object [5,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCtdottdot(self, CTdotTdot: float) -> None:
        """
        Set the object [5,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTdotTdot (double): = object [5,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCthrdrg(self, CTHRDRG: float) -> None:
        """
        Set the object [9,7] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRDRG (double): = object [9,7] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def setCthrn(self, CTHRN: float) -> None:
        """
        Set the object [9,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRN (double): = object [9,3] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCthrndot(self, CTHRNdot: float) -> None:
        """
        Set the object [9,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRNdot (double): = object [9,6] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def setCthrr(self, CTHRR: float) -> None:
        """
        Set the object [9,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRR (double): = object [9,1] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCthrrdot(self, CTHRRdot: float) -> None:
        """
        Set the object [9,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRRdot (double): = object [9,4] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def setCthrsrp(self, CTHRSRP: float) -> None:
        """
        Set the object [9,8] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRSRP (double): = object [9,8] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def setCthrt(self, CTHRT: float) -> None:
        """
        Set the object [9,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRT (double): = object [9,2] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCthrtdot(self, CTHRTdot: float) -> None:
        """
        Set the object [9,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRTdot (double): = object [9,5] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def setCthrthr(self, CTHRTHR: float) -> None:
        """
        Set the object [9,9] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRTHR (double): = object [9,9] in covariance matrix (in m²/s⁴)
        
        
        """
        ...
    def setCtr(self, CTR: float) -> None:
        """
        Set the object [2,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTR (double): = object [2,1] in covariance matrix (in m²)
        
        
        """
        ...
    def setCtt(self, CTT: float) -> None:
        """
        Set the object [2,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTT (double): = object [2,2] in covariance matrix (in m²)
        
        
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

class RTNCovarianceKey(java.lang.Enum['RTNCovarianceKey']):
    """
    Keys for RTNCovariance entries.
    
    Since:
        11.2
    """
    COMMENT: typing.ClassVar['RTNCovarianceKey'] = ...
    CR_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CT_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CT_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CN_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CN_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CN_N: typing.ClassVar['RTNCovarianceKey'] = ...
    CRDOT_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CRDOT_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CRDOT_N: typing.ClassVar['RTNCovarianceKey'] = ...
    CRDOT_RDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CTDOT_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CTDOT_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CTDOT_N: typing.ClassVar['RTNCovarianceKey'] = ...
    CTDOT_RDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CTDOT_TDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CNDOT_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CNDOT_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CNDOT_N: typing.ClassVar['RTNCovarianceKey'] = ...
    CNDOT_RDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CNDOT_TDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CNDOT_NDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CDRG_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CDRG_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CDRG_N: typing.ClassVar['RTNCovarianceKey'] = ...
    CDRG_RDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CDRG_TDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CDRG_NDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CDRG_DRG: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_N: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_RDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_TDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_NDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_DRG: typing.ClassVar['RTNCovarianceKey'] = ...
    CSRP_SRP: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_R: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_T: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_N: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_RDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_TDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_NDOT: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_DRG: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_SRP: typing.ClassVar['RTNCovarianceKey'] = ...
    CTHR_THR: typing.ClassVar['RTNCovarianceKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: RTNCovariance) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (RTNCovariance): container to fill
        
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
    def valueOf(name: str) -> 'RTNCovarianceKey':
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
    def values() -> typing.MutableSequence['RTNCovarianceKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RTNCovarianceKey c : RTNCovarianceKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RTNCovarianceWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for RTN covariance matrix data block for CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    ...

class ScreenType(java.lang.Enum['ScreenType']):
    """
    Screening type options allowed in CCSDS Conjunction Data Messages.
    """
    SHAPE: typing.ClassVar['ScreenType'] = ...
    PC: typing.ClassVar['ScreenType'] = ...
    PC_MAX: typing.ClassVar['ScreenType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ScreenType':
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
    def values() -> typing.MutableSequence['ScreenType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ScreenType c : ScreenType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ScreenVolumeFrame(java.lang.Enum['ScreenVolumeFrame']):
    """
    Screening volume frame possibilities used in CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    RTN: typing.ClassVar['ScreenVolumeFrame'] = ...
    TVN: typing.ClassVar['ScreenVolumeFrame'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ScreenVolumeFrame':
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
    def values() -> typing.MutableSequence['ScreenVolumeFrame']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ScreenVolumeFrame c : ScreenVolumeFrame.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ScreenVolumeShape(java.lang.Enum['ScreenVolumeShape']):
    """
    Screening volume shape possibilities used in CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    ELLIPSOID: typing.ClassVar['ScreenVolumeShape'] = ...
    BOX: typing.ClassVar['ScreenVolumeShape'] = ...
    SPHERE: typing.ClassVar['ScreenVolumeShape'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ScreenVolumeShape':
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
    def values() -> typing.MutableSequence['ScreenVolumeShape']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ScreenVolumeShape c : ScreenVolumeShape.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SigmaEigenvectorsCovariance(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for Sigma/Eigenvectors Covariance data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    The positional covariance one-sigma dispersions corresponding to the major, intermediate and minor eigenvalues, followed by the associated eigenvectors. The data is presented on a single line (12 values separated by spaces). (Condition: Mandatory if ALT_COV_TYPE = CSIG3EIGVEC3)
    """
    def __init__(self, altCovFlag: bool):
        """
        Simple constructor.
        
        The Sigma/Eigenvectors Covariance data is only provided if ALT_COV_TYPE is CSIG3EIGVEC3, otherwise its terms will return NaN.
        
        Parameters:
            altCovFlag (boolean): Flag indicating whether the alternate covariance type set in the CDM Object metadata section is Sigma/Eigenvectors
                Covariance.
        
        
        """
        ...
    def getCsig3eigvec3(self) -> typing.MutableSequence[float]:
        """
        Get the Sigma/Eigenvectors Covariance data.
        
        The Sigma/Eigenvectors Covariance data is only provided if ALT_COV_TYPE is CSIG3EIGVEC3, otherwise its terms will return NaN.
        
        Returns:
            the covariance data in the Sigma/Eigenvectors format.
        
        
        """
        ...
    def isAltCovFlagSet(self) -> bool:
        """
        Get the flag indicating whether the alternate covariance type set in the CDM Object metadata section is Sigma/Eigenvectors Covariance.
        
        Returns:
            the altCovFlag
        
        
        """
        ...
    def setCsig3eigvec3(self, csig3eigvec3: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Set the Sigma/Eigenvectors Covariance data.
        
        Parameters:
            csig3eigvec3 (double[]): the covariance data in the Sigma/Eigenvectors format.
        
        
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

class SigmaEigenvectorsCovarianceKey(java.lang.Enum['SigmaEigenvectorsCovarianceKey']):
    """
    Keys for SigmaEigenvectorsCovariance entries.
    """
    COMMENT: typing.ClassVar['SigmaEigenvectorsCovarianceKey'] = ...
    CSIG3EIGVEC3: typing.ClassVar['SigmaEigenvectorsCovarianceKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: SigmaEigenvectorsCovariance) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (SigmaEigenvectorsCovariance): container to fill
        
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
    def valueOf(name: str) -> 'SigmaEigenvectorsCovarianceKey':
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
    def values() -> typing.MutableSequence['SigmaEigenvectorsCovarianceKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (SigmaEigenvectorsCovarianceKey c : SigmaEigenvectorsCovarianceKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StateVector(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for state vector data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    Since:
        11.2
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getPositionVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get object Position Vector.
        
        Returns:
            object Position Vector (in m)
        
        
        """
        ...
    def getVelocityVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get object Velocity Vector.
        
        Returns:
            object Velocity Vector (in m/s)
        
        
        """
        ...
    def setX(self, X: float) -> None:
        """
        Set object Position Vector X component.
        
        Parameters:
            X (double): object Position Vector X component (in m)
        
        
        """
        ...
    def setXdot(self, Xdot: float) -> None:
        """
        Set object Velocity Vector X component.
        
        Parameters:
            Xdot (double): object Velocity Vector X component (in m/s)
        
        
        """
        ...
    def setY(self, Y: float) -> None:
        """
        Set object Position Vector Y component.
        
        Parameters:
            Y (double): object Position Vector Y component (in m)
        
        
        """
        ...
    def setYdot(self, Ydot: float) -> None:
        """
        Set object Velocity Vector Y component.
        
        Parameters:
            Ydot (double): object Velocity Vector Y component (in m/s)
        
        
        """
        ...
    def setZ(self, Z: float) -> None:
        """
        Set object Position Vector Z component.
        
        Parameters:
            Z (double): object Position Vector Z component (in m)
        
        
        """
        ...
    def setZdot(self, Zdot: float) -> None:
        """
        Set object Velocity Vector Z component.
        
        Parameters:
            Zdot (double): object Velocity Vector Z component (in m/s)
        
        
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

class StateVectorKey(java.lang.Enum['StateVectorKey']):
    """
    Keys for StateVector entries.
    
    Since:
        11.2
    """
    COMMENT: typing.ClassVar['StateVectorKey'] = ...
    X: typing.ClassVar['StateVectorKey'] = ...
    Y: typing.ClassVar['StateVectorKey'] = ...
    Z: typing.ClassVar['StateVectorKey'] = ...
    X_DOT: typing.ClassVar['StateVectorKey'] = ...
    Y_DOT: typing.ClassVar['StateVectorKey'] = ...
    Z_DOT: typing.ClassVar['StateVectorKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: StateVector) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (StateVector): container to fill
        
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
    def valueOf(name: str) -> 'StateVectorKey':
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
    def values() -> typing.MutableSequence['StateVectorKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (StateVectorKey c : StateVectorKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StateVectorWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    Writer for state vector data for CCSDS Conjunction Data Messages.
    
    Since:
        11.2
    """
    ...

class XYZCovariance(org.orekit.files.ccsds.section.CommentsContainer):
    """
    Container for XYZ covariance matrix data.
    
    Beware that the Orekit getters and setters all rely on SI units. The parsers and writers take care of converting these SI units into CCSDS mandatory units. The Unit class provides useful fromSI and toSI methods in case the callers already use CCSDS units instead of the API SI units. The general-purpose Unit class (without an 's') and the CCSDS-specific Units class (with an 's') also provide some predefined units. These predefined units and the fromSI and toSI conversion methods are indeed what the parsers and writers use for the conversions.
    
    This class as a RealMatrix as attribute which can be access with getXYZCovariaxMatrix method. Beware that there are thus two ways to modify the XYZ covariance : setC… (setCxx, setCyx…) which should be prioritized and setEntry(row, col, value).
    
    The XYZ Covariance Matrix is only provided if ALT_COV_TYPE is XYZ, otherwise its terms will return NaN.
    
    When available, the matrix is given in the 9×9 Lower Triangular Form. All parameters of the 6×6 position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
    """
    def __init__(self, covXYZset: bool):
        """
        Simple constructor. To update matrix value there are 2 ways to modify the XYZ covariance : setC... ( setCxx, setCyx ...) which should be prioritized and getXYZCovariaxMatrix.setEntry(row, col, value).
        
        The XYZ Covariance Matrix is only provided if ALT_COV_TYPE is XYZ, otherwise its terms will return NaN.
        
        When available, the matrix is given in the 9×9 Lower Triangular Form. All parameters of the 6×6 position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        
        Parameters:
            covXYZset (boolean): Flag indicating whether the alternate covariance type set in the CDM Object metadata section is XYZ.
        
        
        """
        ...
    def getCdrgdrg(self) -> float:
        """
        Get the object [7,7] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def getCdrgx(self) -> float:
        """
        Get the object [7,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCdrgxdot(self) -> float:
        """
        Get the object [7,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCdrgy(self) -> float:
        """
        Get the object [7,2] in covariance matrix.
        
        Returns:
            the object [7,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCdrgydot(self) -> float:
        """
        Get the object [7,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCdrgz(self) -> float:
        """
        Get the object [7,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCdrgzdot(self) -> float:
        """
        Get the object [7,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [7,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCsrpdrg(self) -> float:
        """
        Get the object [8,7] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def getCsrpsrp(self) -> float:
        """
        Get the object [8,8] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,8] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def getCsrpx(self) -> float:
        """
        Get the object [8,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCsrpxdot(self) -> float:
        """
        Get the object [8,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCsrpy(self) -> float:
        """
        Get the object [8,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCsrpydot(self) -> float:
        """
        Get the object [8,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCsrpz(self) -> float:
        """
        Get the object [8,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def getCsrpzdot(self) -> float:
        """
        Get the object [8,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [8,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def getCthrdrg(self) -> float:
        """
        Get the object [9,7] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,7] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def getCthrsrp(self) -> float:
        """
        Get the object [9,8] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,8] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def getCthrthr(self) -> float:
        """
        Get the object [9,9] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,9] in covariance matrix (in m²/s⁴)
        
        
        """
        ...
    def getCthrx(self) -> float:
        """
        Get the object [9,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,1] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCthrxdot(self) -> float:
        """
        Get the object [9,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,4] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def getCthry(self) -> float:
        """
        Get the object [9,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,2] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCthrydot(self) -> float:
        """
        Get the object [9,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,5] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def getCthrz(self) -> float:
        """
        Get the object [9,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,3] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCthrzdot(self) -> float:
        """
        Get the object [9,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [9,6] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def getCxdotx(self) -> float:
        """
        Get the object [4,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [4,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCxdotxdot(self) -> float:
        """
        Get the object [4, 4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [4, 4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCxdoty(self) -> float:
        """
        Get the object [4,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [4,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCxdotz(self) -> float:
        """
        Get the object [4, 3] in covariance matrix (with index starting at 1) .
        
        Returns:
            the object [4, 3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCxx(self) -> float:
        """
        Get the object [1,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [1,1] in covariance matrix (in m²)
        
        
        """
        ...
    def getCydotx(self) -> float:
        """
        Get the object [5, 1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5, 1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCydotxdot(self) -> float:
        """
        Get the object [5,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCydoty(self) -> float:
        """
        Get the object [5,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCydotydot(self) -> float:
        """
        Get the object [5,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCydotz(self) -> float:
        """
        Get the object [5,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [5,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCyx(self) -> float:
        """
        Get the object [2,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [2,1] in covariance matrix (in m²)
        
        
        """
        ...
    def getCyy(self) -> float:
        """
        Get the object [2,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [2,2] in covariance matrix (in m²)
        
        
        """
        ...
    def getCzdotx(self) -> float:
        """
        Get the object [6,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCzdotxdot(self) -> float:
        """
        Get the object [6,4] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCzdoty(self) -> float:
        """
        Get the object [6,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCzdotydot(self) -> float:
        """
        Get the object [6,5] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCzdotz(self) -> float:
        """
        Get the object [6,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def getCzdotzdot(self) -> float:
        """
        Get the object [6,6] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [6,6] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def getCzx(self) -> float:
        """
        Get the object [3,1] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [3,1] in covariance matrix (in m²)
        
        
        """
        ...
    def getCzy(self) -> float:
        """
        Get the object [3,2] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [3,2] in covariance matrix (in m²)
        
        
        """
        ...
    def getCzz(self) -> float:
        """
        Get the object [3,3] in covariance matrix (with index starting at 1).
        
        Returns:
            the object [3,3] in covariance matrix (in m²)
        
        
        """
        ...
    def getXYZCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
        Get the XYZ covariance matrix.
        
        The XYZ Covariance Matrix is only provided if ALT_COV_TYPE is XYZ, otherwise its terms will return NaN.
        
        When available, the matrix is given in the 9×9 Lower Triangular Form. All parameters of the 6×6 position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        
        Returns:
            the XYZ covariance matrix
        
        
        """
        ...
    def isCovXYZset(self) -> bool:
        """
        Get the flag indicating whether the alternate covariance type set in the CDM Object metadata section is XYZ.
        
        Returns:
            the covXYZset
        
        
        """
        ...
    def setCdrgdrg(self, CDRGDRG: float) -> None:
        """
        Set the object [7,7] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGDRG (double): = object [7,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def setCdrgx(self, CDRGX: float) -> None:
        """
        Set the object [7,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGX (double): = object [7,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCdrgxdot(self, CDRGXdot: float) -> None:
        """
        Set the object [7,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGXdot (double): = object [7,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCdrgy(self, CDRGY: float) -> None:
        """
        Set the object [7,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGY (double): = object [7,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCdrgydot(self, CDRGYdot: float) -> None:
        """
        Set the object [7,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGYdot (double): = object [7,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCdrgz(self, CDRGZ: float) -> None:
        """
        Set the object [7,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGZ (double): = object [7,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCdrgzdot(self, CDRGZdot: float) -> None:
        """
        Set the object [7,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CDRGZdot (double): = object [7,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCovarianceMatrixEntry(self, j: int, k: int, entry: float) -> None:
        """
        Set an entry in the XYZ covariance matrix.
        
        Both m(j, k) and m(k, j) are set.
        
        Parameters:
            j (int): row index (must be between 0 and 5 (inclusive)
            k (int): column index (must be between 0 and 5 (inclusive)
            entry (double): value of the matrix entry
        
        
        """
        ...
    def setCsrpdrg(self, CSRPDRG: float) -> None:
        """
        Set the object [8,7] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPDRG (double): = object [8,7] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def setCsrpsrp(self, CSRPSRP: float) -> None:
        """
        Set the object [8,8] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPSRP (double): = object [8,8] in covariance matrix (in m⁴/kg²)
        
        
        """
        ...
    def setCsrpx(self, CSRPX: float) -> None:
        """
        Set the object [8,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPX (double): = object [8,1] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCsrpxdot(self, CSRPXdot: float) -> None:
        """
        Set the object [8,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPXdot (double): = object [8,4] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCsrpy(self, CSRPY: float) -> None:
        """
        Set the object [8,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPY (double): = object [8,2] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCsrpydot(self, CSRPYdot: float) -> None:
        """
        Set the object [8,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPYdot (double): = object [8,5] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCsrpz(self, CSRPZ: float) -> None:
        """
        Set the object [8,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPZ (double): = object [8,3] in covariance matrix (in m³/kg)
        
        
        """
        ...
    def setCsrpzdot(self, CSRPZdot: float) -> None:
        """
        Set the object [8,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CSRPZdot (double): = object [8,6] in covariance matrix (in m³/(kg.s))
        
        
        """
        ...
    def setCthrdrg(self, CTHRDRG: float) -> None:
        """
        Set the object [9,7] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRDRG (double): = object [9,7] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def setCthrsrp(self, CTHRSRP: float) -> None:
        """
        Set the object [9,8] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRSRP (double): = object [9,8] in covariance matrix (in m³/(kg.s²))
        
        
        """
        ...
    def setCthrthr(self, CTHRTHR: float) -> None:
        """
        Set the object [9,9] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRTHR (double): = object [9,9] in covariance matrix (in m²/s⁴)
        
        
        """
        ...
    def setCthrx(self, CTHRX: float) -> None:
        """
        Set the object [9,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRX (double): = object [9,1] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCthrxdot(self, CTHRXdot: float) -> None:
        """
        Set the object [9,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRXdot (double): = object [9,4] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def setCthry(self, CTHRY: float) -> None:
        """
        Set the object [9,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRY (double): = object [9,2] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCthrydot(self, CTHRYdot: float) -> None:
        """
        Set the object [9,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRYdot (double): = object [9,5] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def setCthrz(self, CTHRZ: float) -> None:
        """
        Set the object [9,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRZ (double): = object [9,3] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCthrzdot(self, CTHRZdot: float) -> None:
        """
        Set the object [9,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CTHRZdot (double): = object [9,6] in covariance matrix (in m²/s³)
        
        
        """
        ...
    def setCxdotx(self, CXdotX: float) -> None:
        """
        Set the object [4,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CXdotX (double): = object [4,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCxdotxdot(self, CXdotXdot: float) -> None:
        """
        Set the object [4, 4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CXdotXdot (double): = object [4, 4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCxdoty(self, CXdotY: float) -> None:
        """
        Set the object [4, 2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CXdotY (double): = object [4, 2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCxdotz(self, CXdotZ: float) -> None:
        """
        Set the object [4, 3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CXdotZ (double): = object [4,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCxx(self, CXX: float) -> None:
        """
        Set the object [1,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CXX (double): = object [1,1] in covariance matrix (in m²)
        
        
        """
        ...
    def setCydotx(self, CYdotX: float) -> None:
        """
        Set the object [5,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CYdotX (double): = object [5,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCydotxdot(self, CYdotXdot: float) -> None:
        """
        Set the object [5,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CYdotXdot (double): = object [5,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCydoty(self, CYdotY: float) -> None:
        """
        Set the object [5,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CYdotY (double): = object [5,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCydotydot(self, CYdotYdot: float) -> None:
        """
        Set the object [5,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CYdotYdot (double): = object [5,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCydotz(self, CYdotZ: float) -> None:
        """
        Set the object [5,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CYdotZ (double): = object [5,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCyx(self, CYX: float) -> None:
        """
        Set the object [2,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CYX (double): = object [2,1] in covariance matrix (in m²)
        
        
        """
        ...
    def setCyy(self, CYY: float) -> None:
        """
        Set the object [2,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CYY (double): = object [2,2] in covariance matrix (in m²)
        
        
        """
        ...
    def setCzdotx(self, CZdotX: float) -> None:
        """
        Set the object [6,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZdotX (double): = object [6,1] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCzdotxdot(self, CZdotXdot: float) -> None:
        """
        Set the object [6,4] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZdotXdot (double): = object [6,4] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCzdoty(self, CZdotY: float) -> None:
        """
        Set the object [6,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZdotY (double): = object [6,2] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCzdotydot(self, CZdotYdot: float) -> None:
        """
        Set the object [6,5] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZdotYdot (double): = object [6,5] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCzdotz(self, CZdotZ: float) -> None:
        """
        Set the object [6,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZdotZ (double): = object [6,3] in covariance matrix (in m²/s)
        
        
        """
        ...
    def setCzdotzdot(self, CZdotZdot: float) -> None:
        """
        Set the object [6,6] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZdotZdot (double): = object [6,6] in covariance matrix (in m²/s²)
        
        
        """
        ...
    def setCzx(self, CZX: float) -> None:
        """
        Set the object [3,1] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZX (double): = object [3,1] in covariance matrix (in m²)
        
        
        """
        ...
    def setCzy(self, CZY: float) -> None:
        """
        Set the object [3,2] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZY (double): = object [3,2] in covariance matrix (in m²)
        
        
        """
        ...
    def setCzz(self, CZZ: float) -> None:
        """
        Set the object [3,3] in covariance matrix (with index starting at 1).
        
        Parameters:
            CZZ (double): = object [3,3] in covariance matrix (in m²)
        
        
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

class XYZCovarianceKey(java.lang.Enum['XYZCovarianceKey']):
    """
    Keys for XYZCovariance entries.
    """
    COMMENT: typing.ClassVar['XYZCovarianceKey'] = ...
    CX_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CY_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CY_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CZ_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CZ_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CZ_Z: typing.ClassVar['XYZCovarianceKey'] = ...
    CXDOT_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CXDOT_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CXDOT_Z: typing.ClassVar['XYZCovarianceKey'] = ...
    CXDOT_XDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CYDOT_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CYDOT_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CYDOT_Z: typing.ClassVar['XYZCovarianceKey'] = ...
    CYDOT_XDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CYDOT_YDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CZDOT_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CZDOT_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CZDOT_Z: typing.ClassVar['XYZCovarianceKey'] = ...
    CZDOT_XDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CZDOT_YDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CZDOT_ZDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CDRG_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CDRG_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CDRG_Z: typing.ClassVar['XYZCovarianceKey'] = ...
    CDRG_XDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CDRG_YDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CDRG_ZDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CDRG_DRG: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_Z: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_XDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_YDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_ZDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_DRG: typing.ClassVar['XYZCovarianceKey'] = ...
    CSRP_SRP: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_X: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_Y: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_Z: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_XDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_YDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_ZDOT: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_DRG: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_SRP: typing.ClassVar['XYZCovarianceKey'] = ...
    CTHR_THR: typing.ClassVar['XYZCovarianceKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, context: org.orekit.files.ccsds.utils.ContextBinding, container: XYZCovariance) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            context (ContextBinding): context binding
            container (XYZCovariance): container to fill
        
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
    def valueOf(name: str) -> 'XYZCovarianceKey':
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
    def values() -> typing.MutableSequence['XYZCovarianceKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (XYZCovarianceKey c : XYZCovarianceKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class XmlSubStructureKey(java.lang.Enum['XmlSubStructureKey']):
    """
    Keywords for CDM data sub-structure in XML files.
    
    Since:
        11.2
    """
    COMMENT: typing.ClassVar['XmlSubStructureKey'] = ...
    relativeMetadataData: typing.ClassVar['XmlSubStructureKey'] = ...
    segment: typing.ClassVar['XmlSubStructureKey'] = ...
    relativeStateVector: typing.ClassVar['XmlSubStructureKey'] = ...
    odParameters: typing.ClassVar['XmlSubStructureKey'] = ...
    additionalParameters: typing.ClassVar['XmlSubStructureKey'] = ...
    stateVector: typing.ClassVar['XmlSubStructureKey'] = ...
    covarianceMatrix: typing.ClassVar['XmlSubStructureKey'] = ...
    userDefinedParameters: typing.ClassVar['XmlSubStructureKey'] = ...
    def process(self, token: org.orekit.files.ccsds.utils.lexical.ParseToken, parser: CdmParser) -> bool:
        """
        Process one token.
        
        Parameters:
            token (ParseToken): token to process
            parser (CdmParser): CDM file parser
        
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
    def valueOf(name: str) -> 'XmlSubStructureKey':
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
    def values() -> typing.MutableSequence['XmlSubStructureKey']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (XmlSubStructureKey c : XmlSubStructureKey.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmWriter(CdmMessageWriter):
    """
    Writer for CCSDS Conjunction Data Message.
    
    Since:
        11.2
    """
    CCSDS_CDM_VERS: typing.ClassVar[float] = ...
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
    def __init__(self, conventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext):
        """
        Complete constructor.
        
        Calling this constructor directly is not recommended. Users should rather use buildCdmWriter.
        
        Parameters:
            conventions (IERSConventions): IERS Conventions
            dataContext (DataContext): used to retrieve frames, time scales, etc.
        
        
        """
        ...
    def writeRelativeMetadataContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, formatVersion: float, relativeMetadata: CdmRelativeMetadata) -> None:
        """
        Description copied from class: writeRelativeMetadataContent Write RelativeMetadata part only once after header.
        
        Specified by: writeRelativeMetadataContent in class CdmMessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            formatVersion (double): format version to use
            relativeMetadata (CdmRelativeMetadata): relative metadata to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, formatVersion: float, segment: org.orekit.files.ccsds.section.Segment[CdmMetadata, CdmData]) -> None:
        """
        Write one segment content (without XML wrapping).
        
        Specified by: writeSegmentContent in class CdmMessageWriter
        
        Parameters:
            generator (Generator): generator to use for producing output
            formatVersion (double): format version to use
            segment (Segment<CdmMetadata, CdmData> segment): segment to write
        
        Raises:
            IOException: if any buffer writing operations fails
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.cdm")``.

    AdditionalCovarianceMetadata: typing.Type[AdditionalCovarianceMetadata]
    AdditionalCovarianceMetadataKey: typing.Type[AdditionalCovarianceMetadataKey]
    AdditionalParameters: typing.Type[AdditionalParameters]
    AdditionalParametersKey: typing.Type[AdditionalParametersKey]
    AdditionalParametersWriter: typing.Type[AdditionalParametersWriter]
    AltCovarianceType: typing.Type[AltCovarianceType]
    Cdm: typing.Type[Cdm]
    CdmData: typing.Type[CdmData]
    CdmHeader: typing.Type[CdmHeader]
    CdmHeaderKey: typing.Type[CdmHeaderKey]
    CdmHeaderProcessingState: typing.Type[CdmHeaderProcessingState]
    CdmMessageWriter: typing.Type[CdmMessageWriter]
    CdmMetadata: typing.Type[CdmMetadata]
    CdmMetadataKey: typing.Type[CdmMetadataKey]
    CdmMetadataWriter: typing.Type[CdmMetadataWriter]
    CdmParser: typing.Type[CdmParser]
    CdmRelativeMetadata: typing.Type[CdmRelativeMetadata]
    CdmRelativeMetadataKey: typing.Type[CdmRelativeMetadataKey]
    CdmSegment: typing.Type[CdmSegment]
    CdmWriter: typing.Type[CdmWriter]
    CovarianceMethod: typing.Type[CovarianceMethod]
    Maneuvrable: typing.Type[Maneuvrable]
    ODParameters: typing.Type[ODParameters]
    ODParametersKey: typing.Type[ODParametersKey]
    ODParametersWriter: typing.Type[ODParametersWriter]
    RTNCovariance: typing.Type[RTNCovariance]
    RTNCovarianceKey: typing.Type[RTNCovarianceKey]
    RTNCovarianceWriter: typing.Type[RTNCovarianceWriter]
    ScreenType: typing.Type[ScreenType]
    ScreenVolumeFrame: typing.Type[ScreenVolumeFrame]
    ScreenVolumeShape: typing.Type[ScreenVolumeShape]
    SigmaEigenvectorsCovariance: typing.Type[SigmaEigenvectorsCovariance]
    SigmaEigenvectorsCovarianceKey: typing.Type[SigmaEigenvectorsCovarianceKey]
    StateVector: typing.Type[StateVector]
    StateVectorKey: typing.Type[StateVectorKey]
    StateVectorWriter: typing.Type[StateVectorWriter]
    XYZCovariance: typing.Type[XYZCovariance]
    XYZCovarianceKey: typing.Type[XYZCovarianceKey]
    XmlSubStructureKey: typing.Type[XmlSubStructureKey]
