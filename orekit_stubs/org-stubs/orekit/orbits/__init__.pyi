
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.analysis.polynomials
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.time
import org.orekit.utils
import typing



_AbstractFieldOrbitInterpolator__KK = typing.TypeVar('_AbstractFieldOrbitInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class AbstractFieldOrbitInterpolator(org.orekit.time.AbstractFieldTimeInterpolator['FieldOrbit'[_AbstractFieldOrbitInterpolator__KK], _AbstractFieldOrbitInterpolator__KK], typing.Generic[_AbstractFieldOrbitInterpolator__KK]):
    """
    Abstract class for orbit interpolator.
    """
    def __init__(self, interpolationPoints: int, extrapolationThreshold: float, outputInertialFrame: org.orekit.frames.Frame):
        """
        Constructor.
        
        Parameters:
            interpolationPoints (int): number of interpolation points
            extrapolationThreshold (double): extrapolation threshold beyond which the propagation will fail
            outputInertialFrame (Frame): output inertial frame
        
        
        """
        ...
    def getOutputInertialFrame(self) -> org.orekit.frames.Frame:
        """
        Get output inertial frame.
        
        Returns:
            output inertial frame
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.FieldTimeStamped], typing.Sequence[org.orekit.time.FieldTimeStamped], typing.Set[org.orekit.time.FieldTimeStamped]]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_AbstractFieldOrbitInterpolator__KK], collection: typing.Union[java.util.Collection['FieldOrbit'[_AbstractFieldOrbitInterpolator__KK]], typing.Sequence['FieldOrbit'[_AbstractFieldOrbitInterpolator__KK]], typing.Set['FieldOrbit'[_AbstractFieldOrbitInterpolator__KK]]]) -> 'FieldOrbit'[_AbstractFieldOrbitInterpolator__KK]: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_AbstractFieldOrbitInterpolator__KK], stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...

class AbstractOrbitInterpolator(org.orekit.time.AbstractTimeInterpolator['Orbit']):
    """
    Abstract class for orbit interpolator.
    """
    def __init__(self, interpolationPoints: int, extrapolationThreshold: float, outputInertialFrame: org.orekit.frames.Frame):
        """
        Constructor.
        
        Parameters:
            interpolationPoints (int): number of interpolation points
            extrapolationThreshold (double): extrapolation threshold beyond which the propagation will fail
            outputInertialFrame (Frame): output inertial frame
        
        
        """
        ...
    @staticmethod
    def checkOrbitsConsistency(sample: typing.Union[java.util.Collection['Orbit'], typing.Sequence['Orbit'], typing.Set['Orbit']]) -> None:
        """
        Check orbits consistency by comparing their gravitational parameters µ.
        
        Parameters:
            sample (Collection<Orbit> sample): orbits sample
        
        
        """
        ...
    def getOutputInertialFrame(self) -> org.orekit.frames.Frame:
        """
        Get output inertial frame.
        
        Returns:
            output inertial frame
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection['Orbit'], typing.Sequence['Orbit'], typing.Set['Orbit']]) -> 'Orbit': ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.TimeStamped]) -> org.orekit.time.TimeStamped: ...

class CR3BPDifferentialCorrection:
    """
    Class implementing the differential correction method for Halo or Lyapunov Orbits. It is not a simple differential correction, it uses higher order terms to be more accurate and meet orbits requirements.
    
    Since:
        10.2
    
    Also see:
        "Three-dimensional, periodic, Halo Orbits by Kathleen Connor Howell, Stanford University"
    """
    def __init__(self, firstguess: org.orekit.utils.PVCoordinates, syst: org.orekit.bodies.CR3BPSystem, orbitalPeriod: float):
        """
        Simple Constructor.
        
        Standard constructor using DormandPrince853 integrator for the differential correction
        
        Parameters:
            firstguess (PVCoordinates): first guess PVCoordinates of the point to start differential correction
            syst (CR3BPSystem): CR3BP System considered
            orbitalPeriod (double): Orbital Period of the required orbit
        
        
        """
        ...
    def compute(self, type: 'LibrationOrbitType') -> org.orekit.utils.PVCoordinates:
        """
        Return the real starting PVCoordinates on the Libration orbit type after differential correction from a first guess.
        
        Parameters:
            type (LibrationOrbitType): libration orbit type
        
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
    Utility methods for converting between different latitude arguments used by CircularOrbit.
    
    Since:
        12.1
    
    Also see:
        CircularOrbit
    """
    @staticmethod
    def convertAlpha(oldType: 'PositionAngleType', alpha: float, ex: float, ey: float, newType: 'PositionAngleType') -> float:
        """
        Convert argument of latitude.
        
        Parameters:
            oldType (PositionAngleType): old position angle type
            alpha (double): old value for argument of latitude
            ex (double): ex
            ey (double): ey
            newType (PositionAngleType): new position angle type
        
        Returns:
            convert argument of latitude
        
        Since:
            12.2
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(ex: float, ey: float, alphaE: float) -> float:
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
    def eccentricToTrue(ex: float, ey: float, alphaE: float) -> float:
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
    def meanToEccentric(ex: float, ey: float, alphaM: float) -> float:
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
    def meanToTrue(ex: float, ey: float, alphaM: float) -> float:
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
    def trueToEccentric(ex: float, ey: float, alphaV: float) -> float:
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
    def trueToMean(ex: float, ey: float, alphaV: float) -> float:
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
    Utility methods for converting between different longitude arguments used by EquinoctialOrbit.
    
    Since:
        12.1
    
    Also see:
        EquinoctialOrbit
    """
    @staticmethod
    def convertL(oldType: 'PositionAngleType', l: float, ex: float, ey: float, newType: 'PositionAngleType') -> float:
        """
        Convert argument of longitude.
        
        Parameters:
            oldType (PositionAngleType): old position angle type
            l (double): old value for argument of longitude
            ex (double): ex
            ey (double): ey
            newType (PositionAngleType): new position angle type
        
        Returns:
            converted argument of longitude
        
        Since:
            12.2
        
        
        """
        ...
    @staticmethod
    def eccentricToMean(ex: float, ey: float, lE: float) -> float:
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
    def eccentricToTrue(ex: float, ey: float, lE: float) -> float:
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
    def meanToEccentric(ex: float, ey: float, lM: float) -> float:
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
    def meanToTrue(ex: float, ey: float, lM: float) -> float:
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
    def trueToEccentric(ex: float, ey: float, lV: float) -> float:
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
    def trueToMean(ex: float, ey: float, lV: float) -> float:
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
    Utility methods for converting between different latitude arguments used by FieldCircularOrbit.
    
    Since:
        12.1
    
    Also see:
        FieldCircularOrbit
    """
    _convertAlpha__T = typing.TypeVar('_convertAlpha__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def convertAlpha(oldType: 'PositionAngleType', alpha: _convertAlpha__T, ex: _convertAlpha__T, ey: _convertAlpha__T, newType: 'PositionAngleType') -> _convertAlpha__T:
        """
        Convert argument of latitude.
        
        Parameters:
            oldType (PositionAngleType): old position angle type
            alpha (T): old value for argument of latitude
            ex (T): ex
            ey (T): ey
            newType (PositionAngleType): new position angle type
        
        Returns:
            convert argument of latitude
        
        Since:
            12.2
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(ex: _eccentricToMean__T, ey: _eccentricToMean__T, alphaE: _eccentricToMean__T) -> _eccentricToMean__T:
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
    def eccentricToTrue(ex: _eccentricToTrue__T, ey: _eccentricToTrue__T, alphaE: _eccentricToTrue__T) -> _eccentricToTrue__T:
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
    def meanToEccentric(ex: _meanToEccentric__T, ey: _meanToEccentric__T, alphaM: _meanToEccentric__T) -> _meanToEccentric__T:
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
    def meanToTrue(ex: _meanToTrue__T, ey: _meanToTrue__T, alphaM: _meanToTrue__T) -> _meanToTrue__T:
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
    def trueToEccentric(ex: _trueToEccentric__T, ey: _trueToEccentric__T, alphaV: _trueToEccentric__T) -> _trueToEccentric__T:
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
    def trueToMean(ex: _trueToMean__T, ey: _trueToMean__T, alphaV: _trueToMean__T) -> _trueToMean__T:
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
    Utility methods for converting between different longitude arguments used by FieldEquinoctialOrbit.
    
    Since:
        12.1
    
    Also see:
        FieldEquinoctialOrbit
    """
    _convertL__T = typing.TypeVar('_convertL__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def convertL(oldType: 'PositionAngleType', l: _convertL__T, ex: _convertL__T, ey: _convertL__T, newType: 'PositionAngleType') -> _convertL__T:
        """
        Convert argument of longitude.
        
        Parameters:
            oldType (PositionAngleType): old position angle type
            l (T): old value for argument of longitude
            ex (T): ex
            ey (T): ey
            newType (PositionAngleType): new position angle type
        
        Returns:
            converted argument of longitude
        
        Since:
            12.2
        
        
        """
        ...
    _eccentricToMean__T = typing.TypeVar('_eccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def eccentricToMean(ex: _eccentricToMean__T, ey: _eccentricToMean__T, lE: _eccentricToMean__T) -> _eccentricToMean__T:
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
    def eccentricToTrue(ex: _eccentricToTrue__T, ey: _eccentricToTrue__T, lE: _eccentricToTrue__T) -> _eccentricToTrue__T:
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
    def meanToEccentric(ex: _meanToEccentric__T, ey: _meanToEccentric__T, lM: _meanToEccentric__T) -> _meanToEccentric__T:
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
    def meanToTrue(ex: _meanToTrue__T, ey: _meanToTrue__T, lM: _meanToTrue__T) -> _meanToTrue__T:
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
    def trueToEccentric(ex: _trueToEccentric__T, ey: _trueToEccentric__T, lV: _trueToEccentric__T) -> _trueToEccentric__T:
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
    def trueToMean(ex: _trueToMean__T, ey: _trueToMean__T, lV: _trueToMean__T) -> _trueToMean__T:
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
    Utility methods for converting between different Keplerian anomalies.
    """
    _convertAnomaly__T = typing.TypeVar('_convertAnomaly__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def convertAnomaly(oldType: 'PositionAngleType', anomaly: _convertAnomaly__T, e: _convertAnomaly__T, newType: 'PositionAngleType') -> _convertAnomaly__T:
        """
        Convert anomaly.
        
        Parameters:
            oldType (PositionAngleType): old position angle type
            anomaly (T): old value for anomaly
            e (T): eccentricity
            newType (PositionAngleType): new position angle type
        
        Returns:
            converted anomaly
        
        Since:
            12.2
        
        
        """
        ...
    _ellipticEccentricToMean__T = typing.TypeVar('_ellipticEccentricToMean__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticEccentricToMean(e: _ellipticEccentricToMean__T, E: _ellipticEccentricToMean__T) -> _ellipticEccentricToMean__T:
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
    def ellipticEccentricToTrue(e: _ellipticEccentricToTrue__T, E: _ellipticEccentricToTrue__T) -> _ellipticEccentricToTrue__T:
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
    def ellipticMeanToEccentric(e: _ellipticMeanToEccentric__T, M: _ellipticMeanToEccentric__T) -> _ellipticMeanToEccentric__T:
        """
        Computes the elliptic eccentric anomaly from the elliptic mean anomaly.
        
        The algorithm used here for solving hyperbolic Kepler equation is from Odell, A.W., Gooding, R.H. "Procedures for solving Kepler's equation." Celestial Mechanics 38, 307–334 (1986). https://doi.org/10.1007/BF01238923
        
        Parameters:
            e (T): eccentricity such that 0 ≤ e < 1
            M (T): elliptic mean anomaly (rad)
        
        Returns:
            elliptic eccentric anomaly (rad)
        
        
        """
        ...
    _ellipticMeanToTrue__T = typing.TypeVar('_ellipticMeanToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def ellipticMeanToTrue(e: _ellipticMeanToTrue__T, M: _ellipticMeanToTrue__T) -> _ellipticMeanToTrue__T:
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
    def ellipticTrueToEccentric(e: _ellipticTrueToEccentric__T, v: _ellipticTrueToEccentric__T) -> _ellipticTrueToEccentric__T:
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
    def ellipticTrueToMean(e: _ellipticTrueToMean__T, v: _ellipticTrueToMean__T) -> _ellipticTrueToMean__T:
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
    def hyperbolicEccentricToMean(e: _hyperbolicEccentricToMean__T, H: _hyperbolicEccentricToMean__T) -> _hyperbolicEccentricToMean__T:
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
    def hyperbolicEccentricToTrue(e: _hyperbolicEccentricToTrue__T, H: _hyperbolicEccentricToTrue__T) -> _hyperbolicEccentricToTrue__T:
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
    def hyperbolicMeanToEccentric(e: _hyperbolicMeanToEccentric__T, M: _hyperbolicMeanToEccentric__T) -> _hyperbolicMeanToEccentric__T:
        """
        Computes the hyperbolic eccentric anomaly from the hyperbolic mean anomaly.
        
        The algorithm used here for solving hyperbolic Kepler equation is from Gooding, R.H., Odell, A.W. "The hyperbolic Kepler equation (and the elliptic equation revisited)." Celestial Mechanics 44, 267–282 (1988). https://doi.org/10.1007/BF01235540
        
        Parameters:
            e (T): eccentricity > 1
            M (T): hyperbolic mean anomaly
        
        Returns:
            hyperbolic eccentric anomaly
        
        
        """
        ...
    _hyperbolicMeanToTrue__T = typing.TypeVar('_hyperbolicMeanToTrue__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def hyperbolicMeanToTrue(e: _hyperbolicMeanToTrue__T, M: _hyperbolicMeanToTrue__T) -> _hyperbolicMeanToTrue__T:
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
    def hyperbolicTrueToEccentric(e: _hyperbolicTrueToEccentric__T, v: _hyperbolicTrueToEccentric__T) -> _hyperbolicTrueToEccentric__T:
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
    def hyperbolicTrueToMean(e: _hyperbolicTrueToMean__T, v: _hyperbolicTrueToMean__T) -> _hyperbolicTrueToMean__T:
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
    This class handles orbital parameters.
    
    For user convenience, both the Cartesian and the equinoctial elements are provided by this class, regardless of the canonical representation implemented in the derived class (which may be classical Keplerian elements for example).
    
    The parameters are defined in a frame specified by the user. It is important to make sure this frame is consistent: it probably is inertial and centered on the central body. This information is used for example by some force models.
    
    Instance of this class are guaranteed to be immutable.
    
    Since:
        9.0
    
    Also see:
        Orbit
    """
    def addKeplerContribution(self, type: 'PositionAngleType', gm: _FieldOrbit__T, pDot: typing.Union[typing.List[_FieldOrbit__T], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (FieldOrbit): attraction coefficient to use
            pDot (FieldOrbit[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
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
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldOrbit__T]:
        """
        Get the date of orbital parameters.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date of the orbital parameters
        
        
        """
        ...
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
    def getJacobianWrtCartesian(self, type: 'PositionAngleType', jacobian: typing.Union[typing.List[typing.MutableSequence[_FieldOrbit__T]], jpype.JArray]) -> None:
        """
        Compute the Jacobian of the orbital parameters with respect to the Cartesian parameters.
        
        Element jacobian[i][j] is the derivative of parameter i of the orbit with respect to Cartesian coordinate j. This means each row corresponds to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates x, y, z, xDot, yDot and zDot.
        
        Parameters:
            type (PositionAngleType): type of the position angle to use
            jacobian (FieldOrbit[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                corner will be modified
        
        
        """
        ...
    def getJacobianWrtParameters(self, type: 'PositionAngleType', jacobian: typing.Union[typing.List[typing.MutableSequence[_FieldOrbit__T]], jpype.JArray]) -> None:
        """
        Compute the Jacobian of the Cartesian parameters with respect to the orbital parameters.
        
        Element jacobian[i][j] is the derivative of Cartesian coordinate i of the orbit with respect to orbital parameter j. This means each row corresponds to one Cartesian coordinate x, y, z, xdot, ydot, zdot whereas columns 0 to 5 correspond to the orbital parameters.
        
        Parameters:
            type (PositionAngleType): type of the position angle to use
            jacobian (FieldOrbit[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
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
    @typing.overload
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldOrbit__T]: ...
    @typing.overload
    def getVelocity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbit__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldOrbit__T]: ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if Cartesian coordinates include non-Keplerian acceleration.
        
        Parameters:
            pva (FieldPVCoordinates<T> pva): Cartesian coordinates
            mu (T): central attraction coefficient
        
        Returns:
            true if Cartesian coordinates include non-Keplerian acceleration
        
        public boolean hasNonKeplerianAcceleration()
        
        Check if orbit includes non-Keplerian rates.
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Since:
            13.0
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'FieldOrbit'[_FieldOrbit__T]:
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        Since:
            13.0
        
        
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
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _FieldOrbit__T: ...
    def toOrbit(self) -> 'Orbit':
        """
        Transforms the FieldOrbit instance into an Orbit instance.
        
        Returns:
            Orbit instance with same properties
        
        
        """
        ...

class KeplerianAnomalyUtility:
    """
    Utility methods for converting between different Keplerian anomalies.
    """
    @staticmethod
    def convertAnomaly(oldType: 'PositionAngleType', anomaly: float, e: float, newType: 'PositionAngleType') -> float:
        """
        Convert anomaly.
        
        Parameters:
            oldType (PositionAngleType): old position angle type
            anomaly (double): old value for anomaly
            e (double): eccentricity
            newType (PositionAngleType): new position angle type
        
        Returns:
            converted anomaly
        
        Since:
            12.2
        
        
        """
        ...
    @staticmethod
    def ellipticEccentricToMean(e: float, E: float) -> float:
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
    def ellipticEccentricToTrue(e: float, E: float) -> float:
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
    def ellipticMeanToEccentric(e: float, M: float) -> float:
        """
        Computes the elliptic eccentric anomaly from the elliptic mean anomaly.
        
        The algorithm used here for solving hyperbolic Kepler equation is from Odell, A.W., Gooding, R.H. "Procedures for solving Kepler's equation." Celestial Mechanics 38, 307–334 (1986). https://doi.org/10.1007/BF01238923
        
        Parameters:
            e (double): eccentricity such that 0 ≤ e < 1
            M (double): elliptic mean anomaly (rad)
        
        Returns:
            elliptic eccentric anomaly (rad)
        
        
        """
        ...
    @staticmethod
    def ellipticMeanToTrue(e: float, M: float) -> float:
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
    def ellipticTrueToEccentric(e: float, v: float) -> float:
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
    def ellipticTrueToMean(e: float, v: float) -> float:
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
    def hyperbolicEccentricToMean(e: float, H: float) -> float:
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
    def hyperbolicEccentricToTrue(e: float, H: float) -> float:
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
    def hyperbolicMeanToEccentric(e: float, M: float) -> float:
        """
        Computes the hyperbolic eccentric anomaly from the hyperbolic mean anomaly.
        
        The algorithm used here for solving hyperbolic Kepler equation is from Gooding, R.H., Odell, A.W. "The hyperbolic Kepler equation (and the elliptic equation revisited)." Celestial Mechanics 44, 267–282 (1988). https://doi.org/10.1007/BF01235540
        
        Parameters:
            e (double): eccentricity > 1
            M (double): hyperbolic mean anomaly
        
        Returns:
            hyperbolic eccentric anomaly
        
        
        """
        ...
    @staticmethod
    def hyperbolicMeanToTrue(e: float, M: float) -> float:
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
    def hyperbolicTrueToEccentric(e: float, v: float) -> float:
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
    def hyperbolicTrueToMean(e: float, v: float) -> float:
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
    Utility class to predict position and velocity under Keplerian motion, using lightweight routines based on Cartesian coordinates. Computations do not require a reference frame or an epoch.
    
    Since:
        12.1
    
    Also see:
        KeplerianPropagator,
        FieldKeplerianPropagator, CartesianOrbit,
        FieldCartesianOrbit
    """
    _predictPositionVelocity_0__T = typing.TypeVar('_predictPositionVelocity_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def predictPositionVelocity(dt: _predictPositionVelocity_0__T, position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_predictPositionVelocity_0__T], velocity: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_predictPositionVelocity_0__T], mu: _predictPositionVelocity_0__T) -> org.orekit.utils.FieldPVCoordinates[_predictPositionVelocity_0__T]:
        """
        Method to propagate position and velocity according to Keplerian dynamics. For long time of flights, it is preferable to use KeplerianPropagator.
        
        Parameters:
            dt (T): time of flight
            position (FieldVector3D<T> position): initial position vector
            velocity (FieldVector3D<T> velocity): initial velocity vector
            mu (T): central body gravitational parameter
        
        Returns:
            predicted position-velocity
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def predictPositionVelocity(dt: float, position: org.hipparchus.geometry.euclidean.threed.Vector3D, velocity: org.hipparchus.geometry.euclidean.threed.Vector3D, mu: float) -> org.orekit.utils.PVCoordinates:
        """
        Method to propagate position and velocity according to Keplerian dynamics. For long time of flights, it is preferable to use KeplerianPropagator.
        
        Parameters:
            dt (double): time of flight
            position (Vector3D): initial position vector
            velocity (Vector3D): initial velocity vector
            mu (double): central body gravitational parameter
        
        Returns:
            predicted position-velocity
        
        """
        ...

class LibrationOrbit:
    """
    Base class for libration orbits.
    
    Since:
        10.2
    
    Also see:
        HaloOrbit, LyapunovOrbit
    """
    def applyDifferentialCorrection(self) -> None:
        """
        Apply differential correction.
        
        This will update initialPV and orbitalPeriod parameters.
        """
        ...
    def getInitialPV(self) -> org.orekit.utils.PVCoordinates:
        """
        Return the initialPV on the libration orbit.
        
        This will return the exact initialPV only if you applied a prior differential correction. If you did not, you can use the method applyCorrectionOnPV
        
        Returns:
            initialPV on the libration orbit
        
        
        """
        ...
    def getManifolds(self, s: org.orekit.propagation.SpacecraftState, isStable: bool) -> org.orekit.utils.PVCoordinates:
        """
        Return a manifold direction from one position on a libration Orbit.
        
        Parameters:
            s (SpacecraftState): SpacecraftState with additional equations
            isStable (boolean): true if the manifold is stable
        
        Returns:
            manifold first guess Position-Velocity of a point on the libration Orbit
        
        
        """
        ...
    def getOrbitalPeriod(self) -> float:
        """
        Return the orbital period of the libration orbit.
        
        Returns:
            orbital period of the libration orbit
        
        
        """
        ...

class LibrationOrbitFamily(java.lang.Enum['LibrationOrbitFamily']):
    """
    Enumerate for LibrationOrbit family.
    
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
    def valueOf(name: str) -> 'LibrationOrbitFamily':
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
    def values() -> typing.MutableSequence['LibrationOrbitFamily']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (LibrationOrbitFamily c : LibrationOrbitFamily.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LibrationOrbitType(java.lang.Enum['LibrationOrbitType']):
    """
    Enumerate for LibrationOrbit type.
    
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
    def valueOf(name: str) -> 'LibrationOrbitType':
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
    def values() -> typing.MutableSequence['LibrationOrbitType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (LibrationOrbitType c : LibrationOrbitType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Orbit(org.orekit.utils.ShiftablePVCoordinatesHolder['Orbit']):
    """
    This class handles orbital parameters.
    
    For user convenience, both the Cartesian and the equinoctial elements are provided by this class, regardless of the canonical representation implemented in the derived class (which may be classical Keplerian elements for example).
    
    The parameters are defined in a frame specified by the user. It is important to make sure this frame is consistent: it probably is inertial and centered on the central body. This information is used for example by some force models.
    
    Instance of this class are guaranteed to be immutable.
    """
    def addKeplerContribution(self, type: 'PositionAngleType', gm: float, pDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (double): attraction coefficient to use
            pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            semi-major axis derivative (m/s)
        
        Since:
            9.0
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date of orbital parameters.
        
        Specified by: getDate in interface TimeStamped
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            eccentricity derivative
        
        Since:
            9.0
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        Since:
            9.0
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        Since:
            9.0
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            first component of the inclination vector derivative
        
        Since:
            9.0
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            second component of the inclination vector derivative
        
        Since:
            9.0
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            inclination derivative (rad/s)
        
        Since:
            9.0
        
        
        """
        ...
    def getJacobianWrtCartesian(self, type: 'PositionAngleType', jacobian: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
        Compute the Jacobian of the orbital parameters with respect to the Cartesian parameters.
        
        Element jacobian[i][j] is the derivative of parameter i of the orbit with respect to Cartesian coordinate j. This means each row corresponds to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates x, y, z, xDot, yDot and zDot.
        
        Parameters:
            type (PositionAngleType): type of the position angle to use
            jacobian (double[][]): placeholder 6x6 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x6, only the 6x6 upper left
                corner will be modified
        
        
        """
        ...
    def getJacobianWrtParameters(self, type: 'PositionAngleType', jacobian: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
        Compute the Jacobian of the Cartesian parameters with respect to the orbital parameters.
        
        Element jacobian[i][j] is the derivative of Cartesian coordinate i of the orbit with respect to orbital parameter j. This means each row corresponds to one Cartesian coordinate x, y, z, xdot, ydot, zdot whereas columns 0 to 5 correspond to the orbital parameters.
        
        Parameters:
            type (PositionAngleType): type of the position angle to use
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        Since:
            9.0
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        Since:
            9.0
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        Since:
            9.0
        
        
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
    def getPVCoordinates(self, otherDate: org.orekit.time.AbsoluteDate, otherFrame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            otherDate (AbsoluteDate): current date
            otherFrame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the TimeStampedPVCoordinates in definition frame.
        
        Returns:
            in the definition frame
        
        Also see:
            getPVCoordinates
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, outputFrame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the TimeStampedPVCoordinates in a specified frame.
        
        Parameters:
            outputFrame (Frame): frame in which the position/velocity coordinates shall be computed
        
        Returns:
            in the specified output frame
        
        Also see:
            getPVCoordinates
        
        """
        ...
    @typing.overload
    def getPosition(self, otherDate: org.orekit.time.AbsoluteDate, otherFrame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            otherDate (AbsoluteDate): current date
            otherFrame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        """
        ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position in definition frame.
        
        Returns:
            position in the definition frame
        
        Since:
            12.0
        
        Also see:
            getPVCoordinates
        
        
        """
        ...
    @typing.overload
    def getPosition(self, outputFrame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position in a specified frame.
        
        Parameters:
            outputFrame (Frame): frame in which the position coordinates shall be computed
        
        Returns:
            position in the specified output frame
        
        Since:
            12.0
        
        Also see:
            getPosition
        
        """
        ...
    def getType(self) -> 'OrbitType':
        """
        Get the orbit type.
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if Cartesian coordinates include non-Keplerian acceleration.
        
        Parameters:
            pva (PVCoordinates): Cartesian coordinates
            mu (double): central attraction coefficient
        
        Returns:
            true if Cartesian coordinates include non-Keplerian acceleration
        
        public boolean hasNonKeplerianAcceleration()
        
        Check if orbit includes non-Keplerian rates.
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Since:
            13.0
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'Orbit':
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        Since:
            13.0
        
        
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
    def shiftedBy(self, double: float) -> 'Orbit':
        """
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'Orbit': ...

class OrbitType(java.lang.Enum['OrbitType']):
    """
    Enumerate for Orbit and FieldOrbit parameters types.
    """
    CARTESIAN: typing.ClassVar['OrbitType'] = ...
    CIRCULAR: typing.ClassVar['OrbitType'] = ...
    EQUINOCTIAL: typing.ClassVar['OrbitType'] = ...
    KEPLERIAN: typing.ClassVar['OrbitType'] = ...
    POS_X: typing.ClassVar[str] = ...
    """
    Name for position along X.
    
    Also see:
        constant
    
    
    """
    POS_Y: typing.ClassVar[str] = ...
    """
    Name for position along Y.
    
    Also see:
        constant
    
    
    """
    POS_Z: typing.ClassVar[str] = ...
    """
    Name for position along Z.
    
    Also see:
        constant
    
    
    """
    VEL_X: typing.ClassVar[str] = ...
    """
    Name for velocity along X.
    
    Also see:
        constant
    
    
    """
    VEL_Y: typing.ClassVar[str] = ...
    """
    Name for velocity along Y.
    
    Also see:
        constant
    
    
    """
    VEL_Z: typing.ClassVar[str] = ...
    """
    Name for velocity along Z.
    
    Also see:
        constant
    
    
    """
    A: typing.ClassVar[str] = ...
    """
    Name for semi major axis.
    
    Also see:
        constant
    
    
    """
    ECC: typing.ClassVar[str] = ...
    """
    Name for eccentricity.
    
    Also see:
        constant
    
    
    """
    E_X: typing.ClassVar[str] = ...
    """
    Name for eccentricity vector first component.
    
    Also see:
        constant
    
    
    """
    E_Y: typing.ClassVar[str] = ...
    """
    Name for eccentricity vector second component.
    
    Also see:
        constant
    
    
    """
    INC: typing.ClassVar[str] = ...
    """
    Name for inclination.
    
    Also see:
        constant
    
    
    """
    H_X: typing.ClassVar[str] = ...
    """
    Name for inclination vector first component.
    
    Also see:
        constant
    
    
    """
    H_Y: typing.ClassVar[str] = ...
    """
    Name for inclination vector second component .
    
    Also see:
        constant
    
    
    """
    PA: typing.ClassVar[str] = ...
    """
    Name for perigee argument.
    
    Also see:
        constant
    
    
    """
    RAAN: typing.ClassVar[str] = ...
    """
    Name for right ascension of ascending node.
    
    Also see:
        constant
    
    
    """
    MEAN_ANOM: typing.ClassVar[str] = ...
    """
    Name for mean anomaly.
    
    Also see:
        constant
    
    
    """
    ECC_ANOM: typing.ClassVar[str] = ...
    """
    Name for eccentric anomaly.
    
    Also see:
        constant
    
    
    """
    TRUE_ANOM: typing.ClassVar[str] = ...
    """
    Name for mean anomaly.
    
    Also see:
        constant
    
    
    """
    MEAN_LAT_ARG: typing.ClassVar[str] = ...
    """
    Name for mean argument of latitude.
    
    Also see:
        constant
    
    
    """
    ECC_LAT_ARG: typing.ClassVar[str] = ...
    """
    Name for eccentric argument of latitude.
    
    Also see:
        constant
    
    
    """
    TRUE_LAT_ARG: typing.ClassVar[str] = ...
    """
    Name for mean argument of latitude.
    
    Also see:
        constant
    
    
    """
    MEAN_LON_ARG: typing.ClassVar[str] = ...
    """
    Name for mean argument of longitude.
    
    Also see:
        constant
    
    
    """
    ECC_LON_ARG: typing.ClassVar[str] = ...
    """
    Name for eccentric argument of longitude.
    
    Also see:
        constant
    
    
    """
    TRUE_LON_ARG: typing.ClassVar[str] = ...
    """
    Name for mean argument of longitude.
    
    Also see:
        constant
    
    
    """
    _convertToFieldOrbit__T = typing.TypeVar('_convertToFieldOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def convertToFieldOrbit(self, field: org.hipparchus.Field[_convertToFieldOrbit__T], orbit: Orbit) -> FieldOrbit[_convertToFieldOrbit__T]:
        """
        Convert an orbit to the "Fielded" instance type.
        
        Parameters:
            field (Field<T> field): CalculusField
            orbit (Orbit): base orbit
        
        Returns:
            converted FieldOrbit with type guaranteed to match (so it can be cast safely)
        
        Since:
            12.0
        
        
        """
        ...
    _convertType_0__T = typing.TypeVar('_convertType_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def convertType(self, fieldOrbit: FieldOrbit[_convertType_0__T]) -> FieldOrbit[_convertType_0__T]: ...
    @typing.overload
    def convertType(self, orbit: Orbit) -> Orbit:
        """
        Convert an orbit to the instance type.
        
        The returned orbit is the specified instance itself if its type already matches, otherwise, a new orbit of the proper type created
        
        Parameters:
            orbit (Orbit): orbit to convert
        
        Returns:
            converted orbit with type guaranteed to match (so it can be cast safely)
        
        public abstract <T extends CalculusFieldElement<T>> FieldOrbit<T> convertType (FieldOrbit<T> orbit)
        
        Convert an orbit to the instance type.
        
        The returned orbit is the specified instance itself if its type already matches, otherwise, a new orbit of the proper type created
        
        Parameters:
            orbit (FieldOrbit<T> orbit): orbit to convert
        
        Returns:
            converted orbit with type guaranteed to match (so it can be cast safely)
        
        
        """
        ...
    def getDrivers(self, dP: float, orbit: Orbit, type: 'PositionAngleType') -> org.orekit.utils.ParameterDriversList:
        """
        Get parameters drivers initialized from a reference orbit.
        
        Parameters:
            dP (double): user specified position error
            orbit (Orbit): reference orbit
            type (PositionAngleType): type of the angle
        
        Returns:
            parameters drivers initialized from reference orbit
        
        
        """
        ...
    def isPositionAngleBased(self) -> bool:
        """
        Tells if the orbit type is based on position angles or not.
        
        Returns:
            true if based on PositionAngleType
        
        Since:
            12.0
        
        
        """
        ...
    _mapArrayToOrbit_0__T = typing.TypeVar('_mapArrayToOrbit_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mapArrayToOrbit(self, tArray: typing.Union[typing.List[_mapArrayToOrbit_0__T], jpype.JArray], tArray2: typing.Union[typing.List[_mapArrayToOrbit_0__T], jpype.JArray], positionAngleType: 'PositionAngleType', fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_mapArrayToOrbit_0__T], t3: _mapArrayToOrbit_0__T, frame: org.orekit.frames.Frame) -> FieldOrbit[_mapArrayToOrbit_0__T]: ...
    @typing.overload
    def mapArrayToOrbit(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], positionAngleType: 'PositionAngleType', absoluteDate: org.orekit.time.AbsoluteDate, double3: float, frame: org.orekit.frames.Frame) -> Orbit:
        """
        Convert state array to orbital parameters.
        
        Note that all implementations of this method must be consistent with the implementation of the getJacobianWrtCartesian method for the corresponding orbit type in terms of parameters order and meaning.
        
        Parameters:
            array (double[]): state as a flat array (it can have more than 6 elements, extra elements are ignored)
            arrayDot (double[]): state derivative as a flat array (it can be null, in which case Keplerian motion is assumed, and it can have more than 6
                elements, extra elements are ignored)
            type (PositionAngleType): type of the angle
            date (AbsoluteDate): integration date
            mu (double): central attraction coefficient used for propagation (m³/s²)
            frame (Frame): frame in which integration is performed
        
        Returns:
            orbit corresponding to the flat array as a space dynamics object
        
        public abstract <T extends CalculusFieldElement<T>> FieldOrbit<T> mapArrayToOrbit (T[] array, T[] arrayDot, PositionAngleType type, FieldAbsoluteDate<T> date, T mu, Frame frame)
        
        Convert state array to orbital parameters.
        
        Note that all implementations of this method must be consistent with the implementation of the getJacobianWrtCartesian method for the corresponding orbit type in terms of parameters order and meaning.
        
        Parameters:
            array (T[]): state as a flat array (it can have more than 6 elements, extra elements are ignored)
            arrayDot (T[]): state derivative as a flat array (it can be null, in which case Keplerian motion is assumed,
            type (PositionAngleType): type of the angle
            date (FieldAbsoluteDate<T> date): integration date
            mu (T): central attraction coefficient used for propagation (m³/s²)
            frame (Frame): frame in which integration is performed
        
        Returns:
            orbit corresponding to the flat array as a space dynamics object
        
        
        """
        ...
    _mapOrbitToArray_0__T = typing.TypeVar('_mapOrbitToArray_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def mapOrbitToArray(self, fieldOrbit: FieldOrbit[_mapOrbitToArray_0__T], positionAngleType: 'PositionAngleType', tArray: typing.Union[typing.List[_mapOrbitToArray_0__T], jpype.JArray], tArray2: typing.Union[typing.List[_mapOrbitToArray_0__T], jpype.JArray]) -> None: ...
    @typing.overload
    def mapOrbitToArray(self, orbit: Orbit, positionAngleType: 'PositionAngleType', doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Convert orbit to state array.
        
        Note that all implementations of this method must be consistent with the implementation of the getJacobianWrtCartesian method for the corresponding orbit type in terms of parameters order and meaning.
        
        Parameters:
            orbit (Orbit): orbit to map
            type (PositionAngleType): type of the angle
            stateVector (double[]):             flat array into which the state vector should be mapped (it can have more than 6 elements, extra elements are untouched)
            stateVectorDot (double[]): flat array into which the state vector derivative should be mapped (it can be null if derivatives are not desired, and
                it can have more than 6 elements, extra elements are untouched)
        
        public abstract <T extends CalculusFieldElement<T>> void mapOrbitToArray (FieldOrbit<T> orbit, PositionAngleType type, T[] stateVector, T[] stateVectorDot)
        
        Convert orbit to state array.
        
        Note that all implementations of this method must be consistent with the implementation of the getJacobianWrtCartesian method for the corresponding orbit type in terms of parameters order and meaning.
        
        Parameters:
            orbit (FieldOrbit<T> orbit): orbit to map
            type (PositionAngleType): type of the angle
            stateVector (T[]):             flat array into which the state vector should be mapped (it can have more than 6 elements, extra elements are untouched)
            stateVectorDot (T[]): flat array into which the state vector derivative should be mapped (it can be null if derivatives are not desired, and
                it can have more than 6 elements, extra elements are untouched)
        
        
        """
        ...
    _normalize_0__T = typing.TypeVar('_normalize_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def normalize(self, fieldOrbit: FieldOrbit[_normalize_0__T], fieldOrbit2: FieldOrbit[_normalize_0__T]) -> FieldOrbit[_normalize_0__T]: ...
    @typing.overload
    def normalize(self, orbit: Orbit, reference: Orbit) -> Orbit:
        """
        Normalize one orbit with respect to a reference one.
        
        Given a, angular component ζ of an orbit and the corresponding angular component ζᵣ in the reference orbit, the angular component ζₙ of the normalized orbit will be ζₙ = ζ + 2kπ where k is chosen such that ζᵣ - π ≤ ζₙ ≤ ζᵣ + π. This is intended to avoid too large discontinuities and is particularly useful for normalizing the orbit after an impulsive maneuver with respect to the reference picked up before the maneuver.
        
        Parameters:
            orbit (Orbit): orbit to normalize
            reference (Orbit): reference orbit
        
        Returns:
            normalized orbit (the type is guaranteed to match OrbitType)
        
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
    def valueOf(name: str) -> 'OrbitType':
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
    def values() -> typing.MutableSequence['OrbitType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (OrbitType c : OrbitType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_PositionAngleBased__T = typing.TypeVar('_PositionAngleBased__T')  # <T>
class PositionAngleBased(typing.Generic[_PositionAngleBased__T]):
    """
    This interface represent orbit-like trajectory whose definition is based on a so-called position angle.
    
    Since:
        12.0
    
    Also see:
        PositionAngleType, KeplerianOrbit,
        CircularOrbit, EquinoctialOrbit,
        FieldKeplerianOrbit, FieldCircularOrbit,
        FieldEquinoctialOrbit
    """
    def getCachedPositionAngleType(self) -> 'PositionAngleType':
        """
        Get the cached PositionAngleType.
        
        Returns:
            cached type of position angle
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        Since:
            13.0
        
        
        """
        ...
    def withCachedPositionAngleType(self, positionAngleType: 'PositionAngleType') -> _PositionAngleBased__T:
        """
        Creates a new instance with the provided type used for caching.
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        Since:
            13.0
        
        
        """
        ...
    def withKeplerianRates(self) -> _PositionAngleBased__T:
        """
        Creates a new instance such that hasNonKeplerianRates is false.
        
        Returns:
            new object without rates
        
        Since:
            13.0
        
        
        """
        ...

class PositionAngleType(java.lang.Enum['PositionAngleType']):
    """
    Enumerate for true, eccentric and mean position angles.
    
    Also see:
        KeplerianOrbit, CircularOrbit,
        EquinoctialOrbit, FieldKeplerianOrbit,
        FieldCircularOrbit, FieldEquinoctialOrbit
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
    def valueOf(name: str) -> 'PositionAngleType':
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
    def values() -> typing.MutableSequence['PositionAngleType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (PositionAngleType c : PositionAngleType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RichardsonExpansion:
    """
    Class implementing the Third-Order Richardson Expansion.
    
    Since:
        10.2
    
    Also see:
        "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    def __init__(self, cr3bpSystem: org.orekit.bodies.CR3BPSystem, point: org.orekit.utils.LagrangianPoints):
        """
        Simple Constructor.
        
        Parameters:
            cr3bpSystem (CR3BPSystem): CR3BP System considered
            point (LagrangianPoints): Lagrangian Point considered
        
        
        """
        ...
    def computeHaloFirstGuess(self, azr: float, type: LibrationOrbitFamily, t: float, phi: float) -> org.orekit.utils.PVCoordinates:
        """
        Calculate first Guess.
        
        Parameters:
            azr (double): z-axis Amplitude of the required Halo Orbit, meters
            type (LibrationOrbitFamily): type of the Halo Orbit ("Northern" or "Southern")
            t (double): Orbit time, seconds (must be greater than 0)
            phi (double): Orbit phase, rad
        
        Returns:
            PVCoordinates of the first guess
        
        
        """
        ...
    def computeLyapunovFirstGuess(self, ayr: float, t: float, phi: float) -> org.orekit.utils.PVCoordinates:
        """
        Calculate first Guess.
        
        Parameters:
            ayr (double): x-axis Amplitude of the required Lyapunov Orbit, meters
            t (double): time
            phi (double): Orbit phase, rad
        
        Returns:
            PVCoordinates of the first guess
        
        
        """
        ...
    def getCr3bpSystem(self) -> org.orekit.bodies.CR3BPSystem:
        """
        Get the considered CR3BP system.
        
        Returns:
            CRR3BP system
        
        
        """
        ...
    def getHaloOrbitalPeriod(self, azr: float) -> float:
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
    def getLyapunovOrbitalPeriod(self, axr: float) -> float:
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
    Builder for orbits of satellites forming a Walker constellation.
    
    It manages the 2 patterns:
    
      - Delta, with ascending nodes distributed over 360°
      - Star, with ascending nodes distributed over 180°
    
    
    Since:
        12.1
    """
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, pattern: 'WalkerConstellation.Pattern'): ...
    _buildReferenceSlot__O = typing.TypeVar('_buildReferenceSlot__O', bound=Orbit)  # <O>
    def buildReferenceSlot(self, referenceOrbit: _buildReferenceSlot__O) -> 'WalkerConstellationSlot'[_buildReferenceSlot__O]:
        """
        Create the reference slot, which is satellite 0 in plane 0.
        
        Parameters:
            referenceOrbit (O): orbit of the reference satellite, in getPlane 0 and at
                getSatellite satellite index} 0
        
        Returns:
            build reference slot
        
        Also see:
            buildRegularSlots,
            buildSlot
        
        
        """
        ...
    _buildRegularSlots__O = typing.TypeVar('_buildRegularSlots__O', bound=Orbit)  # <O>
    def buildRegularSlots(self, referenceOrbit: _buildRegularSlots__O) -> java.util.List[java.util.List['WalkerConstellationSlot'[_buildRegularSlots__O]]]:
        """
        Create the regular slots.
        
        This method builds the getT regular satellite, with integer getSatellite. If additional in-orbit spare satellites must be created, the buildSlot method must be called explicitly.
        
        The various orbits are built from the referenceOrbit using plane rotations and shiftedBy. This implies that if orbit does not include non-Keplerian derivatives, a simple Keplerian motion is assumed, which is the intended use case.
        
        Parameters:
            referenceOrbit (O): orbit of the reference satellite, in getPlane 0 and at
                getSatellite satellite index} 0
        
        Returns:
            built orbits as a list of list, organized by planes
        
        Also see:
            buildReferenceSlot,
            buildSlot
        
        
        """
        ...
    _buildSlot__O = typing.TypeVar('_buildSlot__O', bound=Orbit)  # <O>
    def buildSlot(self, existingSlot: 'WalkerConstellationSlot'[_buildSlot__O], plane: int, satellite: float) -> 'WalkerConstellationSlot'[_buildSlot__O]:
        """
        Create one offset slot from an already existing slot.
        
        Parameters:
            existingSlot (WalkerConstellationSlot<O> existingSlot): existing slot (may be the buildReferenceSlot or not)
            plane (int): plane index of the new slot (may be non-integer for in-orbit spare satellites)
            satellite (double): new slot satellite index in plane (may be non-integer if needed)
        
        Returns:
            built slot
        
        Also see:
            buildRegularSlots,
            buildReferenceSlot
        
        
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
    def getPattern(self) -> 'WalkerConstellation.Pattern':
        """
        Get the constellation pattern.
        
        Returns:
            constellation pattern
        
        
        """
        ...
    def getT(self) -> int:
        """
        Get the total number of satellites.
        
        Returns:
            total number of satellites
        
        
        """
        ...
    class Pattern(java.lang.Enum['WalkerConstellation.Pattern']):
        DELTA: typing.ClassVar['WalkerConstellation.Pattern'] = ...
        STAR: typing.ClassVar['WalkerConstellation.Pattern'] = ...
        def getRaanDistribution(self) -> float: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'WalkerConstellation.Pattern': ...
        @staticmethod
        def values() -> typing.MutableSequence['WalkerConstellation.Pattern']: ...

_WalkerConstellationSlot__O = typing.TypeVar('_WalkerConstellationSlot__O', bound=Orbit)  # <O>
class WalkerConstellationSlot(typing.Generic[_WalkerConstellationSlot__O]):
    """
    Container for one satellite slot in a WalkerConstellation.
    
    The getSatellite satellite index for regular satellites is an integer, but it is allowed to have non-integer indices to create slots for in-orbit spare satellites between the regular satellites. As an example, one can consider a 24/3/1 Walker constellation with 8 operational satellites in each of the 3 planes at satellites indices 0, 1, 2, 3, 4, 5, 6 and 7, and put for example 2 additional spares in each plane (hence having a total of 30 satellites), by affecting them to intermediate slots 0.5 and 4.5.
    
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
    This class holds Cartesian orbital parameters.
    
    The parameters used internally are the Cartesian coordinates:
    
      - x
      - y
      - z
      - xDot
      - yDot
      - zDot
    
    contained in PVCoordinates.
    
    Note that the implementation of this class delegates all non-Cartesian related computations (getA, getEquinoctialEx...) to an underlying instance of the EquinoctialOrbit class. This implies that using this class only for analytical computations which are always based on non-Cartesian parameters is perfectly possible but somewhat sub-optimal.
    
    The instance CartesianOrbit is guaranteed to be immutable.
    
    Also see:
        Orbit, KeplerianOrbit,
        CircularOrbit, EquinoctialOrbit
    """
    @typing.overload
    def __init__(self, orbit: Orbit): ...
    @typing.overload
    def __init__(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, type: PositionAngleType, gm: float, pDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class Orbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (double): attraction coefficient to use
            pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> float:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class Orbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getADot in class Orbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getE(self) -> float:
        """
        Get the eccentricity.
        
        Specified by: getE in class Orbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEDot in class Orbit
        
        Returns:
            eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialExDot in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialEyDot in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> float:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class Orbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHxDot in class Orbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> float:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class Orbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
        Get the second component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHyDot in class Orbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> float:
        """
        Get the inclination.
        
        Specified by: getI in class Orbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
        Get the inclination derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getIDot in class Orbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> float:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class Orbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLEDot in class Orbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> float:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class Orbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLMDot in class Orbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> float:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class Orbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLvDot in class Orbit
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
        Get the orbit type.
        
        Specified by: getType in class Orbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class Orbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'CartesianOrbit':
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class Orbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'CartesianOrbit':
        """
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'CartesianOrbit': ...
    def toString(self) -> str:
        """
        Returns a string representation of this Orbit object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...

class CircularOrbit(Orbit, PositionAngleBased['CircularOrbit']):
    """
    This class handles circular orbital parameters.
    
    The parameters used internally are the circular elements which can be related to Keplerian elements as follows:
    
      - a
      - e :sub:`x` = e cos(ω)
      - e :sub:`y` = e sin(ω)
      - i
      - Ω
      - α :sub:`v` = v + ω
    
    where Ω stands for the Right Ascension of the Ascending Node and α :sub:`v` stands for the true latitude argument
    
    The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined, i.e. when orbit is neither equatorial nor circular. When orbit is circular (but not equatorial), the circular parameters are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous. When orbit is equatorial, neither the Keplerian nor the circular parameters can be defined unambiguously. EquinoctialOrbit is the recommended way to represent orbits.
    
    The instance CircularOrbit is guaranteed to be immutable.
    
    Also see:
        Orbit, KeplerianOrbit,
        CartesianOrbit, EquinoctialOrbit
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
    def addKeplerContribution(self, type: PositionAngleType, gm: float, pDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class Orbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (double): attraction coefficient to use
            pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> float:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class Orbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getADot in class Orbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getAlpha(self, type: PositionAngleType) -> float:
        """
        Get the latitude argument.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            latitude argument (rad)
        
        
        """
        ...
    def getAlphaDot(self, type: PositionAngleType) -> float:
        """
        Get the latitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            v + ω true latitude argument derivative (rad/s)
        
        Since:
            9.0
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
        Get the cached PositionAngleType.
        
        Specified by: getCachedPositionAngleType in interface PositionAngleBased
        
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
        
        Specified by: getE in class Orbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEDot in class Orbit
        
        Returns:
            eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialExDot in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialEyDot in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> float:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class Orbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHxDot in class Orbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> float:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class Orbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
        Get the second component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHyDot in class Orbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> float:
        """
        Get the inclination.
        
        Specified by: getI in class Orbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
        Get the inclination derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getIDot in class Orbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> float:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class Orbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLEDot in class Orbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> float:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class Orbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLMDot in class Orbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> float:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class Orbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLvDot in class Orbit
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Returns:
            right ascension of the ascending node derivative (rad/s)
        
        Since:
            9.0
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
        Get the orbit type.
        
        Specified by: getType in class Orbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class Orbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Specified by: hasNonKeplerianRates in interface PositionAngleBased
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'CircularOrbit':
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class Orbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'CircularOrbit':
        """
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'CircularOrbit': ...
    def toString(self) -> str:
        """
        Returns a string representation of this Orbit object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...
    def withCachedPositionAngleType(self, positionAngleType: PositionAngleType) -> 'CircularOrbit':
        """
        Creates a new instance with the provided type used for caching.
        
        Specified by: withCachedPositionAngleType in interface PositionAngleBased
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        
        """
        ...
    def withKeplerianRates(self) -> 'CircularOrbit':
        """
        Creates a new instance such that hasNonKeplerianRates is false.
        
        Specified by: withKeplerianRates in interface PositionAngleBased
        
        Returns:
            new object without rates
        
        
        """
        ...

class EquinoctialOrbit(Orbit, PositionAngleBased['EquinoctialOrbit']):
    """
    This class handles equinoctial orbital parameters, which can support both circular and equatorial orbits.
    
    The parameters used internally are the equinoctial elements which can be related to Keplerian elements as follows:
    
         a ex = e cos(ω + Ω) ey = e sin(ω + Ω) hx = tan(i/2) cos(Ω) hy = tan(i/2) sin(Ω) lv = v + ω + Ω where ω stands for the Perigee Argument and Ω stands for the Right Ascension of the Ascending Node.
    
    The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined, i.e. when orbit is neither equatorial nor circular. When orbit is either equatorial or circular, the equinoctial parameters are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous. For this reason, equinoctial parameters are the recommended way to represent orbits. Note however than the present implementation does not handle non-elliptical cases.
    
    The instance EquinoctialOrbit is guaranteed to be immutable.
    
    Also see:
        Orbit, KeplerianOrbit,
        CircularOrbit, CartesianOrbit
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
    def addKeplerContribution(self, type: PositionAngleType, gm: float, pDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class Orbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (double): attraction coefficient to use
            pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> float:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class Orbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getADot in class Orbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
        Get the cached PositionAngleType.
        
        Specified by: getCachedPositionAngleType in interface PositionAngleBased
        
        Returns:
            cached type of position angle
        
        
        """
        ...
    def getE(self) -> float:
        """
        Get the eccentricity.
        
        Specified by: getE in class Orbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEDot in class Orbit
        
        Returns:
            eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialExDot in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialEyDot in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> float:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class Orbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHxDot in class Orbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> float:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class Orbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
        Get the second component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHyDot in class Orbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> float:
        """
        Get the inclination.
        
        Specified by: getI in class Orbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
        Get the inclination derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getIDot in class Orbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getL(self, type: PositionAngleType) -> float:
        """
        Get the longitude argument.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            longitude argument (rad)
        
        
        """
        ...
    def getLDot(self, type: PositionAngleType) -> float:
        """
        Get the longitude argument derivative.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> float:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class Orbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLEDot in class Orbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> float:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class Orbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLMDot in class Orbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> float:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class Orbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLvDot in class Orbit
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
        Get the orbit type.
        
        Specified by: getType in class Orbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class Orbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Specified by: hasNonKeplerianRates in interface PositionAngleBased
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'EquinoctialOrbit':
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class Orbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'EquinoctialOrbit':
        """
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'EquinoctialOrbit': ...
    def toString(self) -> str:
        """
        Returns a string representation of this equinoctial parameters object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...
    def withCachedPositionAngleType(self, positionAngleType: PositionAngleType) -> 'EquinoctialOrbit':
        """
        Creates a new instance with the provided type used for caching.
        
        Specified by: withCachedPositionAngleType in interface PositionAngleBased
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        
        """
        ...
    def withKeplerianRates(self) -> 'EquinoctialOrbit':
        """
        Creates a new instance such that hasNonKeplerianRates is false.
        
        Specified by: withKeplerianRates in interface PositionAngleBased
        
        Returns:
            new object without rates
        
        
        """
        ...

_FieldCartesianOrbit__T = typing.TypeVar('_FieldCartesianOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianOrbit(FieldOrbit[_FieldCartesianOrbit__T], typing.Generic[_FieldCartesianOrbit__T]):
    """
    This class holds Cartesian orbital parameters.
    
    The parameters used internally are the Cartesian coordinates:
    
      - x
      - y
      - z
      - xDot
      - yDot
      - zDot
    
    contained in PVCoordinates.
    
    Note that the implementation of this class delegates all non-Cartesian related computations (getA, getEquinoctialEx...) to an underlying instance of the EquinoctialOrbit class. This implies that using this class only for analytical computations which are always based on non-Cartesian parameters is perfectly possible but somewhat sub-optimal.
    
    The instance CartesianOrbit is guaranteed to be immutable.
    
    Since:
        9.0
    
    Also see:
        Orbit, KeplerianOrbit,
        CircularOrbit, EquinoctialOrbit
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
    def addKeplerContribution(self, type: PositionAngleType, gm: _FieldCartesianOrbit__T, pDot: typing.Union[typing.List[_FieldCartesianOrbit__T], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class FieldOrbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (FieldCartesianOrbit): attraction coefficient to use
            pDot (FieldCartesianOrbit[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> _FieldCartesianOrbit__T:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class FieldOrbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldCartesianOrbit__T:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getADot in class FieldOrbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getE(self) -> _FieldCartesianOrbit__T:
        """
        Get the eccentricity.
        
        Specified by: getE in class FieldOrbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEDot in class FieldOrbit
        
        Returns:
            eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldCartesianOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialExDot in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldCartesianOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialEyDot in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> _FieldCartesianOrbit__T:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class FieldOrbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getHxDot in class FieldOrbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldCartesianOrbit__T:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class FieldOrbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the second component of the inclination vector derivative.
        
        Specified by: getHyDot in class FieldOrbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldCartesianOrbit__T:
        """
        Get the inclination.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getI in class FieldOrbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the inclination derivative.
        
        Specified by: getIDot in class FieldOrbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldCartesianOrbit__T:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class FieldOrbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLEDot in class FieldOrbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldCartesianOrbit__T:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class FieldOrbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLMDot in class FieldOrbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldCartesianOrbit__T:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class FieldOrbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldCartesianOrbit__T:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLvDot in class FieldOrbit
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
        Get the orbit type.
        
        Specified by: getType in class FieldOrbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class FieldOrbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'FieldCartesianOrbit'[_FieldCartesianOrbit__T]:
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class FieldOrbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldCartesianOrbit'[_FieldCartesianOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldCartesianOrbit__T) -> 'FieldCartesianOrbit'[_FieldCartesianOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'FieldCartesianOrbit'[_FieldCartesianOrbit__T]: ...
    def toOrbit(self) -> CartesianOrbit:
        """
        Description copied from class: toOrbit Transforms the FieldOrbit instance into an Orbit instance.
        
        Specified by: toOrbit in class FieldOrbit
        
        Returns:
            Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
        Returns a string representation of this Orbit object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...

_FieldCircularOrbit__T = typing.TypeVar('_FieldCircularOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCircularOrbit(FieldOrbit[_FieldCircularOrbit__T], PositionAngleBased['FieldCircularOrbit'[_FieldCircularOrbit__T]], typing.Generic[_FieldCircularOrbit__T]):
    """
    This class handles circular orbital parameters.
    
    The parameters used internally are the circular elements which can be related to Keplerian elements as follows:
    
      - a
      - e :sub:`x` = e cos(ω)
      - e :sub:`y` = e sin(ω)
      - i
      - Ω
      - α :sub:`v` = v + ω
    
    where Ω stands for the Right Ascension of the Ascending Node and α :sub:`v` stands for the true latitude argument
    
    The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined, i.e. when orbit is neither equatorial nor circular. When orbit is circular (but not equatorial), the circular parameters are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous. When orbit is equatorial, neither the Keplerian nor the circular parameters can be defined unambiguously. EquinoctialOrbit is the recommended way to represent orbits.
    
    The instance CircularOrbit is guaranteed to be immutable.
    
    Since:
        9.0
    
    Also see:
        Orbit, KeplerianOrbit,
        CartesianOrbit, EquinoctialOrbit
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
    def addKeplerContribution(self, type: PositionAngleType, gm: _FieldCircularOrbit__T, pDot: typing.Union[typing.List[_FieldCircularOrbit__T], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class FieldOrbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (FieldCircularOrbit): attraction coefficient to use
            pDot (FieldCircularOrbit[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> _FieldCircularOrbit__T:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class FieldOrbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldCircularOrbit__T:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getADot in class FieldOrbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getAlpha(self, type: PositionAngleType) -> _FieldCircularOrbit__T:
        """
        Get the latitude argument.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            latitude argument (rad)
        
        
        """
        ...
    def getAlphaDot(self, type: PositionAngleType) -> _FieldCircularOrbit__T:
        """
        Get the latitude argument derivative.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
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
        Get the cached PositionAngleType.
        
        Specified by: getCachedPositionAngleType in interface PositionAngleBased
        
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
        
        Specified by: getE in class FieldOrbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldCircularOrbit__T:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEDot in class FieldOrbit
        
        Returns:
            eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldCircularOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldCircularOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialExDot in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldCircularOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldCircularOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialEyDot in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> _FieldCircularOrbit__T:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class FieldOrbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldCircularOrbit__T:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getHxDot in class FieldOrbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldCircularOrbit__T:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class FieldOrbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldCircularOrbit__T:
        """
        Get the second component of the inclination vector derivative.
        
        Specified by: getHyDot in class FieldOrbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldCircularOrbit__T:
        """
        Get the inclination.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getI in class FieldOrbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldCircularOrbit__T:
        """
        Get the inclination derivative.
        
        Specified by: getIDot in class FieldOrbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldCircularOrbit__T:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class FieldOrbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldCircularOrbit__T:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLEDot in class FieldOrbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldCircularOrbit__T:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class FieldOrbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldCircularOrbit__T:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLMDot in class FieldOrbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldCircularOrbit__T:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class FieldOrbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldCircularOrbit__T:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLvDot in class FieldOrbit
        
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
        
        Specified by: getType in class FieldOrbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class FieldOrbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Specified by: hasNonKeplerianRates in interface PositionAngleBased
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]:
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class FieldOrbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldCircularOrbit__T) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]: ...
    def toOrbit(self) -> CircularOrbit:
        """
        Transforms the FieldOrbit instance into an Orbit instance.
        
        Specified by: toOrbit in class FieldOrbit
        
        Returns:
            Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
        Returns a string representation of this Orbit object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...
    def withCachedPositionAngleType(self, positionAngleType: PositionAngleType) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]:
        """
        Creates a new instance with the provided type used for caching.
        
        Specified by: withCachedPositionAngleType in interface PositionAngleBased
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        
        """
        ...
    def withKeplerianRates(self) -> 'FieldCircularOrbit'[_FieldCircularOrbit__T]:
        """
        Creates a new instance such that hasNonKeplerianRates is false.
        
        Specified by: withKeplerianRates in interface PositionAngleBased
        
        Returns:
            new object without rates
        
        
        """
        ...

_FieldEquinoctialOrbit__T = typing.TypeVar('_FieldEquinoctialOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEquinoctialOrbit(FieldOrbit[_FieldEquinoctialOrbit__T], PositionAngleBased['FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]], typing.Generic[_FieldEquinoctialOrbit__T]):
    """
    This class handles equinoctial orbital parameters, which can support both circular and equatorial orbits.
    
    The parameters used internally are the equinoctial elements which can be related to Keplerian elements as follows:
    
         a ex = e cos(ω + Ω) ey = e sin(ω + Ω) hx = tan(i/2) cos(Ω) hy = tan(i/2) sin(Ω) lv = v + ω + Ω where ω stands for the Perigee Argument and Ω stands for the Right Ascension of the Ascending Node.
    
    The conversion equations from and to Keplerian elements given above hold only when both sides are unambiguously defined, i.e. when orbit is neither equatorial nor circular. When orbit is either equatorial or circular, the equinoctial parameters are still unambiguously defined whereas some Keplerian elements (more precisely ω and Ω) become ambiguous. For this reason, equinoctial parameters are the recommended way to represent orbits. Note however than the present implementation does not handle non-elliptical cases.
    
    The instance EquinoctialOrbit is guaranteed to be immutable.
    
    Since:
        9.0
    
    Also see:
        Orbit, KeplerianOrbit,
        CircularOrbit, CartesianOrbit
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
    def addKeplerContribution(self, type: PositionAngleType, gm: _FieldEquinoctialOrbit__T, pDot: typing.Union[typing.List[_FieldEquinoctialOrbit__T], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class FieldOrbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (FieldEquinoctialOrbit): attraction coefficient to use
            pDot (FieldEquinoctialOrbit[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class FieldOrbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getADot in class FieldOrbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
        Get the cached PositionAngleType.
        
        Specified by: getCachedPositionAngleType in interface PositionAngleBased
        
        Returns:
            cached type of position angle
        
        
        """
        ...
    def getE(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the eccentricity.
        
        Specified by: getE in class FieldOrbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEDot in class FieldOrbit
        
        Returns:
            eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialExDot in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialEyDot in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class FieldOrbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getHxDot in class FieldOrbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class FieldOrbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the second component of the inclination vector derivative.
        
        Specified by: getHyDot in class FieldOrbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the inclination.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getI in class FieldOrbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the inclination derivative.
        
        Specified by: getIDot in class FieldOrbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getL(self, type: PositionAngleType) -> _FieldEquinoctialOrbit__T:
        """
        Get the longitude argument.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            longitude argument (rad)
        
        
        """
        ...
    def getLDot(self, type: PositionAngleType) -> _FieldEquinoctialOrbit__T:
        """
        Get the longitude argument derivative.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class FieldOrbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLEDot in class FieldOrbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class FieldOrbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLMDot in class FieldOrbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class FieldOrbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldEquinoctialOrbit__T:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLvDot in class FieldOrbit
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
        Get the orbit type.
        
        Specified by: getType in class FieldOrbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class FieldOrbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Specified by: hasNonKeplerianRates in interface PositionAngleBased
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]:
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class FieldOrbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldEquinoctialOrbit__T) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]: ...
    def toOrbit(self) -> EquinoctialOrbit:
        """
        Transforms the FieldOrbit instance into an Orbit instance.
        
        Specified by: toOrbit in class FieldOrbit
        
        Returns:
            Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
        Returns a string representation of this equinoctial parameters object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...
    def withCachedPositionAngleType(self, positionAngleType: PositionAngleType) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]:
        """
        Creates a new instance with the provided type used for caching.
        
        Specified by: withCachedPositionAngleType in interface PositionAngleBased
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        
        """
        ...
    def withKeplerianRates(self) -> 'FieldEquinoctialOrbit'[_FieldEquinoctialOrbit__T]:
        """
        Creates a new instance such that hasNonKeplerianRates is false.
        
        Specified by: withKeplerianRates in interface PositionAngleBased
        
        Returns:
            new object without rates
        
        
        """
        ...

_FieldKeplerianOrbit__T = typing.TypeVar('_FieldKeplerianOrbit__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldKeplerianOrbit(FieldOrbit[_FieldKeplerianOrbit__T], PositionAngleBased['FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]], typing.Generic[_FieldKeplerianOrbit__T]):
    """
    This class handles traditional Keplerian orbital parameters.
    
    The parameters used internally are the classical Keplerian elements:
    
         a e i ω Ω v where ω stands for the Perigee Argument, Ω stands for the Right Ascension of the Ascending Node and v stands for the true anomaly.
    
    This class supports hyperbolic orbits, using the convention that semi major axis is negative for such orbits (and of course eccentricity is greater than 1).
    
    When orbit is either equatorial or circular, some Keplerian elements (more precisely ω and Ω) become ambiguous so this class should not be used for such orbits. For this reason, EquinoctialOrbit is the recommended way to represent orbits.
    
    The instance KeplerianOrbit is guaranteed to be immutable.
    
    Since:
        9.0
    
    Also see:
        Orbit, CircularOrbit,
        CartesianOrbit, EquinoctialOrbit
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
    def addKeplerContribution(self, type: PositionAngleType, gm: _FieldKeplerianOrbit__T, pDot: typing.Union[typing.List[_FieldKeplerianOrbit__T], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class FieldOrbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (FieldKeplerianOrbit): attraction coefficient to use
            pDot (FieldKeplerianOrbit[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> _FieldKeplerianOrbit__T:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class FieldOrbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getADot in class FieldOrbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getAnomaly(self, type: PositionAngleType) -> _FieldKeplerianOrbit__T:
        """
        Get the anomaly.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            anomaly (rad)
        
        
        """
        ...
    def getAnomalyDot(self, type: PositionAngleType) -> _FieldKeplerianOrbit__T:
        """
        Get the anomaly derivative.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            anomaly derivative (rad/s)
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
        Get the cached PositionAngleType.
        
        Specified by: getCachedPositionAngleType in interface PositionAngleBased
        
        Returns:
            cached type of position angle
        
        
        """
        ...
    def getE(self) -> _FieldKeplerianOrbit__T:
        """
        Get the eccentricity.
        
        Specified by: getE in class FieldOrbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEDot in class FieldOrbit
        
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
        
        Returns:
            eccentric anomaly derivative (rad/s)
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldKeplerianOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialExDot in class FieldOrbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldKeplerianOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getEquinoctialEyDot in class FieldOrbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> _FieldKeplerianOrbit__T:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class FieldOrbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getHxDot in class FieldOrbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> _FieldKeplerianOrbit__T:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class FieldOrbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the second component of the inclination vector derivative.
        
        Specified by: getHyDot in class FieldOrbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> _FieldKeplerianOrbit__T:
        """
        Get the inclination.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getI in class FieldOrbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the inclination derivative.
        
        Specified by: getIDot in class FieldOrbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> _FieldKeplerianOrbit__T:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class FieldOrbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLEDot in class FieldOrbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> _FieldKeplerianOrbit__T:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class FieldOrbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLMDot in class FieldOrbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> _FieldKeplerianOrbit__T:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class FieldOrbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> _FieldKeplerianOrbit__T:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is null.
        
        Specified by: getLvDot in class FieldOrbit
        
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
        
        Returns:
            true anomaly derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
        Get the orbit type.
        
        Specified by: getType in class FieldOrbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class FieldOrbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Specified by: hasNonKeplerianRates in interface PositionAngleBased
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]:
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class FieldOrbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldKeplerianOrbit__T) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]: ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]: ...
    def toOrbit(self) -> 'KeplerianOrbit':
        """
        Transforms the FieldOrbit instance into an Orbit instance.
        
        Specified by: toOrbit in class FieldOrbit
        
        Returns:
            Orbit instance with same properties
        
        
        """
        ...
    def toString(self) -> str:
        """
        Returns a string representation of this Keplerian parameters object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...
    def withCachedPositionAngleType(self, positionAngleType: PositionAngleType) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]:
        """
        Creates a new instance with the provided type used for caching.
        
        Specified by: withCachedPositionAngleType in interface PositionAngleBased
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        
        """
        ...
    def withKeplerianRates(self) -> 'FieldKeplerianOrbit'[_FieldKeplerianOrbit__T]:
        """
        Creates a new instance such that hasNonKeplerianRates is false.
        
        Specified by: withKeplerianRates in interface PositionAngleBased
        
        Returns:
            new object without rates
        
        
        """
        ...

_FieldOrbitBlender__KK = typing.TypeVar('_FieldOrbitBlender__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldOrbitBlender(AbstractFieldOrbitInterpolator[_FieldOrbitBlender__KK], typing.Generic[_FieldOrbitBlender__KK]):
    """
    Orbit blender.
    
    Its purpose is to interpolate orbit state between tabulated orbit states using the concept of blending, exposed in : "Efficient Covariance Interpolation using Blending of Approximate State Error Transitions" by Sergei Tanygin, and applying it to orbit states instead of covariances.
    
    It propagates tabulated values to the interpolating time using given analytical propagator and then blend each propagated states using a smoothstep function. It gives especially good results as explained technical compared to Hermite interpolation when time steps between tabulated values get significant (In LEO, > 10 mn for example).
    
    Also see:
        SmoothStepFactory,
        FieldSmoothStepFunction
    """
    def __init__(self, blendingFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.FieldSmoothStepFunction[_FieldOrbitBlender__KK], analyticalPropagator: org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator[_FieldOrbitBlender__KK], outputInertialFrame: org.orekit.frames.Frame):
        """
        Default constructor.
        
        Parameters:
            blendingFunction (FieldSmoothStepFunction<FieldOrbitBlender> blendingFunction): 
                class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction?is`
                used for blending
            analyticalPropagator (FieldAbstractAnalyticalPropagator<FieldOrbitBlender> analyticalPropagator): analytical propagator used to propagate tabulated orbits to interpolating time
            outputInertialFrame (Frame): output inertial frame
        
        Raises:
            OrekitException: if output frame is not inertial
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.FieldTimeStamped], typing.Sequence[org.orekit.time.FieldTimeStamped], typing.Set[org.orekit.time.FieldTimeStamped]]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbitBlender__KK], collection: typing.Union[java.util.Collection[FieldOrbit[_FieldOrbitBlender__KK]], typing.Sequence[FieldOrbit[_FieldOrbitBlender__KK]], typing.Set[FieldOrbit[_FieldOrbitBlender__KK]]]) -> FieldOrbit[_FieldOrbitBlender__KK]: ...
    @typing.overload
    def interpolate(self, abstractFieldTimeInterpolator: org.orekit.time.AbstractFieldTimeInterpolator.InterpolationData) -> FieldOrbit[_FieldOrbitBlender__KK]: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldOrbitBlender__KK], stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...

_FieldOrbitHermiteInterpolator__KK = typing.TypeVar('_FieldOrbitHermiteInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldOrbitHermiteInterpolator(AbstractFieldOrbitInterpolator[_FieldOrbitHermiteInterpolator__KK], typing.Generic[_FieldOrbitHermiteInterpolator__KK]):
    """
    Class using a Hermite interpolator to interpolate orbits.
    
    Depending on given sample orbit type, the interpolation may differ :
    
      - For Keplerian, Circular and Equinoctial orbits, the interpolated instance is created by polynomial Hermite
        interpolation, using derivatives when available.
      - For Cartesian orbits, the interpolated instance is created using the cartesian derivatives filter given at instance
        construction. Hence, it will fall back to Lagrange interpolation if this instance has been designed to not use
        derivatives.
    
    In any case, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
    Also see:
        FieldOrbit,
        FieldHermiteInterpolator
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
    Class calculating different parameters of a Halo Orbit.
    
    Since:
        10.2
    """
    @typing.overload
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem, pVCoordinates: org.orekit.utils.PVCoordinates, double: float): ...
    @typing.overload
    def __init__(self, richardsonExpansion: RichardsonExpansion, double: float, librationOrbitFamily: LibrationOrbitFamily): ...

class KeplerianOrbit(Orbit, PositionAngleBased['KeplerianOrbit']):
    """
    This class handles traditional Keplerian orbital parameters.
    
    The parameters used internally are the classical Keplerian elements:
    
         a e i ω Ω v where ω stands for the Perigee Argument, Ω stands for the Right Ascension of the Ascending Node and v stands for the true anomaly.
    
    This class supports hyperbolic orbits, using the convention that semi major axis is negative for such orbits (and of course eccentricity is greater than 1).
    
    When orbit is either equatorial or circular, some Keplerian elements (more precisely ω and Ω) become ambiguous so this class should not be used for such orbits. For this reason, EquinoctialOrbit is the recommended way to represent orbits.
    
    The instance KeplerianOrbit is guaranteed to be immutable.
    
    Also see:
        Orbit, CircularOrbit,
        CartesianOrbit, EquinoctialOrbit
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
    def addKeplerContribution(self, type: PositionAngleType, gm: float, pDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class Orbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (double): attraction coefficient to use
            pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def getA(self) -> float:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class Orbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getADot in class Orbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getAnomaly(self, type: PositionAngleType) -> float:
        """
        Get the anomaly.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            anomaly (rad)
        
        
        """
        ...
    def getAnomalyDot(self, type: PositionAngleType) -> float:
        """
        Get the anomaly derivative.
        
        Parameters:
            type (PositionAngleType): type of the angle
        
        Returns:
            anomaly derivative (rad/s)
        
        Since:
            9.0
        
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
        Get the cached PositionAngleType.
        
        Specified by: getCachedPositionAngleType in interface PositionAngleBased
        
        Returns:
            cached type of position angle
        
        
        """
        ...
    def getE(self) -> float:
        """
        Get the eccentricity.
        
        Specified by: getE in class Orbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEDot in class Orbit
        
        Returns:
            eccentricity derivative
        
        
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
        
        Specified by: getEquinoctialEx in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialExDot in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialEyDot in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> float:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class Orbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHxDot in class Orbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> float:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class Orbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
        Get the second component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHyDot in class Orbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> float:
        """
        Get the inclination.
        
        Specified by: getI in class Orbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
        Get the inclination derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getIDot in class Orbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> float:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class Orbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLEDot in class Orbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> float:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class Orbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLMDot in class Orbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> float:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class Orbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLvDot in class Orbit
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
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
        
        If the orbit was created without derivatives, the value returned is Double.
        
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
        
        Specified by: getType in class Orbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def hasNonKeplerianAcceleration(self) -> bool:
        """
        Check if orbit includes non-Keplerian rates.
        
        Overrides: hasNonKeplerianAcceleration in class Orbit
        
        Returns:
            true if orbit includes non-Keplerian derivatives
        
        Also see:
            getADot, getEquinoctialExDot,
            getEquinoctialEyDot, getHxDot,
            getHyDot, getLEDot,
            getLvDot, getLMDot,
            getEDot, getIDot
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Specified by: hasNonKeplerianRates in interface PositionAngleBased
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> 'KeplerianOrbit':
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class Orbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'KeplerianOrbit':
        """
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'KeplerianOrbit': ...
    def toString(self) -> str:
        """
        Returns a string representation of this Keplerian parameters object.
        
        Overrides: Object in class Object
        
        Returns:
            a string representation of this object
        
        
        """
        ...
    def withCachedPositionAngleType(self, positionAngleType: PositionAngleType) -> 'KeplerianOrbit':
        """
        Creates a new instance with the provided type used for caching.
        
        Specified by: withCachedPositionAngleType in interface PositionAngleBased
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        
        """
        ...
    def withKeplerianRates(self) -> 'KeplerianOrbit':
        """
        Creates a new instance such that hasNonKeplerianRates is false.
        
        Specified by: withKeplerianRates in interface PositionAngleBased
        
        Returns:
            new object without rates
        
        
        """
        ...

class LyapunovOrbit(LibrationOrbit):
    """
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
    Orbit blender.
    
    Its purpose is to interpolate orbit state between tabulated orbit states using the concept of blending, exposed in : "Efficient Covariance Interpolation using Blending of Approximate State Error Transitions" by Sergei Tanygin, and applying it to orbit states instead of covariances.
    
    It propagates tabulated values to the interpolating time using given propagator and then blend each propagated states using a smoothstep function. It gives especially good results as explained technical compared to Hermite interpolation when time steps between tabulated values get significant (In LEO, > 10 mn for example).
    
    In most cases, an analytical propagator would be used to quickly fill the gap between tabulated values and recreate a dense ephemeris.
    
    However, a fully configured and accurate numerical propagator can be used to recreate an even more precise ephemeris in case the initial tabulated values were obtained from an external source.
    
    Note that in the current implementation, the returned blended orbit is necessarily Cartesian.
    
    Since:
        12.0
    
    Also see:
        SmoothStepFactory,
        SmoothStepFunction,
        Propagator, AbstractAnalyticalPropagator
    """
    def __init__(self, blendingFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction, blendingPropagator: org.orekit.propagation.Propagator, outputInertialFrame: org.orekit.frames.Frame):
        """
        Default constructor.
        
        In most cases, an analytical propagator would be used to quickly fill the gap between tabulated values and recreate a dense ephemeris.
        
        However, a fully configured and accurate numerical propagator can be used to recreate an even more precise ephemeris in case the initial tabulated values were obtained from an external source.
        
        Parameters:
            blendingFunction (SmoothStepFunction): 
                class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction?is`
                used for blending
            blendingPropagator (Propagator): propagator used to propagate tabulated orbits to interpolating time
            outputInertialFrame (Frame): output inertial frame
        
        Raises:
            OrekitException: if output frame is not inertial
        
            class:`~org.orekit.orbits.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction?is`
        
        
        """
        ...

class OrbitHermiteInterpolator(AbstractOrbitInterpolator):
    """
    Class using a Hermite interpolator to interpolate orbits.
    
    Depending on given sample orbit type, the interpolation may differ :
    
      - For Keplerian, Circular and Equinoctial orbits, the interpolated instance is created by polynomial Hermite
        interpolation, using derivatives when available.
      - For Cartesian orbits, the interpolated instance is created using the cartesian derivatives filter given at instance
        construction. Hence, it will fall back to Lagrange interpolation if this instance has been designed to not use
        derivatives.
    
    In any case, it should be used only with small number of interpolation points (about 10-20 points) in order to avoid `Runge's phenomenon <http://en.wikipedia.org/wiki/Runge%27s_phenomenon>` and numerical problems (including NaN appearing).
    
    Also see:
        Orbit,
        HermiteInterpolator
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
    def __init__(self, system: org.orekit.bodies.CR3BPSystem, initialPV: org.orekit.utils.PVCoordinates, orbitalPeriod: float):
        """
        Constructor.
        
        Parameters:
            system (CR3BPSystem): CR3BP System considered
            initialPV (PVCoordinates): initial position on a libration Orbit
            orbitalPeriod (double): initial orbital period of the libration Orbit
        
        
        """
        ...
    def applyCorrectionOnPV(self, diff: CR3BPDifferentialCorrection) -> org.orekit.utils.PVCoordinates:
        """
        Apply the differential correction to compute more accurate initial PV.
        
        Specified by: applyCorrectionOnPV in class LibrationOrbit
        
        Parameters:
            diff (CR3BPDifferentialCorrection): cr3bp differential correction
        
        Returns:
            corrected PV coordinates
        
        
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

class PythonOrbit(Orbit):
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate, double: float): ...
    @typing.overload
    def __init__(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame, double: float): ...
    def addKeplerContribution(self, type: PositionAngleType, gm: float, pDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add the contribution of the Keplerian motion to parameters derivatives
        
        This method is used by integration-based propagators to evaluate the part of Keplerian motion to evolution of the orbital state.
        
        Specified by: addKeplerContribution in class Orbit
        
        Parameters:
            type (PositionAngleType): type of the position angle in the state
            gm (double): attraction coefficient to use
            pDot (double[]): array containing orbital state derivatives to update (the Keplerian part must be added to the array components, as the
                array may already contain some non-zero elements corresponding to non-Keplerian parts)
        
        
        """
        ...
    def computeJacobianEccentricWrtCartesian(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the Jacobian of the orbital parameters with eccentric angle with respect to the Cartesian parameters.
        
        Element jacobian[i][j] is the derivative of parameter i of the orbit with respect to Cartesian coordinate j. This means each row correspond to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates x, y, z, xDot, yDot and zDot.
        
        The array returned by this method will not be modified.
        
        Specified by: computeJacobianEccentricWrtCartesian in class Orbit
        
        Returns:
            6x6 Jacobian matrix
        
        Also see:
            computeJacobianMeanWrtCartesian,
            computeJacobianTrueWrtCartesian
        
        
        """
        ...
    def computeJacobianMeanWrtCartesian(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the Jacobian of the orbital parameters with mean angle with respect to the Cartesian parameters.
        
        Element jacobian[i][j] is the derivative of parameter i of the orbit with respect to Cartesian coordinate j. This means each row correspond to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates x, y, z, xDot, yDot and zDot.
        
        The array returned by this method will not be modified.
        
        Specified by: computeJacobianMeanWrtCartesian in class Orbit
        
        Returns:
            6x6 Jacobian matrix
        
        Also see:
            computeJacobianEccentricWrtCartesian,
            computeJacobianTrueWrtCartesian
        
        
        """
        ...
    def computeJacobianTrueWrtCartesian(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the Jacobian of the orbital parameters with true angle with respect to the Cartesian parameters.
        
        Element jacobian[i][j] is the derivative of parameter i of the orbit with respect to Cartesian coordinate j. This means each row correspond to one orbital parameter whereas columns 0 to 5 correspond to the Cartesian coordinates x, y, z, xDot, yDot and zDot.
        
        The array returned by this method will not be modified.
        
        Specified by: computeJacobianTrueWrtCartesian in class Orbit
        
        Returns:
            6x6 Jacobian matrix
        
        Also see:
            computeJacobianMeanWrtCartesian,
            computeJacobianEccentricWrtCartesian
        
        
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
    def getA(self) -> float:
        """
        Get the semi-major axis.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        Specified by: getA in class Orbit
        
        Returns:
            semi-major axis (m)
        
        
        """
        ...
    def getADot(self) -> float:
        """
        Get the semi-major axis derivative.
        
        Note that the semi-major axis is considered negative for hyperbolic orbits.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getADot in class Orbit
        
        Returns:
            semi-major axis derivative (m/s)
        
        
        """
        ...
    def getE(self) -> float:
        """
        Get the eccentricity.
        
        Specified by: getE in class Orbit
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getEDot(self) -> float:
        """
        Get the eccentricity derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEDot in class Orbit
        
        Returns:
            eccentricity derivative
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEx in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialExDot(self) -> float:
        """
        Get the first component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialExDot in class Orbit
        
        Returns:
            first component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector.
        
        Specified by: getEquinoctialEy in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector
        
        
        """
        ...
    def getEquinoctialEyDot(self) -> float:
        """
        Get the second component of the equinoctial eccentricity vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getEquinoctialEyDot in class Orbit
        
        Returns:
            second component of the equinoctial eccentricity vector derivative
        
        
        """
        ...
    def getHx(self) -> float:
        """
        Get the first component of the inclination vector.
        
        Specified by: getHx in class Orbit
        
        Returns:
            first component of the inclination vector
        
        
        """
        ...
    def getHxDot(self) -> float:
        """
        Get the first component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHxDot in class Orbit
        
        Returns:
            first component of the inclination vector derivative
        
        
        """
        ...
    def getHy(self) -> float:
        """
        Get the second component of the inclination vector.
        
        Specified by: getHy in class Orbit
        
        Returns:
            second component of the inclination vector
        
        
        """
        ...
    def getHyDot(self) -> float:
        """
        Get the second component of the inclination vector derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getHyDot in class Orbit
        
        Returns:
            second component of the inclination vector derivative
        
        
        """
        ...
    def getI(self) -> float:
        """
        Get the inclination.
        
        Specified by: getI in class Orbit
        
        Returns:
            inclination (rad)
        
        
        """
        ...
    def getIDot(self) -> float:
        """
        Get the inclination derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getIDot in class Orbit
        
        Returns:
            inclination derivative (rad/s)
        
        
        """
        ...
    def getLE(self) -> float:
        """
        Get the eccentric longitude argument.
        
        Specified by: getLE in class Orbit
        
        Returns:
            E + ω + Ω eccentric longitude argument (rad)
        
        
        """
        ...
    def getLEDot(self) -> float:
        """
        Get the eccentric longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLEDot in class Orbit
        
        Returns:
            d(E + ω + Ω)/dt eccentric longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLM(self) -> float:
        """
        Get the mean longitude argument.
        
        Specified by: getLM in class Orbit
        
        Returns:
            M + ω + Ω mean longitude argument (rad)
        
        
        """
        ...
    def getLMDot(self) -> float:
        """
        Get the mean longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLMDot in class Orbit
        
        Returns:
            d(M + ω + Ω)/dt mean longitude argument derivative (rad/s)
        
        
        """
        ...
    def getLv(self) -> float:
        """
        Get the true longitude argument.
        
        Specified by: getLv in class Orbit
        
        Returns:
            v + ω + Ω true longitude argument (rad)
        
        
        """
        ...
    def getLvDot(self) -> float:
        """
        Get the true longitude argument derivative.
        
        If the orbit was created without derivatives, the value returned is Double.
        
        Specified by: getLvDot in class Orbit
        
        Returns:
            d(v + ω + Ω)/dt true longitude argument derivative (rad/s)
        
        
        """
        ...
    def getType(self) -> OrbitType:
        """
        Get the orbit type.
        
        Specified by: getType in class Orbit
        
        Returns:
            orbit type
        
        
        """
        ...
    def inFrame(self, inertialFrame: org.orekit.frames.Frame) -> Orbit:
        """
        Create a new object representing the same physical orbital state, but attached to a different reference frame. If the new frame is not inertial, an exception will be thrown.
        
        Specified by: inFrame in class Orbit
        
        Parameters:
            inertialFrame (Frame): reference frame of output orbit
        
        Returns:
            orbit with different frame
        
        
        """
        ...
    def initPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute the position/velocity coordinates from the canonical parameters.
        
        Specified by: initPVCoordinates in class Orbit
        
        Returns:
            computed position/velocity coordinates
        
        
        """
        ...
    def initPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the position coordinates from the canonical parameters.
        
        Specified by: initPosition in class Orbit
        
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
    @typing.overload
    def shiftedBy(self, double: float) -> Orbit:
        """
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted orbit.
        
        The orbit can be slightly shifted to close dates. The shifting model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. Shifting is not intended as a replacement for proper orbit propagation but should be sufficient for small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Specified by: shiftedBy in class Orbit
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new orbit, shifted with respect to the instance (which is immutable)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> Orbit: ...

_PythonPositionAngleBased__T = typing.TypeVar('_PythonPositionAngleBased__T')  # <T>
class PythonPositionAngleBased(PositionAngleBased[_PythonPositionAngleBased__T], typing.Generic[_PythonPositionAngleBased__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCachedPositionAngleType(self) -> PositionAngleType:
        """
        Get the cached PositionAngleType.
        
        Specified by: getCachedPositionAngleType in interface PositionAngleBased
        
        Returns:
            cached type of position angle
        
        
        """
        ...
    def hasNonKeplerianRates(self) -> bool:
        """
        Description copied from interface: hasNonKeplerianRates Tells whether the instance holds rates (first-order time derivatives) for dependent variables that are incompatible with Keplerian motion.
        
        Specified by: hasNonKeplerianRates in interface PositionAngleBased
        
        Returns:
            true if and only if holding non-Keplerian rates
        
        
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
    def withCachedPositionAngleType(self, positionAngleType: PositionAngleType) -> _PythonPositionAngleBased__T:
        """
        Description copied from interface: withCachedPositionAngleType Creates a new instance with the provided type used for caching.
        
        Specified by: withCachedPositionAngleType in interface PositionAngleBased
        
        Parameters:
            positionAngleType (PositionAngleType): position angle type to use for caching value
        
        Returns:
            new object
        
        
        """
        ...
    def withKeplerianRates(self) -> _PythonPositionAngleBased__T:
        """
        Description copied from interface: withKeplerianRates Creates a new instance such that hasNonKeplerianRates is false.
        
        Specified by: withKeplerianRates in interface PositionAngleBased
        
        Returns:
            new object without rates
        
        
        """
        ...


class __module_protocol__(Protocol):
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
