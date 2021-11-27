import java.util
import java.util.stream
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.utils
import org.orekit.time
import org.orekit.utils
import typing



class LOSBuilder:
    def __init__(self, list: java.util.List[org.hipparchus.geometry.euclidean.threed.Vector3D]): ...
    @typing.overload
    def addTransform(self, lOSTransform: 'LOSTransform') -> 'LOSBuilder': ...
    @typing.overload
    def addTransform(self, timeIndependentLOSTransform: 'TimeIndependentLOSTransform') -> 'LOSBuilder': ...
    def build(self) -> 'TimeDependentLOS': ...

class LOSTransform:
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], absoluteDate: org.orekit.time.AbsoluteDate, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]: ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class TimeDependentLOS:
    def getLOS(self, int: int, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _getLOSDerivatives__T = typing.TypeVar('_getLOSDerivatives__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    def getLOSDerivatives(self, int: int, absoluteDate: org.orekit.time.AbsoluteDate, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_getLOSDerivatives__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLOSDerivatives__T]: ...
    def getNbPixels(self) -> int: ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...

class TimeIndependentLOSTransform:
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]: ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class FixedZHomothety(TimeIndependentLOSTransform):
    def __init__(self, string: str, double: float): ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]: ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.los")``.

    FixedZHomothety: typing.Type[FixedZHomothety]
    LOSBuilder: typing.Type[LOSBuilder]
    LOSTransform: typing.Type[LOSTransform]
    TimeDependentLOS: typing.Type[TimeDependentLOS]
    TimeIndependentLOSTransform: typing.Type[TimeIndependentLOSTransform]
