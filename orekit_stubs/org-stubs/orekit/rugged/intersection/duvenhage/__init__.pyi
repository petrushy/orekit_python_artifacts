
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

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
    
        The algorithm is described in the 2009 paper:
        :class:`~org.orekit.rugged.intersection.duvenhage.https:.researchspace.csir.co.za.dspace.bitstream.10204.3041.1.Duvenhage_2009.pdf`.
    """
    def __init__(self, tileUpdater: typing.Union[org.orekit.rugged.raster.TileUpdater, typing.Callable], int: int, boolean: bool, boolean2: bool): ...
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
    """
    public class MinMaxTreeTile extends :class:`~org.orekit.rugged.raster.SimpleTile`
    
        Implementation of a :class:`~org.orekit.rugged.raster.Tile` with a min/max kd tree.
    
        A n level min/max kd-tree contains sub-tiles merging individual cells together from coarse-grained (at level 0) to
        fine-grained (at level n-1). Level n-1, which is the deepest one, is computed from the raw cells by merging adjacent
        cells pairs columns (i.e. cells at indices (i, 2j) and (i, 2j+1) are merged together by computing and storing the
        minimum and maximum in a sub-tile. Level n-1 therefore has the same number of rows but half the number of columns of the
        raw tile, and its sub-tiles are 1 cell high and 2 cells wide. Level n-2 is computed from level n-1 by merging sub-tiles
        rows. Level n-2 therefore has half the number of rows and half the number of columns of the raw tile, and its sub-tiles
        are 2 cells high and 2 cells wide. Level n-3 is again computed by merging columns, level n-4 merging rows and so on. As
        depth decreases, the number of sub-tiles decreases and their size increase. Level 0 is reached when there is only either
        one row or one column of large sub-tiles.
    
        During the merging process, if at some stage there is an odd number of rows or columns, then the last sub-tile at next
        level will not be computed by merging two rows/columns from the current level, but instead computed by simply copying
        the last single row/column. The process is therefore well defined for any raw tile initial dimensions. A direct
        consequence is that the dimension of the sub-tiles in the last row or column may be smaller than the dimension of
        regular sub-tiles.
    
        If we consider for example a tall 107 ⨉ 19 raw tile, the min/max kd-tree will have 9 levels:
    
        Also see:
            :class:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTileFactory`
    """
    def getCrossedBoundaryColumns(self, int: int, int2: int, int3: int) -> typing.MutableSequence[int]:
        """
            Get the index of sub-tiles start columns crossed.
        
            When going from one column to another column at some tree level, we cross sub-tiles boundaries. This method returns the
            index of these boundaries.
        
            Parameters:
                column1 (int): starting column
                column2 (int): ending column (excluded)
                level (int): tree level
        
            Returns:
                indices of columns crossed at sub-tiles boundaries, in crossing order, the endpoints *are* included (i.e. if
                :code:`column1` or :code:`column2` are boundary columns, they will be in returned array)
        
        
        """
        ...
    def getCrossedBoundaryRows(self, int: int, int2: int, int3: int) -> typing.MutableSequence[int]:
        """
            Get the index of sub-tiles start rows crossed.
        
            When going from one row to another row at some tree level, we cross sub-tiles boundaries. This method returns the index
            of these boundaries.
        
            Parameters:
                row1 (int): starting row
                row2 (int): ending row
                level (int): tree level
        
            Returns:
                indices of rows crossed at sub-tiles boundaries, in crossing order, the endpoints *are* included (i.e. if :code:`row1`
                or :code:`row2` are boundary rows, they will be in returned array)
        
        
        """
        ...
    def getLevels(self) -> int:
        """
            Get the number of kd-tree levels (not counting raw elevations).
        
            Returns:
                number of kd-tree levels
        
            Also see:
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMinElevation`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMaxElevation`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMergeLevel`
        
        
        """
        ...
    @typing.overload
    def getMaxElevation(self, int: int, int2: int, int3: int) -> float:
        """
            Get the maximum elevation at some level tree.
        
            Note that the max elevation is *not* computed only at cell center, but considering that it is interpolated considering
            also Eastwards and Northwards neighbors, and extends up to the center of these neighbors. As an example, lets consider
            four neighboring cells in some Digital Elevation Model:
            When we interpolate elevation at a point located slightly South-West to the center of the (i+1, j+1) cell, we use all
            four cells in the interpolation, and we will get a result very close to 12 if we start close to (i+1, j+1) cell center.
            As the max value for this interpolation is stored at (i, j) indices, this implies that :code:`getMaxElevation(i, j, l)`
            must return 12 if l is chosen such that the sub-tile at tree level l includes cell (i,j) but not cell (i+1, j+1). In
            other words, interpolation implies sub-tile boundaries are overshoot by one column to the East and one row to the North
            when computing max.
        
            Parameters:
                i (int): row index of the cell
                j (int): column index of the cell
                level (int): tree level
        
            Returns:
                maximum value that can be reached when interpolating elevation in the sub-tile
        
            Also see:
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getLevels`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMinElevation`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMergeLevel`
        
        
        """
        ...
    @typing.overload
    def getMaxElevation(self) -> float: ...
    def getMergeLevel(self, int: int, int2: int, int3: int, int4: int) -> int:
        """
            Get the deepest level at which two cells are merged in the same min/max sub-tile.
        
            Parameters:
                i1 (int): row index of first cell
                j1 (int): column index of first cell
                i2 (int): row index of second cell
                j2 (int): column index of second cell
        
            Returns:
                deepest level at which two cells are merged in the same min/max sub-tile, or -1 if they are never merged in the same
                sub-tile
        
            Also see:
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getLevels`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMinElevation`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMaxElevation`
        
        
        """
        ...
    @typing.overload
    def getMinElevation(self, int: int, int2: int, int3: int) -> float:
        """
            Get the minimum elevation at some level tree.
        
            Note that the min elevation is *not* computed only at cell center, but considering that it is interpolated considering
            also Eastwards and Northwards neighbors, and extends up to the center of these neighbors. As an example, lets consider
            four neighboring cells in some Digital Elevation Model:
            When we interpolate elevation at a point located slightly South-West to the center of the (i+1, j+1) cell, we use all
            four cells in the interpolation, and we will get a result very close to 10 if we start close to (i+1, j+1) cell center.
            As the min value for this interpolation is stored at (i, j) indices, this implies that :code:`getMinElevation(i, j, l)`
            must return 10 if l is chosen such that the sub-tile at tree level l includes cell (i,j) but not cell (i+1, j+1). In
            other words, interpolation implies sub-tile boundaries are overshoot by one column to the East and one row to the North
            when computing min.
        
            Parameters:
                i (int): row index of the cell
                j (int): column index of the cell
                level (int): tree level
        
            Returns:
                minimum value that can be reached when interpolating elevation in the sub-tile
        
            Also see:
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getLevels`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMaxElevation`,
                :meth:`~org.orekit.rugged.intersection.duvenhage.MinMaxTreeTile.getMergeLevel`
        
        
        """
        ...
    @typing.overload
    def getMinElevation(self) -> float: ...
    def isColumnMerging(self, int: int) -> bool:
        """
            Check if the merging operation between level and level-1 is a column merging.
        
            Parameters:
                level (int): level to check
        
            Returns:
                true if the merging operation between level and level-1 is a column merging, false if is a row merging
        
        
        """
        ...
    def locateMax(self, int: int, int2: int, int3: int) -> typing.MutableSequence[int]:
        """
            Locate the cell at which max elevation is reached for a specified level.
        
            Max is computed with respect to the continuous interpolated elevation, which takes four neighboring cells into account.
            This implies that the cell at which max value is reached for some level is either within the sub-tile for this level, or
            in some case it may be one column outside to the East or one row outside to the North. See
            :meth:`~org.orekit.rugged.raster.SimpleTile.getMaxElevation` for a more complete explanation.
        
            Parameters:
                i (int): row index of the cell
                j (int): column index of the cell
                level (int): tree level of the sub-tile considered
        
            Returns:
                row/column indices of the cell at which min elevation is reached
        
        
        """
        ...
    def locateMin(self, int: int, int2: int, int3: int) -> typing.MutableSequence[int]:
        """
            Locate the cell at which min elevation is reached for a specified level.
        
            Min is computed with respect to the continuous interpolated elevation, which takes four neighboring cells into account.
            This implies that the cell at which min value is reached for some level is either within the sub-tile for this level, or
            in some case it may be one column outside to the East or one row outside to the North. See
            :meth:`~org.orekit.rugged.raster.SimpleTile.getMinElevation` for a more complete explanation.
        
            Parameters:
                i (int): row index of the cell
                j (int): column index of the cell
                level (int): tree level of the sub-tile considered
        
            Returns:
                row/column indices of the cell at which min elevation is reached
        
        
        """
        ...

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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.intersection.duvenhage")``.

    DuvenhageAlgorithm: typing.Type[DuvenhageAlgorithm]
    MinMaxTreeTile: typing.Type[MinMaxTreeTile]
    MinMaxTreeTileFactory: typing.Type[MinMaxTreeTileFactory]
