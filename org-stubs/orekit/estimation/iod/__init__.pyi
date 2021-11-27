import org.hipparchus.geometry.euclidean.threed
import org.orekit.estimation.measurements
import org.orekit.frames
import org.orekit.orbits
import org.orekit.time
import org.orekit.utils
import typing



class IodGibbs:
    """
    public class IodGibbs extends Object
    
        Gibbs initial orbit determination. An orbit is determined from three position vectors. Reference: Vallado, D.,
        Fundamentals of Astrodynamics and Applications
    
        Since:
            8.0
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.KeplerianOrbit:
        """
            Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measure frame
                r1 (Vector3D): position 1 measured in frame
                date1 (:class:`~org.orekit.time.AbsoluteDate`): date of measure 1
                r2 (Vector3D): position 2 measured in frame
                date2 (:class:`~org.orekit.time.AbsoluteDate`): date of measure 2
                r3 (Vector3D): position 3 measured in frame
                date3 (:class:`~org.orekit.time.AbsoluteDate`): date of measure 3
        
            Returns:
                an initial orbit estimation
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pV: org.orekit.estimation.measurements.PV, pV2: org.orekit.estimation.measurements.PV, pV3: org.orekit.estimation.measurements.PV) -> org.orekit.orbits.KeplerianOrbit:
        """
            Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measurements frame
                p1 (:class:`~org.orekit.estimation.measurements.Position`): First position measurement
                p2 (:class:`~org.orekit.estimation.measurements.Position`): Second position measurement
                p3 (:class:`~org.orekit.estimation.measurements.Position`): Third position measurement
        
            Returns:
                an initial orbit estimation
        
            Since:
                11.0
        
            Give an initial orbit estimation, assuming Keplerian motion. All observations should be from the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): measure frame
                pv1 (:class:`~org.orekit.estimation.measurements.PV`): PV measure 1 taken in frame
                pv2 (:class:`~org.orekit.estimation.measurements.PV`): PV measure 2 taken in frame
                pv3 (:class:`~org.orekit.estimation.measurements.PV`): PV measure 3 taken in frame
        
            Returns:
                an initial orbit estimation
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position, position3: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.KeplerianOrbit: ...

class IodGooding:
    """
    public class IodGooding extends Object
    
        Gooding angles only initial orbit determination, assuming Keplerian motion. An orbit is determined from three angular
        observations. Reference: Gooding, R.H., A New Procedure for Orbit Determination Based on Three Lines of Sight (Angles
        only), Technical Report 93004, April 1993
    
        Since:
            8.0
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, double: float, double2: float) -> org.orekit.orbits.KeplerianOrbit:
        """
            Orbit got from Observed Three Lines of Sight (angles only).
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                O1 (Vector3D): Observer position 1
                O2 (Vector3D): Observer position 2
                O3 (Vector3D): Observer position 3
                lineOfSight1 (Vector3D): line of sight 1
                dateObs1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                lineOfSight2 (Vector3D): line of sight 2
                dateObs2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 2
                lineOfSight3 (Vector3D): line of sight 3
                dateObs3 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 3
                rho1init (double): initial guess of the range problem. range 1, in meters
                rho3init (double): initial guess of the range problem. range 3, in meters
                nRev (int): number of complete revolutions between observation1 and 3
                direction (boolean): true if posigrade (short way)
        
            Returns:
                an estimate of the Keplerian orbit
        
            Orbit got from Observed Three Lines of Sight (angles only). assuming there was less than an half revolution between
            start and final date
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                O1 (Vector3D): Observer position 1
                O2 (Vector3D): Observer position 2
                O3 (Vector3D): Observer position 3
                lineOfSight1 (Vector3D): line of sight 1
                dateObs1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                lineOfSight2 (Vector3D): line of sight 2
                dateObs2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                lineOfSight3 (Vector3D): line of sight 3
                dateObs3 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                rho1init (double): initial guess of the range problem. range 1, in meters
                rho3init (double): initial guess of the range problem. range 3, in meters
        
            Returns:
                an estimate of the Keplerian orbit
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, double: float, double2: float, int: int, boolean: bool) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec, double: float, double2: float) -> org.orekit.orbits.KeplerianOrbit:
        """
            Orbit got from three angular observations.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
                rho1init (double): initial guess of the range problem. range 1, in meters
                rho3init (double): initial guess of the range problem. range 3, in meters
                nRev (int): number of complete revolutions between observation 1 and 3
                direction (boolean): true if posigrade (short way)
        
            Returns:
                an estimate of the Keplerian orbit
        
            Since:
                11.0
        
            Orbit got from three angular observations.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
                rho1init (double): initial guess of the range problem. range 1, in meters
                rho3init (double): initial guess of the range problem. range 3, in meters
        
            Returns:
                an estimate of the Keplerian orbit
        
            Since:
                11.0
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec, double: float, double2: float, int: int, boolean: bool) -> org.orekit.orbits.KeplerianOrbit: ...
    def getRange1(self) -> float:
        """
            Get the range for observation (1).
        
            Returns:
                the range for observation (1).
        
        
        """
        ...
    def getRange2(self) -> float:
        """
            Get the range for observation (2).
        
            Returns:
                the range for observation (2).
        
        
        """
        ...
    def getRange3(self) -> float:
        """
            Get the range for observation (3).
        
            Returns:
                the range for observation (3).
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def lineOfSight(double: float, double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Calculates the line of sight vector.
        
            Parameters:
                alpha (double): right ascension angle, in radians
                delta (double): declination angle, in radians
        
            Returns:
                the line of sight vector
        
            Since:
                11.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def lineOfSight(angularRaDec: org.orekit.estimation.measurements.AngularRaDec) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Calculate the line of sight vector from an AngularRaDec measurement.
        
            Parameters:
                raDec (:class:`~org.orekit.estimation.measurements.AngularRaDec`): measurement
        
            Returns:
                the line of sight vector
        
            Since:
                11.0
        
        
        """
        ...

class IodLambert:
    """
    public class IodLambert extends Object
    
        Lambert initial orbit determination, assuming Keplerian motion. An orbit is determined from two position vectors.
        References: Battin, R.H., An Introduction to the Mathematics and Methods of Astrodynamics, AIAA Education, 1999.
        Lancaster, E.R. and Blanchard, R.C., A Unified Form of LambertÃ¢â‚¬â„¢s Theorem, Goddard Space Flight Center, 1968.
    
        Since:
            8.0
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.KeplerianOrbit:
        """
            Estimate a Keplerian orbit given two position vectors and a duration.
        
            The logic for setting :code:`posigrade` and :code:`nRev` is that the sweep angle ÃŽâ€�Ã�â€¦ travelled by the object
            between :code:`t1` and :code:`t2` is 2Ã�â‚¬ :code:`nRev +1` - ÃŽÂ± if :code:`posigrade` is false and 2Ã�â‚¬ :code:`nRev`
            + ÃŽÂ± if :code:`posigrade` is true, where ÃŽÂ± is the separation angle between :code:`p1` and :code:`p2`, which is
            always computed between 0 and Ã�â‚¬ (because in 3D without a normal reference, vector angles cannot go past Ã�â‚¬).
        
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
                p1 (Vector3D): position vector 1
                t1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                p2 (Vector3D): position vector 2
                t2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 2
        
            Returns:
                an initial Keplerian orbit estimate
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.KeplerianOrbit:
        """
            Estimate an initial orbit from two position measurements.
        
            The logic for setting :code:`posigrade` and :code:`nRev` is that the sweep angle ÃŽâ€�Ã�â€¦ travelled by the object
            between :code:`t1` and :code:`t2` is 2Ã�â‚¬ :code:`nRev +1` - ÃŽÂ± if :code:`posigrade` is false and 2Ã�â‚¬ :code:`nRev`
            + ÃŽÂ± if :code:`posigrade` is true, where ÃŽÂ± is the separation angle between :code:`p1` and :code:`p2`, which is
            always computed between 0 and Ã�â‚¬ (because in 3D without a normal reference, vector angles cannot go past Ã�â‚¬).
        
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
                an initial orbit estimation
        
            Since:
                11.0
        
        """
        ...

class IodLaplace:
    """
    public class IodLaplace extends Object
    
        Laplace angles-only initial orbit determination, assuming Keplerian motion. An orbit is determined from three angular
        observations from the same site. Reference: Bate, R., Mueller, D. D., & White, J. E. (1971). Fundamentals of
        astrodynamics. New York: Dover Publications.
    
        Since:
            10.1
    """
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pVCoordinates: org.orekit.utils.PVCoordinates, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec) -> org.orekit.orbits.CartesianOrbit:
        """
            Estimate the orbit from three angular observations at the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                obsPva (:class:`~org.orekit.utils.PVCoordinates`): Observer coordinates at time of raDec2
                raDec1 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): first angular observation
                raDec2 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): second angular observation
                raDec3 (:class:`~org.orekit.estimation.measurements.AngularRaDec`): third angular observation
        
            Returns:
                estimate of the orbit at the central date or null if no estimate is possible with the given data
        
            Since:
                11.0
        
            Estimate orbit from three line of sight angles from the same location.
        
            Parameters:
                frame (:class:`~org.orekit.frames.Frame`): inertial frame for observer coordinates and orbit estimate
                obsPva (:class:`~org.orekit.utils.PVCoordinates`): Observer coordinates at time obsDate2
                obsDate1 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 1
                los1 (Vector3D): line of sight unit vector 1
                obsDate2 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 2
                los2 (Vector3D): line of sight unit vector 2
                obsDate3 (:class:`~org.orekit.time.AbsoluteDate`): date of observation 3
                los3 (Vector3D): line of sight unit vector 3
        
            Returns:
                estimate of the orbit at the central date dateObs2 or null if no estimate is possible with the given data
        
        
        """
        ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pVCoordinates: org.orekit.utils.PVCoordinates, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.orbits.CartesianOrbit: ...
    @typing.overload
    @staticmethod
    def lineOfSight(double: float, double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Calculates the line of sight vector.
        
            Parameters:
                alpha (double): right ascension angle, in radians
                delta (double): declination angle, in radians
        
            Returns:
                the line of sight vector
        
            Since:
                11.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def lineOfSight(angularRaDec: org.orekit.estimation.measurements.AngularRaDec) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Calculate the line of sight vector from an AngularRaDec measurement.
        
            Parameters:
                raDec (:class:`~org.orekit.estimation.measurements.AngularRaDec`): measurement
        
            Returns:
                the line of sight vector
        
            Since:
                11.0
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.iod")``.

    IodGibbs: typing.Type[IodGibbs]
    IodGooding: typing.Type[IodGooding]
    IodLambert: typing.Type[IodLambert]
    IodLaplace: typing.Type[IodLaplace]
