import java.io
import java.lang
import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.analysis.polynomials
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.orbits.class-use
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.time
import org.orekit.utils
import typing



_AbstractFieldOrbitInterpolator__KK = typing.TypeVar('_AbstractFieldOrbitInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class AbstractFieldOrbitInterpolator(org.orekit.time.AbstractFieldTimeInterpolator['FieldOrbit'[_AbstractFieldOrbitInterpolator__KK], _AbstractFieldOrbitInterpolator__KK], typing.Generic[_AbstractFieldOrbitInterpolator__KK]):
    """
    public abstract class AbstractFieldOrbitInterpolator<KK extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<KK>> extends :class:`~org.orekit.time.AbstractFieldTimeInterpolator`<:class:`~org.orekit.orbits.FieldOrbit`<KK>, KK>
    
        Abstract class for orbit interpolator.
    """
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame): ...
    def getOutputInertialFrame(self) -> org.orekit.frames.Frame:
        """
            Get output inertial frame.
        
            Returns:
                output inertial frame
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.FieldTimeStamped], typing.Sequence[org.orekit.time.FieldTimeStamped]]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_AbstractFieldOrbitInterpolator__KK], collection: typing.Union[java.util.Collection['FieldOrbit'[_AbstractFieldOrbitInterpolator__KK]], typing.Sequence['FieldOrbit'[_AbstractFieldOrbitInterpolator__KK]]]) -> 'FieldOrbit'[_AbstractFieldOrbitInterpolator__KK]: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_AbstractFieldOrbitInterpolator__KK], stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...

class AbstractOrbitInterpolator(org.orekit.time.AbstractTimeInterpolator['Orbit']):
    """
    public abstract class AbstractOrbitInterpolator extends :class:`~org.orekit.time.AbstractTimeInterpolator`<:class:`~org.orekit.orbits.Orbit`>
    
        Abstract class for orbit interpolator.
    """
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame): ...
    @staticmethod
    def checkOrbitsConsistency(collection: typing.Union[java.util.Collection['Orbit'], typing.Sequence['Orbit']]) -> None: ...
    def getOutputInertialFrame(self) -> org.orekit.frames.Frame:
        """
            Get output inertial frame.
        
            Returns:
                output inertial frame
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection['Orbit'], typing.Sequence['Orbit']]) -> 'Orbit': ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.TimeStamped]) -> org.orekit.time.TimeStamped: ...

class CR3BPDifferentialCorrection:
    """
    public class CR3BPDifferentialCorrection extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class implementing the differential correction method for Halo or Lyapunov Orbits. It is not a simple differential
        correction, it uses higher order terms to be more accurate and meet orbits requirements.
    
        Since:
            10.2
    
        Also see:
            "Three-dimensional, periodic, Halo Orbits by Kathleen Connor Howell, Stanford University"
    """
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, cR3BPSystem: org.orekit.bodies.CR3BPSystem, double: float): ...
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

class CircularLatitudeArgumentUtility:
    """
    public class CircularLatitudeArgumentUtility extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility methods for converting between different latitude arguments used by :class:`~org.orekit.orbits.CircularOrbit`.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.orbits.CircularOrbit`
    """
    @staticmethod
    def convertAlpha(positionAngleType: 'PositionAngleType', double: float, double2: float, double3: float, positionAngleType2: 'PositionAngleType') -> float:
        """
            Convert argument of latitude.
        
            Parameters:
                oldType (:class:`~org.orekit.orbits.PositionAngleType`): old position angle type
                alpha (double): old value for argument of latitude
                ex (double): ex
                ey (double): ey
                newType (:class:`~org.orekit.orbits.PositionAngleType`): new position angle type
        
            Returns:
                convert argument of latitude
        
            Since:
                12.2
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(double: float, double2: float, double3: float) -> float:
        """
            Computes the mean latitude argument from the eccentric latitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of circular eccentricity vector
                ey (double): e sin(ω), second component of circular eccentricity vector
                alphaE (double): = E + ω mean latitude argument (rad)
        
            Returns:
                the mean latitude argument.
        
        
        """
        ...
    @staticmethod
    def eccentricToTrue(double: float, double2: float, double3: float) -> float:
        """
            Computes the true latitude argument from the eccentric latitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of circular eccentricity vector
                ey (double): e sin(ω), second component of circular eccentricity vector
                alphaE (double): = E + ω eccentric latitude argument (rad)
        
            Returns:
                the true latitude argument.
        
        
        """
        ...
    @staticmethod
    def meanToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric latitude argument from the mean latitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of circular eccentricity vector
                ey (double): e sin(ω), second component of circular eccentricity vector
                alphaM (double): = M + ω mean latitude argument (rad)
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...
    @staticmethod
    def meanToTrue(double: float, double2: float, double3: float) -> float:
        """
            Computes the true latitude argument from the eccentric latitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of circular eccentricity vector
                ey (double): e sin(ω), second component of circular eccentricity vector
                alphaM (double): = M + ω mean latitude argument (rad)
        
            Returns:
                the true latitude argument.
        
        
        """
        ...
    @staticmethod
    def trueToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric latitude argument from the true latitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of circular eccentricity vector
                ey (double): e sin(ω), second component of circular eccentricity vector
                alphaV (double): = V + ω true latitude argument (rad)
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...
    @staticmethod
    def trueToMean(double: float, double2: float, double3: float) -> float:
        """
            Computes the mean latitude argument from the eccentric latitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of circular eccentricity vector
                ey (double): e sin(ω), second component of circular eccentricity vector
                alphaV (double): = V + ω true latitude argument (rad)
        
            Returns:
                the mean latitude argument.
        
        
        """
        ...

class EquinoctialLongitudeArgumentUtility:
    """
    public class EquinoctialLongitudeArgumentUtility extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility methods for converting between different longitude arguments used by
        :class:`~org.orekit.orbits.EquinoctialOrbit`.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.orbits.EquinoctialOrbit`
    """
    @staticmethod
    def convertL(positionAngleType: 'PositionAngleType', double: float, double2: float, double3: float, positionAngleType2: 'PositionAngleType') -> float:
        """
            Convert argument of longitude.
        
            Parameters:
                oldType (:class:`~org.orekit.orbits.PositionAngleType`): old position angle type
                l (double): old value for argument of longitude
                ex (double): ex
                ey (double): ey
                newType (:class:`~org.orekit.orbits.PositionAngleType`): new position angle type
        
            Returns:
                converted argument of longitude
        
            Since:
                12.2
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(double: float, double2: float, double3: float) -> float:
        """
            Computes the mean longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of eccentricity vector
                ey (double): e sin(ω), second component of eccentricity vector
                lE (double): = E + ω + Ω mean longitude argument (rad)
        
            Returns:
                the mean longitude argument.
        
        
        """
        ...
    @staticmethod
    def eccentricToTrue(double: float, double2: float, double3: float) -> float:
        """
            Computes the true longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of eccentricity vector
                ey (double): e sin(ω), second component of eccentricity vector
                lE (double): = E + ω + Ω eccentric longitude argument (rad)
        
            Returns:
                the true longitude argument.
        
        
        """
        ...
    @staticmethod
    def meanToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric longitude argument from the mean longitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of eccentricity vector
                ey (double): e sin(ω), second component of eccentricity vector
                lM (double): = M + ω + Ω mean longitude argument (rad)
        
            Returns:
                the eccentric longitude argument.
        
        
        """
        ...
    @staticmethod
    def meanToTrue(double: float, double2: float, double3: float) -> float:
        """
            Computes the true longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of eccentricity vector
                ey (double): e sin(ω), second component of eccentricity vector
                lM (double): = M + ω + Ω mean longitude argument (rad)
        
            Returns:
                the true longitude argument.
        
        
        """
        ...
    @staticmethod
    def trueToEccentric(double: float, double2: float, double3: float) -> float:
        """
            Computes the eccentric longitude argument from the true longitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of eccentricity vector
                ey (double): e sin(ω), second component of eccentricity vector
                lV (double): = V + ω + Ω true longitude argument (rad)
        
            Returns:
                the eccentric longitude argument.
        
        
        """
        ...
    @staticmethod
    def trueToMean(double: float, double2: float, double3: float) -> float:
        """
            Computes the mean longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (double): e cos(ω), first component of eccentricity vector
                ey (double): e sin(ω), second component of eccentricity vector
                lV (double): = V + ω + Ω true longitude argument (rad)
        
            Returns:
                the mean longitude argument.
        
        
        """
        ...

class FieldCircularLatitudeArgumentUtility:
    """
    public class FieldCircularLatitudeArgumentUtility extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility methods for converting between different latitude arguments used by
        :class:`~org.orekit.orbits.FieldCircularOrbit`.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.orbits.FieldCircularOrbit`
    """
    _convertAlpha__T = typing.TypeVar('_convertAlpha__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def convertAlpha(positionAngleType: 'PositionAngleType', t: _convertAlpha__T, t2: _convertAlpha__T, t3: _convertAlpha__T, positionAngleType2: 'PositionAngleType') -> _convertAlpha__T:
        """
            Convert argument of latitude.
        
            Parameters:
                oldType (:class:`~org.orekit.orbits.PositionAngleType`): old position angle type
                alpha (T): old value for argument of latitude
                ex (T): ex
                ey (T): ey
                newType (:class:`~org.orekit.orbits.PositionAngleType`): new position angle type
        
            Returns:
                convert argument of latitude
        
            Since:
                12.2
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(t: _eccentricToMean__T, t2: _eccentricToMean__T, t3: _eccentricToMean__T) -> _eccentricToMean__T:
        """
            Computes the mean latitude argument from the eccentric latitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of circular eccentricity vector
                ey (T): e sin(ω), second component of circular eccentricity vector
                alphaE (T): = E + ω eccentric latitude argument (rad)
        
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
                ex (T): e cos(ω), first component of circular eccentricity vector
                ey (T): e sin(ω), second component of circular eccentricity vector
                alphaE (T): = E + ω eccentric latitude argument (rad)
        
            Returns:
                the true latitude argument.
        
        
        """
        ...
    _meanToEccentric__T = typing.TypeVar('_meanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToEccentric(t: _meanToEccentric__T, t2: _meanToEccentric__T, t3: _meanToEccentric__T) -> _meanToEccentric__T:
        """
            Computes the eccentric latitude argument from the mean latitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of circular eccentricity vector
                ey (T): e sin(ω), second component of circular eccentricity vector
                alphaM (T): = M + ω mean latitude argument (rad)
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...
    _meanToTrue__T = typing.TypeVar('_meanToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToTrue(t: _meanToTrue__T, t2: _meanToTrue__T, t3: _meanToTrue__T) -> _meanToTrue__T:
        """
            Computes the true latitude argument from the eccentric latitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of circular eccentricity vector
                ey (T): e sin(ω), second component of circular eccentricity vector
                alphaM (T): = M + ω mean latitude argument (rad)
        
            Returns:
                the true latitude argument.
        
        
        """
        ...
    _trueToEccentric__T = typing.TypeVar('_trueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToEccentric(t: _trueToEccentric__T, t2: _trueToEccentric__T, t3: _trueToEccentric__T) -> _trueToEccentric__T:
        """
            Computes the eccentric latitude argument from the true latitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of circular eccentricity vector
                ey (T): e sin(ω), second component of circular eccentricity vector
                alphaV (T): = v + ω true latitude argument (rad)
        
            Returns:
                the eccentric latitude argument.
        
        
        """
        ...
    _trueToMean__T = typing.TypeVar('_trueToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToMean(t: _trueToMean__T, t2: _trueToMean__T, t3: _trueToMean__T) -> _trueToMean__T:
        """
            Computes the mean latitude argument from the eccentric latitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of circular eccentricity vector
                ey (T): e sin(ω), second component of circular eccentricity vector
                alphaV (T): = V + ω true latitude argument (rad)
        
            Returns:
                the mean latitude argument.
        
        
        """
        ...

class FieldEquinoctialLongitudeArgumentUtility:
    """
    public class FieldEquinoctialLongitudeArgumentUtility extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility methods for converting between different longitude arguments used by
        :class:`~org.orekit.orbits.FieldEquinoctialOrbit`.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.orbits.FieldEquinoctialOrbit`
    """
    _convertL__T = typing.TypeVar('_convertL__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def convertL(positionAngleType: 'PositionAngleType', t: _convertL__T, t2: _convertL__T, t3: _convertL__T, positionAngleType2: 'PositionAngleType') -> _convertL__T:
        """
            Convert argument of longitude.
        
            Parameters:
                oldType (:class:`~org.orekit.orbits.PositionAngleType`): old position angle type
                l (T): old value for argument of longitude
                ex (T): ex
                ey (T): ey
                newType (:class:`~org.orekit.orbits.PositionAngleType`): new position angle type
        
            Returns:
                converted argument of longitude
        
            Since:
                12.2
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(t: _eccentricToMean__T, t2: _eccentricToMean__T, t3: _eccentricToMean__T) -> _eccentricToMean__T:
        """
            Computes the mean longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of eccentricity vector
                ey (T): e sin(ω), second component of eccentricity vector
                lE (T): = E + ω + Ω mean longitude argument (rad)
        
            Returns:
                the mean longitude argument.
        
        
        """
        ...
    _eccentricToTrue__T = typing.TypeVar('_eccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToTrue(t: _eccentricToTrue__T, t2: _eccentricToTrue__T, t3: _eccentricToTrue__T) -> _eccentricToTrue__T:
        """
            Computes the true longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of eccentricity vector
                ey (T): e sin(ω), second component of eccentricity vector
                lE (T): = E + ω + Ω eccentric longitude argument (rad)
        
            Returns:
                the true longitude argument.
        
        
        """
        ...
    _meanToEccentric__T = typing.TypeVar('_meanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToEccentric(t: _meanToEccentric__T, t2: _meanToEccentric__T, t3: _meanToEccentric__T) -> _meanToEccentric__T:
        """
            Computes the eccentric longitude argument from the mean longitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of eccentricity vector
                ey (T): e sin(ω), second component of eccentricity vector
                lM (T): = M + ω + Ω mean longitude argument (rad)
        
            Returns:
                the eccentric longitude argument.
        
        
        """
        ...
    _meanToTrue__T = typing.TypeVar('_meanToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToTrue(t: _meanToTrue__T, t2: _meanToTrue__T, t3: _meanToTrue__T) -> _meanToTrue__T:
        """
            Computes the true longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of eccentricity vector
                ey (T): e sin(ω), second component of eccentricity vector
                lM (T): = M + ω + Ω mean longitude argument (rad)
        
            Returns:
                the true longitude argument.
        
        
        """
        ...
    _trueToEccentric__T = typing.TypeVar('_trueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToEccentric(t: _trueToEccentric__T, t2: _trueToEccentric__T, t3: _trueToEccentric__T) -> _trueToEccentric__T:
        """
            Computes the eccentric longitude argument from the true longitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of eccentricity vector
                ey (T): e sin(ω), second component of eccentricity vector
                lV (T): = V + ω + Ω true longitude argument (rad)
        
            Returns:
                the eccentric longitude argument.
        
        
        """
        ...
    _trueToMean__T = typing.TypeVar('_trueToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToMean(t: _trueToMean__T, t2: _trueToMean__T, t3: _trueToMean__T) -> _trueToMean__T:
        """
            Computes the mean longitude argument from the eccentric longitude argument.
        
            Parameters:
                ex (T): e cos(ω), first component of eccentricity vector
                ey (T): e sin(ω), second component of eccentricity vector
                lV (T): = V + ω + Ω true longitude argument (rad)
        
            Returns:
                the mean longitude argument.
        
        
        """
        ...

class FieldKeplerianAnomalyUtility:
    """
    public class FieldKeplerianAnomalyUtility extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility methods for converting between different Keplerian anomalies.
    """
    _convertAnomaly__T = typing.TypeVar('_convertAnomaly__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def convertAnomaly(positionAngleType: 'PositionAngleType', t: _convertAnomaly__T, t2: _convertAnomaly__T, positionAngleType2: 'PositionAngleType') -> _convertAnomaly__T:
        """
            Convert anomaly.
        
            Parameters:
                oldType (:class:`~org.orekit.orbits.PositionAngleType`): old position angle type
                anomaly (T): old value for anomaly
                e (T): eccentricity
                newType (:class:`~org.orekit.orbits.PositionAngleType`): new position angle type
        
            Returns:
                converted anomaly
        
            Since:
                12.2
        
        
        """
        ...
    _ellipticEccentricToMean__T = typing.TypeVar('_ellipticEccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticEccentricToMean(t: _ellipticEccentricToMean__T, t2: _ellipticEccentricToMean__T) -> _ellipticEccentricToMean__T:
        """
            Computes the elliptic mean anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                e (T): eccentricity such that 0 ≤ e < 1
                E (T): elliptic eccentric anomaly (rad)
        
            Returns:
                elliptic mean anomaly (rad)
        
        
        """
        ...
    _ellipticEccentricToTrue__T = typing.TypeVar('_ellipticEccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticEccentricToTrue(t: _ellipticEccentricToTrue__T, t2: _ellipticEccentricToTrue__T) -> _ellipticEccentricToTrue__T:
        """
            Computes the elliptic true anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                e (T): eccentricity such that 0 ≤ e < 1
                E (T): elliptic eccentric anomaly (rad)
        
            Returns:
                elliptic true anomaly (rad)
        
        
        """
        ...
    _ellipticMeanToEccentric__T = typing.TypeVar('_ellipticMeanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticMeanToEccentric(t: _ellipticMeanToEccentric__T, t2: _ellipticMeanToEccentric__T) -> _ellipticMeanToEccentric__T:
        """
            Computes the elliptic eccentric anomaly from the elliptic mean anomaly.
        
            The algorithm used here for solving hyperbolic Kepler equation is from Odell, A.W., Gooding, R.H. "Procedures for
            solving Kepler's equation." Celestial Mechanics 38, 307–334 (1986). https://doi.org/10.1007/BF01238923
        
            Parameters:
                e (T): eccentricity such that 0 ≤ e < 1
                M (T): elliptic mean anomaly (rad)
        
            Returns:
                elliptic eccentric anomaly (rad)
        
        
        """
        ...
    _ellipticMeanToTrue__T = typing.TypeVar('_ellipticMeanToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticMeanToTrue(t: _ellipticMeanToTrue__T, t2: _ellipticMeanToTrue__T) -> _ellipticMeanToTrue__T:
        """
            Computes the elliptic true anomaly from the elliptic mean anomaly.
        
            Parameters:
                e (T): eccentricity such that 0 ≤ e < 1
                M (T): elliptic mean anomaly (rad)
        
            Returns:
                elliptic true anomaly (rad)
        
        
        """
        ...
    _ellipticTrueToEccentric__T = typing.TypeVar('_ellipticTrueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticTrueToEccentric(t: _ellipticTrueToEccentric__T, t2: _ellipticTrueToEccentric__T) -> _ellipticTrueToEccentric__T:
        """
            Computes the elliptic eccentric anomaly from the elliptic true anomaly.
        
            Parameters:
                e (T): eccentricity such that 0 ≤ e < 1
                v (T): elliptic true anomaly (rad)
        
            Returns:
                elliptic eccentric anomaly (rad)
        
        
        """
        ...
    _ellipticTrueToMean__T = typing.TypeVar('_ellipticTrueToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticTrueToMean(t: _ellipticTrueToMean__T, t2: _ellipticTrueToMean__T) -> _ellipticTrueToMean__T:
        """
            Computes the elliptic mean anomaly from the elliptic true anomaly.
        
            Parameters:
                e (T): eccentricity such that 0 ≤ e < 1
                v (T): elliptic true anomaly (rad)
        
            Returns:
                elliptic mean anomaly (rad)
        
        
        """
        ...
    _hyperbolicEccentricToMean__T = typing.TypeVar('_hyperbolicEccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicEccentricToMean(t: _hyperbolicEccentricToMean__T, t2: _hyperbolicEccentricToMean__T) -> _hyperbolicEccentricToMean__T:
        """
            Computes the hyperbolic mean anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                e (T): eccentricity > 1
                H (T): hyperbolic eccentric anomaly
        
            Returns:
                hyperbolic mean anomaly
        
        
        """
        ...
    _hyperbolicEccentricToTrue__T = typing.TypeVar('_hyperbolicEccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicEccentricToTrue(t: _hyperbolicEccentricToTrue__T, t2: _hyperbolicEccentricToTrue__T) -> _hyperbolicEccentricToTrue__T:
        """
            Computes the hyperbolic true anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                e (T): eccentricity > 1
                H (T): hyperbolic eccentric anomaly
        
            Returns:
                hyperbolic true anomaly (rad)
        
        
        """
        ...
    _hyperbolicMeanToEccentric__T = typing.TypeVar('_hyperbolicMeanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicMeanToEccentric(t: _hyperbolicMeanToEccentric__T, t2: _hyperbolicMeanToEccentric__T) -> _hyperbolicMeanToEccentric__T:
        """
            Computes the hyperbolic eccentric anomaly from the hyperbolic mean anomaly.
        
            The algorithm used here for solving hyperbolic Kepler equation is from Gooding, R.H., Odell, A.W. "The hyperbolic Kepler
            equation (and the elliptic equation revisited)." Celestial Mechanics 44, 267–282 (1988).
            https://doi.org/10.1007/BF01235540
        
            Parameters:
                e (T): eccentricity > 1
                M (T): hyperbolic mean anomaly
        
            Returns:
                hyperbolic eccentric anomaly
        
        
        """
        ...
    _hyperbolicMeanToTrue__T = typing.TypeVar('_hyperbolicMeanToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicMeanToTrue(t: _hyperbolicMeanToTrue__T, t2: _hyperbolicMeanToTrue__T) -> _hyperbolicMeanToTrue__T:
        """
            Computes the hyperbolic true anomaly from the hyperbolic mean anomaly.
        
            Parameters:
                e (T): eccentricity > 1
                M (T): hyperbolic mean anomaly
        
            Returns:
                hyperbolic true anomaly (rad)
        
        
        """
        ...
    _hyperbolicTrueToEccentric__T = typing.TypeVar('_hyperbolicTrueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicTrueToEccentric(t: _hyperbolicTrueToEccentric__T, t2: _hyperbolicTrueToEccentric__T) -> _hyperbolicTrueToEccentric__T:
        """
            Computes the hyperbolic eccentric anomaly from the hyperbolic true anomaly.
        
            Parameters:
                e (T): eccentricity > 1
                v (T): hyperbolic true anomaly (rad)
        
            Returns:
                hyperbolic eccentric anomaly
        
        
        """
        ...
    _hyperbolicTrueToMean__T = typing.TypeVar('_hyperbolicTrueToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicTrueToMean(t: _hyperbolicTrueToMean__T, t2: _hyperbolicTrueToMean__T) -> _hyperbolicTrueToMean__T:
        """
            Computes the hyperbolic mean anomaly from the hyperbolic true anomaly.
        
            Parameters:
                e (T): eccentricity > 1
                v (T): hyperbolic true anomaly (rad)
        
            Returns:
                hyperbolic mean anomaly
        
        
        """
        ...

_FieldOrbit__T = typing.TypeVar('_FieldOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldOrbit(org.orekit.utils.FieldPVCoordinatesProvider[_FieldOrbit__T], org.orekit.time.FieldTimeStamped[_FieldOrbit__T], org.orekit.time.FieldTimeShiftable['FieldOrbit'[_FieldOrbit__T], _FieldOrbit__T], typing.Generic[_FieldOrbit__T]):
    """
    public abstract class FieldOrbit<T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T>, :class:`~org.orekit.time.FieldTimeStamped`<T>, :class:`~org.orekit.time.FieldTimeShiftable`<:class:`~org.orekit.orbits.FieldOrbit`<T>, T>
    
        This class handles orbital parameters.
    
        For user convenience, both the Cartesian and the equinoctial elements are provided by this class, regardless of the
        canonical representation implemented in the derived class (which may be classical Keplerian elements for example).
    
        The parameters are defined in a frame specified by the user. It is important to make sure this frame is consistent: it
        probably is inertial and centered on the central body. This information is used for example by some force models.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`
    """
    def addKeplerContribution(self, positionAngleType: 'PositionAngleType', t: _FieldOrbit__T, tArray: typing.List[_FieldOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
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
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
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
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
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
    def getJacobianWrtCartesian(self, positionAngleType: 'PositionAngleType', tArray: typing.List[typing.List[_FieldOrbit__T]]) -> None:
        """
            Compute the Jacobian of the orbital parameters with respect to the Cartesian parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of parameter i of the orbit with respect to Cartesian coordinate j.
            This means each row corresponds to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates
            x, y, z, xDot, yDot and zDot.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle to use
                jacobian (:class:`~org.orekit.orbits.FieldOrbit`[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                    corner will be modified
        
        
        """
        ...
    def getJacobianWrtParameters(self, positionAngleType: 'PositionAngleType', tArray: typing.List[typing.List[_FieldOrbit__T]]) -> None:
        """
            Compute the Jacobian of the Cartesian parameters with respect to the orbital parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of Cartesian coordinate i of the orbit with respect to orbital
            parameter j. This means each row corresponds to one Cartesian coordinate x, y, z, xdot, ydot, zdot whereas columns 0 to
            5 correspond to the orbital parameters.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle to use
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldOrbit__T:
        """
            Get the mean longitude argument.
        
            Returns:
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldOrbit__T:
        """
            Get the true longitude argument.
        
            Returns:
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getMeanAnomalyDotWrtA(self) -> _FieldOrbit__T:
        """
            Get the derivative of the mean anomaly with respect to the semi major axis.
        
            Returns:
                derivative of the mean anomaly with respect to the semi major axis
        
        
        """
        ...
    def getMu(self) -> _FieldOrbit__T:
        """
            Get the central attraction coefficient used for position and velocity conversions (m³/s²).
        
            Returns:
                central attraction coefficient used for position and velocity conversions (m³/s²)
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldOrbit__T]: ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldOrbit__T]: ...
    @typing.overload
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbit__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldOrbit__T]: ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldOrbit__T]: ...
    @typing.overload
    def getPosition(self, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldOrbit__T]: ...
    @typing.overload
    def getPosition(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbit__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldOrbit__T]: ...
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
    def isElliptical(self) -> bool:
        """
            Returns true if and only if the orbit is elliptical i.e. has a non-negative semi-major axis.
        
            Returns:
                true if getA() is strictly greater than 0
        
            Since:
                12.0
        
        
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

class KeplerianAnomalyUtility:
    """
    public final class KeplerianAnomalyUtility extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility methods for converting between different Keplerian anomalies.
    """
    @staticmethod
    def convertAnomaly(positionAngleType: 'PositionAngleType', double: float, double2: float, positionAngleType2: 'PositionAngleType') -> float:
        """
            Convert anomaly.
        
            Parameters:
                oldType (:class:`~org.orekit.orbits.PositionAngleType`): old position angle type
                anomaly (double): old value for anomaly
                e (double): eccentricity
                newType (:class:`~org.orekit.orbits.PositionAngleType`): new position angle type
        
            Returns:
                converted anomaly
        
            Since:
                12.2
        
        
        """
        ...
    @staticmethod
    def ellipticEccentricToMean(double: float, double2: float) -> float:
        """
            Computes the elliptic mean anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                e (double): eccentricity such that 0 ≤ e < 1
                E (double): elliptic eccentric anomaly (rad)
        
            Returns:
                elliptic mean anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def ellipticEccentricToTrue(double: float, double2: float) -> float:
        """
            Computes the elliptic true anomaly from the elliptic eccentric anomaly.
        
            Parameters:
                e (double): eccentricity such that 0 ≤ e < 1
                E (double): elliptic eccentric anomaly (rad)
        
            Returns:
                elliptic true anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def ellipticMeanToEccentric(double: float, double2: float) -> float:
        """
            Computes the elliptic eccentric anomaly from the elliptic mean anomaly.
        
            The algorithm used here for solving hyperbolic Kepler equation is from Odell, A.W., Gooding, R.H. "Procedures for
            solving Kepler's equation." Celestial Mechanics 38, 307–334 (1986). https://doi.org/10.1007/BF01238923
        
            Parameters:
                e (double): eccentricity such that 0 ≤ e < 1
                M (double): elliptic mean anomaly (rad)
        
            Returns:
                elliptic eccentric anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def ellipticMeanToTrue(double: float, double2: float) -> float:
        """
            Computes the elliptic true anomaly from the elliptic mean anomaly.
        
            Parameters:
                e (double): eccentricity such that 0 ≤ e < 1
                M (double): elliptic mean anomaly (rad)
        
            Returns:
                elliptic true anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def ellipticTrueToEccentric(double: float, double2: float) -> float:
        """
            Computes the elliptic eccentric anomaly from the elliptic true anomaly.
        
            Parameters:
                e (double): eccentricity such that 0 ≤ e < 1
                v (double): elliptic true anomaly (rad)
        
            Returns:
                elliptic eccentric anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def ellipticTrueToMean(double: float, double2: float) -> float:
        """
            Computes the elliptic mean anomaly from the elliptic true anomaly.
        
            Parameters:
                e (double): eccentricity such that 0 ≤ e < 1
                v (double): elliptic true anomaly (rad)
        
            Returns:
                elliptic mean anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def hyperbolicEccentricToMean(double: float, double2: float) -> float:
        """
            Computes the hyperbolic mean anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                e (double): eccentricity > 1
                H (double): hyperbolic eccentric anomaly
        
            Returns:
                hyperbolic mean anomaly
        
        
        """
        ...
    @staticmethod
    def hyperbolicEccentricToTrue(double: float, double2: float) -> float:
        """
            Computes the hyperbolic true anomaly from the hyperbolic eccentric anomaly.
        
            Parameters:
                e (double): eccentricity > 1
                H (double): hyperbolic eccentric anomaly
        
            Returns:
                hyperbolic true anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def hyperbolicMeanToEccentric(double: float, double2: float) -> float:
        """
            Computes the hyperbolic eccentric anomaly from the hyperbolic mean anomaly.
        
            The algorithm used here for solving hyperbolic Kepler equation is from Gooding, R.H., Odell, A.W. "The hyperbolic Kepler
            equation (and the elliptic equation revisited)." Celestial Mechanics 44, 267–282 (1988).
            https://doi.org/10.1007/BF01235540
        
            Parameters:
                e (double): eccentricity > 1
                M (double): hyperbolic mean anomaly
        
            Returns:
                hyperbolic eccentric anomaly
        
        
        """
        ...
    @staticmethod
    def hyperbolicMeanToTrue(double: float, double2: float) -> float:
        """
            Computes the hyperbolic true anomaly from the hyperbolic mean anomaly.
        
            Parameters:
                e (double): eccentricity > 1
                M (double): hyperbolic mean anomaly
        
            Returns:
                hyperbolic true anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def hyperbolicTrueToEccentric(double: float, double2: float) -> float:
        """
            Computes the hyperbolic eccentric anomaly from the hyperbolic true anomaly.
        
            Parameters:
                e (double): eccentricity > 1
                v (double): hyperbolic true anomaly (rad)
        
            Returns:
                hyperbolic eccentric anomaly
        
        
        """
        ...
    @staticmethod
    def hyperbolicTrueToMean(double: float, double2: float) -> float:
        """
            Computes the hyperbolic mean anomaly from the hyperbolic true anomaly.
        
            Parameters:
                e (double): eccentricity > 1
                v (double): hyperbolic true anomaly (rad)
        
            Returns:
                hyperbolic mean anomaly
        
        
        """
        ...

class KeplerianMotionCartesianUtility:
    """
    public class KeplerianMotionCartesianUtility extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility class to predict position and velocity under Keplerian motion, using lightweight routines based on Cartesian
        coordinates. Computations do not require a reference frame or an epoch.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.analytical.KeplerianPropagator`,
            :class:`~org.orekit.propagation.analytical.FieldKeplerianPropagator`, :class:`~org.orekit.orbits.CartesianOrbit`,
            :class:`~org.orekit.orbits.FieldCartesianOrbit`
    """
    _predictPositionVelocity_0__T = typing.TypeVar('_predictPositionVelocity_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def predictPositionVelocity(t: _predictPositionVelocity_0__T, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_predictPositionVelocity_0__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_predictPositionVelocity_0__T], t2: _predictPositionVelocity_0__T) -> org.orekit.utils.FieldPVCoordinates[_predictPositionVelocity_0__T]:
        """
            Method to propagate position and velocity according to Keplerian dynamics. For long time of flights, it is preferable to
            use :class:`~org.orekit.propagation.analytical.KeplerianPropagator`.
        
            Parameters:
                dt (T): time of flight
                position (:class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> position): initial position vector
                velocity (:class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> velocity): initial velocity vector
                mu (T): central body gravitational parameter
        
            Returns:
                predicted position-velocity
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def predictPositionVelocity(double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float) -> org.orekit.utils.PVCoordinates:
        """
            Method to propagate position and velocity according to Keplerian dynamics. For long time of flights, it is preferable to
            use :class:`~org.orekit.propagation.analytical.KeplerianPropagator`.
        
            Parameters:
                dt (double): time of flight
                position (:class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): initial position vector
                velocity (:class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): initial velocity vector
                mu (double): central body gravitational parameter
        
            Returns:
                predicted position-velocity
        
        """
        ...

class LibrationOrbit:
    """
    public abstract class LibrationOrbit extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for libration orbits.
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.orbits.HaloOrbit`, :class:`~org.orekit.orbits.LyapunovOrbit`
    """
    def applyDifferentialCorrection(self) -> None:
        """
            Apply differential correction.
        
            This will update :code:`initialPV` and :code:`orbitalPeriod` parameters.
        
        """
        ...
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
    public enum LibrationOrbitFamily extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.orbits.LibrationOrbitFamily`>
    
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
                name (:class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
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
    public enum LibrationOrbitType extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.orbits.LibrationOrbitType`>
    
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
                name (:class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
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

class Orbit(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['Orbit'], java.io.Serializable, org.orekit.utils.PVCoordinatesProvider):
    """
    public abstract class Orbit extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.orbits.Orbit`>, :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`, :class:`~org.orekit.utils.PVCoordinatesProvider`
    
        This class handles orbital parameters.
    
        For user convenience, both the Cartesian and the equinoctial elements are provided by this class, regardless of the
        canonical representation implemented in the derived class (which may be classical Keplerian elements for example).
    
        The parameters are defined in a frame specified by the user. It is important to make sure this frame is consistent: it
        probably is inertial and centered on the central body. This information is used for example by some force models.
    
        Instance of this class are guaranteed to be immutable.
    
        Also see:
            :meth:`~serialized`
    """
    def addKeplerContribution(self, positionAngleType: 'PositionAngleType', double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
            Get the first component of the equinoctial eccentricity vector.
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                inclination derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getJacobianWrtCartesian(self, positionAngleType: 'PositionAngleType', doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Compute the Jacobian of the orbital parameters with respect to the Cartesian parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of parameter i of the orbit with respect to Cartesian coordinate j.
            This means each row corresponds to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates
            x, y, z, xDot, yDot and zDot.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle to use
                jacobian (double[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                    corner will be modified
        
        
        """
        ...
    def getJacobianWrtParameters(self, positionAngleType: 'PositionAngleType', doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Compute the Jacobian of the Cartesian parameters with respect to the orbital parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of Cartesian coordinate i of the orbit with respect to orbital
            parameter j. This means each row corresponds to one Cartesian coordinate x, y, z, xdot, ydot, zdot whereas columns 0 to
            5 correspond to the orbital parameters.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle to use
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
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
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
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
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
            Since:
                9.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getMeanAnomalyDotWrtA(self) -> float:
        """
            Get the derivative of the mean anomaly with respect to the semi major axis.
        
            Returns:
                derivative of the mean anomaly with respect to the semi major axis
        
        
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
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates` in
                interface :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                otherDate (:class:`~org.orekit.time.AbsoluteDate`): current date
                otherFrame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position in definition frame.
        
            Returns:
                position in the definition frame
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.getPVCoordinates`
        
        
        """
        ...
    @typing.overload
    def getPosition(self, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPosition` in
                interface :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                otherDate (:class:`~org.orekit.time.AbsoluteDate`): current date
                otherFrame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                position of the body (m and)
        
            Get the position in a specified frame.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): frame in which the position coordinates shall be computed
        
            Returns:
                position in the specified output frame
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.getPosition`
        
        """
        ...
    @typing.overload
    def getPosition(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
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
    def isElliptical(self) -> bool:
        """
            Returns true if and only if the orbit is elliptical i.e. has a non-negative semi-major axis.
        
            Returns:
                true if getA() is strictly greater than 0
        
            Since:
                12.0
        
        
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
    public enum OrbitType extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.orbits.OrbitType`>
    
        Enumerate for :class:`~org.orekit.orbits.Orbit` and :class:`~org.orekit.orbits.FieldOrbit` parameters types.
    """
    CARTESIAN: typing.ClassVar['OrbitType'] = ...
    CIRCULAR: typing.ClassVar['OrbitType'] = ...
    EQUINOCTIAL: typing.ClassVar['OrbitType'] = ...
    KEPLERIAN: typing.ClassVar['OrbitType'] = ...
    POS_X: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` POS_X
    
        Name for position along X.
    
        Also see:
            :meth:`~constant`
    
    
    """
    POS_Y: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` POS_Y
    
        Name for position along Y.
    
        Also see:
            :meth:`~constant`
    
    
    """
    POS_Z: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` POS_Z
    
        Name for position along Z.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VEL_X: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` VEL_X
    
        Name for velocity along X.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VEL_Y: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` VEL_Y
    
        Name for velocity along Y.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VEL_Z: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` VEL_Z
    
        Name for velocity along Z.
    
        Also see:
            :meth:`~constant`
    
    
    """
    A: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` A
    
        Name for semi major axis.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ECC
    
        Name for eccentricity.
    
        Also see:
            :meth:`~constant`
    
    
    """
    E_X: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` E_X
    
        Name for eccentricity vector first component.
    
        Also see:
            :meth:`~constant`
    
    
    """
    E_Y: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` E_Y
    
        Name for eccentricity vector second component.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INC: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` INC
    
        Name for inclination.
    
        Also see:
            :meth:`~constant`
    
    
    """
    H_X: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` H_X
    
        Name for inclination vector first component.
    
        Also see:
            :meth:`~constant`
    
    
    """
    H_Y: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` H_Y
    
        Name for inclination vector second component .
    
        Also see:
            :meth:`~constant`
    
    
    """
    PA: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` PA
    
        Name for perigee argument.
    
        Also see:
            :meth:`~constant`
    
    
    """
    RAAN: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` RAAN
    
        Name for right ascension of ascending node.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN_ANOM: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEAN_ANOM
    
        Name for mean anomaly.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC_ANOM: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ECC_ANOM
    
        Name for eccentric anomaly.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUE_ANOM: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TRUE_ANOM
    
        Name for mean anomaly.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN_LAT_ARG: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEAN_LAT_ARG
    
        Name for mean argument of latitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC_LAT_ARG: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ECC_LAT_ARG
    
        Name for eccentric argument of latitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUE_LAT_ARG: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TRUE_LAT_ARG
    
        Name for mean argument of latitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MEAN_LON_ARG: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MEAN_LON_ARG
    
        Name for mean argument of longitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ECC_LON_ARG: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ECC_LON_ARG
    
        Name for eccentric argument of longitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUE_LON_ARG: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` TRUE_LON_ARG
    
        Name for mean argument of longitude.
    
        Also see:
            :meth:`~constant`
    
    
    """
    _convertToFieldOrbit__T = typing.TypeVar('_convertToFieldOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def convertToFieldOrbit(self, field: org.hipparchus.Field[_convertToFieldOrbit__T], orbit: Orbit) -> FieldOrbit[_convertToFieldOrbit__T]: ...
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
        
        public abstract <T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> :class:`~org.orekit.orbits.FieldOrbit`<T> convertType (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit)
        
            Convert an orbit to the instance type.
        
            The returned orbit is the specified instance itself if its type already matches, otherwise, a new orbit of the proper
            type created
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): orbit to convert
        
            Returns:
                converted orbit with type guaranteed to match (so it can be cast safely)
        
        
        """
        ...
    def getDrivers(self, double: float, orbit: Orbit, positionAngleType: 'PositionAngleType') -> org.orekit.utils.ParameterDriversList:
        """
            Get parameters drivers initialized from a reference orbit.
        
            Parameters:
                dP (double): user specified position error
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                parameters drivers initialized from reference orbit
        
        
        """
        ...
    def isPositionAngleBased(self) -> bool:
        """
            Tells if the orbit type is based on position angles or not.
        
            Returns:
                true if based on :class:`~org.orekit.orbits.PositionAngleType`
        
            Since:
                12.0
        
        
        """
        ...
    _mapArrayToOrbit_0__T = typing.TypeVar('_mapArrayToOrbit_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mapArrayToOrbit(self, tArray: typing.List[_mapArrayToOrbit_0__T], tArray2: typing.List[_mapArrayToOrbit_0__T], positionAngleType: 'PositionAngleType', fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mapArrayToOrbit_0__T], t3: _mapArrayToOrbit_0__T, frame: org.orekit.frames.Frame) -> FieldOrbit[_mapArrayToOrbit_0__T]: ...
    @typing.overload
    def mapArrayToOrbit(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], positionAngleType: 'PositionAngleType', absoluteDate: org.orekit.time.AbsoluteDate, double3: float, frame: org.orekit.frames.Frame) -> Orbit:
        """
            Convert state array to orbital parameters.
        
            Note that all implementations of this method *must* be consistent with the implementation of the
            :meth:`~org.orekit.orbits.Orbit.getJacobianWrtCartesian` method for the corresponding orbit type in terms of parameters
            order and meaning.
        
            Parameters:
                array (double[]): state as a flat array (it can have more than 6 elements, extra elements are ignored)
                arrayDot (double[]): state derivative as a flat array (it can be null, in which case Keplerian motion is assumed, and it can have more than 6
                    elements, extra elements are ignored)
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
                date (:class:`~org.orekit.time.AbsoluteDate`): integration date
                mu (double): central attraction coefficient used for propagation (m³/s²)
                frame (:class:`~org.orekit.frames.Frame`): frame in which integration is performed
        
            Returns:
                orbit corresponding to the flat array as a space dynamics object
        
        public abstract <T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> :class:`~org.orekit.orbits.FieldOrbit`<T> mapArrayToOrbit (T[] array, T[] arrayDot, :class:`~org.orekit.orbits.PositionAngleType` type, :class:`~org.orekit.time.FieldAbsoluteDate`<T> date, T mu, :class:`~org.orekit.frames.Frame` frame)
        
            Convert state array to orbital parameters.
        
            Note that all implementations of this method *must* be consistent with the implementation of the
            :meth:`~org.orekit.orbits.Orbit.getJacobianWrtCartesian` method for the corresponding orbit type in terms of parameters
            order and meaning.
        
            Parameters:
                array (T[]): state as a flat array (it can have more than 6 elements, extra elements are ignored)
                arrayDot (T[]): state derivative as a flat array (it can be null, in which case Keplerian motion is assumed,
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): integration date
                mu (T): central attraction coefficient used for propagation (m³/s²)
                frame (:class:`~org.orekit.frames.Frame`): frame in which integration is performed
        
            Returns:
                orbit corresponding to the flat array as a space dynamics object
        
        
        """
        ...
    _mapOrbitToArray_0__T = typing.TypeVar('_mapOrbitToArray_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mapOrbitToArray(self, fieldOrbit: FieldOrbit[_mapOrbitToArray_0__T], positionAngleType: 'PositionAngleType', tArray: typing.List[_mapOrbitToArray_0__T], tArray2: typing.List[_mapOrbitToArray_0__T]) -> None: ...
    @typing.overload
    def mapOrbitToArray(self, orbit: Orbit, positionAngleType: 'PositionAngleType', doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None:
        """
            Convert orbit to state array.
        
            Note that all implementations of this method *must* be consistent with the implementation of the
            :meth:`~org.orekit.orbits.Orbit.getJacobianWrtCartesian` method for the corresponding orbit type in terms of parameters
            order and meaning.
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to map
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
                stateVector (double[]):             flat array into which the state vector should be mapped (it can have more than 6 elements, extra elements are untouched)
                stateVectorDot (double[]): flat array into which the state vector derivative should be mapped (it can be null if derivatives are not desired, and
                    it can have more than 6 elements, extra elements are untouched)
        
        public abstract <T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> void mapOrbitToArray (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit, :class:`~org.orekit.orbits.PositionAngleType` type, T[] stateVector, T[] stateVectorDot)
        
            Convert orbit to state array.
        
            Note that all implementations of this method *must* be consistent with the implementation of the
            :meth:`~org.orekit.orbits.Orbit.getJacobianWrtCartesian` method for the corresponding orbit type in terms of parameters
            order and meaning.
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): orbit to map
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
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
        
            Given a, angular component ζ of an orbit and the corresponding angular component ζᵣ in the reference orbit, the
            angular component ζₙ of the normalized orbit will be ζₙ = ζ + 2kπ where k is chosen such that ζᵣ - π ≤
            ζₙ ≤ ζᵣ + π. This is intended to avoid too large discontinuities and is particularly useful for normalizing the
            orbit after an impulsive maneuver with respect to the reference picked up before the maneuver.
        
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
                name (:class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
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

class PositionAngleBased:
    """
    public interface PositionAngleBased
    
        This interface represent orbit-like trajectory whose definition is based on a so-called position angle.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.orbits.PositionAngleType`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CircularOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`,
            :class:`~org.orekit.orbits.FieldKeplerianOrbit`, :class:`~org.orekit.orbits.FieldCircularOrbit`,
            :class:`~org.orekit.orbits.FieldEquinoctialOrbit`
    """
    def getCachedPositionAngleType(self) -> 'PositionAngleType':
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Returns:
                cached type of position angle
        
        
        """
        ...
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Returns:
                true if and only if holding rates
        
        
        """
        ...
    def removeRates(self) -> 'PositionAngleBased':
        """
            Create a new instance such that :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` is false.
        
            Returns:
                new object without rates
        
        
        """
        ...

class PositionAngleType(java.lang.Enum['PositionAngleType']):
    """
    public enum PositionAngleType extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.orbits.PositionAngleType`>
    
        Enumerate for true, eccentric and mean position angles.
    
        Also see:
            :class:`~org.orekit.orbits.KeplerianOrbit`, :class:`~org.orekit.orbits.CircularOrbit`,
            :class:`~org.orekit.orbits.EquinoctialOrbit`, :class:`~org.orekit.orbits.FieldKeplerianOrbit`,
            :class:`~org.orekit.orbits.FieldCircularOrbit`, :class:`~org.orekit.orbits.FieldEquinoctialOrbit`
    """
    MEAN: typing.ClassVar['PositionAngleType'] = ...
    ECCENTRIC: typing.ClassVar['PositionAngleType'] = ...
    TRUE: typing.ClassVar['PositionAngleType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PositionAngleType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['PositionAngleType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PositionAngleType c : PositionAngleType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RichardsonExpansion:
    """
    public class RichardsonExpansion extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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

class WalkerConstellation:
    """
    public class WalkerConstellation extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Builder for orbits of satellites forming a Walker constellation.
    
        Since:
            12.1
    """
    def __init__(self, int: int, int2: int, int3: int): ...
    _buildReferenceSlot__O = typing.TypeVar('_buildReferenceSlot__O', bound=Orbit)  # <O>
    def buildReferenceSlot(self, o: _buildReferenceSlot__O) -> 'WalkerConstellationSlot'[_buildReferenceSlot__O]:
        """
            Create the reference slot, which is satellite 0 in plane 0.
        
            Parameters:
                referenceOrbit (O): orbit of the reference satellite, in :meth:`~org.orekit.orbits.WalkerConstellationSlot.getPlane` 0 and at
                    :meth:`~org.orekit.orbits.WalkerConstellationSlot.getSatellite` satellite index} 0
        
            Returns:
                build reference slot
        
            Also see:
                :meth:`~org.orekit.orbits.WalkerConstellation.buildRegularSlots`,
                :meth:`~org.orekit.orbits.WalkerConstellation.buildSlot`
        
        
        """
        ...
    _buildRegularSlots__O = typing.TypeVar('_buildRegularSlots__O', bound=Orbit)  # <O>
    def buildRegularSlots(self, o: _buildRegularSlots__O) -> java.util.List[java.util.List['WalkerConstellationSlot'[_buildRegularSlots__O]]]: ...
    _buildSlot__O = typing.TypeVar('_buildSlot__O', bound=Orbit)  # <O>
    def buildSlot(self, walkerConstellationSlot: 'WalkerConstellationSlot'[_buildSlot__O], int: int, double: float) -> 'WalkerConstellationSlot'[_buildSlot__O]:
        """
            Create one offset slot from an already existing slot.
        
            Parameters:
                existingSlot (:class:`~org.orekit.orbits.WalkerConstellationSlot`<O> existingSlot): existing slot (may be the :meth:`~org.orekit.orbits.WalkerConstellation.buildReferenceSlot` or not)
                plane (int): plane index of the new slot (may be non-integer for in-orbit spare satellites)
                satellite (double): new slot satellite index in plane (may be non-integer if needed)
        
            Returns:
                built slot
        
            Also see:
                :meth:`~org.orekit.orbits.WalkerConstellation.buildRegularSlots`,
                :meth:`~org.orekit.orbits.WalkerConstellation.buildReferenceSlot`
        
        
        """
        ...
    def getF(self) -> int:
        """
            Get the phasing parameter.
        
            Returns:
                phasing parameter
        
        
        """
        ...
    def getP(self) -> int:
        """
            Get the number of orbital planes.
        
            Returns:
                number of orbital planes
        
        
        """
        ...
    def getT(self) -> int:
        """
            Get the total number of satellites.
        
            Returns:
                total number of satellites
        
        
        """
        ...

_WalkerConstellationSlot__O = typing.TypeVar('_WalkerConstellationSlot__O', bound=Orbit)  # <O>
class WalkerConstellationSlot(typing.Generic[_WalkerConstellationSlot__O]):
    """
    public class WalkerConstellationSlot<O extends :class:`~org.orekit.orbits.Orbit`> extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for one satellite slot in a :class:`~org.orekit.orbits.WalkerConstellation`.
    
        The :meth:`~org.orekit.orbits.WalkerConstellationSlot.getSatellite` satellite index for regular satellites is an
        integer, but it is allowed to have non-integer indices to create slots for in-orbit spare satellites between the regular
        satellites. As an example, one can consider a 24/3/1 Walker constellation with 8 operational satellites in each of the 3
        planes at satellites indices 0, 1, 2, 3, 4, 5, 6 and 7, and put for example 2 additional spares in each plane (hence
        having a total of 30 satellites), by affecting them to intermediate slots 0.5 and 4.5.
    
        Since:
            12.1
    """
    def getConstellation(self) -> WalkerConstellation:
        """
            Get the constellation.
        
            Returns:
                constellation
        
        
        """
        ...
    def getOrbit(self) -> _WalkerConstellationSlot__O:
        """
            Get the orbit.
        
            Returns:
                orbit
        
        
        """
        ...
    def getPlane(self) -> int:
        """
            Get the plane index.
        
            Returns:
                plane index
        
        
        """
        ...
    def getSatellite(self) -> float:
        """
            Get the satellite index in plane.
        
            Not that the index may be non-integer, for example to deal with in-orbit spare satellites
        
            Returns:
                satellite index in plane
        
        
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
    def addKeplerContribution(self, positionAngleType: PositionAngleType, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.addKeplerContribution` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
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
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
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
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
        """
        ...

class CircularOrbit(Orbit, PositionAngleBased):
    """
    public class CircularOrbit extends :class:`~org.orekit.orbits.Orbit` implements :class:`~org.orekit.orbits.PositionAngleBased`
    
        This class handles circular orbital parameters.
    
        The parameters used internally are the circular elements which can be related to Keplerian elements as follows:
    
          - a
          - e :sub:`x` = e cos(ω)
          - e :sub:`y` = e sin(ω)
          - i
          - Ω
          - α :sub:`v` = v + ω
    
        where Ω stands for the Right Ascension of the Ascending Node and α :sub:`v` stands for the true latitude argument
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is circular (but not equatorial), the circular parameters
        are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous. When orbit
        is equatorial, neither the Keplerian nor the circular parameters can be defined unambiguously.
        :class:`~org.orekit.orbits.EquinoctialOrbit` is the recommended way to represent orbits.
    
        The instance :code:`CircularOrbit` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngleType: PositionAngleType, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.addKeplerContribution` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(double: float, double2: float, double3: float) -> float: ...
    @staticmethod
    def eccentricToTrue(double: float, double2: float, double3: float) -> float: ...
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getAlpha(self, positionAngleType: PositionAngleType) -> float:
        """
            Get the latitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                latitude argument (rad)
        
        
        """
        ...
    def getAlphaDot(self, positionAngleType: PositionAngleType) -> float:
        """
            Get the latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
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
                E + ω eccentric latitude argument (rad)
        
        
        """
        ...
    def getAlphaEDot(self) -> float:
        """
            Get the eccentric latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                d(E + ω)/dt eccentric latitude argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getAlphaM(self) -> float:
        """
            Get the mean latitude argument.
        
            Returns:
                M + ω mean latitude argument (rad)
        
        
        """
        ...
    def getAlphaMDot(self) -> float:
        """
            Get the mean latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                d(M + ω)/dt mean latitude argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getAlphaV(self) -> float:
        """
            Get the true latitude argument.
        
            Returns:
                v + ω true latitude argument (rad)
        
        
        """
        ...
    def getAlphaVDot(self) -> float:
        """
            Get the true latitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Returns:
                v + ω true latitude argument derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.getCachedPositionAngleType` in
                interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                cached type of position angle
        
        
        """
        ...
    def getCircularEx(self) -> float:
        """
            Get the first component of the circular eccentricity vector.
        
            Returns:
                ex = e cos(ω), first component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularExDot(self) -> float:
        """
            Get the first component of the circular eccentricity vector derivative.
        
            Returns:
                ex = e cos(ω), first component of the circular eccentricity vector derivative
        
            Since:
                9.0
        
        
        """
        ...
    def getCircularEy(self) -> float:
        """
            Get the second component of the circular eccentricity vector.
        
            Returns:
                ey = e sin(ω), second component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularEyDot(self) -> float:
        """
            Get the second component of the circular eccentricity vector derivative.
        
            Returns:
                ey = e sin(ω), second component of the circular eccentricity vector derivative
        
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
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
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
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
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                true if and only if holding rates
        
        
        """
        ...
    @staticmethod
    def meanToEccentric(double: float, double2: float, double3: float) -> float: ...
    def removeRates(self) -> 'CircularOrbit':
        """
            Create a new instance such that :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` is false.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.removeRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                new object without rates
        
        
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    @staticmethod
    def trueToEccentric(double: float, double2: float, double3: float) -> float: ...

class EquinoctialOrbit(Orbit, PositionAngleBased):
    """
    public class EquinoctialOrbit extends :class:`~org.orekit.orbits.Orbit` implements :class:`~org.orekit.orbits.PositionAngleBased`
    
        This class handles equinoctial orbital parameters, which can support both circular and equatorial orbits.
    
        The parameters used internally are the equinoctial elements which can be related to Keplerian elements as follows:
    
        .. code-block: java
        
             a
             ex = e cos(ω + Ω)
             ey = e sin(ω + Ω)
             hx = tan(i/2) cos(Ω)
             hy = tan(i/2) sin(Ω)
             lv = v + ω + Ω
           
        where ω stands for the Perigee Argument and Ω stands for the Right Ascension of the Ascending Node.
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is either equatorial or circular, the equinoctial
        parameters are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous.
        For this reason, equinoctial parameters are the recommended way to represent orbits. Note however than the present
        implementation does not handle non-elliptical cases.
    
        The instance :code:`EquinoctialOrbit` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CircularOrbit`, :class:`~org.orekit.orbits.CartesianOrbit`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngleType: PositionAngleType, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.addKeplerContribution` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(double: float, double2: float, double3: float) -> float: ...
    @staticmethod
    def eccentricToTrue(double: float, double2: float, double3: float) -> float: ...
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.getCachedPositionAngleType` in
                interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                cached type of position angle
        
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getIDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                inclination derivative (rad/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getL(self, positionAngleType: PositionAngleType) -> float:
        """
            Get the longitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                longitude argument (rad)
        
        
        """
        ...
    def getLDot(self, positionAngleType: PositionAngleType) -> float:
        """
            Get the longitude argument derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
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
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
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
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
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
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                true if and only if holding rates
        
        
        """
        ...
    @staticmethod
    def meanToEccentric(double: float, double2: float, double3: float) -> float: ...
    def removeRates(self) -> 'EquinoctialOrbit':
        """
            Create a new instance such that :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` is false.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.removeRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                new object without rates
        
        
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    @staticmethod
    def trueToEccentric(double: float, double2: float, double3: float) -> float: ...

_FieldCartesianOrbit__T = typing.TypeVar('_FieldCartesianOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianOrbit(FieldOrbit[_FieldCartesianOrbit__T], typing.Generic[_FieldCartesianOrbit__T]):
    """
    public class FieldCartesianOrbit<T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T>
    
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
    def __init__(self, field: org.hipparchus.Field[_FieldCartesianOrbit__T], cartesianOrbit: CartesianOrbit): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldCartesianOrbit__T], orbit: Orbit): ...
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldCartesianOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldCartesianOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCartesianOrbit__T], t: _FieldCartesianOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldCartesianOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldCartesianOrbit__T): ...
    def addKeplerContribution(self, positionAngleType: PositionAngleType, t: _FieldCartesianOrbit__T, tArray: typing.List[_FieldCartesianOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.addKeplerContribution` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
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
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
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
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldCartesianOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldCartesianOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldCartesianOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
        """
        ...

_FieldCircularOrbit__T = typing.TypeVar('_FieldCircularOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCircularOrbit(FieldOrbit[_FieldCircularOrbit__T], PositionAngleBased, typing.Generic[_FieldCircularOrbit__T]):
    """
    public class FieldCircularOrbit<T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T> implements :class:`~org.orekit.orbits.PositionAngleBased`
    
        This class handles circular orbital parameters.
    
        The parameters used internally are the circular elements which can be related to Keplerian elements as follows:
    
          - a
          - e :sub:`x` = e cos(ω)
          - e :sub:`y` = e sin(ω)
          - i
          - Ω
          - α :sub:`v` = v + ω
    
        where Ω stands for the Right Ascension of the Ascending Node and α :sub:`v` stands for the true latitude argument
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is circular (but not equatorial), the circular parameters
        are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous. When orbit
        is equatorial, neither the Keplerian nor the circular parameters can be defined unambiguously.
        :class:`~org.orekit.orbits.EquinoctialOrbit` is the recommended way to represent orbits.
    
        The instance :code:`CircularOrbit` is guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`
    """
    @typing.overload
    def __init__(self, t: _FieldCircularOrbit__T, t2: _FieldCircularOrbit__T, t3: _FieldCircularOrbit__T, t4: _FieldCircularOrbit__T, t5: _FieldCircularOrbit__T, t6: _FieldCircularOrbit__T, t7: _FieldCircularOrbit__T, t8: _FieldCircularOrbit__T, t9: _FieldCircularOrbit__T, t10: _FieldCircularOrbit__T, t11: _FieldCircularOrbit__T, t12: _FieldCircularOrbit__T, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t13: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldCircularOrbit__T, t2: _FieldCircularOrbit__T, t3: _FieldCircularOrbit__T, t4: _FieldCircularOrbit__T, t5: _FieldCircularOrbit__T, t6: _FieldCircularOrbit__T, t7: _FieldCircularOrbit__T, t8: _FieldCircularOrbit__T, t9: _FieldCircularOrbit__T, t10: _FieldCircularOrbit__T, t11: _FieldCircularOrbit__T, t12: _FieldCircularOrbit__T, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t13: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldCircularOrbit__T, t2: _FieldCircularOrbit__T, t3: _FieldCircularOrbit__T, t4: _FieldCircularOrbit__T, t5: _FieldCircularOrbit__T, t6: _FieldCircularOrbit__T, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t7: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldCircularOrbit__T, t2: _FieldCircularOrbit__T, t3: _FieldCircularOrbit__T, t4: _FieldCircularOrbit__T, t5: _FieldCircularOrbit__T, t6: _FieldCircularOrbit__T, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t7: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldCircularOrbit__T], circularOrbit: CircularOrbit): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldCircularOrbit__T], orbit: Orbit): ...
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldCircularOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldCircularOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCircularOrbit__T], t: _FieldCircularOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldCircularOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldCircularOrbit__T): ...
    def addKeplerContribution(self, positionAngleType: PositionAngleType, t: _FieldCircularOrbit__T, tArray: typing.List[_FieldCircularOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.addKeplerContribution` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldCircularOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldCircularOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(t: _eccentricToMean__T, t2: _eccentricToMean__T, t3: _eccentricToMean__T) -> _eccentricToMean__T: ...
    _eccentricToTrue__T = typing.TypeVar('_eccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToTrue(t: _eccentricToTrue__T, t2: _eccentricToTrue__T, t3: _eccentricToTrue__T) -> _eccentricToTrue__T: ...
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
    def getAlpha(self, positionAngleType: PositionAngleType) -> _FieldCircularOrbit__T:
        """
            Get the latitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                latitude argument (rad)
        
        
        """
        ...
    def getAlphaDot(self, positionAngleType: PositionAngleType) -> _FieldCircularOrbit__T:
        """
            Get the latitude argument derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                latitude argument derivative (rad/s)
        
        
        """
        ...
    def getAlphaE(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentric latitude argument.
        
            Returns:
                E + ω eccentric latitude argument (rad)
        
        
        """
        ...
    def getAlphaEDot(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentric latitude argument derivative.
        
            Returns:
                d(E + ω)/dt eccentric latitude argument derivative (rad/s)
        
        
        """
        ...
    def getAlphaM(self) -> _FieldCircularOrbit__T:
        """
            Get the mean latitude argument.
        
            Returns:
                M + ω mean latitude argument (rad)
        
        
        """
        ...
    def getAlphaMDot(self) -> _FieldCircularOrbit__T:
        """
            Get the mean latitude argument derivative.
        
            Returns:
                d(M + ω)/dt mean latitude argument derivative (rad/s)
        
        
        """
        ...
    def getAlphaV(self) -> _FieldCircularOrbit__T:
        """
            Get the true latitude argument.
        
            Returns:
                v + ω true latitude argument (rad)
        
        
        """
        ...
    def getAlphaVDot(self) -> _FieldCircularOrbit__T:
        """
            Get the true latitude argument derivative.
        
            Returns:
                d(v + ω)/dt true latitude argument derivative (rad/s)
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.getCachedPositionAngleType` in
                interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                cached type of position angle
        
        
        """
        ...
    def getCircularEx(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the circular eccentricity vector.
        
            Returns:
                ex = e cos(ω), first component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularExDot(self) -> _FieldCircularOrbit__T:
        """
            Get the first component of the circular eccentricity vector derivative.
        
            Returns:
                d(ex)/dt = d(e cos(ω))/dt, first component of the circular eccentricity vector derivative
        
        
        """
        ...
    def getCircularEy(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the circular eccentricity vector.
        
            Returns:
                ey = e sin(ω), second component of the circular eccentricity vector
        
        
        """
        ...
    def getCircularEyDot(self) -> _FieldCircularOrbit__T:
        """
            Get the second component of the circular eccentricity vector derivative.
        
            Returns:
                d(ey)/dt = d(e sin(ω))/dt, second component of the circular eccentricity vector derivative
        
        
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
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
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
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldCircularOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldCircularOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldCircularOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldCircularOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldCircularOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
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
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                true if and only if holding rates
        
        
        """
        ...
    _meanToEccentric__T = typing.TypeVar('_meanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToEccentric(t: _meanToEccentric__T, t2: _meanToEccentric__T, t3: _meanToEccentric__T) -> _meanToEccentric__T: ...
    def removeRates(self) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]: ...
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    _trueToEccentric__T = typing.TypeVar('_trueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToEccentric(t: _trueToEccentric__T, t2: _trueToEccentric__T, t3: _trueToEccentric__T) -> _trueToEccentric__T: ...

_FieldEquinoctialOrbit__T = typing.TypeVar('_FieldEquinoctialOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEquinoctialOrbit(FieldOrbit[_FieldEquinoctialOrbit__T], PositionAngleBased, typing.Generic[_FieldEquinoctialOrbit__T]):
    """
    public class FieldEquinoctialOrbit<T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T> implements :class:`~org.orekit.orbits.PositionAngleBased`
    
        This class handles equinoctial orbital parameters, which can support both circular and equatorial orbits.
    
        The parameters used internally are the equinoctial elements which can be related to Keplerian elements as follows:
    
        .. code-block: java
        
             a
             ex = e cos(ω + Ω)
             ey = e sin(ω + Ω)
             hx = tan(i/2) cos(Ω)
             hy = tan(i/2) sin(Ω)
             lv = v + ω + Ω
           
        where ω stands for the Perigee Argument and Ω stands for the Right Ascension of the Ascending Node.
    
        The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined,
        i.e. when orbit is neither equatorial nor circular. When orbit is either equatorial or circular, the equinoctial
        parameters are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous.
        For this reason, equinoctial parameters are the recommended way to represent orbits. Note however than the present
        implementation does not handle non-elliptical cases.
    
        The instance :code:`EquinoctialOrbit` is guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.KeplerianOrbit`,
            :class:`~org.orekit.orbits.CircularOrbit`, :class:`~org.orekit.orbits.CartesianOrbit`
    """
    @typing.overload
    def __init__(self, t: _FieldEquinoctialOrbit__T, t2: _FieldEquinoctialOrbit__T, t3: _FieldEquinoctialOrbit__T, t4: _FieldEquinoctialOrbit__T, t5: _FieldEquinoctialOrbit__T, t6: _FieldEquinoctialOrbit__T, t7: _FieldEquinoctialOrbit__T, t8: _FieldEquinoctialOrbit__T, t9: _FieldEquinoctialOrbit__T, t10: _FieldEquinoctialOrbit__T, t11: _FieldEquinoctialOrbit__T, t12: _FieldEquinoctialOrbit__T, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t13: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldEquinoctialOrbit__T, t2: _FieldEquinoctialOrbit__T, t3: _FieldEquinoctialOrbit__T, t4: _FieldEquinoctialOrbit__T, t5: _FieldEquinoctialOrbit__T, t6: _FieldEquinoctialOrbit__T, t7: _FieldEquinoctialOrbit__T, t8: _FieldEquinoctialOrbit__T, t9: _FieldEquinoctialOrbit__T, t10: _FieldEquinoctialOrbit__T, t11: _FieldEquinoctialOrbit__T, t12: _FieldEquinoctialOrbit__T, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t13: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldEquinoctialOrbit__T, t2: _FieldEquinoctialOrbit__T, t3: _FieldEquinoctialOrbit__T, t4: _FieldEquinoctialOrbit__T, t5: _FieldEquinoctialOrbit__T, t6: _FieldEquinoctialOrbit__T, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t7: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldEquinoctialOrbit__T, t2: _FieldEquinoctialOrbit__T, t3: _FieldEquinoctialOrbit__T, t4: _FieldEquinoctialOrbit__T, t5: _FieldEquinoctialOrbit__T, t6: _FieldEquinoctialOrbit__T, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t7: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEquinoctialOrbit__T], equinoctialOrbit: EquinoctialOrbit): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldEquinoctialOrbit__T], orbit: Orbit): ...
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldEquinoctialOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldEquinoctialOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEquinoctialOrbit__T], t: _FieldEquinoctialOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldEquinoctialOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldEquinoctialOrbit__T): ...
    def addKeplerContribution(self, positionAngleType: PositionAngleType, t: _FieldEquinoctialOrbit__T, tArray: typing.List[_FieldEquinoctialOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.addKeplerContribution` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldEquinoctialOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldEquinoctialOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(t: _eccentricToMean__T, t2: _eccentricToMean__T, t3: _eccentricToMean__T) -> _eccentricToMean__T: ...
    _eccentricToTrue__T = typing.TypeVar('_eccentricToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToTrue(t: _eccentricToTrue__T, t2: _eccentricToTrue__T, t3: _eccentricToTrue__T) -> _eccentricToTrue__T: ...
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
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.getCachedPositionAngleType` in
                interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                cached type of position angle
        
        
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
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
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
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
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
    def getL(self, positionAngleType: PositionAngleType) -> _FieldEquinoctialOrbit__T:
        """
            Get the longitude argument.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                longitude argument (rad)
        
        
        """
        ...
    def getLDot(self, positionAngleType: PositionAngleType) -> _FieldEquinoctialOrbit__T:
        """
            Get the longitude argument derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldEquinoctialOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
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
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                true if and only if holding rates
        
        
        """
        ...
    _meanToEccentric__T = typing.TypeVar('_meanToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def meanToEccentric(t: _meanToEccentric__T, t2: _meanToEccentric__T, t3: _meanToEccentric__T) -> _meanToEccentric__T: ...
    def removeRates(self) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]: ...
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
        """
        ...
    _trueToEccentric__T = typing.TypeVar('_trueToEccentric__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def trueToEccentric(t: _trueToEccentric__T, t2: _trueToEccentric__T, t3: _trueToEccentric__T) -> _trueToEccentric__T: ...

_FieldKeplerianOrbit__T = typing.TypeVar('_FieldKeplerianOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldKeplerianOrbit(FieldOrbit[_FieldKeplerianOrbit__T], PositionAngleBased, typing.Generic[_FieldKeplerianOrbit__T]):
    """
    public class FieldKeplerianOrbit<T extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.orbits.FieldOrbit`<T> implements :class:`~org.orekit.orbits.PositionAngleBased`
    
        This class handles traditional Keplerian orbital parameters.
    
        The parameters used internally are the classical Keplerian elements:
    
        .. code-block: java
        
             a
             e
             i
             ω
             Ω
             v
           
        where ω stands for the Perigee Argument, Ω stands for the Right Ascension of the Ascending Node and v stands for the
        true anomaly.
    
        This class supports hyperbolic orbits, using the convention that semi major axis is negative for such orbits (and of
        course eccentricity is greater than 1).
    
        When orbit is either equatorial or circular, some Keplerian elements (more precisely ω and Ω) become ambiguous so this
        class should not be used for such orbits. For this reason, :class:`~org.orekit.orbits.EquinoctialOrbit` is the
        recommended way to represent orbits.
    
        The instance :code:`KeplerianOrbit` is guaranteed to be immutable.
    
        Since:
            9.0
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.CircularOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`
    """
    @typing.overload
    def __init__(self, t: _FieldKeplerianOrbit__T, t2: _FieldKeplerianOrbit__T, t3: _FieldKeplerianOrbit__T, t4: _FieldKeplerianOrbit__T, t5: _FieldKeplerianOrbit__T, t6: _FieldKeplerianOrbit__T, t7: _FieldKeplerianOrbit__T, t8: _FieldKeplerianOrbit__T, t9: _FieldKeplerianOrbit__T, t10: _FieldKeplerianOrbit__T, t11: _FieldKeplerianOrbit__T, t12: _FieldKeplerianOrbit__T, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t13: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldKeplerianOrbit__T, t2: _FieldKeplerianOrbit__T, t3: _FieldKeplerianOrbit__T, t4: _FieldKeplerianOrbit__T, t5: _FieldKeplerianOrbit__T, t6: _FieldKeplerianOrbit__T, t7: _FieldKeplerianOrbit__T, t8: _FieldKeplerianOrbit__T, t9: _FieldKeplerianOrbit__T, t10: _FieldKeplerianOrbit__T, t11: _FieldKeplerianOrbit__T, t12: _FieldKeplerianOrbit__T, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t13: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldKeplerianOrbit__T, t2: _FieldKeplerianOrbit__T, t3: _FieldKeplerianOrbit__T, t4: _FieldKeplerianOrbit__T, t5: _FieldKeplerianOrbit__T, t6: _FieldKeplerianOrbit__T, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t7: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, t: _FieldKeplerianOrbit__T, t2: _FieldKeplerianOrbit__T, t3: _FieldKeplerianOrbit__T, t4: _FieldKeplerianOrbit__T, t5: _FieldKeplerianOrbit__T, t6: _FieldKeplerianOrbit__T, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t7: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldKeplerianOrbit__T], keplerianOrbit: 'KeplerianOrbit'): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldKeplerianOrbit__T], orbit: Orbit): ...
    @typing.overload
    def __init__(self, fieldOrbit: FieldOrbit[_FieldKeplerianOrbit__T]): ...
    @typing.overload
    def __init__(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldKeplerianOrbit__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianOrbit__T], t: _FieldKeplerianOrbit__T): ...
    @typing.overload
    def __init__(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldKeplerianOrbit__T], frame: org.orekit.frames.Frame, t2: _FieldKeplerianOrbit__T): ...
    def addKeplerContribution(self, positionAngleType: PositionAngleType, t: _FieldKeplerianOrbit__T, tArray: typing.List[_FieldKeplerianOrbit__T]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.addKeplerContribution` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
                gm (:class:`~org.orekit.orbits.FieldKeplerianOrbit`): attraction coefficient to use
                pDot (:class:`~org.orekit.orbits.FieldKeplerianOrbit`[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
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
    def getAnomaly(self, positionAngleType: PositionAngleType) -> _FieldKeplerianOrbit__T:
        """
            Get the anomaly.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                anomaly (rad)
        
        
        """
        ...
    def getAnomalyDot(self, positionAngleType: PositionAngleType) -> _FieldKeplerianOrbit__T:
        """
            Get the anomaly derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                anomaly derivative (rad/s)
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.getCachedPositionAngleType` in
                interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                cached type of position angle
        
        
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
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
        
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
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLEDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldKeplerianOrbit__T:
        """
            Get the mean longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLM` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLMDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldKeplerianOrbit__T:
        """
            Get the true longitude argument.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLv` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldKeplerianOrbit__T:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is null.
        
            Specified by:
                :meth:`~org.orekit.orbits.FieldOrbit.getLvDot` in class :class:`~org.orekit.orbits.FieldOrbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
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
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                true if and only if holding rates
        
        
        """
        ...
    def removeRates(self) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]: ...
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
        """
        ...

_FieldOrbitBlender__KK = typing.TypeVar('_FieldOrbitBlender__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldOrbitBlender(AbstractFieldOrbitInterpolator[_FieldOrbitBlender__KK], typing.Generic[_FieldOrbitBlender__KK]):
    """
    public class FieldOrbitBlender<KK extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<KK>> extends :class:`~org.orekit.orbits.AbstractFieldOrbitInterpolator`<KK>
    
        Orbit blender.
    
        Its purpose is to interpolate orbit state between tabulated orbit states using the concept of blending, exposed in :
        "Efficient Covariance Interpolation using Blending of Approximate State Error Transitions" by Sergei Tanygin, and
        applying it to orbit states instead of covariances.
    
        It propagates tabulated values to the interpolating time using given analytical propagator and then blend each
        propagated states using a smoothstep function. It gives especially good results as explained
        :class:`~org.orekit.orbits.https:.orekit.org.doc.technical` compared to Hermite interpolation when time steps between
        tabulated values get significant (In LEO, > 10 mn for example).
    
        Also see:
            :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory?is`,
            :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory.FieldSmoothStepFunction?is`
    """
    def __init__(self, fieldSmoothStepFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.FieldSmoothStepFunction[_FieldOrbitBlender__KK], fieldAbstractAnalyticalPropagator: org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator[_FieldOrbitBlender__KK], frame: org.orekit.frames.Frame): ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.FieldTimeStamped], typing.Sequence[org.orekit.time.FieldTimeStamped]]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbitBlender__KK], collection: typing.Union[java.util.Collection[FieldOrbit[_FieldOrbitBlender__KK]], typing.Sequence[FieldOrbit[_FieldOrbitBlender__KK]]]) -> FieldOrbit[_FieldOrbitBlender__KK]: ...
    @typing.overload
    def interpolate(self, abstractFieldTimeInterpolator: org.orekit.time.AbstractFieldTimeInterpolator.InterpolationData) -> FieldOrbit[_FieldOrbitBlender__KK]: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbitBlender__KK], stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...

_FieldOrbitHermiteInterpolator__KK = typing.TypeVar('_FieldOrbitHermiteInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldOrbitHermiteInterpolator(AbstractFieldOrbitInterpolator[_FieldOrbitHermiteInterpolator__KK], typing.Generic[_FieldOrbitHermiteInterpolator__KK]):
    """
    public class FieldOrbitHermiteInterpolator<KK extends :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<KK>> extends :class:`~org.orekit.orbits.AbstractFieldOrbitInterpolator`<KK>
    
        Class using a Hermite interpolator to interpolate orbits.
    
        Depending on given sample orbit type, the interpolation may differ :
    
          - For Keplerian, Circular and Equinoctial orbits, the interpolated instance is created by polynomial Hermite
            interpolation, using derivatives when available.
          - For Cartesian orbits, the interpolated instance is created using the cartesian derivatives filter given at instance
            construction. Hence, it will fall back to Lagrange interpolation if this instance has been designed to not use
            derivatives.
    
    
        In any case, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid
        `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN
        appearing).
    
        Also see:
            :class:`~org.orekit.orbits.FieldOrbit`,
            :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.FieldHermiteInterpolator?is`
    """
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    def getPVAFilter(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get filter for derivatives from the sample to use in position-velocity-acceleration interpolation.
        
            Returns:
                filter for derivatives from the sample to use in position-velocity-acceleration interpolation
        
        
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

class KeplerianOrbit(Orbit, PositionAngleBased):
    """
    public class KeplerianOrbit extends :class:`~org.orekit.orbits.Orbit` implements :class:`~org.orekit.orbits.PositionAngleBased`
    
        This class handles traditional Keplerian orbital parameters.
    
        The parameters used internally are the classical Keplerian elements:
    
        .. code-block: java
        
             a
             e
             i
             ω
             Ω
             v
           
        where ω stands for the Perigee Argument, Ω stands for the Right Ascension of the Ascending Node and v stands for the
        true anomaly.
    
        This class supports hyperbolic orbits, using the convention that semi major axis is negative for such orbits (and of
        course eccentricity is greater than 1).
    
        When orbit is either equatorial or circular, some Keplerian elements (more precisely ω and Ω) become ambiguous so this
        class should not be used for such orbits. For this reason, :class:`~org.orekit.orbits.EquinoctialOrbit` is the
        recommended way to represent orbits.
    
        The instance :code:`KeplerianOrbit` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.orbits.CircularOrbit`,
            :class:`~org.orekit.orbits.CartesianOrbit`, :class:`~org.orekit.orbits.EquinoctialOrbit`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double13: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngleType: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, positionAngleType: PositionAngleType, positionAngleType2: PositionAngleType, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double7: float): ...
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, positionAngleType: PositionAngleType, double: float, doubleArray: typing.List[float]) -> None:
        """
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.addKeplerContribution` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getADot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                semi-major axis derivative (m/s)
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getAnomaly(self, positionAngleType: PositionAngleType) -> float:
        """
            Get the anomaly.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                anomaly (rad)
        
        
        """
        ...
    def getAnomalyDot(self, positionAngleType: PositionAngleType) -> float:
        """
            Get the anomaly derivative.
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the angle
        
            Returns:
                anomaly derivative (rad/s)
        
            Since:
                9.0
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.getCachedPositionAngleType` in
                interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                cached type of position angle
        
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
            Get the first component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEx` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
            Get the first component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialExDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                first component of the equinoctial eccentricity vector derivative
        
            Also see:
                :meth:`~org.orekit.orbits.Orbit.hasDerivatives`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEy` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
            Get the second component of the equinoctial eccentricity vector derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getEquinoctialEyDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                second component of the equinoctial eccentricity vector derivative
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
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
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
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
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                true if and only if holding rates
        
        
        """
        ...
    def removeRates(self) -> 'KeplerianOrbit':
        """
            Create a new instance such that :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` is false.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.removeRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                new object without rates
        
        
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
                :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
            Returns:
                a string representation of this object
        
        
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

class OrbitBlender(AbstractOrbitInterpolator):
    """
    public class OrbitBlender extends :class:`~org.orekit.orbits.AbstractOrbitInterpolator`
    
        Orbit blender.
    
        Its purpose is to interpolate orbit state between tabulated orbit states using the concept of blending, exposed in :
        "Efficient Covariance Interpolation using Blending of Approximate State Error Transitions" by Sergei Tanygin, and
        applying it to orbit states instead of covariances.
    
        It propagates tabulated values to the interpolating time using given propagator and then blend each propagated states
        using a smoothstep function. It gives especially good results as explained
        :class:`~org.orekit.orbits.https:.orekit.org.doc.technical` compared to Hermite interpolation when time steps between
        tabulated values get significant (In LEO, > 10 mn for example).
    
        **In most cases, an analytical propagator would be used to quickly fill the gap between tabulated values and recreate a
        dense ephemeris**.
    
        However, a fully configured and accurate numerical propagator can be used to recreate an even more precise ephemeris in
        case the initial tabulated values were obtained from an external source.
    
        Note that in the current implementation, the returned blended orbit is necessarily Cartesian.
    
        Since:
            12.0
    
        Also see:
            :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory?is`,
            :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction?is`,
            :class:`~org.orekit.propagation.Propagator`, :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    """
    def __init__(self, smoothStepFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction, propagator: org.orekit.propagation.Propagator, frame: org.orekit.frames.Frame): ...

class OrbitHermiteInterpolator(AbstractOrbitInterpolator):
    """
    public class OrbitHermiteInterpolator extends :class:`~org.orekit.orbits.AbstractOrbitInterpolator`
    
        Class using a Hermite interpolator to interpolate orbits.
    
        Depending on given sample orbit type, the interpolation may differ :
    
          - For Keplerian, Circular and Equinoctial orbits, the interpolated instance is created by polynomial Hermite
            interpolation, using derivatives when available.
          - For Cartesian orbits, the interpolated instance is created using the cartesian derivatives filter given at instance
            construction. Hence, it will fall back to Lagrange interpolation if this instance has been designed to not use
            derivatives.
    
    
        In any case, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid
        `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN
        appearing).
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`,
            :class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`
    """
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    def getPVAFilter(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get filter for derivatives from the sample to use in position-velocity-acceleration interpolation.
        
            Returns:
                filter for derivatives from the sample to use in position-velocity-acceleration interpolation
        
        
        """
        ...

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
    def addKeplerContribution(self, positionAngleType: PositionAngleType, double: float, doubleArray: typing.List[float]) -> None:
        """
            Description copied from class: :meth:`~org.orekit.orbits.Orbit.addKeplerContribution`
            Add the contribution of the Keplerian motion to parameters derivatives
        
            This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the
            orbital state.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.addKeplerContribution` in class :class:`~org.orekit.orbits.Orbit`
        
            Parameters:
                type (:class:`~org.orekit.orbits.PositionAngleType`): type of the position angle in the state
                gm (double): attraction coefficient to use
                pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be *added* to the array components, as the
                    array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def computeJacobianEccentricWrtCartesian(self) -> typing.List[typing.List[float]]:
        """
            Compute the Jacobian of the orbital parameters with eccentric angle with respect to the Cartesian parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of parameter i of the orbit with respect to Cartesian coordinate j.
            This means each row correspond to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates
            x, y, z, xDot, yDot and zDot.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.computeJacobianEccentricWrtCartesian` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                6x6 Jacobian matrix
        
            Also see:
                :meth:`~org.orekit.orbits.PythonOrbit.computeJacobianMeanWrtCartesian`,
                :meth:`~org.orekit.orbits.PythonOrbit.computeJacobianTrueWrtCartesian`
        
        
        """
        ...
    def computeJacobianMeanWrtCartesian(self) -> typing.List[typing.List[float]]:
        """
            Compute the Jacobian of the orbital parameters with mean angle with respect to the Cartesian parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of parameter i of the orbit with respect to Cartesian coordinate j.
            This means each row correspond to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates
            x, y, z, xDot, yDot and zDot.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.computeJacobianMeanWrtCartesian` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                6x6 Jacobian matrix
        
            Also see:
                :meth:`~org.orekit.orbits.PythonOrbit.computeJacobianEccentricWrtCartesian`,
                :meth:`~org.orekit.orbits.PythonOrbit.computeJacobianTrueWrtCartesian`
        
        
        """
        ...
    def computeJacobianTrueWrtCartesian(self) -> typing.List[typing.List[float]]:
        """
            Compute the Jacobian of the orbital parameters with true angle with respect to the Cartesian parameters.
        
            Element :code:`jacobian[i][j]` is the derivative of parameter i of the orbit with respect to Cartesian coordinate j.
            This means each row correspond to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates
            x, y, z, xDot, yDot and zDot.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.computeJacobianTrueWrtCartesian` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                6x6 Jacobian matrix
        
            Also see:
                :meth:`~org.orekit.orbits.PythonOrbit.computeJacobianMeanWrtCartesian`,
                :meth:`~org.orekit.orbits.PythonOrbit.computeJacobianEccentricWrtCartesian`
        
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
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
                E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
            Get the eccentric longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLEDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
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
                M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
            Get the mean longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLMDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
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
                v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
            Get the true longitude argument derivative.
        
            If the orbit was created without derivatives, the value returned is
            :meth:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double.html?is`.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.getLvDot` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
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
    def initPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Description copied from class: :meth:`~org.orekit.orbits.Orbit.initPosition`
            Compute the position coordinates from the canonical parameters.
        
            Specified by:
                :meth:`~org.orekit.orbits.Orbit.initPosition` in class :class:`~org.orekit.orbits.Orbit`
        
            Returns:
                computed position coordinates
        
        
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

class PythonPositionAngleBased(PositionAngleBased):
    """
    public class PythonPositionAngleBased extends :class:`~org.orekit.orbits.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.orbits.PositionAngleBased`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
            Get the cached :class:`~org.orekit.orbits.PositionAngleType`.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.getCachedPositionAngleType` in
                interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                cached type of position angle
        
        
        """
        ...
    def hasRates(self) -> bool:
        """
            Tells whether the instance holds rates (first-order time derivatives) for dependent variables.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                true if and only if holding rates
        
        
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
    def removeRates(self) -> PositionAngleBased:
        """
            Create a new instance such that :meth:`~org.orekit.orbits.PositionAngleBased.hasRates` is false.
        
            Specified by:
                :meth:`~org.orekit.orbits.PositionAngleBased.removeRates` in interface :class:`~org.orekit.orbits.PositionAngleBased`
        
            Returns:
                new object without rates
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.orbits")``.

    AbstractFieldOrbitInterpolator: typing.Type[AbstractFieldOrbitInterpolator]
    AbstractOrbitInterpolator: typing.Type[AbstractOrbitInterpolator]
    CR3BPDifferentialCorrection: typing.Type[CR3BPDifferentialCorrection]
    CartesianOrbit: typing.Type[CartesianOrbit]
    CircularLatitudeArgumentUtility: typing.Type[CircularLatitudeArgumentUtility]
    CircularOrbit: typing.Type[CircularOrbit]
    EquinoctialLongitudeArgumentUtility: typing.Type[EquinoctialLongitudeArgumentUtility]
    EquinoctialOrbit: typing.Type[EquinoctialOrbit]
    FieldCartesianOrbit: typing.Type[FieldCartesianOrbit]
    FieldCircularLatitudeArgumentUtility: typing.Type[FieldCircularLatitudeArgumentUtility]
    FieldCircularOrbit: typing.Type[FieldCircularOrbit]
    FieldEquinoctialLongitudeArgumentUtility: typing.Type[FieldEquinoctialLongitudeArgumentUtility]
    FieldEquinoctialOrbit: typing.Type[FieldEquinoctialOrbit]
    FieldKeplerianAnomalyUtility: typing.Type[FieldKeplerianAnomalyUtility]
    FieldKeplerianOrbit: typing.Type[FieldKeplerianOrbit]
    FieldOrbit: typing.Type[FieldOrbit]
    FieldOrbitBlender: typing.Type[FieldOrbitBlender]
    FieldOrbitHermiteInterpolator: typing.Type[FieldOrbitHermiteInterpolator]
    HaloOrbit: typing.Type[HaloOrbit]
    KeplerianAnomalyUtility: typing.Type[KeplerianAnomalyUtility]
    KeplerianMotionCartesianUtility: typing.Type[KeplerianMotionCartesianUtility]
    KeplerianOrbit: typing.Type[KeplerianOrbit]
    LibrationOrbit: typing.Type[LibrationOrbit]
    LibrationOrbitFamily: typing.Type[LibrationOrbitFamily]
    LibrationOrbitType: typing.Type[LibrationOrbitType]
    LyapunovOrbit: typing.Type[LyapunovOrbit]
    Orbit: typing.Type[Orbit]
    OrbitBlender: typing.Type[OrbitBlender]
    OrbitHermiteInterpolator: typing.Type[OrbitHermiteInterpolator]
    OrbitType: typing.Type[OrbitType]
    PositionAngleBased: typing.Type[PositionAngleBased]
    PositionAngleType: typing.Type[PositionAngleType]
    PythonLibrationOrbit: typing.Type[PythonLibrationOrbit]
    PythonOrbit: typing.Type[PythonOrbit]
    PythonPositionAngleBased: typing.Type[PythonPositionAngleBased]
    RichardsonExpansion: typing.Type[RichardsonExpansion]
    WalkerConstellation: typing.Type[WalkerConstellation]
    WalkerConstellationSlot: typing.Type[WalkerConstellationSlot]
    class-use: org.orekit.orbits.class-use.__module_protocol__
