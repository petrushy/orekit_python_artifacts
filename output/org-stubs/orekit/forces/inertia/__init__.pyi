import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.forces
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.utils
import typing



class InertialForces(org.orekit.forces.AbstractForceModel):
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def dependsOnPositionOnly(self) -> bool: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParameterDriver(self, string: str) -> org.orekit.utils.ParameterDriver: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.inertia")``.

    InertialForces: typing.Type[InertialForces]
