
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import jpype
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.spherical.twod
import org.orekit.bodies
import org.orekit.orbits
import typing



class EllipsoidTessellator:
    """
    Class used to tessellate an interest zone on an ellipsoid in either Tile or grids of GeodeticPoint.
    
    This class is typically used for Earth Observation missions, in order to create tiles or grids that may be used as the basis of visibility event detectors. Tiles are used when surface-related elements are needed, the tiles created completely cover the zone of interest. Grids are used when point-related elements are needed, the points created lie entirely within the zone of interest.
    
    One should note that as tessellation essentially creates a 2 dimensional almost Cartesian map, it can never perfectly fulfill geometrical dimensions because neither sphere nor ellipsoid are developable surfaces. This implies that the tesselation will always be distorted, and distortion increases as the size of the zone to be tessellated increases.
    
    Since:
        7.1
    """
    def __init__(self, ellipsoid: org.orekit.bodies.OneAxisEllipsoid, aiming: 'TileAiming', quantization: int):
        """
        Simple constructor.
        
        The quantization parameter is used internally to adjust points positioning. For example when quantization is set to 4, a complete tile that has 4 corner points separated by the tile lengths will really be computed on a grid containing 25 points (5 rows of 5 points, as each side will be split in 4 segments, hence will have 5 points). This quantization allows rough adjustment to balance margins around the zone of interest and improves geometric accuracy as the along and across directions are readjusted at each points.
        
        It is recommended to use at least 2 as the quantization parameter for tiling. The rationale is that using only 1 for quantization would imply all points used are tiles vertices, and hence would lead small zones to generate 4 tiles with a shared vertex inside the zone and the 4 tiles covering the four quadrants at North-West, North-East, South-East and South-West. A quantization value of at least 2 allows to shift the tiles so the center point is an inside point rather than a tile vertex, hence allowing a single tile to cover the small zone. A value even greater like 4 or 8 would allow even finer positioning to balance the tiles margins around the zone.
        
        Parameters:
            ellipsoid (OneAxisEllipsoid): underlying ellipsoid
            aiming (TileAiming): aiming used for orienting tiles
            quantization (int): number of segments tiles sides are split into for tiles fine positioning
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def buildSimpleZone(tolerance: float, *points: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet:
        """
        In order to build more complex zones (not connected or with holes), the user should directly call Hipparchus SphericalPolygonsSet constructors and RegionFactory if set operations are needed (union, intersection, difference ...).
        
        Take care that the vertices boundary points must be given counterclockwise. Using the wrong order defines the complementary of the real zone, and will often result in tessellation failure as the zone is too wide.
        
        Parameters:
            tolerance (double): angular separation below which points are considered equal (typically 1.0e-10)
            points (GeodeticPoint...): vertices of the boundary, in counterclockwise order
        
        Returns:
            a zone defined on the unit 2-sphere
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def buildSimpleZone(tolerance: float, *points: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet: ...
    def sample(self, zone: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, width: float, length: float) -> java.util.List[java.util.List[org.orekit.bodies.GeodeticPoint]]:
        """
        Sample a zone of interest into a grid sample of GeodeticPoint.
        
        The created points will be entirely within the zone of interest.
        
        Parameters:
            zone (SphericalPolygonsSet): zone of interest to sample
            width (double): grid sample cells width as a distance on surface (in meters)
            length (double): grid sample cells length as a distance on surface (in meters)
        
        Returns:
            a list of lists of points sampling the zone of interest, each sub-list corresponding to a part not connected to the
            other parts (for example for islands)
        
        
        """
        ...
    def tessellate(self, zone: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet, fullWidth: float, fullLength: float, widthOverlap: float, lengthOverlap: float, truncateLastWidth: bool, truncateLastLength: bool) -> java.util.List[java.util.List['Tile']]:
        """
        Tessellate a zone of interest into tiles.
        
        The created tiles will completely cover the zone of interest.
        
        The distance between a vertex at a tile corner and the vertex at the same corner in the next vertex are computed by subtracting the overlap width (resp. overlap length) from the full width (resp. full length). If for example the full width is specified to be 55 km and the overlap in width is specified to be +5 km, successive tiles would span as follows:
        
          - tile 1 covering from 0 km to 55 km
          - tile 2 covering from 50 km to 105 km
          - tile 3 covering from 100 km to 155 km
          - ...
        
        In order to achieve the same 50 km step but using a 5 km gap instead of an overlap, one would need to specify the full width to be 45 km and the overlap to be -5 km. With these settings, successive tiles would span as follows:
        
          - tile 1 covering from 0 km to 45 km
          - tile 2 covering from 50 km to 95 km
          - tile 3 covering from 100 km to 155 km
          - ...
        
        
        Parameters:
            zone (SphericalPolygonsSet): zone of interest to tessellate
            fullWidth (double): full tiles width as a distance on surface, including overlap (in meters)
            fullLength (double): full tiles length as a distance on surface, including overlap (in meters)
            widthOverlap (double): overlap between adjacent tiles (in meters), if negative the tiles will have a gap between each other instead of an
                overlap
            lengthOverlap (double): overlap between adjacent tiles (in meters), if negative the tiles will have a gap between each other instead of an
                overlap
            truncateLastWidth (boolean): if true, the first tiles strip will be started as close as possible to the zone of interest, and the last tiles strip
                will have its width reduced to also remain close to the zone of interest; if false all tiles strip will have the same
                fullWidth and they will be balanced around zone of interest
            truncateLastLength (boolean): if true, the first tile in each strip will be started as close as possible to the zone of interest, and the last tile in
                each strip will have its length reduced to also remain close to the zone of interest; if false all tiles in each strip
                will have the same fullLength and they will be balanced around zone of interest
        
        Returns:
            a list of lists of tiles covering the zone of interest, each sub-list corresponding to a part not connected to the other
            parts (for example for islands)
        
        
        """
        ...

class Tile(java.io.Serializable):
    """
    Simple data structure for a quadrilateral tile shape on a body surface.
    
    This class is devoted to simple usage only. It assumes the edges are strictly between 0 and π radians and that the angles between edges are also strictly between 0 and π radians.
    
    Also see:
        AlongTrackAiming,
        ConstantAzimuthAiming, serialized
    """
    def __init__(self, v0: org.orekit.bodies.GeodeticPoint, v1: org.orekit.bodies.GeodeticPoint, v2: org.orekit.bodies.GeodeticPoint, v3: org.orekit.bodies.GeodeticPoint):
        """
        Create a tile.
        
        It is caller responsibility o ensure the vertices define a simple non-degenerated tile (i.e. edges are strictly between 0 than π radians and angles between edges are also strictly between 0 and π radians). No checks are performed here.
        
        Parameters:
            v0 (GeodeticPoint): first vertex
            v1 (GeodeticPoint): second vertex
            v2 (GeodeticPoint): third vertex
            v3 (GeodeticPoint): fourth vertex
        
        
        """
        ...
    def getCenter(self) -> org.orekit.bodies.GeodeticPoint:
        """
        Get the center point.
        
        The center points corresponds to getInterpolatedPoint
        
        Returns:
            center point
        
        
        """
        ...
    def getInterpolatedPoint(self, u: float, v: float) -> org.orekit.bodies.GeodeticPoint:
        """
        Get an interpolated point inside the tile.
        
        The interpolated point is based on bilinear interpolations along the body surface assumed to be spherical, and along the vertical axis.
        
        The interpolation parameters are chosen such that (u = 0, v = 0) maps to vertex v0, (u = 1, v = 0) maps to vertex v1, (u = 1, v = 1) maps to vertex v2 and (u = 0, v = 1) maps to vertex v3.
        
        Parameters:
            u (double): first interpolation parameter (should be between 0 and 1 to remain inside the tile)
            v (double): second interpolation parameter (should be between 0 and 1 to remain inside the tile)
        
        Returns:
            interpolated point
        
        
        """
        ...
    def getVertices(self) -> typing.MutableSequence[org.orekit.bodies.GeodeticPoint]:
        """
        Get the four vertices.
        
        Returns:
            four vertices
        
        
        """
        ...

class TileAiming:
    """
    Interface defining the aiming direction of Tile.
    """
    def alongTileDirection(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, gp: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Find the along tile direction for tessellation at specified point.
        
        Parameters:
            point (Vector3D): point on the ellipsoid (Cartesian coordinates)
            gp (GeodeticPoint): point on the ellipsoid (geodetic coordinates)
        
        Returns:
            normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]:
        """
        Get points at which aiming direction cannot be computed.
        
        As per Brouwer's HairyBallTheorem, any vector field on the 2-sphere has at least one zero. This implies that any implementation of this interface has at least one point where the aiming direction cannot be computed. The most typical example is aiming always towards North pole, for which both poles are singular points.
        
        Returns:
            a non-empty (as per hairy ball theorem) list of points where aiming direction is either zero or cannot be computed
        
        Since:
            10.0
        
        
        """
        ...

class AlongTrackAiming(TileAiming):
    """
    Class used to orient tiles along an orbit track.
    
    Also see:
        ConstantAzimuthAiming,
        DivertedSingularityAiming
    """
    def __init__(self, ellipsoid: org.orekit.bodies.OneAxisEllipsoid, orbit: org.orekit.orbits.Orbit, isAscending: bool):
        """
        Simple constructor.
        
        Parameters:
            ellipsoid (OneAxisEllipsoid): ellipsoid body on which the zone is defined
            orbit (Orbit): orbit along which tiles should be aligned
            isAscending (boolean): indicator for zone tiling with respect to ascending or descending orbits
        
        
        """
        ...
    def alongTileDirection(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, gp: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Find the along tile direction for tessellation at specified point.
        
        Specified by: alongTileDirection in interface TileAiming
        
        Parameters:
            point (Vector3D): point on the ellipsoid (Cartesian coordinates)
            gp (GeodeticPoint): point on the ellipsoid (geodetic coordinates)
        
        Returns:
            normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]:
        """
        Get points at which aiming direction cannot be computed.
        
        As per Brouwer's HairyBallTheorem, any vector field on the 2-sphere has at least one zero. This implies that any implementation of this interface has at least one point where the aiming direction cannot be computed. The most typical example is aiming always towards North pole, for which both poles are singular points.
        
        Specified by: getSingularPoints in interface TileAiming
        
        Returns:
            a non-empty (as per hairy ball theorem) list of points where aiming direction is either zero or cannot be computed
        
        
        """
        ...

class ConstantAzimuthAiming(TileAiming):
    """
    Class used to orient tiles with respect to a geographic azimuth.
    
    Also see:
        AlongTrackAiming,
        DivertedSingularityAiming
    """
    def __init__(self, ellipsoid: org.orekit.bodies.OneAxisEllipsoid, azimuth: float):
        """
        Simple constructor.
        
        Parameters:
            ellipsoid (OneAxisEllipsoid): ellipsoid body on which the zone is defined
            azimuth (double): geographic azimuth of the tiles
        
        
        """
        ...
    def alongTileDirection(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, gp: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Find the along tile direction for tessellation at specified point.
        
        Specified by: alongTileDirection in interface TileAiming
        
        Parameters:
            point (Vector3D): point on the ellipsoid (Cartesian coordinates)
            gp (GeodeticPoint): point on the ellipsoid (geodetic coordinates)
        
        Returns:
            normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]:
        """
        Get points at which aiming direction cannot be computed.
        
        As per Brouwer's HairyBallTheorem, any vector field on the 2-sphere has at least one zero. This implies that any implementation of this interface has at least one point where the aiming direction cannot be computed. The most typical example is aiming always towards North pole, for which both poles are singular points.
        
        Specified by: getSingularPoints in interface TileAiming
        
        Returns:
            a non-empty (as per hairy ball theorem) list of points where aiming direction is either zero or cannot be computed
        
        
        """
        ...

class DivertedSingularityAiming(TileAiming):
    """
    Class used to orient tiles such that there are no singularities within the zone of interest.
    
    This class is mainly useful for sample a zone on ground when the grid directions is not really important and when the zone contains the pole, which is a singular point for both ConstantAzimuthAiming and AlongTrackAiming.
    
    Also see:
        AlongTrackAiming,
        ConstantAzimuthAiming
    """
    def __init__(self, forbiddenZone: org.hipparchus.geometry.spherical.twod.SphericalPolygonsSet):
        """
        Simple constructor.
        
        Parameters:
            forbiddenZone (SphericalPolygonsSet): zone out of which singularity should be diverted
        
        
        """
        ...
    def alongTileDirection(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, gp: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Find the along tile direction for tessellation at specified point.
        
        Specified by: alongTileDirection in interface TileAiming
        
        Parameters:
            point (Vector3D): point on the ellipsoid (Cartesian coordinates)
            gp (GeodeticPoint): point on the ellipsoid (geodetic coordinates)
        
        Returns:
            normalized along tile direction
        
        
        """
        ...
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]:
        """
        Get points at which aiming direction cannot be computed.
        
        As per Brouwer's HairyBallTheorem, any vector field on the 2-sphere has at least one zero. This implies that any implementation of this interface has at least one point where the aiming direction cannot be computed. The most typical example is aiming always towards North pole, for which both poles are singular points.
        
        Specified by: getSingularPoints in interface TileAiming
        
        Returns:
            a non-empty (as per hairy ball theorem) list of points where aiming direction is either zero or cannot be computed
        
        
        """
        ...

class PythonTileAiming(TileAiming):
    def __init__(self): ...
    def alongTileDirection(self, point: org.hipparchus.geometry.euclidean.threed.Vector3D, gp: org.orekit.bodies.GeodeticPoint) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Find the along tile direction for tessellation at specified point.
        
        Specified by: alongTileDirection in interface TileAiming
        
        Parameters:
            point (Vector3D): point on the ellipsoid (Cartesian coordinates)
            gp (GeodeticPoint): point on the ellipsoid (geodetic coordinates)
        
        Returns:
            normalized along tile direction
        
        
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
    def getSingularPoints(self) -> java.util.List[org.orekit.bodies.GeodeticPoint]:
        """
        Get points at which aiming direction cannot be computed.
        
        As per Brouwer's `hairy ball theorem <http://mathworld.wolfram.com/HairyBallTheorem.html>`, any vector field on the 2-sphere has at least one zero. This implies that any implementation of this interface has at least one point where the aiming direction cannot be computed. The most typical example is aiming always towards North pole, for which both poles are singular points.
        
        Specified by: getSingularPoints in interface TileAiming
        
        Returns:
            a non-empty (as per hairy ball theorem) list of points where aiming direction is either zero or cannot be computed
        
        Since:
            10.0
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.tessellation")``.

    AlongTrackAiming: typing.Type[AlongTrackAiming]
    ConstantAzimuthAiming: typing.Type[ConstantAzimuthAiming]
    DivertedSingularityAiming: typing.Type[DivertedSingularityAiming]
    EllipsoidTessellator: typing.Type[EllipsoidTessellator]
    PythonTileAiming: typing.Type[PythonTileAiming]
    Tile: typing.Type[Tile]
    TileAiming: typing.Type[TileAiming]
