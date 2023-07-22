import java.util
import org.hipparchus.analysis.interpolation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.intersection
import org.orekit.rugged.linesensor
import org.orekit.rugged.utils
import typing



class AtmosphericComputationParameters:
    def __init__(self): ...
    def configureCorrectionGrid(self, lineSensor: org.orekit.rugged.linesensor.LineSensor, int: int, int2: int) -> None: ...
    def getDefaultInverseLocMargin(self) -> float: ...
    def getInverseLocMargin(self) -> float: ...
    def getMaxLineSensor(self) -> float: ...
    def getMinLineSensor(self) -> float: ...
    def getNbLineGrid(self) -> int: ...
    def getNbPixelGrid(self) -> int: ...
    def getSensorName(self) -> str: ...
    def getUgrid(self) -> typing.List[float]: ...
    def getVgrid(self) -> typing.List[float]: ...
    def setGridSteps(self, int: int, int2: int) -> None: ...
    def setInverseLocMargin(self, double: float) -> None: ...

class AtmosphericRefraction:
    def applyCorrection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint, intersectionAlgorithm: org.orekit.rugged.intersection.IntersectionAlgorithm) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...
    def computeGridCorrectionFunctions(self, sensorPixelArray: typing.List[typing.List[org.orekit.rugged.linesensor.SensorPixel]]) -> None: ...
    def configureCorrectionGrid(self, lineSensor: org.orekit.rugged.linesensor.LineSensor, int: int, int2: int) -> None: ...
    def deactivateComputation(self) -> None: ...
    def getBifLine(self) -> org.hipparchus.analysis.interpolation.BilinearInterpolatingFunction: ...
    def getBifPixel(self) -> org.hipparchus.analysis.interpolation.BilinearInterpolatingFunction: ...
    def getComputationParameters(self) -> AtmosphericComputationParameters: ...
    def isSameContext(self, string: str, int: int, int2: int) -> bool: ...
    def mustBeComputed(self) -> bool: ...
    def reactivateComputation(self) -> None: ...
    def setGridSteps(self, int: int, int2: int) -> None: ...
    def setInverseLocMargin(self, double: float) -> None: ...

class ConstantRefractionLayer:
    def __init__(self, double: float, double2: float): ...
    def getLowestAltitude(self) -> float: ...
    def getRefractiveIndex(self) -> float: ...

class MultiLayerModel(AtmosphericRefraction):
    @typing.overload
    def __init__(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid): ...
    @typing.overload
    def __init__(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, list: java.util.List[ConstantRefractionLayer]): ...
    def applyCorrection(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint, intersectionAlgorithm: org.orekit.rugged.intersection.IntersectionAlgorithm) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.refraction")``.

    AtmosphericComputationParameters: typing.Type[AtmosphericComputationParameters]
    AtmosphericRefraction: typing.Type[AtmosphericRefraction]
    ConstantRefractionLayer: typing.Type[ConstantRefractionLayer]
    MultiLayerModel: typing.Type[MultiLayerModel]
