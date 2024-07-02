import java.util
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.forces
import org.orekit.frames
import org.orekit.propagation
import org.orekit.utils
import typing



class InertialForces(org.orekit.forces.ForceModel):
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def dependsOnPositionOnly(self) -> bool: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.inertia")``.

    InertialForces: typing.Type[InertialForces]
