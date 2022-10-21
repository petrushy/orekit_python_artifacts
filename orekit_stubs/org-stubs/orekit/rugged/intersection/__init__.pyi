import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.api
import org.orekit.rugged.intersection.duvenhage
import org.orekit.rugged.raster
import org.orekit.rugged.utils
import typing



class IntersectionAlgorithm:
    """
    public interface IntersectionAlgorithm
    
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
    def getElevation(self, double: float, double2: float) -> float:
        """
            Get elevation at a given ground point.
        
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
        
            Parameters:
                ellipsoid (:class:`~org.orekit.rugged.utils.ExtendedEllipsoid`): reference ellipsoid
                position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
                closeGuess (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): guess close to the real intersection
        
            Returns:
                point at which the line first enters ground
        
        
        """
        ...

class BasicScanAlgorithm(IntersectionAlgorithm):
    """
    public class BasicScanAlgorithm extends Object implements :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
    
        Intersection computation using a basic algorithm based on exhaustive scan.
    
        The algorithm simply computes entry and exit points at high and low altitudes, and scans all Digital Elevation Models in
        the sub-tiles defined by these two corner points. It is not designed for operational use.
    """
    def __init__(self, tileUpdater: org.orekit.rugged.raster.TileUpdater, int: int): ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
            Get the algorithmId.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getAlgorithmId`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Returns:
                the algorithmId
        
        
        """
        ...
    def getElevation(self, double: float, double2: float) -> float:
        """
            Get elevation at a given ground point.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getElevation`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
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
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.intersection`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
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
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.refineIntersection`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Parameters:
                ellipsoid (:class:`~org.orekit.rugged.utils.ExtendedEllipsoid`): reference ellipsoid
                position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
                closeGuess (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): guess close to the real intersection
        
            Returns:
                point at which the line first enters ground
        
        
        """
        ...

class ConstantElevationAlgorithm(IntersectionAlgorithm):
    """
    public class ConstantElevationAlgorithm extends Object implements :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
    
        Intersection ignoring Digital Elevation Model.
    
        This implementation uses a constant elevation over the ellipsoid.
    """
    def __init__(self, double: float): ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
            Get the algorithmId.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getAlgorithmId`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Returns:
                the algorithmId
        
        
        """
        ...
    def getElevation(self, double: float, double2: float) -> float:
        """
            Get elevation at a given ground point.
        
            As this algorithm uses a constant elevation, this method always returns the same value.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getElevation`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
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
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.intersection`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
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
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.refineIntersection`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Parameters:
                ellipsoid (:class:`~org.orekit.rugged.utils.ExtendedEllipsoid`): reference ellipsoid
                position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
                closeGuess (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): guess close to the real intersection
        
            Returns:
                point at which the line first enters ground
        
        
        """
        ...

class IgnoreDEMAlgorithm(IntersectionAlgorithm):
    """
    public class IgnoreDEMAlgorithm extends Object implements :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
    
        Intersection ignoring Digital Elevation Model.
    
        This dummy implementation simply uses the ellipsoid itself.
    """
    def __init__(self): ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId:
        """
            Get the algorithmId.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getAlgorithmId`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Returns:
                the algorithmId
        
        
        """
        ...
    def getElevation(self, double: float, double2: float) -> float:
        """
            Get elevation at a given ground point.
        
            As this algorithm ignored the Digital Elevation Model, this method always returns 0.0.
        
            Specified by:
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.getElevation`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
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
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.intersection`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
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
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.refineIntersection`Â in
                interfaceÂ :class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`
        
            Parameters:
                ellipsoid (:class:`~org.orekit.rugged.utils.ExtendedEllipsoid`): reference ellipsoid
                position (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel position in ellipsoid frame
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel line-of-sight in ellipsoid frame
                closeGuess (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): guess close to the real intersection
        
            Returns:
                point at which the line first enters ground
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.intersection")``.

    BasicScanAlgorithm: typing.Type[BasicScanAlgorithm]
    ConstantElevationAlgorithm: typing.Type[ConstantElevationAlgorithm]
    IgnoreDEMAlgorithm: typing.Type[IgnoreDEMAlgorithm]
    IntersectionAlgorithm: typing.Type[IntersectionAlgorithm]
    duvenhage: org.orekit.rugged.intersection.duvenhage.__module_protocol__
