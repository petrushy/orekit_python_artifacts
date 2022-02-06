import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.forces.drag
import org.orekit.forces.empirical
import org.orekit.forces.gravity
import org.orekit.forces.inertia
import org.orekit.forces.maneuvers
import org.orekit.forces.radiation
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



class BoxAndSolarArraySpacecraft(org.orekit.forces.radiation.RadiationSensitive, org.orekit.forces.drag.DragSensitive):
    """
    public class BoxAndSolarArraySpacecraft extends Object implements :class:`~org.orekit.forces.radiation.RadiationSensitive`, :class:`~org.orekit.forces.drag.DragSensitive`
    
        Class representing the features of a classical satellite with a convex body shape and rotating flat solar arrays.
    
        The body can be either a simple parallelepipedic box aligned with spacecraft axes or a set of facets defined by their
        area and normal vector. This should handle accurately most spacecraft shapes.
    
        The solar array rotation with respect to satellite body can be either the best lighting orientation (i.e. Sun exactly in
        solar array meridian plane defined by solar array rotation axis and solar array normal vector) or a rotation evolving
        linearly according to a start position and an angular rate (which can be set to 0 for non-rotating panels, which may
        occur in special modes or during contingencies).
    
        The lift component of the drag force can be optionally considered. It should probably only be used for reentry
        computation, with much denser atmosphere than in regular orbit propagation. The lift component is computed using a ratio
        of molecules that experience specular reflection instead of diffuse reflection (absorption followed by outgassing at
        negligible velocity). Without lift (i.e. when the lift ratio is set to 0), drag force is along atmosphere relative
        velocity. With lift (i.e. when the lift ratio is set to any value between 0 and 1), the drag force depends on both
        relative velocity direction and facets normal orientation. For a single panel, if the relative velocity is head-on (i.e.
        aligned with the panel normal), the force will be in the same direction with and without lift, but the magnitude with
        lift ratio set to 1.0 will be twice the magnitude with lift ratio set to 0.0 (because atmosphere molecules bounces
        backward at same velocity in case of specular reflection).
    
        This model does not take cast shadow between body and solar array into account.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double4: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double4: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double4: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double4: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double5: float, double6: float, double7: float, double8: float, double9: float): ...
    @typing.overload
    def __init__(self, facetArray: typing.List['BoxAndSolarArraySpacecraft.Facet'], pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, facetArray: typing.List['BoxAndSolarArraySpacecraft.Facet'], pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, facetArray: typing.List['BoxAndSolarArraySpacecraft.Facet'], pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float, double5: float): ...
    @typing.overload
    def __init__(self, facetArray: typing.List['BoxAndSolarArraySpacecraft.Facet'], pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_dragAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_dragAcceleration_0__T], t: _dragAcceleration_0__T, t2: _dragAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], tArray: typing.List[_dragAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                density (T): atmospheric density at spacecraft position
                relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, double2: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                density (double): atmospheric density at spacecraft position
                relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getNormal_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]:
        """
            Get solar array normal in spacecraft frame.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
        
            Returns:
                solar array normal in spacecraft frame
        
        
        """
        ...
    @typing.overload
    def getNormal(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get solar array normal in spacecraft frame.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
        
            Returns:
                solar array normal in spacecraft frame
        
        """
        ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_radiationPressureAcceleration_0__T], frame: org.orekit.frames.Frame, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_radiationPressureAcceleration_0__T], t: _radiationPressureAcceleration_0__T, fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (FieldVector3D<T> position): position of spacecraft in reference frame
                rotation (FieldRotation<T> rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (T): current mass
                flux (FieldVector3D<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, double: float, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): inertial reference frame for state (both orbit and attitude)
                position (Vector3D): position of spacecraft in reference frame
                rotation (Rotation): orientation (attitude) of the spacecraft with respect to reference frame
                mass (double): current mass
                flux (Vector3D): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/sÂ²)
        
        """
        ...
    class Facet:
        def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
        def getArea(self) -> float: ...
        def getNormal(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class ForceModel:
    """
    public interface ForceModel
    
        This interface represents a force modifying spacecraft motion.
    
        Objects implementing this interface are intended to be added to a
        :class:`~org.orekit.propagation.numerical.NumericalPropagator` before the propagation is started.
    
        The propagator will call at each step the :meth:`~org.orekit.forces.ForceModel.addContribution` method. The force model
        instance will extract all the state data it needs (date, position, velocity, frame, attitude, mass) from the first
        parameter. From these state data, it will compute the perturbing acceleration. It will then add this acceleration to the
        second parameter which will take thins contribution into account and will use the Gauss equations to evaluate its impact
        on the global state derivative.
    
        Force models which create discontinuous acceleration patterns (typically for maneuvers start/stop or solar eclipses
        entry/exit) must provide one or more :class:`~org.orekit.propagation.events.EventDetector` to the propagator thanks to
        their :meth:`~org.orekit.forces.ForceModel.getEventsDetectors` method. This method is called once just before
        propagation starts. The events states will be checked by the propagator to ensure accurate propagation and proper events
        handling.
    """
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
        
            Since:
                9.0
        
        
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
        
            Since:
                9.0
        
        """
        ...
    _addContribution_0__T = typing.TypeVar('_addContribution_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addContribution(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_addContribution_0__T], fieldTimeDerivativesEquations: org.orekit.propagation.numerical.FieldTimeDerivativesEquations[_addContribution_0__T]) -> None:
        """
            Compute the contribution of the force model to the perturbing acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                adder (:class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`<T> adder): object where the contribution should be added
        
        
        """
        ...
    @typing.overload
    def addContribution(self, spacecraftState: org.orekit.propagation.SpacecraftState, timeDerivativesEquations: org.orekit.propagation.numerical.TimeDerivativesEquations) -> None:
        """
            Compute the contribution of the force model to the perturbing acceleration.
        
            The default implementation simply adds the null as a non-Keplerian acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                adder (:class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`): object where the contribution should be added
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
            Since:
                9.0
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParameterDriver(self, string: str) -> org.orekit.utils.ParameterDriver:
        """
            Get parameter value from its name.
        
            Parameters:
                name (String): parameter name
        
            Returns:
                parameter value
        
            Since:
                8.0
        
        
        """
        ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get force model parameters.
        
            Returns:
                force model parameters
        
            Since:
                9.0
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T]) -> typing.List[_getParameters_1__T]:
        """
            Get force model parameters.
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                force model parameters
        
            Since:
                9.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`, null or
            null
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> initialState): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.FieldAbsoluteDate`<T> target): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`, null or
            null
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...
    def isSupported(self, string: str) -> bool:
        """
            Check if a parameter is supported.
        
            Supported parameters are those listed by :meth:`~org.orekit.forces.ForceModel.getParametersDrivers`.
        
            Parameters:
                name (String): parameter name to check
        
            Returns:
                true if the parameter is supported
        
            Also see:
                :meth:`~org.orekit.forces.ForceModel.getParametersDrivers`
        
        
        """
        ...

class AbstractForceModel(ForceModel):
    """
    public abstract class AbstractForceModel extends Object implements :class:`~org.orekit.forces.ForceModel`
    
        Base class for force models.
    
        Since:
            8.0
    """
    def __init__(self): ...
    def getParameterDriver(self, string: str) -> org.orekit.utils.ParameterDriver:
        """
            Get parameter value from its name.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.getParameterDriver` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                name (String): parameter name
        
            Returns:
                parameter value
        
        
        """
        ...
    def isSupported(self, string: str) -> bool:
        """
            Check if a parameter is supported.
        
            Supported parameters are those listed by :meth:`~org.orekit.forces.ForceModel.getParametersDrivers`.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.isSupported` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                name (String): parameter name to check
        
            Returns:
                true if the parameter is supported
        
            Also see:
                :meth:`~org.orekit.forces.ForceModel.getParametersDrivers`
        
        
        """
        ...

class PythonForceModel(ForceModel):
    """
    public class PythonForceModel extends Object implements :class:`~org.orekit.forces.ForceModel`
    """
    def __init__(self): ...
    _acceleration_1__T = typing.TypeVar('_acceleration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
            Compute acceleration.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_1__T], tArray: typing.List[_acceleration_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_1__T]: ...
    _acceleration_FT__T = typing.TypeVar('_acceleration_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def acceleration_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_FT__T], tArray: typing.List[_acceleration_FT__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_FT__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
        
        """
        ...
    _addContribution_1__T = typing.TypeVar('_addContribution_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addContribution(self, spacecraftState: org.orekit.propagation.SpacecraftState, timeDerivativesEquations: org.orekit.propagation.numerical.TimeDerivativesEquations) -> None:
        """
            Compute the contribution of the force model to the perturbing acceleration.
        
            The default implementation simply adds the null as a non-Keplerian acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.addContribution` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                adder (:class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`): object where the contribution should be added
        
        """
        ...
    @typing.overload
    def addContribution(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_addContribution_1__T], fieldTimeDerivativesEquations: org.orekit.propagation.numerical.FieldTimeDerivativesEquations[_addContribution_1__T]) -> None:
        """
            Compute the contribution of the force model to the perturbing acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.addContribution` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                adder (:class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`<T> adder): object where the contribution should be added
        
        
        """
        ...
    _addContribution_FF__T = typing.TypeVar('_addContribution_FF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def addContribution_FF(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_addContribution_FF__T], fieldTimeDerivativesEquations: org.orekit.propagation.numerical.FieldTimeDerivativesEquations[_addContribution_FF__T]) -> None: ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.dependsOnPositionOnly` in interface :class:`~org.orekit.forces.ForceModel`
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
            Since:
                9.0
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParameterDriver(self, string: str) -> org.orekit.utils.ParameterDriver:
        """
            Get parameter value from its name.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.getParameterDriver` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                name (String): parameter name
        
            Returns:
                parameter value
        
            Since:
                8.0
        
        
        """
        ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get force model parameters.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.getParameters` in interface :class:`~org.orekit.forces.ForceModel`
        
            Returns:
                force model parameters
        
            Since:
                9.0
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T]) -> typing.List[_getParameters_1__T]:
        """
            Get force model parameters.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.getParameters` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                force model parameters
        
            Since:
                9.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getParameters_F__T = typing.TypeVar('_getParameters_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getParameters_F(self, field: org.hipparchus.Field[_getParameters_F__T]) -> typing.List[_getParameters_F__T]:
        """
            Get force model parameters.
        
            Parameters:
                field (Field<T> field): field to which the elements belong
        
            Returns:
                force model parameters
        
            Since:
                9.0
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.PythonForceModel.addContribution`,
            :meth:`~org.orekit.forces.PythonForceModel.addContribution`, null or null
        
            The default implementation of this method does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.init` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    def isSupported(self, string: str) -> bool:
        """
            Check if a parameter is supported.
        
            Supported parameters are those listed by :meth:`~org.orekit.forces.PythonForceModel.getParametersDrivers`.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.isSupported` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                name (String): parameter name to check
        
            Returns:
                true if the parameter is supported
        
            Also see:
                :meth:`~org.orekit.forces.PythonForceModel.getParametersDrivers`
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...

class PythonAbstractForceModel(AbstractForceModel):
    """
    public class PythonAbstractForceModel extends :class:`~org.orekit.forces.AbstractForceModel`
    """
    def __init__(self): ...
    _acceleration_1__T = typing.TypeVar('_acceleration_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration. Extension point for Python.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
            Compute acceleration. Automatically directs to the Python extension point acceleration_FT
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_1__T], tArray: typing.List[_acceleration_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_1__T]: ...
    _acceleration_FT__T = typing.TypeVar('_acceleration_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def acceleration_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_FT__T], tArray: typing.List[_acceleration_FT__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_FT__T]:
        """
            Compute acceleration, Alternative python interface point for the acceleration method. Extension point for Python.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
            Since:
                9.0
        
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only. Extension point for Python.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
            Since:
                9.0
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces")``.

    AbstractForceModel: typing.Type[AbstractForceModel]
    BoxAndSolarArraySpacecraft: typing.Type[BoxAndSolarArraySpacecraft]
    ForceModel: typing.Type[ForceModel]
    PythonAbstractForceModel: typing.Type[PythonAbstractForceModel]
    PythonForceModel: typing.Type[PythonForceModel]
    drag: org.orekit.forces.drag.__module_protocol__
    empirical: org.orekit.forces.empirical.__module_protocol__
    gravity: org.orekit.forces.gravity.__module_protocol__
    inertia: org.orekit.forces.inertia.__module_protocol__
    maneuvers: org.orekit.forces.maneuvers.__module_protocol__
    radiation: org.orekit.forces.radiation.__module_protocol__
