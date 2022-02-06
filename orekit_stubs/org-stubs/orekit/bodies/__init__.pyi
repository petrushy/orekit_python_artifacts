import java.io
import java.lang
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.euclidean.twod
import org.orekit.data
import org.orekit.frames
import org.orekit.time
import org.orekit.utils
import typing



class BodyShape(java.io.Serializable):
    """
    public interface BodyShape extends Serializable
    
        Interface representing the rigid surface shape of a natural body.
    
        The shape is not provided as a single complete geometric model, but single points can be queried
        (:meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint`).
    """
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
            Get body frame related to body shape.
        
            Returns:
                body frame related to body shape
        
        
        """
        ...
    _getIntersectionPoint_0__T = typing.TypeVar('_getIntersectionPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getIntersectionPoint(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_0__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_0__T]) -> 'FieldGeodeticPoint'[_getIntersectionPoint_0__T]:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Parameters:
                line (FieldLine<T> line): test line (may intersect the body or not)
                close (FieldVector3D<T> close): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> 'GeodeticPoint':
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Parameters:
                line (Line): test line (may intersect the body or not)
                close (Vector3D): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    @typing.overload
    def projectToGround(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Project a point to the ground.
        
            Parameters:
                point (Vector3D): point to project
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Since:
                7.0
        
            Also see:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround`
        
        """
        ...
    @typing.overload
    def projectToGround(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Project a moving point to the ground.
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): moving point
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Since:
                7.0
        
            Also see:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround`
        
        
        """
        ...
    _transform_0__T = typing.TypeVar('_transform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, fieldGeodeticPoint: 'FieldGeodeticPoint'[_transform_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_0__T]:
        """
            Transform a surface-relative point to a Cartesian point.
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def transform(self, geodeticPoint: 'GeodeticPoint') -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a Cartesian point to a surface-relative point.
        
            Parameters:
                point (Vector3D): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Transform a surface-relative point to a Cartesian point.
        
            Parameters:
                point (:class:`~org.orekit.bodies.GeodeticPoint`): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
        """
        ...
    @typing.overload
    def transform(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_2__T]) -> 'FieldGeodeticPoint'[_transform_2__T]:
        """
            Transform a Cartesian point to a surface-relative point.
        
            Parameters:
                point (FieldVector3D<T> point): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Since:
                9.0
        
        """
        ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> 'GeodeticPoint': ...

class CR3BPFactory:
    """
    public class CR3BPFactory extends Object
    
        Factory class creating predefined CR3BP system using CR3BPSystem class. For example, Earth-Moon CR3BP System.
    
        Since:
            10.2
    
        Also see:
            :class:`~org.orekit.bodies.CR3BPSystem`
    """
    @staticmethod
    def getEarthMoonCR3BP() -> 'CR3BPSystem': ...
    @staticmethod
    def getSunEarthCR3BP(absoluteDate: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> 'CR3BPSystem': ...
    @staticmethod
    def getSunJupiterCR3BP(absoluteDate: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> 'CR3BPSystem': ...
    @staticmethod
    def getSystem(celestialBody: 'CelestialBody', celestialBody2: 'CelestialBody', double: float) -> 'CR3BPSystem':
        """
            Get the corresponding CR3BP System.
        
            Parameters:
                primaryBody (:class:`~org.orekit.bodies.CelestialBody`): Primary Body in the CR3BP System
                secondaryBody (:class:`~org.orekit.bodies.CelestialBody`): Secondary Body in the CR3BP System
                a (double): Semi-Major Axis of the secondary body
        
            Returns:
                corresponding CR3BP System
        
        
        """
        ...

class CR3BPSystem:
    """
    public class CR3BPSystem extends Object
    
        Class creating, from two different celestial bodies, the corresponding system with respect to the Circular Restricted
        Three Body problem hypotheses.
    
        Since:
            10.2
    
        Also see:
            "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    @typing.overload
    def __init__(self, celestialBody: 'CelestialBody', celestialBody2: 'CelestialBody', double: float): ...
    @typing.overload
    def __init__(self, celestialBody: 'CelestialBody', celestialBody2: 'CelestialBody', double: float, double2: float): ...
    def getDdim(self) -> float:
        """
            Get the CR3BP distance between the two bodies.
        
            Returns:
                CR3BP distance between the two bodies(m)
        
        
        """
        ...
    def getGamma(self, lagrangianPoints: org.orekit.utils.LagrangianPoints) -> float:
        """
            Get the position of the Lagrangian point in the CR3BP Rotating frame.
        
            Parameters:
                lagrangianPoint (:class:`~org.orekit.utils.LagrangianPoints`): Lagrangian Point to consider
        
            Returns:
                Distance between a Lagrangian Point and its closest primary.
        
        
        """
        ...
    def getLPosition(self, lagrangianPoints: org.orekit.utils.LagrangianPoints) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position of the Lagrangian point in the CR3BP Rotating frame.
        
            Parameters:
                lagrangianPoint (:class:`~org.orekit.utils.LagrangianPoints`): Lagrangian Point to consider
        
            Returns:
                position of the Lagrangian point in the CR3BP Rotating frame (-)
        
        
        """
        ...
    def getMassRatio(self) -> float:
        """
            Get the CR3BP mass ratio of the system mu2/(mu1+mu2).
        
            Returns:
                CR3BP mass ratio of the system mu2/(mu1+mu2)
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the CR3BP system.
        
            Returns:
                name of the CR3BP system
        
        
        """
        ...
    def getPrimary(self) -> 'CelestialBody':
        """
            Get the primary CelestialBody.
        
            Returns:
                primary CelestialBody
        
        
        """
        ...
    def getRealAPV(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.AbsolutePVCoordinates:
        """
            Get the AbsolutePVCoordinates from normalized units to standard units in an output frame. This method ensure the
            constituency of the date of returned AbsolutePVCoordinate, especially when apv0 is the result of a propagation in CR3BP
            normalized model.
        
            Parameters:
                apv0 (:class:`~org.orekit.utils.AbsolutePVCoordinates`): Normalized AbsolutePVCoordinates in the rotating frame
                initialDate (:class:`~org.orekit.time.AbsoluteDate`): Date of the at the beginning of the propagation
                outputFrame (:class:`~org.orekit.frames.Frame`): Frame in which the output AbsolutePVCoordinates will be
        
            Returns:
                AbsolutePVCoordinates in the output frame [m,m/s]
        
        
        """
        ...
    def getRotatingFrame(self) -> org.orekit.frames.Frame:
        """
            Get the CR3BP Rotating Frame.
        
            Returns:
                CR3BP Rotating Frame
        
        
        """
        ...
    def getSecondary(self) -> 'CelestialBody':
        """
            Get the secondary CelestialBody.
        
            Returns:
                secondary CelestialBody
        
        
        """
        ...
    def getTdim(self) -> float:
        """
            Get the CR3BP orbital period of m2 around m1.
        
            Returns:
                CR3BP orbital period of m2 around m1(s)
        
        
        """
        ...
    def getVdim(self) -> float:
        """
            Get the CR3BP orbital velocity of m2.
        
            Returns:
                CR3BP orbital velocity of m2(m/s)
        
        
        """
        ...

class CelestialBodies:
    """
    public interface CelestialBodies
    
        Commonly used celestial bodies. This interface defines methods for obtaining intances of the commonly used celestial
        bodies.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.bodies.CelestialBodyFactory`
    """
    def getBody(self, string: str) -> 'CelestialBody':
        """
            Get a celestial body. The names of the common bodies are defined as constants in
            :class:`~org.orekit.bodies.CelestialBodyFactory`.
        
            Parameters:
                name (String): name of the celestial body
        
            Returns:
                celestial body
        
        
        """
        ...
    def getEarth(self) -> 'CelestialBody':
        """
            Get the Earth singleton body.
        
            Returns:
                Earth body
        
        
        """
        ...
    def getEarthMoonBarycenter(self) -> 'CelestialBody':
        """
            Get the Earth-Moon barycenter singleton bodies pair.
        
            Both the :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame` and
            :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame` for this bodies pair are aligned with
            :meth:`~org.orekit.frames.FramesFactory.getICRF` (and therefore also :meth:`~org.orekit.frames.FramesFactory.getGCRF`)
        
            Returns:
                Earth-Moon barycenter bodies pair
        
        
        """
        ...
    def getJupiter(self) -> 'CelestialBody':
        """
            Get the Jupiter singleton body.
        
            Returns:
                Jupiter body
        
        
        """
        ...
    def getMars(self) -> 'CelestialBody':
        """
            Get the Mars singleton body.
        
            Returns:
                Mars body
        
        
        """
        ...
    def getMercury(self) -> 'CelestialBody':
        """
            Get the Mercury singleton body.
        
            Returns:
                Sun body
        
        
        """
        ...
    def getMoon(self) -> 'CelestialBody':
        """
            Get the Moon singleton body.
        
            Returns:
                Moon body
        
        
        """
        ...
    def getNeptune(self) -> 'CelestialBody':
        """
            Get the Neptune singleton body.
        
            Returns:
                Neptune body
        
        
        """
        ...
    def getPluto(self) -> 'CelestialBody':
        """
            Get the Pluto singleton body.
        
            Returns:
                Pluto body
        
        
        """
        ...
    def getSaturn(self) -> 'CelestialBody':
        """
            Get the Saturn singleton body.
        
            Returns:
                Saturn body
        
        
        """
        ...
    def getSolarSystemBarycenter(self) -> 'CelestialBody':
        """
            Get the solar system barycenter aggregated body.
        
            Both the :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame` and
            :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame` for this aggregated body are aligned with
            :meth:`~org.orekit.frames.FramesFactory.getICRF` (and therefore also :meth:`~org.orekit.frames.FramesFactory.getGCRF`)
        
            Returns:
                solar system barycenter aggregated body
        
        
        """
        ...
    def getSun(self) -> 'CelestialBody':
        """
            Get the Sun singleton body.
        
            Returns:
                Sun body
        
        
        """
        ...
    def getUranus(self) -> 'CelestialBody':
        """
            Get the Uranus singleton body.
        
            Returns:
                Uranus body
        
        
        """
        ...
    def getVenus(self) -> 'CelestialBody':
        """
            Get the Venus singleton body.
        
            Returns:
                Venus body
        
        
        """
        ...

class CelestialBody(java.io.Serializable, org.orekit.utils.ExtendedPVCoordinatesProvider):
    """
    public interface CelestialBody extends Serializable, :class:`~org.orekit.utils.ExtendedPVCoordinatesProvider`
    
        Interface for celestial bodies like Sun, Moon or solar system planets.
    
        Also see:
            :class:`~org.orekit.bodies.CelestialBodyFactory`
    """
    def getBodyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
            Get a body oriented, body centered frame.
        
            The frame is always bound to the body center, and its axes have a fixed orientation with respect to the celestial body.
        
            Returns:
                a body oriented, body centered frame
        
            Also see:
                :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame`
        
        
        """
        ...
    def getGM(self) -> float:
        """
            Get the attraction coefficient of the body.
        
            Returns:
                attraction coefficient of the body (mÂ³/sÂ²)
        
        
        """
        ...
    def getInertiallyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
            Get an inertially oriented, body centered frame.
        
            The frame is always bound to the body center, and its axes have a fixed orientation with respect to other inertial
            frames.
        
            Returns:
                an inertially oriented, body centered frame
        
            Also see:
                :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame`
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the body.
        
            Returns:
                name of the body
        
        
        """
        ...

class CelestialBodyFactory:
    """
    public class CelestialBodyFactory extends Object
    
        Factory class for bodies of the solar system.
    
        The :meth:`~org.orekit.bodies.CelestialBodyFactory.getSun`, the :meth:`~org.orekit.bodies.CelestialBodyFactory.getMoon`
        and the planets (including the Pluto dwarf planet) are provided by this factory. In addition, two important points are
        provided for convenience: the :meth:`~org.orekit.bodies.CelestialBodyFactory.getSolarSystemBarycenter` and the
        :meth:`~org.orekit.bodies.CelestialBodyFactory.getEarthMoonBarycenter`.
    
        The underlying body-centered frames are either direct children of :meth:`~org.orekit.frames.FramesFactory.getEME2000`
        (for :meth:`~org.orekit.bodies.CelestialBodyFactory.getMoon` and
        :meth:`~org.orekit.bodies.CelestialBodyFactory.getEarthMoonBarycenter`) or children from other body-centered frames. For
        example, the path from EME2000 to Jupiter-centered frame is: EME2000, Earth-Moon barycenter centered, solar system
        barycenter centered, Jupiter-centered. The defining transforms of these frames are combinations of simple linear
        :meth:`~org.orekit.frames.Transform.Transform` transforms without any rotation. The frame axes are therefore always
        parallel to :meth:`~org.orekit.frames.FramesFactory.getEME2000` frame axes.
    
        The position of the bodies provided by this class are interpolated using the JPL DE 405/DE 406 ephemerides.
    """
    SOLAR_SYSTEM_BARYCENTER: typing.ClassVar[str] = ...
    """
    public static final String SOLAR_SYSTEM_BARYCENTER
    
        Predefined name for solar system barycenter.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    SUN: typing.ClassVar[str] = ...
    """
    public static final String SUN
    
        Predefined name for Sun.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    MERCURY: typing.ClassVar[str] = ...
    """
    public static final String MERCURY
    
        Predefined name for Mercury.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    VENUS: typing.ClassVar[str] = ...
    """
    public static final String VENUS
    
        Predefined name for Venus.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    EARTH_MOON: typing.ClassVar[str] = ...
    """
    public static final String EARTH_MOON
    
        Predefined name for Earth-Moon barycenter.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    EARTH: typing.ClassVar[str] = ...
    """
    public static final String EARTH
    
        Predefined name for Earth.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    MOON: typing.ClassVar[str] = ...
    """
    public static final String MOON
    
        Predefined name for Moon.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    MARS: typing.ClassVar[str] = ...
    """
    public static final String MARS
    
        Predefined name for Mars.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    JUPITER: typing.ClassVar[str] = ...
    """
    public static final String JUPITER
    
        Predefined name for Jupiter.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    SATURN: typing.ClassVar[str] = ...
    """
    public static final String SATURN
    
        Predefined name for Saturn.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    URANUS: typing.ClassVar[str] = ...
    """
    public static final String URANUS
    
        Predefined name for Uranus.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    NEPTUNE: typing.ClassVar[str] = ...
    """
    public static final String NEPTUNE
    
        Predefined name for Neptune.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    PLUTO: typing.ClassVar[str] = ...
    """
    public static final String PLUTO
    
        Predefined name for Pluto.
    
        Also see:
            :meth:`~org.orekit.bodies.CelestialBodyFactory.getBody`, :meth:`~constant`
    
    
    """
    @staticmethod
    def addCelestialBodyLoader(string: str, celestialBodyLoader: 'CelestialBodyLoader') -> None: ...
    @typing.overload
    @staticmethod
    def addDefaultCelestialBodyLoader(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def addDefaultCelestialBodyLoader(string: str, string2: str) -> None: ...
    @typing.overload
    @staticmethod
    def clearCelestialBodyCache() -> None: ...
    @typing.overload
    @staticmethod
    def clearCelestialBodyCache(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def clearCelestialBodyLoaders() -> None: ...
    @typing.overload
    @staticmethod
    def clearCelestialBodyLoaders(string: str) -> None: ...
    @staticmethod
    def getBody(string: str) -> CelestialBody: ...
    @staticmethod
    def getCelestialBodies() -> 'LazyLoadedCelestialBodies': ...
    @staticmethod
    def getEarth() -> CelestialBody: ...
    @staticmethod
    def getEarthMoonBarycenter() -> CelestialBody: ...
    @staticmethod
    def getJupiter() -> CelestialBody: ...
    @staticmethod
    def getMars() -> CelestialBody: ...
    @staticmethod
    def getMercury() -> CelestialBody: ...
    @staticmethod
    def getMoon() -> CelestialBody: ...
    @staticmethod
    def getNeptune() -> CelestialBody: ...
    @staticmethod
    def getPluto() -> CelestialBody: ...
    @staticmethod
    def getSaturn() -> CelestialBody: ...
    @staticmethod
    def getSolarSystemBarycenter() -> CelestialBody: ...
    @staticmethod
    def getSun() -> CelestialBody: ...
    @staticmethod
    def getUranus() -> CelestialBody: ...
    @staticmethod
    def getVenus() -> CelestialBody: ...

class CelestialBodyLoader:
    """
    public interface CelestialBodyLoader
    
        Interface for loading celestial bodies.
    """
    def loadCelestialBody(self, string: str) -> CelestialBody:
        """
            Load celestial body.
        
            Parameters:
                name (String): name of the celestial body
        
            Returns:
                loaded celestial body
        
        
        """
        ...

class Ellipse(java.io.Serializable):
    """
    public class Ellipse extends Object implements Serializable
    
        Model of a 2D ellipse in 3D space.
    
        These ellipses are mainly created as plane sections of general 3D ellipsoids, but can be used for other purposes.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            7.0
    
        Also see:
            :meth:`~org.orekit.bodies.Ellipsoid.getPlaneSection`, :meth:`~serialized`
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, double2: float, frame: org.orekit.frames.Frame): ...
    def getA(self) -> float:
        """
            Get the semi major axis.
        
            Returns:
                semi major axis
        
        
        """
        ...
    def getB(self) -> float:
        """
            Get the semi minor axis.
        
            Returns:
                semi minor axis
        
        
        """
        ...
    def getCenter(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the center of the 2D ellipse.
        
            Returns:
                center of the 2D ellipse
        
        
        """
        ...
    def getCenterOfCurvature(self, vector2D: org.hipparchus.geometry.euclidean.twod.Vector2D) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
            Find the center of curvature (point on the evolute) at the nadir of a point.
        
            Parameters:
                point (Vector2D): point in the ellipse plane
        
            Returns:
                center of curvature of the ellipse directly at point nadir
        
            Since:
                7.1
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the defining frame.
        
            Returns:
                defining frame
        
        
        """
        ...
    def getU(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the unit vector along the major axis.
        
            Returns:
                unit vector along the major axis
        
        
        """
        ...
    def getV(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the unit vector along the minor axis.
        
            Returns:
                unit vector along the minor axis
        
        
        """
        ...
    def pointAt(self, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get a point of the 2D ellipse.
        
            Parameters:
                theta (double): angular parameter on the ellipse (really the eccentric anomaly)
        
            Returns:
                ellipse point at theta, in underlying ellipsoid frame
        
        
        """
        ...
    @typing.overload
    def projectToEllipse(self, vector2D: org.hipparchus.geometry.euclidean.twod.Vector2D) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
            Find the closest ellipse point.
        
            Parameters:
                p (Vector2D): point in the ellipse plane to project on the ellipse itself
        
            Returns:
                closest point belonging to 2D meridian ellipse
        
            Project position-velocity-acceleration on an ellipse.
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): position-velocity-acceleration to project, in the reference frame
        
            Returns:
                projected position-velocity-acceleration
        
        
        """
        ...
    @typing.overload
    def projectToEllipse(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def toPlane(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
            Project a point to the ellipse plane.
        
            Parameters:
                p (Vector3D): point defined with respect to 3D frame
        
            Returns:
                point defined with respect to ellipse
        
            Also see:
                :meth:`~org.orekit.bodies.Ellipse.toSpace`
        
        
        """
        ...
    def toSpace(self, vector2D: org.hipparchus.geometry.euclidean.twod.Vector2D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Create a point from its ellipse-relative coordinates.
        
            Parameters:
                p (Vector2D): point defined with respect to ellipse
        
            Returns:
                point defined with respect to 3D frame
        
            Also see:
                :meth:`~org.orekit.bodies.Ellipse.toPlane`
        
        
        """
        ...

class Ellipsoid(java.io.Serializable):
    """
    public class Ellipsoid extends Object implements Serializable
    
        Modeling of a general three-axes ellipsoid.
    
        Since:
            7.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, frame: org.orekit.frames.Frame, double: float, double2: float, double3: float): ...
    def getA(self) -> float:
        """
            Get the length of the first semi-axis.
        
            Returns:
                length of the first semi-axis (m)
        
        
        """
        ...
    def getB(self) -> float:
        """
            Get the length of the second semi-axis.
        
            Returns:
                length of the second semi-axis (m)
        
        
        """
        ...
    def getC(self) -> float:
        """
            Get the length of the third semi-axis.
        
            Returns:
                length of the third semi-axis (m)
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the ellipsoid central frame.
        
            Returns:
                ellipsoid central frame
        
        
        """
        ...
    def getPlaneSection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> Ellipse: ...
    def isInside(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> bool:
        """
            Check if a point is inside the ellipsoid.
        
            Parameters:
                point (Vector3D): point to check, in the ellipsoid frame
        
            Returns:
                true if the point is inside the ellipsoid (or exactly on ellipsoid surface)
        
            Since:
                7.1
        
        
        """
        ...
    def pointOnLimb(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

_FieldGeodeticPoint__T = typing.TypeVar('_FieldGeodeticPoint__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGeodeticPoint(typing.Generic[_FieldGeodeticPoint__T]):
    """
    public class FieldGeodeticPoint<T extends CalculusFieldElement<T>> extends Object
    
        Point location relative to a 2D body surface, using null.
    
        Instance of this class are guaranteed to be immutable.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.bodies.BodyShape`
    """
    def __init__(self, t: _FieldGeodeticPoint__T, t2: _FieldGeodeticPoint__T, t3: _FieldGeodeticPoint__T): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAltitude(self) -> _FieldGeodeticPoint__T:
        """
            Get the altitude.
        
            Returns:
                altitude
        
        
        """
        ...
    def getEast(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]: ...
    def getLatitude(self) -> _FieldGeodeticPoint__T:
        """
            Get the latitude.
        
            Returns:
                latitude, an angular value in the range [-Ï€/2, Ï€/2]
        
        
        """
        ...
    def getLongitude(self) -> _FieldGeodeticPoint__T:
        """
            Get the longitude.
        
            Returns:
                longitude, an angular value in the range [-Ï€, Ï€]
        
        
        """
        ...
    def getNadir(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]: ...
    def getNorth(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]: ...
    def getSouth(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]: ...
    def getWest(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]: ...
    def getZenith(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class GeodeticPoint(java.io.Serializable):
    """
    public class GeodeticPoint extends Object implements Serializable
    
        Point location relative to a 2D body surface.
    
        Instance of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.bodies.BodyShape`, :class:`~org.orekit.bodies.FieldGeodeticPoint`, :meth:`~serialized`
    """
    NORTH_POLE: typing.ClassVar['GeodeticPoint'] = ...
    """
    public static final :class:`~org.orekit.bodies.GeodeticPoint` NORTH_POLE
    
        North pole.
    
        Since:
            10.0
    
    
    """
    SOUTH_POLE: typing.ClassVar['GeodeticPoint'] = ...
    """
    public static final :class:`~org.orekit.bodies.GeodeticPoint` SOUTH_POLE
    
        South pole.
    
        Since:
            10.0
    
    
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAltitude(self) -> float:
        """
            Get the altitude.
        
            Returns:
                altitude
        
        
        """
        ...
    def getEast(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction to the east of point, expressed in parent shape frame.
        
            The east direction is defined in the horizontal plane in order to complete direct triangle (east, north, zenith).
        
            Returns:
                unit vector in the east direction
        
            Also see:
                :meth:`~org.orekit.bodies.GeodeticPoint.getWest`
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
            Get the latitude.
        
            Returns:
                latitude, an angular value in the range [-Ï€/2, Ï€/2]
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
            Get the longitude.
        
            Returns:
                longitude, an angular value in the range [-Ï€, Ï€]
        
        
        """
        ...
    def getNadir(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction below the point, expressed in parent shape frame.
        
            The nadir direction is the opposite of zenith direction.
        
            Returns:
                unit vector in the nadir direction
        
            Also see:
                :meth:`~org.orekit.bodies.GeodeticPoint.getZenith`
        
        
        """
        ...
    def getNorth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction to the north of point, expressed in parent shape frame.
        
            The north direction is defined in the horizontal plane (normal to zenith direction) and following the local meridian.
        
            Returns:
                unit vector in the north direction
        
            Also see:
                :meth:`~org.orekit.bodies.GeodeticPoint.getSouth`
        
        
        """
        ...
    def getSouth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction to the south of point, expressed in parent shape frame.
        
            The south direction is the opposite of north direction.
        
            Returns:
                unit vector in the south direction
        
            Also see:
                :meth:`~org.orekit.bodies.GeodeticPoint.getNorth`
        
        
        """
        ...
    def getWest(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction to the west of point, expressed in parent shape frame.
        
            The west direction is the opposite of east direction.
        
            Returns:
                unit vector in the west direction
        
            Also see:
                :meth:`~org.orekit.bodies.GeodeticPoint.getEast`
        
        
        """
        ...
    def getZenith(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction above the point, expressed in parent shape frame.
        
            The zenith direction is defined as the normal to local horizontal plane.
        
            Returns:
                unit vector in the zenith direction
        
            Also see:
                :meth:`~org.orekit.bodies.GeodeticPoint.getNadir`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class IAUPole(java.io.Serializable):
    """
    public interface IAUPole extends Serializable
    
        Interface for IAU pole and prime meridian orientations.
    
        This interface defines methods compliant with the report of the IAU/IAG Working Group on Cartographic Coordinates and
        Rotational Elements of the Planets and Satellites (WGCCRE). These definitions are common for all recent versions of this
        report published every three years.
    
        The precise values of pole direction and W angle coefficients may vary from publication year as models are adjusted. The
        latest value of constants for implementing this interface can be found in the `working group site
        <http://astrogeology.usgs.gov/Projects/WGCCRE/>`.
    
        Also see:
            :class:`~org.orekit.bodies.CelestialBodies`
    """
    _getNode_0__T = typing.TypeVar('_getNode_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNode(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getNode_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNode_0__T]:
        """
            Get the body Q Node direction in ICRF frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                body Q Node direction in ICRF frame
        
            Since:
                9.1
        
        
        """
        ...
    @typing.overload
    def getNode(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the body Q Node direction in ICRF frame.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                body Q Node direction in ICRF frame
        
            Since:
                9.1
        
        """
        ...
    _getPole_0__T = typing.TypeVar('_getPole_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPole(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPole_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPole_0__T]:
        """
            Get the body North pole direction in ICRF frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                body North pole direction in ICRF frame
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def getPole(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the body North pole direction in ICRF frame.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                body North pole direction in ICRF frame
        
        """
        ...
    _getPrimeMeridianAngle_1__T = typing.TypeVar('_getPrimeMeridianAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPrimeMeridianAngle(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the prime meridian angle.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                prime meridian vector
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngle(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPrimeMeridianAngle_1__T]) -> _getPrimeMeridianAngle_1__T:
        """
            Get the prime meridian angle.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                prime meridian vector
        
            Since:
                9.0
        
        
        """
        ...

class JPLEphemeridesLoader(org.orekit.data.AbstractSelfFeedingLoader, CelestialBodyLoader):
    """
    public class JPLEphemeridesLoader extends :class:`~org.orekit.data.AbstractSelfFeedingLoader` implements :class:`~org.orekit.bodies.CelestialBodyLoader`
    
        Loader for JPL ephemerides binary files (DE 4xx) and similar formats (INPOP 06/08/10).
    
        JPL ephemerides binary files contain ephemerides for all solar system planets.
    
        The JPL ephemerides binary files are recognized thanks to their base names, which must match the pattern
        :code:`[lu]nx[mp]####.ddd` (or :code:`[lu]nx[mp]####.ddd.gz` for gzip-compressed files) where # stands for a digit
        character and where ddd is an ephemeris type (typically 405 or 406).
    
        The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files are
        named :code:`unx[mp]####.ddd`, while little-endian files are named :code:`lnx[mp]####.ddd`.
    
        The IMCCE ephemerides binary files are recognized thanks to their base names, which must match the pattern
        :code:`inpop*.dat` (or :code:`inpop*.dat.gz` for gzip-compressed files) where * stands for any string.
    
        The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files contain
        :code:`bigendian` in their names, while little-endian files contain :code:`littleendian` in their names.
    
        The loader supports files in TDB or TCB time scales.
    """
    DEFAULT_DE_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_DE_SUPPORTED_NAMES
    
        Default supported files name pattern for JPL DE files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_INPOP_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_INPOP_SUPPORTED_NAMES
    
        Default supported files name pattern for IMCCE INPOP files.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, ephemerisType: 'JPLEphemeridesLoader.EphemerisType'): ...
    @typing.overload
    def __init__(self, string: str, ephemerisType: 'JPLEphemeridesLoader.EphemerisType', dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales, frame: org.orekit.frames.Frame): ...
    def getLoadedAstronomicalUnit(self) -> float:
        """
            Get astronomical unit.
        
            Returns:
                astronomical unit in meters
        
        
        """
        ...
    def getLoadedConstant(self, stringArray: typing.List[str]) -> float:
        """
            Get a constant defined in the ephemerides headers.
        
            Note that since constants are defined in the JPL headers files, they are available as soon as one file is available,
            even if it doesn't match the desired central date. This is because the header must be parsed before the dates can be
            checked.
        
            There are alternate names for constants since for example JPL names are different from INPOP names (Sun gravity: GMS or
            GM_Sun, Mars gravity: GM4 or GM_Mar...).
        
            Parameters:
                names (String...): alternate names of the constant
        
            Returns:
                value of the constant of NaN if the constant is not defined
        
        
        """
        ...
    def getLoadedEarthMoonMassRatio(self) -> float:
        """
            Get Earth/Moon mass ratio.
        
            Returns:
                Earth/Moon mass ratio
        
        
        """
        ...
    def getLoadedGravitationalCoefficient(self, ephemerisType: 'JPLEphemeridesLoader.EphemerisType') -> float:
        """
            Get the gravitational coefficient of a body.
        
            Parameters:
                body (:class:`~org.orekit.bodies.JPLEphemeridesLoader.EphemerisType`): body for which the gravitational coefficient is requested
        
            Returns:
                gravitational coefficient in mÂ³/sÂ²
        
        
        """
        ...
    def getMaxChunksDuration(self) -> float:
        """
            Get the maximal chunks duration.
        
            Returns:
                chunks maximal duration in seconds
        
        
        """
        ...
    def loadCelestialBody(self, string: str) -> CelestialBody:
        """
            Load celestial body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodyLoader.loadCelestialBody`Â in
                interfaceÂ :class:`~org.orekit.bodies.CelestialBodyLoader`
        
            Parameters:
                name (String): name of the celestial body
        
            Returns:
                loaded celestial body
        
        
        """
        ...
    class EphemerisType(java.lang.Enum['JPLEphemeridesLoader.EphemerisType']):
        SOLAR_SYSTEM_BARYCENTER: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        SUN: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        MERCURY: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        VENUS: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        EARTH_MOON: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        EARTH: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        MOON: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        MARS: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        JUPITER: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        SATURN: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        URANUS: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        NEPTUNE: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        PLUTO: typing.ClassVar['JPLEphemeridesLoader.EphemerisType'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'JPLEphemeridesLoader.EphemerisType': ...
        @staticmethod
        def values() -> typing.List['JPLEphemeridesLoader.EphemerisType']: ...
    class RawPVProvider:
        _getRawPV_0__T = typing.TypeVar('_getRawPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        @typing.overload
        def getRawPV(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getRawPV_0__T]) -> org.orekit.utils.FieldPVCoordinates[_getRawPV_0__T]: ...
        @typing.overload
        def getRawPV(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates: ...

class LazyLoadedCelestialBodies(CelestialBodies):
    """
    public class LazyLoadedCelestialBodies extends Object implements :class:`~org.orekit.bodies.CelestialBodies`
    
        This class lazily loads auxiliary data when it is needed by a requested body. It is designed to match the behavior of
        :class:`~org.orekit.bodies.CelestialBodyFactory` in Orekit 10.0.
    
        Since:
            10.1
    
        Also see:
            :class:`~org.orekit.bodies.CelestialBodyFactory`
    """
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales, frame: org.orekit.frames.Frame): ...
    def addCelestialBodyLoader(self, string: str, celestialBodyLoader: CelestialBodyLoader) -> None:
        """
            Add a loader for celestial bodies.
        
            Parameters:
                name (String): name of the body (may be one of the predefined names or a user-defined name)
                loader (:class:`~org.orekit.bodies.CelestialBodyLoader`): custom loader to add for the body
        
            Also see:
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addDefaultCelestialBodyLoader`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`
        
        
        """
        ...
    @typing.overload
    def addDefaultCelestialBodyLoader(self, string: str) -> None:
        """
            Add the default loaders for all predefined celestial bodies.
        
            Parameters:
                supportedNames (String): regular expression for supported files names (may be null if the default JPL file names are used)
        
                    The default loaders look for DE405 or DE406 JPL ephemerides.
        
            Also see:
                DE405 JPL ephemerides, DE406 JPL ephemerides,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addCelestialBodyLoader`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addDefaultCelestialBodyLoader`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`
        
            Add the default loaders for celestial bodies.
        
            Parameters:
                name (String): name of the body (if not one of the predefined names, the method does nothing)
                supportedNames (String): regular expression for supported files names (may be null if the default JPL file names are used)
        
                    The default loaders look for DE405 or DE406 JPL ephemerides.
        
            Also see:
                DE405 JPL ephemerides, DE406 JPL ephemerides,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addCelestialBodyLoader`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addDefaultCelestialBodyLoader`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`
        
        
        """
        ...
    @typing.overload
    def addDefaultCelestialBodyLoader(self, string: str, string2: str) -> None: ...
    @typing.overload
    def clearCelestialBodyCache(self) -> None:
        """
            Clear all loaded celestial bodies.
        
            Calling this method will remove all loaded bodies from the internal cache. Subsequent calls to
            :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.getBody` or similar methods will result in a reload of the requested
            body from the configured loader(s).
        
        """
        ...
    @typing.overload
    def clearCelestialBodyCache(self, string: str) -> None:
        """
            Clear the specified celestial body from the internal cache.
        
            Parameters:
                name (String): name of the body
        
        """
        ...
    @typing.overload
    def clearCelestialBodyLoaders(self) -> None:
        """
            Clear loaders for all celestial bodies.
        
            Calling this method also clears all loaded celestial bodies.
        
            Also see:
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addCelestialBodyLoader`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyCache`
        
        
        """
        ...
    @typing.overload
    def clearCelestialBodyLoaders(self, string: str) -> None:
        """
            Clear loaders for one celestial body.
        
            Calling this method also clears the celestial body that has been loaded via this
            :class:`~org.orekit.bodies.CelestialBodyLoader`.
        
            Parameters:
                name (String): name of the body
        
            Also see:
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addCelestialBodyLoader`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders`,
                :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyCache`
        
        """
        ...
    def getBody(self, string: str) -> CelestialBody:
        """
            Get a celestial body. The names of the common bodies are defined as constants in
            :class:`~org.orekit.bodies.CelestialBodyFactory`.
        
            If no :class:`~org.orekit.bodies.CelestialBodyLoader` has been added by calling
            :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addCelestialBodyLoader` or if
            :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.clearCelestialBodyLoaders` has been called afterwards, the
            :meth:`~org.orekit.bodies.LazyLoadedCelestialBodies.addDefaultCelestialBodyLoader` method will be called automatically,
            once with the default name for JPL DE ephemerides and once with the default name for IMCCE INPOP files.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getBody` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Parameters:
                name (String): name of the celestial body
        
            Returns:
                celestial body
        
        
        """
        ...
    def getEarth(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getEarth`
            Get the Earth singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getEarth` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Earth body
        
        
        """
        ...
    def getEarthMoonBarycenter(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getEarthMoonBarycenter`
            Get the Earth-Moon barycenter singleton bodies pair.
        
            Both the :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame` and
            :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame` for this bodies pair are aligned with
            :meth:`~org.orekit.frames.FramesFactory.getICRF` (and therefore also :meth:`~org.orekit.frames.FramesFactory.getGCRF`)
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getEarthMoonBarycenter`Â in
                interfaceÂ :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Earth-Moon barycenter bodies pair
        
        
        """
        ...
    def getJupiter(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getJupiter`
            Get the Jupiter singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getJupiter` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Jupiter body
        
        
        """
        ...
    def getMars(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getMars`
            Get the Mars singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getMars` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Mars body
        
        
        """
        ...
    def getMercury(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getMercury`
            Get the Mercury singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getMercury` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Sun body
        
        
        """
        ...
    def getMoon(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getMoon`
            Get the Moon singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getMoon` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Moon body
        
        
        """
        ...
    def getNeptune(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getNeptune`
            Get the Neptune singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getNeptune` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Neptune body
        
        
        """
        ...
    def getPluto(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getPluto`
            Get the Pluto singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getPluto` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Pluto body
        
        
        """
        ...
    def getSaturn(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getSaturn`
            Get the Saturn singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getSaturn` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Saturn body
        
        
        """
        ...
    def getSolarSystemBarycenter(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getSolarSystemBarycenter`
            Get the solar system barycenter aggregated body.
        
            Both the :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame` and
            :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame` for this aggregated body are aligned with
            :meth:`~org.orekit.frames.FramesFactory.getICRF` (and therefore also :meth:`~org.orekit.frames.FramesFactory.getGCRF`)
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getSolarSystemBarycenter`Â in
                interfaceÂ :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                solar system barycenter aggregated body
        
        
        """
        ...
    def getSun(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getSun`
            Get the Sun singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getSun` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Sun body
        
        
        """
        ...
    def getUranus(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getUranus`
            Get the Uranus singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getUranus` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Uranus body
        
        
        """
        ...
    def getVenus(self) -> CelestialBody:
        """
            Description copied from interface: :meth:`~org.orekit.bodies.CelestialBodies.getVenus`
            Get the Venus singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getVenus` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Venus body
        
        
        """
        ...

class OneAxisEllipsoid(Ellipsoid, BodyShape):
    """
    public class OneAxisEllipsoid extends :class:`~org.orekit.bodies.Ellipsoid` implements :class:`~org.orekit.bodies.BodyShape`
    
        Modeling of a one-axis ellipsoid.
    
        One-axis ellipsoids is a good approximate model for most planet-size and larger natural bodies. It is the equilibrium
        shape reached by a fluid body under its own gravity field when it rotates. The symmetry axis is the rotation or polar
        axis.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float, frame: org.orekit.frames.Frame): ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
            Get body frame related to body shape.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getBodyFrame` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Returns:
                body frame related to body shape
        
        
        """
        ...
    _getCartesianIntersectionPoint_0__T = typing.TypeVar('_getCartesianIntersectionPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getCartesianIntersectionPoint(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_getCartesianIntersectionPoint_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getCartesianIntersectionPoint_0__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getCartesianIntersectionPoint_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getCartesianIntersectionPoint_0__T]:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Parameters:
                line (FieldLine<T> line): test line (may intersect the body or not)
                close (FieldVector3D<T> close): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
            Since:
                9.3
        
        
        """
        ...
    @typing.overload
    def getCartesianIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Parameters:
                line (Line): test line (may intersect the body or not)
                close (Vector3D): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
            Since:
                9.3
        
        """
        ...
    def getEquatorialRadius(self) -> float:
        """
            Get the equatorial radius of the body.
        
            Returns:
                equatorial radius of the body (m)
        
        
        """
        ...
    def getFlattening(self) -> float:
        """
            Get the flattening of the body: f = (a-b)/a.
        
            Returns:
                the flattening
        
        
        """
        ...
    _getIntersectionPoint_0__T = typing.TypeVar('_getIntersectionPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getIntersectionPoint(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_0__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_0__T]) -> FieldGeodeticPoint[_getIntersectionPoint_0__T]:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                line (FieldLine<T> line): test line (may intersect the body or not)
                close (FieldVector3D<T> close): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> GeodeticPoint:
        """
            Get the intersection point of a line with the surface of the body.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                line (Line): test line (may intersect the body or not)
                close (Vector3D): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    @typing.overload
    def projectToGround(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Project a point to the ground.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (Vector3D): point to project
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Also see:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround`
        
        """
        ...
    @typing.overload
    def projectToGround(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Project a moving point to the ground.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): moving point
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Also see:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround`
        
        
        """
        ...
    def setAngularThreshold(self, double: float) -> None:
        """
            Set the angular convergence threshold.
        
            The angular threshold is used both to identify points close to the ellipse axes and as the convergence threshold used to
            stop the iterations in the :meth:`~org.orekit.bodies.OneAxisEllipsoid.transform` method.
        
            If this method is not called, the default value is set to 10 :sup:`-12` .
        
            Parameters:
                angularThreshold (double): angular convergence threshold (rad)
        
        
        """
        ...
    _transform_0__T = typing.TypeVar('_transform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, fieldGeodeticPoint: FieldGeodeticPoint[_transform_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_0__T]:
        """
            Transform a surface-relative point to a Cartesian point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
        """
        ...
    @typing.overload
    def transform(self, geodeticPoint: GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a surface-relative point to a Cartesian point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.GeodeticPoint`): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
            Transform a Cartesian point to a surface-relative point.
        
            This method is based on Toshio Fukushima's algorithm which uses Halley's method. transformation from Cartesian to
            Geodetic Coordinates Accelerated by Halley's Method, Toshio Fukushima, Journal of Geodesy 9(12):689-693, February 2006
        
            Some changes have been added to the original method:
        
              - in order to handle more accurately corner cases near the pole
              - in order to handle properly corner cases near the equatorial plane, even far inside the ellipsoid
              - in order to handle very flat ellipsoids
        
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (Vector3D): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Transform a Cartesian point to a surface-relative point.
        
            Parameters:
                point (:class:`~org.orekit.utils.PVCoordinates`): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point, using time as the single derivation parameter
        
        
        """
        ...
    @typing.overload
    def transform(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_2__T]) -> FieldGeodeticPoint[_transform_2__T]:
        """
            Transform a Cartesian point to a surface-relative point.
        
            This method is based on Toshio Fukushima's algorithm which uses Halley's method. transformation from Cartesian to
            Geodetic Coordinates Accelerated by Halley's Method, Toshio Fukushima, Journal of Geodesy 9(12):689-693, February 2006
        
            Some changes have been added to the original method:
        
              - in order to handle more accurately corner cases near the pole
              - in order to handle properly corner cases near the equatorial plane, even far inside the ellipsoid
              - in order to handle very flat ellipsoids
        
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (FieldVector3D<T> point): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
        """
        ...
    @typing.overload
    def transform(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> FieldGeodeticPoint[org.hipparchus.analysis.differentiation.DerivativeStructure]: ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> GeodeticPoint: ...

class PythonBodyShape(BodyShape):
    """
    public class PythonBodyShape extends Object implements :class:`~org.orekit.bodies.BodyShape`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
            Get body frame related to body shape. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getBodyFrame` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Returns:
                body frame related to body shape
        
        
        """
        ...
    _getIntersectionPoint_0__T = typing.TypeVar('_getIntersectionPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getIntersectionPoint(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_0__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_0__T]) -> FieldGeodeticPoint[_getIntersectionPoint_0__T]:
        """
            Get the intersection point of a line with the surface of the body. Extension point for Python.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                line (FieldLine<T> line): test line (may intersect the body or not)
                close (FieldVector3D<T> close): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> GeodeticPoint:
        """
            Get the intersection point of a line with the surface of the body. Extension point for Python.
        
            A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two
            points case). The close parameter is used to select which of these points should be returned. The selected point is the
            one that is closest to the close point.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.getIntersectionPoint` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                line (Line): test line (may intersect the body or not)
                close (Vector3D): point used for intersections selection
                frame (:class:`~org.orekit.frames.Frame`): frame in which line is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the line in given frame
        
            Returns:
                intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    @typing.overload
    def projectToGround(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Project a point to the ground. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (Vector3D): point to project
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Since:
                7.0
        
            Also see:
                :meth:`~org.orekit.bodies.PythonBodyShape.projectToGround`
        
        """
        ...
    @typing.overload
    def projectToGround(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Project a moving point to the ground. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.projectToGround` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                pv (:class:`~org.orekit.utils.TimeStampedPVCoordinates`): moving point
                frame (:class:`~org.orekit.frames.Frame`): frame in which moving point is expressed
        
            Returns:
                ground point exactly at the local vertical of specified point, in the same frame as specified point
        
            Since:
                7.0
        
            Also see:
                :meth:`~org.orekit.bodies.PythonBodyShape.projectToGround`
        
        
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
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_3__T = typing.TypeVar('_transform_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, geodeticPoint: GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a Cartesian point to a surface-relative point. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (Vector3D): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.AbsoluteDate`): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Transform a surface-relative point to a Cartesian point. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.GeodeticPoint`): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
            Transform a surface-relative point to a Cartesian point. Redirects to FieldVector3Dtransfor(...) for Python extension.
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> GeodeticPoint: ...
    @typing.overload
    def transform(self, fieldGeodeticPoint: FieldGeodeticPoint[_transform_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T]: ...
    @typing.overload
    def transform(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_3__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_3__T]) -> FieldGeodeticPoint[_transform_3__T]:
        """
            Transform a Cartesian point to a surface-relative point. Redirects to transform_FFF(...) for Python extension
        
            Specified by:
                :meth:`~org.orekit.bodies.BodyShape.transform` in interface :class:`~org.orekit.bodies.BodyShape`
        
            Parameters:
                point (FieldVector3D<T> point): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Since:
                9.0
        
        """
        ...
    _transform_F__T = typing.TypeVar('_transform_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def transform_F(self, fieldGeodeticPoint: FieldGeodeticPoint[_transform_F__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_F__T]:
        """
            Transform a surface-relative point to a Cartesian point. Extension point for Python. Connects to method transform.
        
            Parameters:
                point (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> point): surface-relative point
        
            Returns:
                point at the same location but as a Cartesian point
        
            Since:
                9.0
        
        
        """
        ...
    _transform_FFF__T = typing.TypeVar('_transform_FFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def transform_FFF(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_FFF__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_FFF__T]) -> FieldGeodeticPoint[_transform_FFF__T]:
        """
            Transform a Cartesian point to a surface-relative point. Extension point for Python.
        
            Parameters:
                point (FieldVector3D<T> point): Cartesian point
                frame (:class:`~org.orekit.frames.Frame`): frame in which Cartesian point is expressed
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date of the computation (used for frames conversions)
        
            Returns:
                point at the same location but as a surface-relative point
        
            Since:
                9.0
        
        
        """
        ...

class PythonCelestialBodies(CelestialBodies):
    """
    public class PythonCelestialBodies extends Object implements :class:`~org.orekit.bodies.CelestialBodies`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getBody(self, string: str) -> CelestialBody:
        """
            Get a celestial body. The names of the common bodies are defined as constants in
            :class:`~org.orekit.bodies.CelestialBodyFactory`.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getBody` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Parameters:
                name (String): name of the celestial body
        
            Returns:
                celestial body
        
        
        """
        ...
    def getEarth(self) -> CelestialBody:
        """
            Get the Earth singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getEarth` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Earth body
        
        
        """
        ...
    def getEarthMoonBarycenter(self) -> CelestialBody:
        """
            Get the Earth-Moon barycenter singleton bodies pair.
        
            Both the :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame` and
            :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame` for this bodies pair are aligned with
            :meth:`~org.orekit.frames.FramesFactory.getICRF` (and therefore also :meth:`~org.orekit.frames.FramesFactory.getGCRF`)
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getEarthMoonBarycenter`Â in
                interfaceÂ :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Earth-Moon barycenter bodies pair
        
        
        """
        ...
    def getJupiter(self) -> CelestialBody:
        """
            Get the Jupiter singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getJupiter` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Jupiter body
        
        
        """
        ...
    def getMars(self) -> CelestialBody:
        """
            Get the Mars singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getMars` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Mars body
        
        
        """
        ...
    def getMercury(self) -> CelestialBody:
        """
            Get the Mercury singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getMercury` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Sun body
        
        
        """
        ...
    def getMoon(self) -> CelestialBody:
        """
            Get the Moon singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getMoon` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Moon body
        
        
        """
        ...
    def getNeptune(self) -> CelestialBody:
        """
            Get the Neptune singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getNeptune` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Neptune body
        
        
        """
        ...
    def getPluto(self) -> CelestialBody:
        """
            Get the Pluto singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getPluto` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Pluto body
        
        
        """
        ...
    def getSaturn(self) -> CelestialBody:
        """
            Get the Saturn singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getSaturn` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Saturn body
        
        
        """
        ...
    def getSolarSystemBarycenter(self) -> CelestialBody:
        """
            Get the solar system barycenter aggregated body.
        
            Both the :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame` and
            :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame` for this aggregated body are aligned with
            :meth:`~org.orekit.frames.FramesFactory.getICRF` (and therefore also :meth:`~org.orekit.frames.FramesFactory.getGCRF`)
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getSolarSystemBarycenter`Â in
                interfaceÂ :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                solar system barycenter aggregated body
        
        
        """
        ...
    def getSun(self) -> CelestialBody:
        """
            Get the Sun singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getSun` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Sun body
        
        
        """
        ...
    def getUranus(self) -> CelestialBody:
        """
            Get the Uranus singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getUranus` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Uranus body
        
        
        """
        ...
    def getVenus(self) -> CelestialBody:
        """
            Get the Venus singleton body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodies.getVenus` in interface :class:`~org.orekit.bodies.CelestialBodies`
        
            Returns:
                Venus body
        
        
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

class PythonCelestialBody(CelestialBody):
    """
    public class PythonCelestialBody extends Object implements :class:`~org.orekit.bodies.CelestialBody`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getBodyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
            Get a body oriented, body centered frame. Extension point for Python.
        
            The frame is always bound to the body center, and its axes have a fixed orientation with respect to the celestial body.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBody.getBodyOrientedFrame` in interface :class:`~org.orekit.bodies.CelestialBody`
        
            Returns:
                a body oriented, body centered frame
        
            Also see:
                :meth:`~org.orekit.bodies.PythonCelestialBody.getInertiallyOrientedFrame`
        
        
        """
        ...
    def getGM(self) -> float:
        """
            Get the attraction coefficient of the body. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBody.getGM` in interface :class:`~org.orekit.bodies.CelestialBody`
        
            Returns:
                attraction coefficient of the body (mÂ³/sÂ²)
        
        
        """
        ...
    def getInertiallyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
            Get an inertially oriented, body centered frame. Extension point for Python.
        
            The frame is always bound to the body center, and its axes have a fixed orientation with respect to other inertial
            frames.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBody.getInertiallyOrientedFrame`Â in
                interfaceÂ :class:`~org.orekit.bodies.CelestialBody`
        
            Returns:
                an inertially oriented, body centered frame
        
            Also see:
                :meth:`~org.orekit.bodies.PythonCelestialBody.getBodyOrientedFrame`
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the body. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBody.getName` in interface :class:`~org.orekit.bodies.CelestialBody`
        
            Returns:
                name of the body
        
        
        """
        ...
    _getPVCoordinates_1__T = typing.TypeVar('_getPVCoordinates_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :code:`PVCoordinates` of the body in the selected frame. Extension point for Python.
        
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
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_1__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getPVCoordinates_1__T]:
        """
            Get the :code:`FieldPVCoordinates` of the body in the selected frame. Links to getPVCoordinates_FF() for Python
            extension
        
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
    def getPVCoordinates_FF(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_FF__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getPVCoordinates_FF__T]:
        """
            Get the :code:`FieldPVCoordinates` of the body in the selected frame. Extension point for Python. Links to
            getPVCoordinates()
        
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
    _toFieldPVCoordinatesProvider__T = typing.TypeVar('_toFieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toFieldPVCoordinatesProvider(self, field: org.hipparchus.Field[_toFieldPVCoordinatesProvider__T]) -> org.orekit.utils.FieldPVCoordinatesProvider[_toFieldPVCoordinatesProvider__T]:
        """
            Convert to a :class:`~org.orekit.utils.FieldPVCoordinatesProvider` with a specific type. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.utils.ExtendedPVCoordinatesProvider.toFieldPVCoordinatesProvider`Â in
                interfaceÂ :class:`~org.orekit.utils.ExtendedPVCoordinatesProvider`
        
            Parameters:
                field (Field<T> field): field for the argument and value
        
            Returns:
                converted function
        
        
        """
        ...

class PythonCelestialBodyLoader(CelestialBodyLoader):
    """
    public class PythonCelestialBodyLoader extends Object implements :class:`~org.orekit.bodies.CelestialBodyLoader`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def loadCelestialBody(self, string: str) -> CelestialBody:
        """
            Load celestial body. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.bodies.CelestialBodyLoader.loadCelestialBody`Â in
                interfaceÂ :class:`~org.orekit.bodies.CelestialBodyLoader`
        
            Parameters:
                name (String): name of the celestial body
        
            Returns:
                loaded celestial body
        
        
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

class PythonIAUPole(IAUPole):
    """
    public class PythonIAUPole extends Object implements :class:`~org.orekit.bodies.IAUPole`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getNode_1__T = typing.TypeVar('_getNode_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNode(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the body Q Node direction in ICRF frame.
        
            Specified by:
                :meth:`~org.orekit.bodies.IAUPole.getNode` in interface :class:`~org.orekit.bodies.IAUPole`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                body Q Node direction in ICRF frame
        
            Since:
                9.1
        
            Get the body Q Node direction in ICRF frame.
        
            Specified by:
                :meth:`~org.orekit.bodies.IAUPole.getNode` in interface :class:`~org.orekit.bodies.IAUPole`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                body Q Node direction in ICRF frame
        
            Since:
                9.1
        
        
        """
        ...
    @typing.overload
    def getNode(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getNode_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNode_1__T]: ...
    _getNode_F__T = typing.TypeVar('_getNode_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getNode_F(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getNode_F__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNode_F__T]:
        """
            Get the body Q Node direction in ICRF frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                body Q Node direction in ICRF frame
        
            Since:
                9.1
        
        
        """
        ...
    _getPole_1__T = typing.TypeVar('_getPole_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPole(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the body North pole direction in ICRF frame.
        
            Specified by:
                :meth:`~org.orekit.bodies.IAUPole.getPole` in interface :class:`~org.orekit.bodies.IAUPole`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                body North pole direction in ICRF frame
        
            Get the body North pole direction in ICRF frame.
        
            Specified by:
                :meth:`~org.orekit.bodies.IAUPole.getPole` in interface :class:`~org.orekit.bodies.IAUPole`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                body North pole direction in ICRF frame
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def getPole(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPole_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPole_1__T]: ...
    _getPole_F__T = typing.TypeVar('_getPole_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPole_F(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPole_F__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPole_F__T]:
        """
            Get the body North pole direction in ICRF frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                body North pole direction in ICRF frame
        
            Since:
                9.0
        
        
        """
        ...
    _getPrimeMeridianAngle_1__T = typing.TypeVar('_getPrimeMeridianAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPrimeMeridianAngle(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the prime meridian angle.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
            Specified by:
                :meth:`~org.orekit.bodies.IAUPole.getPrimeMeridianAngle` in interface :class:`~org.orekit.bodies.IAUPole`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                prime meridian vector
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngle(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPrimeMeridianAngle_1__T]) -> _getPrimeMeridianAngle_1__T:
        """
            Get the prime meridian angle.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
            Specified by:
                :meth:`~org.orekit.bodies.IAUPole.getPrimeMeridianAngle` in interface :class:`~org.orekit.bodies.IAUPole`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                prime meridian vector
        
            Since:
                9.0
        
        
        """
        ...
    _getPrimeMeridianAngle_F__T = typing.TypeVar('_getPrimeMeridianAngle_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPrimeMeridianAngle_F(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPrimeMeridianAngle_F__T]) -> _getPrimeMeridianAngle_F__T:
        """
            Get the prime meridian angle.
        
            The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
        
            Returns:
                prime meridian vector
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.bodies")``.

    BodyShape: typing.Type[BodyShape]
    CR3BPFactory: typing.Type[CR3BPFactory]
    CR3BPSystem: typing.Type[CR3BPSystem]
    CelestialBodies: typing.Type[CelestialBodies]
    CelestialBody: typing.Type[CelestialBody]
    CelestialBodyFactory: typing.Type[CelestialBodyFactory]
    CelestialBodyLoader: typing.Type[CelestialBodyLoader]
    Ellipse: typing.Type[Ellipse]
    Ellipsoid: typing.Type[Ellipsoid]
    FieldGeodeticPoint: typing.Type[FieldGeodeticPoint]
    GeodeticPoint: typing.Type[GeodeticPoint]
    IAUPole: typing.Type[IAUPole]
    JPLEphemeridesLoader: typing.Type[JPLEphemeridesLoader]
    LazyLoadedCelestialBodies: typing.Type[LazyLoadedCelestialBodies]
    OneAxisEllipsoid: typing.Type[OneAxisEllipsoid]
    PythonBodyShape: typing.Type[PythonBodyShape]
    PythonCelestialBodies: typing.Type[PythonCelestialBodies]
    PythonCelestialBody: typing.Type[PythonCelestialBody]
    PythonCelestialBodyLoader: typing.Type[PythonCelestialBodyLoader]
    PythonIAUPole: typing.Type[PythonIAUPole]
