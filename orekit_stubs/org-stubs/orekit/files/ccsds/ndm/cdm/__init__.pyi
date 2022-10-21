import java.lang
import java.util
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
    public class AdditionalCovarianceMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for the additional covariance metadata (optional).
    """
    def __init__(self): ...
    def getDcpSensitivityVectorPosition(self) -> typing.List[float]:
        """
            Get the DCP sensitivity vector (position errors at TCA).
        
            Returns:
                the dcpSensitivityVectorPosition
        
        
        """
        ...
    def getDcpSensitivityVectorVelocity(self) -> typing.List[float]:
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
    def setDcpSensitivityVectorPosition(self, doubleArray: typing.List[float]) -> None:
        """
            Set the DCP sensitivity vector (position errors at TCA).
        
            Parameters:
                dcpSensitivityVectorPosition (double[]): the dcpSensitivityVectorPosition to set
        
        
        """
        ...
    def setDcpSensitivityVectorVelocity(self, doubleArray: typing.List[float]) -> None:
        """
            Set the DCP sensitivity vector (velocity errors at TCA).
        
            Parameters:
                dcpSensitivityVectorVelocity (double[]): the dcpSensitivityVectorVelocity to set
        
        
        """
        ...
    def setDensityForecastUncertainty(self, double: float) -> None:
        """
            Set the atmospheric density forecast error.
        
            Parameters:
                densityForecastUncertainty (double): the cScaleFactorMax to set
        
        
        """
        ...
    def setScreeningDataSource(self, string: str) -> None:
        """
            Set the source (or origin) of the specific orbital data for this object.
        
            Parameters:
                screeningDataSource (String): the screeningDataSource to set
        
        
        """
        ...
    def setcScaleFactor(self, double: float) -> None:
        """
            Set the (median) suggested covariance scale factor.
        
            Parameters:
                cScaleFactor (double): the cScaleFactor to set
        
        
        """
        ...
    def setcScaleFactorMax(self, double: float) -> None:
        """
            set the maximum suggested covariance scale factor.
        
            Parameters:
                cScaleFactorMax (double): the cScaleFactorMax to set
        
        
        """
        ...
    def setcScaleFactorMin(self, double: float) -> None:
        """
            Set the minimum suggested covariance scale factor.
        
            Parameters:
                cScaleFactorMin (double): the cScaleFactorMin to set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AdditionalCovarianceMetadataKey(java.lang.Enum['AdditionalCovarianceMetadataKey']):
    """
    public enum AdditionalCovarianceMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.AdditionalCovarianceMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.AdditionalCovarianceMetadata` entries.
    """
    COMMENT: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    DENSITY_FORECAST_UNCERTAINTY: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    CSCALE_FACTOR_MIN: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    CSCALE_FACTOR: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    CSCALE_FACTOR_MAX: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    SCREENING_DATA_SOURCE: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    DCP_SENSITIVITY_VECTOR_POSITION: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    DCP_SENSITIVITY_VECTOR_VELOCITY: typing.ClassVar['AdditionalCovarianceMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, additionalCovarianceMetadata: AdditionalCovarianceMetadata) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.AdditionalCovarianceMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'AdditionalCovarianceMetadataKey':
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
    def values() -> typing.List['AdditionalCovarianceMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (AdditionalCovarianceMetadataKey c : AdditionalCovarianceMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdditionalParameters(org.orekit.files.ccsds.ndm.CommonPhysicalProperties):
    """
    public class AdditionalParameters extends :class:`~org.orekit.files.ccsds.ndm.CommonPhysicalProperties`
    
        Container for additional parameters data block.
    
        Since:
            11.2
    """
    def __init__(self): ...
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
                the object area (in mÂ²) exposed to atmospheric drag
        
        
        """
        ...
    def getAreaPC(self) -> float:
        """
            Get the actual area of the object.
        
            Returns:
                the object area (in mÂ²)
        
        
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
                the object area (in mÂ²) exposed to solar radiation pressure
        
        
        """
        ...
    def getCDAreaOverMass(self) -> float:
        """
            Get the objectâ€™s Cd x A/m used to propagate the state vector and covariance to TCA.
        
            Returns:
                the objectâ€™s Cd x A/m (in mÂ²/kg)
        
        
        """
        ...
    def getCRAreaOverMass(self) -> float:
        """
            Get the objectâ€™s Cr x A/m used to propagate the state vector and covariance to TCA.
        
            Returns:
                the objectâ€™s Cr x A/m (in mÂ²/kg)
        
        
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
    def getPeriapsissAltitude(self) -> float:
        """
            Get the distance of the closest point in the objects orbit above the equatorial radius of the central body.
        
            Returns:
                the periapsissAltitude
        
        
        """
        ...
    def getSedr(self) -> float:
        """
            Get the amount of energy being removed from the objectÃ¢â‚¬â„¢s orbit by atmospheric drag. This value is an average
            calculated during the OD. SEDR = Specific Energy Dissipation Rate.
        
            Returns:
                the amount of energy (in W/kg) being removed from the objectâ€™s orbit by atmospheric drag
        
        
        """
        ...
    def getThrustAcceleration(self) -> float:
        """
            Get the objectâ€™s acceleration due to in-track thrust used to propagate the state vector and covariance to TCA.
        
            Returns:
                the objectâ€™s acceleration (in m/sÂ²) due to in-track thrust
        
        
        """
        ...
    def setApoapsisAltitude(self, double: float) -> None:
        """
            Set the distance of the furthest point in the objects orbit above the equatorial radius of the central body.
        
            Parameters:
                apoapsisAltitude (double): the apoapsisHeight to set
        
        
        """
        ...
    def setAreaDRG(self, double: float) -> None:
        """
            Set the effective area of the object exposed to atmospheric drag.
        
            Parameters:
                areaDRG (double): area (in mÂ²) value to be set
        
        
        """
        ...
    def setAreaPC(self, double: float) -> None:
        """
            Set the actual area of the object.
        
            Parameters:
                areaPC (double): area (in mÂ²) value to be set
        
        
        """
        ...
    def setAreaPCMax(self, double: float) -> None:
        """
            Set the maximum area for the object to be used to compute the collision probability.
        
            Parameters:
                areaPCMax (double): the areaPCMax to set
        
        
        """
        ...
    def setAreaPCMin(self, double: float) -> None:
        """
            Get the minimum area of the object to be used to compute the collision probability.
        
            Parameters:
                areaPCMin (double): the areaPCMin to set
        
        
        """
        ...
    def setAreaSRP(self, double: float) -> None:
        """
            Set the effective area of the object exposed to solar radiation pressure.
        
            Parameters:
                areaSRP (double): area (in mÂ²) to be set
        
        
        """
        ...
    def setCDAreaOverMass(self, double: float) -> None:
        """
            Set the objectâ€™s Cd x A/m used to propagate the state vector and covariance to TCA.
        
            Parameters:
                CDAreaOverMass (double): objectâ€™s Cd x A/m (in mÂ²/kg) value to be set
        
        
        """
        ...
    def setCRAreaOverMass(self, double: float) -> None:
        """
            Set the objectâ€™s Cr x A/m used to propagate the state vector and covariance to TCA.
        
            Parameters:
                CRAreaOverMass (double): objectâ€™s Cr x A/m (in mÂ²/kg) value to be set
        
        
        """
        ...
    def setCovConfidence(self, double: float) -> None:
        """
            Set the measure of the confidence in the covariance errors matching reality.
        
            Parameters:
                covConfidence (double): the covConfidence to set
        
        
        """
        ...
    def setCovConfidenceMethod(self, string: str) -> None:
        """
            Set the method used for the calculation of COV_CONFIDENCE.
        
            Parameters:
                covConfidenceMethod (String): the covConfidenceMethod to set
        
        
        """
        ...
    def setHbr(self, double: float) -> None:
        """
            Set the object hard body radius.
        
            Parameters:
                hbr (double): the object hard body radius.
        
        
        """
        ...
    def setInclination(self, double: float) -> None:
        """
            Set the angle between the objects orbit plane and the orbit centers equatorial plane.
        
            Parameters:
                inclination (double): the inclination to set
        
        
        """
        ...
    def setMass(self, double: float) -> None:
        """
            Set the mass of the object.
        
            Parameters:
                mass (double): mass (in kg) of the object to be set
        
        
        """
        ...
    def setPeriapsissAltitude(self, double: float) -> None:
        """
            Set the distance of the closest point in the objects orbit above the equatorial radius of the central body.
        
            Parameters:
                periapsissAltitude (double): the periapsissHeight to set
        
        
        """
        ...
    def setSedr(self, double: float) -> None:
        """
            Set the amount of energy being removed from the objectÃ¢â‚¬â„¢s orbit by atmospheric drag. This value is an average
            calculated during the OD. SEDR = Specific Energy Dissipation Rate.
        
            Parameters:
                SEDR (double): amount of energy (in W/kg) being removed from the objectâ€™s orbit by atmospheric drag
        
        
        """
        ...
    def setThrustAcceleration(self, double: float) -> None:
        """
            Set the objectâ€™s acceleration due to in-track thrust used to propagate the state vector and covariance to TCA.
        
            Parameters:
                thrustAcceleration (double): objectâ€™s acceleration (in m/sÂ²) due to in-track thrust
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.ndm.CommonPhysicalProperties.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.ndm.CommonPhysicalProperties`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class AdditionalParametersKey(java.lang.Enum['AdditionalParametersKey']):
    """
    public enum AdditionalParametersKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.AdditionalParametersKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.AdditionalParameters` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, additionalParameters: AdditionalParameters) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.AdditionalParameters`): container to fill
        
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
    def valueOf(string: str) -> 'AdditionalParametersKey':
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
    def values() -> typing.List['AdditionalParametersKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (AdditionalParametersKey c : AdditionalParametersKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AdditionalParametersWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class AdditionalParametersWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for additional parameters data block for CCSDS Conjunction Data Messages.
    
        Since:
            11.2
    """
    ...

class AltCovarianceType(java.lang.Enum['AltCovarianceType']):
    """
    public enum AltCovarianceType extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.AltCovarianceType`>
    
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
    def valueOf(string: str) -> 'AltCovarianceType':
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
    def values() -> typing.List['AltCovarianceType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (AltCovarianceType c : AltCovarianceType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Cdm(org.orekit.files.ccsds.ndm.NdmConstituent['CdmHeader', 'CdmSegment']):
    """
    public class Cdm extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.ndm.cdm.CdmHeader`, :class:`~org.orekit.files.ccsds.ndm.cdm.CdmSegment`>
    
        This class stores all the information of the Conjunction Data Message (CDM) File parsed by CdmParser. It contains the
        header and a list of segments each containing metadata and a list of data lines.
    
        Since:
            11.2
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final String ROOT
    
        Root element for XML files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORMAT_VERSION_KEY: typing.ClassVar[str] = ...
    """
    public static final String FORMAT_VERSION_KEY
    
        Key for format version.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, cdmHeader: 'CdmHeader', list: java.util.List['CdmSegment'], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...
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
    public class CdmData extends Object implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Container for Conjunction Data Message data.
    
        Since:
            11.2
    """
    @typing.overload
    def __init__(self, commentsContainer: org.orekit.files.ccsds.section.CommentsContainer, oDParameters: 'ODParameters', additionalParameters: AdditionalParameters, stateVector: 'StateVector', rTNCovariance: 'RTNCovariance'): ...
    @typing.overload
    def __init__(self, commentsContainer: org.orekit.files.ccsds.section.CommentsContainer, oDParameters: 'ODParameters', additionalParameters: AdditionalParameters, stateVector: 'StateVector', rTNCovariance: 'RTNCovariance', additionalCovarianceMetadata: AdditionalCovarianceMetadata): ...
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
        
            The RTN Covariance Matrix is provided in the 9Ãƒâ€”9 Lower Triangular Form. All parameters of the 6Ãƒâ€”6
            position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        
            Returns:
                covariance matrix block
        
        
        """
        ...
    def getSig3Eigvec3CovarianceBlock(self) -> 'SigmaEigenvectorsCovariance':
        """
            Get the Sigma / Eigenvector covariance logical block.
        
            This block is not mandatory and on condition that :meth:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadataKey.ALT_COV_TYPE` =
            :meth:`~org.orekit.files.ccsds.ndm.cdm.AltCovarianceType.CSIG3EIGVEC3`.
        
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
            Get the Covariance Matrix in the XYZ Coordinate Frame (defined by value of
            :meth:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadataKey.ALT_COV_REF_FRAME`).
        
            This block is not mandatory and on condition that :meth:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadataKey.ALT_COV_TYPE` =
            :meth:`~org.orekit.files.ccsds.ndm.cdm.AltCovarianceType.XYZ`.
        
            This method will return null if the block is not defined in the CDM.
        
            Returns:
                XYZ covariance matrix block
        
        
        """
        ...
    def setUserDefinedBlock(self, userDefined: org.orekit.files.ccsds.ndm.odm.UserDefined) -> None:
        """
            Set the user defined logical block.
        
            This block is added at the end of the CDM parsing as common to both Object 1 and 2.
        
            Parameters:
                userDefinedBlock (:class:`~org.orekit.files.ccsds.ndm.odm.UserDefined`): the user defined block to set
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class CdmHeader(org.orekit.files.ccsds.section.Header):
    """
    public class CdmHeader extends :class:`~org.orekit.files.ccsds.section.Header`
    
        Header of a CCSDS Conjunction Data Message.
    
        Since:
            11.2
    """
    def __init__(self, double: float): ...
    def getClassification(self) -> str:
        """
            Get the classification or caveats text message of this CDM.
        
            Returns:
                the classification
        
        
        """
        ...
    def getMessageFor(self) -> str:
        """
            Get the spacecraft name for which the CDM is provided stored in MESSAGE_FOR key.
        
            Returns:
                messageFor the spacecraft name for which the CDM is provided.
        
        
        """
        ...
    def setClassification(self, string: str) -> None:
        """
            Set the classification or caveats text message of this CDM.
        
            Parameters:
                classification (String): the classification to set
        
        
        """
        ...
    def setMessageFor(self, string: str) -> None:
        """
            Set the spacecraft name for which the CDM is provided stored in MESSAGE_FOR key.
        
            Parameters:
                spacecraftNames (String): the spacecraft name for which the CDM is provided.
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.Header.validate` in class :class:`~org.orekit.files.ccsds.section.Header`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class CdmHeaderKey(java.lang.Enum['CdmHeaderKey']):
    """
    public enum CdmHeaderKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.CdmHeaderKey`>
    
        Keywords allowed in :class:`~org.orekit.files.ccsds.ndm.cdm.CdmHeader`.
    
        Since:
            11.2
    """
    MESSAGE_FOR: typing.ClassVar['CdmHeaderKey'] = ...
    CLASSIFICATION: typing.ClassVar['CdmHeaderKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, cdmHeader: CdmHeader) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                header (:class:`~org.orekit.files.ccsds.ndm.cdm.CdmHeader`): header to fill
        
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
    def valueOf(string: str) -> 'CdmHeaderKey':
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
    def values() -> typing.List['CdmHeaderKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CdmHeaderKey c : CdmHeaderKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmHeaderProcessingState(org.orekit.files.ccsds.utils.parsing.ProcessingState):
    """
    public class CdmHeaderProcessingState extends Object implements :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
    
        :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState` for :class:`~org.orekit.files.ccsds.ndm.cdm.CdmHeader`.
    
        Since:
            11.2
    """
    def __init__(self, cdmParser: 'CdmParser'): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool:
        """
            Process one token.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.ProcessingState.processToken`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.parsing.ProcessingState`
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
        
            Returns:
                true if token was processed, false otherwise
        
        
        """
        ...

class CdmMessageWriter(org.orekit.files.ccsds.utils.generation.MessageWriter[CdmHeader, 'CdmSegment', Cdm]):
    """
    public abstract class CdmMessageWriter extends Object implements :class:`~org.orekit.files.ccsds.utils.generation.MessageWriter`<:class:`~org.orekit.files.ccsds.ndm.cdm.CdmHeader`, :class:`~org.orekit.files.ccsds.ndm.cdm.CdmSegment`, :class:`~org.orekit.files.ccsds.ndm.cdm.Cdm`>
    
        Cdm message writer.
    
        Since:
            11.2
    """
    DEFAULT_ORIGINATOR: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_ORIGINATOR
    
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
    def writeFooter(self, generator: org.orekit.files.ccsds.utils.generation.Generator) -> None: ...
    def writeHeader(self, generator: org.orekit.files.ccsds.utils.generation.Generator, cdmHeader: CdmHeader) -> None: ...
    def writeRelativeMetadataContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, cdmRelativeMetadata: 'CdmRelativeMetadata') -> None: ...
    def writeSegment(self, generator: org.orekit.files.ccsds.utils.generation.Generator, cdmSegment: 'CdmSegment') -> None: ...
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, segment: org.orekit.files.ccsds.section.Segment['CdmMetadata', CdmData]) -> None: ...

class CdmMetadata(org.orekit.files.ccsds.section.Metadata):
    """
    public class CdmMetadata extends :class:`~org.orekit.files.ccsds.section.Metadata`
    
        This class gathers the meta-data present in the Conjunction Data Message (CDM).
    
        Since:
            11.2
    """
    def __init__(self): ...
    def getAdmMsgLink(self) -> str:
        """
            Get the unique identifier of Attitude Data Message(s) that are linked (relevant) to this Conjunction Data Message.
        
            Returns:
                the admMsgLink
        
        
        """
        ...
    def getAltCovRefFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get the value of :code:`ALT_COV_REF_FRAME` as an Orekit :class:`~org.orekit.frames.Frame`.
        
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
    def getEarthTides(self) -> bool:
        """
            Get boolean that indicates if Earth and ocean tides are taken into account or not.
        
            Returns:
                isEarthTides boolean
        
        
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
            Get the reference frame in which data are given: used for state vector and Keplerian elements data (and for the
            covariance reference frame if none is given).
        
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
    def getIntrackThrust(self) -> bool:
        """
            Get boolean that indicates if intrack thrust modeling was into account or not.
        
            Returns:
                isEarthTides boolean
        
        
        """
        ...
    def getManeuverable(self) -> 'Maneuvrable':
        """
            Get the ability of object to maneuver or not.
        
            Returns:
                the ability to maneuver
        
        
        """
        ...
    def getNBodyPerturbations(self) -> java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]: ...
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
            Get the flag indicating whether new tracking observations are anticipated prior to the issue of the next CDM associated
            with the event specified by CONJUNCTION_ID.
        
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
            Get the value of :code:`REF_FRAME` as an Orekit :class:`~org.orekit.frames.Frame`. The :code:`ORBIT_CENTER` key word has
            not been applied yet, so the returned frame may not correspond to the reference frame of the data in the file.
        
            Returns:
                the reference frame
        
        
        """
        ...
    def getRelativeMetadata(self) -> 'CdmRelativeMetadata':
        """
            Get the relative metadata following header, they are the common metadata for the CDM.
        
            Returns:
                relativeMetadata relative metadata
        
        
        """
        ...
    def getSolarRadiationPressure(self) -> bool:
        """
            Get boolean that indicates if Solar Radiation Pressure is taken into account or not.
        
            Returns:
                isSolarRadPressure boolean
        
        
        """
        ...
    def setAdmMsgLink(self, string: str) -> None:
        """
            Set the unique identifier of Attitude Data Message(s) that are linked (relevant) to this Conjunction Data Message.
        
            Parameters:
                admMsgLink (String): the admMsgLink to set
        
        
        """
        ...
    def setAltCovRefFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set the name of the reference frame in which the alternate covariance data are given.
        
            Parameters:
                altCovRefFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): alternate covariance reference frame
        
        
        """
        ...
    def setAltCovType(self, altCovarianceType: AltCovarianceType) -> None:
        """
            Set the flag indicating the type of alternate covariance information provided.
        
            Parameters:
                altCovType (:class:`~org.orekit.files.ccsds.ndm.cdm.AltCovarianceType`): the altCovType to set
        
        
        """
        ...
    def setAtmosphericModel(self, string: str) -> None:
        """
            Set name of atmospheric model.
        
            Parameters:
                atmosphericModel (String): name of atmospheric model
        
        
        """
        ...
    def setCatalogName(self, string: str) -> None:
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
                covarianceMethod (:class:`~org.orekit.files.ccsds.ndm.cdm.CovarianceMethod`): method name for covariance calculation
        
        
        """
        ...
    def setCovarianceSource(self, string: str) -> None:
        """
            Set the source of the covariance data.
        
            Parameters:
                covarianceSource (String): the covarianceSource to set
        
        
        """
        ...
    def setEarthTides(self, boolean: bool) -> None:
        """
            Set boolean that indicates if Earth and ocean tides are taken into account or not.
        
            Parameters:
                EarthTides (boolean): boolean
        
        
        """
        ...
    def setEphemName(self, string: str) -> None:
        """
            Set the name of external ephemeris used for OD.
        
            Parameters:
                ephemName (String): me of external ephemeris used
        
        
        """
        ...
    def setGravityModel(self, string: str, int: int, int2: int) -> None:
        """
            Set gravity model.
        
            Parameters:
                name (String): name of the model
                degree (int): degree of the model
                order (int): order of the model
        
        
        """
        ...
    def setInternationalDes(self, string: str) -> None:
        """
            Set the international designator used for object.
        
            Parameters:
                internationalDes (String): for the object to be set
        
        
        """
        ...
    def setIntrackThrust(self, boolean: bool) -> None:
        """
            Set boolean that indicates if intrack thrust modeling was into account or not.
        
            Parameters:
                IntrackThrustModeled (boolean): boolean
        
        
        """
        ...
    def setManeuverable(self, maneuvrable: 'Maneuvrable') -> None:
        """
            Set the object maneuver ability.
        
            Parameters:
                maneuverable (:class:`~org.orekit.files.ccsds.ndm.cdm.Maneuvrable`): ability to maneuver
        
        
        """
        ...
    def setNBodyPerturbations(self, list: java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]) -> None: ...
    def setObject(self, string: str) -> None:
        """
            Set the object name for which metadata are given.
        
            Parameters:
                object (String): = object 1 or 2 to be set
        
        
        """
        ...
    def setObjectDesignator(self, string: str) -> None:
        """
            Set the satellite designator for the object for which metadata are given.
        
            Parameters:
                objectDesignator (String): for the spacecraft to be set
        
        
        """
        ...
    def setObjectName(self, string: str) -> None:
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
                objectType (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ObjectType`): type of object
        
        
        """
        ...
    def setObsBeforeNextMessage(self, yesNoUnknown: org.orekit.files.ccsds.definitions.YesNoUnknown) -> None:
        """
            Set the flag indicating whether new tracking observations are anticipated prior to the issue of the next CDM associated
            with the event specified by CONJUNCTION_ID.
        
            Parameters:
                obsBeforeNextMessage (:class:`~org.orekit.files.ccsds.definitions.YesNoUnknown`): the obsBeforeNextMessage to set
        
        
        """
        ...
    def setOdmMsgLink(self, string: str) -> None:
        """
            Set the unique identifier of Orbit Data Message(s) that are linked (relevant) to this Conjunction Data Message.
        
            Parameters:
                odmMsgLink (String): the odmMsgLink to set
        
        
        """
        ...
    def setOperatorContactPosition(self, string: str) -> None:
        """
            Set the contact position for the object owner / operator.
        
            Parameters:
                opContact (String): for the object to be set
        
        
        """
        ...
    def setOperatorEmail(self, string: str) -> None:
        """
            Set the object operator email.
        
            Parameters:
                operatorEmail (String): operator email for the object to be set
        
        
        """
        ...
    def setOperatorOrganization(self, string: str) -> None:
        """
            Set the contact organisation of the object.
        
            Parameters:
                operatorOrganization (String): contact organisation for the object to be set
        
        
        """
        ...
    def setOperatorPhone(self, string: str) -> None:
        """
            Set the operator phone of the object.
        
            Parameters:
                operatorPhone (String): contact phone for the object to be set
        
        
        """
        ...
    def setOrbitCenter(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
            Set the central body name for object 1 and 2.
        
            Parameters:
                orbitCenter (:class:`~org.orekit.files.ccsds.definitions.BodyFacade`): name of the central body
        
        
        """
        ...
    def setRefFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set the name of the reference frame in which the state vector data are given.
        
            Parameters:
                refFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): reference frame
        
        
        """
        ...
    def setRelativeMetadata(self, cdmRelativeMetadata: 'CdmRelativeMetadata') -> None:
        """
            Set the relative metadata following header, they are the common metadata for the CDM.
        
            Parameters:
                relativeMetadata (:class:`~org.orekit.files.ccsds.ndm.cdm.CdmRelativeMetadata`): relative metadata
        
        
        """
        ...
    def setSolarRadiationPressure(self, boolean: bool) -> None:
        """
            Set boolean that indicates if Solar Radiation Pressure is taken into account or not.
        
            Parameters:
                isSolRadPressure (boolean): boolean
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.Metadata.validate` in class :class:`~org.orekit.files.ccsds.section.Metadata`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class CdmMetadataKey(java.lang.Enum['CdmMetadataKey']):
    """
    public enum CdmMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadata` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, cdmMetadata: CdmMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'CdmMetadataKey':
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
    def values() -> typing.List['CdmMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CdmMetadataKey c : CdmMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmMetadataWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class CdmMetadataWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for Metadata for CCSDS Conjunction Data Messages.
    
        Since:
            11.2
    """
    def __init__(self, cdmMetadata: CdmMetadata): ...

class CdmParser(org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser[Cdm, 'CdmParser']):
    """
    public class CdmParser extends :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`<:class:`~org.orekit.files.ccsds.ndm.cdm.Cdm`, :class:`~org.orekit.files.ccsds.ndm.cdm.CdmParser`>
    
        Base class for Conjunction Data Message parsers.
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            11.2
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior): ...
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
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeData`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeHeader(self) -> bool:
        """
            Finalize header after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def finalizeMetadata(self) -> bool:
        """
            Finalize metadata after parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.finalizeMetadata`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def getHeader(self) -> CdmHeader:
        """
            Get file header to fill.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.getHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                file header to fill
        
        
        """
        ...
    def inData(self) -> bool:
        """
            Acknowledge data parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inData`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inHeader(self) -> bool:
        """
            Acknowledge header parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def inMetadata(self) -> bool:
        """
            Acknowledge metada parsing has started.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.inMetadata`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareData(self) -> bool:
        """
            Prepare data for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareData`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareHeader(self) -> bool:
        """
            Prepare header for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def prepareMetadata(self) -> bool:
        """
            Prepare metadata for parsing.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.prepareMetadata`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                true if parser was able to perform the action
        
        
        """
        ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None:
        """
            Reset parser to initial state before parsing.
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class CdmRelativeMetadata:
    """
    public class CdmRelativeMetadata extends Object
    
        This class gathers the relative meta-data present in the Conjunction Data Message (CDM).
    
        Since:
            11.2
    """
    def __init__(self): ...
    def addComment(self, string: str) -> None:
        """
            Set comment for relative metadata.
        
            Parameters:
                comments (String): to be set
        
        
        """
        ...
    def checkNotNull(self, object: typing.Any, enum: java.lang.Enum[typing.Any]) -> None:
        """
            Complain if a field is null.
        
            Parameters:
                field (Object): field to check
                key (Enum<?> key): key associated with the field
        
        
        """
        ...
    def checkScreenVolumeConditions(self) -> None: ...
    def getApproachAngle(self) -> float:
        """
            Get the approach angle computed between Objects 1 and 2 in the RTN coordinate frame relative to object 1.
        
            Returns:
                the approachAngle
        
        
        """
        ...
    def getCollisionPercentile(self) -> typing.List[int]:
        """
            Get the array of 1 to n elements indicating the percentile(s) for which estimates of the collision probability are
            provided in the COLLISION_PROBABILITY variable.
        
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
            Get the Originatorâ€™s ID that uniquely identifies the conjunction to which the message refers.
        
            Returns:
                the conjunction id
        
        
        """
        ...
    def getMahalanobisDistance(self) -> float:
        """
            Get the Mahalanobis Distance. The length of the relative position vector, normalized to one-sigma dispersions of the
            combined error covariance in the direction of the relative position vector.
        
            Returns:
                the mahalanobisDistance
        
        
        """
        ...
    def getMaxCollisionProbability(self) -> float:
        """
        
            Returns:
                the maxCollisionProbability
        
        
        """
        ...
    def getMaxCollisionProbabilityMethod(self) -> org.orekit.files.ccsds.definitions.PocMethodFacade:
        """
        
            Returns:
                the maxCollisionProbabilityMethod
        
        
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
            Get the Object2Ã¢â‚¬â„¢s position vector relative to Object1's at TCA in RTN frame, getX for R component, getY for T
            component, getZ for N component.
        
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
            Get the Object2Ã¢â‚¬â„¢s velocity vector relative to Object1's at TCA in RTN frame, getX for R component, getY for T
            component, getZ for N component.
        
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
        
            Returns:
                the screenVolumeRadius
        
        
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
            Get the R or T (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding
            frame.
        
            Returns:
                first component size of the screening volume (in m)
        
        
        """
        ...
    def getScreenVolumeY(self) -> float:
        """
            Get the T or V (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding
            frame.
        
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
        
            Returns:
                the sefiCollisionProbability
        
        
        """
        ...
    def getSefiCollisionProbabilityMethod(self) -> org.orekit.files.ccsds.definitions.PocMethodFacade:
        """
        
            Returns:
                the sefiCollisionProbabilityMethod
        
        
        """
        ...
    def getSefiFragmentationModel(self) -> str:
        """
        
            Returns:
                the sefiFragmentationModel
        
        
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
            Get the Time System that: for CDM, is used for relative metadata, metadata, OD parameters, state vector. In CDM all date
            are given in UTC.
        
            Returns:
                the time system
        
        
        """
        ...
    def setApproachAngle(self, double: float) -> None:
        """
            Set the approach angle computed between Objects 1 and 2 in the RTN coordinate frame relative to object 1.
        
            Parameters:
                approachAngle (double): the approachAngle to set
        
        
        """
        ...
    def setCollisionPercentile(self, intArray: typing.List[int]) -> None:
        """
            Set the array of 1 to n elements indicating the percentile(s) for which estimates of the collision probability are
            provided in the COLLISION_PROBABILITY variable.
        
            Parameters:
                collisionPercentile (int[]): the collisionPercentile to set
        
        
        """
        ...
    def setCollisionProbaMethod(self, pocMethodFacade: org.orekit.files.ccsds.definitions.PocMethodFacade) -> None:
        """
            Set the method that was used to calculate the collision probability.
        
            Parameters:
                collisionProbaMethod (:class:`~org.orekit.files.ccsds.definitions.PocMethodFacade`): method used to calculate probability of collision
        
        
        """
        ...
    def setCollisionProbability(self, double: float) -> None:
        """
            Set the probability (between 0.0 and 1.0) that Object1 and Object2 will collide.
        
            Parameters:
                collisionProbability (double): first component size of the screening volume
        
        
        """
        ...
    def setConjunctionId(self, string: str) -> None:
        """
            Set the Originatorâ€™s ID that uniquely identifies the conjunction to which the message refers.
        
            Parameters:
                conjunctionId (String): the conjunction id to be set
        
        
        """
        ...
    def setMahalanobisDistance(self, double: float) -> None:
        """
            Set the Mahalanobis Distance. The length of the relative position vector, normalized to one-sigma dispersions of the
            combined error covariance in the direction of the relative position vector.
        
            Parameters:
                mahalanobisDistance (double): the mahalanobisDistance to set
        
        
        """
        ...
    def setMaxCollisionProbability(self, double: float) -> None:
        """
        
            Parameters:
                maxCollisionProbability (double): the maxCollisionProbability to set
        
        
        """
        ...
    def setMaxCollisionProbabilityMethod(self, pocMethodFacade: org.orekit.files.ccsds.definitions.PocMethodFacade) -> None:
        """
        
            Parameters:
                pocMethodFacade (:class:`~org.orekit.files.ccsds.definitions.PocMethodFacade`): the maxCollisionProbabilityMethod to set
        
        
        """
        ...
    def setMissDistance(self, double: float) -> None:
        """
            Set the norm of relative position vector at TCA.
        
            Parameters:
                missDistance (double): the miss distance to be set (in m)
        
        
        """
        ...
    def setNextMessageEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set Scheduled UTC epoch of the next CDM associated with the event identified by CONJUNCTION_ID.
        
            Parameters:
                nextMessageEpoch (:class:`~org.orekit.time.AbsoluteDate`): the nextMessageEpoch to set
        
        
        """
        ...
    def setPreviousMessageEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the UTC epoch of the previous CDM issued for the event identified by CONJUNCTION_ID.
        
            Parameters:
                previousMessageEpoch (:class:`~org.orekit.time.AbsoluteDate`): the previousMessageEpoch to set
        
        
        """
        ...
    def setPreviousMessageId(self, string: str) -> None:
        """
            Set the ID of previous CDM issued for event identified by CONJUNCTION_ID.
        
            Parameters:
                previousMessageId (String): the previousMessageId to set
        
        
        """
        ...
    def setRelativePositionN(self, double: float) -> None:
        """
            Set the N component of Object2â€™s position relative to Object1â€™s in RTN frame.
        
            Parameters:
                relativePositionN (double): the N component (in m) of Object2â€™s position relative to Object1â€™s
        
        
        """
        ...
    def setRelativePositionR(self, double: float) -> None:
        """
            Set the R component of Object2â€™s position relative to Object1â€™s in RTN frame.
        
            Parameters:
                relativePositionR (double): the R component (in m) of Object2â€™s position relative to Object1â€™s
        
        
        """
        ...
    def setRelativePositionT(self, double: float) -> None:
        """
            Set the T component of Object2â€™s position relative to Object1â€™s in RTN frame.
        
            Parameters:
                relativePositionT (double): the T component (in m) of Object2â€™s position relative to Object1â€™s
        
        
        """
        ...
    def setRelativeSpeed(self, double: float) -> None:
        """
            Set the norm of relative velocity vector at TCA.
        
            Parameters:
                relativeSpeed (double): the relative speed (in m/s) at TCA to be set
        
        
        """
        ...
    def setRelativeVelocityN(self, double: float) -> None:
        """
            Set the N component of Object2â€™s velocity relative to Object1â€™s in RTN frame.
        
            Parameters:
                relativeVelocityN (double): the N component (in m/s) of Object2â€™s velocity relative to Object1â€™s
        
        
        """
        ...
    def setRelativeVelocityR(self, double: float) -> None:
        """
            Set the R component of Object2â€™s velocity relative to Object1â€™s in RTN frame.
        
            Parameters:
                relativeVelocityR (double): the R component (in m/s) of Object2â€™s velocity relative to Object1â€™s
        
        
        """
        ...
    def setRelativeVelocityT(self, double: float) -> None:
        """
            Set the T component of Object2â€™s velocity relative to Object1â€™s in RTN frame.
        
            Parameters:
                relativeVelocityT (double): the T component (in m/s) of Object2â€™s velocity relative to Object1â€™s
        
        
        """
        ...
    def setScreenEntryTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time in UTC when Object2 enters the screening volume.
        
            Parameters:
                screenEntryTime (:class:`~org.orekit.time.AbsoluteDate`): time in UTC when Object2 enters the screening volume
        
        
        """
        ...
    def setScreenExitTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time in UTC when Object2 exits the screening volume.
        
            Parameters:
                screenExitTime (:class:`~org.orekit.time.AbsoluteDate`): time in UTC when Object2 exits the screening volume
        
        
        """
        ...
    def setScreenPcThreshold(self, double: float) -> None:
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
                screenType (:class:`~org.orekit.files.ccsds.ndm.cdm.ScreenType`): the screenType to set
        
        
        """
        ...
    def setScreenVolumeFrame(self, screenVolumeFrame: 'ScreenVolumeFrame') -> None:
        """
            Set the name of the Object1 centered reference frame in which the screening volume data are given.
        
            Parameters:
                screenVolumeFrame (:class:`~org.orekit.files.ccsds.ndm.cdm.ScreenVolumeFrame`): name of screen volume frame
        
        
        """
        ...
    def setScreenVolumeRadius(self, double: float) -> None:
        """
        
            Parameters:
                screenVolumeRadius (double): the screenVolumeRadius to set
        
        
        """
        ...
    def setScreenVolumeShape(self, screenVolumeShape: 'ScreenVolumeShape') -> None:
        """
            Set the shape of the screening volume.
        
            Parameters:
                screenVolumeShape (:class:`~org.orekit.files.ccsds.ndm.cdm.ScreenVolumeShape`): shape of the screening volume
        
        
        """
        ...
    def setScreenVolumeX(self, double: float) -> None:
        """
            Set the R or T (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding
            frame.
        
            Parameters:
                screenVolumeX (double): first component size of the screening volume (in m)
        
        
        """
        ...
    def setScreenVolumeY(self, double: float) -> None:
        """
            Set the T or V (depending on if RTN or TVN is selected) component size of the screening volume in the corresponding
            frame.
        
            Parameters:
                screenVolumeY (double): second component size of the screening volume (in m)
        
        
        """
        ...
    def setScreenVolumeZ(self, double: float) -> None:
        """
            Set the N component size of the screening volume in the corresponding frame.
        
            Parameters:
                screenVolumeZ (double): third component size of the screening volume (in m)
        
        
        """
        ...
    def setSefiCollisionProbability(self, double: float) -> None:
        """
        
            Parameters:
                sefiCollisionProbability (double): the sefiCollisionProbability to set
        
        
        """
        ...
    def setSefiCollisionProbabilityMethod(self, pocMethodFacade: org.orekit.files.ccsds.definitions.PocMethodFacade) -> None:
        """
        
            Parameters:
                pocMethodFacade (:class:`~org.orekit.files.ccsds.definitions.PocMethodFacade`): the sefiCollisionProbabilityMethod to set
        
        
        """
        ...
    def setSefiFragmentationModel(self, string: str) -> None:
        """
        
            Parameters:
                sefiFragmentationModel (String): the sefiFragmentationModel to set
        
        
        """
        ...
    def setStartScreenPeriod(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start time in UTC of the screening period for the conjunction assessment.
        
            Parameters:
                startScreenPeriod (:class:`~org.orekit.time.AbsoluteDate`): start time in UTC of the screening period to be set
        
        
        """
        ...
    def setStopScreenPeriod(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the stop time in UTC of the screening period for the conjunction assessment.
        
            Parameters:
                stopScreenPeriod (:class:`~org.orekit.time.AbsoluteDate`): stop time in UTC of the screening period to be set
        
        
        """
        ...
    def setTca(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the date and time in UTC of the closest approach.
        
            Parameters:
                tca (:class:`~org.orekit.time.AbsoluteDate`): time of closest approach to be set
        
        
        """
        ...
    def setTimeSystem(self, timeSystem: org.orekit.files.ccsds.definitions.TimeSystem) -> None:
        """
            Set the Time System that: for CDM, is used for relative metadata, metadata, OD parameters, state vector. In CDM all date
            are given in UTC.
        
            Parameters:
                timeSystem (:class:`~org.orekit.files.ccsds.definitions.TimeSystem`): the time system to be set
        
        
        """
        ...
    def validate(self) -> None:
        """
            Check is all mandatory entries have been initialized.
        
        """
        ...

class CdmRelativeMetadataKey(java.lang.Enum['CdmRelativeMetadataKey']):
    """
    public enum CdmRelativeMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.CdmRelativeMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.CdmRelativeMetadata` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, cdmRelativeMetadata: CdmRelativeMetadata) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.CdmRelativeMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'CdmRelativeMetadataKey':
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
    def values() -> typing.List['CdmRelativeMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CdmRelativeMetadataKey c : CdmRelativeMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmSegment(org.orekit.files.ccsds.section.Segment[CdmMetadata, CdmData]):
    """
    public class CdmSegment extends :class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadata`, :class:`~org.orekit.files.ccsds.ndm.cdm.CdmData`>
    
        This class stores the metadata and data for one object.
    
        Since:
            11.2
    """
    def __init__(self, cdmMetadata: CdmMetadata, cdmData: CdmData): ...

class CovarianceMethod(java.lang.Enum['CovarianceMethod']):
    """
    public enum CovarianceMethod extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.CovarianceMethod`>
    
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
    def valueOf(string: str) -> 'CovarianceMethod':
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
    def values() -> typing.List['CovarianceMethod']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CovarianceMethod c : CovarianceMethod.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Maneuvrable(java.lang.Enum['Maneuvrable']):
    """
    public enum Maneuvrable extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.Maneuvrable`>
    
        Maneuvrable possibilities used in CCSDS Conjunction Data Messages.
    
        Since:
            11.2
    """
    YES: typing.ClassVar['Maneuvrable'] = ...
    NO: typing.ClassVar['Maneuvrable'] = ...
    N_A: typing.ClassVar['Maneuvrable'] = ...
    @staticmethod
    def getEnum(string: str) -> 'Maneuvrable': ...
    def getValue(self) -> str: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Maneuvrable':
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
    def values() -> typing.List['Maneuvrable']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (Maneuvrable c : Maneuvrable.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ODParameters(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class ODParameters extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for OD parameters data block.
    
        Since:
            11.2
    """
    def __init__(self): ...
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
    def setActualOdSpan(self, double: float) -> None:
        """
            Set the actual OD time based on the observations available and the RECOMMENDED_OD_SPAN.
        
            Parameters:
                actualOdSpan (double): the actual OD time (in days)
        
        
        """
        ...
    def setObsAvailable(self, int: int) -> None:
        """
            Set the number of observations available for the OD of the object.
        
            Parameters:
                obsAvailable (int): the number of observations available
        
        
        """
        ...
    def setObsUsed(self, int: int) -> None:
        """
            Set the number of observations accepted for the OD of the object.
        
            Parameters:
                obsUsed (int): the number of observations used
        
        
        """
        ...
    def setOdEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the epoch of the orbit determination used for this message.
        
            Parameters:
                odEpoch (:class:`~org.orekit.time.AbsoluteDate`): the odEpoch to set
        
        
        """
        ...
    def setRecommendedOdSpan(self, double: float) -> None:
        """
            Set the recommended OD time span calculated for the object.
        
            Parameters:
                recommendedOdSpan (double): recommended OD time span (in days) calculated for the object
        
        
        """
        ...
    def setResidualsAccepted(self, double: float) -> None:
        """
            Set the percentage of residuals accepted in the OD of the object (from 0 to 100).
        
            Parameters:
                residualsAccepted (double): the percentage of residuals accepted in the OD to be set
        
        
        """
        ...
    def setTimeLastObsEnd(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start of a time interval (UTC) that contains the time of the last accepted observation.
        
            Parameters:
                timeLastObsEnd (:class:`~org.orekit.time.AbsoluteDate`): the start of a time interval (UTC)
        
        
        """
        ...
    def setTimeLastObsStart(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start of a time interval (UTC) that contains the time of the last accepted observation.
        
            Parameters:
                timeLastObsStart (:class:`~org.orekit.time.AbsoluteDate`): the start of a time interval (UTC)
        
        
        """
        ...
    def setTracksAvailable(self, int: int) -> None:
        """
            Set the number of sensor tracks available for the OD of the object.
        
            Parameters:
                tracksAvailable (int): the number of sensor tracks available
        
        
        """
        ...
    def setTracksUsed(self, int: int) -> None:
        """
            Set the number of sensor tracks used for the OD of the object.
        
            Parameters:
                tracksUsed (int): the number of sensor tracks used
        
        
        """
        ...
    def setWeightedRMS(self, double: float) -> None:
        """
            Set the weighted Root Mean Square (RMS) of the residuals from a batch least squares OD.
        
            Parameters:
                WeightedRMS (double): the weighted Root Mean Square (RMS) of the residuals from a batch least squares OD
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class ODParametersKey(java.lang.Enum['ODParametersKey']):
    """
    public enum ODParametersKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.ODParametersKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.ODParameters` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, oDParameters: ODParameters) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.ODParameters`): container to fill
        
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
    def valueOf(string: str) -> 'ODParametersKey':
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
    def values() -> typing.List['ODParametersKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ODParametersKey c : ODParametersKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ODParametersWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class ODParametersWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for OD parameters data block for CCSDS Conjunction Data Messages.
    
        Since:
            11.2
    """
    ...

class RTNCovariance(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class RTNCovariance extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for RTN covariance matrix data. This class as a RealMatrix as attribute which can be acces with
        getRTNCovariaxMatrix method. Beware that there are thus 2 ways to modify the RTN covariance : setC... ( setCrr, setCtr
        ...) which should be prioritized and getRTNCovariaxMatrix.setEntry(row, col, value).
    
        The RTN Covariance Matrix is provided in the 9Ãƒâ€”9 Lower Triangular Form. All parameters of the 6Ãƒâ€”6
        position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
    
        Since:
            11.2
    """
    def __init__(self): ...
    def getCdrgdrg(self) -> float:
        """
            Get the object [7,7] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def getCdrgn(self) -> float:
        """
            Get the object [7,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCdrgndot(self) -> float:
        """
            Get the object [7,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCdrgr(self) -> float:
        """
            Get the object [7,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCdrgrdot(self) -> float:
        """
            Get the object [7,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCdrgt(self) -> float:
        """
            Get the object [7,2] in covariance matrix.
        
            Returns:
                the object [7,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCdrgtdot(self) -> float:
        """
            Get the object [7,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCndotn(self) -> float:
        """
            Get the object [6,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCndotndot(self) -> float:
        """
            Get the object [6,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,6] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCndotr(self) -> float:
        """
            Get the object [6,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCndotrdot(self) -> float:
        """
            Get the object [6,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCndott(self) -> float:
        """
            Get the object [6,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCndottdot(self) -> float:
        """
            Get the object [6,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCnn(self) -> float:
        """
            Get the object [3,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [3,3] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCnr(self) -> float:
        """
            Get the object [3,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [3,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCnt(self) -> float:
        """
            Get the object [3,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [3,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCrdotn(self) -> float:
        """
            Get the object [4, 3] in covariance matrix (with index starting at 1) .
        
            Returns:
                the object [4, 3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCrdotr(self) -> float:
        """
            Get the object [4,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [4,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCrdotrdot(self) -> float:
        """
            Get the object [4, 4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [4, 4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCrdott(self) -> float:
        """
            Get the object [4,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [4,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCrr(self) -> float:
        """
            Get the object [1,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [1,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCsrpdrg(self) -> float:
        """
            Get the object [8,7] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def getCsrpn(self) -> float:
        """
            Get the object [8,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCsrpndot(self) -> float:
        """
            Get the object [8,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCsrpr(self) -> float:
        """
            Get the object [8,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCsrprdot(self) -> float:
        """
            Get the object [8,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCsrpsrp(self) -> float:
        """
            Get the object [8,8] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,8] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def getCsrpt(self) -> float:
        """
            Get the object [8,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCsrptdot(self) -> float:
        """
            Get the object [8,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCtdotn(self) -> float:
        """
            Get the object [5,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCtdotr(self) -> float:
        """
            Get the object [5, 1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5, 1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCtdotrdot(self) -> float:
        """
            Get the object [5,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCtdott(self) -> float:
        """
            Get the object [5,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCtdottdot(self) -> float:
        """
            Get the object [5,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCthrdrg(self) -> float:
        """
            Get the object [9,7] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,7] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def getCthrn(self) -> float:
        """
            Get the object [9,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,3] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCthrndot(self) -> float:
        """
            Get the object [9,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,6] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def getCthrr(self) -> float:
        """
            Get the object [9,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,1] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCthrrdot(self) -> float:
        """
            Get the object [9,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,4] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def getCthrsrp(self) -> float:
        """
            Get the object [9,8] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,8] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def getCthrt(self) -> float:
        """
            Get the object [9,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,2] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCthrtdot(self) -> float:
        """
            Get the object [9,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,5] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def getCthrthr(self) -> float:
        """
            Get the object [9,9] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,9] in covariance matrix (in mÂ²/sâ�´)
        
        
        """
        ...
    def getCtr(self) -> float:
        """
            Get the object [2,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [2,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCtt(self) -> float:
        """
            Get the object [2,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [2,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getRTNCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the RTN covariance matrix.
        
            The RTN Covariance Matrix is provided in the 9Ãƒâ€”9 Lower Triangular Form. All parameters of the 6Ãƒâ€”6
            position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        
            Returns:
                the RTN covariance matrix
        
        
        """
        ...
    def setCdrgdrg(self, double: float) -> None:
        """
            Set the object [7,7] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGDRG (double): = object [7,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def setCdrgn(self, double: float) -> None:
        """
            Set the object [7,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGN (double): = object [7,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCdrgndot(self, double: float) -> None:
        """
            Set the object [7,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGNdot (double): = object [7,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCdrgr(self, double: float) -> None:
        """
            Set the object [7,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGR (double): = object [7,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCdrgrdot(self, double: float) -> None:
        """
            Set the object [7,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGRdot (double): = object [7,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCdrgt(self, double: float) -> None:
        """
            Set the object [7,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGT (double): = object [7,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCdrgtdot(self, double: float) -> None:
        """
            Set the object [7,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGTdot (double): = object [7,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCndotn(self, double: float) -> None:
        """
            Set the object [6,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNdotN (double): = object [6,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCndotndot(self, double: float) -> None:
        """
            Set the object [6,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNdotNdot (double): = object [6,6] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCndotr(self, double: float) -> None:
        """
            Set the object [6,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNdotR (double): = object [6,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCndotrdot(self, double: float) -> None:
        """
            Set the object [6,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNdotRdot (double): = object [6,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCndott(self, double: float) -> None:
        """
            Set the object [6,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNdotT (double): = object [6,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCndottdot(self, double: float) -> None:
        """
            Set the object [6,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNdotTdot (double): = object [6,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCnn(self, double: float) -> None:
        """
            Set the object [3,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNN (double): = object [3,3] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCnr(self, double: float) -> None:
        """
            Set the object [3,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNR (double): = object [3,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCnt(self, double: float) -> None:
        """
            Set the object [3,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CNT (double): = object [3,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCovarianceMatrixEntry(self, int: int, int2: int, double: float) -> None:
        """
            Set an entry in the RTN covariance matrix.
        
            Both m(j, k) and m(k, j) are set.
        
            Parameters:
                j (int): row index (must be between 0 and 5 (inclusive)
                k (int): column index (must be between 0 and 5 (inclusive)
                entry (double): value of the matrix entry
        
        
        """
        ...
    def setCrdotn(self, double: float) -> None:
        """
            Set the object [4, 3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CRdotN (double): = object [4,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCrdotr(self, double: float) -> None:
        """
            Set the object [4,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CRdotR (double): = object [4,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCrdotrdot(self, double: float) -> None:
        """
            Set the object [4, 4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CRdotRdot (double): = object [4, 4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCrdott(self, double: float) -> None:
        """
            Set the object [4, 2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CRdotT (double): = object [4, 2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCrr(self, double: float) -> None:
        """
            Set the object [1,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CRR (double): = object [1,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCsrpdrg(self, double: float) -> None:
        """
            Set the object [8,7] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPDRG (double): = object [8,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def setCsrpn(self, double: float) -> None:
        """
            Set the object [8,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPN (double): = object [8,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCsrpndot(self, double: float) -> None:
        """
            Set the object [8,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPNdot (double): = object [8,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCsrpr(self, double: float) -> None:
        """
            Set the object [8,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPR (double): = object [8,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCsrprdot(self, double: float) -> None:
        """
            Set the object [8,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPRdot (double): = object [8,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCsrpsrp(self, double: float) -> None:
        """
            Set the object [8,8] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPSRP (double): = object [8,8] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def setCsrpt(self, double: float) -> None:
        """
            Set the object [8,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPT (double): = object [8,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCsrptdot(self, double: float) -> None:
        """
            Set the object [8,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPTdot (double): = object [8,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCtdotn(self, double: float) -> None:
        """
            Set the object [5,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTdotN (double): = object [5,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCtdotr(self, double: float) -> None:
        """
            Set the object [5,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTdotR (double): = object [5,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCtdotrdot(self, double: float) -> None:
        """
            Set the object [5,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTdotRdot (double): = object [5,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCtdott(self, double: float) -> None:
        """
            Set the object [5,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTdotT (double): = object [5,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCtdottdot(self, double: float) -> None:
        """
            Set the object [5,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTdotTdot (double): = object [5,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCthrdrg(self, double: float) -> None:
        """
            Set the object [9,7] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRDRG (double): = object [9,7] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def setCthrn(self, double: float) -> None:
        """
            Set the object [9,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRN (double): = object [9,3] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCthrndot(self, double: float) -> None:
        """
            Set the object [9,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRNdot (double): = object [9,6] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def setCthrr(self, double: float) -> None:
        """
            Set the object [9,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRR (double): = object [9,1] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCthrrdot(self, double: float) -> None:
        """
            Set the object [9,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRRdot (double): = object [9,4] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def setCthrsrp(self, double: float) -> None:
        """
            Set the object [9,8] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRSRP (double): = object [9,8] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def setCthrt(self, double: float) -> None:
        """
            Set the object [9,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRT (double): = object [9,2] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCthrtdot(self, double: float) -> None:
        """
            Set the object [9,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRTdot (double): = object [9,5] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def setCthrthr(self, double: float) -> None:
        """
            Set the object [9,9] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRTHR (double): = object [9,9] in covariance matrix (in mÂ²/sâ�´)
        
        
        """
        ...
    def setCtr(self, double: float) -> None:
        """
            Set the object [2,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTR (double): = object [2,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCtt(self, double: float) -> None:
        """
            Set the object [2,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTT (double): = object [2,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class RTNCovarianceKey(java.lang.Enum['RTNCovarianceKey']):
    """
    public enum RTNCovarianceKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.RTNCovarianceKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.RTNCovariance` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, rTNCovariance: RTNCovariance) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.RTNCovariance`): container to fill
        
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
    def valueOf(string: str) -> 'RTNCovarianceKey':
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
    def values() -> typing.List['RTNCovarianceKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (RTNCovarianceKey c : RTNCovarianceKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RTNCovarianceWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class RTNCovarianceWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for RTN covariance matrix data block for CCSDS Conjunction Data Messages.
    
        Since:
            11.2
    """
    ...

class ScreenType(java.lang.Enum['ScreenType']):
    """
    public enum ScreenType extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.ScreenType`>
    
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
    def valueOf(string: str) -> 'ScreenType':
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
    def values() -> typing.List['ScreenType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ScreenType c : ScreenType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ScreenVolumeFrame(java.lang.Enum['ScreenVolumeFrame']):
    """
    public enum ScreenVolumeFrame extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.ScreenVolumeFrame`>
    
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
    def valueOf(string: str) -> 'ScreenVolumeFrame':
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
    def values() -> typing.List['ScreenVolumeFrame']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ScreenVolumeFrame c : ScreenVolumeFrame.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ScreenVolumeShape(java.lang.Enum['ScreenVolumeShape']):
    """
    public enum ScreenVolumeShape extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.ScreenVolumeShape`>
    
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
    def valueOf(string: str) -> 'ScreenVolumeShape':
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
    def values() -> typing.List['ScreenVolumeShape']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ScreenVolumeShape c : ScreenVolumeShape.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SigmaEigenvectorsCovariance(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class SigmaEigenvectorsCovariance extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for Sigma/Eigenvectors Covariance data. The positional covariance one-sigma dispersions corresponding to the
        major, intermediate and minor eigenvalues, followed by the associated eigenvectors. The data is presented on a single
        line (12 values separated by spaces). (Condition: Mandatory if ALT_COV_TYPE = CSIG3EIGVEC3)
    """
    def __init__(self, boolean: bool): ...
    def getCsig3eigvec3(self) -> typing.List[float]:
        """
            Get the Sigma/Eigenvectors Covariance data.
        
            The Sigma/Eigenvectors Covariance data is only provided if
            :meth:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadataKey.ALT_COV_TYPE` is
            :meth:`~org.orekit.files.ccsds.ndm.cdm.AltCovarianceType.CSIG3EIGVEC3`, otherwise its terms will return NaN.
        
            Returns:
                covarianceData the covariance data in the Sigma/Eigenvectors format.
        
        
        """
        ...
    def isAltCovFlagSet(self) -> bool:
        """
            Get the flag indicating whether the alternate covariance type set in the CDM Object metadata section is
            Sigma/Eigenvectors Covariance.
        
            Returns:
                the altCovFlag
        
        
        """
        ...
    def setCsig3eigvec3(self, doubleArray: typing.List[float]) -> None:
        """
            Set the Sigma/Eigenvectors Covariance data.
        
            Parameters:
                csig3eigvec3 (double[]): the covariance data in the Sigma/Eigenvectors format.
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class SigmaEigenvectorsCovarianceKey(java.lang.Enum['SigmaEigenvectorsCovarianceKey']):
    """
    public enum SigmaEigenvectorsCovarianceKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.SigmaEigenvectorsCovarianceKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.SigmaEigenvectorsCovariance` entries.
    """
    COMMENT: typing.ClassVar['SigmaEigenvectorsCovarianceKey'] = ...
    CSIG3EIGVEC3: typing.ClassVar['SigmaEigenvectorsCovarianceKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, sigmaEigenvectorsCovariance: SigmaEigenvectorsCovariance) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.SigmaEigenvectorsCovariance`): container to fill
        
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
    def valueOf(string: str) -> 'SigmaEigenvectorsCovarianceKey':
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
    def values() -> typing.List['SigmaEigenvectorsCovarianceKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (SigmaEigenvectorsCovarianceKey c : SigmaEigenvectorsCovarianceKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StateVector(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class StateVector extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for state vector data.
    
        Since:
            11.2
    """
    def __init__(self): ...
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
    def setX(self, double: float) -> None:
        """
            Set object Position Vector X component.
        
            Parameters:
                X (double): object Position Vector X component (in m)
        
        
        """
        ...
    def setXdot(self, double: float) -> None:
        """
            Set object Velocity Vector X component.
        
            Parameters:
                Xdot (double): object Velocity Vector X component (in m/s)
        
        
        """
        ...
    def setY(self, double: float) -> None:
        """
            Set object Position Vector Y component.
        
            Parameters:
                Y (double): object Position Vector Y component (in m)
        
        
        """
        ...
    def setYdot(self, double: float) -> None:
        """
            Set object Velocity Vector Y component.
        
            Parameters:
                Ydot (double): object Velocity Vector Y component (in m/s)
        
        
        """
        ...
    def setZ(self, double: float) -> None:
        """
            Set object Position Vector Z component.
        
            Parameters:
                Z (double): object Position Vector Z component (in m)
        
        
        """
        ...
    def setZdot(self, double: float) -> None:
        """
            Set object Velocity Vector Z component.
        
            Parameters:
                Zdot (double): object Velocity Vector Z component (in m/s)
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class StateVectorKey(java.lang.Enum['StateVectorKey']):
    """
    public enum StateVectorKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.StateVectorKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.StateVector` entries.
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, stateVector: StateVector) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.StateVector`): container to fill
        
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
    def valueOf(string: str) -> 'StateVectorKey':
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
    def values() -> typing.List['StateVectorKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (StateVectorKey c : StateVectorKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class StateVectorWriter(org.orekit.files.ccsds.section.AbstractWriter):
    """
    public class StateVectorWriter extends :class:`~org.orekit.files.ccsds.section.AbstractWriter`
    
        Writer for state vector data for CCSDS Conjunction Data Messages.
    
        Since:
            11.2
    """
    ...

class XYZCovariance(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class XYZCovariance extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Container for XYZ covariance matrix data. This class as a RealMatrix as attribute which can be acces with
        getXYZCovariaxMatrix method. Beware that there are thus 2 ways to modify the XYZ covariance : setC... ( setCxx, setCyx
        ...) which should be prioritized and getXYZCovariaxMatrix.setEntry(row, col, value).
    
        The XYZ Covariance Matrix is only provided if :meth:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadataKey.ALT_COV_TYPE` is
        :meth:`~org.orekit.files.ccsds.ndm.cdm.AltCovarianceType.XYZ`, otherwise its terms will return NaN.
    
        When available, the matrix is given in the 9Ãƒâ€”9 Lower Triangular Form. All parameters of the 6Ãƒâ€”6
        position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
    """
    def __init__(self, boolean: bool): ...
    def getCdrgdrg(self) -> float:
        """
            Get the object [7,7] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def getCdrgx(self) -> float:
        """
            Get the object [7,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCdrgxdot(self) -> float:
        """
            Get the object [7,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCdrgy(self) -> float:
        """
            Get the object [7,2] in covariance matrix.
        
            Returns:
                the object [7,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCdrgydot(self) -> float:
        """
            Get the object [7,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCdrgz(self) -> float:
        """
            Get the object [7,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCdrgzdot(self) -> float:
        """
            Get the object [7,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [7,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCsrpdrg(self) -> float:
        """
            Get the object [8,7] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def getCsrpsrp(self) -> float:
        """
            Get the object [8,8] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,8] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def getCsrpx(self) -> float:
        """
            Get the object [8,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCsrpxdot(self) -> float:
        """
            Get the object [8,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCsrpy(self) -> float:
        """
            Get the object [8,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCsrpydot(self) -> float:
        """
            Get the object [8,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCsrpz(self) -> float:
        """
            Get the object [8,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def getCsrpzdot(self) -> float:
        """
            Get the object [8,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [8,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def getCthrdrg(self) -> float:
        """
            Get the object [9,7] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,7] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def getCthrsrp(self) -> float:
        """
            Get the object [9,8] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,8] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def getCthrthr(self) -> float:
        """
            Get the object [9,9] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,9] in covariance matrix (in mÂ²/sâ�´)
        
        
        """
        ...
    def getCthrx(self) -> float:
        """
            Get the object [9,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,1] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCthrxdot(self) -> float:
        """
            Get the object [9,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,4] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def getCthry(self) -> float:
        """
            Get the object [9,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,2] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCthrydot(self) -> float:
        """
            Get the object [9,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,5] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def getCthrz(self) -> float:
        """
            Get the object [9,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,3] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCthrzdot(self) -> float:
        """
            Get the object [9,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [9,6] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def getCxdotx(self) -> float:
        """
            Get the object [4,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [4,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCxdotxdot(self) -> float:
        """
            Get the object [4, 4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [4, 4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCxdoty(self) -> float:
        """
            Get the object [4,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [4,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCxdotz(self) -> float:
        """
            Get the object [4, 3] in covariance matrix (with index starting at 1) .
        
            Returns:
                the object [4, 3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCxx(self) -> float:
        """
            Get the object [1,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [1,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCydotx(self) -> float:
        """
            Get the object [5, 1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5, 1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCydotxdot(self) -> float:
        """
            Get the object [5,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCydoty(self) -> float:
        """
            Get the object [5,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCydotydot(self) -> float:
        """
            Get the object [5,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCydotz(self) -> float:
        """
            Get the object [5,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [5,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCyx(self) -> float:
        """
            Get the object [2,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [2,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCyy(self) -> float:
        """
            Get the object [2,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [2,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCzdotx(self) -> float:
        """
            Get the object [6,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCzdotxdot(self) -> float:
        """
            Get the object [6,4] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCzdoty(self) -> float:
        """
            Get the object [6,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCzdotydot(self) -> float:
        """
            Get the object [6,5] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCzdotz(self) -> float:
        """
            Get the object [6,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def getCzdotzdot(self) -> float:
        """
            Get the object [6,6] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [6,6] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def getCzx(self) -> float:
        """
            Get the object [3,1] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [3,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCzy(self) -> float:
        """
            Get the object [3,2] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [3,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getCzz(self) -> float:
        """
            Get the object [3,3] in covariance matrix (with index starting at 1).
        
            Returns:
                the object [3,3] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def getXYZCovarianceMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the XYZ covariance matrix.
        
            The XYZ Covariance Matrix is only provided if :meth:`~org.orekit.files.ccsds.ndm.cdm.CdmMetadataKey.ALT_COV_TYPE` is
            :meth:`~org.orekit.files.ccsds.ndm.cdm.AltCovarianceType.XYZ`, otherwise its terms will return NaN.
        
            When available, the matrix is given in the 9Ãƒâ€”9 Lower Triangular Form. All parameters of the 6Ãƒâ€”6
            position/velocity submatrix are mandatory. The remaining elements will return NaN if not provided.
        
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
    def setCdrgdrg(self, double: float) -> None:
        """
            Set the object [7,7] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGDRG (double): = object [7,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def setCdrgx(self, double: float) -> None:
        """
            Set the object [7,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGX (double): = object [7,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCdrgxdot(self, double: float) -> None:
        """
            Set the object [7,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGXdot (double): = object [7,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCdrgy(self, double: float) -> None:
        """
            Set the object [7,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGY (double): = object [7,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCdrgydot(self, double: float) -> None:
        """
            Set the object [7,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGYdot (double): = object [7,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCdrgz(self, double: float) -> None:
        """
            Set the object [7,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGZ (double): = object [7,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCdrgzdot(self, double: float) -> None:
        """
            Set the object [7,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CDRGZdot (double): = object [7,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCovarianceMatrixEntry(self, int: int, int2: int, double: float) -> None:
        """
            Set an entry in the XYZ covariance matrix.
        
            Both m(j, k) and m(k, j) are set.
        
            Parameters:
                j (int): row index (must be between 0 and 5 (inclusive)
                k (int): column index (must be between 0 and 5 (inclusive)
                entry (double): value of the matrix entry
        
        
        """
        ...
    def setCsrpdrg(self, double: float) -> None:
        """
            Set the object [8,7] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPDRG (double): = object [8,7] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def setCsrpsrp(self, double: float) -> None:
        """
            Set the object [8,8] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPSRP (double): = object [8,8] in covariance matrix (in mâ�´/kgÂ²)
        
        
        """
        ...
    def setCsrpx(self, double: float) -> None:
        """
            Set the object [8,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPX (double): = object [8,1] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCsrpxdot(self, double: float) -> None:
        """
            Set the object [8,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPXdot (double): = object [8,4] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCsrpy(self, double: float) -> None:
        """
            Set the object [8,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPY (double): = object [8,2] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCsrpydot(self, double: float) -> None:
        """
            Set the object [8,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPYdot (double): = object [8,5] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCsrpz(self, double: float) -> None:
        """
            Set the object [8,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPZ (double): = object [8,3] in covariance matrix (in mÂ³/kg)
        
        
        """
        ...
    def setCsrpzdot(self, double: float) -> None:
        """
            Set the object [8,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CSRPZdot (double): = object [8,6] in covariance matrix (in mÂ³/(kg.s))
        
        
        """
        ...
    def setCthrdrg(self, double: float) -> None:
        """
            Set the object [9,7] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRDRG (double): = object [9,7] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def setCthrsrp(self, double: float) -> None:
        """
            Set the object [9,8] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRSRP (double): = object [9,8] in covariance matrix (in mÂ³/(kg.sÂ²))
        
        
        """
        ...
    def setCthrthr(self, double: float) -> None:
        """
            Set the object [9,9] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRTHR (double): = object [9,9] in covariance matrix (in mÂ²/sâ�´)
        
        
        """
        ...
    def setCthrx(self, double: float) -> None:
        """
            Set the object [9,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRX (double): = object [9,1] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCthrxdot(self, double: float) -> None:
        """
            Set the object [9,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRXdot (double): = object [9,4] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def setCthry(self, double: float) -> None:
        """
            Set the object [9,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRY (double): = object [9,2] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCthrydot(self, double: float) -> None:
        """
            Set the object [9,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRYdot (double): = object [9,5] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def setCthrz(self, double: float) -> None:
        """
            Set the object [9,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRZ (double): = object [9,3] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCthrzdot(self, double: float) -> None:
        """
            Set the object [9,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CTHRZdot (double): = object [9,6] in covariance matrix (in mÂ²/sÂ³)
        
        
        """
        ...
    def setCxdotx(self, double: float) -> None:
        """
            Set the object [4,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CXdotX (double): = object [4,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCxdotxdot(self, double: float) -> None:
        """
            Set the object [4, 4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CXdotXdot (double): = object [4, 4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCxdoty(self, double: float) -> None:
        """
            Set the object [4, 2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CXdotY (double): = object [4, 2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCxdotz(self, double: float) -> None:
        """
            Set the object [4, 3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CXdotZ (double): = object [4,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCxx(self, double: float) -> None:
        """
            Set the object [1,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CXX (double): = object [1,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCydotx(self, double: float) -> None:
        """
            Set the object [5,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CYdotX (double): = object [5,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCydotxdot(self, double: float) -> None:
        """
            Set the object [5,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CYdotXdot (double): = object [5,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCydoty(self, double: float) -> None:
        """
            Set the object [5,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CYdotY (double): = object [5,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCydotydot(self, double: float) -> None:
        """
            Set the object [5,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CYdotYdot (double): = object [5,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCydotz(self, double: float) -> None:
        """
            Set the object [5,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CYdotZ (double): = object [5,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCyx(self, double: float) -> None:
        """
            Set the object [2,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CYX (double): = object [2,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCyy(self, double: float) -> None:
        """
            Set the object [2,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CYY (double): = object [2,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCzdotx(self, double: float) -> None:
        """
            Set the object [6,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZdotX (double): = object [6,1] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCzdotxdot(self, double: float) -> None:
        """
            Set the object [6,4] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZdotXdot (double): = object [6,4] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCzdoty(self, double: float) -> None:
        """
            Set the object [6,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZdotY (double): = object [6,2] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCzdotydot(self, double: float) -> None:
        """
            Set the object [6,5] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZdotYdot (double): = object [6,5] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCzdotz(self, double: float) -> None:
        """
            Set the object [6,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZdotZ (double): = object [6,3] in covariance matrix (in mÂ²/s)
        
        
        """
        ...
    def setCzdotzdot(self, double: float) -> None:
        """
            Set the object [6,6] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZdotZdot (double): = object [6,6] in covariance matrix (in mÂ²/sÂ²)
        
        
        """
        ...
    def setCzx(self, double: float) -> None:
        """
            Set the object [3,1] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZX (double): = object [3,1] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCzy(self, double: float) -> None:
        """
            Set the object [3,2] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZY (double): = object [3,2] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def setCzz(self, double: float) -> None:
        """
            Set the object [3,3] in covariance matrix (with index starting at 1).
        
            Parameters:
                CZZ (double): = object [3,3] in covariance matrix (in mÂ²)
        
        
        """
        ...
    def validate(self, double: float) -> None:
        """
            Check is all mandatory entries have been initialized.
        
            This method should throw an exception if some mandatory entries are missing or not compatible with version number.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.section.Section.validate` in interface :class:`~org.orekit.files.ccsds.section.Section`
        
            Overrides:
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class XYZCovarianceKey(java.lang.Enum['XYZCovarianceKey']):
    """
    public enum XYZCovarianceKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.XYZCovarianceKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.cdm.XYZCovariance` entries.
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, xYZCovariance: XYZCovariance) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.cdm.XYZCovariance`): container to fill
        
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
    def valueOf(string: str) -> 'XYZCovarianceKey':
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
    def values() -> typing.List['XYZCovarianceKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (XYZCovarianceKey c : XYZCovarianceKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class XmlSubStructureKey(java.lang.Enum['XmlSubStructureKey']):
    """
    public enum XmlSubStructureKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.cdm.XmlSubStructureKey`>
    
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
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, cdmParser: CdmParser) -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                parser (:class:`~org.orekit.files.ccsds.ndm.cdm.CdmParser`): CDM file parser
        
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
    def valueOf(string: str) -> 'XmlSubStructureKey':
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
    def values() -> typing.List['XmlSubStructureKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (XmlSubStructureKey c : XmlSubStructureKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CdmWriter(CdmMessageWriter):
    """
    public class CdmWriter extends :class:`~org.orekit.files.ccsds.ndm.cdm.CdmMessageWriter`
    
        Writer for CCSDS Conjunction Data Message.
    
        Since:
            11.2
    """
    CCSDS_CDM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_CDM_VERS
    
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
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext): ...
    def writeRelativeMetadataContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, cdmRelativeMetadata: CdmRelativeMetadata) -> None: ...
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, segment: org.orekit.files.ccsds.section.Segment[CdmMetadata, CdmData]) -> None: ...


class __module_protocol__(typing.Protocol):
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
