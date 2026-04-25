
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import java.util.function
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.hipparchus.util
import org.orekit.attitudes
import org.orekit.bodies
import org.orekit.data
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils.formatting
import org.orekit.utils.units
import typing



class AbsolutePVCoordinatesHermiteInterpolator(org.orekit.time.AbstractTimeInterpolator['AbsolutePVCoordinates']):
    """
    Class using a Hermite interpolator to interpolate absolute position-velocity-acceleration coordinates.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
        class:`~org.orekit.utils.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, AbsolutePVCoordinates
    """
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: 'CartesianDerivativesFilter'): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: 'CartesianDerivativesFilter'): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    def getFilter(self) -> 'CartesianDerivativesFilter':
        """
        Get the filter for derivatives from the sample to use in interpolation.
        
        Returns:
            filter for derivatives from the sample to use in interpolation.
        
        
        """
        ...
    def getOutputFrame(self) -> org.orekit.frames.Frame:
        """
        Get output frame for the interpolated instance.
        
        Returns:
            output frame for the interpolated instance
        
        
        """
        ...

class AngularCoordinates(org.orekit.time.TimeShiftable['AngularCoordinates'], java.io.Serializable):
    """
    Simple container for rotation/rotation rate/rotation acceleration triplets.
    
    The state can be slightly shifted to close dates. This shift is based on an approximate solution of the fixed acceleration motion. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
    This class is the angular counterpart to PVCoordinates.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        serialized
    """
    IDENTITY: typing.ClassVar['AngularCoordinates'] = ...
    """
    Fixed orientation parallel with reference frame (identity rotation, zero rotation rate and acceleration).
    """
    ___init___1__U = typing.TypeVar('___init___1__U', bound=org.hipparchus.analysis.differentiation.Derivative)  # <U>
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[___init___1__U]): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, pVCoordinates: 'PVCoordinates', pVCoordinates2: 'PVCoordinates'): ...
    @typing.overload
    def __init__(self, pVCoordinates: 'PVCoordinates', pVCoordinates2: 'PVCoordinates', pVCoordinates3: 'PVCoordinates', pVCoordinates4: 'PVCoordinates', double: float): ...
    def addOffset(self, offset: 'AngularCoordinates') -> 'AngularCoordinates':
        """
        Add an offset from the instance.
        
        We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. addOffset(b) and addOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Parameters:
            offset (AngularCoordinates): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            subtractOffset
        
        
        """
        ...
    _applyTo_0__T = typing.TypeVar('_applyTo_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _applyTo_2__T = typing.TypeVar('_applyTo_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def applyTo(self, fieldPVCoordinates: 'FieldPVCoordinates'[_applyTo_0__T]) -> 'FieldPVCoordinates'[_applyTo_0__T]:
        """
        Apply the rotation to a pv coordinates.
        
        Parameters:
            pv (FieldPVCoordinates<T> pv): vector to apply the rotation to
        
        Returns:
            a new pv coordinates which is the image of pv by the rotation
        
        Since:
            9.0
        
        Apply the rotation to a pv coordinates.
        
        Parameters:
            pv (TimeStampedFieldPVCoordinates<T> pv): vector to apply the rotation to
        
        Returns:
            a new pv coordinates which is the image of pv by the rotation
        
        Since:
            9.0
        
        
        """
        ...
    @typing.overload
    def applyTo(self, pVCoordinates: 'PVCoordinates') -> 'PVCoordinates':
        """
        Apply the rotation to a pv coordinates.
        
        Parameters:
            pv (PVCoordinates): vector to apply the rotation to
        
        Returns:
            a new pv coordinates which is the image of pv by the rotation
        
        Apply the rotation to a pv coordinates.
        
        Parameters:
            pv (TimeStampedPVCoordinates): vector to apply the rotation to
        
        Returns:
            a new pv coordinates which is the image of pv by the rotation
        
        """
        ...
    @typing.overload
    def applyTo(self, timeStampedFieldPVCoordinates: 'TimeStampedFieldPVCoordinates'[_applyTo_2__T]) -> 'TimeStampedFieldPVCoordinates'[_applyTo_2__T]: ...
    @typing.overload
    def applyTo(self, timeStampedPVCoordinates: 'TimeStampedPVCoordinates') -> 'TimeStampedPVCoordinates': ...
    @staticmethod
    def createFromModifiedRodrigues(r: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> 'AngularCoordinates':
        """
        Convert a modified Rodrigues vector and derivatives to angular coordinates.
        
        Parameters:
            r (double[][]): modified Rodrigues vector (with first and second times derivatives)
        
        Returns:
            angular coordinates
        
        Also see:
            getModifiedRodrigues
        
        
        """
        ...
    @staticmethod
    def estimateRate(start: org.hipparchus.geometry.euclidean.threed.Rotation, end: org.hipparchus.geometry.euclidean.threed.Rotation, dt: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    def getModifiedRodrigues(self, sign: float) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Convert rotation, rate and acceleration to modified Rodrigues vector and derivatives.
        
        The modified Rodrigues vector is tan(θ/4) u where θ and u are the rotation angle and axis respectively.
        
        Parameters:
            sign (double): multiplicative sign for quaternion components
        
        Returns:
            modified Rodrigues vector and derivatives (vector on row 0, first derivative on row 1, second derivative on row 2)
        
        Also see:
            createFromModifiedRodrigues
        
        
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
            the rotation acceleration vector dΩ/dt (rad/s²).
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the rotation rate.
        
        Returns:
            the rotation rate vector Ω (rad/s).
        
        
        """
        ...
    def revert(self) -> 'AngularCoordinates':
        """
        Revert a rotation/rotation rate/ rotation acceleration triplet. Build a triplet which reverse the effect of another triplet.
        
        Returns:
            a new triplet whose effect is the reverse of the effect of the instance
        
        
        """
        ...
    def rotationShiftedBy(self, dt: float) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get a time-shifted rotation. Same as shiftedBy except only the shifted rotation is computed.
        
        The state can be slightly shifted to close dates. This shift is based on an approximate solution of the fixed acceleration motion. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Also see:
            shiftedBy
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, dt: org.orekit.time.TimeOffset) -> org.orekit.time.TimeShiftable:
        """
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on an approximate solution of the fixed acceleration motion. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'AngularCoordinates': ...
    def subtractOffset(self, offset: 'AngularCoordinates') -> 'AngularCoordinates':
        """
        Subtract an offset from the instance.
        
        We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. subtractOffset(b) and subtractOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Parameters:
            offset (AngularCoordinates): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            addOffset
        
        
        """
        ...
    def toDerivativeStructureRotation(self, order: int) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.DerivativeStructure]:
        """
        Transform the instance to a FieldRotation<DerivativeStructure>.
        
        The DerivativeStructure coordinates correspond to time-derivatives up to the user-specified order.
        
        Parameters:
            order (int): derivation order for the vector components
        
        Returns:
            rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...
    def toUnivariateDerivative1Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.UnivariateDerivative1]:
        """
        Transform the instance to a FieldRotation<UnivariateDerivative1>.
        
        The UnivariateDerivative1 coordinates correspond to time-derivatives up to the order 1.
        
        Returns:
            rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...
    def toUnivariateDerivative2Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.UnivariateDerivative2]:
        """
        Transform the instance to a FieldRotation<UnivariateDerivative2>.
        
        The UnivariateDerivative2 coordinates correspond to time-derivatives up to the order 2.
        
        Returns:
            rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...

class AngularDerivativesFilter(java.lang.Enum['AngularDerivativesFilter']):
    """
    Enumerate for selecting which derivatives to use in TimeStampedAngularCoordinates and TimeStampedFieldAngularCoordinates interpolation.
    
    Since:
        7.0
    
    Also see:
        interpolate,
        interpolate,
        CartesianDerivativesFilter
    """
    USE_R: typing.ClassVar['AngularDerivativesFilter'] = ...
    USE_RR: typing.ClassVar['AngularDerivativesFilter'] = ...
    USE_RRA: typing.ClassVar['AngularDerivativesFilter'] = ...
    @staticmethod
    def getFilter(order: int) -> 'AngularDerivativesFilter':
        """
        Get the filter corresponding to a maximum derivation order.
        
        Parameters:
            order (int): maximum derivation order
        
        Returns:
            the filter corresponding to derivation order
        
        Raises:
            IllegalArgumentException: if the order is out of range
        
        
        """
        ...
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
    def valueOf(name: str) -> 'AngularDerivativesFilter':
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
    def values() -> typing.MutableSequence['AngularDerivativesFilter']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (AngularDerivativesFilter c : AngularDerivativesFilter.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class CartesianCovarianceUtils:
    """
    Utility class for conversions related to Cartesian covariance matrices.
    
    Since:
        12.2
    """
    @staticmethod
    def changeReferenceFrame(inputFrame: org.orekit.frames.Frame, outputFrame: org.hipparchus.linear.RealMatrix, covarianceMatrix: org.orekit.time.AbsoluteDate, date: org.orekit.frames.Frame) -> org.hipparchus.linear.RealMatrix:
        """
        Convert input position-velocity covariance matrix between reference frames.
        
        Parameters:
            inputFrame (Frame): input frame
            outputFrame (RealMatrix): output frame
            covarianceMatrix (AbsoluteDate): position-velocity covariance matrix in reference frame
            date (Frame): epoch
        
        Returns:
            converted covariance matrix
        
        
        """
        ...
    @staticmethod
    def convertFromLofType(position: org.orekit.frames.LOFType, velocity: org.hipparchus.linear.RealMatrix, covarianceMatrix: org.hipparchus.geometry.euclidean.threed.Vector3D, lofType: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.linear.RealMatrix:
        """
        Convert input position-velocity covariance matrix from local frame to reference one.
        
        Parameters:
            position (LOFType): position vector in reference frame
            velocity (RealMatrix): velocity vector in reference frame
            covarianceMatrix (Vector3D): position-velocity covariance matrix in local frame
            lofType (Vector3D): input local orbital frame
        
        Returns:
            converted covariance matrix
        
        
        """
        ...
    @staticmethod
    def convertToLofType(position: org.hipparchus.geometry.euclidean.threed.Vector3D, velocity: org.hipparchus.geometry.euclidean.threed.Vector3D, covarianceMatrix: org.hipparchus.linear.RealMatrix, lofType: org.orekit.frames.LOFType) -> org.hipparchus.linear.RealMatrix:
        """
        Convert input position-velocity covariance matrix from reference frame to local one.
        
        Parameters:
            position (Vector3D): position vector in reference frame
            velocity (Vector3D): velocity vector in reference frame
            covarianceMatrix (RealMatrix): position-velocity covariance matrix in reference frame
            lofType (LOFType): output local orbital frame
        
        Returns:
            converted covariance matrix
        
        
        """
        ...

class CartesianDerivativesFilter(java.lang.Enum['CartesianDerivativesFilter']):
    """
    Enumerate for selecting which derivatives to use in TimeStampedPVCoordinates and TimeStampedFieldPVCoordinates interpolation.
    
    Since:
        7.0
    
    Also see:
        interpolate,
        interpolate, AngularDerivativesFilter
    """
    USE_P: typing.ClassVar['CartesianDerivativesFilter'] = ...
    USE_PV: typing.ClassVar['CartesianDerivativesFilter'] = ...
    USE_PVA: typing.ClassVar['CartesianDerivativesFilter'] = ...
    @staticmethod
    def getFilter(order: int) -> 'CartesianDerivativesFilter':
        """
        Get the filter corresponding to a maximum derivation order.
        
        Parameters:
            order (int): maximum derivation order
        
        Returns:
            the filter corresponding to derivation order
        
        Raises:
            IllegalArgumentException: if the order is out of range
        
        
        """
        ...
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
    def valueOf(name: str) -> 'CartesianDerivativesFilter':
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
    def values() -> typing.MutableSequence['CartesianDerivativesFilter']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (CartesianDerivativesFilter c : CartesianDerivativesFilter.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Constants:
    """
    Set of useful physical constants.
    """
    SPEED_OF_LIGHT: typing.ClassVar[float] = ...
    """
    Speed of light: 299792458.0 m/s.
    
    Also see:
        constant
    
    
    """
    IAU_2012_ASTRONOMICAL_UNIT: typing.ClassVar[float] = ...
    """
    Astronomical unit as a conventional unit of length since IAU 2012 resolution B2: 149597870700.0 m.
    
    Also see:
        `IAU 2012 resolutions <http://www.iau.org/static/resolutions/IAU2012_English.pdf>`, constant
    
    
    """
    IAU_2015_NOMINAL_SOLAR_RADIUS: typing.ClassVar[float] = ...
    """
    Solar radius as defined by IAU 2015 resolution B3: 695700000.0 m.
    
    Also see:
        pdf, constant
    
    
    """
    IAU_2015_NOMINAL_SUN_GM: typing.ClassVar[float] = ...
    """
    Sun attraction coefficient as defined by IAU 2015 resolution B3: 1.3271244e20 (m³/s²).
    
    Also see:
        constant
    
    
    """
    IAU_2015_NOMINAL_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius as defined by IAU 2015 resolution B3: 6.3781e6 (m).
    
    Also see:
        constant
    
    
    """
    IAU_2015_NOMINAL_EARTH_POLAR_RADIUS: typing.ClassVar[float] = ...
    """
    Earth polar radius as defined by IAU 2015 resolution B3: 6.3568e6 (m).
    
    Also see:
        constant
    
    
    """
    IAU_2015_NOMINAL_EARTH_GM: typing.ClassVar[float] = ...
    """
    Earth attraction coefficient as defined by IAU 2015 resolution B3: 3.986004e14 (m³/s²).
    
    Also see:
        constant
    
    
    """
    IAU_2015_NOMINAL_JUPITER_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Jupiter equatorial radius as defined by IAU 2015 resolution B3: 7.1492e7 (m).
    
    Also see:
        constant
    
    
    """
    IAU_2015_NOMINAL_JUPITER_POLAR_RADIUS: typing.ClassVar[float] = ...
    """
    Jupiter polar radius as defined by IAU 2015 resolution B3: 6.6854e7 (m).
    
    Also see:
        constant
    
    
    """
    IAU_2015_NOMINAL_JUPITER_GM: typing.ClassVar[float] = ...
    """
    Jupiter attraction coefficient as defined by IAU 2015 resolution B3: 1.2668653e17 (m³/s²).
    
    Also see:
        constant
    
    
    """
    JULIAN_DAY: typing.ClassVar[float] = ...
    """
    Duration of a mean solar day: 86400.0 s.
    
    Also see:
        constant
    
    
    """
    JULIAN_YEAR: typing.ClassVar[float] = ...
    """
    Duration of a Julian year: 365.25 JULIAN_DAY.
    
    Also see:
        constant
    
    
    """
    JULIAN_CENTURY: typing.ClassVar[float] = ...
    """
    Duration of a Julian century: 36525 JULIAN_DAY.
    
    Also see:
        constant
    
    
    """
    BESSELIAN_YEAR: typing.ClassVar[float] = ...
    """
    Duration of a Besselian year: 365.242198781 JULIAN_DAY.
    
    Also see:
        constant
    
    
    """
    ARC_SECONDS_TO_RADIANS: typing.ClassVar[float] = ...
    """
    Conversion factor from arc seconds to radians: 2PI/(36060*60).
    
    Also see:
        constant
    
    
    """
    G0_STANDARD_GRAVITY: typing.ClassVar[float] = ...
    """
    Standard gravity constant, used in maneuvers definition: 9.80665 m/s².
    
    Also see:
        constant
    
    
    """
    SUN_RADIUS: typing.ClassVar[float] = ...
    """
    Sun radius: 695700000 m (source: resolution B3 from IAU 2015).
    
    Also see:
        constant
    
    
    """
    MOON_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Moon equatorial radius: 1737400 m.
    
    Also see:
        constant
    
    
    """
    WGS84_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from WGS84 model: 6378137.0 m.
    
    Also see:
        constant
    
    
    """
    WGS84_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    Earth flattening from WGS84 model: 1.0 / 298.257223563.
    
    Also see:
        constant
    
    
    """
    WGS84_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    Earth angular velocity from WGS84 model: 7.292115e-5 rad/s.
    
    Also see:
        constant
    
    
    """
    WGS84_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from WGS84 model: 3.986004418e14 m³/s².
    
    Also see:
        constant
    
    
    """
    WGS84_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from WGS84 model: .
    
    Also see:
        constant
    
    
    """
    GRS80_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from GRS80 model: 6378137.0 m.
    
    Also see:
        constant
    
    
    """
    GRS80_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    Earth flattening from GRS80 model: 1.0 / 298.257222101.
    
    Also see:
        constant
    
    
    """
    GRS80_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    Earth angular velocity from GRS80 model: 7.292115e-5 rad/s.
    
    Also see:
        constant
    
    
    """
    GRS80_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from GRS80 model: 3.986005e14 m³/s².
    
    Also see:
        constant
    
    
    """
    GRS80_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from GRS80 model: -1.08263e-3.
    
    Also see:
        constant
    
    
    """
    EGM96_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from EGM96 model: 6378136.3 m.
    
    Also see:
        constant
    
    
    """
    EGM96_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from EGM96 model: 3.986004415e14 m³/s².
    
    Also see:
        constant
    
    
    """
    EGM96_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from EGM96 model: -1.08262668355315e-3.
    
    Also see:
        constant
    
    
    """
    EGM96_EARTH_C30: typing.ClassVar[float] = ...
    """
    Earth un-normalized third zonal coefficient from EGM96 model: 2.53265648533224e-6.
    
    Also see:
        constant
    
    
    """
    EGM96_EARTH_C40: typing.ClassVar[float] = ...
    """
    Earth un-normalized fourth zonal coefficient from EGM96 model: 1.619621591367e-6.
    
    Also see:
        constant
    
    
    """
    EGM96_EARTH_C50: typing.ClassVar[float] = ...
    """
    Earth un-normalized fifth zonal coefficient from EGM96 model: 2.27296082868698e-7.
    
    Also see:
        constant
    
    
    """
    EGM96_EARTH_C60: typing.ClassVar[float] = ...
    """
    Earth un-normalized sixth zonal coefficient from EGM96 model: -5.40681239107085e-7.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from GRIM5C1 model: 6378136.46 m.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    Earth flattening from GRIM5C1 model: 1.0 / 298.25765.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    Earth angular velocity from GRIM5C1 model: 7.292115e-5 rad/s.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from GRIM5C1 model: 3.986004415e14 m³/s².
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from GRIM5C1 model: -1.082626110612609e-3.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_C30: typing.ClassVar[float] = ...
    """
    Earth un-normalized third zonal coefficient from GRIM5C1 model: 2.536150841690056e-6.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_C40: typing.ClassVar[float] = ...
    """
    Earth un-normalized fourth zonal coefficient from GRIM5C1 model: 1.61936352497151e-6.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_C50: typing.ClassVar[float] = ...
    """
    Earth un-normalized fifth zonal coefficient from GRIM5C1 model: 2.231013736607540e-7.
    
    Also see:
        constant
    
    
    """
    GRIM5C1_EARTH_C60: typing.ClassVar[float] = ...
    """
    Earth un-normalized sixth zonal coefficient from GRIM5C1 model: -5.402895357302363e-7.
    
    Also see:
        constant
    
    
    """
    EIGEN5C_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from EIGEN5C model: 6378136.46 m.
    
    Also see:
        constant
    
    
    """
    EIGEN5C_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from EIGEN5C model: 3.986004415e14 m³/s².
    
    Also see:
        constant
    
    
    """
    EIGEN5C_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from EIGEN5C model: -1.082626457231767e-3.
    
    Also see:
        constant
    
    
    """
    EIGEN5C_EARTH_C30: typing.ClassVar[float] = ...
    """
    Earth un-normalized third zonal coefficient from EIGEN5C model: 2.532547231862799e-6.
    
    Also see:
        constant
    
    
    """
    EIGEN5C_EARTH_C40: typing.ClassVar[float] = ...
    """
    Earth un-normalized fourth zonal coefficient from EIGEN5C model: 1.619964434136e-6.
    
    Also see:
        constant
    
    
    """
    EIGEN5C_EARTH_C50: typing.ClassVar[float] = ...
    """
    Earth un-normalized fifth zonal coefficient from EIGEN5C model: 2.277928487005437e-7.
    
    Also see:
        constant
    
    
    """
    EIGEN5C_EARTH_C60: typing.ClassVar[float] = ...
    """
    Earth un-normalized sixth zonal coefficient from EIGEN5C model: -5.406653715879098e-7.
    
    Also see:
        constant
    
    
    """
    IERS96_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from IERS96 model: 6378136.49 m.
    
    Also see:
        constant
    
    
    """
    IERS96_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    Earth flattening from IERS96 model: 1.0 / 298.25642.
    
    Also see:
        constant
    
    
    """
    IERS96_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    Earth angular velocity from IERS96 model: 7.292115e-5 rad/s.
    
    Also see:
        constant
    
    
    """
    IERS96_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from IERS96 model: 3.986004418e14 m³/s².
    
    Also see:
        constant
    
    
    """
    IERS96_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from IERS96 model: -1.0826359e-3.
    
    Also see:
        constant
    
    
    """
    IERS2003_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from IERS2003 model: 6378136.6 m.
    
    Also see:
        constant
    
    
    """
    IERS2003_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    Earth flattening from IERS2003 model: 1.0 / 298.25642.
    
    Also see:
        constant
    
    
    """
    IERS2003_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    Earth angular velocity from IERS2003 model: 7.292115e-5 rad/s.
    
    Also see:
        constant
    
    
    """
    IERS2003_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from IERS2003 model: 3.986004418e14 m³/s².
    
    Also see:
        constant
    
    
    """
    IERS2003_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from IERS2003 model: -1.0826359e-3.
    
    Also see:
        constant
    
    
    """
    IERS2010_EARTH_EQUATORIAL_RADIUS: typing.ClassVar[float] = ...
    """
    Earth equatorial radius from IERS2010 model: 6378136.6 m.
    
    Also see:
        constant
    
    
    """
    IERS2010_EARTH_FLATTENING: typing.ClassVar[float] = ...
    """
    Earth flattening from IERS2010 model: 1.0 / 298.25642.
    
    Also see:
        constant
    
    
    """
    IERS2010_EARTH_ANGULAR_VELOCITY: typing.ClassVar[float] = ...
    """
    Earth angular velocity from IERS2010 model: 7.292115e-5 rad/s.
    
    Also see:
        constant
    
    
    """
    IERS2010_EARTH_MU: typing.ClassVar[float] = ...
    """
    Earth gravitational constant from IERS2010 model: 3.986004418e14 m³/s².
    
    Also see:
        constant
    
    
    """
    IERS2010_EARTH_C20: typing.ClassVar[float] = ...
    """
    Earth un-normalized second zonal coefficient from IERS2010 model: -1.0826359e-3.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_GAUSSIAN_GRAVITATIONAL_CONSTANT: typing.ClassVar[float] = ...
    """
    Gaussian gravitational constant: 0.01720209895 √(AU³/d²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_ASTRONOMICAL_UNIT: typing.ClassVar[float] = ...
    """
    Astronomical Unit: 149597870691 m.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_GM: typing.ClassVar[float] = ...
    """
    Sun attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_MERCURY_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/Mercury mass ratio: 6023600.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_MERCURY_GM: typing.ClassVar[float] = ...
    """
    Sun/Mercury attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_VENUS_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/Venus mass ratio: 408523.71.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_VENUS_GM: typing.ClassVar[float] = ...
    """
    Sun/Venus attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_EARTH_PLUS_MOON_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/(Earth + Moon) mass ratio: 328900.56.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_EARTH_PLUS_MOON_GM: typing.ClassVar[float] = ...
    """
    Sun/(Earth + Moon) attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_EARTH_MOON_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Earth/Moon mass ratio: 81.30059.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_MOON_GM: typing.ClassVar[float] = ...
    """
    Moon attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_EARTH_GM: typing.ClassVar[float] = ...
    """
    Earth attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_MARS_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/(Mars system) mass ratio: 3098708.0.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_MARS_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    Sun/(Mars system) attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_JUPITER_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/(Jupiter system) mass ratio: 1047.3486.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_JUPITER_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    Sun/(Jupiter system) ttraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_SATURN_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/(Saturn system) mass ratio: 3497.898.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SATURN_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    Sun/(Saturn system) attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_URANUS_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/(Uranus system) mass ratio: 22902.98.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_URANUS_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    Sun/(Uranus system) attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_NEPTUNE_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/(Neptune system) mass ratio: 19412.24.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_NEPTUNE_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    Sun/(Neptune system) attraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """
    JPL_SSD_SUN_PLUTO_SYSTEM_MASS_RATIO: typing.ClassVar[float] = ...
    """
    Sun/(Pluto system) mass ratio: 1.35e8.
    
    Also see:
        constant
    
    
    """
    JPL_SSD_PLUTO_SYSTEM_GM: typing.ClassVar[float] = ...
    """
    Sun/(Pluto system) ttraction coefficient (m³/s²).
    
    Also see:
        constant
    
    
    """

class DataDictionary(java.io.Serializable):
    """
    String → Object mapping, for small number of keys.
    
    This class is a low overhead for a very small number of keys. It is based on simple array and string comparison. It plays the same role a Map<String, Object> but with reduced features and not intended for large number of keys. For such needs the regular Map<String, Object> should be preferred.
    
    Since:
        13.0
    
    Also see:
        DoubleArrayDictionary, serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, dataDictionary: 'DataDictionary'): ...
    def clear(self) -> None:
        """
        Remove all entries.
        """
        ...
    def get(self, key: str) -> typing.Any:
        """
        Get the value corresponding to a key.
        
        Parameters:
            key (String): entry key
        
        Returns:
            copy of the value corresponding to the key or null if key not present
        
        
        """
        ...
    def getData(self) -> java.util.List['DataDictionary.Entry']:
        """
        Get an unmodifiable view of the dictionary entries.
        
        Returns:
            unmodifiable view of the dictionary entries
        
        
        """
        ...
    def getEntry(self, key: str) -> 'DataDictionary.Entry':
        """
        Get a complete entry.
        
        Parameters:
            key (String): entry key
        
        Returns:
            entry with key if it exists, null otherwise
        
        
        """
        ...
    def put(self, key: str, value: typing.Any) -> None:
        """
        Add an entry.
        
        If an entry with the same key already exists, it will be removed first.
        
        The new entry is always put at the end.
        
        Parameters:
            key (String): entry key
            value (Object): entry value
        
        
        """
        ...
    def putAll(self, dictionary: 'DataDictionary') -> None:
        """
        Put all the entries from another dictionary.
        
        Parameters:
            dictionary (DataDictionary): dictionary to copy into the instance
        
        
        """
        ...
    def putAllDoubles(self, map: typing.Union[java.util.Map[str, typing.Union[typing.List[float], jpype.JArray]], typing.Mapping[str, typing.Union[typing.List[float], jpype.JArray]]]) -> None:
        """
        Put all the double[] entries from the map in the dictionary.
        
        Parameters:
            map (Map<String, double[]> map): map to copy into the instance
        
        
        """
        ...
    def remove(self, key: str) -> bool:
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
    def toDoubleDictionary(self) -> 'DoubleArrayDictionary':
        """
        Creates a double values dictionary.
        
        Creates a DoubleArrayDictionary with all double[] values contained in the instance.
        
        Returns:
            a double values dictionary
        
        
        """
        ...
    def toMap(self) -> java.util.Map[str, typing.Any]:
        """
        Create a map from the instance.
        
        The map contains a copy of the instance data
        
        Returns:
            copy of the dictionary, as an independent map
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str:
        """
        Get a string representation of the dictionary.
        
        This string representation is intended for improving displays in debuggers only.
        
        Overrides: Object in class Object
        
        Returns:
            string representation of the dictionary
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def toString(map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> str: ...
    class Entry(java.io.Serializable):
        def getKey(self) -> str: ...
        def getValue(self) -> typing.Any: ...
        def increment(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
        def scaledIncrement(self, double: float, entry: 'DoubleArrayDictionary.Entry') -> None: ...
        def zero(self) -> None: ...

class DerivativeStateUtils:
    """
    Utility class used to convert state vectors in Taylor differential algebra.
    
    Since:
        13.1
    
    Also see:
        Gradient
    """
    @staticmethod
    def buildAbsolutePVGradient(field: org.hipparchus.analysis.differentiation.GradientField, coordinates: 'AbsolutePVCoordinates') -> 'FieldAbsolutePVCoordinates'[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Method creating a Gradient version of the input coordinates, using the state vector as the independent variables of a first- order Taylor algebra. If the number of variables is greater than 6, mass will be considered one.
        
        Parameters:
            field (GradientField): gradient field
            coordinates (AbsolutePVCoordinates): absolute coordinates
        
        Returns:
            fielded coordinates
        
        Also see:
            AbsolutePVCoordinates, FieldAbsolutePVCoordinates
        
        
        """
        ...
    @staticmethod
    def buildOrbitGradient(field: org.hipparchus.analysis.differentiation.GradientField, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.FieldOrbit[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Method creating a Gradient version of the input orbit, using the state vector as the independent variables of a first- order Taylor algebra. If the number of variables is greater than 6, mass will be considered one.
        
        Parameters:
            field (GradientField): gradient field
            orbit (Orbit): orbit
        
        Returns:
            fielded orbit
        
        Also see:
            FieldOrbit, Orbit
        
        
        """
        ...
    @staticmethod
    def buildSpacecraftStateGradient(field: org.hipparchus.analysis.differentiation.GradientField, state: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Method creating a Gradient version of the input state, using the state vector as the independent variables of a first- order Taylor algebra. If the number of variables is greater than 6, mass will be considered one. Additional data and derivatives are ignored.
        
        Parameters:
            field (GradientField): gradient field
            state (SpacecraftState): full state
            attitudeProvider (AttitudeProvider): provider to recompute attitude, can be null
        
        Returns:
            fielded state
        
        Also see:
            FieldSpacecraftState, SpacecraftState
        
        
        """
        ...
    @staticmethod
    def buildSpacecraftStateTransitionGradient(state: org.orekit.propagation.SpacecraftState, partialDerivatives: org.hipparchus.linear.RealMatrix, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Method creating a Gradient version of the input state from a given transition matrix. The number of independent variables equals the number of columns. The number of rows tells how many state variables are considered to be the dependent variables in the Taylor differential algebra. If the number of state variables is greater than 6, mass will be considered one. Additional data and derivatives are ignored.
        
        Parameters:
            state (SpacecraftState): full state
            partialDerivatives (RealMatrix): Jacobian matrix of state variables to consider as dependent ones, w.r.t. unknown parameters
            attitudeProvider (AttitudeProvider): provider to recompute attitude, can be null
        
        Returns:
            fielded state
        
        Also see:
            FieldSpacecraftState, SpacecraftState
        
        
        """
        ...

class Differentiation:
    """
    Utility class for differentiating various kinds of functions.
    
    Since:
        8.0
    """
    @typing.overload
    @staticmethod
    def differentiate(parameterFunction: typing.Union['ParameterFunction', typing.Callable], int: int, double: float) -> 'ParameterFunction':
        """
        Differentiate a scalar function using finite differences.
        
        Parameters:
            function (ParameterFunction): function to differentiate
            nbPoints (int): number of points used for finite differences
            step (double): step for finite differences, in physical units
        
        Returns:
            scalar function evaluating to the derivative of the original function
        
        Since:
            9.3
        
        Differentiate a vector function using finite differences.
        
        Parameters:
            function (StateFunction): function to differentiate
            dimension (int): dimension of the vector value of the function
            provider (AttitudeProvider): attitude provider to use for modified states
            orbitType (OrbitType): type used to map the orbit to a one dimensional array
            positionAngleType (PositionAngleType): type of the position angle used for orbit mapping to array
            dP (double): user specified position error, used for step size computation for finite differences
            nbPoints (int): number of points used for finite differences
        
        Returns:
            matrix function evaluating to the Jacobian of the original function
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def differentiate(stateFunction: typing.Union['StateFunction', typing.Callable], int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, int2: int) -> 'StateJacobian': ...

class DoubleArrayDictionary(java.io.Serializable):
    """
    String → double[] mapping, for small number of keys.
    
    This class is a low overhead for a very small number of keys. It is based on simple array and string comparison. It plays the same role a Map<String, double[]> but with reduced features and not intended for large number of keys. For such needs the regular Map<String, double[]> should be preferred.
    
    Since:
        11.1
    
    Also see:
        DataDictionary, serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Union[typing.List[float], jpype.JArray]], typing.Mapping[str, typing.Union[typing.List[float], jpype.JArray]]]): ...
    @typing.overload
    def __init__(self, doubleArrayDictionary: 'DoubleArrayDictionary'): ...
    def clear(self) -> None:
        """
        Remove all entries.
        """
        ...
    def get(self, key: str) -> typing.MutableSequence[float]:
        """
        Get the value corresponding to a key.
        
        Parameters:
            key (String): entry key
        
        Returns:
            copy of the value corresponding to the key or null if key not present
        
        
        """
        ...
    def getData(self) -> java.util.List['DoubleArrayDictionary.Entry']:
        """
        Get an unmodifiable view of the dictionary entries.
        
        Returns:
            unmodifiable view of the dictionary entries
        
        
        """
        ...
    def getEntry(self, key: str) -> 'DoubleArrayDictionary.Entry':
        """
        Get a complete entry.
        
        Parameters:
            key (String): entry key
        
        Returns:
            entry with key if it exists, null otherwise
        
        
        """
        ...
    def put(self, key: str, value: typing.Union[typing.List[float], jpype.JArray]) -> None:
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
    def putAll(self, dictionary: typing.Union[java.util.Map[str, typing.Union[typing.List[float], jpype.JArray]], typing.Mapping[str, typing.Union[typing.List[float], jpype.JArray]]]) -> None:
        """
        Put all the entries from another dictionary.
        
        Parameters:
            dictionary (DoubleArrayDictionary): dictionary to copy into the instance
        
        
        """
        ...
    @typing.overload
    def putAll(self, doubleArrayDictionary: 'DoubleArrayDictionary') -> None: ...
    def remove(self, key: str) -> bool:
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
    def toMap(self) -> java.util.Map[str, typing.MutableSequence[float]]:
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
        
        Overrides: Object in class Object
        
        Returns:
            string representation of the dictionary
        
        
        """
        ...
    class Entry(java.io.Serializable):
        def getKey(self) -> str: ...
        def getValue(self) -> typing.MutableSequence[float]: ...
        def increment(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
        def scaledIncrement(self, double: float, entry: 'DoubleArrayDictionary.Entry') -> None: ...
        def size(self) -> int: ...
        def zero(self) -> None: ...

class ElevationMask(java.io.Serializable):
    """
    Class for modeling the ground elevation values around a given point.
    
    Instances of this class can be considered to be immutable
    
    Since:
        6.1
    
    Also see:
        serialized
    """
    def __init__(self, mask: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]):
        """
        Creates an instance of an Elevation mask based on the passed in parameter.
        
        Parameters:
            mask (double[][]): azimuth-elevation mask (rad). First column (i.e. mask[i][0]) should contain azimuth values and the second column (i.e.
                mask[i][1]) should contain corresponding elevations
        
        
        """
        ...
    def getElevation(self, azimuth: float) -> float:
        """
        Get the interpolated elevation for a given azimuth according to the mask.
        
        Parameters:
            azimuth (double): azimuth (rad)
        
        Returns:
            elevation angle (rad)
        
        
        """
        ...

class ExpungePolicy(java.lang.Enum['ExpungePolicy']):
    """
    Expunge policy to apply when a TimeSpanMap exceeds its capacity.
    
    Since:
        13.1
    """
    EXPUNGE_EARLIEST: typing.ClassVar['ExpungePolicy'] = ...
    EXPUNGE_LATEST: typing.ClassVar['ExpungePolicy'] = ...
    EXPUNGE_FARTHEST: typing.ClassVar['ExpungePolicy'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ExpungePolicy':
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
    def values() -> typing.MutableSequence['ExpungePolicy']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ExpungePolicy c : ExpungePolicy.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ExtendedPositionProviderAdapter(org.orekit.frames.Frame):
    """
    Adapter from ExtendedPositionProvider to TransformProvider.
    
    The transform provider is a simple translation from a defining frame such that the origin of the transformed frame corresponds to the moving point.
    
    This class is roughly the inverse of FrameAdapter
    
    Since:
        12.0
    
    Also see:
        FrameAdapter
    """
    def __init__(self, parent: org.orekit.frames.Frame, provider: typing.Union['ExtendedPositionProvider', typing.Callable], name: str):
        """
        Simple constructor.
        
        Parameters:
            parent (Frame): parent frame (must be non-null)
            provider (ExtendedPositionProvider): coordinates provider defining the position of origin of the transformed frame
            name (String): name of the frame
        
        
        """
        ...

_FieldAbsolutePVCoordinatesHermiteInterpolator__KK = typing.TypeVar('_FieldAbsolutePVCoordinatesHermiteInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldAbsolutePVCoordinatesHermiteInterpolator(org.orekit.time.AbstractFieldTimeInterpolator['FieldAbsolutePVCoordinates'[_FieldAbsolutePVCoordinatesHermiteInterpolator__KK], _FieldAbsolutePVCoordinatesHermiteInterpolator__KK], typing.Generic[_FieldAbsolutePVCoordinatesHermiteInterpolator__KK]):
    """
    Class using a Hermite interpolator to interpolate absolute position-velocity-acceleration coordinates.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
        class:`~org.orekit.utils.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.FieldHermiteInterpolator?is`, FieldAbsolutePVCoordinates
    """
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    def getFilter(self) -> CartesianDerivativesFilter:
        """
        Get filter for derivatives from the sample to use in interpolation.
        
        Returns:
            filter for derivatives from the sample to use in interpolation
        
        
        """
        ...
    def getOutputFrame(self) -> org.orekit.frames.Frame:
        """
        Get output frame for the interpolated instance.
        
        Returns:
            output frame for the interpolated instance
        
        
        """
        ...

_FieldAngularCoordinates__T = typing.TypeVar('_FieldAngularCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAngularCoordinates(org.orekit.time.FieldTimeShiftable['FieldAngularCoordinates'[_FieldAngularCoordinates__T], _FieldAngularCoordinates__T], typing.Generic[_FieldAngularCoordinates__T]):
    """
    Simple container for rotation / rotation rate pairs, using CalculusFieldElement.
    
    The state can be slightly shifted to close dates. This shift is based on a simple quadratic model. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
    This class is the angular counterpart to FieldPVCoordinates.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        6.0
    
    Also see:
        AngularCoordinates
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
    def addOffset(self, offset: 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]:
        """
        Add an offset from the instance.
        
        We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. addOffset(b) and addOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Parameters:
            offset (FieldAngularCoordinates<FieldAngularCoordinates> offset): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            subtractOffset
        
        
        """
        ...
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
    def createFromModifiedRodrigues(r: typing.Union[typing.List[typing.MutableSequence[_createFromModifiedRodrigues__T]], jpype.JArray]) -> 'FieldAngularCoordinates'[_createFromModifiedRodrigues__T]:
        """
        Convert a modified Rodrigues vector and derivatives to angular coordinates.
        
        Parameters:
            r (T[][]): modified Rodrigues vector (with first and second times derivatives)
        
        Returns:
            angular coordinates
        
        Since:
            9.0
        
        Also see:
            getModifiedRodrigues
        
        
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
    def getModifiedRodrigues(self, sign: float) -> typing.MutableSequence[typing.MutableSequence[_FieldAngularCoordinates__T]]:
        """
        Convert rotation, rate and acceleration to modified Rodrigues vector and derivatives.
        
        The modified Rodrigues vector is tan(θ/4) u where θ and u are the rotation angle and axis respectively.
        
        Parameters:
            sign (double): multiplicative sign for quaternion components
        
        Returns:
            modified Rodrigues vector and derivatives (vector on row 0, first derivative on row 1, second derivative on row 2)
        
        Since:
            9.0
        
        Also see:
            createFromModifiedRodrigues
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAngularCoordinates__T]:
        """
        Get the rotation.
        
        Returns:
            the rotation.
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAngularCoordinates__T]:
        """
        Get the rotation acceleration.
        
        Returns:
            the rotation acceleration vector dΩ/dt (rad/s²).
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAngularCoordinates__T]:
        """
        Get the rotation rate.
        
        Returns:
            the rotation rate vector (rad/s).
        
        
        """
        ...
    def revert(self) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]:
        """
        Revert a rotation / rotation rate / rotation acceleration triplet.
        
        Build a triplet which reverse the effect of another triplet.
        
        Returns:
            a new triplet whose effect is the reverse of the effect of the instance
        
        
        """
        ...
    def rotationShiftedBy(self, dt: _FieldAngularCoordinates__T) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAngularCoordinates__T]:
        """
        Get a time-shifted rotation. Same as shiftedBy except only the shifted rotation is computed.
        
        The state can be slightly shifted to close dates. This shift is based on an approximate solution of the fixed acceleration motion. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
        Parameters:
            dt (FieldAngularCoordinates): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Since:
            11.2
        
        Also see:
            shiftedBy
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _FieldAngularCoordinates__T: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAngularCoordinates__T) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]: ...
    def subtractOffset(self, offset: 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]) -> 'FieldAngularCoordinates'[_FieldAngularCoordinates__T]:
        """
        Subtract an offset from the instance.
        
        We consider here that the offset Rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. subtractOffset(b) and subtractOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Parameters:
            offset (FieldAngularCoordinates<FieldAngularCoordinates> offset): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            addOffset
        
        
        """
        ...
    def toAngularCoordinates(self) -> AngularCoordinates:
        """
        Convert to a regular angular coordinates.
        
        Returns:
            a regular angular coordinates
        
        
        """
        ...
    def toDerivativeStructureRotation(self, order: int) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_FieldAngularCoordinates__T]]:
        """
        Transform the instance to a FieldRotation<FieldDerivativeStructure>.
        
        The FieldDerivativeStructure coordinates correspond to time-derivatives up to the user-specified order.
        
        Parameters:
            order (int): derivation order for the vector components
        
        Returns:
            rotation with time-derivatives embedded within the coordinates
        
        Since:
            9.2
        
        
        """
        ...
    def toUnivariateDerivative1Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1[_FieldAngularCoordinates__T]]:
        """
        Transform the instance to a FieldRotation<UnivariateDerivative1>.
        
        The UnivariateDerivative1 coordinates correspond to time-derivatives up to the order 1.
        
        Returns:
            rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...
    def toUnivariateDerivative2Rotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldAngularCoordinates__T]]:
        """
        Transform the instance to a FieldRotation<UnivariateDerivative2>.
        
        The UnivariateDerivative2 coordinates correspond to time-derivatives up to the order 2.
        
        Returns:
            rotation with time-derivatives embedded within the coordinates
        
        
        """
        ...

_FieldArrayDictionary__T = typing.TypeVar('_FieldArrayDictionary__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldArrayDictionary(typing.Generic[_FieldArrayDictionary__T]):
    """
    String → CalculusFieldElement[] mapping, for small number of keys.
    
    This class is a low overhead for a very small number of keys. It is based on simple array and string comparison. It plays the same role a Map<String, T[]> but with reduced features and not intended for large number of keys. For such needs the regular Map<String, T[]> should be preferred.
    
    Since:
        11.1
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldArrayDictionary__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldArrayDictionary__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldArrayDictionary__T], map: typing.Union[java.util.Map[str, typing.Union[typing.List[_FieldArrayDictionary__T], jpype.JArray]], typing.Mapping[str, typing.Union[typing.List[_FieldArrayDictionary__T], jpype.JArray]]]): ...
    @typing.overload
    def __init__(self, fieldArrayDictionary: 'FieldArrayDictionary'[_FieldArrayDictionary__T]): ...
    def clear(self) -> None:
        """
        Remove all entries.
        """
        ...
    def get(self, key: str) -> typing.MutableSequence[_FieldArrayDictionary__T]:
        """
        Get the value corresponding to a key.
        
        Parameters:
            key (String): entry key
        
        Returns:
            copy of the value corresponding to the key or null if key not present
        
        
        """
        ...
    def getData(self) -> java.util.List['FieldArrayDictionary.Entry']:
        """
        Get an unmodifiable view of the dictionary entries.
        
        Returns:
            unmodifiable view of the dictionary entries
        
        
        """
        ...
    def getEntry(self, key: str) -> 'FieldArrayDictionary.Entry':
        """
        Get a complete entry.
        
        Parameters:
            key (String): entry key
        
        Returns:
            entry with key if it exists, null otherwise
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldArrayDictionary__T]:
        """
        Get the field to which elements belong.
        
        Returns:
            field to which elements belong
        
        
        """
        ...
    @typing.overload
    def put(self, string: str, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add an entry.
        
        If an entry with the same key already exists, it will be removed first.
        
        The new entry is always put at the end.
        
        Parameters:
            key (String): entry key
            value (FieldArrayDictionary[]): entry value
        
        Add an entry.
        
        If an entry with the same key already exists, it will be removed first.
        
        The new entry is always put at the end.
        
        Parameters:
            key (String): entry key
            value (double[]): entry value
        
        
        """
        ...
    @typing.overload
    def put(self, string: str, tArray: typing.Union[typing.List[_FieldArrayDictionary__T], jpype.JArray]) -> None: ...
    @typing.overload
    def putAll(self, map: typing.Union[java.util.Map[str, typing.Union[typing.List[_FieldArrayDictionary__T], jpype.JArray]], typing.Mapping[str, typing.Union[typing.List[_FieldArrayDictionary__T], jpype.JArray]]]) -> None: ...
    @typing.overload
    def putAll(self, fieldArrayDictionary: 'FieldArrayDictionary'[_FieldArrayDictionary__T]) -> None: ...
    def remove(self, key: str) -> bool:
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
    def toMap(self) -> java.util.Map[str, typing.MutableSequence[_FieldArrayDictionary__T]]:
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
        
        Overrides: Object in class Object
        
        Returns:
            string representation of the dictionary
        
        
        """
        ...
    def unmodifiableView(self) -> 'FieldArrayDictionary'[_FieldArrayDictionary__T]:
        """
        Get an unmodifiable view of the dictionary.
        
        The return dictionary is backed by the original instance and offers read-only access to it, but all operations that modify it throw an UnsupportedOperationException.
        
        Returns:
            unmodifiable view of the dictionary
        
        
        """
        ...
    class Entry:
        def getKey(self) -> str: ...
        def getValue(self) -> typing.MutableSequence[_FieldArrayDictionary__T]: ...
        @typing.overload
        def increment(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
        @typing.overload
        def increment(self, tArray: typing.Union[typing.List[_FieldArrayDictionary__T], jpype.JArray]) -> None: ...
        @typing.overload
        def scaledIncrement(self, double: float, fieldArrayDictionary: 'FieldArrayDictionary.Entry') -> None: ...
        @typing.overload
        def scaledIncrement(self, t: _FieldArrayDictionary__T, fieldArrayDictionary: 'FieldArrayDictionary.Entry') -> None: ...
        def size(self) -> int: ...
        def zero(self) -> None: ...

_FieldDataDictionary__T = typing.TypeVar('_FieldDataDictionary__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDataDictionary(typing.Generic[_FieldDataDictionary__T]):
    """
    String → Object mapping, for small number of keys.
    
    This class is a low overhead for a very small number of keys. It is based on simple array and string comparison. It plays the same role a Map<String, Object> but with reduced features and not intended for large number of keys. For such needs the regular Map<String, Object> should be preferred.
    
    Since:
        13.0
    
    Also see:
        FieldArrayDictionary
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDataDictionary__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDataDictionary__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDataDictionary__T], map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    @typing.overload
    def __init__(self, fieldDataDictionary: 'FieldDataDictionary'[_FieldDataDictionary__T]): ...
    def clear(self) -> None:
        """
        Remove all entries.
        """
        ...
    def get(self, key: str) -> typing.Any:
        """
        Get the value corresponding to a key.
        
        Parameters:
            key (String): entry key
        
        Returns:
            copy of the value corresponding to the key or null if key not present
        
        
        """
        ...
    def getData(self) -> java.util.List['FieldDataDictionary.Entry']:
        """
        Get an unmodifiable view of the dictionary entries.
        
        Returns:
            unmodifiable view of the dictionary entries
        
        
        """
        ...
    def getEntry(self, key: str) -> 'FieldDataDictionary.Entry':
        """
        Get a complete entry.
        
        Parameters:
            key (String): entry key
        
        Returns:
            entry with key if it exists, null otherwise
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldDataDictionary__T]:
        """
        Get the field to which elements belong.
        
        Returns:
            the field to which elements belong
        
        
        """
        ...
    def put(self, key: str, value: typing.Any) -> None:
        """
        Add an entry.
        
        If an entry with the same key already exists, it will be removed first.
        
        The new entry is always put at the end.
        
        Parameters:
            key (String): entry key
            value (Object): entry value
        
        
        """
        ...
    @typing.overload
    def putAll(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> None: ...
    @typing.overload
    def putAll(self, fieldDataDictionary: 'FieldDataDictionary'[_FieldDataDictionary__T]) -> None: ...
    def putAllFields(self, map: typing.Union[java.util.Map[str, typing.Union[typing.List[_FieldDataDictionary__T], jpype.JArray]], typing.Mapping[str, typing.Union[typing.List[_FieldDataDictionary__T], jpype.JArray]]]) -> None:
        """
        Put all the T[] entries from the map in the dictionary.
        
        Parameters:
            map (Map<String, FieldDataDictionary[]> map): map to copy into the instance
        
        
        """
        ...
    def remove(self, key: str) -> bool:
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
    def toFieldArrayDictionary(self) -> FieldArrayDictionary[_FieldDataDictionary__T]:
        """
        Creates a "field" values dictionary.
        
        Creates a DoubleArrayDictionary with all double[] values contained in the instance.
        
        Returns:
            a double values dictionary
        
        
        """
        ...
    def toMap(self) -> java.util.Map[str, typing.Any]:
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
        
        Overrides: Object in class Object
        
        Returns:
            string representation of the dictionary
        
        
        """
        ...
    class Entry:
        def getKey(self) -> str: ...
        def getValue(self) -> typing.Any: ...
        @typing.overload
        def scaledIncrement(self, double: float, fieldArrayDictionary: FieldArrayDictionary.Entry) -> None: ...
        @typing.overload
        def scaledIncrement(self, t: _FieldDataDictionary__T, fieldArrayDictionary: FieldArrayDictionary.Entry) -> None: ...

_FieldLegendrePolynomials__T = typing.TypeVar('_FieldLegendrePolynomials__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLegendrePolynomials(typing.Generic[_FieldLegendrePolynomials__T]):
    """
    Computes the P :sub:`nm` (t) coefficients.
    
    The computation of the Legendre polynomials is performed following: Heiskanen and Moritz, Physical Geodesy, 1967, eq. 1-62
    
    Since:
        11.0
    """
    def __init__(self, degree: int, order: int, t: _FieldLegendrePolynomials__T):
        """
        Create Legendre polynomials for the given degree and order.
        
        Parameters:
            degree (int): degree of the spherical harmonics
            order (int): order of the spherical harmonics
            t (FieldLegendrePolynomials): argument for polynomials calculation
        
        
        """
        ...
    def getPnm(self, n: int, m: int) -> _FieldLegendrePolynomials__T:
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
class FieldPVCoordinates(org.orekit.time.FieldTimeShiftable['FieldPVCoordinates'[_FieldPVCoordinates__T], _FieldPVCoordinates__T], org.hipparchus.util.FieldBlendable['FieldPVCoordinates'[_FieldPVCoordinates__T], _FieldPVCoordinates__T], typing.Generic[_FieldPVCoordinates__T]):
    """
    Simple container for Position/Velocity pairs, using CalculusFieldElement.
    
    The state can be slightly shifted to close dates. This shift is based on a simple linear model. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
    
    This class is the angular counterpart to FieldAngularCoordinates.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        6.0
    
    Also see:
        PVCoordinates
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
    def blendArithmeticallyWith(self, fieldPVCoordinates: 'FieldPVCoordinates'[_FieldPVCoordinates__T], t: _FieldPVCoordinates__T) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]:
        """
        Specified by: FieldBlendable in interface FieldBlendable
        
        Raises:
            MathIllegalArgumentException: 
        
        """
        ...
    def crossProduct(self, pv2: 'FieldPVCoordinates'[_FieldPVCoordinates__T]) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]:
        """
        Compute the cross-product of two instances.
        
        Parameters:
            pv2 (FieldPVCoordinates<FieldPVCoordinates> pv2): second instances
        
        Returns:
            the cross product v1 ^ v2 as a new instance
        
        
        """
        ...
    _estimateVelocity__T = typing.TypeVar('_estimateVelocity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def estimateVelocity(start: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateVelocity__T], end: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateVelocity__T], dt: float) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimateVelocity__T]:
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
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]:
        """
        Gets the acceleration.
        
        Returns:
            the acceleration vector (m/s²).
        
        
        """
        ...
    def getAngularVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]:
        """
        Get the angular velocity (spin) of this point as seen from the origin.
        
        The angular velocity vector is parallel to the getMomentum and is computed by ω = p × v / ||p||²
        
        Returns:
            the angular velocity vector
        
        Also see:
            `Angular Velocity on Wikipedia <http://en.wikipedia.org/wiki/Angular_velocity>`
        
        
        """
        ...
    def getMomentum(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]:
        """
        Gets the momentum.
        
        This vector is the p ⊗ v where p is position, v is velocity and ⊗ is cross product. To get the real physical angular momentum you need to multiply this vector by the mass.
        
        The returned vector is recomputed each time this method is called, it is not cached.
        
        Returns:
            a new instance of the momentum vector (m²/s).
        
        
        """
        ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]:
        """
        Gets the position.
        
        Returns:
            the position vector (m).
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]:
        """
        Gets the velocity.
        
        Returns:
            the velocity vector (m/s).
        
        
        """
        ...
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
    def negate(self) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]:
        """
        Get the opposite of the instance.
        
        Returns:
            a new position-velocity which is opposite to the instance
        
        
        """
        ...
    def normalize(self) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]:
        """
        Normalize the position part of the instance.
        
        The computed coordinates first component (position) will be a normalized vector, the second component (velocity) will be the derivative of the first component (hence it will generally not be normalized), and the third component (acceleration) will be the derivative of the second component (hence it will generally not be normalized).
        
        Returns:
            a new instance, with first component normalized and remaining component computed to have consistent derivatives
        
        
        """
        ...
    def positionShiftedBy(self, dt: _FieldPVCoordinates__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinates__T]:
        """
        Get a time-shifted position. Same as shiftedBy except that only the sifted position is returned.
        
        The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Parameters:
            dt (FieldPVCoordinates): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Since:
            11.2
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _FieldPVCoordinates__T: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldPVCoordinates__T) -> 'FieldPVCoordinates'[_FieldPVCoordinates__T]: ...
    def toDerivativeStructurePV(self, order: int) -> 'FieldPVCoordinates'[org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_FieldPVCoordinates__T]]:
        """
        Transform the instance to a FieldPVCoordinates<FieldDerivativeStructure>.
        
        The FieldDerivativeStructure coordinates correspond to time-derivatives up to the user-specified order. As both the instance components getPosition, getVelocity and getAcceleration and the FieldDerivativeStructure of the components holds time-derivatives, there are several ways to retrieve these derivatives. If for example the order is set to 2, then both getPartialDerivative(2), getPartialDerivative(1) and getValue() return the exact same value.
        
        If derivation order is 1, the first derivative of acceleration will be computed as a Keplerian-only jerk. If derivation order is 2, the second derivative of velocity (which is also the first derivative of acceleration) will be computed as a Keplerian-only jerk, and the second derivative of acceleration will be computed as a Keplerian-only jounce.
        
        Parameters:
            order (int): derivation order for the vector components (must be either 0, 1 or 2)
        
        Returns:
            pv coordinates with time-derivatives embedded within the coordinates
        
        Since:
            9.2
        
        
        """
        ...
    def toDerivativeStructureVector(self, order: int) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_FieldPVCoordinates__T]]:
        """
        Transform the instance to a FieldVector3D<FieldDerivativeStructure>.
        
        The FieldDerivativeStructure coordinates correspond to time-derivatives up to the user-specified order.
        
        Parameters:
            order (int): derivation order for the vector components (must be either 0, 1 or 2)
        
        Returns:
            vector with time-derivatives embedded within the coordinates
        
        Since:
            9.2
        
        
        """
        ...
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
        
        Overrides: Object in class Object
        
        Returns:
            string representation of this position/velocity pair
        
        
        """
        ...
    def toUnivariateDerivative1PV(self) -> 'FieldPVCoordinates'[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1[_FieldPVCoordinates__T]]:
        """
        Transform the instance to a FieldPVCoordinates<FieldUnivariateDerivative1>.
        
        The FieldUnivariateDerivative1 coordinates correspond to time-derivatives up to the order 1. The first derivative of acceleration will be computed as a Keplerian-only jerk.
        
        Returns:
            pv coordinates with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        
        """
        ...
    def toUnivariateDerivative1Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1[_FieldPVCoordinates__T]]:
        """
        Transform the instance to a FieldVector3D<FieldUnivariateDerivative1>.
        
        The FieldUnivariateDerivative1 coordinates correspond to time-derivatives up to the order 1.
        
        Returns:
            vector with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        Also see:
            toUnivariateDerivative2Vector
        
        
        """
        ...
    def toUnivariateDerivative2PV(self) -> 'FieldPVCoordinates'[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldPVCoordinates__T]]:
        """
        Transform the instance to a FieldPVCoordinates<FieldUnivariateDerivative2>.
        
        The FieldUnivariateDerivative2 coordinates correspond to time-derivatives up to the order 2. As derivation order is 2, the second derivative of velocity (which is also the first derivative of acceleration) will be computed as a Keplerian-only jerk, and the second derivative of acceleration will be computed as a Keplerian-only jounce.
        
        Returns:
            pv coordinates with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        
        """
        ...
    def toUnivariateDerivative2Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldPVCoordinates__T]]:
        """
        Transform the instance to a FieldVector3D<FieldUnivariateDerivative2>.
        
        The FieldUnivariateDerivative2 coordinates correspond to time-derivatives up to the order 2.
        
        Returns:
            vector with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        Also see:
            toUnivariateDerivative1Vector
        
        
        """
        ...

_FieldPVCoordinatesProvider__T = typing.TypeVar('_FieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPVCoordinatesProvider(typing.Generic[_FieldPVCoordinatesProvider__T]):
    """
    Interface for PV coordinates providers.
    """
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_FieldPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> 'TimeStampedFieldPVCoordinates'[_FieldPVCoordinatesProvider__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Parameters:
            date (FieldAbsoluteDate<FieldPVCoordinatesProvider> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_FieldPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinatesProvider__T]:
        """
        Get the position of the body in the selected frame.
        
        Parameters:
            date (FieldAbsoluteDate<FieldPVCoordinatesProvider> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        Since:
            12.0
        
        
        """
        ...
    def getVelocity(self, date: org.orekit.time.FieldAbsoluteDate[_FieldPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPVCoordinatesProvider__T]:
        """
        Get the velocity of the body in the selected frame.
        
        Parameters:
            date (FieldAbsoluteDate<FieldPVCoordinatesProvider> date): current date
            frame (Frame): the frame where to define the velocity
        
        Returns:
            velocity of the body (m/s)
        
        Since:
            13.1
        
        
        """
        ...

class FieldSortedListTrimmer:
    """
    A trimmer for externally stored chronologically sorted lists.
    
    Since:
        12.1
    """
    def __init__(self, neighborsSize: int):
        """
        Create a new cache with the given neighbors size and data.
        
        Parameters:
            neighborsSize (int): size of the list returned from getNeighborsSubList.
        
        
        """
        ...
    def getNeighborsSize(self) -> int:
        """
        Get size of the list returned from getNeighborsSubList.
        
        Returns:
            size of the list returned from getNeighborsSubList
        
        
        """
        ...
    _getNeighborsSubList__T = typing.TypeVar('_getNeighborsSubList__T', bound=org.orekit.time.FieldTimeStamped)  # <T>
    _getNeighborsSubList__K = typing.TypeVar('_getNeighborsSubList__K', bound=org.hipparchus.CalculusFieldElement)  # <K>
    def getNeighborsSubList(self, central: org.orekit.time.FieldAbsoluteDate[_getNeighborsSubList__K], data: java.util.List[_getNeighborsSubList__T]) -> java.util.List[_getNeighborsSubList__T]:
        """
        Get the entries surrounding a central date.
        
        If the central date is well within covered range, the returned array will be balanced with half the points before central date and half the points after it (depending on n parity, of course). If the central date is near the boundary, then the returned array will be unbalanced and will contain only the n earliest (or latest) entries. A typical example of the later case is leap seconds cache, since the number of leap seconds cannot be arbitrarily increased.
        
        Parameters:
            central (FieldAbsoluteDate<K> central): central date
            data (List<T> data): complete list of entries (must be chronologically sorted)
        
        Returns:
            entries surrounding the specified date (sublist of data)
        
        
        """
        ...

_FieldTimeSpanMap__Span__S = typing.TypeVar('_FieldTimeSpanMap__Span__S')  # <S>
_FieldTimeSpanMap__Span__F = typing.TypeVar('_FieldTimeSpanMap__Span__F', bound=org.hipparchus.CalculusFieldElement)  # <F>
_FieldTimeSpanMap__Transition__S = typing.TypeVar('_FieldTimeSpanMap__Transition__S')  # <S>
_FieldTimeSpanMap__Transition__F = typing.TypeVar('_FieldTimeSpanMap__Transition__F', bound=org.hipparchus.CalculusFieldElement)  # <F>
_FieldTimeSpanMap__T = typing.TypeVar('_FieldTimeSpanMap__T')  # <T>
_FieldTimeSpanMap__F = typing.TypeVar('_FieldTimeSpanMap__F', bound=org.hipparchus.CalculusFieldElement)  # <F>
class FieldTimeSpanMap(typing.Generic[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]):
    """
    Container for objects that apply to spans of time.
    
    Time span maps can be seen either as an ordered collection of Span or as an ordered collection of Transition. Both views are dual one to each other. A time span extends from one transition to the next one, and a transition separates one time span from the next one. Each time span contains one entry that is valid during the time span; this entry may be null if nothing is valid during this time span.
    
    Typical uses of FieldTimeSpanMap are to hold piecewise data, like for example an orbit count that changes at ascending nodes (in which case the entry would be an Integer), or a visibility status between several objects (in which case the entry would be a Boolean), or a drag coefficient that is expected to be estimated daily or three-hourly.
    
    Time span maps are built progressively. At first, they contain one Span only whose validity extends from past infinity to future infinity. Then new entries are added one at a time, associated with transition dates, in order to build up the complete map. The transition dates can be either the start of validity (when calling addValidAfter), or the end of the validity (when calling addValidBefore). Entries are often added at one end only (and mainly in chronological order), but this is not required. It is possible for example to first set up a map that covers a large range (say one day), and then to insert intermediate dates using for example propagation and event detectors to carve out some parts. This is akin to the way Binary Space Partitioning Trees work.
    
    Since 13.1, this class is thread-safe
    
    Since:
        7.1
    """
    def __init__(self, entry: _FieldTimeSpanMap__T, field: org.hipparchus.Field[_FieldTimeSpanMap__F]):
        """
        Create a map containing a single object, initially valid throughout the timeline.
        
        The real validity of this first entry will be truncated as other entries are either addValidBefore it or addValidAfter it.
        
        The initial configureExpunge is to never expunge any entries, it can be changed afterward by calling configureExpunge
        
        Parameters:
            entry (FieldTimeSpanMap): entry (initially valid throughout the timeline)
            field (Field<FieldTimeSpanMap> field): field used by default.
        
        
        """
        ...
    @typing.overload
    def addValidAfter(self, t: _FieldTimeSpanMap__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F], boolean: bool) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]: ...
    @typing.overload
    def addValidAfter(self, t: _FieldTimeSpanMap__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F]) -> None: ...
    @typing.overload
    def addValidBefore(self, t: _FieldTimeSpanMap__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F], boolean: bool) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]: ...
    @typing.overload
    def addValidBefore(self, t: _FieldTimeSpanMap__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F]) -> None: ...
    def addValidBetween(self, entry: _FieldTimeSpanMap__T, earliestValidityDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F], latestValidityDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F]) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Add an entry valid between two limit dates.
        
        As an entry is valid, it truncates or overrides the validity of the neighboring entries already present in the map.
        
        Parameters:
            entry (FieldTimeSpanMap): entry to add
            earliestValidityDate (FieldAbsoluteDate<FieldTimeSpanMap> earliestValidityDate): date after which the entry is valid
            latestValidityDate (FieldAbsoluteDate<FieldTimeSpanMap> latestValidityDate): date before which the entry is valid
        
        Returns:
            span with added entry
        
        Since:
            13.1
        
        
        """
        ...
    def configureExpunge(self, newMaxNbSpans: int, newMaxRange: float, newExpungePolicy: ExpungePolicy) -> None:
        """
        Configure (or reconfigure) expunge policy for later additions.
        
        When an entry is added to the map (using either addValidBefore, addValidBetween, or addValidAfter that exceeds the allowed capacity in terms of number of time spans or maximum time range between the earliest and the latest transitions, then exceeding data is expunged according to the expungePolicy.
        
        Note that as the policy depends on the date at which new entries are added, the policy will be enforced only for the next calls to addValidBefore, addValidBetween, and addValidAfter, it is not enforce immediately.
        
        Parameters:
            newMaxNbSpans (int): maximum number of time spans
            newMaxRange (double): maximum time range between the earliest and the latest transitions
            newExpungePolicy (ExpungePolicy): expunge policy to apply when capacity is exceeded
        
        Since:
            13.1
        
        
        """
        ...
    def extractRange(self, start: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F], end: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F]) -> 'FieldTimeSpanMap'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Extract a range of the map.
        
        The object returned will be a new independent instance that will contain only the transitions that lie in the specified range.
        
        Consider, for example, a map containing objects O₀ valid before t₁, O₁ valid between t₁ and t₂, O₂ valid between t₂ and t₃, O₃ valid between t₃ and t₄, and O₄ valid after t₄. then calling this method with a start date between t₁ and t₂ and a end date between t₃ and t₄ will result in a new map containing objects O₁ valid before t₂, O₂ valid between t₂ and t₃, and O₃ valid after t₃. The validity of O₁ is therefore extended in the past, and the validity of O₃ is extended in the future.
        
        Parameters:
            start (FieldAbsoluteDate<FieldTimeSpanMap> start): earliest date at which a transition is included in the range (may be set to
                PAST_INFINITY to keep all early transitions)
            end (FieldAbsoluteDate<FieldTimeSpanMap> end): latest date at which a transition is included in the r (may be set to
                FUTURE_INFINITY to keep all late transitions)
        
        Returns:
            a new instance with all transitions restricted to the specified range
        
        Since:
            13.1
        
        
        """
        ...
    def forEach(self, action: typing.Union[java.util.function.Consumer[_FieldTimeSpanMap__T], typing.Callable[[_FieldTimeSpanMap__T], None]]) -> None:
        """
        Performs an action for each non-null element of the map.
        
        The action is performed chronologically.
        
        Parameters:
            action (Consumer<FieldTimeSpanMap> action): action to perform on the non-null elements
        
        Since:
            13.1
        
        
        """
        ...
    def get(self, date: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F]) -> _FieldTimeSpanMap__T:
        """
        Get the entry valid at a specified date.
        
        The expected complexity is O(1) for successive calls with neighboring dates, which is the more frequent use in propagation or orbit determination applications, and O(n) for random calls.
        
        Parameters:
            date (FieldAbsoluteDate<FieldTimeSpanMap> date): date at which the entry must be valid
        
        Returns:
            valid entry at specified date
        
        Also see:
            getSpan
        
        
        """
        ...
    def getFirstNonNullSpan(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Get the first (earliest) span with non-null data.
        
        Returns:
            first (earliest) span with non-null data
        
        Since:
            13.1
        
        
        """
        ...
    def getFirstSpan(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Get the first (earliest) span.
        
        Returns:
            first (earliest) span
        
        Since:
            13.1
        
        
        """
        ...
    def getFirstTransition(self) -> 'FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Get the first (earliest) transition.
        
        Returns:
            first (earliest) transition, or null if there are no transitions
        
        Since:
            13.1
        
        
        """
        ...
    def getLastNonNullSpan(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Get the last (latest) span with non-null data.
        
        Returns:
            last (latest) span with non-null data
        
        Since:
            13.1
        
        
        """
        ...
    def getLastSpan(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Get the last (latest) span.
        
        Returns:
            last (latest) span
        
        Since:
            13.1
        
        
        """
        ...
    def getLastTransition(self) -> 'FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Get the last (latest) transition.
        
        Returns:
            last (latest) transition, or null if there are no transitions
        
        Since:
            13.1
        
        
        """
        ...
    def getSpan(self, date: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__F]) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]:
        """
        Get the time span containing a specified date.
        
        The expected complexity is O(1) for successive calls with neighboring dates, which is the more frequent use in propagation or orbit determination applications, and O(n) for random calls.
        
        Parameters:
            date (FieldAbsoluteDate<FieldTimeSpanMap> date): date belonging to the desired time span
        
        Returns:
            time span containing the specified date
        
        Since:
            13.1
        
        
        """
        ...
    def getSpansNumber(self) -> int:
        """
        Get the number of spans.
        
        The number of spans is always at least 1. The number of transitions is always 1 lower than the number of spans.
        
        Returns:
            number of spans
        
        Since:
            13.1
        
        
        """
        ...
    def getTransitions(self) -> java.util.SortedSet['FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__T, _FieldTimeSpanMap__F]]:
        """
        Deprecated. as of 13.1, this method is replaced by getFirstTransition and then following intertwined links between Span and Transition Get an unmodifiable view of the sorted transitions.
        
        Note that since 13.1, this method creates a copy of the current data, it therefore does not update when new spans are added
        
        Returns:
            unmodifiable view of the sorted transitions
        
        
        """
        ...
    class Span(typing.Generic[_FieldTimeSpanMap__Span__S, _FieldTimeSpanMap__Span__F]):
        def getData(self) -> _FieldTimeSpanMap__Span__S: ...
        def getEnd(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__Span__F]: ...
        def getEndTransition(self) -> 'FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__Span__S, _FieldTimeSpanMap__Span__F]: ...
        def getStart(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__Span__F]: ...
        def getStartTransition(self) -> 'FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__Span__S, _FieldTimeSpanMap__Span__F]: ...
        def next(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__Span__S, _FieldTimeSpanMap__Span__F]: ...
        def previous(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__Span__S, _FieldTimeSpanMap__Span__F]: ...
    class Transition(org.orekit.time.FieldTimeStamped[_FieldTimeSpanMap__Transition__F], typing.Generic[_FieldTimeSpanMap__Transition__S, _FieldTimeSpanMap__Transition__F]):
        def getAfter(self) -> _FieldTimeSpanMap__Transition__S: ...
        def getBefore(self) -> _FieldTimeSpanMap__Transition__S: ...
        def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__Transition__F]: ...
        def getSpanAfter(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__Transition__S, _FieldTimeSpanMap__Transition__F]: ...
        def getSpanBefore(self) -> 'FieldTimeSpanMap.Span'[_FieldTimeSpanMap__Transition__S, _FieldTimeSpanMap__Transition__F]: ...
        def next(self) -> 'FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__Transition__S, _FieldTimeSpanMap__Transition__F]: ...
        def previous(self) -> 'FieldTimeSpanMap.Transition'[_FieldTimeSpanMap__Transition__S, _FieldTimeSpanMap__Transition__F]: ...
        def resetDate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeSpanMap__Transition__F], boolean: bool) -> None: ...

_FieldTimeStampedCache__T = typing.TypeVar('_FieldTimeStampedCache__T', bound=org.orekit.time.FieldTimeStamped)  # <T>
_FieldTimeStampedCache__KK = typing.TypeVar('_FieldTimeStampedCache__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldTimeStampedCache(typing.Generic[_FieldTimeStampedCache__T, _FieldTimeStampedCache__KK]):
    """
    Interface for a data structure that can provide concurrent access to FieldTimeStamped data surrounding a given date.
    
    Also see:
        ImmutableFieldTimeStampedCache
    """
    def getEarliest(self) -> _FieldTimeStampedCache__T:
        """
        Get the earliest entry in this cache.
        
        Returns:
            earliest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getLatest(self) -> _FieldTimeStampedCache__T:
        """
        Get the latest entry in this cache.
        
        Returns:
            latest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getMaxNeighborsSize(self) -> int:
        """
        Get the fixed size of the lists returned by getNeighbors.
        
        Returns:
            size of the list
        
        
        """
        ...
    @typing.overload
    def getNeighbors(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeStampedCache__KK], int: int) -> java.util.stream.Stream[_FieldTimeStampedCache__T]: ...
    @typing.overload
    def getNeighbors(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeStampedCache__KK]) -> java.util.stream.Stream[_FieldTimeStampedCache__T]: ...

_FieldTrackingCoordinates__T = typing.TypeVar('_FieldTrackingCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTrackingCoordinates(typing.Generic[_FieldTrackingCoordinates__T]):
    """
    Container for azimut/elevation/range coordinates as seen from a ground point.
    
    Since:
        12.0
    
    Also see:
        TopocentricFrame
    """
    @typing.overload
    def __init__(self, t: _FieldTrackingCoordinates__T, t2: _FieldTrackingCoordinates__T, t3: _FieldTrackingCoordinates__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTrackingCoordinates__T], trackingCoordinates: 'TrackingCoordinates'): ...
    def getAzimuth(self) -> _FieldTrackingCoordinates__T:
        """
        Get the azimuth.
        
        The azimuth is the angle between the North direction at local point and the projection in local horizontal plane of the direction from local point to given point. Azimuth angles are counted clockwise, i.e positive towards the East.
        
        Returns:
            azimuth
        
        
        """
        ...
    def getElevation(self) -> _FieldTrackingCoordinates__T:
        """
        Get the elevation.
        
        The elevation is the angle between the local horizontal and the direction from local point to given point.
        
        Returns:
            elevation
        
        
        """
        ...
    def getRange(self) -> _FieldTrackingCoordinates__T:
        """
        Get the range.
        
        Returns:
            range
        
        
        """
        ...

class Fieldifier:
    """
    Utility class used to convert class to their Field equivalent.
    """
    _fieldify_0__T = typing.TypeVar('_fieldify_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _fieldify_1__T = typing.TypeVar('_fieldify_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def fieldify(field: org.hipparchus.Field[_fieldify_0__T], realMatrix: org.hipparchus.linear.RealMatrix) -> org.hipparchus.linear.FieldMatrix[_fieldify_0__T]:
        """
        Fieldify given matrix with given field.
        
        Parameters:
            field (Field<T> field): field to fieldify with
            matrix (RealMatrix): matrix to fieldify
        
        Returns:
            fielded matrix
        
        Fieldify given state covariance with given field.
        
        Parameters:
            field (Field<T> field): field to which the
            stateCovariance (StateCovariance): state covariance to fieldify
        
        Returns:
            fielded state covariance
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def fieldify(field: org.hipparchus.Field[_fieldify_1__T], stateCovariance: org.orekit.propagation.StateCovariance) -> org.orekit.propagation.FieldStateCovariance[_fieldify_1__T]: ...

class Formatter:
    """
    Formatter used to produce strings from data.
    
    Interface for formatters to be passed to generators, dictating how to write doubles and datetime.
    
    Since:
        13.0
    """
    STANDARDIZED_LOCALE: typing.ClassVar[java.util.Locale] = ...
    """
    Standardized locale to use, to ensure files can be exchanged without internationalization issues.
    """
    DATE_FORMAT: typing.ClassVar[str] = ...
    """
    String format used for dates.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def toString(self, double: float) -> str:
        """
        Format a double number.
        
        Parameters:
            value (double): number to format
        
        Returns:
            number formatted.
        
        Format a date. Does not check if date time is real or if it will meet formating requirements.
        
        Parameters:
            year (int): of date to be formatted
            month (int): of date to be formatted
            day (int): of month to be formatted
            hour (int): to be formatted
            minute (int): to be formatted
            seconds (double): and sub-seconds to be formatted
        
        Returns:
            date formatted to match the following format [yyyy-MM-ddTHH:mm:ss.S#]
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str: ...

class IERSConventions(java.lang.Enum['IERSConventions']):
    """
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
        Evaluate the date offset between the current date and the getNutationReferenceEpoch.
        
        This method uses the getDefault.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            date offset in Julian centuries
        
        Since:
            6.1
        
        Also see:
            evaluateTC
        
        Evaluate the date offset between the current date and the getNutationReferenceEpoch.
        
        Parameters:
            date (AbsoluteDate): current date
            timeScales (TimeScales): used in the evaluation.
        
        Returns:
            date offset in Julian centuries
        
        Since:
            10.1
        
        DefaultDataContext public <T extends CalculusFieldElement<T>> T evaluateTC (FieldAbsoluteDate<T> date)
        
        Evaluate the date offset between the current date and the getNutationReferenceEpoch.
        
        This method uses the getDefault.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            date offset in Julian centuries
        
        Since:
            9.0
        
        Also see:
            evaluateTC
        
        """
        ...
    @typing.overload
    def evaluateTC(self, absoluteDate: org.orekit.time.AbsoluteDate, timeScales: org.orekit.time.TimeScales) -> float: ...
    @typing.overload
    def evaluateTC(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_evaluateTC_2__T]) -> _evaluateTC_2__T: ...
    @typing.overload
    def evaluateTC(self, date: org.orekit.time.FieldAbsoluteDate[_evaluateTC_3__T], timeScales: org.orekit.time.TimeScales) -> _evaluateTC_3__T:
        """
        Evaluate the date offset between the current date and the getNutationReferenceEpoch.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            timeScales (TimeScales): used in the evaluation.
        
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
            timeScales (TimeScales): used in the computation. The TT and TAI scales are used.
        
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
        
        This method uses the getDefault.
        
        Returns:
            function computing tidal corrections for Earth Orientation Parameters, for xp, yp, ut1 and lod respectively
        
        Since:
            6.1
        
        Also see:
            getEOPTidalCorrection
        
        """
        ...
    @typing.overload
    def getEarthOrientationAngleFunction(self, timeScale: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction:
        """
        Get the function computing the raw Earth Orientation Angle.
        
        This method uses the getDefault.
        
        The raw angle does not contain any correction. If for example dTU1 correction due to tidal effect is desired, it must be added afterward by the caller. The returned value contain the angle as the value and the angular rate as the first derivative.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
        
        Returns:
            function computing the rawEarth Orientation Angle, in the non-rotating origin paradigm
        
        Since:
            6.1
        
        Also see:
            getEarthOrientationAngleFunction
        
        Get the function computing the raw Earth Orientation Angle.
        
        The raw angle does not contain any correction. If for example dTU1 correction due to tidal effect is desired, it must be added afterward by the caller. The returned value contain the angle as the value and the angular rate as the first derivative.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
            tai (TimeScale): TAI time scale
        
        Returns:
            function computing the rawEarth Orientation Angle, in the non-rotating origin paradigm
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getEarthOrientationAngleFunction(self, timeScale: org.orekit.time.TimeScale, timeScale2: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction: ...
    @typing.overload
    def getGASTFunction(self, ut1: org.orekit.time.TimeScale, eopHistory: org.orekit.frames.EOPHistory, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScalarFunction:
        """
        Get the function computing Greenwich apparent sidereal time, in radians.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
            eopHistory (EOPHistory): EOP history. If null then no nutation correction is applied for EOP.
            timeScales (TimeScales): TAI time scale.
        
        Returns:
            function computing Greenwich apparent sidereal time
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getGASTFunction(self, ut1: org.orekit.time.TimeScale, eopHistory: org.orekit.frames.EOPHistory) -> org.orekit.time.TimeScalarFunction:
        """
        Get the function computing Greenwich apparent sidereal time, in radians.
        
        This method uses the getDefault if eopHistory == null.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
            eopHistory (EOPHistory): EOP history. If null then no nutation correction is applied for EOP.
        
        Returns:
            function computing Greenwich apparent sidereal time
        
        Since:
            6.1
        
        Also see:
            getGASTFunction
        
        """
        ...
    @typing.overload
    def getGMSTFunction(self, ut1: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScalarFunction:
        """
        Get the function computing Greenwich mean sidereal time, in radians.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
            timeScales (TimeScales): other time scales used in the computation including TAI and TT.
        
        Returns:
            function computing Greenwich mean sidereal time
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getGMSTFunction(self, ut1: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction:
        """
        Get the function computing Greenwich mean sidereal time, in radians.
        
        This method uses the getDefault.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
        
        Returns:
            function computing Greenwich mean sidereal time
        
        Since:
            6.1
        
        Also see:
            getGMSTFunction
        
        """
        ...
    @typing.overload
    def getGMSTRateFunction(self, ut1: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeScalarFunction:
        """
        Get the function computing Greenwich mean sidereal time rate, in radians per second.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
            timeScales (TimeScales): other time scales used in the computation including TAI and TT.
        
        Returns:
            function computing Greenwich mean sidereal time rate
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getGMSTRateFunction(self, ut1: org.orekit.time.TimeScale) -> org.orekit.time.TimeScalarFunction:
        """
        Get the function computing Greenwich mean sidereal time rate, in radians per second.
        
        This method uses the getDefault.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
        
        Returns:
            function computing Greenwich mean sidereal time rate
        
        Since:
            9.0
        
        Also see:
            getGMSTRateFunction
        
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
            timeScales (TimeScales): used in computing the function.
        
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
        
        This method uses the getDefault.
        
        Returns:
            function computing mean obliquity of the ecliptic
        
        Since:
            6.1
        
        Also see:
            getMeanObliquityFunction
        
        """
        ...
    def getNominalTidalDisplacement(self) -> typing.MutableSequence[float]:
        """
        Get the nominal values of the displacement numbers.
        
        Returns:
            an array containing h⁽⁰⁾, h⁽²⁾, h₃, hI diurnal, hI semi-diurnal, l⁽⁰⁾, l⁽¹⁾ diurnal, l⁽¹⁾
            semi-diurnal, l⁽²⁾, l₃, lI diurnal, lI semi-diurnal, H₀ permanent deformation amplitude
        
        Since:
            9.1
        
        
        """
        ...
    @typing.overload
    def getNutationArguments(self, timeScale: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.data.FundamentalNutationArguments:
        """
        Get the fundamental nutation arguments.
        
        Parameters:
            timeScale (TimeScale): time scale for computing Greenwich Mean Sidereal Time (typically getUT1)
            timeScales (TimeScales): other time scales used in the computation including TAI and TT.
        
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
            timeScales (TimeScales): other time scales used in the computation including TAI and TT.
        
        Returns:
            fundamental nutation arguments
        
        Since:
            10.1
        
        Also see:
            getNutationArguments
        
        Get the fundamental nutation arguments.
        
        This method uses the getDefault.
        
        Parameters:
            timeScale (TimeScale): time scale for computing Greenwich Mean Sidereal Time (typically getUT1)
        
        Returns:
            fundamental nutation arguments
        
        Since:
            6.1
        
        Also see:
            getNutationArguments,
            getNutationArguments
        
        """
        ...
    @typing.overload
    def getNutationCorrectionConverter(self) -> 'IERSConventions.NutationCorrectionConverter':
        """
        Create a function converting nutation corrections between δX/δY and δΔψ/δΔε.
        
          - δX/δY nutation corrections are used with the Non-Rotating Origin paradigm.
          - δΔψ/δΔε nutation corrections are used with the equinox-based paradigm.
        
        This method uses the getDefault.
        
        Returns:
            a new converter
        
        Since:
            6.1
        
        Also see:
            getNutationCorrectionConverter
        
        """
        ...
    @typing.overload
    def getNutationCorrectionConverter(self, timeScales: org.orekit.time.TimeScales) -> 'IERSConventions.NutationCorrectionConverter':
        """
        Create a function converting nutation corrections between δX/δY and δΔψ/δΔε.
        
          - δX/δY nutation corrections are used with the Non-Rotating Origin paradigm.
          - δΔψ/δΔε nutation corrections are used with the equinox-based paradigm.
        
        
        Parameters:
            timeScales (TimeScales): used to define the conversion.
        
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
        
        The function returned computes the two classical angles ΔΨ and Δε, and the correction to the equation of equinoxes introduced since 1997-02-27 by IAU 1994 resolution C7 (the correction is forced to 0 before this date)
        
        Parameters:
            timeScales (TimeScales): used in the computation including TAI and TT.
        
        Returns:
            function computing the nutation in longitude ΔΨ and Δε and the correction of equation of equinoxes
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getNutationFunction(self) -> org.orekit.time.TimeVectorFunction:
        """
        Get the function computing the nutation angles.
        
        This method uses the getDefault.
        
        The function returned computes the two classical angles ΔΨ and Δε, and the correction to the equation of equinoxes introduced since 1997-02-27 by IAU 1994 resolution C7 (the correction is forced to 0 before this date)
        
        Returns:
            function computing the nutation in longitude ΔΨ and Δε and the correction of equation of equinoxes
        
        Since:
            6.1
        
        """
        ...
    @typing.overload
    def getNutationReferenceEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference epoch for fundamental nutation arguments.
        
        This method uses the getDefault.
        
        Returns:
            reference epoch for fundamental nutation arguments
        
        Since:
            6.1
        
        Also see:
            getNutationReferenceEpoch
        
        """
        ...
    @typing.overload
    def getNutationReferenceEpoch(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference epoch for fundamental nutation arguments.
        
        Parameters:
            timeScales (TimeScales): to use for the reference epoch.
        
        Returns:
            reference epoch for fundamental nutation arguments
        
        Since:
            10.1
        
        
        """
        ...
    def getOceanPoleTide(self, eopHistory: org.orekit.frames.EOPHistory) -> org.orekit.time.TimeVectorFunction:
        """
        Get the function computing ocean pole tide (ΔC₂₁, ΔS₂₁).
        
        Parameters:
            eopHistory (EOPHistory): EOP history
        
        Returns:
            model for ocean pole tide (ΔC₂₀, ΔC₂₁, ΔS₂₁, ΔC₂₂, ΔS₂₂).
        
        Since:
            6.1
        
        
        """
        ...
    def getPermanentTide(self) -> float:
        """
        Get the permanent tide to be removed from ΔC₂₀ when zero-tide potentials are used.
        
        Returns:
            permanent tide to remove
        
        
        """
        ...
    @typing.overload
    def getPrecessionFunction(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
        Get the function computing the precession angles.
        
        The function returned computes the three precession angles ψ :sub:`A` (around Z axis), ω :sub:`A` (around X axis) and χ :sub:`A` (around Z axis). The constant angle ε₀ for the fourth rotation (around X axis) can be retrieved by evaluating the function returned by getMeanObliquityFunction at getNutationReferenceEpoch.
        
        Parameters:
            timeScales (TimeScales): used to define the function.
        
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
        
        The function returned computes the three precession angles ψ :sub:`A` (around Z axis), ω :sub:`A` (around X axis) and χ :sub:`A` (around Z axis). The constant angle ε₀ for the fourth rotation (around X axis) can be retrieved by evaluating the function returned by getMeanObliquityFunction at getNutationReferenceEpoch.
        
        This method uses the getDefault.
        
        Returns:
            function computing the precession angle
        
        Since:
            6.1
        
        Also see:
            getPrecessionFunction
        
        """
        ...
    def getSolidPoleTide(self, eopHistory: org.orekit.frames.EOPHistory) -> org.orekit.time.TimeVectorFunction:
        """
        Get the function computing solid pole tide (ΔC₂₁, ΔS₂₁).
        
        Parameters:
            eopHistory (EOPHistory): EOP history
        
        Returns:
            model for solid pole tide (ΔC₂₀, ΔC₂₁, ΔS₂₁, ΔC₂₂, ΔS₂₂).
        
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
        
        protected static CompiledSeries getTidalDisplacementFrequencyCorrectionDiurnal (String tableName, int cols, int rIp, int rOp, int tIp, int tOp)
        
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
            rIp (int): column holding ∆Rf(ip) in the diurnal tides table, counting from 1
            rOp (int): column holding ∆Rf(op) in the diurnal tides table, counting from 1
            tIp (int): column holding ∆Tf(ip) in the diurnal tides table, counting from 1
            tOp (int): column holding ∆Tf(op) in the diurnal tides table, counting from 1
        
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
        
        protected static CompiledSeries getTidalDisplacementFrequencyCorrectionZonal (String tableName, int cols, int rIp, int rOp, int tIp, int tOp)
        
        Get the correction function for tidal displacement for zonal tides.
        
          - f[0]: radial correction
          - f[1]: North correction
        
        
        Parameters:
            tableName (String): name for the zonal tides table
            cols (int): total number of columns of the table
            rIp (int): column holding ∆Rf(ip) in the table, counting from 1
            rOp (int): column holding ∆Rf(op) in the table, counting from 1
            tIp (int): column holding ∆Tf(ip) in the table, counting from 1
            tOp (int): column holding ∆Tf(op) in the table, counting from 1
        
        Returns:
            correction function for tidal displacement for zonal tides
        
        Since:
            9.1
        
        
        """
        ...
    @typing.overload
    def getTideFrequencyDependenceFunction(self, ut1: org.orekit.time.TimeScale, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
        Parameters:
            ut1 (TimeScale): UT1 time scale
            timeScales (TimeScales): other time scales used in the computation including TAI and TT.
        
        Returns:
            frequency dependence model for tides computation (ΔC₂₀, ΔC₂₁, ΔS₂₁, ΔC₂₂, ΔS₂₂).
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    def getTideFrequencyDependenceFunction(self, ut1: org.orekit.time.TimeScale) -> org.orekit.time.TimeVectorFunction:
        """
        This method uses the getDefault.
        
        Parameters:
            ut1 (TimeScale): UT1 time scale
        
        Returns:
            frequency dependence model for tides computation (ΔC₂₀, ΔC₂₁, ΔS₂₁, ΔC₂₂, ΔS₂₂).
        
        Since:
            6.1
        
        Also see:
            getTideFrequencyDependenceFunction
        
        """
        ...
    @typing.overload
    def getXYSpXY2Function(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.time.TimeVectorFunction:
        """
        Get the function computing the Celestial Intermediate Pole and Celestial Intermediate Origin components.
        
        The returned function computes the two X, Y components of CIP and the S+XY/2 component of the non-rotating CIO.
        
        Parameters:
            timeScales (TimeScales): used to define the function.
        
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
        
        This method uses the getDefault.
        
        Returns:
            function computing the Celestial Intermediate Pole and Celestial Intermediate Origin components
        
        Since:
            6.1
        
        Also see:
            getXYSpXY2Function
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'IERSConventions':
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
    def values() -> typing.MutableSequence['IERSConventions']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (IERSConventions c : IERSConventions.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...
    class NutationCorrectionConverter:
        def toEquinox(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float) -> typing.MutableSequence[float]: ...
        def toNonRotating(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float) -> typing.MutableSequence[float]: ...

class InterpolationTableLoader(org.orekit.data.DataLoader):
    """
    Used to read an interpolation table from a data file.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def getAbscissaGrid(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the abscissa grid for the interpolation function.
        
        Returns:
            the abscissa grid for the interpolation function, or null if the file could not be read
        
        
        """
        ...
    def getOrdinateGrid(self) -> typing.MutableSequence[float]:
        """
        Returns a copy of the ordinate grid for the interpolation function.
        
        Returns:
            the ordinate grid for the interpolation function, or null if the file could not be read
        
        
        """
        ...
    def getValuesSamples(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Returns a copy of the values samples for the interpolation function.
        
        Returns:
            the values samples for the interpolation function, or null if the file could not be read
        
        
        """
        ...
    def loadData(self, input: java.io.InputStream, name: str) -> None:
        """
        Loads an bi-variate interpolation table from the given InputStream. The format of the table is as follows (number of rows/columns can be extended):
        
          Table: tableName
        
              | 0.0 |  60.0 |  66.0 ------------------------- 0 | 0.0 | 0.003 | 0.006 500 | 0.0 | 0.003 | 0.006
        
        Specified by: loadData in interface DataLoader
        
        Parameters:
            input (InputStream): the input stream to read data from
            name (String): the name of the input file
        
        Raises:
            IOException: if data can't be read
            ParseException: if data can't be parsed
        
        
        """
        ...
    def stillAcceptsData(self) -> bool:
        """
        Check if the loader still accepts new data.
        
        This method is used to speed up data loading by interrupting crawling the data sets as soon as a loader has found the data it was waiting for. For loaders that can merge data from any number of sources (for example JPL ephemerides or Earth Orientation Parameters that are split among several files), this method should always return true to make sure no data is left over.
        
        Specified by: stillAcceptsData in interface DataLoader
        
        Returns:
            true while the loader still accepts new data
        
        
        """
        ...

class LagrangianPoints(java.lang.Enum['LagrangianPoints']):
    """
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
    def valueOf(name: str) -> 'LagrangianPoints':
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
    def values() -> typing.MutableSequence['LagrangianPoints']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (LagrangianPoints c : LagrangianPoints.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LegendrePolynomials:
    """
    Computes the P :sub:`nm` (t) coefficients.
    
    The computation of the Legendre polynomials is performed following: Heiskanen and Moritz, Physical Geodesy, 1967, eq. 1-62
    
    Since:
        11.0
    """
    def __init__(self, degree: int, order: int, t: float):
        """
        Create Legendre polynomials for the given degree and order.
        
        Parameters:
            degree (int): degree of the spherical harmonics
            order (int): order of the spherical harmonics
            t (double): argument for polynomials calculation
        
        
        """
        ...
    def getPnm(self, n: int, m: int) -> float:
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
    Container for Love numbers.
    
    Since:
        6.1
    
    Also see:
        serialized
    """
    def __init__(self, real: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], imaginary: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], plus: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            real (double[][]): real part of the nominal Love numbers
            imaginary (double[][]): imaginary part of the nominal Love numbers
            plus (double[][]): time-dependent part of the Love numbers
        
        
        """
        ...
    def getImaginary(self, n: int, m: int) -> float:
        """
        Get the imaginary part of a nominal Love numbers.
        
        Parameters:
            n (int): degree of the Love number (must be less than getSize)
            m (int): order of the Love number (must be less than n)
        
        Returns:
            imaginary part of k :sub:`n,m`
        
        
        """
        ...
    def getPlus(self, n: int, m: int) -> float:
        """
        Get the real part of a nominal Love numbers.
        
        Parameters:
            n (int): degree of the Love number (must be less than getSize)
            m (int): order of the Love number (must be less than n)
        
        Returns:
            k :sub:`n,m` :sup:`+`
        
        
        """
        ...
    def getReal(self, n: int, m: int) -> float:
        """
        Get the real part of a nominal Love numbers.
        
        Parameters:
            n (int): degree of the Love number (must be less than getSize)
            m (int): order of the Love number (must be less than n)
        
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
    Interface for Multiple shooting methods.
    
    Since:
        10.2
    """
    def compute(self) -> java.util.List[org.orekit.propagation.SpacecraftState]:
        """
        Return the list of corrected patch points. An optimizer is better suited for this problem
        
        Returns:
            patchedSpacecraftStates
        
        
        """
        ...

_OccultationEngine__FieldOccultationAngles__T = typing.TypeVar('_OccultationEngine__FieldOccultationAngles__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class OccultationEngine:
    """
    Computation engine for occultation events.
    
    Since:
        12.0
    """
    def __init__(self, occulted: typing.Union['ExtendedPositionProvider', typing.Callable], occultedRadius: float, occulting: org.orekit.bodies.OneAxisEllipsoid):
        """
        Build a new occultation engine.
        
        Parameters:
            occulted (ExtendedPositionProvider): the body to be occulted
            occultedRadius (double): the radius of the body to be occulted (m)
            occulting (OneAxisEllipsoid): the occulting body
        
        
        """
        ...
    _angles_0__T = typing.TypeVar('_angles_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def angles(self, state: org.orekit.propagation.FieldSpacecraftState[_angles_0__T]) -> 'OccultationEngine.FieldOccultationAngles'[_angles_0__T]:
        """
        Compute the occultation angles as seen from a spacecraft.
        
        Parameters:
            state (FieldSpacecraftState<T> state): the current state information: date, kinematics, attitude
        
        Returns:
            occultation angles
        
        
        """
        ...
    @typing.overload
    def angles(self, state: org.orekit.propagation.SpacecraftState) -> 'OccultationEngine.OccultationAngles':
        """
        Compute the occultation angles as seen from a spacecraft.
        
        Parameters:
            state (SpacecraftState): the current state information: date, kinematics, attitude
        
        Returns:
            occultation angles
        
        """
        ...
    def getOcculted(self) -> 'ExtendedPositionProvider':
        """
        Getter for the occulted body.
        
        Returns:
            the occulted body
        
        
        """
        ...
    def getOccultedRadius(self) -> float:
        """
        Getter for the occultedRadius.
        
        Returns:
            the occultedRadius
        
        
        """
        ...
    def getOcculting(self) -> org.orekit.bodies.OneAxisEllipsoid:
        """
        Getter for the occulting body.
        
        Returns:
            the occulting body
        
        
        """
        ...
    class FieldOccultationAngles(typing.Generic[_OccultationEngine__FieldOccultationAngles__T]):
        def getLimbRadius(self) -> _OccultationEngine__FieldOccultationAngles__T: ...
        def getOccultedApparentRadius(self) -> _OccultationEngine__FieldOccultationAngles__T: ...
        def getSeparation(self) -> _OccultationEngine__FieldOccultationAngles__T: ...
    class OccultationAngles:
        def getLimbRadius(self) -> float: ...
        def getOccultedApparentRadius(self) -> float: ...
        def getSeparation(self) -> float: ...

class OrekitConfiguration:
    """
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
    def getOrekitVersion() -> str:
        """
        Get Orekit version.
        
        The version is automatically retrieved from a properties file generated at maven compilation time. When using an IDE not configured to use maven, then a default value "unknown" will be returned.
        
        Returns:
            Orekit version
        
        Since:
            13.0
        
        
        """
        ...
    @staticmethod
    def setCacheSlotsNumber(slotsNumber: int) -> None:
        """
        Set the number of slots to use in caches.
        
        Parameters:
            slotsNumber (int): number of slots to use in caches
        
        
        """
        ...

class PVCoordinates(org.orekit.time.TimeShiftable['PVCoordinates'], org.hipparchus.util.Blendable['PVCoordinates']):
    """
    Simple container for Position/Velocity/Acceleration triplets.
    
    The state can be slightly shifted to close dates. This shift is based on a simple quadratic model. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
    
    This class is the angular counterpart to AngularCoordinates.
    
    Instances of this class are guaranteed to be immutable.
    """
    ZERO: typing.ClassVar['PVCoordinates'] = ...
    """
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
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, pVCoordinates: 'PVCoordinates', pVCoordinates2: 'PVCoordinates'): ...
    def blendArithmeticallyWith(self, pVCoordinates: 'PVCoordinates', double: float) -> 'PVCoordinates':
        """
        Specified by: Blendable in interface Blendable
        
        Raises:
            MathIllegalArgumentException: 
        
        """
        ...
    @staticmethod
    def crossProduct(pv1: 'PVCoordinates', pv2: 'PVCoordinates') -> 'PVCoordinates':
        """
        Compute the cross-product of two instances.
        
        Parameters:
            pv1 (PVCoordinates): first instances
            pv2 (PVCoordinates): second instances
        
        Returns:
            the cross product v1 ^ v2 as a new instance
        
        
        """
        ...
    @staticmethod
    def estimateVelocity(start: org.hipparchus.geometry.euclidean.threed.Vector3D, end: org.hipparchus.geometry.euclidean.threed.Vector3D, dt: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
            the acceleration vector (m/s²).
        
        
        """
        ...
    def getAngularVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the angular velocity (spin) of this point as seen from the origin.
        
        The angular velocity vector is parallel to the getMomentum and is computed by ω = p × v / ||p||²
        
        Returns:
            the angular velocity vector
        
        Also see:
            `Angular Velocity on Wikipedia <http://en.wikipedia.org/wiki/Angular_velocity>`
        
        
        """
        ...
    def getMomentum(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Gets the momentum.
        
        This vector is the p ⊗ v where p is position, v is velocity and ⊗ is cross product. To get the real physical angular momentum you need to multiply this vector by the mass.
        
        The returned vector is recomputed each time this method is called, it is not cached.
        
        Returns:
            a new instance of the momentum vector (m²/s).
        
        
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
        
        The computed coordinates first component (position) will be a normalized vector, the second component (velocity) will be the derivative of the first component (hence it will generally not be normalized), and the third component (acceleration) will be the derivative of the second component (hence it will generally not be normalized).
        
        Returns:
            a new instance, with first component normalized and remaining component computed to have consistent derivatives
        
        
        """
        ...
    def positionShiftedBy(self, dt: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get a time-shifted position. Same as shiftedBy except that only the sifted position is returned.
        
        The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, dt: org.orekit.time.TimeOffset) -> org.orekit.time.TimeShiftable:
        """
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'PVCoordinates': ...
    def toDerivativeStructurePV(self, order: int) -> FieldPVCoordinates[org.hipparchus.analysis.differentiation.DerivativeStructure]:
        """
        Transform the instance to a FieldPVCoordinates<DerivativeStructure>.
        
        The DerivativeStructure coordinates correspond to time-derivatives up to the user-specified order. As both the instance components getPosition, getVelocity and getAcceleration and the DerivativeStructure of the components holds time-derivatives, there are several ways to retrieve these derivatives. If for example the order is set to 2, then both getPartialDerivative(2), getPartialDerivative(1) and getValue() return the exact same value.
        
        If derivation order is 1, the first derivative of acceleration will be computed as a Keplerian-only jerk. If derivation order is 2, the second derivative of velocity (which is also the first derivative of acceleration) will be computed as a Keplerian-only jerk, and the second derivative of acceleration will be computed as a Keplerian-only jounce.
        
        Parameters:
            order (int): derivation order for the vector components (must be either 0, 1 or 2)
        
        Returns:
            pv coordinates with time-derivatives embedded within the coordinates
        
        Since:
            9.2
        
        
        """
        ...
    def toDerivativeStructureVector(self, order: int) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.DerivativeStructure]:
        """
        Transform the instance to a FieldVector3D<DerivativeStructure>.
        
        The DerivativeStructure coordinates correspond to time-derivatives up to the user-specified order.
        
        Parameters:
            order (int): derivation order for the vector components (must be either 0, 1 or 2)
        
        Returns:
            vector with time-derivatives embedded within the coordinates
        
        
        """
        ...
    def toString(self) -> str:
        """
        Return a string representation of this position/velocity pair.
        
        Overrides: Object in class Object
        
        Returns:
            string representation of this position/velocity pair
        
        
        """
        ...
    def toUnivariateDerivative1PV(self) -> FieldPVCoordinates[org.hipparchus.analysis.differentiation.UnivariateDerivative1]:
        """
        Transform the instance to a FieldPVCoordinates<UnivariateDerivative1>.
        
        The UnivariateDerivative1 coordinates correspond to time-derivatives up to the order 1. The first derivative of acceleration will be computed as a Keplerian-only jerk.
        
        Returns:
            pv coordinates with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        
        """
        ...
    def toUnivariateDerivative1Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative1]:
        """
        Transform the instance to a FieldVector3D<UnivariateDerivative1>.
        
        The UnivariateDerivative1 coordinates correspond to time-derivatives up to the order 1.
        
        Returns:
            vector with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        Also see:
            toUnivariateDerivative2Vector
        
        
        """
        ...
    def toUnivariateDerivative2PV(self) -> FieldPVCoordinates[org.hipparchus.analysis.differentiation.UnivariateDerivative2]:
        """
        Transform the instance to a FieldPVCoordinates<UnivariateDerivative2>.
        
        The UnivariateDerivative2 coordinates correspond to time-derivatives up to the order 2. As derivation order is 2, the second derivative of velocity (which is also the first derivative of acceleration) will be computed as a Keplerian-only jerk, and the second derivative of acceleration will be computed as a Keplerian-only jounce.
        
        Returns:
            pv coordinates with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        
        """
        ...
    def toUnivariateDerivative2Vector(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative2]:
        """
        Transform the instance to a FieldVector3D<UnivariateDerivative2>.
        
        The UnivariateDerivative2 coordinates correspond to time-derivatives up to the order 2.
        
        Returns:
            vector with time-derivatives embedded within the coordinates
        
        Since:
            10.2
        
        Also see:
            toUnivariateDerivative1Vector
        
        
        """
        ...

class PVCoordinatesProvider:
    """
    Interface for PV coordinates providers.
    """
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position of the body in the selected frame.
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        Since:
            12.0
        
        
        """
        ...
    def getVelocity(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the velocity of the body in the selected frame.
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the velocity
        
        Returns:
            velocity of the body (m/s)
        
        Since:
            13.1
        
        
        """
        ...

class ParameterDriver:
    """
    Class allowing to drive the value of a parameter.
    
    This class is typically used as a bridge between an estimation algorithm (typically orbit determination or optimizer) and an internal parameter in a physical model that needs to be tuned, or a bridge between a finite differences algorithm and an internal parameter in a physical model that needs to be slightly offset. The physical model will expose to the algorithm a set of instances of this class so the algorithm can call the setValue method to update the parameter value at a given date. Some parameters driver only have 1 value estimated/driven over the all period (constructor by default). Some others have several values estimated/driven on several periods/intervals. For example if the time period is 3 days for a drag parameter estimated all days then 3 values would be estimated, one for each time period. In order to allow several values to be estimated, the PDriver has a name and a value TimeSpanMap as attribute. In order, to cut the time span map there are 2 options :
    
      - Passive cut calling the addSpans method. Given a start date, an end date and
        and a validity period (in sec) for the driver, the addSpans method will cut
        the interval of name and value time span map from start date to date end in several interval of validity period
        duration. This method should not be called on orbital drivers and must be called only once at beginning of the process
        (for example beginning of orbit determination). WARNING : In order to ensure convergence for orbit determination, the
        start, end date and driver periodicity must be wisely chosen. There must be enough measurements on each interval or
        convergence won't reach or singular matrices will appear.
      - Active cut calling the addSpanAtDate method. Given a date, the method will cut
        the value and name time span name, in order to have a new span starting at the given date. Can be called several time to
        cut the time map as wished. WARNING : In order to ensure convergence for orbit determination, if the method is called
        several time, the start date must be wisely chosen. There must be enough measurements on each interval or convergence
        won't reach or singular matrices will appear.
    
    Several ways exist in order to get a ParameterDriver value at a certain date for parameters having several values on several intervals.
    
      - First of all, the step estimation, that is to say, if a value wants to be known at a certain date, the value returned is
        the one of span beginning corresponding to the date. With this definition a value will be kept constant all along the
        span duration and will be the value at span start.
      - The continuous estimation, that is to say, when a value wants be to known at a date t, the value returned would be a
        linear interpolation between the value at the beginning of the span corresponding to date t and end this span (which is
        also the beginning of next span). NOT IMPLEMENTED FOR NOW
    
    Each time the value is set, the physical model will be notified as it will register a ParameterObserver for this purpose.
    
    This design has two major goals. First, it allows an external algorithm to drive internal parameters blindly, as it only needs to get a list of instances of this class, without knowing what they really drive. Second, it allows the physical model to not expose directly setters methods for its parameters. In order to be able to modify the parameter value, the algorithm must retrieve a parameter driver.
    
    Since:
        8.0
    
    Also see:
        ParameterObserver
    """
    SPAN: typing.ClassVar[str] = ...
    """
    Name of the parameter.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, string: str, timeSpanMap: 'TimeSpanMap'[str], timeSpanMap2: 'TimeSpanMap'[float], double: float, double2: float, double3: float, double4: float): ...
    def addObserver(self, observer: 'ParameterObserver') -> None:
        """
        Add an observer for this driver.
        
        The observer valueSpanMapChanged method is called once automatically when the observer is added, and then called at each value change.
        
        Parameters:
            observer (ParameterObserver): observer to add while being updated
        
        
        """
        ...
    def addSpanAtDate(self, spanStartDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Create a new span in values and names time span map given a start date. One must be aware of the importance of choosing wise dates if this function is called several times to create several span at wanted times. Indeed, if orbit determination is performed it might not converge or find singular matrix if the spans are too short and contains to few measurements. Must be called before any computation (for example before orbit determination).
        
        Parameters:
            spanStartDate (AbsoluteDate): wanted start date for parameter value interval starts to be estimated.
        
        Since:
            12.0
        
        
        """
        ...
    def addSpans(self, orbitDeterminationStartDate: org.orekit.time.AbsoluteDate, orbitDeterminationEndDate: org.orekit.time.AbsoluteDate, validityPeriodForDriver: float) -> None:
        """
        Cut values and names time span map given orbit determination start and end and driver periodicity.
        
        For example for a drag coefficient the validity period would be 1 days = 86400sec. To be called after constructor to cut the temporal axis with the wanted parameter driver temporality for estimations on the wanted interval.
        
        Must be called only once at the beginning of orbit determination for example. If called several times, will throw exception. If parameter estimations intervals must be changed then a new ParameterDriver must be created or the function addSpanAtDate should be used.
        
        This function should not be called on DateDriver and any of ParameterDrivenDateIntervalDetector attribute, because there is no sense to estimate several values for dateDriver.
        
        The choice of orbitDeterminationStartDate, orbitDeterminationEndDate and validityPeriodForDriver in a case of orbit determination must be done carefully, indeed, enough measurement should be available for each time interval or the orbit determination won't converge.
        
        Parameters:
            orbitDeterminationStartDate (AbsoluteDate): start date for which the parameter driver starts to be estimated.
            orbitDeterminationEndDate (AbsoluteDate): end date for which the parameter driver stops to be estimated.
            validityPeriodForDriver (double): validity period for which the parameter value is effective (for example 1 day for drag coefficient). Warning,
                validityPeriod should not be too short or the orbit determination won't converge.
        
        Since:
            12.0
        
        
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
        Get parameter driver general name.
        
        Returns:
            name
        
        
        """
        ...
    def getNameSpan(self, date: org.orekit.time.AbsoluteDate) -> str:
        """
        Get name of the parameter span for a specific date.
        
        Parameters:
            date (AbsoluteDate): date at which the name of the span wants to be known
        
        Returns:
            name data of the name time span map at date
        
        
        """
        ...
    def getNamesSpanMap(self) -> 'TimeSpanMap'[str]:
        """
        Get current name span map of the parameterDriver, cut in interval in accordance with value span map and validity period.
        
        Note that if the expunge policy of the names map is configureExpunge, then the expunge policy of the getValueSpanMap should be reconfigured too with the same settings.
        
        Returns:
            current name span map
        
        Since:
            12.0
        
        
        """
        ...
    def getNbOfValues(self) -> int:
        """
        Get the number of values to estimate that is to say the number. of Span present in valueSpanMap
        
        Returns:
            int the number of values to estimate
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def getNormalizedValue(self) -> float:
        """
        for which the setPeriod method wasn't called) otherwise it will throw an exception.
        
        The normalized value is a non-dimensional value suitable for use as part of a vector in an optimization process. It is computed as (current - reference)/scale.
        
        Returns:
            normalized value
        
        
        """
        ...
    @typing.overload
    def getNormalizedValue(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get normalized value at specific date.
        
        The normalized value is a non-dimensional value suitable for use as part of a vector in an optimization process. It is computed as (current - reference)/scale.
        
        Parameters:
            date (AbsoluteDate): date for which the normalized value wants to be known
        
        Returns:
            normalized value
        
        """
        ...
    def getObservers(self) -> java.util.List['ParameterObserver']:
        """
        Get the observers for this driver.
        
        Returns:
            an unmodifiable view of the observers for this driver
        
        Since:
            9.1
        
        
        """
        ...
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
    def getTransitionDates(self) -> typing.MutableSequence[org.orekit.time.AbsoluteDate]:
        """
        Get the dates of the transitions TimeSpanMap.
        
        Returns:
            dates of the transitions TimeSpanMap
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def getValue(self) -> float:
        """
        to say for which the setPeriod method wasn't called)
        
        Returns:
            current parameter value
        
        """
        ...
    @typing.overload
    def getValue(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
        Get current parameter value at specific date, depending on isContinuousEstimation value, the value returned will be obtained by step estimation or continuous estimation.
        
        Parameters:
            date (AbsoluteDate): date for which the value wants to be known. Only if parameter driver has 1 value estimated over the all orbit
                determination period (not validity period intervals for estimation), the date value can be null and then the
                only estimated value will be returned, in this case the date can also be whatever the value returned would be the same.
                Moreover in this particular case one can also call the getValue.
        
        Returns:
            current parameter value at date date, or for the all period if no validity period (= 1 value estimated over the all
            orbit determination period)
        
        public Gradient getValue (int freeParameters, Map<String, Integer> indices)
        
        Get the value as a gradient at special date.
        
        Parameters:
            freeParameters (int): total number of free parameters in the gradient
            indices (Map<String, Integer> indices): indices of the differentiation parameters in derivatives computations
        
        Returns:
            value with derivatives, will throw exception if called on a PDriver having several values driven
        
        Since:
            10.2
        
        public Gradient getValue (int freeParameters, Map<String, Integer> indices, AbsoluteDate date)
        
        Get the value as a gradient at special date.
        
        Parameters:
            freeParameters (int): total number of free parameters in the gradient
            indices (Map<String, Integer> indices): indices of the differentiation parameters in derivatives computations, must be span name and not driver name
            date (AbsoluteDate): date for which the value wants to be known. Only if parameter driver has 1 value estimated over the all orbit
                determination period (not validity period intervals for estimation), the date value can be null and then the
                only estimated value will be returned
        
        Returns:
            value with derivatives
        
        Since:
            10.2
        
        
        """
        ...
    @typing.overload
    def getValue(self, int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]]) -> org.hipparchus.analysis.differentiation.Gradient: ...
    @typing.overload
    def getValue(self, int: int, map: typing.Union[java.util.Map[str, int], typing.Mapping[str, int]], absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.analysis.differentiation.Gradient: ...
    def getValueContinuousEstimation(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get current parameter value at specific date with continuous estimation.
        
        Parameters:
            date (AbsoluteDate): date for which the value wants to be known. Only if parameter driver has 1 value estimated over the all orbit
                determination period (not validity period intervals for estimation), the date value can be null and then the
                only estimated value will be returned, in this case the date can also be whatever the value returned would be the same.
                Moreover in this particular case one can also call the getValue.
        
        Returns:
            current parameter value at date date, or for the all period if no validity period (= 1 value estimated over the all
            orbit determination period)
        
        Since:
            12.0
        
        
        """
        ...
    def getValueSpanMap(self) -> 'TimeSpanMap'[float]:
        """
        Get value time span map for parameterDriver.
        
        Note that if the expunge policy of the values map is configureExpunge, then the expunge policy of the getNamesSpanMap names map} should be reconfigured too with the same settings.
        
        Returns:
            value time span map
        
        Since:
            12.0
        
        
        """
        ...
    def getValueStepEstimation(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get current parameter value at specific date with step estimation.
        
        Parameters:
            date (AbsoluteDate): date for which the value wants to be known. Only if parameter driver has 1 value estimated over the all orbit
                determination period (not validity period intervals for estimation), the date value can be null and then the
                only estimated value will be returned, in this case the date can also be whatever the value returned would be the same.
                Moreover in this particular case one can also call the getValue.
        
        Returns:
            current parameter value at date date, or for the all period if no validity period (= 1 value estimated over the all
            orbit determination period)
        
        
        """
        ...
    def getValues(self) -> typing.MutableSequence[float]:
        """
        Get all values of the valueSpanMap in the chronological order.
        
        Returns:
            double[] containing values of the valueSpanMap in the chronological order
        
        
        """
        ...
    def isContinuousEstimation(self) -> bool:
        """
        Check if parameter estimation is continuous, that is to say when a value wants to be known at date t, the value returned will be an interpolation between start value on span corresponding for date t and end value (which corresponds to the start of the next span), continuous estimation. Or not continuous, that is to say when a value wants to be known at date t, the value returned will be the value of the start of span corresponding to date t, step estimation.
        
        Returns:
            true if continuous estimation/definition, false if step estimation/definition
        
        Since:
            12.0
        
        
        """
        ...
    def isSelected(self) -> bool:
        """
        Check if parameter is selected.
        
        Selection is used for estimated parameters in orbit determination, or to compute the Jacobian matrix in partial derivatives computation.
        
        Returns:
            true if parameter is selected, false if it is not
        
        
        """
        ...
    def removeObserver(self, observer: 'ParameterObserver') -> None:
        """
        Remove an observer.
        
        Parameters:
            observer (ParameterObserver): observer to remove
        
        Since:
            9.1
        
        
        """
        ...
    def replaceObserver(self, oldObserver: 'ParameterObserver', newObserver: 'ParameterObserver') -> None:
        """
        Replace an observer.
        
        Parameters:
            oldObserver (ParameterObserver): observer to replace
            newObserver (ParameterObserver): new observer to use
        
        Since:
            10.1
        
        
        """
        ...
    def setContinuousEstimation(self, continuous: bool) -> None:
        """
        Set parameter estimation to continuous, by default step estimation.
        
        Continuous estimation : when a value wants to be known at date t, the value returned will be an interpolation between start value of the span corresponding to date t and end value (which corresponds to the start of the next span).
        
        Step estimation : when a value wants to be known at date t, the value returned will be the value of the beginning of span corresponding to date t, step estimation.
        
        Parameters:
            continuous (boolean): if true the parameter will be estimated with continuous estimation, if false with step estimation.
        
        
        """
        ...
    def setMaxValue(self, maxValue: float) -> None:
        """
        Set maximum parameter value.
        
        Parameters:
            maxValue (double): the maximum value to set.
        
        Since:
            9.3
        
        
        """
        ...
    def setMinValue(self, minValue: float) -> None:
        """
        Set minimum parameter value.
        
        Parameters:
            minValue (double): the minimum value to set.
        
        Since:
            9.3
        
        
        """
        ...
    def setName(self, name: str) -> None:
        """
        Change the general name of this parameter driver.
        
        Parameters:
            name (String): new name
        
        
        """
        ...
    @typing.overload
    def setNormalizedValue(self, double: float) -> None:
        """
        Set normalized value at specific date.
        
        The normalized value is a non-dimensional value suitable for use as part of a vector in an optimization process. It is computed as (current - reference)/scale.
        
        Parameters:
            date (double): date for which the normalized value wants to be set
            normalized (AbsoluteDate): value
        
        Set normalized value at specific date. Only useable on ParameterDriver which have only 1 span on their TimeSpanMap value (that is to say for which the setPeriod method wasn't called) otherwise it will throw an exception.
        
        The normalized value is a non-dimensional value suitable for use as part of a vector in an optimization process. It is computed as (current - reference)/scale.
        
        Parameters:
            normalized (double): value
        
        
        """
        ...
    @typing.overload
    def setNormalizedValue(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setReferenceDate(self, newReferenceDate: org.orekit.time.AbsoluteDate) -> None:
        """
        Set reference date.
        
        Parameters:
            newReferenceDate (AbsoluteDate): new reference date
        
        Since:
            9.0
        
        
        """
        ...
    def setReferenceValue(self, referenceValue: float) -> None:
        """
        Set reference parameter value.
        
        Parameters:
            referenceValue (double): the reference value to set.
        
        Since:
            9.3
        
        
        """
        ...
    def setScale(self, scale: float) -> None:
        """
        Set scale.
        
        Parameters:
            scale (double): the scale to set.
        
        Since:
            9.3
        
        
        """
        ...
    def setSelected(self, selected: bool) -> None:
        """
        Configure a parameter selection status.
        
        Selection is used for estimated parameters in orbit determination, or to compute the Jacobian matrix in partial derivatives computation.
        
        Parameters:
            selected (boolean): if true the parameter is selected, otherwise it will be fixed
        
        
        """
        ...
    @typing.overload
    def setValue(self, double: float) -> None:
        """
        Set parameter value at specific date.
        
        If newValue is below getMinValue, it will be silently set to getMinValue. If newValue is above getMaxValue, it will be silently set to getMaxValue.
        
        Parameters:
            date (double): date for which the value wants to be set. Only if parameter driver has 1 value estimated over the all orbit
                determination period (not validity period intervals for estimation), the date value can be null
            newValue (AbsoluteDate): new value to set
        
        Set parameter value. Only usable on ParameterDriver which have only 1 span on their TimeSpanMap value (that is to say for which the setPeriod method wasn't called)
        
        If newValue is below getMinValue, it will be silently set to getMinValue. If newValue is above getMaxValue, it will be silently set to getMaxValue.
        
        Parameters:
            newValue (double): new value to set
        
        
        """
        ...
    @typing.overload
    def setValue(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def setValueSpanMap(self, driver: 'ParameterDriver') -> None:
        """
        Set current parameter value span map to match another driver. In order to keep consistency, the validity period and name span map are updated.
        
        Parameters:
            driver (ParameterDriver): for which the value span map wants to be copied for the current driver
        
        Since:
            12.0
        
        
        """
        ...
    def toString(self) -> str:
        """
        Get a text representation of the parameter.
        
        Overrides: Object in class Object
        
        Returns:
            text representation of the parameter, in the form name = value.
        
        
        """
        ...

class ParameterDriversProvider:
    """
    Provider for ParameterDriver.
    
    Since:
        11.2
    """
    @staticmethod
    def findByName(driversList: java.util.List[ParameterDriver], name: str) -> bool:
        """
        Find if a parameter driver with a given name already exists in a list of parameter drivers.
        
        Parameters:
            driversList (List<ParameterDriver> driversList): the list of parameter drivers
            name (String): the parameter driver's name to filter with
        
        Returns:
            true if the name was found, false otherwise
        
        Since:
            13.0
        
        
        """
        ...
    def getNbParametersDriversValue(self) -> int:
        """
        Get total number of spans for all the parameters driver.
        
        Returns:
            total number of span to be estimated
        
        Since:
            12.0
        
        
        """
        ...
    def getParameterDriver(self, name: str) -> ParameterDriver:
        """
        Get parameter value from its name.
        
        Parameters:
            name (String): parameter name
        
        Returns:
            parameter value
        
        Since:
            8.0
        
        
        """
        ...
    _getParameters_2__T = typing.TypeVar('_getParameters_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getParameters_3__T = typing.TypeVar('_getParameters_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.MutableSequence[float]:
        """
        Get model parameters.
        
        Returns:
            model parameters, will throw an exception if one PDriver has several values driven. If it's the case (if at least 1
            PDriver of the model has several values driven) the method
            getParameters must be used.
        
        Since:
            12.0
        
        """
        ...
    @typing.overload
    def getParameters(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Get model parameters.
        
        Parameters:
            date (AbsoluteDate): date at which the parameters want to be known, can be new AbsoluteDate() if all the parameters have no validity period
                that is to say that they have only 1 estimated value over the all interval
        
        Returns:
            model parameters
        
        Since:
            12.0
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_2__T]) -> typing.MutableSequence[_getParameters_2__T]:
        """
        Get model parameters.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
        
        Returns:
            model parameters, will throw an exception if one PDriver of the has several values driven. If it's the case (if at least
            1 PDriver of the model has several values driven) the method
            getParameters must be used.
        
        Since:
            9.0
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_3__T], date: org.orekit.time.FieldAbsoluteDate[_getParameters_3__T]) -> typing.MutableSequence[_getParameters_3__T]:
        """
        Get model parameters.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            date (FieldAbsoluteDate<T> date): field date at which the parameters want to be known, can be new AbsoluteDate() if all the parameters have no validity
                period.
        
        Returns:
            model parameters
        
        Since:
            9.0
        
        
        """
        ...
    _getParametersAllValues_1__T = typing.TypeVar('_getParametersAllValues_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParametersAllValues(self) -> typing.MutableSequence[float]:
        """
        Get model parameters, return a list a all span values of all parameters.
        
        Returns:
            model parameters
        
        Since:
            12.0
        
        """
        ...
    @typing.overload
    def getParametersAllValues(self, field: org.hipparchus.Field[_getParametersAllValues_1__T]) -> typing.MutableSequence[_getParametersAllValues_1__T]:
        """
        Get model parameters.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
        
        Returns:
            model parameters
        
        Since:
            9.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def isSupported(self, name: str) -> bool:
        """
        Check if a parameter is supported.
        
        Supported parameters are those listed by getParametersDrivers.
        
        Parameters:
            name (String): parameter name to check
        
        Returns:
            true if the parameter is supported
        
        Since:
            8.0
        
        Also see:
            getParametersDrivers
        
        
        """
        ...

class ParameterFunction:
    """
    Interface representing a scalar function depending on a ParameterDriver.
    
    Since:
        8.0
    
    Also see:
        differentiate
    """
    def value(self, parameterDriver: ParameterDriver, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Evaluate the function.
        
        Parameters:
            parameterDriver (ParameterDriver): driver for the parameter.
            date (AbsoluteDate): date at which the function wants to be known
        
        Returns:
            scalar value of the function
        
        
        """
        ...

class ParameterObserver:
    """
    Interface for observing parameters changes.
    
    Since:
        8.0
    
    Also see:
        ParameterDriver
    """
    def estimationTypeChanged(self, previousIsContinuous: bool, driver: ParameterDriver) -> None:
        """
        Notify that a parameter estimation type (continuous or step) has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousIsContinuous (boolean): previous estimation type, continuous estimation if true, step estimation if not.
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def maxValueChanged(self, previousMaxValue: float, driver: ParameterDriver) -> None:
        """
        Notify that a parameter maximum value has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousMaxValue (double): previous maximum value
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def minValueChanged(self, previousMinValue: float, driver: ParameterDriver) -> None:
        """
        Notify that a parameter minimum value has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousMinValue (double): previous minimum value
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def nameChanged(self, previousName: str, driver: ParameterDriver) -> None:
        """
        Notify that a parameter name has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousName (String): previous name
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def referenceDateChanged(self, previousReferenceDate: org.orekit.time.AbsoluteDate, driver: ParameterDriver) -> None:
        """
        Notify that a parameter reference date has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousReferenceDate (AbsoluteDate): previous date (null if it is the first time the reference date is changed)
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def referenceValueChanged(self, previousReferenceValue: float, driver: ParameterDriver) -> None:
        """
        Notify that a parameter reference value has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousReferenceValue (double): previous reference value
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def scaleChanged(self, previousScale: float, driver: ParameterDriver) -> None:
        """
        Notify that a parameter scale has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousScale (double): previous scale
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def selectionChanged(self, previousSelection: bool, driver: ParameterDriver) -> None:
        """
        Notify that a parameter selection status has been changed.
        
        The default implementation does nothing
        
        Parameters:
            previousSelection (boolean): previous selection
            driver (ParameterDriver): parameter driver that has been changed
        
        Since:
            9.0
        
        
        """
        ...
    def valueChanged(self, previousValue: float, driver: ParameterDriver, date: org.orekit.time.AbsoluteDate) -> None:
        """
        Notify that a parameter value has been changed.
        
        Parameters:
            previousValue (double): previous value
            driver (ParameterDriver): parameter driver that has been changed
            date (AbsoluteDate): date for which the parameter value have been updated
        
        
        """
        ...
    def valueSpanMapChanged(self, previousValueSpanMap: 'TimeSpanMap'[float], driver: ParameterDriver) -> None:
        """
        Notify that a parameter value span map has been changed.
        
        Parameters:
            previousValueSpanMap (TimeSpanMap<Double> previousValueSpanMap): previous value
            driver (ParameterDriver): parameter driver that has been changed
        
        
        """
        ...

class SecularAndHarmonic:
    """
    Class for fitting evolution of osculating orbital parameters.
    
    This class allows conversion from osculating parameters to mean parameters.
    """
    def __init__(self, secularDegree: int, *pulsations: float):
        """
        Simple constructor.
        
        Parameters:
            secularDegree (int): degree of polynomial secular part
            pulsations (double...): pulsations of harmonic part
        
        
        """
        ...
    def addPoint(self, date: org.orekit.time.AbsoluteDate, osculatingValue: float) -> None:
        """
        Add a fitting point.
        
        The point weight is set to 1.0
        
        Parameters:
            date (AbsoluteDate): date of the point
            osculatingValue (double): osculating value
        
        Also see:
            addWeightedPoint
        
        
        """
        ...
    def addWeightedPoint(self, date: org.orekit.time.AbsoluteDate, osculatingValue: float, weight: float) -> None:
        """
        Add a weighted fitting point.
        
        Parameters:
            date (AbsoluteDate): date of the point
            osculatingValue (double): osculating value
            weight (double): weight of the points
        
        Since:
            12.0
        
        
        """
        ...
    def approximateAsPolynomialOnly(self, combinedDegree: int, combinedReference: org.orekit.time.AbsoluteDate, meanDegree: int, meanHarmonics: int, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate, step: float) -> typing.MutableSequence[float]:
        """
        Approximate an already fitted model to polynomial only terms.
        
        This method is mainly used in order to combine the large amplitude long periods with the secular part as a new approximate polynomial model over some time range. This should be used rather than simply extracting the polynomial coefficients from getFittedParameters when some periodic terms amplitudes are large (for example Sun resonance effects on local solar time in sun synchronous orbits). In theses cases, the pure polynomial secular part in the coefficients may be far from the mean model.
        
        Parameters:
            combinedDegree (int): desired degree for the combined polynomial
            combinedReference (AbsoluteDate): desired reference date for the combined polynomial
            meanDegree (int): degree of polynomial secular part to consider
            meanHarmonics (int): number of harmonics terms to consider
            start (AbsoluteDate): start date of the approximation time range
            end (AbsoluteDate): end date of the approximation time range
            step (double): sampling step
        
        Returns:
            coefficients of the approximate polynomial (in increasing degree order), using the user provided reference date
        
        
        """
        ...
    def fit(self) -> None:
        """
        Fit parameters.
        
        Also see:
            getFittedParameters
        
        
        """
        ...
    def getFittedParameters(self) -> typing.MutableSequence[float]:
        """
        Get a copy of the last fitted parameters.
        
        Returns:
            copy of the last fitted parameters.
        
        Also see:
            fit
        
        
        """
        ...
    def getHarmonicAmplitude(self) -> float:
        """
        Get an upper bound of the fitted harmonic amplitude.
        
        Returns:
            upper bound of the fitted harmonic amplitude
        
        
        """
        ...
    def getPulsations(self) -> typing.MutableSequence[float]:
        """
        Get the pulsations of harmonic part.
        
        Returns:
            pulsations of harmonic part
        
        Since:
            12.0
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference date.
        
        Returns:
            reference date
        
        Also see:
            resetFitting
        
        
        """
        ...
    def getSecularDegree(self) -> int:
        """
        Get degree of polynomial secular part.
        
        Returns:
            degree of polynomial secular part
        
        Since:
            12.0
        
        
        """
        ...
    def meanDerivative(self, date: org.orekit.time.AbsoluteDate, degree: int, harmonics: int) -> float:
        """
        Get mean derivative, truncated to first components.
        
        Parameters:
            date (AbsoluteDate): current date
            degree (int): degree of polynomial secular part to consider
            harmonics (int): number of harmonics terms to consider
        
        Returns:
            mean derivative at current date
        
        
        """
        ...
    def meanSecondDerivative(self, date: org.orekit.time.AbsoluteDate, degree: int, harmonics: int) -> float:
        """
        Get mean second derivative, truncated to first components.
        
        Parameters:
            date (AbsoluteDate): current date
            degree (int): degree of polynomial secular part
            harmonics (int): number of harmonics terms to consider
        
        Returns:
            mean second derivative at current date
        
        
        """
        ...
    def meanValue(self, date: org.orekit.time.AbsoluteDate, degree: int, harmonics: int) -> float:
        """
        Get mean value, truncated to first components.
        
        Parameters:
            date (AbsoluteDate): current date
            degree (int): degree of polynomial secular part to consider
            harmonics (int): number of harmonics terms to consider
        
        Returns:
            mean value at current date
        
        
        """
        ...
    def osculatingDerivative(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get fitted osculating derivative.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            osculating derivative at current date
        
        
        """
        ...
    def osculatingSecondDerivative(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get fitted osculating second derivative.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            osculating second derivative at current date
        
        
        """
        ...
    def osculatingValue(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get fitted osculating value.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            osculating value at current date
        
        
        """
        ...
    def resetFitting(self, date: org.orekit.time.AbsoluteDate, *initialGuess: float) -> None:
        """
        Reset fitting.
        
        Parameters:
            date (AbsoluteDate): reference date
            initialGuess (double...): initial guess for the parameters
        
        Also see:
            getReferenceDate
        
        
        """
        ...
    def setConvergenceRMS(self, convergenceRMS: float) -> None:
        """
        Set RMS for convergence.
        
        The RMS is the square-root of the sum of squared of the residuals, divided by the number of measurements.
        
        Parameters:
            convergenceRMS (double): RMS below which convergence is considered to have been reached
        
        Since:
            10.3
        
        
        """
        ...
    def setMaxIter(self, maxIter: int) -> None:
        """
        Set maximum number of iterations.
        
        Parameters:
            maxIter (int): maximum number of iterations
        
        Since:
            10.3
        
        
        """
        ...

class SortedListTrimmer:
    """
    A trimmer for externally stored chronologically sorted lists.
    
    Since:
        12.1
    """
    def __init__(self, neighborsSize: int):
        """
        Create a new trimmer with the given neighbors size.
        
        Parameters:
            neighborsSize (int): size of the list returned from getNeighborsSubList
        
        
        """
        ...
    def getNeighborsSize(self) -> int:
        """
        Get size of the list returned from getNeighborsSubList.
        
        Returns:
            size of the list returned from getNeighborsSubList
        
        
        """
        ...
    _getNeighborsSubList__T = typing.TypeVar('_getNeighborsSubList__T', bound=org.orekit.time.TimeStamped)  # <T>
    def getNeighborsSubList(self, central: org.orekit.time.AbsoluteDate, data: java.util.List[_getNeighborsSubList__T]) -> java.util.List[_getNeighborsSubList__T]:
        """
        Get the entries surrounding a central date.
        
        If the central date is well within covered range, the returned array will be balanced with half the points before central date and half the points after it (depending on n parity, of course). If the central date is near the boundary, then the returned array will be unbalanced and will contain only the n earliest (or latest) entries. A typical example of the later case is leap seconds cache, since the number of leap seconds cannot be arbitrarily increased.
        
        Parameters:
            central (AbsoluteDate): central date
            data (List<T> data): complete list of entries (must be chronologically sorted)
        
        Returns:
            entries surrounding the specified date (sublist of data)
        
        
        """
        ...

class StateFunction:
    """
    Interface representing a vector function depending on SpacecraftState.
    
    Since:
        8.0
    
    Also see:
        differentiate, StateJacobian
    """
    def value(self, state: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]:
        """
        Evaluate the function.
        
        Parameters:
            state (SpacecraftState): spacecraft state as the sole free parameter of the function.
        
        Returns:
            vector value of the function
        
        
        """
        ...

class StateJacobian:
    """
    Interface representing the Jacobian of a vector function depending on SpacecraftState.
    
    Since:
        8.0
    
    Also see:
        differentiate, StateFunction
    """
    def value(self, state: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Evaluate the Jacobian of the function.
        
        Parameters:
            state (SpacecraftState): spacecraft state as the sole free parameter of the function.
        
        Returns:
            Jacobian matrix
        
        
        """
        ...

_TimeSpanMap__Span__S = typing.TypeVar('_TimeSpanMap__Span__S')  # <S>
_TimeSpanMap__Transition__S = typing.TypeVar('_TimeSpanMap__Transition__S')  # <S>
_TimeSpanMap__T = typing.TypeVar('_TimeSpanMap__T')  # <T>
class TimeSpanMap(typing.Generic[_TimeSpanMap__T]):
    """
    Container for objects that apply to spans of time.
    
    Time span maps can be seen either as an ordered collection of Span or as an ordered collection of Transition. Both views are dual one to each other. A time span extends from one transition to the next one, and a transition separates one time span from the next one. Each time span contains one entry that is valid during the time span; this entry may be null if nothing is valid during this time span.
    
    Typical uses of TimeSpanMap are to hold piecewise data, like for example an orbit count that changes at ascending nodes (in which case the entry would be an Integer), or a visibility status between several objects (in which case the entry would be a Boolean), or a drag coefficient that is expected to be estimated daily or three-hourly.
    
    Time span maps are built progressively. At first, they contain one Span only whose validity extends from past infinity to future infinity. Then new entries are added one at a time, associated with transition dates, in order to build up the complete map. The transition dates can be either the start of validity (when calling addValidAfter), or the end of the validity (when calling addValidBefore). Entries are often added at one end only (and mainly in chronological order), but this is not required. It is possible for example to first set up a map that covers a large range (say one day), and then to insert intermediate dates using for example propagation and event detectors to carve out some parts. This is akin to the way Binary Space Partitioning Trees work.
    
    Since 11.1, this class is thread-safe
    
    Since:
        7.1
    """
    def __init__(self, entry: _TimeSpanMap__T):
        """
        Create a map containing a single object, initially valid throughout the timeline.
        
        The real validity of this first entry will be truncated as other entries are either addValidBefore it or addValidAfter it.
        
        The initial configureExpunge is to never expunge any entries, it can be changed afterward by calling configureExpunge
        
        Parameters:
            entry (TimeSpanMap): entry (initially valid throughout the timeline)
        
        
        """
        ...
    def addValidAfter(self, entry: _TimeSpanMap__T, earliestValidityDate: org.orekit.time.AbsoluteDate, erasesLater: bool) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Add an entry valid after a limit date.
        
        As an entry is valid, it truncates or overrides the validity of the neighboring entries already present in the map.
        
        If the map already contains transitions that occur later than earliestValidityDate, the erasesLater parameter controls what to do with them. Let's consider the time span [tₖ; tₖ₊₁[ associated with entry eₖ that would have been valid at time earliestValidityDate prior to the call to the method (i.e. tₖ < earliestValidityDate < tₖ₊₁).
        
          - if erasesLater is true, then all later transitions from and including tₖ₊₁ are erased, and the
            entry will be valid from earliestValidityDate to future infinity
          - if erasesLater is false, then all later transitions are preserved, and the entry will be valid
            from earliestValidityDate to tₖ₊₁
        
        In both cases, the existing entry eₖ time span will be truncated and will be valid only from tₖ to earliestValidityDate.
        
        Parameters:
            entry (TimeSpanMap): entry to add
            earliestValidityDate (AbsoluteDate): date after which the entry is valid
            erasesLater (boolean): if true, the entry erases all existing transitions that are later than earliestValidityDate
        
        Returns:
            span with added entry
        
        Since:
            11.1
        
        
        """
        ...
    def addValidBefore(self, entry: _TimeSpanMap__T, latestValidityDate: org.orekit.time.AbsoluteDate, erasesEarlier: bool) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Add an entry valid before a limit date.
        
        As an entry is valid, it truncates or overrides the validity of the neighboring entries already present in the map.
        
        If the map already contains transitions that occur earlier than latestValidityDate, the erasesEarlier parameter controls what to do with them. Let's consider the time span [tₖ; tₖ₊₁[ associated with entry eₖ that would have been valid at time latestValidityDate prior to the call to the method (i.e. tₖ < latestValidityDate < tₖ₊₁).
        
          - if erasesEarlier is true, then all earlier transitions up to and including tₖ are erased, and the
            entry will be valid from past infinity to latestValidityDate
          - if erasesEarlier is false, then all earlier transitions are preserved, and the entry will be
            valid from tₖ to latestValidityDate
        
        In both cases, the existing entry eₖ time span will be truncated and will be valid only from latestValidityDate to tₖ₊₁.
        
        Parameters:
            entry (TimeSpanMap): entry to add
            latestValidityDate (AbsoluteDate): date before which the entry is valid
            erasesEarlier (boolean): if true, the entry erases all existing transitions that are earlier than latestValidityDate
        
        Returns:
            span with added entry
        
        Since:
            11.1
        
        
        """
        ...
    def addValidBetween(self, entry: _TimeSpanMap__T, earliestValidityDate: org.orekit.time.AbsoluteDate, latestValidityDate: org.orekit.time.AbsoluteDate) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Add an entry valid between two limit dates.
        
        As an entry is valid, it truncates or overrides the validity of the neighboring entries already present in the map.
        
        Parameters:
            entry (TimeSpanMap): entry to add
            earliestValidityDate (AbsoluteDate): date after which the entry is valid
            latestValidityDate (AbsoluteDate): date before which the entry is valid
        
        Returns:
            span with added entry
        
        Since:
            11.1
        
        
        """
        ...
    def configureExpunge(self, newMaxNbSpans: int, newMaxRange: float, newExpungePolicy: ExpungePolicy) -> None:
        """
        Configure (or reconfigure) expunge policy for later additions.
        
        When an entry is added to the map (using either addValidBefore, addValidBetween, or addValidAfter that exceeds the allowed capacity in terms of number of time spans or maximum time range between the earliest and the latest transitions, then exceeding data is expunged according to the expungePolicy.
        
        Note that as the policy depends on the date at which new entries are added, the policy will be enforced only for the next calls to addValidBefore, addValidBetween, and addValidAfter, it is not enforce immediately.
        
        Parameters:
            newMaxNbSpans (int): maximum number of time spans
            newMaxRange (double): maximum time range between the earliest and the latest transitions
            newExpungePolicy (ExpungePolicy): expunge policy to apply when capacity is exceeded
        
        Since:
            13.1
        
        
        """
        ...
    def extractRange(self, start: org.orekit.time.AbsoluteDate, end: org.orekit.time.AbsoluteDate) -> 'TimeSpanMap'[_TimeSpanMap__T]:
        """
        Extract a range of the map.
        
        The object returned will be a new independent instance that will contain only the transitions that lie in the specified range.
        
        Consider, for example, a map containing objects O₀ valid before t₁, O₁ valid between t₁ and t₂, O₂ valid between t₂ and t₃, O₃ valid between t₃ and t₄, and O₄ valid after t₄. then calling this method with a start date between t₁ and t₂ and a end date between t₃ and t₄ will result in a new map containing objects O₁ valid before t₂, O₂ valid between t₂ and t₃, and O₃ valid after t₃. The validity of O₁ is therefore extended in the past, and the validity of O₃ is extended in the future.
        
        Parameters:
            start (AbsoluteDate): earliest date at which a transition is included in the range (may be set to
                PAST_INFINITY to keep all early transitions)
            end (AbsoluteDate): latest date at which a transition is included in the r (may be set to
                FUTURE_INFINITY to keep all late transitions)
        
        Returns:
            a new instance with all transitions restricted to the specified range
        
        Since:
            9.2
        
        
        """
        ...
    def forEach(self, action: typing.Union[java.util.function.Consumer[_TimeSpanMap__T], typing.Callable[[_TimeSpanMap__T], None]]) -> None:
        """
        Performs an action for each non-null element of the map.
        
        The action is performed chronologically.
        
        Parameters:
            action (Consumer<TimeSpanMap> action): action to perform on the non-null elements
        
        Since:
            10.3
        
        
        """
        ...
    def get(self, date: org.orekit.time.AbsoluteDate) -> _TimeSpanMap__T:
        """
        Get the entry valid at a specified date.
        
        The expected complexity is O(1) for successive calls with neighboring dates, which is the more frequent use in propagation or orbit determination applications, and O(n) for random calls.
        
        Parameters:
            date (AbsoluteDate): date at which the entry must be valid
        
        Returns:
            valid entry at specified date
        
        Also see:
            getSpan
        
        
        """
        ...
    def getFirstNonNullSpan(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Get the first (earliest) span with non-null data.
        
        Returns:
            first (earliest) span with non-null data
        
        Since:
            12.1
        
        
        """
        ...
    def getFirstSpan(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Get the first (earliest) span.
        
        Returns:
            first (earliest) span
        
        Since:
            11.1
        
        
        """
        ...
    def getFirstTransition(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__T]:
        """
        Get the first (earliest) transition.
        
        Returns:
            first (earliest) transition, or null if there are no transitions
        
        Since:
            11.1
        
        
        """
        ...
    def getLastNonNullSpan(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Get the last (latest) span with non-null data.
        
        Returns:
            last (latest) span with non-null data
        
        Since:
            12.1
        
        
        """
        ...
    def getLastSpan(self) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Get the last (latest) span.
        
        Returns:
            last (latest) span
        
        Since:
            11.1
        
        
        """
        ...
    def getLastTransition(self) -> 'TimeSpanMap.Transition'[_TimeSpanMap__T]:
        """
        Get the last (latest) transition.
        
        Returns:
            last (latest) transition, or null if there are no transitions
        
        Since:
            11.1
        
        
        """
        ...
    def getSpan(self, date: org.orekit.time.AbsoluteDate) -> 'TimeSpanMap.Span'[_TimeSpanMap__T]:
        """
        Get the time span containing a specified date.
        
        The expected complexity is O(1) for successive calls with neighboring dates, which is the more frequent use in propagation or orbit determination applications, and O(n) for random calls.
        
        Parameters:
            date (AbsoluteDate): date belonging to the desired time span
        
        Returns:
            time span containing the specified date
        
        Since:
            9.3
        
        
        """
        ...
    def getSpansNumber(self) -> int:
        """
        Get the number of spans.
        
        The number of spans is always at least 1. The number of transitions is always 1 lower than the number of spans.
        
        Returns:
            number of spans
        
        Since:
            11.1
        
        
        """
        ...
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
        def resetDate(self, absoluteDate: org.orekit.time.AbsoluteDate, boolean: bool) -> None: ...

class TimeStampedAngularCoordinatesHermiteInterpolator(org.orekit.time.AbstractTimeInterpolator['TimeStampedAngularCoordinates']):
    """
    Class using Hermite interpolator to interpolate time stamped angular coordinates.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
        class:`~org.orekit.utils.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, TimeStampedAngularCoordinates
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float, angularDerivativesFilter: AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, angularDerivativesFilter: AngularDerivativesFilter): ...
    def getFilter(self) -> AngularDerivativesFilter:
        """
        Get filter for derivatives from the sample to use in interpolation.
        
        Returns:
            filter for derivatives from the sample to use in interpolation
        
        
        """
        ...

_TimeStampedCache__T = typing.TypeVar('_TimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class TimeStampedCache(typing.Generic[_TimeStampedCache__T]):
    """
    Interface for a data structure that can provide concurrent access to TimeStamped data surrounding a given date.
    
    Also see:
        GenericTimeStampedCache, ImmutableTimeStampedCache
    """
    def getEarliest(self) -> _TimeStampedCache__T:
        """
        Get the earliest entry in this cache.
        
        Returns:
            earliest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getLatest(self) -> _TimeStampedCache__T:
        """
        Get the latest entry in this cache.
        
        Returns:
            latest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getMaxNeighborsSize(self) -> int:
        """
        Get the maximum size of the lists returned by getNeighbors.
        
        Returns:
            size of the list
        
        
        """
        ...
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int) -> java.util.stream.Stream[_TimeStampedCache__T]: ...
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_TimeStampedCache__T]: ...

_TimeStampedFieldAngularCoordinatesHermiteInterpolator__KK = typing.TypeVar('_TimeStampedFieldAngularCoordinatesHermiteInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class TimeStampedFieldAngularCoordinatesHermiteInterpolator(org.orekit.time.AbstractFieldTimeInterpolator['TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinatesHermiteInterpolator__KK], _TimeStampedFieldAngularCoordinatesHermiteInterpolator__KK], typing.Generic[_TimeStampedFieldAngularCoordinatesHermiteInterpolator__KK]):
    """
    Class using Hermite interpolator to interpolate time stamped angular coordinates.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
        class:`~org.orekit.utils.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.FieldHermiteInterpolator?is`, TimeStampedFieldAngularCoordinates
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float, angularDerivativesFilter: AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, angularDerivativesFilter: AngularDerivativesFilter): ...
    def getFilter(self) -> AngularDerivativesFilter:
        """
        Get filter for derivatives from the sample to use in interpolation.
        
        Returns:
            filter for derivatives from the sample to use in interpolation
        
        
        """
        ...

_TimeStampedFieldPVCoordinatesHermiteInterpolator__KK = typing.TypeVar('_TimeStampedFieldPVCoordinatesHermiteInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class TimeStampedFieldPVCoordinatesHermiteInterpolator(org.orekit.time.AbstractFieldTimeInterpolator['TimeStampedFieldPVCoordinates'[_TimeStampedFieldPVCoordinatesHermiteInterpolator__KK], _TimeStampedFieldPVCoordinatesHermiteInterpolator__KK], typing.Generic[_TimeStampedFieldPVCoordinatesHermiteInterpolator__KK]):
    """
    Class using a Hermite interpolator to interpolate time stamped position-velocity-acceleration coordinates.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
        class:`~org.orekit.utils.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.FieldHermiteInterpolator?is`, TimeStampedFieldPVCoordinates
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float, cartesianDerivativesFilter: CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, cartesianDerivativesFilter: CartesianDerivativesFilter): ...
    def getFilter(self) -> CartesianDerivativesFilter:
        """
        filter for derivatives from the sample to use in interpolation.
        
        Returns:
            filter for derivatives from the sample to use in interpolation
        
        
        """
        ...

_TimeStampedGenerator__T = typing.TypeVar('_TimeStampedGenerator__T', bound=org.orekit.time.TimeStamped)  # <T>
class TimeStampedGenerator(typing.Generic[_TimeStampedGenerator__T]):
    """
    Generator to use for creating entries in GenericTimeStampedCache.
    
    As long as a generator is referenced by one GenericTimeStampedCache only, it is guaranteed to be called in a thread-safe way, even if the cache is used in a multi-threaded environment. The cache takes care of scheduling the calls to all the methods defined in this interface so only one thread uses them at any time. There is no need for the implementing classes to handle synchronization or locks by themselves.
    
    The generator is provided by the user of the GenericTimeStampedCache and should be consistent with the way he will use the cached data.
    
    If entries must have regular time gaps (for example one entry every 3600 seconds), then the generator must ensure by itself all generated entries are exactly located on the expected regular grid, even if they are generated in random order. The reason for that is that the cache may ask for entries in different ranges and merge these ranges afterwards. A typical example would be a cache first calling the generator for 6 points around 2012-02-19T17:48:00 and when these points are exhausted calling the generator again for 6 new points around 2012-02-19T23:20:00. If all points must be exactly 3600 seconds apart, the generator should generate the first 6 points at 2012-02-19T15:00:00, 2012-02-19T16:00:00, 2012-02-19T17:00:00, 2012-02-19T18:00:00, 2012-02-19T19:00:00 and 2012-02-19T20:00:00, and the next 6 points at 2012-02-19T21:00:00, 2012-02-19T22:00:00, 2012-02-19T23:00:00, 2012-02-20T00:00:00, 2012-02-20T01:00:00 and 2012-02-20T02:00:00. If the separation between the points is irrelevant, the first points could be generated at 17:48:00 instead of 17:00:00 or 18:00:00. The cache will merge arrays returned from different calls in the same global time slot.
    """
    def generate(self, existingDate: org.orekit.time.AbsoluteDate, date: org.orekit.time.AbsoluteDate) -> java.util.List[_TimeStampedGenerator__T]:
        """
        Generate a chronologically sorted list of entries to be cached.
        
        If existingDate is earlier than date, the range covered by generated entries must cover at least from existingDate (excluded) to date (included). If existingDate is later than date, the range covered by generated entries must cover at least from date (included) to existingDate (excluded).
        
        The generated entries may cover a range larger than the minimum specified above if the generator prefers to generate large chunks of data at once. It may generate again entries already generated by an earlier call (typically at existingDate), these extra entries will be silently ignored by the cache.
        
        Non-coverage of the minimum range may lead to a loss of data, as the gap will not be filled by the GenericTimeStampedCache in subsequent calls.
        
        The generated entries must be chronologically sorted.
        
        Parameters:
            existingDate (AbsoluteDate): date of the closest already existing entry (may be null)
            date (AbsoluteDate): date that must be covered by the range of the generated array
        
        Returns:
            chronologically sorted list of generated entries
        
        
        """
        ...

class TimeStampedPVCoordinatesHermiteInterpolator(org.orekit.time.AbstractTimeInterpolator['TimeStampedPVCoordinates']):
    """
    Class using a Hermite interpolator to interpolate time stamped position-velocity-acceleration coordinates.
    
    As this implementation of interpolation is polynomial, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
        class:`~org.orekit.utils.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, TimeStampedPVCoordinates
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float, cartesianDerivativesFilter: CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, cartesianDerivativesFilter: CartesianDerivativesFilter): ...
    def getFilter(self) -> CartesianDerivativesFilter:
        """
        Get filter for derivatives from the sample to use in interpolation.
        
        Returns:
            filter for derivatives from the sample to use in interpolation
        
        
        """
        ...

class TrackingCoordinates:
    """
    Container for azimut/elevation/range coordinates as seen from a ground point.
    
    Since:
        12.0
    
    Also see:
        TopocentricFrame
    """
    def __init__(self, azimuth: float, elevation: float, range: float):
        """
        Simple constructor.
        
        Parameters:
            azimuth (double): azimuth
            elevation (double): elevation
            range (double): range
        
        
        """
        ...
    def getAzimuth(self) -> float:
        """
        Get the azimuth.
        
        The azimuth is the angle between the North direction at local point and the projection in local horizontal plane of the direction from local point to given point. Azimuth angles are counted clockwise, i.e positive towards the East.
        
        Returns:
            azimuth
        
        
        """
        ...
    def getElevation(self) -> float:
        """
        Get the elevation.
        
        The elevation is the angle between the local horizontal and the direction from local point to given point.
        
        Returns:
            elevation
        
        
        """
        ...
    def getRange(self) -> float:
        """
        Get the range.
        
        Returns:
            range
        
        
        """
        ...

class WaypointPVBuilder:
    """
    Builder class, enabling incremental building of an PVCoordinatesProvider instance using waypoints defined on an ellipsoid.
    
    Given a series of waypoints ((date, point) tuples), build a PVCoordinatesProvider representing the path. The static methods provide implementations for the most common path definitions (cartesian, great-circle, loxodrome). If these methods are insufficient, the public constructor provides a way to customize the path definition.
    
    This class connects the path segments using the AggregatedPVCoordinatesProvider. As such, no effort is made to smooth the velocity between segments. While position is unaffected, the velocity may be discontinuous between adjacent time points. Thus, care should be taken when modeling paths with abrupt direction changes (e.g. fast-moving aircraft); understand how the PVCoordinatesProvider will be used in the particular application.
    
    Since:
        11.3
    """
    def __init__(self, factory: typing.Union['WaypointPVBuilder.InterpolationFactory', typing.Callable], body: org.orekit.bodies.OneAxisEllipsoid):
        """
        Create a new instance.
        
        Parameters:
            factory (InterpolationFactory): The factory used to create the intermediate coordinate providers between waypoints.
            body (OneAxisEllipsoid): The central body, on which the way points are defined.
        
        
        """
        ...
    def addWaypoint(self, point: org.orekit.bodies.GeodeticPoint, date: org.orekit.time.AbsoluteDate) -> 'WaypointPVBuilder':
        """
        Add a waypoint.
        
        Parameters:
            point (GeodeticPoint): the waypoint location
            date (AbsoluteDate): the waypoint time
        
        Returns:
            this instance
        
        
        """
        ...
    def build(self) -> PVCoordinatesProvider:
        """
        Build a PVCoordinatesProvider from the waypoints added to this builder.
        
        Returns:
            the coordinates provider instance.
        
        
        """
        ...
    @staticmethod
    def cartesianBuilder(body: org.orekit.bodies.OneAxisEllipsoid) -> 'WaypointPVBuilder':
        """
        Construct a waypoint builder interpolating points using a linear cartesian interpolation.
        
        Parameters:
            body (OneAxisEllipsoid): the reference ellipsoid on which the waypoints are defined.
        
        Returns:
            the waypoint builder
        
        
        """
        ...
    def constantAfter(self) -> 'WaypointPVBuilder':
        """
        Indicate the resulting PVCoordinatesProvider provide a constant location of the last waypoint after to the last time.
        
        Returns:
            this instance
        
        
        """
        ...
    def constantBefore(self) -> 'WaypointPVBuilder':
        """
        Indicate the resulting PVCoordinatesProvider provide a constant location of the first waypoint prior to the first time.
        
        Returns:
            this instance
        
        
        """
        ...
    @staticmethod
    def greatCircleBuilder(body: org.orekit.bodies.OneAxisEllipsoid) -> 'WaypointPVBuilder':
        """
        Construct a waypoint builder interpolating points using a great-circle.
        
        The altitude of the intermediate points is linearly interpolated from the bounding waypoints. Extrapolating before the first waypoint or after the last waypoint may result in undefined altitudes.
        
        Parameters:
            body (OneAxisEllipsoid): the reference ellipsoid on which the waypoints are defined.
        
        Returns:
            the waypoint builder
        
        
        """
        ...
    def invalidAfter(self) -> 'WaypointPVBuilder':
        """
        Indicate the resulting PVCoordinatesProvider should be invalid after the last waypoint.
        
        Returns:
            this instance
        
        
        """
        ...
    def invalidBefore(self) -> 'WaypointPVBuilder':
        """
        Indicate the resulting PVCoordinatesProvider should be invalid before the first waypoint.
        
        Returns:
            this instance
        
        
        """
        ...
    @staticmethod
    def loxodromeBuilder(body: org.orekit.bodies.OneAxisEllipsoid) -> 'WaypointPVBuilder':
        """
        Construct a waypoint builder interpolating points using a loxodrome (or Rhumbline).
        
        Parameters:
            body (OneAxisEllipsoid): the reference ellipsoid on which the waypoints are defined.
        
        Returns:
            the waypoint builder
        
        
        """
        ...
    class InterpolationFactory:
        def create(self, absoluteDate: org.orekit.time.AbsoluteDate, geodeticPoint: org.orekit.bodies.GeodeticPoint, absoluteDate2: org.orekit.time.AbsoluteDate, geodeticPoint2: org.orekit.bodies.GeodeticPoint, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid) -> PVCoordinatesProvider: ...

class AbstractMultipleShooting(MultipleShooting):
    """
    Multiple shooting method using only constraints on state vectors of patch points (and possibly on epoch and integration time).
    
    Since:
        10.2
    
    Also see:
        "TRAJECTORY DESIGN AND ORBIT MAINTENANCE STRATEGIES IN MULTI-BODY DYNAMICAL REGIMES by Thomas A. Pavlak, Purdue
        University"
    """
    def addConstraint(self, patchIndex: int, componentIndex: int, constraintValue: float) -> None:
        """
        Add a constraint on one component of one patch point.
        
        Parameters:
            patchIndex (int): Patch point index (zero-based)
            componentIndex (int): Index of the component which is constrained (zero-based)
            constraintValue (double): constraint value
        
        
        """
        ...
    def compute(self) -> java.util.List[org.orekit.propagation.SpacecraftState]:
        """
        Return the list of corrected patch points. An optimizer is better suited for this problem
        
        Specified by: compute in interface MultipleShooting
        
        Returns:
            patchedSpacecraftStates
        
        
        """
        ...
    def setEpochFreedom(self, patchIndex: int, isFree: bool) -> None:
        """
        Set the epoch of a patch point to free or not.
        
        Parameters:
            patchIndex (int): Patch point index (zero-based)
            isFree (boolean): constraint value
        
        
        """
        ...
    def setPatchPointComponentFreedom(self, patchIndex: int, componentIndex: int, isFree: bool) -> None:
        """
        Set a component of a patch point to free or not.
        
        Parameters:
            patchIndex (int): Patch point index (zero-based)
            componentIndex (int): Index of the component to be constrained (zero-based)
            isFree (boolean): constraint value
        
        
        """
        ...
    def setScaleLength(self, scaleLength: float) -> None:
        """
        Set the scale length.
        
        Parameters:
            scaleLength (double): scale length in meters
        
        
        """
        ...
    def setScaleTime(self, scaleTime: float) -> None:
        """
        Set the scale time.
        
        Parameters:
            scaleTime (double): scale time in seconds
        
        
        """
        ...

class AccurateFormatter(Formatter):
    """
    Formatter used to produce strings from data with high accuracy.
    
    When producing test output from computed data, we want the shortest decimal representation of a floating point number that maintains round-trip safety. That is, a correct parser can recover the exact original number.
    
    For efficiency, this class uses the RyuDouble algorithm for producing shortest string representation with round-trip safety.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Public constructor.
        """
        ...
    @typing.overload
    @staticmethod
    def format(double: float) -> str: ...
    @typing.overload
    @staticmethod
    def format(int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, double: float) -> str:
        """
        Formats to full accuracy. Format a double number.
        
        Specified by: toString in interface Formatter
        
        Parameters:
            value (double): number to format
        
        Returns:
            number formatted.
        
        Formats the seconds variable with maximum precision needed. Format a date. Does not check if date time is real or if it will meet formating requirements.
        
        Specified by: toString in interface Formatter
        
        Parameters:
            year (int): of date to be formatted
            month (int): of date to be formatted
            day (int): of month to be formatted
            hour (int): to be formatted
            minute (int): to be formatted
            seconds (double): and sub-seconds to be formatted
        
        Returns:
            date formatted to match the following format [yyyy-MM-ddTHH:mm:ss.S#]
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str: ...

class AggregatedPVCoordinatesProvider(PVCoordinatesProvider):
    """
    Aggregate multiple PVCoordinatesProvider instances together.
    
    This can be used to describe an aircraft or surface vehicle.
    
    Since:
        11.3
    """
    @typing.overload
    def __init__(self, timeSpanMap: TimeSpanMap[typing.Union[PVCoordinatesProvider, typing.Callable]]): ...
    @typing.overload
    def __init__(self, timeSpanMap: TimeSpanMap[typing.Union[PVCoordinatesProvider, typing.Callable]], absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the first date of the range.
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
        Description copied from interface: getPVCoordinates Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from interface: getPosition Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    class Builder:
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, pVCoordinatesProvider: typing.Union[PVCoordinatesProvider, typing.Callable]): ...
        def addPVProviderAfter(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinatesProvider: typing.Union[PVCoordinatesProvider, typing.Callable], boolean: bool) -> 'AggregatedPVCoordinatesProvider.Builder': ...
        def addPVProviderBefore(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinatesProvider: typing.Union[PVCoordinatesProvider, typing.Callable], boolean: bool) -> 'AggregatedPVCoordinatesProvider.Builder': ...
        def build(self) -> 'AggregatedPVCoordinatesProvider': ...
        def invalidAfter(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'AggregatedPVCoordinatesProvider.Builder': ...
        def invalidBefore(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'AggregatedPVCoordinatesProvider.Builder': ...
    class InvalidPVProvider(PVCoordinatesProvider):
        def __init__(self): ...
        def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates': ...

class BoundedPVCoordinatesProvider(PVCoordinatesProvider):
    """
    Interface for bounded PV coordinates providers.
    
    Since:
        13.1
    
    Also see:
        PVCoordinatesProvider
    """
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the first date of the range.
        
        Returns:
            the first date of the range
        
        
        """
        ...
    @staticmethod
    def of(interval: typing.Union[PVCoordinatesProvider, typing.Callable], provider: org.orekit.time.TimeInterval) -> 'BoundedPVCoordinatesProvider':
        """
        Bound a given coordinates provider.
        
        Parameters:
            interval (PVCoordinatesProvider): time interval
            provider (TimeInterval): input provider
        
        Returns:
            bounded provider
        
        
        """
        ...

class ConstantPVCoordinatesProvider(PVCoordinatesProvider):
    """
    Provider based on a single point. When getPVCoordinates is called, the constant point will be translated to the destination frame and returned. This behavior is different than getPVCoordinates (which uses shiftedBy internally.). Use this class when no shifting should be performed (e.g. representing a fixed point on the ground).
    
    Since:
        11.3
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, pVCoordinates: PVCoordinates, frame: org.orekit.frames.Frame): ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
        Description copied from interface: getPVCoordinates Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from interface: getPosition Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class DateDriver(ParameterDriver, org.orekit.time.TimeStamped):
    """
    ParameterDriver allowing to drive a date.
    
    Since:
        11.1
    """
    def __init__(self, base: org.orekit.time.AbsoluteDate, name: str, start: bool):
        """
        Simple constructor.
        
        At construction, the parameter is configured as not selected, the reference date is set to null, the value (i.e. the date offset) is set to 0, the scale is set to 1 and the minimum and maximum values are set to negative and positive infinity respectively.
        
        Parameters:
            base (AbsoluteDate): base date corresponding to shift = 0
            name (String): name of the parameter
            start (boolean): if true, the driver corresponds to a start date
        
        
        """
        ...
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
        
        Specified by: getDate in interface TimeStamped
        
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

class ExtendedPositionProvider(PVCoordinatesProvider):
    """
    Interface for position providers (including for Field). Emulates position (and derivatives) vector as a function of time.
    
    Since:
        12.1
    """
    _getPVCoordinates_0__T = typing.TypeVar('_getPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_0__T], frame: org.orekit.frames.Frame) -> 'TimeStampedFieldPVCoordinates'[_getPVCoordinates_0__T]:
        """
        Get the position-velocity-acceleration in the selected frame.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position-velocity-acceleration vector
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    _getPosition_0__T = typing.TypeVar('_getPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_getPosition_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPosition_0__T]:
        """
        Get the position in the selected frame.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position
        
        
        """
        ...
    @typing.overload
    def getPosition(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def toExtendedPVCoordinatesProvider(self) -> 'ExtendedPVCoordinatesProvider':
        """
        Deprecated. since 13.0. Only there to help transition out. Method to convert as ExtendedPVCoordinatesProvider.
        
        Returns:
            converted object
        
        Since:
            13.0
        
        
        """
        ...
    _toFieldPVCoordinatesProvider__T = typing.TypeVar('_toFieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toFieldPVCoordinatesProvider(self, field: org.hipparchus.Field[_toFieldPVCoordinatesProvider__T]) -> FieldPVCoordinatesProvider[_toFieldPVCoordinatesProvider__T]:
        """
        Convert to a FieldPVCoordinatesProvider with a specific type.
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...

_FieldBoundedPVCoordinatesProvider__T = typing.TypeVar('_FieldBoundedPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBoundedPVCoordinatesProvider(FieldPVCoordinatesProvider[_FieldBoundedPVCoordinatesProvider__T], typing.Generic[_FieldBoundedPVCoordinatesProvider__T]):
    """
    Interface for bounded, Field PV coordinates providers.
    
    Since:
        13.1
    
    Also see:
        FieldPVCoordinatesProvider
    """
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldBoundedPVCoordinatesProvider__T]:
        """
        Get the last date of the range.
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldBoundedPVCoordinatesProvider__T]:
        """
        Get the first date of the range.
        
        Returns:
            the first date of the range
        
        
        """
        ...

_FieldShiftingPVCoordinatesProvider__T = typing.TypeVar('_FieldShiftingPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldShiftingPVCoordinatesProvider(FieldPVCoordinatesProvider[_FieldShiftingPVCoordinatesProvider__T], typing.Generic[_FieldShiftingPVCoordinatesProvider__T]):
    """
    Provider using simple shiftedBy shiftedBy} and frame transforms for evolution.
    
    Since:
        12.1
    """
    def __init__(self, referencePV: 'TimeStampedFieldPVCoordinates'[_FieldShiftingPVCoordinatesProvider__T], referenceFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            referencePV (TimeStampedFieldPVCoordinates<FieldShiftingPVCoordinatesProvider> referencePV): reference coordinates
            referenceFrame (Frame): frame in which reference is defined
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_FieldShiftingPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> 'TimeStampedFieldPVCoordinates'[_FieldShiftingPVCoordinatesProvider__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<FieldShiftingPVCoordinatesProvider> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_FieldShiftingPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldShiftingPVCoordinatesProvider__T]:
        """
        Description copied from interface: getPosition Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<FieldShiftingPVCoordinatesProvider> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...

_GenericTimeStampedCache__T = typing.TypeVar('_GenericTimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class GenericTimeStampedCache(TimeStampedCache[_GenericTimeStampedCache__T], typing.Generic[_GenericTimeStampedCache__T]):
    """
    Generic thread-safe cache for TimeStamped data.
    """
    DEFAULT_CACHED_SLOTS_NUMBER: typing.ClassVar[int] = ...
    """
    Default number of independent cached time slots.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, timeStampedGenerator: typing.Union[TimeStampedGenerator[_GenericTimeStampedCache__T], typing.Callable[[org.orekit.time.AbsoluteDate, org.orekit.time.AbsoluteDate], java.util.List[org.orekit.time.TimeStamped]]]): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float, double2: float, timeStampedGenerator: typing.Union[TimeStampedGenerator[_GenericTimeStampedCache__T], typing.Callable[[org.orekit.time.AbsoluteDate, org.orekit.time.AbsoluteDate], java.util.List[org.orekit.time.TimeStamped]]], double3: float): ...
    def getEarliest(self) -> _GenericTimeStampedCache__T:
        """
        Get the earliest entry in this cache.
        
        Specified by: getEarliest in interface TimeStampedCache
        
        Returns:
            earliest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
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
        
        This number of calls is related to the number of cache misses and may be used to tune the cache configuration. Each cache miss implies at least one call is performed, but may require several calls if the new date is far offset from the existing cache, depending on the number of elements and step between elements in the arrays returned by the generator.
        
        Returns:
            number of calls to the generate method
        
        Also see:
            getGetNeighborsCalls
        
        
        """
        ...
    def getGenerator(self) -> TimeStampedGenerator[_GenericTimeStampedCache__T]:
        """
        Get the generator.
        
        Returns:
            generator
        
        
        """
        ...
    def getGetNeighborsCalls(self) -> int:
        """
        Get the number of calls to the getNeighbors method.
        
        This number of calls is used as a reference to interpret getGenerateCalls.
        
        Returns:
            number of calls to the getNeighbors method
        
        Also see:
            getGenerateCalls
        
        
        """
        ...
    def getLatest(self) -> _GenericTimeStampedCache__T:
        """
        Get the latest entry in this cache.
        
        Specified by: getLatest in interface TimeStampedCache
        
        Returns:
            latest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getMaxNeighborsSize(self) -> int:
        """
        Get the maximum size of the lists returned by getNeighbors.
        
        Specified by: getMaxNeighborsSize in interface TimeStampedCache
        
        Returns:
            size of the list
        
        
        """
        ...
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
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_GenericTimeStampedCache__T]: ...
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int) -> java.util.stream.Stream[_GenericTimeStampedCache__T]: ...
    def getNewSlotQuantumGap(self) -> float:
        """
        Get quantum gap above which a new slot is created instead of extending an existing one.
        
        The quantum gap is the newSlotInterval value provided at construction rounded to the nearest quantum step used internally by the cache.
        
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
        
        This number should remain small when the max number of slots is sufficient with respect to the number of concurrent requests to the cache. If it increases too much, then the cache configuration is probably bad and cache does not really improve things (in this case, the getGenerateCalls will probably increase too.
        
        Returns:
            number of slots evictions
        
        
        """
        ...

_ImmutableFieldTimeStampedCache__T = typing.TypeVar('_ImmutableFieldTimeStampedCache__T', bound=org.orekit.time.FieldTimeStamped)  # <T>
_ImmutableFieldTimeStampedCache__KK = typing.TypeVar('_ImmutableFieldTimeStampedCache__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class ImmutableFieldTimeStampedCache(FieldTimeStampedCache[_ImmutableFieldTimeStampedCache__T, _ImmutableFieldTimeStampedCache__KK], typing.Generic[_ImmutableFieldTimeStampedCache__T, _ImmutableFieldTimeStampedCache__KK]):
    """
    A cache of TimeStamped data that provides concurrency through immutability. This strategy is suitable when all the cached data is stored in memory. (For example, UTCScale) This class then provides convenient methods for accessing the data.
    """
    def __init__(self, maxNeighborsSize: int, data: typing.Union[java.util.Collection[_ImmutableFieldTimeStampedCache__T], typing.Sequence[_ImmutableFieldTimeStampedCache__T], typing.Set[_ImmutableFieldTimeStampedCache__T]]):
        """
        Create a new cache with the given neighbors size and data.
        
        Parameters:
            maxNeighborsSize (int): the maximum size of the list returned from getNeighbors. Must be less
                than or equal to size().
            data (Collection<? extends ImmutableFieldTimeStampedCache> data): the backing data for this cache. The list will be copied to ensure immutability. To guarantee immutability the entries
                in data must be immutable themselves. There must be more data than maxNeighborsSize.
        
        Raises:
            IllegalArgumentException: if size() or if maxNeighborsSize is negative
        
        
        """
        ...
    _emptyCache__TS = typing.TypeVar('_emptyCache__TS', bound=org.orekit.time.FieldTimeStamped)  # <TS>
    _emptyCache__CFE = typing.TypeVar('_emptyCache__CFE', bound=org.hipparchus.CalculusFieldElement)  # <CFE>
    @staticmethod
    def emptyCache() -> 'ImmutableFieldTimeStampedCache'[_emptyCache__TS, _emptyCache__CFE]:
        """
        Get an empty immutable cache.
        
        Returns:
            an empty ImmutableTimeStampedCache.
        
        Since:
            12.1
        
        
        """
        ...
    def getAll(self) -> java.util.List[_ImmutableFieldTimeStampedCache__T]:
        """
        Get all the data in this cache.
        
        Returns:
            a sorted collection of all data passed in the .
        
        
        """
        ...
    def getEarliest(self) -> _ImmutableFieldTimeStampedCache__T:
        """
        Get the earliest entry in this cache.
        
        Specified by: getEarliest in interface FieldTimeStampedCache
        
        Returns:
            earliest cached entry
        
        
        """
        ...
    def getLatest(self) -> _ImmutableFieldTimeStampedCache__T:
        """
        Get the latest entry in this cache.
        
        Specified by: getLatest in interface FieldTimeStampedCache
        
        Returns:
            latest cached entry
        
        
        """
        ...
    def getMaxNeighborsSize(self) -> int:
        """
        Get the fixed size of the lists returned by getNeighbors.
        
        Specified by: getMaxNeighborsSize in interface FieldTimeStampedCache
        
        Returns:
            size of the list
        
        
        """
        ...
    @typing.overload
    def getNeighbors(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_ImmutableFieldTimeStampedCache__KK]) -> java.util.stream.Stream[_ImmutableFieldTimeStampedCache__T]: ...
    @typing.overload
    def getNeighbors(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_ImmutableFieldTimeStampedCache__KK], int: int) -> java.util.stream.Stream[_ImmutableFieldTimeStampedCache__T]: ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

_ImmutableTimeStampedCache__T = typing.TypeVar('_ImmutableTimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class ImmutableTimeStampedCache(TimeStampedCache[_ImmutableTimeStampedCache__T], typing.Generic[_ImmutableTimeStampedCache__T]):
    """
    A cache of TimeStamped data that provides concurrency through immutability. This strategy is suitable when all of the cached data is stored in memory. (For example, UTCScale) This class then provides convenient methods for accessing the data.
    """
    def __init__(self, maxNeighborsSize: int, data: typing.Union[java.util.Collection[_ImmutableTimeStampedCache__T], typing.Sequence[_ImmutableTimeStampedCache__T], typing.Set[_ImmutableTimeStampedCache__T]]):
        """
        Create a new cache with the given neighbors size and data.
        
        Parameters:
            maxNeighborsSize (int): the maximum size of the list returned from getNeighbors. Must be
                less than or equal to size().
            data (Collection<? extends ImmutableTimeStampedCache> data): the backing data for this cache. The list will be copied to ensure immutability. To guarantee immutability the entries
                in data must be immutable themselves. There must be more data than maxNeighborsSize.
        
        Raises:
            IllegalArgumentException: if size() or if neighborsSize is negative
        
        
        """
        ...
    _emptyCache__TS = typing.TypeVar('_emptyCache__TS', bound=org.orekit.time.TimeStamped)  # <TS>
    @staticmethod
    def emptyCache() -> 'ImmutableTimeStampedCache'[_emptyCache__TS]:
        """
        Get an empty immutable cache, cast to the correct type.
        
        Returns:
            an empty ImmutableTimeStampedCache.
        
        
        """
        ...
    def getAll(self) -> java.util.List[_ImmutableTimeStampedCache__T]:
        """
        Get all of the data in this cache.
        
        Returns:
            a sorted collection of all data passed in the .
        
        
        """
        ...
    def getEarliest(self) -> _ImmutableTimeStampedCache__T:
        """
        Get the earliest entry in this cache.
        
        Specified by: getEarliest in interface TimeStampedCache
        
        Returns:
            earliest cached entry
        
        
        """
        ...
    def getLatest(self) -> _ImmutableTimeStampedCache__T:
        """
        Get the latest entry in this cache.
        
        Specified by: getLatest in interface TimeStampedCache
        
        Returns:
            latest cached entry
        
        
        """
        ...
    def getMaxNeighborsSize(self) -> int:
        """
        Get the maximum size of the lists returned by getNeighbors.
        
        Specified by: getMaxNeighborsSize in interface TimeStampedCache
        
        Returns:
            size of the list
        
        
        """
        ...
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_ImmutableTimeStampedCache__T]: ...
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int) -> java.util.stream.Stream[_ImmutableTimeStampedCache__T]: ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class ParameterDriversList:
    """
    Class managing several ParameterDriver, taking care of duplicated names.
    
    Once parameter drivers sharing the same name have been added to an instance of this class, they are permanently bound together and also bound to the getDrivers that manages them. This means that if drivers d1, d2... dn are added to the list and both correspond to parameter name "P", then getDrivers will return a list containing a delegating driver delegateD for the same name "P". Afterwards, whenever either setValue or setReferenceDate is called on any of the n+1 instances d1, d2... dn or delegateD, the call will be automatically forwarded to the n remaining instances, hence ensuring they remain consistent with each other.
    
    Since:
        8.0
    """
    def __init__(self):
        """
        Creates an empty list.
        """
        ...
    def add(self, driver: ParameterDriver) -> None:
        """
        Add a driver.
        
        If the driver is already present, it will not be added. If another driver managing the same parameter is present, both drivers will be managed together, existing drivers being set to the value of the last driver added (i.e. each addition overrides the parameter value).
        
        Warning if a driver is added and a driver with the same name was already added before, they should have the same validity periods to avoid surprises. Whatever, all driver having same name will have their valueSpanMap, nameSpanMap and validity period overwritten with the last driver added attributes.
        
        Parameters:
            driver (ParameterDriver): driver to add
        
        
        """
        ...
    def filter(self, selected: bool) -> None:
        """
        Filter parameters to keep only one type of selection status.
        
        Parameters:
            selected (boolean): if true, only isSelected parameters will be kept, the other ones will be
                removed
        
        
        """
        ...
    def findByName(self, name: str) -> 'ParameterDriversList.DelegatingDriver':
        """
        Find a DelegatingDriver by name.
        
        Parameters:
            name (String): name to check
        
        Returns:
            a DelegatingDriver managing this parameter name
        
        Since:
            9.1
        
        
        """
        ...
    def findDelegatingSpanNameBySpanName(self, name: str) -> str:
        """
        Find a DelegatingDriver by name.
        
        Parameters:
            name (String): name to check
        
        Returns:
            a DelegatingDriver managing this parameter name
        
        Since:
            9.1
        
        
        """
        ...
    def getDrivers(self) -> java.util.List['ParameterDriversList.DelegatingDriver']:
        """
        Get delegating drivers for all parameters.
        
        The delegating drivers are not the same as the drivers added to the list, but they delegate to them.
        
        All delegating drivers manage parameters with different names.
        
        Returns:
            unmodifiable view of the list of delegating drivers
        
        
        """
        ...
    def getNbParams(self) -> int:
        """
        Get the number of parameters with different names.
        
        Returns:
            number of parameters with different names
        
        
        """
        ...
    def getNbValuesToEstimate(self) -> int:
        """
        Get the number of values to estimate for parameters with different names.
        
        Returns:
            number of values to estimate for parameters with different names
        
        
        """
        ...
    def sort(self) -> None:
        """
        Sort the parameters lexicographically.
        """
        ...
    class DelegatingDriver(ParameterDriver):
        def getRawDrivers(self) -> java.util.List[ParameterDriver]: ...

class PythonConstants(Constants):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldPVCoordinatesProvider__T = typing.TypeVar('_PythonFieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldPVCoordinatesProvider(FieldPVCoordinatesProvider[_PythonFieldPVCoordinatesProvider__T], typing.Generic[_PythonFieldPVCoordinatesProvider__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> 'TimeStampedFieldPVCoordinates'[_PythonFieldPVCoordinatesProvider__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldPVCoordinatesProvider> date): current date
            frame (Frame): the frame where to define the position
        
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

_PythonFieldTimeStampedCache__T = typing.TypeVar('_PythonFieldTimeStampedCache__T', bound=org.orekit.time.FieldTimeStamped)  # <T>
_PythonFieldTimeStampedCache__KK = typing.TypeVar('_PythonFieldTimeStampedCache__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class PythonFieldTimeStampedCache(FieldTimeStampedCache[_PythonFieldTimeStampedCache__T, _PythonFieldTimeStampedCache__KK], typing.Generic[_PythonFieldTimeStampedCache__T, _PythonFieldTimeStampedCache__KK]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEarliest(self) -> _PythonFieldTimeStampedCache__T:
        """
        Get the earliest entry in this cache.
        
        Specified by: getEarliest in interface FieldTimeStampedCache
        
        Returns:
            earliest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getLatest(self) -> _PythonFieldTimeStampedCache__T:
        """
        Description copied from interface: getLatest Get the latest entry in this cache.
        
        Specified by: getLatest in interface FieldTimeStampedCache
        
        Returns:
            latest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getMaxNeighborsSize(self) -> int:
        """
        Get the fixed size of the lists returned by getNeighbors.
        
        Specified by: getMaxNeighborsSize in interface FieldTimeStampedCache
        
        Returns:
            size of the list
        
        
        """
        ...
    @typing.overload
    def getNeighbors(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldTimeStampedCache__KK]) -> java.util.stream.Stream[_PythonFieldTimeStampedCache__T]: ...
    @typing.overload
    def getNeighbors(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldTimeStampedCache__KK], int: int) -> java.util.stream.Stream[_PythonFieldTimeStampedCache__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonFormatter(Formatter):
    def __init__(self): ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, double: float) -> str:
        """
        Format a double number.
        
        Specified by: toString in interface Formatter
        
        Parameters:
            value (double): number to format
        
        Returns:
            number formatted.
        
        Format a date. Does not check if date time is real or if it will meet formating requirements.
        
        Specified by: toString in interface Formatter
        
        Parameters:
            year (int): of date to be formatted
            month (int): of date to be formatted
            day (int): of month to be formatted
            hour (int): to be formatted
            minute (int): to be formatted
            seconds (double): and sub-seconds to be formatted
        
        Returns:
            date formatted to match the following format [yyyy-MM-ddTHH:mm:ss.S#]
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str: ...

class PythonMultipleShooting(MultipleShooting):
    def __init__(self): ...
    def compute(self) -> java.util.List[org.orekit.propagation.SpacecraftState]:
        """
        Return the list of corrected patch points. An optimizer is better suited for this problem
        
        Specified by: compute in interface MultipleShooting
        
        Returns:
            patchedSpacecraftStates
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonPVCoordinatesProvider(PVCoordinatesProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
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

class PythonParameterDriversProvider(ParameterDriversProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonParameterFunction(ParameterFunction):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def value(self, parameterDriver: ParameterDriver, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Evaluate the function.
        
        Specified by: value in interface ParameterFunction
        
        Parameters:
            parameterDriver (ParameterDriver): driver for the parameter.
            date (AbsoluteDate): date at which the function wants to be known
        
        Returns:
            scalar value of the function
        
        
        """
        ...

class PythonParameterObserver(ParameterObserver):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def valueChanged(self, previousValue: float, driver: ParameterDriver, date: org.orekit.time.AbsoluteDate) -> None:
        """
        Description copied from interface: valueChanged Notify that a parameter value has been changed.
        
        Specified by: valueChanged in interface ParameterObserver
        
        Parameters:
            previousValue (double): previous value
            driver (ParameterDriver): parameter driver that has been changed
            date (AbsoluteDate): date for which the parameter value have been updated
        
        
        """
        ...
    def valueSpanMapChanged(self, previousValueSpanMap: TimeSpanMap[float], driver: ParameterDriver) -> None:
        """
        Description copied from interface: valueSpanMapChanged Notify that a parameter value span map has been changed.
        
        Specified by: valueSpanMapChanged in interface ParameterObserver
        
        Parameters:
            previousValueSpanMap (TimeSpanMap<Double> previousValueSpanMap): previous value
            driver (ParameterDriver): parameter driver that has been changed
        
        
        """
        ...

class PythonStateFunction(StateFunction):
    def __init__(self): ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def value(self, state: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]:
        """
        Evaluate the function.
        
        Specified by: value in interface StateFunction
        
        Parameters:
            state (SpacecraftState): spacecraft state as the sole free parameter of the function.
        
        Returns:
            vector value of the function
        
        
        """
        ...

class PythonStateJacobian(StateJacobian):
    def __init__(self): ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def value(self, state: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Evaluate the Jacobian of the function.
        
        Specified by: value in interface StateJacobian
        
        Parameters:
            state (SpacecraftState): spacecraft state as the sole free parameter of the function.
        
        Returns:
            Jacobian matric
        
        
        """
        ...

_PythonTimeStampedCache__T = typing.TypeVar('_PythonTimeStampedCache__T', bound=org.orekit.time.TimeStamped)  # <T>
class PythonTimeStampedCache(TimeStampedCache[_PythonTimeStampedCache__T], typing.Generic[_PythonTimeStampedCache__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEarliest(self) -> _PythonTimeStampedCache__T:
        """
        Get the earliest entry in this cache.
        
        Specified by: getEarliest in interface TimeStampedCache
        
        Returns:
            earliest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getLatest(self) -> _PythonTimeStampedCache__T:
        """
        Get the latest entry in this cache.
        
        Specified by: getLatest in interface TimeStampedCache
        
        Returns:
            latest cached entry
        
        Raises:
            IllegalStateException: if this cache is empty
        
        
        """
        ...
    def getMaxNeighborsSize(self) -> int:
        """
        Get the maximum size of the lists returned by getNeighbors.
        
        Specified by: getMaxNeighborsSize in interface TimeStampedCache
        
        Returns:
            size of the list
        
        
        """
        ...
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.stream.Stream[_PythonTimeStampedCache__T]: ...
    @typing.overload
    def getNeighbors(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int) -> java.util.stream.Stream[_PythonTimeStampedCache__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonTimeStampedGenerator__T = typing.TypeVar('_PythonTimeStampedGenerator__T', bound=org.orekit.time.TimeStamped)  # <T>
class PythonTimeStampedGenerator(TimeStampedGenerator[_PythonTimeStampedGenerator__T], typing.Generic[_PythonTimeStampedGenerator__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def generate(self, existingDate: org.orekit.time.AbsoluteDate, date: org.orekit.time.AbsoluteDate) -> java.util.List[_PythonTimeStampedGenerator__T]:
        """
        Generate a chronologically sorted list of entries to be cached.
        
        If existingDate is earlier than date, the range covered by generated entries must cover at least from existingDate (excluded) to date (included). If existingDate is later than date, the range covered by generated entries must cover at least from date (included) to existingDate (excluded).
        
        The generated entries may cover a range larger than the minimum specified above if the generator prefers to generate large chunks of data at once. It may generate again entries already generated by an earlier call (typically at existingDate), these extra entries will be silently ignored by the cache.
        
        Non-coverage of the minimum range may lead to a loss of data, as the gap will not be filled by the GenericTimeStampedCache in subsequent calls.
        
        The generated entries must be chronologically sorted.
        
        Specified by: generate in interface TimeStampedGenerator
        
        Parameters:
            existingDate (AbsoluteDate): date of the closest already existing entry (may be null)
            date (AbsoluteDate): date that must be covered by the range of the generated array
        
        Returns:
            chronologically sorted list of generated entries
        
        
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

_ShiftablePVCoordinatesHolder__T = typing.TypeVar('_ShiftablePVCoordinatesHolder__T', bound=PVCoordinatesProvider)  # <T>
class ShiftablePVCoordinatesHolder(PVCoordinatesProvider, org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['ShiftablePVCoordinatesHolder'[_ShiftablePVCoordinatesHolder__T]], typing.Generic[_ShiftablePVCoordinatesHolder__T]):
    """
    Interface for time-shiftable PV provider holding themselves PV coordinates.
    
    Since:
        13.1.2
    """
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Getter for the intrinsic frame.
        
        Returns:
            frame
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> 'TimeStampedPVCoordinates':
        """
        Getter for the intrinsic position-velocity vector.
        
        Returns:
            position-velocity
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
        Description copied from interface: getPVCoordinates Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Getter for the position vector.
        
        Returns:
            position
        
        """
        ...
    @typing.overload
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from interface: getPosition Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...
    @typing.overload
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Getter for the velocity vector.
        
        Returns:
            velocity
        
        """
        ...
    @typing.overload
    def getVelocity(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Description copied from interface: getVelocity Get the velocity of the body in the selected frame.
        
        Specified by: getVelocity in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the velocity
        
        Returns:
            velocity of the body (m/s)
        
        
        """
        ...

class ShiftingPVCoordinatesProvider(PVCoordinatesProvider):
    """
    Provider using simple shiftedBy shiftedBy} and frame transforms for evolution.
    
    Since:
        12.1
    """
    def __init__(self, referencePV: 'TimeStampedPVCoordinates', referenceFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            referencePV (TimeStampedPVCoordinates): reference coordinates
            referenceFrame (Frame): frame in which reference is defined
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> 'TimeStampedPVCoordinates':
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...

class TimeStampedAngularCoordinates(AngularCoordinates, org.orekit.time.TimeStamped):
    """
    TimeStamped version of AngularCoordinates.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        7.0
    
    Also see:
        serialized
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
    def addOffset(self, offset: AngularCoordinates) -> 'TimeStampedAngularCoordinates':
        """
        Add an offset from the instance.
        
        We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. addOffset(b) and addOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Overrides: addOffset in class AngularCoordinates
        
        Parameters:
            offset (AngularCoordinates): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            subtractOffset
        
        
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
    def revert(self) -> 'TimeStampedAngularCoordinates':
        """
        Revert a rotation/rotation rate pair. Build a pair which reverse the effect of another pair.
        
        Overrides: revert in class AngularCoordinates
        
        Returns:
            a new pair whose effect is the reverse of the effect of the instance
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'TimeStampedAngularCoordinates':
        """
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on a simple linear model. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Overrides: shiftedBy in class AngularCoordinates
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on a simple linear model. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (TimeOffset): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'TimeStampedAngularCoordinates': ...
    def subtractOffset(self, offset: AngularCoordinates) -> 'TimeStampedAngularCoordinates':
        """
        Subtract an offset from the instance.
        
        We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. subtractOffset(b) and subtractOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Overrides: subtractOffset in class AngularCoordinates
        
        Parameters:
            offset (AngularCoordinates): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            addOffset
        
        
        """
        ...

_TimeStampedFieldAngularCoordinates__T = typing.TypeVar('_TimeStampedFieldAngularCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class TimeStampedFieldAngularCoordinates(FieldAngularCoordinates[_TimeStampedFieldAngularCoordinates__T], org.orekit.time.FieldTimeStamped[_TimeStampedFieldAngularCoordinates__T], typing.Generic[_TimeStampedFieldAngularCoordinates__T]):
    """
    TimeStamped version of FieldAngularCoordinates.
    
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
    def addOffset(self, offset: FieldAngularCoordinates[_TimeStampedFieldAngularCoordinates__T]) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]:
        """
        Add an offset from the instance.
        
        We consider here that the offset rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. addOffset(b) and addOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Overrides: addOffset in class FieldAngularCoordinates
        
        Parameters:
            offset (FieldAngularCoordinates<TimeStampedFieldAngularCoordinates> offset): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            subtractOffset
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldAngularCoordinates__T]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def revert(self) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]:
        """
        Revert a rotation/rotation rate pair. Build a pair which reverse the effect of another pair.
        
        Overrides: revert in class FieldAngularCoordinates
        
        Returns:
            a new pair whose effect is the reverse of the effect of the instance
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _TimeStampedFieldAngularCoordinates__T: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _TimeStampedFieldAngularCoordinates__T) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]: ...
    def subtractOffset(self, offset: FieldAngularCoordinates[_TimeStampedFieldAngularCoordinates__T]) -> 'TimeStampedFieldAngularCoordinates'[_TimeStampedFieldAngularCoordinates__T]:
        """
        Subtract an offset from the instance.
        
        We consider here that the offset Rotation is applied first and the instance is applied afterward. Note that angular coordinates do not commute under this operation, i.e. subtractOffset(b) and subtractOffset(a) lead to different results in most cases.
        
        The two methods addOffset and subtractOffset are designed so that round trip applications are possible. This means that both addOffset(ac2) and subtractOffset(ac2) return angular coordinates equal to ac1.
        
        Overrides: subtractOffset in class FieldAngularCoordinates
        
        Parameters:
            offset (FieldAngularCoordinates<TimeStampedFieldAngularCoordinates> offset): offset to subtract
        
        Returns:
            new instance, with offset subtracted
        
        Also see:
            addOffset
        
        
        """
        ...

_TimeStampedFieldPVCoordinates__T = typing.TypeVar('_TimeStampedFieldPVCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class TimeStampedFieldPVCoordinates(FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], org.orekit.time.FieldTimeStamped[_TimeStampedFieldPVCoordinates__T], typing.Generic[_TimeStampedFieldPVCoordinates__T]):
    """
    TimeStamped version of FieldPVCoordinates.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        7.0
    """
    ___init___28__U = typing.TypeVar('___init___28__U', bound=org.hipparchus.analysis.differentiation.FieldDerivative)  # <U>
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_TimeStampedFieldPVCoordinates__T], timeStampedPVCoordinates: 'TimeStampedPVCoordinates'): ...
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
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___28__U]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T], fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T], fieldPVCoordinates: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T], fieldPVCoordinates2: FieldPVCoordinates[_TimeStampedFieldPVCoordinates__T]): ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_TimeStampedFieldPVCoordinates__T]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _TimeStampedFieldPVCoordinates__T: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'TimeStampedFieldPVCoordinates'[_TimeStampedFieldPVCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, t: _TimeStampedFieldPVCoordinates__T) -> 'TimeStampedFieldPVCoordinates'[_TimeStampedFieldPVCoordinates__T]: ...
    @typing.overload
    def toString(self) -> str:
        """
        Return a string representation of this date, position, velocity, and acceleration.
        
        This method uses the getDefault.
        
        Overrides: toString in class FieldPVCoordinates
        
        Returns:
            string representation of this.
        
        """
        ...
    @typing.overload
    def toString(self, utc: org.orekit.time.TimeScale) -> str:
        """
        Return a string representation of this date, position, velocity, and acceleration.
        
        Parameters:
            utc (TimeScale): time scale used to print the date.
        
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
    TimeStamped version of PVCoordinates.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        7.0
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
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'TimeStampedPVCoordinates':
        """
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Overrides: shiftedBy in class PVCoordinates
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'TimeStampedPVCoordinates': ...
    @typing.overload
    def toString(self) -> str:
        """
        Return a string representation of this date, position, velocity, and acceleration.
        
        This method uses the getDefault.
        
        Overrides: toString in class PVCoordinates
        
        Returns:
            string representation of this.
        
        """
        ...
    @typing.overload
    def toString(self, utc: org.orekit.time.TimeScale) -> str:
        """
        Return a string representation of this date, position, velocity, and acceleration.
        
        Parameters:
            utc (TimeScale): time scale used to print the date.
        
        Returns:
            string representation of this.
        
        
        """
        ...
    def toTaylorProvider(self, instanceFrame: org.orekit.frames.Frame) -> PVCoordinatesProvider:
        """
        Create a local provider using simply Taylor expansion through shiftedBy.
        
        The time evolution is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Parameters:
            instanceFrame (Frame): frame in which the instance is defined
        
        Returns:
            provider based on Taylor expansion, for small time shifts around instance date
        
        
        """
        ...

class TruncatedCcsdsFormatter(Formatter):
    """
    Formatter used to produce strings from data that are compliant with CCSDS standards.
    
    Formats a double number to achieve CCSDS formatting standards for: OPM, OMM, OEM, or OCM (502.0-B-3 7.5.6), CDM (508.0-B-1 6.3.2.2), TDM (503.0-B-2 4.3.4), and ADM (504.0-B-2 6.8.4.1). This states that the mantissa shall not exceed 16 digits.
    
    This does NOT ensure round-trip safety. See AccurateFormatter for a formatter that ensures round trip safety.
    
    Since:
        13.0
    """
    def __init__(self):
        """
        Public constructor.
        """
        ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, double: float) -> str:
        """
        Format a double number. Formats to CCSDS compliant standards.
        
        Specified by: toString in interface Formatter
        
        Parameters:
            value (double): number to format
        
        Returns:
            number formatted to full accuracy or CCSDS standards
        
        Formats to CCSDS 16 digit standard for the seconds variable. Format a date. Does not check if date time is real or if it will meet formating requirements.
        
        Specified by: toString in interface Formatter
        
        Parameters:
            year (int): of date to be formatted
            month (int): of date to be formatted
            day (int): of month to be formatted
            hour (int): to be formatted
            minute (int): to be formatted
            seconds (double): and sub-seconds to be formatted
        
        Returns:
            date formatted to match the following format [yyyy-MM-ddTHH:mm:ss.S#]
        
        
        """
        ...
    @typing.overload
    def toString(self, int: int, int2: int, int3: int, int4: int, int5: int, double: float) -> str: ...

class AbsolutePVCoordinates(TimeStampedPVCoordinates, org.orekit.time.TimeStamped, PVCoordinatesProvider):
    """
    Position - Velocity - Acceleration linked to a date and a frame.
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
            outputFrame (Frame): frame in which the position/velocity coordinates shall be computed
        
        Returns:
            TimeStampedPVCoordinates
        
        Raises:
            OrekitException: if transformation between frames cannot be computed
        
        Also see:
            getPVCoordinates
        
        Description copied from interface: getPVCoordinates Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            otherDate (AbsoluteDate): current date
            outputFrame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates: ...
    @typing.overload
    def getPosition(self, outputFrame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position in a specified frame.
        
        Parameters:
            outputFrame (Frame): frame in which the position coordinates shall be computed
        
        Returns:
            position
        
        Since:
            12.0
        
        Also see:
            getPVCoordinates
        
        
        """
        ...
    @typing.overload
    def getPosition(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'AbsolutePVCoordinates':
        """
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Overrides: shiftedBy in class TimeStampedPVCoordinates
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Overrides: shiftedBy in class TimeStampedPVCoordinates
        
        Parameters:
            dt (TimeOffset): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable)
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'AbsolutePVCoordinates': ...
    @typing.overload
    def toTaylorProvider(self) -> PVCoordinatesProvider:
        """
        Create a local provider using simply Taylor expansion through shiftedBy.
        
        The time evolution is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Returns:
            provider based on Taylor expansion, for small time shifts around instance date
        
        
        """
        ...
    @typing.overload
    def toTaylorProvider(self, frame: org.orekit.frames.Frame) -> PVCoordinatesProvider: ...

class ExtendedPVCoordinatesProvider(ExtendedPositionProvider):
    """
    Deprecated. since 13.0. Use ExtendedPositionProvider instead. Interface for PV coordinates providers that also support fields.
    
    Since:
        9.2
    """
    _getPVCoordinates_0__T = typing.TypeVar('_getPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_0__T], frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_getPVCoordinates_0__T]:
        """
        Deprecated. Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface ExtendedPositionProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates: ...
    _getPosition_0__T = typing.TypeVar('_getPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_getPosition_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPosition_0__T]:
        """
        Deprecated. Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface ExtendedPositionProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def getPosition(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

_FieldAbsolutePVCoordinates__T = typing.TypeVar('_FieldAbsolutePVCoordinates__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbsolutePVCoordinates(TimeStampedFieldPVCoordinates[_FieldAbsolutePVCoordinates__T], org.orekit.time.FieldTimeStamped[_FieldAbsolutePVCoordinates__T], FieldPVCoordinatesProvider[_FieldAbsolutePVCoordinates__T], typing.Generic[_FieldAbsolutePVCoordinates__T]):
    """
    Field implementation of AbsolutePVCoordinates.
    
    Also see:
        AbsolutePVCoordinates
    """
    ___init___1__U = typing.TypeVar('___init___1__U', bound=org.hipparchus.analysis.differentiation.FieldDerivative)  # <U>
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAbsolutePVCoordinates__T], absolutePVCoordinates: AbsolutePVCoordinates): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[___init___1__U]): ...
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
    @typing.overload
    def getPosition(self, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T]: ...
    @typing.overload
    def getPosition(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbsolutePVCoordinates__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T]: ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAbsolutePVCoordinates__T]: ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _FieldAbsolutePVCoordinates__T: ...
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
    def toTaylorProvider(self) -> FieldPVCoordinatesProvider[_FieldAbsolutePVCoordinates__T]:
        """
        Create a local provider using simply Taylor expansion through shiftedBy.
        
        The time evolution is based on a simple Taylor expansion. It is not intended as a replacement for proper orbit propagation (it is not even Keplerian!) but should be sufficient for either small time shifts or coarse accuracy.
        
        Returns:
            provider based on Taylor expansion, for small time shifts around instance date
        
        
        """
        ...

class FrameAdapter(ExtendedPositionProvider):
    """
    Adapter from Frame to ExtendedPositionProvider.
    
    The moving point is the origin of the adapted frame.
    
    This class is roughly the inverse of ExtendedPositionProviderAdapter
    
    Since:
        12.0
    
    Also see:
        ExtendedPositionProviderAdapter
    """
    def __init__(self, originFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            originFrame (Frame): frame whose origin coordinates are desired
        
        
        """
        ...
    _getPVCoordinates_0__T = typing.TypeVar('_getPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_0__T], frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_getPVCoordinates_0__T]:
        """
        Get the position-velocity-acceleration in the selected frame.
        
        Specified by: getPVCoordinates in interface ExtendedPositionProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position-velocity-acceleration vector
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface ExtendedPositionProvider
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    _getPosition_0__T = typing.TypeVar('_getPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_getPosition_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPosition_0__T]:
        """
        Get the position in the selected frame.
        
        Specified by: getPosition in interface ExtendedPositionProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position
        
        
        """
        ...
    @typing.overload
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        """
        ...

class MultipleShooter(AbstractMultipleShooting):
    """
    Multiple shooting method applicable for trajectories, in an ephemeris model. Not suited for closed orbits.
    
    Since:
        10.2
    
    Also see:
        "TRAJECTORY DESIGN AND ORBIT MAINTENANCE STRATEGIES IN MULTI-BODY DYNAMICAL REGIMES by Thomas A. Pavlak, Purdue
        University"
    """
    def __init__(self, initialGuessList: java.util.List[org.orekit.propagation.SpacecraftState], propagatorList: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], epochEquations: java.util.List[org.orekit.propagation.numerical.EpochDerivativesEquations], tolerance: float, maxIter: int):
        """
        Simple Constructor.
        
        Standard constructor for multiple shooting which can be used with non-autonomous systems.
        
        Parameters:
            initialGuessList (List<SpacecraftState> initialGuessList): initial patch points to be corrected
            propagatorList (List<NumericalPropagator> propagatorList): list of propagators associated to each patch point
            epochEquations (List<EpochDerivativesEquations> epochEquations): list of additional derivatives providers linked to propagatorList
            tolerance (double): convergence tolerance on the constraint vector
            maxIter (int): maximum number of iterations
        
        
        """
        ...

class PythonAbstractMultipleShooting(AbstractMultipleShooting):
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], double: float, int: int, boolean: bool, string: str): ...
    def computeAdditionalConstraints(self, propagatedSP: java.util.List[org.orekit.propagation.SpacecraftState]) -> typing.MutableSequence[float]:
        """
        Compute the additional constraints.
        
        Specified by: computeAdditionalConstraints in class AbstractMultipleShooting
        
        Parameters:
            propagatedSP (List<SpacecraftState> propagatedSP): propagated SpacecraftState
        
        Returns:
            additional constraints
        
        
        """
        ...
    def computeAdditionalJacobianMatrix(self, propagatedSP: java.util.List[org.orekit.propagation.SpacecraftState]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute a part of the Jacobian matrix from additional constraints.
        
        Specified by: computeAdditionalJacobianMatrix in class AbstractMultipleShooting
        
        Parameters:
            propagatedSP (List<SpacecraftState> propagatedSP): propagatedSP
        
        Returns:
            Jacobian sub-matrix
        
        
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
    def getAugmentedInitialState(self, i: int) -> org.orekit.propagation.SpacecraftState:
        """
        Description copied from class: getAugmentedInitialState Compute the additional state from the additionalEquations.
        
        Specified by: getAugmentedInitialState in class AbstractMultipleShooting
        
        Parameters:
            i (int): index of the state
        
        Returns:
            SpacecraftState with the additional state within.
        
        
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

class PythonBoundedPVCoordinatesProvider(BoundedPVCoordinatesProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getMaxDate Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getMinDate Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates:
        """
        Description copied from interface: getPVCoordinates Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
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

class PythonExtendedPositionProvider(ExtendedPositionProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getPosition_1__T = typing.TypeVar('_getPosition_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPosition(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_getPosition_1__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPosition_1__T]:
        """
        Get the position in the selected frame.
        
        Specified by: getPosition in interface ExtendedPositionProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position
        
        
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

_PythonFieldBoundedPVCoordinatesProvider__T = typing.TypeVar('_PythonFieldBoundedPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldBoundedPVCoordinatesProvider(FieldBoundedPVCoordinatesProvider[_PythonFieldBoundedPVCoordinatesProvider__T], typing.Generic[_PythonFieldBoundedPVCoordinatesProvider__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPVCoordinatesProvider__T]:
        """
        Description copied from interface: getMaxDate Get the last date of the range.
        
        Specified by: getMaxDate in interface FieldBoundedPVCoordinatesProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPVCoordinatesProvider__T]:
        """
        Description copied from interface: getMinDate Get the first date of the range.
        
        Specified by: getMinDate in interface FieldBoundedPVCoordinatesProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPVCoordinatesProvider__T], frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_PythonFieldBoundedPVCoordinatesProvider__T]:
        """
        Description copied from interface: getPVCoordinates Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldBoundedPVCoordinatesProvider> date): current date
            frame (Frame): the frame where to define the position
        
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

_PythonShiftablePVCoordinatesHolder__T = typing.TypeVar('_PythonShiftablePVCoordinatesHolder__T', bound=PVCoordinatesProvider)  # <T>
class PythonShiftablePVCoordinatesHolder(ShiftablePVCoordinatesHolder[_PythonShiftablePVCoordinatesHolder__T], typing.Generic[_PythonShiftablePVCoordinatesHolder__T]):
    """
    Python implementation of the ShiftablePVCoordinatesHolder interface. This class is part of the JCC Python interface and exposes all methods natively.
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Getter for the intrinsic frame.
        
        Specified by: getFrame in interface ShiftablePVCoordinatesHolder
        
        Returns:
            frame
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> TimeStampedPVCoordinates:
        """
        Getter for the intrinsic position-velocity vector.
        
        Specified by: getPVCoordinates in interface ShiftablePVCoordinatesHolder
        
        Returns:
            position-velocity
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Specified by: getPVCoordinates in interface ShiftablePVCoordinatesHolder
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
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
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _PythonShiftablePVCoordinatesHolder__T: ...
    @typing.overload
    def shiftedBy(self, double: float) -> ShiftablePVCoordinatesHolder[_PythonShiftablePVCoordinatesHolder__T]: ...

class PythonExtendedPVCoordinatesProvider(ExtendedPVCoordinatesProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getPVCoordinates_0__T = typing.TypeVar('_getPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_0__T], frame: org.orekit.frames.Frame) -> TimeStampedFieldPVCoordinates[_getPVCoordinates_0__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface ExtendedPositionProvider
        
        Specified by: getPVCoordinates in interface ExtendedPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface ExtendedPositionProvider
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.utils")``.

    AbsolutePVCoordinates: typing.Type[AbsolutePVCoordinates]
    AbsolutePVCoordinatesHermiteInterpolator: typing.Type[AbsolutePVCoordinatesHermiteInterpolator]
    AbstractMultipleShooting: typing.Type[AbstractMultipleShooting]
    AccurateFormatter: typing.Type[AccurateFormatter]
    AggregatedPVCoordinatesProvider: typing.Type[AggregatedPVCoordinatesProvider]
    AngularCoordinates: typing.Type[AngularCoordinates]
    AngularDerivativesFilter: typing.Type[AngularDerivativesFilter]
    BoundedPVCoordinatesProvider: typing.Type[BoundedPVCoordinatesProvider]
    CartesianCovarianceUtils: typing.Type[CartesianCovarianceUtils]
    CartesianDerivativesFilter: typing.Type[CartesianDerivativesFilter]
    ConstantPVCoordinatesProvider: typing.Type[ConstantPVCoordinatesProvider]
    Constants: typing.Type[Constants]
    DataDictionary: typing.Type[DataDictionary]
    DateDriver: typing.Type[DateDriver]
    DerivativeStateUtils: typing.Type[DerivativeStateUtils]
    Differentiation: typing.Type[Differentiation]
    DoubleArrayDictionary: typing.Type[DoubleArrayDictionary]
    ElevationMask: typing.Type[ElevationMask]
    ExpungePolicy: typing.Type[ExpungePolicy]
    ExtendedPVCoordinatesProvider: typing.Type[ExtendedPVCoordinatesProvider]
    ExtendedPositionProvider: typing.Type[ExtendedPositionProvider]
    ExtendedPositionProviderAdapter: typing.Type[ExtendedPositionProviderAdapter]
    FieldAbsolutePVCoordinates: typing.Type[FieldAbsolutePVCoordinates]
    FieldAbsolutePVCoordinatesHermiteInterpolator: typing.Type[FieldAbsolutePVCoordinatesHermiteInterpolator]
    FieldAngularCoordinates: typing.Type[FieldAngularCoordinates]
    FieldArrayDictionary: typing.Type[FieldArrayDictionary]
    FieldBoundedPVCoordinatesProvider: typing.Type[FieldBoundedPVCoordinatesProvider]
    FieldDataDictionary: typing.Type[FieldDataDictionary]
    FieldLegendrePolynomials: typing.Type[FieldLegendrePolynomials]
    FieldPVCoordinates: typing.Type[FieldPVCoordinates]
    FieldPVCoordinatesProvider: typing.Type[FieldPVCoordinatesProvider]
    FieldShiftingPVCoordinatesProvider: typing.Type[FieldShiftingPVCoordinatesProvider]
    FieldSortedListTrimmer: typing.Type[FieldSortedListTrimmer]
    FieldTimeSpanMap: typing.Type[FieldTimeSpanMap]
    FieldTimeStampedCache: typing.Type[FieldTimeStampedCache]
    FieldTrackingCoordinates: typing.Type[FieldTrackingCoordinates]
    Fieldifier: typing.Type[Fieldifier]
    Formatter: typing.Type[Formatter]
    FrameAdapter: typing.Type[FrameAdapter]
    GenericTimeStampedCache: typing.Type[GenericTimeStampedCache]
    IERSConventions: typing.Type[IERSConventions]
    ImmutableFieldTimeStampedCache: typing.Type[ImmutableFieldTimeStampedCache]
    ImmutableTimeStampedCache: typing.Type[ImmutableTimeStampedCache]
    InterpolationTableLoader: typing.Type[InterpolationTableLoader]
    LagrangianPoints: typing.Type[LagrangianPoints]
    LegendrePolynomials: typing.Type[LegendrePolynomials]
    LoveNumbers: typing.Type[LoveNumbers]
    MultipleShooter: typing.Type[MultipleShooter]
    MultipleShooting: typing.Type[MultipleShooting]
    OccultationEngine: typing.Type[OccultationEngine]
    OrekitConfiguration: typing.Type[OrekitConfiguration]
    PVCoordinates: typing.Type[PVCoordinates]
    PVCoordinatesProvider: typing.Type[PVCoordinatesProvider]
    ParameterDriver: typing.Type[ParameterDriver]
    ParameterDriversList: typing.Type[ParameterDriversList]
    ParameterDriversProvider: typing.Type[ParameterDriversProvider]
    ParameterFunction: typing.Type[ParameterFunction]
    ParameterObserver: typing.Type[ParameterObserver]
    PythonAbstractMultipleShooting: typing.Type[PythonAbstractMultipleShooting]
    PythonBoundedPVCoordinatesProvider: typing.Type[PythonBoundedPVCoordinatesProvider]
    PythonConstants: typing.Type[PythonConstants]
    PythonExtendedPVCoordinatesProvider: typing.Type[PythonExtendedPVCoordinatesProvider]
    PythonExtendedPositionProvider: typing.Type[PythonExtendedPositionProvider]
    PythonFieldBoundedPVCoordinatesProvider: typing.Type[PythonFieldBoundedPVCoordinatesProvider]
    PythonFieldPVCoordinatesProvider: typing.Type[PythonFieldPVCoordinatesProvider]
    PythonFieldTimeStampedCache: typing.Type[PythonFieldTimeStampedCache]
    PythonFormatter: typing.Type[PythonFormatter]
    PythonMultipleShooting: typing.Type[PythonMultipleShooting]
    PythonPVCoordinatesProvider: typing.Type[PythonPVCoordinatesProvider]
    PythonParameterDriversProvider: typing.Type[PythonParameterDriversProvider]
    PythonParameterFunction: typing.Type[PythonParameterFunction]
    PythonParameterObserver: typing.Type[PythonParameterObserver]
    PythonShiftablePVCoordinatesHolder: typing.Type[PythonShiftablePVCoordinatesHolder]
    PythonStateFunction: typing.Type[PythonStateFunction]
    PythonStateJacobian: typing.Type[PythonStateJacobian]
    PythonTimeStampedCache: typing.Type[PythonTimeStampedCache]
    PythonTimeStampedGenerator: typing.Type[PythonTimeStampedGenerator]
    SecularAndHarmonic: typing.Type[SecularAndHarmonic]
    ShiftablePVCoordinatesHolder: typing.Type[ShiftablePVCoordinatesHolder]
    ShiftingPVCoordinatesProvider: typing.Type[ShiftingPVCoordinatesProvider]
    SortedListTrimmer: typing.Type[SortedListTrimmer]
    StateFunction: typing.Type[StateFunction]
    StateJacobian: typing.Type[StateJacobian]
    TimeSpanMap: typing.Type[TimeSpanMap]
    TimeStampedAngularCoordinates: typing.Type[TimeStampedAngularCoordinates]
    TimeStampedAngularCoordinatesHermiteInterpolator: typing.Type[TimeStampedAngularCoordinatesHermiteInterpolator]
    TimeStampedCache: typing.Type[TimeStampedCache]
    TimeStampedFieldAngularCoordinates: typing.Type[TimeStampedFieldAngularCoordinates]
    TimeStampedFieldAngularCoordinatesHermiteInterpolator: typing.Type[TimeStampedFieldAngularCoordinatesHermiteInterpolator]
    TimeStampedFieldPVCoordinates: typing.Type[TimeStampedFieldPVCoordinates]
    TimeStampedFieldPVCoordinatesHermiteInterpolator: typing.Type[TimeStampedFieldPVCoordinatesHermiteInterpolator]
    TimeStampedGenerator: typing.Type[TimeStampedGenerator]
    TimeStampedPVCoordinates: typing.Type[TimeStampedPVCoordinates]
    TimeStampedPVCoordinatesHermiteInterpolator: typing.Type[TimeStampedPVCoordinatesHermiteInterpolator]
    TrackingCoordinates: typing.Type[TrackingCoordinates]
    TruncatedCcsdsFormatter: typing.Type[TruncatedCcsdsFormatter]
    WaypointPVBuilder: typing.Type[WaypointPVBuilder]
    formatting: org.orekit.utils.formatting.__module_protocol__
    units: org.orekit.utils.units.__module_protocol__
