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
    """
    public class InertialForces extends :class:`~org.orekit.forces.AbstractForceModel`
    
        Inertial force model.
    
        This force model adds the pseudo-forces due to inertia between the integrating frame and a reference inertial frame from
        which this force model is built.
    
        Two typical use-cases are propagating :class:`~org.orekit.utils.AbsolutePVCoordinates` in either:
    
          - a non-inertial frame (for example propagating in the rotating :meth:`~org.orekit.frames.FramesFactory.getITRF` frame),
          - an inertial frame that is not related to the main attracting body (for example propagating in
            :meth:`~org.orekit.frames.FramesFactory.getEME2000` frame a trajectory about the Sun and Jupiter).
    
    
        In the second used case above, the attraction from the two main bodies, i.e. the Sun and Jupiter, should be represented
        by :class:`~org.orekit.forces.gravity.SingleBodyAbsoluteAttraction` instances.
    
        Also see:
            :class:`~org.orekit.forces.gravity.SingleBodyAbsoluteAttraction`
    """
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParameterDriver(self, string: str) -> org.orekit.utils.ParameterDriver:
        """
            Get parameter value from its name.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.getParameterDriver` in interface :class:`~org.orekit.forces.ForceModel`
        
            Overrides:
                :meth:`~org.orekit.forces.AbstractForceModel.getParameterDriver`Â in
                classÂ :class:`~org.orekit.forces.AbstractForceModel`
        
            Parameters:
                name (String): parameter name
        
            Returns:
                parameter value
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.inertia")``.

    InertialForces: typing.Type[InertialForces]
