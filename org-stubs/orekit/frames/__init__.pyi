import java.io
import java.lang
import java.util
import java.util.function
import java.util.stream
import org
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.data
import org.orekit.time
import org.orekit.utils
import typing



class AbstractEopLoader(org.orekit.data.AbstractSelfFeedingLoader):
    """
    public class AbstractEopLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader`
    
        Base class for EOP loaders.
    """
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager, supplier: typing.Union[java.util.function.Supplier[org.orekit.time.TimeScale], typing.Callable[[], org.orekit.time.TimeScale]]): ...

class EOPEntry(org.orekit.time.TimeStamped, java.io.Serializable):
    """
    public class EOPEntry extends Object implements :class:`~org.orekit.time.TimeStamped`, Serializable
    
        This class holds an Earth Orientation Parameters entry.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, iTRFVersion: 'ITRFVersion', absoluteDate: org.orekit.time.AbsoluteDate): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getDdEps(self) -> float:
        """
            Get the correction for nutation in obliquity Î´Î”Îµ.
        
            Returns:
                correction for nutation in obliquity Î´Î”Îµ
        
        
        """
        ...
    def getDdPsi(self) -> float:
        """
            Get the correction for nutation in longitude Î´Î”Î¨.
        
            Returns:
                correction for nutation in longitude Î´Î”Î¨
        
        
        """
        ...
    def getDx(self) -> float:
        """
            Get the correction for Celestial Intermediate Pole (CIP) coordinates.
        
            Returns:
                correction for Celestial Intermediate Pole (CIP) coordinates
        
        
        """
        ...
    def getDy(self) -> float:
        """
            Get the correction for Celestial Intermediate Pole (CIP) coordinates.
        
            Returns:
                correction for Celestial Intermediate Pole (CIP) coordinates
        
        
        """
        ...
    def getITRFType(self) -> 'ITRFVersion':
        """
            Get the ITRF version this entry defines.
        
            Returns:
                ITRF version this entry defines
        
            Since:
                9.2
        
        
        """
        ...
    def getLOD(self) -> float:
        """
            Get the LoD (Length of Day) value.
        
            Returns:
                LoD in seconds
        
        
        """
        ...
    def getMjd(self) -> int:
        """
            Get the entry date (modified julian day, 00h00 UTC scale).
        
            Returns:
                entry date
        
            Also see:
                :meth:`~org.orekit.frames.EOPEntry.getDate`
        
        
        """
        ...
    def getUT1MinusUTC(self) -> float:
        """
            Get the UT1-UTC value.
        
            Returns:
                UT1-UTC in seconds
        
        
        """
        ...
    def getX(self) -> float:
        """
            Get the X component of the pole motion.
        
            Returns:
                X component of pole motion
        
        
        """
        ...
    def getY(self) -> float:
        """
            Get the Y component of the pole motion.
        
            Returns:
                Y component of pole motion
        
        
        """
        ...

class EOPHistory(java.io.Serializable):
    """
    public class EOPHistory extends Object implements Serializable
    
        This class loads any kind of Earth Orientation Parameter data throughout a large time range.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, collection: typing.Union[java.util.Collection[EOPEntry], typing.Sequence[EOPEntry], typing.Set[EOPEntry]], boolean: bool, timeScales: org.orekit.time.TimeScales): ...
    def checkEOPContinuity(self, double: float) -> None:
        """
            Check Earth orientation parameters continuity.
        
            Parameters:
                maxGap (double): maximal allowed gap between entries (in seconds)
        
        
        """
        ...
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
            Get the IERS conventions to which these EOP apply.
        
            Returns:
                IERS conventions to which these EOP apply
        
        
        """
        ...
    def getEndDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the last available Earth Orientation Parameters.
        
            Returns:
                the end date of the available data
        
        
        """
        ...
    def getEntries(self) -> java.util.List[EOPEntry]: ...
    _getEquinoxNutationCorrection_1__T = typing.TypeVar('_getEquinoxNutationCorrection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getEquinoxNutationCorrection(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Get the correction to the nutation parameters for equinox-based paradigm.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the correction is desired
        
            Returns:
                nutation correction in longitude Î”Î¨ and in obliquity Î”Îµ (zero if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getEquinoxNutationCorrection(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getEquinoxNutationCorrection_1__T]) -> typing.List[_getEquinoxNutationCorrection_1__T]:
        """
            Get the correction to the nutation parameters for equinox-based paradigm.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which the correction is desired
        
            Returns:
                nutation correction in longitude Î”Î¨ and in obliquity Î”Îµ (zero if date is outside covered range)
        
        
        """
        ...
    def getITRFVersion(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'ITRFVersion':
        """
            Get the ITRF version.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the value is desired
        
            Returns:
                ITRF version of the EOP covering the specified date
        
            Since:
                9.2
        
        
        """
        ...
    _getLOD_1__T = typing.TypeVar('_getLOD_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLOD(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the LoD (Length of Day) value.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the value is desired
        
            Returns:
                LoD in seconds (0 if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getLOD(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getLOD_1__T]) -> _getLOD_1__T:
        """
            Get the LoD (Length of Day) value.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which the value is desired
        
            Returns:
                LoD in seconds (0 if date is outside covered range)
        
            Since:
                9.0
        
        
        """
        ...
    def getNonInterpolatingEOPHistory(self) -> 'EOPHistory':
        """
            Get non-interpolating version of the instance.
        
            Returns:
                non-interpolatig version of the instance
        
        
        """
        ...
    _getNonRotatinOriginNutationCorrection_1__T = typing.TypeVar('_getNonRotatinOriginNutationCorrection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNonRotatinOriginNutationCorrection(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Get the correction to the nutation parameters for Non-Rotating Origin paradigm.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the correction is desired
        
            Returns:
                nutation correction in Celestial Intermediat Pole coordinates Î´X and Î´Y (zero if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getNonRotatinOriginNutationCorrection(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getNonRotatinOriginNutationCorrection_1__T]) -> typing.List[_getNonRotatinOriginNutationCorrection_1__T]:
        """
            Get the correction to the nutation parameters for Non-Rotating Origin paradigm.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which the correction is desired
        
            Returns:
                nutation correction in Celestial Intermediat Pole coordinates Î´X and Î´Y (zero if date is outside covered range)
        
        
        """
        ...
    _getPoleCorrection_0__T = typing.TypeVar('_getPoleCorrection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPoleCorrection(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPoleCorrection_0__T]) -> 'FieldPoleCorrection'[_getPoleCorrection_0__T]:
        """
            Get the pole IERS Reference Pole correction.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which the correction is desired
        
            Returns:
                pole correction (:meth:`~org.orekit.frames.PoleCorrection.NULL_CORRECTION` if date is outside covered range)
        
        
        """
        ...
    @typing.overload
    def getPoleCorrection(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'PoleCorrection':
        """
            Get the pole IERS Reference Pole correction.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the correction is desired
        
            Returns:
                pole correction (:meth:`~org.orekit.frames.PoleCorrection.NULL_CORRECTION` if date is outside covered range)
        
        """
        ...
    def getStartDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the first available Earth Orientation Parameters.
        
            Returns:
                the start date of the available data
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
            Get the time scales used in computing EOP corrections.
        
            Returns:
                set of time scales.
        
            Since:
                10.1
        
        
        """
        ...
    _getUT1MinusUTC_1__T = typing.TypeVar('_getUT1MinusUTC_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getUT1MinusUTC(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the UT1-UTC value.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the value is desired
        
            Returns:
                UT1-UTC in seconds (0 if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getUT1MinusUTC(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getUT1MinusUTC_1__T]) -> _getUT1MinusUTC_1__T:
        """
            Get the UT1-UTC value.
        
            The data provided comes from the IERS files. It is smoothed data.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date at which the value is desired
        
            Returns:
                UT1-UTC in seconds (0 if date is outside covered range)
        
            Since:
                9.0
        
        
        """
        ...
    def isSimpleEop(self) -> bool:
        """
            Determine if this history uses simplified EOP corrections.
        
            Returns:
                :code:`true` if tidal corrections are ignored, :code:`false` otherwise.
        
        
        """
        ...
    def usesInterpolation(self) -> bool:
        """
            Check if the instance uses interpolation on tidal corrections.
        
            Returns:
                true if the instance uses interpolation on tidal corrections
        
        
        """
        ...

class EOPHistoryLoader:
    """
    public interface EOPHistoryLoader
    
        Interface for loading Earth Orientation Parameters history.
    
        Since:
            6.1
    """
    def fillHistory(self, nutationCorrectionConverter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, sortedSet: java.util.SortedSet[EOPEntry]) -> None: ...
    class Parser:
        @staticmethod
        def newBulletinBParser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: 'ItrfVersionProvider', timeScales: org.orekit.time.TimeScales) -> 'EOPHistoryLoader.Parser': ...
        @staticmethod
        def newEopC04Parser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: 'ItrfVersionProvider', timeScales: org.orekit.time.TimeScales) -> 'EOPHistoryLoader.Parser': ...
        @staticmethod
        def newFinalsColumnsParser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: 'ItrfVersionProvider', timeScales: org.orekit.time.TimeScales, boolean: bool) -> 'EOPHistoryLoader.Parser': ...
        @staticmethod
        def newFinalsXmlParser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: 'ItrfVersionProvider', timeScales: org.orekit.time.TimeScales) -> 'EOPHistoryLoader.Parser': ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.Collection[EOPEntry]: ...

_FieldPoleCorrection__T = typing.TypeVar('_FieldPoleCorrection__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPoleCorrection(typing.Generic[_FieldPoleCorrection__T]):
    """
    public class FieldPoleCorrection<T extends CalculusFieldElement<T>> extends Object
    
        Simple container class for pole correction parameters.
    
        This class is a simple container, it does not provide any processing method.
    
        Since:
            9.0
    """
    def __init__(self, t: _FieldPoleCorrection__T, t2: _FieldPoleCorrection__T): ...
    def getXp(self) -> _FieldPoleCorrection__T:
        """
            Get the x :sub:`p` parameter.
        
            Returns:
                x :sub:`p` parameter
        
        
        """
        ...
    def getYp(self) -> _FieldPoleCorrection__T:
        """
            Get the y :sub:`p` parameter.
        
            Returns:
                y :sub:`p` parameter
        
        
        """
        ...

_FieldTransform__T = typing.TypeVar('_FieldTransform__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTransform(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['FieldTransform'[_FieldTransform__T]], typing.Generic[_FieldTransform__T]):
    """
    public class FieldTransform<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.frames.FieldTransform`<T>>
    
        Transformation class in three dimensional space.
    
        This class represents the transformation engine between :class:`~org.orekit.frames.Frame`. It is used both to define the
        relationship between each frame and its parent frame and to gather all individual transforms into one operation when
        converting between frames far away from each other.
    
        The convention used in OREKIT is vectorial transformation. It means that a transformation is defined as a transform to
        apply to the coordinates of a vector expressed in the old frame to obtain the same vector expressed in the new frame.
    
        Instances of this class are guaranteed to be immutable.
    
        Examples
    ----------
    
    
        Example of translation from R :sub:`A` to R :sub:`B`
    ------------------------------------------------------
    
    
        We want to transform the :class:`~org.orekit.utils.FieldPVCoordinates` PV :sub:`A` to PV :sub:`B` with :
    
        PV :sub:`A` = ({1, 0, 0}, {2, 0, 0}, {3, 0, 0});
    
    
        PV :sub:`B` = ({0, 0, 0}, {0, 0, 0}, {0, 0, 0});
    
        The transform to apply then is defined as follows :
    
        .. code-block: java
        
        
         Vector3D translation  = new Vector3D(-1, 0, 0);
         Vector3D velocity     = new Vector3D(-2, 0, 0);
         Vector3D acceleration = new Vector3D(-3, 0, 0);
        
         Transform R1toR2 = new Transform(date, translation, velocity, acceleration);
        
         PVB = R1toR2.transformPVCoordinate(PVA);
         
    
        Example of rotation from R :sub:`A` to R :sub:`B`
    ---------------------------------------------------
    
    
        We want to transform the :class:`~org.orekit.utils.FieldPVCoordinates` PV :sub:`A` to PV :sub:`B` with
    
        PV :sub:`A` = ({1, 0, 0}, { 1, 0, 0});
    
    
        PV :sub:`B` = ({0, 1, 0}, {-2, 1, 0});
    
        The transform to apply then is defined as follows :
    
        .. code-block: java
        
        
         Rotation rotation = new Rotation(Vector3D.PLUS_K, FastMath.PI / 2);
         Vector3D rotationRate = new Vector3D(0, 0, -2);
        
         Transform R1toR2 = new Transform(rotation, rotationRate);
        
         PVB = R1toR2.transformPVCoordinates(PVA);
         
    
        Since:
            9.0
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTransform__T], transform: 'Transform'): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldTransform: 'FieldTransform'[_FieldTransform__T], fieldTransform2: 'FieldTransform'[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldAngularCoordinates: org.orekit.utils.FieldAngularCoordinates[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]): ...
    def freeze(self) -> 'FieldTransform'[_FieldTransform__T]: ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    def getAngular(self) -> org.orekit.utils.FieldAngularCoordinates[_FieldTransform__T]: ...
    def getCartesian(self) -> org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getFieldDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTransform__T]: ...
    _getIdentity__T = typing.TypeVar('_getIdentity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getIdentity(field: org.hipparchus.Field[_getIdentity__T]) -> 'FieldTransform'[_getIdentity__T]:
        """
            Get the identity transform.
        
            Parameters:
                field (Field<T> field): field for the components
        
            Returns:
                identity transform
        
        
        """
        ...
    def getInverse(self) -> 'FieldTransform'[_FieldTransform__T]: ...
    def getJacobian(self, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, tArray: typing.List[typing.List[_FieldTransform__T]]) -> None:
        """
            Compute the Jacobian of the :meth:`~org.orekit.frames.FieldTransform.transformPVCoordinates` method of the transform.
        
            Element :code:`jacobian[i][j]` is the derivative of Cartesian coordinate i of the transformed
            :class:`~org.orekit.utils.FieldPVCoordinates` with respect to Cartesian coordinate j of the input
            :class:`~org.orekit.utils.FieldPVCoordinates` in method
            :meth:`~org.orekit.frames.FieldTransform.transformPVCoordinates`.
        
            This definition implies that if we define position-velocity coordinates :code:`PVÃ¢â€šï¿½ =
            transform.transformPVCoordinates(PVÃ¢â€šâ‚¬)` then their differentials dPVÃ¢â€šï¿½ and dPVÃ¢â€šâ‚¬ will obey the
            following relation where J is the matrix computed by this method: :code:`dPVÃ¢â€šï¿½ = J Ã— dPVÃ¢â€šâ‚¬`
        
            Parameters:
                selector (:class:`~org.orekit.utils.CartesianDerivativesFilter`): selector specifying the size of the upper left corner that must be filled (either 3x3 for positions only, 6x6 for
                    positions and velocities, 9x9 for positions, velocities and accelerations)
                jacobian (:class:`~org.orekit.frames.FieldTransform`[][]):             placeholder matrix whose upper-left corner is to be filled with the Jacobian, the rest of the matrix remaining untouched
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T]: ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_1__T = typing.TypeVar('_interpolate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_2__T = typing.TypeVar('_interpolate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_0__T], collection: typing.Union[java.util.Collection['FieldTransform'[_interpolate_0__T]], typing.Sequence['FieldTransform'[_interpolate_0__T]], typing.Set['FieldTransform'[_interpolate_0__T]]]) -> 'FieldTransform'[_interpolate_0__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_1__T], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, collection: typing.Union[java.util.Collection['FieldTransform'[_interpolate_1__T]], typing.Sequence['FieldTransform'[_interpolate_1__T]], typing.Set['FieldTransform'[_interpolate_1__T]]]) -> 'FieldTransform'[_interpolate_1__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_2__T], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, stream: java.util.stream.Stream['FieldTransform'[_interpolate_2__T]]) -> 'FieldTransform'[_interpolate_2__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldTransform'[_FieldTransform__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldTransform__T) -> 'FieldTransform'[_FieldTransform__T]: ...
    @typing.overload
    def transformLine(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_FieldTransform__T]) -> org.hipparchus.geometry.euclidean.threed.FieldLine[_FieldTransform__T]: ...
    @typing.overload
    def transformLine(self, line: org.hipparchus.geometry.euclidean.threed.Line) -> org.hipparchus.geometry.euclidean.threed.FieldLine[_FieldTransform__T]: ...
    @typing.overload
    def transformPVCoordinates(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]: ...
    @typing.overload
    def transformPVCoordinates(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]: ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTransform__T]) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTransform__T]: ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTransform__T]: ...
    @typing.overload
    def transformPosition(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    @typing.overload
    def transformPosition(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    @typing.overload
    def transformVector(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...
    @typing.overload
    def transformVector(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]: ...

_FieldTransformGenerator__T = typing.TypeVar('_FieldTransformGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTransformGenerator(org.orekit.utils.TimeStampedGenerator[FieldTransform[_FieldTransformGenerator__T]], typing.Generic[_FieldTransformGenerator__T]):
    """
    public class FieldTransformGenerator<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.utils.TimeStampedGenerator`<:class:`~org.orekit.frames.FieldTransform`<T>>
    
        Generator to use field transforms in :class:`~org.orekit.utils.GenericTimeStampedCache`.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.utils.GenericTimeStampedCache`
    """
    def __init__(self, field: org.hipparchus.Field[_FieldTransformGenerator__T], int: int, transformProvider: 'TransformProvider', double: float): ...
    def generate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> java.util.List[FieldTransform[_FieldTransformGenerator__T]]: ...

class Frame(java.io.Serializable):
    """
    public class Frame extends Object implements Serializable
    
        Tridimensional references frames class.
    
        Frame Presentation
    --------------------
    
    
        This class is the base class for all frames in OREKIT. The frames are linked together in a tree with some specific frame
        chosen as the root of the tree. Each frame is defined by :class:`~org.orekit.frames.Transform` combining any number of
        translations and rotations from a reference frame which is its parent frame in the tree structure.
    
        When we say a :class:`~org.orekit.frames.Transform` t is *from frame :sub:`A` to frame :sub:`B`*, we mean that if the
        coordinates of some absolute vector (say the direction of a distant star for example) has coordinates u :sub:`A` in
        frame :sub:`A` and u :sub:`B` in frame :sub:`B` , then u :sub:`B` =:meth:`~org.orekit.frames.Transform.transformVector`.
    
        The transforms may be constant or varying, depending on the implementation of the
        :class:`~org.orekit.frames.TransformProvider` used to define the frame. For simple fixed transforms, using
        :class:`~org.orekit.frames.FixedTransformProvider` is sufficient. For varying transforms (time-dependent or
        telemetry-based for example), it may be useful to define specific implementations of
        :class:`~org.orekit.frames.TransformProvider`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, frame: 'Frame', transform: 'Transform', string: str): ...
    @typing.overload
    def __init__(self, frame: 'Frame', transform: 'Transform', string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, frame: 'Frame', transformProvider: 'TransformProvider', string: str): ...
    @typing.overload
    def __init__(self, frame: 'Frame', transformProvider: 'TransformProvider', string: str, boolean: bool): ...
    def getAncestor(self, int: int) -> 'Frame': ...
    def getDepth(self) -> int:
        """
            Get the depth of the frame.
        
            The depth of a frame is the number of parents frame between it and the frames tree root. It is 0 for the root frame, and
            the depth of a frame is the depth of its parent frame plus one.
        
            Returns:
                depth of the frame
        
        
        """
        ...
    def getFrozenFrame(self, frame: 'Frame', absoluteDate: org.orekit.time.AbsoluteDate, string: str) -> 'Frame':
        """
            Get a new version of the instance, frozen with respect to a reference frame.
        
            Freezing a frame consist in computing its position and orientation with respect to another frame at some freezing date
            and fixing them so they do not depend on time anymore. This means the frozen frame is fixed with respect to the
            reference frame.
        
            One typical use of this method is to compute an inertial launch reference frame by freezing a
            :class:`~org.orekit.frames.TopocentricFrame` at launch date with respect to an inertial frame. Another use is to freeze
            an equinox-related celestial frame at a reference epoch date.
        
            Only the frame returned by this method is frozen, the instance by itself is not affected by calling this method and
            still moves freely.
        
            Parameters:
                reference (:class:`~org.orekit.frames.Frame`): frame with respect to which the instance will be frozen
                freezingDate (:class:`~org.orekit.time.AbsoluteDate`): freezing date
                frozenName (String): name of the frozen frame
        
            Returns:
                a frozen version of the instance
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name.
        
            Returns:
                the name
        
        
        """
        ...
    def getParent(self) -> 'Frame':
        """
            Get the parent frame.
        
            Returns:
                parent frame
        
        
        """
        ...
    @staticmethod
    def getRoot() -> 'Frame':
        """
            Get the unique root frame.
        
            Returns:
                the unique instance of the root frame
        
        
        """
        ...
    def getTransformProvider(self) -> 'TransformProvider':
        """
            Get the provider for transform from parent frame to instance.
        
            Returns:
                provider for transform from parent frame to instance
        
        
        """
        ...
    _getTransformTo_0__T = typing.TypeVar('_getTransformTo_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransformTo(self, frame: 'Frame', fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransformTo_0__T]) -> FieldTransform[_getTransformTo_0__T]:
        """
            Get the transform from the instance to another frame.
        
            Parameters:
                destination (:class:`~org.orekit.frames.Frame`): destination frame to which we want to transform vectors
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): the date (can be null if it is sure than no date dependent frame is used)
        
            Returns:
                transform from the instance to the destination frame
        
        
        """
        ...
    @typing.overload
    def getTransformTo(self, frame: 'Frame', absoluteDate: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
            Get the transform from the instance to another frame.
        
            Parameters:
                destination (:class:`~org.orekit.frames.Frame`): destination frame to which we want to transform vectors
                date (:class:`~org.orekit.time.AbsoluteDate`): the date (can be null if it is sure than no date dependent frame is used)
        
            Returns:
                transform from the instance to the destination frame
        
        """
        ...
    def isChildOf(self, frame: 'Frame') -> bool:
        """
            Determine if a Frame is a child of another one.
        
            Parameters:
                potentialAncestor (:class:`~org.orekit.frames.Frame`): supposed ancestor frame
        
            Returns:
                true if the potentialAncestor belongs to the path from instance to the root frame, excluding itself
        
        
        """
        ...
    def isPseudoInertial(self) -> bool:
        """
            Check if the frame is pseudo-inertial.
        
            Pseudo-inertial frames are frames that do have a linear motion and either do not rotate or rotate at a very low rate
            resulting in neglectible inertial forces. This means they are suitable for orbit definition and propagation using
            Newtonian mechanics. Frames that are *not* pseudo-inertial are *not* suitable for orbit definition and propagation.
        
            Returns:
                true if frame is pseudo-inertial
        
        
        """
        ...
    def toString(self) -> str:
        """
            New definition of the java.util toString() method.
        
            Overrides:
                 in class 
        
            Returns:
                the name
        
        
        """
        ...

class Frames:
    def getCIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getEME2000(self) -> 'FactoryManagedFrame': ...
    def getEOPHistory(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> EOPHistory: ...
    def getEcliptic(self, iERSConventions: org.orekit.utils.IERSConventions) -> Frame: ...
    def getFrame(self, predefined: 'Predefined') -> Frame: ...
    def getGCRF(self) -> Frame: ...
    @typing.overload
    def getGTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getGTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getICRF(self) -> Frame: ...
    @typing.overload
    def getITRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getITRF(self, iTRFVersion: 'ITRFVersion', iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'VersionedITRF': ...
    def getITRFEquinox(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    def getPZ9011(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getTEME(self) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getVeis1950(self) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def of(timeScales: org.orekit.time.TimeScales, supplier: typing.Union[java.util.function.Supplier[Frame], typing.Callable[[], Frame]]) -> 'Frames': ...
    @typing.overload
    @staticmethod
    def of(timeScales: org.orekit.time.TimeScales, celestialBodies: org.orekit.bodies.CelestialBodies) -> 'Frames': ...

class FramesFactory:
    RAPID_DATA_PREDICTION_COLUMNS_1980_FILENAME: typing.ClassVar[str] = ...
    RAPID_DATA_PREDICTION_XML_1980_FILENAME: typing.ClassVar[str] = ...
    EOPC04_1980_FILENAME: typing.ClassVar[str] = ...
    BULLETINB_1980_FILENAME: typing.ClassVar[str] = ...
    RAPID_DATA_PREDICITON_COLUMNS_2000_FILENAME: typing.ClassVar[str] = ...
    RAPID_DATA_PREDICITON_XML_2000_FILENAME: typing.ClassVar[str] = ...
    EOPC04_2000_FILENAME: typing.ClassVar[str] = ...
    BULLETINB_2000_FILENAME: typing.ClassVar[str] = ...
    BULLETINA_FILENAME: typing.ClassVar[str] = ...
    @staticmethod
    def addDefaultEOP1980HistoryLoaders(string: str, string2: str, string3: str, string4: str, string5: str) -> None: ...
    @staticmethod
    def addDefaultEOP2000HistoryLoaders(string: str, string2: str, string3: str, string4: str, string5: str) -> None: ...
    @staticmethod
    def addEOPHistoryLoader(iERSConventions: org.orekit.utils.IERSConventions, eOPHistoryLoader: EOPHistoryLoader) -> None: ...
    @staticmethod
    def clearEOPHistoryLoaders() -> None: ...
    @staticmethod
    def findEOP(frame: Frame) -> EOPHistory: ...
    @staticmethod
    def getCIRF(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getEME2000() -> 'FactoryManagedFrame': ...
    @staticmethod
    def getEOPHistory(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> EOPHistory: ...
    @staticmethod
    def getEcliptic(iERSConventions: org.orekit.utils.IERSConventions) -> Frame: ...
    @staticmethod
    def getFrame(predefined: 'Predefined') -> Frame: ...
    @staticmethod
    def getFrames() -> 'LazyLoadedFrames': ...
    @staticmethod
    def getGCRF() -> Frame: ...
    @typing.overload
    @staticmethod
    def getGTOD(boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getGTOD(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getICRF() -> Frame: ...
    @typing.overload
    @staticmethod
    def getITRF(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getITRF(iTRFVersion: 'ITRFVersion', iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'VersionedITRF': ...
    @staticmethod
    def getITRFEquinox(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getMOD(boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getMOD(iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    _getNonInterpolatingTransform_0__T = typing.TypeVar('_getNonInterpolatingTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getNonInterpolatingTransform(frame: Frame, frame2: Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getNonInterpolatingTransform_0__T]) -> FieldTransform[_getNonInterpolatingTransform_0__T]: ...
    @typing.overload
    @staticmethod
    def getNonInterpolatingTransform(frame: Frame, frame2: Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> 'Transform': ...
    @staticmethod
    def getPZ9011(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getTEME() -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTIRF(iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTIRF(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTOD(boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTOD(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getVeis1950() -> 'FactoryManagedFrame': ...
    @staticmethod
    def setEOPContinuityThreshold(double: float) -> None: ...

class ItrfVersionProvider:
    """
    public interface ItrfVersionProvider
    
        Interface for retrieving the ITRF version for a given set of EOP data.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.frames.ITRFVersionLoader`
    """
    def getConfiguration(self, string: str, int: int) -> 'ITRFVersionLoader.ITRFVersionConfiguration':
        """
            Get the ITRF version configuration defined by a given file at specified date.
        
            Parameters:
                name (String): EOP file name
                mjd (int): date of the EOP in modified Julian day
        
            Returns:
                configuration valid around specified date in the file
        
        
        """
        ...

class LOFType(java.lang.Enum['LOFType']):
    """
    public enum LOFType extends Enum<:class:`~org.orekit.frames.LOFType`>
    
        Enumerate for different types of Local Orbital Frames.
    """
    TNW: typing.ClassVar['LOFType'] = ...
    QSW: typing.ClassVar['LOFType'] = ...
    LVLH: typing.ClassVar['LOFType'] = ...
    LVLH_CCSDS: typing.ClassVar['LOFType'] = ...
    VVLH: typing.ClassVar['LOFType'] = ...
    VNC: typing.ClassVar['LOFType'] = ...
    EQW: typing.ClassVar['LOFType'] = ...
    NTW: typing.ClassVar['LOFType'] = ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]: ...
    @typing.overload
    def rotationFromInertial(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Get the rotation from inertial frame to local orbital frame.
        
            This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well,
            the full :meth:`~org.orekit.frames.LOFType.transformFromInertial` method must be called and the complete rotation
            transform must be extracted from it.
        
            Parameters:
                pv (:class:`~org.orekit.utils.PVCoordinates`): position-velocity of the spacecraft in some inertial frame
        
            Returns:
                rotation from inertial frame to local orbital frame
        
        public abstract <T extends CalculusFieldElement<T>> FieldRotation<T> rotationFromInertial(Field<T> field, :class:`~org.orekit.utils.FieldPVCoordinates`<T> pv)
        
            Get the rotation from inertial frame to local orbital frame.
        
            This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well,
            the full :meth:`~org.orekit.frames.LOFType.transformFromInertial` method must be called and the complete rotation
            transform must be extracted from it.
        
            Parameters:
                field (Field<T> field): field to which the elements belong
                pv (:class:`~org.orekit.utils.FieldPVCoordinates`<T> pv): position-velocity of the spacecraft in some inertial frame
        
            Returns:
                rotation from inertial frame to local orbital frame
        
            Since:
                9.0
        
        
        """
        ...
    _transformFromInertial_0__T = typing.TypeVar('_transformFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformFromInertial(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transformFromInertial_0__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_transformFromInertial_0__T]) -> FieldTransform[_transformFromInertial_0__T]:
        """
            Get the transform from an inertial frame defining position-velocity and the local orbital frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                pv (:class:`~org.orekit.utils.FieldPVCoordinates`<T> pv): position-velocity of the spacecraft in some inertial frame
        
            Returns:
                transform from the frame where position-velocity are defined to local orbital frame
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def transformFromInertial(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates) -> 'Transform':
        """
            Get the transform from an inertial frame defining position-velocity and the local orbital frame.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                pv (:class:`~org.orekit.utils.PVCoordinates`): position-velocity of the spacecraft in some inertial frame
        
            Returns:
                transform from the frame where position-velocity are defined to local orbital frame
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LOFType':
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
    def values() -> typing.List['LOFType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (LOFType c : LOFType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LazyLoadedEop:
    """
    public class LazyLoadedEop extends Object
    
        Loads Earth Orientation Parameters (EOP) from a configured set of :class:`~org.orekit.frames.EOPHistoryLoader`s on
        demand. Methods are synchronized so it is safe for access from multiple threads.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.frames.LazyLoadedFrames`, :class:`~org.orekit.frames.FramesFactory`
    """
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def addDefaultEOP1980HistoryLoaders(self, string: str, string2: str, string3: str, string4: str, string5: str, supplier: typing.Union[java.util.function.Supplier[org.orekit.time.TimeScale], typing.Callable[[], org.orekit.time.TimeScale]]) -> None: ...
    def addDefaultEOP2000HistoryLoaders(self, string: str, string2: str, string3: str, string4: str, string5: str, supplier: typing.Union[java.util.function.Supplier[org.orekit.time.TimeScale], typing.Callable[[], org.orekit.time.TimeScale]]) -> None: ...
    def addEOPHistoryLoader(self, iERSConventions: org.orekit.utils.IERSConventions, eOPHistoryLoader: EOPHistoryLoader) -> None:
        """
            Add a loader for Earth Orientation Parameters history.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions to which EOP history applies
                loader (:class:`~org.orekit.frames.EOPHistoryLoader`): custom loader to add for the EOP history
        
            Also see:
                :meth:`~org.orekit.frames.LazyLoadedEop.addDefaultEOP1980HistoryLoaders`,
                :meth:`~org.orekit.frames.LazyLoadedEop.clearEOPHistoryLoaders`
        
        
        """
        ...
    def clearEOPHistoryLoaders(self) -> None:
        """
            Clear loaders for Earth Orientation Parameters history.
        
            Also see:
                :meth:`~org.orekit.frames.LazyLoadedEop.addEOPHistoryLoader`,
                :meth:`~org.orekit.frames.LazyLoadedEop.addDefaultEOP1980HistoryLoaders`
        
        
        """
        ...
    def getDataProvidersManager(self) -> org.orekit.data.DataProvidersManager:
        """
            Get the data providers manager for this instance.
        
            Returns:
                the provider of EOP data files.
        
        
        """
        ...
    def getEOPHistory(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool, timeScales: org.orekit.time.TimeScales) -> EOPHistory:
        """
            Get Earth Orientation Parameters history.
        
            If no :class:`~org.orekit.frames.EOPHistoryLoader` has been added by calling
            :meth:`~org.orekit.frames.LazyLoadedEop.addEOPHistoryLoader` or if
            :meth:`~org.orekit.frames.LazyLoadedEop.clearEOPHistoryLoaders` has been called afterwards, the
            :meth:`~org.orekit.frames.LazyLoadedEop.addDefaultEOP1980HistoryLoaders` and
            :meth:`~org.orekit.frames.LazyLoadedEop.addDefaultEOP2000HistoryLoaders` methods will be called automatically with
            supported file names parameters all set to null, in order to get the default loaders configuration.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): conventions for which EOP history is requested
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
                timeScales (:class:`~org.orekit.time.TimeScales`): to use when loading EOP and computing corrections.
        
            Returns:
                Earth Orientation Parameters history
        
        
        """
        ...
    def setEOPContinuityThreshold(self, double: float) -> None:
        """
            Set the threshold to check EOP continuity.
        
            The default threshold (used if this method is never called) is 5 Julian days. If after loading EOP entries some holes
            between entries exceed this threshold, an exception will be triggered.
        
            One case when calling this method is really useful is for applications that use a single Bulletin A, as these bulletins
            have a roughly one month wide hole for the first bulletin of each month, which contains older final data in addition to
            the rapid data and the predicted data.
        
            Parameters:
                threshold (double): threshold to use for checking EOP continuity (in seconds)
        
        
        """
        ...

class OrphanFrame(java.io.Serializable):
    """
    public class OrphanFrame extends Object implements Serializable
    
        Prototype frame that can be built from leaf to roots and later attached to a tree.
    
        Regular :class:`~org.orekit.frames.Frame` instances can be built only from a parent frame, i.e. the frames tree can be
        built only from root to leafs. In some cases, it may desirable to build a subset tree and attach it to the main tree
        after build time, which means the tree is built from leafs to root. This class allows building this subtree.
    
        During the build process, the :class:`~org.orekit.frames.Frame` associated with each
        :class:`~org.orekit.frames.OrphanFrame` is not available. It becomes available only once the
        :class:`~org.orekit.frames.OrphanFrame` has been attached to the main tree, and at this time it can be used to compute
        :class:`~org.orekit.frames.Transform`.
    
        Since:
            6.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    @typing.overload
    def addChild(self, orphanFrame: 'OrphanFrame', transform: 'Transform', boolean: bool) -> None:
        """
            Add a child.
        
            If a child is added after the instance has been attached, the child and all its tree will be attached immediately too.
        
            Parameters:
                child (:class:`~org.orekit.frames.OrphanFrame`): child to add
                transform (:class:`~org.orekit.frames.Transform`): transform from instance to child
                isPseudoInertial (boolean): true if child is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
            Add a child.
        
            If a child is added after the instance has been attached, the child and all its tree will be attached immediately too.
        
            Parameters:
                child (:class:`~org.orekit.frames.OrphanFrame`): child to add
                transformProvider (:class:`~org.orekit.frames.TransformProvider`): provider for transform from instance to child
                isPseudoInertial (boolean): true if child is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
        
        """
        ...
    @typing.overload
    def addChild(self, orphanFrame: 'OrphanFrame', transformProvider: 'TransformProvider', boolean: bool) -> None: ...
    @typing.overload
    def attachTo(self, frame: Frame, transform: 'Transform', boolean: bool) -> None:
        """
            Attach the instance (and all its children down to leafs) to the main tree.
        
            Parameters:
                parent (:class:`~org.orekit.frames.Frame`): parent frame to attach to
                transform (:class:`~org.orekit.frames.Transform`): transform from parent frame to instance
                isPseudoInertial (boolean): true if frame is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
            Attach the instance (and all its children down to leafs) to the main tree.
        
            Parameters:
                parent (:class:`~org.orekit.frames.Frame`): parent frame to attach to
                transformProvider (:class:`~org.orekit.frames.TransformProvider`): provider for transform from parent frame to instance
                isPseudoInertial (boolean): true if frame is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
        
        """
        ...
    @typing.overload
    def attachTo(self, frame: Frame, transformProvider: 'TransformProvider', boolean: bool) -> None: ...
    def getChildren(self) -> java.util.List['OrphanFrame']: ...
    def getFrame(self) -> Frame:
        """
            Get the associated :class:`~org.orekit.frames.Frame`.
        
            Returns:
                associated frame
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class PoleCorrection(java.io.Serializable):
    """
    public class PoleCorrection extends Object implements Serializable
    
        Simple container class for pole correction parameters.
    
        This class is a simple container, it does not provide any processing method.
    
        Also see:
            :meth:`~serialized`
    """
    NULL_CORRECTION: typing.ClassVar['PoleCorrection'] = ...
    """
    public static final :class:`~org.orekit.frames.PoleCorrection` NULL_CORRECTION
    
        Null correction (xp = 0, yp = 0).
    
    """
    def __init__(self, double: float, double2: float): ...
    def getXp(self) -> float:
        """
            Get the x :sub:`p` parameter.
        
            Returns:
                x :sub:`p` parameter
        
        
        """
        ...
    def getYp(self) -> float:
        """
            Get the y :sub:`p` parameter.
        
            Returns:
                y :sub:`p` parameter
        
        
        """
        ...

class Predefined(java.lang.Enum['Predefined']):
    """
    public enum Predefined extends Enum<:class:`~org.orekit.frames.Predefined`>
    
        Predefined frames provided by :class:`~org.orekit.frames.Frames`.
    """
    GCRF: typing.ClassVar['Predefined'] = ...
    ICRF: typing.ClassVar['Predefined'] = ...
    ECLIPTIC_CONVENTIONS_1996: typing.ClassVar['Predefined'] = ...
    ECLIPTIC_CONVENTIONS_2003: typing.ClassVar['Predefined'] = ...
    ECLIPTIC_CONVENTIONS_2010: typing.ClassVar['Predefined'] = ...
    EME2000: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    VEIS_1950: typing.ClassVar['Predefined'] = ...
    GTOD_WITHOUT_EOP_CORRECTIONS: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_WITHOUT_EOP_CORRECTIONS: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    MOD_WITHOUT_EOP_CORRECTIONS: typing.ClassVar['Predefined'] = ...
    MOD_CONVENTIONS_2010: typing.ClassVar['Predefined'] = ...
    MOD_CONVENTIONS_2003: typing.ClassVar['Predefined'] = ...
    MOD_CONVENTIONS_1996: typing.ClassVar['Predefined'] = ...
    TEME: typing.ClassVar['Predefined'] = ...
    PZ90_11: typing.ClassVar['Predefined'] = ...
    def getName(self) -> str:
        """
            Get the name of the frame.
        
            Returns:
                name of the frame
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Predefined':
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
    def values() -> typing.List['Predefined']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (Predefined c : Predefined.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Transform(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['Transform'], org.orekit.time.TimeInterpolable['Transform'], java.io.Serializable):
    """
    public class Transform extends Object implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.frames.Transform`>, :class:`~org.orekit.time.TimeInterpolable`<:class:`~org.orekit.frames.Transform`>, Serializable
    
        Transformation class in three dimensional space.
    
        This class represents the transformation engine between :class:`~org.orekit.frames.Frame`. It is used both to define the
        relationship between each frame and its parent frame and to gather all individual transforms into one operation when
        converting between frames far away from each other.
    
        The convention used in OREKIT is vectorial transformation. It means that a transformation is defined as a transform to
        apply to the coordinates of a vector expressed in the old frame to obtain the same vector expressed in the new frame.
    
        Instances of this class are guaranteed to be immutable.
    
        Examples
    ----------
    
    
        Example of translation from R :sub:`A` to R :sub:`B`
    ------------------------------------------------------
    
    
        We want to transform the :class:`~org.orekit.utils.PVCoordinates` PV :sub:`A` to PV :sub:`B` with :
    
        PV :sub:`A` = ({1, 0, 0}, {2, 0, 0}, {3, 0, 0});
    
    
        PV :sub:`B` = ({0, 0, 0}, {0, 0, 0}, {0, 0, 0});
    
        The transform to apply then is defined as follows :
    
        .. code-block: java
        
        
         Vector3D translation  = new Vector3D(-1, 0, 0);
         Vector3D velocity     = new Vector3D(-2, 0, 0);
         Vector3D acceleration = new Vector3D(-3, 0, 0);
        
         Transform R1toR2 = new Transform(date, translation, velocity, acceleration);
        
         PVB = R1toR2.transformPVCoordinates(PVA);
         
    
        Example of rotation from R :sub:`A` to R :sub:`B`
    ---------------------------------------------------
    
    
        We want to transform the :class:`~org.orekit.utils.PVCoordinates` PV :sub:`A` to PV :sub:`B` with
    
        PV :sub:`A` = ({1, 0, 0}, { 1, 0, 0});
    
    
        PV :sub:`B` = ({0, 1, 0}, {-2, 1, 0});
    
        The transform to apply then is defined as follows :
    
        .. code-block: java
        
        
         Rotation rotation = new Rotation(Vector3D.PLUS_K, FastMath.PI / 2);
         Vector3D rotationRate = new Vector3D(0, 0, -2);
        
         Transform R1toR2 = new Transform(rotation, rotationRate);
        
         PVB = R1toR2.transformPVCoordinates(PVA);
         
    
        Also see:
            :meth:`~serialized`
    """
    IDENTITY: typing.ClassVar['Transform'] = ...
    """
    public static final :class:`~org.orekit.frames.Transform` IDENTITY
    
        Identity transform.
    
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, transform: 'Transform', transform2: 'Transform'): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, angularCoordinates: org.orekit.utils.AngularCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates): ...
    def freeze(self) -> 'Transform':
        """
            Get a frozen transform.
        
            This method creates a copy of the instance but frozen in time, i.e. with velocity, acceleration and rotation rate forced
            to zero.
        
            Returns:
                a new transform, without any time-dependent parts
        
        
        """
        ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the second time derivative of the translation.
        
            Returns:
                second time derivative of the translation
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getCartesian`, :meth:`~org.orekit.frames.Transform.getTranslation`,
                :meth:`~org.orekit.frames.Transform.getVelocity`
        
        
        """
        ...
    def getAngular(self) -> org.orekit.utils.AngularCoordinates:
        """
            Get the underlying elementary angular part.
        
            A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method
            returns this unique elementary rotation with its derivative.
        
            Returns:
                underlying elementary angular part
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getRotation`, :meth:`~org.orekit.frames.Transform.getRotationRate`,
                :meth:`~org.orekit.frames.Transform.getRotationAcceleration`
        
        
        """
        ...
    def getCartesian(self) -> org.orekit.utils.PVCoordinates:
        """
            Get the underlying elementary Cartesian part.
        
            A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method
            returns this unique elementary translation with its derivative.
        
            Returns:
                underlying elementary Cartesian part
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getTranslation`, :meth:`~org.orekit.frames.Transform.getVelocity`
        
        
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
    def getInverse(self) -> 'Transform':
        """
            Get the inverse transform of the instance.
        
            Returns:
                inverse transform of the instance
        
        
        """
        ...
    def getJacobian(self, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Compute the Jacobian of the :meth:`~org.orekit.frames.Transform.transformPVCoordinates` method of the transform.
        
            Element :code:`jacobian[i][j]` is the derivative of Cartesian coordinate i of the transformed
            :class:`~org.orekit.utils.PVCoordinates` with respect to Cartesian coordinate j of the input
            :class:`~org.orekit.utils.PVCoordinates` in method :meth:`~org.orekit.frames.Transform.transformPVCoordinates`.
        
            This definition implies that if we define position-velocity coordinates
        
            .. code-block: java
            
            
             PVâ‚� = transform.transformPVCoordinates(PVâ‚€), then
             
        
            their differentials dPVâ‚� and dPVâ‚€ will obey the following relation where J is the matrix computed by this method:
        
            .. code-block: java
            
            
             dPVâ‚� = J × dPVâ‚€
             
        
            Parameters:
                selector (:class:`~org.orekit.utils.CartesianDerivativesFilter`): selector specifying the size of the upper left corner that must be filled (either 3x3 for positions only, 6x6 for
                    positions and velocities, 9x9 for positions, velocities and accelerations)
                jacobian (double[][]):             placeholder matrix whose upper-left corner is to be filled with the Jacobian, the rest of the matrix remaining untouched
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Get the underlying elementary rotation.
        
            A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method
            returns this unique elementary rotation.
        
            Returns:
                underlying elementary rotation
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getAngular`, :meth:`~org.orekit.frames.Transform.getRotationRate`,
                :meth:`~org.orekit.frames.Transform.getRotationAcceleration`
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the second time derivative of the rotation.
        
            Returns:
                Second time derivative of the rotation
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getAngular`, :meth:`~org.orekit.frames.Transform.getRotation`,
                :meth:`~org.orekit.frames.Transform.getRotationRate`
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the first time derivative of the rotation.
        
            The norm represents the angular rate.
        
            Returns:
                First time derivative of the rotation
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getAngular`, :meth:`~org.orekit.frames.Transform.getRotation`,
                :meth:`~org.orekit.frames.Transform.getRotationAcceleration`
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the underlying elementary translation.
        
            A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method
            returns this unique elementary translation.
        
            Returns:
                underlying elementary translation
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getCartesian`, :meth:`~org.orekit.frames.Transform.getVelocity`,
                :meth:`~org.orekit.frames.Transform.getAcceleration`
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the first time derivative of the translation.
        
            Returns:
                first time derivative of the translation
        
            Also see:
                :meth:`~org.orekit.frames.Transform.getCartesian`, :meth:`~org.orekit.frames.Transform.getTranslation`,
                :meth:`~org.orekit.frames.Transform.getAcceleration`
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream['Transform']) -> 'Transform': ...
    @typing.overload
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, collection: typing.Union[java.util.Collection['Transform'], typing.Sequence['Transform'], typing.Set['Transform']]) -> 'Transform': ...
    def shiftedBy(self, double: float) -> 'Transform':
        """
            Get a time-shifted instance.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    def transformLine(self, line: org.hipparchus.geometry.euclidean.threed.Line) -> org.hipparchus.geometry.euclidean.threed.Line:
        """
            Transform a line.
        
            Parameters:
                line (Line): to transform
        
            Returns:
                transformed line
        
        
        """
        ...
    _transformPVCoordinates_0__T = typing.TypeVar('_transformPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transformPVCoordinates_2__T = typing.TypeVar('_transformPVCoordinates_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformPVCoordinates(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_transformPVCoordinates_0__T]) -> org.orekit.utils.FieldPVCoordinates[_transformPVCoordinates_0__T]:
        """
            Transform :class:`~org.orekit.utils.FieldPVCoordinates` including kinematic effects.
        
            Parameters:
                pv (:class:`~org.orekit.utils.FieldPVCoordinates`<T> pv): position-velocity to transform.
        
            Returns:
                transformed position-velocity
        
            Transform :class:`~org.orekit.utils.TimeStampedFieldPVCoordinates` including kinematic effects.
        
            In order to allow the user more flexibility, this method does *not* check for consistency between the transform
            :meth:`~org.orekit.frames.Transform.getDate` and the time-stamped position-velocity
            :meth:`~org.orekit.utils.TimeStampedFieldPVCoordinates.getDate`. The returned value will always have the same
            :meth:`~org.orekit.utils.TimeStampedFieldPVCoordinates.getDate` as the input argument, regardless of the instance
            :meth:`~org.orekit.frames.Transform.getDate`.
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedFieldPVCoordinates`<T> pv): time-stamped position-velocity to transform.
        
            Returns:
                transformed time-stamped position-velocity
        
            Since:
                7.0
        
        
        """
        ...
    @typing.overload
    def transformPVCoordinates(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.orekit.utils.PVCoordinates:
        """
            Transform :class:`~org.orekit.utils.PVCoordinates` including kinematic effects.
        
            Parameters:
                pva (:class:`~org.orekit.utils.PVCoordinates`): the position-velocity-acceleration triplet to transform.
        
            Returns:
                transformed position-velocity-acceleration
        
            Transform :class:`~org.orekit.utils.TimeStampedPVCoordinates` including kinematic effects.
        
            In order to allow the user more flexibility, this method does *not* check for consistency between the transform
            :meth:`~org.orekit.frames.Transform.getDate` and the time-stamped position-velocity
            :meth:`~org.orekit.utils.TimeStampedPVCoordinates.getDate`. The returned value will always have the same
            :meth:`~org.orekit.utils.TimeStampedPVCoordinates.getDate` as the input argument, regardless of the instance
            :meth:`~org.orekit.frames.Transform.getDate`.
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): time-stamped position-velocity to transform.
        
            Returns:
                transformed time-stamped position-velocity
        
            Since:
                7.0
        
        """
        ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_transformPVCoordinates_2__T]) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_transformPVCoordinates_2__T]: ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    _transformPosition_0__T = typing.TypeVar('_transformPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformPosition(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformPosition_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformPosition_0__T]:
        """
            Transform a position vector (including translation effects).
        
            Parameters:
                position (FieldVector3D<T> position): vector to transform
        
            Returns:
                transformed position
        
        
        """
        ...
    @typing.overload
    def transformPosition(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a position vector (including translation effects).
        
            Parameters:
                position (Vector3D): vector to transform
        
            Returns:
                transformed position
        
        """
        ...
    _transformVector_0__T = typing.TypeVar('_transformVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformVector(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformVector_0__T]:
        """
            Transform a vector (ignoring translation effects).
        
            Parameters:
                vector (FieldVector3D<T> vector): vector to transform
        
            Returns:
                transformed vector
        
        
        """
        ...
    @typing.overload
    def transformVector(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a vector (ignoring translation effects).
        
            Parameters:
                vector (Vector3D): vector to transform
        
            Returns:
                transformed vector
        
        """
        ...

class TransformGenerator(org.orekit.utils.TimeStampedGenerator[Transform]):
    """
    public class TransformGenerator extends Object implements :class:`~org.orekit.utils.TimeStampedGenerator`<:class:`~org.orekit.frames.Transform`>
    
        Generator to use transforms in :class:`~org.orekit.utils.GenericTimeStampedCache`.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.utils.GenericTimeStampedCache`
    """
    def __init__(self, int: int, transformProvider: 'TransformProvider', double: float): ...
    def generate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> java.util.List[Transform]: ...

class TransformProvider(java.io.Serializable):
    """
    public interface TransformProvider extends Serializable
    
        Interface for Transform providers.
    
        The transform provider interface is mainly used to define the transform between a frame and its parent frame.
    """
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

class TransformProviderUtils:
    """
    public class TransformProviderUtils extends Object
    
        Utility for Transform providers.
    
        Since:
            9.2
    """
    IDENTITY_PROVIDER: typing.ClassVar[TransformProvider] = ...
    """
    public static final :class:`~org.orekit.frames.TransformProvider` IDENTITY_PROVIDER
    
        Identity provider.
    
        The transforms generated by this providers are always :meth:`~org.orekit.frames.Transform.IDENTITY`.
    
    """
    @staticmethod
    def getCombinedProvider(transformProvider: TransformProvider, transformProvider2: TransformProvider) -> TransformProvider:
        """
            Combine two transform providers.
        
            Parameters:
                first (:class:`~org.orekit.frames.TransformProvider`): first provider to apply
                second (:class:`~org.orekit.frames.TransformProvider`): second provider to apply
        
            Returns:
                a new provider which provide a transform similar to :code:`new Transform(date, first.getTransform(date),
                second.getTransform(date))`
        
        
        """
        ...
    @staticmethod
    def getReversedProvider(transformProvider: TransformProvider) -> TransformProvider:
        """
            Reverse a transform provider.
        
            Parameters:
                provider (:class:`~org.orekit.frames.TransformProvider`): provider to reverse
        
            Returns:
                a new provider which provide a transform similar to :code:`provider.getTransform(date).getInverse()`
        
        
        """
        ...

class AbstractFrames(Frames):
    def __init__(self, timeScales: org.orekit.time.TimeScales, supplier: typing.Union[java.util.function.Supplier[Frame], typing.Callable[[], Frame]]): ...
    def getCIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getEME2000(self) -> 'FactoryManagedFrame': ...
    def getEcliptic(self, iERSConventions: org.orekit.utils.IERSConventions) -> Frame: ...
    def getFrame(self, predefined: Predefined) -> Frame: ...
    def getGCRF(self) -> Frame: ...
    @typing.overload
    def getGTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getGTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getICRF(self) -> Frame: ...
    @typing.overload
    def getITRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getITRF(self, iTRFVersion: 'ITRFVersion', iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'VersionedITRF': ...
    def getITRFEquinox(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    def getPZ9011(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getTEME(self) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getVeis1950(self) -> 'FactoryManagedFrame': ...

class CR3BPRotatingFrame(Frame):
    """
    public class CR3BPRotatingFrame extends :class:`~org.orekit.frames.Frame`
    
        Class creating the rotating frame centered on the barycenter of the CR3BP System.
    
        Since:
            10.2
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, celestialBody: org.orekit.bodies.CelestialBody, celestialBody2: org.orekit.bodies.CelestialBody): ...

class EOPBasedTransformProvider(TransformProvider):
    """
    public interface EOPBasedTransformProvider extends :class:`~org.orekit.frames.TransformProvider`
    
        Interface for Transform providers that use :class:`~org.orekit.frames.EOPHistory`.
    
        Since:
            7.1
    """
    def getEOPHistory(self) -> EOPHistory:
        """
            Get the EOP history.
        
            Returns:
                EOP history
        
        
        """
        ...
    def getNonInterpolatingProvider(self) -> 'EOPBasedTransformProvider':
        """
            Get a version of the provider that does *not* cache tidal corrections.
        
            This method removes the performance enhancing interpolation features that are used by default in EOP-based provider, in
            order to focus on accuracy. The interpolation features are intended to save processing time by avoiding doing tidal
            correction evaluation at each time step and caching some results. This method can be used to avoid this (it is
            automatically called by :meth:`~org.orekit.frames.FramesFactory.getNonInterpolatingTransform`, when very high accuracy
            is desired, or for testing purposes. It should be used with care, as doing the full computation is *really* costly.
        
            Returns:
                version of the provider that does *not* cache tidal corrections
        
            Also see:
                :meth:`~org.orekit.frames.FramesFactory.getNonInterpolatingTransform`
        
        
        """
        ...

class EclipticProvider(TransformProvider):
    """
    public class EclipticProvider extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
        An inertial frame aligned with the ecliptic.
    
        The IAU defines the ecliptic as "the plane perpendicular to the mean heliocentric orbital angular momentum vector of the
        Earth-Moon barycentre in the BCRS (IAU 2006 Resolution B1)." The +z axis is aligned with the angular momentum vector,
        and the +x axis is aligned with +x axis of :meth:`~org.orekit.frames.Frames.getMOD`.
    
        This implementation agrees with the JPL 406 ephemerides to within 0.5 arc seconds.
    
        Since:
            7.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScales: org.orekit.time.TimeScales): ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Description copied from interface: :meth:`~org.orekit.frames.TransformProvider.getTransform`
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Description copied from interface: :meth:`~org.orekit.frames.TransformProvider.getTransform`
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

class FactoryManagedFrame(Frame):
    """
    public class FactoryManagedFrame extends :class:`~org.orekit.frames.Frame`
    
        Base class for the predefined frames that are managed by :class:`~org.orekit.frames.Frames`.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, frame: Frame, transformProvider: TransformProvider, boolean: bool, predefined: Predefined): ...
    def getFactoryKey(self) -> Predefined:
        """
            Get the key of the frame within the factory.
        
            Returns:
                key of the frame within the factory
        
        
        """
        ...

class FixedTransformProvider(TransformProvider):
    """
    public class FixedTransformProvider extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
        Transform provider using fixed transform.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, transform: Transform): ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

class HelmertTransformation(TransformProvider):
    """
    public class HelmertTransformation extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
        Transformation class for geodetic systems.
    
        The Helmert transformation is mainly used to convert between various realizations of geodetic frames, for example in the
        ITRF family.
    
        The original Helmert transformation is a 14 parameters transform that includes translation, velocity, rotation, rotation
        rate and scale factor. The scale factor is useful for coordinates near Earth surface, but it cannot be extended to outer
        space as it would correspond to a non-unitary transform. Therefore, the scale factor is *not* used here.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            5.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float): ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference epoch of the transform.
        
            Returns:
                reference epoch of the transform
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...
    class Predefined(java.lang.Enum['HelmertTransformation.Predefined']):
        ITRF_2014_TO_ITRF_2008: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_2005: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_2000: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1997: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1996: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1994: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1993: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1992: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1991: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1990: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1989: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1988: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_2005: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_2000: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1997: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1996: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1994: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1993: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1992: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1991: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1990: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1989: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1988: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        @typing.overload
        def createTransformedITRF(self, frame: Frame, string: str) -> Frame: ...
        @typing.overload
        def createTransformedITRF(self, frame: Frame, string: str, timeScale: org.orekit.time.TimeScale) -> Frame: ...
        def getDestination(self) -> 'ITRFVersion': ...
        def getOrigin(self) -> 'ITRFVersion': ...
        @typing.overload
        def getTransformation(self) -> 'HelmertTransformation': ...
        @typing.overload
        def getTransformation(self, timeScale: org.orekit.time.TimeScale) -> 'HelmertTransformation': ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'HelmertTransformation.Predefined': ...
        @staticmethod
        def values() -> typing.List['HelmertTransformation.Predefined']: ...

class ITRFVersion(java.lang.Enum['ITRFVersion']):
    """
    public enum ITRFVersion extends Enum<:class:`~org.orekit.frames.ITRFVersion`>
    
        Enumerate for ITRF versions.
    
        Since:
            9.2
    
        Also see:
            :class:`~org.orekit.frames.EOPEntry`, :class:`~org.orekit.frames.HelmertTransformation`
    """
    ITRF_2014: typing.ClassVar['ITRFVersion'] = ...
    ITRF_2008: typing.ClassVar['ITRFVersion'] = ...
    ITRF_2005: typing.ClassVar['ITRFVersion'] = ...
    ITRF_2000: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1997: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1996: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1994: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1993: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1992: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1991: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1990: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1989: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1988: typing.ClassVar['ITRFVersion'] = ...
    @typing.overload
    @staticmethod
    def getConverter(iTRFVersion: 'ITRFVersion', iTRFVersion2: 'ITRFVersion') -> 'ITRFVersion.Converter':
        """
            Find a converter between specified ITRF frames.
        
            Parameters:
                origin (:class:`~org.orekit.frames.ITRFVersion`): origin ITRF
                destination (:class:`~org.orekit.frames.ITRFVersion`): destination ITRF
                tt (:class:`~org.orekit.time.TimeScale`): TT time scale.
        
            Returns:
                transform from :code:`origin` to :code:`destination`
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getConverter(iTRFVersion: 'ITRFVersion', iTRFVersion2: 'ITRFVersion', timeScale: org.orekit.time.TimeScale) -> 'ITRFVersion.Converter': ...
    @typing.overload
    @staticmethod
    def getITRFVersion(int: int) -> 'ITRFVersion':
        """
            Find an ITRF version from its reference year.
        
            Parameters:
                year (int): reference year of the frame version
        
            Returns:
                ITRF version for specified year
        
            Find an ITRF version from its name.
        
            Parameters:
                name (String): name of the frame version (case is ignored)
        
            Returns:
                ITRF version
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getITRFVersion(string: str) -> 'ITRFVersion': ...
    def getName(self) -> str:
        """
            Get the name the frame version.
        
            Returns:
                name of the frame version
        
        
        """
        ...
    def getYear(self) -> int:
        """
            Get the reference year of the frame version.
        
            Returns:
                reference year of the frame version
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ITRFVersion':
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
    def values() -> typing.List['ITRFVersion']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (ITRFVersion c : ITRFVersion.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...
    class Converter(TransformProvider):
        def getDestination(self) -> 'ITRFVersion': ...
        def getOrigin(self) -> 'ITRFVersion': ...
        _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        @typing.overload
        def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]: ...
        @typing.overload
        def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform: ...

class ITRFVersionLoader(ItrfVersionProvider):
    """
    public class ITRFVersionLoader extends Object implements :class:`~org.orekit.frames.ItrfVersionProvider`
    
        Loader for ITRF version configuration file.
    
        The ITRF version configuration file specifies the :class:`~org.orekit.frames.ITRFVersion` that each type of Earth
        Orientation Parameter file contains for each date. This configuration file is used to interpret :code:`EOP C04` files,
        :code:`Bulletin A` files, :code:`Bulletin B` files, :code:`rapid data and prediction files in columns format` files,
        :code:`rapid data and prediction files in XML format` files...
    
        This file is an Orekit-specific configuration file.
    
        This class is immutable and hence thread-safe
    
        Since:
            9.2
    
        Also see:
            :code:`EOPC04FilesLoader`, :code:`BulletinAFilesLoader`, :code:`BulletinBFilesLoader`,
            :code:`RapidDataAndPredictionColumnsLoader`, :code:`RapidDataAndPredictionXMLLoader`
    """
    SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String SUPPORTED_NAMES
    
        Regular expression for supported files names.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getConfiguration(self, string: str, int: int) -> 'ITRFVersionLoader.ITRFVersionConfiguration':
        """
            Description copied from interface: :meth:`~org.orekit.frames.ItrfVersionProvider.getConfiguration`
            Get the ITRF version configuration defined by a given file at specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.ItrfVersionProvider.getConfiguration`Â in
                interfaceÂ :class:`~org.orekit.frames.ItrfVersionProvider`
        
            Parameters:
                name (String): EOP file name
                mjd (int): date of the EOP in modified Julian day
        
            Returns:
                configuration valid around specified date in the file
        
        
        """
        ...
    class ITRFVersionConfiguration:
        def __init__(self, string: str, iTRFVersion: ITRFVersion, int: int, int2: int): ...
        def appliesTo(self, string: str) -> bool: ...
        def getVersion(self) -> ITRFVersion: ...
        def isValid(self, int: int) -> bool: ...

class InterpolatingTransformProvider(TransformProvider):
    """
    public class InterpolatingTransformProvider extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
        Transform provider using thread-safe interpolation on transforms sample.
    
        The interpolation is a polynomial Hermite interpolation, which can either use or ignore the derivatives provided by the
        raw provider. This means that simple raw providers that do not compute derivatives can be used, the derivatives will be
        added appropriately by the interpolation process.
    
        Also see:
            :class:`~org.orekit.utils.GenericTimeStampedCache`, :class:`~org.orekit.frames.ShiftingTransformProvider`,
            :meth:`~serialized`
    """
    def __init__(self, transformProvider: TransformProvider, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, int: int, double: float, int2: int, double2: float, double3: float): ...
    def getGridPoints(self) -> int:
        """
            Get the number of interpolation grid points.
        
            Returns:
                number of interpolation grid points
        
        
        """
        ...
    def getRawProvider(self) -> TransformProvider:
        """
            Get the underlying provider for raw (non-interpolated) transforms.
        
            Returns:
                provider for raw (non-interpolated) transforms
        
        
        """
        ...
    def getStep(self) -> float:
        """
            Get the grid points time step.
        
            Returns:
                grid points time step
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

class L1Frame(Frame):
    """
    public class L1Frame extends :class:`~org.orekit.frames.Frame`
    
        Class to create a L1 centered frame with :class:`~org.orekit.frames.L1TransformProvider`. Parent frame is always set as
        primaryBody.getInertiallyOrientedFrame()
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody, celestialBody2: org.orekit.bodies.CelestialBody): ...

class L1TransformProvider(TransformProvider):
    """
    public class L1TransformProvider extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
        L1 Transform provider for a frame on the L1 Lagrange point of two celestial bodies.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody, celestialBody2: org.orekit.bodies.CelestialBody): ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

class L2Frame(Frame):
    """
    public class L2Frame extends :class:`~org.orekit.frames.Frame`
    
        Class to create a L2 centered frame with :code:`L2TransformProvider`. Parent frame is always set as
        primaryBody.getInertiallyOrientedFrame()
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody, celestialBody2: org.orekit.bodies.CelestialBody): ...

class LocalOrbitalFrame(Frame):
    """
    public class LocalOrbitalFrame extends :class:`~org.orekit.frames.Frame`
    
        Class for frames moving with an orbiting satellite.
    
        There are several local orbital frames available. They are specified by the :class:`~org.orekit.frames.LOFType`
        enumerate.
    
        Do not use the :meth:`~org.orekit.frames.Frame.getTransformTo` method as it is not implemented.
    
        Also see:
            :meth:`~org.orekit.propagation.SpacecraftState.toTransform`, :meth:`~serialized`
    """
    def __init__(self, frame: Frame, lOFType: LOFType, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, string: str): ...

class PythonEOPHistoryLoader(EOPHistoryLoader):
    """
    public class PythonEOPHistoryLoader extends Object implements :class:`~org.orekit.frames.EOPHistoryLoader`
    """
    def __init__(self): ...
    def fillHistory(self, nutationCorrectionConverter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, sortedSet: java.util.SortedSet[EOPEntry]) -> None: ...
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

class PythonItrfVersionProvider(ItrfVersionProvider):
    """
    public class PythonItrfVersionProvider extends Object implements :class:`~org.orekit.frames.ItrfVersionProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getConfiguration(self, string: str, int: int) -> ITRFVersionLoader.ITRFVersionConfiguration:
        """
            Get the ITRF version configuration defined by a given file at specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.ItrfVersionProvider.getConfiguration`Â in
                interfaceÂ :class:`~org.orekit.frames.ItrfVersionProvider`
        
            Parameters:
                name (String): EOP file name
                mjd (int): date of the EOP in modified Julian day
        
            Returns:
                configuration valid around specified date in the file
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class PythonTransformProvider(TransformProvider):
    """
    public class PythonTransformProvider extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getTransform_1__T = typing.TypeVar('_getTransform_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_1__T]) -> FieldTransform[_getTransform_1__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
            Since:
                9.0
        
        
        """
        ...
    _getTransform_F__T = typing.TypeVar('_getTransform_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getTransform_F(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_F__T]) -> FieldTransform[_getTransform_F__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
            Since:
                9.0
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class ShiftingTransformProvider(TransformProvider):
    """
    public class ShiftingTransformProvider extends Object implements :class:`~org.orekit.frames.TransformProvider`
    
        Transform provider using thread-safe shifts on transforms sample.
    
        The shifts take derivatives into account, up to user specified order.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.utils.GenericTimeStampedCache`, :class:`~org.orekit.frames.InterpolatingTransformProvider`,
            :meth:`~serialized`
    """
    def __init__(self, transformProvider: TransformProvider, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, int: int, double: float, int2: int, double2: float, double3: float): ...
    def getGridPoints(self) -> int:
        """
            Get the number of interpolation grid points.
        
            Returns:
                number of interpolation grid points
        
        
        """
        ...
    def getRawProvider(self) -> TransformProvider:
        """
            Get the underlying provider for raw (non-interpolated) transforms.
        
            Returns:
                provider for raw (non-interpolated) transforms
        
        
        """
        ...
    def getStep(self) -> float:
        """
            Get the grid points time step.
        
            Returns:
                grid points time step
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

class TopocentricFrame(Frame, org.orekit.utils.PVCoordinatesProvider):
    """
    public class TopocentricFrame extends :class:`~org.orekit.frames.Frame` implements :class:`~org.orekit.utils.PVCoordinatesProvider`
    
        Topocentric frame.
    
        Frame associated to a position near the surface of a body shape.
    
        The origin of the frame is at the defining :class:`~org.orekit.bodies.GeodeticPoint` location, and the right-handed
        canonical trihedra is:
    
          - X axis in the local horizontal plane (normal to zenith direction) and following the local parallel towards East
          - Y axis in the horizontal plane (normal to zenith direction) and following the local meridian towards North
          - Z axis towards Zenith direction
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, bodyShape: org.orekit.bodies.BodyShape, geodeticPoint: org.orekit.bodies.GeodeticPoint, string: str): ...
    def computeLimitVisibilityPoint(self, double: float, double2: float, double3: float) -> org.orekit.bodies.GeodeticPoint:
        """
            Compute the limit visibility point for a satellite in a given direction.
        
            This method can be used to compute visibility circles around ground stations for example, using a simple loop on
            azimuth, with either a fixed elevation or an elevation that depends on azimuth to take ground masks into account.
        
            Parameters:
                radius (double): satellite distance to Earth center
                azimuth (double): pointing azimuth from station
                elevation (double): pointing elevation from station
        
            Returns:
                limit visibility point for the satellite
        
        
        """
        ...
    _getAzimuth_1__T = typing.TypeVar('_getAzimuth_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAzimuth(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the azimuth of a point with regards to the topocentric frame center point.
        
            The azimuth is the angle between the North direction at local point and the projection in local horizontal plane of the
            direction from local point to given point. Azimuth angles are counted clockwise, i.e positive towards the East.
        
            Parameters:
                extPoint (Vector3D): point for which elevation shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.AbsoluteDate`): computation date
        
            Returns:
                azimuth of the point
        
        """
        ...
    @typing.overload
    def getAzimuth(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAzimuth_1__T], frame: Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAzimuth_1__T]) -> _getAzimuth_1__T:
        """
            Get the azimuth of a point with regards to the topocentric frame center point.
        
            The azimuth is the angle between the North direction at local point and the projection in local horizontal plane of the
            direction from local point to given point. Azimuth angles are counted clockwise, i.e positive towards the East.
        
            Parameters:
                extPoint (FieldVector3D<T> extPoint): point for which elevation shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): computation date
        
            Returns:
                azimuth of the point
        
            Since:
                9.3
        
        
        """
        ...
    def getEast(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the east direction of topocentric frame, expressed in parent shape frame.
        
            The east direction is defined in the horizontal plane in order to complete direct triangle (east, north, zenith).
        
            Returns:
                unit vector in the east direction
        
            Also see:
                :meth:`~org.orekit.frames.TopocentricFrame.getWest`
        
        
        """
        ...
    _getElevation_1__T = typing.TypeVar('_getElevation_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getElevation(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the elevation of a point with regards to the local point.
        
            The elevation is the angle between the local horizontal and the direction from local point to given point.
        
            Parameters:
                extPoint (Vector3D): point for which elevation shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.AbsoluteDate`): computation date
        
            Returns:
                elevation of the point
        
        """
        ...
    @typing.overload
    def getElevation(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getElevation_1__T], frame: Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getElevation_1__T]) -> _getElevation_1__T:
        """
            Get the elevation of a point with regards to the local point.
        
            The elevation is the angle between the local horizontal and the direction from local point to given point.
        
            Parameters:
                extPoint (FieldVector3D<T> extPoint): point for which elevation shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): computation date
        
            Returns:
                elevation of the point
        
            Since:
                9.3
        
        
        """
        ...
    def getNadir(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the nadir direction of topocentric frame, expressed in parent shape frame.
        
            The nadir direction is the opposite of zenith direction.
        
            Returns:
                unit vector in the nadir direction
        
            Also see:
                :meth:`~org.orekit.frames.TopocentricFrame.getZenith`
        
        
        """
        ...
    def getNorth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the north direction of topocentric frame, expressed in parent shape frame.
        
            The north direction is defined in the horizontal plane (normal to zenith direction) and following the local meridian.
        
            Returns:
                unit vector in the north direction
        
            Also see:
                :meth:`~org.orekit.frames.TopocentricFrame.getSouth`
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the topocentric frame origin in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                position/velocity of the topocentric frame origin (m and m/s)
        
        
        """
        ...
    def getParentShape(self) -> org.orekit.bodies.BodyShape:
        """
            Get the body shape on which the local point is defined.
        
            Returns:
                body shape on which the local point is defined
        
        
        """
        ...
    _getPoint_0__T = typing.TypeVar('_getPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPoint(self, field: org.hipparchus.Field[_getPoint_0__T]) -> org.orekit.bodies.FieldGeodeticPoint[_getPoint_0__T]:
        """
            Get the surface point defining the origin of the frame.
        
            Parameters:
                field (Field<T> field): of the elements
        
            Returns:
                surface point defining the origin of the frame
        
            Since:
                9.3
        
        
        """
        ...
    @typing.overload
    def getPoint(self) -> org.orekit.bodies.GeodeticPoint:
        """
            Get the surface point defining the origin of the frame.
        
            Returns:
                surface point defining the origin of the frame
        
        """
        ...
    _getRange_1__T = typing.TypeVar('_getRange_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getRange(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the range of a point with regards to the topocentric frame center point.
        
            Parameters:
                extPoint (Vector3D): point for which range shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.AbsoluteDate`): computation date
        
            Returns:
                range (distance) of the point
        
        """
        ...
    @typing.overload
    def getRange(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getRange_1__T], frame: Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getRange_1__T]) -> _getRange_1__T:
        """
            Get the range of a point with regards to the topocentric frame center point.
        
            Parameters:
                extPoint (FieldVector3D<T> extPoint): point for which range shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): computation date
        
            Returns:
                range (distance) of the point
        
            Since:
                9.3
        
        
        """
        ...
    _getRangeRate_1__T = typing.TypeVar('_getRangeRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getRangeRate(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the range rate of a point with regards to the topocentric frame center point.
        
            Parameters:
                extPV (:class:`~org.orekit.utils.PVCoordinates`): point/velocity for which range rate shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.AbsoluteDate`): computation date
        
            Returns:
                range rate of the point (positive if point departs from frame)
        
        """
        ...
    @typing.overload
    def getRangeRate(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_getRangeRate_1__T], frame: Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getRangeRate_1__T]) -> _getRangeRate_1__T:
        """
            Get the range rate of a point with regards to the topocentric frame center point.
        
            Parameters:
                extPV (:class:`~org.orekit.utils.FieldPVCoordinates`<T> extPV): point/velocity for which range rate shall be computed
                frame (:class:`~org.orekit.frames.Frame`): frame in which the point is defined
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): computation date
        
            Returns:
                range rate of the point (positive if point departs from frame)
        
            Since:
                9.3
        
        
        """
        ...
    def getSouth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the south direction of topocentric frame, expressed in parent shape frame.
        
            The south direction is the opposite of north direction.
        
            Returns:
                unit vector in the south direction
        
            Also see:
                :meth:`~org.orekit.frames.TopocentricFrame.getNorth`
        
        
        """
        ...
    def getWest(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the west direction of topocentric frame, expressed in parent shape frame.
        
            The west direction is the opposite of east direction.
        
            Returns:
                unit vector in the west direction
        
            Also see:
                :meth:`~org.orekit.frames.TopocentricFrame.getEast`
        
        
        """
        ...
    def getZenith(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the zenith direction of topocentric frame, expressed in parent shape frame.
        
            The zenith direction is defined as the normal to local horizontal plane.
        
            Returns:
                unit vector in the zenith direction
        
            Also see:
                :meth:`~org.orekit.frames.TopocentricFrame.getNadir`
        
        
        """
        ...
    def pointAtDistance(self, double: float, double2: float, double3: float) -> org.orekit.bodies.GeodeticPoint:
        """
            Compute the point observed from the station at some specified distance.
        
            Parameters:
                azimuth (double): pointing azimuth from station
                elevation (double): pointing elevation from station
                distance (double): distance to station
        
            Returns:
                observed point
        
        
        """
        ...

class TwoBodiesBaryFrame(Frame):
    """
    public class TwoBodiesBaryFrame extends :class:`~org.orekit.frames.Frame`
    
        Class creating the inertial barycenter frame from two bodies.
    
        Since:
            10.2
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody, celestialBody2: org.orekit.bodies.CelestialBody): ...

class UpdatableFrame(Frame):
    """
    public class UpdatableFrame extends :class:`~org.orekit.frames.Frame`
    
        Frame whose transform from its parent can be updated.
    
        This class allows to control the relative position of two parts of the global frames tree using any two frames in each
        part as control handles. Consider the following simplified frames tree as an example:
    
        .. code-block: java
        
        
                      GCRF
                        |
          --------------------------------
          |             |                |
         Sun        satellite          Earth
                        |                |
                on-board antenna   ground station
                                         |
                                  tracking antenna
         
    
        Tracking measurements really correspond to the link between the ground and on-board antennas. This is tightly linked to
        the transform between these two frames, however neither frame is the direct parent frame of the other one: the path
        involves four intermediate frames. When we process a measurement, what we really want to update is the transform that
        defines the satellite frame with respect to its parent GCRF frame.
    
        In order to implement the above case, the satellite frame is defined as an instance of this class and its
        :meth:`~org.orekit.frames.UpdatableFrame.updateTransform` would be called each time we want to adjust the frame, i.e.
        each time we get a new measurement between the two antennas.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, frame: Frame, transform: Transform, string: str): ...
    @typing.overload
    def __init__(self, frame: Frame, transform: Transform, string: str, boolean: bool): ...
    def updateTransform(self, frame: Frame, frame2: Frame, transform: Transform, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Update the transform from parent frame implicitly according to two other frames.
        
            This method allows to control the relative position of two parts of the global frames tree using any two frames in each
            part as control handles. Consider the following simplified frames tree as an example:
        
            .. code-block: java
            
            
                          GCRF
                            |
              --------------------------------
              |             |                |
             Sun        satellite          Earth
                            |                |
                    on-board antenna   ground station
                                             |
                                      tracking antenna
             
        
            Tracking measurements really correspond to the link between the ground and on-board antennas. This is tightly linked to
            the transform between these two frames, however neither frame is the direct parent frame of the other one: the path
            involves four intermediate frames. When we process a measurement, what we really want to update is the transform that
            defines the satellite frame with respect to its parent GCRF frame. This is the purpose of this method. This update is
            done by the following call, where :code:`measurementTransform` represents the measurement as a simple translation
            transform between the two antenna frames:
        
            .. code-block: java
            
            
             satellite.updateTransform(onBoardAntenna, trackingAntenna,
                                       measurementTransform, date);
             
        
            One way to represent the behavior of the method is to consider the sub-tree rooted at the instance on one hand
            (satellite and on-board antenna in the example above) and the tree containing all the other frames on the other hand
            (GCRF, Sun, Earth, ground station, tracking antenna). Both tree are considered as two solid sets linked together by a
            flexible spring, which is the transform we want to update. The method stretches the spring to make sure the transform
            between the two specified frames (one in each tree part) matches the specified transform.
        
            Parameters:
                f1 (:class:`~org.orekit.frames.Frame`): first control frame (may be the instance itself)
                f2 (:class:`~org.orekit.frames.Frame`): second control frame (may be the instance itself)
                f1Tof2 (:class:`~org.orekit.frames.Transform`): desired transform from first to second control frame
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the transform
        
        
        """
        ...

class VersionedITRF(Frame):
    """
    public class VersionedITRF extends :class:`~org.orekit.frames.Frame`
    
        Specific version of International Terrestrial Reference Frame.
    
        This class represents an ITRF with a specific version, regardless of the version of the underlying
        :class:`~org.orekit.frames.EOPEntry`.
    
        Since:
            9.2
    
        Also see:
            :meth:`~serialized`
    """
    def getITRFVersion(self) -> ITRFVersion:
        """
            Get the ITRF version.
        
            Returns:
                ITRF version
        
        
        """
        ...

class GTODProvider(EOPBasedTransformProvider):
    """
    public class GTODProvider extends Object implements :class:`~org.orekit.frames.EOPBasedTransformProvider`
    
        Greenwich True Of Date Frame, also known as True of Date Rotating frame (TDR) or Greenwich Rotating Coordinate frame
        (GCR).
    
        This frame handles the sidereal time according to IAU-82 model.
    
        Its parent frame is the :code:`TODProvider`.
    
        The pole motion is not applied here.
    
        Also see:
            :meth:`~serialized`
    """
    def getEOPHistory(self) -> EOPHistory:
        """
            Get the EOP history.
        
            Specified by:
                :meth:`~org.orekit.frames.EOPBasedTransformProvider.getEOPHistory`Â in
                interfaceÂ :class:`~org.orekit.frames.EOPBasedTransformProvider`
        
            Returns:
                EOP history
        
        
        """
        ...
    def getNonInterpolatingProvider(self) -> 'GTODProvider':
        """
            Get a version of the provider that does *not* cache tidal corrections.
        
            This method removes the performance enhancing interpolation features that are used by default in EOP-based provider, in
            order to focus on accuracy. The interpolation features are intended to save processing time by avoiding doing tidal
            correction evaluation at each time step and caching some results. This method can be used to avoid this (it is
            automatically called by :meth:`~org.orekit.frames.FramesFactory.getNonInterpolatingTransform`, when very high accuracy
            is desired, or for testing purposes. It should be used with care, as doing the full computation is *really* costly.
        
            Specified by:
                :meth:`~org.orekit.frames.EOPBasedTransformProvider.getNonInterpolatingProvider`Â in
                interfaceÂ :class:`~org.orekit.frames.EOPBasedTransformProvider`
        
            Returns:
                version of the provider that does *not* cache tidal corrections
        
            Also see:
                :meth:`~org.orekit.frames.FramesFactory.getNonInterpolatingTransform`
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...

class LazyLoadedFrames(AbstractFrames):
    """
    public class LazyLoadedFrames extends :class:`~org.orekit.frames.AbstractFrames`
    
        This class lazily loads auxiliary data when it is needed by a requested frame. It is designed to match the behavior of
        :class:`~org.orekit.frames.FramesFactory` in Orekit 10.0.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.frames.LazyLoadedEop`
    """
    def __init__(self, lazyLoadedEop: LazyLoadedEop, timeScales: org.orekit.time.TimeScales, celestialBodies: org.orekit.bodies.CelestialBodies): ...
    def addDefaultEOP1980HistoryLoaders(self, string: str, string2: str, string3: str, string4: str, string5: str) -> None:
        """
            Add the default loaders EOP history (IAU 1980 precession/nutation).
        
            The default loaders look for IERS EOP C04 and bulletins B files. They correspond to
            :meth:`~org.orekit.utils.IERSConventions.IERS_1996` conventions.
        
            Parameters:
                rapidDataColumnsSupportedNames (String): regular expression for supported rapid data columns EOP files names (may be null if the default IERS file names are
                    used)
                rapidDataXMLSupportedNames (String): regular expression for supported rapid data XML EOP files names (may be null if the default IERS file names are used)
                eopC04SupportedNames (String): regular expression for supported EOP C04 files names (may be null if the default IERS file names are used)
                bulletinBSupportedNames (String): regular expression for supported bulletin B files names (may be null if the default IERS file names are used)
                bulletinASupportedNames (String): regular expression for supported bulletin A files names (may be null if the default IERS file names are used)
        
            Also see:
                `IERS EOP C04 files <http://hpiers.obspm.fr/eoppc/eop/eopc04/>`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.addEOPHistoryLoader`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.clearEOPHistoryLoaders`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.addDefaultEOP2000HistoryLoaders`
        
        
        """
        ...
    def addDefaultEOP2000HistoryLoaders(self, string: str, string2: str, string3: str, string4: str, string5: str) -> None:
        """
            Add the default loaders for EOP history (IAU 2000/2006 precession/nutation).
        
            The default loaders look for IERS EOP C04 and bulletins B files. They correspond to both
            :meth:`~org.orekit.utils.IERSConventions.IERS_2003` and :meth:`~org.orekit.utils.IERSConventions.IERS_2010` conventions.
        
            Parameters:
                rapidDataColumnsSupportedNames (String): regular expression for supported rapid data columns EOP files names (may be null if the default IERS file names are
                    used)
                rapidDataXMLSupportedNames (String): regular expression for supported rapid data XML EOP files names (may be null if the default IERS file names are used)
                eopC04SupportedNames (String): regular expression for supported EOP C04 files names (may be null if the default IERS file names are used)
                bulletinBSupportedNames (String): regular expression for supported bulletin B files names (may be null if the default IERS file names are used)
                bulletinASupportedNames (String): regular expression for supported bulletin A files names (may be null if the default IERS file names are used)
        
            Also see:
                `IERS EOP C04 files <http://hpiers.obspm.fr/eoppc/eop/eopc04/>`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.addEOPHistoryLoader`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.clearEOPHistoryLoaders`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.addDefaultEOP1980HistoryLoaders`
        
        
        """
        ...
    def addEOPHistoryLoader(self, iERSConventions: org.orekit.utils.IERSConventions, eOPHistoryLoader: EOPHistoryLoader) -> None:
        """
            Add a loader for Earth Orientation Parameters history.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): IERS conventions to which EOP history applies
                loader (:class:`~org.orekit.frames.EOPHistoryLoader`): custom loader to add for the EOP history
        
            Also see:
                :meth:`~org.orekit.frames.LazyLoadedFrames.addDefaultEOP1980HistoryLoaders`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.clearEOPHistoryLoaders`
        
        
        """
        ...
    def clearEOPHistoryLoaders(self) -> None:
        """
            Clear loaders for Earth Orientation Parameters history.
        
            Also see:
                :meth:`~org.orekit.frames.LazyLoadedFrames.addEOPHistoryLoader`,
                :meth:`~org.orekit.frames.LazyLoadedFrames.addDefaultEOP1980HistoryLoaders`
        
        
        """
        ...
    def getEOPHistory(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> EOPHistory:
        """
            Get Earth Orientation Parameters history.
        
            If no :class:`~org.orekit.frames.EOPHistoryLoader` has been added by calling
            :meth:`~org.orekit.frames.LazyLoadedFrames.addEOPHistoryLoader` or if
            :meth:`~org.orekit.frames.LazyLoadedFrames.clearEOPHistoryLoaders` has been called afterwards, the
            :meth:`~org.orekit.frames.LazyLoadedFrames.addDefaultEOP1980HistoryLoaders` and
            :meth:`~org.orekit.frames.LazyLoadedFrames.addDefaultEOP2000HistoryLoaders` methods will be called automatically with
            supported file names parameters all set to null, in order to get the default loaders configuration.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): conventions for which EOP history is requested
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Earth Orientation Parameters history
        
        
        """
        ...
    def setEOPContinuityThreshold(self, double: float) -> None:
        """
            Set the threshold to check EOP continuity.
        
            The default threshold (used if this method is never called) is 5 Julian days. If after loading EOP entries some holes
            between entries exceed this threshold, an exception will be triggered.
        
            One case when calling this method is really useful is for applications that use a single Bulletin A, as these bulletins
            have a roughly one month wide hole for the first bulletin of each month, which contains older final data in addition to
            the rapid data and the predicted data.
        
            Parameters:
                threshold (double): threshold to use for checking EOP continuity (in seconds)
        
        
        """
        ...

class PythonAbstractFrames(AbstractFrames):
    """
    public class PythonAbstractFrames extends :class:`~org.orekit.frames.AbstractFrames`
    """
    def __init__(self, timeScales: org.orekit.time.TimeScales, supplier: typing.Union[java.util.function.Supplier[Frame], typing.Callable[[], Frame]]): ...
    def finalize(self) -> None: ...
    def getEOPHistory(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> EOPHistory:
        """
            Get Earth Orientation Parameters history.
        
            Parameters:
                conventions (:class:`~org.orekit.utils.IERSConventions`): conventions for which EOP history is requested
                simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
            Returns:
                Earth Orientation Parameters history
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class PythonEOPBasedTransformProvider(EOPBasedTransformProvider):
    """
    public class PythonEOPBasedTransformProvider extends Object implements :class:`~org.orekit.frames.EOPBasedTransformProvider`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getEOPHistory(self) -> EOPHistory:
        """
            Get the EOP history.
        
            Specified by:
                :meth:`~org.orekit.frames.EOPBasedTransformProvider.getEOPHistory`Â in
                interfaceÂ :class:`~org.orekit.frames.EOPBasedTransformProvider`
        
            Returns:
                EOP history
        
        
        """
        ...
    def getNonInterpolatingProvider(self) -> EOPBasedTransformProvider:
        """
            Get a version of the provider that does *not* cache tidal corrections.
        
            This method removes the performance enhancing interpolation features that are used by default in EOP-based provider, in
            order to focus on accuracy. The interpolation features are intended to save processing time by avoiding doing tidal
            correction evaluation at each time step and caching some results. This method can be used to avoid this (it is
            automatically called by :meth:`~org.orekit.frames.FramesFactory.getNonInterpolatingTransform`, when very high accuracy
            is desired, or for testing purposes. It should be used with care, as doing the full computation is *really* costly.
        
            Specified by:
                :meth:`~org.orekit.frames.EOPBasedTransformProvider.getNonInterpolatingProvider`Â in
                interfaceÂ :class:`~org.orekit.frames.EOPBasedTransformProvider`
        
            Returns:
                version of the provider that does *not* cache tidal corrections
        
            Also see:
                :meth:`~org.orekit.frames.FramesFactory.getNonInterpolatingTransform`
        
        
        """
        ...
    _getTransform_1__T = typing.TypeVar('_getTransform_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> Transform:
        """
            Get the :class:`~org.orekit.frames.Transform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                transform at specified date
        
        """
        ...
    @typing.overload
    def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_1__T]) -> FieldTransform[_getTransform_1__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Specified by:
                :meth:`~org.orekit.frames.TransformProvider.getTransform` in interface :class:`~org.orekit.frames.TransformProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
            Since:
                9.0
        
        
        """
        ...
    _getTransform_F__T = typing.TypeVar('_getTransform_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getTransform_F(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_F__T]) -> FieldTransform[_getTransform_F__T]:
        """
            Get the :class:`~org.orekit.frames.FieldTransform` corresponding to specified date.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                transform at specified date
        
            Since:
                9.0
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class PythonAbstractEopParser(org.orekit.frames.AbstractEopParser):
    """
    public class PythonAbstractEopParser extends Object
    """
    def __init__(self, nutationCorrectionConverter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, itrfVersionProvider: ItrfVersionProvider, timeScale: org.orekit.time.TimeScale): ...
    def finalize(self) -> None: ...
    def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.Collection[EOPEntry]: ...
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

class AbstractEopParser: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.frames")``.

    AbstractEopLoader: typing.Type[AbstractEopLoader]
    AbstractEopParser: typing.Type[AbstractEopParser]
    AbstractFrames: typing.Type[AbstractFrames]
    CR3BPRotatingFrame: typing.Type[CR3BPRotatingFrame]
    EOPBasedTransformProvider: typing.Type[EOPBasedTransformProvider]
    EOPEntry: typing.Type[EOPEntry]
    EOPHistory: typing.Type[EOPHistory]
    EOPHistoryLoader: typing.Type[EOPHistoryLoader]
    EclipticProvider: typing.Type[EclipticProvider]
    FactoryManagedFrame: typing.Type[FactoryManagedFrame]
    FieldPoleCorrection: typing.Type[FieldPoleCorrection]
    FieldTransform: typing.Type[FieldTransform]
    FieldTransformGenerator: typing.Type[FieldTransformGenerator]
    FixedTransformProvider: typing.Type[FixedTransformProvider]
    Frame: typing.Type[Frame]
    Frames: typing.Type[Frames]
    FramesFactory: typing.Type[FramesFactory]
    GTODProvider: typing.Type[GTODProvider]
    HelmertTransformation: typing.Type[HelmertTransformation]
    ITRFVersion: typing.Type[ITRFVersion]
    ITRFVersionLoader: typing.Type[ITRFVersionLoader]
    InterpolatingTransformProvider: typing.Type[InterpolatingTransformProvider]
    ItrfVersionProvider: typing.Type[ItrfVersionProvider]
    L1Frame: typing.Type[L1Frame]
    L1TransformProvider: typing.Type[L1TransformProvider]
    L2Frame: typing.Type[L2Frame]
    LOFType: typing.Type[LOFType]
    LazyLoadedEop: typing.Type[LazyLoadedEop]
    LazyLoadedFrames: typing.Type[LazyLoadedFrames]
    LocalOrbitalFrame: typing.Type[LocalOrbitalFrame]
    OrphanFrame: typing.Type[OrphanFrame]
    PoleCorrection: typing.Type[PoleCorrection]
    Predefined: typing.Type[Predefined]
    PythonAbstractEopParser: typing.Type[PythonAbstractEopParser]
    PythonAbstractFrames: typing.Type[PythonAbstractFrames]
    PythonEOPBasedTransformProvider: typing.Type[PythonEOPBasedTransformProvider]
    PythonEOPHistoryLoader: typing.Type[PythonEOPHistoryLoader]
    PythonItrfVersionProvider: typing.Type[PythonItrfVersionProvider]
    PythonTransformProvider: typing.Type[PythonTransformProvider]
    ShiftingTransformProvider: typing.Type[ShiftingTransformProvider]
    TopocentricFrame: typing.Type[TopocentricFrame]
    Transform: typing.Type[Transform]
    TransformGenerator: typing.Type[TransformGenerator]
    TransformProvider: typing.Type[TransformProvider]
    TransformProviderUtils: typing.Type[TransformProviderUtils]
    TwoBodiesBaryFrame: typing.Type[TwoBodiesBaryFrame]
    UpdatableFrame: typing.Type[UpdatableFrame]
    VersionedITRF: typing.Type[VersionedITRF]
