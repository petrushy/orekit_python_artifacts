
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.forces
import org.orekit.forces.maneuvers
import org.orekit.forces.maneuvers.trigger
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.time
import typing



class Duration(org.orekit.propagation.AdditionalDataProvider[typing.MutableSequence[float]]):
    """
    Generator for one column of a Jacobian matrix for special case of maneuver duration.
    
    Typical use cases for this are estimation of maneuver duration during either orbit determination or maneuver optimization.
    
    Since:
        11.1
    
    Also see:
        MedianDate, TriggerDate
    """
    def __init__(self, startName: str, stopName: str, columnName: str):
        """
        Simple constructor.
        
        Parameters:
            startName (String): name of the parameter corresponding to the start date
            stopName (String): name of the parameter corresponding to the stop date
            columnName (String): name of the parameter corresponding to the column
        
        
        """
        ...
    def getAdditionalData(self, state: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]:
        """
        Get the additional data.
        
        Specified by: getAdditionalData in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): spacecraft state to which additional data should correspond
        
        Returns:
            additional state corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Specified by: getName in interface AdditionalDataProvider
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def yields(self, state: org.orekit.propagation.SpacecraftState) -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional data being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final SpacecraftState state) {
             return !state.hasAdditionalData("STM");
         }
         
        
        The default implementation returns false, meaning that state data can be getAdditionalData immediately.
        
        The column state can be computed only if the start and stop dates columns are available.
        
        Specified by: yields in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

class MassDepletionDelay(org.orekit.propagation.integration.AdditionalDerivativesProvider):
    """
    Generator for effect of delaying mass depletion when delaying a maneuver, when the mass itself is not included in the transition matrix. It neglects the influence of mass in other force models e.g. drag. For more accurate derivatives, one should use the full 7x7 state transition matrix instead.
    
    Since:
        11.1
    """
    PREFIX: typing.ClassVar[str] = ...
    """
    Prefix for state name.
    
    Also see:
        constant
    
    
    """
    def __init__(self, triggerName: str, manageStart: bool, maneuver: org.orekit.forces.maneuvers.Maneuver, *nonGravitationalForces: org.orekit.forces.ForceModel):
        """
        Constructor.
        
        The generated additional state and derivatives will be named by prepending the PREFIX to the name of the date trigger parameter.
        
        Parameters:
            triggerName (String): name of the date trigger parameter
            manageStart (boolean): if true, we compute derivatives with respect to maneuver start
            maneuver (Maneuver): maneuver that is delayed
            nonGravitationalForces (ForceModel...): list of non-gravitational forces, used only if mass is not in STM. They are assumed to be inversely depending on mass.
        
        
        """
        ...
    def combinedDerivatives(self, state: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.integration.CombinedDerivatives:
        """
        Compute the derivatives related to the additional state (and optionally main state increments).
        
        Specified by: combinedDerivatives in interface AdditionalDerivativesProvider
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the generated column.
        
        Specified by: getDimension in interface AdditionalDerivativesProvider
        
        Returns:
            dimension of the generated column
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional derivatives (which will become state once integrated).
        
        Specified by: getName in interface AdditionalDerivativesProvider
        
        Returns:
            name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the generator at the start of propagation.
        
        Specified by: init in interface AdditionalDerivativesProvider
        
        Parameters:
            initialState (SpacecraftState): initial state information at the start of propagation
            target (AbsoluteDate): date of propagation
        
        
        """
        ...

class MedianDate(org.orekit.propagation.AdditionalDataProvider[typing.MutableSequence[float]]):
    """
    Generator for one column of a Jacobian matrix for special case of maneuver median date.
    
    Typical use cases for this are estimation of maneuver median date during either orbit determination or maneuver optimization.
    
    Since:
        11.1
    
    Also see:
        Duration, TriggerDate
    """
    def __init__(self, startName: str, stopName: str, columnName: str):
        """
        Simple constructor.
        
        Parameters:
            startName (String): name of the parameter corresponding to the start date
            stopName (String): name of the parameter corresponding to the stop date
            columnName (String): name of the parameter corresponding to the column
        
        
        """
        ...
    def getAdditionalData(self, state: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]:
        """
        Get the additional data.
        
        Specified by: getAdditionalData in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): spacecraft state to which additional data should correspond
        
        Returns:
            additional state corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Specified by: getName in interface AdditionalDataProvider
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def yields(self, state: org.orekit.propagation.SpacecraftState) -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional data being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final SpacecraftState state) {
             return !state.hasAdditionalData("STM");
         }
         
        
        The default implementation returns false, meaning that state data can be getAdditionalData immediately.
        
        The column state can be computed only if the start and stop dates columns are available.
        
        Specified by: yields in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

class TriggerDate(org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter, org.orekit.propagation.AdditionalDataProvider[typing.MutableSequence[float]]):
    """
    Generator for one column of a Jacobian matrix for special case of trigger dates.
    
    Typical use cases for this are estimation of maneuver start and stop date during either orbit determination or maneuver optimization.
    
    Let \((t_0, y_0)\) be the state at propagation start, \((t_1, y_1)\) be the state at maneuver trigger time, \((t_t, y_t)\) be the state at any arbitrary time \(t\) during propagation, and \(f_m(t, y)\) be the contribution of the maneuver to the global ODE \(\frac{dy}{dt} = f(t, y)\). We are interested in the Jacobian column \(\frac{\partial y_t}{\partial t_1}\).
    
    There are two parts in this Jacobian: the primary part corresponds to the full contribution of the jump in the dynamics due to the maneuver as it is delayed by a small amount \(dt_1\), whereas the secondary part corresponds to change of acceleration after maneuver start as the mass depletion is delayed and therefore the spacecraft mass is different from the mass for nominal start time. This second part is already contained in the first one when the mass is included in the transition matrix (7x7 instead of 6x6).
    
    The primary part is computed as follows. After trigger time \(t_1\) (according to propagation direction), \[\frac{\partial y_t}{\partial t_1} = \pm \frac{\partial y_t}{\partial y_1} f_m(t_1, y_1)\] where the sign depends on \(t_1\) being a start or stop trigger and propagation being forward or backward.
    
    We don't have \(\frac{\partial y_t}{\partial y_1}\) available if \(t_1 \neq t_0\), but we have \(\frac{\partial y_t}{\partial y_0}\) at any time since it can be computed by integrating variational equations for numerical propagation or by other closed form expressions for analytical propagators. We use the classical composition rule to recover the state transition matrix with respect to intermediate time \(t_1\): \[\frac{\partial y_t}{\partial y_0} = \frac{\partial y_t}{\partial y_1} \frac{\partial y_1}{\partial y_0}\] We deduce \[\frac{\partial y_t}{\partial y_1} = \frac{\partial y_t}{\partial y_0} \left(\frac{\partial y_1}{\partial y_0}\right)^{-1}\]
    
    The contribution of the primary part to the Jacobian column can therefore be computed using the following closed-form expression: \[\frac{\partial y_t}{\partial t_1} = \pm \frac{\partial y_t}{\partial y_0} \left(\frac{\partial y_1}{\partial y_0}\right)^{-1} f_m(t_1, y_1) = \frac{\partial y_t}{\partial y_0} c_1\] where \(c_1\) is the signed contribution of maneuver at \(t_1\) and is computed at trigger time by solving \(\frac{\partial y_1}{\partial y_0} c_1 = \pm f_m(t_1, y_1)\).
    
    As the primary part of the column is generated using a closed-form expression, this generator implements the AdditionalDataProvider interface and stores the column directly in the primary state during propagation.
    
    As the closed-form expression requires picking \(c_1\) at trigger time \(t_1\), it works only if propagation starts outside of the maneuver and passes over \(t_1\) during integration.
    
    The secondary part, if needed (as it is not required if the mass is already included the state transition matrix i.e. when the latter is 7x7), is computed as follows. Let m be the mass and m_s its value at switching time t_s. Let (x,y,z) be the position vector, (vx, vy, vz) the velocity and (ax, ay, az) the total acceleration, we have \(\dot \frac{\partial x} {\partial \partial m_s} = \frac{\partial vx }{\partial m_s})) and similar expressions for y and z. Furthermore, \(\dot \frac{\partial vx}{ \partial \partial m_s} = \frac{\partial ax }{\partial m} . \frac{\partial m }{\partial m_s} \), and symmetric equations for vy and vy. The fact is that \( \frac{\partial m}{ \partial m_s} = 1 \) assuming the mass rate q only depends on time. On the other hand, \( \frac{\partial m_s}{ \partial t_s }= q(t_s) \)/ By the chain rule of derivation, one gets the contribution due to the mass depletion delay.
    
    The contribution of the secondary part to the Jacobian column can therefore be computed by integrating the partial derivative of the acceleration, to get the partial derivative of the position.
    
    As the secondary part of the column is generated using a differential equation, a separate underlying generator implementing the AdditionalDerivativesProvider interface is set up to perform the integration during propagation.
    
    This generator takes care to sum up the primary and secondary parts so the full column of the Jacobian is computed.
    
    The implementation takes care to not resetting \(c_1\) at propagation start. This allows to get proper Jacobian if we interrupt propagation in the middle of a maneuver and restart propagation where it left.
    
    Since:
        11.1
    
    Also see:
        MedianDate, Duration
    """
    @typing.overload
    def __init__(self, stmName: str, triggerName: str, manageStart: bool, maneuver: org.orekit.forces.maneuvers.Maneuver, threshold: float, isMassInStm: bool, *nonGravitationalForces: org.orekit.forces.ForceModel): ...
    @typing.overload
    def __init__(self, stmName: str, triggerName: str, manageStart: bool, maneuver: org.orekit.forces.maneuvers.Maneuver, threshold: float, *nonGravitationalForces: org.orekit.forces.ForceModel): ...
    def getAdditionalData(self, state: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]:
        """
        Get the additional data.
        
        Specified by: getAdditionalData in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): spacecraft state to which additional data should correspond
        
        Returns:
            additional state corresponding to spacecraft state
        
        
        """
        ...
    def getMassDepletionDelay(self) -> MassDepletionDelay:
        """
        Get the mass depletion effect processor. Can be null.
        
        Returns:
            mass depletion effect processor
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Specified by: getName in interface AdditionalDataProvider
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialization method called at propagation start.
        
        The default implementation does nothing.
        
        Specified by: init in interface AdditionalDataProvider
        
        Specified by: init in interface ManeuverTriggersResetter
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state (at the start of propagation).
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...
    def maneuverTriggered(self, state: org.orekit.propagation.SpacecraftState, start: bool) -> None:
        """
        Observe a maneuver trigger.
        
        The start parameter corresponds to physical flow of time from past to future, not to propagation direction which can be backward. This means that during forward propagations, the first call will have start set to true and the second call will have start set to false, whereas in backward propagation, the first call will have start set to false and the second call will have start set to true.
        
        Specified by: maneuverTriggered in interface ManeuverTriggersResetter
        
        Parameters:
            state (SpacecraftState): spacecraft state at trigger date (before applying the maneuver)
            start (boolean): if true, the trigger is the start of the maneuver
        
        
        """
        ...
    def resetState(self, state: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Reset state as a maneuver triggers.
        
        Specified by: resetState in interface ManeuverTriggersResetter
        
        Parameters:
            state (SpacecraftState): spacecraft state at trigger date
        
        Returns:
            reset state taking into account maneuver start/stop
        
        
        """
        ...
    def yields(self, state: org.orekit.propagation.SpacecraftState) -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional data being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final SpacecraftState state) {
             return !state.hasAdditionalData("STM");
         }
         
        
        The default implementation returns false, meaning that state data can be getAdditionalData immediately.
        
        The column state can be computed only if the State Transition Matrix state is available.
        
        Specified by: yields in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers.jacobians")``.

    Duration: typing.Type[Duration]
    MassDepletionDelay: typing.Type[MassDepletionDelay]
    MedianDate: typing.Type[MedianDate]
    TriggerDate: typing.Type[TriggerDate]
