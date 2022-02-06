import org.orekit.forces.maneuvers
import org.orekit.forces.maneuvers.trigger
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.time
import typing



class Duration(org.orekit.propagation.AdditionalStateProvider):
    """
    public class Duration extends Object implements :class:`~org.orekit.propagation.AdditionalStateProvider`
    
        Generator for one column of a Jacobian matrix for special case of maneuver duration.
    
        Typical use cases for this are estimation of maneuver duration during either orbit determination or maneuver
        optimization.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.jacobians.MedianDate`, :class:`~org.orekit.forces.maneuvers.jacobians.TriggerDate`
    """
    def __init__(self, string: str, string2: str, string3: str): ...
    def getAdditionalState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
        """
            Get the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState`Â in
                interfaceÂ :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which additional state should correspond
        
            Returns:
                additional state corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getName`Â in
                interfaceÂ :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...

class MassDepletionDelay(org.orekit.propagation.integration.AdditionalDerivativesProvider):
    """
    public class MassDepletionDelay extends Object implements :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
    
        Generator for effect of delaying mass depletion when delaying a maneuver.
    
        Since:
            11.1
    """
    PREFIX: typing.ClassVar[str] = ...
    """
    public static final String PREFIX
    
        Prefix for state name.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, boolean: bool, maneuver: org.orekit.forces.maneuvers.Maneuver): ...
    def derivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
        """
            Compute the derivatives related to the additional state parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.derivatives`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                    :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.yield` method)
        
            Returns:
                computed derivatives
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the dimension of the generated column.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getDimension`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Returns:
                dimension of the generated column
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional derivatives (which will become state once integrated).
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getName`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the generator at the start of propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state information at the start of propagation
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation
        
        
        """
        ...

class MedianDate(org.orekit.propagation.AdditionalStateProvider):
    """
    public class MedianDate extends Object implements :class:`~org.orekit.propagation.AdditionalStateProvider`
    
        Generator for one column of a Jacobian matrix for special case of maneuver median date.
    
        Typical use cases for this are estimation of maneuver median date during either orbit determination or maneuver
        optimization.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.jacobians.Duration`, :class:`~org.orekit.forces.maneuvers.jacobians.TriggerDate`
    """
    def __init__(self, string: str, string2: str, string3: str): ...
    def getAdditionalState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
        """
            Get the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState`Â in
                interfaceÂ :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which additional state should correspond
        
            Returns:
                additional state corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getName`Â in
                interfaceÂ :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...

class TriggerDate(org.orekit.propagation.AdditionalStateProvider, org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter):
    """
    public class TriggerDate extends Object implements :class:`~org.orekit.propagation.AdditionalStateProvider`, :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`
    
        Generator for one column of a Jacobian matrix for special case of trigger dates.
    
        Typical use cases for this are estimation of maneuver start and stop date during either orbit determination or maneuver
        optimization.
    
        Let \((t_0, y_0)\) be the state at propagation start, \((t_1, y_1)\) be the state at maneuver trigger time, \((t_t,
        y_t)\) be the state at any arbitrary time \(t\) during propagation, and \(f_m(t, y)\) be the contribution of the
        maneuver to the global ODE \(\frac{dy}{dt} = f(t, y)\). We are interested in the Jacobian column \(\frac{\partial
        y_t}{\partial t_1}\).
    
        There are two parts in this Jacobian: the primary part corresponds to the full contribution of the acceleration due to
        the maneuver as it is delayed by a small amount \(dt_1\), whereas the secondary part corresponds to change of
        acceleration after maneuver start as the mass depletion is delayed and therefore the spacecraft mass is different from
        the mass for nominal start time.
    
        The primary part is computed as follows. After trigger time \(t_1\) (according to propagation direction),
        \[\frac{\partial y_t}{\partial t_1} = \pm \frac{\partial y_t}{\partial y_1} f_m(t_1, y_1)\] where the sign depends on
        \(t_1\) being a start or stop trigger and propagation being forward or backward.
    
        We don't have \(\frac{\partial y_t}{\partial y_1}\) available if \(t_1 \neq t_0\), but we have \(\frac{\partial
        y_t}{\partial y_0}\) at any time since it can be computed by integrating variational equations for numerical propagation
        or by other closed form expressions for analytical propagators. We use the classical composition rule to recover the
        state transition matrix with respect to intermediate time \(t_1\): \[\frac{\partial y_t}{\partial y_0} = \frac{\partial
        y_t}{\partial y_1} \frac{\partial y_1}{\partial y_0}\] We deduce \[\frac{\partial y_t}{\partial y_1} = \frac{\partial
        y_t}{\partial y_0} \left(\frac{\partial y_1}{\partial y_0}\right)^{-1}\]
    
        The contribution of the primary part to the Jacobian column can therefore be computed using the following closed-form
        expression: \[\frac{\partial y_t}{\partial t_1} = \pm \frac{\partial y_t}{\partial y_0} \left(\frac{\partial
        y_1}{\partial y_0}\right)^{-1} f_m(t_1, y_1) = \frac{\partial y_t}{\partial y_0} c_1\] where \(c_1\) is the signed
        contribution of maneuver at \(t_1\) and is computed at trigger time by solving \(\frac{\partial y_1}{\partial y_0} c_1 =
        \pm f_m(t_1, y_1)\).
    
        As the primary part of the column is generated using a closed-form expression, this generator implements the
        :class:`~org.orekit.propagation.AdditionalStateProvider` interface and stores the column directly in the primary state
        during propagation.
    
        As the closed-form expression requires picking \(c_1\) at trigger time \(t_1\), it works only if propagation starts
        outside of the maneuver and passes over \(t_1\) during integration.
    
        The secondary part is computed as follows. We have acceleration \(\vec{\Gamma} = \frac{\vec{F}}{m}\) and \(m = m_0 - q
        (t - t_s)\), where \(m\) is current mass, \(m_0\) is initial mass and \(t_s\) is maneuver trigger time. A delay \(dt_s\)
        on trigger time induces delaying mass depletion. We get: \[d\vec{\Gamma} = \frac{-\vec{F}}{m^2} dm =
        \frac{-\vec{F}}{m^2} q dt_s = -\vec{\Gamma}\frac{q}{m} dt_s\] From this total differential, we extract the partial
        derivative of the acceleration \[\frac{\partial\vec{\Gamma}}{\partial t_s} = -\vec{\Gamma}\frac{q}{m}\]
    
        The contribution of the secondary part to the Jacobian column can therefore be computed by integrating the partial
        derivative of the acceleration, to get the partial derivative of the position.
    
        As the secondary part of the column is generated using a differential equation, a separate underlying generator
        implementing the :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider` interface is set up to
        perform the integration during propagation.
    
        This generator takes care to sum up the primary and secondary parts so the full column of the Jacobian is computed.
    
        The implementation takes care to *not* resetting \(c_1\) at propagation start. This allows to get proper Jacobian if we
        interrupt propagation in the middle of a maneuver and restart propagation where it left.
    
        Since:
            11.1
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.jacobians.MedianDate`, :class:`~org.orekit.forces.maneuvers.jacobians.Duration`
    """
    def __init__(self, string: str, string2: str, boolean: bool, maneuver: org.orekit.forces.maneuvers.Maneuver, double: float): ...
    def getAdditionalState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
        """
            Get the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState`Â in
                interfaceÂ :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which additional state should correspond
        
            Returns:
                additional state corresponding to spacecraft state
        
        
        """
        ...
    def getMassDepletionDelay(self) -> MassDepletionDelay:
        """
            Get the mass depletion effect processor.
        
            Returns:
                mass depletion effect processor
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getName`Â in
                interfaceÂ :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialization method called at propagation start.
        
            The default implementation does nothing.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter.init`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial spacecraft state (at the start of propagation).
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    def maneuverTriggered(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> None:
        """
            Observe a maneuver trigger.
        
            The :code:`start` parameter corresponds to physical flow of time from past to future, not to propagation direction which
            can be backward. This means that during forward propagations, the first call will have :code:`start` set to :code:`true`
            and the second call will have :code:`start` set to :code:`false`, whereas in backward propagation, the first call will
            have :code:`start` set to :code:`false` and the second call will have :code:`start` set to :code:`true`.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter.maneuverTriggered`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at trigger date (before applying the maneuver)
                start (boolean): if true, the trigger is the start of the maneuver
        
        
        """
        ...
    def resetState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Reset state as a maneuver triggers.
        
            Specified by:
                :meth:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter.resetState`Â in
                interfaceÂ :class:`~org.orekit.forces.maneuvers.trigger.ManeuverTriggersResetter`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at trigger date
        
            Returns:
                reset state taking into account maneuver start/stop
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.maneuvers.jacobians")``.

    Duration: typing.Type[Duration]
    MassDepletionDelay: typing.Type[MassDepletionDelay]
    MedianDate: typing.Type[MedianDate]
    TriggerDate: typing.Type[TriggerDate]
