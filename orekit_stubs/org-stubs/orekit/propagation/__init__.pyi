import java.io
import java.lang
import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.analysis.polynomials
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation.analytical
import org.orekit.propagation.class-use
import org.orekit.propagation.conversion
import org.orekit.propagation.events
import org.orekit.propagation.integration
import org.orekit.propagation.numerical
import org.orekit.propagation.sampling
import org.orekit.propagation.semianalytical
import org.orekit.time
import org.orekit.utils
import typing



class AbstractStateCovarianceInterpolator(org.orekit.time.AbstractTimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, 'StateCovariance']]):
    """
    public abstract class AbstractStateCovarianceInterpolator extends :class:`~org.orekit.time.AbstractTimeInterpolator`<:class:`~org.orekit.time.TimeStampedPair`<:class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.propagation.StateCovariance`>>
    
        Abstract class for orbit and state covariance interpolator.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`, :class:`~org.orekit.propagation.StateCovariance`,
            :class:`~org.orekit.time.TimeStampedPair`
    """
    DEFAULT_POSITION_ANGLE: typing.ClassVar[org.orekit.orbits.PositionAngleType] = ...
    """
    public static final :class:`~org.orekit.orbits.PositionAngleType` DEFAULT_POSITION_ANGLE
    
        Default position angle for covariance expressed in Cartesian elements.
    
    """
    COLUMN_DIM: typing.ClassVar[int] = ...
    """
    public static final int COLUMN_DIM
    
        Default column dimension for position-velocity state covariance.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROW_DIM: typing.ClassVar[int] = ...
    """
    public static final int ROW_DIM
    
        Default row dimension for position-velocity state covariance.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], lOFType: org.orekit.frames.LOFType): ...
    def getOrbitInterpolator(self) -> org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit]: ...
    def getOutFrame(self) -> org.orekit.frames.Frame:
        """
            Get output frame.
        
            Returns:
                output frame. Can be null.
        
        
        """
        ...
    def getOutLOF(self) -> org.orekit.frames.LOFType:
        """
            Get output local orbital frame.
        
            Returns:
                output local orbital frame. Can be null.
        
        
        """
        ...
    def getOutOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get output orbit type.
        
            Returns:
                output orbit type.
        
        
        """
        ...
    def getOutPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get output position angle type.
        
            Returns:
                output position angle.
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeStamped], typing.Sequence[org.orekit.time.TimeStamped]]) -> org.orekit.time.TimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.TimeStamped]) -> org.orekit.time.TimeStamped: ...
    @typing.overload
    def interpolate(self, abstractTimeInterpolator: org.orekit.time.AbstractTimeInterpolator.InterpolationData) -> org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, 'StateCovariance']: ...

class AdditionalStateProvider:
    """
    public interface AdditionalStateProvider
    
        This interface allows to modify :class:`~org.orekit.propagation.SpacecraftState` and set up additional state data.
    
        :class:`~org.orekit.propagation.Propagator` generate :class:`~org.orekit.propagation.SpacecraftState` that contain at
        least orbit, attitude, and mass. These states may however also contain
        :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalState`. Instances of classes implementing this interface are
        intended to be registered to propagators so they can either modify the basic components (orbit, attitude and mass) or
        add additional states incrementally after having computed the basic components.
    
        Some additional states may depend on previous additional states to be already available the before they can be computed.
        It may even be impossible to compute some of these additional states at some time if they depend on conditions that are
        fulfilled only after propagation as started or some event has occurred. As the propagator builds the complete state
        incrementally, looping over the registered providers, it must call their
        :meth:`~org.orekit.propagation.AdditionalStateProvider.update` methods in an order that fulfill these dependencies that
        may be time-dependent and are not related to the order in which the providers are registered to the propagator. This
        reordering is performed each time the complete state is built, using a yield mechanism. The propagator first pushes all
        providers in a stack and then empty the stack, one provider at a time, taking care to select only providers that do
        *not* :meth:`~org.orekit.propagation.AdditionalStateProvider.yields` when asked. Consider for example a case where
        providers A, B and C have been registered and provider B needs in fact the additional state generated by provider C.
        Then when a complete state is built, the propagator puts the three providers in a new stack, and then starts the
        incremental generation of additional states. It first checks provider A which does not yield so it is popped from the
        stack and the additional state it generates is added. Then provider B is checked, but it yields because state from
        provider C is not yet available. So propagator checks provider C which does not yield, so it is popped out of the stack
        and applied. At this stage, provider B is the only remaining one in the stack, so it is checked again, but this time it
        does not yield because the state from provider C is available as it has just been added, so provider B is popped from
        the stack and applied. The stack is now empty and the propagator can return the completed state.
    
        It is possible that at some stages in the propagation, a subset of the providers registered to a propagator all yield
        and cannot :meth:`~org.orekit.propagation.AdditionalStateProvider.update` the state. This happens for example during the
        initialization phase of a propagator that computes State Transition Matrices or Jacobian matrices. These features are
        managed as secondary equations in the ODE integrator, and initialized after the primary equations (which correspond to
        orbit) have been initialized. So when the primary equation are initialized, the providers that depend on the secondary
        state will all yield. This behavior is expected. Another case occurs when users set up additional states that induce a
        dependency loop (state A depending on state B which depends on state C which depends on state A). In this case, the
        three corresponding providers will wait for each other and indefinitely yield. This second case is a deadlock and
        results from a design error of the additional states management at application level. The propagator cannot know it in
        advance if a subset of providers that all yield is normal or not. So at propagator level, when either situation is
        detected, the propagator just gives up and returns the most complete state it was able to compute, without generating
        any error. Errors will indeed not be triggered in the first case (once the primary equations have been initialized, the
        secondary equations will be initialized too), and they will be triggered in the second case as soon as user attempts to
        retrieve an additional state that was not added.
    
        Also see:
            :class:`~org.orekit.propagation.Propagator`, :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`,
            :class:`~org.orekit.propagation.AbstractStateModifier`
    """
    def getAdditionalState(self, spacecraftState: 'SpacecraftState') -> typing.List[float]:
        """
            Get the additional state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which additional state should correspond
        
            Returns:
                additional state corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new state, it should
            return the empty string as its name.
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, spacecraftState: 'SpacecraftState', absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the additional state provider at the start of propagation.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state information at the start of propagation
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation
        
            Since:
                11.2
        
        
        """
        ...
    def update(self, spacecraftState: 'SpacecraftState') -> 'SpacecraftState':
        """
            Update a state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to update
        
            Returns:
                updated state
        
            Since:
                12.1
        
        
        """
        ...
    def yields(self, spacecraftState: 'SpacecraftState') -> bool:
        """
            Check if this provider should yield so another provider has an opportunity to add missing parts.
        
            Decision to yield is often based on an additional state being
            :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState` in the provided :code:`state` (but it could
            theoretically also depend on an additional state derivative being
            :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalStateDerivative`, or any other criterion). If for example a
            provider needs the state transition matrix, it could implement this method as:
        
            .. code-block: java
            
             public boolean yields(final SpacecraftState state) {
                 return !state.getAdditionalStates().containsKey("STM");
             }
             
        
            The default implementation returns :code:`false`, meaning that state data can be
            :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState` immediately.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state to handle
        
            Returns:
                true if this provider should yield so another provider has an opportunity to add missing parts as the state is
                incrementally built up
        
            Since:
                11.1
        
        
        """
        ...

class EphemerisGenerator:
    """
    public interface EphemerisGenerator
    
        Generator for ephemerides.
    
        This interface is mainly implemented by nested classes within propagators. These classes monitor the ongoing propagation
        and stores in memory all the necessary data. Once the initial propagation has completed, the data stored allows them to
        build an :class:`~org.orekit.propagation.BoundedPropagator` that can be used to rerun the propagation (perhaps with
        different event detectors and step handlers) without doing the full computation.
    
        Analytical propagators will mainly store only the start and stop date and the model itself, so ephemeris will just call
        the model back. Integration-based propagators will mainly store the
        :class:`~org.orekit.propagation.sampling.OrekitStepInterpolator` at each step so the ephemeris can select the proper
        interpolator and evaluate it for any date covered by the initial propagation.
    
        Since:
            11.0
    """
    def getGeneratedEphemeris(self) -> 'BoundedPropagator':
        """
            Get the ephemeris generated during the propagation.
        
            Returns:
                generated ephemeris
        
        
        """
        ...

_FieldAdditionalStateProvider__T = typing.TypeVar('_FieldAdditionalStateProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdditionalStateProvider(typing.Generic[_FieldAdditionalStateProvider__T]):
    """
    public interface FieldAdditionalStateProvider<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        This interface allows to modify :class:`~org.orekit.propagation.FieldSpacecraftState` and set up additional state data.
    
        :class:`~org.orekit.propagation.FieldPropagator` generate :class:`~org.orekit.propagation.FieldSpacecraftState` that
        contain at least orbit, attitude, and mass. These states may however also contain
        :meth:`~org.orekit.propagation.FieldSpacecraftState.addAdditionalState`. Instances of classes implementing this
        interface are intended to be registered to propagators so they can either modify the basic components (orbit, attitude
        and mass) or add additional states incrementally after having computed the basic components.
    
        Some additional states may depend on previous additional states to be already available the before they can be computed.
        It may even be impossible to compute some of these additional states at some time if they depend on conditions that are
        fulfilled only after propagation as started or some event has occurred. As the propagator builds the complete state
        incrementally, looping over the registered providers, it must call their
        :meth:`~org.orekit.propagation.FieldAdditionalStateProvider.update` methods in an order that fulfill these dependencies
        that may be time-dependent and are not related to the order in which the providers are registered to the propagator.
        This reordering is performed each time the complete state is built, using a yield mechanism. The propagator first pushes
        all providers in a stack and then empty the stack, one provider at a time, taking care to select only providers that do
        *not* :meth:`~org.orekit.propagation.FieldAdditionalStateProvider.yields` when asked. Consider for example a case where
        providers A, B and C have been registered and provider B needs in fact the additional state generated by provider C.
        Then when a complete state is built, the propagator puts the three providers in a new stack, and then starts the
        incremental generation of additional states. It first checks provider A which does not yield so it is popped from the
        stack and the additional state it generates is added. Then provider B is checked, but it yields because state from
        provider C is not yet available. So propagator checks provider C which does not yield, so it is popped out of the stack
        and applied. At this stage, provider B is the only remaining one in the stack, so it is checked again, but this time it
        does not yield because the state from provider C is available as it has just been added, so provider B is popped from
        the stack and applied. The stack is now empty and the propagator can return the completed state.
    
        It is possible that at some stages in the propagation, a subset of the providers registered to a propagator all yield
        and cannot :meth:`~org.orekit.propagation.FieldAdditionalStateProvider.update` the state. This happens for example
        during the initialization phase of a propagator that computes State Transition Matrices or Jacobian matrices. These
        features are managed as secondary equations in the ODE integrator, and initialized after the primary equations (which
        correspond to orbit) have been initialized. So when the primary equation are initialized, the providers that depend on
        the secondary state will all yield. This behavior is expected. Another case occurs when users set up additional states
        that induce a dependency loop (state A depending on state B which depends on state C which depends on state A). In this
        case, the three corresponding providers will wait for each other and indefinitely yield. This second case is a deadlock
        and results from a design error of the additional states management at application level. The propagator cannot know it
        in advance if a subset of providers that all yield is normal or not. So at propagator level, when either situation is
        detected, the propagator just gives up and returns the most complete state it was able to compute, without generating
        any error. Errors will indeed not be triggered in the first case (once the primary equations have been initialized, the
        secondary equations will be initialized too), and they will be triggered in the second case as soon as user attempts to
        retrieve an additional state that was not added.
    
        Also see:
            :class:`~org.orekit.propagation.FieldPropagator`,
            :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider`,
            :class:`~org.orekit.propagation.FieldAbstractStateModifier`
    """
    def getAdditionalState(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldAdditionalStateProvider__T]) -> typing.List[_FieldAdditionalStateProvider__T]: ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new state, it should
            return the empty string as its name.
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldAdditionalStateProvider__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAdditionalStateProvider__T]) -> None: ...
    def update(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldAdditionalStateProvider__T]) -> 'FieldSpacecraftState'[_FieldAdditionalStateProvider__T]: ...
    def yields(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldAdditionalStateProvider__T]) -> bool: ...

_FieldEphemerisGenerator__T = typing.TypeVar('_FieldEphemerisGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEphemerisGenerator(typing.Generic[_FieldEphemerisGenerator__T]):
    """
    public interface FieldEphemerisGenerator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        Generator for ephemerides.
    
        This interface is mainly implemented by nested classes within propagators. These classes monitor the ongoing propagation
        and stores in memory all the necessary data. Once the initial propagation has completed, the data stored allows them to
        build an :class:`~org.orekit.propagation.FieldBoundedPropagator` that can be used to rerun the propagation (perhaps with
        different event detectors and step handlers) without doing the full computation.
    
        Analytical propagators will mainly store only the start and stop date and the model itself, so ephemeris will just call
        the model back. Integration-based propagators will mainly store the
        :class:`~org.orekit.propagation.sampling.FieldOrekitStepInterpolator` at each step so the ephemeris can select the
        proper interpolator and evaluate it for any date covered by the initial propagation.
    
        Since:
            11.0
    """
    def getGeneratedEphemeris(self) -> 'FieldBoundedPropagator'[_FieldEphemerisGenerator__T]: ...

_FieldPropagator__T = typing.TypeVar('_FieldPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPropagator(org.orekit.utils.FieldPVCoordinatesProvider[_FieldPropagator__T], typing.Generic[_FieldPropagator__T]):
    """
    public interface FieldPropagator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T>
    
        This interface provides a way to propagate an orbit at any time.
    
        This interface is the top-level abstraction for orbit propagation. It only allows propagation to a predefined date. It
        is implemented by analytical models which have no time limit, by orbit readers based on external data files, by
        numerical integrators using rich force models and by continuous models built after numerical integration has been
        completed and dense output data as been gathered.
    """
    DEFAULT_MASS: typing.ClassVar[float] = ...
    """
    static final double DEFAULT_MASS
    
        Default mass.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def addAdditionalStateProvider(self, fieldAdditionalStateProvider: FieldAdditionalStateProvider[_FieldPropagator__T]) -> None: ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, d: _addEventDetector__D) -> None: ...
    def clearEventsDetectors(self) -> None:
        """
            Remove all events detectors.
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`,
                :meth:`~org.orekit.propagation.FieldPropagator.getEventsDetectors`
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
            Remove all step handlers.
        
            This convenience method is equivalent to call :code:`getMultiplexer().clear()`
        
            Since:
                11.0
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.getMultiplexer`,
                :meth:`~org.orekit.propagation.sampling.FieldStepHandlerMultiplexer.clear`
        
        
        """
        ...
    def getAdditionalStateProviders(self) -> java.util.List[FieldAdditionalStateProvider[_FieldPropagator__T]]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Returns:
                attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_FieldPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_FieldPropagator__T]]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> 'FieldSpacecraftState'[_FieldPropagator__T]: ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_FieldPropagator__T]: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldPropagator__T]: ...
    def getPosition(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPropagator__T]: ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which an :class:`~org.orekit.propagation.FieldAdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.FieldPropagator.addAdditionalStateProvider` method. If the propagator is an
            :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`, the states for which a set of
            :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addAdditionalDerivativesProvider` method
            are also counted as managed additional states.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.FieldPropagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.resetState` method is called at an event
            occurrence and happens to change the unmanaged additional state.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T]) -> 'FieldSpacecraftState'[_FieldPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T]) -> 'FieldSpacecraftState'[_FieldPropagator__T]: ...
    def resetInitialState(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldPropagator__T]) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    @typing.overload
    def setStepHandler(self, t: _FieldPropagator__T, fieldOrekitFixedStepHandler: org.orekit.propagation.sampling.FieldOrekitFixedStepHandler[_FieldPropagator__T]) -> None: ...
    @typing.overload
    def setStepHandler(self, fieldOrekitStepHandler: org.orekit.propagation.sampling.FieldOrekitStepHandler[_FieldPropagator__T]) -> None: ...

_FieldSpacecraftState__T = typing.TypeVar('_FieldSpacecraftState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSpacecraftState(org.orekit.time.FieldTimeStamped[_FieldSpacecraftState__T], org.orekit.time.FieldTimeShiftable['FieldSpacecraftState'[_FieldSpacecraftState__T], _FieldSpacecraftState__T], typing.Generic[_FieldSpacecraftState__T]):
    """
    public class FieldSpacecraftState<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.FieldTimeStamped`<T>, :class:`~org.orekit.time.FieldTimeShiftable`<:class:`~org.orekit.propagation.FieldSpacecraftState`<T>, T>
    
        This class is the representation of a complete state holding orbit, attitude and mass information at a given date, meant
        primarily for propagation.
    
        It contains an :class:`~org.orekit.orbits.FieldOrbit`, or a :class:`~org.orekit.utils.FieldAbsolutePVCoordinates` if
        there is no definite central body, plus the current mass and attitude at the intrinsic
        :class:`~org.orekit.time.FieldAbsoluteDate`. Quantities are guaranteed to be consistent in terms of date and reference
        frame. The spacecraft state may also contain additional states, which are simply named double arrays which can hold any
        user-defined data.
    
        The state can be slightly shifted to close dates. This actual shift varies between
        :class:`~org.orekit.orbits.FieldOrbit` and :class:`~org.orekit.utils.FieldAbsolutePVCoordinates`. For attitude it is a
        linear extrapolation taking the spin rate into account and no mass change. It is *not* intended as a replacement for
        proper orbit and attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
        The instance :code:`FieldSpacecraftState` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`, :class:`~org.orekit.propagation.SpacecraftState`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSpacecraftState__T], spacecraftState: 'SpacecraftState'): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T], fieldArrayDictionary2: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T], fieldArrayDictionary2: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    def addAdditionalState(self, string: str, tArray: typing.List[_FieldSpacecraftState__T]) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]: ...
    def addAdditionalStateDerivative(self, string: str, tArray: typing.List[_FieldSpacecraftState__T]) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]: ...
    def ensureCompatibleAdditionalStates(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldSpacecraftState__T]) -> None: ...
    def getA(self) -> _FieldSpacecraftState__T:
        """
            Get the semi-major axis.
        
            Returns:
                semi-major axis (m), or {code Double.NaN} if the state contains an absolute position-velocity-acceleration rather than
                an orbit
        
        
        """
        ...
    def getAbsPVA(self) -> org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T]: ...
    def getAdditionalState(self, string: str) -> typing.List[_FieldSpacecraftState__T]:
        """
            Get an additional state.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                value of the additional state
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.hasAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalStatesValues`
        
        
        """
        ...
    def getAdditionalStateDerivative(self, string: str) -> typing.List[_FieldSpacecraftState__T]:
        """
            Get an additional state derivative.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state derivative
        
            Returns:
                value of the additional state derivative
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.addAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.hasAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalStatesDerivatives`
        
        
        """
        ...
    def getAdditionalStatesDerivatives(self) -> org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]: ...
    def getAdditionalStatesValues(self) -> org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]: ...
    def getAttitude(self) -> org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftState__T]: ...
    def getE(self) -> _FieldSpacecraftState__T:
        """
            Get the eccentricity.
        
            Returns:
                eccentricity, or {code Double.NaN} if the state contains an absolute position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getEquinoctialEx`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getEquinoctialEy`
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldSpacecraftState__T:
        """
            Get the first component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e cos(ω + Ω), first component of eccentricity vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getE`
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldSpacecraftState__T:
        """
            Get the second component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e sin(ω + Ω), second component of the eccentricity vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getE`
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the defining frame.
        
            Returns:
                the frame in which state is defined
        
        
        """
        ...
    def getHx(self) -> _FieldSpacecraftState__T:
        """
            Get the first component of the inclination vector (as per equinoctial parameters).
        
            Returns:
                tan(i/2) cos(Ω), first component of the inclination vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getI`
        
        
        """
        ...
    def getHy(self) -> _FieldSpacecraftState__T:
        """
            Get the second component of the inclination vector (as per equinoctial parameters).
        
            Returns:
                tan(i/2) sin(Ω), second component of the inclination vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getI`
        
        
        """
        ...
    def getI(self) -> _FieldSpacecraftState__T:
        """
            Get the inclination.
        
            Returns:
                inclination (rad)
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getHx`, :meth:`~org.orekit.propagation.FieldSpacecraftState.getHy`
        
        
        """
        ...
    def getKeplerianMeanMotion(self) -> _FieldSpacecraftState__T:
        """
            Get the Keplerian mean motion.
        
            The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian mean motion in radians per second, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
        
        """
        ...
    def getKeplerianPeriod(self) -> _FieldSpacecraftState__T:
        """
            Get the Keplerian period.
        
            The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian period in seconds, or {code Double.NaN} if the state contains an absolute position-velocity-acceleration
                rather than an orbit
        
        
        """
        ...
    def getLE(self) -> _FieldSpacecraftState__T:
        """
            Get the eccentric latitude argument (as per equinoctial parameters).
        
            Returns:
                E + ω + Ω eccentric longitude argument (rad), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getLv`, :meth:`~org.orekit.propagation.FieldSpacecraftState.getLM`
        
        
        """
        ...
    def getLM(self) -> _FieldSpacecraftState__T:
        """
            Get the mean longitude argument (as per equinoctial parameters).
        
            Returns:
                M + ω + Ω mean latitude argument (rad), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getLv`, :meth:`~org.orekit.propagation.FieldSpacecraftState.getLE`
        
        
        """
        ...
    def getLv(self) -> _FieldSpacecraftState__T:
        """
            Get the true latitude argument (as per equinoctial parameters).
        
            Returns:
                v + ω + Ω true longitude argument (rad), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getLE`, :meth:`~org.orekit.propagation.FieldSpacecraftState.getLM`
        
        
        """
        ...
    def getMass(self) -> _FieldSpacecraftState__T:
        """
            Gets the current mass.
        
            Returns:
                the mass (kg)
        
        
        """
        ...
    def getMu(self) -> _FieldSpacecraftState__T:
        """
            Get the central attraction coefficient.
        
            Returns:
                mu central attraction coefficient (m^3/s^2), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
        
        """
        ...
    def getOrbit(self) -> org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPosition(self, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldSpacecraftState__T]: ...
    def hasAdditionalState(self, string: str) -> bool:
        """
            Check if an additional state is available.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is available
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalStatesValues`
        
        
        """
        ...
    def hasAdditionalStateDerivative(self, string: str) -> bool:
        """
            Check if an additional state derivative is available.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state derivative
        
            Returns:
                true if the additional state derivative is available
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.addAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalStatesDerivatives`
        
        
        """
        ...
    def isOrbitDefined(self) -> bool:
        """
            Check if the state contains an orbit part.
        
            A state contains either an :class:`~org.orekit.utils.FieldAbsolutePVCoordinates` or an
            :class:`~org.orekit.orbits.FieldOrbit`.
        
            Returns:
                true if state contains an orbit (in which case :meth:`~org.orekit.propagation.FieldSpacecraftState.getOrbit` will not
                throw an exception), or false if the state contains an absolut position-velocity-acceleration (in which case
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAbsPVA` will not throw an exception)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldSpacecraftState__T) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]: ...
    def toSpacecraftState(self) -> 'SpacecraftState':
        """
            To convert a FieldSpacecraftState instance into a SpacecraftState instance.
        
            Returns:
                SpacecraftState instance with the same properties
        
        
        """
        ...
    def toStaticTransform(self) -> org.orekit.frames.FieldStaticTransform[_FieldSpacecraftState__T]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def toTransform(self) -> org.orekit.frames.FieldTransform[_FieldSpacecraftState__T]: ...

_FieldSpacecraftStateInterpolator__KK = typing.TypeVar('_FieldSpacecraftStateInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldSpacecraftStateInterpolator(org.orekit.time.AbstractFieldTimeInterpolator[FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], typing.Generic[_FieldSpacecraftStateInterpolator__KK]):
    """
    public class FieldSpacecraftStateInterpolator<KK extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<KK>> extends :class:`~org.orekit.time.AbstractFieldTimeInterpolator`<:class:`~org.orekit.propagation.FieldSpacecraftState`<KK>, KK>
    
        Generic class for spacecraft state interpolator.
    
        The user can specify what interpolator to use for each attribute of the spacecraft state. However, at least one
        interpolator for either orbit or absolute position-velocity-acceleration is needed. All the other interpolators can be
        left to null if the user do not want to interpolate these values.
    
        Also see:
            :class:`~org.orekit.propagation.SpacecraftState`
    """
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, fieldTimeInterpolator: org.orekit.time.FieldTimeInterpolator[org.orekit.orbits.FieldOrbit[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator2: org.orekit.time.FieldTimeInterpolator[org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator3: org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator4: org.orekit.time.FieldTimeInterpolator[org.orekit.attitudes.FieldAttitude[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator5: org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, fieldTimeInterpolator: org.orekit.time.FieldTimeInterpolator[org.orekit.orbits.FieldOrbit[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator2: org.orekit.time.FieldTimeInterpolator[org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator3: org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator4: org.orekit.time.FieldTimeInterpolator[org.orekit.attitudes.FieldAttitude[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], fieldTimeInterpolator5: org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]): ...
    def getAbsPVAInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]: ...
    def getAdditionalStateInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]: ...
    def getAttitudeInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.attitudes.FieldAttitude[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]: ...
    def getMassInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]: ...
    def getOrbitInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.orbits.FieldOrbit[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]: ...
    def getOutputFrame(self) -> org.orekit.frames.Frame:
        """
            Get output frame.
        
            Returns:
                output frame
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[org.orekit.time.FieldTimeInterpolator[org.orekit.time.FieldTimeStamped[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.FieldTimeStamped], typing.Sequence[org.orekit.time.FieldTimeStamped]]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftStateInterpolator__KK], collection: typing.Union[java.util.Collection[FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK]], typing.Sequence[FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK]]]) -> FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK]: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftStateInterpolator__KK], stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...

_FieldStateCovariance__T = typing.TypeVar('_FieldStateCovariance__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStateCovariance(org.orekit.time.FieldTimeStamped[_FieldStateCovariance__T], typing.Generic[_FieldStateCovariance__T]):
    """
    public class FieldStateCovariance<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.FieldTimeStamped`<T>
    
        This class is the representation of a covariance matrix at a given date.
    
        Currently, the covariance only represents the orbital elements.
    
        It is possible to change the covariance frame by using the
        :meth:`~org.orekit.propagation.FieldStateCovariance.changeCovarianceFrame` or
        :meth:`~org.orekit.propagation.FieldStateCovariance.changeCovarianceFrame` method. These methods are based on Equations
        (18) and (20) of *Covariance Transformations for Satellite Flight Dynamics Operations* by David A. SVallado.
    
        Finally, covariance orbit type can be changed using the
        :meth:`~org.orekit.propagation.FieldStateCovariance.changeCovarianceType` method.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, fieldMatrix: org.hipparchus.linear.FieldMatrix[_FieldStateCovariance__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStateCovariance__T], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, fieldMatrix: org.hipparchus.linear.FieldMatrix[_FieldStateCovariance__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStateCovariance__T], lOF: org.orekit.frames.LOF): ...
    @typing.overload
    def changeCovarianceFrame(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldStateCovariance__T], frame: org.orekit.frames.Frame) -> 'FieldStateCovariance'[_FieldStateCovariance__T]: ...
    @typing.overload
    def changeCovarianceFrame(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldStateCovariance__T], lOF: org.orekit.frames.LOF) -> 'FieldStateCovariance'[_FieldStateCovariance__T]: ...
    def changeCovarianceType(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldStateCovariance__T], orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> 'FieldStateCovariance'[_FieldStateCovariance__T]: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldStateCovariance__T]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the covariance frame.
        
            Returns:
                the covariance frame (can be null)
        
            Also see:
                :meth:`~org.orekit.propagation.FieldStateCovariance.getLOF`
        
        
        """
        ...
    def getLOF(self) -> org.orekit.frames.LOF:
        """
            Get the covariance LOF type.
        
            Returns:
                the covariance LOF type (can be null)
        
            Also see:
                :meth:`~org.orekit.propagation.FieldStateCovariance.getFrame`
        
        
        """
        ...
    def getMatrix(self) -> org.hipparchus.linear.FieldMatrix[_FieldStateCovariance__T]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the covariance orbit type.
        
            Returns:
                the covariance orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get the covariance angle type.
        
            Returns:
                the covariance angle type
        
        
        """
        ...
    def shiftedBy(self, field: org.hipparchus.Field[_FieldStateCovariance__T], fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldStateCovariance__T], t: _FieldStateCovariance__T) -> 'FieldStateCovariance'[_FieldStateCovariance__T]: ...
    def toStateCovariance(self) -> 'StateCovariance':
        """
            Get new state covariance instance.
        
            Returns:
                new state covariance instance.
        
        
        """
        ...

class MatricesHarvester:
    """
    public interface MatricesHarvester
    
        Interface for extracting State Transition Matrices and Jacobians matrices from
        :class:`~org.orekit.propagation.SpacecraftState`.
    
        The State Transition Matrix and Jacobians matrices with respect to propagation parameters are stored in the state as
        :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`. Each propagator and support classes have their own
        way to handle them. The interface leverages these differences which are implementation details and provides a higher
        level access to these matrices, regardless of how they were computed and stored.
    
        Since:
            11.1
    """
    def getJacobiansColumnsNames(self) -> java.util.List[str]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type used for the matrix computation.
        
            Returns:
                the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, spacecraftState: 'SpacecraftState') -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian with respect to propagation parameters.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get the position angle used for the matrix computation.
        
            Irrelevant if :meth:`~org.orekit.propagation.MatricesHarvester.getOrbitType` returns
            :meth:`~org.orekit.orbits.OrbitType.CARTESIAN`.
        
            Returns:
                the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, spacecraftState: 'SpacecraftState') -> org.hipparchus.linear.RealMatrix:
        """
            Extract state transition matrix from state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
                :class:`~org.orekit.orbits.OrbitType`.
        
        
        """
        ...
    def setReferenceState(self, spacecraftState: 'SpacecraftState') -> None:
        """
            Set up reference state.
        
            This method is called whenever the global propagation reference state changes. This corresponds to the start of
            propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering.
            Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute
            analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not
            use it at all.
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): reference state to set
        
        
        """
        ...

class PropagationType(java.lang.Enum['PropagationType']):
    """
    public enum PropagationType extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.propagation.PropagationType`>
    
        Enumerate to define the propagation type used by the propagator.
    
        This enumerate can also be used to define if the orbital state is defined with osculating or mean elements at the
        propagator initialization.
    """
    MEAN: typing.ClassVar['PropagationType'] = ...
    OSCULATING: typing.ClassVar['PropagationType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PropagationType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['PropagationType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PropagationType c : PropagationType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Propagator(org.orekit.utils.PVCoordinatesProvider):
    """
    public interface Propagator extends :class:`~org.orekit.utils.PVCoordinatesProvider`
    
        This interface provides a way to propagate an orbit at any time.
    
        This interface is the top-level abstraction for orbit propagation. It only allows propagation to a predefined date. It
        is implemented by analytical models which have no time limit, by orbit readers based on external data files, by
        numerical integrators using rich force models and by continuous models built after numerical integration has been
        completed and dense output data as been gathered.
    
        Note that one single propagator cannot be called from multiple threads. Its configuration can be changed as there is at
        least a :meth:`~org.orekit.propagation.Propagator.resetInitialState` method, and even propagators that do not support
        resetting state (like the :class:`~org.orekit.propagation.analytical.tle.TLEPropagator` do cache some internal data
        during computation. However, as long as they are configured with independent building blocks (mainly event handlers and
        step handlers that may preserve some internal state), and as long as they are called from one thread only, they *can* be
        used in multi-threaded applications. Synchronizing several propagators to run in parallel is also possible using
        :class:`~org.orekit.propagation.PropagatorsParallelizer`.
    """
    DEFAULT_MASS: typing.ClassVar[float] = ...
    """
    static final double DEFAULT_MASS
    
        Default mass.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def addAdditionalStateProvider(self, additionalStateProvider: AdditionalStateProvider) -> None:
        """
            Add a set of user-specified state parameters to be computed along with the orbit propagation.
        
            Parameters:
                additionalStateProvider (:class:`~org.orekit.propagation.AdditionalStateProvider`): provider for additional state
        
        
        """
        ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, t: _addEventDetector__T) -> None:
        """
            Add an event detector.
        
            Parameters:
                detector (T): event detector to add
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.clearEventsDetectors`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
            Remove all events detectors.
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.addEventDetector`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
            Remove all step handlers.
        
            This convenience method is equivalent to call :code:`getMultiplexer().clear()`
        
            Since:
                11.0
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.getMultiplexer`,
                :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.clear`
        
        
        """
        ...
    def getAdditionalStateProviders(self) -> java.util.List[AdditionalStateProvider]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Returns:
                attitude provider
        
        
        """
        ...
    @staticmethod
    def getDefaultLaw(frames: org.orekit.frames.Frames) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get a default law using the given frames.
        
            Parameters:
                frames (:class:`~org.orekit.frames.Frames`): the set of frames to use.
        
            Returns:
                attitude law.
        
        
        """
        ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
            Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
            This generator can be used when the user needs fast random access to the orbit state at any time between the initial and
            target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and
            backward inside the propagation range before finding their result even if the propagator used is integration-based and
            only goes from one initial time to one target time.
        
            Beware that when used with integration-based propagators, the generator will store **all** intermediate results. It is
            therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with
            analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to
            call it back as needed, so it is less memory intensive.
        
            The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call
            to either :meth:`~org.orekit.propagation.Propagator.propagate` or :meth:`~org.orekit.propagation.Propagator.propagate`
            is called. The proper way to use this method is therefore to do:
        
            .. code-block: java
            
               EphemerisGenerator generator = propagator.getEphemerisGenerator();
               propagator.propagate(target);
               BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
             
        
            Returns:
                ephemeris generator
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> 'SpacecraftState':
        """
            Get the propagator initial state.
        
            Returns:
                initial state
        
        
        """
        ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer:
        """
            Get the multiplexer holding all step handlers.
        
            Returns:
                multiplexer holding all step handlers
        
            Since:
                11.0
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates` in
                interface :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPosition` in
                interface :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                position of the body (m and)
        
        
        """
        ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which a :class:`~org.orekit.propagation.AdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` method.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.Propagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` method is called at an event occurrence
            and happens to change the unmanaged additional state.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'SpacecraftState':
        """
            Propagate towards a target date.
        
            Simple propagators use only the target date as the specification for computing the propagated state. More feature rich
            propagators can consider other information and provide different operating modes or G-stop facilities to stop at
            pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
            Parameters:
                target (:class:`~org.orekit.time.AbsoluteDate`): target date towards which orbit state should be propagated
        
            Returns:
                propagated state
        
            Propagate from a start date towards a target date.
        
            Those propagators use a start date and a target date to compute the propagated state. For propagators using event
            detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is
            performed, without processing any event computation. Then complete propagation is performed from start date to target
            date.
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start date from which orbit state should be propagated
                target (:class:`~org.orekit.time.AbsoluteDate`): target date to which orbit state should be propagated
        
            Returns:
                propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> 'SpacecraftState': ...
    def resetInitialState(self, spacecraftState: 'SpacecraftState') -> None:
        """
            Reset the propagator initial state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    @typing.overload
    def setStepHandler(self, double: float, orekitFixedStepHandler: typing.Union[org.orekit.propagation.sampling.OrekitFixedStepHandler, typing.Callable]) -> None:
        """
            Set a single handler for fixed stepsizes.
        
            This convenience method is equivalent to call :code:`getMultiplexer().clear()` followed by
            :code:`getMultiplexer().add(h, handler)`
        
            Parameters:
                h (double): fixed stepsize (s)
                handler (:class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`): handler called at the end of each finalized step
        
            Since:
                11.0
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.getMultiplexer`,
                :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.add`
        
        """
        ...
    @typing.overload
    def setStepHandler(self, orekitStepHandler: org.orekit.propagation.sampling.OrekitStepHandler) -> None:
        """
            Set a single handler for variable stepsizes.
        
            This convenience method is equivalent to call :code:`getMultiplexer().clear()` followed by
            :code:`getMultiplexer().add(handler)`
        
            Parameters:
                handler (:class:`~org.orekit.propagation.sampling.OrekitStepHandler`): handler called at the end of each finalized step
        
            Since:
                11.0
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.getMultiplexer`,
                :meth:`~org.orekit.propagation.sampling.StepHandlerMultiplexer.add`
        
        
        """
        ...
    def setupMatricesComputation(self, string: str, realMatrix: org.hipparchus.linear.RealMatrix, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary) -> MatricesHarvester:
        """
            Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
            If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that
            will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
            The arguments for initial matrices *must* be compatible with the :class:`~org.orekit.orbits.OrbitType` and
            :class:`~org.orekit.orbits.PositionAngleType` that will be used by the propagator.
        
            The default implementation throws an exception as the method is not supported by all propagators.
        
            Parameters:
                stmName (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): State Transition Matrix state name
                initialStm (:class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.linear.RealMatrix?is`): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
                initialJacobianColumns (:class:`~org.orekit.utils.DoubleArrayDictionary`): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                    from the dictionary, the corresponding initial column is assumed to be 0
        
            Returns:
                harvester to retrieve computed matrices during and after propagation
        
            Since:
                11.1
        
        
        """
        ...

class PropagatorsParallelizer:
    """
    public class PropagatorsParallelizer extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class provides a way to propagate simultaneously several orbits.
    
        Multi-satellites propagation is based on multi-threading. Therefore, care must be taken so that all propagators can be
        run in a multi-thread context. This implies that all propagators are built independently and that they rely on force
        models that are also built independently. An obvious mistake would be to reuse a maneuver force model, as these models
        need to cache the firing/not-firing status. Objects used by force models like atmosphere models for drag force or others
        may also cache intermediate variables, so separate instances for each propagator must be set up.
    
        This class *will* create new threads for running the propagators. It adds a new
        :class:`~org.orekit.propagation.sampling.MultiSatStepHandler` to manage the steps all at once, in addition to the
        existing individual step handlers that are preserved.
    
        All propagators remain independent of each other (they don't even know they are managed by the parallelizer) and advance
        their simulation time following their own algorithm. The parallelizer will block them at the end of each step and allow
        them to continue in order to maintain synchronization. The :class:`~org.orekit.propagation.sampling.MultiSatStepHandler`
        will experience perfectly synchronized steps, but some propagators may already be slightly ahead of time as depicted in
        the following rendering; were simulation times flows from left to right:
    
        .. code-block: java
        
            propagator 1   : -------------[++++current step++++]>
                                          |
            propagator 2   : ----[++++current step++++]--------->
                                          |           |
            ...                           |           |
            propagator n   : ---------[++++current step++++]---->
                                          |           |
                                          V           V
            global handler : -------------[global step]--------->
         
    
        The previous sketch shows that propagator 1 has already computed states up to the end of the propagation, but
        propagators 2 up to n are still late. The global step seen by the handler will be the common part between all
        propagators steps. Once this global step has been handled, the parallelizer will let the more late propagator (here
        propagator 2) to go one step further and a new global step will be computed and handled, until all propagators reach the
        end.
    
        This class does *not* provide multi-satellite events. As events may truncate steps and even reset state, all events
        (including multi-satellite events) are handled at a very low level within each propagators and cannot be managed from
        outside by the parallelizer. For accurate handling of multi-satellite events, the event detector should be registered
        *within* the propagator of one satellite and have access to an independent propagator (typically an analytical
        propagator or an ephemeris) of the other satellite. As the embedded propagator will be called by the detector which
        itself is called by the first propagator, it should really be a dedicated propagator and should not also appear as one
        of the parallelized propagators, otherwise conflicts will appear here.
    
        Since:
            9.0
    """
    @typing.overload
    def __init__(self, list: java.util.List[Propagator], double: float, multiSatFixedStepHandler: org.orekit.propagation.sampling.MultiSatFixedStepHandler): ...
    @typing.overload
    def __init__(self, list: java.util.List[Propagator], multiSatStepHandler: org.orekit.propagation.sampling.MultiSatStepHandler): ...
    def getPropagators(self) -> java.util.List[Propagator]: ...
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> java.util.List['SpacecraftState']: ...

class SpacecraftState(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['SpacecraftState'], java.io.Serializable):
    """
    public class SpacecraftState extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.propagation.SpacecraftState`>, :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        This class is the representation of a complete state holding orbit, attitude and mass information at a given date, meant
        primarily for propagation.
    
        It contains an :class:`~org.orekit.orbits.Orbit`, or an :class:`~org.orekit.utils.AbsolutePVCoordinates` if there is no
        definite central body, plus the current mass and attitude at the intrinsic :class:`~org.orekit.time.AbsoluteDate`.
        Quantities are guaranteed to be consistent in terms of date and reference frame. The spacecraft state may also contain
        additional states, which are simply named double arrays which can hold any user-defined data.
    
        The state can be slightly shifted to close dates. This actual shift varies between :class:`~org.orekit.orbits.Orbit` and
        :class:`~org.orekit.utils.AbsolutePVCoordinates`. For attitude it is a linear extrapolation taking the spin rate into
        account and no mass change. It is *not* intended as a replacement for proper orbit and attitude propagation but should
        be sufficient for either small time shifts or coarse accuracy.
    
        The instance :code:`SpacecraftState` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`, :meth:`~serialized`
    """
    DEFAULT_MASS: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_MASS
    
        Default mass.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, double: float, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, double: float, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary, doubleArrayDictionary2: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, double: float): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, double: float, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, double: float): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, double: float, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, double: float, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary, doubleArrayDictionary2: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    def addAdditionalState(self, string: str, doubleArray: typing.List[float]) -> 'SpacecraftState':
        """
            Add an additional state.
        
            :class:`~org.orekit.propagation.SpacecraftState` instances are immutable, so this method does *not* change the instance,
            but rather creates a new instance, which has the same orbit, attitude, mass and additional states as the original
            instance, except it also has the specified state. If the original instance already had an additional state with the same
            name, it will be overridden. If it did not have any additional state with that name, the new instance will have one more
            additional state than the original instance.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
                value (double...): value of the additional state
        
            Returns:
                a new instance, with the additional state added
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStatesValues`
        
        
        """
        ...
    def addAdditionalStateDerivative(self, string: str, doubleArray: typing.List[float]) -> 'SpacecraftState':
        """
            Add an additional state derivative.
        
            :class:`~org.orekit.propagation.SpacecraftState` instances are immutable, so this method does *not* change the instance,
            but rather creates a new instance, which has the same components as the original instance, except it also has the
            specified state derivative. If the original instance already had an additional state derivative with the same name, it
            will be overridden. If it did not have any additional state derivative with that name, the new instance will have one
            more additional state derivative than the original instance.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state derivative (names containing "orekit" with any case are reserved for the library internal
                    use)
                value (double...): value of the additional state derivative
        
            Returns:
                a new instance, with the additional state added
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStatesDerivatives`
        
        
        """
        ...
    def ensureCompatibleAdditionalStates(self, spacecraftState: 'SpacecraftState') -> None: ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Returns:
                semi-major axis (m), or {code Double.NaN} if the state contains an absolute position-velocity-acceleration rather than
                an orbit
        
        
        """
        ...
    def getAbsPVA(self) -> org.orekit.utils.AbsolutePVCoordinates: ...
    def getAdditionalState(self, string: str) -> typing.List[float]:
        """
            Get an additional state.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                value of the additional state
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStatesValues`
        
        
        """
        ...
    def getAdditionalStateDerivative(self, string: str) -> typing.List[float]:
        """
            Get an additional state derivative.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state derivative
        
            Returns:
                value of the additional state derivative
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStatesDerivatives`
        
        
        """
        ...
    def getAdditionalStatesDerivatives(self) -> org.orekit.utils.DoubleArrayDictionary:
        """
            Get an unmodifiable map of additional states derivatives.
        
            Returns:
                unmodifiable map of additional states derivatives
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStateDerivative`
        
        
        """
        ...
    def getAdditionalStatesValues(self) -> org.orekit.utils.DoubleArrayDictionary:
        """
            Get an unmodifiable map of additional states.
        
            Returns:
                unmodifiable map of additional states
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`
        
        
        """
        ...
    def getAttitude(self) -> org.orekit.attitudes.Attitude:
        """
            Get the attitude.
        
            Returns:
                the attitude.
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Returns:
                eccentricity, or {code Double.NaN} if the state contains an absolute position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getEquinoctialEx`,
                :meth:`~org.orekit.propagation.SpacecraftState.getEquinoctialEy`
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e cos(ω + Ω), first component of eccentricity vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getE`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e sin(ω + Ω), second component of the eccentricity vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getE`
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the defining frame.
        
            Returns:
                the frame in which state is defined
        
        
        """
        ...
    def getHx(self) -> float:
        """
            Get the first component of the inclination vector (as per equinoctial parameters).
        
            Returns:
                tan(i/2) cos(Ω), first component of the inclination vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getI`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector (as per equinoctial parameters).
        
            Returns:
                tan(i/2) sin(Ω), second component of the inclination vector, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getI`
        
        
        """
        ...
    def getI(self) -> float:
        """
            Get the inclination.
        
            Returns:
                inclination (rad)
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getHx`, :meth:`~org.orekit.propagation.SpacecraftState.getHy`
        
        
        """
        ...
    def getKeplerianMeanMotion(self) -> float:
        """
            Get the Keplerian mean motion.
        
            The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian mean motion in radians per second, or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
        
        """
        ...
    def getKeplerianPeriod(self) -> float:
        """
            Get the Keplerian period.
        
            The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian period in seconds, or {code Double.NaN} if the state contains an absolute position-velocity-acceleration
                rather than an orbit
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric latitude argument (as per equinoctial parameters).
        
            Returns:
                E + ω + Ω eccentric longitude argument (rad), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getLv`, :meth:`~org.orekit.propagation.SpacecraftState.getLM`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument (as per equinoctial parameters).
        
            Returns:
                M + ω + Ω mean latitude argument (rad), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getLv`, :meth:`~org.orekit.propagation.SpacecraftState.getLE`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true latitude argument (as per equinoctial parameters).
        
            Returns:
                v + ω + Ω true longitude argument (rad), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getLE`, :meth:`~org.orekit.propagation.SpacecraftState.getLM`
        
        
        """
        ...
    def getMass(self) -> float:
        """
            Gets the current mass.
        
            Returns:
                the mass (kg)
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central attraction coefficient.
        
            Returns:
                mu central attraction coefficient (m^3/s^2), or {code Double.NaN} if the state contains an absolute
                position-velocity-acceleration rather than an orbit
        
        
        """
        ...
    def getOrbit(self) -> org.orekit.orbits.Orbit: ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.TimeStampedPVCoordinates` in orbit definition frame.
        
            Compute the position and velocity of the satellite. This method caches its results, and recompute them only when the
            method is called with a new value for mu. The result is provided as a reference to the internally cached
            :class:`~org.orekit.utils.TimeStampedPVCoordinates`, so the caller is responsible to copy it in a separate
            :class:`~org.orekit.utils.TimeStampedPVCoordinates` if it needs to keep the value for a while.
        
            Returns:
                pvCoordinates in orbit definition frame
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.TimeStampedPVCoordinates` in given output frame.
        
            Compute the position and velocity of the satellite. This method caches its results, and recompute them only when the
            method is called with a new value for mu. The result is provided as a reference to the internally cached
            :class:`~org.orekit.utils.TimeStampedPVCoordinates`, so the caller is responsible to copy it in a separate
            :class:`~org.orekit.utils.TimeStampedPVCoordinates` if it needs to keep the value for a while.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): frame in which coordinates should be defined
        
            Returns:
                pvCoordinates in orbit definition frame
        
        
        """
        ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position in orbit definition frame.
        
            Returns:
                position in orbit definition frame
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getPVCoordinates`
        
        """
        ...
    @typing.overload
    def getPosition(self, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the position in given output frame.
        
            Parameters:
                outputFrame (:class:`~org.orekit.frames.Frame`): frame in which position should be defined
        
            Returns:
                position in given output frame
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getPVCoordinates`
        
        
        """
        ...
    def hasAdditionalState(self, string: str) -> bool:
        """
            Check if an additional state is available.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is available
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStatesValues`
        
        
        """
        ...
    def hasAdditionalStateDerivative(self, string: str) -> bool:
        """
            Check if an additional state derivative is available.
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state derivative
        
            Returns:
                true if the additional state derivative is available
        
            Since:
                11.1
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStateDerivative`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStatesDerivatives`
        
        
        """
        ...
    def isOrbitDefined(self) -> bool:
        """
            Check if the state contains an orbit part.
        
            A state contains either an :class:`~org.orekit.utils.AbsolutePVCoordinates` or an :class:`~org.orekit.orbits.Orbit`.
        
            Returns:
                true if state contains an orbit (in which case :meth:`~org.orekit.propagation.SpacecraftState.getOrbit` will not throw
                an exception), or false if the state contains an absolut position-velocity-acceleration (in which case
                :meth:`~org.orekit.propagation.SpacecraftState.getAbsPVA` will not throw an exception)
        
        
        """
        ...
    def shiftedBy(self, double: float) -> 'SpacecraftState':
        """
            Get a time-shifted state.
        
            The state can be slightly shifted to close dates. This shift is based on simple models. For orbits, the model is a
            Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian
            acceleration if derivatives are available. For attitude, a polynomial model is used. Neither mass nor additional states
            change. Shifting is *not* intended as a replacement for proper orbit and attitude propagation but should be sufficient
            for small time shifts or coarse accuracy.
        
            As a rough order of magnitude, the following table shows the extrapolation errors obtained between this simple shift
            method and an :class:`~org.orekit.propagation.numerical.NumericalPropagator` for a low Earth Sun Synchronous Orbit, with
            a 20x20 gravity field, Sun and Moon third bodies attractions, drag and solar radiation pressure. Beware that these
            results will be different for other orbits.
        
            Specified by:
                :meth:`~org.orekit.time.TimeShiftable.shiftedBy` in interface :class:`~org.orekit.time.TimeShiftable`
        
            Parameters:
                dt (double): time shift in seconds
        
            Returns:
                a new state, shifted with respect to the instance (which is immutable) except for the mass and additional states which
                stay unchanged
        
        
        """
        ...
    def toStaticTransform(self) -> org.orekit.frames.StaticTransform:
        """
            Compute the static transform from state defining frame to spacecraft frame.
        
            Returns:
                static transform from specified frame to current spacecraft frame
        
            Since:
                12.0
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.toTransform`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in
                class :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
        
        
        """
        ...
    def toTransform(self) -> org.orekit.frames.Transform:
        """
            Compute the transform from state defining frame to spacecraft frame.
        
            The spacecraft frame origin is at the point defined by the orbit (or absolute position-velocity-acceleration), and its
            orientation is defined by the attitude.
        
            Returns:
                transform from specified frame to current spacecraft frame
        
        
        """
        ...

class SpacecraftStateInterpolator(org.orekit.time.AbstractTimeInterpolator[SpacecraftState]):
    """
    public class SpacecraftStateInterpolator extends :class:`~org.orekit.time.AbstractTimeInterpolator`<:class:`~org.orekit.propagation.SpacecraftState`>
    
        Generic class for spacecraft state interpolator.
    
        The user can specify what interpolator to use for each attribute of the spacecraft state. However, at least one
        interpolator for either orbit or absolute position-velocity-acceleration is needed. All the other interpolators can be
        left to null if the user do not want to interpolate these values.
    
        Also see:
            :class:`~org.orekit.propagation.SpacecraftState`
    """
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, int: int, double: float, frame: org.orekit.frames.Frame, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.utils.AbsolutePVCoordinates], timeInterpolator3: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble], timeInterpolator4: org.orekit.time.TimeInterpolator[org.orekit.attitudes.Attitude], timeInterpolator5: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble]): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, int: int, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.utils.AbsolutePVCoordinates], timeInterpolator3: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble], timeInterpolator4: org.orekit.time.TimeInterpolator[org.orekit.attitudes.Attitude], timeInterpolator5: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble]): ...
    @staticmethod
    def checkSampleAndInterpolatorConsistency(list: java.util.List[SpacecraftState], boolean: bool, boolean2: bool) -> None: ...
    @staticmethod
    def checkStatesDefinitionsConsistency(list: java.util.List[SpacecraftState]) -> None: ...
    def getAbsPVAInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.utils.AbsolutePVCoordinates]]: ...
    def getAdditionalStateInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble]]: ...
    def getAttitudeInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.attitudes.Attitude]]: ...
    def getMassInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble]]: ...
    def getOrbitInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit]]: ...
    def getOutputFrame(self) -> org.orekit.frames.Frame:
        """
            Get output frame.
        
            Returns:
                output frame
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStamped]]: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[SpacecraftState], typing.Sequence[SpacecraftState]]) -> SpacecraftState: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.TimeStamped]) -> org.orekit.time.TimeStamped: ...

class StateCovariance(org.orekit.time.TimeStamped):
    """
    public class StateCovariance extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.time.TimeStamped`
    
        This class is the representation of a covariance matrix at a given date.
    
        Currently, the covariance only represents the orbital elements.
    
        It is possible to change the covariance frame by using the
        :meth:`~org.orekit.propagation.StateCovariance.changeCovarianceFrame` or
        :meth:`~org.orekit.propagation.StateCovariance.changeCovarianceFrame` method. These methods are based on Equations (18)
        and (20) of *Covariance Transformations for Satellite Flight Dynamics Operations* by David A. SVallado.
    
        Finally, covariance orbit type can be changed using the
        :meth:`~org.orekit.propagation.StateCovariance.changeCovarianceType` method.
    
        Since:
            11.3
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    public static final int STATE_DIMENSION
    
        State dimension.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, absoluteDate: org.orekit.time.AbsoluteDate, lOF: org.orekit.frames.LOF): ...
    @typing.overload
    def changeCovarianceFrame(self, orbit: org.orekit.orbits.Orbit, frame: org.orekit.frames.Frame) -> 'StateCovariance':
        """
            Get the covariance in a given local orbital frame.
        
            Changing the covariance frame is a linear process, this method does not introduce approximation unless a change in
            covariance orbit type is required.
        
            This is based on equation (18) to (20) "from Vallado, D. A. (2004). Covariance transformations for satellite flight
            dynamics operations."
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to which the covariance matrix should correspond
                lofOut (:class:`~org.orekit.frames.LOF`): output local orbital frame
        
            Returns:
                a new covariance state, expressed in the output local orbital frame
        
            Get the covariance in the output frame.
        
            Changing the covariance frame is a linear process, this method does not introduce approximation unless a change in
            covariance orbit type is required.
        
            This is based on equation (18) to (20) "from Vallado, D. A. (2004). Covariance transformations for satellite flight
            dynamics operations."
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to which the covariance matrix should correspond
                frameOut (:class:`~org.orekit.frames.Frame`): output frame
        
            Returns:
                a new covariance state, expressed in the output frame
        
        
        """
        ...
    @typing.overload
    def changeCovarianceFrame(self, orbit: org.orekit.orbits.Orbit, lOF: org.orekit.frames.LOF) -> 'StateCovariance': ...
    def changeCovarianceType(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> 'StateCovariance':
        """
            Get the covariance matrix in another orbit type.
        
            The covariance orbit type **cannot** be changed if the covariance matrix is expressed in a
            :class:`~org.orekit.frames.LOF` or a non-pseudo inertial frame.
        
            As this type change uses the jacobian matrix of the transformation, it introduces a linear approximation. Hence, the
            current covariance matrix **will not exactly match** the new linearized case and the distribution will not follow a
            generalized Gaussian distribution anymore.
        
            This is based on equation (1) to (6) from "Vallado, D. A. (2004). Covariance transformations for satellite flight
            dynamics operations."
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to which the covariance matrix should correspond
                outOrbitType (:class:`~org.orekit.orbits.OrbitType`): target orbit type of the state covariance matrix
                outAngleType (:class:`~org.orekit.orbits.PositionAngleType`): target position angle type of the state covariance matrix
        
            Returns:
                a new covariance state, expressed in the target orbit type with the target position angle
        
            Also see:
                :meth:`~org.orekit.propagation.StateCovariance.changeCovarianceFrame`
        
        
        """
        ...
    @staticmethod
    def checkFrameAndOrbitTypeConsistency(frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType) -> None:
        """
            Check constructor's inputs consistency.
        
            Parameters:
                covarianceFrame (:class:`~org.orekit.frames.Frame`): covariance frame (inertial or Earth fixed)
                inputType (:class:`~org.orekit.orbits.OrbitType`): orbit type of the covariance
        
            Raises:
                :class:`~org.orekit.errors.OrekitException`: if input frame is not pseudo-inertial AND the orbit type is not Cartesian
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date..
        
            Specified by:
                :meth:`~org.orekit.time.TimeStamped.getDate` in interface :class:`~org.orekit.time.TimeStamped`
        
            Returns:
                date attached to the object
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the covariance frame.
        
            Returns:
                the covariance frame (can be null)
        
            Also see:
                :meth:`~org.orekit.propagation.StateCovariance.getLOF`
        
        
        """
        ...
    def getLOF(self) -> org.orekit.frames.LOF:
        """
            Get the covariance LOF type.
        
            Returns:
                the covariance LOF type (can be null)
        
            Also see:
                :meth:`~org.orekit.propagation.StateCovariance.getFrame`
        
        
        """
        ...
    def getMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the covariance matrix.
        
            Returns:
                the covariance matrix
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the covariance orbit type.
        
            Returns:
                the covariance orbit type
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get the covariance angle type.
        
            Returns:
                the covariance angle type
        
        
        """
        ...
    @staticmethod
    def getStm(orbit: org.orekit.orbits.Orbit, double: float) -> org.hipparchus.linear.RealMatrix:
        """
            Get the state transition matrix considering Keplerian contribution only.
        
            Parameters:
                initialOrbit (:class:`~org.orekit.orbits.Orbit`): orbit to which the initial covariance matrix should correspond
                dt (double): time difference between the two orbits
        
            Returns:
                the state transition matrix used to shift the covariance matrix
        
        
        """
        ...
    @staticmethod
    def inputAndOutputAreIdentical(orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, orbitType2: org.orekit.orbits.OrbitType, positionAngleType2: org.orekit.orbits.PositionAngleType) -> bool:
        """
            Checks if input/output orbit and angle types are identical.
        
            Parameters:
                inOrbitType (:class:`~org.orekit.orbits.OrbitType`): input orbit type
                inAngleType (:class:`~org.orekit.orbits.PositionAngleType`): input angle type
                outOrbitType (:class:`~org.orekit.orbits.OrbitType`): output orbit type
                outAngleType (:class:`~org.orekit.orbits.PositionAngleType`): output angle type
        
            Returns:
                flag defining if input/output orbit and angle types are identical
        
        
        """
        ...
    @staticmethod
    def inputAndOutputOrbitTypesAreCartesian(orbitType: org.orekit.orbits.OrbitType, orbitType2: org.orekit.orbits.OrbitType) -> bool:
        """
            Checks if input and output orbit types are both :code:`OrbitType.CARTESIAN`.
        
            Parameters:
                inOrbitType (:class:`~org.orekit.orbits.OrbitType`): input orbit type
                outOrbitType (:class:`~org.orekit.orbits.OrbitType`): output orbit type
        
            Returns:
                flag defining if input and output orbit types are both :code:`OrbitType.CARTESIAN`
        
        
        """
        ...
    def shiftedBy(self, orbit: org.orekit.orbits.Orbit, double: float) -> 'StateCovariance':
        """
            Get a time-shifted covariance matrix.
        
            The shifting model is a linearized, Keplerian one. In other words, it is based on a state transition matrix that is
            computed assuming Keplerian motion.
        
            Shifting is *not* intended as a replacement for proper covariance propagation, but should be sufficient for small time
            shifts or coarse accuracy.
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): orbit to which the covariance matrix should correspond
                dt (double): time shift in seconds
        
            Returns:
                a new covariance state, shifted with respect to the instance
        
        
        """
        ...

class AbstractMatricesHarvester(MatricesHarvester):
    """
    public abstract class AbstractMatricesHarvester extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.MatricesHarvester`
    
        Base harvester between two-dimensional Jacobian matrices and one-dimensional
        :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`.
    
        Since:
            11.1
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    public static final int STATE_DIMENSION
    
        State dimension, fixed to 6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def freezeColumnsNames(self) -> None:
        """
            Freeze the names of the Jacobian columns.
        
            This method is called when propagation starts, i.e. when configuration is completed
        
        """
        ...
    def getInitialJacobianColumn(self, string: str) -> typing.List[float]:
        """
            Get the initial column of Jacobian matrix with respect to named parameter.
        
            Parameters:
                columnName (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the column
        
            Returns:
                initial column of the Jacobian matrix
        
        
        """
        ...
    def getInitialStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the initial State Transition Matrix.
        
            Returns:
                initial State Transition Matrix
        
        
        """
        ...
    def getParametersJacobian(self, spacecraftState: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian with respect to propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getParametersJacobian` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getStateTransitionMatrix(self, spacecraftState: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Extract state transition matrix from state.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getStateTransitionMatrix` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
                :class:`~org.orekit.orbits.OrbitType`.
        
        
        """
        ...
    def getStmName(self) -> str:
        """
            Get the State Transition Matrix state name.
        
            Returns:
                State Transition Matrix state name
        
        
        """
        ...
    def setReferenceState(self, spacecraftState: SpacecraftState) -> None:
        """
            Set up reference state.
        
            This method is called whenever the global propagation reference state changes. This corresponds to the start of
            propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering.
            Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute
            analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not
            use it at all.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.setReferenceState` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): reference state to set
        
        
        """
        ...

class AbstractPropagator(Propagator):
    """
    public abstract class AbstractPropagator extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.Propagator`
    
        Common handling of :class:`~org.orekit.propagation.Propagator` methods for analytical propagators.
    
        This abstract class allows to provide easily the full set of :class:`~org.orekit.propagation.Propagator` methods,
        including all propagation modes support and discrete events support for any simple propagation method.
    """
    def addAdditionalStateProvider(self, additionalStateProvider: AdditionalStateProvider) -> None:
        """
            Add a set of user-specified state parameters to be computed along with the orbit propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                provider (:class:`~org.orekit.propagation.AdditionalStateProvider`): provider for additional state
        
        
        """
        ...
    def getAdditionalStateProviders(self) -> java.util.List[AdditionalStateProvider]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                attitude provider
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getFrame` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> SpacecraftState:
        """
            Get the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                initial state
        
        
        """
        ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getManagedAdditionalStates` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer:
        """
            Get the multiplexer holding all step handlers.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getMultiplexer` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                multiplexer holding all step handlers
        
        
        """
        ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which a :class:`~org.orekit.propagation.AdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` method.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.Propagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` method is called at an event occurrence
            and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.isAdditionalStateManaged` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
            Propagate towards a target date.
        
            Simple propagators use only the target date as the specification for computing the propagated state. More feature rich
            propagators can consider other information and provide different operating modes or G-stop facilities to stop at
            pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.propagate` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                target (:class:`~org.orekit.time.AbsoluteDate`): target date towards which orbit state should be propagated
        
            Returns:
                propagated state
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    def setupMatricesComputation(self, string: str, realMatrix: org.hipparchus.linear.RealMatrix, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary) -> MatricesHarvester:
        """
            Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
            If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that
            will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
            The arguments for initial matrices *must* be compatible with the :class:`~org.orekit.orbits.OrbitType` and
            :class:`~org.orekit.orbits.PositionAngleType` that will be used by the propagator.
        
            The default implementation throws an exception as the method is not supported by all propagators.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setupMatricesComputation` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                stmName (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): State Transition Matrix state name
                initialStm (:class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.linear.RealMatrix?is`): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
                initialJacobianColumns (:class:`~org.orekit.utils.DoubleArrayDictionary`): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                    from the dictionary, the corresponding initial column is assumed to be 0
        
            Returns:
                harvester to retrieve computed matrices during and after propagation
        
        
        """
        ...

class AbstractStateModifier(AdditionalStateProvider):
    """
    public abstract class AbstractStateModifier extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.AdditionalStateProvider`
    
        Abstract base class for modifying state during propagation.
    
        This class is a specialized implementation of :class:`~org.orekit.propagation.AdditionalStateProvider` with a name set
        to the empty string and returning a null additional state.
    
        Beware that changing the state undercover from the propagator may have many side effects. Using this class should
        therefore be done cautiously.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.Propagator`, :class:`~org.orekit.propagation.AdditionalStateProvider`
    """
    def __init__(self): ...
    def change(self, spacecraftState: SpacecraftState) -> SpacecraftState:
        """
            Change main state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to change
        
            Returns:
                changed state
        
        
        """
        ...
    def getAdditionalState(self, spacecraftState: SpacecraftState) -> typing.List[float]:
        """
            Get the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which additional state should correspond
        
            Returns:
                additional state corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new state, it should
            return the empty string as its name.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getName` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def update(self, spacecraftState: SpacecraftState) -> SpacecraftState:
        """
            Update a state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.update` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to update
        
            Returns:
                updated state
        
        
        """
        ...

class BoundedPropagator(Propagator):
    """
    public interface BoundedPropagator extends :class:`~org.orekit.propagation.Propagator`
    
        This interface is intended for ephemerides valid only during a time range.
    
        This interface provides a mean to retrieve orbital parameters at any time within a given range. It should be implemented
        by orbit readers based on external data files and by continuous models built after numerical integration has been
        completed and dense output data as been gathered.
    """
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the first date of the range.
        
            Returns:
                the first date of the range
        
        
        """
        ...

_FieldAbstractPropagator__T = typing.TypeVar('_FieldAbstractPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractPropagator(FieldPropagator[_FieldAbstractPropagator__T], typing.Generic[_FieldAbstractPropagator__T]):
    """
    public abstract class FieldAbstractPropagator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.FieldPropagator`<T>
    
        Common handling of :class:`~org.orekit.propagation.Propagator` methods for analytical propagators.
    
        This abstract class allows to provide easily the full set of :class:`~org.orekit.propagation.Propagator` methods,
        including all propagation modes support and discrete events support for any simple propagation method.
    """
    def addAdditionalStateProvider(self, fieldAdditionalStateProvider: FieldAdditionalStateProvider[_FieldAbstractPropagator__T]) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[FieldAdditionalStateProvider[_FieldAbstractPropagator__T]]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getAttitudeProvider` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                attitude provider
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldAbstractPropagator__T]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getFrame` in interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> FieldSpacecraftState[_FieldAbstractPropagator__T]: ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getManagedAdditionalStates` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_FieldAbstractPropagator__T]: ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which an :class:`~org.orekit.propagation.FieldAdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.FieldPropagator.addAdditionalStateProvider` method. If the propagator is an
            :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`, the states for which a set of
            :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addAdditionalDerivativesProvider` method
            are also counted as managed additional states.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.FieldPropagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.resetState` method is called at an event
            occurrence and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.isAdditionalStateManaged` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldAbstractPropagator__T]) -> FieldSpacecraftState[_FieldAbstractPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractPropagator__T]) -> FieldSpacecraftState[_FieldAbstractPropagator__T]: ...
    def resetInitialState(self, fieldSpacecraftState: FieldSpacecraftState[_FieldAbstractPropagator__T]) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.setAttitudeProvider` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...

_FieldAbstractStateModifier__T = typing.TypeVar('_FieldAbstractStateModifier__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractStateModifier(FieldAdditionalStateProvider[_FieldAbstractStateModifier__T], typing.Generic[_FieldAbstractStateModifier__T]):
    """
    public abstract class FieldAbstractStateModifier<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.FieldAdditionalStateProvider`<T>
    
        Abstract base class for modifying state during propagation.
    
        This class is a specialized implementation of :class:`~org.orekit.propagation.AdditionalStateProvider` with a name set
        to the empty string and returning a null additional state.
    
        Beware that changing the state undercover from the propagator may have many side effects. Using this class should
        therefore be done cautiously.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.Propagator`, :class:`~org.orekit.propagation.AdditionalStateProvider`
    """
    def __init__(self): ...
    def change(self, fieldSpacecraftState: FieldSpacecraftState[_FieldAbstractStateModifier__T]) -> FieldSpacecraftState[_FieldAbstractStateModifier__T]: ...
    def getAdditionalState(self, fieldSpacecraftState: FieldSpacecraftState[_FieldAbstractStateModifier__T]) -> typing.List[_FieldAbstractStateModifier__T]: ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new state, it should
            return the empty string as its name.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldAdditionalStateProvider.getName` in
                interface :class:`~org.orekit.propagation.FieldAdditionalStateProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def update(self, fieldSpacecraftState: FieldSpacecraftState[_FieldAbstractStateModifier__T]) -> FieldSpacecraftState[_FieldAbstractStateModifier__T]: ...

_FieldBoundedPropagator__T = typing.TypeVar('_FieldBoundedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBoundedPropagator(FieldPropagator[_FieldBoundedPropagator__T], typing.Generic[_FieldBoundedPropagator__T]):
    """
    public interface FieldBoundedPropagator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.FieldPropagator`<T>
    
        This interface is intended for ephemerides valid only during a time range.
    
        This interface provides a mean to retrieve orbital parameters at any time within a given range. It should be implemented
        by orbit readers based on external data files and by continuous models built after numerical integration has been
        completed and dense output data as been gathered.
    """
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldBoundedPropagator__T]: ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldBoundedPropagator__T]: ...

class PythonAdditionalStateProvider(AdditionalStateProvider):
    """
    public class PythonAdditionalStateProvider extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.AdditionalStateProvider`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAdditionalState(self, spacecraftState: SpacecraftState) -> typing.List[float]:
        """
            Get the additional state. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which additional state should correspond
        
            Returns:
                additional state corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getName` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Returns:
                name of the additional state
        
        
        """
        ...
    def init(self, spacecraftState: SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the additional state provider at the start of propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.init` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state information at the start of propagation
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation
        
            Since:
                11.2
        
        
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
    def yields(self, spacecraftState: SpacecraftState) -> bool:
        """
            Check if this provider should yield so another provider has an opportunity to add missing parts.
        
            Decision to yield is often based on an additional state being
            :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState` in the provided :code:`state` (but it could
            theoretically also depend on an additional state derivative being
            :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalStateDerivative`, or any other criterion). If for example a
            provider needs the state transition matrix, it could implement this method as:
        
            .. code-block: java
            
             public boolean yields(final SpacecraftState state) {
                 return !state.getAdditionalStates().containsKey("STM");
             }
             
        
            The default implementation returns :code:`false`, meaning that state data can be
            :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState` immediately.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.yields` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state to handle
        
            Returns:
                true if this provider should yield so another provider has an opportunity to add missing parts as the state is
                incrementally built up
        
        
        """
        ...

class PythonEphemerisGenerator(EphemerisGenerator):
    """
    public class PythonEphemerisGenerator extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.EphemerisGenerator`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getGeneratedEphemeris(self) -> BoundedPropagator:
        """
            Get the ephemeris generated during the propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.EphemerisGenerator.getGeneratedEphemeris` in
                interface :class:`~org.orekit.propagation.EphemerisGenerator`
        
            Returns:
                generated ephemeris
        
        
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

_PythonFieldAdditionalStateProvider__T = typing.TypeVar('_PythonFieldAdditionalStateProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdditionalStateProvider(FieldAdditionalStateProvider[_PythonFieldAdditionalStateProvider__T], typing.Generic[_PythonFieldAdditionalStateProvider__T]):
    """
    public class PythonFieldAdditionalStateProvider<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.FieldAdditionalStateProvider`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAdditionalState(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldAdditionalStateProvider__T]) -> typing.List[_PythonFieldAdditionalStateProvider__T]: ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldAdditionalStateProvider.getName` in
                interface :class:`~org.orekit.propagation.FieldAdditionalStateProvider`
        
            Returns:
                name of the additional state
        
        
        """
        ...
    def init(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldAdditionalStateProvider__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAdditionalStateProvider__T]) -> None: ...
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
    def yield_(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldAdditionalStateProvider__T]) -> bool: ...

_PythonFieldEphemerisGenerator__T = typing.TypeVar('_PythonFieldEphemerisGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEphemerisGenerator(FieldEphemerisGenerator[_PythonFieldEphemerisGenerator__T], typing.Generic[_PythonFieldEphemerisGenerator__T]):
    """
    public class PythonFieldEphemerisGenerator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.FieldEphemerisGenerator`<T>
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getGeneratedEphemeris(self) -> FieldBoundedPropagator[_PythonFieldEphemerisGenerator__T]: ...
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

_PythonFieldPropagator__T = typing.TypeVar('_PythonFieldPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldPropagator(FieldPropagator[_PythonFieldPropagator__T], typing.Generic[_PythonFieldPropagator__T]):
    """
    public class PythonFieldPropagator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.FieldPropagator`<T>
    """
    def __init__(self): ...
    def addAdditionalStateProvider(self, fieldAdditionalStateProvider: FieldAdditionalStateProvider[_PythonFieldPropagator__T]) -> None: ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, d: _addEventDetector__D) -> None: ...
    def clearEventsDetectors(self) -> None:
        """
            Remove all events detectors.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.clearEventsDetectors` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`,
                :meth:`~org.orekit.propagation.FieldPropagator.getEventsDetectors`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[FieldAdditionalStateProvider[_PythonFieldPropagator__T]]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getAttitudeProvider` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldPropagator__T]]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getFrame` in interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> FieldSpacecraftState[_PythonFieldPropagator__T]: ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getManagedAdditionalStates` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_PythonFieldPropagator__T]: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_PythonFieldPropagator__T]: ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which an :class:`~org.orekit.propagation.FieldAdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.FieldPropagator.addAdditionalStateProvider` method. If the propagator is an
            :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`, the states for which a set of
            :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addAdditionalDerivativesProvider` method
            are also counted as managed additional states.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.FieldPropagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.resetState` method is called at an event
            occurrence and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.isAdditionalStateManaged` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T]) -> FieldSpacecraftState[_PythonFieldPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T]) -> FieldSpacecraftState[_PythonFieldPropagator__T]: ...
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
    def resetInitialState(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldPropagator__T]) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.setAttitudeProvider` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...

class PythonMatricesHarvester(MatricesHarvester):
    """
    public class PythonMatricesHarvester extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.MatricesHarvester`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getJacobiansColumnsNames(self) -> java.util.List[str]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.MatricesHarvester.getOrbitType`
            Get the orbit type used for the matrix computation.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getOrbitType` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Returns:
                the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, spacecraftState: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian with respect to propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getParametersJacobian` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.MatricesHarvester.getPositionAngleType`
            Get the position angle used for the matrix computation.
        
            Irrelevant if :meth:`~org.orekit.propagation.MatricesHarvester.getOrbitType` returns
            :meth:`~org.orekit.orbits.OrbitType.CARTESIAN`.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getPositionAngleType` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Returns:
                the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, spacecraftState: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Extract state transition matrix from state.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getStateTransitionMatrix` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
                :class:`~org.orekit.orbits.OrbitType`.
        
        
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
    def setReferenceState(self, spacecraftState: SpacecraftState) -> None:
        """
            Set up reference state.
        
            This method is called whenever the global propagation reference state changes. This corresponds to the start of
            propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering.
            Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute
            analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not
            use it at all.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.setReferenceState` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): reference state to set
        
        
        """
        ...

class PythonPropagator(Propagator):
    """
    public class PythonPropagator extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.Propagator`
    """
    def __init__(self): ...
    def addAdditionalStateProvider(self, additionalStateProvider: AdditionalStateProvider) -> None:
        """
            Add a set of user-specified state parameters to be computed along with the orbit propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                additionalStateProvider (:class:`~org.orekit.propagation.AdditionalStateProvider`): provider for additional state
        
        
        """
        ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, t: _addEventDetector__T) -> None:
        """
            Add an event detector.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.addEventDetector` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                detector (T): event detector to add
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.clearEventsDetectors`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
            Remove all events detectors.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.clearEventsDetectors` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.addEventDetector`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[AdditionalStateProvider]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
            Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
            This generator can be used when the user needs fast random access to the orbit state at any time between the initial and
            target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and
            backward inside the propagation range before finding their result even if the propagator used is integration-based and
            only goes from one initial time to one target time.
        
            Beware that when used with integration-based propagators, the generator will store **all** intermediate results. It is
            therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with
            analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to
            call it back as needed, so it is less memory intensive.
        
            The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call
            to either :meth:`~org.orekit.propagation.Propagator.propagate` or :meth:`~org.orekit.propagation.Propagator.propagate`
            is called. The proper way to use this method is therefore to do:
        
            .. code-block: java
            
               EphemerisGenerator generator = propagator.getEphemerisGenerator();
               propagator.propagate(target);
               BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
             
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getEphemerisGenerator` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                ephemeris generator
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getFrame` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> SpacecraftState:
        """
            Get the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                initial state
        
        
        """
        ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getManagedAdditionalStates` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer:
        """
            Get the multiplexer holding all step handlers.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getMultiplexer` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                multiplexer holding all step handlers
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getPVCoordinates` in interface :class:`~org.orekit.propagation.Propagator`
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates` in
                interface :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which a :class:`~org.orekit.propagation.AdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` method.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.Propagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` method is called at an event occurrence
            and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.isAdditionalStateManaged` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
            Propagate towards a target date.
        
            Simple propagators use only the target date as the specification for computing the propagated state. More feature rich
            propagators can consider other information and provide different operating modes or G-stop facilities to stop at
            pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.propagate` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                target (:class:`~org.orekit.time.AbsoluteDate`): target date towards which orbit state should be propagated
        
            Returns:
                propagated state
        
            Propagate from a start date towards a target date.
        
            Those propagators use a start date and a target date to compute the propagated state. For propagators using event
            detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is
            performed, without processing any event computation. Then complete propagation is performed from start date to target
            date.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.propagate` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start date from which orbit state should be propagated
                target (:class:`~org.orekit.time.AbsoluteDate`): target date to which orbit state should be propagated
        
            Returns:
                propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    def setupMatricesComputation(self, string: str, realMatrix: org.hipparchus.linear.RealMatrix, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary) -> MatricesHarvester:
        """
            Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
            If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that
            will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
            The arguments for initial matrices *must* be compatible with the :class:`~org.orekit.orbits.OrbitType` and
            :class:`~org.orekit.orbits.PositionAngleType` that will be used by the propagator.
        
            The default implementation throws an exception as the method is not supported by all propagators.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setupMatricesComputation` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                stmName (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): State Transition Matrix state name
                initialStm (:class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.linear.RealMatrix?is`): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
                initialJacobianColumns (:class:`~org.orekit.utils.DoubleArrayDictionary`): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                    from the dictionary, the corresponding initial column is assumed to be 0
        
            Returns:
                harvester to retrieve computed matrices during and after propagation
        
        
        """
        ...

class StateCovarianceBlender(AbstractStateCovarianceInterpolator):
    """
    public class StateCovarianceBlender extends :class:`~org.orekit.propagation.AbstractStateCovarianceInterpolator`
    
        State covariance blender.
    
        Its purpose is to interpolate state covariance between tabulated state covariances by using the concept of blending,
        exposed in : "Efficient Covariance Interpolation using Blending of Approximate State Error Transitions" by Sergei
        Tanygin.
    
        It propagates tabulated values to the interpolation date assuming a standard keplerian model and then blend each
        propagated covariances using a smoothstep function.
    
        It gives accurate results as explained :class:`~org.orekit.propagation.https:.orekit.org.doc.technical`. In the very
        poorly tracked test case evolving in a highly dynamical environment mentioned in the linked thread, the user can expect
        at worst errors of less than 0.25% in position sigmas and less than 0.4% in velocity sigmas with steps of 40mn between
        tabulated values.
    
        Also see:
            
            class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory?is`,
            :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction?is`
    """
    @typing.overload
    def __init__(self, smoothStepFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, smoothStepFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], lOFType: org.orekit.frames.LOFType): ...

class StateCovarianceKeplerianHermiteInterpolator(AbstractStateCovarianceInterpolator):
    """
    public class StateCovarianceKeplerianHermiteInterpolator extends :class:`~org.orekit.propagation.AbstractStateCovarianceInterpolator`
    
        State covariance Keplerian quintic interpolator.
    
        Its purpose is to interpolate state covariance between tabulated state covariances using polynomial interpolation. To do
        so, it uses a
        :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`
        and compute the first and second order derivatives at tabulated states assuming a standard Keplerian motion depending on
        given derivatives filter.
    
        It gives very accurate results as explained :class:`~org.orekit.propagation.https:.orekit.org.doc.technical`. In the
        very poorly tracked test case evolving in a highly dynamical environment mentioned in the linked thread, the user can
        expect at worst errors of less than 0.2% in position sigmas and less than 0.35% in velocity sigmas with steps of 40mn
        between tabulated values.
    
        However, note that this method does not guarantee the positive definiteness of the computed state covariance as opposed
        to :class:`~org.orekit.propagation.StateCovarianceBlender`.
    
        Also see:
            
            class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`,
            :class:`~org.orekit.propagation.StateCovarianceBlender`
    """
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, lOFType: org.orekit.frames.LOFType): ...
    @typing.overload
    def __init__(self, int: int, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, int: int, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], lOFType: org.orekit.frames.LOFType): ...
    @typing.overload
    def __init__(self, int: int, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, int: int, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, lOFType: org.orekit.frames.LOFType): ...
    @typing.overload
    def __init__(self, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], lOFType: org.orekit.frames.LOFType): ...
    def getFilter(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get Filter defining if only the state covariance value are used or if first or/and second Keplerian derivatives should
            be used.
        
            Returns:
                Filter defining if only the state covariance value are used or if first or/and second Keplerian derivatives should be
                used.
        
        
        """
        ...

class StateCovarianceMatrixProvider(AdditionalStateProvider):
    """
    public class StateCovarianceMatrixProvider extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.AdditionalStateProvider`
    
        Additional state provider for state covariance matrix.
    
        This additional state provider allows computing a propagated covariance matrix based on a user defined input state
        covariance matrix. The computation of the propagated covariance matrix uses the State Transition Matrix between the
        propagated spacecraft state and the initial state. As a result, the user must define the name :code:`of the provider for
        the State Transition Matrix`.
    
        As the State Transition Matrix and the input state covariance matrix can be expressed in different orbit types, the user
        must specify both orbit types when building the covariance provider. In addition, the position angle used in both
        matrices must also be specified.
    
        In order to add this additional state provider to an orbit propagator, user must use the
        :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` method.
    
        For a given propagated spacecraft :code:`state`, the propagated state covariance matrix is accessible through the method
        :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getStateCovariance`
    
        Since:
            11.3
    """
    def __init__(self, string: str, string2: str, matricesHarvester: MatricesHarvester, stateCovariance: StateCovariance): ...
    def getAdditionalState(self, spacecraftState: SpacecraftState) -> typing.List[float]:
        """
            Get the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which additional state should correspond
        
            Returns:
                additional state corresponding to spacecraft state
        
        
        """
        ...
    def getCovarianceOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type in which the covariance matrix is expressed.
        
            Returns:
                the orbit type
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new state, it should
            return the empty string as its name.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.getName` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    @typing.overload
    def getStateCovariance(self, spacecraftState: SpacecraftState) -> StateCovariance:
        """
            Get the state covariance in the same frame/local orbital frame, orbit type and position angle as the initial covariance.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which the covariance matrix should correspond
        
            Returns:
                the state covariance
        
            Also see:
                :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getStateCovariance`,
                :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getStateCovariance`
        
            Get the state covariance expressed in a given frame.
        
            The output covariance matrix is expressed in the same orbit type as
            :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getCovarianceOrbitType`.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which the covariance matrix should correspond
                frame (:class:`~org.orekit.frames.Frame`): output frame for which the output covariance matrix must be expressed (must be inertial)
        
            Returns:
                the state covariance expressed in :code:`frame`
        
            Also see:
                :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getStateCovariance`,
                :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getStateCovariance`
        
            Get the state covariance expressed in a given orbit type.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to which the covariance matrix should correspond
                orbitType (:class:`~org.orekit.orbits.OrbitType`): output orbit type
                angleType (:class:`~org.orekit.orbits.PositionAngleType`): output position angle (not used if orbitType equals :code:`CARTESIAN`)
        
            Returns:
                the state covariance in :code:`orbitType` and :code:`angleType`
        
            Also see:
                :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getStateCovariance`,
                :meth:`~org.orekit.propagation.StateCovarianceMatrixProvider.getStateCovariance`
        
        
        """
        ...
    @typing.overload
    def getStateCovariance(self, spacecraftState: SpacecraftState, frame: org.orekit.frames.Frame) -> StateCovariance: ...
    @typing.overload
    def getStateCovariance(self, spacecraftState: SpacecraftState, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> StateCovariance: ...
    def init(self, spacecraftState: SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the additional state provider at the start of propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.init` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state information at the start of propagation
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation
        
        
        """
        ...
    def yields(self, spacecraftState: SpacecraftState) -> bool:
        """
            Check if this provider should yield so another provider has an opportunity to add missing parts.
        
            Decision to yield is often based on an additional state being
            :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState` in the provided :code:`state` (but it could
            theoretically also depend on an additional state derivative being
            :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalStateDerivative`, or any other criterion). If for example a
            provider needs the state transition matrix, it could implement this method as:
        
            .. code-block: java
            
             public boolean yields(final SpacecraftState state) {
                 return !state.getAdditionalStates().containsKey("STM");
             }
             
        
            The default implementation returns :code:`false`, meaning that state data can be
            :meth:`~org.orekit.propagation.AdditionalStateProvider.getAdditionalState` immediately.
        
            The covariance matrix can be computed only if the State Transition Matrix state is available.
        
            Specified by:
                :meth:`~org.orekit.propagation.AdditionalStateProvider.yields` in
                interface :class:`~org.orekit.propagation.AdditionalStateProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state to handle
        
            Returns:
                true if this provider should yield so another provider has an opportunity to add missing parts as the state is
                incrementally built up
        
        
        """
        ...

class PythonAbstractMatricesHarvester(AbstractMatricesHarvester):
    """
    public class PythonAbstractMatricesHarvester extends :class:`~org.orekit.propagation.AbstractMatricesHarvester`
    """
    def __init__(self, string: str, realMatrix: org.hipparchus.linear.RealMatrix, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    def finalize(self) -> None: ...
    def freezeColumnsNames(self) -> None:
        """
            Freeze the names of the Jacobian columns.
        
            This method is called when propagation starts, i.e. when configuration is completed
        
            Specified by:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.freezeColumnsNames` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
        
        """
        ...
    def getJacobiansColumnsNames(self) -> java.util.List[str]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type used for the matrix computation.
        
            Returns:
                the orbit type used for the matrix computation
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get the position angle used for the matrix computation.
        
            Irrelevant if :meth:`~org.orekit.propagation.MatricesHarvester.getOrbitType` returns
            :meth:`~org.orekit.orbits.OrbitType.CARTESIAN`.
        
            Returns:
                the position angle used for the matrix computation
        
        
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

class PythonAbstractPropagator(AbstractPropagator):
    """
    public class PythonAbstractPropagator extends :class:`~org.orekit.propagation.AbstractPropagator`
    """
    def __init__(self): ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, t: _addEventDetector__T) -> None:
        """
            Extension point for Python. Add an event detector.
        
            Parameters:
                detector (T): 
            Also see:
                :meth:`~org.orekit.propagation.Propagator.clearEventsDetectors`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
            Extension point for Python. Remove all events detectors.
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.addEventDetector`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
            Extension point for Python. Set up an ephemeris generator that will monitor the propagation for building an ephemeris
            from it once completed.
        
            This generator can be used when the user needs fast random access to the orbit state at any time between the initial and
            target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and
            backward inside the propagation range before finding their result even if the propagator used is integration-based and
            only goes from one initial time to one target time.
        
            Beware that when used with integration-based propagators, the generator will store **all** intermediate results. It is
            therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with
            analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to
            call it back as needed, so it is less memory intensive.
        
            The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call
            to either :meth:`~org.orekit.propagation.Propagator.propagate` or :meth:`~org.orekit.propagation.Propagator.propagate`
            is called. The proper way to use this method is therefore to do:
        
            .. code-block: java
            
               EphemerisGenerator generator = propagator.getEphemerisGenerator();
               propagator.propagate(target);
               BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
             
        
            Returns:
                ephemeris generator
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
            Propagate from a start date towards a target date. Extension point for Python.
        
            Those propagators use a start date and a target date to compute the propagated state. For propagators using event
            detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is
            performed, without processing any event computation. Then complete propagation is performed from start date to target
            date.
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start date from which orbit state should be propagated
                target (:class:`~org.orekit.time.AbsoluteDate`): target date to which orbit state should be propagated
        
            Returns:
                propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
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

class PythonAbstractStateModifier(AbstractStateModifier):
    """
    public class PythonAbstractStateModifier extends :class:`~org.orekit.propagation.AbstractStateModifier`
    """
    def __init__(self): ...
    def change(self, spacecraftState: SpacecraftState) -> SpacecraftState:
        """
            Description copied from class: :meth:`~org.orekit.propagation.AbstractStateModifier.change`
            Change main state.
        
            Specified by:
                :meth:`~org.orekit.propagation.AbstractStateModifier.change` in
                class :class:`~org.orekit.propagation.AbstractStateModifier`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state to change
        
            Returns:
                changed state
        
        
        """
        ...

class PythonBoundedPropagator(BoundedPropagator):
    """
    public class PythonBoundedPropagator extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.BoundedPropagator`
    """
    def __init__(self): ...
    def addAdditionalStateProvider(self, additionalStateProvider: AdditionalStateProvider) -> None:
        """
            Add a set of user-specified state parameters to be computed along with the orbit propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                additionalStateProvider (:class:`~org.orekit.propagation.AdditionalStateProvider`): provider for additional state
        
        
        """
        ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, t: _addEventDetector__T) -> None:
        """
            Add an event detector.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.addEventDetector` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                detector (T): event detector to add
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.clearEventsDetectors`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
            Remove all events detectors.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.clearEventsDetectors` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.addEventDetector`,
                :meth:`~org.orekit.propagation.Propagator.getEventsDetectors`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[AdditionalStateProvider]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
            Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
            This generator can be used when the user needs fast random access to the orbit state at any time between the initial and
            target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and
            backward inside the propagation range before finding their result even if the propagator used is integration-based and
            only goes from one initial time to one target time.
        
            Beware that when used with integration-based propagators, the generator will store **all** intermediate results. It is
            therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with
            analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to
            call it back as needed, so it is less memory intensive.
        
            The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call
            to either :meth:`~org.orekit.propagation.Propagator.propagate` or :meth:`~org.orekit.propagation.Propagator.propagate`
            is called. The proper way to use this method is therefore to do:
        
            .. code-block: java
            
               EphemerisGenerator generator = propagator.getEphemerisGenerator();
               propagator.propagate(target);
               BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
             
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getEphemerisGenerator` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                ephemeris generator
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getFrame` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> SpacecraftState:
        """
            Get the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                initial state
        
        
        """
        ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getManagedAdditionalStates` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Specified by:
                :meth:`~org.orekit.propagation.BoundedPropagator.getMaxDate` in
                interface :class:`~org.orekit.propagation.BoundedPropagator`
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the first date of the range.
        
            Specified by:
                :meth:`~org.orekit.propagation.BoundedPropagator.getMinDate` in
                interface :class:`~org.orekit.propagation.BoundedPropagator`
        
            Returns:
                the first date of the range
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer:
        """
            Get the multiplexer holding all step handlers.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getMultiplexer` in interface :class:`~org.orekit.propagation.Propagator`
        
            Returns:
                multiplexer holding all step handlers
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getPVCoordinates` in interface :class:`~org.orekit.propagation.Propagator`
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates` in
                interface :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which a :class:`~org.orekit.propagation.AdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` method.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.Propagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` method is called at an event occurrence
            and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.isAdditionalStateManaged` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
            Propagate towards a target date.
        
            Simple propagators use only the target date as the specification for computing the propagated state. More feature rich
            propagators can consider other information and provide different operating modes or G-stop facilities to stop at
            pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.propagate` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                target (:class:`~org.orekit.time.AbsoluteDate`): target date towards which orbit state should be propagated
        
            Returns:
                propagated state
        
            Propagate from a start date towards a target date.
        
            Those propagators use a start date and a target date to compute the propagated state. For propagators using event
            detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is
            performed, without processing any event computation. Then complete propagation is performed from start date to target
            date.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.propagate` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                start (:class:`~org.orekit.time.AbsoluteDate`): start date from which orbit state should be propagated
                target (:class:`~org.orekit.time.AbsoluteDate`): target date to which orbit state should be propagated
        
            Returns:
                propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
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
    def resetInitialState(self, spacecraftState: SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...

_PythonFieldAbstractPropagator__T = typing.TypeVar('_PythonFieldAbstractPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractPropagator(FieldAbstractPropagator[_PythonFieldAbstractPropagator__T], typing.Generic[_PythonFieldAbstractPropagator__T]):
    """
    public class PythonFieldAbstractPropagator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.FieldAbstractPropagator`<T>
    """
    def __init__(self, field: org.hipparchus.Field[_PythonFieldAbstractPropagator__T]): ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, d: _addEventDetector__D) -> None: ...
    def clearEventsDetectors(self) -> None:
        """
            Remove all events detectors.
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`,
                :meth:`~org.orekit.propagation.FieldPropagator.getEventsDetectors`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldAbstractPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldAbstractPropagator__T]]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractPropagator__T]) -> FieldSpacecraftState[_PythonFieldAbstractPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractPropagator__T]) -> FieldSpacecraftState[_PythonFieldAbstractPropagator__T]: ...
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

_PythonFieldBoundedPropagator__T = typing.TypeVar('_PythonFieldBoundedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldBoundedPropagator(FieldBoundedPropagator[_PythonFieldBoundedPropagator__T], typing.Generic[_PythonFieldBoundedPropagator__T]):
    """
    public class PythonFieldBoundedPropagator<T extends :class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.FieldBoundedPropagator`<T>
    """
    def __init__(self): ...
    def addAdditionalStateProvider(self, fieldAdditionalStateProvider: FieldAdditionalStateProvider[_PythonFieldBoundedPropagator__T]) -> None: ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, d: _addEventDetector__D) -> None: ...
    def clearEventsDetectors(self) -> None:
        """
            Remove all events detectors.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.clearEventsDetectors` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.addEventDetector`,
                :meth:`~org.orekit.propagation.FieldPropagator.getEventsDetectors`
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[FieldAdditionalStateProvider[_PythonFieldBoundedPropagator__T]]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getAttitudeProvider` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldBoundedPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldBoundedPropagator__T]]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getFrame` in interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]: ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getManagedAdditionalStates` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]: ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]: ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_PythonFieldBoundedPropagator__T]: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_PythonFieldBoundedPropagator__T]: ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which an :class:`~org.orekit.propagation.FieldAdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.FieldPropagator.addAdditionalStateProvider` method. If the propagator is an
            :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`, the states for which a set of
            :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addAdditionalDerivativesProvider` method
            are also counted as managed additional states.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.FieldPropagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.resetState` method is called at an event
            occurrence and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.isAdditionalStateManaged` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Parameters:
                name (:class:`~org.orekit.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]: ...
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
    def resetInitialState(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldBoundedPropagator__T]) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.setAttitudeProvider` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation")``.

    AbstractMatricesHarvester: typing.Type[AbstractMatricesHarvester]
    AbstractPropagator: typing.Type[AbstractPropagator]
    AbstractStateCovarianceInterpolator: typing.Type[AbstractStateCovarianceInterpolator]
    AbstractStateModifier: typing.Type[AbstractStateModifier]
    AdditionalStateProvider: typing.Type[AdditionalStateProvider]
    BoundedPropagator: typing.Type[BoundedPropagator]
    EphemerisGenerator: typing.Type[EphemerisGenerator]
    FieldAbstractPropagator: typing.Type[FieldAbstractPropagator]
    FieldAbstractStateModifier: typing.Type[FieldAbstractStateModifier]
    FieldAdditionalStateProvider: typing.Type[FieldAdditionalStateProvider]
    FieldBoundedPropagator: typing.Type[FieldBoundedPropagator]
    FieldEphemerisGenerator: typing.Type[FieldEphemerisGenerator]
    FieldPropagator: typing.Type[FieldPropagator]
    FieldSpacecraftState: typing.Type[FieldSpacecraftState]
    FieldSpacecraftStateInterpolator: typing.Type[FieldSpacecraftStateInterpolator]
    FieldStateCovariance: typing.Type[FieldStateCovariance]
    MatricesHarvester: typing.Type[MatricesHarvester]
    PropagationType: typing.Type[PropagationType]
    Propagator: typing.Type[Propagator]
    PropagatorsParallelizer: typing.Type[PropagatorsParallelizer]
    PythonAbstractMatricesHarvester: typing.Type[PythonAbstractMatricesHarvester]
    PythonAbstractPropagator: typing.Type[PythonAbstractPropagator]
    PythonAbstractStateModifier: typing.Type[PythonAbstractStateModifier]
    PythonAdditionalStateProvider: typing.Type[PythonAdditionalStateProvider]
    PythonBoundedPropagator: typing.Type[PythonBoundedPropagator]
    PythonEphemerisGenerator: typing.Type[PythonEphemerisGenerator]
    PythonFieldAbstractPropagator: typing.Type[PythonFieldAbstractPropagator]
    PythonFieldAdditionalStateProvider: typing.Type[PythonFieldAdditionalStateProvider]
    PythonFieldBoundedPropagator: typing.Type[PythonFieldBoundedPropagator]
    PythonFieldEphemerisGenerator: typing.Type[PythonFieldEphemerisGenerator]
    PythonFieldPropagator: typing.Type[PythonFieldPropagator]
    PythonMatricesHarvester: typing.Type[PythonMatricesHarvester]
    PythonPropagator: typing.Type[PythonPropagator]
    SpacecraftState: typing.Type[SpacecraftState]
    SpacecraftStateInterpolator: typing.Type[SpacecraftStateInterpolator]
    StateCovariance: typing.Type[StateCovariance]
    StateCovarianceBlender: typing.Type[StateCovarianceBlender]
    StateCovarianceKeplerianHermiteInterpolator: typing.Type[StateCovarianceKeplerianHermiteInterpolator]
    StateCovarianceMatrixProvider: typing.Type[StateCovarianceMatrixProvider]
    analytical: org.orekit.propagation.analytical.__module_protocol__
    class-use: org.orekit.propagation.class-use.__module_protocol__
    conversion: org.orekit.propagation.conversion.__module_protocol__
    events: org.orekit.propagation.events.__module_protocol__
    integration: org.orekit.propagation.integration.__module_protocol__
    numerical: org.orekit.propagation.numerical.__module_protocol__
    sampling: org.orekit.propagation.sampling.__module_protocol__
    semianalytical: org.orekit.propagation.semianalytical.__module_protocol__
