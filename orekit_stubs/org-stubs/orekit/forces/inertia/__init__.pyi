
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
    Inertial force model.
    
    This force model adds the pseudo-forces due to inertia between the integrating frame and a reference inertial frame from which this force model is built.
    
    Two typical use-cases are propagating AbsolutePVCoordinates in either:
    
      - a non-inertial frame (for example propagating in the rotating getITRF frame),
      - an inertial frame that is not related to the main attracting body (for example propagating in
        getEME2000 frame a trajectory about the Sun and Jupiter).
    
    In the second used case above, the attraction from the two main bodies, i.e. the Sun and Jupiter, should be represented by SingleBodyAbsoluteAttraction instances.
    
    Also see:
        SingleBodyAbsoluteAttraction
    """
    def __init__(self, referenceInertialFrame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        Parameters:
            referenceInertialFrame (Frame): the pseudo-inertial frame to use as reference for the inertial forces
        
        Raises:
            OrekitIllegalArgumentException: if frame is not a isPseudoInertial
        
        
        """
        ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
        Check if force model depends on position only at a given, fixed date.
        
        Specified by: dependsOnPositionOnly in interface ForceModel
        
        Returns:
            true if force model depends on position only, false if it depends on mass or velocity, either directly or due to a
            dependency on attitude
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.inertia")``.

    InertialForces: typing.Type[InertialForces]
