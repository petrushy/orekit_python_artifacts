import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.forces.class-use
import org.orekit.forces.drag
import org.orekit.forces.empirical
import org.orekit.forces.gravity
import org.orekit.forces.inertia
import org.orekit.forces.maneuvers
import org.orekit.forces.radiation
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



class BoxAndSolarArraySpacecraft(org.orekit.forces.radiation.RadiationSensitive, org.orekit.forces.drag.DragSensitive):
    """
    public class BoxAndSolarArraySpacecraft extends :class:`~org.orekit.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.radiation.RadiationSensitive`, :class:`~org.orekit.forces.drag.DragSensitive`
    
        Class representing the features of a classical satellite with a convex body shape.
    
        The body can be either a simple parallelepipedic box aligned with spacecraft axes or a set of panels defined by their
        area and normal vector. Some panels may be moving to model solar arrays (or antennas that could point anywhere). This
        should handle accurately most spacecraft shapes. This model does not take cast shadows into account.
    
        The lift component of the drag force can be optionally considered. It should probably only be used for reentry
        computation, with much denser atmosphere than in regular orbit propagation. The lift component is computed using a ratio
        of molecules that experience specular reflection instead of diffuse reflection (absorption followed by outgassing at
        negligible velocity). Without lift (i.e. when the lift ratio is set to 0), drag force is along atmosphere relative
        velocity. With lift (i.e. when the lift ratio is set to any value between 0 and 1), the drag force depends on both
        relative velocity direction and panels normal orientation. For a single panel, if the relative velocity is head-on (i.e.
        aligned with the panel normal), the force will be in the same direction with and without lift, but the magnitude with
        lift ratio set to 1.0 will be twice the magnitude with lift ratio set to 0.0 (because atmosphere molecules bounces
        backward at same velocity in case of specular reflection).
    
        Each :class:`~org.orekit.forces.Panel` has its own set of radiation and drag coefficients. In orbit determination
        context, it would not be possible to estimate each panel individually, therefore
        :meth:`~org.orekit.forces.BoxAndSolarArraySpacecraft.getDragParametersDrivers` returns a single
        :class:`~org.orekit.utils.ParameterDriver` representing a
        :meth:`~org.orekit.forces.drag.DragSensitive.GLOBAL_DRAG_FACTOR` that applies to all panels drag coefficients and the
        :meth:`~org.orekit.forces.BoxAndSolarArraySpacecraft.getRadiationParametersDrivers` returns a single
        :class:`~org.orekit.utils.ParameterDriver` representing a
        :meth:`~org.orekit.forces.radiation.RadiationSensitive.GLOBAL_RADIATION_FACTOR` that applies to all panels radiation
        coefficients.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double4: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, list: java.util.List['Panel']): ...
    @staticmethod
    def buildBox(double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float) -> java.util.List['Panel']: ...
    @staticmethod
    def buildPanels(double: float, double2: float, double3: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double4: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double5: float, double6: float, double7: float, double8: float) -> java.util.List['Panel']: ...
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_dragAcceleration_0__T], t: _dragAcceleration_0__T, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], tArray: typing.List[_dragAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                :meth:`~org.orekit.forces.drag.DragSensitive.dragAcceleration` in
                interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                density (T): atmospheric density at spacecraft position
                relativeVelocity (:class:`~org.orekit.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to drag.
        
            The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
            Specified by:
                :meth:`~org.orekit.forces.drag.DragSensitive.dragAcceleration` in
                interface :class:`~org.orekit.forces.drag.DragSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                density (double): atmospheric density at spacecraft position
                relativeVelocity (:class:`~org.orekit.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPanels(self) -> java.util.List['Panel']: ...
    def getRadiationParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _radiationPressureAcceleration_0__T = typing.TypeVar('_radiationPressureAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def radiationPressureAcceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_radiationPressureAcceleration_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T], tArray: typing.List[_radiationPressureAcceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_radiationPressureAcceleration_0__T]:
        """
            Compute the acceleration due to radiation pressure.
        
            This method implements equation 8-44 from David A. Vallado's Fundamentals of Astrodynamics and Applications, third
            edition, 2007, Microcosm Press.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                flux (:class:`~org.orekit.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> flux): radiation flux in the same inertial frame as spacecraft orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def radiationPressureAcceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration due to radiation pressure.
        
            Specified by:
                :meth:`~org.orekit.forces.radiation.RadiationSensitive.radiationPressureAcceleration` in
                interface :class:`~org.orekit.forces.radiation.RadiationSensitive`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                flux (:class:`~org.orekit.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): radiation flux in the same inertial frame as spacecraft orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...

class ForceModel(org.orekit.utils.ParameterDriversProvider, org.orekit.propagation.events.EventDetectorsProvider):
    """
    public interface ForceModel extends :class:`~org.orekit.utils.ParameterDriversProvider`, :class:`~org.orekit.propagation.events.EventDetectorsProvider`
    
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
        their :meth:`~org.orekit.forces.ForceModel.getEventDetectors` method. This method is called once just before propagation
        starts. The events states will be checked by the propagator to ensure accurate propagation and proper events handling.
    """
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
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
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
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
        
            The default implementation simply adds the :meth:`~org.orekit.forces.ForceModel.acceleration` as a non-Keplerian
            acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                adder (:class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`): object where the contribution should be added
        
        """
        ...
    def dependsOnAttitudeRate(self) -> bool:
        """
            Check if force model depends on attitude's rotation rate or acceleration at a given, fixed date. If false, it
            essentially means that at most the attitude's rotation is used when computing the acceleration vector. The default
            implementation returns false as common forces do not.
        
            Returns:
                true if force model depends on attitude derivatives
        
            Since:
                12.1
        
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force model depends on position only at a given, fixed date.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
            Since:
                9.0
        
        
        """
        ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`,
            :meth:`~org.orekit.forces.ForceModel.acceleration` or :meth:`~org.orekit.forces.ForceModel.acceleration`
        
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
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`,
            :meth:`~org.orekit.forces.ForceModel.acceleration` or :meth:`~org.orekit.forces.ForceModel.acceleration`
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        """
        ...

class Panel:
    """
    public abstract class Panel extends :class:`~org.orekit.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class representing one panel of a satellite.
    
        Since:
            3.0
    
        Also see:
            :class:`~org.orekit.forces.FixedPanel`, :class:`~org.orekit.forces.PointingPanel`,
            :class:`~org.orekit.forces.SlewingPanel`
    """
    def getAbsorption(self) -> float:
        """
            Get radiation pressure absorption coefficient.
        
            Returns:
                radiation pressure absorption coefficient
        
        
        """
        ...
    def getArea(self) -> float:
        """
            Get panel area.
        
            Returns:
                panel area
        
        
        """
        ...
    def getDrag(self) -> float:
        """
            Get drag coefficient.
        
            Returns:
                drag coefficient
        
        
        """
        ...
    def getLiftRatio(self) -> float:
        """
            Get drag lift ratio.
        
            Returns:
                drag lift ratio
        
        
        """
        ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]: ...
    @typing.overload
    def getNormal(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get panel normal in spacecraft frame.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        public abstract <T extends :class:`~org.orekit.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> :class:`~org.orekit.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.FieldVector3D?is`<T> getNormal (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state)
        
            Get panel normal in spacecraft frame.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        
        """
        ...
    def getReflection(self) -> float:
        """
            Get radiation pressure specular reflection coefficient.
        
            Returns:
                radiation pressure specular reflection coefficient
        
        
        """
        ...
    def isDoubleSided(self) -> bool:
        """
            Check if the panel is double-sided (typically solar arrays).
        
            Returns:
                true if panel is double-sided
        
        
        """
        ...

class FixedPanel(Panel):
    """
    public class FixedPanel extends :class:`~org.orekit.forces.Panel`
    
        Class representing one panel of a satellite, fixed with respect to satellite body.
    
        It is mainly used to represent one facet of the body of the satellite.
    
        Since:
            3.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, boolean: bool, double2: float, double3: float, double4: float, double5: float): ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]:
        """
            Get panel normal in spacecraft frame.
        
            Specified by:
                :meth:`~org.orekit.forces.Panel.getNormal` in class :class:`~org.orekit.forces.Panel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        
        """
        ...
    @typing.overload
    def getNormal(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get panel normal in spacecraft frame.
        
            Specified by:
                :meth:`~org.orekit.forces.Panel.getNormal` in class :class:`~org.orekit.forces.Panel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        """
        ...

class PointingPanel(Panel):
    """
    public class PointingPanel extends :class:`~org.orekit.forces.Panel`
    
        Class representing one panel of a satellite, roughly pointing towards some target.
    
        It is mainly used to represent a rotating solar array that points towards the Sun.
    
        The panel rotation with respect to satellite body is the best pointing orientation achievable when the rotation axix is
        fixed by body attitude. Target is therefore always exactly in meridian plane defined by rotation axis and panel normal
        vector.
    
        These panels are considered to be always :meth:`~org.orekit.forces.Panel.isDoubleSided`.
    
        Since:
            3.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double: float, double2: float, double3: float, double4: float, double5: float): ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]:
        """
            Get panel normal in spacecraft frame.
        
            Specified by:
                :meth:`~org.orekit.forces.Panel.getNormal` in class :class:`~org.orekit.forces.Panel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        
        """
        ...
    @typing.overload
    def getNormal(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get panel normal in spacecraft frame.
        
            Specified by:
                :meth:`~org.orekit.forces.Panel.getNormal` in class :class:`~org.orekit.forces.Panel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        """
        ...

class PythonForceModel(ForceModel):
    """
    public class PythonForceModel extends :class:`~org.orekit.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.ForceModel`
    """
    def __init__(self): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
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
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    _addContribution_0__T = typing.TypeVar('_addContribution_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def addContribution(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_addContribution_0__T], fieldTimeDerivativesEquations: org.orekit.propagation.numerical.FieldTimeDerivativesEquations[_addContribution_0__T]) -> None:
        """
            Compute the contribution of the force model to the perturbing acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.addContribution` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                adder (:class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`<T> adder): object where the contribution should be added
        
        
        """
        ...
    @typing.overload
    def addContribution(self, spacecraftState: org.orekit.propagation.SpacecraftState, timeDerivativesEquations: org.orekit.propagation.numerical.TimeDerivativesEquations) -> None:
        """
            Compute the contribution of the force model to the perturbing acceleration.
        
            The default implementation simply adds the :meth:`~org.orekit.forces.ForceModel.acceleration` as a non-Keplerian
            acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.addContribution` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                adder (:class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`): object where the contribution should be added
        
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
    def finalize(self) -> None: ...
    def getParameterDriver(self, string: str) -> org.orekit.utils.ParameterDriver:
        """
            Get parameter value from its name.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameterDriver` in
                interface :class:`~org.orekit.utils.ParameterDriversProvider`
        
            Parameters:
                name (:class:`~org.orekit.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): parameter name
        
            Returns:
                parameter value
        
        
        """
        ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getParameters_3__T = typing.TypeVar('_getParameters_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getParameters_1__T]) -> typing.List[_getParameters_1__T]: ...
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get model parameters.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` in
                interface :class:`~org.orekit.utils.ParameterDriversProvider`
        
            Returns:
                model parameters, will throw an exception if one PDriver has several values driven. If it's the case (if at least 1
                PDriver of the model has several values driven) the method
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` must be used.
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_3__T]) -> typing.List[_getParameters_3__T]:
        """
            Get model parameters.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` in
                interface :class:`~org.orekit.utils.ParameterDriversProvider`
        
            Parameters:
                field (:class:`~org.orekit.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field to which the elements belong
        
            Returns:
                model parameters, will throw an exception if one PDriver of the has several values driven. If it's the case (if at least
                1 PDriver of the model has several values driven) the method
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParameters` must be used.
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`,
            :meth:`~org.orekit.forces.ForceModel.acceleration` or :meth:`~org.orekit.forces.ForceModel.acceleration`
        
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
        
            Supported parameters are those listed by :meth:`~org.orekit.utils.ParameterDriversProvider.getParametersDrivers`.
        
            Specified by:
                :meth:`~org.orekit.utils.ParameterDriversProvider.isSupported` in
                interface :class:`~org.orekit.utils.ParameterDriversProvider`
        
            Parameters:
                name (:class:`~org.orekit.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): parameter name to check
        
            Returns:
                true if the parameter is supported
        
            Also see:
                :meth:`~org.orekit.utils.ParameterDriversProvider.getParametersDrivers`
        
        
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

class SlewingPanel(Panel):
    """
    public class SlewingPanel extends :class:`~org.orekit.forces.Panel`
    
        Class representing one panel of a satellite, slewing about an axis at constant rate.
    
        It is mainly used to represent a solar array with fixed rate rotation.
    
        The panel rotation evolves linearly according to a start position and an angular rate (which can be set to 0 for
        non-rotating panels, which may occur in special modes or during contingencies).
    
        These panels are considered to be always :meth:`~org.orekit.forces.Panel.isDoubleSided`.
    
        Since:
            3.0
    """
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    _getNormal_0__T = typing.TypeVar('_getNormal_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNormal(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getNormal_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getNormal_0__T]:
        """
            Get panel normal in spacecraft frame.
        
            Specified by:
                :meth:`~org.orekit.forces.Panel.getNormal` in class :class:`~org.orekit.forces.Panel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        
        """
        ...
    @typing.overload
    def getNormal(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get panel normal in spacecraft frame.
        
            Specified by:
                :meth:`~org.orekit.forces.Panel.getNormal` in class :class:`~org.orekit.forces.Panel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current spacecraft state
        
            Returns:
                panel normal in spacecraft frame
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces")``.

    BoxAndSolarArraySpacecraft: typing.Type[BoxAndSolarArraySpacecraft]
    FixedPanel: typing.Type[FixedPanel]
    ForceModel: typing.Type[ForceModel]
    Panel: typing.Type[Panel]
    PointingPanel: typing.Type[PointingPanel]
    PythonForceModel: typing.Type[PythonForceModel]
    SlewingPanel: typing.Type[SlewingPanel]
    class-use: org.orekit.forces.class-use.__module_protocol__
    drag: org.orekit.forces.drag.__module_protocol__
    empirical: org.orekit.forces.empirical.__module_protocol__
    gravity: org.orekit.forces.gravity.__module_protocol__
    inertia: org.orekit.forces.inertia.__module_protocol__
    maneuvers: org.orekit.forces.maneuvers.__module_protocol__
    radiation: org.orekit.forces.radiation.__module_protocol__
