
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.api
import org.orekit.rugged.intersection.duvenhage
import org.orekit.rugged.raster
import org.orekit.rugged.utils
import typing



class IntersectionAlgorithm:
    """
    Interface for Digital Elevation Model intersection algorithm.
    """
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
        Get the algorithmId.
        
        Returns:
            the algorithmId
        
        Since:
            2.2
        
        
        """
        ...
    def getElevation(self, latitude: float, longitude: float) -> float:
        """
        Get elevation at a given ground point.
        
        Parameters:
            latitude (double): ground point latitude
            longitude (double): ground point longitude
        
        Returns:
            elevation at specified point
        
        
        """
        ...
    def intersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Compute intersection of line with Digital Elevation Model.
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...
    def refineIntersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, closeGuess: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Refine intersection of line with Digital Elevation Model.
        
        This method is used to refine an intersection when a close guess is already known. The intersection is typically looked for by a direct cellIntersection in the tile which already contains the close guess, or any similar very fast algorithm.
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
            closeGuess (NormalizedGeodeticPoint): guess close to the real intersection
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...

class BasicScanAlgorithm(IntersectionAlgorithm):
    """
    Intersection computation using a basic algorithm based on exhaustive scan.
    
    The algorithm simply computes entry and exit points at high and low altitudes, and scans all Digital Elevation Models in the sub-tiles defined by these two corner points. It is not designed for operational use.
    """
    def __init__(self, updater: typing.Union[org.orekit.rugged.raster.TileUpdater, typing.Callable], maxCachedTiles: int, isOverlappingTiles: bool):
        """
        Simple constructor.
        
        Parameters:
            updater (TileUpdater): updater used to load Digital Elevation Model tiles
            maxCachedTiles (int): maximum number of tiles stored in the cache
            isOverlappingTiles (boolean): flag to tell if the DEM tiles are overlapping: true if overlapping; false otherwise.
        
        
        """
        ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
        Get the algorithmId.
        
        Specified by: getAlgorithmId in interface IntersectionAlgorithm
        
        Returns:
            the algorithmId
        
        
        """
        ...
    def getElevation(self, latitude: float, longitude: float) -> float:
        """
        Get elevation at a given ground point.
        
        Specified by: getElevation in interface IntersectionAlgorithm
        
        Parameters:
            latitude (double): ground point latitude
            longitude (double): ground point longitude
        
        Returns:
            elevation at specified point
        
        
        """
        ...
    def intersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Compute intersection of line with Digital Elevation Model.
        
        Specified by: intersection in interface IntersectionAlgorithm
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...
    def refineIntersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, closeGuess: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Refine intersection of line with Digital Elevation Model.
        
        This method is used to refine an intersection when a close guess is already known. The intersection is typically looked for by a direct cellIntersection in the tile which already contains the close guess, or any similar very fast algorithm.
        
        Specified by: refineIntersection in interface IntersectionAlgorithm
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
            closeGuess (NormalizedGeodeticPoint): guess close to the real intersection
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...

class ConstantElevationAlgorithm(IntersectionAlgorithm):
    """
    Intersection ignoring Digital Elevation Model.
    
    This implementation uses a constant elevation over the ellipsoid.
    """
    def __init__(self, constantElevation: float):
        """
        Simple constructor.
        
        Parameters:
            constantElevation (double): constant elevation over ellipsoid
        
        
        """
        ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
        Get the algorithmId.
        
        Specified by: getAlgorithmId in interface IntersectionAlgorithm
        
        Returns:
            the algorithmId
        
        
        """
        ...
    def getElevation(self, latitude: float, longitude: float) -> float:
        """
        Get elevation at a given ground point.
        
        As this algorithm uses a constant elevation, this method always returns the same value.
        
        Specified by: getElevation in interface IntersectionAlgorithm
        
        Parameters:
            latitude (double): ground point latitude
            longitude (double): ground point longitude
        
        Returns:
            elevation at specified point
        
        
        """
        ...
    def intersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Compute intersection of line with Digital Elevation Model.
        
        Specified by: intersection in interface IntersectionAlgorithm
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...
    def refineIntersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, closeGuess: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Refine intersection of line with Digital Elevation Model.
        
        This method is used to refine an intersection when a close guess is already known. The intersection is typically looked for by a direct cellIntersection in the tile which already contains the close guess, or any similar very fast algorithm.
        
        Specified by: refineIntersection in interface IntersectionAlgorithm
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
            closeGuess (NormalizedGeodeticPoint): guess close to the real intersection
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...

class IgnoreDEMAlgorithm(IntersectionAlgorithm):
    """
    Intersection ignoring Digital Elevation Model.
    
    This dummy implementation simply uses the ellipsoid itself.
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
        Get the algorithmId.
        
        Specified by: getAlgorithmId in interface IntersectionAlgorithm
        
        Returns:
            the algorithmId
        
        
        """
        ...
    def getElevation(self, latitude: float, longitude: float) -> float:
        """
        Get elevation at a given ground point.
        
        As this algorithm ignored the Digital Elevation Model, this method always returns 0.0.
        
        Specified by: getElevation in interface IntersectionAlgorithm
        
        Parameters:
            latitude (double): ground point latitude
            longitude (double): ground point longitude
        
        Returns:
            elevation at specified point
        
        
        """
        ...
    def intersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Compute intersection of line with Digital Elevation Model.
        
        Specified by: intersection in interface IntersectionAlgorithm
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...
    def refineIntersection(self, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, closeGuess: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Refine intersection of line with Digital Elevation Model.
        
        This method is used to refine an intersection when a close guess is already known. The intersection is typically looked for by a direct cellIntersection in the tile which already contains the close guess, or any similar very fast algorithm.
        
        Specified by: refineIntersection in interface IntersectionAlgorithm
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): reference ellipsoid
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
            closeGuess (NormalizedGeodeticPoint): guess close to the real intersection
        
        Returns:
            point at which the line first enters ground
        
        
        """
        ...

class PythonIntersectionAlgorithmI(IntersectionAlgorithm):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId: ...
    def getElevation(self, double: float, double2: float) -> float: ...
    def intersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def refineIntersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.intersection")``.

    BasicScanAlgorithm: typing.Type[BasicScanAlgorithm]
    ConstantElevationAlgorithm: typing.Type[ConstantElevationAlgorithm]
    IgnoreDEMAlgorithm: typing.Type[IgnoreDEMAlgorithm]
    IntersectionAlgorithm: typing.Type[IntersectionAlgorithm]
    PythonIntersectionAlgorithmI: typing.Type[PythonIntersectionAlgorithmI]
    duvenhage: org.orekit.rugged.intersection.duvenhage.__module_protocol__
