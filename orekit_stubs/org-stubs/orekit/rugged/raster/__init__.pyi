import java.lang
import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.utils
import typing



_TileFactory__T = typing.TypeVar('_TileFactory__T', bound='Tile')  # <T>
class TileFactory(typing.Generic[_TileFactory__T]):
    """
    public interface TileFactory<T extends :class:`~org.orekit.rugged.raster.Tile`>
    
        Interface representing a factory for raster tile.
    """
    def createTile(self) -> _TileFactory__T:
        """
            Create an empty tile.
        
            Returns:
                e new empty tile
        
        
        """
        ...

class TileUpdater:
    """
    public interface TileUpdater
    
        Interface used to update Digital Elevation Model tiles.
    
        Implementations of this interface must be provided by the image processing mission-specific layer, thus allowing the
        Rugged library to access the Digital Elevation Model data.
    """
    def updateTile(self, double: float, double2: float, updatableTile: 'UpdatableTile') -> None:
        """
            Update the tile according to the Digital Elevation Model.
        
            This method is the hook used by the Rugged library to delegate Digital Elevation Model loading to user-provided
            mission-specific code. When this method is called, the specified :class:`~org.orekit.rugged.raster.UpdatableTile` is
            empty and must be updated by calling :meth:`~org.orekit.rugged.raster.UpdatableTile.setGeometry` once at the start of
            the method to set up the tile geometry, and then calling :meth:`~org.orekit.rugged.raster.UpdatableTile.setElevation`
            once for each cell in the tile to set the cell elevation.
        
            The implementation must fulfill the requirements:
        
              - The tiles must overlap each other by one cell (i.e. cells that belong to the northernmost row of one tile must also
                belong to the sourthernmost row of another tile and cells that belong to the easternmost column of one tile must also
                belong to the westernmost column of another tile).
              - As elevations are interpolated within Digital Elevation Model cells using four cells at indices (kLat, kLon), (kLat+1,
                kLon), (kLat, kLon+1), (kLat+1, kLon+1). A point in the northernmost row (resp. easternmost column) miss neighboring
                points at row kLat+1 (resp. neighboring points at column kLon+1) and therefore cannot be interpolated. The method should
                therefore select the northernmost tile if the specified latitude is in the overlapping row between two tiles, and it
                should select the easternmost tile if the specified longitude is in the overlapping column between two tiles. Failing to
                do so will trigger an error at caller level mentioning the missing required neighbors.
              - The elevation at cells as set when calling :meth:`~org.orekit.rugged.raster.UpdatableTile.setElevation` must be the
                elevation corresponding to the latitude :code:`minLatitude + kLat * latitudeStep` and longitude :code:`minLongitude +
                kLon * longitudeStep`, where :code:`minLatitude`, :code:`latitudeStep`, :code:`minLongitude` and :code:`longitudeStep`
                correspond to the parameter of the :meth:`~org.orekit.rugged.raster.UpdatableTile.setGeometry` call.
        
        
            Parameters:
                latitude (double): latitude that must be covered by the tile (rad)
                longitude (double): longitude that must be covered by the tile (rad)
                tile (:class:`~org.orekit.rugged.raster.UpdatableTile`): to update
        
        
        """
        ...

_TilesCache__T = typing.TypeVar('_TilesCache__T', bound='Tile')  # <T>
class TilesCache(typing.Generic[_TilesCache__T]):
    """
    public class TilesCache<T extends :class:`~org.orekit.rugged.raster.Tile`> extends Object
    
        Cache for Digital Elevation Model :class:`~org.orekit.rugged.raster.Tile`.
    
        Beware, this cache is *not* thread-safe!
    """
    def __init__(self, tileFactory: TileFactory[_TilesCache__T], tileUpdater: TileUpdater, int: int): ...
    def getTile(self, double: float, double2: float) -> _TilesCache__T:
        """
            Get the tile covering a ground point.
        
            Parameters:
                latitude (double): ground point latitude
                longitude (double): ground point longitude
        
            Returns:
                tile covering the ground point
        
        
        """
        ...

class UpdatableTile:
    """
    public interface UpdatableTile
    
        Interface representing one tile of a raster Digital Elevation Model.
    """
    def setElevation(self, int: int, int2: int, double: float) -> None:
        """
            Set the elevation for one raster element.
        
            BEWARE! The order of the indices follows geodetic conventions, i.e. the latitude is given first and longitude
            afterwards, so the first index specifies a *row* index with zero at South and max value at North, and the second index
            specifies a *column* index with zero at West and max value at East. This is *not* the same as some raster conventions
            (as our row index increases from South to North) and this is also not the same as Cartesian coordinates as our ordinate
            index appears before our abscissa index).
        
            Parameters:
                latitudeIndex (int): index of latitude (row index)
                longitudeIndex (int): index of longitude (column index)
                elevation (double): elevation (m)
        
        
        """
        ...
    def setGeometry(self, double: float, double2: float, double3: float, double4: float, int: int, int2: int) -> None:
        """
            Set the tile global geometry.
        
            Parameters:
                minLatitude (double): minimum latitude (rad)
                minLongitude (double): minimum longitude (rad)
                latitudeStep (double): step in latitude (size of one raster element) (rad)
                longitudeStep (double): step in longitude (size of one raster element) (rad)
                latitudeRows (int): number of latitude rows
                longitudeColumns (int): number of longitude columns
        
        
        """
        ...

class SimpleTileFactory(TileFactory['SimpleTile']):
    """
    public class SimpleTileFactory extends Object implements :class:`~org.orekit.rugged.raster.TileFactory`<:class:`~org.orekit.rugged.raster.SimpleTile`>
    
        Simple implementation of a :class:`~org.orekit.rugged.raster.TileFactory` for
        :class:`~org.orekit.rugged.raster.SimpleTile`.
    """
    def __init__(self): ...
    def createTile(self) -> 'SimpleTile':
        """
            Create an empty tile.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.TileFactory.createTile` in interface :class:`~org.orekit.rugged.raster.TileFactory`
        
            Returns:
                e new empty tile
        
        
        """
        ...

class Tile(UpdatableTile):
    """
    public interface Tile extends :class:`~org.orekit.rugged.raster.UpdatableTile`
    
        Interface representing a raster tile.
    
        The elevations are considered to be at the *center* of each cells. The minimum latitude and longitude hence correspond
        to the *center* of the most South-West cell, and the maximum latitude and longitude correspond to the *center* of the
        most North-East cell.
    """
    def cellIntersection(self, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, int: int, int2: int) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
            Find the intersection of a line-of-sight and a Digital Elevation Model cell.
        
            Beware that for continuity reasons, the point argument in :code:`cellIntersection` is normalized with respect to other
            points used by the caller. This implies that the longitude may be outside of the [-Ã�â‚¬ ; +Ã�â‚¬] interval (or the [0 ;
            2Ã�â‚¬] interval, depending on the DEM). In particular, when a Line Of Sight crosses the antimeridian at Ã‚Â±Ã�â‚¬
            longitude, the library may call the :code:`cellIntersection` method with a point having a longitude of -Ã�â‚¬-ÃŽÂµ to
            ensure this continuity. As tiles are stored with longitude clipped to a some DEM specific interval (either [-Ã�â‚¬ ;
            +Ã�â‚¬] or [0 ; 2Ã�â‚¬]), implementations MUST take care to clip the input point back to the tile interval using
            :code:`MathUtils.normalizeAngle(p.getLongitude(), someLongitudeWithinTheTile)`. The output point normalization should
            also be made consistent with the current tile.
        
            Parameters:
                p (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): point on the line (beware its longitude is *not* normalized with respect to tile)
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight, in the topocentric frame (East, North, Zenith) of the point, scaled to match radians in the horizontal
                    plane and meters along the vertical axis
                latitudeIndex (int): latitude index of the Digital Elevation Model cell
                longitudeIndex (int): longitude index of the Digital Elevation Model cell
        
            Returns:
                point corresponding to line-of-sight crossing the Digital Elevation Model surface if it lies within the cell, null
                otherwise
        
        
        """
        ...
    def getElevationAtIndices(self, int: int, int2: int) -> float:
        """
            Get the elevation of an exact grid point.
        
            Parameters:
                latitudeIndex (int): grid point index along latitude
                longitudeIndex (int): grid point index along longitude
        
            Returns:
                elevation at grid point (m)
        
        
        """
        ...
    def getFloorLatitudeIndex(self, double: float) -> int:
        """
            Get the floor latitude index of a point.
        
            The specified latitude is always between index and index+1.
        
            Parameters:
                latitude (double): geodetic latitude
        
            Returns:
                floor latitude index (it may lie outside of the tile!)
        
        
        """
        ...
    def getFloorLongitudeIndex(self, double: float) -> int:
        """
            Get the floor longitude index of a point.
        
            The specified longitude is always between index and index+1.
        
            Parameters:
                longitude (double): geodetic longitude
        
            Returns:
                floor longitude index (it may lie outside of the tile!)
        
        
        """
        ...
    def getLatitudeAtIndex(self, int: int) -> float:
        """
            Get the latitude at some index.
        
            Parameters:
                latitudeIndex (int): latitude index
        
            Returns:
                latitude at the specified index (rad) (latitude of the center of the cells of specified row)
        
        
        """
        ...
    def getLatitudeRows(self) -> int:
        """
            Get number of latitude rows.
        
            Returns:
                number of latitude rows
        
        
        """
        ...
    def getLatitudeStep(self) -> float:
        """
            Get step in latitude (size of one raster element).
        
            Returns:
                step in latitude (rad)
        
        
        """
        ...
    def getLocation(self, double: float, double2: float) -> 'Tile.Location':
        """
            Check if a tile covers a ground point.
        
            Parameters:
                latitude (double): ground point latitude
                longitude (double): ground point longitude
        
            Returns:
                location of the ground point with respect to tile
        
        
        """
        ...
    def getLongitudeAtIndex(self, int: int) -> float:
        """
            Get the longitude at some index.
        
            Parameters:
                longitudeIndex (int): longitude index
        
            Returns:
                longitude at the specified index (rad) (longitude of the center of the cells of specified column)
        
        
        """
        ...
    def getLongitudeColumns(self) -> int:
        """
            Get number of longitude columns.
        
            Returns:
                number of longitude columns
        
        
        """
        ...
    def getLongitudeStep(self) -> float:
        """
            Get step in longitude (size of one raster element).
        
            Returns:
                step in longitude (rad)
        
        
        """
        ...
    def getMaxElevation(self) -> float:
        """
            Get the maximum elevation in the tile.
        
            Returns:
                maximum elevation in the tile (m)
        
        
        """
        ...
    def getMaxElevationLatitudeIndex(self) -> int:
        """
            Get the latitude index of max elevation.
        
            Returns:
                latitude index of max elevation
        
        
        """
        ...
    def getMaxElevationLongitudeIndex(self) -> int:
        """
            Get the longitude index of max elevation.
        
            Returns:
                longitude index of max elevation
        
        
        """
        ...
    def getMaximumLatitude(self) -> float:
        """
            Get maximum latitude.
        
            Beware that as a point at maximum latitude is the northernmost one of the grid, it doesn't have a northwards neighbor
            and therefore calling :meth:`~org.orekit.rugged.raster.Tile.getLocation` on such a latitude will return either
            :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH_WEST`, :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH` or
            :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH_EAST`, but can *never* return
            :meth:`~org.orekit.rugged.raster.Tile.Location.HAS_INTERPOLATION_NEIGHBORS`!
        
            Returns:
                maximum latitude (rad) (latitude of the center of the cells of North row)
        
        
        """
        ...
    def getMaximumLongitude(self) -> float:
        """
            Get maximum longitude.
        
            Beware that as a point at maximum longitude is the easternmost one of the grid, it doesn't have an eastwards neighbor
            and therefore calling :meth:`~org.orekit.rugged.raster.Tile.getLocation` on such a longitude will return either
            :meth:`~org.orekit.rugged.raster.Tile.Location.SOUTH_EAST`, :meth:`~org.orekit.rugged.raster.Tile.Location.EAST` or
            :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH_EAST`, but can *never* return
            :meth:`~org.orekit.rugged.raster.Tile.Location.HAS_INTERPOLATION_NEIGHBORS`!
        
            Returns:
                maximum longitude (rad) (longitude of the center of the cells of East column)
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
            Get the minimum elevation in the tile.
        
            Returns:
                minimum elevation in the tile (m)
        
        
        """
        ...
    def getMinElevationLatitudeIndex(self) -> int:
        """
            Get the latitude index of min elevation.
        
            Returns:
                latitude index of min elevation
        
        
        """
        ...
    def getMinElevationLongitudeIndex(self) -> int:
        """
            Get the longitude index of min elevation.
        
            Returns:
                longitude index of min elevation
        
        
        """
        ...
    def getMinimumLatitude(self) -> float:
        """
            Get minimum latitude of grid interpolation points.
        
            Returns:
                minimum latitude of grid interpolation points (rad) (latitude of the center of the cells of South row)
        
        
        """
        ...
    def getMinimumLongitude(self) -> float:
        """
            Get minimum longitude.
        
            Returns:
                minimum longitude (rad) (longitude of the center of the cells of West column)
        
        
        """
        ...
    def interpolateElevation(self, double: float, double2: float) -> float:
        """
            Interpolate elevation.
        
            In order to cope with numerical accuracy issues when computing points at tile boundary, a slight tolerance (typically
            1/8 cell) around the tile is allowed. Elevation can therefore be interpolated (really extrapolated in this case) even
            for points slightly overshooting tile boundaries, using the closest tile cell. Attempting to interpolate too far from
            the tile will trigger an exception.
        
            Parameters:
                latitude (double): ground point latitude
                longitude (double): ground point longitude
        
            Returns:
                interpolated elevation (m)
        
        
        """
        ...
    def tileUpdateCompleted(self) -> None:
        """
            Hook called at the end of tile update completion.
        
        """
        ...
    class Location(java.lang.Enum['Tile.Location']):
        SOUTH_WEST: typing.ClassVar['Tile.Location'] = ...
        WEST: typing.ClassVar['Tile.Location'] = ...
        NORTH_WEST: typing.ClassVar['Tile.Location'] = ...
        NORTH: typing.ClassVar['Tile.Location'] = ...
        NORTH_EAST: typing.ClassVar['Tile.Location'] = ...
        EAST: typing.ClassVar['Tile.Location'] = ...
        SOUTH_EAST: typing.ClassVar['Tile.Location'] = ...
        SOUTH: typing.ClassVar['Tile.Location'] = ...
        HAS_INTERPOLATION_NEIGHBORS: typing.ClassVar['Tile.Location'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Tile.Location': ...
        @staticmethod
        def values() -> typing.List['Tile.Location']: ...

class SimpleTile(Tile):
    """
    public class SimpleTile extends Object implements :class:`~org.orekit.rugged.raster.Tile`
    
        Simple implementation of a :class:`~org.orekit.rugged.raster.Tile`.
    
        Also see:
            :class:`~org.orekit.rugged.raster.SimpleTileFactory`
    """
    def cellIntersection(self, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, int: int, int2: int) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
            Find the intersection of a line-of-sight and a Digital Elevation Model cell.
        
            Beware that for continuity reasons, the point argument in :code:`cellIntersection` is normalized with respect to other
            points used by the caller. This implies that the longitude may be outside of the [-Ã�â‚¬ ; +Ã�â‚¬] interval (or the [0 ;
            2Ã�â‚¬] interval, depending on the DEM). In particular, when a Line Of Sight crosses the antimeridian at Ã‚Â±Ã�â‚¬
            longitude, the library may call the :code:`cellIntersection` method with a point having a longitude of -Ã�â‚¬-ÃŽÂµ to
            ensure this continuity. As tiles are stored with longitude clipped to a some DEM specific interval (either [-Ã�â‚¬ ;
            +Ã�â‚¬] or [0 ; 2Ã�â‚¬]), implementations MUST take care to clip the input point back to the tile interval using
            :code:`MathUtils.normalizeAngle(p.getLongitude(), someLongitudeWithinTheTile)`. The output point normalization should
            also be made consistent with the current tile.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.cellIntersection` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                p (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): point on the line (beware its longitude is *not* normalized with respect to tile)
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight, in the topocentric frame (East, North, Zenith) of the point, scaled to match radians in the horizontal
                    plane and meters along the vertical axis
                latitudeIndex (int): latitude index of the Digital Elevation Model cell
                longitudeIndex (int): longitude index of the Digital Elevation Model cell
        
            Returns:
                point corresponding to line-of-sight crossing the Digital Elevation Model surface if it lies within the cell, null
                otherwise
        
        
        """
        ...
    def getElevationAtIndices(self, int: int, int2: int) -> float:
        """
            Get the elevation of an exact grid point.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getElevationAtIndices` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                latitudeIndex (int): grid point index along latitude
                longitudeIndex (int): grid point index along longitude
        
            Returns:
                elevation at grid point (m)
        
        
        """
        ...
    def getFloorLatitudeIndex(self, double: float) -> int:
        """
            Get the floor latitude index of a point.
        
            The specified latitude is always between index and index+1.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getFloorLatitudeIndex` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                latitude (double): geodetic latitude
        
            Returns:
                floor latitude index (it may lie outside of the tile!)
        
        
        """
        ...
    def getFloorLongitudeIndex(self, double: float) -> int:
        """
            Get the floor longitude index of a point.
        
            The specified longitude is always between index and index+1.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getFloorLongitudeIndex` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                longitude (double): geodetic longitude
        
            Returns:
                floor longitude index (it may lie outside of the tile!)
        
        
        """
        ...
    def getLatitudeAtIndex(self, int: int) -> float:
        """
            Get the latitude at some index.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getLatitudeAtIndex` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                latitudeIndex (int): latitude index
        
            Returns:
                latitude at the specified index (rad) (latitude of the center of the cells of specified row)
        
        
        """
        ...
    def getLatitudeRows(self) -> int:
        """
            Get number of latitude rows.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getLatitudeRows` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                number of latitude rows
        
        
        """
        ...
    def getLatitudeStep(self) -> float:
        """
            Get step in latitude (size of one raster element).
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getLatitudeStep` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                step in latitude (rad)
        
        
        """
        ...
    def getLocation(self, double: float, double2: float) -> Tile.Location:
        """
            Check if a tile covers a ground point.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getLocation` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                latitude (double): ground point latitude
                longitude (double): ground point longitude
        
            Returns:
                location of the ground point with respect to tile
        
        
        """
        ...
    def getLongitudeAtIndex(self, int: int) -> float:
        """
            Get the longitude at some index.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getLongitudeAtIndex` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                longitudeIndex (int): longitude index
        
            Returns:
                longitude at the specified index (rad) (longitude of the center of the cells of specified column)
        
        
        """
        ...
    def getLongitudeColumns(self) -> int:
        """
            Get number of longitude columns.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getLongitudeColumns` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                number of longitude columns
        
        
        """
        ...
    def getLongitudeStep(self) -> float:
        """
            Get step in longitude (size of one raster element).
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getLongitudeStep` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                step in longitude (rad)
        
        
        """
        ...
    def getMaxElevation(self) -> float:
        """
            Get the maximum elevation in the tile.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMaxElevation` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                maximum elevation in the tile (m)
        
        
        """
        ...
    def getMaxElevationLatitudeIndex(self) -> int:
        """
            Get the latitude index of max elevation.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMaxElevationLatitudeIndex`Â in
                interfaceÂ :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                latitude index of max elevation
        
        
        """
        ...
    def getMaxElevationLongitudeIndex(self) -> int:
        """
            Get the longitude index of max elevation.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMaxElevationLongitudeIndex`Â in
                interfaceÂ :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                longitude index of max elevation
        
        
        """
        ...
    def getMaximumLatitude(self) -> float:
        """
            Get maximum latitude.
        
            Beware that as a point at maximum latitude is the northernmost one of the grid, it doesn't have a northwards neighbor
            and therefore calling :meth:`~org.orekit.rugged.raster.Tile.getLocation` on such a latitude will return either
            :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH_WEST`, :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH` or
            :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH_EAST`, but can *never* return
            :meth:`~org.orekit.rugged.raster.Tile.Location.HAS_INTERPOLATION_NEIGHBORS`!
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMaximumLatitude` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                maximum latitude (rad) (latitude of the center of the cells of North row)
        
        
        """
        ...
    def getMaximumLongitude(self) -> float:
        """
            Get maximum longitude.
        
            Beware that as a point at maximum longitude is the easternmost one of the grid, it doesn't have an eastwards neighbor
            and therefore calling :meth:`~org.orekit.rugged.raster.Tile.getLocation` on such a longitude will return either
            :meth:`~org.orekit.rugged.raster.Tile.Location.SOUTH_EAST`, :meth:`~org.orekit.rugged.raster.Tile.Location.EAST` or
            :meth:`~org.orekit.rugged.raster.Tile.Location.NORTH_EAST`, but can *never* return
            :meth:`~org.orekit.rugged.raster.Tile.Location.HAS_INTERPOLATION_NEIGHBORS`!
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMaximumLongitude` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                maximum longitude (rad) (longitude of the center of the cells of East column)
        
        
        """
        ...
    def getMinElevation(self) -> float:
        """
            Get the minimum elevation in the tile.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMinElevation` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                minimum elevation in the tile (m)
        
        
        """
        ...
    def getMinElevationLatitudeIndex(self) -> int:
        """
            Get the latitude index of min elevation.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMinElevationLatitudeIndex`Â in
                interfaceÂ :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                latitude index of min elevation
        
        
        """
        ...
    def getMinElevationLongitudeIndex(self) -> int:
        """
            Get the longitude index of min elevation.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMinElevationLongitudeIndex`Â in
                interfaceÂ :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                longitude index of min elevation
        
        
        """
        ...
    def getMinimumLatitude(self) -> float:
        """
            Get minimum latitude of grid interpolation points.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMinimumLatitude` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                minimum latitude of grid interpolation points (rad) (latitude of the center of the cells of South row)
        
        
        """
        ...
    def getMinimumLongitude(self) -> float:
        """
            Get minimum longitude.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.getMinimumLongitude` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Returns:
                minimum longitude (rad) (longitude of the center of the cells of West column)
        
        
        """
        ...
    def interpolateElevation(self, double: float, double2: float) -> float:
        """
            Interpolate elevation.
        
            In order to cope with numerical accuracy issues when computing points at tile boundary, a slight tolerance (typically
            1/8 cell) around the tile is allowed. Elevation can therefore be interpolated (really extrapolated in this case) even
            for points slightly overshooting tile boundaries, using the closest tile cell. Attempting to interpolate too far from
            the tile will trigger an exception.
        
            This classes uses an arbitrary 1/8 cell tolerance for interpolating slightly out of tile points.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.interpolateElevation` in interface :class:`~org.orekit.rugged.raster.Tile`
        
            Parameters:
                latitude (double): ground point latitude
                longitude (double): ground point longitude
        
            Returns:
                interpolated elevation (m)
        
        
        """
        ...
    def setElevation(self, int: int, int2: int, double: float) -> None:
        """
            Set the elevation for one raster element.
        
            BEWARE! The order of the indices follows geodetic conventions, i.e. the latitude is given first and longitude
            afterwards, so the first index specifies a *row* index with zero at South and max value at North, and the second index
            specifies a *column* index with zero at West and max value at East. This is *not* the same as some raster conventions
            (as our row index increases from South to North) and this is also not the same as Cartesian coordinates as our ordinate
            index appears before our abscissa index).
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.UpdatableTile.setElevation`Â in
                interfaceÂ :class:`~org.orekit.rugged.raster.UpdatableTile`
        
            Parameters:
                latitudeIndex (int): index of latitude (row index)
                longitudeIndex (int): index of longitude (column index)
                elevation (double): elevation (m)
        
        
        """
        ...
    def setGeometry(self, double: float, double2: float, double3: float, double4: float, int: int, int2: int) -> None:
        """
            Set the tile global geometry.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.UpdatableTile.setGeometry`Â in
                interfaceÂ :class:`~org.orekit.rugged.raster.UpdatableTile`
        
            Parameters:
                newMinLatitude (double): minimum latitude (rad)
                newMinLongitude (double): minimum longitude (rad)
                newLatitudeStep (double): step in latitude (size of one raster element) (rad)
                newLongitudeStep (double): step in longitude (size of one raster element) (rad)
                newLatitudeRows (int): number of latitude rows
                newLongitudeColumns (int): number of longitude columns
        
        
        """
        ...
    def tileUpdateCompleted(self) -> None:
        """
            Hook called at the end of tile update completion.
        
            Specified by:
                :meth:`~org.orekit.rugged.raster.Tile.tileUpdateCompleted` in interface :class:`~org.orekit.rugged.raster.Tile`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.raster")``.

    SimpleTile: typing.Type[SimpleTile]
    SimpleTileFactory: typing.Type[SimpleTileFactory]
    Tile: typing.Type[Tile]
    TileFactory: typing.Type[TileFactory]
    TileUpdater: typing.Type[TileUpdater]
    TilesCache: typing.Type[TilesCache]
    UpdatableTile: typing.Type[UpdatableTile]
