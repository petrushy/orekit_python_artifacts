import java.lang
import java.util
import org.hipparchus.complex
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.bodies
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.ndm.odm
import org.orekit.files.ccsds.ndm.odm.oem
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.generation
import org.orekit.files.ccsds.utils.lexical
import org.orekit.files.general
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import org.orekit.utils.units
import typing



class Covariance(org.orekit.time.TimeStamped):
    """
    public class Covariance extends Object implements :class:`~org.orekit.time.TimeStamped`
    
        Covariance entry.
    
        Since:
            11.0
    """
    def __init__(self, elementsType: org.orekit.files.ccsds.definitions.ElementsType, ordering: 'Ordering', absoluteDate: org.orekit.time.AbsoluteDate, stringArray: typing.List[str], int: int): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the covariance matrix.
        
            Returns:
                covariance matrix
        
        
        """
        ...
    def getType(self) -> org.orekit.files.ccsds.definitions.ElementsType:
        """
            Get the type of the elements.
        
            Returns:
                type of the elements
        
        
        """
        ...

class CovarianceHistory:
    """
    public class CovarianceHistory extends Object
    
        Covariance history.
    
        Since:
            11.0
    """
    def getCovariances(self) -> java.util.List[Covariance]: ...
    def getMetadata(self) -> 'CovarianceHistoryMetadata':
        """
            Get metadata.
        
            Returns:
                metadata
        
        
        """
        ...

class CovarianceHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class CovarianceHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for covariance history.
    
        Since:
            11.0
    """
    def getCovBasis(self) -> str:
        """
            Get basis of this covariance time history data.
        
            Returns:
                basis of this covariance time history data
        
        
        """
        ...
    def getCovBasisID(self) -> str:
        """
            Get identification number of the orbit determination or simulation upon which this covariance is based.
        
            Returns:
                identification number of the orbit determination or simulation upon which this covariance is based
        
        
        """
        ...
    def getCovConfidence(self) -> float:
        """
            Get the measure of confidence in covariance error matching reality.
        
            Returns:
                measure of confidence in covariance error matching reality
        
        
        """
        ...
    def getCovFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.CovarianceHistoryMetadata.getCovReferenceFrame`.
        
            Returns:
                epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.CovarianceHistoryMetadata.getCovReferenceFrame`
        
        
        """
        ...
    def getCovID(self) -> str:
        """
            Get covariance identification number.
        
            Returns:
                covariance identification number
        
        
        """
        ...
    def getCovNextID(self) -> str:
        """
            Get identification number of next covariance.
        
            Returns:
                identification number of next covariance
        
        
        """
        ...
    def getCovOrdering(self) -> 'Ordering':
        """
            Get covariance ordering.
        
            Returns:
                covariance ordering
        
        
        """
        ...
    def getCovPrevID(self) -> str:
        """
            Get identification number of previous covariance.
        
            Returns:
                identification number of previous covariance
        
        
        """
        ...
    def getCovReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get reference frame of the covariance.
        
            Returns:
                reference frame of the covariance
        
        
        """
        ...
    def getCovScaleMax(self) -> float:
        """
            Get the maximum scale factor to apply to achieve realism.
        
            Returns:
                maximum scale factor to apply to achieve realism
        
        
        """
        ...
    def getCovScaleMin(self) -> float:
        """
            Get the minimum scale factor to apply to achieve realism.
        
            Returns:
                minimum scale factor to apply to achieve realism
        
        
        """
        ...
    def getCovType(self) -> org.orekit.files.ccsds.definitions.ElementsType:
        """
            Get covariance element set type.
        
            Returns:
                covariance element set type
        
        
        """
        ...
    def getCovUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def setCovBasis(self, string: str) -> None:
        """
            Set basis of this covariance time history data.
        
            Parameters:
                covBasis (String): basis of this covariance time history data
        
        
        """
        ...
    def setCovBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this covariance is based.
        
            Parameters:
                covBasisID (String): identification number of the orbit determination or simulation upon which this covariance is based
        
        
        """
        ...
    def setCovConfidence(self, double: float) -> None:
        """
            Set the measure of confidence in covariance error matching reality.
        
            Parameters:
                covConfidence (double): measure of confidence in covariance error matching reality
        
        
        """
        ...
    def setCovFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.CovarianceHistoryMetadata.getCovReferenceFrame`.
        
            Parameters:
                covFrameEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.CovarianceHistoryMetadata.getCovReferenceFrame`
        
        
        """
        ...
    def setCovID(self, string: str) -> None:
        """
            Set covariance identification number.
        
            Parameters:
                covID (String): covariance identification number
        
        
        """
        ...
    def setCovNextID(self, string: str) -> None:
        """
            Set identification number of next covariance.
        
            Parameters:
                covNextID (String): identification number of next covariance
        
        
        """
        ...
    def setCovOrdering(self, ordering: 'Ordering') -> None:
        """
            Set covariance ordering.
        
            Parameters:
                covOrdering (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ordering`): covariance ordering
        
        
        """
        ...
    def setCovPrevID(self, string: str) -> None:
        """
            Set identification number of previous covariance.
        
            Parameters:
                covPrevID (String): identification number of previous covariance
        
        
        """
        ...
    def setCovReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame of the covariance.
        
            Parameters:
                covReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setCovScaleMax(self, double: float) -> None:
        """
            Set the maximum scale factor to apply to achieve realism.
        
            Parameters:
                covScaleMax (double): maximum scale factor to apply to achieve realism
        
        
        """
        ...
    def setCovScaleMin(self, double: float) -> None:
        """
            Set the minimum scale factor to apply to achieve realism.
        
            Parameters:
                covScaleMin (double): minimum scale factor to apply to achieve realism
        
        
        """
        ...
    def setCovType(self, elementsType: org.orekit.files.ccsds.definitions.ElementsType) -> None:
        """
            Set covariance element set type.
        
            Parameters:
                covType (:class:`~org.orekit.files.ccsds.definitions.ElementsType`): covariance element set type
        
        
        """
        ...
    def setCovUnits(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
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

class CovarianceHistoryMetadataKey(java.lang.Enum['CovarianceHistoryMetadataKey']):
    """
    public enum CovarianceHistoryMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.CovarianceHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.CovarianceHistoryMetadata` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_ID: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_PREV_ID: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_NEXT_ID: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_BASIS: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_BASIS_ID: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_REF_FRAME: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_FRAME_EPOCH: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_SCALE_MIN: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_SCALE_MAX: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_CONFIDENCE: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_TYPE: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_ORDERING: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    COV_UNITS: typing.ClassVar['CovarianceHistoryMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, covarianceHistoryMetadata: CovarianceHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.CovarianceHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'CovarianceHistoryMetadataKey':
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
    def values() -> typing.List['CovarianceHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CovarianceHistoryMetadataKey c : CovarianceHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ManBasis(java.lang.Enum['ManBasis']):
    """
    public enum ManBasis extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManBasis`>
    
        Basis of maneuver used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    CANDIDATE: typing.ClassVar['ManBasis'] = ...
    PLANNED: typing.ClassVar['ManBasis'] = ...
    ANTICIPATED: typing.ClassVar['ManBasis'] = ...
    DETERMINED_TLM: typing.ClassVar['ManBasis'] = ...
    DETERMINED_OD: typing.ClassVar['ManBasis'] = ...
    SIMULATED: typing.ClassVar['ManBasis'] = ...
    OTHER: typing.ClassVar['ManBasis'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ManBasis':
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
    def values() -> typing.List['ManBasis']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ManBasis c : ManBasis.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Maneuver(org.orekit.time.TimeStamped):
    """
    public class Maneuver extends Object implements :class:`~org.orekit.time.TimeStamped`
    
        Maneuver entry.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get acceleration.
        
            Returns:
                acceleration
        
        
        """
        ...
    def getAccelerationDirectionSigma(self) -> float:
        """
            Get one Ïƒ angular off-nominal acceleration direction.
        
            Returns:
                one Ïƒ angular off-nominal acceleration direction
        
        
        """
        ...
    def getAccelerationInterpolation(self) -> org.orekit.files.ccsds.definitions.OnOff:
        """
            Get interpolation mode between current and next acceleration line.
        
            Returns:
                interpolation mode between current and next acceleration line
        
        
        """
        ...
    def getAccelerationMagnitudeSigma(self) -> float:
        """
            Get one Ïƒ percent error on acceleration magnitude.
        
            Returns:
                one Ïƒ percent error on acceleration magnitude
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getDeltaMass(self) -> float:
        """
            Get mass change.
        
            Returns:
                mass change
        
        
        """
        ...
    def getDeployDirSigma(self) -> float:
        """
            Get one Ïƒ angular off-nominal deployment vector direction.
        
            Returns:
                one Ïƒ angular off-nominal deployment vector direction
        
        
        """
        ...
    def getDeployDv(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get velocity increment of deployed "child" object.
        
            Returns:
                velocity increment of deployed "child" object
        
        
        """
        ...
    def getDeployDvCda(self) -> float:
        """
            Get typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object.
        
            Returns:
                typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object
        
        
        """
        ...
    def getDeployDvRatio(self) -> float:
        """
            Get ratio of child-to-host Î”V vectors.
        
            Returns:
                ratio of child-to-host Î”V vectors
        
        
        """
        ...
    def getDeployDvSigma(self) -> float:
        """
            Get one Ïƒ percent error on deployment Î”V magnitude.
        
            Returns:
                one Ïƒ percent error on deployment Î”V magnitude
        
        
        """
        ...
    def getDeployId(self) -> str:
        """
            Get identifier of resulting "child" object deployed from this host.
        
            Returns:
                identifier of resulting "child" object deployed from this host
        
        
        """
        ...
    def getDeployMass(self) -> float:
        """
            Get decrement in host mass as a result of deployment.
        
            Returns:
                decrement in host mass as a result of deployment (shall be â‰¤ 0)
        
        
        """
        ...
    def getDuration(self) -> float:
        """
            Get duration.
        
            Returns:
                duration
        
        
        """
        ...
    def getDv(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get velocity increment.
        
            Returns:
                velocity increment
        
        
        """
        ...
    def getDvDirSigma(self) -> float:
        """
            Get one Ïƒ angular off-nominal Î”V direction.
        
            Returns:
                one Ïƒ angular off-nominal Î”V direction
        
        
        """
        ...
    def getDvMagSigma(self) -> float:
        """
            Get one Ïƒ percent error on Î”V magnitude.
        
            Returns:
                one Ïƒ percent error on Î”V magnitude
        
        
        """
        ...
    def getThrust(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get thrust.
        
            Returns:
                thrust
        
        
        """
        ...
    def getThrustDirectionSigma(self) -> float:
        """
            Get one Ïƒ angular off-nominal thrust direction.
        
            Returns:
                one Ïƒ angular off-nominal thrust direction
        
        
        """
        ...
    def getThrustEfficiency(self) -> float:
        """
            Get thrust efficiency Î·.
        
            Returns:
                thrust efficiency Î· (typically between 0.0 and 1.0)
        
        
        """
        ...
    def getThrustInterpolation(self) -> org.orekit.files.ccsds.definitions.OnOff:
        """
            Get interpolation mode between current and next thrust line.
        
            Returns:
                interpolation mode between current and next thrust line
        
        
        """
        ...
    def getThrustIsp(self) -> float:
        """
            Get thrust specific impulse.
        
            Returns:
                thrust specific impulse
        
        
        """
        ...
    def getThrustMagnitudeSigma(self) -> float:
        """
            Get one Ïƒ percent error on thrust magnitude.
        
            Returns:
                one Ïƒ percent error on thrust magnitude
        
        
        """
        ...
    def setAcceleration(self, int: int, double: float) -> None:
        """
            Set acceleration component.
        
            Parameters:
                i (int): component index
                ai (double): i :sup:`th` component of acceleration
        
        
        """
        ...
    def setAccelerationDirectionSigma(self, double: float) -> None:
        """
            Set one Ïƒ angular off-nominal acceleration direction.
        
            Parameters:
                accelerationDirectionSigma (double): one Ïƒ angular off-nominal acceleration direction
        
        
        """
        ...
    def setAccelerationInterpolation(self, onOff: org.orekit.files.ccsds.definitions.OnOff) -> None:
        """
            Set interpolation mode between current and next acceleration line.
        
            Parameters:
                accelerationInterpolation (:class:`~org.orekit.files.ccsds.definitions.OnOff`): interpolation mode between current and next acceleration line
        
        
        """
        ...
    def setAccelerationMagnitudeSigma(self, double: float) -> None:
        """
            Set one Ïƒ percent error on acceleration magnitude.
        
            Parameters:
                accelerationMagnitudeSigma (double): one Ïƒ percent error on acceleration magnitude
        
        
        """
        ...
    def setDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): maneuver date
        
        
        """
        ...
    def setDeltaMass(self, double: float) -> None:
        """
            Set mass change.
        
            Parameters:
                deltaMass (double): mass change
        
        
        """
        ...
    def setDeployDirSigma(self, double: float) -> None:
        """
            Set one Ïƒ angular off-nominal deployment vector direction.
        
            Parameters:
                deployDirSigma (double): one Ïƒ angular off-nominal deployment vector direction
        
        
        """
        ...
    def setDeployDv(self, int: int, double: float) -> None:
        """
            Set velocity increment component of deployed "child" object.
        
            Parameters:
                i (int): component index
                deployDvi (double): i :sup:`th` component of velocity increment of deployed "child" object
        
        
        """
        ...
    def setDeployDvCda(self, double: float) -> None:
        """
            Set typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object.
        
            Parameters:
                deployDvCda (double): typical (50th percentile) product of drag coefficient times cross-sectional area of deployed "child" object
        
        
        """
        ...
    def setDeployDvRatio(self, double: float) -> None:
        """
            Set ratio of child-to-host Î”V vectors.
        
            Parameters:
                deployDvRatio (double): ratio of child-to-host Î”V vectors
        
        
        """
        ...
    def setDeployDvSigma(self, double: float) -> None:
        """
            Set one Ïƒ percent error on deployment Î”V magnitude.
        
            Parameters:
                deployDvSigma (double): one Ïƒ percent error on deployment Î”V magnitude
        
        
        """
        ...
    def setDeployId(self, string: str) -> None:
        """
            Set identifier of resulting "child" object deployed from this host.
        
            Parameters:
                deployId (String): identifier of resulting "child" object deployed from this host
        
        
        """
        ...
    def setDeployMass(self, double: float) -> None:
        """
            Set decrement in host mass as a result of deployment.
        
            Parameters:
                deployMass (double): decrement in host mass as a result of deployment (shall be â‰¤ 0)
        
        
        """
        ...
    def setDuration(self, double: float) -> None:
        """
            Set duration.
        
            Parameters:
                duration (double): duration
        
        
        """
        ...
    def setDv(self, int: int, double: float) -> None:
        """
            Set velocity increment component.
        
            Parameters:
                i (int): component index
                dVi (double): i :sup:`th` component of velocity increment
        
        
        """
        ...
    def setDvDirSigma(self, double: float) -> None:
        """
            Set one Ïƒ angular off-nominal Î”V direction.
        
            Parameters:
                dvDirSigma (double): one Ïƒ angular off-nominal Î”V direction
        
        
        """
        ...
    def setDvMagSigma(self, double: float) -> None:
        """
            Set one Ïƒ percent error on Î”V magnitude.
        
            Parameters:
                dvMagSigma (double): one Ïƒ percent error on Î”V magnitude
        
        
        """
        ...
    def setThrust(self, int: int, double: float) -> None:
        """
            Set thrust component.
        
            Parameters:
                i (int): component index
                ti (double): i :sup:`th` component of thrust
        
        
        """
        ...
    def setThrustDirectionSigma(self, double: float) -> None:
        """
            Set one Ïƒ angular off-nominal thrust direction.
        
            Parameters:
                thrustDirectionSigma (double): one Ïƒ angular off-nominal thrust direction
        
        
        """
        ...
    def setThrustEfficiency(self, double: float) -> None:
        """
            Set thrust efficiency Î·.
        
            Parameters:
                thrustEfficiency (double): thrust efficiency Î· (typically between 0.0 and 1.0)
        
        
        """
        ...
    def setThrustInterpolation(self, onOff: org.orekit.files.ccsds.definitions.OnOff) -> None:
        """
            Set interpolation mode between current and next thrust line.
        
            Parameters:
                thrustInterpolation (:class:`~org.orekit.files.ccsds.definitions.OnOff`): interpolation mode between current and next thrust line
        
        
        """
        ...
    def setThrustIsp(self, double: float) -> None:
        """
            Set thrust specific impulse.
        
            Parameters:
                thrustIsp (double): thrust specific impulse
        
        
        """
        ...
    def setThrustMagnitudeSigma(self, double: float) -> None:
        """
            Set one Ïƒ percent error on thrust magnitude.
        
            Parameters:
                thrustMagnitudeSigma (double): one Ïƒ percent error on thrust magnitude
        
        
        """
        ...

class ManeuverFieldType(java.lang.Enum['ManeuverFieldType']):
    """
    public enum ManeuverFieldType extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverFieldType`>
    
        Maneuver field type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    TIME_ABSOLUTE: typing.ClassVar['ManeuverFieldType'] = ...
    TIME_RELATIVE: typing.ClassVar['ManeuverFieldType'] = ...
    MAN_DURA: typing.ClassVar['ManeuverFieldType'] = ...
    DELTA_MASS: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_X: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_Y: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_Z: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_INTERP: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_MAG_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    ACC_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DV_X: typing.ClassVar['ManeuverFieldType'] = ...
    DV_Y: typing.ClassVar['ManeuverFieldType'] = ...
    DV_Z: typing.ClassVar['ManeuverFieldType'] = ...
    DV_MAG_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DV_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    THR_X: typing.ClassVar['ManeuverFieldType'] = ...
    THR_Y: typing.ClassVar['ManeuverFieldType'] = ...
    THR_Z: typing.ClassVar['ManeuverFieldType'] = ...
    THR_EFFIC: typing.ClassVar['ManeuverFieldType'] = ...
    THR_INTERP: typing.ClassVar['ManeuverFieldType'] = ...
    THR_ISP: typing.ClassVar['ManeuverFieldType'] = ...
    THR_MAG_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    THR_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_ID: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_X: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_Y: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_Z: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_MASS: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DIR_SIGMA: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_RATIO: typing.ClassVar['ManeuverFieldType'] = ...
    DEPLOY_DV_CDA: typing.ClassVar['ManeuverFieldType'] = ...
    def checkUnit(self, unit: org.orekit.utils.units.Unit) -> None:
        """
            Check if parsed unit is compatible with field type.
        
            Parameters:
                parsedUnit (:class:`~org.orekit.utils.units.Unit`): unit to check
        
        
        """
        ...
    def getUnit(self) -> org.orekit.utils.units.Unit:
        """
            Get the field unit.
        
            Returns:
                field unit
        
        
        """
        ...
    def isTime(self) -> bool:
        """
            Check if a field is a time field.
        
            Returns:
                true if field is a time field
        
        
        """
        ...
    def outputField(self, timeConverter: org.orekit.files.ccsds.definitions.TimeConverter, maneuver: Maneuver) -> str:
        """
            Output one maneuver field.
        
            Parameters:
                converter (:class:`~org.orekit.files.ccsds.definitions.TimeConverter`): converter for dates
                maneuver (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Maneuver`): maneuver containing the field to output
        
            Returns:
                output field
        
        
        """
        ...
    def process(self, string: str, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, maneuver: Maneuver, int: int, string2: str) -> None:
        """
            Process one field.
        
            Parameters:
                field (String): field to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                maneuver (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Maneuver`): maneuver to fill
                lineNumber (int): line number at which the field occurs
                fileName (String): name of the file in which the field occurs
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ManeuverFieldType':
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
    def values() -> typing.List['ManeuverFieldType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ManeuverFieldType c : ManeuverFieldType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ManeuverHistory:
    """
    public class ManeuverHistory extends Object
    
        Maneuver history.
    
        Since:
            11.0
    """
    def getManeuvers(self) -> java.util.List[Maneuver]: ...
    def getMetadata(self) -> 'ManeuverHistoryMetadata':
        """
            Get metadata.
        
            Returns:
                metadata
        
        
        """
        ...

class ManeuverHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class ManeuverHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for maneuver history.
    
        Since:
            11.0
    """
    def getDcBodyFrame(self) -> org.orekit.files.ccsds.definitions.SpacecraftBodyFrame:
        """
            Get spacecraft body frame in which :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyTrigger`
            is specified.
        
            Returns:
                spacecraft body frame in which :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyTrigger` is
                specified
        
        
        """
        ...
    def getDcBodyTrigger(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyFrame` for triggering duty
            cycle.
        
            Returns:
                direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyFrame` for triggering duty
                cycle
        
        
        """
        ...
    def getDcExecStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start time of initial duty cycle-based maneuver execution.
        
            Returns:
                start time of initial duty cycle-based maneuver execution
        
        
        """
        ...
    def getDcExecStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end time of final duty cycle-based maneuver execution.
        
            Returns:
                end time of final duty cycle-based maneuver execution
        
        
        """
        ...
    def getDcMaxCycles(self) -> int:
        """
            Get the maximum number of "ON" duty cycles.
        
            Returns:
                maximum number of "ON" duty cycles (-1 if not set)
        
        
        """
        ...
    def getDcMinCycles(self) -> int:
        """
            Get the minimum number of "ON" duty cycles.
        
            Returns:
                minimum number of "ON" duty cycles (-1 if not set)
        
        
        """
        ...
    def getDcPhaseStartAngle(self) -> float:
        """
            Get phase angle of pulse start.
        
            Returns:
                phase angle of pulse start
        
        
        """
        ...
    def getDcPhaseStopAngle(self) -> float:
        """
            Get phase angle of pulse stop.
        
            Returns:
                phase angle of pulse stop
        
        
        """
        ...
    def getDcRefDir(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get reference direction for triggering duty cycle.
        
            Returns:
                reference direction for triggering duty cycle
        
        
        """
        ...
    def getDcRefTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get duty cycle thrust reference time.
        
            Returns:
                duty cycle thrust reference time
        
        
        """
        ...
    def getDcTimePulseDuration(self) -> float:
        """
            Get duty cycle pulse "ON" duration.
        
            Returns:
                duty cycle pulse "ON" duration
        
        
        """
        ...
    def getDcTimePulsePeriod(self) -> float:
        """
            Get duty cycle elapsed time between start of a pulse and start of next pulse.
        
            Returns:
                duty cycle elapsed time between start of a pulse and start of next pulse
        
        
        """
        ...
    def getDcType(self) -> org.orekit.files.ccsds.definitions.DutyCycleType:
        """
            Get type of duty cycle.
        
            Returns:
                type of duty cycle
        
        
        """
        ...
    def getDcWindowClose(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end time of duty cycle-based maneuver window.
        
            Returns:
                end time of duty cycle-based maneuver window
        
        
        """
        ...
    def getDcWindowOpen(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start time of duty cycle-based maneuver window.
        
            Returns:
                start time of duty cycle-based maneuver window
        
        
        """
        ...
    def getGravitationalAssist(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
            Get the origin of gravitational assist.
        
            Returns:
                the origin of gravitational assist.
        
        
        """
        ...
    def getManBasis(self) -> ManBasis:
        """
            Get basis of this maneuver history data.
        
            Returns:
                basis of this maneuver history data
        
        
        """
        ...
    def getManBasisID(self) -> str:
        """
            Get identification number of the orbit determination or simulation upon which this maneuver is based.
        
            Returns:
                identification number of the orbit determination or simulation upon which this maneuver is based
        
        
        """
        ...
    def getManComposition(self) -> java.util.List[ManeuverFieldType]: ...
    def getManDeviceID(self) -> str:
        """
            Get identifier of the device used for this maneuver.
        
            Returns:
                identifier of the device used for this maneuver
        
        
        """
        ...
    def getManFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getManReferenceFrame`.
        
            Returns:
                epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getManReferenceFrame`
        
        
        """
        ...
    def getManID(self) -> str:
        """
            Get maneuver identification number.
        
            Returns:
                maneuver identification number
        
        
        """
        ...
    def getManNextEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get start time of next maneuver.
        
            Returns:
                start time of next maneuver
        
        
        """
        ...
    def getManNextID(self) -> str:
        """
            Get identification number of next maneuver.
        
            Returns:
                identification number of next maneuver
        
        
        """
        ...
    def getManPredSource(self) -> str:
        """
            Get prediction source on which this maneuver is based.
        
            Returns:
                prediction source on which this maneuver is based
        
        
        """
        ...
    def getManPrevEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get completion time of previous maneuver.
        
            Returns:
                completion time of previous maneuver
        
        
        """
        ...
    def getManPrevID(self) -> str:
        """
            Get identification number of previous maneuver.
        
            Returns:
                identification number of previous maneuver
        
        
        """
        ...
    def getManPurpose(self) -> java.util.List[str]:
        """
            Get the purposes of the maneuver.
        
            Returns:
                purposes of the maneuver
        
        
        """
        ...
    def getManReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get reference frame of the maneuver.
        
            Returns:
                reference frame of the maneuver
        
        
        """
        ...
    def getManUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
    def setDcBodyFrame(self, spacecraftBodyFrame: org.orekit.files.ccsds.definitions.SpacecraftBodyFrame) -> None:
        """
            Set spacecraft body frame in which :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyTrigger`
            is specified.
        
            Parameters:
                dcBodyFrame (:class:`~org.orekit.files.ccsds.definitions.SpacecraftBodyFrame`): spacecraft body frame in which :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyTrigger` is
                    specified
        
        
        """
        ...
    def setDcBodyTrigger(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyFrame` for triggering duty
            cycle.
        
            Parameters:
                dcBodyTrigger (Vector3D): direction in :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getDcBodyFrame` for triggering duty
                    cycle
        
        
        """
        ...
    def setDcExecStart(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start time of initial duty cycle-based maneuver execution.
        
            Parameters:
                dcExecStart (:class:`~org.orekit.time.AbsoluteDate`): start time of initial duty cycle-based maneuver execution
        
        
        """
        ...
    def setDcExecStop(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the end time of final duty cycle-based maneuver execution.
        
            Parameters:
                dcExecStop (:class:`~org.orekit.time.AbsoluteDate`): end time of final duty cycle-based maneuver execution
        
        
        """
        ...
    def setDcMaxCycles(self, int: int) -> None:
        """
            Set the maximum number of "ON" duty cycles.
        
            Parameters:
                dcMaxCycles (int): maximum number of "ON" duty cycles
        
        
        """
        ...
    def setDcMinCycles(self, int: int) -> None:
        """
            Set the minimum number of "ON" duty cycles.
        
            Parameters:
                dcMinCycles (int): minimum number of "ON" duty cycles
        
        
        """
        ...
    def setDcPhaseStartAngle(self, double: float) -> None:
        """
            Set phase angle of pulse start.
        
            Parameters:
                dcPhaseStartAngle (double): phase angle of pulse start
        
        
        """
        ...
    def setDcPhaseStopAngle(self, double: float) -> None:
        """
            Set phase angle of pulse stop.
        
            Parameters:
                dcPhaseStopAngle (double): phase angle of pulse stop
        
        
        """
        ...
    def setDcRefDir(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Set reference direction for triggering duty cycle.
        
            Parameters:
                dcRefDir (Vector3D): reference direction for triggering duty cycle
        
        
        """
        ...
    def setDcRefTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set duty cycle thrust reference time.
        
            Parameters:
                dcRefTime (:class:`~org.orekit.time.AbsoluteDate`): duty cycle thrust reference time
        
        
        """
        ...
    def setDcTimePulseDuration(self, double: float) -> None:
        """
            Set duty cycle pulse "ON" duration.
        
            Parameters:
                dcTimePulseDuration (double): duty cycle pulse "ON" duration
        
        
        """
        ...
    def setDcTimePulsePeriod(self, double: float) -> None:
        """
            Set duty cycle elapsed time between start of a pulse and start of next pulse.
        
            Parameters:
                dcTimePulsePeriod (double): duty cycle elapsed time between start of a pulse and start of next pulse
        
        
        """
        ...
    def setDcType(self, dutyCycleType: org.orekit.files.ccsds.definitions.DutyCycleType) -> None:
        """
            Set type of duty cycle.
        
            Parameters:
                dcType (:class:`~org.orekit.files.ccsds.definitions.DutyCycleType`): type of duty cycle
        
        
        """
        ...
    def setDcWindowClose(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the end time of duty cycle-based maneuver window.
        
            Parameters:
                dcWindowClose (:class:`~org.orekit.time.AbsoluteDate`): end time of duty cycle-based maneuver window
        
        
        """
        ...
    def setDcWindowOpen(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the start time of duty cycle-based maneuver window.
        
            Parameters:
                dcWindowOpen (:class:`~org.orekit.time.AbsoluteDate`): start time of duty cycle-based maneuver window
        
        
        """
        ...
    def setGravitationalAssist(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
            Set the origin of gravitational assist.
        
            Parameters:
                gravitationalAssist (:class:`~org.orekit.files.ccsds.definitions.BodyFacade`): origin of gravitational assist to be set
        
        
        """
        ...
    def setManBasis(self, manBasis: ManBasis) -> None:
        """
            Set basis of this maneuver history data.
        
            Parameters:
                manBasis (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManBasis`): basis of this maneuver history data
        
        
        """
        ...
    def setManBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this maneuver is based.
        
            Parameters:
                manBasisID (String): identification number of the orbit determination or simulation upon which this maneuver is based
        
        
        """
        ...
    def setManComposition(self, list: java.util.List[ManeuverFieldType]) -> None: ...
    def setManDeviceID(self, string: str) -> None:
        """
            Set identifier of the device used for this maneuver.
        
            Parameters:
                manDeviceID (String): identifier of the device used for this maneuver
        
        
        """
        ...
    def setManFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getManReferenceFrame`.
        
            Parameters:
                manFrameEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata.getManReferenceFrame`
        
        
        """
        ...
    def setManID(self, string: str) -> None:
        """
            Set maneuver identification number.
        
            Parameters:
                manID (String): maneuver identification number
        
        
        """
        ...
    def setManNextEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set start time of next maneuver.
        
            Parameters:
                manNextEpoch (:class:`~org.orekit.time.AbsoluteDate`): start time of next maneuver
        
        
        """
        ...
    def setManNextID(self, string: str) -> None:
        """
            Set identification number of next maneuver.
        
            Parameters:
                manNextID (String): identification number of next maneuver
        
        
        """
        ...
    def setManPredSource(self, string: str) -> None:
        """
            Set prediction source on which this maneuver is based.
        
            Parameters:
                manPredSource (String): prediction source on which this maneuver is based
        
        
        """
        ...
    def setManPrevEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set completion time of previous maneuver.
        
            Parameters:
                manPrevEpoch (:class:`~org.orekit.time.AbsoluteDate`): completion time of previous maneuver
        
        
        """
        ...
    def setManPrevID(self, string: str) -> None:
        """
            Set identification number of previous maneuver.
        
            Parameters:
                manPrevID (String): identification number of previous maneuver
        
        
        """
        ...
    def setManPurpose(self, list: java.util.List[str]) -> None:
        """
            Set the purposes of the maneuver.
        
            Parameters:
                manPurpose (List<String> manPurpose): purposes of the maneuver
        
        
        """
        ...
    def setManReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame of the maneuver.
        
            Parameters:
                manReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setManUnits(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
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

class ManeuverHistoryMetadataKey(java.lang.Enum['ManeuverHistoryMetadataKey']):
    """
    public enum ManeuverHistoryMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_ID: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_PREV_ID: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_NEXT_ID: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_BASIS: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_BASIS_ID: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_DEVICE_ID: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_PREV_EPOCH: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_NEXT_EPOCH: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_PURPOSE: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_PRED_SOURCE: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_REF_FRAME: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_FRAME_EPOCH: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    GRAV_ASSIST_NAME: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_TYPE: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_WIN_OPEN: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_WIN_CLOSE: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_MIN_CYCLES: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_MAX_CYCLES: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_EXEC_START: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_EXEC_STOP: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_REF_TIME: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_TIME_PULSE_DURATION: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_TIME_PULSE_PERIOD: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_REF_DIR: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_BODY_FRAME: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_BODY_TRIGGER: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_PA_START_ANGLE: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    DC_PA_STOP_ANGLE: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_COMPOSITION: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    MAN_UNITS: typing.ClassVar['ManeuverHistoryMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, maneuverHistoryMetadata: ManeuverHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ManeuverHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'ManeuverHistoryMetadataKey':
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
    def values() -> typing.List['ManeuverHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ManeuverHistoryMetadataKey c : ManeuverHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ObjectType(java.lang.Enum['ObjectType']):
    """
    public enum ObjectType extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ObjectType`>
    
        Object type used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    PAYLOAD: typing.ClassVar['ObjectType'] = ...
    ROCKET_BODY: typing.ClassVar['ObjectType'] = ...
    DEBRIS: typing.ClassVar['ObjectType'] = ...
    UNKNOWN: typing.ClassVar['ObjectType'] = ...
    OTHER: typing.ClassVar['ObjectType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ObjectType':
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
    def values() -> typing.List['ObjectType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ObjectType c : ObjectType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Ocm(org.orekit.files.ccsds.ndm.NdmConstituent[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment['OcmMetadata', 'OcmData']], org.orekit.files.general.EphemerisFile[org.orekit.utils.TimeStampedPVCoordinates, 'TrajectoryStateHistory']):
    """
    public class Ocm extends :class:`~org.orekit.files.ccsds.ndm.NdmConstituent`<:class:`~org.orekit.files.ccsds.section.Header`,:class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`,:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmData`>> implements :class:`~org.orekit.files.general.EphemerisFile`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`,:class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistory`>
    
        This class gathers the informations present in the Orbit Comprehensive Message (OCM).
    
        Since:
            11.0
    """
    ROOT: typing.ClassVar[str] = ...
    """
    public static final String ROOT
    
        Root element for XML messages.
    
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
    TRAJ_LINE: typing.ClassVar[str] = ...
    """
    public static final String TRAJ_LINE
    
        Trajectory line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    COV_LINE: typing.ClassVar[str] = ...
    """
    public static final String COV_LINE
    
        Covariance line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAN_LINE: typing.ClassVar[str] = ...
    """
    public static final String MAN_LINE
    
        Maneuver line element for XML messages.
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNKNOWN_OBJECT: typing.ClassVar[str] = ...
    """
    public static final String UNKNOWN_OBJECT
    
        Default name for unknown object.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, header: org.orekit.files.ccsds.section.Header, list: java.util.List[org.orekit.files.ccsds.section.Segment['OcmMetadata', 'OcmData']], iERSConventions: org.orekit.utils.IERSConventions, dataContext: org.orekit.data.DataContext, double: float): ...
    def getData(self) -> 'OcmData':
        """
            Get the data from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`.
        
            Returns:
                data from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`
        
        
        """
        ...
    def getMetadata(self) -> 'OcmMetadata':
        """
            Get the metadata from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`.
        
            Returns:
                metadata from the single :meth:`~org.orekit.files.ccsds.ndm.NdmConstituent.getSegments`
        
        
        """
        ...
    def getSatellites(self) -> java.util.Map[str, 'OcmSatelliteEphemeris']: ...

class OcmData(org.orekit.files.ccsds.section.Data):
    """
    public class OcmData extends Object implements :class:`~org.orekit.files.ccsds.section.Data`
    
        Data container for Orbit Comprehensive Messages.
    
        Since:
            11.0
    """
    def __init__(self, list: java.util.List['TrajectoryStateHistory'], physicalProperties: 'PhysicalProperties', list2: java.util.List[CovarianceHistory], list3: java.util.List[ManeuverHistory], perturbations: 'Perturbations', orbitDetermination: 'OrbitDetermination', userDefined: org.orekit.files.ccsds.ndm.odm.UserDefined): ...
    def getCovarianceBlocks(self) -> java.util.List[CovarianceHistory]: ...
    def getManeuverBlocks(self) -> java.util.List[ManeuverHistory]: ...
    def getOTrajectoryBlocks(self) -> java.util.List['TrajectoryStateHistory']: ...
    def getOrbitDeterminationBlock(self) -> 'OrbitDetermination':
        """
            Get orbit determination logical block.
        
            Returns:
                orbit determination logical block (may be null)
        
        
        """
        ...
    def getPerturbationsBlock(self) -> 'Perturbations':
        """
            Get perturbations logical block.
        
            Returns:
                perturbations logical block (may be null)
        
        
        """
        ...
    def getPhysicBlock(self) -> 'PhysicalProperties':
        """
            Get physical properties logical block.
        
            Returns:
                physical properties logical block (may be null)
        
        
        """
        ...
    def getUserDefinedBlock(self) -> org.orekit.files.ccsds.ndm.odm.UserDefined:
        """
            Get user defined parameters logical block.
        
            Returns:
                user defined parameters logical block (may be null)
        
        
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

class OcmDataSubStructureKey(java.lang.Enum['OcmDataSubStructureKey']):
    """
    public enum OcmDataSubStructureKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmDataSubStructureKey`>
    
        Keywords for OCM data sub-structure.
    
        Since:
            11.0
    """
    TRAJ: typing.ClassVar['OcmDataSubStructureKey'] = ...
    traj: typing.ClassVar['OcmDataSubStructureKey'] = ...
    PHYS: typing.ClassVar['OcmDataSubStructureKey'] = ...
    phys: typing.ClassVar['OcmDataSubStructureKey'] = ...
    COV: typing.ClassVar['OcmDataSubStructureKey'] = ...
    covar: typing.ClassVar['OcmDataSubStructureKey'] = ...
    MAN: typing.ClassVar['OcmDataSubStructureKey'] = ...
    man: typing.ClassVar['OcmDataSubStructureKey'] = ...
    PERT: typing.ClassVar['OcmDataSubStructureKey'] = ...
    pert: typing.ClassVar['OcmDataSubStructureKey'] = ...
    OD: typing.ClassVar['OcmDataSubStructureKey'] = ...
    od: typing.ClassVar['OcmDataSubStructureKey'] = ...
    USER: typing.ClassVar['OcmDataSubStructureKey'] = ...
    userDef: typing.ClassVar['OcmDataSubStructureKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, ocmParser: 'OcmParser') -> bool:
        """
            Process one token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                parser (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmParser`): OCM file parser
        
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
    def valueOf(string: str) -> 'OcmDataSubStructureKey':
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
    def values() -> typing.List['OcmDataSubStructureKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OcmDataSubStructureKey c : OcmDataSubStructureKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OcmMetadata(org.orekit.files.ccsds.ndm.odm.OdmMetadata):
    """
    public class OcmMetadata extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmMetadata`
    
        Meta-data for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`.
    
        Since:
            11.0
    """
    def getAdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Attitude Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Attitude Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getAlternateNames(self) -> java.util.List[str]:
        """
            Get the alternate names for this space object.
        
            Returns:
                alternate names
        
        
        """
        ...
    def getCatalogName(self) -> str:
        """
            Get the specification of satellite catalog source.
        
            Returns:
                specification of satellite catalog source
        
        
        """
        ...
    def getCdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Conjunction Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Conjunction Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getCelestialSource(self) -> str:
        """
            Get the source and version of celestial body (e.g. Sun/Earth/Planetary).
        
            Returns:
                source and version of celestial body (e.g. Sun/Earth/Planetary)
        
        
        """
        ...
    def getClassification(self) -> str:
        """
            Get the message classification.
        
            Returns:
                message classification.
        
        
        """
        ...
    def getConstellation(self) -> str:
        """
            Get the name of the constellation this space object belongs to.
        
            Returns:
                name of the constellation this space object belongs to
        
        
        """
        ...
    def getCountry(self) -> str:
        """
            Get the name of the country where the space object owner is based.
        
            Returns:
                name of the country where the space object owner is based
        
        
        """
        ...
    def getEopSource(self) -> str:
        """
            Get the source and version of Earth Orientation Parameters.
        
            Returns:
                source and version of Earth Orientation Parameters
        
        
        """
        ...
    def getEpochT0(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the epoch to which *all* relative times are referenced in data blocks.
        
            Returns:
                epoch to which *all* relative times are referenced in data blocks
        
        
        """
        ...
    def getInternationalDesignator(self) -> str:
        """
            Get the international designator for the object.
        
            Returns:
                international designator for the object
        
        
        """
        ...
    def getInterpMethodEOP(self) -> str:
        """
            Get the interpolation method for Earth Orientation Parameters.
        
            Returns:
                interpolation method for Earth Orientation Parameters
        
        
        """
        ...
    def getNextMessageEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the creation date of next message from a given originator.
        
            Returns:
                creation date of next message from a given originator
        
        
        """
        ...
    def getNextMessageID(self) -> str:
        """
            Get the unique ID identifying next message from a given originator.
        
            Returns:
                unique ID identifying next message from a given originator
        
        
        """
        ...
    def getObjectDesignator(self) -> str:
        """
            Get the unique satellite identification designator for the object.
        
            Returns:
                unique satellite identification designator for the object.
        
        
        """
        ...
    def getObjectType(self) -> ObjectType:
        """
            Get the type of object.
        
            Returns:
                type of object
        
        
        """
        ...
    def getOcmDataElements(self) -> java.util.List[str]:
        """
            Get the list of elements of information data blocks included in this message.
        
            Returns:
                list of elements of information data blocks included in this message
        
        
        """
        ...
    def getOperator(self) -> str:
        """
            Get the operator of the space object.
        
            Returns:
                operator of the space object
        
        
        """
        ...
    def getOpsStatus(self) -> 'OpsStatus':
        """
            Get the operational status.
        
            Returns:
                operational status
        
        
        """
        ...
    def getOrbitCategory(self) -> 'OrbitCategory':
        """
            Get the orbit category.
        
            Returns:
                orbit category
        
        
        """
        ...
    def getOriginatorAddress(self) -> str:
        """
            Get the address of Programmatic Point Of Contact at originator.
        
            Returns:
                address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOriginatorPOC(self) -> str:
        """
            Get the programmatic Point Of Contact at originator.
        
            Returns:
                programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOriginatorPhone(self) -> str:
        """
            Get the phone number of Programmatic Point Of Contact at originator.
        
            Returns:
                phone number of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOriginatorPosition(self) -> str:
        """
            Get the position of Programmatic Point Of Contact at originator.
        
            Returns:
                position of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def getOwner(self) -> str:
        """
            Get the owner of the space object.
        
            Returns:
                owner of the space object
        
        
        """
        ...
    def getPreviousMessageEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the creation date of previous message from a given originator.
        
            Returns:
                creation date of previous message from a given originator
        
        
        """
        ...
    def getPreviousMessageID(self) -> str:
        """
            Get the unique ID identifying previous message from a given originator.
        
            Returns:
                unique ID identifying previous message from a given originator
        
        
        """
        ...
    def getPrmMessageLink(self) -> str:
        """
            Get the Unique identifier of Pointing Request Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Pointing Request Message linked to this Orbit Data Message
        
        
        """
        ...
    def getRdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Reentry Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Reentry Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getSclkOffsetAtEpoch(self) -> float:
        """
            Get the spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Returns:
                spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def getSclkSecPerSISec(self) -> float:
        """
            Get the number of spacecraft clock seconds occurring during one SI second.
        
            Returns:
                number of spacecraft clock seconds occurring during one SI second
        
        
        """
        ...
    def getStartTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the time of the earliest data contained in the OCM.
        
            Returns:
                time of the earliest data contained in the OCM
        
        
        """
        ...
    def getStopTime(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the time of the latest data contained in the OCM.
        
            Returns:
                time of the latest data contained in the OCM
        
        
        """
        ...
    def getTaimutcT0(self) -> float:
        """
            Get the difference (TAI Ã¢â‚¬â€œ UTC) in seconds at epoch
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Returns:
                difference (TAI â€“ UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def getTdmMessageLink(self) -> str:
        """
            Get the Unique identifier of Tracking Data Message linked to this Orbit Data Message.
        
            Returns:
                Unique identifier of Tracking Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def getTechAddress(self) -> str:
        """
            Get the address of Technical Point Of Contact at originator.
        
            Returns:
                address of Technical Point Of Contact at originator
        
        
        """
        ...
    def getTechOrg(self) -> str:
        """
            Get the creating agency or operator.
        
            Returns:
                creating agency or operator
        
        
        """
        ...
    def getTechPOC(self) -> str:
        """
            Get the Technical Point Of Contact at originator.
        
            Returns:
                Technical Point Of Contact at originator
        
        
        """
        ...
    def getTechPhone(self) -> str:
        """
            Get the phone number of Technical Point Of Contact at originator.
        
            Returns:
                phone number of Technical Point Of Contact at originator
        
        
        """
        ...
    def getTechPosition(self) -> str:
        """
            Get the position of Technical Point Of Contact at originator.
        
            Returns:
                position of Technical Point Of Contact at originator
        
        
        """
        ...
    def getTimeSpan(self) -> float:
        """
            Get the span of time in seconds that the OCM covers.
        
            Returns:
                span of time in seconds that the OCM covers
        
        
        """
        ...
    def getUt1mutcT0(self) -> float:
        """
            Get the difference (UT1 Ã¢â‚¬â€œ UTC) in seconds at epoch
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Returns:
                difference (UT1 â€“ UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def setAdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Attitude Data Message linked to this Orbit Data Message.
        
            Parameters:
                admMessageLink (String): Unique identifier of Attitude Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setAlternateNames(self, list: java.util.List[str]) -> None:
        """
            Set the alternate names for this space object.
        
            Parameters:
                alternateNames (List<String> alternateNames): alternate names
        
        
        """
        ...
    def setCatalogName(self, string: str) -> None:
        """
            Set the specification of satellite catalog source.
        
            Parameters:
                catalogName (String): specification of satellite catalog source
        
        
        """
        ...
    def setCdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Conjunction Data Message linked to this Orbit Data Message.
        
            Parameters:
                cdmMessageLink (String): Unique identifier of Conjunction Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setCelestialSource(self, string: str) -> None:
        """
            Set the source and version of celestial body (e.g. Sun/Earth/Planetary).
        
            Parameters:
                celestialSource (String): source and version of celestial body (e.g. Sun/Earth/Planetary)
        
        
        """
        ...
    def setClassification(self, string: str) -> None:
        """
            Set the message classification.
        
            Parameters:
                classification (String): message classification
        
        
        """
        ...
    def setConstellation(self, string: str) -> None:
        """
            Set the name of the constellation this space object belongs to.
        
            Parameters:
                constellation (String): name of the constellation this space object belongs to
        
        
        """
        ...
    def setCountry(self, string: str) -> None:
        """
            Set the name of the country where the space object owner is based.
        
            Parameters:
                country (String): name of the country where the space object owner is based
        
        
        """
        ...
    def setEopSource(self, string: str) -> None:
        """
            Set the source and version of Earth Orientation Parameters.
        
            Parameters:
                eopSource (String): source and version of Earth Orientation Parameters
        
        
        """
        ...
    def setEpochT0(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the epoch to which *all* relative times are referenced in data blocks.
        
            Parameters:
                epochT0 (:class:`~org.orekit.time.AbsoluteDate`): epoch to which *all* relative times are referenced in data blocks
        
        
        """
        ...
    def setInternationalDesignator(self, string: str) -> None:
        """
            Set the international designator for the object.
        
            Parameters:
                internationalDesignator (String): international designator for the object
        
        
        """
        ...
    def setInterpMethodEOP(self, string: str) -> None:
        """
            Set the interpolation method for Earth Orientation Parameters.
        
            Parameters:
                interpMethodEOP (String): interpolation method for Earth Orientation Parameters
        
        
        """
        ...
    def setNextMessageEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the creation date of next message from a given originator.
        
            Parameters:
                nextMessageEpoch (:class:`~org.orekit.time.AbsoluteDate`): creation date of next message from a given originator
        
        
        """
        ...
    def setNextMessageID(self, string: str) -> None:
        """
            Set the unique ID identifying next message from a given originator.
        
            Parameters:
                nextMessageID (String): unique ID identifying next message from a given originator
        
        
        """
        ...
    def setObjectDesignator(self, string: str) -> None:
        """
            Set the unique satellite identification designator for the object.
        
            Parameters:
                objectDesignator (String): unique satellite identification designator for the object
        
        
        """
        ...
    def setObjectType(self, objectType: ObjectType) -> None:
        """
            Set the type of object.
        
            Parameters:
                objectType (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ObjectType`): type of object
        
        
        """
        ...
    def setOcmDataElements(self, list: java.util.List[str]) -> None:
        """
            Set the list of elements of information data blocks included in this message.
        
            Parameters:
                ocmDataElements (List<String> ocmDataElements): list of elements of information data blocks included in this message
        
        
        """
        ...
    def setOperator(self, string: str) -> None:
        """
            Set the operator of the space object.
        
            Parameters:
                operator (String): operator of the space object
        
        
        """
        ...
    def setOpsStatus(self, opsStatus: 'OpsStatus') -> None:
        """
            Set the operational status.
        
            Parameters:
                opsStatus (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OpsStatus`): operational status
        
        
        """
        ...
    def setOrbitCategory(self, orbitCategory: 'OrbitCategory') -> None:
        """
            Set the orbit category.
        
            Parameters:
                orbitCategory (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCategory`): orbit category
        
        
        """
        ...
    def setOriginatorAddress(self, string: str) -> None:
        """
            Set the address of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorAddress (String): address of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPOC(self, string: str) -> None:
        """
            Set the programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPOC (String): programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPhone(self, string: str) -> None:
        """
            GSet the phone number of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPhone (String): phone number of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOriginatorPosition(self, string: str) -> None:
        """
            Set the position of Programmatic Point Of Contact at originator.
        
            Parameters:
                originatorPosition (String): position of Programmatic Point Of Contact at originator
        
        
        """
        ...
    def setOwner(self, string: str) -> None:
        """
            Set the owner of the space object.
        
            Parameters:
                owner (String): owner of the space object
        
        
        """
        ...
    def setPreviousMessageEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the creation date of previous message from a given originator.
        
            Parameters:
                previousMessageEpoch (:class:`~org.orekit.time.AbsoluteDate`): creation date of previous message from a given originator
        
        
        """
        ...
    def setPreviousMessageID(self, string: str) -> None:
        """
            Set the unique ID identifying previous message from a given originator.
        
            Parameters:
                previousMessageID (String): unique ID identifying previous message from a given originator
        
        
        """
        ...
    def setPrmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Pointing Request Message linked to this Orbit Data Message.
        
            Parameters:
                prmMessageLink (String): Unique identifier of Pointing Request Message linked to this Orbit Data Message
        
        
        """
        ...
    def setRdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Reentry Data Message linked to this Orbit Data Message.
        
            Parameters:
                rdmMessageLink (String): Unique identifier of Reentry Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setSclkOffsetAtEpoch(self, double: float) -> None:
        """
            Set the spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Parameters:
                sclkOffsetAtEpoch (double): spacecraft clock count at :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def setSclkSecPerSISec(self, double: float) -> None:
        """
            Set the number of spacecraft clock seconds occurring during one SI second.
        
            Parameters:
                secClockPerSISec (double): number of spacecraft clock seconds occurring during one SI second
        
        
        """
        ...
    def setStartTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time of the earliest data contained in the OCM.
        
            Parameters:
                startTime (:class:`~org.orekit.time.AbsoluteDate`): time of the earliest data contained in the OCM
        
        
        """
        ...
    def setStopTime(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the time of the latest data contained in the OCM.
        
            Parameters:
                stopTime (:class:`~org.orekit.time.AbsoluteDate`): time of the latest data contained in the OCM
        
        
        """
        ...
    def setTaimutcT0(self, double: float) -> None:
        """
            Set the difference (TAI Ã¢â‚¬â€œ UTC) in seconds at epoch
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Parameters:
                taimutcT0 (double): difference (TAI â€“ UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
        """
        ...
    def setTdmMessageLink(self, string: str) -> None:
        """
            Set the Unique identifier of Tracking Data Message linked to this Orbit Data Message.
        
            Parameters:
                tdmMessageLink (String): Unique identifier of Tracking Data Message linked to this Orbit Data Message
        
        
        """
        ...
    def setTechAddress(self, string: str) -> None:
        """
            Set the address of Technical Point Of Contact at originator.
        
            Parameters:
                techAddress (String): address of Technical Point Of Contact at originator
        
        
        """
        ...
    def setTechOrg(self, string: str) -> None:
        """
            Set the creating agency or operator.
        
            Parameters:
                techOrg (String): creating agency or operator
        
        
        """
        ...
    def setTechPOC(self, string: str) -> None:
        """
            Set the Technical Point Of Contact at originator.
        
            Parameters:
                techPOC (String): Technical Point Of Contact at originator
        
        
        """
        ...
    def setTechPhone(self, string: str) -> None:
        """
            Set the phone number of Technical Point Of Contact at originator.
        
            Parameters:
                techPhone (String): phone number of Technical Point Of Contact at originator
        
        
        """
        ...
    def setTechPosition(self, string: str) -> None:
        """
            Set the position of Technical Point Of Contact at originator.
        
            Parameters:
                techPosition (String): position of Technical Point Of Contact at originator
        
        
        """
        ...
    def setTimeSpan(self, double: float) -> None:
        """
            Set the span of time in seconds that the OCM covers.
        
            Parameters:
                timeSpan (double): span of time in seconds that the OCM covers
        
        
        """
        ...
    def setUt1mutcT0(self, double: float) -> None:
        """
            Set the difference (UT1 Ã¢â‚¬â€œ UTC) in seconds at epoch
            :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`.
        
            Parameters:
                ut1mutcT0 (double): difference (UT1 â€“ UTC) in seconds at epoch :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata.getEpochT0`
        
        
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

class OcmMetadataKey(java.lang.Enum['OcmMetadataKey']):
    """
    public enum OcmMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata` entries.
    
        Since:
            11.0
    """
    CLASSIFICATION: typing.ClassVar['OcmMetadataKey'] = ...
    INTERNATIONAL_DESIGNATOR: typing.ClassVar['OcmMetadataKey'] = ...
    CATALOG_NAME: typing.ClassVar['OcmMetadataKey'] = ...
    OBJECT_DESIGNATOR: typing.ClassVar['OcmMetadataKey'] = ...
    ALTERNATE_NAMES: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_POC: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_POSITION: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_PHONE: typing.ClassVar['OcmMetadataKey'] = ...
    ORIGINATOR_ADDRESS: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_ORG: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_POC: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_POSITION: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_PHONE: typing.ClassVar['OcmMetadataKey'] = ...
    TECH_ADDRESS: typing.ClassVar['OcmMetadataKey'] = ...
    PREVIOUS_MESSAGE_ID: typing.ClassVar['OcmMetadataKey'] = ...
    NEXT_MESSAGE_ID: typing.ClassVar['OcmMetadataKey'] = ...
    ADM_MESSAGE_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    CDM_MESSAGE_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    PRM_MESSAGE_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    RDM_MESSAGE_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    TDM_MESSAGE_LINK: typing.ClassVar['OcmMetadataKey'] = ...
    OPERATOR: typing.ClassVar['OcmMetadataKey'] = ...
    OWNER: typing.ClassVar['OcmMetadataKey'] = ...
    COUNTRY: typing.ClassVar['OcmMetadataKey'] = ...
    CONSTELLATION: typing.ClassVar['OcmMetadataKey'] = ...
    OBJECT_TYPE: typing.ClassVar['OcmMetadataKey'] = ...
    EPOCH_TZERO: typing.ClassVar['OcmMetadataKey'] = ...
    OPS_STATUS: typing.ClassVar['OcmMetadataKey'] = ...
    ORBIT_CATEGORY: typing.ClassVar['OcmMetadataKey'] = ...
    OCM_DATA_ELEMENTS: typing.ClassVar['OcmMetadataKey'] = ...
    SCLK_OFFSET_AT_EPOCH: typing.ClassVar['OcmMetadataKey'] = ...
    SCLK_SEC_PER_SI_SEC: typing.ClassVar['OcmMetadataKey'] = ...
    PREVIOUS_MESSAGE_EPOCH: typing.ClassVar['OcmMetadataKey'] = ...
    NEXT_MESSAGE_EPOCH: typing.ClassVar['OcmMetadataKey'] = ...
    START_TIME: typing.ClassVar['OcmMetadataKey'] = ...
    STOP_TIME: typing.ClassVar['OcmMetadataKey'] = ...
    TIME_SPAN: typing.ClassVar['OcmMetadataKey'] = ...
    TAIMUTC_AT_TZERO: typing.ClassVar['OcmMetadataKey'] = ...
    UT1MUTC_AT_TZERO: typing.ClassVar['OcmMetadataKey'] = ...
    EOP_SOURCE: typing.ClassVar['OcmMetadataKey'] = ...
    INTERP_METHOD_EOP: typing.ClassVar['OcmMetadataKey'] = ...
    CELESTIAL_SOURCE: typing.ClassVar['OcmMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, ocmMetadata: OcmMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'OcmMetadataKey':
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
    def values() -> typing.List['OcmMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OcmMetadataKey c : OcmMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OcmParser(org.orekit.files.ccsds.ndm.odm.OdmParser[Ocm, 'OcmParser'], org.orekit.files.general.EphemerisFileParser[Ocm]):
    """
    public class OcmParser extends :class:`~org.orekit.files.ccsds.ndm.odm.OdmParser`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`,:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmParser`> implements :class:`~org.orekit.files.general.EphemerisFileParser`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`>
    
        A parser for the CCSDS OCM (Orbit Comprehensive Message).
    
        Note than starting with Orekit 11.0, CCSDS message parsers are mutable objects that gather the data being parsed, until
        the message is complete and the :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractMessageParser.parseMessage` method
        has returned. This implies that parsers should *not* be used in a multi-thread context. The recommended way to use
        parsers is to either dedicate one parser for each message and drop it afterwards, or to use a single-thread loop.
    
        Since:
            11.0
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, dataContext: org.orekit.data.DataContext, double: float, parsedUnitsBehavior: org.orekit.files.ccsds.ndm.ParsedUnitsBehavior): ...
    def build(self) -> Ocm:
        """
            Build the file from parsed entries.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.build`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
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
    def getHeader(self) -> org.orekit.files.ccsds.section.Header:
        """
            Get file header to fill.
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser.getHeader`Â in
                classÂ :class:`~org.orekit.files.ccsds.utils.parsing.AbstractConstituentParser`
        
            Returns:
                file header to fill
        
        
        """
        ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]: ...
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
    def parse(self, dataSource: org.orekit.data.DataSource) -> Ocm:
        """
            Parse an ephemeris file from a data source.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFileParser.parse`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFileParser`
        
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
        
            Specified by:
                :meth:`~org.orekit.files.ccsds.utils.lexical.MessageParser.reset`Â in
                interfaceÂ :class:`~org.orekit.files.ccsds.utils.lexical.MessageParser`
        
            Parameters:
                fileFormat (:class:`~org.orekit.files.ccsds.utils.FileFormat`): format of the file ready to be parsed
        
        
        """
        ...

class OcmSatelliteEphemeris(org.orekit.files.general.EphemerisFile.SatelliteEphemeris[org.orekit.utils.TimeStampedPVCoordinates, 'TrajectoryStateHistory']):
    """
    public class OcmSatelliteEphemeris extends Object implements :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`,:class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistory`>
    
        OCM ephemeris blocks for a single satellite.
    
        Since:
            11.0
    """
    def __init__(self, string: str, double: float, list: java.util.List['TrajectoryStateHistory']): ...
    def getId(self) -> str:
        """
            Get the satellite ID. The satellite ID is unique only within the same ephemeris file.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getId`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the satellite's ID, never :code:`null`.
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getMu`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getPropagator`, in
                mÃ‚Â³/sÃ‚Â².
        
        
        """
        ...
    def getSegments(self) -> java.util.List['TrajectoryStateHistory']: ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStart`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of the ephemeris.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris.getStop`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.SatelliteEphemeris`
        
            Returns:
                ephemeris end date.
        
        
        """
        ...

class OcmWriter(org.orekit.files.ccsds.utils.generation.AbstractMessageWriter[org.orekit.files.ccsds.section.Header, org.orekit.files.ccsds.section.Segment[OcmMetadata, OcmData], Ocm]):
    """
    public class OcmWriter extends :class:`~org.orekit.files.ccsds.utils.generation.AbstractMessageWriter`<:class:`~org.orekit.files.ccsds.section.Header`,:class:`~org.orekit.files.ccsds.section.Segment`<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmMetadata`,:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OcmData`>,:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`>
    
        Writer for CCSDS Orbit Comprehensive Message.
    
        Since:
            11.0
    """
    CCSDS_OCM_VERS: typing.ClassVar[float] = ...
    """
    public static final double CCSDS_OCM_VERS
    
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
    def writeSegmentContent(self, generator: org.orekit.files.ccsds.utils.generation.Generator, double: float, segment: org.orekit.files.ccsds.section.Segment[OcmMetadata, OcmData]) -> None: ...

class OpsStatus(java.lang.Enum['OpsStatus']):
    """
    public enum OpsStatus extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OpsStatus`>
    
        Operational status used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    OPERATIONAL: typing.ClassVar['OpsStatus'] = ...
    NONOPERATIONAL: typing.ClassVar['OpsStatus'] = ...
    PARTIALLY_OPERATIONAL: typing.ClassVar['OpsStatus'] = ...
    BACKUP: typing.ClassVar['OpsStatus'] = ...
    STANBY: typing.ClassVar['OpsStatus'] = ...
    EXTENDED_MISSION: typing.ClassVar['OpsStatus'] = ...
    REENTRY_MODE: typing.ClassVar['OpsStatus'] = ...
    DECAYED: typing.ClassVar['OpsStatus'] = ...
    UNKNOWN: typing.ClassVar['OpsStatus'] = ...
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
    def valueOf(string: str) -> 'OpsStatus':
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
    def values() -> typing.List['OpsStatus']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OpsStatus c : OpsStatus.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitCategory(java.lang.Enum['OrbitCategory']):
    """
    public enum OrbitCategory extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitCategory`>
    
        Orbit category used in CCSDS :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ocm`.
    
        Since:
            11.0
    """
    EGO: typing.ClassVar['OrbitCategory'] = ...
    ESO: typing.ClassVar['OrbitCategory'] = ...
    GHO: typing.ClassVar['OrbitCategory'] = ...
    GEO: typing.ClassVar['OrbitCategory'] = ...
    GSO: typing.ClassVar['OrbitCategory'] = ...
    GTO: typing.ClassVar['OrbitCategory'] = ...
    HAO: typing.ClassVar['OrbitCategory'] = ...
    HEO: typing.ClassVar['OrbitCategory'] = ...
    IGO: typing.ClassVar['OrbitCategory'] = ...
    LEO: typing.ClassVar['OrbitCategory'] = ...
    LMO: typing.ClassVar['OrbitCategory'] = ...
    MEO: typing.ClassVar['OrbitCategory'] = ...
    MGO: typing.ClassVar['OrbitCategory'] = ...
    NSO: typing.ClassVar['OrbitCategory'] = ...
    UFO: typing.ClassVar['OrbitCategory'] = ...
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
    def valueOf(string: str) -> 'OrbitCategory':
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
    def values() -> typing.List['OrbitCategory']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OrbitCategory c : OrbitCategory.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OrbitDetermination(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class OrbitDetermination extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Orbit determination data.
    
        Since:
            11.0
    """
    def getActualOdSpan(self) -> float:
        """
            Get actual time span used for the OD of the object.
        
            Returns:
                actual time span used for the OD of the object
        
        
        """
        ...
    def getConfidence(self) -> float:
        """
            Get confidence metric.
        
            Returns:
                confidence metric
        
        
        """
        ...
    def getConsiderN(self) -> int:
        """
            Get number of consider parameters.
        
            Returns:
                number of consider parameters
        
        
        """
        ...
    def getConsiderParameters(self) -> java.util.List[str]:
        """
            Get description of consider parameters.
        
            Returns:
                description of consider parameters
        
        
        """
        ...
    def getDataTypes(self) -> java.util.List[str]:
        """
            Get observation data types used.
        
            Returns:
                observation data types used
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get time tag for orbit determination solved-for state.
        
            Returns:
                time tag for orbit determination solved-for state
        
        
        """
        ...
    def getEpochEigenMaj(self) -> float:
        """
            Get positional error ellipsoid 1Ïƒ major eigenvalue at the epoch of OD.
        
            Returns:
                positional error ellipsoid 1Ïƒ major eigenvalue at the epoch of OD
        
        
        """
        ...
    def getEpochEigenMed(self) -> float:
        """
            Get positional error ellipsoid 1Ïƒ intermediate eigenvalue at the epoch of OD.
        
            Returns:
                positional error ellipsoid 1Ïƒ intermediate eigenvalue at the epoch of OD
        
        
        """
        ...
    def getEpochEigenMin(self) -> float:
        """
            Get positional error ellipsoid 1Ïƒ minor eigenvalue at the epoch of OD.
        
            Returns:
                positional error ellipsoid 1Ïƒ minor eigenvalue at the epoch of OD
        
        
        """
        ...
    def getGdop(self) -> float:
        """
            Get generalize Dilution Of Precision.
        
            Returns:
                generalize Dilution Of Precision
        
        
        """
        ...
    def getId(self) -> str:
        """
            Get identification number.
        
            Returns:
                identification number
        
        
        """
        ...
    def getMaxPredictedEigenMaj(self) -> float:
        """
            Get maximum predicted major eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM.
        
            Returns:
                maximum predicted major eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def getMaximumObsGap(self) -> float:
        """
            Get maximum time between observations in the OD of the object.
        
            Returns:
                maximum time between observations in the OD of the object
        
        
        """
        ...
    def getMethod(self) -> org.orekit.files.ccsds.definitions.OdMethodFacade:
        """
            Get orbit determination method.
        
            Returns:
                orbit determination method
        
        
        """
        ...
    def getMinPredictedEigenMin(self) -> float:
        """
            Get minimum predicted minor eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM.
        
            Returns:
                minimum predicted v eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def getObsAvailable(self) -> int:
        """
            Get number of observations available within the actual OD span.
        
            Returns:
                number of observations available within the actual OD span
        
        
        """
        ...
    def getObsUsed(self) -> int:
        """
            Get number of observations accepted within the actual OD span.
        
            Returns:
                number of observations accepted within the actual OD span
        
        
        """
        ...
    def getPrevId(self) -> str:
        """
            Get identification of previous orbit determination.
        
            Returns:
                identification of previous orbit determination
        
        
        """
        ...
    def getRecommendedOdSpan(self) -> float:
        """
            Get sime span of observation recommended for the OD of the object.
        
            Returns:
                sime span of observation recommended for the OD of the object
        
        
        """
        ...
    def getSensors(self) -> java.util.List[str]:
        """
            Get description of sensors used.
        
            Returns:
                description of sensors used
        
        
        """
        ...
    def getSensorsN(self) -> int:
        """
            Get number of sensors used.
        
            Returns:
                number of sensors used
        
        
        """
        ...
    def getSolveN(self) -> int:
        """
            Get number of solved-for states.
        
            Returns:
                number of solved-for states
        
        
        """
        ...
    def getSolveStates(self) -> java.util.List[str]:
        """
            Get description of state elements solved-for.
        
            Returns:
                description of state elements solved-for
        
        
        """
        ...
    def getTimeSinceFirstObservation(self) -> float:
        """
            Get time elapsed between first accepted observation on epoch.
        
            Returns:
                time elapsed between first accepted observation on epoch
        
        
        """
        ...
    def getTimeSinceLastObservation(self) -> float:
        """
            Get time elapsed between last accepted observation on epoch.
        
            Returns:
                time elapsed between last accepted observation on epoch
        
        
        """
        ...
    def getTracksAvailable(self) -> int:
        """
            Get number of sensors tracks available for the OD within the actual OD span.
        
            Returns:
                number of sensors tracks available for the OD within the actual OD span
        
        
        """
        ...
    def getTracksUsed(self) -> int:
        """
            Get number of sensors tracks accepted for the OD within the actual OD span.
        
            Returns:
                number of sensors tracks accepted for the OD within the actual OD span
        
        
        """
        ...
    def getWeightedRms(self) -> float:
        """
            Get weighted RMS residual ratio.
        
            Returns:
                weighted RMS residual ratio
        
        
        """
        ...
    def setActualOdSpan(self, double: float) -> None:
        """
            Set actual time span used for the OD of the object.
        
            Parameters:
                actualOdSpan (double): actual time span used for the OD of the object
        
        
        """
        ...
    def setConfidence(self, double: float) -> None:
        """
            Set confidence metric.
        
            Parameters:
                confidence (double): confidence metric
        
        
        """
        ...
    def setConsiderN(self, int: int) -> None:
        """
            Set number of consider parameters.
        
            Parameters:
                considerN (int): number of consider parameters
        
        
        """
        ...
    def setConsiderParameters(self, list: java.util.List[str]) -> None:
        """
            Set description of consider parameters.
        
            Parameters:
                considerParameters (List<String> considerParameters): description of consider parameters
        
        
        """
        ...
    def setDataTypes(self, list: java.util.List[str]) -> None:
        """
            Set observation data types used.
        
            Parameters:
                dataTypes (List<String> dataTypes): observation data types used
        
        
        """
        ...
    def setEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set time tag for orbit determination solved-for state.
        
            Parameters:
                epoch (:class:`~org.orekit.time.AbsoluteDate`): time tag for orbit determination solved-for state
        
        
        """
        ...
    def setEpochEigenMaj(self, double: float) -> None:
        """
            Set positional error ellipsoid 1Ïƒ major eigenvalue at the epoch of OD.
        
            Parameters:
                epochEigenMaj (double): positional error ellipsoid 1Ïƒ major eigenvalue at the epoch of OD
        
        
        """
        ...
    def setEpochEigenMed(self, double: float) -> None:
        """
            Set positional error ellipsoid 1Ïƒ intermediate eigenvalue at the epoch of OD.
        
            Parameters:
                epochEigenMed (double): positional error ellipsoid 1Ïƒ intermediate eigenvalue at the epoch of OD
        
        
        """
        ...
    def setEpochEigenMin(self, double: float) -> None:
        """
            Set positional error ellipsoid 1Ïƒ minor eigenvalue at the epoch of OD.
        
            Parameters:
                epochEigenMin (double): positional error ellipsoid 1Ïƒ minor eigenvalue at the epoch of OD
        
        
        """
        ...
    def setGdop(self, double: float) -> None:
        """
            Set generalize Dilution Of Precision.
        
            Parameters:
                gdop (double): generalize Dilution Of Precision
        
        
        """
        ...
    def setId(self, string: str) -> None:
        """
            Set identification number.
        
            Parameters:
                id (String): identification number
        
        
        """
        ...
    def setMaxPredictedEigenMaj(self, double: float) -> None:
        """
            Set maximum predicted major eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM.
        
            Parameters:
                maxPredictedEigenMaj (double): maximum predicted major eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def setMaximumObsGap(self, double: float) -> None:
        """
            Set maximum time between observations in the OD of the object.
        
            Parameters:
                maximumObsGap (double): maximum time between observations in the OD of the object
        
        
        """
        ...
    def setMethod(self, odMethodFacade: org.orekit.files.ccsds.definitions.OdMethodFacade) -> None:
        """
            Set orbit determination method.
        
            Parameters:
                method (:class:`~org.orekit.files.ccsds.definitions.OdMethodFacade`): orbit determination method
        
        
        """
        ...
    def setMinPredictedEigenMin(self, double: float) -> None:
        """
            Set minimum predicted minor eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM.
        
            Parameters:
                minPredictedEigenMin (double): minimum predicted minor eigenvalue of 1Ïƒ positional error ellipsoid over entire time span of the OCM
        
        
        """
        ...
    def setObsAvailable(self, int: int) -> None:
        """
            Set number of observations available within the actual OD span.
        
            Parameters:
                obsAvailable (int): number of observations available within the actual OD span
        
        
        """
        ...
    def setObsUsed(self, int: int) -> None:
        """
            Set number of observations accepted within the actual OD span.
        
            Parameters:
                obsUsed (int): number of observations accepted within the actual OD span
        
        
        """
        ...
    def setPrevId(self, string: str) -> None:
        """
            Set identification of previous orbit determination.
        
            Parameters:
                prevId (String): identification of previous orbit determination
        
        
        """
        ...
    def setRecommendedOdSpan(self, double: float) -> None:
        """
            Set sime span of observation recommended for the OD of the object.
        
            Parameters:
                recommendedOdSpan (double): sime span of observation recommended for the OD of the object
        
        
        """
        ...
    def setSensors(self, list: java.util.List[str]) -> None:
        """
            Set description of sensors used.
        
            Parameters:
                sensors (List<String> sensors): description of sensors used
        
        
        """
        ...
    def setSensorsN(self, int: int) -> None:
        """
            Set number of sensors used.
        
            Parameters:
                sensorsN (int): number of sensors used
        
        
        """
        ...
    def setSolveN(self, int: int) -> None:
        """
            Set number of solved-for states.
        
            Parameters:
                solveN (int): number of solved-for states
        
        
        """
        ...
    def setSolveStates(self, list: java.util.List[str]) -> None:
        """
            Set description of state elements solved-for.
        
            Parameters:
                solveStates (List<String> solveStates): description of state elements solved-for
        
        
        """
        ...
    def setTimeSinceFirstObservation(self, double: float) -> None:
        """
            Set time elapsed between first accepted observation on epoch.
        
            Parameters:
                timeSinceFirstObservation (double): time elapsed between first accepted observation on epoch
        
        
        """
        ...
    def setTimeSinceLastObservation(self, double: float) -> None:
        """
            Set time elapsed between last accepted observation on epoch.
        
            Parameters:
                timeSinceLastObservation (double): time elapsed between last accepted observation on epoch
        
        
        """
        ...
    def setTracksAvailable(self, int: int) -> None:
        """
            Set number of sensors tracks available for the OD within the actual OD span.
        
            Parameters:
                tracksAvailable (int): number of sensors tracks available for the OD within the actual OD span
        
        
        """
        ...
    def setTracksUsed(self, int: int) -> None:
        """
            Set number of sensors tracks accepted for the OD within the actual OD span.
        
            Parameters:
                tracksUsed (int): number of sensors tracks accepted for the OD within the actual OD span
        
        
        """
        ...
    def setWeightedRms(self, double: float) -> None:
        """
            Set weighted RMS residual ratio.
        
            Parameters:
                weightedRms (double): weighted RMS residual ratio
        
        
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

class OrbitDeterminationKey(java.lang.Enum['OrbitDeterminationKey']):
    """
    public enum OrbitDeterminationKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitDeterminationKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitDetermination` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_ID: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_PREV_ID: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_METHOD: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH: typing.ClassVar['OrbitDeterminationKey'] = ...
    DAYS_SINCE_FIRST_OBS: typing.ClassVar['OrbitDeterminationKey'] = ...
    DAYS_SINCE_LAST_OBS: typing.ClassVar['OrbitDeterminationKey'] = ...
    RECOMMENDED_OD_SPAN: typing.ClassVar['OrbitDeterminationKey'] = ...
    ACTUAL_OD_SPAN: typing.ClassVar['OrbitDeterminationKey'] = ...
    OBS_AVAILABLE: typing.ClassVar['OrbitDeterminationKey'] = ...
    OBS_USED: typing.ClassVar['OrbitDeterminationKey'] = ...
    TRACKS_AVAILABLE: typing.ClassVar['OrbitDeterminationKey'] = ...
    TRACKS_USED: typing.ClassVar['OrbitDeterminationKey'] = ...
    MAXIMUM_OBS_GAP: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH_EIGMAJ: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH_EIGMED: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_EPOCH_EIGMIN: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_MAX_PRED_EIGMAJ: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_MIN_PRED_EIGMIN: typing.ClassVar['OrbitDeterminationKey'] = ...
    OD_CONFIDENCE: typing.ClassVar['OrbitDeterminationKey'] = ...
    GDOP: typing.ClassVar['OrbitDeterminationKey'] = ...
    SOLVE_N: typing.ClassVar['OrbitDeterminationKey'] = ...
    SOLVE_STATES: typing.ClassVar['OrbitDeterminationKey'] = ...
    CONSIDER_N: typing.ClassVar['OrbitDeterminationKey'] = ...
    CONSIDER_PARAMS: typing.ClassVar['OrbitDeterminationKey'] = ...
    SENSORS_N: typing.ClassVar['OrbitDeterminationKey'] = ...
    SENSORS: typing.ClassVar['OrbitDeterminationKey'] = ...
    WEIGHTED_RMS: typing.ClassVar['OrbitDeterminationKey'] = ...
    DATA_TYPES: typing.ClassVar['OrbitDeterminationKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, orbitDetermination: OrbitDetermination) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.OrbitDetermination`): container to fill
        
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
    def valueOf(string: str) -> 'OrbitDeterminationKey':
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
    def values() -> typing.List['OrbitDeterminationKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OrbitDeterminationKey c : OrbitDeterminationKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Ordering(java.lang.Enum['Ordering']):
    """
    public enum Ordering extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Ordering`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Covariance` elements ordering.
    
        Since:
            11.0
    """
    LTM: typing.ClassVar['Ordering'] = ...
    UTM: typing.ClassVar['Ordering'] = ...
    FULL: typing.ClassVar['Ordering'] = ...
    LTMWCC: typing.ClassVar['Ordering'] = ...
    UTMWCC: typing.ClassVar['Ordering'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Ordering':
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
    def values() -> typing.List['Ordering']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (Ordering c : Ordering.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Perturbations(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class Perturbations extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Perturbation parameters.
    
        Since:
            11.0
    """
    def __init__(self, celestialBodies: org.orekit.bodies.CelestialBodies): ...
    def getAlbedoGridSize(self) -> int:
        """
            Get albedo grid size.
        
            Returns:
                albedo grid size
        
        
        """
        ...
    def getAlbedoModel(self) -> str:
        """
            Get albedo model.
        
            Returns:
                albedo model
        
        
        """
        ...
    def getAtmosphericModel(self) -> str:
        """
            Get name of atmospheric model.
        
            Returns:
                name of atmospheric model
        
        
        """
        ...
    def getCentralBodyRotation(self) -> float:
        """
            Get central body angular rotation rate.
        
            Returns:
                central body angular rotation rate
        
        
        """
        ...
    def getEquatorialRadius(self) -> float:
        """
            Get oblate spheroid equatorial radius of central body.
        
            Returns:
                oblate spheroid equatorial radius of central body
        
        
        """
        ...
    def getFixedF10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7
        
        
        """
        ...
    def getFixedF10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7
        
        
        """
        ...
    def getFixedGeomagneticAp(self) -> float:
        """
            Get fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aâ‚š.
        
            Returns:
                fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aâ‚š
        
        
        """
        ...
    def getFixedGeomagneticDst(self) -> float:
        """
            Get fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst.
        
            Returns:
                fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst
        
        
        """
        ...
    def getFixedGeomagneticKp(self) -> float:
        """
            Get fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kâ‚š.
        
            Returns:
                fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kâ‚š
        
        
        """
        ...
    def getFixedM10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux daily proxy M10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux daily proxy M10.7
        
        
        """
        ...
    def getFixedM10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7
        
        
        """
        ...
    def getFixedS10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux daily proxy S10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux daily proxy S10.7
        
        
        """
        ...
    def getFixedS10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7
        
        
        """
        ...
    def getFixedY10P7(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux daily proxy Y10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux daily proxy Y10.7
        
        
        """
        ...
    def getFixedY10P7Mean(self) -> float:
        """
            Get fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7.
        
            Returns:
                fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7
        
        
        """
        ...
    def getGm(self) -> float:
        """
            Get gravitational coefficient of attracting body.
        
            Returns:
                gravitational coefficient of attracting body
        
        
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
    def getInterpMethodSW(self) -> str:
        """
            Get the interpolation method for Space Weather data.
        
            Returns:
                interpolation method for Space Weather data
        
        
        """
        ...
    def getNBodyPerturbations(self) -> java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]: ...
    def getOblateFlattening(self) -> float:
        """
            Get central body oblate spheroid oblateness.
        
            Returns:
                central body oblate spheroid oblateness
        
        
        """
        ...
    def getOceanTidesModel(self) -> str:
        """
            Get ocean tides model.
        
            Returns:
                ocean tides model
        
        
        """
        ...
    def getReductionTheory(self) -> str:
        """
            Get reduction theory used for precession and nutation modeling.
        
            Returns:
                reduction theory used for precession and nutation modeling
        
        
        """
        ...
    def getShadowBodies(self) -> java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]: ...
    def getShadowModel(self) -> 'ShadowModel':
        """
            Get shadow model used for solar radiation pressure.
        
            Returns:
                shadow model used for solar radiation pressure
        
        
        """
        ...
    def getSolidTidesModel(self) -> str:
        """
            Get solid tides model.
        
            Returns:
                solid tides model
        
        
        """
        ...
    def getSpaceWeatherEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the Space Weather data.
        
            Returns:
                epoch of the Space Weather data
        
        
        """
        ...
    def getSpaceWeatherSource(self) -> str:
        """
            Get Space Weather data source.
        
            Returns:
                Space Weather data source
        
        
        """
        ...
    def getSrpModel(self) -> str:
        """
            Get Solar Radiation Pressure model.
        
            Returns:
                Solar Radiation Pressure model
        
        
        """
        ...
    def setAlbedoGridSize(self, int: int) -> None:
        """
            Set albedo grid size.
        
            Parameters:
                albedoGridSize (int): albedo grid size
        
        
        """
        ...
    def setAlbedoModel(self, string: str) -> None:
        """
            Set albedo model.
        
            Parameters:
                albedoModel (String): albedo model
        
        
        """
        ...
    def setAtmosphericModel(self, string: str) -> None:
        """
            Set name of atmospheric model.
        
            Parameters:
                atmosphericModel (String): name of atmospheric model
        
        
        """
        ...
    def setCentralBodyRotation(self, double: float) -> None:
        """
            Set central body angular rotation rate.
        
            Parameters:
                centralBodyRotation (double): central body angular rotation rate
        
        
        """
        ...
    def setEquatorialRadius(self, double: float) -> None:
        """
            Set oblate spheroid equatorial radius of central body.
        
            Parameters:
                equatorialRadius (double): oblate spheroid equatorial radius of central body
        
        
        """
        ...
    def setFixedF10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7.
        
            Parameters:
                fixedF10P7 (double): fixed (time invariant) value of the Solar Flux Unit daily proxy F10.7
        
        
        """
        ...
    def setFixedF10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7.
        
            Parameters:
                fixedF10P7Mean (double): fixed (time invariant) value of the Solar Flux Unit 81-day running center-average proxy F10.7
        
        
        """
        ...
    def setFixedGeomagneticAp(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aâ‚š.
        
            Parameters:
                fixedGeomagneticAp (double): fixed (time invariant) value of the planetary 3-hour-range geomagnetic index aâ‚š
        
        
        """
        ...
    def setFixedGeomagneticDst(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst.
        
            Parameters:
                fixedGeomagneticDst (double): fixed (time invariant) value of the planetary 1-hour-range geomagnetic index Dst
        
        
        """
        ...
    def setFixedGeomagneticKp(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kâ‚š.
        
            Parameters:
                fixedGeomagneticKp (double): fixed (time invariant) value of the planetary 3-hour-range geomagnetic index Kâ‚š
        
        
        """
        ...
    def setFixedM10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux daily proxy M10.7.
        
            Parameters:
                fixedM10P7 (double): fixed (time invariant) value of the Solar Flux daily proxy M10.7
        
        
        """
        ...
    def setFixedM10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7.
        
            Parameters:
                fixedM10P7Mean (double): fixed (time invariant) value of the Solar Flux 81-day running center-average proxy M10.7
        
        
        """
        ...
    def setFixedS10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux daily proxy S10.7.
        
            Parameters:
                fixedS10P7 (double): fixed (time invariant) value of the Solar Flux daily proxy S10.7
        
        
        """
        ...
    def setFixedS10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7.
        
            Parameters:
                fixedS10P7Mean (double): fixed (time invariant) value of the Solar Flux 81-day running center-average proxy S10.7
        
        
        """
        ...
    def setFixedY10P7(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux daily proxy Y10.7.
        
            Parameters:
                fixedY10P7 (double): fixed (time invariant) value of the Solar Flux daily proxy Y10.7
        
        
        """
        ...
    def setFixedY10P7Mean(self, double: float) -> None:
        """
            Set fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7.
        
            Parameters:
                fixedY10P7Mean (double): fixed (time invariant) value of the Solar Flux 81-day running center-average proxy Y10.7
        
        
        """
        ...
    def setGm(self, double: float) -> None:
        """
            Set gravitational coefficient of attracting body.
        
            Parameters:
                gm (double): gravitational coefficient of attracting body
        
        
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
    def setInterpMethodSW(self, string: str) -> None:
        """
            Set the interpolation method for Space Weather data.
        
            Parameters:
                interpMethodSW (String): interpolation method for Space Weather data
        
        
        """
        ...
    def setNBodyPerturbations(self, list: java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]) -> None: ...
    def setOblateFlattening(self, double: float) -> None:
        """
            Set central body oblate spheroid oblateness.
        
            Parameters:
                oblateFlattening (double): central body oblate spheroid oblateness
        
        
        """
        ...
    def setOceanTidesModel(self, string: str) -> None:
        """
            Set ocean tides model.
        
            Parameters:
                oceanTidesModel (String): ocean tides model
        
        
        """
        ...
    def setReductionTheory(self, string: str) -> None:
        """
            Set reduction theory used for precession and nutation modeling.
        
            Parameters:
                reductionTheory (String): reduction theory used for precession and nutation modeling
        
        
        """
        ...
    def setShadowBodies(self, list: java.util.List[org.orekit.files.ccsds.definitions.BodyFacade]) -> None: ...
    def setShadowModel(self, shadowModel: 'ShadowModel') -> None:
        """
            Set shadow model used for solar radiation pressure.
        
            Parameters:
                shadowModel (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ShadowModel`): shadow model used for solar radiation pressure
        
        
        """
        ...
    def setSolidTidesModel(self, string: str) -> None:
        """
            Set solid tides model.
        
            Parameters:
                solidTidesModel (String): solid tides model
        
        
        """
        ...
    def setSpaceWeatherEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the Space Weather data.
        
            Parameters:
                spaceWeatherEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the Space Weather data
        
        
        """
        ...
    def setSpaceWeatherSource(self, string: str) -> None:
        """
            Set Space Weather data source.
        
            Parameters:
                spaceWeatherSource (String): Space Weather data source
        
        
        """
        ...
    def setSrpModel(self, string: str) -> None:
        """
            Set Solar Radiation Pressure model.
        
            Parameters:
                srpModel (String): Solar Radiation Pressure model
        
        
        """
        ...

class PerturbationsKey(java.lang.Enum['PerturbationsKey']):
    """
    public enum PerturbationsKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.PerturbationsKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.Perturbations` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['PerturbationsKey'] = ...
    ATMOSPHERIC_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    GRAVITY_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    EQUATORIAL_RADIUS: typing.ClassVar['PerturbationsKey'] = ...
    GM: typing.ClassVar['PerturbationsKey'] = ...
    N_BODY_PERTURBATIONS: typing.ClassVar['PerturbationsKey'] = ...
    CENTRAL_BODY_ROTATION: typing.ClassVar['PerturbationsKey'] = ...
    OBLATE_FLATTENING: typing.ClassVar['PerturbationsKey'] = ...
    OCEAN_TIDES_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    SOLID_TIDES_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    REDUCTION_THEORY: typing.ClassVar['PerturbationsKey'] = ...
    ALBEDO_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    ALBEDO_GRID_SIZE: typing.ClassVar['PerturbationsKey'] = ...
    SHADOW_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    SHADOW_BODIES: typing.ClassVar['PerturbationsKey'] = ...
    SRP_MODEL: typing.ClassVar['PerturbationsKey'] = ...
    SW_DATA_SOURCE: typing.ClassVar['PerturbationsKey'] = ...
    SW_DATA_EPOCH: typing.ClassVar['PerturbationsKey'] = ...
    SW_INTERP_METHOD: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_GEOMAG_KP: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_GEOMAG_AP: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_GEOMAG_DST: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_F10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_F10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_M10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_M10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_S10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_S10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_Y10P7: typing.ClassVar['PerturbationsKey'] = ...
    FIXED_Y10P7_MEAN: typing.ClassVar['PerturbationsKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, perturbations: Perturbations) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.Perturbations`): container to fill
        
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
    def valueOf(string: str) -> 'PerturbationsKey':
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
    def values() -> typing.List['PerturbationsKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (PerturbationsKey c : PerturbationsKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PhysicalProperties(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class PhysicalProperties extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Spacecraft physical properties.
    
        Since:
            11.0
    """
    def getAttitudeActuatorType(self) -> str:
        """
            Get the type of actuator for attitude control.
        
            Returns:
                type of actuator for attitude control
        
        
        """
        ...
    def getAttitudeControlAccuracy(self) -> float:
        """
            Get the accuracy of attitude control.
        
            Returns:
                accuracy of attitude control
        
        
        """
        ...
    def getAttitudeControlMode(self) -> str:
        """
            Get the attitude control mode.
        
            Returns:
                attitude control mode
        
        
        """
        ...
    def getAttitudeKnowledgeAccuracy(self) -> float:
        """
            Get the accuracy of attitude knowledge.
        
            Returns:
                accuracy of attitude knowledge
        
        
        """
        ...
    def getAttitudePointingAccuracy(self) -> float:
        """
            Get the overall accuracy of spacecraft to maintain attitude.
        
            Returns:
                overall accuracy of spacecraft to maintain attitude
        
        
        """
        ...
    def getBolDv(self) -> float:
        """
            Get the total Î”V capability at beginning of life.
        
            Returns:
                total Î”V capability at beginning of life
        
        
        """
        ...
    def getBusModel(self) -> str:
        """
            Get the bus model name.
        
            Returns:
                bus model name
        
        
        """
        ...
    def getDockedWith(self) -> java.util.List[str]:
        """
            Get the other space objects this object is docked to.
        
            Returns:
                the oother space objects this object is docked to
        
        
        """
        ...
    def getDragCoefficient(self) -> float:
        """
            Get the nominal drag coefficient.
        
            Returns:
                the nominal drag coefficient
        
        
        """
        ...
    def getDragConstantArea(self) -> float:
        """
            Get the attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB.
        
            Returns:
                attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def getDragUncertainty(self) -> float:
        """
            Get the drag coefficient 1Ïƒ uncertainty.
        
            Returns:
                drag coefficient 1Ïƒ uncertainty (in %)
        
        
        """
        ...
    def getDryMass(self) -> float:
        """
            Get the mass without propellant.
        
            Returns:
                mass without propellant
        
        
        """
        ...
    def getInertiaMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the inertia matrix.
        
            Returns:
                the inertia matrix
        
        
        """
        ...
    def getInitialWetMass(self) -> float:
        """
            Get the total mass at beginning of life.
        
            Returns:
                total mass at beginning of life
        
        
        """
        ...
    def getManeuversFrequency(self) -> float:
        """
            Get the average frequency of orbit or attitude maneuvers (in SI units, hence per second).
        
            Returns:
                average frequency of orbit or attitude maneuvers (in SI units, hence per second).
        
        
        """
        ...
    def getManeuversPerYear(self) -> float:
        """
            Get the average number of orbit or attitude maneuvers per year.
        
            Returns:
                average number of orbit or attitude maneuvers per year.
        
        
        """
        ...
    def getManufacturer(self) -> str:
        """
            Get manufacturer name.
        
            Returns:
                manufacturer name
        
        
        """
        ...
    def getMaxAreaForCollisionProbability(self) -> float:
        """
            Get the maximum cross-sectional area for collision probability estimation purposes.
        
            Returns:
                maximum cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def getMaxRcs(self) -> float:
        """
            Get the maximum radar cross-section.
        
            Returns:
                maximum radar cross-section
        
        
        """
        ...
    def getMaxThrust(self) -> float:
        """
            Get the maximum composite thrust the spacecraft can accomplish.
        
            Returns:
                maximum composite thrust the spacecraft can accomplish
        
        
        """
        ...
    def getMinAreaForCollisionProbability(self) -> float:
        """
            Get the minimum cross-sectional area for collision probability estimation purposes.
        
            Returns:
                minimum cross-sectional area for collision probability estimation purposes
        
        
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
            Get the cross-sectional area of Optimally Enclosing Box along Y-OEB.
        
            Returns:
                cross-sectional area of Optimally Enclosing Box along Y-OEB
        
        
        """
        ...
    def getOebAreaAlongMax(self) -> float:
        """
            Get the cross-sectional area of Optimally Enclosing Box along X-OEB.
        
            Returns:
                cross-sectional area of Optimally Enclosing Box along X-OEB
        
        
        """
        ...
    def getOebAreaAlongMin(self) -> float:
        """
            Get the cross-sectional area of Optimally Enclosing Box along Z-OEB.
        
            Returns:
                cross-sectional area of Optimally Enclosing Box along X-OEB
        
        
        """
        ...
    def getOebIntermediate(self) -> float:
        """
            Get the dimensions of Optimally Enclosing Box along Y-OEB (i.e intermediate).
        
            Returns:
                dimensions of Optimally Enclosing Box along Y-OEB (i.e intermediate).
        
        
        """
        ...
    def getOebMax(self) -> float:
        """
            Get the dimensions of Optimally Enclosing Box along X-OEB (i.e max).
        
            Returns:
                dimensions of Optimally Enclosing Box along X-OEB (i.e max)
        
        
        """
        ...
    def getOebMin(self) -> float:
        """
            Get the dimensions of Optimally Enclosing Box along Z-OEB (i.e min).
        
            Returns:
                dimensions of Optimally Enclosing Box along Z-OEB (i.e min)
        
        
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
    def getReflectivity(self) -> float:
        """
            Get the typical (50th percentile) coefficient of reflectivity.
        
            Returns:
                typical (50th percentile) coefficient of reflectivity
        
        
        """
        ...
    def getRemainingDv(self) -> float:
        """
            Get the total Î”V remaining for spacecraft.
        
            Returns:
                total Î”V remaining for spacecraft
        
        
        """
        ...
    def getSrpCoefficient(self) -> float:
        """
            Get the nominal SRP coefficient.
        
            Returns:
                nominal SRP coefficient
        
        
        """
        ...
    def getSrpConstantArea(self) -> float:
        """
            Get the attitude-independent SRP area, not already into attitude-dependent area along OEB.
        
            Returns:
                attitude-independent SRP area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def getSrpUncertainty(self) -> float:
        """
            Get the SRP coefficient 1Ïƒ uncertainty.
        
            Returns:
                SRP coefficient 1Ïƒ uncertainty
        
        
        """
        ...
    def getTypAreaForCollisionProbability(self) -> float:
        """
            Get the typical (50th percentile) cross-sectional area for collision probability estimation purposes.
        
            Returns:
                typical (50th percentile) cross-sectional area for collision probability estimation purposes
        
        
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
    def getWetMass(self) -> float:
        """
            Get the total mass at Tâ‚€.
        
            Returns:
                total mass at Tâ‚€
        
        
        """
        ...
    def setAttitudeActuatorType(self, string: str) -> None:
        """
            Set the type of actuator for attitude control.
        
            Parameters:
                attitudeActuatorType (String): type of actuator for attitude control
        
        
        """
        ...
    def setAttitudeControlAccuracy(self, double: float) -> None:
        """
            Set the accuracy of attitude control.
        
            Parameters:
                attitudeControlAccuracy (double): accuracy of attitude control
        
        
        """
        ...
    def setAttitudeControlMode(self, string: str) -> None:
        """
            Set the attitude control mode.
        
            Parameters:
                attitudeControlMode (String): attitude control mode
        
        
        """
        ...
    def setAttitudeKnowledgeAccuracy(self, double: float) -> None:
        """
            Set the accuracy of attitude knowledge.
        
            Parameters:
                attitudeKnowledgeAccuracy (double): accuracy of attitude knowledge
        
        
        """
        ...
    def setAttitudePointingAccuracy(self, double: float) -> None:
        """
            Set the overall accuracy of spacecraft to maintain attitude.
        
            Parameters:
                attitudePointingAccuracy (double): overall accuracy of spacecraft to maintain attitude
        
        
        """
        ...
    def setBolDv(self, double: float) -> None:
        """
            Set the total Î”V capability at beginning of life.
        
            Parameters:
                bolDv (double): total Î”V capability at beginning of life
        
        
        """
        ...
    def setBusModel(self, string: str) -> None:
        """
            Set the bus model name.
        
            Parameters:
                busModel (String): bus model name
        
        
        """
        ...
    def setDockedWith(self, list: java.util.List[str]) -> None:
        """
            Set the other space objects this object is docked to.
        
            Parameters:
                dockedWith (List<String> dockedWith): the other space objects this object is docked to
        
        
        """
        ...
    def setDragCoefficient(self, double: float) -> None:
        """
            Set the the nominal drag coefficient.
        
            Parameters:
                dragCoefficient (double): the nominal drag coefficient
        
        
        """
        ...
    def setDragConstantArea(self, double: float) -> None:
        """
            Set the attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB.
        
            Parameters:
                dragConstantArea (double): attitude-independent drag cross-sectional area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def setDragUncertainty(self, double: float) -> None:
        """
            Set the drag coefficient 1Ïƒ uncertainty.
        
            Parameters:
                dragUncertainty (double): drag coefficient 1Ïƒ uncertainty (in %)
        
        
        """
        ...
    def setDryMass(self, double: float) -> None:
        """
            Set the mass without propellant.
        
            Parameters:
                dryMass (double): mass without propellant
        
        
        """
        ...
    def setInertiaMatrixEntry(self, int: int, int2: int, double: float) -> None:
        """
            Set an entry in the inertia matrix.
        
            Both I(j, k) and I(k, j) are set.
        
            Parameters:
                j (int): row index (must be between 0 and 3 (inclusive)
                k (int): column index (must be between 0 and 3 (inclusive)
                entry (double): value of the matrix entry
        
        
        """
        ...
    def setInitialWetMass(self, double: float) -> None:
        """
            Set the total mass at beginning of life.
        
            Parameters:
                initialWetMass (double): total mass at beginning of life
        
        
        """
        ...
    def setManeuversFrequency(self, double: float) -> None:
        """
            Set the average frequency of orbit or attitude maneuvers (in SI units, hence per second).
        
            Parameters:
                maneuversFrequency (double): average frequency of orbit or attitude (in SI units, hence per second).
        
        
        """
        ...
    def setManufacturer(self, string: str) -> None:
        """
            Set manufacturer name.
        
            Parameters:
                manufacturer (String): manufacturer name
        
        
        """
        ...
    def setMaxAreaForCollisionProbability(self, double: float) -> None:
        """
            Set the maximum cross-sectional area for collision probability estimation purposes.
        
            Parameters:
                maxAreaForCollisionProbability (double): maximum cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def setMaxRcs(self, double: float) -> None:
        """
            Set the maximum radar cross-section.
        
            Parameters:
                maxRcs (double): maximum radar cross-section
        
        
        """
        ...
    def setMaxThrust(self, double: float) -> None:
        """
            Set the maximum composite thrust the spacecraft can accomplish.
        
            Parameters:
                maxThrust (double): maximum composite thrust the spacecraft can accomplish
        
        
        """
        ...
    def setMinAreaForCollisionProbability(self, double: float) -> None:
        """
            Set the minimum cross-sectional area for collision probability estimation purposes.
        
            Parameters:
                minAreaForCollisionProbability (double): minimum cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def setMinRcs(self, double: float) -> None:
        """
            Set the minimum radar cross-section.
        
            Parameters:
                minRcs (double): minimum radar cross-section
        
        
        """
        ...
    def setOebAreaAlongIntermediate(self, double: float) -> None:
        """
            Set the cross-sectional area of Optimally Enclosing Box along Y-OEB.
        
            Parameters:
                oebAreaAlongIntermediate (double): cross-sectional area of Optimally Enclosing Box along X-OEB
        
        
        """
        ...
    def setOebAreaAlongMax(self, double: float) -> None:
        """
            Set the cross-sectional area of Optimally Enclosing Box along X-OEB.
        
            Parameters:
                oebAreaAlongMax (double): cross-sectional area of Optimally Enclosing Box along X-OEB
        
        
        """
        ...
    def setOebAreaAlongMin(self, double: float) -> None:
        """
            Set the cross-sectional area of Optimally Enclosing Box along Z-OEB.
        
            Parameters:
                oebAreaAlongMin (double): cross-sectional area of Optimally Enclosing Box along X-OEB
        
        
        """
        ...
    def setOebIntermediate(self, double: float) -> None:
        """
            Set the dimensions of Optimally Enclosing Box along Y-OEB (i.e intermediate).
        
            Parameters:
                oebIntermediate (double): dimensions of Optimally Enclosing Box along Y-OEB (i.e intermediate).
        
        
        """
        ...
    def setOebMax(self, double: float) -> None:
        """
            Set the dimensions of Optimally Enclosing Box along X-OEB (i.e max).
        
            Parameters:
                oebMax (double): dimensions of Optimally Enclosing Box along X-OEB (i.e max)
        
        
        """
        ...
    def setOebMin(self, double: float) -> None:
        """
            Set the dimensions of Optimally Enclosing Box along Z-OEB (i.e min).
        
            Parameters:
                oebMin (double): dimensions of Optimally Enclosing Box along Z-OEB (i.e min)
        
        
        """
        ...
    def setOebParentFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set the Optimally Enclosing Box parent reference frame.
        
            Parameters:
                oebParentFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): Optimally Enclosing Box parent reference frame
        
        
        """
        ...
    def setOebParentFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set the Optimally Enclosing Box parent reference frame epoch.
        
            Parameters:
                oebParentFrameEpoch (:class:`~org.orekit.time.AbsoluteDate`): Optimally Enclosing Box parent reference frame epoch
        
        
        """
        ...
    def setOebQ(self, int: int, double: float) -> None:
        """
            set the component of quaternion defining Optimally Enclosing Box.
        
            Parameters:
                i (int): index of the component
                qI (double): component of quaternion defining Optimally Enclosing Box
        
        
        """
        ...
    def setRcs(self, double: float) -> None:
        """
            Set the typical (50th percentile) radar cross-section.
        
            Parameters:
                rcs (double): typical (50th percentile) radar cross-section
        
        
        """
        ...
    def setReflectivity(self, double: float) -> None:
        """
            Set the typical (50th percentile) coefficient of reflectivity.
        
            Parameters:
                reflectivity (double): typical (50th percentile) coefficient of reflectivity
        
        
        """
        ...
    def setRemainingDv(self, double: float) -> None:
        """
            Set the total Î”V remaining for spacecraft.
        
            Parameters:
                remainingDv (double): total Î”V remaining for spacecraft
        
        
        """
        ...
    def setSrpCoefficient(self, double: float) -> None:
        """
            Set the nominal SRP coefficient.
        
            Parameters:
                srpCoefficient (double): nominal SRP coefficient
        
        
        """
        ...
    def setSrpConstantArea(self, double: float) -> None:
        """
            Set the attitude-independent SRP area, not already into attitude-dependent area along OEB.
        
            Parameters:
                srpConstantArea (double): attitude-independent SRP area, not already into attitude-dependent area along OEB
        
        
        """
        ...
    def setSrpUncertainty(self, double: float) -> None:
        """
            Set the SRP coefficient 1Ïƒ uncertainty.
        
            Parameters:
                srpUncertainty (double): SRP coefficient 1Ïƒ uncertainty.
        
        
        """
        ...
    def setTypAreaForCollisionProbability(self, double: float) -> None:
        """
            Get the typical (50th percentile) cross-sectional area for collision probability estimation purposes.
        
            Parameters:
                typAreaForCollisionProbability (double): typical (50th percentile) cross-sectional area for collision probability estimation purposes
        
        
        """
        ...
    def setVmAbsolute(self, double: float) -> None:
        """
            Set the typical (50th percentile) visual magnitude.
        
            Parameters:
                vmAbsolute (double): typical (50th percentile) visual magnitude
        
        
        """
        ...
    def setVmApparent(self, double: float) -> None:
        """
            Set the typical (50th percentile) apparent visual magnitude.
        
            Parameters:
                vmApparent (double): typical (50th percentile) apparent visual magnitude
        
        
        """
        ...
    def setVmApparentMax(self, double: float) -> None:
        """
            Set the maximum apparent visual magnitude.
        
            Parameters:
                vmApparentMax (double): maximum apparent visual magnitude
        
        
        """
        ...
    def setVmApparentMin(self, double: float) -> None:
        """
            Set the minimum apparent visual magnitude.
        
            Parameters:
                vmApparentMin (double): minimum apparent visual magnitude
        
        
        """
        ...
    def setWetMass(self, double: float) -> None:
        """
            Set the total mass at Tâ‚€.
        
            Parameters:
                wetMass (double): total mass at Tâ‚€
        
        
        """
        ...

class PhysicalPropertiesKey(java.lang.Enum['PhysicalPropertiesKey']):
    """
    public enum PhysicalPropertiesKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.PhysicalPropertiesKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.PhysicalProperties` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['PhysicalPropertiesKey'] = ...
    MANUFACTURER: typing.ClassVar['PhysicalPropertiesKey'] = ...
    BUS_MODEL: typing.ClassVar['PhysicalPropertiesKey'] = ...
    DOCKED_WITH: typing.ClassVar['PhysicalPropertiesKey'] = ...
    DRAG_CONST_AREA: typing.ClassVar['PhysicalPropertiesKey'] = ...
    DRAG_COEFF_NOM: typing.ClassVar['PhysicalPropertiesKey'] = ...
    DRAG_UNCERTAINTY: typing.ClassVar['PhysicalPropertiesKey'] = ...
    INITIAL_WET_MASS: typing.ClassVar['PhysicalPropertiesKey'] = ...
    WET_MASS: typing.ClassVar['PhysicalPropertiesKey'] = ...
    DRY_MASS: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_PARENT_FRAME: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_PARENT_FRAME_EPOCH: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_Q1: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_Q2: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_Q3: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_QC: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_MAX: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_INT: typing.ClassVar['PhysicalPropertiesKey'] = ...
    OEB_MIN: typing.ClassVar['PhysicalPropertiesKey'] = ...
    AREA_ALONG_OEB_MAX: typing.ClassVar['PhysicalPropertiesKey'] = ...
    AREA_ALONG_OEB_INT: typing.ClassVar['PhysicalPropertiesKey'] = ...
    AREA_ALONG_OEB_MIN: typing.ClassVar['PhysicalPropertiesKey'] = ...
    AREA_MIN_FOR_PC: typing.ClassVar['PhysicalPropertiesKey'] = ...
    AREA_MAX_FOR_PC: typing.ClassVar['PhysicalPropertiesKey'] = ...
    AREA_TYP_FOR_PC: typing.ClassVar['PhysicalPropertiesKey'] = ...
    RCS: typing.ClassVar['PhysicalPropertiesKey'] = ...
    RCS_MIN: typing.ClassVar['PhysicalPropertiesKey'] = ...
    RCS_MAX: typing.ClassVar['PhysicalPropertiesKey'] = ...
    SRP_CONST_AREA: typing.ClassVar['PhysicalPropertiesKey'] = ...
    SOLAR_RAD_COEFF: typing.ClassVar['PhysicalPropertiesKey'] = ...
    SOLAR_RAD_UNCERTAINTY: typing.ClassVar['PhysicalPropertiesKey'] = ...
    VM_ABSOLUTE: typing.ClassVar['PhysicalPropertiesKey'] = ...
    VM_APPARENT_MIN: typing.ClassVar['PhysicalPropertiesKey'] = ...
    VM_APPARENT: typing.ClassVar['PhysicalPropertiesKey'] = ...
    VM_APPARENT_MAX: typing.ClassVar['PhysicalPropertiesKey'] = ...
    REFLECTIVITY: typing.ClassVar['PhysicalPropertiesKey'] = ...
    ATT_CONTROL_MODE: typing.ClassVar['PhysicalPropertiesKey'] = ...
    ATT_ACTUATOR_TYPE: typing.ClassVar['PhysicalPropertiesKey'] = ...
    ATT_KNOWLEDGE: typing.ClassVar['PhysicalPropertiesKey'] = ...
    ATT_CONTROL: typing.ClassVar['PhysicalPropertiesKey'] = ...
    ATT_POINTING: typing.ClassVar['PhysicalPropertiesKey'] = ...
    AVG_MANEUVER_FREQ: typing.ClassVar['PhysicalPropertiesKey'] = ...
    MAX_THRUST: typing.ClassVar['PhysicalPropertiesKey'] = ...
    DV_BOL: typing.ClassVar['PhysicalPropertiesKey'] = ...
    DV_REMAINING: typing.ClassVar['PhysicalPropertiesKey'] = ...
    IXX: typing.ClassVar['PhysicalPropertiesKey'] = ...
    IYY: typing.ClassVar['PhysicalPropertiesKey'] = ...
    IZZ: typing.ClassVar['PhysicalPropertiesKey'] = ...
    IXY: typing.ClassVar['PhysicalPropertiesKey'] = ...
    IXZ: typing.ClassVar['PhysicalPropertiesKey'] = ...
    IYZ: typing.ClassVar['PhysicalPropertiesKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, physicalProperties: PhysicalProperties) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                data (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.PhysicalProperties`): data to fill
        
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
    def valueOf(string: str) -> 'PhysicalPropertiesKey':
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
    def values() -> typing.List['PhysicalPropertiesKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (PhysicalPropertiesKey c : PhysicalPropertiesKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ShadowModel(java.lang.Enum['ShadowModel']):
    """
    public enum ShadowModel extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.ShadowModel`>
    
        Shadow model for solar radiation pressure.
    
        Since:
            11.0
    """
    NONE: typing.ClassVar['ShadowModel'] = ...
    CYLINDRICAL: typing.ClassVar['ShadowModel'] = ...
    CONE: typing.ClassVar['ShadowModel'] = ...
    DUAL_CONE: typing.ClassVar['ShadowModel'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ShadowModel':
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
    def values() -> typing.List['ShadowModel']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ShadowModel c : ShadowModel.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TrajectoryState(org.orekit.time.TimeStamped):
    """
    public class TrajectoryState extends Object implements :class:`~org.orekit.time.TimeStamped`
    
        Trajectory state entry.
    
        Since:
            11.0
    """
    def __init__(self, elementsType: org.orekit.files.ccsds.definitions.ElementsType, absoluteDate: org.orekit.time.AbsoluteDate, stringArray: typing.List[str], int: int, list: java.util.List[org.orekit.utils.units.Unit]): ...
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get which derivatives of position are available in this state.
        
            Returns:
                a value indicating if the file contains velocity and/or acceleration
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getElements(self) -> typing.List[float]:
        """
            Get trajectory elements.
        
            Returns:
                trajectory elements
        
        
        """
        ...
    def getType(self) -> org.orekit.files.ccsds.definitions.ElementsType:
        """
            Get the type of the elements.
        
            Returns:
                type of the elements
        
        
        """
        ...
    def toCartesian(self, double: float) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Convert to Cartesian coordinates.
        
            Parameters:
                mu (double): gravitational parameter in mÂ³/sÂ²
        
            Returns:
                Cartesian coordinates
        
        
        """
        ...

class TrajectoryStateHistory(org.orekit.files.general.EphemerisFile.EphemerisSegment[org.orekit.utils.TimeStampedPVCoordinates]):
    """
    public class TrajectoryStateHistory extends Object implements :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`<:class:`~org.orekit.utils.TimeStampedPVCoordinates`>
    
        Trajectory state history.
    
        Since:
            11.0
    """
    def getAvailableDerivatives(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get which derivatives of position are available in this ephemeris segment.
        
            While :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates` always returns position, velocity,
            and acceleration the return value from this method indicates which of those are in the ephemeris file and are actually
            valid.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getAvailableDerivatives`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                a value indicating if the file contains velocity and/or acceleration data.
        
        
        """
        ...
    def getCoordinates(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the reference frame for this ephemeris segment. The defining frame for
            :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getCoordinates`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getFrame`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the reference frame for this segment. Never :code:`null`.
        
        
        """
        ...
    def getInterpolationSamples(self) -> int:
        """
            Get the number of samples to use in interpolation.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getInterpolationSamples`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the number of points to use for interpolation.
        
        
        """
        ...
    def getMetadata(self) -> 'TrajectoryStateHistoryMetadata':
        """
            Get metadata.
        
            Returns:
                metadata
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the standard gravitational parameter for the satellite.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getMu`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                the gravitational parameter used in :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getPropagator`, in
                mÃ‚Â³/sÃ‚Â².
        
        
        """
        ...
    def getStart(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMinDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStart`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment start date.
        
        
        """
        ...
    def getStop(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date of this ephemeris segment.
        
            The date returned by this method is equivalent to :code:`getPropagator().getMaxDate()`.
        
            Specified by:
                :meth:`~org.orekit.files.general.EphemerisFile.EphemerisSegment.getStop`Â in
                interfaceÂ :class:`~org.orekit.files.general.EphemerisFile.EphemerisSegment`
        
            Returns:
                ephemeris segment end date.
        
        
        """
        ...
    def getTrajectoryStates(self) -> java.util.List[TrajectoryState]: ...

class TrajectoryStateHistoryMetadata(org.orekit.files.ccsds.section.CommentsContainer):
    """
    public class TrajectoryStateHistoryMetadata extends :class:`~org.orekit.files.ccsds.section.CommentsContainer`
    
        Metadata for trajectory state history.
    
        Since:
            11.0
    """
    def getCenter(self) -> org.orekit.files.ccsds.definitions.BodyFacade:
        """
            Get the origin of reference frame.
        
            Returns:
                the origin of reference frame.
        
        
        """
        ...
    def getInterpolationDegree(self) -> int:
        """
            Get the interpolation degree.
        
            Returns:
                the interpolation degree
        
        
        """
        ...
    def getInterpolationMethod(self) -> org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod:
        """
            Get the interpolation method to be used.
        
            Returns:
                the interpolation method
        
        
        """
        ...
    def getOrbAveraging(self) -> str:
        """
            Get type of averaging (Osculating, mean Brouwer, other.
        
            Returns:
                type of averaging (Osculating, mean Brouwer, other .).
        
        
        """
        ...
    def getOrbRevNum(self) -> int:
        """
            Get the integer orbit revolution number.
        
            Returns:
                integer orbit revolution number (-1 if not set)
        
        
        """
        ...
    def getOrbRevNumBasis(self) -> int:
        """
            Get the basis for orbit revolution number.
        
            This specifies if first launch/deployment is on orbit 0 or 1.
        
            Returns:
                basis for orbit revolution number (-1 if not set)
        
        
        """
        ...
    def getTrajBasis(self) -> str:
        """
            Get basis of this trajectory state time history data.
        
            Returns:
                basis of this trajectory state time history data
        
        
        """
        ...
    def getTrajBasisID(self) -> str:
        """
            Get identification number of the orbit determination or simulation upon which this trajectory is based.
        
            Returns:
                identification number of the orbit determination or simulation upon which this trajectory is based
        
        
        """
        ...
    def getTrajFrameEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`.
        
            Returns:
                epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`
        
        
        """
        ...
    def getTrajID(self) -> str:
        """
            Get trajectory identification number.
        
            Returns:
                trajectory identification number
        
        
        """
        ...
    def getTrajNextID(self) -> str:
        """
            Get identification number of next trajectory.
        
            Returns:
                identification number of next trajectory
        
        
        """
        ...
    def getTrajPrevID(self) -> str:
        """
            Get identification number of previous trajectory.
        
            Returns:
                identification number of previous trajectory
        
        
        """
        ...
    def getTrajReferenceFrame(self) -> org.orekit.files.ccsds.definitions.FrameFacade:
        """
            Get reference frame of the trajectory.
        
            Returns:
                reference frame of the trajectory
        
        
        """
        ...
    def getTrajType(self) -> org.orekit.files.ccsds.definitions.ElementsType:
        """
            Get trajectory element set type.
        
            Returns:
                trajectory element set type
        
        
        """
        ...
    def getTrajUnits(self) -> java.util.List[org.orekit.utils.units.Unit]: ...
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
    def setCenter(self, bodyFacade: org.orekit.files.ccsds.definitions.BodyFacade) -> None:
        """
            Set the origin of reference frame.
        
            Parameters:
                center (:class:`~org.orekit.files.ccsds.definitions.BodyFacade`): origin of reference frame to be set
        
        
        """
        ...
    def setInterpolationDegree(self, int: int) -> None:
        """
            Set the interpolation degree.
        
            Parameters:
                interpolationDegree (int): the interpolation degree to be set
        
        
        """
        ...
    def setInterpolationMethod(self, interpolationMethod: org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod) -> None:
        """
            Set the interpolation method to be used.
        
            Parameters:
                interpolationMethod (:class:`~org.orekit.files.ccsds.ndm.odm.oem.InterpolationMethod`): the interpolation method to be set
        
        
        """
        ...
    def setOrbAveraging(self, string: str) -> None:
        """
            Set type of averaging (Osculating, mean Brouwer, other.
        
            Parameters:
                orbAveraging (String): type of averaging (Osculating, mean Brouwer, other .).
        
        
        """
        ...
    def setOrbRevNum(self, int: int) -> None:
        """
            Set the integer orbit revolution number.
        
            Parameters:
                orbRevNum (int): integer orbit revolution number
        
        
        """
        ...
    def setOrbRevNumBasis(self, int: int) -> None:
        """
            Set the basis for orbit revolution number.
        
            This specifies if first launch/deployment is on orbit 0 or 1.
        
            Parameters:
                orbRevNumBasis (int): basis for orbit revolution number
        
        
        """
        ...
    def setTrajBasis(self, string: str) -> None:
        """
            Set basis of this trajectory state time history data.
        
            Parameters:
                trajBasis (String): basis of this trajectory state time history data
        
        
        """
        ...
    def setTrajBasisID(self, string: str) -> None:
        """
            Set identification number of the orbit determination or simulation upon which this trajectory is based.
        
            Parameters:
                trajBasisID (String): identification number of the orbit determination or simulation upon which this trajectory is based
        
        
        """
        ...
    def setTrajFrameEpoch(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`.
        
            Parameters:
                trajFrameEpoch (:class:`~org.orekit.time.AbsoluteDate`): epoch of the :meth:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata.getTrajReferenceFrame`
        
        
        """
        ...
    def setTrajID(self, string: str) -> None:
        """
            Set trajectory identification number.
        
            Parameters:
                trajID (String): trajectory identification number
        
        
        """
        ...
    def setTrajNextID(self, string: str) -> None:
        """
            Set identification number of next trajectory.
        
            Parameters:
                trajNextID (String): identification number of next trajectory
        
        
        """
        ...
    def setTrajPrevID(self, string: str) -> None:
        """
            Set identification number of previous trajectory.
        
            Parameters:
                trajPrevID (String): identification number of previous trajectory
        
        
        """
        ...
    def setTrajReferenceFrame(self, frameFacade: org.orekit.files.ccsds.definitions.FrameFacade) -> None:
        """
            Set reference frame of the trajectory.
        
            Parameters:
                trajReferenceFrame (:class:`~org.orekit.files.ccsds.definitions.FrameFacade`): the reference frame to be set
        
        
        """
        ...
    def setTrajType(self, elementsType: org.orekit.files.ccsds.definitions.ElementsType) -> None:
        """
            Set trajectory element set type.
        
            Parameters:
                trajType (:class:`~org.orekit.files.ccsds.definitions.ElementsType`): trajectory element set type
        
        
        """
        ...
    def setTrajUnits(self, list: java.util.List[org.orekit.utils.units.Unit]) -> None: ...
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
                :meth:`~org.orekit.files.ccsds.section.CommentsContainer.validate`Â in
                classÂ :class:`~org.orekit.files.ccsds.section.CommentsContainer`
        
            Parameters:
                version (double): format version
        
        
        """
        ...

class TrajectoryStateHistoryMetadataKey(java.lang.Enum['TrajectoryStateHistoryMetadataKey']):
    """
    public enum TrajectoryStateHistoryMetadataKey extends Enum<:class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadataKey`>
    
        Keys for :class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata` entries.
    
        Since:
            11.0
    """
    COMMENT: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_PREV_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_NEXT_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_BASIS: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_BASIS_ID: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    INTERPOLATION: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    INTERPOLATION_DEGREE: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    ORB_AVERAGING: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    CENTER_NAME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_REF_FRAME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_FRAME_EPOCH: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    USEABLE_START_TIME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    USEABLE_STOP_TIME: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    ORB_REVNUM: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    ORB_REVNUM_BASIS: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_TYPE: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    TRAJ_UNITS: typing.ClassVar['TrajectoryStateHistoryMetadataKey'] = ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken, contextBinding: org.orekit.files.ccsds.utils.ContextBinding, trajectoryStateHistoryMetadata: TrajectoryStateHistoryMetadata) -> bool:
        """
            Process an token.
        
            Parameters:
                token (:class:`~org.orekit.files.ccsds.utils.lexical.ParseToken`): token to process
                context (:class:`~org.orekit.files.ccsds.utils.ContextBinding`): context binding
                container (:class:`~org.orekit.files.ccsds.ndm.odm.ocm.TrajectoryStateHistoryMetadata`): container to fill
        
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
    def valueOf(string: str) -> 'TrajectoryStateHistoryMetadataKey':
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
    def values() -> typing.List['TrajectoryStateHistoryMetadataKey']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (TrajectoryStateHistoryMetadataKey c : TrajectoryStateHistoryMetadataKey.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.ndm.odm.ocm")``.

    Covariance: typing.Type[Covariance]
    CovarianceHistory: typing.Type[CovarianceHistory]
    CovarianceHistoryMetadata: typing.Type[CovarianceHistoryMetadata]
    CovarianceHistoryMetadataKey: typing.Type[CovarianceHistoryMetadataKey]
    ManBasis: typing.Type[ManBasis]
    Maneuver: typing.Type[Maneuver]
    ManeuverFieldType: typing.Type[ManeuverFieldType]
    ManeuverHistory: typing.Type[ManeuverHistory]
    ManeuverHistoryMetadata: typing.Type[ManeuverHistoryMetadata]
    ManeuverHistoryMetadataKey: typing.Type[ManeuverHistoryMetadataKey]
    ObjectType: typing.Type[ObjectType]
    Ocm: typing.Type[Ocm]
    OcmData: typing.Type[OcmData]
    OcmDataSubStructureKey: typing.Type[OcmDataSubStructureKey]
    OcmMetadata: typing.Type[OcmMetadata]
    OcmMetadataKey: typing.Type[OcmMetadataKey]
    OcmParser: typing.Type[OcmParser]
    OcmSatelliteEphemeris: typing.Type[OcmSatelliteEphemeris]
    OcmWriter: typing.Type[OcmWriter]
    OpsStatus: typing.Type[OpsStatus]
    OrbitCategory: typing.Type[OrbitCategory]
    OrbitDetermination: typing.Type[OrbitDetermination]
    OrbitDeterminationKey: typing.Type[OrbitDeterminationKey]
    Ordering: typing.Type[Ordering]
    Perturbations: typing.Type[Perturbations]
    PerturbationsKey: typing.Type[PerturbationsKey]
    PhysicalProperties: typing.Type[PhysicalProperties]
    PhysicalPropertiesKey: typing.Type[PhysicalPropertiesKey]
    ShadowModel: typing.Type[ShadowModel]
    TrajectoryState: typing.Type[TrajectoryState]
    TrajectoryStateHistory: typing.Type[TrajectoryStateHistory]
    TrajectoryStateHistoryMetadata: typing.Type[TrajectoryStateHistoryMetadata]
    TrajectoryStateHistoryMetadataKey: typing.Type[TrajectoryStateHistoryMetadataKey]
