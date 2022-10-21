import java.util
import org.hipparchus.analysis.interpolation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.intersection
import org.orekit.rugged.linesensor
import org.orekit.rugged.utils
import typing



class AtmosphericComputationParameters:
    """
    public class AtmosphericComputationParameters extends Object
    
        Atmospheric refraction computation parameters. Defines for inverse location a set of parameters in order to be able to
        perform the computation.
    
        Since:
            2.1
    """
    def __init__(self): ...
    def configureCorrectionGrid(self, lineSensor: org.orekit.rugged.linesensor.LineSensor, int: int, int2: int) -> None:
        """
            Configuration of the interpolation grid. This grid is associated to the given sensor, with the given min and max lines.
        
            Parameters:
                sensor (:class:`~org.orekit.rugged.linesensor.LineSensor`): line sensor
                minLine (int): min line defined for the inverse location
                maxLine (int): max line defined for the inverse location
        
        
        """
        ...
    def getDefaultInverseLocMargin(self) -> float:
        """
        
            Returns:
                the default inverse location margin for computation of inverse location with atmospheric refraction correction.
        
            Since:
                3.0
        
        
        """
        ...
    def getInverseLocMargin(self) -> float:
        """
        
            Returns:
                the inverse location margin for computation of inverse location with atmospheric refraction correction.
        
            Since:
                3.0
        
        
        """
        ...
    def getMaxLineSensor(self) -> float:
        """
        
            Returns:
                the max line used to compute the current grids
        
        
        """
        ...
    def getMinLineSensor(self) -> float:
        """
        
            Returns:
                the min line used to compute the current grids
        
        
        """
        ...
    def getNbLineGrid(self) -> int:
        """
        
            Returns:
                the size of line grid
        
        
        """
        ...
    def getNbPixelGrid(self) -> int:
        """
        
            Returns:
                the size of pixel grid
        
        
        """
        ...
    def getSensorName(self) -> str:
        """
        
            Returns:
                the sensor name used to compute the current grids
        
        
        """
        ...
    def getUgrid(self) -> typing.List[float]:
        """
        
            Returns:
                the pixel grid
        
        
        """
        ...
    def getVgrid(self) -> typing.List[float]:
        """
        
            Returns:
                the line grid
        
        
        """
        ...
    def setGridSteps(self, int: int, int2: int) -> None:
        """
            Set the grid steps in pixel and line (used to compute inverse location). Overwrite the default values, for time
            optimization if necessary.
        
            Parameters:
                gridPixelStep (int): grid pixel step for the inverse location computation
                gridLineStep (int): grid line step for the inverse location computation
        
        
        """
        ...
    def setInverseLocMargin(self, double: float) -> None:
        """
            Set the margin for computation of inverse location with atmospheric refraction correction. Overwrite the default value
            DEFAULT_INVLOC_MARGIN. No check is done about this margin. A recommended value is around 1.
        
            Parameters:
                inverseLocMargin (double): margin in pixel size to compute inverse location with atmospheric refraction correction.
        
            Since:
                3.0
        
        
        """
        ...

class AtmosphericRefraction:
    """
    public abstract class AtmosphericRefraction extends Object
    
        Base class for atmospheric refraction model.
    
        Since:
            2.0
    """
    def applyCorrection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint, intersectionAlgorithm: org.orekit.rugged.intersection.IntersectionAlgorithm) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
            Apply correction to the intersected point with an atmospheric refraction model.
        
            Parameters:
                satPos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite position, in *body frame*
                satLos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite line of sight, in *body frame*
                rawIntersection (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): intersection point before refraction correction
                algorithm (:class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`): intersection algorithm
        
            Returns:
                corrected point with the effect of atmospheric refraction
                :meth:`~org.orekit.rugged.utils.ExtendedEllipsoid.pointAtAltitude` or see
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.refineIntersection`
        
        
        """
        ...
    def computeGridCorrectionFunctions(self, sensorPixelArray: typing.List[typing.List[org.orekit.rugged.linesensor.SensorPixel]]) -> None:
        """
            Compute the correction functions for pixel and lines. The corrections are computed for pixels and lines, on a regular
            grid at sensor level. The corrections are based on the difference on grid nodes (where direct loc is known with
            atmosphere refraction) and the sensor pixel found by inverse loc without atmosphere refraction. The bilinear
            interpolating functions are then computed for pixel and for line. Need to be computed only once for a given sensor with
            the same minLine and maxLine.
        
            Parameters:
                sensorPixelGridInverseWithout (:class:`~org.orekit.rugged.linesensor.SensorPixel`[][]): inverse location grid WITHOUT atmospheric refraction
        
            Since:
                2.1
        
        
        """
        ...
    def configureCorrectionGrid(self, lineSensor: org.orekit.rugged.linesensor.LineSensor, int: int, int2: int) -> None:
        """
            Configuration of the interpolation grid. This grid is associated to the given sensor, with the given min and max lines.
        
            Parameters:
                sensor (:class:`~org.orekit.rugged.linesensor.LineSensor`): line sensor
                minLine (int): min line defined for the inverse location
                maxLine (int): max line defined for the inverse location
        
            Since:
                2.1
        
        
        """
        ...
    def deactivateComputation(self) -> None:
        """
            Deactivate computation (needed for the inverse location computation).
        
            Since:
                2.1
        
        
        """
        ...
    def getBifLine(self) -> org.hipparchus.analysis.interpolation.BilinearInterpolatingFunction:
        """
        
            Returns:
                the bilinear interpolating function for line correction
        
        
        """
        ...
    def getBifPixel(self) -> org.hipparchus.analysis.interpolation.BilinearInterpolatingFunction:
        """
        
            Returns:
                the bilinear interpolating function for pixel correction
        
        
        """
        ...
    def getComputationParameters(self) -> AtmosphericComputationParameters:
        """
            Get the computation parameters.
        
            Returns:
                the AtmosphericComputationParameters
        
            Since:
                2.1
        
        
        """
        ...
    def isSameContext(self, string: str, int: int, int2: int) -> bool:
        """
            Check if the current atmospheric parameters are the same as the asked ones.
        
            Parameters:
                sensorName (String): the asked sensor name
                minLine (int): the asked min line
                maxLine (int): the asked max line
        
            Returns:
                true if same context; false otherwise
        
            Since:
                2.1
        
        
        """
        ...
    def mustBeComputed(self) -> bool:
        """
            Tell if the computation must be performed.
        
            Returns:
                true if computation must be performed; false otherwise
        
            Since:
                2.1
        
        
        """
        ...
    def reactivateComputation(self) -> None:
        """
            Reactivate computation (needed for the inverse location computation).
        
            Since:
                2.1
        
        
        """
        ...
    def setGridSteps(self, int: int, int2: int) -> None:
        """
            Set the grid steps in pixel and line (used to compute inverse location). Overwrite the default values, for time
            optimization for instance.
        
            Parameters:
                pixelStep (int): pixel step for the inverse location computation
                lineStep (int): line step for the inverse location computation
        
            Since:
                2.1
        
        
        """
        ...
    def setInverseLocMargin(self, double: float) -> None:
        """
            Set the margin for computation of inverse location with atmospheric refraction correction. Overwrite the default value
            DEFAULT_INVLOC_MARGIN. No check is done about this margin. A recommended value is around 1.
        
            Parameters:
                inverseLocMargin (double): margin in pixel size to compute inverse location with atmospheric refraction correction.
        
            Since:
                3.0
        
        
        """
        ...

class ConstantRefractionLayer:
    """
    public class ConstantRefractionLayer extends Object
    
        Class that represents a constant refraction layer to be used with
        :class:`~org.orekit.rugged.refraction.MultiLayerModel`.
    
        Since:
            2.0
    """
    def __init__(self, double: float, double2: float): ...
    def getLowestAltitude(self) -> float:
        """
        
            Returns:
                the lowest altitude of the layer (m)
        
        
        """
        ...
    def getRefractiveIndex(self) -> float:
        """
        
            Returns:
                the refractive index of the layer
        
        
        """
        ...

class MultiLayerModel(AtmosphericRefraction):
    """
    public class MultiLayerModel extends :class:`~org.orekit.rugged.refraction.AtmosphericRefraction`
    
        Atmospheric refraction model based on multiple layers with associated refractive index.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid): ...
    @typing.overload
    def __init__(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, list: java.util.List[ConstantRefractionLayer]): ...
    def applyCorrection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint, intersectionAlgorithm: org.orekit.rugged.intersection.IntersectionAlgorithm) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
            Apply correction to the intersected point with an atmospheric refraction model.
        
            Specified by:
                :meth:`~org.orekit.rugged.refraction.AtmosphericRefraction.applyCorrection`Â in
                classÂ :class:`~org.orekit.rugged.refraction.AtmosphericRefraction`
        
            Parameters:
                satPos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite position, in *body frame*
                satLos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite line of sight, in *body frame*
                rawIntersection (:class:`~org.orekit.rugged.utils.NormalizedGeodeticPoint`): intersection point before refraction correction
                algorithm (:class:`~org.orekit.rugged.intersection.IntersectionAlgorithm`): intersection algorithm
        
            Returns:
                corrected point with the effect of atmospheric refraction
                :meth:`~org.orekit.rugged.utils.ExtendedEllipsoid.pointAtAltitude` or see
                :meth:`~org.orekit.rugged.intersection.IntersectionAlgorithm.refineIntersection`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.refraction")``.

    AtmosphericComputationParameters: typing.Type[AtmosphericComputationParameters]
    AtmosphericRefraction: typing.Type[AtmosphericRefraction]
    ConstantRefractionLayer: typing.Type[ConstantRefractionLayer]
    MultiLayerModel: typing.Type[MultiLayerModel]
