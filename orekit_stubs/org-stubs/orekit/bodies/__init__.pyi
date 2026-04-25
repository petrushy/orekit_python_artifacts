
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

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



class AnalyticalSolarPositionProvider(org.orekit.utils.ExtendedPositionProvider):
    """
    Class computing low-fidelity positions for the Sun. They should only be used in the decades around the year 2000.
    
    Reference: Montenbruck, Oliver, and Gill, Eberhard. Satellite orbits : models, methods, and applications. Berlin New York: Springer, 2000.
    
    Since:
        12.2
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
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

class BodyShape:
    """
    Interface representing the rigid surface shape of a natural body.
    
    The shape is not provided as a single complete geometric model, but single points can be queried (getIntersectionPoint).
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
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_0__T], close: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_0__T], frame: org.orekit.frames.Frame, date: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_0__T]) -> 'FieldGeodeticPoint'[_getIntersectionPoint_0__T]:
        """
        Get the intersection point of a line with the surface of the body.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Parameters:
            line (FieldLine<T> line): test line (may intersect the body or not)
            close (FieldVector3D<T> close): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (FieldAbsoluteDate<T> date): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        Since:
            9.0
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, close: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, date: org.orekit.time.AbsoluteDate) -> 'GeodeticPoint':
        """
        Get the intersection point of a line with the surface of the body.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Parameters:
            line (Line): test line (may intersect the body or not)
            close (Vector3D): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (AbsoluteDate): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    @typing.overload
    def projectToGround(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Project a point to the ground.
        
        Parameters:
            point (Vector3D): point to project
            date (AbsoluteDate): current date
            frame (Frame): frame in which moving point is expressed
        
        Returns:
            ground point exactly at the local vertical of specified point, in the same frame as specified point
        
        Since:
            7.0
        
        Also see:
            projectToGround
        
        """
        ...
    @typing.overload
    def projectToGround(self, pv: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Project a moving point to the ground.
        
        Parameters:
            pv (TimeStampedPVCoordinates): moving point
            frame (Frame): frame in which moving point is expressed
        
        Returns:
            ground point exactly at the local vertical of specified point, in the same frame as specified point
        
        Since:
            7.0
        
        Also see:
            projectToGround
        
        
        """
        ...
    _transform_0__T = typing.TypeVar('_transform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, point: 'FieldGeodeticPoint'[_transform_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_0__T]:
        """
        Transform a surface-relative point to a Cartesian point.
        
        Parameters:
            point (FieldGeodeticPoint<T> point): surface-relative point
        
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
            frame (Frame): frame in which Cartesian point is expressed
            date (AbsoluteDate): date of the computation (used for frames conversions)
        
        Returns:
            point at the same location but as a surface-relative point
        
        Transform a surface-relative point to a Cartesian point.
        
        Parameters:
            point (GeodeticPoint): surface-relative point
        
        Returns:
            point at the same location but as a Cartesian point
        
        """
        ...
    @typing.overload
    def transform(self, point: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T], frame: org.orekit.frames.Frame, date: org.orekit.time.FieldAbsoluteDate[_transform_2__T]) -> 'FieldGeodeticPoint'[_transform_2__T]:
        """
        Transform a Cartesian point to a surface-relative point.
        
        Parameters:
            point (FieldVector3D<T> point): Cartesian point
            frame (Frame): frame in which Cartesian point is expressed
            date (FieldAbsoluteDate<T> date): date of the computation (used for frames conversions)
        
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
    Factory class creating predefined CR3BP system using CR3BPSystem class. For example, Earth-Moon CR3BP System.
    
    Since:
        10.2
    
    Also see:
        CR3BPSystem
    """
    @staticmethod
    def getEarthMoonCR3BP() -> 'CR3BPSystem':
        """
        Get the Earth-Moon CR3BP singleton bodies pair.
        
        Returns:
            Earth-Moon CR3BP system
        
        
        """
        ...
    @staticmethod
    def getSunEarthCR3BP(date: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> 'CR3BPSystem':
        """
        Get the Sun-Earth CR3BP singleton bodies pair.
        
        Parameters:
            date (AbsoluteDate): date
            timeScale (TimeScale): time scale
        
        Returns:
            Sun-Earth CR3BP system
        
        
        """
        ...
    @staticmethod
    def getSunJupiterCR3BP(date: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> 'CR3BPSystem':
        """
        Get the Sun-Jupiter CR3BP singleton bodies pair.
        
        Parameters:
            date (AbsoluteDate): date
            timeScale (TimeScale): time scale
        
        Returns:
            Sun-Jupiter CR3BP system
        
        
        """
        ...
    @staticmethod
    def getSystem(primaryBody: 'CelestialBody', secondaryBody: 'CelestialBody', a: float) -> 'CR3BPSystem':
        """
        Get the corresponding CR3BP System.
        
        Parameters:
            primaryBody (CelestialBody): Primary Body in the CR3BP System
            secondaryBody (CelestialBody): Secondary Body in the CR3BP System
            a (double): Semi-Major Axis of the secondary body
        
        Returns:
            corresponding CR3BP System
        
        
        """
        ...

class CR3BPSystem:
    """
    Class creating, from two different celestial bodies, the corresponding system with respect to the Circular Restricted Three Body problem hypotheses.
    
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
    def getGamma(self, lagrangianPoint: org.orekit.utils.LagrangianPoints) -> float:
        """
        Get the position of the Lagrangian point in the CR3BP Rotating frame.
        
        Parameters:
            lagrangianPoint (LagrangianPoints): Lagrangian Point to consider
        
        Returns:
            Distance between a Lagrangian Point and its closest primary.
        
        
        """
        ...
    def getLPosition(self, lagrangianPoint: org.orekit.utils.LagrangianPoints) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position of the Lagrangian point in the CR3BP Rotating frame.
        
        Parameters:
            lagrangianPoint (LagrangianPoints): Lagrangian Point to consider
        
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
    def getRealAPV(self, apv0: org.orekit.utils.AbsolutePVCoordinates, initialDate: org.orekit.time.AbsoluteDate, outputFrame: org.orekit.frames.Frame) -> org.orekit.utils.AbsolutePVCoordinates:
        """
        Get the AbsolutePVCoordinates from normalized units to standard units in an output frame. This method ensure the constituency of the date of returned AbsolutePVCoordinate, especially when apv0 is the result of a propagation in CR3BP normalized model.
        
        Parameters:
            apv0 (AbsolutePVCoordinates): Normalized AbsolutePVCoordinates in the rotating frame
            initialDate (AbsoluteDate): Date of the at the beginning of the propagation
            outputFrame (Frame): Frame in which the output AbsolutePVCoordinates will be
        
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
    Commonly used celestial bodies. This interface defines methods for obtaining intances of the commonly used celestial bodies.
    
    Since:
        10.1
    
    Also see:
        CelestialBodyFactory
    """
    def getBody(self, name: str) -> 'CelestialBody':
        """
        Get a celestial body. The names of the common bodies are defined as constants in CelestialBodyFactory.
        
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
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this bodies pair are aligned with getICRF (and therefore also getGCRF)
        
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
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this aggregated body are aligned with getICRF (and therefore also getGCRF)
        
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

class CelestialBody(org.orekit.utils.ExtendedPositionProvider):
    """
    Interface for celestial bodies like Sun, Moon or solar system planets.
    
    Also see:
        CelestialBodyFactory
    """
    def getBodyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
        Get a body oriented, body centered frame.
        
        The frame is always bound to the body center, and its axes have a fixed orientation with respect to the celestial body.
        
        Returns:
            a body oriented, body centered frame
        
        Also see:
            getInertiallyOrientedFrame
        
        
        """
        ...
    def getGM(self) -> float:
        """
        Get the attraction coefficient of the body.
        
        Returns:
            attraction coefficient of the body (m³/s²)
        
        
        """
        ...
    def getInertiallyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
        Get an inertially oriented, body centered frame.
        
        The frame is always bound to the body center, and its axes have a fixed orientation with respect to other inertial frames.
        
        Returns:
            an inertially oriented, body centered frame
        
        Also see:
            getBodyOrientedFrame
        
        
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
    Factory class for bodies of the solar system.
    
    The getSun, the getMoon and the planets (including the Pluto dwarf planet) are provided by this factory. In addition, two important points are provided for convenience: the getSolarSystemBarycenter and the getEarthMoonBarycenter.
    
    The underlying body-centered frames are either direct children of getEME2000 (for getMoon and getEarthMoonBarycenter) or children from other body-centered frames. For example, the path from EME2000 to Jupiter-centered frame is: EME2000, Earth-Moon barycenter centered, solar system barycenter centered, Jupiter-centered. The defining transforms of these frames are combinations of simple linear transforms without any rotation. The frame axes are therefore always parallel to getEME2000 frame axes.
    
    The position of the bodies provided by this class are interpolated using the JPL DE 405/DE 406 ephemerides.
    """
    SOLAR_SYSTEM_BARYCENTER: typing.ClassVar[str] = ...
    """
    Predefined name for solar system barycenter.
    
    Also see:
        getBody, constant
    
    
    """
    SUN: typing.ClassVar[str] = ...
    """
    Predefined name for Sun.
    
    Also see:
        getBody, constant
    
    
    """
    MERCURY: typing.ClassVar[str] = ...
    """
    Predefined name for Mercury.
    
    Also see:
        getBody, constant
    
    
    """
    VENUS: typing.ClassVar[str] = ...
    """
    Predefined name for Venus.
    
    Also see:
        getBody, constant
    
    
    """
    EARTH_MOON: typing.ClassVar[str] = ...
    """
    Predefined name for Earth-Moon barycenter.
    
    Also see:
        getBody, constant
    
    
    """
    EARTH: typing.ClassVar[str] = ...
    """
    Predefined name for Earth.
    
    Also see:
        getBody, constant
    
    
    """
    MOON: typing.ClassVar[str] = ...
    """
    Predefined name for Moon.
    
    Also see:
        getBody, constant
    
    
    """
    MARS: typing.ClassVar[str] = ...
    """
    Predefined name for Mars.
    
    Also see:
        getBody, constant
    
    
    """
    JUPITER: typing.ClassVar[str] = ...
    """
    Predefined name for Jupiter.
    
    Also see:
        getBody, constant
    
    
    """
    SATURN: typing.ClassVar[str] = ...
    """
    Predefined name for Saturn.
    
    Also see:
        getBody, constant
    
    
    """
    URANUS: typing.ClassVar[str] = ...
    """
    Predefined name for Uranus.
    
    Also see:
        getBody, constant
    
    
    """
    NEPTUNE: typing.ClassVar[str] = ...
    """
    Predefined name for Neptune.
    
    Also see:
        getBody, constant
    
    
    """
    PLUTO: typing.ClassVar[str] = ...
    """
    Predefined name for Pluto.
    
    Also see:
        getBody, constant
    
    
    """
    @staticmethod
    def addCelestialBodyLoader(name: str, loader: typing.Union['CelestialBodyLoader', typing.Callable]) -> None:
        """
        Add a loader for celestial bodies.
        
        Parameters:
            name (String): name of the body (may be one of the predefined names or a user-defined name)
            loader (CelestialBodyLoader): custom loader to add for the body
        
        Also see:
            addDefaultCelestialBodyLoader,
            clearCelestialBodyLoaders,
            clearCelestialBodyLoaders
        
        
        """
        ...
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
    def getBody(name: str) -> CelestialBody:
        """
        Get a celestial body.
        
        If no CelestialBodyLoader has been added by calling addCelestialBodyLoader or if clearCelestialBodyLoaders has been called afterwards, the addDefaultCelestialBodyLoader method will be called automatically, once with the default name for JPL DE ephemerides and once with the default name for IMCCE INPOP files.
        
        Parameters:
            name (String): name of the celestial body
        
        Returns:
            celestial body
        
        
        """
        ...
    @staticmethod
    def getCelestialBodies() -> 'LazyLoadedCelestialBodies':
        """
        Get the instance of CelestialBodies that is called by the static methods in this class.
        
        Returns:
            the reference frames used by this factory.
        
        
        """
        ...
    @staticmethod
    def getEarth() -> CelestialBody:
        """
        Get the Earth singleton body.
        
        Returns:
            Earth body
        
        
        """
        ...
    @staticmethod
    def getEarthMoonBarycenter() -> CelestialBody:
        """
        Get the Earth-Moon barycenter singleton bodies pair.
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this bodies pair are aligned with getICRF (and therefore also getGCRF)
        
        Returns:
            Earth-Moon barycenter bodies pair
        
        
        """
        ...
    @staticmethod
    def getJupiter() -> CelestialBody:
        """
        Get the Jupiter singleton body.
        
        Returns:
            Jupiter body
        
        
        """
        ...
    @staticmethod
    def getMars() -> CelestialBody:
        """
        Get the Mars singleton body.
        
        Returns:
            Mars body
        
        
        """
        ...
    @staticmethod
    def getMercury() -> CelestialBody:
        """
        Get the Mercury singleton body.
        
        Returns:
            Sun body
        
        
        """
        ...
    @staticmethod
    def getMoon() -> CelestialBody:
        """
        Get the Moon singleton body.
        
        Returns:
            Moon body
        
        
        """
        ...
    @staticmethod
    def getNeptune() -> CelestialBody:
        """
        Get the Neptune singleton body.
        
        Returns:
            Neptune body
        
        
        """
        ...
    @staticmethod
    def getPluto() -> CelestialBody:
        """
        Get the Pluto singleton body.
        
        Returns:
            Pluto body
        
        
        """
        ...
    @staticmethod
    def getSaturn() -> CelestialBody:
        """
        Get the Saturn singleton body.
        
        Returns:
            Saturn body
        
        
        """
        ...
    @staticmethod
    def getSolarSystemBarycenter() -> CelestialBody:
        """
        Get the solar system barycenter aggregated body.
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this aggregated body are aligned with getICRF (and therefore also getGCRF)
        
        Returns:
            solar system barycenter aggregated body
        
        
        """
        ...
    @staticmethod
    def getSun() -> CelestialBody:
        """
        Get the Sun singleton body.
        
        Returns:
            Sun body
        
        
        """
        ...
    @staticmethod
    def getUranus() -> CelestialBody:
        """
        Get the Uranus singleton body.
        
        Returns:
            Uranus body
        
        
        """
        ...
    @staticmethod
    def getVenus() -> CelestialBody:
        """
        Get the Venus singleton body.
        
        Returns:
            Venus body
        
        
        """
        ...

class CelestialBodyLoader:
    """
    Interface for loading celestial bodies.
    """
    def loadCelestialBody(self, name: str) -> CelestialBody:
        """
        Load celestial body.
        
        Parameters:
            name (String): name of the celestial body
        
        Returns:
            loaded celestial body
        
        
        """
        ...

class Ellipse:
    """
    Model of a 2D ellipse in 3D space.
    
    These ellipses are mainly created as plane sections of general 3D ellipsoids, but can be used for other purposes.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        7.0
    
    Also see:
        getPlaneSection
    """
    def __init__(self, center: org.hipparchus.geometry.euclidean.threed.Vector3D, u: org.hipparchus.geometry.euclidean.threed.Vector3D, v: org.hipparchus.geometry.euclidean.threed.Vector3D, a: float, b: float, frame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            center (Vector3D): center of the 2D ellipse
            u (Vector3D): unit vector along the major axis
            v (Vector3D): unit vector along the minor axis
            a (double): semi major axis
            b (double): semi minor axis
            frame (Frame): frame in which the ellipse is defined
        
        
        """
        ...
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
    def getCenterOfCurvature(self, point: org.hipparchus.geometry.euclidean.twod.Vector2D) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
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
    def pointAt(self, theta: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
            pv (TimeStampedPVCoordinates): position-velocity-acceleration to project, in the reference frame
        
        Returns:
            projected position-velocity-acceleration
        
        
        """
        ...
    @typing.overload
    def projectToEllipse(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def toPlane(self, p: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
        Project a point to the ellipse plane.
        
        Parameters:
            p (Vector3D): point defined with respect to 3D frame
        
        Returns:
            point defined with respect to ellipse
        
        Also see:
            toSpace
        
        
        """
        ...
    def toSpace(self, p: org.hipparchus.geometry.euclidean.twod.Vector2D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Create a point from its ellipse-relative coordinates.
        
        Parameters:
            p (Vector2D): point defined with respect to ellipse
        
        Returns:
            point defined with respect to 3D frame
        
        Also see:
            toPlane
        
        
        """
        ...

class Ellipsoid:
    """
    Modeling of a general three-axes ellipsoid.
    
    Since:
        7.0
    """
    def __init__(self, frame: org.orekit.frames.Frame, a: float, b: float, c: float):
        """
        Simple constructor.
        
        Parameters:
            frame (Frame): at the ellipsoid center, aligned with principal axes
            a (double): first semi-axis length
            b (double): second semi-axis length
            c (double): third semi-axis length
        
        
        """
        ...
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
    _getPlaneSection_1__T = typing.TypeVar('_getPlaneSection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPlaneSection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> Ellipse: ...
    @typing.overload
    def getPlaneSection(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPlaneSection_1__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPlaneSection_1__T]) -> 'FieldEllipse'[_getPlaneSection_1__T]: ...
    _isInside_0__T = typing.TypeVar('_isInside_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isInside(self, point: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_isInside_0__T]) -> bool:
        """
        Check if a point is inside the ellipsoid.
        
        Parameters:
            point (FieldVector3D<T> point): point to check, in the ellipsoid frame
        
        Returns:
            true if the point is inside the ellipsoid (or exactly on ellipsoid surface)
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def isInside(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D) -> bool:
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
    _pointOnLimb_0__T = typing.TypeVar('_pointOnLimb_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pointOnLimb(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_pointOnLimb_0__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_pointOnLimb_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_pointOnLimb_0__T]: ...
    @typing.overload
    def pointOnLimb(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

_FieldEllipse__T = typing.TypeVar('_FieldEllipse__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEllipse(typing.Generic[_FieldEllipse__T]):
    """
    Model of a 2D ellipse in 3D space.
    
    These ellipses are mainly created as plane sections of general 3D ellipsoids, but can be used for other purposes.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        12.0
    
    Also see:
        getPlaneSection
    """
    def __init__(self, center: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T], u: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T], v: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T], a: _FieldEllipse__T, b: _FieldEllipse__T, frame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            center (FieldVector3D<FieldEllipse> center): center of the 2D ellipse
            u (FieldVector3D<FieldEllipse> u): unit vector along the major axis
            v (FieldVector3D<FieldEllipse> v): unit vector along the minor axis
            a (FieldEllipse): semi major axis
            b (FieldEllipse): semi minor axis
            frame (Frame): frame in which the ellipse is defined
        
        
        """
        ...
    def getA(self) -> _FieldEllipse__T:
        """
        Get the semi major axis.
        
        Returns:
            semi major axis
        
        
        """
        ...
    def getB(self) -> _FieldEllipse__T:
        """
        Get the semi minor axis.
        
        Returns:
            semi minor axis
        
        
        """
        ...
    def getCenter(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T]:
        """
        Get the center of the 2D ellipse.
        
        Returns:
            center of the 2D ellipse
        
        
        """
        ...
    def getCenterOfCurvature(self, point: org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldEllipse__T]) -> org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldEllipse__T]:
        """
        Find the center of curvature (point on the evolute) at the nadir of a point.
        
        Parameters:
            point (FieldVector2D<FieldEllipse> point): point in the ellipse plane
        
        Returns:
            center of curvature of the ellipse directly at point nadir
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the defining frame.
        
        Returns:
            defining frame
        
        
        """
        ...
    def getU(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T]:
        """
        Get the unit vector along the major axis.
        
        Returns:
            unit vector along the major axis
        
        
        """
        ...
    def getV(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T]:
        """
        Get the unit vector along the minor axis.
        
        Returns:
            unit vector along the minor axis
        
        
        """
        ...
    def pointAt(self, theta: _FieldEllipse__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T]:
        """
        Get a point of the 2D ellipse.
        
        Parameters:
            theta (FieldEllipse): angular parameter on the ellipse (really the eccentric anomaly)
        
        Returns:
            ellipse point at theta, in underlying ellipsoid frame
        
        
        """
        ...
    @typing.overload
    def projectToEllipse(self, fieldVector2D: org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldEllipse__T]) -> org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldEllipse__T]: ...
    @typing.overload
    def projectToEllipse(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldEllipse__T]) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldEllipse__T]: ...
    def toPlane(self, p: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T]) -> org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldEllipse__T]:
        """
        Project a point to the ellipse plane.
        
        Parameters:
            p (FieldVector3D<FieldEllipse> p): point defined with respect to 3D frame
        
        Returns:
            point defined with respect to ellipse
        
        Also see:
            toSpace
        
        
        """
        ...
    def toSpace(self, p: org.hipparchus.geometry.euclidean.twod.FieldVector2D[_FieldEllipse__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldEllipse__T]:
        """
        Create a point from its ellipse-relative coordinates.
        
        Parameters:
            p (FieldVector2D<FieldEllipse> p): point defined with respect to ellipse
        
        Returns:
            point defined with respect to 3D frame
        
        Also see:
            toPlane
        
        
        """
        ...

_FieldGeodeticPoint__T = typing.TypeVar('_FieldGeodeticPoint__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGeodeticPoint(typing.Generic[_FieldGeodeticPoint__T]):
    """
    Point location relative to a 2D body surface, using CalculusFieldElement.
    
    Instance of this class are guaranteed to be immutable.
    
    Since:
        7.1
    
    Also see:
        BodyShape
    """
    @typing.overload
    def __init__(self, t: _FieldGeodeticPoint__T, t2: _FieldGeodeticPoint__T, t3: _FieldGeodeticPoint__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldGeodeticPoint__T], geodeticPoint: 'GeodeticPoint'): ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getAltitude(self) -> _FieldGeodeticPoint__T:
        """
        Get the altitude.
        
        Returns:
            altitude
        
        
        """
        ...
    def getEast(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]:
        """
        Get the direction to the east of point, expressed in parent shape frame.
        
        The east direction is defined in the horizontal plane in order to complete direct triangle (east, north, zenith).
        
        Returns:
            unit vector in the east direction
        
        Also see:
            getWest
        
        
        """
        ...
    def getLatitude(self) -> _FieldGeodeticPoint__T:
        """
        Get the latitude.
        
        Returns:
            latitude, an angular value in the range [-π/2, π/2]
        
        
        """
        ...
    def getLongitude(self) -> _FieldGeodeticPoint__T:
        """
        Get the longitude.
        
        Returns:
            longitude, an angular value in the range [-π, π]
        
        
        """
        ...
    def getNadir(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]:
        """
        Get the direction below the point, expressed in parent shape frame.
        
        The nadir direction is the opposite of zenith direction.
        
        Returns:
            unit vector in the nadir direction
        
        Also see:
            getZenith
        
        
        """
        ...
    def getNorth(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]:
        """
        Get the direction to the north of point, expressed in parent shape frame.
        
        The north direction is defined in the horizontal plane (normal to zenith direction) and following the local meridian.
        
        Returns:
            unit vector in the north direction
        
        Also see:
            getSouth
        
        
        """
        ...
    def getSouth(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]:
        """
        Get the direction to the south of point, expressed in parent shape frame.
        
        The south direction is the opposite of north direction.
        
        Returns:
            unit vector in the south direction
        
        Also see:
            getNorth
        
        
        """
        ...
    def getWest(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]:
        """
        Get the direction to the west of point, expressed in parent shape frame.
        
        The west direction is the opposite of east direction.
        
        Returns:
            unit vector in the west direction
        
        Also see:
            getEast
        
        
        """
        ...
    def getZenith(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldGeodeticPoint__T]:
        """
        Get the direction above the point, expressed in parent shape frame.
        
        The zenith direction is defined as the normal to local horizontal plane.
        
        Returns:
            unit vector in the zenith direction
        
        Also see:
            getNadir
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def toGeodeticPoint(self) -> 'GeodeticPoint':
        """
        Get non-Field equivalent.
        
        Returns:
            geodetic point
        
        Since:
            12.2
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class GeodeticPoint(java.io.Serializable):
    """
    Point location relative to a 2D body surface.
    
    Instance of this class are guaranteed to be immutable.
    
    Also see:
        BodyShape, FieldGeodeticPoint, serialized
    """
    NORTH_POLE: typing.ClassVar['GeodeticPoint'] = ...
    """
    North pole.
    
    Since:
        10.0
    
    
    """
    SOUTH_POLE: typing.ClassVar['GeodeticPoint'] = ...
    """
    South pole.
    
    Since:
        10.0
    
    
    """
    def __init__(self, latitude: float, longitude: float, altitude: float):
        """
        Build a new instance. The angular coordinates will be normalized so that the latitude is between ±π/2 and the longitude is between ±π.
        
        Parameters:
            latitude (double): latitude of the point (rad)
            longitude (double): longitude of the point (rad)
            altitude (double): altitude of the point (m)
        
        Also see:
            SexagesimalAngle
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
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
            getWest
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
        Get the latitude.
        
        Returns:
            latitude, an angular value in the range [-π/2, π/2]
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
        Get the longitude.
        
        Returns:
            longitude, an angular value in the range [-π, π]
        
        
        """
        ...
    def getNadir(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the direction below the point, expressed in parent shape frame.
        
        The nadir direction is the opposite of zenith direction.
        
        Returns:
            unit vector in the nadir direction
        
        Also see:
            getZenith
        
        
        """
        ...
    def getNorth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the direction to the north of point, expressed in parent shape frame.
        
        The north direction is defined in the horizontal plane (normal to zenith direction) and following the local meridian.
        
        Returns:
            unit vector in the north direction
        
        Also see:
            getSouth
        
        
        """
        ...
    def getSouth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the direction to the south of point, expressed in parent shape frame.
        
        The south direction is the opposite of north direction.
        
        Returns:
            unit vector in the south direction
        
        Also see:
            getNorth
        
        
        """
        ...
    def getWest(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the direction to the west of point, expressed in parent shape frame.
        
        The west direction is the opposite of east direction.
        
        Returns:
            unit vector in the west direction
        
        Also see:
            getEast
        
        
        """
        ...
    def getZenith(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the direction above the point, expressed in parent shape frame.
        
        The zenith direction is defined as the normal to local horizontal plane.
        
        Returns:
            unit vector in the zenith direction
        
        Also see:
            getNadir
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class IAUPole(java.io.Serializable):
    """
    Interface for IAU pole and prime meridian orientations.
    
    This interface defines methods compliant with the report of the IAU/IAG Working Group on Cartographic Coordinates and Rotational Elements of the Planets and Satellites (WGCCRE). These definitions are common for all recent versions of this report published every three years.
    
    The precise values of pole direction and W angle coefficients may vary from publication year as models are adjusted. The latest value of constants for implementing this interface can be found in the `working group site <http://astrogeology.usgs.gov/Projects/WGCCRE/>`.
    
    Also see:
        CelestialBodies
    """
    _getNode_0__T = typing.TypeVar('_getNode_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNode(self, date: org.orekit.time.FieldAbsoluteDate[_getNode_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNode_0__T]:
        """
        Get the body Q Node direction in ICRF frame.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            body Q Node direction in ICRF frame
        
        Since:
            9.1
        
        
        """
        ...
    @typing.overload
    def getNode(self, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the body Q Node direction in ICRF frame.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            body Q Node direction in ICRF frame
        
        Since:
            9.1
        
        """
        ...
    _getPole_0__T = typing.TypeVar('_getPole_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPole(self, date: org.orekit.time.FieldAbsoluteDate[_getPole_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPole_0__T]:
        """
        Get the body North pole direction in ICRF frame.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            body North pole direction in ICRF frame
        
        Since:
            9.0
        
        
        """
        ...
    @typing.overload
    def getPole(self, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the body North pole direction in ICRF frame.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            body North pole direction in ICRF frame
        
        """
        ...
    _getPrimeMeridianAngle_1__T = typing.TypeVar('_getPrimeMeridianAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPrimeMeridianAngle(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the prime meridian angle.
        
        The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            prime meridian vector
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngle(self, date: org.orekit.time.FieldAbsoluteDate[_getPrimeMeridianAngle_1__T]) -> _getPrimeMeridianAngle_1__T:
        """
        Get the prime meridian angle.
        
        The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            prime meridian vector
        
        Since:
            9.0
        
        
        """
        ...

class Loxodrome:
    """
    Perform calculations on a loxodrome (commonly, a rhumb line) on an ellipsoid.
    
    A Rhumb_line is an arc on an ellipsoid's surface that intersects every meridian at the same angle.
    
    Since:
        11.3
    """
    @typing.overload
    def __init__(self, geodeticPoint: GeodeticPoint, double: float, oneAxisEllipsoid: 'OneAxisEllipsoid'): ...
    @typing.overload
    def __init__(self, geodeticPoint: GeodeticPoint, double: float, oneAxisEllipsoid: 'OneAxisEllipsoid', double2: float): ...
    def getAltitude(self) -> float:
        """
        Get the altitude above the reference body.
        
        Returns:
            the altitude above the reference body
        
        
        """
        ...
    def getAzimuth(self) -> float:
        """
        Get the azimuth.
        
        Returns:
            the azimuth
        
        
        """
        ...
    def getBody(self) -> 'OneAxisEllipsoid':
        """
        Get the body on which the loxodrome is defined.
        
        Returns:
            the body on which the loxodrome is defined
        
        
        """
        ...
    def getPoint(self) -> GeodeticPoint:
        """
        Get the geodetic point defining the loxodrome.
        
        Returns:
            the geodetic point defining the loxodrome
        
        
        """
        ...
    def pointAtDistance(self, distance: float) -> GeodeticPoint:
        """
        Calculate the point at the specified distance from the origin point along the loxodrome. A positive distance follows the line in the azimuth direction (i.e. northward for arcs with azimuth angles [3π/2, 2π] or [0, π/2]). Negative distances travel in the opposite direction along the rhumb line. Distance is computed at the altitude of the origin point.
        
        Parameters:
            distance (double): the distance to travel (meters)
        
        Returns:
            the point at the specified distance from the origin
        
        
        """
        ...

class SexagesimalAngle:
    """
    Container for sexagesimal angle.
    
    Instance of this class are guaranteed to be immutable.
    
    Since:
        13.0
    
    Also see:
        GeodeticPoint
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int, double: float): ...
    def getAngle(self) -> float:
        """
        Get the corresponding angle in radians.
        
        Returns:
            angle in radians
        
        
        """
        ...
    def getArcMinute(self) -> int:
        """
        Get arc-minute part of the angle.
        
        Returns:
            arc-minute part of the angle
        
        
        """
        ...
    def getArcSecond(self) -> float:
        """
        Get arc-second part of the angle.
        
        Returns:
            arc-second part of the angle
        
        
        """
        ...
    def getDegree(self) -> int:
        """
        Get degree part of the angle.
        
        Returns:
            degree part of the angle
        
        
        """
        ...
    def getSign(self) -> int:
        """
        Get sign.
        
        Returns:
            sign
        
        
        """
        ...

_FieldTimeStampedGeodeticPoint__T = typing.TypeVar('_FieldTimeStampedGeodeticPoint__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTimeStampedGeodeticPoint(FieldGeodeticPoint[_FieldTimeStampedGeodeticPoint__T], org.orekit.time.FieldTimeStamped[_FieldTimeStampedGeodeticPoint__T], typing.Generic[_FieldTimeStampedGeodeticPoint__T]):
    """
    Implements a time-stamped FieldGeodeticPoint.
    
    Since:
        13.1
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTimeStampedGeodeticPoint__T], timeStampedGeodeticPoint: 'TimeStampedGeodeticPoint'): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeStampedGeodeticPoint__T], t: _FieldTimeStampedGeodeticPoint__T, t2: _FieldTimeStampedGeodeticPoint__T, t3: _FieldTimeStampedGeodeticPoint__T): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTimeStampedGeodeticPoint__T], fieldGeodeticPoint: FieldGeodeticPoint[_FieldTimeStampedGeodeticPoint__T]): ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: equals in class FieldGeodeticPoint
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTimeStampedGeodeticPoint__T]:
        """
        Description copied from interface: getDate Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class FieldGeodeticPoint
        
        
        """
        ...

class JPLEphemeridesLoader(org.orekit.data.AbstractSelfFeedingLoader, CelestialBodyLoader):
    """
    Loader for JPL ephemerides binary files (DE 4xx) and similar formats (INPOP 06/08/10).
    
    JPL ephemerides binary files contain ephemerides for all solar system planets.
    
    The JPL ephemerides binary files are recognized thanks to their base names, which must match the pattern [lu]nx[mp] (or [lu]nx[mp] for gzip-compressed files) where # stands for a digit character and where ddd is an ephemeris type (typically 405 or 406).
    
    The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files are named unx[mp], while little-endian files are named lnx[mp].
    
    The IMCCE ephemerides binary files are recognized thanks to their base names, which must match the pattern dat (or gz for gzip-compressed files) where * stands for any string.
    
    The loader supports files encoded in big-endian as well as in little-endian notation. Usually, big-endian files contain bigendian in their names, while little-endian files contain littleendian in their names.
    
    The loader supports files in TDB or TCB time scales.
    """
    DEFAULT_DE_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default supported files name pattern for JPL DE files.
    
    Also see:
        constant
    
    
    """
    DEFAULT_INPOP_SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Default supported files name pattern for IMCCE INPOP files.
    
    Also see:
        constant
    
    
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
    def getLoadedConstant(self, *names: str) -> float:
        """
        Get a constant defined in the ephemerides headers.
        
        Note that since constants are defined in the JPL headers files, they are available as soon as one file is available, even if it doesn't match the desired central date. This is because the header must be parsed before the dates can be checked.
        
        There are alternate names for constants since for example JPL names are different from INPOP names (Sun gravity: GMS or GM_Sun, Mars gravity: GM4 or GM_Mar...).
        
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
    def getLoadedGravitationalCoefficient(self, body: 'JPLEphemeridesLoader.EphemerisType') -> float:
        """
        Get the gravitational coefficient of a body.
        
        Parameters:
            body (EphemerisType): body for which the gravitational coefficient is requested
        
        Returns:
            gravitational coefficient in m³/s²
        
        
        """
        ...
    def getMaxChunksDuration(self) -> float:
        """
        Get the maximal chunks duration.
        
        Returns:
            chunks maximal duration in seconds
        
        
        """
        ...
    def loadCelestialBody(self, name: str) -> CelestialBody:
        """
        Load celestial body.
        
        Specified by: loadCelestialBody in interface CelestialBodyLoader
        
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
        def values() -> typing.MutableSequence['JPLEphemeridesLoader.EphemerisType']: ...
    class RawPVProvider:
        _getRawPV_0__T = typing.TypeVar('_getRawPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        @typing.overload
        def getRawPV(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getRawPV_0__T]) -> org.orekit.utils.FieldPVCoordinates[_getRawPV_0__T]: ...
        @typing.overload
        def getRawPV(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates: ...
        _getRawPosition_0__T = typing.TypeVar('_getRawPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        @typing.overload
        def getRawPosition(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getRawPosition_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getRawPosition_0__T]: ...
        @typing.overload
        def getRawPosition(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class LazyLoadedCelestialBodies(CelestialBodies):
    """
    This class lazily loads auxiliary data when it is needed by a requested body. It is designed to match the behavior of CelestialBodyFactory in Orekit 10.0.
    
    Since:
        10.1
    
    Also see:
        CelestialBodyFactory
    """
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScales: org.orekit.time.TimeScales, gcrf: org.orekit.frames.Frame):
        """
        Create a celestial body factory with the given auxiliary data sources.
        
        Parameters:
            dataProvidersManager (DataProvidersManager): supplies JPL ephemerides auxiliary data files.
            timeScales (TimeScales): set of time scales to use when loading bodies.
            gcrf (Frame): Earth centered frame aligned with ICRF.
        
        
        """
        ...
    def addCelestialBodyLoader(self, name: str, loader: typing.Union[CelestialBodyLoader, typing.Callable]) -> None:
        """
        Add a loader for celestial bodies.
        
        Parameters:
            name (String): name of the body (may be one of the predefined names or a user-defined name)
            loader (CelestialBodyLoader): custom loader to add for the body
        
        Also see:
            addDefaultCelestialBodyLoader,
            clearCelestialBodyLoaders,
            clearCelestialBodyLoaders
        
        
        """
        ...
    @typing.overload
    def addDefaultCelestialBodyLoader(self, string: str) -> None:
        """
        Parameters:
            supportedNames (String): regular expression for supported files names (may be null if the default JPL file names are used)
        
                The default loaders look for DE405 or DE406 JPL ephemerides.
        
        Also see:
            de405,
            de406,
            addCelestialBodyLoader,
            addDefaultCelestialBodyLoader,
            clearCelestialBodyLoaders,
            clearCelestialBodyLoaders
        
        Add the default loaders for celestial bodies.
        
        Parameters:
            name (String): name of the body (if not one of the predefined names, the method does nothing)
            supportedNames (String): regular expression for supported files names (may be null if the default JPL file names are used)
        
                The default loaders look for DE405 or DE406 JPL ephemerides.
        
        Also see:
            de405,
            de406,
            addCelestialBodyLoader,
            addDefaultCelestialBodyLoader,
            clearCelestialBodyLoaders,
            clearCelestialBodyLoaders
        
        
        """
        ...
    @typing.overload
    def addDefaultCelestialBodyLoader(self, string: str, string2: str) -> None: ...
    @typing.overload
    def clearCelestialBodyCache(self) -> None:
        """
        Clear all loaded celestial bodies.
        
        Calling this method will remove all loaded bodies from the internal cache. Subsequent calls to getBody or similar methods will result in a reload of the requested body from the configured loader(s).
        """
        ...
    @typing.overload
    def clearCelestialBodyCache(self, name: str) -> None:
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
            addCelestialBodyLoader,
            clearCelestialBodyLoaders,
            clearCelestialBodyCache
        
        
        """
        ...
    @typing.overload
    def clearCelestialBodyLoaders(self, name: str) -> None:
        """
        Clear loaders for one celestial body.
        
        Calling this method also clears the celestial body that has been loaded via this CelestialBodyLoader.
        
        Parameters:
            name (String): name of the body
        
        Also see:
            addCelestialBodyLoader,
            clearCelestialBodyLoaders,
            clearCelestialBodyCache
        
        """
        ...
    def getBody(self, name: str) -> CelestialBody:
        """
        Get a celestial body. The names of the common bodies are defined as constants in CelestialBodyFactory.
        
        If no CelestialBodyLoader has been added by calling addCelestialBodyLoader or if clearCelestialBodyLoaders has been called afterwards, the addDefaultCelestialBodyLoader method will be called automatically, once with the default name for JPL DE ephemerides and once with the default name for IMCCE INPOP files.
        
        Specified by: getBody in interface CelestialBodies
        
        Parameters:
            name (String): name of the celestial body
        
        Returns:
            celestial body
        
        
        """
        ...
    def getEarth(self) -> CelestialBody:
        """
        Description copied from interface: getEarth Get the Earth singleton body.
        
        Specified by: getEarth in interface CelestialBodies
        
        Returns:
            Earth body
        
        
        """
        ...
    def getEarthMoonBarycenter(self) -> CelestialBody:
        """
        Description copied from interface: getEarthMoonBarycenter Get the Earth-Moon barycenter singleton bodies pair.
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this bodies pair are aligned with getICRF (and therefore also getGCRF)
        
        Specified by: getEarthMoonBarycenter in interface CelestialBodies
        
        Returns:
            Earth-Moon barycenter bodies pair
        
        
        """
        ...
    def getJupiter(self) -> CelestialBody:
        """
        Description copied from interface: getJupiter Get the Jupiter singleton body.
        
        Specified by: getJupiter in interface CelestialBodies
        
        Returns:
            Jupiter body
        
        
        """
        ...
    def getMars(self) -> CelestialBody:
        """
        Description copied from interface: getMars Get the Mars singleton body.
        
        Specified by: getMars in interface CelestialBodies
        
        Returns:
            Mars body
        
        
        """
        ...
    def getMercury(self) -> CelestialBody:
        """
        Description copied from interface: getMercury Get the Mercury singleton body.
        
        Specified by: getMercury in interface CelestialBodies
        
        Returns:
            Sun body
        
        
        """
        ...
    def getMoon(self) -> CelestialBody:
        """
        Description copied from interface: getMoon Get the Moon singleton body.
        
        Specified by: getMoon in interface CelestialBodies
        
        Returns:
            Moon body
        
        
        """
        ...
    def getNeptune(self) -> CelestialBody:
        """
        Description copied from interface: getNeptune Get the Neptune singleton body.
        
        Specified by: getNeptune in interface CelestialBodies
        
        Returns:
            Neptune body
        
        
        """
        ...
    def getPluto(self) -> CelestialBody:
        """
        Description copied from interface: getPluto Get the Pluto singleton body.
        
        Specified by: getPluto in interface CelestialBodies
        
        Returns:
            Pluto body
        
        
        """
        ...
    def getSaturn(self) -> CelestialBody:
        """
        Description copied from interface: getSaturn Get the Saturn singleton body.
        
        Specified by: getSaturn in interface CelestialBodies
        
        Returns:
            Saturn body
        
        
        """
        ...
    def getSolarSystemBarycenter(self) -> CelestialBody:
        """
        Description copied from interface: getSolarSystemBarycenter Get the solar system barycenter aggregated body.
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this aggregated body are aligned with getICRF (and therefore also getGCRF)
        
        Specified by: getSolarSystemBarycenter in interface CelestialBodies
        
        Returns:
            solar system barycenter aggregated body
        
        
        """
        ...
    def getSun(self) -> CelestialBody:
        """
        Description copied from interface: getSun Get the Sun singleton body.
        
        Specified by: getSun in interface CelestialBodies
        
        Returns:
            Sun body
        
        
        """
        ...
    def getUranus(self) -> CelestialBody:
        """
        Description copied from interface: getUranus Get the Uranus singleton body.
        
        Specified by: getUranus in interface CelestialBodies
        
        Returns:
            Uranus body
        
        
        """
        ...
    def getVenus(self) -> CelestialBody:
        """
        Description copied from interface: getVenus Get the Venus singleton body.
        
        Specified by: getVenus in interface CelestialBodies
        
        Returns:
            Venus body
        
        
        """
        ...

class LoxodromeArc(Loxodrome):
    """
    Loxodrome defined by a start and ending point.
    
    Since:
        11.3
    """
    @typing.overload
    def __init__(self, geodeticPoint: GeodeticPoint, geodeticPoint2: GeodeticPoint, oneAxisEllipsoid: 'OneAxisEllipsoid'): ...
    @typing.overload
    def __init__(self, geodeticPoint: GeodeticPoint, geodeticPoint2: GeodeticPoint, oneAxisEllipsoid: 'OneAxisEllipsoid', double: float): ...
    def calculatePointAlongArc(self, fraction: float) -> GeodeticPoint:
        """
        Calculate a point at a specific percentage along the arc.
        
        Parameters:
            fraction (double): the fraction along the arc to compute the point
        
        Returns:
            the point along the arc
        
        
        """
        ...
    def getDistance(self) -> float:
        """
        Compute the distance of the arc along the surface of the ellipsoid.
        
        Returns:
            the distance (meters)
        
        
        """
        ...
    def getFinalPoint(self) -> GeodeticPoint:
        """
        Get the final point of the arc.
        
        Returns:
            the ending point of the arc
        
        
        """
        ...

class OneAxisEllipsoid(Ellipsoid, BodyShape):
    """
    Modeling of a one-axis ellipsoid.
    
    One-axis ellipsoids is a good approximate model for most planet-size and larger natural bodies. It is the equilibrium shape reached by a fluid body under its own gravity field when it rotates. The symmetry axis is the rotation or polar axis.
    """
    def __init__(self, ae: float, f: float, bodyFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Standard values for Earth models can be found in the Constants class:
        
        Parameters:
            ae (double): equatorial radius
            f (double): the flattening (f = (a-b)/a)
            bodyFrame (Frame): body frame related to body shape
        
        Also see:
            getITRF
        
        
        """
        ...
    _azimuthBetweenPoints_1__T = typing.TypeVar('_azimuthBetweenPoints_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def azimuthBetweenPoints(self, origin: GeodeticPoint, destination: GeodeticPoint) -> float:
        """
        Compute the azimuth angle from local north between the two points. The angle is calculated clockwise from local north at the origin point and follows the rhumb line to the destination point.
        
        Parameters:
            origin (GeodeticPoint): the origin point, at which the azimuth angle will be computed (non-null)
            destination (GeodeticPoint): the destination point, to which the angle is defined (non-null)
        
        Returns:
            the resulting azimuth angle (radians, [0-2pi))
        
        Since:
            11.3
        
        """
        ...
    @typing.overload
    def azimuthBetweenPoints(self, origin: FieldGeodeticPoint[_azimuthBetweenPoints_1__T], destination: FieldGeodeticPoint[_azimuthBetweenPoints_1__T]) -> _azimuthBetweenPoints_1__T:
        """
        Compute the azimuth angle from local north between the two points. The angle is calculated clockwise from local north at the origin point and follows the rhumb line to the destination point.
        
        Parameters:
            origin (FieldGeodeticPoint<T> origin): the origin point, at which the azimuth angle will be computed (non-null)
            destination (FieldGeodeticPoint<T> destination): the destination point, to which the angle is defined (non-null)
        
        Returns:
            the resulting azimuth angle (radians, [0-2pi))
        
        Since:
            11.3
        
        
        """
        ...
    _geodeticToIsometricLatitude_1__T = typing.TypeVar('_geodeticToIsometricLatitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def geodeticToIsometricLatitude(self, geodeticLatitude: float) -> float:
        """
        Compute the IsometricLatitude corresponding to the provided latitude.
        
        Parameters:
            geodeticLatitude (double): the latitude (radians, within interval [-pi/2, +pi/2])
        
        Returns:
            the isometric latitude (radians)
        
        Since:
            11.3
        
        """
        ...
    @typing.overload
    def geodeticToIsometricLatitude(self, geodeticLatitude: _geodeticToIsometricLatitude_1__T) -> _geodeticToIsometricLatitude_1__T:
        """
        Compute the IsometricLatitude corresponding to the provided latitude.
        
        Parameters:
            geodeticLatitude (T): the latitude (radians, within interval [-pi/2, +pi/2])
        
        Returns:
            the isometric latitude (radians)
        
        Since:
            11.3
        
        
        """
        ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
        Get body frame related to body shape.
        
        Be mindful that the OneAxisEllipsoid.getBodyFrame() and the OneAxisEllipsoid.getFrame() methods return the same object.
        
        Specified by: getBodyFrame in interface BodyShape
        
        Returns:
            body frame related to body shape
        
        
        """
        ...
    _getCartesianIntersectionPoint_0__T = typing.TypeVar('_getCartesianIntersectionPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getCartesianIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.FieldLine[_getCartesianIntersectionPoint_0__T], close: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getCartesianIntersectionPoint_0__T], frame: org.orekit.frames.Frame, date: org.orekit.time.FieldAbsoluteDate[_getCartesianIntersectionPoint_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getCartesianIntersectionPoint_0__T]:
        """
        Get the intersection point of a line with the surface of the body.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Parameters:
            line (FieldLine<T> line): test line (may intersect the body or not)
            close (FieldVector3D<T> close): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (FieldAbsoluteDate<T> date): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        Since:
            9.3
        
        
        """
        ...
    @typing.overload
    def getCartesianIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, close: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the intersection point of a line with the surface of the body.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Parameters:
            line (Line): test line (may intersect the body or not)
            close (Vector3D): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (AbsoluteDate): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        Since:
            9.3
        
        """
        ...
    def getEccentricity(self) -> float:
        """
        Get the first eccentricity of the ellipsoid: e = sqrt(f * (2.0 - f)).
        
        Returns:
            the eccentricity
        
        
        """
        ...
    def getEccentricitySquared(self) -> float:
        """
        Get the first eccentricity squared of the ellipsoid: e^2 = f * (2.0 - f).
        
        Returns:
            the eccentricity squared
        
        
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
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_0__T], close: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_0__T], frame: org.orekit.frames.Frame, date: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_0__T]) -> FieldGeodeticPoint[_getIntersectionPoint_0__T]:
        """
        Get the intersection point of a line with the surface of the body.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Specified by: getIntersectionPoint in interface BodyShape
        
        Parameters:
            line (FieldLine<T> line): test line (may intersect the body or not)
            close (FieldVector3D<T> close): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (FieldAbsoluteDate<T> date): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, close: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, date: org.orekit.time.AbsoluteDate) -> GeodeticPoint:
        """
        Get the intersection point of a line with the surface of the body.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Specified by: getIntersectionPoint in interface BodyShape
        
        Parameters:
            line (Line): test line (may intersect the body or not)
            close (Vector3D): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (AbsoluteDate): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    _lowestAltitudeIntermediate_0__T = typing.TypeVar('_lowestAltitudeIntermediate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def lowestAltitudeIntermediate(self, endpoint1: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_lowestAltitudeIntermediate_0__T], endpoint2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_lowestAltitudeIntermediate_0__T]) -> FieldGeodeticPoint[_lowestAltitudeIntermediate_0__T]:
        """
        Find intermediate point of lowest altitude along a line between two endpoints.
        
        Parameters:
            endpoint1 (FieldVector3D<T> endpoint1): first endpoint, in body frame
            endpoint2 (FieldVector3D<T> endpoint2): second endpoint, in body frame
        
        Returns:
            point with lowest altitude between endpoint1 and endpoint2.
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def lowestAltitudeIntermediate(self, endpoint1: org.hipparchus.geometry.euclidean.threed.Vector3D, endpoint2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> GeodeticPoint:
        """
        Find intermediate point of lowest altitude along a line between two endpoints.
        
        Parameters:
            endpoint1 (Vector3D): first endpoint, in body frame
            endpoint2 (Vector3D): second endpoint, in body frame
        
        Returns:
            point with lowest altitude between endpoint1 and endpoint2.
        
        Since:
            12.0
        
        """
        ...
    _pointAtAltitude_0__T = typing.TypeVar('_pointAtAltitude_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pointAtAltitude(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_pointAtAltitude_0__T], t: _pointAtAltitude_0__T, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_pointAtAltitude_0__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_pointAtAltitude_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_pointAtAltitude_0__T]: ...
    @typing.overload
    def pointAtAltitude(self, line: org.hipparchus.geometry.euclidean.threed.Line, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def projectToGround(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Project a point to the ground.
        
        Specified by: projectToGround in interface BodyShape
        
        Parameters:
            point (Vector3D): point to project
            date (AbsoluteDate): current date
            frame (Frame): frame in which moving point is expressed
        
        Returns:
            ground point exactly at the local vertical of specified point, in the same frame as specified point
        
        Also see:
            projectToGround
        
        """
        ...
    @typing.overload
    def projectToGround(self, pv: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Project a moving point to the ground.
        
        Specified by: projectToGround in interface BodyShape
        
        Parameters:
            pv (TimeStampedPVCoordinates): moving point
            frame (Frame): frame in which moving point is expressed
        
        Returns:
            ground point exactly at the local vertical of specified point, in the same frame as specified point
        
        Also see:
            projectToGround
        
        
        """
        ...
    def setAngularThreshold(self, angularThreshold: float) -> None:
        """
        Set the angular convergence threshold.
        
        The angular threshold is used both to identify points close to the ellipse axes and as the convergence threshold used to stop the iterations in the transform method.
        
        If this method is not called, the default value is set to 10 :sup:`-12` .
        
        Parameters:
            angularThreshold (double): angular convergence threshold (rad)
        
        
        """
        ...
    _transform_0__T = typing.TypeVar('_transform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, point: FieldGeodeticPoint[_transform_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_0__T]:
        """
        Transform a surface-relative point to a Cartesian point.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (FieldGeodeticPoint<T> point): surface-relative point
        
        Returns:
            point at the same location but as a Cartesian point
        
        """
        ...
    @typing.overload
    def transform(self, geodeticPoint: GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Transform a surface-relative point to a Cartesian point.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (GeodeticPoint): surface-relative point
        
        Returns:
            point at the same location but as a Cartesian point
        
        Transform a Cartesian point to a surface-relative point.
        
        This method is based on Toshio Fukushima's algorithm which uses Halley's method. 227215135_Transformation_from_Cartesian_to_Geodetic_Coordinates_Accelerated_by_Halley's_Method, Toshio Fukushima, Journal of Geodesy 9(12):689-693, February 2006
        
        Some changes have been added to the original method:
        
          - in order to handle more accurately corner cases near the pole
          - in order to handle properly corner cases near the equatorial plane, even far inside the ellipsoid
          - in order to handle very flat ellipsoids
        
        In some rare cases (for example very flat ellipsoid, or points close to ellipsoid center), the loop may fail to converge. As this seems to happen only in degenerate cases, a design choice was to return an approximate point corresponding to last iteration. This point may be incorrect and fail to give the initial point back if doing roundtrip by calling transform. This design choice was made to avoid NaNs appearing for example in inter-satellites visibility checks when two satellites are almost on opposite sides of Earth. The intermediate points far within the Earth should not prevent the detection algorithm to find visibility start/end.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (Vector3D): Cartesian point
            frame (Frame): frame in which Cartesian point is expressed
            date (AbsoluteDate): date of the computation (used for frames conversions)
        
        Returns:
            point at the same location but as a surface-relative point
        
        """
        ...
    @typing.overload
    def transform(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T], frame: org.orekit.frames.Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_transform_2__T]) -> FieldGeodeticPoint[_transform_2__T]:
        """
        Transform a Cartesian point to a surface-relative point.
        
        This method is based on Toshio Fukushima's algorithm which uses Halley's method. 227215135_Transformation_from_Cartesian_to_Geodetic_Coordinates_Accelerated_by_Halley's_Method, Toshio Fukushima, Journal of Geodesy 9(12):689-693, February 2006
        
        Some changes have been added to the original method:
        
          - in order to handle more accurately corner cases near the pole
          - in order to handle properly corner cases near the equatorial plane, even far inside the ellipsoid
          - in order to handle very flat ellipsoids
        
        In some rare cases (for example very flat ellipsoid, or points close to ellipsoid center), the loop may fail to converge. As this seems to happen only in degenerate cases, a design choice was to return an approximate point corresponding to last iteration. This point may be incorrect and fail to give the initial point back if doing roundtrip by calling transform. This design choice was made to avoid NaNs appearing for example in inter-satellites visibility checks when two satellites are almost on opposite sides of Earth. The intermediate points far within the Earth should not prevent the detection algorithm to find visibility start/end.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (FieldVector3D<T> point): Cartesian point
            frame (Frame): frame in which Cartesian point is expressed
            date (FieldAbsoluteDate<T> date): date of the computation (used for frames conversions)
        
        Returns:
            point at the same location but as a surface-relative point
        
        public FieldGeodeticPoint<UnivariateDerivative2> transform (PVCoordinates point, Frame frame, AbsoluteDate date)
        
        Transform a Cartesian point to a surface-relative point.
        
        Parameters:
            point (PVCoordinates): Cartesian point
            frame (Frame): frame in which Cartesian point is expressed
            date (AbsoluteDate): date of the computation (used for frames conversions)
        
        Returns:
            point at the same location but as a surface-relative point, using time as the single derivation parameter
        
        
        """
        ...
    @typing.overload
    def transform(self, pVCoordinates: org.orekit.utils.PVCoordinates, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> FieldGeodeticPoint[org.hipparchus.analysis.differentiation.UnivariateDerivative2]: ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> GeodeticPoint: ...

class PythonBodyShape(BodyShape):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
        Get body frame related to body shape. Extension point for Python.
        
        Specified by: getBodyFrame in interface BodyShape
        
        Returns:
            body frame related to body shape
        
        
        """
        ...
    _getIntersectionPoint_0__T = typing.TypeVar('_getIntersectionPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.FieldLine[_getIntersectionPoint_0__T], close: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getIntersectionPoint_0__T], frame: org.orekit.frames.Frame, date: org.orekit.time.FieldAbsoluteDate[_getIntersectionPoint_0__T]) -> FieldGeodeticPoint[_getIntersectionPoint_0__T]:
        """
        Get the intersection point of a line with the surface of the body.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Specified by: getIntersectionPoint in interface BodyShape
        
        Parameters:
            line (FieldLine<T> line): test line (may intersect the body or not)
            close (FieldVector3D<T> close): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (FieldAbsoluteDate<T> date): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        
        """
        ...
    @typing.overload
    def getIntersectionPoint(self, line: org.hipparchus.geometry.euclidean.threed.Line, close: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, date: org.orekit.time.AbsoluteDate) -> GeodeticPoint:
        """
        Get the intersection point of a line with the surface of the body. Extension point for Python.
        
        A line may have several intersection points with a closed surface (we consider the one point case as a degenerated two points case). The close parameter is used to select which of these points should be returned. The selected point is the one that is closest to the close point.
        
        Specified by: getIntersectionPoint in interface BodyShape
        
        Parameters:
            line (Line): test line (may intersect the body or not)
            close (Vector3D): point used for intersections selection
            frame (Frame): frame in which line is expressed
            date (AbsoluteDate): date of the line in given frame
        
        Returns:
            intersection point at altitude zero or null if the line does not intersect the surface
        
        """
        ...
    @typing.overload
    def projectToGround(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Project a point to the ground.
        
        Specified by: projectToGround in interface BodyShape
        
        Parameters:
            point (Vector3D): point to project
            date (AbsoluteDate): current date
            frame (Frame): frame in which moving point is expressed
        
        Returns:
            ground point exactly at the local vertical of specified point, in the same frame as specified point
        
        Also see:
            projectToGround
        
        """
        ...
    @typing.overload
    def projectToGround(self, pv: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Project a moving point to the ground.
        
        Specified by: projectToGround in interface BodyShape
        
        Parameters:
            pv (TimeStampedPVCoordinates): moving point
            frame (Frame): frame in which moving point is expressed
        
        Returns:
            ground point exactly at the local vertical of specified point, in the same frame as specified point
        
        Also see:
            projectToGround
        
        
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
    _transform_0__T = typing.TypeVar('_transform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transform_2__T = typing.TypeVar('_transform_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transform(self, point: FieldGeodeticPoint[_transform_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_0__T]:
        """
        Transform a surface-relative point to a Cartesian point.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (FieldGeodeticPoint<T> point): surface-relative point
        
        Returns:
            point at the same location but as a Cartesian point
        
        
        """
        ...
    @typing.overload
    def transform(self, geodeticPoint: GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Transform a Cartesian point to a surface-relative point.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (Vector3D): Cartesian point
            frame (Frame): frame in which Cartesian point is expressed
            date (AbsoluteDate): date of the computation (used for frames conversions)
        
        Returns:
            point at the same location but as a surface-relative point
        
        Transform a surface-relative point to a Cartesian point.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (GeodeticPoint): surface-relative point
        
        Returns:
            point at the same location but as a Cartesian point
        
        """
        ...
    @typing.overload
    def transform(self, point: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transform_2__T], frame: org.orekit.frames.Frame, date: org.orekit.time.FieldAbsoluteDate[_transform_2__T]) -> FieldGeodeticPoint[_transform_2__T]:
        """
        Transform a Cartesian point to a surface-relative point.
        
        Specified by: transform in interface BodyShape
        
        Parameters:
            point (FieldVector3D<T> point): Cartesian point
            frame (Frame): frame in which Cartesian point is expressed
            date (FieldAbsoluteDate<T> date): date of the computation (used for frames conversions)
        
        Returns:
            point at the same location but as a surface-relative point
        
        """
        ...
    @typing.overload
    def transform(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> GeodeticPoint: ...

class PythonCelestialBodies(CelestialBodies):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBody(self, name: str) -> CelestialBody:
        """
        Get a celestial body. The names of the common bodies are defined as constants in CelestialBodyFactory.
        
        Specified by: getBody in interface CelestialBodies
        
        Parameters:
            name (String): name of the celestial body
        
        Returns:
            celestial body
        
        
        """
        ...
    def getEarth(self) -> CelestialBody:
        """
        Get the Earth singleton body.
        
        Specified by: getEarth in interface CelestialBodies
        
        Returns:
            Earth body
        
        
        """
        ...
    def getEarthMoonBarycenter(self) -> CelestialBody:
        """
        Get the Earth-Moon barycenter singleton bodies pair.
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this bodies pair are aligned with getICRF (and therefore also getGCRF)
        
        Specified by: getEarthMoonBarycenter in interface CelestialBodies
        
        Returns:
            Earth-Moon barycenter bodies pair
        
        
        """
        ...
    def getJupiter(self) -> CelestialBody:
        """
        Get the Jupiter singleton body.
        
        Specified by: getJupiter in interface CelestialBodies
        
        Returns:
            Jupiter body
        
        
        """
        ...
    def getMars(self) -> CelestialBody:
        """
        Get the Mars singleton body.
        
        Specified by: getMars in interface CelestialBodies
        
        Returns:
            Mars body
        
        
        """
        ...
    def getMercury(self) -> CelestialBody:
        """
        Get the Mercury singleton body.
        
        Specified by: getMercury in interface CelestialBodies
        
        Returns:
            Sun body
        
        
        """
        ...
    def getMoon(self) -> CelestialBody:
        """
        Get the Moon singleton body.
        
        Specified by: getMoon in interface CelestialBodies
        
        Returns:
            Moon body
        
        
        """
        ...
    def getNeptune(self) -> CelestialBody:
        """
        Get the Neptune singleton body.
        
        Specified by: getNeptune in interface CelestialBodies
        
        Returns:
            Neptune body
        
        
        """
        ...
    def getPluto(self) -> CelestialBody:
        """
        Get the Pluto singleton body.
        
        Specified by: getPluto in interface CelestialBodies
        
        Returns:
            Pluto body
        
        
        """
        ...
    def getSaturn(self) -> CelestialBody:
        """
        Get the Saturn singleton body.
        
        Specified by: getSaturn in interface CelestialBodies
        
        Returns:
            Saturn body
        
        
        """
        ...
    def getSolarSystemBarycenter(self) -> CelestialBody:
        """
        Get the solar system barycenter aggregated body.
        
        Both the getInertiallyOrientedFrame and getBodyOrientedFrame for this aggregated body are aligned with getICRF (and therefore also getGCRF)
        
        Specified by: getSolarSystemBarycenter in interface CelestialBodies
        
        Returns:
            solar system barycenter aggregated body
        
        
        """
        ...
    def getSun(self) -> CelestialBody:
        """
        Get the Sun singleton body.
        
        Specified by: getSun in interface CelestialBodies
        
        Returns:
            Sun body
        
        
        """
        ...
    def getUranus(self) -> CelestialBody:
        """
        Get the Uranus singleton body.
        
        Specified by: getUranus in interface CelestialBodies
        
        Returns:
            Uranus body
        
        
        """
        ...
    def getVenus(self) -> CelestialBody:
        """
        Get the Venus singleton body.
        
        Specified by: getVenus in interface CelestialBodies
        
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
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getBodyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
        Get a body oriented, body centered frame.
        
        The frame is always bound to the body center, and its axes have a fixed orientation with respect to the celestial body.
        
        Specified by: getBodyOrientedFrame in interface CelestialBody
        
        Returns:
            a body oriented, body centered frame
        
        Also see:
            getInertiallyOrientedFrame
        
        
        """
        ...
    def getGM(self) -> float:
        """
        Get the attraction coefficient of the body.
        
        Specified by: getGM in interface CelestialBody
        
        Returns:
            attraction coefficient of the body (m³/s²)
        
        
        """
        ...
    def getInertiallyOrientedFrame(self) -> org.orekit.frames.Frame:
        """
        Get an inertially oriented, body centered frame.
        
        The frame is always bound to the body center, and its axes have a fixed orientation with respect to other inertial frames.
        
        Specified by: getInertiallyOrientedFrame in interface CelestialBody
        
        Returns:
            an inertially oriented, body centered frame
        
        Also see:
            getBodyOrientedFrame
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the body.
        
        Specified by: getName in interface CelestialBody
        
        Returns:
            name of the body
        
        
        """
        ...
    _getPVCoordinates_0__T = typing.TypeVar('_getPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getPVCoordinates_0__T]:
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
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
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
    _toFieldPVCoordinatesProvider__T = typing.TypeVar('_toFieldPVCoordinatesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def toFieldPVCoordinatesProvider(self, field: org.hipparchus.Field[_toFieldPVCoordinatesProvider__T]) -> org.orekit.utils.FieldPVCoordinatesProvider[_toFieldPVCoordinatesProvider__T]:
        """
        Convert to a FieldPVCoordinatesProvider with a specific type.
        
        Specified by: toFieldPVCoordinatesProvider in interface ExtendedPositionProvider
        
        Parameters:
            field (Field<T> field): field for the argument and value
        
        Returns:
            converted function
        
        
        """
        ...

class PythonCelestialBodyLoader(CelestialBodyLoader):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def loadCelestialBody(self, name: str) -> CelestialBody:
        """
        Load celestial body. Extension point for Python.
        
        Specified by: loadCelestialBody in interface CelestialBodyLoader
        
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
    Also see:
        serialized
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
    _getNode_0__T = typing.TypeVar('_getNode_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNode(self, date: org.orekit.time.FieldAbsoluteDate[_getNode_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNode_0__T]:
        """
        Get the body Q Node direction in ICRF frame.
        
        Specified by: getNode in interface IAUPole
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            body Q Node direction in ICRF frame
        
        
        """
        ...
    @typing.overload
    def getNode(self, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the body Q Node direction in ICRF frame.
        
        Specified by: getNode in interface IAUPole
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            body Q Node direction in ICRF frame
        
        """
        ...
    _getPole_0__T = typing.TypeVar('_getPole_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPole(self, date: org.orekit.time.FieldAbsoluteDate[_getPole_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPole_0__T]:
        """
        Get the body North pole direction in ICRF frame.
        
        Specified by: getPole in interface IAUPole
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            body North pole direction in ICRF frame
        
        
        """
        ...
    @typing.overload
    def getPole(self, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the body North pole direction in ICRF frame.
        
        Specified by: getPole in interface IAUPole
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            body North pole direction in ICRF frame
        
        """
        ...
    _getPrimeMeridianAngle_1__T = typing.TypeVar('_getPrimeMeridianAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPrimeMeridianAngle(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the prime meridian angle.
        
        The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
        Specified by: getPrimeMeridianAngle in interface IAUPole
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            prime meridian vector
        
        """
        ...
    @typing.overload
    def getPrimeMeridianAngle(self, date: org.orekit.time.FieldAbsoluteDate[_getPrimeMeridianAngle_1__T]) -> _getPrimeMeridianAngle_1__T:
        """
        Get the prime meridian angle.
        
        The prime meridian angle is the angle between the Q node and the prime meridian. represents the body rotation.
        
        Specified by: getPrimeMeridianAngle in interface IAUPole
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            prime meridian vector
        
        
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

class TimeStampedGeodeticPoint(GeodeticPoint, org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['TimeStampedGeodeticPoint']):
    """
    Implements a time-stamped GeodeticPoint.
    
    Since:
        13.1
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, geodeticPoint: GeodeticPoint): ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: equals in class GeodeticPoint
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getDate Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class GeodeticPoint
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, dt: org.orekit.time.TimeOffset) -> org.orekit.time.TimeShiftable:
        """
        Description copied from interface: shiftedBy Get a time-shifted instance.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'TimeStampedGeodeticPoint': ...
    def toString(self) -> str:
        """
        Overrides: toString in class GeodeticPoint
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.bodies")``.

    AnalyticalSolarPositionProvider: typing.Type[AnalyticalSolarPositionProvider]
    BodyShape: typing.Type[BodyShape]
    CR3BPFactory: typing.Type[CR3BPFactory]
    CR3BPSystem: typing.Type[CR3BPSystem]
    CelestialBodies: typing.Type[CelestialBodies]
    CelestialBody: typing.Type[CelestialBody]
    CelestialBodyFactory: typing.Type[CelestialBodyFactory]
    CelestialBodyLoader: typing.Type[CelestialBodyLoader]
    Ellipse: typing.Type[Ellipse]
    Ellipsoid: typing.Type[Ellipsoid]
    FieldEllipse: typing.Type[FieldEllipse]
    FieldGeodeticPoint: typing.Type[FieldGeodeticPoint]
    FieldTimeStampedGeodeticPoint: typing.Type[FieldTimeStampedGeodeticPoint]
    GeodeticPoint: typing.Type[GeodeticPoint]
    IAUPole: typing.Type[IAUPole]
    JPLEphemeridesLoader: typing.Type[JPLEphemeridesLoader]
    LazyLoadedCelestialBodies: typing.Type[LazyLoadedCelestialBodies]
    Loxodrome: typing.Type[Loxodrome]
    LoxodromeArc: typing.Type[LoxodromeArc]
    OneAxisEllipsoid: typing.Type[OneAxisEllipsoid]
    PythonBodyShape: typing.Type[PythonBodyShape]
    PythonCelestialBodies: typing.Type[PythonCelestialBodies]
    PythonCelestialBody: typing.Type[PythonCelestialBody]
    PythonCelestialBodyLoader: typing.Type[PythonCelestialBodyLoader]
    PythonIAUPole: typing.Type[PythonIAUPole]
    SexagesimalAngle: typing.Type[SexagesimalAngle]
    TimeStampedGeodeticPoint: typing.Type[TimeStampedGeodeticPoint]
