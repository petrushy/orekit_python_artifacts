import java.io
import java.lang
import java.util
import java.util.function
import java.util.stream
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.data
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils.units
import typing



class AccurateFormatter:
    """
    public class AccurateFormatter extends Object
    
        Formatter used to produce strings from data with high accuracy.
    
        When producing test output from computed data, we want the shortest decimal representation of a floating point number
        that maintains round-trip safety. That is, a correct parser can recover the exact original number.
    
        For efficiency, this class uses the null algorithm for producing shortest string representation with round-trip safety.
    
        Since:
            11.0
    """
    STANDARDIZED_LOCALE: typing.ClassVar[java.util.Locale] = ...
    """
    public static final Locale STANDARDIZED_LOCALE
    
        Standardized locale to use, to ensure files can be exchanged without internationalization issues.
    
    """
    @typing.overload
    @staticmethod
    def format(double: float) -> str:
        """
            Format a double number.
        
            Parameters:
                value (double): number to format
        
            Returns:
                number formatted to full accuracy
        
            Format a date.
        
            Parameters:
                year (int): year
                month (int): month
                day (int): day
                hour (int): hour
                minute (int): minute
                seconds (double): seconds
        
            Returns:
                date formatted to full accuracy
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def format(int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str: ...

class AngularCoordinates(org.orekit.time.TimeShiftable['AngularCoordinates'], java.io.Serializable):
    """
    public class AngularCoordinates extends Object implements :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.utils.AngularCoordinates`>, Serializable
    
        Simple container for rotation/rotation rate/rotation acceleration triplets.
    
        The state can be slightly shifted to close dates. This shift is based on an approximate solution of the fixed
        acceleration motion. It is *not* intended as a replacement for proper attitude propagation but should be sufficient for
        either small time shifts or coarse accuracy.
    
        This class is the angular counterpart to :class:`~org.orekit.utils.PVCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :meth:`~serialized`
    """
    IDENTITY: typing.ClassVar['AngularCoordinates'] = ...
    """
    public static final :class:`~org.orekit.utils.AngularCoordinates` IDENTITY
    
        Fixed orientation parallel with reference frame (identity rotation, zero rotation rate and acceleration).
    
    """
    ___init___1__U = typing.TypeVar('___init___1__U', bound=org.hipparchus.analysis.differentiation.Derivative)  # <U>
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[___init___1__U]): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, pVCoordinates: 'PVCoordinates', pVCoordinates2: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, pVCoordinates: 'PVCoordinates', pVCoordinates2: 'PVCoordinates', pVCoordinates3: 'PVCoordinates', pVCoordinates4: 'PVCoordinates', double: float): ...
    def addOffset(self, angularCoordinates: 'AngularCoordinates') -> 'AngularCoordinates':
        """
            Add an offset from the instance.
        
            We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular
            coordinates do *not* commute under this operation, i.e. :code:`a.addOffset(b)` and :code:`b.addOffset(a)` lead to
            *different* results in most cases.
        
            The two methods :meth:`~org.orekit.utils.AngularCoordinates.addOffset` and
            :meth:`~org.orekit.utils.AngularCoordinates.subtractOffset` are designed so that round trip applications are possible.
            This means that both :code:`ac1.subtractOffset(ac2).addOffset(ac2)` and :code:`ac1.addOffset(ac2).subtractOffset(ac2)`
            return angular coordinates equal to ac1.
        
            Parameters:
                offset (:class:`~org.orekit.utils.AngularCoordinates`): offset to subtract
        
            Returns:
                new instance, with offset subtracted
        
            Also see:
                :meth:`~org.orekit.utils.AngularCoordinates.subtractOffset`
        
        
        """
        ...
    _applyTo_0__T = typing.TypeVar('_applyTo_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _applyTo_2__T = typing.TypeVar('_applyTo_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def applyTo(self, fieldPVCoordinates: 'FieldPVCoordinates'[_applyTo_0__T]) -> 'FieldPVCoordinates'[_applyTo_0__T]:
        """
            Apply the rotation to a pv coordinates.
        
            Parameters:
                pv (:class:`~org.orekit.utils.FieldPVCoordinates`<T> pv): vector to apply the rotation to
        
            Returns:
                a new pv coordinates which is the image of u by the rotation
        
            Since:
                9.0
        
            Apply the rotation to a pv coordinates.
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedFieldPVCoordinates`<T> pv): vector to apply the rotation to
        
            Returns:
                a new pv coordinates which is the image of u by the rotation
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def applyTo(self, pVCoordinates: 'PVCoordinates') -> 'PVCoordinates':
        """
            Apply the rotation to a pv coordinates.
        
            Parameters:
                pv (:class:`~org.orekit.utils.PVCoordinates`): vector to apply the rotation to
        
            Returns:
                a new pv coordinates which is the image of u by the rotation
        
            Apply the rotation to a pv coordinates.
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): vector to apply the rotation to
        
            Returns:
                a new pv coordinates which is the image of u by the rotation
        
        """
        ...
    @typing.overload
    def applyTo(self, timeStampedFieldPVCoordinates: 'TimeStampedFieldPVCoordinates'[_applyTo_2__T]) -> 'TimeStampedFieldPVCoordinates'[_applyTo_2__T]: ...
    @typing.overload
    def applyTo(self, timeStampedPVCoordinates: 'TimeStampedPVCoordinates') -> 'TimeStampedPVCoordinates': ...
    @staticmethod
    def createFromModifiedRodrigues(doubleArray: typing.List[typing.List[float]]) -> 'AngularCoordinates':
        """
            Convert a modified Rodrigues vector and derivatives to angular coordinates.
        
            Parameters:
                r (double[][]): modified Rodrigues vector (with first and second times derivatives)
        
            Returns:
                angular coordinates
        
            Also see:
                :meth:`~org.orekit.utils.AngularCoordinates.getModifiedRodrigues`
        
        
        """
        ...
    @staticmethod
    def estimateRate(rotation: org.hipparchus.geometry.euclidean.threed.Rotation, rotation2: org.hipparchus.geometry.euclidean.threed.Rotation, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Estimate rotation rate between two orientations.
        
            Estimation is based on a simple fixed rate rotation during the time interval between the two orientations.
        
            Parameters:
                start (Rotation): start orientation
                end (Rotation): end orientation
                dt (double): time elapsed between the dates of the two orientations
        
            Returns:
                rotation rate allowing to go from start to end orientations
        
        
        """
        ...
    def getModifiedRodrigues(self, double: float) -> typing.List[typing.List[float]]:
        """
            Convert rotation, rate and acceleration to modified Rodrigues vector and derivatives.
        
            The modified Rodrigues vector is tan(Î¸/4) u where Î¸ and u are the rotation angle and axis respectively.
        
            Parameters:
                sign (double): multiplicative sign for quaternion components
        
            Returns:
                modified Rodrigues vector and derivatives (vector on row 0, first derivative on row 1, second derivative on row 2)
        
            Also see:
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
            Get the rotation.
        
            Returns:
                the rotation.
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the rotation acceleration.
        
            Returns:
                the rotation acceleration vector dÎ©/dt (rad/sÂ²).
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the rotation rate.
        
            Returns:
                the rotation rate vector Î© (rad/s).
        
        
        """
        ...
    def revert(self) -> 'AngularCoordinates':
        """
            Revert a rotation/rotation rate/ rotation acceleration triplet. Build a triplet which reverse the effect of another
            triplet.
        
            Returns:
                a new triplet whose effect is the reverse of the effect of the instance
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'AngularCoordinates':
        """
            Get a time-shifted state.
        
            The state can be slightly shifted to close dates. This shift is based on an approximate solution of the fixed
            acceleration motion. It is *not* intended as a replacement for proper attitude propagation but should be sufficient for
            either small time shifts or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def subtractOffset(self, angularCoordinates: 'AngularCoordinates') -> 'AngularCoordinates':
        """
            Subtract an offset from the instance.
        
            We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular
            coordinates do *not* commute under this operation, i.e. :code:`a.subtractOffset(b)` and :code:`b.subtractOffset(a)` lead
            to *different* results in most cases.
        
            The two methods :meth:`~org.orekit.utils.AngularCoordinates.addOffset` and
            :meth:`~org.orekit.utils.AngularCoordinates.subtractOffset` are designed so that round trip applications are possible.
            This means that both :code:`ac1.subtractOffset(ac2).addOffset(ac2)` and :code:`ac1.addOffset(ac2).subtractOffset(ac2)`
            return angular coordinates equal to ac1.
        
            Parameters:
                offset (:class:`~org.orekit.utils.AngularCoordinates`): offset to subtract
        
            Returns:
                new instance, with offset subtracted
        
            Also see:
                :meth:`~org.orekit.utils.AngularCoordinates.addOffset`
        
        
        """
        ...
    def toDerivativeStructureRotation(self, int: int) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.DerivativeStructure]:
        """
            Transform the instance to a null<null>.
        
            The null coordinates correspond to time-derivatives up to the user-specified order.
        
            Parameters:
                order (int): derivation order for the vector components
        
            Returns:
                rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...
    def toUnivariateDerivative1Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.UnivariateDerivative1]:
        """
            Transform the instance to a null<null>.
        
            The null coordinates correspond to time-derivatives up to the order 1.
        
            Returns:
                rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...
    def toUnivariateDerivative2Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.UnivariateDerivative2]:
        """
            Transform the instance to a null<null>.
        
            The null coordinates correspond to time-derivatives up to the order 2.
        
            Returns:
                rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...

class AngularDerivativesFilter(java.lang.Enum['AngularDerivativesFilter']):
    """
    public enum AngularDerivativesFilter extends Enum<:class:`~org.orekit.utils.AngularDerivativesFilter`>
    
        Enumerate for selecting which derivatives to use in :class:`~org.orekit.utils.TimeStampedAngularCoordinates` and
        :class:`~org.orekit.utils.TimeStampedFieldAngularCoordinates` interpolation.
    
        Since:
            7.0
    
        Also see:
            :meth:`~org.orekit.utils.TimeStampedAngularCoordinates.interpolate`,
            :meth:`~org.orekit.utils.TimeStampedFieldAngularCoordinates.interpolate`,
            :class:`~org.orekit.utils.CartesianDerivativesFilter`
    """
    USE_R: typing.ClassVar['AngularDerivativesFilter'] = ...
    USE_RR: typing.ClassVar['AngularDerivativesFilter'] = ...
    USE_RRA: typing.ClassVar['AngularDerivativesFilter'] = ...
    @staticmethod
    def getFilter(int: int) -> 'AngularDerivativesFilter': ...
    def getMaxOrder(self) -> int:
        """
            Get the maximum derivation order.
        
            Returns:
                maximum derivation order
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AngularDerivativesFilter':
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
    def values() -> typing.List['AngularDerivativesFilter']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (AngularDerivativesFilter c : AngularDerivativesFilter.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CartesianDerivativesFilter(java.lang.Enum['CartesianDerivativesFilter']):
    """
    public enum CartesianDerivativesFilter extends Enum<:class:`~org.orekit.utils.CartesianDerivativesFilter`>
    
        Enumerate for selecting which derivatives to use in :class:`~org.orekit.utils.TimeStampedPVCoordinates` and
        :class:`~org.orekit.utils.TimeStampedFieldPVCoordinates` interpolation.
    
        Since:
            7.0
    
        Also see:
            :meth:`~org.orekit.utils.TimeStampedPVCoordinates.interpolate`,
            :meth:`~org.orekit.utils.TimeStampedFieldPVCoordinates.interpolate`, :class:`~org.orekit.utils.AngularDerivativesFilter`
    """
    USE_P: typing.ClassVar['CartesianDerivativesFilter'] = ...
    USE_PV: typing.ClassVar['CartesianDerivativesFilter'] = ...
    USE_PVA: typing.ClassVar['CartesianDerivativesFilter'] = ...
    @staticmethod
    def getFilter(int: int) -> 'CartesianDerivativesFilter': ...
    def getMaxOrder(self) -> int:
        """
            Get the maximum derivation order.
        
            Returns:
                maximum derivation order
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CartesianDerivativesFilter':
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
    def values() -> typing.List['CartesianDerivativesFilter']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (CartesianDerivativesFilter c : CartesianDerivativesFilter.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Constants:
    """
    public interface Constants
    
        Set of useful physical constants.
    """
    SPEED_OF_LIGHT: typing.ClassVar[float] = ...
    """
    static final double SPEED_OF_LIGHT
    
        Speed of light: 299792458.0 m/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IAU_2012_ASTRONOMICAL_UNIT: typing.ClassVar[float] = ...
    """
    static final double IAU_2012_ASTRONOMICAL_UNIT
    
        Astronomical unit as a conventional unit of length since IAU 2012 resolution B2: 149597870700.0 m.
    
        Also see:
            `IAU 2012 resolutions <http://www.iau.org/static/resolutions/IAU2012_English.pdf>`, :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_SOLAR_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_SOLAR_RADIUS
    
        Solar radius as defined by IAU 2015 resolution B3: 695700000.0 m.
    
        Also see:
            IAU 2015 resolutions, :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_SUN_GM: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_SUN_GM
    
        Sun attraction coefficient as defined by IAU 2015 resolution B3: 1.3271244e20 (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius as defined by IAU 2015 resolution B3: 6.3781e6 (m).
    
        Also see:
            :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_EARTH_POLAR_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_EARTH_POLAR_RADIUS
    
        Earth polar radius as defined by IAU 2015 resolution B3: 6.3568e6 (m).
    
        Also see:
            :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_EARTH_GM: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_EARTH_GM
    
        Earth attraction coefficient as defined by IAU 2015 resolution B3: 3.986004e14 (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_JUPITER_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_JUPITER_EQUATORIAL_RADIUS
    
        Jupiter equatorial radius as defined by IAU 2015 resolution B3: 7.1492e7 (m).
    
        Also see:
            :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_JUPITER_POLAR_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_JUPITER_POLAR_RADIUS
    
        Jupiter polar radius as defined by IAU 2015 resolution B3: 6.6854e7 (m).
    
        Also see:
            :meth:`~constant`
    
    
    """
    IAU_2015_NOMINAL_JUPITER_GM: typing.ClassVar[float] = ...
    """
    static final double IAU_2015_NOMINAL_JUPITER_GM
    
        Jupiter attraction coefficient as defined by IAU 2015 resolution B3: 1.2668653e17 (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JULIAN_DAY: typing.ClassVar[float] = ...
    """
    static final double JULIAN_DAY
    
        Duration of a mean solar day: 86400.0 s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JULIAN_YEAR: typing.ClassVar[float] = ...
    """
    static final double JULIAN_YEAR
    
        Duration of a Julian year: 365.25 :meth:`~org.orekit.utils.Constants.JULIAN_DAY`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JULIAN_CENTURY: typing.ClassVar[float] = ...
    """
    static final double JULIAN_CENTURY
    
        Duration of a Julian century: 36525 :meth:`~org.orekit.utils.Constants.JULIAN_DAY`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BESSELIAN_YEAR: typing.ClassVar[float] = ...
    """
    static final double BESSELIAN_YEAR
    
        Duration of a Besselian year: 365.242198781 :meth:`~org.orekit.utils.Constants.JULIAN_DAY`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ARC_SECONDS_TO_RADIANS: typing.ClassVar[float] = ...
    """
    static final double ARC_SECONDS_TO_RADIANS
    
        Conversion factor from arc seconds to radians: 2*PI/(360*60*60).
    
        Also see:
            :meth:`~constant`
    
    
    """
    G0_STANDARD_GRAVITY: typing.ClassVar[float] = ...
    """
    static final double G0_STANDARD_GRAVITY
    
        Standard gravity constant, used in maneuvers definition: 9.80665 m/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    SUN_RADIUS: typing.ClassVar[float] = ...
    """
    static final double SUN_RADIUS
    
        Sun radius: 695500000 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MOON_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double MOON_EQUATORIAL_RADIUS
    
        Moon equatorial radius: 1737400 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    WGS84_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double WGS84_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from WGS84 model: 6378137.0 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    WGS84_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    static final double WGS84_EARTH_FLATTENING
    
        Earth flattening from WGS84 model: 1.0 / 298.257223563.
    
        Also see:
            :meth:`~constant`
    
    
    """
    WGS84_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    static final double WGS84_EARTH_ANGULAR_VELOCITY
    
        Earth angular velocity from WGS84 model: 7.292115e-5 rad/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    WGS84_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double WGS84_EARTH_MU
    
        Earth gravitational constant from WGS84 model: 3.986004418e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    WGS84_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double WGS84_EARTH_C20
    
        Earth un-normalized second zonal coefficient from WGS84 model: .
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRS80_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double GRS80_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from GRS80 model: 6378137.0 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRS80_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    static final double GRS80_EARTH_FLATTENING
    
        Earth flattening from GRS80 model: 1.0 / 298.257222101.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRS80_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    static final double GRS80_EARTH_ANGULAR_VELOCITY
    
        Earth angular velocity from GRS80 model: 7.292115e-5 rad/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRS80_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double GRS80_EARTH_MU
    
        Earth gravitational constant from GRS80 model: 3.986005e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRS80_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double GRS80_EARTH_C20
    
        Earth un-normalized second zonal coefficient from GRS80 model: -1.08263e-3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM96_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double EGM96_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from EGM96 model: 6378136.3 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM96_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double EGM96_EARTH_MU
    
        Earth gravitational constant from EGM96 model: 3.986004415e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM96_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double EGM96_EARTH_C20
    
        Earth un-normalized second zonal coefficient from EGM96 model: -1.08262668355315e-3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM96_EARTH_C30: typing.ClassVar[float] = ...
    """
    static final double EGM96_EARTH_C30
    
        Earth un-normalized third zonal coefficient from EGM96 model: 2.53265648533224e-6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM96_EARTH_C40: typing.ClassVar[float] = ...
    """
    static final double EGM96_EARTH_C40
    
        Earth un-normalized fourth zonal coefficient from EGM96 model: 1.619621591367e-6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM96_EARTH_C50: typing.ClassVar[float] = ...
    """
    static final double EGM96_EARTH_C50
    
        Earth un-normalized fifth zonal coefficient from EGM96 model: 2.27296082868698e-7.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EGM96_EARTH_C60: typing.ClassVar[float] = ...
    """
    static final double EGM96_EARTH_C60
    
        Earth un-normalized sixth zonal coefficient from EGM96 model: -5.40681239107085e-7.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from GRIM5C1 model: 6378136.46 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_FLATTENING
    
        Earth flattening from GRIM5C1 model: 1.0 / 298.25765.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_ANGULAR_VELOCITY
    
        Earth angular velocity from GRIM5C1 model: 7.292115e-5 rad/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_MU
    
        Earth gravitational constant from GRIM5C1 model: 3.986004415e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_C20
    
        Earth un-normalized second zonal coefficient from GRIM5C1 model: -1.082626110612609e-3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_C30: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_C30
    
        Earth un-normalized third zonal coefficient from GRIM5C1 model: 2.536150841690056e-6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_C40: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_C40
    
        Earth un-normalized fourth zonal coefficient from GRIM5C1 model: 1.61936352497151e-6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_C50: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_C50
    
        Earth un-normalized fifth zonal coefficient from GRIM5C1 model: 2.231013736607540e-7.
    
        Also see:
            :meth:`~constant`
    
    
    """
    GRIM5C1_EARTH_C60: typing.ClassVar[float] = ...
    """
    static final double GRIM5C1_EARTH_C60
    
        Earth un-normalized sixth zonal coefficient from GRIM5C1 model: -5.402895357302363e-7.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EIGEN5C_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double EIGEN5C_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from EIGEN5C model: 6378136.46 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EIGEN5C_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double EIGEN5C_EARTH_MU
    
        Earth gravitational constant from EIGEN5C model: 3.986004415e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    EIGEN5C_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double EIGEN5C_EARTH_C20
    
        Earth un-normalized second zonal coefficient from EIGEN5C model: -1.082626457231767e-3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EIGEN5C_EARTH_C30: typing.ClassVar[float] = ...
    """
    static final double EIGEN5C_EARTH_C30
    
        Earth un-normalized third zonal coefficient from EIGEN5C model: 2.532547231862799e-6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EIGEN5C_EARTH_C40: typing.ClassVar[float] = ...
    """
    static final double EIGEN5C_EARTH_C40
    
        Earth un-normalized fourth zonal coefficient from EIGEN5C model: 1.619964434136e-6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EIGEN5C_EARTH_C50: typing.ClassVar[float] = ...
    """
    static final double EIGEN5C_EARTH_C50
    
        Earth un-normalized fifth zonal coefficient from EIGEN5C model: 2.277928487005437e-7.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EIGEN5C_EARTH_C60: typing.ClassVar[float] = ...
    """
    static final double EIGEN5C_EARTH_C60
    
        Earth un-normalized sixth zonal coefficient from EIGEN5C model: -5.406653715879098e-7.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS96_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IERS96_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from IERS96 model: 6378136.49 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS96_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    static final double IERS96_EARTH_FLATTENING
    
        Earth flattening from IERS96 model: 1.0 / 298.25642.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS96_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    static final double IERS96_EARTH_ANGULAR_VELOCITY
    
        Earth angular velocity from IERS96 model: 7.292115e-5 rad/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS96_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double IERS96_EARTH_MU
    
        Earth gravitational constant from IERS96 model: 3.986004418e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS96_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double IERS96_EARTH_C20
    
        Earth un-normalized second zonal coefficient from IERS96 model: -1.0826359e-3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2003_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IERS2003_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from IERS2003 model: 6378136.6 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2003_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    static final double IERS2003_EARTH_FLATTENING
    
        Earth flattening from IERS2003 model: 1.0 / 298.25642.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2003_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    static final double IERS2003_EARTH_ANGULAR_VELOCITY
    
        Earth angular velocity from IERS2003 model: 7.292115e-5 rad/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2003_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double IERS2003_EARTH_MU
    
        Earth gravitational constant from IERS2003 model: 3.986004418e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2003_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double IERS2003_EARTH_C20
    
        Earth un-normalized second zonal coefficient from IERS2003 model: -1.0826359e-3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2010_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    static final double IERS2010_EARTH_EQUATORIAL_RADIUS
    
        Earth equatorial radius from IERS2010 model: 6378136.6 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2010_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    static final double IERS2010_EARTH_FLATTENING
    
        Earth flattening from IERS2010 model: 1.0 / 298.25642.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2010_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    static final double IERS2010_EARTH_ANGULAR_VELOCITY
    
        Earth angular velocity from IERS2010 model: 7.292115e-5 rad/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2010_EARTH_MU: typing.ClassVar[float] = ...
    """
    static final double IERS2010_EARTH_MU
    
        Earth gravitational constant from IERS2010 model: 3.986004418e14 mÂ³/sÂ².
    
        Also see:
            :meth:`~constant`
    
    
    """
    IERS2010_EARTH_C20: typing.ClassVar[float] = ...
    """
    static final double IERS2010_EARTH_C20
    
        Earth un-normalized second zonal coefficient from IERS2010 model: -1.0826359e-3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_GAUSSIAN_GRAVITATIONAL_CONSTANT: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_GAUSSIAN_GRAVITATIONAL_CONSTANT
    
        Gaussian gravitational constant: 0.01720209895 âˆš(AUÂ³/dÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_ASTRONOMICAL_UNIT: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_ASTRONOMICAL_UNIT
    
        Astronomical Unit: 149597870691 m.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_GM
    
        Sun attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_MERCURY_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_MERCURY_MASS_RATIO
    
        Sun/Mercury mass ratio: 6023600.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_MERCURY_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_MERCURY_GM
    
        Sun/Mercury attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_VENUS_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_VENUS_MASS_RATIO
    
        Sun/Venus mass ratio: 408523.71.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_VENUS_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_VENUS_GM
    
        Sun/Venus attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_EARTH_PLUS_MOON_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_EARTH_PLUS_MOON_MASS_RATIO
    
        Sun/(Earth + Moon) mass ratio: 328900.56.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_EARTH_PLUS_MOON_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_EARTH_PLUS_MOON_GM
    
        Sun/(Earth + Moon) attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_EARTH_MOON_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_EARTH_MOON_MASS_RATIO
    
        Earth/Moon mass ratio: 81.30059.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_MOON_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_MOON_GM
    
        Moon attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_EARTH_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_EARTH_GM
    
        Earth attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_MARS_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_MARS_SYSTEM_MASS_RATIO
    
        Sun/(Mars system) mass ratio: 3098708.0.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_MARS_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_MARS_SYSTEM_GM
    
        Sun/(Mars system) attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_JUPITER_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_JUPITER_SYSTEM_MASS_RATIO
    
        Sun/(Jupiter system) mass ratio: 1047.3486.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_JUPITER_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_JUPITER_SYSTEM_GM
    
        Sun/(Jupiter system) ttraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_SATURN_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_SATURN_SYSTEM_MASS_RATIO
    
        Sun/(Saturn system) mass ratio: 3497.898.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SATURN_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SATURN_SYSTEM_GM
    
        Sun/(Saturn system) attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_URANUS_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_URANUS_SYSTEM_MASS_RATIO
    
        Sun/(Uranus system) mass ratio: 22902.98.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_URANUS_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_URANUS_SYSTEM_GM
    
        Sun/(Uranus system) attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_NEPTUNE_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_NEPTUNE_SYSTEM_MASS_RATIO
    
        Sun/(Neptune system) mass ratio: 19412.24.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_NEPTUNE_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_NEPTUNE_SYSTEM_GM
    
        Sun/(Neptune system) attraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_SUN_PLUTO_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_SUN_PLUTO_SYSTEM_MASS_RATIO
    
        Sun/(Pluto system) mass ratio: 1.35e8.
    
        Also see:
            :meth:`~constant`
    
    
    """
    JPL_SSD_PLUTO_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    static final double JPL_SSD_PLUTO_SYSTEM_GM
    
        Sun/(Pluto system) ttraction coefficient (mÂ³/sÂ²).
    
        Also see:
            :meth:`~constant`
    
    
    """

class Differentiation:
    """
    public class Differentiation extends Object
    
        Utility class for differentiating various kinds of functions.
    
        Since:
            8.0
    """
    @typing.overload
    @staticmethod
    def differentiate(parameterFunction: 'ParameterFunction', int: int, double: float) -> 'ParameterFunction':
        """
            Differentiate a scalar function using finite differences.
        
            Parameters:
                function (:class:`~org.orekit.utils.ParameterFunction`): function to differentiate
                nbPoints (int): number of points used for finite differences
                step (double): step for finite differences, in *physical* units
        
            Returns:
                scalar function evaluating to the derivative of the original function
        
            Since:
                9.3
        
            Differentiate a vector function using finite differences.
        
            Parameters:
                function (:class:`~org.orekit.utils.StateFunction`): function to differentiate
                dimension (int): dimension of the vector value of the function
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider to use for modified states
                orbitType (:class:`~org.orekit.orbits.OrbitType`): type used to map the orbit to a one dimensional array
                positionAngle (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle used for orbit mapping to array
                dP (double): user specified position error, used for step size computation for finite differences
                nbPoints (int): number of points used for finite differences
        
            Returns:
                matrix function evaluating to the Jacobian of the original function
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def differentiate(stateFunction: 'StateFunction', int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider, orbitType: org.orekit.orbits.OrbitType, positionAngle: org.orekit.orbits.PositionAngle, double: float, int2: int) -> 'StateJacobian': ...

class DoubleArrayDictionary(java.io.Serializable):
    """
    public class DoubleArrayDictionary extends Object implements Serializable
    
        String â†’ double[] mapping, for small number of keys.
    
        This class is a low overhead for a very small number of keys. It is based on simple array and string comparison. It
        plays the same role a :code:`Map<String, double[]>` but with reduced features and not intended for large number of keys.
        For such needs the regular :code:`Map<String, double[]>` should be preferred.
    
        Since:
            11.1
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, doubleArrayDictionary: 'DoubleArrayDictionary'): ...
    def clear(self) -> None:
        """
            Remove all entries.
        
        """
        ...
    def get(self, string: str) -> typing.List[float]:
        """
            Get the value corresponding to a key.
        
            Parameters:
                key (String): entry key
        
            Returns:
                copy of the value corresponding to the key or null if key not present
        
        
        """
        ...
    def getData(self) -> java.util.List['DoubleArrayDictionary.Entry']: ...
    def getEntry(self, string: str) -> 'DoubleArrayDictionary.Entry':
        """
            Get a complete entry.
        
            Parameters:
                key (String): entry key
        
            Returns:
                entry with key if it exists, null otherwise
        
        
        """
        ...
    def put(self, string: str, doubleArray: typing.List[float]) -> None:
        """
            Add an entry.
        
            If an entry with the same key already exists, it will be removed first.
        
            The new entry is always put at the end.
        
            Parameters:
                key (String): entry key
                value (double[]): entry value
        
        
        """
        ...
    @typing.overload
    def putAll(self, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]) -> None:
        """
            Put all the entries from the map in the dictionary.
        
            Parameters:
                map (Map<String,double[]> map): map to copy into the instance
        
            Put all the entries from another dictionary.
        
            Parameters:
                dictionary (:class:`~org.orekit.utils.DoubleArrayDictionary`): dictionary to copy into the instance
        
        
        """
        ...
    @typing.overload
    def putAll(self, doubleArrayDictionary: 'DoubleArrayDictionary') -> None: ...
    def remove(self, string: str) -> bool:
        """
            Remove an entry.
        
            Parameters:
                key (String): key of the entry to remove
        
            Returns:
                true if an entry has been removed, false if the key was not present
        
        
        """
        ...
    def size(self) -> int:
        """
            Get the number of dictionary entries.
        
            Returns:
                number of dictionary entries
        
        
        """
        ...
    def toMap(self) -> java.util.Map[str, typing.List[float]]:
        """
            Create a map from the instance.
        
            The map contains a copy of the instance data
        
            Returns:
                copy of the dictionary, as an independent map
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a string representation of the dictionary.
        
            This string representation is intended for improving displays in debuggers only.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of the dictionary
        
        
        """
        ...
    def unmodifiableView(self) -> 'DoubleArrayDictionary':
        """
            Get an unmodifiable view of the dictionary.
        
            The return dictionary is backed by the original instance and offers :code:`read-only` access to it, but all operations
            that modify it throw an null.
        
            Returns:
                unmodifiable view of the dictionary
        
        
        """
        ...
    class Entry(java.io.Serializable):
        def getKey(self) -> str: ...
        def getValue(self) -> typing.List[float]: ...
        def increment(self, doubleArray: typing.List[float]) -> None: ...
        def size(self) -> int: ...
        def zero(self) -> None: ...

class ElevationMask(java.io.Serializable):
    """
    public class ElevationMask extends Object implements Serializable
    
        Class for modeling the ground elevation values around a given point.
    
        Instances of this class can be considered to be immutable
    
        Since:
            6.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    def getElevation(self, double: float) -> float:
        """
            Get the interpolated elevation for a given azimuth according to the mask.
        
            Parameters:
                azimuth (double): azimuth (rad)
        
            Returns:
                elevation angle (rad)
        
        
        """
        ...

_FieldAngularCoordinates__T = typing.TypeVar('_FieldAngularCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAngularCoordinates(typing.Generic[_FieldAngularCoordinates__T]):
    """
    public class FieldAngularCoordinates<T extends CalculusFieldElement<T>> extends Object
    
        Simple container for rotation / rotation rate pairs, using null.
    
        The state can be slightly shifted to close dates. This shift is based on a simple quadratic model. It is *not* intended
        as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse
        accuracy.
    
        This class is the angular counterpart to :class:`~org.orekit.utils.FieldPVCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            6.0
    
        Also see:
            :class:`~org.orekit.utils.AngularCoordinates`
    """
    ___init___1__U = typing.TypeVar('___init___1__U', bound=org.hipparchus.analysis.differentiation.FieldDerivative)  # <U>
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAngularCoordinates__T], angularCoordinates: AngularCoordinates): ...
    @typing.overload
    def __init__(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[___init___1__U]): ...
    @typing.overload
    def __init__(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAngularCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAngularCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAngularCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAngularCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAngularCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldAngularCoordinates__T], fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldAngularCoordinates__T], fieldPVCoordinates3: 'FieldPVCoordinates'[_FieldAngularCoordinates__T], fieldPVCoordinates4: 'FieldPVCoordinates'[_FieldAngularCoordinates__T], double: float): ...
    def addOffset(self, fieldAngularCoordinates: 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]: ...
    @typing.overload
    def applyTo(self, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldAngularCoordinates__T]) -> 'FieldPVCoordinates'[_FieldAngularCoordinates__T]: ...
    @typing.overload
    def applyTo(self, pVCoordinates: 'PVCoordinates') -> 'FieldPVCoordinates'[_FieldAngularCoordinates__T]: ...
    @typing.overload
    def applyTo(self, timeStampedFieldPVCoordinates: 'TimeStampedFieldPVCoordinates'[_FieldAngularCoordinates__T]) -> 'TimeStampedFieldPVCoordinates'[_FieldAngularCoordinates__T]: ...
    @typing.overload
    def applyTo(self, timeStampedPVCoordinates: 'TimeStampedPVCoordinates') -> 'TimeStampedFieldPVCoordinates'[_FieldAngularCoordinates__T]: ...
    _createFromModifiedRodrigues__T = typing.TypeVar('_createFromModifiedRodrigues__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def createFromModifiedRodrigues(tArray: typing.List[typing.List[_createFromModifiedRodrigues__T]]) -> 'FieldAngularCoordinates'[_createFromModifiedRodrigues__T]:
        """
            Convert a modified Rodrigues vector and derivatives to angular coordinates.
        
            Parameters:
                r (T[][]): modified Rodrigues vector (with first and second times derivatives)
        
            Returns:
                angular coordinates
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.utils.FieldAngularCoordinates.getModifiedRodrigues`
        
        
        """
        ...
    _estimateRate_0__T = typing.TypeVar('_estimateRate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _estimateRate_1__T = typing.TypeVar('_estimateRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def estimateRate(fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_estimateRate_0__T], fieldRotation2: org.hipparchus.geometry.euclidean.threed.FieldRotation[_estimateRate_0__T], double: float) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateRate_0__T]:
        """
            Estimate rotation rate between two orientations.
        
            Estimation is based on a simple fixed rate rotation during the time interval between the two orientations.
        
            Parameters:
                start (FieldRotation<T> start): start orientation
                end (FieldRotation<T> end): end orientation
                dt (double): time elapsed between the dates of the two orientations
        
            Returns:
                rotation rate allowing to go from start to end orientations
        
            Estimate rotation rate between two orientations.
        
            Estimation is based on a simple fixed rate rotation during the time interval between the two orientations.
        
            Parameters:
                start (FieldRotation<T> start): start orientation
                end (FieldRotation<T> end): end orientation
                dt (T): time elapsed between the dates of the two orientations
        
            Returns:
                rotation rate allowing to go from start to end orientations
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def estimateRate(fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_estimateRate_1__T], fieldRotation2: org.hipparchus.geometry.euclidean.threed.FieldRotation[_estimateRate_1__T], t: _estimateRate_1__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateRate_1__T]: ...
    _getIdentity__T = typing.TypeVar('_getIdentity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getIdentity(field: org.hipparchus.Field[_getIdentity__T]) -> 'FieldAngularCoordinates'[_getIdentity__T]:
        """
            Fixed orientation parallel with reference frame (identity rotation, zero rotation rate and acceleration).
        
            Parameters:
                field (Field<T> field): field for the components
        
            Returns:
                a new fixed orientation parallel with reference frame
        
        
        """
        ...
    def getModifiedRodrigues(self, double: float) -> typing.List[typing.List[_FieldAngularCoordinates__T]]:
        """
            Convert rotation, rate and acceleration to modified Rodrigues vector and derivatives.
        
            The modified Rodrigues vector is tan(Î¸/4) u where Î¸ and u are the rotation angle and axis respectively.
        
            Parameters:
                sign (double): multiplicative sign for quaternion components
        
            Returns:
                modified Rodrigues vector and derivatives (vector on row 0, first derivative on row 1, second derivative on row 2)
        
            Since:
                9.0
        
            Also see:
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAngularCoordinates__T]: ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAngularCoordinates__T]: ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAngularCoordinates__T]: ...
    def revert(self) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAngularCoordinates__T) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]: ...
    def subtractOffset(self, fieldAngularCoordinates: 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]: ...
    def toAngularCoordinates(self) -> AngularCoordinates:
        """
            Convert to a regular angular coordinates.
        
            Returns:
                a regular angular coordinates
        
        
        """
        ...
    def toDerivativeStructureRotation(self, int: int) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_FieldAngularCoordinates__T]]: ...
    def toUnivariateDerivative1Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1[_FieldAngularCoordinates__T]]: ...
    def toUnivariateDerivative2Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldAngularCoordinates__T]]: ...

_FieldArrayDictionary__T = typing.TypeVar('_FieldArrayDictionary__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldArrayDictionary(typing.Generic[_FieldArrayDictionary__T]):
    """
    public class FieldArrayDictionary<T extends CalculusFieldElement<T>> extends Object
    
        String â†’ CalculusFieldElement[] mapping, for small number of keys.
    
        This class is a low overhead for a very small number of keys. It is based on simple array and string comparison. It
        plays the same role a :code:`Map<String, T[]>` but with reduced features and not intended for large number of keys. For
        such needs the regular :code:`Map<String, T[]>` should be preferred.
    
        Since:
            11.1
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldArrayDictionary__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldArrayDictionary__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldArrayDictionary__T], map: typing.Union[java.util.Map[str, typing.List[_FieldArrayDictionary__T]], typing.Mapping[str, typing.List[_FieldArrayDictionary__T]]]): ...
    @typing.overload
    def __init__(self, fieldArrayDictionary: 'FieldArrayDictionary'[_FieldArrayDictionary__T]): ...
    def clear(self) -> None:
        """
            Remove all entries.
        
        """
        ...
    def get(self, string: str) -> typing.List[_FieldArrayDictionary__T]:
        """
            Get the value corresponding to a key.
        
            Parameters:
                key (String): entry key
        
            Returns:
                copy of the value corresponding to the key or null if key not present
        
        
        """
        ...
    def getData(self) -> java.util.List['FieldArrayDictionary.Entry']: ...
    def getEntry(self, string: str) -> 'FieldArrayDictionary.Entry':
        """
            Get a complete entry.
        
            Parameters:
                key (String): entry key
        
            Returns:
                entry with key if it exists, null otherwise
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldArrayDictionary__T]: ...
    @typing.overload
    def put(self, string: str, doubleArray: typing.List[float]) -> None:
        """
            Add an entry.
        
            If an entry with the same key already exists, it will be removed first.
        
            The new entry is always put at the end.
        
            Parameters:
                key (String): entry key
                value (:class:`~org.orekit.utils.FieldArrayDictionary`[]): entry value
        
            Add an entry.
        
            If an entry with the same key already exists, it will be removed first.
        
            The new entry is always put at the end.
        
            Parameters:
                key (String): entry key
                value (double[]): entry value
        
        
        """
        ...
    @typing.overload
    def put(self, string: str, tArray: typing.List[_FieldArrayDictionary__T]) -> None: ...
    @typing.overload
    def putAll(self, map: typing.Union[java.util.Map[str, typing.List[_FieldArrayDictionary__T]], typing.Mapping[str, typing.List[_FieldArrayDictionary__T]]]) -> None: ...
    @typing.overload
    def putAll(self, fieldArrayDictionary: 'FieldArrayDictionary'[_FieldArrayDictionary__T]) -> None: ...
    def remove(self, string: str) -> bool:
        """
            remove an entry.
        
            Parameters:
                key (String): key of the entry to remove
        
            Returns:
                true if an entry has been removed, false if the key was not present
        
        
        """
        ...
    def size(self) -> int:
        """
            Get the number of dictionary entries.
        
            Returns:
                number of dictionary entries
        
        
        """
        ...
    def toMap(self) -> java.util.Map[str, typing.List[_FieldArrayDictionary__T]]: ...
    def toString(self) -> str:
        """
            Get a string representation of the dictionary.
        
            This string representation is intended for improving displays in debuggers only.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of the dictionary
        
        
        """
        ...
    def unmodifiableView(self) -> 'FieldArrayDictionary'[_FieldArrayDictionary__T]: ...
    class Entry:
        def getKey(self) -> str: ...
        def getValue(self) -> typing.List[_FieldArrayDictionary__T]: ...
        @typing.overload
        def increment(self, doubleArray: typing.List[float]) -> None: ...
        @typing.overload
        def increment(self, tArray: typing.List[_FieldArrayDictionary__T]) -> None: ...
        def size(self) -> int: ...
        def zero(self) -> None: ...

_FieldLegendrePolynomials__T = typing.TypeVar('_FieldLegendrePolynomials__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLegendrePolynomials(typing.Generic[_FieldLegendrePolynomials__T]):
    """
    public class FieldLegendrePolynomials<T extends CalculusFieldElement<T>> extends Object
    
        Computes the P :sub:`nm` (t) coefficients.
    
        The computation of the Legendre polynomials is performed following: Heiskanen and Moritz, Physical Geodesy, 1967, eq.
        1-62
    
        Since:
            11.0
    """
    def __init__(self, int: int, int2: int, t: _FieldLegendrePolynomials__T): ...
    def getPnm(self, int: int, int2: int) -> _FieldLegendrePolynomials__T:
        """
            Return the coefficient P :sub:`nm` .
        
            Parameters:
                n (int): index
                m (int): index
        
            Returns:
                The coefficient P :sub:`nm`
        
        
        """
        ...

_FieldPVCoordinates__T = typing.TypeVar('_FieldPVCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPVCoordinates(org.orekit.time.TimeShiftable['FieldPVCoordinates'[_FieldPVCoordinates__T]], typing.Generic[_FieldPVCoordinates__T]):
    """
    public class FieldPVCoordinates<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.utils.FieldPVCoordinates`<T>>
    
        Simple container for Position/Velocity pairs, using null.
    
        The state can be slightly shifted to close dates. This shift is based on a simple linear model. It is *not* intended as
        a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time
        shifts or coarse accuracy.
    
        This class is the angular counterpart to :class:`~org.orekit.utils.FieldAngularCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            6.0
    
        Also see:
            :class:`~org.orekit.utils.PVCoordinates`
    """
    ___init___13__U = typing.TypeVar('___init___13__U', bound=org.hipparchus.analysis.differentiation.FieldDerivative)  # <U>
    @typing.overload
    def __init__(self, double: float, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], double2: float, fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], double2: float, fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldPVCoordinates__T], double3: float, fieldPVCoordinates3: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, double: float, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], double2: float, fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldPVCoordinates__T], double3: float, fieldPVCoordinates3: 'FieldPVCoordinates'[_FieldPVCoordinates__T], double4: float, fieldPVCoordinates4: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], t2: _FieldPVCoordinates__T, fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], t2: _FieldPVCoordinates__T, fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldPVCoordinates__T], t3: _FieldPVCoordinates__T, fieldPVCoordinates3: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], t2: _FieldPVCoordinates__T, fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldPVCoordinates__T], t3: _FieldPVCoordinates__T, fieldPVCoordinates3: 'FieldPVCoordinates'[_FieldPVCoordinates__T], t4: _FieldPVCoordinates__T, fieldPVCoordinates4: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, pVCoordinates: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, pVCoordinates: 'PVCoordinates', t2: _FieldPVCoordinates__T, pVCoordinates2: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, pVCoordinates: 'PVCoordinates', t2: _FieldPVCoordinates__T, pVCoordinates2: 'PVCoordinates', t3: _FieldPVCoordinates__T, pVCoordinates3: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, t: _FieldPVCoordinates__T, pVCoordinates: 'PVCoordinates', t2: _FieldPVCoordinates__T, pVCoordinates2: 'PVCoordinates', t3: _FieldPVCoordinates__T, pVCoordinates3: 'PVCoordinates', t4: _FieldPVCoordinates__T, pVCoordinates4: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldPVCoordinates__T], pVCoordinates: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___13__U]): ...
    @typing.overload
    def __init__(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T], fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], fieldPVCoordinates2: 'FieldPVCoordinates'[_FieldPVCoordinates__T]): ...
    def crossProduct(self, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T]) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]: ...
    _estimateVelocity__T = typing.TypeVar('_estimateVelocity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def estimateVelocity(fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateVelocity__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateVelocity__T], double: float) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateVelocity__T]:
        """
            Estimate velocity between two positions.
        
            Estimation is based on a simple fixed velocity translation during the time interval between the two positions.
        
            Parameters:
                start (FieldVector3D<T> start): start position
                end (FieldVector3D<T> end): end position
                dt (double): time elapsed between the dates of the two positions
        
            Returns:
                velocity allowing to go from start to end positions
        
        
        """
        ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]: ...
    def getAngularVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]: ...
    def getMomentum(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]: ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]: ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]: ...
    _getZero__T = typing.TypeVar('_getZero__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getZero(field: org.hipparchus.Field[_getZero__T]) -> 'FieldPVCoordinates'[_getZero__T]:
        """
            Get fixed position/velocity at origin (both p, v and a are zero vectors).
        
            Parameters:
                field (Field<T> field): field for the components
        
            Returns:
                a new fixed position/velocity at origin
        
        
        """
        ...
    def negate(self) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]: ...
    def normalize(self) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldPVCoordinates__T) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]: ...
    def toDerivativeStructurePV(self, int: int) -> 'FieldPVCoordinates'[org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_FieldPVCoordinates__T]]: ...
    def toDerivativeStructureVector(self, int: int) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_FieldPVCoordinates__T]]: ...
    def toPVCoordinates(self) -> 'PVCoordinates':
        """
            Convert to a constant position-velocity.
        
            Returns:
                a constant position-velocity
        
        
        """
        ...
    def toString(self) -> str:
        """
            Return a string representation of this position/velocity pair.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of this position/velocity pair
        
        
        """
        ...
    def toUnivariateDerivative1PV(self) -> 'FieldPVCoordinates'[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1[_FieldPVCoordinates__T]]: ...
    def toUnivariateDerivative1Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1[_FieldPVCoordinates__T]]: ...
    def toUnivariateDerivative2PV(self) -> 'FieldPVCoordinates'[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldPVCoordinates__T]]: ...
    def toUnivariateDerivative2Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldPVCoordinates__T]]: ...

_FieldPVCoordinatesProvider__T = typing.TypeVar('_FieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPVCoordinatesProvider(typing.Generic[_FieldPVCoordinatesProvider__T]):
    """
    public interface FieldPVCoordinatesProvider<T extends CalculusFieldElement<T>>
    
        Interface for PV coordinates providers.
    """
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> 'TimeStampedFieldPVCoordinates'[_FieldPVCoordinatesProvider__T]: ...

_FieldTimeSpanMap__Transition__S = typing.TypeVar('_FieldTimeSpanMap__Transition__S')  # <S>
_FieldTimeSpanMap__Transition__D = typing.TypeVar('_FieldTimeSpanMap__Transition__D', bound=org.hipparchus.CalculusFieldElement)  # <D>
_FieldTimeSpanMap__T = typing.TypeVar('_FieldTimeSpanMap__T')  # <T>
_FieldTimeSpanMap__D = typing.TypeVar('_FieldTimeSpanMap__D', bound=org.hipparchus.CalculusFieldElement)  # <D>
class FieldTimeSpanMap(typing.Generic[_FieldTimeSpanMap__T, _FieldTimeSpanMap__D]):
    """
    public class FieldTimeSpanMap<T,D extends CalculusFieldElement<D>> extends Object
    
        Container for objects that apply to spans of time.
    
        Since:
            7.1
    """
    def __init__(self, t: _FieldTimeSpanMap__T, field: org.hipparchus.Field[_FieldTimeSpanMap__D]): ...
    def addValidAfter(self, t: _FieldTimeSpanMap__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__D]) -> None: ...
    def addValidBefore(self, t: _FieldTimeSpanMap__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__D]) -> None: ...
    def get(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__D]) -> _FieldTimeSpanMap__T: ...
    def getTransitions(self) -> java.util.SortedSet['FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__D]]: ...
    class Transition(org.orekit.time.TimeStamped, typing.Generic[_FieldTimeSpanMap__Transition__S, _FieldTimeSpanMap__Transition__D]):
        def getAbsoluteDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__Transition__D]: ...
        def getAfter(self) -> _FieldTimeSpanMap__Transition__S: ...
        def getBefore(self) -> _FieldTimeSpanMap__Transition__S: ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...

class IERSConventions(java.lang.Enum['IERSConventions']):
    """
    public enum IERSConventions extends Enum<:class:`~org.orekit.utils.IERSConventions`>
    
        Supported IERS conventions.
    
        Since:
            6.0
    """
    IERS_1996: typing.ClassVar['IERSConventions'] = ...
    IERS_2003: typing.ClassVar['IERSConventions'] = ...
    IERS_2010: typing.ClassVar['IERSConventions'] = ...
    _evaluateTC_2__T = typing.TypeVar('_evaluateTC_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _evaluateTC_3__T = typing.TypeVar('_evaluateTC_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def evaluateTC(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Evaluate the date offset between the current date and the
            :meth:`~org.orekit.utils.IERSConventions.getNutationReferenceEpoch`.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                date offset in Julian centuries
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.evaluateTC`
        
            Evaluate the date offset between the current date and the
            :meth:`~org.orekit.utils.IERSConventions.getNutationReferenceEpoch`.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                timeScales (:class:`~org.orekit.time.TimeScales`): used in the evaluation.
        
            Returns:
                date offset in Julian centuries
        
            Since:
                10.1
        
        :class:`~org.orekit.annotation.DefaultDataContext` public <T extends CalculusFieldElement<T>> T evaluateTC(:class:`~org.orekit.time.FieldAbsoluteDate`<T> date)
        
            Evaluate the date offset between the current date and the
            :meth:`~org.orekit.utils.IERSConventions.getNutationReferenceEpoch`.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                date offset in Julian centuries
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.evaluateTC`
        
        """
        ...
    @typing.overload
    def evaluateTC(self, absoluteDate: org.orekit.time.AbsoluteDate, timeScales: org.orekit.time.TimeScales) -> float: ...
    @typing.overload
    def evaluateTC(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_evaluateTC_2__T]) -> _evaluateTC_2__T: ...
    @typing.overload
    def evaluateTC(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_evaluateTC_3__T], timeScales: org.orekit.time.TimeScales) -> _evaluateTC_3__T:
        """
            Evaluate the date offset between the current date and the
            :meth:`~org.orekit.utils.IERSConventions.getNutationReferenceEpoch`.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                timeScales (:class:`~org.orekit.time.TimeScales`): used in the evaluation.
        
            Returns:
                date offset in Julian centuries
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getEOPTidalCorrection(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing tidal corrections for Earth Orientation Parameters.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): used in the computation. The TT and TAI scales are used.
        
            Returns:
                function computing tidal corrections for Earth Orientation Parameters, for xp, yp, ut1 and lod respectively
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getEOPTidalCorrection(self) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing tidal corrections for Earth Orientation Parameters.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                function computing tidal corrections for Earth Orientation Parameters, for xp, yp, ut1 and lod respectively
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getEOPTidalCorrection`
        
        """
        ...
    @typing.overload
    def getEarthOrientationAngleFunction(self, timeScale: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing the raw Earth Orientation Angle.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            The raw angle does not contain any correction. If for example dTU1 correction due to tidal effect is desired, it must be
            added afterward by the caller. The returned value contain the angle as the value and the angular rate as the first
            derivative.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
        
            Returns:
                function computing the rawEarth Orientation Angle, in the non-rotating origin paradigm
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getEarthOrientationAngleFunction`
        
            Get the function computing the raw Earth Orientation Angle.
        
            The raw angle does not contain any correction. If for example dTU1 correction due to tidal effect is desired, it must be
            added afterward by the caller. The returned value contain the angle as the value and the angular rate as the first
            derivative.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
                tai (:class:`~org.orekit.time.TimeScale`): TAI time scale
        
            Returns:
                function computing the rawEarth Orientation Angle, in the non-rotating origin paradigm
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getEarthOrientationAngleFunction(self, timeScale: org.orekit.time.TimeScale, timeScale2: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction: ...
    @typing.overload
    def getGASTFunction(self, timeScale: org.orekit.time.TimeScale, eOPHistory: org.orekit.frames.EOPHistory, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing Greenwich apparent sidereal time, in radians.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
                eopHistory (:class:`~org.orekit.frames.EOPHistory`): EOP history. If :code:`null` then no nutation correction is applied for EOP.
                timeScales (:class:`~org.orekit.time.TimeScales`): TAI time scale.
        
            Returns:
                function computing Greenwich apparent sidereal time
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getGASTFunction(self, timeScale: org.orekit.time.TimeScale, eOPHistory: org.orekit.frames.EOPHistory) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing Greenwich apparent sidereal time, in radians.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault` if :code:`eopHistory == null`.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
                eopHistory (:class:`~org.orekit.frames.EOPHistory`): EOP history. If :code:`null` then no nutation correction is applied for EOP.
        
            Returns:
                function computing Greenwich apparent sidereal time
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getGASTFunction`
        
        """
        ...
    @typing.overload
    def getGMSTFunction(self, timeScale: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing Greenwich mean sidereal time, in radians.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
                timeScales (:class:`~org.orekit.time.TimeScales`): other time scales used in the computation including TAI and TT.
        
            Returns:
                function computing Greenwich mean sidereal time
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getGMSTFunction(self, timeScale: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing Greenwich mean sidereal time, in radians.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
        
            Returns:
                function computing Greenwich mean sidereal time
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getGMSTFunction`
        
        """
        ...
    @typing.overload
    def getGMSTRateFunction(self, timeScale: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing Greenwich mean sidereal time rate, in radians per second.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
                timeScales (:class:`~org.orekit.time.TimeScales`): other time scales used in the computation including TAI and TT.
        
            Returns:
                function computing Greenwich mean sidereal time rate
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getGMSTRateFunction(self, timeScale: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing Greenwich mean sidereal time rate, in radians per second.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
        
            Returns:
                function computing Greenwich mean sidereal time rate
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getGMSTRateFunction`
        
        """
        ...
    def getLoveNumbers(self) -> 'LoveNumbers':
        """
            Get the Love numbers.
        
            Returns:
                Love numbers
        
            Since:
                6.1
        
        
        """
        ...
    @typing.overload
    def getMeanObliquityFunction(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing mean obliquity of the ecliptic.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): used in computing the function.
        
            Returns:
                function computing mean obliquity of the ecliptic
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getMeanObliquityFunction(self) -> org.orekit.time.TimeScalarFunction:
        """
            Get the function computing mean obliquity of the ecliptic.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                function computing mean obliquity of the ecliptic
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getMeanObliquityFunction`
        
        """
        ...
    def getNominalTidalDisplacement(self) -> typing.List[float]:
        """
            Get the nominal values of the displacement numbers.
        
            Returns:
                an array containing hÃ¢ï¿½Â½Ã¢ï¿½Â°Ã¢ï¿½Â¾, hÃ¢ï¿½Â½Ã‚Â²Ã¢ï¿½Â¾, hÃ¢â€šÆ’, hI diurnal, hI semi-diurnal,
                lÃ¢ï¿½Â½Ã¢ï¿½Â°Ã¢ï¿½Â¾, lÃ¢ï¿½Â½Ã‚Â¹Ã¢ï¿½Â¾ diurnal, lÃ¢ï¿½Â½Ã‚Â¹Ã¢ï¿½Â¾ semi-diurnal, lÃ¢ï¿½Â½Ã‚Â²Ã¢ï¿½Â¾, lÃ¢â€šÆ’, lI
                diurnal, lI semi-diurnal, HÃ¢â€šâ‚¬ permanent deformation amplitude
        
            Since:
                9.1
        
        
        """
        ...
    @typing.overload
    def getNutationArguments(self, timeScale: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.data.FundamentalNutationArguments:
        """
            Get the fundamental nutation arguments.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale for computing Greenwich Mean Sidereal Time (typically :meth:`~org.orekit.time.TimeScales.getUT1`)
                timeScales (:class:`~org.orekit.time.TimeScales`): other time scales used in the computation including TAI and TT.
        
            Returns:
                fundamental nutation arguments
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getNutationArguments(self, timeScale: org.orekit.time.TimeScale) -> org.orekit.data.FundamentalNutationArguments:
        """
            Get the fundamental nutation arguments. Does not compute GMST based values: gamma, gammaDot.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): other time scales used in the computation including TAI and TT.
        
            Returns:
                fundamental nutation arguments
        
            Since:
                10.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getNutationArguments`
        
            Get the fundamental nutation arguments.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale for computing Greenwich Mean Sidereal Time (typically :meth:`~org.orekit.time.TimeScales.getUT1`)
        
            Returns:
                fundamental nutation arguments
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getNutationArguments`,
                :meth:`~org.orekit.utils.IERSConventions.getNutationArguments`
        
        """
        ...
    @typing.overload
    def getNutationCorrectionConverter(self) -> 'IERSConventions.NutationCorrectionConverter':
        """
            Create a function converting nutation corrections between Î´X/Î´Y and Î´Î”Ïˆ/Î´Î”Îµ.
        
              - Î´X/Î´Y nutation corrections are used with the Non-Rotating Origin paradigm.
              - Î´Î”Ïˆ/Î´Î”Îµ nutation corrections are used with the equinox-based paradigm.
        
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                a new converter
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getNutationCorrectionConverter`
        
        """
        ...
    @typing.overload
    def getNutationCorrectionConverter(self, timeScales: org.orekit.time.TimeScales) -> 'IERSConventions.NutationCorrectionConverter':
        """
            Create a function converting nutation corrections between Î´X/Î´Y and Î´Î”Ïˆ/Î´Î”Îµ.
        
              - Î´X/Î´Y nutation corrections are used with the Non-Rotating Origin paradigm.
              - Î´Î”Ïˆ/Î´Î”Îµ nutation corrections are used with the equinox-based paradigm.
        
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): used to define the conversion.
        
            Returns:
                a new converter
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getNutationFunction(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing the nutation angles.
        
            The function returned computes the two classical angles ÃŽâ€�ÃŽÂ¨ and ÃŽâ€�ÃŽÂµ, and the correction to the equation of
            equinoxes introduced since 1997-02-27 by IAU 1994 resolution C7 (the correction is forced to 0 before this date)
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): used in the computation including TAI and TT.
        
            Returns:
                function computing the nutation in longitude Î”Î¨ and Î”Îµ and the correction of equation of equinoxes
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getNutationFunction(self) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing the nutation angles.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            The function returned computes the two classical angles ÃŽâ€�ÃŽÂ¨ and ÃŽâ€�ÃŽÂµ, and the correction to the equation of
            equinoxes introduced since 1997-02-27 by IAU 1994 resolution C7 (the correction is forced to 0 before this date)
        
            Returns:
                function computing the nutation in longitude Î”Î¨ and Î”Îµ and the correction of equation of equinoxes
        
            Since:
                6.1
        
        """
        ...
    @typing.overload
    def getNutationReferenceEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference epoch for fundamental nutation arguments.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                reference epoch for fundamental nutation arguments
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getNutationReferenceEpoch`
        
        """
        ...
    @typing.overload
    def getNutationReferenceEpoch(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference epoch for fundamental nutation arguments.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): to use for the reference epoch.
        
            Returns:
                reference epoch for fundamental nutation arguments
        
            Since:
                10.1
        
        
        """
        ...
    def getOceanPoleTide(self, eOPHistory: org.orekit.frames.EOPHistory) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing ocean pole tide (Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�).
        
            Parameters:
                eopHistory (:class:`~org.orekit.frames.EOPHistory`): EOP history
        
            Returns:
                model for ocean pole tide (Î”Câ‚‚â‚€, Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�, Î”Câ‚‚â‚‚, Î”Sâ‚‚â‚‚).
        
            Since:
                6.1
        
        
        """
        ...
    def getPermanentTide(self) -> float:
        """
            Get the permanent tide to be *removed* from Î”Câ‚‚â‚€ when zero-tide potentials are used.
        
            Returns:
                permanent tide to remove
        
        
        """
        ...
    @typing.overload
    def getPrecessionFunction(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing the precession angles.
        
            The function returned computes the three precession angles Ã�Ë† :sub:`A` (around Z axis), Ã�â€° :sub:`A` (around X axis)
            and Ã�â€¡ :sub:`A` (around Z axis). The constant angle ÃŽÂµÃ¢â€šâ‚¬ for the fourth rotation (around X axis) can be
            retrieved by evaluating the function returned by :meth:`~org.orekit.utils.IERSConventions.getMeanObliquityFunction` at
            :meth:`~org.orekit.utils.IERSConventions.getNutationReferenceEpoch`.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): used to define the function.
        
            Returns:
                function computing the precession angle
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getPrecessionFunction(self) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing the precession angles.
        
            The function returned computes the three precession angles Ã�Ë† :sub:`A` (around Z axis), Ã�â€° :sub:`A` (around X axis)
            and Ã�â€¡ :sub:`A` (around Z axis). The constant angle ÃŽÂµÃ¢â€šâ‚¬ for the fourth rotation (around X axis) can be
            retrieved by evaluating the function returned by :meth:`~org.orekit.utils.IERSConventions.getMeanObliquityFunction` at
            :meth:`~org.orekit.utils.IERSConventions.getNutationReferenceEpoch`.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                function computing the precession angle
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getPrecessionFunction`
        
        """
        ...
    def getSolidPoleTide(self, eOPHistory: org.orekit.frames.EOPHistory) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing solid pole tide (Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�).
        
            Parameters:
                eopHistory (:class:`~org.orekit.frames.EOPHistory`): EOP history
        
            Returns:
                model for solid pole tide (Î”Câ‚‚â‚€, Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�, Î”Câ‚‚â‚‚, Î”Sâ‚‚â‚‚).
        
            Since:
                6.1
        
        
        """
        ...
    def getTidalDisplacementFrequencyCorrectionDiurnal(self) -> org.orekit.data.PoissonSeries.CompiledSeries:
        """
            Get the correction function for tidal displacement for diurnal tides.
        
              - f[0]: radial correction, longitude cosine part
              - f[1]: radial correction, longitude sine part
              - f[2]: North correction, longitude cosine part
              - f[3]: North correction, longitude sine part
              - f[4]: East correction, longitude cosine part
              - f[5]: East correction, longitude sine part
        
        
            Returns:
                correction function for tidal displacement
        
            Since:
                9.1
        
        protected static :class:`~org.orekit.data.PoissonSeries.CompiledSeries` getTidalDisplacementFrequencyCorrectionDiurnal(String tableName, int cols, int rIp, int rOp, int tIp, int tOp)
        
            Get the correction function for tidal displacement for diurnal tides.
        
              - f[0]: radial correction, longitude cosine part
              - f[1]: radial correction, longitude sine part
              - f[2]: North correction, longitude cosine part
              - f[3]: North correction, longitude sine part
              - f[4]: East correction, longitude cosine part
              - f[5]: East correction, longitude sine part
        
        
            Parameters:
                tableName (String): name for the diurnal tides table
                cols (int): total number of columns of the diurnal tides table
                rIp (int): column holding âˆ†Rf(ip) in the diurnal tides table, counting from 1
                rOp (int): column holding âˆ†Rf(op) in the diurnal tides table, counting from 1
                tIp (int): column holding âˆ†Tf(ip) in the diurnal tides table, counting from 1
                tOp (int): column holding âˆ†Tf(op) in the diurnal tides table, counting from 1
        
            Returns:
                correction function for tidal displacement for diurnal tides
        
            Since:
                9.1
        
        
        """
        ...
    def getTidalDisplacementFrequencyCorrectionZonal(self) -> org.orekit.data.PoissonSeries.CompiledSeries:
        """
            Get the correction function for tidal displacement for zonal tides.
        
              - f[0]: radial correction
              - f[1]: North correction
        
        
            Returns:
                correction function for tidal displacement
        
            Since:
                9.1
        
        protected static :class:`~org.orekit.data.PoissonSeries.CompiledSeries` getTidalDisplacementFrequencyCorrectionZonal(String tableName, int cols, int rIp, int rOp, int tIp, int tOp)
        
            Get the correction function for tidal displacement for zonal tides.
        
              - f[0]: radial correction
              - f[1]: North correction
        
        
            Parameters:
                tableName (String): name for the zonal tides table
                cols (int): total number of columns of the table
                rIp (int): column holding âˆ†Rf(ip) in the table, counting from 1
                rOp (int): column holding âˆ†Rf(op) in the table, counting from 1
                tIp (int): column holding âˆ†Tf(ip) in the table, counting from 1
                tOp (int): column holding âˆ†Tf(op) in the table, counting from 1
        
            Returns:
                correction function for tidal displacement for zonal tides
        
            Since:
                9.1
        
        
        """
        ...
    @typing.overload
    def getTideFrequencyDependenceFunction(self, timeScale: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing frequency dependent terms (Î”Câ‚‚â‚€, Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�, Î”Câ‚‚â‚‚, Î”Sâ‚‚â‚‚).
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
                timeScales (:class:`~org.orekit.time.TimeScales`): other time scales used in the computation including TAI and TT.
        
            Returns:
                frequency dependence model for tides computation (Î”Câ‚‚â‚€, Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�, Î”Câ‚‚â‚‚, Î”Sâ‚‚â‚‚).
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getTideFrequencyDependenceFunction(self, timeScale: org.orekit.time.TimeScale) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing frequency dependent terms (Î”Câ‚‚â‚€, Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�, Î”Câ‚‚â‚‚, Î”Sâ‚‚â‚‚).
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Parameters:
                ut1 (:class:`~org.orekit.time.TimeScale`): UT1 time scale
        
            Returns:
                frequency dependence model for tides computation (Î”Câ‚‚â‚€, Î”Câ‚‚â‚�, Î”Sâ‚‚â‚�, Î”Câ‚‚â‚‚, Î”Sâ‚‚â‚‚).
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getTideFrequencyDependenceFunction`
        
        """
        ...
    @typing.overload
    def getXYSpXY2Function(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing the Celestial Intermediate Pole and Celestial Intermediate Origin components.
        
            The returned function computes the two X, Y components of CIP and the S+XY/2 component of the non-rotating CIO.
        
            Parameters:
                timeScales (:class:`~org.orekit.time.TimeScales`): used to define the function.
        
            Returns:
                function computing the Celestial Intermediate Pole and Celestial Intermediate Origin components
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def getXYSpXY2Function(self) -> org.orekit.time.TimeVectorFunction:
        """
            Get the function computing the Celestial Intermediate Pole and Celestial Intermediate Origin components.
        
            The returned function computes the two X, Y components of CIP and the S+XY/2 component of the non-rotating CIO.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Returns:
                function computing the Celestial Intermediate Pole and Celestial Intermediate Origin components
        
            Since:
                6.1
        
            Also see:
                :meth:`~org.orekit.utils.IERSConventions.getXYSpXY2Function`
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IERSConventions':
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
    def values() -> typing.List['IERSConventions']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (IERSConventions c : IERSConventions.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...
    class NutationCorrectionConverter:
        def toEquinox(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float) -> typing.List[float]: ...
        def toNonRotating(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float) -> typing.List[float]: ...

class InterpolationTableLoader(org.orekit.data.DataLoader):
    """
    public class InterpolationTableLoader extends Object implements :class:`~org.orekit.data.DataLoader`
    
        Used to read an interpolation table from a data file.
    """
    def __init__(self): ...
    def getAbscissaGrid(self) -> typing.List[float]:
        """
            Returns a copy of the abscissa grid for the interpolation function.
        
            Returns:
                the abscissa grid for the interpolation function, or :code:`null` if the file could not be read
        
        
        """
        ...
    def getOrdinateGrid(self) -> typing.List[float]:
        """
            Returns a copy of the ordinate grid for the interpolation function.
        
            Returns:
                the ordinate grid for the interpolation function, or :code:`null` if the file could not be read
        
        
        """
        ...
    def getValuesSamples(self) -> typing.List[typing.List[float]]:
        """
            Returns a copy of the values samples for the interpolation function.
        
            Returns:
                the values samples for the interpolation function, or :code:`null` if the file could not be read
        
        
        """
        ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def stillAcceptsData(self) -> bool:
        """
            Check if the loader still accepts new data.
        
            This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the
            data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or
            Earth Orientation Parameters that are split among several files), this method should always return true to make sure no
            data is left over.
        
            Specified by:
                :meth:`~org.orekit.data.DataLoader.stillAcceptsData` in interface :class:`~org.orekit.data.DataLoader`
        
            Returns:
                true while the loader still accepts new data
        
        
        """
        ...

class LagrangianPoints(java.lang.Enum['LagrangianPoints']):
    """
    public enum LagrangianPoints extends Enum<:class:`~org.orekit.utils.LagrangianPoints`>
    
        Enumerate for selecting which Lagrangian Point to consider in different classes.
    
        Since:
            10.2
    """
    L1: typing.ClassVar['LagrangianPoints'] = ...
    L2: typing.ClassVar['LagrangianPoints'] = ...
    L3: typing.ClassVar['LagrangianPoints'] = ...
    L4: typing.ClassVar['LagrangianPoints'] = ...
    L5: typing.ClassVar['LagrangianPoints'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LagrangianPoints':
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
    def values() -> typing.List['LagrangianPoints']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (LagrangianPoints c : LagrangianPoints.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LegendrePolynomials:
    """
    public class LegendrePolynomials extends Object
    
        Computes the P :sub:`nm` (t) coefficients.
    
        The computation of the Legendre polynomials is performed following: Heiskanen and Moritz, Physical Geodesy, 1967, eq.
        1-62
    
        Since:
            11.0
    """
    def __init__(self, int: int, int2: int, double: float): ...
    def getPnm(self, int: int, int2: int) -> float:
        """
            Return the coefficient P :sub:`nm` .
        
            Parameters:
                n (int): index
                m (int): index
        
            Returns:
                The coefficient P :sub:`nm`
        
        
        """
        ...

class LoveNumbers(java.io.Serializable):
    """
    public class LoveNumbers extends Object implements Serializable
    
        Container for Love numbers.
    
        Since:
            6.1
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[typing.List[float]]): ...
    def getImaginary(self, int: int, int2: int) -> float:
        """
            Get the imaginary part of a nominal Love numbers.
        
            Parameters:
                n (int): degree of the Love number (must be less than :meth:`~org.orekit.utils.LoveNumbers.getSize`)
                m (int): order of the Love number (must be less than :code:`n`)
        
            Returns:
                imaginary part of k :sub:`n,m`
        
        
        """
        ...
    def getPlus(self, int: int, int2: int) -> float:
        """
            Get the real part of a nominal Love numbers.
        
            Parameters:
                n (int): degree of the Love number (must be less than :meth:`~org.orekit.utils.LoveNumbers.getSize`)
                m (int): order of the Love number (must be less than :code:`n`)
        
            Returns:
                k :sub:`n,m` :sup:`+`
        
        
        """
        ...
    def getReal(self, int: int, int2: int) -> float:
        """
            Get the real part of a nominal Love numbers.
        
            Parameters:
                n (int): degree of the Love number (must be less than :meth:`~org.orekit.utils.LoveNumbers.getSize`)
                m (int): order of the Love number (must be less than :code:`n`)
        
            Returns:
                real part of k :sub:`n,m`
        
        
        """
        ...
    def getSize(self) -> int:
        """
            Get the size of the arrays.
        
            Returns:
                size of the arrays (i.e. max degree for Love numbers + 1)
        
        
        """
        ...

class MultipleShooting:
    """
    public interface MultipleShooting
    
        Interface for Multiple shooting methods.
    
        Since:
            10.2
    """
    def compute(self) -> java.util.List[org.orekit.propagation.SpacecraftState]: ...

class OrekitConfiguration:
    """
    public class OrekitConfiguration extends Object
    
        Utility class for setting global configuration parameters.
    """
    @staticmethod
    def getCacheSlotsNumber() -> int:
        """
            Get the number of slots to use in caches.
        
            Returns:
                number of slots to use in caches
        
        
        """
        ...
    @staticmethod
    def setCacheSlotsNumber(int: int) -> None:
        """
            Set the number of slots to use in caches.
        
            Parameters:
                slotsNumber (int): number of slots to use in caches
        
        
        """
        ...

class PVCoordinates(org.orekit.time.TimeShiftable['PVCoordinates'], java.io.Serializable):
    """
    public class PVCoordinates extends Object implements :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.utils.PVCoordinates`>, Serializable
    
        Simple container for Position/Velocity/Acceleration triplets.
    
        The state can be slightly shifted to close dates. This shift is based on a simple quadratic model. It is *not* intended
        as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time
        shifts or coarse accuracy.
    
        This class is the angular counterpart to :class:`~org.orekit.utils.AngularCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :meth:`~serialized`
    """
    ZERO: typing.ClassVar['PVCoordinates'] = ...
    """
    public static final :class:`~org.orekit.utils.PVCoordinates` ZERO
    
        Fixed position/velocity at origin (both p, v and a are zero vectors).
    
    """
    ___init___5__U = typing.TypeVar('___init___5__U', bound=org.hipparchus.analysis.differentiation.Derivative)  # <U>
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, pVCoordinates: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, double: float, pVCoordinates: 'PVCoordinates', double2: float, pVCoordinates2: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, double: float, pVCoordinates: 'PVCoordinates', double2: float, pVCoordinates2: 'PVCoordinates', double3: float, pVCoordinates3: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, double: float, pVCoordinates: 'PVCoordinates', double2: float, pVCoordinates2: 'PVCoordinates', double3: float, pVCoordinates3: 'PVCoordinates', double4: float, pVCoordinates4: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___5__U]): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, pVCoordinates: 'PVCoordinates', pVCoordinates2: 'PVCoordinates'): ...
    @staticmethod
    def crossProduct(pVCoordinates: 'PVCoordinates', pVCoordinates2: 'PVCoordinates') -> 'PVCoordinates':
        """
            Compute the cross-product of two instances.
        
            Parameters:
                pv1 (:class:`~org.orekit.utils.PVCoordinates`): first instances
                pv2 (:class:`~org.orekit.utils.PVCoordinates`): second instances
        
            Returns:
                the cross product v1 ^ v2 as a new instance
        
        
        """
        ...
    @staticmethod
    def estimateVelocity(vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Estimate velocity between two positions.
        
            Estimation is based on a simple fixed velocity translation during the time interval between the two positions.
        
            Parameters:
                start (Vector3D): start position
                end (Vector3D): end position
                dt (double): time elapsed between the dates of the two positions
        
            Returns:
                velocity allowing to go from start to end positions
        
        
        """
        ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Gets the acceleration.
        
            Returns:
                the acceleration vector (m/sÂ²).
        
        
        """
        ...
    def getAngularVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the angular velocity (spin) of this point as seen from the origin.
        
            The angular velocity vector is parallel to the :meth:`~org.orekit.utils.PVCoordinates.getMomentum` and is computed by
            Ã�â€° = p Ã— v / ||p||Ã‚Â²
        
            Returns:
                the angular velocity vector
        
            Also see:
                `Angular Velocity on Wikipedia <http://en.wikipedia.org/wiki/Angular_velocity>`
        
        
        """
        ...
    def getMomentum(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Gets the momentum.
        
            This vector is the p âŠ— v where p is position, v is velocity and âŠ— is cross product. To get the real physical angular
            momentum you need to multiply this vector by the mass.
        
            The returned vector is recomputed each time this method is called, it is not cached.
        
            Returns:
                a new instance of the momentum vector (mÂ²/s).
        
        
        """
        ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Gets the position.
        
            Returns:
                the position vector (m).
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Gets the velocity.
        
            Returns:
                the velocity vector (m/s).
        
        
        """
        ...
    def negate(self) -> 'PVCoordinates':
        """
            Get the opposite of the instance.
        
            Returns:
                a new position-velocity which is opposite to the instance
        
        
        """
        ...
    def normalize(self) -> 'PVCoordinates':
        """
            Normalize the position part of the instance.
        
            The computed coordinates first component (position) will be a normalized vector, the second component (velocity) will be
            the derivative of the first component (hence it will generally not be normalized), and the third component
            (acceleration) will be the derivative of the second component (hence it will generally not be normalized).
        
            Returns:
                a new instance, with first component normalized and remaining component computed to have consistent derivatives
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'PVCoordinates':
        """
            Get a time-shifted state.
        
            The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is *not* intended
            as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time
            shifts or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def toDerivativeStructurePV(self, int: int) -> FieldPVCoordinates[org.hipparchus.analysis.differentiation.DerivativeStructure]:
        """
            Transform the instance to a :class:`~org.orekit.utils.FieldPVCoordinates`<null>.
        
            The null coordinates correspond to time-derivatives up to the user-specified order. As both the instance components
            :meth:`~org.orekit.utils.PVCoordinates.getPosition`, :meth:`~org.orekit.utils.PVCoordinates.getVelocity` and
            :meth:`~org.orekit.utils.PVCoordinates.getAcceleration` and the null of the components holds time-derivatives, there are
            several ways to retrieve these derivatives. If for example the :code:`order` is set to 2, then both
            :code:`pv.getPosition().getX().getPartialDerivative(2)`, :code:`pv.getVelocity().getX().getPartialDerivative(1)` and
            :code:`pv.getAcceleration().getX().getValue()` return the exact same value.
        
            If derivation order is 1, the first derivative of acceleration will be computed as a Keplerian-only jerk. If derivation
            order is 2, the second derivative of velocity (which is also the first derivative of acceleration) will be computed as a
            Keplerian-only jerk, and the second derivative of acceleration will be computed as a Keplerian-only jounce.
        
            Parameters:
                order (int): derivation order for the vector components (must be either 0, 1 or 2)
        
            Returns:
                pv coordinates with time-derivatives embedded within the coordinates
        
            Since:
                9.2
        
        
        """
        ...
    def toDerivativeStructureVector(self, int: int) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.DerivativeStructure]:
        """
            Transform the instance to a null<null>.
        
            The null coordinates correspond to time-derivatives up to the user-specified order.
        
            Parameters:
                order (int): derivation order for the vector components (must be either 0, 1 or 2)
        
            Returns:
                vector with time-derivatives embedded within the coordinates
        
        
        """
        ...
    def toString(self) -> str:
        """
            Return a string representation of this position/velocity pair.
        
            Overrides:
                 in class 
        
            Returns:
                string representation of this position/velocity pair
        
        
        """
        ...
    def toUnivariateDerivative1PV(self) -> FieldPVCoordinates[org.hipparchus.analysis.differentiation.UnivariateDerivative1]:
        """
            Transform the instance to a :class:`~org.orekit.utils.FieldPVCoordinates`<null>.
        
            The null coordinates correspond to time-derivatives up to the order 1. The first derivative of acceleration will be
            computed as a Keplerian-only jerk.
        
            Returns:
                pv coordinates with time-derivatives embedded within the coordinates
        
            Since:
                10.2
        
        
        """
        ...
    def toUnivariateDerivative1Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative1]:
        """
            Transform the instance to a null<null>.
        
            The null coordinates correspond to time-derivatives up to the order 1.
        
            Returns:
                vector with time-derivatives embedded within the coordinates
        
            Since:
                10.2
        
            Also see:
                :meth:`~org.orekit.utils.PVCoordinates.toUnivariateDerivative2Vector`
        
        
        """
        ...
    def toUnivariateDerivative2PV(self) -> FieldPVCoordinates[org.hipparchus.analysis.differentiation.UnivariateDerivative2]:
        """
            Transform the instance to a :class:`~org.orekit.utils.FieldPVCoordinates`<null>.
        
            The null coordinates correspond to time-derivatives up to the order 2. As derivation order is 2, the second derivative
            of velocity (which is also the first derivative of acceleration) will be computed as a Keplerian-only jerk, and the
            second derivative of acceleration will be computed as a Keplerian-only jounce.
        
            Returns:
                pv coordinates with time-derivatives embedded within the coordinates
        
            Since:
                10.2
        
        
        """
        ...
    def toUnivariateDerivative2Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative2]:
        """
            Transform the instance to a null<null>.
        
            The null coordinates correspond to time-derivatives up to the order 2.
        
            Returns:
                vector with time-derivatives embedded within the coordinates
        
            Since:
                10.2
        
            Also see:
                :meth:`~org.orekit.utils.PVCoordinates.toUnivariateDerivative1Vector`
        
        
        """
        ...

class PVCoordinatesProvider:
    """
    public interface PVCoordinatesProvider
    
        Interface for PV coordinates providers.
    """
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...

class ParameterDriver:
    """
    public class ParameterDriver extends Object
    
        Class allowing to drive the value of a parameter.
    
        This class is typically used as a bridge between an estimation algorithm (typically orbit determination or optimizer)
        and an internal parameter in a physical model that needs to be tuned, or a bridge between a finite differences algorithm
        and an internal parameter in a physical model that needs to be slightly offset. The physical model will expose to the
        algorithm a set of instances of this class so the algorithm can call the
        :meth:`~org.orekit.utils.ParameterDriver.setValue` method to update the parameter value. Each time the value is set, the
        physical model will be notified as it will register a :class:`~org.orekit.utils.ParameterObserver` for this purpose.
    
        This design has two major goals. First, it allows an external algorithm to drive internal parameters almost anonymously,
        as it only needs to get a list of instances of this class, without knowing what they really drive. Second, it allows the
        physical model to not expose directly setters methods for its parameters. In order to be able to modify the parameter
        value, the algorithm *must* retrieve a parameter driver.
    
        Since:
            8.0
    
        Also see:
            :class:`~org.orekit.utils.ParameterObserver`
    """
    def __init__(self, string: str, double: float, double2: float, double3: float, double4: float): ...
    def addObserver(self, parameterObserver: 'ParameterObserver') -> None:
        """
            Add an observer for this driver.
        
            The observer :meth:`~org.orekit.utils.ParameterObserver.valueChanged` method is called once automatically when the
            observer is added, and then called at each value change.
        
            Parameters:
                observer (:class:`~org.orekit.utils.ParameterObserver`): observer to add while being updated
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
            Get maximum parameter value.
        
            Returns:
                maximum parameter value
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
            Get minimum parameter value.
        
            Returns:
                minimum parameter value
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get name.
        
            Returns:
                name
        
        
        """
        ...
    def getNormalizedValue(self) -> float:
        """
            Get normalized value.
        
            The normalized value is a non-dimensional value suitable for use as part of a vector in an optimization process. It is
            computed as :code:`(current - reference)/scale`.
        
            Returns:
                normalized value
        
        
        """
        ...
    def getObservers(self) -> java.util.List['ParameterObserver']: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get current reference date.
        
            Returns:
                current reference date (null if it was never set)
        
            Since:
                9.0
        
        
        """
        ...
    def getReferenceValue(self) -> float:
        """
            Get reference parameter value.
        
            Returns:
                reference parameter value
        
        
        """
        ...
    def getScale(self) -> float:
        """
            Get scale.
        
            Returns:
                scale
        
        
        """
        ...
    @typing.overload
    def getValue(self) -> float:
        """
            Get current parameter value.
        
            Returns:
                current parameter value
        
        """
        ...
    @typing.overload
    def getValue(self, int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.hipparchus.analysis.differentiation.Gradient:
        """
            Get the value as a gradient.
        
            Parameters:
                freeParameters (int): total number of free parameters in the gradient
                indices (Map<String,Integer> indices): indices of the differentiation parameters in derivatives computations
        
            Returns:
                value with derivatives
        
            Since:
                10.2
        
        
        """
        ...
    def isSelected(self) -> bool:
        """
            Check if parameter is selected.
        
            Selection is used for estimated parameters in orbit determination, or to compute the Jacobian matrix in partial
            derivatives computation.
        
            Returns:
                true if parameter is selected, false if it is not
        
        
        """
        ...
    def removeObserver(self, parameterObserver: 'ParameterObserver') -> None:
        """
            Remove an observer.
        
            Parameters:
                observer (:class:`~org.orekit.utils.ParameterObserver`): observer to remove
        
            Since:
                9.1
        
        
        """
        ...
    def replaceObserver(self, parameterObserver: 'ParameterObserver', parameterObserver2: 'ParameterObserver') -> None:
        """
            Replace an observer.
        
            Parameters:
                oldObserver (:class:`~org.orekit.utils.ParameterObserver`): observer to replace
                newObserver (:class:`~org.orekit.utils.ParameterObserver`): new observer to use
        
            Since:
                10.1
        
        
        """
        ...
    def setMaxValue(self, double: float) -> None:
        """
            Set maximum parameter value.
        
            Parameters:
                maxValue (double): the maximum value to set.
        
            Since:
                9.3
        
        
        """
        ...
    def setMinValue(self, double: float) -> None:
        """
            Set minimum parameter value.
        
            Parameters:
                minValue (double): the minimum value to set.
        
            Since:
                9.3
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Change the name of this parameter driver.
        
            Parameters:
                name (String): new name
        
        
        """
        ...
    def setNormalizedValue(self, double: float) -> None:
        """
            Set normalized value.
        
            The normalized value is a non-dimensional value suitable for use as part of a vector in an optimization process. It is
            computed as :code:`(current - reference)/scale`.
        
            Parameters:
                normalized (double): value
        
        
        """
        ...
    def setReferenceDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Set reference date.
        
            Parameters:
                newReferenceDate (:class:`~org.orekit.time.AbsoluteDate`): new reference date
        
            Since:
                9.0
        
        
        """
        ...
    def setReferenceValue(self, double: float) -> None:
        """
            Set reference parameter value.
        
            Parameters:
                referenceValue (double): the reference value to set.
        
            Since:
                9.3
        
        
        """
        ...
    def setScale(self, double: float) -> None:
        """
            Set scale.
        
            Parameters:
                scale (double): the scale to set.
        
            Since:
                9.3
        
        
        """
        ...
    def setSelected(self, boolean: bool) -> None:
        """
            Configure a parameter selection status.
        
            Selection is used for estimated parameters in orbit determination, or to compute the Jacobian matrix in partial
            derivatives computation.
        
            Parameters:
                selected (boolean): if true the parameter is selected, otherwise it will be fixed
        
        
        """
        ...
    def setValue(self, double: float) -> None:
        """
            Set parameter value.
        
            If :code:`newValue` is below :meth:`~org.orekit.utils.ParameterDriver.getMinValue`, it will be silently set to
            :meth:`~org.orekit.utils.ParameterDriver.getMinValue`. If :code:`newValue` is above
            :meth:`~org.orekit.utils.ParameterDriver.getMaxValue`, it will be silently set to
            :meth:`~org.orekit.utils.ParameterDriver.getMaxValue`.
        
            Parameters:
                newValue (double): new value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a text representation of the parameter.
        
            Overrides:
                 in class 
        
            Returns:
                text representation of the parameter, in the form name = value.
        
        
        """
        ...

class ParameterFunction:
    """
    public interface ParameterFunction
    
        Interface representing a scalar function depending on a :class:`~org.orekit.utils.ParameterDriver`.
    
        Since:
            8.0
    
        Also see:
            :meth:`~org.orekit.utils.Differentiation.differentiate`
    """
    def value(self, parameterDriver: ParameterDriver) -> float:
        """
            Evaluate the function.
        
            Parameters:
                parameterDriver (:class:`~org.orekit.utils.ParameterDriver`): driver for the parameter.
        
            Returns:
                scalar value of the function
        
        
        """
        ...

class ParameterObserver:
    """
    public interface ParameterObserver
    
        Interface for observing parameters changes.
    
        Since:
            8.0
    
        Also see:
            :class:`~org.orekit.utils.ParameterDriver`
    """
    def maxValueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter maximum value has been changed.
        
            The default implementation does nothing
        
            Parameters:
                previousMaxValue (double): previous maximum value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def minValueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter minimum value has been changed.
        
            The default implementation does nothing
        
            Parameters:
                previousMinValue (double): previous minimum value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def nameChanged(self, string: str, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter name has been changed.
        
            The default implementation does nothing
        
            Parameters:
                previousName (String): previous name
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def referenceDateChanged(self, absoluteDate: org.orekit.time.AbsoluteDate, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter reference date has been changed.
        
            The default implementation does nothing
        
            Parameters:
                previousReferenceDate (:class:`~org.orekit.time.AbsoluteDate`): previous date (null if it is the first time the reference date is changed)
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def referenceValueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter reference value has been changed.
        
            The default implementation does nothing
        
            Parameters:
                previousReferenceValue (double): previous reference value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def scaleChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter scale has been changed.
        
            The default implementation does nothing
        
            Parameters:
                previousScale (double): previous scale
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def selectionChanged(self, boolean: bool, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter selection status has been changed.
        
            The default implementation does nothing
        
            Parameters:
                previousSelection (boolean): previous selection
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def valueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter value has been changed.
        
            Parameters:
                previousValue (double): previous value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
        
        """
        ...

class SecularAndHarmonic:
    """
    public class SecularAndHarmonic extends Object
    
        Class for fitting evolution of osculating orbital parameters.
    
        This class allows conversion from osculating parameters to mean parameters.
    """
    def __init__(self, int: int, doubleArray: typing.List[float]): ...
    def addPoint(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> None:
        """
            Add a fitting point.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the point
                osculatingValue (double): osculating value
        
        
        """
        ...
    def approximateAsPolynomialOnly(self, int: int, absoluteDate: org.orekit.time.AbsoluteDate, int2: int, int3: int, absoluteDate2: org.orekit.time.AbsoluteDate, absoluteDate3: org.orekit.time.AbsoluteDate, double: float) -> typing.List[float]:
        """
            Approximate an already fitted model to polynomial only terms.
        
            This method is mainly used in order to combine the large amplitude long periods with the secular part as a new
            approximate polynomial model over some time range. This should be used rather than simply extracting the polynomial
            coefficients from :meth:`~org.orekit.utils.SecularAndHarmonic.getFittedParameters` when some periodic terms amplitudes
            are large (for example Sun resonance effects on local solar time in sun synchronous orbits). In theses cases, the pure
            polynomial secular part in the coefficients may be far from the mean model.
        
            Parameters:
                combinedDegree (int): desired degree for the combined polynomial
                combinedReference (:class:`~org.orekit.time.AbsoluteDate`): desired reference date for the combined polynomial
                meanDegree (int): degree of polynomial secular part to consider
                meanHarmonics (int): number of harmonics terms to consider
                start (:class:`~org.orekit.time.AbsoluteDate`): start date of the approximation time range
                end (:class:`~org.orekit.time.AbsoluteDate`): end date of the approximation time range
                step (double): sampling step
        
            Returns:
                coefficients of the approximate polynomial (in increasing degree order), using the user provided reference date
        
        
        """
        ...
    def fit(self) -> None:
        """
            Fit parameters.
        
            Also see:
                :meth:`~org.orekit.utils.SecularAndHarmonic.getFittedParameters`
        
        
        """
        ...
    def getFittedParameters(self) -> typing.List[float]:
        """
            Get a copy of the last fitted parameters.
        
            Returns:
                copy of the last fitted parameters.
        
            Also see:
                :meth:`~org.orekit.utils.SecularAndHarmonic.fit`
        
        
        """
        ...
    def getHarmonicAmplitude(self) -> float:
        """
            Get an upper bound of the fitted harmonic amplitude.
        
            Returns:
                upper bound of the fitted harmonic amplitude
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the reference date.
        
            Returns:
                reference date
        
            Also see:
                :meth:`~org.orekit.utils.SecularAndHarmonic.resetFitting`
        
        
        """
        ...
    def meanDerivative(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int, int2: int) -> float:
        """
            Get mean derivative, truncated to first components.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                degree (int): degree of polynomial secular part to consider
                harmonics (int): number of harmonics terms to consider
        
            Returns:
                mean derivative at current date
        
        
        """
        ...
    def meanSecondDerivative(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int, int2: int) -> float:
        """
            Get mean second derivative, truncated to first components.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                degree (int): degree of polynomial secular part
                harmonics (int): number of harmonics terms to consider
        
            Returns:
                mean second derivative at current date
        
        
        """
        ...
    def meanValue(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int, int2: int) -> float:
        """
            Get mean value, truncated to first components.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                degree (int): degree of polynomial secular part to consider
                harmonics (int): number of harmonics terms to consider
        
            Returns:
                mean value at current date
        
        
        """
        ...
    def osculatingDerivative(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get fitted osculating derivative.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                osculating derivative at current date
        
        
        """
        ...
    def osculatingSecondDerivative(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get fitted osculating second derivative.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                osculating second derivative at current date
        
        
        """
        ...
    def osculatingValue(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get fitted osculating value.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                osculating value at current date
        
        
        """
        ...
    def resetFitting(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]) -> None:
        """
            Reset fitting.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): reference date
                initialGuess (double...): initial guess for the parameters
        
            Also see:
                :meth:`~org.orekit.utils.SecularAndHarmonic.getReferenceDate`
        
        
        """
        ...
    def setConvergenceRMS(self, double: float) -> None:
        """
            Set RMS for convergence.
        
            The RMS is the square-root of the sum of squared of the residuals, divided by the number of measurements.
        
            Parameters:
                convergenceRMS (double): RMS below which convergence is considered to have been reached
        
            Since:
                10.3
        
        
        """
        ...
    def setMaxIter(self, int: int) -> None:
        """
            Set maximum number of iterations.
        
            Parameters:
                maxIter (int): maximum number of iterations
        
            Since:
                10.3
        
        
        """
        ...

class StateFunction:
    """
    public interface StateFunction
    
        Interface representing a vector function depending on :class:`~org.orekit.propagation.SpacecraftState`.
    
        Since:
            8.0
    
        Also see:
            :meth:`~org.orekit.utils.Differentiation.differentiate`, :class:`~org.orekit.utils.StateJacobian`
    """
    def value(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
        """
            Evaluate the function.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state as the sole free parameter of the function.
        
            Returns:
                vector value of the function
        
        
        """
        ...

class StateJacobian:
    """
    public interface StateJacobian
    
        Interface representing the Jacobian of a vector function depending on :class:`~org.orekit.propagation.SpacecraftState`.
    
        Since:
            8.0
    
        Also see:
            :meth:`~org.orekit.utils.Differentiation.differentiate`, :class:`~org.orekit.utils.StateFunction`
    """
    def value(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[typing.List[float]]:
        """
            Evaluate the Jacobian of the function.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state as the sole free parameter of the function.
        
            Returns:
                Jacobian matric
        
        
        """
        ...

_TimeSpanMap__Span__S = typing.TypeVar('_TimeSpanMap__Span__S')  # <S>
_TimeSpanMap__Transition__S = typing.TypeVar('_TimeSpanMap__Transition__S')  # <S>
_TimeSpanMap__T = typing.TypeVar('_TimeSpanMap__T')  # <T>
class TimeSpanMap(typing.Generic[_TimeSpanMap__T]):
    """
    public class TimeSpanMap<T> extends Object
    
        Container for objects that apply to spans of time.
    
        Time span maps can be seen either as an ordered collection of :class:`~org.orekit.utils.TimeSpanMap.Span` or as an
        ordered collection of :class:`~org.orekit.utils.TimeSpanMap.Transition`. Both views are dual one to each other. A time
        span extends from one transition to the next one, and a transition separates one time span from the next one. Each time
        span contains one entry that is valid during the time span; this entry may be null if nothing is valid during this time
        span.
    
        Typical uses of :class:`~org.orekit.utils.TimeSpanMap` are to hold piecewise data, like for example an orbit count that
        changes at ascending nodes (in which case the entry would be an null), or a visibility status between several objects
        (in which case the entry would be a null) or a drag coefficient that is expected to be estimated daily or three-hourly
        (this is how :class:`~org.orekit.forces.drag.TimeSpanDragForce` is implemented).
    
        Time span maps are built progressively. At first, they contain one :class:`~org.orekit.utils.TimeSpanMap.Span` only
        whose validity extends from past infinity to future infinity. Then new entries are added one at a time, associated with
        transition dates, in order to build up the complete map. The transition dates can be either the start of validity (when
        calling :meth:`~org.orekit.utils.TimeSpanMap.addValidAfter`), or the end of the validity (when calling
        :meth:`~org.orekit.utils.TimeSpanMap.addValidBefore`). Entries are often added at one end only (and mainly in
        chronological order), but this is not required. It is possible for example to first set up a map that cover a large
        range (say one day), and then to insert intermediate dates using for example propagation and event detectors to carve
        out some parts. This is akin to the way Binary Space Partitioning Trees work.
    
        Since 11.1, this class is thread-safe
    
        Since:
            7.1
    """
    def __init__(self, t: _TimeSpanMap__T): ...
    @typing.overload
    def addValidAfter(self, t: _TimeSpanMap__T, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]: ...
    @typing.overload
    def addValidAfter(self, t: _TimeSpanMap__T, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    @typing.overload
    def addValidBefore(self, t: _TimeSpanMap__T, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]: ...
    @typing.overload
    def addValidBefore(self, t: _TimeSpanMap__T, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def addValidBetween(self, t: _TimeSpanMap__T, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]: ...
    def extractRange(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> 'TimeSpanMap'[_TimeSpanMap__T]: ...
    def forEach(self, consumer: typing.Union[java.util.function.Consumer[_TimeSpanMap__T], typing.Callable[[_TimeSpanMap__T], None]]) -> None: ...
    def get(self, absoluteDate: org.orekit.time.AbsoluteDate) -> _TimeSpanMap__T:
        """
            Get the entry valid at a specified date.
        
            The expected complexity is O(1) for successive calls with neighboring dates, which is the more frequent use in
            propagation or orbit determination applications, and O(n) for random calls.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the entry must be valid
        
            Returns:
                valid entry at specified date
        
            Also see:
                :meth:`~org.orekit.utils.TimeSpanMap.getSpan`
        
        
        """
        ...
    def getFirstSpan(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]: ...
    def getFirstTransition(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__T]: ...
    def getLastSpan(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]: ...
    def getLastTransition(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__T]: ...
    def getSpan(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]: ...
    def getSpansNumber(self) -> int:
        """
            Get the number of spans.
        
            The number of spans is always at least 1. The number of transitions is always 1 less than the number of spans.
        
            Returns:
                number of spans
        
            Since:
                11.1
        
        
        """
        ...
    def getTransitions(self) -> java.util.NavigableSet['TimeSpanMap.Transition'[_TimeSpanMap__T]]: ...
    class Span(typing.Generic[_TimeSpanMap__Span__S]):
        def getData(self) -> _TimeSpanMap__Span__S: ...
        def getEnd(self) -> org.orekit.time.AbsoluteDate: ...
        def getEndTransition(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__Span__S]: ...
        def getStart(self) -> org.orekit.time.AbsoluteDate: ...
        def getStartTransition(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__Span__S]: ...
        def next(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__Span__S]: ...
        def previous(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__Span__S]: ...
    class Transition(org.orekit.time.TimeStamped, typing.Generic[_TimeSpanMap__Transition__S]):
        def getAfter(self) -> _TimeSpanMap__Transition__S: ...
        def getBefore(self) -> _TimeSpanMap__Transition__S: ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getSpanAfter(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__Transition__S]: ...
        def getSpanBefore(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__Transition__S]: ...
        def next(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__Transition__S]: ...
        def previous(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__Transition__S]: ...

_TimeStampedCache__T = typing.TypeVar('_TimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class TimeStampedCache(typing.Generic[_TimeStampedCache__T]):
    """
    public interface TimeStampedCache<T extends :class:`~org.orekit.time.TimeStamped`>
    
        Interface for a data structure that can provide concurrent access to :class:`~org.orekit.time.TimeStamped` data
        surrounding a given date.
    
        Also see:
            :class:`~org.orekit.utils.GenericTimeStampedCache`, :class:`~org.orekit.utils.ImmutableTimeStampedCache`
    """
    def getEarliest(self) -> _TimeStampedCache__T: ...
    def getLatest(self) -> _TimeStampedCache__T: ...
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_TimeStampedCache__T]: ...
    def getNeighborsSize(self) -> int:
        """
            Get the fixed size of the lists returned by :meth:`~org.orekit.utils.TimeStampedCache.getNeighbors`.
        
            Returns:
                size of the list
        
        
        """
        ...

_TimeStampedGenerator__T = typing.TypeVar('_TimeStampedGenerator__T', bound=org.orekit.time.TimeStamped)  # <T>
class TimeStampedGenerator(typing.Generic[_TimeStampedGenerator__T]):
    """
    public interface TimeStampedGenerator<T extends :class:`~org.orekit.time.TimeStamped`>
    
        Generator to use for creating entries in :class:`~org.orekit.utils.GenericTimeStampedCache`.
    
        As long as a generator is referenced by one :class:`~org.orekit.utils.GenericTimeStampedCache` only, it is guaranteed to
        be called in a thread-safe way, even if the cache is used in a multi-threaded environment. The cache takes care of
        scheduling the calls to all the methods defined in this interface so only one thread uses them at any time. There is no
        need for the implementing classes to handle synchronization or locks by themselves.
    
        The generator is provided by the user of the :class:`~org.orekit.utils.GenericTimeStampedCache` and should be consistent
        with the way he will use the cached data.
    
        If entries must have regular time gaps (for example one entry every 3600 seconds), then the generator must ensure by
        itself all generated entries are exactly located on the expected regular grid, even if they are generated in random
        order. The reason for that is that the cache may ask for entries in different ranges and merge these ranges afterwards.
        A typical example would be a cache first calling the generator for 6 points around 2012-02-19T17:48:00 and when these
        points are exhausted calling the generator again for 6 new points around 2012-02-19T23:20:00. If all points must be
        exactly 3600 seconds apart, the generator should generate the first 6 points at 2012-02-19T15:00:00,
        2012-02-19T16:00:00, 2012-02-19T17:00:00, 2012-02-19T18:00:00, 2012-02-19T19:00:00 and 2012-02-19T20:00:00, and the next
        6 points at 2012-02-19T21:00:00, 2012-02-19T22:00:00, 2012-02-19T23:00:00, 2012-02-20T00:00:00, 2012-02-20T01:00:00 and
        2012-02-20T02:00:00. If the separation between the points is irrelevant, the first points could be generated at 17:48:00
        instead of 17:00:00 or 18:00:00. The cache *will* merge arrays returned from different calls in the same global time
        slot.
    """
    def generate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> java.util.List[_TimeStampedGenerator__T]: ...

class AbstractMultipleShooting(MultipleShooting):
    """
    public abstract class AbstractMultipleShooting extends Object implements :class:`~org.orekit.utils.MultipleShooting`
    
        Multiple shooting method using only constraints on state vectors of patch points (and possibly on epoch and integration
        time).
    
        Since:
            10.2
    
        Also see:
            "TRAJECTORY DESIGN AND ORBIT MAINTENANCE STRATEGIES IN MULTI-BODY DYNAMICAL REGIMES by Thomas A. Pavlak, Purdue
            University"
    """
    def addConstraint(self, int: int, int2: int, double: float) -> None:
        """
            Add a constraint on one component of one patch point.
        
            Parameters:
                patchNumber (int): Patch point with constraint
                componentIndex (int): Component of the patch points which are constrained.
                constraintValue (double): constraint value
        
        
        """
        ...
    def compute(self) -> java.util.List[org.orekit.propagation.SpacecraftState]: ...
    def setClosedOrbitConstraint(self, boolean: bool) -> None:
        """
            Set the constraint of a closed orbit or not.
        
            Parameters:
                isClosed (boolean): true if orbit should be closed
        
        
        """
        ...
    def setEpochFreedom(self, int: int, boolean: bool) -> None:
        """
            Set the epoch a patch point to free or not.
        
            Parameters:
                patchNumber (int): Patch point
                isFree (boolean): constraint value
        
        
        """
        ...
    def setPatchPointComponentFreedom(self, int: int, int2: int, boolean: bool) -> None:
        """
            Set a component of a patch point to free or not.
        
            Parameters:
                patchNumber (int): Patch point with constraint
                componentIndex (int): Component of the patch points which are constrained.
                isFree (boolean): constraint value
        
        
        """
        ...

class DateDriver(ParameterDriver, org.orekit.time.TimeStamped):
    """
    public class DateDriver extends :class:`~org.orekit.utils.ParameterDriver` implements :class:`~org.orekit.time.TimeStamped`
    
        :class:`~org.orekit.utils.ParameterDriver` allowing to drive a date.
    
        Since:
            11.1
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, string: str, boolean: bool): ...
    def getBaseDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the base (unshifted) date.
        
            Returns:
                base (unshifted) date
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the shifted date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                shifted date
        
        
        """
        ...
    def isStart(self) -> bool:
        """
            Check if driver corresponds to a start date.
        
            Returns:
                true if driver corresponds to a start date
        
        
        """
        ...

class ExtendedPVCoordinatesProvider(PVCoordinatesProvider):
    """
    public interface ExtendedPVCoordinatesProvider extends :class:`~org.orekit.utils.PVCoordinatesProvider`
    
        Interface for PV coordinates providers that also support fields.
    
        Since:
            9.2
    """
    _getPVCoordinates_0__T = typing.TypeVar('_getPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_0__T], frame: org.orekit.frames.Frame) -> 'TimeStampedFieldPVCoordinates'[_getPVCoordinates_0__T]:
        """
            Get the :class:`~org.orekit.utils.FieldPVCoordinates` of the body in the selected frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates': ...
    _toFieldPVCoordinatesProvider__T = typing.TypeVar('_toFieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toFieldPVCoordinatesProvider(self, field: org.hipparchus.Field[_toFieldPVCoordinatesProvider__T]) -> FieldPVCoordinatesProvider[_toFieldPVCoordinatesProvider__T]:
        """
            Convert to a :class:`~org.orekit.utils.FieldPVCoordinatesProvider` with a specific type.
        
            Parameters:
                field (Field<T> field): field for the argument and value
        
            Returns:
                converted function
        
        
        """
        ...

_GenericTimeStampedCache__T = typing.TypeVar('_GenericTimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class GenericTimeStampedCache(TimeStampedCache[_GenericTimeStampedCache__T], typing.Generic[_GenericTimeStampedCache__T]):
    """
    public class GenericTimeStampedCache<T extends :class:`~org.orekit.time.TimeStamped`> extends Object implements :class:`~org.orekit.utils.TimeStampedCache`<T>
    
        Generic thread-safe cache for :class:`~org.orekit.time.TimeStamped` data.
    """
    DEFAULT_CACHED_SLOTS_NUMBER: typing.ClassVar[int] = ...
    """
    public static final int DEFAULT_CACHED_SLOTS_NUMBER
    
        Default number of independent cached time slots.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, int: int, int2: int, double: float, double2: float, timeStampedGenerator: TimeStampedGenerator[_GenericTimeStampedCache__T]): ...
    def getEarliest(self) -> _GenericTimeStampedCache__T: ...
    def getEntries(self) -> int:
        """
            Get the total number of entries cached.
        
            Returns:
                total number of entries cached
        
        
        """
        ...
    def getGenerateCalls(self) -> int:
        """
            Get the number of calls to the generate method.
        
            This number of calls is related to the number of cache misses and may be used to tune the cache configuration. Each
            cache miss implies at least one call is performed, but may require several calls if the new date is far offset from the
            existing cache, depending on the number of elements and step between elements in the arrays returned by the generator.
        
            Returns:
                number of calls to the generate method
        
            Also see:
                :meth:`~org.orekit.utils.GenericTimeStampedCache.getGetNeighborsCalls`
        
        
        """
        ...
    def getGenerator(self) -> TimeStampedGenerator[_GenericTimeStampedCache__T]: ...
    def getGetNeighborsCalls(self) -> int:
        """
            Get the number of calls to the :meth:`~org.orekit.utils.GenericTimeStampedCache.getNeighbors` method.
        
            This number of calls is used as a reference to interpret
            :meth:`~org.orekit.utils.GenericTimeStampedCache.getGenerateCalls`.
        
            Returns:
                number of calls to the :meth:`~org.orekit.utils.GenericTimeStampedCache.getNeighbors` method
        
            Also see:
                :meth:`~org.orekit.utils.GenericTimeStampedCache.getGenerateCalls`
        
        
        """
        ...
    def getLatest(self) -> _GenericTimeStampedCache__T: ...
    def getMaxSlots(self) -> int:
        """
            Get the maximum number of independent cached time slots.
        
            Returns:
                maximum number of independent cached time slots
        
        
        """
        ...
    def getMaxSpan(self) -> float:
        """
            Get the maximum duration span in seconds of one slot.
        
            Returns:
                maximum duration span in seconds of one slot
        
        
        """
        ...
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_GenericTimeStampedCache__T]: ...
    def getNeighborsSize(self) -> int:
        """
            Get the fixed size of the arrays to be returned by :meth:`~org.orekit.utils.GenericTimeStampedCache.getNeighbors`.
        
            Specified by:
                :meth:`~org.orekit.utils.TimeStampedCache.getNeighborsSize` in interface :class:`~org.orekit.utils.TimeStampedCache`
        
            Returns:
                size of the array
        
        
        """
        ...
    def getNewSlotQuantumGap(self) -> float:
        """
            Get quantum gap above which a new slot is created instead of extending an existing one.
        
            The quantum gap is the :code:`newSlotInterval` value provided at construction rounded to the nearest quantum step used
            internally by the cache.
        
            Returns:
                quantum gap in seconds
        
        
        """
        ...
    def getSlots(self) -> int:
        """
            Get the number of slots in use.
        
            Returns:
                number of slots in use
        
        
        """
        ...
    def getSlotsEvictions(self) -> int:
        """
            Get the number of slots evictions.
        
            This number should remain small when the max number of slots is sufficient with respect to the number of concurrent
            requests to the cache. If it increases too much, then the cache configuration is probably bad and cache does not really
            improve things (in this case, the :meth:`~org.orekit.utils.GenericTimeStampedCache.getGenerateCalls` will probably
            increase too.
        
            Returns:
                number of slots evictions
        
        
        """
        ...

_ImmutableTimeStampedCache__T = typing.TypeVar('_ImmutableTimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class ImmutableTimeStampedCache(TimeStampedCache[_ImmutableTimeStampedCache__T], typing.Generic[_ImmutableTimeStampedCache__T]):
    """
    public class ImmutableTimeStampedCache<T extends :class:`~org.orekit.time.TimeStamped`> extends Object implements :class:`~org.orekit.utils.TimeStampedCache`<T>
    
        A cache of :class:`~org.orekit.time.TimeStamped` data that provides concurrency through immutability. This strategy is
        suitable when all of the cached data is stored in memory. (For example, :class:`~org.orekit.time.UTCScale`) This class
        then provides convenient methods for accessing the data.
    """
    def __init__(self, int: int, collection: typing.Union[java.util.Collection[_ImmutableTimeStampedCache__T], typing.Sequence[_ImmutableTimeStampedCache__T], typing.Set[_ImmutableTimeStampedCache__T]]): ...
    _emptyCache__TS = typing.TypeVar('_emptyCache__TS', bound=org.orekit.time.TimeStamped)  # <TS>
    @staticmethod
    def emptyCache() -> 'ImmutableTimeStampedCache'[_emptyCache__TS]: ...
    def getAll(self) -> java.util.List[_ImmutableTimeStampedCache__T]: ...
    def getEarliest(self) -> _ImmutableTimeStampedCache__T:
        """
            Get the earliest entry in this cache.
        
            Specified by:
                :meth:`~org.orekit.utils.TimeStampedCache.getEarliest` in interface :class:`~org.orekit.utils.TimeStampedCache`
        
            Returns:
                earliest cached entry
        
        
        """
        ...
    def getLatest(self) -> _ImmutableTimeStampedCache__T:
        """
            Get the latest entry in this cache.
        
            Specified by:
                :meth:`~org.orekit.utils.TimeStampedCache.getLatest` in interface :class:`~org.orekit.utils.TimeStampedCache`
        
            Returns:
                latest cached entry
        
        
        """
        ...
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_ImmutableTimeStampedCache__T]: ...
    def getNeighborsSize(self) -> int:
        """
            Get the fixed size of the lists returned by :meth:`~org.orekit.utils.TimeStampedCache.getNeighbors`.
        
            Specified by:
                :meth:`~org.orekit.utils.TimeStampedCache.getNeighborsSize` in interface :class:`~org.orekit.utils.TimeStampedCache`
        
            Returns:
                size of the list
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterDriversList:
    """
    public class ParameterDriversList extends Object
    
        Class managing several :class:`~org.orekit.utils.ParameterDriver`, taking care of duplicated names.
    
        Once parameter drivers sharing the same name have been added to an instance of this class, they are permanently bound
        together and also bound to the :meth:`~org.orekit.utils.ParameterDriversList.getDrivers` that manages them. This means
        that if drivers :code:`d1`, :code:`d2`... :code:`dn` are added to the list and both correspond to parameter name "P",
        then :meth:`~org.orekit.utils.ParameterDriversList.getDrivers` will return a list containing a delegating driver
        :code:`delegateD` for the same name "P". Afterwards, whenever either :meth:`~org.orekit.utils.ParameterDriver.setValue`
        or :meth:`~org.orekit.utils.ParameterDriver.setReferenceDate` is called on any of the :code:`n+1` instances :code:`d1`,
        :code:`d2`... :code:`dn` or :code:`delegateD`, the call will be automatically forwarded to the :code:`n` remaining
        instances, hence ensuring they remain consistent with each other.
    
        Since:
            8.0
    """
    def __init__(self): ...
    def add(self, parameterDriver: ParameterDriver) -> None:
        """
            Add a driver.
        
            If the driver is already present, it will not be added. If another driver managing the same parameter is present, both
            drivers will be managed together, existing drivers being set to the value of the last driver added (i.e. each addition
            overrides the parameter value).
        
            Parameters:
                driver (:class:`~org.orekit.utils.ParameterDriver`): driver to add
        
        
        """
        ...
    def filter(self, boolean: bool) -> None:
        """
            Filter parameters to keep only one type of selection status.
        
            Parameters:
                selected (boolean): if true, only :meth:`~org.orekit.utils.ParameterDriver.isSelected` parameters will be kept, the other ones will be
                    removed
        
        
        """
        ...
    def findByName(self, string: str) -> 'ParameterDriversList.DelegatingDriver':
        """
            Find a :class:`~org.orekit.utils.ParameterDriversList.DelegatingDriver` by name.
        
            Parameters:
                name (String): name to check
        
            Returns:
                a :class:`~org.orekit.utils.ParameterDriversList.DelegatingDriver` managing this parameter name
        
            Since:
                9.1
        
        
        """
        ...
    def getDrivers(self) -> java.util.List['ParameterDriversList.DelegatingDriver']: ...
    def getNbParams(self) -> int:
        """
            Get the number of parameters with different names.
        
            Returns:
                number of parameters with different names
        
        
        """
        ...
    def sort(self) -> None:
        """
            Sort the parameters lexicographically.
        
        """
        ...
    class DelegatingDriver(ParameterDriver):
        def getRawDrivers(self) -> java.util.List[ParameterDriver]: ...

_PythonFieldPVCoordinatesProvider__T = typing.TypeVar('_PythonFieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldPVCoordinatesProvider(FieldPVCoordinatesProvider[_PythonFieldPVCoordinatesProvider__T], typing.Generic[_PythonFieldPVCoordinatesProvider__T]):
    """
    public class PythonFieldPVCoordinatesProvider<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> 'TimeStampedFieldPVCoordinates'[_PythonFieldPVCoordinatesProvider__T]: ...
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

class PythonMultipleShooting(MultipleShooting):
    """
    public class PythonMultipleShooting extends Object implements :class:`~org.orekit.utils.MultipleShooting`
    """
    def __init__(self): ...
    def compute(self) -> java.util.List[org.orekit.propagation.SpacecraftState]: ...
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

class PythonPVCoordinatesProvider(PVCoordinatesProvider):
    """
    public class PythonPVCoordinatesProvider extends Object implements :class:`~org.orekit.utils.PVCoordinatesProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
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

class PythonParameterFunction(ParameterFunction):
    """
    public class PythonParameterFunction extends Object implements :class:`~org.orekit.utils.ParameterFunction`
    """
    def __init__(self): ...
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
    def value(self, parameterDriver: ParameterDriver) -> float:
        """
            Evaluate the function.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterFunction.value` in interface :class:`~org.orekit.utils.ParameterFunction`
        
            Parameters:
                parameterDriver (:class:`~org.orekit.utils.ParameterDriver`): driver for the parameter.
        
            Returns:
                scalar value of the function
        
        
        """
        ...

class PythonParameterObserver(ParameterObserver):
    """
    public class PythonParameterObserver extends Object implements :class:`~org.orekit.utils.ParameterObserver`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def maxValueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter maximum value has been changed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.maxValueChanged` in interface :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousMaxValue (double): previous maximum value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def minValueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter minimum value has been changed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.minValueChanged` in interface :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousMinValue (double): previous minimum value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def nameChanged(self, string: str, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter name has been changed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.nameChanged` in interface :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousName (String): previous name
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
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
    def referenceDateChanged(self, absoluteDate: org.orekit.time.AbsoluteDate, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter reference date has been changed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.referenceDateChanged`Â in
                interfaceÂ :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousReferenceDate (:class:`~org.orekit.time.AbsoluteDate`): previous date (null if it is the first time the reference date is changed)
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def referenceValueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter reference value has been changed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.referenceValueChanged`Â in
                interfaceÂ :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousReferenceValue (double): previous reference value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def scaleChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter scale has been changed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.scaleChanged` in interface :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousScale (double): previous scale
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def selectionChanged(self, boolean: bool, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter selection status has been changed.
        
            The default implementation does nothing
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.selectionChanged` in interface :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousSelection (boolean): previous selection
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
            Since:
                9.0
        
        
        """
        ...
    def valueChanged(self, double: float, parameterDriver: ParameterDriver) -> None:
        """
            Notify that a parameter value has been changed.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterObserver.valueChanged` in interface :class:`~org.orekit.utils.ParameterObserver`
        
            Parameters:
                previousValue (double): previous value
                driver (:class:`~org.orekit.utils.ParameterDriver`): parameter driver that has been changed
        
        
        """
        ...

class PythonStateFunction(StateFunction):
    """
    public class PythonStateFunction extends Object implements :class:`~org.orekit.utils.StateFunction`
    """
    def __init__(self): ...
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
    def value(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
        """
            Evaluate the function.
        
            Specified by:
                :meth:`~org.orekit.utils.StateFunction.value` in interface :class:`~org.orekit.utils.StateFunction`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state as the sole free parameter of the function.
        
            Returns:
                vector value of the function
        
        
        """
        ...

class PythonStateJacobian(StateJacobian):
    """
    public class PythonStateJacobian extends Object implements :class:`~org.orekit.utils.StateJacobian`
    """
    def __init__(self): ...
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
    def value(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[typing.List[float]]:
        """
            Evaluate the Jacobian of the function.
        
            Specified by:
                :meth:`~org.orekit.utils.StateJacobian.value` in interface :class:`~org.orekit.utils.StateJacobian`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state as the sole free parameter of the function.
        
            Returns:
                Jacobian matric
        
        
        """
        ...

_PythonTimeStampedCache__T = typing.TypeVar('_PythonTimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class PythonTimeStampedCache(TimeStampedCache[_PythonTimeStampedCache__T], typing.Generic[_PythonTimeStampedCache__T]):
    """
    public class PythonTimeStampedCache<T extends :class:`~org.orekit.time.TimeStamped`> extends Object implements :class:`~org.orekit.utils.TimeStampedCache`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getEarliest(self) -> _PythonTimeStampedCache__T: ...
    def getLatest(self) -> _PythonTimeStampedCache__T: ...
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_PythonTimeStampedCache__T]: ...
    def getNeighborsSize(self) -> int:
        """
            Get the fixed size of the lists returned by :meth:`~org.orekit.utils.PythonTimeStampedCache.getNeighbors`.
        
            Specified by:
                :meth:`~org.orekit.utils.TimeStampedCache.getNeighborsSize` in interface :class:`~org.orekit.utils.TimeStampedCache`
        
            Returns:
                size of the list
        
        
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

_PythonTimeStampedGenerator__T = typing.TypeVar('_PythonTimeStampedGenerator__T', bound=org.orekit.time.TimeStamped)  # <T>
class PythonTimeStampedGenerator(TimeStampedGenerator[_PythonTimeStampedGenerator__T], typing.Generic[_PythonTimeStampedGenerator__T]):
    """
    public class PythonTimeStampedGenerator<T extends :class:`~org.orekit.time.TimeStamped`> extends Object implements :class:`~org.orekit.utils.TimeStampedGenerator`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def generate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> java.util.List[_PythonTimeStampedGenerator__T]: ...
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

class TimeStampedAngularCoordinates(AngularCoordinates, org.orekit.time.TimeStamped):
    """
    public class TimeStampedAngularCoordinates extends :class:`~org.orekit.utils.AngularCoordinates` implements :class:`~org.orekit.time.TimeStamped`
    
        :class:`~org.orekit.time.TimeStamped` version of :class:`~org.orekit.utils.AngularCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            7.0
    
        Also see:
            :meth:`~serialized`
    """
    ___init___0__U = typing.TypeVar('___init___0__U', bound=org.hipparchus.analysis.differentiation.Derivative)  # <U>
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[___init___0__U]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: PVCoordinates, pVCoordinates2: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: PVCoordinates, pVCoordinates2: PVCoordinates, pVCoordinates3: PVCoordinates, pVCoordinates4: PVCoordinates, double: float): ...
    def addOffset(self, angularCoordinates: AngularCoordinates) -> 'TimeStampedAngularCoordinates':
        """
            Add an offset from the instance.
        
            We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular
            coordinates do *not* commute under this operation, i.e. :code:`a.addOffset(b)` and :code:`b.addOffset(a)` lead to
            *different* results in most cases.
        
            The two methods :meth:`~org.orekit.utils.TimeStampedAngularCoordinates.addOffset` and
            :meth:`~org.orekit.utils.TimeStampedAngularCoordinates.subtractOffset` are designed so that round trip applications are
            possible. This means that both :code:`ac1.subtractOffset(ac2).addOffset(ac2)` and
            :code:`ac1.addOffset(ac2).subtractOffset(ac2)` return angular coordinates equal to ac1.
        
            Overrides:
                :meth:`~org.orekit.utils.AngularCoordinates.addOffset` in class :class:`~org.orekit.utils.AngularCoordinates`
        
            Parameters:
                offset (:class:`~org.orekit.utils.AngularCoordinates`): offset to subtract
        
            Returns:
                new instance, with offset subtracted
        
            Also see:
                :meth:`~org.orekit.utils.TimeStampedAngularCoordinates.subtractOffset`
        
        
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
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, angularDerivativesFilter: AngularDerivativesFilter, collection: typing.Union[java.util.Collection['TimeStampedAngularCoordinates'], typing.Sequence['TimeStampedAngularCoordinates'], typing.Set['TimeStampedAngularCoordinates']]) -> 'TimeStampedAngularCoordinates': ...
    def revert(self) -> 'TimeStampedAngularCoordinates':
        """
            Revert a rotation/rotation rate pair. Build a pair which reverse the effect of another pair.
        
            Overrides:
                :meth:`~org.orekit.utils.AngularCoordinates.revert` in class :class:`~org.orekit.utils.AngularCoordinates`
        
            Returns:
                a new pair whose effect is the reverse of the effect of the instance
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'TimeStampedAngularCoordinates':
        """
            Get a time-shifted state.
        
            The state can be slightly shifted to close dates. This shift is based on a simple linear model. It is *not* intended as
            a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Overrides:
                :meth:`~org.orekit.utils.AngularCoordinates.shiftedBy` in class :class:`~org.orekit.utils.AngularCoordinates`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def subtractOffset(self, angularCoordinates: AngularCoordinates) -> 'TimeStampedAngularCoordinates':
        """
            Subtract an offset from the instance.
        
            We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular
            coordinates do *not* commute under this operation, i.e. :code:`a.subtractOffset(b)` and :code:`b.subtractOffset(a)` lead
            to *different* results in most cases.
        
            The two methods :meth:`~org.orekit.utils.TimeStampedAngularCoordinates.addOffset` and
            :meth:`~org.orekit.utils.TimeStampedAngularCoordinates.subtractOffset` are designed so that round trip applications are
            possible. This means that both :code:`ac1.subtractOffset(ac2).addOffset(ac2)` and
            :code:`ac1.addOffset(ac2).subtractOffset(ac2)` return angular coordinates equal to ac1.
        
            Overrides:
                :meth:`~org.orekit.utils.AngularCoordinates.subtractOffset` in class :class:`~org.orekit.utils.AngularCoordinates`
        
            Parameters:
                offset (:class:`~org.orekit.utils.AngularCoordinates`): offset to subtract
        
            Returns:
                new instance, with offset subtracted
        
            Also see:
                :meth:`~org.orekit.utils.TimeStampedAngularCoordinates.addOffset`
        
        
        """
        ...

_TimeStampedFieldAngularCoordinates__T = typing.TypeVar('_TimeStampedFieldAngularCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class TimeStampedFieldAngularCoordinates(FieldAngularCoordinates[_TimeStampedFieldAngularCoordinates__T], org.orekit.time.FieldTimeStamped[_TimeStampedFieldAngularCoordinates__T], typing.Generic[_TimeStampedFieldAngularCoordinates__T]):
    """
    public class TimeStampedFieldAngularCoordinates<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.utils.FieldAngularCoordinates`<T> implements :class:`~org.orekit.time.FieldTimeStamped`<T>
    
        :class:`~org.orekit.time.TimeStamped` version of :class:`~org.orekit.utils.FieldAngularCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            7.0
    """
    ___init___3__U = typing.TypeVar('___init___3__U', bound=org.hipparchus.analysis.differentiation.FieldDerivative)  # <U>
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_TimeStampedFieldAngularCoordinates__T], timeStampedAngularCoordinates: TimeStampedAngularCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_TimeStampedFieldAngularCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldAngularCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldAngularCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], fieldPVCoordinates4: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], double: float): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldAngularCoordinates__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[___init___3__U]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldAngularCoordinates__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_TimeStampedFieldAngularCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldAngularCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldAngularCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldAngularCoordinates__T], fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], fieldPVCoordinates4: FieldPVCoordinates[_TimeStampedFieldAngularCoordinates__T], double: float): ...
    def addOffset(self, fieldAngularCoordinates: FieldAngularCoordinates[_TimeStampedFieldAngularCoordinates__T]) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldAngularCoordinates__T]: ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_1__T = typing.TypeVar('_interpolate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, angularDerivativesFilter: AngularDerivativesFilter, collection: typing.Union[java.util.Collection['TimeStampedFieldAngularCoordinates'[_interpolate_0__T]], typing.Sequence['TimeStampedFieldAngularCoordinates'[_interpolate_0__T]], typing.Set['TimeStampedFieldAngularCoordinates'[_interpolate_0__T]]]) -> 'TimeStampedFieldAngularCoordinates'[_interpolate_0__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_1__T], angularDerivativesFilter: AngularDerivativesFilter, collection: typing.Union[java.util.Collection['TimeStampedFieldAngularCoordinates'[_interpolate_1__T]], typing.Sequence['TimeStampedFieldAngularCoordinates'[_interpolate_1__T]], typing.Set['TimeStampedFieldAngularCoordinates'[_interpolate_1__T]]]) -> 'TimeStampedFieldAngularCoordinates'[_interpolate_1__T]: ...
    def revert(self) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _TimeStampedFieldAngularCoordinates__T) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]: ...
    def subtractOffset(self, fieldAngularCoordinates: FieldAngularCoordinates[_TimeStampedFieldAngularCoordinates__T]) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]: ...

_TimeStampedFieldPVCoordinates__T = typing.TypeVar('_TimeStampedFieldPVCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class TimeStampedFieldPVCoordinates(FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], org.orekit.time.FieldTimeStamped[_TimeStampedFieldPVCoordinates__T], typing.Generic[_TimeStampedFieldPVCoordinates__T]):
    """
    public class TimeStampedFieldPVCoordinates<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.utils.FieldPVCoordinates`<T> implements :class:`~org.orekit.time.FieldTimeStamped`<T>
    
        :class:`~org.orekit.time.TimeStamped` version of :class:`~org.orekit.utils.FieldPVCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            7.0
    """
    ___init___27__U = typing.TypeVar('___init___27__U', bound=org.hipparchus.analysis.differentiation.FieldDerivative)  # <U>
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double2: float, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double2: float, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double3: float, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double2: float, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double3: float, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double4: float, fieldPVCoordinates4: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t2: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t2: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t3: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t2: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t3: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t4: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates4: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates, t2: _TimeStampedFieldPVCoordinates__T, pVCoordinates2: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates, t2: _TimeStampedFieldPVCoordinates__T, pVCoordinates2: PVCoordinates, t3: _TimeStampedFieldPVCoordinates__T, pVCoordinates3: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates, t2: _TimeStampedFieldPVCoordinates__T, pVCoordinates2: PVCoordinates, t3: _TimeStampedFieldPVCoordinates__T, pVCoordinates3: PVCoordinates, t4: _TimeStampedFieldPVCoordinates__T, pVCoordinates4: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T], fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double2: float, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double2: float, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double3: float, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], double: float, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double2: float, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double3: float, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], double4: float, fieldPVCoordinates4: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t2: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t2: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t3: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t2: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t3: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates3: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], t4: _TimeStampedFieldPVCoordinates__T, fieldPVCoordinates4: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates, t2: _TimeStampedFieldPVCoordinates__T, pVCoordinates2: PVCoordinates): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates, t2: _TimeStampedFieldPVCoordinates__T, pVCoordinates2: PVCoordinates, t3: _TimeStampedFieldPVCoordinates__T, pVCoordinates3: PVCoordinates): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], t: _TimeStampedFieldPVCoordinates__T, pVCoordinates: PVCoordinates, t2: _TimeStampedFieldPVCoordinates__T, pVCoordinates2: PVCoordinates, t3: _TimeStampedFieldPVCoordinates__T, pVCoordinates3: PVCoordinates, t4: _TimeStampedFieldPVCoordinates__T, pVCoordinates4: PVCoordinates): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___27__U]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T], fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T]: ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_1__T = typing.TypeVar('_interpolate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_0__T], cartesianDerivativesFilter: CartesianDerivativesFilter, collection: typing.Union[java.util.Collection['TimeStampedFieldPVCoordinates'[_interpolate_0__T]], typing.Sequence['TimeStampedFieldPVCoordinates'[_interpolate_0__T]], typing.Set['TimeStampedFieldPVCoordinates'[_interpolate_0__T]]]) -> 'TimeStampedFieldPVCoordinates'[_interpolate_0__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_1__T], cartesianDerivativesFilter: CartesianDerivativesFilter, stream: java.util.stream.Stream['TimeStampedFieldPVCoordinates'[_interpolate_1__T]]) -> 'TimeStampedFieldPVCoordinates'[_interpolate_1__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'TimeStampedFieldPVCoordinates'[_TimeStampedFieldPVCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _TimeStampedFieldPVCoordinates__T) -> 'TimeStampedFieldPVCoordinates'[_TimeStampedFieldPVCoordinates__T]: ...
    @typing.overload
    def toString(self) -> str:
        """
            Return a string representation of this date, position, velocity, and acceleration.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Overrides:
                :meth:`~org.orekit.utils.FieldPVCoordinates.toString` in class :class:`~org.orekit.utils.FieldPVCoordinates`
        
            Returns:
                string representation of this.
        
        """
        ...
    @typing.overload
    def toString(self, timeScale: org.orekit.time.TimeScale) -> str:
        """
            Return a string representation of this date, position, velocity, and acceleration.
        
            Parameters:
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to print the date.
        
            Returns:
                string representation of this.
        
        
        """
        ...
    def toTimeStampedPVCoordinates(self) -> 'TimeStampedPVCoordinates':
        """
            Convert to a constant position-velocity.
        
            Returns:
                a constant position-velocity
        
            Since:
                9.0
        
        
        """
        ...

class TimeStampedPVCoordinates(PVCoordinates, org.orekit.time.TimeStamped):
    """
    public class TimeStampedPVCoordinates extends :class:`~org.orekit.utils.PVCoordinates` implements :class:`~org.orekit.time.TimeStamped`
    
        :class:`~org.orekit.time.TimeStamped` version of :class:`~org.orekit.utils.PVCoordinates`.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            7.0
    
        Also see:
            :meth:`~serialized`
    """
    ___init___4__U = typing.TypeVar('___init___4__U', bound=org.hipparchus.analysis.differentiation.Derivative)  # <U>
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, pVCoordinates: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, pVCoordinates: PVCoordinates, double2: float, pVCoordinates2: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, pVCoordinates: PVCoordinates, double2: float, pVCoordinates2: PVCoordinates, double3: float, pVCoordinates3: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, pVCoordinates: PVCoordinates, double2: float, pVCoordinates2: PVCoordinates, double3: float, pVCoordinates3: PVCoordinates, double4: float, pVCoordinates4: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___4__U]): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: PVCoordinates, pVCoordinates2: PVCoordinates): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, cartesianDerivativesFilter: CartesianDerivativesFilter, collection: typing.Union[java.util.Collection['TimeStampedPVCoordinates'], typing.Sequence['TimeStampedPVCoordinates'], typing.Set['TimeStampedPVCoordinates']]) -> 'TimeStampedPVCoordinates': ...
    @typing.overload
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, cartesianDerivativesFilter: CartesianDerivativesFilter, stream: java.util.stream.Stream['TimeStampedPVCoordinates']) -> 'TimeStampedPVCoordinates': ...
    def shiftedBy(self, double: float) -> 'TimeStampedPVCoordinates':
        """
            Get a time-shifted state.
        
            The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is *not* intended
            as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time
            shifts or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Overrides:
                :meth:`~org.orekit.utils.PVCoordinates.shiftedBy` in class :class:`~org.orekit.utils.PVCoordinates`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
            Return a string representation of this date, position, velocity, and acceleration.
        
            This method uses the :meth:`~org.orekit.data.DataContext.getDefault`.
        
            Overrides:
                :meth:`~org.orekit.utils.PVCoordinates.toString` in class :class:`~org.orekit.utils.PVCoordinates`
        
            Returns:
                string representation of this.
        
        """
        ...
    @typing.overload
    def toString(self, timeScale: org.orekit.time.TimeScale) -> str:
        """
            Return a string representation of this date, position, velocity, and acceleration.
        
            Parameters:
                utc (:class:`~org.orekit.time.TimeScale`): time scale used to print the date.
        
            Returns:
                string representation of this.
        
        
        """
        ...
    def toTaylorProvider(self, frame: org.orekit.frames.Frame) -> PVCoordinatesProvider:
        """
            Create a local provider using simply Taylor expansion through
            :meth:`~org.orekit.utils.TimeStampedPVCoordinates.shiftedBy`.
        
            The time evolution is based on a simple Taylor expansion. It is *not* intended as a replacement for proper orbit
            propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
            Parameters:
                instanceFrame (:class:`~org.orekit.frames.Frame`): frame in which the instance is defined
        
            Returns:
                provider based on Taylor expansion, for small time shifts around instance date
        
        
        """
        ...

class AbsolutePVCoordinates(TimeStampedPVCoordinates, org.orekit.time.TimeStamped, org.orekit.time.TimeInterpolable['AbsolutePVCoordinates'], java.io.Serializable, PVCoordinatesProvider):
    """
    public class AbsolutePVCoordinates extends :class:`~org.orekit.utils.TimeStampedPVCoordinates` implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeInterpolable`<:class:`~org.orekit.utils.AbsolutePVCoordinates`>, Serializable, :class:`~org.orekit.utils.PVCoordinatesProvider`
    
        Position - Velocity - Acceleration linked to a date and a frame.
    
        Also see:
            :meth:`~serialized`
    """
    ___init___0__U = typing.TypeVar('___init___0__U', bound=org.hipparchus.analysis.differentiation.Derivative)  # <U>
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___0__U]): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: PVCoordinates): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeStampedPVCoordinates: TimeStampedPVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, absolutePVCoordinates: 'AbsolutePVCoordinates'): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, absolutePVCoordinates: 'AbsolutePVCoordinates', double2: float, absolutePVCoordinates2: 'AbsolutePVCoordinates'): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, absolutePVCoordinates: 'AbsolutePVCoordinates', double2: float, absolutePVCoordinates2: 'AbsolutePVCoordinates', double3: float, absolutePVCoordinates3: 'AbsolutePVCoordinates'): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, absolutePVCoordinates: 'AbsolutePVCoordinates', double2: float, absolutePVCoordinates2: 'AbsolutePVCoordinates', double3: float, absolutePVCoordinates3: 'AbsolutePVCoordinates', double4: float, absolutePVCoordinates4: 'AbsolutePVCoordinates'): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, absolutePVCoordinates: 'AbsolutePVCoordinates', absolutePVCoordinates2: 'AbsolutePVCoordinates'): ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the coordinates are defined.
        
            Returns:
                frame in which the coordinates are defined
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> TimeStampedPVCoordinates:
        """
            Get the TimeStampedPVCoordinates.
        
            Returns:
                TimeStampedPVCoordinates
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates:
        """
            Get the TimeStampedPVCoordinates in a specified frame.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): frame in which the position/velocity coordinates shall be computed
        
            Returns:
                TimeStampedPVCoordinates
        
            Raises:
                :class:`~org.orekit.errors.OrekitException`: if transformation between frames cannot be computed
        
            Also see:
                :meth:`~org.orekit.utils.AbsolutePVCoordinates.getPVCoordinates`
        
            Description copied from interface: :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                otherDate (:class:`~org.orekit.time.AbsoluteDate`): current date
                outputFrame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream['AbsolutePVCoordinates']) -> 'AbsolutePVCoordinates': ...
    @typing.overload
    @staticmethod
    def interpolate(frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, cartesianDerivativesFilter: CartesianDerivativesFilter, stream: java.util.stream.Stream['AbsolutePVCoordinates']) -> 'AbsolutePVCoordinates': ...
    @typing.overload
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, cartesianDerivativesFilter: CartesianDerivativesFilter, collection: typing.Union[java.util.Collection[TimeStampedPVCoordinates], typing.Sequence[TimeStampedPVCoordinates], typing.Set[TimeStampedPVCoordinates]]) -> TimeStampedPVCoordinates: ...
    @typing.overload
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, cartesianDerivativesFilter: CartesianDerivativesFilter, stream: java.util.stream.Stream[TimeStampedPVCoordinates]) -> TimeStampedPVCoordinates: ...
    def shiftedBy(self, double: float) -> 'AbsolutePVCoordinates':
        """
            Get a time-shifted state.
        
            The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is *not* intended
            as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time
            shifts or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Overrides:
                :meth:`~org.orekit.utils.TimeStampedPVCoordinates.shiftedBy`Â in
                classÂ :class:`~org.orekit.utils.TimeStampedPVCoordinates`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def toTaylorProvider(self) -> PVCoordinatesProvider:
        """
            Create a local provider using simply Taylor expansion through :meth:`~org.orekit.utils.AbsolutePVCoordinates.shiftedBy`.
        
            The time evolution is based on a simple Taylor expansion. It is *not* intended as a replacement for proper orbit
            propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
            Returns:
                provider based on Taylor expansion, for small time shifts around instance date
        
        
        """
        ...
    @typing.overload
    def toTaylorProvider(self, frame: org.orekit.frames.Frame) -> PVCoordinatesProvider: ...

_FieldAbsolutePVCoordinates__T = typing.TypeVar('_FieldAbsolutePVCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbsolutePVCoordinates(TimeStampedFieldPVCoordinates[_FieldAbsolutePVCoordinates__T], org.orekit.time.FieldTimeStamped[_FieldAbsolutePVCoordinates__T], org.orekit.time.FieldTimeInterpolable['FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], _FieldAbsolutePVCoordinates__T], FieldPVCoordinatesProvider[_FieldAbsolutePVCoordinates__T], typing.Generic[_FieldAbsolutePVCoordinates__T]):
    """
    public class FieldAbsolutePVCoordinates<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.utils.TimeStampedFieldPVCoordinates`<T> implements :class:`~org.orekit.time.FieldTimeStamped`<T>, :class:`~org.orekit.time.FieldTimeInterpolable`<:class:`~org.orekit.utils.FieldAbsolutePVCoordinates`<T>,T>, :class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T>
    
        Field implementation of AbsolutePVCoordinates.
    
        Also see:
            :class:`~org.orekit.utils.AbsolutePVCoordinates`
    """
    ___init___0__U = typing.TypeVar('___init___0__U', bound=org.hipparchus.analysis.differentiation.FieldDerivative)  # <U>
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___0__U]): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T], fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], fieldPVCoordinates: FieldPVCoordinates[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeStampedFieldPVCoordinates: TimeStampedFieldPVCoordinates[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], t: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], t: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], t2: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates2: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], t: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], t2: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates2: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], t3: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates3: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], t: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], t2: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates2: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], t3: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates3: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], t4: _FieldAbsolutePVCoordinates__T, fieldAbsolutePVCoordinates4: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], fieldAbsolutePVCoordinates: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T], fieldAbsolutePVCoordinates2: 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]): ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the coordinates are defined.
        
            Returns:
                frame in which the coordinates are defined
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> TimeStampedFieldPVCoordinates[_FieldAbsolutePVCoordinates__T]: ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_FieldAbsolutePVCoordinates__T]: ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_FieldAbsolutePVCoordinates__T]: ...
    _interpolate_2__T = typing.TypeVar('_interpolate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_3__T = typing.TypeVar('_interpolate_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_4__T = typing.TypeVar('_interpolate_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], collection: typing.Union[java.util.Collection[_FieldAbsolutePVCoordinates__T], typing.Sequence[_FieldAbsolutePVCoordinates__T], typing.Set[_FieldAbsolutePVCoordinates__T]]) -> _FieldAbsolutePVCoordinates__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], stream: java.util.stream.Stream['FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]]) -> 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_2__T], cartesianDerivativesFilter: CartesianDerivativesFilter, stream: java.util.stream.Stream['FieldAbsolutePVCoordinates'[_interpolate_2__T]]) -> 'FieldAbsolutePVCoordinates'[_interpolate_2__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_3__T], cartesianDerivativesFilter: CartesianDerivativesFilter, collection: typing.Union[java.util.Collection[TimeStampedFieldPVCoordinates[_interpolate_3__T]], typing.Sequence[TimeStampedFieldPVCoordinates[_interpolate_3__T]], typing.Set[TimeStampedFieldPVCoordinates[_interpolate_3__T]]]) -> TimeStampedFieldPVCoordinates[_interpolate_3__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_4__T], cartesianDerivativesFilter: CartesianDerivativesFilter, stream: java.util.stream.Stream[TimeStampedFieldPVCoordinates[_interpolate_4__T]]) -> TimeStampedFieldPVCoordinates[_interpolate_4__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAbsolutePVCoordinates__T) -> 'FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinates__T]: ...
    def toAbsolutePVCoordinates(self) -> AbsolutePVCoordinates:
        """
            Converts to an AbsolutePVCoordinates instance.
        
            Returns:
                AbsolutePVCoordinates with same properties
        
        
        """
        ...
    def toTaylorProvider(self) -> FieldPVCoordinatesProvider[_FieldAbsolutePVCoordinates__T]: ...

class MultipleShooter(AbstractMultipleShooting):
    """
    public class MultipleShooter extends :class:`~org.orekit.utils.AbstractMultipleShooting`
    
        Multiple shooting method applicable for trajectories, in an ephemeris model. Not suited for closed orbits.
    
        Since:
            10.2
    
        Also see:
            "TRAJECTORY DESIGN AND ORBIT MAINTENANCE STRATEGIES IN MULTI-BODY DYNAMICAL REGIMES by Thomas A. Pavlak, Purdue
            University"
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], list3: java.util.List[org.orekit.propagation.integration.AdditionalEquations], double: float, double2: float): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], list3: java.util.List[org.orekit.propagation.numerical.EpochDerivativesEquations], double: float, double2: float, int: int): ...

class PythonAbstractMultipleShooting(AbstractMultipleShooting):
    """
    public class PythonAbstractMultipleShooting extends :class:`~org.orekit.utils.AbstractMultipleShooting`
    """
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], double: float, double2: float, int: int, string: str): ...
    def computeAdditionalConstraints(self, list: java.util.List[org.orekit.propagation.SpacecraftState]) -> typing.List[float]: ...
    def computeAdditionalJacobianMatrix(self, list: java.util.List[org.orekit.propagation.SpacecraftState]) -> typing.List[typing.List[float]]: ...
    def finalize(self) -> None: ...
    def getAugmentedInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, additionalEquations: org.orekit.propagation.integration.AdditionalEquations) -> org.orekit.propagation.SpacecraftState:
        """
            Compute the additional state from the additionalEquations.
        
            Overrides:
                :meth:`~org.orekit.utils.AbstractMultipleShooting.getAugmentedInitialState`Â in
                classÂ :class:`~org.orekit.utils.AbstractMultipleShooting`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): SpacecraftState without the additional state
                additionalEquations2 (:class:`~org.orekit.propagation.integration.AdditionalEquations`): Additional Equations.
        
            Returns:
                augmentedSP SpacecraftState with the additional state within.
        
        
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

class PythonExtendedPVCoordinatesProvider(ExtendedPVCoordinatesProvider):
    """
    public class PythonExtendedPVCoordinatesProvider extends Object implements :class:`~org.orekit.utils.ExtendedPVCoordinatesProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getPVCoordinates_1__T = typing.TypeVar('_getPVCoordinates_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_1__T], frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_getPVCoordinates_1__T]:
        """
            Get the :class:`~org.orekit.utils.FieldPVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.ExtendedPVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.ExtendedPVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    _getPVCoordinates_FF__T = typing.TypeVar('_getPVCoordinates_FF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPVCoordinates_FF(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_FF__T], frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_getPVCoordinates_FF__T]:
        """
            Get the :class:`~org.orekit.utils.FieldPVCoordinates` of the body in the selected frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.utils")``.

    AbsolutePVCoordinates: typing.Type[AbsolutePVCoordinates]
    AbstractMultipleShooting: typing.Type[AbstractMultipleShooting]
    AccurateFormatter: typing.Type[AccurateFormatter]
    AngularCoordinates: typing.Type[AngularCoordinates]
    AngularDerivativesFilter: typing.Type[AngularDerivativesFilter]
    CartesianDerivativesFilter: typing.Type[CartesianDerivativesFilter]
    Constants: typing.Type[Constants]
    DateDriver: typing.Type[DateDriver]
    Differentiation: typing.Type[Differentiation]
    DoubleArrayDictionary: typing.Type[DoubleArrayDictionary]
    ElevationMask: typing.Type[ElevationMask]
    ExtendedPVCoordinatesProvider: typing.Type[ExtendedPVCoordinatesProvider]
    FieldAbsolutePVCoordinates: typing.Type[FieldAbsolutePVCoordinates]
    FieldAngularCoordinates: typing.Type[FieldAngularCoordinates]
    FieldArrayDictionary: typing.Type[FieldArrayDictionary]
    FieldLegendrePolynomials: typing.Type[FieldLegendrePolynomials]
    FieldPVCoordinates: typing.Type[FieldPVCoordinates]
    FieldPVCoordinatesProvider: typing.Type[FieldPVCoordinatesProvider]
    FieldTimeSpanMap: typing.Type[FieldTimeSpanMap]
    GenericTimeStampedCache: typing.Type[GenericTimeStampedCache]
    IERSConventions: typing.Type[IERSConventions]
    ImmutableTimeStampedCache: typing.Type[ImmutableTimeStampedCache]
    InterpolationTableLoader: typing.Type[InterpolationTableLoader]
    LagrangianPoints: typing.Type[LagrangianPoints]
    LegendrePolynomials: typing.Type[LegendrePolynomials]
    LoveNumbers: typing.Type[LoveNumbers]
    MultipleShooter: typing.Type[MultipleShooter]
    MultipleShooting: typing.Type[MultipleShooting]
    OrekitConfiguration: typing.Type[OrekitConfiguration]
    PVCoordinates: typing.Type[PVCoordinates]
    PVCoordinatesProvider: typing.Type[PVCoordinatesProvider]
    ParameterDriver: typing.Type[ParameterDriver]
    ParameterDriversList: typing.Type[ParameterDriversList]
    ParameterFunction: typing.Type[ParameterFunction]
    ParameterObserver: typing.Type[ParameterObserver]
    PythonAbstractMultipleShooting: typing.Type[PythonAbstractMultipleShooting]
    PythonExtendedPVCoordinatesProvider: typing.Type[PythonExtendedPVCoordinatesProvider]
    PythonFieldPVCoordinatesProvider: typing.Type[PythonFieldPVCoordinatesProvider]
    PythonMultipleShooting: typing.Type[PythonMultipleShooting]
    PythonPVCoordinatesProvider: typing.Type[PythonPVCoordinatesProvider]
    PythonParameterFunction: typing.Type[PythonParameterFunction]
    PythonParameterObserver: typing.Type[PythonParameterObserver]
    PythonStateFunction: typing.Type[PythonStateFunction]
    PythonStateJacobian: typing.Type[PythonStateJacobian]
    PythonTimeStampedCache: typing.Type[PythonTimeStampedCache]
    PythonTimeStampedGenerator: typing.Type[PythonTimeStampedGenerator]
    SecularAndHarmonic: typing.Type[SecularAndHarmonic]
    StateFunction: typing.Type[StateFunction]
    StateJacobian: typing.Type[StateJacobian]
    TimeSpanMap: typing.Type[TimeSpanMap]
    TimeStampedAngularCoordinates: typing.Type[TimeStampedAngularCoordinates]
    TimeStampedCache: typing.Type[TimeStampedCache]
    TimeStampedFieldAngularCoordinates: typing.Type[TimeStampedFieldAngularCoordinates]
    TimeStampedFieldPVCoordinates: typing.Type[TimeStampedFieldPVCoordinates]
    TimeStampedGenerator: typing.Type[TimeStampedGenerator]
    TimeStampedPVCoordinates: typing.Type[TimeStampedPVCoordinates]
    units: org.orekit.utils.units.__module_protocol__
