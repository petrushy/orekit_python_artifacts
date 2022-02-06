import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.forces
import org.orekit.forces.maneuvers.jacobians
import org.orekit.forces.maneuvers.propulsion
import org.orekit.forces.maneuvers.trigger
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.events
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



_ImpulseManeuver__T = typing.TypeVar('_ImpulseManeuver__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
class ImpulseManeuver(org.orekit.propagation.events.AbstractDetector['ImpulseManeuver'[_ImpulseManeuver__T]], typing.Generic[_ImpulseManeuver__T]):
    """
    public class ImpulseManeuver<T extends :class:`~org.orekit.propagation.events.EventDetector`> extends :class:`~org.orekit.propagation.events.AbstractDetector`<:class:`~org.orekit.forces.maneuvers.ImpulseManeuver`<T>>
    
        Impulse maneuver model.
    
        This class implements an impulse maneuver as a discrete event that can be provided to any
        :class:`~org.orekit.propagation.Propagator`.
    
        The maneuver is triggered when an underlying event generates a null event, in which case this class will generate a null
        event (the stop event from the underlying object is therefore filtered out). In the simple cases, the underlying event
        detector may be a basic :class:`~org.orekit.propagation.events.DateDetector`, but it can also be a more elaborate
        :class:`~org.orekit.propagation.events.ApsideDetector` for apogee maneuvers for example.
    
        The maneuver is defined by a single velocity increment. If no AttitudeProvider is given, the current attitude of the
        spacecraft, defined by the current spacecraft state, will be used as the :class:`~org.orekit.attitudes.AttitudeProvider`
        so the velocity increment should be given in the same pseudoinertial frame as the
        :class:`~org.orekit.propagation.SpacecraftState` used to construct the propagator that will handle the maneuver. If an
        AttitudeProvider is given, the velocity increment given should be defined appropriately in consideration of that
        provider. So, a typical case for tangential maneuvers is to provide a :class:`~org.orekit.attitudes.LofOffset` attitude
        provider along with a velocity increment defined in accordance with that LOF aligned attitude provider; e.g. if the LOF
        aligned attitude provider was constructed using LOFType.VNC the velocity increment should be provided in VNC
        coordinates.
    
        Beware that the triggering event detector must behave properly both before and after maneuver. If for example a node
        detector is used to trigger an inclination maneuver and the maneuver change the orbit to an equatorial one, the node
        detector will fail just after the maneuver, being unable to find a node on an equatorial orbit! This is a real case that
        has been encountered during validation ...
    
        Also see:
            :meth:`~org.orekit.propagation.Propagator.addEventDetector`
    """
    @typing.overload
    def __init__(self, t: _ImpulseManeuver__T, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    @typing.overload
    def __init__(self, t: _ImpulseManeuver__T, attitudeProvider: org.orekit.attitudes.AttitudeProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Compute the value of the switching function. This function must be continuous (at least in its roots neighborhood), as
            the integrator will need to find its roots to locate the events.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.g`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.EventDetector`
        
            Specified by:
                :meth:`~org.orekit.propagation.events.AbstractDetector.g`Â in
                classÂ :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): the current state information: date, kinematics, attitude
        
            Returns:
                value of the switching function
        
        
        """
        ...
    def getAttitudeOverride(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get the Attitude Provider to use during maneuver.
        
            Returns:
                the attitude provider
        
        
        """
        ...
    def getDeltaVSat(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the velocity increment in satellite frame.
        
            Returns:
                velocity increment in satellite frame
        
        
        """
        ...
    def getIsp(self) -> float:
        """
            Get the specific impulse.
        
            Returns:
                specific impulse
        
        
        """
        ...
    def getTrigger(self) -> _ImpulseManeuver__T:
        """
            Get the triggering event.
        
            Returns:
                triggering event
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize event handler at the start of a propagation.
        
            This method is called once at the start of the propagation. It may be used by the event handler to initialize some
            internal data if needed.
        
            The default implementation does nothing
        
            This implementation sets the direction of propagation and initializes the event handler. If a subclass overrides this
            method it should call :code:`super.init(s0, t)`.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.events.EventDetector`
        
            Overrides:
                :meth:`~org.orekit.propagation.events.AbstractDetector.init`Â in
                classÂ :class:`~org.orekit.propagation.events.AbstractDetector`
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                t (:class:`~org.orekit.time.AbsoluteDate`): target time for the integration
        
        
        """
        ...

class Maneuver(org.orekit.forces.AbstractForceModel):
    """
    public class Maneuver extends :class:`~org.orekit.forces.AbstractForceModel`
    
        A generic model for maneuvers. It contains: - An attitude override, this is the attitude used during the maneuver, it
        can be different than the one used for propagation; - A maneuver triggers object from the trigger sub-package. It
        defines the triggers used to start and stop the maneuvers (dates or events for example). - A propulsion model from
        sub-package propulsion. It defines the thrust or ÃŽâ€�V, isp, flow rate etc.. Both the propulsion model and the maneuver
        triggers can contain parameter drivers (for estimation). The convention here is that the propulsion model drivers are
        given before the maneuver triggers when calling the method
        :meth:`~org.orekit.forces.maneuvers.Maneuver.getParametersDrivers`
    
        Since:
            10.2
    """
    def __init__(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider, maneuverTriggers: org.orekit.forces.maneuvers.trigger.ManeuverTriggers, propulsionModel: org.orekit.forces.maneuvers.propulsion.PropulsionModel): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Description copied from interface: 
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
            Description copied from interface: 
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
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
        
        
        """
        ...
    def getAttitudeOverride(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get the attitude override used for the maneuver.
        
            Returns:
                the attitude override
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getManeuverTriggers(self) -> org.orekit.forces.maneuvers.trigger.ManeuverTriggers:
        """
            Get the maneuver triggers.
        
            Returns:
                the maneuver triggers
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the maneuver. The name can be in the propulsion model, in the maneuver triggers or both. If it is in
            both it should be the same since it refers to the same maneuver. The name is inferred from the propulsion model first,
            then from the maneuver triggers if the propulsion model had an empty name.
        
            Returns:
                the name
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPropulsionModel(self) -> org.orekit.forces.maneuvers.propulsion.PropulsionModel:
        """
            Get the propulsion model.
        
            Returns:
                the propulsion model
        
        
        """
        ...
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

class SmallManeuverAnalyticalModel(org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect):
    """
    public class SmallManeuverAnalyticalModel extends Object implements :class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`
    
        Analytical model for small maneuvers.
    
        The aim of this model is to compute quickly the effect at date tÃ¢â€šï¿½ of a small maneuver performed at an earlier
        date tÃ¢â€šâ‚¬. Both the direct effect of the maneuver and the Jacobian of this effect with respect to maneuver
        parameters are available.
    
        These effect are computed analytically using two Jacobian matrices:
    
          1.  JÃ¢â€šâ‚¬: Jacobian of Keplerian or equinoctial elements with respect to Cartesian parameters at date tÃ¢â€šâ‚¬ allows
            to compute maneuver effect as a change in orbital elements at maneuver date tÃ¢â€šâ‚¬,
          2.  J :sub:`1/0` : Jacobian of Keplerian or equinoctial elements at date tÃ¢â€šï¿½ with respect to Keplerian or equinoctial
            elements at date tÃ¢â€šâ‚¬ allows to propagate the change in orbital elements to final date tÃ¢â€šï¿½.
    
    
        The second Jacobian, J :sub:`1/0` , is computed using a simple Keplerian model, i.e. it is the identity except for the
        mean motion row which also includes an off-diagonal element due to semi-major axis change.
    
        The orbital elements change at date tÃ¢â€šï¿½ can be added to orbital elements extracted from state, and the final
        elements taking account the changes are then converted back to appropriate type, which may be different from Keplerian
        or equinoctial elements.
    
        Note that this model takes *only* Keplerian effects into account. This means that using only this class to compute an
        inclination maneuver in Low Earth Orbit will *not* change ascending node drift rate despite inclination has changed (the
        same would be true for a semi-major axis change of course). In order to take this drift into account, an instance of
        :class:`~org.orekit.propagation.analytical.J2DifferentialEffect` must be used together with an instance of this class.
    """
    @typing.overload
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    @typing.overload
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    @typing.overload
    def apply(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Compute the effect of the maneuver on an orbit.
        
            Parameters:
                orbit1 (:class:`~org.orekit.orbits.Orbit`): original orbit at tâ‚�, without maneuver
        
            Returns:
                orbit at tâ‚�, taking the maneuver into account if tâ‚� > tâ‚€
        
            Also see:
                :meth:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel.apply`, null
        
            Compute the effect of the maneuver on a spacecraft state.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect.apply`Â in
                interfaceÂ :class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`
        
            Parameters:
                state1 (:class:`~org.orekit.propagation.SpacecraftState`): original spacecraft state at tâ‚�, without maneuver
        
            Returns:
                spacecraft state at tâ‚�, taking the maneuver into account if tâ‚� > tâ‚€
        
            Also see:
                :meth:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel.apply`, null
        
        
        """
        ...
    @typing.overload
    def apply(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the maneuver.
        
            Returns:
                date of the maneuver
        
        
        """
        ...
    def getInertialDV(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the inertial velocity increment of the maneuver.
        
            Returns:
                velocity increment in a state-dependent inertial frame
        
            Also see:
                :meth:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel.getInertialFrame`
        
        
        """
        ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
            Get the inertial frame in which the velocity increment is defined.
        
            Returns:
                inertial frame in which the velocity increment is defined
        
            Also see:
                :meth:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel.getInertialDV`
        
        
        """
        ...
    def getJacobian(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Compute the Jacobian of the orbit with respect to maneuver parameters.
        
            The Jacobian matrix is a 6x4 matrix. Element jacobian[i][j] corresponds to the partial derivative of orbital parameter i
            with respect to maneuver parameter j. The rows order is the same order as used in null method. Columns (0, 1, 2)
            correspond to the velocity increment coordinates (ÃŽâ€�V :sub:`x` , ÃŽâ€�V :sub:`y` , ÃŽâ€�V :sub:`z` ) in the inertial
            frame returned by :meth:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel.getInertialFrame`, and column 3
            corresponds to the maneuver date tÃ¢â€šâ‚¬.
        
            Parameters:
                orbit1 (:class:`~org.orekit.orbits.Orbit`): original orbit at tâ‚�, without maneuver
                positionAngle (:class:`~org.orekit.orbits.PositionAngle`): type of the position angle to use
                jacobian (double[][]): placeholder 6x4 (or larger) matrix to be filled with the Jacobian, if matrix is larger than 6x4, only the 6x4 upper left
                    corner will be modified
        
            Also see:
                :meth:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel.apply`
        
        
        """
        ...
    def updateMass(self, double: float) -> float:
        """
            Update a spacecraft mass due to maneuver.
        
            Parameters:
                mass (double): masse before maneuver
        
            Returns:
                mass after maneuver
        
        
        """
        ...

class ConfigurableLowThrustManeuver(Maneuver):
    """
    public class ConfigurableLowThrustManeuver extends :class:`~org.orekit.forces.maneuvers.Maneuver`
    
        This class implements a configurable low thrust maneuver.
    
        The maneuver is composed of succession of a burn interval. Burn intervals are defined by two detectors. See
        :class:`~org.orekit.forces.maneuvers.trigger.EventBasedManeuverTriggers` for more details on the detectors. The attitude
        and the thrust direction are provided by an instance of ThrustDirectionProvider See
        :class:`~org.orekit.forces.maneuvers.propulsion.ThrustDirectionAndAttitudeProvider` for more details on thrust direction
        and attitude.
    
        Since:
            10.2
    """
    @typing.overload
    def __init__(self, thrustDirectionAndAttitudeProvider: org.orekit.forces.maneuvers.propulsion.ThrustDirectionAndAttitudeProvider, maneuverTriggers: org.orekit.forces.maneuvers.trigger.ManeuverTriggers, double: float, double2: float): ...
    @typing.overload
    def __init__(self, thrustDirectionAndAttitudeProvider: org.orekit.forces.maneuvers.propulsion.ThrustDirectionAndAttitudeProvider, abstractDetector: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector], abstractDetector2: org.orekit.propagation.events.AbstractDetector[org.orekit.propagation.events.EventDetector], double: float, double2: float): ...
    def getISP(self) -> float:
        """
            Get the specific impulse.
        
            Returns:
                specific impulse (s).
        
        
        """
        ...
    def getThrust(self) -> float:
        """
            Get the thrust.
        
            Returns:
                thrust force (N).
        
        
        """
        ...
    def getThrustDirectionProvider(self) -> org.orekit.forces.maneuvers.propulsion.ThrustDirectionAndAttitudeProvider:
        """
            Getter on Thrust direction and spaceraft attitude provided by an external object.
        
            Returns:
                internal field
        
        
        """
        ...

class ConstantThrustManeuver(Maneuver):
    """
    public class ConstantThrustManeuver extends :class:`~org.orekit.forces.maneuvers.Maneuver`
    
        This class implements a simple maneuver with constant thrust.
    
        The maneuver is defined by a direction in satellite frame. The current attitude of the spacecraft, defined by the
        current spacecraft state, will be used to compute the thrust direction in inertial frame. A typical case for tangential
        maneuvers is to use a :class:`~org.orekit.attitudes.LofOffset` attitude provider for state propagation and a velocity
        increment along the +X satellite axis.
    """
    @typing.overload
    def __init__(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider, dateBasedManeuverTriggers: org.orekit.forces.maneuvers.trigger.DateBasedManeuverTriggers, abstractConstantThrustPropulsionModel: org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, string: str): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider, abstractConstantThrustPropulsionModel: org.orekit.forces.maneuvers.propulsion.AbstractConstantThrustPropulsionModel): ...
    def getDirection(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the direction.
        
            Returns:
                the direction
        
            Since:
                9.2
        
        
        """
        ...
    def getDuration(self) -> float:
        """
            Get the duration of the maneuver (s). duration = endDate - startDate
        
            Returns:
                the duration of the maneuver (s)
        
            Since:
                9.2
        
        
        """
        ...
    def getEndDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end date.
        
            Returns:
                the end date
        
            Since:
                9.2
        
        
        """
        ...
    def getFlowRate(self) -> float:
        """
            Get the flow rate.
        
            Returns:
                flow rate (negative, kg/s).
        
        
        """
        ...
    def getISP(self) -> float:
        """
            Get the specific impulse.
        
            Returns:
                specific impulse (s).
        
        
        """
        ...
    def getStartDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start date.
        
            Returns:
                the start date
        
            Since:
                9.2
        
        
        """
        ...
    def getThrust(self) -> float:
        """
            Get the thrust.
        
            Returns:
                thrust force (N).
        
        
        """
        ...
    def getThrustVector(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the thrust vector (N) in S/C frame.
        
            Returns:
                thrust vector (N) in S/C frame.
        
        
        """
        ...
    _isFiring_0__T = typing.TypeVar('_isFiring_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def isFiring(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_isFiring_0__T]) -> bool:
        """
            Check if maneuvering is on.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state
        
            Returns:
                true if maneuver is on at this state
        
            Since:
                10.1
        
        """
        ...
    @typing.overload
    def isFiring(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> bool:
        """
            Check if maneuvering is on.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state
        
            Returns:
                true if maneuver is on at this state
        
            Since:
                10.1
        
            Check if maneuvering is on.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
        
            Returns:
                true if maneuver is on at this date
        
            Since:
                10.1
        
        
        """
        ...
    @typing.overload
    def isFiring(self, absoluteDate: org.orekit.time.AbsoluteDate) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers")``.

    ConfigurableLowThrustManeuver: typing.Type[ConfigurableLowThrustManeuver]
    ConstantThrustManeuver: typing.Type[ConstantThrustManeuver]
    ImpulseManeuver: typing.Type[ImpulseManeuver]
    Maneuver: typing.Type[Maneuver]
    SmallManeuverAnalyticalModel: typing.Type[SmallManeuverAnalyticalModel]
    jacobians: org.orekit.forces.maneuvers.jacobians.__module_protocol__
    propulsion: org.orekit.forces.maneuvers.propulsion.__module_protocol__
    trigger: org.orekit.forces.maneuvers.trigger.__module_protocol__
