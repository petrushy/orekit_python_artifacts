
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus.analysis.interpolation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.intersection
import org.orekit.rugged.linesensor
import org.orekit.rugged.utils
import typing



class AtmosphericComputationParameters:
    """
    Atmospheric refraction computation parameters. Defines for inverse location a set of parameters in order to be able to perform the computation.
    
    Since:
        2.1
    """
    def __init__(self):
        """
        Default constructor.
        """
        ...
    def configureCorrectionGrid(self, sensor: org.orekit.rugged.linesensor.LineSensor, minLine: int, maxLine: int) -> None:
        """
        Configuration of the interpolation grid. This grid is associated to the given sensor, with the given min and max lines.
        
        Parameters:
            sensor (LineSensor): line sensor
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
    def getUgrid(self) -> typing.MutableSequence[float]:
        """
        Returns:
            the pixel grid
        
        
        """
        ...
    def getVgrid(self) -> typing.MutableSequence[float]:
        """
        Returns:
            the line grid
        
        
        """
        ...
    def setGridSteps(self, gridPixelStep: int, gridLineStep: int) -> None:
        """
        Set the grid steps in pixel and line (used to compute inverse location). Overwrite the default values, for time optimization if necessary.
        
        Parameters:
            gridPixelStep (int): grid pixel step for the inverse location computation
            gridLineStep (int): grid line step for the inverse location computation
        
        
        """
        ...
    def setInverseLocMargin(self, inverseLocMargin: float) -> None:
        """
        Set the margin for computation of inverse location with atmospheric refraction correction. Overwrite the default value DEFAULT_INVLOC_MARGIN. No check is done about this margin. A recommended value is around 1.
        
        Parameters:
            inverseLocMargin (double): margin in pixel size to compute inverse location with atmospheric refraction correction.
        
        Since:
            3.0
        
        
        """
        ...

class AtmosphericRefraction:
    """
    Base class for atmospheric refraction model.
    
    Since:
        2.0
    """
    def applyCorrection(self, satPos: org.hipparchus.geometry.euclidean.threed.Vector3D, satLos: org.hipparchus.geometry.euclidean.threed.Vector3D, rawIntersection: org.orekit.rugged.utils.NormalizedGeodeticPoint, algorithm: org.orekit.rugged.intersection.IntersectionAlgorithm) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Apply correction to the intersected point with an atmospheric refraction model.
        
        Parameters:
            satPos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite position, in body frame
            satLos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite line of sight, in body frame
            rawIntersection (NormalizedGeodeticPoint): intersection point before refraction correction
            algorithm (IntersectionAlgorithm): intersection algorithm
        
        Returns:
            corrected point with the effect of atmospheric refraction
            pointAtAltitude or see
            refineIntersection
        
        
        """
        ...
    def computeGridCorrectionFunctions(self, sensorPixelGridInverseWithout: typing.Union[typing.List[typing.MutableSequence[org.orekit.rugged.linesensor.SensorPixel]], jpype.JArray]) -> None:
        """
        Compute the correction functions for pixel and lines. The corrections are computed for pixels and lines, on a regular grid at sensor level. The corrections are based on the difference on grid nodes (where direct loc is known with atmosphere refraction) and the sensor pixel found by inverse loc without atmosphere refraction. The bilinear interpolating functions are then computed for pixel and for line. Need to be computed only once for a given sensor with the same minLine and maxLine.
        
        Parameters:
            sensorPixelGridInverseWithout (SensorPixel[][]): inverse location grid WITHOUT atmospheric refraction
        
        Since:
            2.1
        
        
        """
        ...
    def configureCorrectionGrid(self, sensor: org.orekit.rugged.linesensor.LineSensor, minLine: int, maxLine: int) -> None:
        """
        Configuration of the interpolation grid. This grid is associated to the given sensor, with the given min and max lines.
        
        Parameters:
            sensor (LineSensor): line sensor
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
    def isSameContext(self, sensorName: str, minLine: int, maxLine: int) -> bool:
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
    def setGridSteps(self, pixelStep: int, lineStep: int) -> None:
        """
        Set the grid steps in pixel and line (used to compute inverse location). Overwrite the default values, for time optimization for instance.
        
        Parameters:
            pixelStep (int): pixel step for the inverse location computation
            lineStep (int): line step for the inverse location computation
        
        Since:
            2.1
        
        
        """
        ...
    def setInverseLocMargin(self, inverseLocMargin: float) -> None:
        """
        Set the margin for computation of inverse location with atmospheric refraction correction. Overwrite the default value DEFAULT_INVLOC_MARGIN. No check is done about this margin. A recommended value is around 1.
        
        Parameters:
            inverseLocMargin (double): margin in pixel size to compute inverse location with atmospheric refraction correction.
        
        Since:
            3.0
        
        
        """
        ...

class ConstantRefractionLayer:
    """
    Class that represents a constant refraction layer to be used with MultiLayerModel.
    
    Since:
        2.0
    """
    def __init__(self, lowestAltitude: float, refractiveIndex: float):
        """
        Simple constructor.
        
        Parameters:
            lowestAltitude (double): lowest altitude of the layer (m)
            refractiveIndex (double): refractive index of the layer
        
        
        """
        ...
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
    Atmospheric refraction model based on multiple layers with associated refractive index.
    
    Since:
        2.0
    """
    @typing.overload
    def __init__(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid): ...
    @typing.overload
    def __init__(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, list: java.util.List[ConstantRefractionLayer]): ...
    def applyCorrection(self, satPos: org.hipparchus.geometry.euclidean.threed.Vector3D, satLos: org.hipparchus.geometry.euclidean.threed.Vector3D, rawIntersection: org.orekit.rugged.utils.NormalizedGeodeticPoint, algorithm: org.orekit.rugged.intersection.IntersectionAlgorithm) -> org.orekit.rugged.utils.NormalizedGeodeticPoint:
        """
        Apply correction to the intersected point with an atmospheric refraction model.
        
        Specified by: applyCorrection in class AtmosphericRefraction
        
        Parameters:
            satPos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite position, in body frame
            satLos (org.hipparchus.geometry.euclidean.threed.Vector3D): satellite line of sight, in body frame
            rawIntersection (NormalizedGeodeticPoint): intersection point before refraction correction
            algorithm (IntersectionAlgorithm): intersection algorithm
        
        Returns:
            corrected point with the effect of atmospheric refraction
            pointAtAltitude or see
            refineIntersection
        
        
        """
        ...

class PythonAtmosphericRefraction(AtmosphericRefraction):
    def __init__(self): ...
    def applyCorrection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint, intersectionAlgorithm: org.orekit.rugged.intersection.IntersectionAlgorithm) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.refraction")``.

    AtmosphericComputationParameters: typing.Type[AtmosphericComputationParameters]
    AtmosphericRefraction: typing.Type[AtmosphericRefraction]
    ConstantRefractionLayer: typing.Type[ConstantRefractionLayer]
    MultiLayerModel: typing.Type[MultiLayerModel]
    PythonAtmosphericRefraction: typing.Type[PythonAtmosphericRefraction]
