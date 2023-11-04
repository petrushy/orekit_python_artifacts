import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.api
import org.orekit.rugged.intersection
import org.orekit.rugged.raster
import org.orekit.rugged.utils
import typing



class DuvenhageAlgorithm(org.orekit.rugged.intersection.IntersectionAlgorithm):
    """
    public class DuvenhageAlgorithm extends :class:`~org.orekit.rugged.intersection.duvenhage.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
    
        Digital Elevation Model intersection using Bernardt Duvenhage's algorithm.
    
        The algorithm is described in the 2009 paper: `Using An Implicit Min/Max KD-Tree for Doing Efficient Terrain Line of
        Sight Calculations <http://researchspace.csir.co.za/dspace/bitstream/10204/3041/1/Duvenhage_2009.pdf>`.
    """
    def __init__(self, tileUpdater: org.orekit.rugged.raster.TileUpdater, int: int, boolean: bool): ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
            Get the algorithmId.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getAlgorithmId` in
                interface :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Returns:
                the algorithmId
        
        
        """
        ...
    def getElevation(self, double: float, double2: float) -> float:
        """
            Get elevation at a given ground point.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getElevation` in
                interface :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Parameters:
                latitude (double): ground point latitude
                longitude (double): ground point longitude
        
            Returns:
                elevation at specified point
        
        
        """
        ...
    def intersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
            Compute intersection of line with Digital Elevation Model.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.intersection` in
                interface :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Parameters:
                ellipsoid (:class:`~org.orekit.rugged.utils.ExtendedEllipsoid`): reference ellipsoid
                position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
        
            Returns:
                point at which the line first enters ground
        
        
        """
        ...
    def refineIntersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
            Refine intersection of line with Digital Elevation Model.
        
            This method is used to refine an intersection when a close guess is already known. The intersection is typically looked
            for by a direct :meth:`~org.orekit.rugged.raster.Tile.cellIntersection` in the tile which already contains the close
            guess, or any similar very fast algorithm.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.refineIntersection` in
                interface :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Parameters:
                ellipsoid (:class:`~org.orekit.rugged.utils.ExtendedEllipsoid`): reference ellipsoid
                position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
                closeGuess (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): guess close to the real intersection
        
            Returns:
                point at which the line first enters ground
        
        
        """
        ...

class MinMaxTreeTile(org.orekit.rugged.raster.SimpleTile):
    def getCrossedBoundaryColumns(self, int: int, int2: int, int3: int) -> typing.List[int]: ...
    def getCrossedBoundaryRows(self, int: int, int2: int, int3: int) -> typing.List[int]: ...
    def getLevels(self) -> int: ...
    @typing.overload
    def getMaxElevation(self, int: int, int2: int, int3: int) -> float: ...
    @typing.overload
    def getMaxElevation(self) -> float: ...
    def getMergeLevel(self, int: int, int2: int, int3: int, int4: int) -> int: ...
    @typing.overload
    def getMinElevation(self, int: int, int2: int, int3: int) -> float: ...
    @typing.overload
    def getMinElevation(self) -> float: ...
    def isColumnMerging(self, int: int) -> bool: ...
    def locateMax(self, int: int, int2: int, int3: int) -> typing.List[int]: ...
    def locateMin(self, int: int, int2: int, int3: int) -> typing.List[int]: ...

class MinMaxTreeTileFactory(org.orekit.rugged.raster.TileFactory[MinMaxTreeTile]):
    """
    public class MinMaxTreeTileFactory extends :class:`~org.orekit.rugged.intersection.duvenhage.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.rugged.raster.TileFactory`<:class:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile`>
    
        Simple implementation of a :class:`~org.orekit.rugged.raster.TileFactory` for
        :class:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile`.
    """
    def __init__(self): ...
    def createTile(self) -> MinMaxTreeTile:
        """
            Create an empty tile.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.TileFactory.createTile` in interface :class:`~org.orekit.rugged.raster.TileFactory`
        
            Returns:
                e new empty tile
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.intersection.duvenhage")``.

    DuvenhageAlgorithm: typing.Type[DuvenhageAlgorithm]
    MinMaxTreeTile: typing.Type[MinMaxTreeTile]
    MinMaxTreeTileFactory: typing.Type[MinMaxTreeTileFactory]
