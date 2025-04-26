
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.forces
import org.orekit.frames
import org.orekit.propagation
import org.orekit.utils
import typing



class InertialForces(org.orekit.forces.ForceModel):
    """
    public class InertialForces extends :class:`~org.orekit.forces.inertia.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.ForceModel`
    
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
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force model depends on position only at a given, fixed date.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.dependsOnPositionOnly` in interface :class:`~org.orekit.forces.ForceModel`
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.inertia")``.

    InertialForces: typing.Type[InertialForces]
