
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.geometry.euclidean.threed
import org.orekit.estimation.measurements
import org.orekit.frames
import org.orekit.orbits
import org.orekit.time
import org.orekit.utils
import typing



class IodGauss:
    """
    public class IodGauss extends :class:`~org.orekit.estimation.iod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Gauss angles-only Initial Orbit Determination (IOD) algorithm.
    
        The algorithm works best when the separation between observation is less than about 60°. The method performs remarkably
        well when the data is separated by 10° or less. An orbit is determined from three lines of sight w.r.t. their
        respective observers inertial positions vectors.
    
        References: Vallado, D., Fundamentals of Astrodynamics and Applications Curtis, Orbital Mechanics for Engineering
        Students
    
        Since:
            12.0
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.orbits.Orbit:
        """
            Estimate and orbit based on Gauss Intial Orbit Determination method.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                obsP1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): observer position at obsDate1
                obsDate1 (:class:`~org.orekit.time.AbsoluteDate`): date of the 1st observation
                los1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight unit vector at obsDate1
                obsP2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): observer position at obsDate2
                obsDate2 (:class:`~org.orekit.time.AbsoluteDate`): date of the 2nd observation
                los2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight unit vector at obsDate2
                obsP3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): observer position at obsDate3
                obsDate3 (:class:`~org.orekit.time.AbsoluteDate`): date of the 3rd observation
                los3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight unit vector at obsDate3
        
            Returns:
                an estimate of the orbit at the central date obsDate2 or null if no estimate is possible with the given data
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl) -> org.orekit.orbits.Orbit:
        """
            Estimate and orbit based on Gauss Intial Orbit Determination method.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                azEl1 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): first angular observation
                azEl2 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): second angular observation
                azEl3 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): third angular observation
        
            Returns:
                an estimate of the orbit at the central date or null if no estimate is possible with the given data
        
            Estimate and orbit based on Gauss Intial Orbit Determination method.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
        
            Returns:
                an estimate of the orbit at the central date or null if no estimate is possible with the given data
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec) -> org.orekit.orbits.Orbit: ...

class IodGibbs:
    """
    public class IodGibbs extends :class:`~org.orekit.estimation.iod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Gibbs position-based Initial Orbit Determination (IOD) algorithm.
    
        An orbit is determined from three position vectors. This method requires the vectors to be coplanar. Orekit uses a
        :code:`default coplanar threshold of 5°`. Reference: Vallado, D., Fundamentals of Astrodynamics and Applications
    
        Since:
            8.0
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
            Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measure frame
                r1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): position 1 measured in frame
                date1 (:class:`~org.orekit.time.AbsoluteDate`): date of measure 1
                r2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): position 2 measured in frame
                date2 (:class:`~org.orekit.time.AbsoluteDate`): date of measure 2
                r3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): position 3 measured in frame
                date3 (:class:`~org.orekit.time.AbsoluteDate`): date of measure 3
        
            Returns:
                an initial orbit estimation at the central date (i.e., date of the second position measurement)
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pV: org.orekit.estimation.measurements.PV, pV2: org.orekit.estimation.measurements.PV, pV3: org.orekit.estimation.measurements.PV) -> org.orekit.orbits.Orbit:
        """
            Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measurements frame
                p1 (:class:`~org.orekit.estimation.measurements.Position`): First position measurement
                p2 (:class:`~org.orekit.estimation.measurements.Position`): Second position measurement
                p3 (:class:`~org.orekit.estimation.measurements.Position`): Third position measurement
        
            Returns:
                an initial orbit estimation at the central date (i.e., date of the second position measurement)
        
            Since:
                11.0
        
            Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measure frame
                pv1 (:class:`~org.orekit.estimation.measurements.PV`): PV measure 1 taken in frame
                pv2 (:class:`~org.orekit.estimation.measurements.PV`): PV measure 2 taken in frame
                pv3 (:class:`~org.orekit.estimation.measurements.PV`): PV measure 3 taken in frame
        
            Returns:
                an initial orbit estimation at the central date (i.e., date of the second PV measurement)
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position, position3: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.Orbit: ...

class IodGooding:
    """
    public class IodGooding extends :class:`~org.orekit.estimation.iod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Gooding angles only Initial Orbit Determination (IOD) algorithm, assuming Keplerian motion.
    
        An orbit is determined from three lines of sight w.r.t. their respective observers inertial positions vectors. Gooding
        algorithm can handle multiple satellite's revolutions. Reference: Gooding, R.H., A New Procedure for Orbit Determination
        Based on Three Lines of Sight (Angles only), Technical Report 93004, April 1993
    
        Since:
            8.0
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, double: float, double2: float) -> org.orekit.orbits.Orbit:
        """
            Estimate orbit from three line of sight.
        
            This signature assumes there was less than an half revolution between start and final date
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                O1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Observer position 1
                O2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Observer position 2
                O3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Observer position 3
                lineOfSight1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight 1
                dateObs1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                lineOfSight2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight 2
                dateObs2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                lineOfSight3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight 3
                dateObs3 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                rho1init (double): initial guess of the range problem. range 1, in meters
                rho3init (double): initial guess of the range problem. range 3, in meters
        
            Returns:
                an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
            Estimate orbit from three line of sight.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                O1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Observer position 1
                O2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Observer position 2
                O3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): Observer position 3
                lineOfSight1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight 1
                dateObs1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                lineOfSight2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight 2
                dateObs2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 2
                lineOfSight3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight 3
                dateObs3 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 3
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
            Estimate orbit from three angular (i.e., azimuth - elevation) observations.
        
            This method doesn't need initial guesses of range values since they are computed by a Gauss algorithm.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                azEl1 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): first angular observation
                azEl2 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): second angular observation
                azEl3 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): third angular observation
        
            Returns:
                an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
            Since:
                13.0
        
            Estimate orbit from three angular (i.e., azimuth - elevation) observations.
        
            This method doesn't need initial guesses of range values since they are computed by a Gauss algorithm.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                azEl1 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): first angular observation
                azEl2 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): second angular observation
                azEl3 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): third angular observation
                nRev (int): number of complete revolutions between observation 1 and 3
                direction (boolean): true if posigrade (short way)
        
            Returns:
                an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
            Since:
                13.0
        
            Estimate orbit from three angular observations.
        
            This signature assumes there was less than an half revolution between start and final date
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                azEl1 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): first angular observation
                azEl2 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): second angular observation
                azEl3 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): third angular observation
                rho1init (double): initial guess of the range problem. range 1, in meters
                rho3init (double): initial guess of the range problem. range 3, in meters
        
            Returns:
                an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
            Since:
                12.0
        
            Estimate orbit from three angular observations.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                azEl1 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): first angular observation
                azEl2 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): second angular observation
                azEl3 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): third angular observation
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
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
        
            Returns:
                an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
            Since:
                13.0
        
            Estimate orbit from three angular (i.e., right ascension - declination) observations.
        
            This method doesn't need initial guesses of range values since they are computed by a Gauss algorithm.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
                nRev (int): number of complete revolutions between observation 1 and 3
                direction (boolean): true if posigrade (short way)
        
            Returns:
                an estimate of the orbit at the central date (i.e., date of the second angular observation)
        
            Since:
                13.0
        
            Estimate orbit from three angular observations.
        
            This signature assumes there was less than an half revolution between start and final date
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
                rho1init (double): initial guess of the range problem. range 1, in meters
                rho3init (double): initial guess of the range problem. range 3, in meters
        
            Returns:
                an estimate of the Keplerian orbit at the central date (i.e., date of the second angular observation)
        
            Since:
                11.0
        
            Estimate orbit from three angular observations.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
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

class IodLambert:
    """
    public class IodLambert extends :class:`~org.orekit.estimation.iod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Lambert position-based Initial Orbit Determination (IOD) algorithm, assuming Keplerian motion.
    
        An orbit is determined from two position vectors. References: Battin, R.H., An Introduction to the Mathematics and
        Methods of Astrodynamics, AIAA Education, 1999. Lancaster, E.R. and Blanchard, R.C., A Unified Form of Lambert’s
        Theorem, Goddard Space Flight Center, 1968.
    
        Since:
            8.0
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
            Estimate a Keplerian orbit given two position vectors and a duration.
        
            The logic for setting :code:`posigrade` and :code:`nRev` is that the sweep angle Δυ travelled by the object between
            :code:`t1` and :code:`t2` is 2π :code:`nRev +1` - α if :code:`posigrade` is false and 2π :code:`nRev` + α if
            :code:`posigrade` is true, where α is the separation angle between :code:`p1` and :code:`p2`, which is always computed
            between 0 and π (because in 3D without a normal reference, vector angles cannot go past π).
        
            This implies that :code:`posigrade` should be set to true if :code:`p2` is located in the half orbit starting at
            :code:`p1` and it should be set to false if :code:`p2` is located in the half orbit ending at :code:`p1`, regardless of
            the number of periods between :code:`t1` and :code:`t2`, and :code:`nRev` should be set accordingly.
        
            As an example, if :code:`t2` is less than half a period after :code:`t1`, then :code:`posigrade` should be :code:`true`
            and :code:`nRev` should be 0. If :code:`t2` is more than half a period after :code:`t1` but less than one period after
            :code:`t1`, :code:`posigrade` should be :code:`false` and :code:`nRev` should be 0.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): frame
                posigrade (boolean): flag indicating the direction of motion
                nRev (int): number of revolutions
                p1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): position vector 1
                t1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                p2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): position vector 2
                t2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 2
        
            Returns:
                an initial Keplerian orbit estimate at the first observation date t1
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, pV: org.orekit.estimation.measurements.PV, pV2: org.orekit.estimation.measurements.PV) -> org.orekit.orbits.Orbit:
        """
            Estimate an initial orbit from two position measurements.
        
            The logic for setting :code:`posigrade` and :code:`nRev` is that the sweep angle Δυ travelled by the object between
            :code:`t1` and :code:`t2` is 2π :code:`nRev +1` - α if :code:`posigrade` is false and 2π :code:`nRev` + α if
            :code:`posigrade` is true, where α is the separation angle between :code:`p1` and :code:`p2`, which is always computed
            between 0 and π (because in 3D without a normal reference, vector angles cannot go past π).
        
            This implies that :code:`posigrade` should be set to true if :code:`p2` is located in the half orbit starting at
            :code:`p1` and it should be set to false if :code:`p2` is located in the half orbit ending at :code:`p1`, regardless of
            the number of periods between :code:`t1` and :code:`t2`, and :code:`nRev` should be set accordingly.
        
            As an example, if :code:`t2` is less than half a period after :code:`t1`, then :code:`posigrade` should be :code:`true`
            and :code:`nRev` should be 0. If :code:`t2` is more than half a period after :code:`t1` but less than one period after
            :code:`t1`, :code:`posigrade` should be :code:`false` and :code:`nRev` should be 0.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measurements frame
                posigrade (boolean): flag indicating the direction of motion
                nRev (int): number of revolutions
                p1 (:class:`~org.orekit.estimation.measurements.Position`): first position measurement
                p2 (:class:`~org.orekit.estimation.measurements.Position`): second position measurement
        
            Returns:
                an initial Keplerian orbit estimation at the first observation date t1
        
            Since:
                11.0
        
            Estimate an initial orbit from two PV measurements.
        
            The logic for setting :code:`posigrade` and :code:`nRev` is that the sweep angle Δυ travelled by the object between
            :code:`t1` and :code:`t2` is 2π :code:`nRev +1` - α if :code:`posigrade` is false and 2π :code:`nRev` + α if
            :code:`posigrade` is true, where α is the separation angle between :code:`p1` and :code:`p2`, which is always computed
            between 0 and π (because in 3D without a normal reference, vector angles cannot go past π).
        
            This implies that :code:`posigrade` should be set to true if :code:`p2` is located in the half orbit starting at
            :code:`p1` and it should be set to false if :code:`p2` is located in the half orbit ending at :code:`p1`, regardless of
            the number of periods between :code:`t1` and :code:`t2`, and :code:`nRev` should be set accordingly.
        
            As an example, if :code:`t2` is less than half a period after :code:`t1`, then :code:`posigrade` should be :code:`true`
            and :code:`nRev` should be 0. If :code:`t2` is more than half a period after :code:`t1` but less than one period after
            :code:`t1`, :code:`posigrade` should be :code:`false` and :code:`nRev` should be 0.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measurements frame
                posigrade (boolean): flag indicating the direction of motion
                nRev (int): number of revolutions
                pv1 (:class:`~org.orekit.estimation.measurements.PV`): first PV measurement
                pv2 (:class:`~org.orekit.estimation.measurements.PV`): second PV measurement
        
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
    public class IodLaplace extends :class:`~org.orekit.estimation.iod.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Laplace angles-only Initial Orbit Determination (IOD) algorithm, assuming Keplerian motion.
    
        Laplace algorithm is one of the first method to determine orbits. An orbit is determined from three lines of sight
        w.r.t. their respective observers inertial positions vectors. For Laplace method, the observer is identical for all
        observations. Reference: Bate, R., Mueller, D. D., & White, J. E. (1971). Fundamentals of astrodynamics. New York: Dover
        Publications.
    
        Since:
            10.1
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularAzEl: org.orekit.estimation.measurements.AngularAzEl, angularAzEl2: org.orekit.estimation.measurements.AngularAzEl, angularAzEl3: org.orekit.estimation.measurements.AngularAzEl) -> org.orekit.orbits.Orbit:
        """
            Estimate the orbit from three angular observations at the same location.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): Observer coordinates at time of raDec2
                azEl1 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): first angular observation
                azEl2 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): second angular observation
                azEl3 (:class:`~org.orekit.estimation.measurements.AngularAzEl`): third angular observation
        
            Returns:
                estimate of the orbit at the central date or null if no estimate is possible with the given data
        
            Since:
                12.0
        
            Estimate the orbit from three angular observations at the same location.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): Observer coordinates at time of raDec2
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
        
            Returns:
                estimate of the orbit at the central date or null if no estimate is possible with the given data
        
            Since:
                11.0
        
            Estimate orbit from three line of sight angles at the same location.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                obsPva (:class:`~org.orekit.utils.PVCoordinates`): Observer coordinates at time obsDate2
                obsDate1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                los1 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight unit vector 1
                obsDate2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 2
                los2 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight unit vector 2
                obsDate3 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 3
                los3 (:class:`~org.orekit.estimation.iod.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): line of sight unit vector 3
        
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
    IodLambert: typing.Type[IodLambert]
    IodLaplace: typing.Type[IodLaplace]
