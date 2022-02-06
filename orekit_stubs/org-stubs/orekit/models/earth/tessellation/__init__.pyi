import java.io
import java.util
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.spherical.twod
import org.orekit.bodies
import org.orekit.orbits
import typing



class EllipsoidTessellator:
    """
    public class EllipsoidTessellator extends Object
    
        Class used to tessellate an interest zone on an ellipsoid in either :class:`~org.orekit.models.earth.tessellation.Tile`
        or grids of :class:`~org.orekit.bodies.GeodeticPoint`.
    
        This class is typically used for Earth Observation missions, in order to create tiles or grids that may be used as the
        basis of visibility event detectors. Tiles are used when surface-related elements are needed, the tiles created
        completely cover the zone of interest. Grids are used when point-related elements are needed, the points created lie
        entirely within the zone of interest.
    
        One should note that as tessellation essentially creates a 2 dimensional almost Cartesian map, it can never perfectly
        fulfill geometrical dimensions because neither sphere nor ellipsoid are developable surfaces. This implies that the
        tesselation will always be distorted, and distortion increases as the size of the zone to be tessellated increases.
    
        Since:
            7.1
    """
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, tileAiming: 'TileAiming', int: int): ...
    @typing.overload
    @staticmethod
    def buildSimpleZone(double: float, doubleArray: typing.List[typing.List[float]]) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet:
        """
            Build a simple zone (connected zone without holes).
        
            In order to build more complex zones (not connected or with holes), the user should directly call Hipparchus null
            constructors and null if set operations are needed (union, intersection, difference ...).
        
            Take care that the vertices boundary points must be given *counterclockwise*. Using the wrong order defines the
            complementary of the real zone, and will often result in tessellation failure as the zone is too wide.
        
            Parameters:
                tolerance (double): angular separation below which points are considered equal (typically 1.0e-10)
                points (:class:`~org.orekit.bodies.GeodeticPoint`...): vertices of the boundary, in *counterclockwise* order
        
            Returns:
                a zone defined on the unit 2-sphere
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def buildSimpleZone(double: float, geodeticPointArray: typing.List[org.orekit.bodies.GeodeticPoint]) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet: ...
    def sample(self, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, double: float, double2: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]: ...
    def tessellate(self, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, double: float, double2: float, double3: float, double4: float, boolean: bool, boolean2: bool) -> java.util.List[java.util.List['Tile']]: ...

class Tile(java.io.Serializable):
    """
    public class Tile extends Object implements Serializable
    
        Simple data structure for a quadrilateral tile shape on a body surface.
    
        This class is devoted to simple usage only. It assumes the edges are strictly between 0 and Ã�â‚¬ radians and that the
        angles between edges are also strictly between 0 and Ã�â‚¬ radians.
    
        Also see:
            :class:`~org.orekit.models.earth.tessellation.AlongTrackAiming`,
            :class:`~org.orekit.models.earth.tessellation.ConstantAzimuthAiming`, :meth:`~serialized`
    """
    def __init__(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, geodeticPoint2: org.orekit.bodies.GeodeticPoint, geodeticPoint3: org.orekit.bodies.GeodeticPoint, geodeticPoint4: org.orekit.bodies.GeodeticPoint): ...
    def getCenter(self) -> org.orekit.bodies.GeodeticPoint:
        """
            Get the center point.
        
            The center points corresponds to :meth:`~org.orekit.models.earth.tessellation.Tile.getInterpolatedPoint`
        
            Returns:
                center point
        
        
        """
        ...
    def getInterpolatedPoint(self, double: float, double2: float) -> org.orekit.bodies.GeodeticPoint:
        """
            Get an interpolated point inside the tile.
        
            The interpolated point is based on bilinear interpolations along the body surface assumed to be *spherical*, and along
            the vertical axis.
        
            The interpolation parameters are chosen such that (u = 0, v = 0) maps to vertex v0, (u = 1, v = 0) maps to vertex v1, (u
            = 1, v = 1) maps to vertex v2 and (u = 0, v = 1) maps to vertex v3.
        
            Parameters:
                u (double): first interpolation parameter (should be between 0 and 1 to remain inside the tile)
                v (double): second interpolation parameter (should be between 0 and 1 to remain inside the tile)
        
            Returns:
                interpolated point
        
        
        """
        ...
    def getVertices(self) -> typing.List[org.orekit.bodies.GeodeticPoint]:
        """
            Get the four vertices.
        
            Returns:
                four vertices
        
        
        """
        ...

class TileAiming:
    """
    public interface TileAiming
    
        Interface defining the aiming direction of :class:`~org.orekit.models.earth.tessellation.Tile`.
    """
    def alongTileDirection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the along tile direction for tessellation at specified point.
        
            Parameters:
                point (Vector3D): point on the ellipsoid (Cartesian coordinates)
                gp (:class:`~org.orekit.bodies.GeodeticPoint`): point on the ellipsoid (geodetic coordinates)
        
            Returns:
                normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]: ...

class AlongTrackAiming(TileAiming):
    """
    public class AlongTrackAiming extends Object implements :class:`~org.orekit.models.earth.tessellation.TileAiming`
    
        Class used to orient tiles along an orbit track.
    
        Also see:
            :class:`~org.orekit.models.earth.tessellation.ConstantAzimuthAiming`,
            :class:`~org.orekit.models.earth.tessellation.DivertedSingularityAiming`
    """
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, orbit: org.orekit.orbits.Orbit, boolean: bool): ...
    def alongTileDirection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the along tile direction for tessellation at specified point.
        
            Specified by:
                :meth:`~org.orekit.models.earth.tessellation.TileAiming.alongTileDirection`Â in
                interfaceÂ :class:`~org.orekit.models.earth.tessellation.TileAiming`
        
            Parameters:
                point (Vector3D): point on the ellipsoid (Cartesian coordinates)
                gp (:class:`~org.orekit.bodies.GeodeticPoint`): point on the ellipsoid (geodetic coordinates)
        
            Returns:
                normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]: ...

class ConstantAzimuthAiming(TileAiming):
    """
    public class ConstantAzimuthAiming extends Object implements :class:`~org.orekit.models.earth.tessellation.TileAiming`
    
        Class used to orient tiles with respect to a geographic azimuth.
    
        Also see:
            :class:`~org.orekit.models.earth.tessellation.AlongTrackAiming`,
            :class:`~org.orekit.models.earth.tessellation.DivertedSingularityAiming`
    """
    def __init__(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    def alongTileDirection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the along tile direction for tessellation at specified point.
        
            Specified by:
                :meth:`~org.orekit.models.earth.tessellation.TileAiming.alongTileDirection`Â in
                interfaceÂ :class:`~org.orekit.models.earth.tessellation.TileAiming`
        
            Parameters:
                point (Vector3D): point on the ellipsoid (Cartesian coordinates)
                gp (:class:`~org.orekit.bodies.GeodeticPoint`): point on the ellipsoid (geodetic coordinates)
        
            Returns:
                normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]: ...

class DivertedSingularityAiming(TileAiming):
    """
    public class DivertedSingularityAiming extends Object implements :class:`~org.orekit.models.earth.tessellation.TileAiming`
    
        Class used to orient tiles such that there are no singularities within the zone of interest.
    
        This class is mainly useful for :meth:`~org.orekit.models.earth.tessellation.EllipsoidTessellator.sample` a zone on
        ground when the grid directions is not really important and when the zone contains the pole, which is a singular point
        for both :class:`~org.orekit.models.earth.tessellation.ConstantAzimuthAiming` and
        :class:`~org.orekit.models.earth.tessellation.AlongTrackAiming`.
    
        Also see:
            :class:`~org.orekit.models.earth.tessellation.AlongTrackAiming`,
            :class:`~org.orekit.models.earth.tessellation.ConstantAzimuthAiming`
    """
    def __init__(self, sphericalPolygonsSet: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet): ...
    def alongTileDirection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the along tile direction for tessellation at specified point.
        
            Specified by:
                :meth:`~org.orekit.models.earth.tessellation.TileAiming.alongTileDirection`Â in
                interfaceÂ :class:`~org.orekit.models.earth.tessellation.TileAiming`
        
            Parameters:
                point (Vector3D): point on the ellipsoid (Cartesian coordinates)
                gp (:class:`~org.orekit.bodies.GeodeticPoint`): point on the ellipsoid (geodetic coordinates)
        
            Returns:
                normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]: ...

class PythonTileAiming(TileAiming):
    """
    public class PythonTileAiming extends Object implements :class:`~org.orekit.models.earth.tessellation.TileAiming`
    """
    def __init__(self): ...
    def alongTileDirection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Find the along tile direction for tessellation at specified point.
        
            Specified by:
                :meth:`~org.orekit.models.earth.tessellation.TileAiming.alongTileDirection`Â in
                interfaceÂ :class:`~org.orekit.models.earth.tessellation.TileAiming`
        
            Parameters:
                point (Vector3D): point on the ellipsoid (Cartesian coordinates)
                gp (:class:`~org.orekit.bodies.GeodeticPoint`): point on the ellipsoid (geodetic coordinates)
        
            Returns:
                normalized along tile direction
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]: ...
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.tessellation")``.

    AlongTrackAiming: typing.Type[AlongTrackAiming]
    ConstantAzimuthAiming: typing.Type[ConstantAzimuthAiming]
    DivertedSingularityAiming: typing.Type[DivertedSingularityAiming]
    EllipsoidTessellator: typing.Type[EllipsoidTessellator]
    PythonTileAiming: typing.Type[PythonTileAiming]
    Tile: typing.Type[Tile]
    TileAiming: typing.Type[TileAiming]
