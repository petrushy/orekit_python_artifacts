
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.estimation.measurements
import org.orekit.frames
import org.orekit.orbits
import org.orekit.time
import org.orekit.utils
import typing



class IodGauss:
    """
    Gauss angles-only Initial Orbit Determination (IOD) algorithm.
    
    The algorithm works best when the separation between observation is less than about 60°. The method performs remarkably well when the data is separated by 10° or less. An orbit is determined from three lines of sight w.r.t. their respective observers inertial positions vectors.
    
    References: Vallado, D., Fundamentals of Astrodynamics and Applications Curtis, Orbital Mechanics for Engineering Students
    
    Since:
        12.0
    """
    def __init__(self, mu: float):
        """
        Constructor.
        
        Parameters:
            mu (double): gravitational constant
        
        
        """
        ...
    @typing.overload
    def estimate(self, outputFrame: org.orekit.frames.Frame, obsP1: org.hipparchus.geometry.euclidean.threed.Vector3D, obsDate1: org.orekit.time.AbsoluteDate, los1: org.hipparchus.geometry.euclidean.threed.Vector3D, obsP2: org.hipparchus.geometry.euclidean.threed.Vector3D, obsDate2: org.orekit.time.AbsoluteDate, los2: org.hipparchus.geometry.euclidean.threed.Vector3D, obsP3: org.hipparchus.geometry.euclidean.threed.Vector3D, obsDate3: org.orekit.time.AbsoluteDate, los3: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.orbits.Orbit:
        """
        Estimate and orbit based on Gauss Intial Orbit Determination method.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            obsP1 (Vector3D): observer position at obsDate1
            obsDate1 (AbsoluteDate): date of the 1st observation
            los1 (Vector3D): line of sight unit vector at obsDate1
            obsP2 (Vector3D): observer position at obsDate2
            obsDate2 (AbsoluteDate): date of the 2nd observation
            los2 (Vector3D): line of sight unit vector at obsDate2
            obsP3 (Vector3D): observer position at obsDate3
            obsDate3 (AbsoluteDate): date of the 3rd observation
            los3 (Vector3D): line of sight unit vector at obsDate3
        
        Returns:
            an estimate of the orbit at the central date obsDate2 or null if no estimate is possible with the given data
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl) -> org.orekit.orbits.Orbit:
        """
        Estimate and orbit based on Gauss Intial Orbit Determination method.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            azEl1 (AngularAzEl): first angular observation
            azEl2 (AngularAzEl): second angular observation
            azEl3 (AngularAzEl): third angular observation
        
        Returns:
            an estimate of the orbit at the central date or null if no estimate is possible with the given data
        
        Estimate and orbit based on Gauss Intial Orbit Determination method.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            raDec1 (AngularRaDec): first angular observation
            raDec2 (AngularRaDec): second angular observation
            raDec3 (AngularRaDec): third angular observation
        
        Returns:
            an estimate of the orbit at the central date or null if no estimate is possible with the given data
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec) -> org.orekit.orbits.Orbit: ...

class IodGibbs:
    """
    Gibbs position-based Initial Orbit Determination (IOD) algorithm.
    
    An orbit is determined from three position vectors. This method requires the vectors to be coplanar. Orekit uses a default coplanar threshold of 5°. Reference: Vallado, D., Fundamentals of Astrodynamics and Applications
    
    Since:
        8.0
    """
    def __init__(self, mu: float):
        """
        Creator.
        
        Parameters:
            mu (double): gravitational constant
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, r1: org.hipparchus.geometry.euclidean.threed.Vector3D, date1: org.orekit.time.AbsoluteDate, r2: org.hipparchus.geometry.euclidean.threed.Vector3D, date2: org.orekit.time.AbsoluteDate, r3: org.hipparchus.geometry.euclidean.threed.Vector3D, date3: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
        Parameters:
            frame (Frame): measure frame
            r1 (Vector3D): position 1 measured in frame
            date1 (AbsoluteDate): date of measure 1
            r2 (Vector3D): position 2 measured in frame
            date2 (AbsoluteDate): date of measure 2
            r3 (Vector3D): position 3 measured in frame
            date3 (AbsoluteDate): date of measure 3
        
        Returns:
            an initial orbit estimation at the central date (i.e., date of the second position measurement)
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pV: org.orekit.estimation.measurements.PV, pV2: org.orekit.estimation.measurements.PV, pV3: org.orekit.estimation.measurements.PV) -> org.orekit.orbits.Orbit:
        """
        Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
        Parameters:
            frame (Frame): measurements frame
            p1 (Position): First position measurement
            p2 (Position): Second position measurement
            p3 (Position): Third position measurement
        
        Returns:
            an initial orbit estimation at the central date (i.e., date of the second position measurement)
        
        Since:
            11.0
        
        Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
        Parameters:
            frame (Frame): measure frame
            pv1 (PV): PV measure 1 taken in frame
            pv2 (PV): PV measure 2 taken in frame
            pv3 (PV): PV measure 3 taken in frame
        
        Returns:
            an initial orbit estimation at the central date (i.e., date of the second PV measurement)
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position, position3: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.Orbit: ...

class IodGooding:
    """
    Gooding angles only Initial Orbit Determination (IOD) algorithm, assuming Keplerian motion.
    
    An orbit is determined from three lines of sight w.r.t. their respective observers inertial positions vectors. Gooding algorithm can handle multiple satellite's revolutions. Reference: Gooding, R.H., A New Procedure for Orbit Determination Based on Three Lines of Sight (Angles only), Technical Report 93004, April 1993
    
    Since:
        8.0
    """
    def __init__(self, mu: float):
        """
        Constructor.
        
        Parameters:
            mu (double): gravitational constant
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, double: float, double2: float) -> org.orekit.orbits.Orbit:
        """
        Estimate orbit from three line of sight.
        
        This signature assumes there was less than an half revolution between start and final date
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            O1 (Vector3D): Observer position 1
            O2 (Vector3D): Observer position 2
            O3 (Vector3D): Observer position 3
            lineOfSight1 (Vector3D): line of sight 1
            dateObs1 (AbsoluteDate): date of observation 1
            lineOfSight2 (Vector3D): line of sight 2
            dateObs2 (AbsoluteDate): date of observation 1
            lineOfSight3 (Vector3D): line of sight 3
            dateObs3 (AbsoluteDate): date of observation 1
            rho1init (double): initial guess of the range problem. range 1, in meters
            rho3init (double): initial guess of the range problem. range 3, in meters
        
        Returns:
            an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
        Estimate orbit from three line of sight.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            O1 (Vector3D): Observer position 1
            O2 (Vector3D): Observer position 2
            O3 (Vector3D): Observer position 3
            lineOfSight1 (Vector3D): line of sight 1
            dateObs1 (AbsoluteDate): date of observation 1
            lineOfSight2 (Vector3D): line of sight 2
            dateObs2 (AbsoluteDate): date of observation 2
            lineOfSight3 (Vector3D): line of sight 3
            dateObs3 (AbsoluteDate): date of observation 3
            rho1init (double): initial guess of the range problem. range 1, in meters
            rho3init (double): initial guess of the range problem. range 3, in meters
            nRev (int): number of complete revolutions between observation1 and 3
            direction (boolean): true if posigrade (short way)
        
        Returns:
            an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, double: float, double2: float, int: int, boolean: bool) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl) -> org.orekit.orbits.Orbit:
        """
        This method doesn't need initial guesses of range values since they are computed by a Gauss algorithm.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            azEl1 (AngularAzEl): first angular observation
            azEl2 (AngularAzEl): second angular observation
            azEl3 (AngularAzEl): third angular observation
        
        Returns:
            an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            13.0
        
        Estimate orbit from three angular (i.e., azimuth - elevation) observations.
        
        This method doesn't need initial guesses of range values since they are computed by a Gauss algorithm.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            azEl1 (AngularAzEl): first angular observation
            azEl2 (AngularAzEl): second angular observation
            azEl3 (AngularAzEl): third angular observation
            nRev (int): number of complete revolutions between observation 1 and 3
            direction (boolean): true if posigrade (short way)
        
        Returns:
            an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            13.0
        
        Estimate orbit from three angular observations.
        
        This signature assumes there was less than an half revolution between start and final date
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            azEl1 (AngularAzEl): first angular observation
            azEl2 (AngularAzEl): second angular observation
            azEl3 (AngularAzEl): third angular observation
            rho1init (double): initial guess of the range problem. range 1, in meters
            rho3init (double): initial guess of the range problem. range 3, in meters
        
        Returns:
            an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            12.0
        
        Estimate orbit from three angular observations.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            azEl1 (AngularAzEl): first angular observation
            azEl2 (AngularAzEl): second angular observation
            azEl3 (AngularAzEl): third angular observation
            rho1init (double): initial guess of the range problem. range 1, in meters
            rho3init (double): initial guess of the range problem. range 3, in meters
            nRev (int): number of complete revolutions between observation 1 and 3
            direction (boolean): true if posigrade (short way)
        
        Returns:
            an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            11.0
        
        Estimate orbit from three angular (i.e., right ascension - declination) observations.
        
        This method doesn't need initial guesses of range values since they are computed by a Gauss algorithm.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            raDec1 (AngularRaDec): first angular observation
            raDec2 (AngularRaDec): second angular observation
            raDec3 (AngularRaDec): third angular observation
        
        Returns:
            an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            13.0
        
        Estimate orbit from three angular (i.e., right ascension - declination) observations.
        
        This method doesn't need initial guesses of range values since they are computed by a Gauss algorithm.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            raDec1 (AngularRaDec): first angular observation
            raDec2 (AngularRaDec): second angular observation
            raDec3 (AngularRaDec): third angular observation
            nRev (int): number of complete revolutions between observation 1 and 3
            direction (boolean): true if posigrade (short way)
        
        Returns:
            an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            13.0
        
        Estimate orbit from three angular observations.
        
        This signature assumes there was less than an half revolution between start and final date
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            raDec1 (AngularRaDec): first angular observation
            raDec2 (AngularRaDec): second angular observation
            raDec3 (AngularRaDec): third angular observation
            rho1init (double): initial guess of the range problem. range 1, in meters
            rho3init (double): initial guess of the range problem. range 3, in meters
        
        Returns:
            an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            11.0
        
        Estimate orbit from three angular observations.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            raDec1 (AngularRaDec): first angular observation
            raDec2 (AngularRaDec): second angular observation
            raDec3 (AngularRaDec): third angular observation
            rho1init (double): initial guess of the range problem. range 1, in meters
            rho3init (double): initial guess of the range problem. range 3, in meters
            nRev (int): number of complete revolutions between observation 1 and 3
            direction (boolean): true if posigrade (short way)
        
        Returns:
            an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
        Since:
            11.0
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl, double: float, double2: float) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl, double: float, double2: float, int: int, boolean: bool) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl, int: int, boolean: bool) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec, double: float, double2: float) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec, double: float, double2: float, int: int, boolean: bool) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec, int: int, boolean: bool) -> org.orekit.orbits.Orbit: ...
    def getRange1(self) -> float:
        """
        Get range for observation (1).
        
        Returns:
            the range for observation (1)
        
        
        """
        ...
    def getRange2(self) -> float:
        """
        Get range for observation (2).
        
        Returns:
            the range for observation (2)
        
        
        """
        ...
    def getRange3(self) -> float:
        """
        Get range for observation (3).
        
        Returns:
            the range for observation (3)
        
        
        """
        ...

class IodHerrickGibbs:
    """
    HerrickGibbs position-based Initial Orbit Determination (IOD) algorithm.
    
    An orbit is determined from three position vectors. Because Gibbs IOD algorithm is limited when the position vectors are to close to one other, Herrick-Gibbs IOD algorithm is a variation made to address this limitation. Because this method is only approximate, it is not robust as the Gibbs method for other cases.
    
    Since:
        13.1
    
    Also see:
        "Vallado, D., Fundamentals of Astrodynamics and Applications, 4th Edition."
    """
    def __init__(self, mu: float):
        """
        Constructor.
        
        Parameters:
            mu (double): gravitational constant
        
        
        """
        ...
    _estimate_0__T = typing.TypeVar('_estimate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, r1: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimate_0__T], date1: org.orekit.time.FieldAbsoluteDate[_estimate_0__T], r2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimate_0__T], date2: org.orekit.time.FieldAbsoluteDate[_estimate_0__T], r3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_estimate_0__T], date3: org.orekit.time.FieldAbsoluteDate[_estimate_0__T]) -> org.orekit.orbits.FieldOrbit[_estimate_0__T]:
        """
        Give an initial orbit estimation, assuming Keplerian motion.
        
        All observations should be from the same location.
        
        Parameters:
            frame (Frame): measurements frame, used as output orbit frame
            r1 (FieldVector3D<T> r1): position vector 1, expressed in frame
            date1 (FieldAbsoluteDate<T> date1): epoch of position vector 1
            r2 (FieldVector3D<T> r2): position vector 2, expressed in frame
            date2 (FieldAbsoluteDate<T> date2): epoch of position vector 2
            r3 (FieldVector3D<T> r3): position vector 3, expressed in frame
            date3 (FieldAbsoluteDate<T> date3): epoch of position vector 3
        
        Returns:
            an initial orbit estimation at the central date (i.e., date of the second position measurement)
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, r1: org.hipparchus.geometry.euclidean.threed.Vector3D, date1: org.orekit.time.AbsoluteDate, r2: org.hipparchus.geometry.euclidean.threed.Vector3D, date2: org.orekit.time.AbsoluteDate, r3: org.hipparchus.geometry.euclidean.threed.Vector3D, date3: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Give an initial orbit estimation, assuming Keplerian motion.
        
        All observations should be from the same location.
        
        Parameters:
            frame (Frame): measurements frame, used as output orbit frame
            r1 (Vector3D): position vector 1, expressed in frame
            date1 (AbsoluteDate): epoch of position vector 1
            r2 (Vector3D): position vector 2, expressed in frame
            date2 (AbsoluteDate): epoch of position vector 2
            r3 (Vector3D): position vector 3, expressed in frame
            date3 (AbsoluteDate): epoch of position vector 3
        
        Returns:
            an initial orbit estimation at the central date (i.e., date of the second position measurement)
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pV: org.orekit.estimation.measurements.PV, pV2: org.orekit.estimation.measurements.PV, pV3: org.orekit.estimation.measurements.PV) -> org.orekit.orbits.Orbit:
        """
        Give an initial orbit estimation, assuming Keplerian motion.
        
        All observations should be from the same location.
        
        Parameters:
            frame (Frame): measurements frame, used as output orbit frame
            p1 (Position): First position measurement
            p2 (Position): Second position measurement
            p3 (Position): Third position measurement
        
        Returns:
            an initial orbit estimation at the central date (i.e., date of the second position measurement)
        
        Give an initial orbit estimation, assuming Keplerian motion.
        
        All observations should be from the same location.
        
        Parameters:
            frame (Frame): measurements frame, used as output orbit frame
            pv1 (PV): First PV measurement
            pv2 (PV): Second PV measurement
            pv3 (PV): Third PV measurement
        
        Returns:
            an initial orbit estimation at the central date (i.e., date of the second PV measurement)
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position, position3: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.Orbit: ...

class IodLambert:
    """
    Lambert position-based Initial Orbit Determination (IOD) algorithm, assuming Keplerian motion.
    
    An orbit is determined from two position vectors.
    
    Since:
        8.0
    
    Also see:
        LambertSolver
    """
    def __init__(self, mu: float):
        """
        Creator.
        
        Parameters:
            mu (double): gravitational constant
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, posigrade: bool, nRev: int, p1: org.hipparchus.geometry.euclidean.threed.Vector3D, t1: org.orekit.time.AbsoluteDate, p2: org.hipparchus.geometry.euclidean.threed.Vector3D, t2: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Estimate a Keplerian orbit given two position vectors and a duration.
        
        The logic for setting posigrade and nRev is that the sweep angle Δυ travelled by the object between t1 and t2 is 2π nRev +1 - α if posigrade is false and 2π nRev + α if posigrade is true, where α is the separation angle between p1 and p2, which is always computed between 0 and π (because in 3D without a normal reference, vector angles cannot go past π).
        
        This implies that posigrade should be set to true if p2 is located in the half orbit starting at p1 and it should be set to false if p2 is located in the half orbit ending at p1, regardless of the number of periods between t1 and t2, and nRev should be set accordingly.
        
        As an example, if t2 is less than half a period after t1, then posigrade should be true and nRev should be 0. If t2 is more than half a period after t1 but less than one period after t1, posigrade should be false and nRev should be 0.
        
        Parameters:
            frame (Frame): frame
            posigrade (boolean): flag indicating the direction of motion
            nRev (int): number of revolutions
            p1 (Vector3D): position vector 1
            t1 (AbsoluteDate): date of observation 1
            p2 (Vector3D): position vector 2
            t2 (AbsoluteDate): date of observation 2
        
        Returns:
            an initial Keplerian orbit estimate at the first observation date t1
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, pV: org.orekit.estimation.measurements.PV, pV2: org.orekit.estimation.measurements.PV) -> org.orekit.orbits.Orbit:
        """
        Estimate an initial orbit from two position measurements.
        
        The logic for setting posigrade and nRev is that the sweep angle Δυ travelled by the object between t1 and t2 is 2π nRev +1 - α if posigrade is false and 2π nRev + α if posigrade is true, where α is the separation angle between p1 and p2, which is always computed between 0 and π (because in 3D without a normal reference, vector angles cannot go past π).
        
        This implies that posigrade should be set to true if p2 is located in the half orbit starting at p1 and it should be set to false if p2 is located in the half orbit ending at p1, regardless of the number of periods between t1 and t2, and nRev should be set accordingly.
        
        As an example, if t2 is less than half a period after t1, then posigrade should be true and nRev should be 0. If t2 is more than half a period after t1 but less than one period after t1, posigrade should be false and nRev should be 0.
        
        Parameters:
            frame (Frame): measurements frame
            posigrade (boolean): flag indicating the direction of motion
            nRev (int): number of revolutions
            p1 (Position): first position measurement
            p2 (Position): second position measurement
        
        Returns:
            an initial Keplerian orbit estimation at the first observation date t1
        
        Since:
            11.0
        
        Estimate an initial orbit from two PV measurements.
        
        The logic for setting posigrade and nRev is that the sweep angle Δυ travelled by the object between t1 and t2 is 2π nRev +1 - α if posigrade is false and 2π nRev + α if posigrade is true, where α is the separation angle between p1 and p2, which is always computed between 0 and π (because in 3D without a normal reference, vector angles cannot go past π).
        
        This implies that posigrade should be set to true if p2 is located in the half orbit starting at p1 and it should be set to false if p2 is located in the half orbit ending at p1, regardless of the number of periods between t1 and t2, and nRev should be set accordingly.
        
        As an example, if t2 is less than half a period after t1, then posigrade should be true and nRev should be 0. If t2 is more than half a period after t1 but less than one period after t1, posigrade should be false and nRev should be 0.
        
        Parameters:
            frame (Frame): measurements frame
            posigrade (boolean): flag indicating the direction of motion
            nRev (int): number of revolutions
            pv1 (PV): first PV measurement
            pv2 (PV): second PV measurement
        
        Returns:
            an initial Keplerian orbit estimation at the first observation date t1
        
        Since:
            12.0
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.Orbit: ...

class IodLaplace:
    """
    Laplace angles-only Initial Orbit Determination (IOD) algorithm, assuming Keplerian motion.
    
    Laplace algorithm is one of the first method to determine orbits. An orbit is determined from three lines of sight w.r.t. their respective observers inertial positions vectors. For Laplace method, the observer is identical for all observations. Reference: Bate, R., Mueller, D. D., & White, J. E. (1971). Fundamentals of astrodynamics. New York: Dover Publications.
    
    Since:
        10.1
    """
    def __init__(self, mu: float):
        """
        Constructor.
        
        Parameters:
            mu (double): gravitational constant
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl) -> org.orekit.orbits.Orbit:
        """
        Estimate the orbit from three angular observations at the same location.
        
        Parameters:
            outputFrame (Frame): Observer coordinates at time of raDec2
            azEl1 (AngularAzEl): first angular observation
            azEl2 (AngularAzEl): second angular observation
            azEl3 (AngularAzEl): third angular observation
        
        Returns:
            estimate of the orbit at the central date or null if no estimate is possible with the given data
        
        Since:
            12.0
        
        Estimate the orbit from three angular observations at the same location.
        
        Parameters:
            outputFrame (Frame): Observer coordinates at time of raDec2
            raDec1 (AngularRaDec): first angular observation
            raDec2 (AngularRaDec): second angular observation
            raDec3 (AngularRaDec): third angular observation
        
        Returns:
            estimate of the orbit at the central date or null if no estimate is possible with the given data
        
        Since:
            11.0
        
        Estimate orbit from three line of sight angles at the same location.
        
        Parameters:
            outputFrame (Frame): inertial frame for observer coordinates and orbit estimate
            obsPva (PVCoordinates): Observer coordinates at time obsDate2
            obsDate1 (AbsoluteDate): date of observation 1
            los1 (Vector3D): line of sight unit vector 1
            obsDate2 (AbsoluteDate): date of observation 2
            los2 (Vector3D): line of sight unit vector 2
            obsDate3 (AbsoluteDate): date of observation 3
            los3 (Vector3D): line of sight unit vector 3
        
        Returns:
            estimate of the orbit at the central date obsDate2 or null if no estimate is possible with the given data
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pVCoordinates: org.orekit.utils.PVCoordinates, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.orbits.Orbit: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.iod")``.

    IodGauss: typing.Type[IodGauss]
    IodGibbs: typing.Type[IodGibbs]
    IodGooding: typing.Type[IodGooding]
    IodHerrickGibbs: typing.Type[IodHerrickGibbs]
    IodLambert: typing.Type[IodLambert]
    IodLaplace: typing.Type[IodLaplace]
