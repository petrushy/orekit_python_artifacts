import java.io
import java.lang
import java.util
import java.util.stream
import org.hipparchus
import org.orekit.attitudes
import org.orekit.bodies
import org.orekit.frames
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



class CR3BPDifferentialCorrection:
    """
    public class CR3BPDifferentialCorrection extends Object
    
        Class implementing the differential correction method for Halo or Lyapunov Orbits. It is not a simple differential
        correction, it uses higher order terms to be more accurate and meet orbits requirements.
    
        Since:
            10.2
    
        Also see:
            "Three-dimensional, periodic, Halo Orbits by Kathleen Connor Howell, Stanford University"
    """
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, cR3BPSystem: org.orekit.bodies.CR3BPSystem, double: float): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, cR3BPSystem: org.orekit.bodies.CR3BPSystem, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider, timeScale: org.orekit.time.TimeScale): ...
    def compute(self, librationOrbitType: 'LibrationOrbitType') -> org.orekit.utils.PVCoordinates:
        """
            Return the real starting PVCoordinates on the Libration orbit type after differential correction from a first guess.
        
            Parameters:
                type (:class:`~org.orekit.orbits.LibrationOrbitType`): libration orbit type
        
            Returns:
                pv Position-Velocity of the starting point on the Halo Orbit
        
        
        """
        ...
    def computeLyapunov(self) -> org.orekit.utils.PVCoordinates:
        """
            Return the real starting PVCoordinates on the Lyapunov orbit after differential correction from a first guess.
        
            Returns:
                pv Position-Velocity of the starting point on the Lyapunov Orbit
        
        
        """
        ...
    def getOrbitalPeriod(self) -> float:
        """
            Get the orbital period of the required orbit.
        
            Returns:
                the orbitalPeriod
        
        
        """
        ...

_FieldOrbit__T = typing.TypeVar('_FieldOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrbit(org.orekit.utils.FieldPVCoordinatesProvider[_FieldOrbit__T], org.orekit.time.FieldTimeStamped[_FieldOrbit__T], org.orekit.time.FieldTimeShiftable['FieldOrbit'[_FieldOrbit__T], _FieldOrbit__T], org.orekit.time.FieldTimeInterpolable['FieldOrbit'[_FieldOrbit__T], _FieldOrbit__T], typing.Generic[_FieldOrbit__T]):
    """
    public abstract class FieldOrbit<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T>, :class:`~org.orekit.time.FieldTimeStamped`<T>, :class:`~org.orekit.time.FieldTimeShiftable`<:class:`~org.orekit.orbits.FieldOrbit`<T>,T>, :class:`~org.orekit.time.FieldTimeInterpolable`<:class:`~org.orekit.orbits.FieldOrbit`<T>,T>
    
        This class handles orbital parameters.
    
        For user convenience, both the Cartesian and the equinoctial elements are provided by this class, regardless of the
        canonical representation implemented in the derived class (which may be classical Keplerian elements for example).
    
        The parameters are defined in a frame specified by the user. It is important to make sure this frame is consistent: it
        probably is inertial and centered on the central body. This information is used for example by some force models.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            9.0
    """
    def addKeplerContribution(self, positionAngle: 'PositionAngle', t: _FieldOrbit__T, tArray: typing.List[_FieldOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> _FieldOrbit__T:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldOrbit__T:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                semi-major axis derivative (m/s)
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldOrbit__T]: ...
    def getE(self) -> _FieldOrbit__T:
        """
            Get the eccentricity.
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldOrbit__T:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbital parameters are defined.
        
            Returns:
                frame in which the orbital parameters are defined
        
        
        """
        ...
    def getHx(self) -> _FieldOrbit__T:
        """
            Get the first component of the inclination vector.
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldOrbit__T:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldOrbit__T:
        """
            Get the second component of the inclination vector.
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldOrbit__T:
        """
            Get the second component of the inclination vector derivative.
        
            Returns:
                second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldOrbit__T:
        """
            Get the inclination.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldOrbit__T:
        """
            Get the inclination derivative.
        
            Returns:
                inclination derivative (rad/s)
        
        
        """
        ...
    def getJacobianWrtCartesian(self, positionAngle: 'PositionAngle', tArray: typing.List[typing.List[_FieldOrbit__T]]) -> None:
        """
            Compute the Jacobian of the orbital parameters with respect to the Cartesian parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of parameter i of the orbit with respect to Cartesian coordinate j.
            This means each row corresponds to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates
            x, y, z, xDot, yDot and zDot.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle to use
                jacobian (:class:`~org.orekit.orbits.FieldOrbit`[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                    corner will be modified
        
        
        """
        ...
    def getJacobianWrtParameters(self, positionAngle: 'PositionAngle', tArray: typing.List[typing.List[_FieldOrbit__T]]) -> None:
        """
            Compute the Jacobian of the Cartesian parameters with respect to the orbital parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of Cartesian coordinate i of the orbit with respect to orbital
            parameter j. This means each row corresponds to one Cartesian coordinate x, y, z, xdot, ydot, zdot whereas columns 0 to
            5 correspond to the orbital parameters.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle to use
                jacobian (:class:`~org.orekit.orbits.FieldOrbit`[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                    corner will be modified
        
        
        """
        ...
    def getKeplerianMeanMotion(self) -> _FieldOrbit__T:
        """
            Get the Keplerian mean motion.
        
            The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian mean motion in radians per second
        
        
        """
        ...
    def getKeplerianPeriod(self) -> _FieldOrbit__T:
        """
            Get the Keplerian period.
        
            The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian period in seconds, or positive infinity for hyperbolic orbits
        
        
        """
        ...
    def getLE(self) -> _FieldOrbit__T:
        """
            Get the eccentric longitude argument.
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldOrbit__T:
        """
            Get the mean longitude argument.
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldOrbit__T:
        """
            Get the true longitude argument.
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getMu(self) -> _FieldOrbit__T:
        """
            Get the central attraction coefficient used for position and velocity conversions (mÂ³/sÂ²).
        
            Returns:
                central attraction coefficient used for position and velocity conversions (mÂ³/sÂ²)
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldOrbit__T]: ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldOrbit__T]: ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbit__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldOrbit__T]: ...
    def getType(self) -> 'OrbitType':
        """
            Get the orbit type.
        
            Returns:
                orbit type
        
        
        """
        ...
    def hasDerivatives(self) -> bool:
        """
            Check if orbit includes derivatives.
        
            Returns:
                true if orbit includes derivatives
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot`, :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getHxDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLEDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLMDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot`, :meth:`~org.orekit.orbits.FieldOrbit.getIDot`
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, t: _FieldOrbit__T) -> 'FieldOrbit'[_FieldOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> _FieldOrbit__T: ...
    def toOrbit(self) -> 'Orbit':
        """
            Transforms the FieldOrbit instance into an Orbit instance.
        
            Returns:
                Orbit instance with same properties
        
        
        """
        ...

class LibrationOrbit:
    """
    public abstract class LibrationOrbit extends Object
    
        Base class for libration orbits.
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.orbits.HaloOrbit`, :class:`~org.orekit.orbits.LyapunovOrbit`
    """
    @typing.overload
    def applyDifferentialCorrection(self) -> None:
        """
            Apply differential correction.
        
            This will update :meth:`~org.orekit.orbits.LibrationOrbit.initialPV` and
            :meth:`~org.orekit.orbits.LibrationOrbit.orbitalPeriod` parameters.
        @Deprecated public void applyDifferentialCorrection(:class:`~org.orekit.attitudes.AttitudeProvider` attitudeProvider, :class:`~org.orekit.time.TimeScale` utc)
        
            Deprecated. as of 11.1, replaced by :meth:`~org.orekit.orbits.LibrationOrbit.applyDifferentialCorrection`
            Apply differential correction.
        
            This will update :meth:`~org.orekit.orbits.LibrationOrbit.initialPV` and
            :meth:`~org.orekit.orbits.LibrationOrbit.orbitalPeriod` parameters.
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the attitude law for the numerocal propagator
                utc (:class:`~org.orekit.time.TimeScale`): UTC time scale
        
        
        """
        ...
    @typing.overload
    def applyDifferentialCorrection(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider, timeScale: org.orekit.time.TimeScale) -> None: ...
    def getInitialPV(self) -> org.orekit.utils.PVCoordinates:
        """
            Return the initialPV on the libration orbit.
        
            This will return the exact initialPV only if you applied a prior differential correction. If you did not, you can use
            the method :meth:`~org.orekit.orbits.LibrationOrbit.applyCorrectionOnPV`
        
            Returns:
                initialPV initialPV on the libration orbit
        
        
        """
        ...
    def getManifolds(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> org.orekit.utils.PVCoordinates:
        """
            Return a manifold direction from one position on a libration Orbit.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpacecraftState with additional equations
                isStable (boolean): true if the manifold is stable
        
            Returns:
                manifold first guess Position-Velocity of a point on the libration Orbit
        
        
        """
        ...
    def getOrbitalPeriod(self) -> float:
        """
            Return the orbital period of the libration orbit.
        
            Returns:
                orbitalPeriod orbital period of the libration orbit
        
        
        """
        ...

class LibrationOrbitFamily(java.lang.Enum['LibrationOrbitFamily']):
    """
    public enum LibrationOrbitFamily extends Enum<:class:`~org.orekit.orbits.LibrationOrbitFamily`>
    
        Enumerate for :class:`~org.orekit.orbits.LibrationOrbit` family.
    
        The Northern and Southern families of Libration orbits are related to through symmetry.
    
        Since:
            10.2
    """
    NORTHERN: typing.ClassVar['LibrationOrbitFamily'] = ...
    SOUTHERN: typing.ClassVar['LibrationOrbitFamily'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LibrationOrbitFamily':
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
    def values() -> typing.List['LibrationOrbitFamily']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (LibrationOrbitFamily c : LibrationOrbitFamily.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LibrationOrbitType(java.lang.Enum['LibrationOrbitType']):
    """
    public enum LibrationOrbitType extends Enum<:class:`~org.orekit.orbits.LibrationOrbitType`>
    
        Enumerate for :class:`~org.orekit.orbits.LibrationOrbit` type.
    
        Since:
            10.2
    """
    HALO: typing.ClassVar['LibrationOrbitType'] = ...
    LYAPUNOV: typing.ClassVar['LibrationOrbitType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LibrationOrbitType':
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
    def values() -> typing.List['LibrationOrbitType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (LibrationOrbitType c : LibrationOrbitType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Orbit(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['Orbit'], org.orekit.time.TimeInterpolable['Orbit'], java.io.Serializable, org.orekit.utils.PVCoordinatesProvider):
    """
    public abstract class Orbit extends Object implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.orbits.Orbit`>, :class:`~org.orekit.time.TimeInterpolable`<:class:`~org.orekit.orbits.Orbit`>, Serializable, :class:`~org.orekit.utils.PVCoordinatesProvider`
    
        This class handles orbital parameters.
    
        For user convenience, both the Cartesian and the equinoctial elements are provided by this class, regardless of the
        canonical representation implemented in the derived class (which may be classical Keplerian elements for example).
    
        The parameters are defined in a frame specified by the user. It is important to make sure this frame is consistent: it
        probably is inertial and centered on the central body. This information is used for example by some force models.
    
        Instance of this class are guaranteed to be immutable.
    
        Also see:
            :meth:`~serialized`
    """
    def addKeplerContribution(self, positionAngle: 'PositionAngle', double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                semi-major axis derivative (m/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date of the orbital parameters
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                eccentricity derivative
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                first component of the equinoctial eccentricity vector
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                second component of the equinoctial eccentricity vector
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbital parameters are defined.
        
            Returns:
                frame in which the orbital parameters are defined
        
        
        """
        ...
    def getHx(self) -> float:
        """
            Get the first component of the inclination vector.
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                first component of the inclination vector derivative
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector.
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
            Get the second component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                second component of the inclination vector derivative
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get the inclination derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                inclination derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getJacobianWrtCartesian(self, positionAngle: 'PositionAngle', doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Compute the Jacobian of the orbital parameters with respect to the Cartesian parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of parameter i of the orbit with respect to Cartesian coordinate j.
            This means each row corresponds to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates
            x, y, z, xDot, yDot and zDot.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle to use
                jacobian (double[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                    corner will be modified
        
        
        """
        ...
    def getJacobianWrtParameters(self, positionAngle: 'PositionAngle', doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Compute the Jacobian of the Cartesian parameters with respect to the orbital parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of Cartesian coordinate i of the orbit with respect to orbital
            parameter j. This means each row corresponds to one Cartesian coordinate x, y, z, xdot, ydot, zdot whereas columns 0 to
            5 correspond to the orbital parameters.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle to use
                jacobian (double[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                    corner will be modified
        
        
        """
        ...
    def getKeplerianMeanMotion(self) -> float:
        """
            Get the Keplerian mean motion.
        
            The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian mean motion in radians per second
        
        
        """
        ...
    def getKeplerianPeriod(self) -> float:
        """
            Get the Keplerian period.
        
            The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian period in seconds, or positive infinity for hyperbolic orbits
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric longitude argument.
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument.
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true longitude argument.
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central acceleration constant.
        
            Returns:
                central acceleration constant
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.TimeStampedPVCoordinates` in definition frame.
        
            Returns:
                pvCoordinates in the definition frame
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.getPVCoordinates`
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.TimeStampedPVCoordinates` in a specified frame.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): frame in which the position/velocity coordinates shall be computed
        
            Returns:
                pvCoordinates in the specified output frame
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.getPVCoordinates`
        
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                otherDate (:class:`~org.orekit.time.AbsoluteDate`): current date
                otherFrame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def getType(self) -> 'OrbitType':
        """
            Get the orbit type.
        
            Returns:
                orbit type
        
        
        """
        ...
    def hasDerivatives(self) -> bool:
        """
            Check if orbit includes derivatives.
        
            Returns:
                true if orbit includes derivatives
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.getADot`, :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot`,
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot`, :meth:`~org.orekit.orbits.Orbit.getHxDot`,
                :meth:`~org.orekit.orbits.Orbit.getHyDot`, :meth:`~org.orekit.orbits.Orbit.getLEDot`,
                :meth:`~org.orekit.orbits.Orbit.getLvDot`, :meth:`~org.orekit.orbits.Orbit.getLMDot`,
                :meth:`~org.orekit.orbits.Orbit.getEDot`, :meth:`~org.orekit.orbits.Orbit.getIDot`
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'Orbit':
        """
            Get a time-shifted orbit.
        
            The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available
            in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available.
            Shifting is *not* intended as a replacement for proper orbit propagation but should be sufficient for small time shifts
            or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...

class OrbitType(java.lang.Enum['OrbitType']):
    """
    public enum OrbitType extends Enum<:class:`~org.orekit.orbits.OrbitType`>
    
        Enumerate for :class:`~org.orekit.orbits.Orbit` parameters types.
    """
    CARTESIAN: typing.ClassVar['OrbitType'] = ...
    CIRCULAR: typing.ClassVar['OrbitType'] = ...
    EQUINOCTIAL: typing.ClassVar['OrbitType'] = ...
    KEPLERIAN: typing.ClassVar['OrbitType'] = ...
    POS_X: typing.ClassVar[str] = ...
    """
    public static final String POS_X
    
        Name for position along X.
    
        Also see:
            :meth:`~constant`
    
    
    """
    POS_Y: typing.ClassVar[str] = ...
    """
    public static final String POS_Y
    
        Name for position along Y.
    
        Also see:
            :meth:`~constant`
    
    
    """
    POS_Z: typing.ClassVar[str] = ...
    """
    public static final String POS_Z
    
        Name for position along Z.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VEL_X: typing.ClassVar[str] = ...
    """
    public static final String VEL_X
    
        Name for velocity along X.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VEL_Y: typing.ClassVar[str] = ...
    """
    public static final String VEL_Y
    
        Name for velocity along Y.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VEL_Z: typing.ClassVar[str] = ...
    """
    public static final String VEL_Z
    
        Name for velocity along Z.
    
        Also see:
            :meth:`~constant`
    
    
    """
    A: typing.ClassVar[str] = ...
    """
    public static final String A
    
        Name for semi major axis.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC: typing.ClassVar[str] = ...
    """
    public static final String ECC
    
        Name for eccentricity.
    
        Also see:
            :meth:`~constant`
    
    
    """
    E_X: typing.ClassVar[str] = ...
    """
    public static final String E_X
    
        Name for eccentricity vector first component.
    
        Also see:
            :meth:`~constant`
    
    
    """
    E_Y: typing.ClassVar[str] = ...
    """
    public static final String E_Y
    
        Name for eccentricity vector second component.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INC: typing.ClassVar[str] = ...
    """
    public static final String INC
    
        Name for inclination.
    
        Also see:
            :meth:`~constant`
    
    
    """
    H_X: typing.ClassVar[str] = ...
    """
    public static final String H_X
    
        Name for inclination vector first component.
    
        Also see:
            :meth:`~constant`
    
    
    """
    H_Y: typing.ClassVar[str] = ...
    """
    public static final String H_Y
    
        Name for inclination vector second component .
    
        Also see:
            :meth:`~constant`
    
    
    """
    PA: typing.ClassVar[str] = ...
    """
    public static final String PA
    
        Name for perigee argument.
    
        Also see:
            :meth:`~constant`
    
    
    """
    RAAN: typing.ClassVar[str] = ...
    """
    public static final String RAAN
    
        Name for right ascension of ascending node.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN_ANOM: typing.ClassVar[str] = ...
    """
    public static final String MEAN_ANOM
    
        Name for mean anomaly.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC_ANOM: typing.ClassVar[str] = ...
    """
    public static final String ECC_ANOM
    
        Name for eccentric anomaly.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUE_ANOM: typing.ClassVar[str] = ...
    """
    public static final String TRUE_ANOM
    
        Name for mean anomaly.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN_LAT_ARG: typing.ClassVar[str] = ...
    """
    public static final String MEAN_LAT_ARG
    
        Name for mean argument of latitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC_LAT_ARG: typing.ClassVar[str] = ...
    """
    public static final String ECC_LAT_ARG
    
        Name for eccentric argument of latitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUE_LAT_ARG: typing.ClassVar[str] = ...
    """
    public static final String TRUE_LAT_ARG
    
        Name for mean argument of latitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN_LON_ARG: typing.ClassVar[str] = ...
    """
    public static final String MEAN_LON_ARG
    
        Name for mean argument of longitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC_LON_ARG: typing.ClassVar[str] = ...
    """
    public static final String ECC_LON_ARG
    
        Name for eccentric argument of longitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUE_LON_ARG: typing.ClassVar[str] = ...
    """
    public static final String TRUE_LON_ARG
    
        Name for mean argument of longitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    _convertType_0__T = typing.TypeVar('_convertType_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def convertType(self, fieldOrbit: FieldOrbit[_convertType_0__T]) -> FieldOrbit[_convertType_0__T]: ...
    @typing.overload
    def convertType(self, orbit: Orbit) -> Orbit:
        """
            Convert an orbit to the instance type.
        
            The returned orbit is the specified instance itself if its type already matches, otherwise, a new orbit of the proper
            type created
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to convert
        
            Returns:
                converted orbit with type guaranteed to match (so it can be cast safely)
        
        public abstract <T extends CalculusFieldElement<T>> :class:`~org.orekit.orbits.FieldOrbit`<T> convertType(:class:`~org.orekit.orbits.FieldOrbit`<T> orbit)
        
            Convert an orbit to the instance type.
        
            The returned orbit is the specified instance itself if its type already matches, otherwise, a new orbit of the proper
            type created
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): orbit to convert
        
            Returns:
                converted orbit with type guaranteed to match (so it can be cast safely)
        
        
        """
        ...
    def getDrivers(self, double: float, orbit: Orbit, positionAngle: 'PositionAngle') -> org.orekit.utils.ParameterDriversList:
        """
            Get parameters drivers initialized from a reference orbit.
        
            Parameters:
                dP (double): user specified position error
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                parameters drivers initialized from reference orbit
        
        
        """
        ...
    _mapArrayToOrbit_0__T = typing.TypeVar('_mapArrayToOrbit_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mapArrayToOrbit(self, tArray: typing.List[_mapArrayToOrbit_0__T], tArray2: typing.List[_mapArrayToOrbit_0__T], positionAngle: 'PositionAngle', fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mapArrayToOrbit_0__T], t3: _mapArrayToOrbit_0__T, frame: org.orekit.frames.Frame) -> FieldOrbit[_mapArrayToOrbit_0__T]: ...
    @typing.overload
    def mapArrayToOrbit(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], positionAngle: 'PositionAngle', absoluteDate: org.orekit.time.AbsoluteDate, double3: float, frame: org.orekit.frames.Frame) -> Orbit:
        """
            Convert state array to orbital parameters.
        
            Note that all implementations of this method *must* be consistent with the implementation of the null method for the
            corresponding orbit type in terms of parameters order and meaning.
        
            Parameters:
                array (double[]): state as a flat array (it can have more than 6 elements, extra elements are ignored)
                arrayDot (double[]): state derivative as a flat array (it can be null, in which case Keplerian motion is assumed, and it can have more than 6
                    elements, extra elements are ignored)
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
                date (:class:`~org.orekit.time.AbsoluteDate`): integration date
                mu (double): central attraction coefficient used for propagation (mÂ³/sÂ²)
                frame (:class:`~org.orekit.frames.Frame`): frame in which integration is performed
        
            Returns:
                orbit corresponding to the flat array as a space dynamics object
        
        public abstract <T extends CalculusFieldElement<T>> :class:`~org.orekit.orbits.FieldOrbit`<T> mapArrayToOrbit(T[] array, T[] arrayDot, :class:`~org.orekit.orbits.PositionAngle` type, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date, T mu, :class:`~org.orekit.frames.Frame` frame)
        
            Convert state array to orbital parameters.
        
            Note that all implementations of this method *must* be consistent with the implementation of the null method for the
            corresponding orbit type in terms of parameters order and meaning.
        
            Parameters:
                array (T[]): state as a flat array (it can have more than 6 elements, extra elements are ignored)
                arrayDot (T[]): state derivative as a flat array (it can be null, in which case Keplerian motion is assumed,
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): integration date
                mu (T): central attraction coefficient used for propagation (mÂ³/sÂ²)
                frame (:class:`~org.orekit.frames.Frame`): frame in which integration is performed
        
            Returns:
                orbit corresponding to the flat array as a space dynamics object
        
        
        """
        ...
    _mapOrbitToArray_0__T = typing.TypeVar('_mapOrbitToArray_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mapOrbitToArray(self, fieldOrbit: FieldOrbit[_mapOrbitToArray_0__T], positionAngle: 'PositionAngle', tArray: typing.List[_mapOrbitToArray_0__T], tArray2: typing.List[_mapOrbitToArray_0__T]) -> None: ...
    @typing.overload
    def mapOrbitToArray(self, orbit: Orbit, positionAngle: 'PositionAngle', doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None:
        """
            Convert orbit to state array.
        
            Note that all implementations of this method *must* be consistent with the implementation of the null method for the
            corresponding orbit type in terms of parameters order and meaning.
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to map
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
                stateVector (double[]):             flat array into which the state vector should be mapped (it can have more than 6 elements, extra elements are untouched)
                stateVectorDot (double[]): flat array into which the state vector derivative should be mapped (it can be null if derivatives are not desired, and
                    it can have more than 6 elements, extra elements are untouched)
        
        public abstract <T extends CalculusFieldElement<T>> void mapOrbitToArray(:class:`~org.orekit.orbits.FieldOrbit`<T> orbit, :class:`~org.orekit.orbits.PositionAngle` type, T[] stateVector, T[] stateVectorDot)
        
            Convert orbit to state array.
        
            Note that all implementations of this method *must* be consistent with the implementation of the null method for the
            corresponding orbit type in terms of parameters order and meaning.
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): orbit to map
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
                stateVector (T[]):             flat array into which the state vector should be mapped (it can have more than 6 elements, extra elements are untouched)
                stateVectorDot (T[]): flat array into which the state vector derivative should be mapped (it can be null if derivatives are not desired, and
                    it can have more than 6 elements, extra elements are untouched)
        
        
        """
        ...
    _normalize_0__T = typing.TypeVar('_normalize_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def normalize(self, fieldOrbit: FieldOrbit[_normalize_0__T], fieldOrbit2: FieldOrbit[_normalize_0__T]) -> FieldOrbit[_normalize_0__T]: ...
    @typing.overload
    def normalize(self, orbit: Orbit, orbit2: Orbit) -> Orbit:
        """
            Normalize one orbit with respect to a reference one.
        
            Given a, angular component ÃŽÂ¶ of an orbit and the corresponding angular component ÃŽÂ¶Ã¡ÂµÂ£ in the reference orbit,
            the angular component ÃŽÂ¶Ã¢â€šâ„¢ of the normalized orbit will be ÃŽÂ¶Ã¢â€šâ„¢ = ÃŽÂ¶ + 2kÃ�â‚¬ where k is chosen such
            that ÃŽÂ¶Ã¡ÂµÂ£ - Ã�â‚¬ Ã¢â€°Â¤ ÃŽÂ¶Ã¢â€šâ„¢ Ã¢â€°Â¤ ÃŽÂ¶Ã¡ÂµÂ£ + Ã�â‚¬. This is intended to avoid too large
            discontinuities and is particularly useful for normalizing the orbit after an impulsive maneuver with respect to the
            reference picked up before the maneuver.
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to normalize
                reference (:class:`~org.orekit.orbits.Orbit`): reference orbit
        
            Returns:
                normalized orbit (the type is guaranteed to match :class:`~org.orekit.orbits.OrbitType`)
        
            Since:
                11.1
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OrbitType':
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
    def values() -> typing.List['OrbitType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (OrbitType c : OrbitType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PositionAngle(java.lang.Enum['PositionAngle']):
    """
    public enum PositionAngle extends Enum<:class:`~org.orekit.orbits.PositionAngle`>
    
        Enumerate for true, eccentric and mean position angles.
    
        Also see:
            :class:`~org.orekit.orbits.KeplerianOrbit`, :class:`~org.orekit.orbits.CircularOrbit`,
            :class:`~org.orekit.orbits.EquinoctialOrbit`
    """
    MEAN: typing.ClassVar['PositionAngle'] = ...
    ECCENTRIC: typing.ClassVar['PositionAngle'] = ...
    TRUE: typing.ClassVar['PositionAngle'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PositionAngle':
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
    def values() -> typing.List['PositionAngle']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            
            for (PositionAngle c : PositionAngle.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RichardsonExpansion:
    """
    public class RichardsonExpansion extends Object
    
        Class implementing the Third-Order Richardson Expansion.
    
        Since:
            10.2
    
        Also see:
            "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem, lagrangianPoints: org.orekit.utils.LagrangianPoints): ...
    def computeHaloFirstGuess(self, double: float, librationOrbitFamily: LibrationOrbitFamily, double2: float, double3: float) -> org.orekit.utils.PVCoordinates:
        """
            Calculate first Guess.
        
            Parameters:
                azr (double): z-axis Amplitude of the required Halo Orbit, meters
                type (:class:`~org.orekit.orbits.LibrationOrbitFamily`): type of the Halo Orbit ("Northern" or "Southern")
                t (double): Orbit time, seconds (must be greater than 0)
                phi (double): Orbit phase, rad
        
            Returns:
                firstGuess PVCoordinates of the first guess
        
        
        """
        ...
    def computeLyapunovFirstGuess(self, double: float, double2: float, double3: float) -> org.orekit.utils.PVCoordinates:
        """
            Calculate first Guess.
        
            Parameters:
                ayr (double): x-axis Amplitude of the required Lyapunov Orbit, meters
                t (double): time
                phi (double): Orbit phase, rad
        
            Returns:
                firstGuess PVCoordinates of the first guess
        
        
        """
        ...
    def getCr3bpSystem(self) -> org.orekit.bodies.CR3BPSystem:
        """
            Get the considered CR3BP system.
        
            Returns:
                CRR3BP system
        
        
        """
        ...
    def getHaloOrbitalPeriod(self, double: float) -> float:
        """
            Return the orbital period of the Halo Orbit.
        
            Parameters:
                azr (double): z-axis Amplitude of the required Halo Orbit, meters
        
            Returns:
                the orbitalPeriod
        
        
        """
        ...
    def getLagrangianPoint(self) -> org.orekit.utils.LagrangianPoints:
        """
            Get the considered lagrangian point.
        
            Returns:
                lagrangian point
        
        
        """
        ...
    def getLyapunovOrbitalPeriod(self, double: float) -> float:
        """
            Return the orbital period of the Halo Orbit.
        
            Parameters:
                axr (double): x-axis Amplitude of the required Lyapunov Orbit, meters
        
            Returns:
                the orbitalPeriod
        
        
        """
        ...

class CartesianOrbit(Orbit):
    """
    public class CartesianOrbit extends :class:`~org.orekit.orbits.Orbit`
    
        This class holds Cartesian orbital parameters.
    
        The parameters used internally are the Cartesian coordinates:
    
          - x
          - y
          - z
          - xDot
          - yDot
          - zDot
    
        contained in :class:`~org.orekit.utils.PVCoordinates`.
    
        Note that the implementation of this class delegates all non-Cartesian related computations
        (:meth:`~org.orekit.orbits.CartesianOrbit.getA`, :meth:`~org.orekit.orbits.CartesianOrbit.getEquinoctialEx`, ...) to an
        underlying instance of the :class:`~org.orekit.orbits.EquinoctialOrbit` class. This implies that using this class only
        for analytical computations which are always based on non-Cartesian parameters is perfectly possible but somewhat
        sub-optimal.
    
        The instance :code:`CartesianOrbit` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CircularOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getA` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHx(self) -> float:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHxDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
            Get the second component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getI` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get the inclination derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getIDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLM` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLv` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getType` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    def hasDerivatives(self) -> bool:
        """
            Check if orbit includes derivatives.
        
            Overrides:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                true if orbit includes derivatives
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.getADot`, :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot`,
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot`, :meth:`~org.orekit.orbits.Orbit.getHxDot`,
                :meth:`~org.orekit.orbits.Orbit.getHyDot`, :meth:`~org.orekit.orbits.Orbit.getLEDot`,
                :meth:`~org.orekit.orbits.Orbit.getLvDot`, :meth:`~org.orekit.orbits.Orbit.getLMDot`,
                :meth:`~org.orekit.orbits.Orbit.getEDot`, :meth:`~org.orekit.orbits.Orbit.getIDot`
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[Orbit]) -> 'CartesianOrbit': ...
    def shiftedBy(self, double: float) -> 'CartesianOrbit':
        """
            Get a time-shifted orbit.
        
            The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available
            in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available.
            Shifting is *not* intended as a replacement for proper orbit propagation but should be sufficient for small time shifts
            or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.shiftedBy` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this Orbit object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...

class CircularOrbit(Orbit):
    """
    public class CircularOrbit extends :class:`~org.orekit.orbits.Orbit`
    
        This class handles circular orbital parameters.
    
        The parameters used internally are the circular elements which can be related to Keplerian elements as follows:
    
          - a
          - e :sub:`x` = e cos(Ï‰)
          - e :sub:`y` = e sin(Ï‰)
          - i
          - Î©
          - Î± :sub:`v` = v + Ï‰
    
        where Î© stands for the Right Ascension of the Ascending Node and Î± :sub:`v` stands for the true latitude argument
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is circular (but not equatorial), the circular parameters
        are still unambiguously defined whereas some Keplerian elements (more precisely Ã�â€° and ÃŽÂ©) become ambiguous. When
        orbit is equatorial, neither the Keplerian nor the circular parameters can be defined unambiguously.
        :class:`~org.orekit.orbits.EquinoctialOrbit` is the recommended way to represent orbits.
    
        The instance :code:`CircularOrbit` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(double: float, double2: float, double3: float) -> float:
        """
            Computes the mean latitude argument from the eccentric latitude argument.
        
            Parameters:
                alphaE (double): = E + Ï‰ mean latitude argument (rad)
                ex (double): e cos(Ï‰), first component of circular eccentricity vector
                ey (double): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the mean latitude argument.
        
        
        """
        ...
    @staticmethod
    def eccentricToTrue(double: float, double2: float, double3: float) -> float:
        """
            Computes the true latitude argument from the eccentric latitude argument.
        
            Parameters:
                alphaE (double): = E + Ï‰ eccentric latitude argument (rad)
                ex (double): e cos(Ï‰), first component of circular eccentricity vector
                ey (double): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the true latitude argument.
        
        
        """
        ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getA` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getAlpha(self, positionAngle: PositionAngle) -> float:
        """
            Get the latitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                latitude argument (rad)
        
        
        """
        ...
    def getAlphaDot(self, positionAngle: PositionAngle) -> float:
        """
            Get the latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                latitude argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getAlphaE(self) -> float:
        """
            Get the eccentric latitude argument.
        
            Returns:
                E + Ï‰ eccentric latitude argument (rad)
        
        
        """
        ...
    def getAlphaEDot(self) -> float:
        """
            Get the eccentric latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(E + Ï‰)/dt eccentric latitude argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getAlphaM(self) -> float:
        """
            Get the mean latitude argument.
        
            Returns:
                M + Ï‰ mean latitude argument (rad)
        
        
        """
        ...
    def getAlphaMDot(self) -> float:
        """
            Get the mean latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(M + Ï‰)/dt mean latitude argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getAlphaV(self) -> float:
        """
            Get the true latitude argument.
        
            Returns:
                v + Ï‰ true latitude argument (rad)
        
        
        """
        ...
    def getAlphaVDot(self) -> float:
        """
            Get the true latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                v + Ï‰ true latitude argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getCircularEx(self) -> float:
        """
            Get the first component of the circular eccentricity vector.
        
            Returns:
                ex = e cos(Ï‰), first component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularExDot(self) -> float:
        """
            Get the first component of the circular eccentricity vector derivative.
        
            Returns:
                ex = e cos(Ï‰), first component of the circular eccentricity vector derivative
        
            Since:
                9.0
        
        
        """
        ...
    def getCircularEy(self) -> float:
        """
            Get the second component of the circular eccentricity vector.
        
            Returns:
                ey = e sin(Ï‰), second component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularEyDot(self) -> float:
        """
            Get the second component of the circular eccentricity vector derivative.
        
            Returns:
                ey = e sin(Ï‰), second component of the circular eccentricity vector derivative
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHx(self) -> float:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHxDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
            Get the second component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getI` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get the inclination derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getIDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLM` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLv` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getRightAscensionOfAscendingNode(self) -> float:
        """
            Get the right ascension of the ascending node.
        
            Returns:
                right ascension of the ascending node (rad)
        
        
        """
        ...
    def getRightAscensionOfAscendingNodeDot(self) -> float:
        """
            Get the right ascension of the ascending node derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                right ascension of the ascending node derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getType` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[Orbit]) -> 'CircularOrbit': ...
    @staticmethod
    def meanToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric latitude argument from the mean latitude argument.
        
            Parameters:
                alphaM (double): = M + Ï‰ mean latitude argument (rad)
                ex (double): e cos(Ï‰), first component of circular eccentricity vector
                ey (double): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'CircularOrbit':
        """
            Get a time-shifted orbit.
        
            The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available
            in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available.
            Shifting is *not* intended as a replacement for proper orbit propagation but should be sufficient for small time shifts
            or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.shiftedBy` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this Orbit object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    @staticmethod
    def trueToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric latitude argument from the true latitude argument.
        
            Parameters:
                alphaV (double): = V + Ï‰ true latitude argument (rad)
                ex (double): e cos(Ï‰), first component of circular eccentricity vector
                ey (double): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...

class EquinoctialOrbit(Orbit):
    """
    public class EquinoctialOrbit extends :class:`~org.orekit.orbits.Orbit`
    
        This class handles equinoctial orbital parameters, which can support both circular and equatorial orbits.
    
        The parameters used internally are the equinoctial elements which can be related to Keplerian elements as follows:
    
        .. code-block: java
        
        
             a
             ex = e cos(Ï‰ + Î©)
             ey = e sin(Ï‰ + Î©)
             hx = tan(i/2) cos(Î©)
             hy = tan(i/2) sin(Î©)
             lv = v + Ï‰ + Î©
           
        where Ï‰ stands for the Perigee Argument and Î© stands for the Right Ascension of the Ascending Node.
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is either equatorial or circular, the equinoctial
        parameters are still unambiguously defined whereas some Keplerian elements (more precisely Ã�â€° and ÃŽÂ©) become
        ambiguous. For this reason, equinoctial parameters are the recommended way to represent orbits.
    
        The instance :code:`EquinoctialOrbit` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CircularOrbit`, :class:`~org.orekit.orbits.CartesianOrbit`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(double: float, double2: float, double3: float) -> float:
        """
            Computes the mean longitude argument from the eccentric longitude argument.
        
            Parameters:
                lE (double): = E + Ï‰ + Î© mean longitude argument (rad)
                ex (double): first component of the eccentricity vector
                ey (double): second component of the eccentricity vector
        
            Returns:
                the mean longitude argument
        
        
        """
        ...
    @staticmethod
    def eccentricToTrue(double: float, double2: float, double3: float) -> float:
        """
            Computes the true longitude argument from the eccentric longitude argument.
        
            Parameters:
                lE (double): = E + Ï‰ + Î© eccentric longitude argument (rad)
                ex (double): first component of the eccentricity vector
                ey (double): second component of the eccentricity vector
        
            Returns:
                the true longitude argument
        
        
        """
        ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getA` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHx(self) -> float:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHxDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
            Get the second component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getI` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get the inclination derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getIDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getL(self, positionAngle: PositionAngle) -> float:
        """
            Get the longitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                longitude argument (rad)
        
        
        """
        ...
    def getLDot(self, positionAngle: PositionAngle) -> float:
        """
            Get the longitude argument derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLM` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLv` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getType` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[Orbit]) -> 'EquinoctialOrbit': ...
    @staticmethod
    def meanToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric longitude argument from the mean longitude argument.
        
            Parameters:
                lM (double): = M + Ï‰ + Î© mean longitude argument (rad)
                ex (double): first component of the eccentricity vector
                ey (double): second component of the eccentricity vector
        
            Returns:
                the eccentric longitude argument
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'EquinoctialOrbit':
        """
            Get a time-shifted orbit.
        
            The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available
            in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available.
            Shifting is *not* intended as a replacement for proper orbit propagation but should be sufficient for small time shifts
            or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.shiftedBy` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this equinoctial parameters object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    @staticmethod
    def trueToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric longitude argument from the true longitude argument.
        
            Parameters:
                lv (double): = v + Ï‰ + Î© true longitude argument (rad)
                ex (double): first component of the eccentricity vector
                ey (double): second component of the eccentricity vector
        
            Returns:
                the eccentric longitude argument
        
        
        """
        ...

_FieldCartesianOrbit__T = typing.TypeVar('_FieldCartesianOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianOrbit(FieldOrbit[_FieldCartesianOrbit__T], typing.Generic[_FieldCartesianOrbit__T]):
    """
    public class FieldCartesianOrbit<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T>
    
        This class holds Cartesian orbital parameters.
    
        The parameters used internally are the Cartesian coordinates:
    
          - x
          - y
          - z
          - xDot
          - yDot
          - zDot
    
        contained in :class:`~org.orekit.utils.PVCoordinates`.
    
        Note that the implementation of this class delegates all non-Cartesian related computations
        (:meth:`~org.orekit.orbits.FieldCartesianOrbit.getA`, :meth:`~org.orekit.orbits.FieldCartesianOrbit.getEquinoctialEx`,
        ...) to an underlying instance of the :class:`~org.orekit.orbits.EquinoctialOrbit` class. This implies that using this
        class only for analytical computations which are always based on non-Cartesian parameters is perfectly possible but
        somewhat sub-optimal.
    
        The instance :code:`CartesianOrbit` is guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CircularOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`
    """
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldCartesianOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldCartesianOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCartesianOrbit__T], t: _FieldCartesianOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldCartesianOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldCartesianOrbit__T): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, t: _FieldCartesianOrbit__T, tArray: typing.List[_FieldCartesianOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldCartesianOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldCartesianOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> _FieldCartesianOrbit__T:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getA` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldCartesianOrbit__T:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
        
        """
        ...
    def getE(self) -> _FieldCartesianOrbit__T:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldCartesianOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldCartesianOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getHx(self) -> _FieldCartesianOrbit__T:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHxDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldCartesianOrbit__T:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the second component of the inclination vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldCartesianOrbit__T:
        """
            Get the inclination.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getI` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the inclination derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getIDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldCartesianOrbit__T:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldCartesianOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldCartesianOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getType` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    def hasDerivatives(self) -> bool:
        """
            Check if orbit includes derivatives.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.hasDerivatives` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                true if orbit includes derivatives
        
            Also see:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot`, :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getHxDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLEDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLMDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot`, :meth:`~org.orekit.orbits.FieldOrbit.getIDot`
        
        
        """
        ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], collection: typing.Union[java.util.Collection[_FieldCartesianOrbit__T], typing.Sequence[_FieldCartesianOrbit__T], typing.Set[_FieldCartesianOrbit__T]]) -> _FieldCartesianOrbit__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCartesianOrbit__T], stream: java.util.stream.Stream[FieldOrbit[_FieldCartesianOrbit__T]]) -> 'FieldCartesianOrbit'[_FieldCartesianOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldCartesianOrbit'[_FieldCartesianOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldCartesianOrbit__T) -> 'FieldCartesianOrbit'[_FieldCartesianOrbit__T]: ...
    def toOrbit(self) -> CartesianOrbit:
        """
            Description copied from class: :meth:`~org.orekit.orbits.FieldOrbit.toOrbit`
            Transforms the FieldOrbit instance into an Orbit instance.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.toOrbit` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this Orbit object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...

_FieldCircularOrbit__T = typing.TypeVar('_FieldCircularOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCircularOrbit(FieldOrbit[_FieldCircularOrbit__T], typing.Generic[_FieldCircularOrbit__T]):
    """
    public class FieldCircularOrbit<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T>
    
        This class handles circular orbital parameters.
    
        The parameters used internally are the circular elements which can be related to Keplerian elements as follows:
    
          - a
          - e :sub:`x` = e cos(Ï‰)
          - e :sub:`y` = e sin(Ï‰)
          - i
          - Î©
          - Î± :sub:`v` = v + Ï‰
    
        where Î© stands for the Right Ascension of the Ascending Node and Î± :sub:`v` stands for the true latitude argument
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is circular (but not equatorial), the circular parameters
        are still unambiguously defined whereas some Keplerian elements (more precisely Ã�â€° and ÃŽÂ©) become ambiguous. When
        orbit is equatorial, neither the Keplerian nor the circular parameters can be defined unambiguously.
        :class:`~org.orekit.orbits.EquinoctialOrbit` is the recommended way to represent orbits.
    
        The instance :code:`CircularOrbit` is guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`
    """
    @typing.overload
    def __init__(self, t: _FieldCircularOrbit__T, t2: _FieldCircularOrbit__T, t3: _FieldCircularOrbit__T, t4: _FieldCircularOrbit__T, t5: _FieldCircularOrbit__T, t6: _FieldCircularOrbit__T, t7: _FieldCircularOrbit__T, t8: _FieldCircularOrbit__T, t9: _FieldCircularOrbit__T, t10: _FieldCircularOrbit__T, t11: _FieldCircularOrbit__T, t12: _FieldCircularOrbit__T, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t13: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldCircularOrbit__T, t2: _FieldCircularOrbit__T, t3: _FieldCircularOrbit__T, t4: _FieldCircularOrbit__T, t5: _FieldCircularOrbit__T, t6: _FieldCircularOrbit__T, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t7: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldCircularOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldCircularOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldCircularOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldCircularOrbit__T): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, t: _FieldCircularOrbit__T, tArray: typing.List[_FieldCircularOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldCircularOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldCircularOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(t: _eccentricToMean__T, t2: _eccentricToMean__T, t3: _eccentricToMean__T) -> _eccentricToMean__T:
        """
            Computes the mean latitude argument from the eccentric latitude argument.
        
            Parameters:
                alphaE (T): = E + Ï‰ eccentric latitude argument (rad)
                ex (T): e cos(Ï‰), first component of circular eccentricity vector
                ey (T): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the mean latitude argument.
        
        
        """
        ...
    _eccentricToTrue__T = typing.TypeVar('_eccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToTrue(t: _eccentricToTrue__T, t2: _eccentricToTrue__T, t3: _eccentricToTrue__T) -> _eccentricToTrue__T:
        """
            Computes the true latitude argument from the eccentric latitude argument.
        
            Parameters:
                alphaE (T): = E + Ï‰ eccentric latitude argument (rad)
                ex (T): e cos(Ï‰), first component of circular eccentricity vector
                ey (T): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the true latitude argument.
        
        
        """
        ...
    def getA(self) -> _FieldCircularOrbit__T:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getA` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldCircularOrbit__T:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
        
        """
        ...
    def getAlpha(self, positionAngle: PositionAngle) -> _FieldCircularOrbit__T:
        """
            Get the latitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                latitude argument (rad)
        
        
        """
        ...
    def getAlphaDot(self, positionAngle: PositionAngle) -> _FieldCircularOrbit__T:
        """
            Get the latitude argument derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                latitude argument derivative (rad/s)
        
        
        """
        ...
    def getAlphaE(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentric latitude argument.
        
            Returns:
                E + Ï‰ eccentric latitude argument (rad)
        
        
        """
        ...
    def getAlphaEDot(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentric latitude argument derivative.
        
            Returns:
                d(E + Ï‰)/dt eccentric latitude argument derivative (rad/s)
        
        
        """
        ...
    def getAlphaM(self) -> _FieldCircularOrbit__T:
        """
            Get the mean latitude argument.
        
            Returns:
                M + Ï‰ mean latitude argument (rad)
        
        
        """
        ...
    def getAlphaMDot(self) -> _FieldCircularOrbit__T:
        """
            Get the mean latitude argument derivative.
        
            Returns:
                d(M + Ï‰)/dt mean latitude argument derivative (rad/s)
        
        
        """
        ...
    def getAlphaV(self) -> _FieldCircularOrbit__T:
        """
            Get the true latitude argument.
        
            Returns:
                v + Ï‰ true latitude argument (rad)
        
        
        """
        ...
    def getAlphaVDot(self) -> _FieldCircularOrbit__T:
        """
            Get the true latitude argument derivative.
        
            Returns:
                d(v + Ï‰)/dt true latitude argument derivative (rad/s)
        
        
        """
        ...
    def getCircularEx(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the circular eccentricity vector.
        
            Returns:
                ex = e cos(Ï‰), first component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularExDot(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the circular eccentricity vector derivative.
        
            Returns:
                d(ex)/dt = d(e cos(Ï‰))/dt, first component of the circular eccentricity vector derivative
        
        
        """
        ...
    def getCircularEy(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the circular eccentricity vector.
        
            Returns:
                ey = e sin(Ï‰), second component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularEyDot(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the circular eccentricity vector derivative.
        
            Returns:
                d(ey)/dt = d(e sin(Ï‰))/dt, second component of the circular eccentricity vector derivative
        
        
        """
        ...
    def getE(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getHx(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHxDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the inclination vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldCircularOrbit__T:
        """
            Get the inclination.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getI` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldCircularOrbit__T:
        """
            Get the inclination derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getIDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldCircularOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldCircularOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldCircularOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldCircularOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getRightAscensionOfAscendingNode(self) -> _FieldCircularOrbit__T:
        """
            Get the right ascension of the ascending node.
        
            Returns:
                right ascension of the ascending node (rad)
        
        
        """
        ...
    def getRightAscensionOfAscendingNodeDot(self) -> _FieldCircularOrbit__T:
        """
            Get the right ascension of the ascending node derivative.
        
            Returns:
                right ascension of the ascending node derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getType` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    def hasDerivatives(self) -> bool:
        """
            Check if orbit includes derivatives.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.hasDerivatives` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                true if orbit includes derivatives
        
            Also see:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot`, :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getHxDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLEDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLMDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot`, :meth:`~org.orekit.orbits.FieldOrbit.getIDot`
        
        
        """
        ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], collection: typing.Union[java.util.Collection[_FieldCircularOrbit__T], typing.Sequence[_FieldCircularOrbit__T], typing.Set[_FieldCircularOrbit__T]]) -> _FieldCircularOrbit__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], stream: java.util.stream.Stream[FieldOrbit[_FieldCircularOrbit__T]]) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]: ...
    _meanToEccentric__T = typing.TypeVar('_meanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToEccentric(t: _meanToEccentric__T, t2: _meanToEccentric__T, t3: _meanToEccentric__T) -> _meanToEccentric__T:
        """
            Computes the eccentric latitude argument from the mean latitude argument.
        
            Parameters:
                alphaM (T): = M + Ï‰ mean latitude argument (rad)
                ex (T): e cos(Ï‰), first component of circular eccentricity vector
                ey (T): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldCircularOrbit__T) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]: ...
    def toOrbit(self) -> CircularOrbit:
        """
            Transforms the FieldOrbit instance into an Orbit instance.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.toOrbit` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this Orbit object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    _trueToEccentric__T = typing.TypeVar('_trueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToEccentric(t: _trueToEccentric__T, t2: _trueToEccentric__T, t3: _trueToEccentric__T) -> _trueToEccentric__T:
        """
            Computes the eccentric latitude argument from the true latitude argument.
        
            Parameters:
                alphaV (T): = v + Ï‰ true latitude argument (rad)
                ex (T): e cos(Ï‰), first component of circular eccentricity vector
                ey (T): e sin(Ï‰), second component of circular eccentricity vector
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...

_FieldEquinoctialOrbit__T = typing.TypeVar('_FieldEquinoctialOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEquinoctialOrbit(FieldOrbit[_FieldEquinoctialOrbit__T], typing.Generic[_FieldEquinoctialOrbit__T]):
    """
    public class FieldEquinoctialOrbit<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T>
    
        This class handles equinoctial orbital parameters, which can support both circular and equatorial orbits.
    
        The parameters used internally are the equinoctial elements which can be related to Keplerian elements as follows:
    
        .. code-block: java
        
        
             a
             ex = e cos(Ï‰ + Î©)
             ey = e sin(Ï‰ + Î©)
             hx = tan(i/2) cos(Î©)
             hy = tan(i/2) sin(Î©)
             lv = v + Ï‰ + Î©
           
        where Ï‰ stands for the Perigee Argument and Î© stands for the Right Ascension of the Ascending Node.
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is either equatorial or circular, the equinoctial
        parameters are still unambiguously defined whereas some Keplerian elements (more precisely Ã�â€° and ÃŽÂ©) become
        ambiguous. For this reason, equinoctial parameters are the recommended way to represent orbits.
    
        The instance :code:`EquinoctialOrbit` is guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CircularOrbit`, :class:`~org.orekit.orbits.CartesianOrbit`
    """
    @typing.overload
    def __init__(self, t: _FieldEquinoctialOrbit__T, t2: _FieldEquinoctialOrbit__T, t3: _FieldEquinoctialOrbit__T, t4: _FieldEquinoctialOrbit__T, t5: _FieldEquinoctialOrbit__T, t6: _FieldEquinoctialOrbit__T, t7: _FieldEquinoctialOrbit__T, t8: _FieldEquinoctialOrbit__T, t9: _FieldEquinoctialOrbit__T, t10: _FieldEquinoctialOrbit__T, t11: _FieldEquinoctialOrbit__T, t12: _FieldEquinoctialOrbit__T, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t13: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldEquinoctialOrbit__T, t2: _FieldEquinoctialOrbit__T, t3: _FieldEquinoctialOrbit__T, t4: _FieldEquinoctialOrbit__T, t5: _FieldEquinoctialOrbit__T, t6: _FieldEquinoctialOrbit__T, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t7: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldEquinoctialOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldEquinoctialOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldEquinoctialOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldEquinoctialOrbit__T): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, t: _FieldEquinoctialOrbit__T, tArray: typing.List[_FieldEquinoctialOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldEquinoctialOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldEquinoctialOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(t: _eccentricToMean__T, t2: _eccentricToMean__T, t3: _eccentricToMean__T) -> _eccentricToMean__T:
        """
            Computes the mean longitude argument from the eccentric longitude argument.
        
            Parameters:
                lE (T): = E + Ï‰ + Î© mean longitude argument (rad)
                ex (T): first component of the eccentricity vector
                ey (T): second component of the eccentricity vector
        
            Returns:
                the mean longitude argument
        
        
        """
        ...
    _eccentricToTrue__T = typing.TypeVar('_eccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToTrue(t: _eccentricToTrue__T, t2: _eccentricToTrue__T, t3: _eccentricToTrue__T) -> _eccentricToTrue__T:
        """
            Computes the true longitude argument from the eccentric longitude argument.
        
            Parameters:
                lE (T): = E + Ï‰ + Î© eccentric longitude argument (rad)
                ex (T): first component of the eccentricity vector
                ey (T): second component of the eccentricity vector
        
            Returns:
                the true longitude argument
        
        
        """
        ...
    def getA(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getA` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
        
        """
        ...
    def getE(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getHx(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHxDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the second component of the inclination vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the inclination.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getI` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the inclination derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getIDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination derivative (rad/s)
        
        
        """
        ...
    def getL(self, positionAngle: PositionAngle) -> _FieldEquinoctialOrbit__T:
        """
            Get the longitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                longitude argument (rad)
        
        
        """
        ...
    def getLDot(self, positionAngle: PositionAngle) -> _FieldEquinoctialOrbit__T:
        """
            Get the longitude argument derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getType` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    def hasDerivatives(self) -> bool:
        """
            Check if orbit includes derivatives.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.hasDerivatives` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                true if orbit includes derivatives
        
            Also see:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot`, :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getHxDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLEDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLMDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot`, :meth:`~org.orekit.orbits.FieldOrbit.getIDot`
        
        
        """
        ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], collection: typing.Union[java.util.Collection[_FieldEquinoctialOrbit__T], typing.Sequence[_FieldEquinoctialOrbit__T], typing.Set[_FieldEquinoctialOrbit__T]]) -> _FieldEquinoctialOrbit__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], stream: java.util.stream.Stream[FieldOrbit[_FieldEquinoctialOrbit__T]]) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]: ...
    _meanToEccentric__T = typing.TypeVar('_meanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToEccentric(t: _meanToEccentric__T, t2: _meanToEccentric__T, t3: _meanToEccentric__T) -> _meanToEccentric__T:
        """
            Computes the eccentric longitude argument from the mean longitude argument.
        
            Parameters:
                lM (T): = M + Ï‰ + Î© mean longitude argument (rad)
                ex (T): first component of the eccentricity vector
                ey (T): second component of the eccentricity vector
        
            Returns:
                the eccentric longitude argument
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldEquinoctialOrbit__T) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]: ...
    def toOrbit(self) -> EquinoctialOrbit:
        """
            Transforms the FieldOrbit instance into an Orbit instance.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.toOrbit` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this equinoctial parameters object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    _trueToEccentric__T = typing.TypeVar('_trueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToEccentric(t: _trueToEccentric__T, t2: _trueToEccentric__T, t3: _trueToEccentric__T) -> _trueToEccentric__T:
        """
            Computes the eccentric longitude argument from the true longitude argument.
        
            Parameters:
                lv (T): = v + Ï‰ + Î© true longitude argument (rad)
                ex (T): first component of the eccentricity vector
                ey (T): second component of the eccentricity vector
        
            Returns:
                the eccentric longitude argument
        
        
        """
        ...

_FieldKeplerianOrbit__T = typing.TypeVar('_FieldKeplerianOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldKeplerianOrbit(FieldOrbit[_FieldKeplerianOrbit__T], typing.Generic[_FieldKeplerianOrbit__T]):
    """
    public class FieldKeplerianOrbit<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T>
    
        This class handles traditional Keplerian orbital parameters.
    
        The parameters used internally are the classical Keplerian elements:
    
        .. code-block: java
        
        
             a
             e
             i
             Ï‰
             Î©
             v
           
        where Ã�â€° stands for the Perigee Argument, ÃŽÂ© stands for the Right Ascension of the Ascending Node and v stands for
        the true anomaly.
    
        This class supports hyperbolic orbits, using the convention that semi major axis is negative for such orbits (and of
        course eccentricity is greater than 1).
    
        When orbit is either equatorial or circular, some Keplerian elements (more precisely Ã�â€° and ÃŽÂ©) become ambiguous so
        this class should not be used for such orbits. For this reason, :class:`~org.orekit.orbits.EquinoctialOrbit` is the
        recommended way to represent orbits.
    
        The instance :code:`KeplerianOrbit` is guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.CircularOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`
    """
    @typing.overload
    def __init__(self, t: _FieldKeplerianOrbit__T, t2: _FieldKeplerianOrbit__T, t3: _FieldKeplerianOrbit__T, t4: _FieldKeplerianOrbit__T, t5: _FieldKeplerianOrbit__T, t6: _FieldKeplerianOrbit__T, t7: _FieldKeplerianOrbit__T, t8: _FieldKeplerianOrbit__T, t9: _FieldKeplerianOrbit__T, t10: _FieldKeplerianOrbit__T, t11: _FieldKeplerianOrbit__T, t12: _FieldKeplerianOrbit__T, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t13: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldKeplerianOrbit__T, t2: _FieldKeplerianOrbit__T, t3: _FieldKeplerianOrbit__T, t4: _FieldKeplerianOrbit__T, t5: _FieldKeplerianOrbit__T, t6: _FieldKeplerianOrbit__T, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t7: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldKeplerianOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldKeplerianOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldKeplerianOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldKeplerianOrbit__T): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, t: _FieldKeplerianOrbit__T, tArray: typing.List[_FieldKeplerianOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldKeplerianOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldKeplerianOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    _ellipticEccentricToMean__T = typing.TypeVar('_ellipticEccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticEccentricToMean(t: _ellipticEccentricToMean__T, t2: _ellipticEccentricToMean__T) -> _ellipticEccentricToMean__T:
        """
            Computes the mean anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                E (T): eccentric anomaly (rad)
                e (T): eccentricity
        
            Returns:
                M the mean anomaly
        
        
        """
        ...
    _ellipticEccentricToTrue__T = typing.TypeVar('_ellipticEccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticEccentricToTrue(t: _ellipticEccentricToTrue__T, t2: _ellipticEccentricToTrue__T) -> _ellipticEccentricToTrue__T:
        """
            Computes the true anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                E (T): eccentric anomaly (rad)
                e (T): eccentricity
        
            Returns:
                v the true anomaly
        
        
        """
        ...
    def getA(self) -> _FieldKeplerianOrbit__T:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getA` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
        
        """
        ...
    def getAnomaly(self, positionAngle: PositionAngle) -> _FieldKeplerianOrbit__T:
        """
            Get the anomaly.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                anomaly (rad)
        
        
        """
        ...
    def getAnomalyDot(self, positionAngle: PositionAngle) -> _FieldKeplerianOrbit__T:
        """
            Get the anomaly derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                anomaly derivative (rad/s)
        
        
        """
        ...
    def getE(self) -> _FieldKeplerianOrbit__T:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                eccentricity derivative
        
        
        """
        ...
    def getEccentricAnomaly(self) -> _FieldKeplerianOrbit__T:
        """
            Get the eccentric anomaly.
        
            Returns:
                eccentric anomaly (rad)
        
        
        """
        ...
    def getEccentricAnomalyDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the eccentric anomaly derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                eccentric anomaly derivative (rad/s)
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldKeplerianOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldKeplerianOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getHx(self) -> _FieldKeplerianOrbit__T:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHx` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHxDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldKeplerianOrbit__T:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHy` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the second component of the inclination vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldKeplerianOrbit__T:
        """
            Get the inclination.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getI` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the inclination derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getIDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldKeplerianOrbit__T:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLE` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldKeplerianOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldKeplerianOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getMeanAnomaly(self) -> _FieldKeplerianOrbit__T:
        """
            Get the mean anomaly.
        
            Returns:
                mean anomaly (rad)
        
        
        """
        ...
    def getMeanAnomalyDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the mean anomaly derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                mean anomaly derivative (rad/s)
        
        
        """
        ...
    def getPerigeeArgument(self) -> _FieldKeplerianOrbit__T:
        """
            Get the perigee argument.
        
            Returns:
                perigee argument (rad)
        
        
        """
        ...
    def getPerigeeArgumentDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the perigee argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                perigee argument derivative (rad/s)
        
        
        """
        ...
    def getRightAscensionOfAscendingNode(self) -> _FieldKeplerianOrbit__T:
        """
            Get the right ascension of the ascending node.
        
            Returns:
                right ascension of the ascending node (rad)
        
        
        """
        ...
    def getRightAscensionOfAscendingNodeDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the right ascension of the ascending node derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                right ascension of the ascending node derivative (rad/s)
        
        
        """
        ...
    def getTrueAnomaly(self) -> _FieldKeplerianOrbit__T:
        """
            Get the true anomaly.
        
            Returns:
                true anomaly (rad)
        
        
        """
        ...
    def getTrueAnomalyDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the true anomaly derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                true anomaly derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getType` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    def hasDerivatives(self) -> bool:
        """
            Check if orbit includes derivatives.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.hasDerivatives` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                true if orbit includes derivatives
        
            Also see:
                :meth:`~org.orekit.orbits.FieldOrbit.getADot`, :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getHxDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getHyDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLEDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot`, :meth:`~org.orekit.orbits.FieldOrbit.getLMDot`,
                :meth:`~org.orekit.orbits.FieldOrbit.getEDot`, :meth:`~org.orekit.orbits.FieldOrbit.getIDot`
        
        
        """
        ...
    _hyperbolicEccentricToMean__T = typing.TypeVar('_hyperbolicEccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicEccentricToMean(t: _hyperbolicEccentricToMean__T, t2: _hyperbolicEccentricToMean__T) -> _hyperbolicEccentricToMean__T:
        """
            Computes the mean anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                H (T): hyperbolic eccentric anomaly (rad)
                e (T): eccentricity
        
            Returns:
                M the mean anomaly
        
        
        """
        ...
    _hyperbolicEccentricToTrue__T = typing.TypeVar('_hyperbolicEccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicEccentricToTrue(t: _hyperbolicEccentricToTrue__T, t2: _hyperbolicEccentricToTrue__T) -> _hyperbolicEccentricToTrue__T:
        """
            Computes the true anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                H (T): hyperbolic eccentric anomaly (rad)
                e (T): eccentricity
        
            Returns:
                v the true anomaly
        
        
        """
        ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], collection: typing.Union[java.util.Collection[_FieldKeplerianOrbit__T], typing.Sequence[_FieldKeplerianOrbit__T], typing.Set[_FieldKeplerianOrbit__T]]) -> _FieldKeplerianOrbit__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], stream: java.util.stream.Stream[FieldOrbit[_FieldKeplerianOrbit__T]]) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]: ...
    _meanToEllipticEccentric__T = typing.TypeVar('_meanToEllipticEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToEllipticEccentric(t: _meanToEllipticEccentric__T, t2: _meanToEllipticEccentric__T) -> _meanToEllipticEccentric__T:
        """
            Computes the elliptic eccentric anomaly from the mean anomaly.
        
            The algorithm used here for solving Kepler equation has been published in: "Procedures for solving Kepler's Equation",
            A. W. Odell and R. H. Gooding, Celestial Mechanics 38 (1986) 307-334
        
            Parameters:
                M (T): mean anomaly (rad)
                e (T): eccentricity
        
            Returns:
                E the eccentric anomaly
        
        
        """
        ...
    _meanToHyperbolicEccentric__T = typing.TypeVar('_meanToHyperbolicEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToHyperbolicEccentric(t: _meanToHyperbolicEccentric__T, t2: _meanToHyperbolicEccentric__T) -> _meanToHyperbolicEccentric__T:
        """
            Computes the hyperbolic eccentric anomaly from the mean anomaly.
        
            The algorithm used here for solving hyperbolic Kepler equation is Danby's iterative method (3rd order) with Vallado's
            initial guess.
        
            Parameters:
                M (T): mean anomaly (rad)
                e (T): eccentricity
        
            Returns:
                H the hyperbolic eccentric anomaly
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldKeplerianOrbit__T) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]: ...
    def toOrbit(self) -> 'KeplerianOrbit':
        """
            Transforms the FieldOrbit instance into an Orbit instance.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.toOrbit` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this Keplerian parameters object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    _trueToEllipticEccentric__T = typing.TypeVar('_trueToEllipticEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToEllipticEccentric(t: _trueToEllipticEccentric__T, t2: _trueToEllipticEccentric__T) -> _trueToEllipticEccentric__T:
        """
            Computes the elliptic eccentric anomaly from the true anomaly.
        
            Parameters:
                v (T): true anomaly (rad)
                e (T): eccentricity
        
            Returns:
                E the elliptic eccentric anomaly
        
        
        """
        ...
    _trueToHyperbolicEccentric__T = typing.TypeVar('_trueToHyperbolicEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToHyperbolicEccentric(t: _trueToHyperbolicEccentric__T, t2: _trueToHyperbolicEccentric__T) -> _trueToHyperbolicEccentric__T:
        """
            Computes the hyperbolic eccentric anomaly from the true anomaly.
        
            Parameters:
                v (T): true anomaly (rad)
                e (T): eccentricity
        
            Returns:
                H the hyperbolic eccentric anomaly
        
        
        """
        ...

class HaloOrbit(LibrationOrbit):
    """
    public class HaloOrbit extends :class:`~org.orekit.orbits.LibrationOrbit`
    
        Class calculating different parameters of a Halo Orbit.
    
        Since:
            10.2
    """
    @typing.overload
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem, pVCoordinates: org.orekit.utils.PVCoordinates, double: float): ...
    @typing.overload
    def __init__(self, richardsonExpansion: RichardsonExpansion, double: float, librationOrbitFamily: LibrationOrbitFamily): ...

class KeplerianOrbit(Orbit):
    """
    public class KeplerianOrbit extends :class:`~org.orekit.orbits.Orbit`
    
        This class handles traditional Keplerian orbital parameters.
    
        The parameters used internally are the classical Keplerian elements:
    
        .. code-block: java
        
        
             a
             e
             i
             Ï‰
             Î©
             v
           
        where Ã�â€° stands for the Perigee Argument, ÃŽÂ© stands for the Right Ascension of the Ascending Node and v stands for
        the true anomaly.
    
        This class supports hyperbolic orbits, using the convention that semi major axis is negative for such orbits (and of
        course eccentricity is greater than 1).
    
        When orbit is either equatorial or circular, some Keplerian elements (more precisely Ã�â€° and ÃŽÂ©) become ambiguous so
        this class should not be used for such orbits. For this reason, :class:`~org.orekit.orbits.EquinoctialOrbit` is the
        recommended way to represent orbits.
    
        The instance :code:`KeplerianOrbit` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.CircularOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngle: PositionAngle, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    @staticmethod
    def ellipticEccentricToMean(double: float, double2: float) -> float:
        """
            Computes the mean anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                E (double): eccentric anomaly (rad)
                e (double): eccentricity
        
            Returns:
                M the mean anomaly
        
            Since:
                9.0
        
        
        """
        ...
    @staticmethod
    def ellipticEccentricToTrue(double: float, double2: float) -> float:
        """
            Computes the true anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                E (double): eccentric anomaly (rad)
                e (double): eccentricity
        
            Returns:
                v the true anomaly
        
            Since:
                9.0
        
        
        """
        ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getA` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getAnomaly(self, positionAngle: PositionAngle) -> float:
        """
            Get the anomaly.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                anomaly (rad)
        
        
        """
        ...
    def getAnomalyDot(self, positionAngle: PositionAngle) -> float:
        """
            Get the anomaly derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the angle
        
            Returns:
                anomaly derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEccentricAnomaly(self) -> float:
        """
            Get the eccentric anomaly.
        
            Returns:
                eccentric anomaly (rad)
        
        
        """
        ...
    def getEccentricAnomalyDot(self) -> float:
        """
            Get the eccentric anomaly derivative.
        
            Returns:
                eccentric anomaly derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHx(self) -> float:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHxDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
            Get the second component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getI` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get the inclination derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getIDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLM` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLv` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getMeanAnomaly(self) -> float:
        """
            Get the mean anomaly.
        
            Returns:
                mean anomaly (rad)
        
        
        """
        ...
    def getMeanAnomalyDot(self) -> float:
        """
            Get the mean anomaly derivative.
        
            Returns:
                mean anomaly derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getPerigeeArgument(self) -> float:
        """
            Get the perigee argument.
        
            Returns:
                perigee argument (rad)
        
        
        """
        ...
    def getPerigeeArgumentDot(self) -> float:
        """
            Get the perigee argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                perigee argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getRightAscensionOfAscendingNode(self) -> float:
        """
            Get the right ascension of the ascending node.
        
            Returns:
                right ascension of the ascending node (rad)
        
        
        """
        ...
    def getRightAscensionOfAscendingNodeDot(self) -> float:
        """
            Get the right ascension of the ascending node derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                right ascension of the ascending node derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getTrueAnomaly(self) -> float:
        """
            Get the true anomaly.
        
            Returns:
                true anomaly (rad)
        
        
        """
        ...
    def getTrueAnomalyDot(self) -> float:
        """
            Get the true anomaly derivative.
        
            Returns:
                true anomaly derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getType` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    @staticmethod
    def hyperbolicEccentricToMean(double: float, double2: float) -> float:
        """
            Computes the mean anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                H (double): hyperbolic eccentric anomaly (rad)
                e (double): eccentricity
        
            Returns:
                M the mean anomaly
        
            Since:
                9.0
        
        
        """
        ...
    @staticmethod
    def hyperbolicEccentricToTrue(double: float, double2: float) -> float:
        """
            Computes the true anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                H (double): hyperbolic eccentric anomaly (rad)
                e (double): eccentricity
        
            Returns:
                v the true anomaly
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[Orbit]) -> 'KeplerianOrbit': ...
    @staticmethod
    def meanToEllipticEccentric(double: float, double2: float) -> float:
        """
            Computes the elliptic eccentric anomaly from the mean anomaly.
        
            The algorithm used here for solving Kepler equation has been published in: "Procedures for solving Kepler's Equation",
            A. W. Odell and R. H. Gooding, Celestial Mechanics 38 (1986) 307-334
        
            Parameters:
                M (double): mean anomaly (rad)
                e (double): eccentricity
        
            Returns:
                E the eccentric anomaly
        
        
        """
        ...
    @staticmethod
    def meanToHyperbolicEccentric(double: float, double2: float) -> float:
        """
            Computes the hyperbolic eccentric anomaly from the mean anomaly.
        
            The algorithm used here for solving hyperbolic Kepler equation is Danby's iterative method (3rd order) with Vallado's
            initial guess.
        
            Parameters:
                M (double): mean anomaly (rad)
                ecc (double): eccentricity
        
            Returns:
                H the hyperbolic eccentric anomaly
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'KeplerianOrbit':
        """
            Get a time-shifted orbit.
        
            The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available
            in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available.
            Shifting is *not* intended as a replacement for proper orbit propagation but should be sufficient for small time shifts
            or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.shiftedBy` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of this Keplerian parameters object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    @staticmethod
    def trueToEllipticEccentric(double: float, double2: float) -> float:
        """
            Computes the elliptic eccentric anomaly from the true anomaly.
        
            Parameters:
                v (double): true anomaly (rad)
                e (double): eccentricity
        
            Returns:
                E the elliptic eccentric anomaly
        
            Since:
                9.0
        
        
        """
        ...
    @staticmethod
    def trueToHyperbolicEccentric(double: float, double2: float) -> float:
        """
            Computes the hyperbolic eccentric anomaly from the true anomaly.
        
            Parameters:
                v (double): true anomaly (rad)
                e (double): eccentricity
        
            Returns:
                H the hyperbolic eccentric anomaly
        
            Since:
                9.0
        
        
        """
        ...

class LyapunovOrbit(LibrationOrbit):
    """
    public class LyapunovOrbit extends :class:`~org.orekit.orbits.LibrationOrbit`
    
        Class calculating different parameters of a Lyapunov Orbit.
    
        Since:
            10.2
    """
    @typing.overload
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem, pVCoordinates: org.orekit.utils.PVCoordinates, double: float): ...
    @typing.overload
    def __init__(self, richardsonExpansion: RichardsonExpansion, double: float): ...

class PythonLibrationOrbit(LibrationOrbit):
    """
    public class PythonLibrationOrbit extends :class:`~org.orekit.orbits.LibrationOrbit`
    """
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem, pVCoordinates: org.orekit.utils.PVCoordinates, double: float): ...
    def applyCorrectionOnPV(self, cR3BPDifferentialCorrection: CR3BPDifferentialCorrection) -> org.orekit.utils.PVCoordinates:
        """
            Apply the differential correction to compute more accurate initial PV.
        
            Specified by:
                :meth:`~org.orekit.orbits.LibrationOrbit.applyCorrectionOnPV` in class :class:`~org.orekit.orbits.LibrationOrbit`
        
            Parameters:
                diff (:class:`~org.orekit.orbits.CR3BPDifferentialCorrection`): cr3bp differential correction
        
            Returns:
                corrected PV coordinates
        
        
        """
        ...
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

class PythonOrbit(Orbit):
    """
    public class PythonOrbit extends :class:`~org.orekit.orbits.Orbit`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngle: PositionAngle, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                 in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getA` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
            Get the semi-major axis derivative.
        
            Note that the semi-major axis is considered negative for hyperbolic orbits.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
            Get the eccentricity derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                eccentricity derivative
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHx(self) -> float:
        """
            Get the first component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
            Get the first component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHxDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the inclination vector derivative
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
            Get the second component of the inclination vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getHyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the inclination vector derivative
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getI` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
            Get the inclination derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getIDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLE` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                E + Ï‰ + Î© eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + Ï‰ + Î©)/dt eccentric longitude argument derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLM` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                M + Ï‰ + Î© mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + Ï‰ + Î©)/dt mean longitude argument derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLv` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                v + Ï‰ + Î© true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + Ï‰ + Î©)/dt true longitude argument derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
            Get the orbit type.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getType` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                orbit type
        
        
        """
        ...
    def initPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Compute the position/velocity coordinates from the canonical parameters.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.initPVCoordinates` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                computed position/velocity coordinates
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[Orbit]) -> Orbit: ...
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
    def shiftedBy(self, double: float) -> Orbit:
        """
            Get a time-shifted orbit.
        
            The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available
            in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available.
            Shifting is *not* intended as a replacement for proper orbit propagation but should be sufficient for small time shifts
            or coarse accuracy.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.shiftedBy` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.orbits")``.

    CR3BPDifferentialCorrection: typing.Type[CR3BPDifferentialCorrection]
    CartesianOrbit: typing.Type[CartesianOrbit]
    CircularOrbit: typing.Type[CircularOrbit]
    EquinoctialOrbit: typing.Type[EquinoctialOrbit]
    FieldCartesianOrbit: typing.Type[FieldCartesianOrbit]
    FieldCircularOrbit: typing.Type[FieldCircularOrbit]
    FieldEquinoctialOrbit: typing.Type[FieldEquinoctialOrbit]
    FieldKeplerianOrbit: typing.Type[FieldKeplerianOrbit]
    FieldOrbit: typing.Type[FieldOrbit]
    HaloOrbit: typing.Type[HaloOrbit]
    KeplerianOrbit: typing.Type[KeplerianOrbit]
    LibrationOrbit: typing.Type[LibrationOrbit]
    LibrationOrbitFamily: typing.Type[LibrationOrbitFamily]
    LibrationOrbitType: typing.Type[LibrationOrbitType]
    LyapunovOrbit: typing.Type[LyapunovOrbit]
    Orbit: typing.Type[Orbit]
    OrbitType: typing.Type[OrbitType]
    PositionAngle: typing.Type[PositionAngle]
    PythonLibrationOrbit: typing.Type[PythonLibrationOrbit]
    PythonOrbit: typing.Type[PythonOrbit]
    RichardsonExpansion: typing.Type[RichardsonExpansion]
