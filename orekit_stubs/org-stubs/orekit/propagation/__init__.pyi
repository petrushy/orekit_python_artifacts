
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.analysis.polynomials
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation.analytical
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
    Abstract class for orbit and state covariance interpolator.
    
    Also see:
        Orbit, StateCovariance,
        TimeStampedPair
    """
    DEFAULT_POSITION_ANGLE: typing.ClassVar[org.orekit.orbits.PositionAngleType] = ...
    """
    Default position angle for covariance expressed in Cartesian elements.
    """
    COLUMN_DIM: typing.ClassVar[int] = ...
    """
    Default column dimension for position-velocity state covariance.
    
    Also see:
        constant
    
    
    """
    ROW_DIM: typing.ClassVar[int] = ...
    """
    Default row dimension for position-velocity state covariance.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], lOFType: org.orekit.frames.LOFType): ...
    def getOrbitInterpolator(self) -> org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit]:
        """
        Get orbit interpolator.
        
        Returns:
            orbit interpolator.
        
        
        """
        ...
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
    def getSubInterpolators(self) -> java.util.List[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStamped]]: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeStamped], typing.Sequence[org.orekit.time.TimeStamped], typing.Set[org.orekit.time.TimeStamped]]) -> org.orekit.time.TimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.TimeStamped]) -> org.orekit.time.TimeStamped: ...
    @typing.overload
    def interpolate(self, abstractTimeInterpolator: org.orekit.time.AbstractTimeInterpolator.InterpolationData) -> org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, 'StateCovariance']: ...

_AdditionalDataProvider__T = typing.TypeVar('_AdditionalDataProvider__T')  # <T>
class AdditionalDataProvider(typing.Generic[_AdditionalDataProvider__T]):
    """
    This interface allows to modify SpacecraftState and set up additional data.
    
    A data can be any type of java Object (i.e., double[], String, class, etc.)
    
    Propagator generate SpacecraftState that contain at least orbit, attitude, and mass. These states may however also contain addAdditionalData. Instances of classes implementing this interface are intended to be registered to propagators so they can either modify the basic components (orbit, attitude and mass) or add additional data incrementally after having computed the basic components.
    
    Some additional data may depend on previous additional data to be already available the before they can be computed. It may even be impossible to compute some of these additional data at some time if they depend on conditions that are fulfilled only after propagation as started or some event has occurred. As the propagator builds the complete state incrementally, looping over the registered providers, it must call their update methods in an order that fulfill these dependencies that may be time-dependent and are not related to the order in which the providers are registered to the propagator. This reordering is performed each time the complete state is built, using a yield mechanism. The propagator first pushes all providers in a stack and then empty the stack, one provider at a time, taking care to select only providers that do not yields when asked. Consider for example a case where providers A, B and C have been registered and provider B needs in fact the additional data generated by provider C. Then when a complete state is built, the propagator puts the three providers in a new stack, and then starts the incremental generation of additional data. It first checks provider A which does not yield so it is popped from the stack and the additional data it generates is added. Then provider B is checked, but it yields because state from provider C is not yet available. So propagator checks provider C which does not yield, so it is popped out of the stack and applied. At this stage, provider B is the only remaining one in the stack, so it is checked again, but this time it does not yield because the state from provider C is available as it has just been added, so provider B is popped from the stack and applied. The stack is now empty and the propagator can return the completed state.
    
    It is possible that at some stages in the propagation, a subset of the providers registered to a propagator all yield and cannot update the data. This happens for example during the initialization phase of a propagator that computes State Transition Matrices or Jacobian matrices. These features are managed as secondary equations in the ODE integrator, and initialized after the primary equations (which correspond to orbit) have been initialized. So when the primary equation are initialized, the providers that depend on the secondary state will all yield. This behavior is expected. Another case occurs when users set up additional data that induce a dependency loop (data A depending on data B which depends on data C which depends on data A). In this case, the three corresponding providers will wait for each other and indefinitely yield. This second case is a deadlock and results from a design error of the additional data management at application level. The propagator cannot know it in advance if a subset of providers that all yield is normal or not. So at propagator level, when either situation is detected, the propagator just gives up and returns the most complete state it was able to compute, without generating any error. Errors will indeed not be triggered in the first case (once the primary equations have been initialized, the secondary equations will be initialized too), and they will be triggered in the second case as soon as user attempts to retrieve an additional data that was not added.
    
    Since:
        13.0
    
    Also see:
        Propagator, AdditionalDerivativesProvider
    """
    def getAdditionalData(self, state: 'SpacecraftState') -> _AdditionalDataProvider__T:
        """
        Get the additional data.
        
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
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, initialState: 'SpacecraftState', target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the additional data provider at the start of propagation.
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state information at the start of propagation
            target (AbsoluteDate): date of propagation
        
        
        """
        ...
    def update(self, state: 'SpacecraftState') -> 'SpacecraftState':
        """
        Update a state.
        
        Parameters:
            state (SpacecraftState): spacecraft state to update
        
        Returns:
            updated state
        
        
        """
        ...
    def yields(self, state: 'SpacecraftState') -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional data being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final SpacecraftState state) {
             return !state.hasAdditionalData("STM");
         }
         
        
        The default implementation returns false, meaning that state data can be getAdditionalData immediately.
        
        Parameters:
            state (SpacecraftState): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

class CartesianToleranceProvider:
    """
    Interface to define integration tolerances for adaptive schemes (like the embedded Runge-Kutta ones) propagating the position-velocity vector and the mass, for a total of 7 primary dependent variables (in that order). The tolerances are given as an array of array: each row has 7 elements, whilst the first column is the absolute tolerances and the second the relative ones.
    
    Since:
        13.0
    
    Also see:
        NumericalPropagator,
        FieldNumericalPropagator,
        CartesianToleranceProvider
    """
    DEFAULT_ABSOLUTE_MASS_TOLERANCE: typing.ClassVar[float] = ...
    """
    Default absolute tolerance for mass integration.
    
    Also see:
        constant
    
    
    """
    _getTolerances_1__T = typing.TypeVar('_getTolerances_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_3__T = typing.TypeVar('_getTolerances_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_5__T = typing.TypeVar('_getTolerances_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTolerances(self, position: org.hipparchus.geometry.euclidean.threed.Vector3D, velocity: org.hipparchus.geometry.euclidean.threed.Vector3D) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Retrieve the integration tolerances given reference position and velocity vectors.
        
        Parameters:
            position (Vector3D): reference position vector
            velocity (Vector3D): reference velocity vector
        
        Returns:
            absolute and relative tolerances
        
        """
        ...
    @typing.overload
    def getTolerances(self, position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_1__T], velocity: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_1__T]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Retrieve the integration tolerances given reference position and velocity Field vectors.
        
        Parameters:
            position (FieldVector3D<T> position): reference position vector
            velocity (FieldVector3D<T> velocity): reference velocity vector
        
        Returns:
            absolute and relative tolerances
        
        """
        ...
    @typing.overload
    def getTolerances(self, cartesianOrbit: org.orekit.orbits.CartesianOrbit) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Retrieve the integration tolerances given a reference Cartesian orbit.
        
        Parameters:
            cartesianOrbit (CartesianOrbit): reference orbit
        
        Returns:
            absolute and relative tolerances
        
        Retrieve the integration tolerances given a reference absolute position-velocity vector.
        
        Parameters:
            absolutePVCoordinates (AbsolutePVCoordinates): reference position-velocity
        
        Returns:
            absolute and relative tolerances
        
        """
        ...
    @typing.overload
    def getTolerances(self, fieldCartesianOrbit: org.orekit.orbits.FieldCartesianOrbit[_getTolerances_3__T]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Retrieve the integration tolerances given a reference Cartesian orbit.
        
        Parameters:
            cartesianOrbit (FieldCartesianOrbit<T> cartesianOrbit): reference orbit
        
        Returns:
            absolute and relative tolerances
        
        Retrieve the integration tolerances given a reference absolute position-velocity vector.
        
        Parameters:
            absolutePVCoordinates (FieldAbsolutePVCoordinates<T> absolutePVCoordinates): reference position-velocity
        
        Returns:
            absolute and relative tolerances
        
        
        """
        ...
    @typing.overload
    def getTolerances(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_getTolerances_5__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def of(double: float) -> 'CartesianToleranceProvider':
        """
        Build a provider based on expected errors for position, velocity and mass respectively.
        
        The tolerances are only orders of magnitude, and integrator tolerances are only local estimates, not global ones. So some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will guarantee a 1mm error position after several orbits integration.
        
        Parameters:
            dP (double): expected position error
            dV (double): expected velocity error
            dM (double): expected mass error
        
        Returns:
            tolerance provider
        
        Build a provider based on expected errors for position only.
        
        The tolerances are only orders of magnitude, and integrator tolerances are only local estimates, not global ones. So some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will guarantee a 1mm error position after several orbits integration.
        
        Parameters:
            dP (double): expected position error
        
        Returns:
            tolerance provider
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(double: float, double2: float, double3: float) -> 'CartesianToleranceProvider': ...

class EphemerisGenerator:
    """
    Generator for ephemerides.
    
    This interface is mainly implemented by nested classes within propagators. These classes monitor the ongoing propagation and stores in memory all the necessary data. Once the initial propagation has completed, the data stored allows them to build an BoundedPropagator that can be used to rerun the propagation (perhaps with different event detectors and step handlers) without doing the full computation.
    
    Analytical propagators will mainly store only the start and stop date and the model itself, so ephemeris will just call the model back. Integration-based propagators will mainly store the OrekitStepInterpolator at each step so the ephemeris can select the proper interpolator and evaluate it for any date covered by the initial propagation.
    
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

_FieldAdditionalDataProvider__O = typing.TypeVar('_FieldAdditionalDataProvider__O')  # <O>
_FieldAdditionalDataProvider__T = typing.TypeVar('_FieldAdditionalDataProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdditionalDataProvider(typing.Generic[_FieldAdditionalDataProvider__O, _FieldAdditionalDataProvider__T]):
    """
    This interface allows to modify FieldSpacecraftState and set up additional data.
    
    FieldPropagator generate FieldSpacecraftState that contain at least orbit, attitude, and mass. These states may however also contain addAdditionalData additional data}. Instances of classes implementing this interface are intended to be registered to propagators so they can either modify the basic components (orbit, attitude and mass) or add additional data incrementally after having computed the basic components.
    
    Some additional data may depend on previous additional data to be already available the before they can be computed. It may even be impossible to compute some of these additional data at some time if they depend on conditions that are fulfilled only after propagation as started or some event has occurred. As the propagator builds the complete state incrementally, looping over the registered providers, it must call their update methods in an order that fulfill these dependencies that may be time-dependent and are not related to the order in which the providers are registered to the propagator. This reordering is performed each time the complete state is built, using a yield mechanism. The propagator first pushes all providers in a stack and then empty the stack, one provider at a time, taking care to select only providers that do not yields when asked. Consider for example a case where providers A, B and C have been registered and provider B needs in fact the additional data generated by provider C. Then when a complete state is built, the propagator puts the three providers in a new stack, and then starts the incremental generation of additional data. It first checks provider A which does not yield so it is popped from the stack and the additional data it generates is added. Then provider B is checked, but it yields because data from provider C is not yet available. So propagator checks provider C which does not yield, so it is popped out of the stack and applied. At this stage, provider B is the only remaining one in the stack, so it is checked again, but this time it does not yield because the data from provider C is available as it has just been added, so provider B is popped from the stack and applied. The stack is now empty and the propagator can return the completed state.
    
    It is possible that at some stages in the propagation, a subset of the providers registered to a propagator all yield and cannot update the data. This happens for example during the initialization phase of a propagator that computes State Transition Matrices or Jacobian matrices. These features are managed as secondary equations in the ODE integrator, and initialized after the primary equations (which correspond to orbit) have been initialized. So when the primary equation are initialized, the providers that depend on the secondary data will all yield. This behavior is expected. Another case occurs when users set up additional data that induce a dependency loop (data A depending on data B which depends on data C which depends on data A). In this case, the three corresponding providers will wait for each other and indefinitely yield. This second case is a deadlock and results from a design error of the additional data management at application level. The propagator cannot know it in advance if a subset of providers that all yield is normal or not. So at propagator level, when either situation is detected, the propagator just gives up and returns the most complete state it was able to compute, without generating any error. Errors will indeed not be triggered in the first case (once the primary equations have been initialized, the secondary equations will be initialized too), and they will be triggered in the second case as soon as user attempts to retrieve an additional data that was not added.
    
    Since:
        13.0
    
    Also see:
        FieldPropagator,
        FieldAdditionalDerivativesProvider,
        FieldAbstractStateModifier
    """
    def getAdditionalData(self, state: 'FieldSpacecraftState'[_FieldAdditionalDataProvider__T]) -> _FieldAdditionalDataProvider__O:
        """
        Get the additional data.
        
        Parameters:
            state (FieldSpacecraftState<FieldAdditionalDataProvider> state): spacecraft state to which additional data should correspond
        
        Returns:
            additional data corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, initialState: 'FieldSpacecraftState'[_FieldAdditionalDataProvider__T], target: org.orekit.time.FieldAbsoluteDate[_FieldAdditionalDataProvider__T]) -> None:
        """
        Initialize the additional state provider at the start of propagation.
        
        Parameters:
            initialState (FieldSpacecraftState<FieldAdditionalDataProvider> initialState): initial state information at the start of propagation
            target (FieldAbsoluteDate<FieldAdditionalDataProvider> target): date of propagation
        
        Since:
            11.2
        
        
        """
        ...
    def update(self, state: 'FieldSpacecraftState'[_FieldAdditionalDataProvider__T]) -> 'FieldSpacecraftState'[_FieldAdditionalDataProvider__T]:
        """
        Update a state.
        
        Parameters:
            state (FieldSpacecraftState<FieldAdditionalDataProvider> state): spacecraft state to update
        
        Returns:
            updated state
        
        Since:
            12.1
        
        
        """
        ...
    def yields(self, state: 'FieldSpacecraftState'[_FieldAdditionalDataProvider__T]) -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional data being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final FieldSpacecraftState state) {
             return state.hasAdditionalData("STM");
         }
         
        
        The default implementation returns false, meaning that the data can be getAdditionalData immediately.
        
        Parameters:
            state (FieldSpacecraftState<FieldAdditionalDataProvider> state): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        Since:
            11.1
        
        
        """
        ...

_FieldEphemerisGenerator__T = typing.TypeVar('_FieldEphemerisGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEphemerisGenerator(typing.Generic[_FieldEphemerisGenerator__T]):
    """
    Generator for ephemerides.
    
    This interface is mainly implemented by nested classes within propagators. These classes monitor the ongoing propagation and stores in memory all the necessary data. Once the initial propagation has completed, the data stored allows them to build an FieldBoundedPropagator that can be used to rerun the propagation (perhaps with different event detectors and step handlers) without doing the full computation.
    
    Analytical propagators will mainly store only the start and stop date and the model itself, so ephemeris will just call the model back. Integration-based propagators will mainly store the FieldOrekitStepInterpolator at each step so the ephemeris can select the proper interpolator and evaluate it for any date covered by the initial propagation.
    
    Since:
        11.0
    """
    def getGeneratedEphemeris(self) -> 'FieldBoundedPropagator'[_FieldEphemerisGenerator__T]:
        """
        Get the ephemeris generated during the propagation.
        
        Returns:
            generated ephemeris
        
        
        """
        ...

_FieldPropagator__T = typing.TypeVar('_FieldPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPropagator(org.orekit.utils.FieldPVCoordinatesProvider[_FieldPropagator__T], typing.Generic[_FieldPropagator__T]):
    """
    This interface provides a way to propagate an orbit at any time.
    
    This interface is the top-level abstraction for orbit propagation. It only allows propagation to a predefined date. It is implemented by analytical models which have no time limit, by orbit readers based on external data files, by numerical integrators using rich force models and by continuous models built after numerical integration has been completed and dense output data as been gathered.
    """
    DEFAULT_MASS: typing.ClassVar[float] = ...
    """
    Default mass.
    
    Also see:
        constant
    
    
    """
    def addAdditionalDataProvider(self, additionalDataProvider: FieldAdditionalDataProvider[typing.Any, _FieldPropagator__T]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Parameters:
            additionalDataProvider (FieldAdditionalDataProvider<?, FieldPropagator> additionalDataProvider): provider for additional data
        
        
        """
        ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, detector: _addEventDetector__D) -> None:
        """
        Add an event detector.
        
        Parameters:
            detector (D): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Remove all events detectors.
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
        Remove all step handlers.
        
        This convenience method is equivalent to call clear()
        
        Since:
            11.0
        
        Also see:
            getMultiplexer,
            clear
        
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[FieldAdditionalDataProvider[typing.Any, _FieldPropagator__T]]:
        """
        Get an unmodifiable list of providers for additional data.
        
        Returns:
            providers for the additional states
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get attitude provider.
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_FieldPropagator__T]:
        """
        Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           FieldEphemerisGenerator<T> generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           FieldBoundedPropagator<T> ephemeris = generator.getGeneratedEphemeris();
         
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_FieldPropagator__T]]:
        """
        Get all the events detectors that have been added.
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> 'FieldSpacecraftState'[_FieldPropagator__T]:
        """
        Get the propagator initial state.
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed data.
        
        Returns:
            names of all managed data
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_FieldPropagator__T]:
        """
        Get the multiplexer holding all step handlers.
        
        Returns:
            multiplexer holding all step handlers
        
        Since:
            11.0
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldPropagator__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<FieldPropagator> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPropagator__T]:
        """
        Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<FieldPropagator> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...
    def getVelocity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldPropagator__T]: ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which an FieldAdditionalDataProvider has been registered by calling the addAdditionalDataProvider method. If the propagator is an FieldAbstractIntegratedPropagator, the states for which a set of FieldAdditionalDerivativesProvider has been registered by calling the addAdditionalDerivativesProvider method are also counted as managed additional states.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T]) -> 'FieldSpacecraftState'[_FieldPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldPropagator__T]) -> 'FieldSpacecraftState'[_FieldPropagator__T]: ...
    def resetInitialState(self, state: 'FieldSpacecraftState'[_FieldPropagator__T]) -> None:
        """
        Reset the propagator initial state.
        
        Parameters:
            state (FieldSpacecraftState<FieldPropagator> state): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    @typing.overload
    def setStepHandler(self, t: _FieldPropagator__T, fieldOrekitFixedStepHandler: typing.Union[org.orekit.propagation.sampling.FieldOrekitFixedStepHandler[_FieldPropagator__T], typing.Callable[['FieldSpacecraftState'[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...
    @typing.overload
    def setStepHandler(self, fieldOrekitStepHandler: typing.Union[org.orekit.propagation.sampling.FieldOrekitStepHandler[_FieldPropagator__T], typing.Callable[[org.orekit.propagation.sampling.FieldOrekitStepInterpolator[org.hipparchus.CalculusFieldElement]], None]]) -> None: ...

_FieldSpacecraftState__T = typing.TypeVar('_FieldSpacecraftState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldSpacecraftState(org.orekit.time.FieldTimeStamped[_FieldSpacecraftState__T], org.orekit.time.FieldTimeShiftable['FieldSpacecraftState'[_FieldSpacecraftState__T], _FieldSpacecraftState__T], typing.Generic[_FieldSpacecraftState__T]):
    """
    This class is the representation of a complete state holding orbit, attitude and mass information at a given date, meant primarily for propagation.
    
    It contains an FieldOrbit, or a FieldAbsolutePVCoordinates if there is no definite central body, plus the current mass and attitude at the intrinsic FieldAbsoluteDate. Quantities are guaranteed to be consistent in terms of date and reference frame. The spacecraft state may also contain additional states, which are simply named double arrays which can hold any user-defined data.
    
    The state can be slightly shifted to close dates. This actual shift varies between FieldOrbit and FieldAbsolutePVCoordinates. For attitude it is a linear extrapolation taking the spin rate into account and no mass change. It is not intended as a replacement for proper orbit and attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
    The instance FieldSpacecraftState is guaranteed to be immutable.
    
    Also see:
        NumericalPropagator, SpacecraftState
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSpacecraftState__T], spacecraftState: 'SpacecraftState'): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldDataDictionary: org.orekit.utils.FieldDataDictionary[_FieldSpacecraftState__T], fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, fieldDataDictionary: org.orekit.utils.FieldDataDictionary[_FieldSpacecraftState__T], fieldArrayDictionary: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]): ...
    def addAdditionalData(self, name: str, value: typing.Any) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]:
        """
        Add an additional data.
        
        FieldSpacecraftState instances are immutable, so this method does not change the instance, but rather creates a new instance, which has the same orbit, attitude, mass and additional states as the original instance, except it also has the specified state. If the original instance already had an additional state with the same name, it will be overridden. If it did not have any additional state with that name, the new instance will have one more additional state than the original instance.
        
        Parameters:
            name (String): name of the additional data (names containing "orekit" * with any case are reserved for the library internal use)
            value (Object): value of the additional data
        
        Returns:
            a new instance, with the additional data added
        
        Also see:
            hasAdditionalData,
            getAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def addAdditionalStateDerivative(self, name: str, *value: _FieldSpacecraftState__T) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]:
        """
        Add an additional state derivative. FieldSpacecraftState instances are immutable, so this method does not change the instance, but rather creates a new instance, which has the same components as the original instance, except it also has the specified state derivative. If the original instance already had an additional state derivative with the same name, it will be overridden. If it did not have any additional state derivative with that name, the new instance will have one more additional state derivative than the original instance.
        
        Parameters:
            name (String): name of the additional state derivative
            value (FieldSpacecraftState...): value of the additional state derivative
        
        Returns:
            a new instance, with the additional state derivative added
        
        Also see:
            hasAdditionalStateDerivative,
            getAdditionalStateDerivative,
            getAdditionalStatesDerivatives
        
        
        """
        ...
    def ensureCompatibleAdditionalStates(self, state: 'FieldSpacecraftState'[_FieldSpacecraftState__T]) -> None:
        """
        Check if two instances have the same set of additional states available.
        
        Only the names and dimensions of the additional states are compared, not their values.
        
        Parameters:
            state (FieldSpacecraftState<FieldSpacecraftState> state): state to compare to instance
        
        Raises:
            MathIllegalArgumentException: if an additional state does not have the same dimension in both states
        
        
        """
        ...
    def getAbsPVA(self) -> org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T]:
        """
        Get the absolute position-velocity-acceleration.
        
        A state contains either an FieldAbsolutePVCoordinates or an FieldOrbit. Which one is present can be checked using isOrbitDefined.
        
        Returns:
            absolute position-velocity-acceleration
        
        Raises:
            OrekitIllegalStateException: if position-velocity-acceleration is null, which mean the state rather contains an
                FieldOrbit
        
        Also see:
            isOrbitDefined,
            getOrbit
        
        
        """
        ...
    def getAdditionalData(self, name: str) -> typing.Any:
        """
        Get an additional data.
        
        Parameters:
            name (String): name of the additional state
        
        Returns:
            value of the additional state
        
        Since:
            13.0
        
        Also see:
            addAdditionalData,
            hasAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def getAdditionalDataValues(self) -> org.orekit.utils.FieldDataDictionary[_FieldSpacecraftState__T]:
        """
        Get an unmodifiable map of additional states.
        
        Returns:
            unmodifiable map of additional states
        
        Since:
            11.1
        
        Also see:
            addAdditionalData,
            hasAdditionalData,
            getAdditionalData
        
        
        """
        ...
    def getAdditionalState(self, name: str) -> typing.MutableSequence[_FieldSpacecraftState__T]:
        """
        Get an additional state.
        
        Parameters:
            name (String): name of the additional state
        
        Returns:
            value of the additional state
        
        Also see:
            hasAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def getAdditionalStateDerivative(self, name: str) -> typing.MutableSequence[_FieldSpacecraftState__T]:
        """
        Get an additional state derivative.
        
        Parameters:
            name (String): name of the additional state derivative
        
        Returns:
            value of the additional state derivative
        
        Since:
            11.1
        
        Also see:
            addAdditionalStateDerivative,
            hasAdditionalStateDerivative,
            getAdditionalStatesDerivatives
        
        
        """
        ...
    def getAdditionalStatesDerivatives(self) -> org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]:
        """
        Get an unmodifiable map of additional states derivatives.
        
        Returns:
            unmodifiable map of additional states derivatives
        
        Since:
            11.1
        
        Also see:
            addAdditionalStateDerivative,
            hasAdditionalStateDerivative,
            getAdditionalStateDerivative
        
        
        """
        ...
    def getAttitude(self) -> org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]:
        """
        Get the attitude.
        
        Returns:
            the attitude.
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftState__T]:
        """
        Get the date.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the defining frame.
        
        Returns:
            the frame in which state is defined
        
        
        """
        ...
    def getMass(self) -> _FieldSpacecraftState__T:
        """
        Gets the current mass.
        
        Returns:
            the mass (kg)
        
        
        """
        ...
    def getOrbit(self) -> org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T]:
        """
        Get the current orbit.
        
        A state contains either an FieldAbsolutePVCoordinates or an FieldOrbit. Which one is present can be checked using isOrbitDefined.
        
        Returns:
            the orbit
        
        Raises:
            OrekitIllegalStateException: if orbit is null, which means the state rather contains an FieldAbsolutePVCoordinates
        
        Also see:
            isOrbitDefined,
            getAbsPVA
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPosition(self, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldSpacecraftState__T]: ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldSpacecraftState__T]:
        """
        Get the velocity in state definition frame.
        
        Returns:
            velocity in state definition frame
        
        Since:
            13.1
        
        
        """
        ...
    def hasAdditionalData(self, name: str) -> bool:
        """
        Check if an additional data is available.
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is available
        
        Also see:
            addAdditionalData,
            getAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def hasAdditionalStateDerivative(self, name: str) -> bool:
        """
        Check if an additional state derivative is available.
        
        Parameters:
            name (String): name of the additional state derivative
        
        Returns:
            true if the additional state derivative is available
        
        Also see:
            addAdditionalStateDerivative,
            getAdditionalStateDerivative,
            getAdditionalStatesDerivatives
        
        
        """
        ...
    def isOrbitDefined(self) -> bool:
        """
        Check if the state contains an orbit part.
        
        A state contains either an FieldAbsolutePVCoordinates or an FieldOrbit.
        
        Returns:
            true if state contains an orbit (in which case getOrbit will not
            throw an exception), or false if the state contains an absolut position-velocity-acceleration (in which case
            getAbsPVA will not throw an exception)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _FieldSpacecraftState__T: ...
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
    def toStaticTransform(self) -> org.orekit.frames.FieldStaticTransform[_FieldSpacecraftState__T]:
        """
        Compute the static transform from state defining frame to spacecraft frame.
        
        Returns:
            static transform from specified frame to current spacecraft frame
        
        Since:
            12.0
        
        Also see:
            toTransform
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def toTransform(self) -> org.orekit.frames.FieldTransform[_FieldSpacecraftState__T]:
        """
        Compute the transform from state defining frame to spacecraft frame.
        
        The spacecraft frame origin is at the point defined by the orbit, and its orientation is defined by the attitude.
        
        Returns:
            transform from specified frame to current spacecraft frame
        
        
        """
        ...
    def withAdditionalData(self, newAdditional: org.orekit.utils.FieldDataDictionary[_FieldSpacecraftState__T]) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]:
        """
        Create a new instance with input additional data.
        
        Parameters:
            newAdditional (FieldDataDictionary<FieldSpacecraftState> newAdditional): data
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...
    def withAdditionalStatesDerivatives(self, newAdditionalDot: org.orekit.utils.FieldArrayDictionary[_FieldSpacecraftState__T]) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]:
        """
        Create a new instance with input additional data.
        
        Parameters:
            newAdditionalDot (FieldArrayDictionary<FieldSpacecraftState> newAdditionalDot): additional derivatives
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...
    def withAttitude(self, newAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]:
        """
        Create a new instance with input attitude.
        
        Parameters:
            newAttitude (FieldAttitude<FieldSpacecraftState> newAttitude): attitude
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...
    def withMass(self, newMass: _FieldSpacecraftState__T) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]:
        """
        Create a new instance with input mass.
        
        Parameters:
            newMass (FieldSpacecraftState): mass
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...

_FieldSpacecraftStateInterpolator__KK = typing.TypeVar('_FieldSpacecraftStateInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldSpacecraftStateInterpolator(org.orekit.time.AbstractFieldTimeInterpolator[FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK], typing.Generic[_FieldSpacecraftStateInterpolator__KK]):
    """
    Generic class for spacecraft state interpolator.
    
    The user can specify what interpolator to use for each attribute of the spacecraft state. However, at least one interpolator for either orbit or absolute position-velocity-acceleration is needed. All the other interpolators can be left to null if the user do not want to interpolate these values.
    
    Also see:
        SpacecraftState
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
    def getAbsPVAInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]:
        """
        Get absolute position-velocity-acceleration interpolator.
        
        Returns:
            optional absolute position-velocity-acceleration interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getAdditionalStateInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]:
        """
        Get additional state interpolator.
        
        Returns:
            optional additional state interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getAttitudeInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.attitudes.FieldAttitude[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]:
        """
        Get attitude interpolator.
        
        Returns:
            optional attitude interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getMassInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.time.TimeStampedField[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]:
        """
        Get mass interpolator.
        
        Returns:
            optional mass interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getOrbitInterpolator(self) -> java.util.Optional[org.orekit.time.FieldTimeInterpolator[org.orekit.orbits.FieldOrbit[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]:
        """
        Get orbit interpolator.
        
        Returns:
            optional orbit interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getOutputFrame(self) -> org.orekit.frames.Frame:
        """
        Get output frame.
        
        Returns:
            output frame
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[org.orekit.time.FieldTimeInterpolator[org.orekit.time.FieldTimeStamped[_FieldSpacecraftStateInterpolator__KK], _FieldSpacecraftStateInterpolator__KK]]:
        """
        Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Specified by: getSubInterpolators in interface FieldTimeInterpolator
        
        Overrides: getSubInterpolators in class AbstractFieldTimeInterpolator
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.FieldTimeStamped], typing.Sequence[org.orekit.time.FieldTimeStamped], typing.Set[org.orekit.time.FieldTimeStamped]]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftStateInterpolator__KK], collection: typing.Union[java.util.Collection[FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK]], typing.Sequence[FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK]], typing.Set[FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK]]]) -> FieldSpacecraftState[_FieldSpacecraftStateInterpolator__KK]: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftStateInterpolator__KK], stream: java.util.stream.Stream[org.orekit.time.FieldTimeStamped]) -> org.orekit.time.FieldTimeStamped: ...

_FieldStateCovariance__T = typing.TypeVar('_FieldStateCovariance__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStateCovariance(org.orekit.time.FieldTimeStamped[_FieldStateCovariance__T], typing.Generic[_FieldStateCovariance__T]):
    """
    This class is the representation of a covariance matrix at a given date.
    
    Currently, the covariance only represents the orbital elements.
    
    It is possible to change the covariance frame by using the changeCovarianceFrame or changeCovarianceFrame method. These methods are based on Equations (18) and (20) of Covariance Transformations for Satellite Flight Dynamics Operations by David A. SVallado.
    
    Finally, covariance orbit type can be changed using the changeCovarianceType method.
    
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
    def changeCovarianceType(self, orbit: org.orekit.orbits.FieldOrbit[_FieldStateCovariance__T], outOrbitType: org.orekit.orbits.OrbitType, outAngleType: org.orekit.orbits.PositionAngleType) -> 'FieldStateCovariance'[_FieldStateCovariance__T]:
        """
        Get the covariance matrix in another orbit type.
        
        The covariance orbit type cannot be changed if the covariance matrix is expressed in a LOF or a non-pseudo inertial frame.
        
        As this type change uses the jacobian matrix of the transformation, it introduces a linear approximation. Hence, the current covariance matrix will not exactly match the new linearized case and the distribution will not follow a generalized Gaussian distribution anymore.
        
        This is based on equation (1) to (6) from "Vallado, D. A. (2004). Covariance transformations for satellite flight dynamics operations."
        
        Parameters:
            orbit (FieldOrbit<FieldStateCovariance> orbit): orbit to which the covariance matrix should correspond
            outOrbitType (OrbitType): target orbit type of the state covariance matrix
            outAngleType (PositionAngleType): target position angle type of the state covariance matrix
        
        Returns:
            a new covariance state, expressed in the target orbit type with the target position angle
        
        Also see:
            changeCovarianceFrame
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldStateCovariance__T]:
        """
        Get the date..
        
        Specified by: getDate in interface FieldTimeStamped
        
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
            getLOF
        
        
        """
        ...
    def getLOF(self) -> org.orekit.frames.LOF:
        """
        Get the covariance LOF type.
        
        Returns:
            the covariance LOF type (can be null)
        
        Also see:
            getFrame
        
        
        """
        ...
    def getMatrix(self) -> org.hipparchus.linear.FieldMatrix[_FieldStateCovariance__T]:
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
    def shiftedBy(self, field: org.hipparchus.Field[_FieldStateCovariance__T], orbit: org.orekit.orbits.FieldOrbit[_FieldStateCovariance__T], dt: _FieldStateCovariance__T) -> 'FieldStateCovariance'[_FieldStateCovariance__T]:
        """
        Get a time-shifted covariance matrix.
        
        The shifting model is a linearized, Keplerian one. In other words, it is based on a state transition matrix that is computed assuming Keplerian motion.
        
        Shifting is not intended as a replacement for proper covariance propagation, but should be sufficient for small time shifts or coarse accuracy.
        
        Parameters:
            field (Field<FieldStateCovariance> field): to which the elements belong
            orbit (FieldOrbit<FieldStateCovariance> orbit): orbit to which the covariance matrix should correspond
            dt (FieldStateCovariance): time shift in seconds
        
        Returns:
            a new covariance state, shifted with respect to the instance
        
        
        """
        ...
    def toStateCovariance(self) -> 'StateCovariance':
        """
        Get new state covariance instance.
        
        Returns:
            new state covariance instance.
        
        
        """
        ...

class LinearKeplerianCovarianceHandler(org.orekit.propagation.sampling.OrekitFixedStepHandler):
    """
    Class implementing step handlers to propagate orbital covariance using linearized Keplerian motion, no matter the propagation model. Although less precise than using the same perturbations than the propagator, it is more computationally performant.
    
    Since:
        13.1
    
    Also see:
        StateCovarianceMatrixProvider
    """
    def __init__(self, initialCovariance: 'StateCovariance'):
        """
        Constructor.
        
        Parameters:
            initialCovariance (StateCovariance): initial orbital covariance
        
        
        """
        ...
    def getStatesCovariances(self) -> java.util.List['StateCovariance']:
        """
        Gets a copy of the covariances.
        
        Returns:
            state covariances
        
        
        """
        ...
    def handleStep(self, currentState: 'SpacecraftState') -> None:
        """
        Description copied from interface: handleStep Handle the current step.
        
        Specified by: handleStep in interface OrekitFixedStepHandler
        
        Parameters:
            currentState (SpacecraftState): current state at step time
        
        
        """
        ...
    def init(self, s0: 'SpacecraftState', t: org.orekit.time.AbsoluteDate, dt: float) -> None:
        """
        Description copied from interface: init Initialize step handler at the start of a propagation.
        
        This method is called once at the start of the propagation. It may be used by the step handler to initialize some internal data if needed.
        
        Specified by: init in interface OrekitFixedStepHandler
        
        Parameters:
            s0 (SpacecraftState): initial state
            t (AbsoluteDate): target time for the integration
            dt (double): the duration in seconds of the fixed step. This value is positive even if propagation is backwards.
        
        
        """
        ...
    def toOrekitStepHandler(self) -> org.orekit.propagation.sampling.OrekitStepHandler:
        """
        Convert into a non-fixed step handler, based on the instance (so do not use it elsewhere for something else).
        
        Returns:
            fixed-step handler
        
        Also see:
            OrekitStepHandler
        
        
        """
        ...

class MatricesHarvester:
    """
    Interface for extracting State Transition Matrices and Jacobians matrices from SpacecraftState.
    
    The State Transition Matrix and Jacobians matrices with respect to propagation parameters are stored in the state as getAdditionalState. Each propagator and support classes have their own way to handle them. The interface leverages these differences which are implementation details and provides a higher level access to these matrices, regardless of how they were computed and stored.
    
    Since:
        11.1
    """
    def getJacobiansColumnsNames(self) -> java.util.List[str]:
        """
        Get the names of the parameters in the matrix returned by getParametersJacobian.
        
        Beware that the names of the parameters are fully known only once all force models have been set up and their parameters properly selected. Applications that retrieve the matrices harvester first and select the force model parameters to retrieve afterwards (but obviously before starting propagation) must take care to wait until the parameters have been set up before they call this method. Calling the method too early would return wrong results.
        
        The names are returned in the Jacobians matrix columns order
        
        Returns:
            names of the parameters (i.e. columns) of the Jacobian matrix
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get the orbit type used for the matrix computation.
        
        Returns:
            the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, state: 'SpacecraftState') -> org.hipparchus.linear.RealMatrix:
        """
        Get the Jacobian with respect to propagation parameters.
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get the position angle used for the matrix computation.
        
        Irrelevant if getOrbitType returns CARTESIAN.
        
        Returns:
            the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, state: 'SpacecraftState') -> org.hipparchus.linear.RealMatrix:
        """
        Extract state transition matrix from state.
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
            OrbitType.
        
        
        """
        ...
    def setReferenceState(self, reference: 'SpacecraftState') -> None:
        """
        Set up reference state.
        
        This method is called whenever the global propagation reference state changes. This corresponds to the start of propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering. Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not use it at all.
        
        Parameters:
            reference (SpacecraftState): reference state to set
        
        
        """
        ...

class PropagationType(java.lang.Enum['PropagationType']):
    """
    Enumerate to define the propagation type used by the propagator.
    
    This enumerate can also be used to define if the orbital state is defined with osculating or mean elements at the propagator initialization.
    """
    MEAN: typing.ClassVar['PropagationType'] = ...
    OSCULATING: typing.ClassVar['PropagationType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'PropagationType':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['PropagationType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (PropagationType c : PropagationType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Propagator(org.orekit.utils.PVCoordinatesProvider):
    """
    This interface provides a way to propagate an orbit at any time.
    
    This interface is the top-level abstraction for orbit propagation. It only allows propagation to a predefined date. It is implemented by analytical models which have no time limit, by orbit readers based on external data files, by numerical integrators using rich force models and by continuous models built after numerical integration has been completed and dense output data as been gathered.
    
    Note that one single propagator cannot be called from multiple threads. Its configuration can be changed as there is at least a resetInitialState method, and even propagators that do not support resetting state (like the TLEPropagator do cache some internal data during computation. However, as long as they are configured with independent building blocks (mainly event handlers and step handlers that may preserve some internal state), and as long as they are called from one thread only, they can be used in multi-threaded applications. Synchronizing several propagators to run in parallel is also possible using PropagatorsParallelizer.
    """
    DEFAULT_MASS: typing.ClassVar[float] = ...
    """
    Default mass.
    
    Also see:
        constant
    
    
    """
    def addAdditionalDataProvider(self, additionalDataProvider: AdditionalDataProvider[typing.Any]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Parameters:
            additionalDataProvider (AdditionalDataProvider<?> additionalDataProvider): provider for additional data
        
        
        """
        ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, detector: _addEventDetector__T) -> None:
        """
        Add an event detector.
        
        Parameters:
            detector (T): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Remove all events detectors.
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def clearStepHandlers(self) -> None:
        """
        Remove all step handlers.
        
        This convenience method is equivalent to call clear()
        
        Since:
            11.0
        
        Also see:
            getMultiplexer,
            clear
        
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[AdditionalDataProvider[typing.Any]]:
        """
        List<AdditionalDataProvider<?>> getAdditionalDataProviders()
        
        Get an unmodifiable list of providers for additional data.
        
        Returns:
            providers for the additional data
        
        
        """
        ...
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
            frames (Frames): the set of frames to use.
        
        Returns:
            attitude law.
        
        
        """
        ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
        Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           EphemerisGenerator generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
         
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]:
        """
        Get all the events detectors that have been added.
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> 'SpacecraftState':
        """
        Get the propagator initial state.
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed additional data.
        
        Returns:
            names of all managed additional data
        
        
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
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which a AdditionalDataProvider has been registered by calling the addAdditionalDataProvider method.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'SpacecraftState':
        """
        Propagate towards a target date.
        
        Simple propagators use only the target date as the specification for computing the propagated state. More feature rich propagators can consider other information and provide different operating modes or G-stop facilities to stop at pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
        Parameters:
            target (AbsoluteDate): target date towards which orbit state should be propagated
        
        Returns:
            propagated state
        
        Propagate from a start date towards a target date.
        
        Those propagators use a start date and a target date to compute the propagated state. For propagators using event detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is performed, without processing any event computation. Then complete propagation is performed from start date to target date.
        
        Parameters:
            start (AbsoluteDate): start date from which orbit state should be propagated
            target (AbsoluteDate): target date to which orbit state should be propagated
        
        Returns:
            propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> 'SpacecraftState': ...
    def resetInitialState(self, state: 'SpacecraftState') -> None:
        """
        Reset the propagator initial state.
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    @typing.overload
    def setStepHandler(self, h: float, handler: typing.Union[org.orekit.propagation.sampling.OrekitFixedStepHandler, typing.Callable]) -> None:
        """
        Set a single handler for fixed stepsizes.
        
        This convenience method is equivalent to call clear() followed by add(h, handler)
        
        Parameters:
            h (double): fixed stepsize (s)
            handler (OrekitFixedStepHandler): handler called at the end of each finalized step
        
        Since:
            11.0
        
        Also see:
            getMultiplexer,
            add
        
        """
        ...
    @typing.overload
    def setStepHandler(self, handler: typing.Union[org.orekit.propagation.sampling.OrekitStepHandler, typing.Callable]) -> None:
        """
        Set a single handler for variable stepsizes.
        
        This convenience method is equivalent to call clear() followed by add(handler)
        
        Parameters:
            handler (OrekitStepHandler): handler called at the end of each finalized step
        
        Since:
            11.0
        
        Also see:
            getMultiplexer,
            add
        
        
        """
        ...
    def setupMatricesComputation(self, stmName: str, initialStm: org.hipparchus.linear.RealMatrix, initialJacobianColumns: org.orekit.utils.DoubleArrayDictionary) -> MatricesHarvester:
        """
        Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
        If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
        The arguments for initial matrices must be compatible with the OrbitType and PositionAngleType that will be used by the propagator.
        
        The default implementation throws an exception as the method is not supported by all propagators.
        
        Parameters:
            stmName (String): State Transition Matrix state name
            initialStm (RealMatrix): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
            initialJacobianColumns (DoubleArrayDictionary): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                from the dictionary, the corresponding initial column is assumed to be 0
        
        Returns:
            harvester to retrieve computed matrices during and after propagation
        
        Since:
            11.1
        
        
        """
        ...

class PropagatorsParallelizer:
    """
    This class provides a way to propagate simultaneously several orbits.
    
    Multi-satellites propagation is based on multi-threading. Therefore, care must be taken so that all propagators can be run in a multi-thread context. This implies that all propagators are built independently and that they rely on force models that are also built independently. An obvious mistake would be to reuse a maneuver force model, as these models need to cache the firing/not-firing status. Objects used by force models like atmosphere models for drag force or others may also cache intermediate variables, so separate instances for each propagator must be set up.
    
    This class will create new threads for running the propagators. It adds a new MultiSatStepHandler to manage the steps all at once, in addition to the existing individual step handlers that are preserved.
    
    All propagators remain independent of each other (they don't even know they are managed by the parallelizer) and advance their simulation time following their own algorithm. The parallelizer will block them at the end of each step and allow them to continue in order to maintain synchronization. The MultiSatStepHandler will experience perfectly synchronized steps, but some propagators may already be slightly ahead of time as depicted in the following rendering; were simulation times flows from left to right:
    
        propagator 1   : -------------[++++current step++++]> | propagator 2   : ----[++++current step++++]---------> |           | ...                           |           | propagator n   : ---------[++++current step++++]----> |           | V           V global handler : -------------[global step]--------->
    
    The previous sketch shows that propagator 1 has already computed states up to the end of the propagation, but propagators 2 up to n are still late. The global step seen by the handler will be the common part between all propagators steps. Once this global step has been handled, the parallelizer will let the more late propagator (here propagator 2) to go one step further and a new global step will be computed and handled, until all propagators reach the end.
    
    This class does not provide multi-satellite events. As events may truncate steps and even reset state, all events (including multi-satellite events) are handled at a very low level within each propagators and cannot be managed from outside by the parallelizer. For accurate handling of multi-satellite events, the event detector should be registered within the propagator of one satellite and have access to an independent propagator (typically an analytical propagator or an ephemeris) of the other satellite. As the embedded propagator will be called by the detector which itself is called by the first propagator, it should really be a dedicated propagator and should not also appear as one of the parallelized propagators, otherwise conflicts will appear here.
    
    Since:
        9.0
    """
    @typing.overload
    def __init__(self, list: java.util.List[Propagator], double: float, multiSatFixedStepHandler: typing.Union[org.orekit.propagation.sampling.MultiSatFixedStepHandler, typing.Callable]): ...
    @typing.overload
    def __init__(self, list: java.util.List[Propagator], multiSatStepHandler: typing.Union[org.orekit.propagation.sampling.MultiSatStepHandler, typing.Callable]): ...
    def getPropagators(self) -> java.util.List[Propagator]:
        """
        Get an unmodifiable list of the underlying mono-satellite propagators.
        
        Returns:
            unmodifiable list of the underlying mono-satellite propagators
        
        
        """
        ...
    def propagate(self, start: org.orekit.time.AbsoluteDate, target: org.orekit.time.AbsoluteDate) -> java.util.List['SpacecraftState']:
        """
        Propagate from a start date towards a target date.
        
        Parameters:
            start (AbsoluteDate): start date from which orbit state should be propagated
            target (AbsoluteDate): target date to which orbit state should be propagated
        
        Returns:
            propagated states
        
        
        """
        ...

class SpacecraftState(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['SpacecraftState']):
    """
    This class is the representation of a complete state holding orbit, attitude and mass information at a given date, meant primarily for propagation.
    
    It contains an Orbit, or an AbsolutePVCoordinates if there is no definite central body, plus the current mass and attitude at the intrinsic AbsoluteDate. Quantities are guaranteed to be consistent in terms of date and reference frame. The spacecraft state may also contain additional data, which are simply named.
    
    The state can be slightly shifted to close dates. This actual shift varies between Orbit and AbsolutePVCoordinates. For attitude it is a linear extrapolation taking the spin rate into account and no mass change. It is not intended as a replacement for proper orbit and attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
    The instance SpacecraftState is guaranteed to be immutable.
    
    Also see:
        NumericalPropagator
    """
    DEFAULT_MASS: typing.ClassVar[float] = ...
    """
    Default mass.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, double: float, dataDictionary: org.orekit.utils.DataDictionary, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, double: float): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, double: float): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, double: float, dataDictionary: org.orekit.utils.DataDictionary, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    def addAdditionalData(self, name: str, value: typing.Any) -> 'SpacecraftState':
        """
        Add an additional data.
        
        SpacecraftState instances are immutable, so this method does not change the instance, but rather creates a new instance, which has the same orbit, attitude, mass and additional states as the original instance, except it also has the specified state. If the original instance already had an additional data with the same name, it will be overridden. If it did not have any additional state with that name, the new instance will have one more additional state than the original instance.
        
        Parameters:
            name (String): name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
            value (Object): value of the additional data
        
        Returns:
            a new instance, with the additional data added
        
        Since:
            13.0
        
        Also see:
            hasAdditionalData,
            getAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def addAdditionalStateDerivative(self, name: str, *value: float) -> 'SpacecraftState':
        """
        Add an additional state derivative.
        
        SpacecraftState instances are immutable, so this method does not change the instance, but rather creates a new instance, which has the same components as the original instance, except it also has the specified state derivative. If the original instance already had an additional state derivative with the same name, it will be overridden. If it did not have any additional state derivative with that name, the new instance will have one more additional state derivative than the original instance.
        
        Parameters:
            name (String): name of the additional state derivative (names containing "orekit" with any case are reserved for the library internal
                use)
            value (double...): value of the additional state derivative
        
        Returns:
            a new instance, with the additional state added
        
        Since:
            11.1
        
        Also see:
            hasAdditionalStateDerivative,
            getAdditionalStateDerivative,
            getAdditionalStatesDerivatives
        
        
        """
        ...
    def ensureCompatibleAdditionalStates(self, state: 'SpacecraftState') -> None:
        """
        Check if two instances have the same set of additional states available.
        
        Only the names and dimensions of the additional states are compared, not their values.
        
        Parameters:
            state (SpacecraftState): state to compare to instance
        
        Raises:
            MathIllegalStateException: if an additional state does not have the same dimension in both states
        
        
        """
        ...
    def getAbsPVA(self) -> org.orekit.utils.AbsolutePVCoordinates:
        """
        Get the absolute position-velocity-acceleration.
        
        A state contains either an AbsolutePVCoordinates or an Orbit. Which one is present can be checked using isOrbitDefined.
        
        Returns:
            absolute position-velocity-acceleration
        
        Raises:
            OrekitIllegalStateException: if position-velocity-acceleration is null, which mean the state rather contains an Orbit
        
        Also see:
            isOrbitDefined, getOrbit
        
        
        """
        ...
    def getAdditionalData(self, name: str) -> typing.Any:
        """
        Get an additional data.
        
        Parameters:
            name (String): name of the additional state
        
        Returns:
            value of the additional state
        
        Since:
            13.0
        
        Also see:
            addAdditionalData,
            hasAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def getAdditionalDataValues(self) -> org.orekit.utils.DataDictionary:
        """
        Get an unmodifiable map of additional data.
        
        Returns:
            unmodifiable map of additional data
        
        Since:
            11.1
        
        Also see:
            addAdditionalData,
            hasAdditionalData,
            getAdditionalState
        
        
        """
        ...
    def getAdditionalState(self, name: str) -> typing.MutableSequence[float]:
        """
        Get an additional state.
        
        Parameters:
            name (String): name of the additional state
        
        Returns:
            value of the additional state
        
        Also see:
            hasAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def getAdditionalStateDerivative(self, name: str) -> typing.MutableSequence[float]:
        """
        Get an additional state derivative.
        
        Parameters:
            name (String): name of the additional state derivative
        
        Returns:
            value of the additional state derivative
        
        Since:
            11.1
        
        Also see:
            addAdditionalStateDerivative,
            hasAdditionalStateDerivative,
            getAdditionalStatesDerivatives
        
        
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
            addAdditionalStateDerivative,
            hasAdditionalStateDerivative,
            getAdditionalStateDerivative
        
        
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
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the defining frame.
        
        Returns:
            the frame in which state is defined
        
        
        """
        ...
    def getMass(self) -> float:
        """
        Gets the current mass.
        
        Returns:
            the mass (kg)
        
        
        """
        ...
    def getOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Get the current orbit.
        
        A state contains either an AbsolutePVCoordinates or an Orbit. Which one is present can be checked using isOrbitDefined.
        
        Returns:
            the orbit
        
        Raises:
            OrekitIllegalStateException: if orbit is null, which means the state rather contains an AbsolutePVCoordinates
        
        Also see:
            isOrbitDefined,
            getAbsPVA
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the TimeStampedPVCoordinates in orbit definition frame.
        
        Compute the position and velocity of the satellite. This method caches its results, and recompute them only when the method is called with a new value for mu. The result is provided as a reference to the internally cached TimeStampedPVCoordinates, so the caller is responsible to copy it in a separate TimeStampedPVCoordinates if it needs to keep the value for a while.
        
        Returns:
            in orbit definition frame
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, outputFrame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the TimeStampedPVCoordinates in given output frame.
        
        Compute the position and velocity of the satellite. This method caches its results, and recompute them only when the method is called with a new value for mu. The result is provided as a reference to the internally cached TimeStampedPVCoordinates, so the caller is responsible to copy it in a separate TimeStampedPVCoordinates if it needs to keep the value for a while.
        
        Parameters:
            outputFrame (Frame): frame in which coordinates should be defined
        
        Returns:
            in given output frame
        
        
        """
        ...
    @typing.overload
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position in state definition frame.
        
        Returns:
            position in state definition frame
        
        Since:
            12.0
        
        Also see:
            getPVCoordinates
        
        """
        ...
    @typing.overload
    def getPosition(self, outputFrame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position in given output frame.
        
        Parameters:
            outputFrame (Frame): frame in which position should be defined
        
        Returns:
            position in given output frame
        
        Since:
            12.0
        
        Also see:
            getPVCoordinates
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the velocity in state definition frame.
        
        Returns:
            velocity in state definition frame
        
        Since:
            13.1
        
        Also see:
            getPVCoordinates
        
        
        """
        ...
    def hasAdditionalData(self, name: str) -> bool:
        """
        Check if an additional data is available.
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is available
        
        Also see:
            addAdditionalData,
            getAdditionalState,
            getAdditionalData,
            getAdditionalDataValues
        
        
        """
        ...
    def hasAdditionalStateDerivative(self, name: str) -> bool:
        """
        Check if an additional state derivative is available.
        
        Parameters:
            name (String): name of the additional state derivative
        
        Returns:
            true if the additional state derivative is available
        
        Since:
            11.1
        
        Also see:
            addAdditionalStateDerivative,
            getAdditionalStateDerivative,
            getAdditionalStatesDerivatives
        
        
        """
        ...
    def isOrbitDefined(self) -> bool:
        """
        Check if the state contains an orbit part.
        
        A state contains either an AbsolutePVCoordinates or an Orbit.
        
        Returns:
            true if state contains an orbit (in which case getOrbit will not throw
            an exception), or false if the state contains an absolut position-velocity-acceleration (in which case
            getAbsPVA will not throw an exception)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'SpacecraftState':
        """
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on simple models. For orbits, the model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. For attitude, a polynomial model is used. Neither mass nor additional states change. Shifting is not intended as a replacement for proper orbit and attitude propagation but should be sufficient for small time shifts or coarse accuracy.
        
        As a rough order of magnitude, the following table shows the extrapolation errors obtained between this simple shift method and an NumericalPropagator for a low Earth Sun Synchronous Orbit, with a 20x20 gravity field, Sun and Moon third bodies attractions, drag and solar radiation pressure. Beware that these results will be different for other orbits.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable) except for the mass and additional states which
            stay unchanged
        
        Get a time-shifted state.
        
        The state can be slightly shifted to close dates. This shift is based on simple models. For orbits, the model is a Keplerian one if no derivatives are available in the orbit, or Keplerian plus quadratic effect of the non-Keplerian acceleration if derivatives are available. For attitude, a polynomial model is used. Neither mass nor additional states change. Shifting is not intended as a replacement for proper orbit and attitude propagation but should be sufficient for small time shifts or coarse accuracy.
        
        As a rough order of magnitude, the following table shows the extrapolation errors obtained between this simple shift method and an NumericalPropagator for a low Earth Sun Synchronous Orbit, with a 20x20 gravity field, Sun and Moon third bodies attractions, drag and solar radiation pressure. Beware that these results will be different for other orbits.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (TimeOffset): time shift in seconds
        
        Returns:
            a new state, shifted with respect to the instance (which is immutable) except for the mass and additional states which
            stay unchanged
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'SpacecraftState': ...
    def toStaticTransform(self) -> org.orekit.frames.StaticTransform:
        """
        Compute the static transform from state defining frame to spacecraft frame.
        
        Returns:
            static transform from specified frame to current spacecraft frame
        
        Since:
            12.0
        
        Also see:
            toTransform
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def toTransform(self) -> org.orekit.frames.Transform:
        """
        Compute the transform from state defining frame to spacecraft frame.
        
        The spacecraft frame origin is at the point defined by the orbit (or absolute position-velocity-acceleration), and its orientation is defined by the attitude.
        
        Returns:
            transform from specified frame to current spacecraft frame
        
        
        """
        ...
    def withAdditionalData(self, dataDictionary: org.orekit.utils.DataDictionary) -> 'SpacecraftState':
        """
        Create a new instance with input additional data.
        
        Parameters:
            dataDictionary (DataDictionary): additional data
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...
    def withAdditionalStatesDerivatives(self, additionalStateDerivatives: org.orekit.utils.DoubleArrayDictionary) -> 'SpacecraftState':
        """
        Create a new instance with input additional data.
        
        Parameters:
            additionalStateDerivatives (DoubleArrayDictionary): additional state derivatives
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...
    def withAttitude(self, newAttitude: org.orekit.attitudes.Attitude) -> 'SpacecraftState':
        """
        Create a new instance with input attitude.
        
        Parameters:
            newAttitude (Attitude): attitude
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...
    def withMass(self, newMass: float) -> 'SpacecraftState':
        """
        Create a new instance with input mass.
        
        Parameters:
            newMass (double): mass
        
        Returns:
            new state
        
        Since:
            13.0
        
        
        """
        ...

class SpacecraftStateInterpolator(org.orekit.time.AbstractTimeInterpolator[SpacecraftState]):
    """
    Generic class for spacecraft state interpolator.
    
    The user can specify what interpolator to use for each attribute of the spacecraft state. However, at least one interpolator for either orbit or absolute position-velocity-acceleration is needed. All the other interpolators can be left to null if the user do not want to interpolate these values.
    
    Also see:
        SpacecraftState
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
    @staticmethod
    def checkSampleAndInterpolatorConsistency(sample: java.util.List[SpacecraftState], orbitInterpolatorIsPresent: bool, absPVInterpolatorIsPresent: bool) -> None:
        """
        Check that an interpolator exist for given sample state definition.
        
        Parameters:
            sample (List<SpacecraftState> sample): sample (non empty)
            orbitInterpolatorIsPresent (boolean): flag defining if an orbit interpolator has been defined for this instance
            absPVInterpolatorIsPresent (boolean): flag defining if an absolute position-velocity-acceleration interpolator has been defined for this instance
        
        Raises:
            OrekitIllegalArgumentException: if there is no defined interpolator for given sample spacecraft state definition type
        
        
        """
        ...
    @staticmethod
    def checkStatesDefinitionsConsistency(states: java.util.List[SpacecraftState]) -> None:
        """
        Check that all state are either orbit defined or based on absolute position-velocity-acceleration.
        
        Parameters:
            states (List<SpacecraftState> states): spacecraft state sample
        
        
        """
        ...
    def getAbsPVAInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.utils.AbsolutePVCoordinates]]:
        """
        Get absolute position-velocity-acceleration interpolator.
        
        Returns:
            optional absolute position-velocity-acceleration interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getAdditionalStateInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble]]:
        """
        Get additional state interpolator.
        
        Returns:
            optional additional state interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getAttitudeInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.attitudes.Attitude]]:
        """
        Get attitude interpolator.
        
        Returns:
            optional attitude interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getMassInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedDouble]]:
        """
        Get mass interpolator.
        
        Returns:
            optional mass interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getOrbitInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit]]:
        """
        Get orbit interpolator.
        
        Returns:
            optional orbit interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getOutputFrame(self) -> org.orekit.frames.Frame:
        """
        Get output frame.
        
        Returns:
            output frame
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStamped]]:
        """
        Get all lowest level interpolators implemented by this instance, otherwise return a list with this instance only.
        
        An example would be the spacecraft state interpolator which can use different interpolators for each of its attributes (orbit, absolute position-velocity-acceleration coordinates, mass...). In this case, it would return the list of all of these interpolators (or possibly all of their sub-interpolators if they were to use multiple interpolators themselves).
        
        Specified by: getSubInterpolators in interface TimeInterpolator
        
        Overrides: getSubInterpolators in class AbstractTimeInterpolator
        
        Returns:
            list of interpolators
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[SpacecraftState], typing.Sequence[SpacecraftState], typing.Set[SpacecraftState]]) -> SpacecraftState: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream[org.orekit.time.TimeStamped]) -> org.orekit.time.TimeStamped: ...

class StateCovariance(org.orekit.time.TimeStamped):
    """
    This class is the representation of a covariance matrix at a given date.
    
    Currently, the covariance only represents the orbital elements.
    
    It is possible to change the covariance frame by using the changeCovarianceFrame or changeCovarianceFrame method. These methods are based on Equations (18) and (20) of Covariance Transformations for Satellite Flight Dynamics Operations by David A. SVallado.
    
    Finally, covariance orbit type can be changed using the changeCovarianceType method.
    
    Since:
        11.3
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    State dimension.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, absoluteDate: org.orekit.time.AbsoluteDate, lOF: org.orekit.frames.LOF): ...
    @typing.overload
    def changeCovarianceFrame(self, orbit: org.orekit.orbits.Orbit, frame: org.orekit.frames.Frame) -> 'StateCovariance':
        """
        Get the covariance in a given local orbital frame.
        
        Changing the covariance frame is a linear process, this method does not introduce approximation unless a change in covariance orbit type is required.
        
        This is based on equation (18) to (20) "from Vallado, D. A. (2004). Covariance transformations for satellite flight dynamics operations."
        
        Parameters:
            orbit (Orbit): orbit to which the covariance matrix should correspond
            lofOut (LOF): output local orbital frame
        
        Returns:
            a new covariance state, expressed in the output local orbital frame
        
        Get the covariance in the output frame.
        
        Changing the covariance frame is a linear process, this method does not introduce approximation unless a change in covariance orbit type is required.
        
        This is based on equation (18) to (20) "from Vallado, D. A. (2004). Covariance transformations for satellite flight dynamics operations."
        
        Parameters:
            orbit (Orbit): orbit to which the covariance matrix should correspond
            frameOut (Frame): output frame
        
        Returns:
            a new covariance state, expressed in the output frame
        
        
        """
        ...
    @typing.overload
    def changeCovarianceFrame(self, orbit: org.orekit.orbits.Orbit, lOF: org.orekit.frames.LOF) -> 'StateCovariance': ...
    def changeCovarianceType(self, orbit: org.orekit.orbits.Orbit, outOrbitType: org.orekit.orbits.OrbitType, outAngleType: org.orekit.orbits.PositionAngleType) -> 'StateCovariance':
        """
        Get the covariance matrix in another orbit type.
        
        The covariance orbit type cannot be changed if the covariance matrix is expressed in a LOF or a non-pseudo inertial frame.
        
        As this type change uses the jacobian matrix of the transformation, it introduces a linear approximation. Hence, the current covariance matrix will not exactly match the new linearized case and the distribution will not follow a generalized Gaussian distribution anymore.
        
        This is based on equation (1) to (6) from "Vallado, D. A. (2004). Covariance transformations for satellite flight dynamics operations."
        
        Parameters:
            orbit (Orbit): orbit to which the covariance matrix should correspond
            outOrbitType (OrbitType): target orbit type of the state covariance matrix
            outAngleType (PositionAngleType): target position angle type of the state covariance matrix
        
        Returns:
            a new covariance state, expressed in the target orbit type with the target position angle
        
        Also see:
            changeCovarianceFrame
        
        
        """
        ...
    @staticmethod
    def checkFrameAndOrbitTypeConsistency(covarianceFrame: org.orekit.frames.Frame, inputType: org.orekit.orbits.OrbitType) -> None:
        """
        Check constructor's inputs consistency.
        
        Parameters:
            covarianceFrame (Frame): covariance frame (inertial or Earth fixed)
            inputType (OrbitType): orbit type of the covariance
        
        Raises:
            OrekitException: if input frame is not pseudo-inertial AND the orbit type is not Cartesian
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date..
        
        Specified by: getDate in interface TimeStamped
        
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
            getLOF
        
        
        """
        ...
    def getLOF(self) -> org.orekit.frames.LOF:
        """
        Get the covariance LOF type.
        
        Returns:
            the covariance LOF type (can be null)
        
        Also see:
            getFrame
        
        
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
    def getStm(initialOrbit: org.orekit.orbits.Orbit, dt: float) -> org.hipparchus.linear.RealMatrix:
        """
        Deprecated.
        since 13.1. If you must, do: final RealMatrix stm = MatrixUtils.createRealIdentityMatrix(STATE_DIMENSION); double
        contribution = initialOrbit.getMeanAnomalyDotWrtA() * dt; stm.setEntry(5, 0, contribution);
        Get the state transition matrix considering Keplerian contribution only and assuming equinoctial elements with mean
        anomaly.
        
        Parameters:
            initialOrbit (Orbit): orbit to which the initial covariance matrix should correspond
            dt (double): time difference between the two orbits
        
        Returns:
            the state transition matrix used to shift the covariance matrix
        
        
        """
        ...
    @staticmethod
    def inputAndOutputAreIdentical(inOrbitType: org.orekit.orbits.OrbitType, inAngleType: org.orekit.orbits.PositionAngleType, outOrbitType: org.orekit.orbits.OrbitType, outAngleType: org.orekit.orbits.PositionAngleType) -> bool:
        """
        Checks if input/output orbit and angle types are identical.
        
        Parameters:
            inOrbitType (OrbitType): input orbit type
            inAngleType (PositionAngleType): input angle type
            outOrbitType (OrbitType): output orbit type
            outAngleType (PositionAngleType): output angle type
        
        Returns:
            flag defining if input/output orbit and angle types are identical
        
        
        """
        ...
    @staticmethod
    def inputAndOutputOrbitTypesAreCartesian(inOrbitType: org.orekit.orbits.OrbitType, outOrbitType: org.orekit.orbits.OrbitType) -> bool:
        """
        Checks if input and output orbit types are both CARTESIAN.
        
        Parameters:
            inOrbitType (OrbitType): input orbit type
            outOrbitType (OrbitType): output orbit type
        
        Returns:
            flag defining if input and output orbit types are both CARTESIAN
        
        
        """
        ...
    def shiftedBy(self, orbit: org.orekit.orbits.Orbit, dt: float) -> 'StateCovariance':
        """
        Get a time-shifted covariance matrix.
        
        The shifting model is a linearized, Keplerian one. In other words, it is based on a state transition matrix that is computed assuming Keplerian motion.
        
        Shifting is not intended as a replacement for proper covariance propagation, but should be sufficient for small time shifts or coarse accuracy.
        
        Parameters:
            orbit (Orbit): orbit to which the covariance matrix should correspond
            dt (double): time shift in seconds
        
        Returns:
            a new covariance state, shifted with respect to the instance
        
        
        """
        ...

class AbstractMatricesHarvester(MatricesHarvester):
    """
    Base harvester between two-dimensional Jacobian matrices and one-dimensional getAdditionalState.
    
    Since:
        11.1
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    Deprecated. as of 13.1, use DEFAULT_STATE_DIMENSION State dimension, fixed to 6.
    
    Also see:
        constant
    
    
    """
    DEFAULT_STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    Default state dimension, equivalent to position and velocity vectors.
    
    Also see:
        constant
    
    
    """
    def freezeColumnsNames(self) -> None:
        """
        Freeze the names of the Jacobian columns.
        
        This method is called when propagation starts, i.e. when configuration is completed
        """
        ...
    def getInitialJacobianColumn(self, columnName: str) -> typing.MutableSequence[float]:
        """
        Get the initial column of Jacobian matrix with respect to named parameter.
        
        Parameters:
            columnName (String): name of the column
        
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
    def getParametersJacobian(self, state: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the Jacobian with respect to propagation parameters.
        
        Specified by: getParametersJacobian in interface MatricesHarvester
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getStateDimension(self) -> int:
        """
        Getter for the state dimension.
        
        Returns:
            state dimension
        
        Since:
            13.1
        
        
        """
        ...
    def getStateTransitionMatrix(self, state: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Extract state transition matrix from state.
        
        Specified by: getStateTransitionMatrix in interface MatricesHarvester
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
            OrbitType.
        
        
        """
        ...
    def getStmName(self) -> str:
        """
        Get the State Transition Matrix state name.
        
        Returns:
            State Transition Matrix state name
        
        
        """
        ...
    def setReferenceState(self, reference: SpacecraftState) -> None:
        """
        Set up reference state.
        
        This method is called whenever the global propagation reference state changes. This corresponds to the start of propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering. Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not use it at all.
        
        Specified by: setReferenceState in interface MatricesHarvester
        
        Parameters:
            reference (SpacecraftState): reference state to set
        
        
        """
        ...
    def toArray(self, matrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Set the STM data into an array.
        
        Parameters:
            matrix (double[][]): STM matrix
        
        Returns:
            an array containing the STM data
        
        Since:
            13.1
        
        
        """
        ...
    def toSquareMatrix(self, array: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.linear.RealMatrix:
        """
        Convert a flattened array to a square matrix.
        
        Parameters:
            array (double[]): input array
        
        Returns:
            the corresponding matrix
        
        Since:
            13.1
        
        
        """
        ...

class AbstractPropagator(Propagator):
    """
    Common handling of Propagator methods for propagators.
    
    This abstract class allows to provide easily the full set of Propagator methods, including all propagation modes support and discrete events support for any simple propagation method.
    """
    def addAdditionalDataProvider(self, provider: AdditionalDataProvider[typing.Any]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Specified by: addAdditionalDataProvider in interface Propagator
        
        Parameters:
            provider (AdditionalDataProvider<?> provider): provider for additional data
        
        
        """
        ...
    def clearMatricesComputation(self) -> None:
        """
        Erases the internal matrices harvester.
        
        Since:
            13.1
        
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[AdditionalDataProvider[typing.Any]]:
        """
        Get an unmodifiable list of providers for additional data.
        
        Specified by: getAdditionalDataProviders in interface Propagator
        
        Returns:
            providers for the additional data
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get attitude provider.
        
        Specified by: getAttitudeProvider in interface Propagator
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface Propagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> SpacecraftState:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface Propagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed additional data.
        
        Specified by: getManagedAdditionalData in interface Propagator
        
        Returns:
            names of all managed additional data
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer:
        """
        Get the multiplexer holding all step handlers.
        
        Specified by: getMultiplexer in interface Propagator
        
        Returns:
            multiplexer holding all step handlers
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which a AdditionalDataProvider has been registered by calling the addAdditionalDataProvider method.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface Propagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    @typing.overload
    def propagate(self, target: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
        Propagate towards a target date.
        
        Simple propagators use only the target date as the specification for computing the propagated state. More feature rich propagators can consider other information and provide different operating modes or G-stop facilities to stop at pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
        Specified by: propagate in interface Propagator
        
        Parameters:
            target (AbsoluteDate): target date towards which orbit state should be propagated
        
        Returns:
            propagated state
        
        
        """
        ...
    def removeAdditionalDataProvider(self, name: str) -> None:
        """
        Remove an additional data provider.
        
        Parameters:
            name (String): data name
        
        Since:
            13.1
        
        
        """
        ...
    def resetInitialState(self, state: SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface Propagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    def setupMatricesComputation(self, stmName: str, initialStm: org.hipparchus.linear.RealMatrix, initialJacobianColumns: org.orekit.utils.DoubleArrayDictionary) -> MatricesHarvester:
        """
        Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
        If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
        The arguments for initial matrices must be compatible with the OrbitType and PositionAngleType that will be used by the propagator.
        
        The default implementation throws an exception as the method is not supported by all propagators.
        
        Specified by: setupMatricesComputation in interface Propagator
        
        Parameters:
            stmName (String): State Transition Matrix state name
            initialStm (RealMatrix): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
            initialJacobianColumns (DoubleArrayDictionary): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                from the dictionary, the corresponding initial column is assumed to be 0
        
        Returns:
            harvester to retrieve computed matrices during and after propagation
        
        
        """
        ...
    def updateAdditionalData(self, original: SpacecraftState) -> SpacecraftState:
        """
        Update state by adding all additional data.
        
        Parameters:
            original (SpacecraftState): original state
        
        Returns:
            updated state, with all additional data included (including
            updateUnmanagedData data)
        
        Also see:
            addAdditionalDataProvider,
            updateUnmanagedData
        
        
        """
        ...

class AbstractStateModifier(AdditionalDataProvider[typing.MutableSequence[float]]):
    """
    Abstract base class for modifying state during propagation.
    
    This class is a specialized implementation of AdditionalDataProvider with a name set to the empty string and returning a null additional state.
    
    Beware that changing the state undercover from the propagator may have many side effects. Using this class should therefore be done cautiously.
    
    Since:
        12.1
    
    Also see:
        Propagator, AdditionalDataProvider
    """
    def __init__(self): ...
    def change(self, state: SpacecraftState) -> SpacecraftState:
        """
        Change main state.
        
        Parameters:
            state (SpacecraftState): spacecraft state to change
        
        Returns:
            changed state
        
        
        """
        ...
    def getAdditionalData(self, state: SpacecraftState) -> typing.MutableSequence[float]:
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
    def update(self, state: SpacecraftState) -> SpacecraftState:
        """
        Update a state.
        
        Specified by: update in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): spacecraft state to update
        
        Returns:
            updated state
        
        
        """
        ...

class BoundedPropagator(Propagator, org.orekit.utils.BoundedPVCoordinatesProvider):
    """
    This interface is intended for ephemerides valid only during a time range.
    
    This interface provides a mean to retrieve orbital parameters at any time within a given range. It should be implemented by orbit readers based on external data files and by continuous models built after numerical integration has been completed and dense output data as been gathered.
    """
    ...

_FieldAbstractPropagator__T = typing.TypeVar('_FieldAbstractPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractPropagator(FieldPropagator[_FieldAbstractPropagator__T], typing.Generic[_FieldAbstractPropagator__T]):
    """
    Common handling of Propagator methods for analytical propagators.
    
    This abstract class allows to provide easily the full set of Propagator methods, including all propagation modes support and discrete events support for any simple propagation method.
    """
    def addAdditionalDataProvider(self, additionalDataProvider: FieldAdditionalDataProvider[typing.Any, _FieldAbstractPropagator__T]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Specified by: addAdditionalDataProvider in interface FieldPropagator
        
        Parameters:
            additionalDataProvider (FieldAdditionalDataProvider<?, FieldAbstractPropagator> additionalDataProvider): provider for additional data
        
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[FieldAdditionalDataProvider[typing.Any, _FieldAbstractPropagator__T]]:
        """
        Get an unmodifiable list of providers for additional data.
        
        Specified by: getAdditionalDataProviders in interface FieldPropagator
        
        Returns:
            providers for the additional states
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get attitude provider.
        
        Specified by: getAttitudeProvider in interface FieldPropagator
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldAbstractPropagator__T]:
        """
        Field getter.
        
        Returns:
            field used
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface FieldPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> FieldSpacecraftState[_FieldAbstractPropagator__T]:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface FieldPropagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed data.
        
        Specified by: getManagedAdditionalData in interface FieldPropagator
        
        Returns:
            names of all managed data
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_FieldAbstractPropagator__T]:
        """
        Get the multiplexer holding all step handlers.
        
        Specified by: getMultiplexer in interface FieldPropagator
        
        Returns:
            multiplexer holding all step handlers
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which an FieldAdditionalDataProvider has been registered by calling the addAdditionalDataProvider method. If the propagator is an FieldAbstractIntegratedPropagator, the states for which a set of FieldAdditionalDerivativesProvider has been registered by calling the addAdditionalDerivativesProvider method are also counted as managed additional states.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface FieldPropagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldAbstractPropagator__T]) -> FieldSpacecraftState[_FieldAbstractPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractPropagator__T]) -> FieldSpacecraftState[_FieldAbstractPropagator__T]: ...
    def removeAdditionalDataProvider(self, name: str) -> None:
        """
        Remove an additional data provider.
        
        Parameters:
            name (String): data name
        
        Since:
            13.1
        
        
        """
        ...
    def resetInitialState(self, state: FieldSpacecraftState[_FieldAbstractPropagator__T]) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface FieldPropagator
        
        Parameters:
            state (FieldSpacecraftState<FieldAbstractPropagator> state): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface FieldPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    def updateAdditionalData(self, original: FieldSpacecraftState[_FieldAbstractPropagator__T]) -> FieldSpacecraftState[_FieldAbstractPropagator__T]:
        """
        Update state by adding all additional data.
        
        Parameters:
            original (FieldSpacecraftState<FieldAbstractPropagator> original): original state
        
        Returns:
            updated state, with all additional data included
        
        Also see:
            addAdditionalDataProvider
        
        
        """
        ...

_FieldAbstractStateModifier__T = typing.TypeVar('_FieldAbstractStateModifier__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractStateModifier(FieldAdditionalDataProvider[typing.MutableSequence[_FieldAbstractStateModifier__T], _FieldAbstractStateModifier__T], typing.Generic[_FieldAbstractStateModifier__T]):
    """
    Abstract base class for modifying state during propagation.
    
    This class is a specialized implementation of FieldAdditionalDataProvider with a name set to the empty string and returning a null additional data.
    
    Beware that changing the state undercover from the propagator may have many side effects. Using this class should therefore be done cautiously.
    
    Since:
        12.1
    
    Also see:
        Propagator, FieldAdditionalDataProvider
    """
    def __init__(self): ...
    def change(self, state: FieldSpacecraftState[_FieldAbstractStateModifier__T]) -> FieldSpacecraftState[_FieldAbstractStateModifier__T]:
        """
        Change main state.
        
        Parameters:
            state (FieldSpacecraftState<FieldAbstractStateModifier> state): spacecraft state to change
        
        Returns:
            changed state
        
        
        """
        ...
    def getAdditionalData(self, state: FieldSpacecraftState[_FieldAbstractStateModifier__T]) -> typing.MutableSequence[_FieldAbstractStateModifier__T]:
        """
        Get the additional data.
        
        Specified by: getAdditionalData in interface FieldAdditionalDataProvider
        
        Parameters:
            state (FieldSpacecraftState<FieldAbstractStateModifier> state): spacecraft state to which additional data should correspond
        
        Returns:
            additional data corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Specified by: getName in interface FieldAdditionalDataProvider
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def update(self, state: FieldSpacecraftState[_FieldAbstractStateModifier__T]) -> FieldSpacecraftState[_FieldAbstractStateModifier__T]:
        """
        Update a state.
        
        Specified by: update in interface FieldAdditionalDataProvider
        
        Parameters:
            state (FieldSpacecraftState<FieldAbstractStateModifier> state): spacecraft state to update
        
        Returns:
            updated state
        
        
        """
        ...

_FieldBoundedPropagator__T = typing.TypeVar('_FieldBoundedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBoundedPropagator(FieldPropagator[_FieldBoundedPropagator__T], org.orekit.utils.FieldBoundedPVCoordinatesProvider[_FieldBoundedPropagator__T], typing.Generic[_FieldBoundedPropagator__T]):
    """
    This interface is intended for ephemerides valid only during a time range.
    
    This interface provides a mean to retrieve orbital parameters at any time within a given range. It should be implemented by orbit readers based on external data files and by continuous models built after numerical integration has been completed and dense output data as been gathered.
    """
    ...

class PythonAbstractStateCovarianceInterpolator(AbstractStateCovarianceInterpolator):
    """
    Python implementation of the AbstractStateCovarianceInterpolator class. This class is part of the JCC Python interface and exposes abstract methods natively.
    """
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, int: int, double: float, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], lOFType: org.orekit.frames.LOFType): ...
    def computeInterpolatedCovarianceInOrbitFrame(self, uncertainStates: java.util.List[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, StateCovariance]], interpolatedOrbit: org.orekit.orbits.Orbit) -> StateCovariance:
        """
        Compute the interpolated covariance expressed in the interpolated orbit frame.
        
        Specified by: computeInterpolatedCovarianceInOrbitFrame in class AbstractStateCovarianceInterpolator
        
        Parameters:
            uncertainStates (List<TimeStampedPair<Orbit, StateCovariance>>): list of orbits and associated covariances
            interpolatedOrbit (Orbit): interpolated orbit
        
        Returns:
            interpolated covariance expressed in the interpolated orbit frame
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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

_PythonAdditionalDataProvider__T = typing.TypeVar('_PythonAdditionalDataProvider__T')  # <T>
class PythonAdditionalDataProvider(AdditionalDataProvider[_PythonAdditionalDataProvider__T], typing.Generic[_PythonAdditionalDataProvider__T]):
    """
    Python implementation of the AdditionalDataProvider interface. This class is part of the JCC Python interface and exposes all methods natively.
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAdditionalData(self, state: SpacecraftState) -> _PythonAdditionalDataProvider__T:
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

class PythonCartesianToleranceProvider(CartesianToleranceProvider):
    """
    Python implementation of the CartesianToleranceProvider interface. This class is part of the JCC Python interface and exposes all methods natively.
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getTolerances_0__T = typing.TypeVar('_getTolerances_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_2__T = typing.TypeVar('_getTolerances_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_4__T = typing.TypeVar('_getTolerances_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTolerances(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_0__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_0__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, cartesianOrbit: org.orekit.orbits.CartesianOrbit) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Description copied from interface: getTolerances Retrieve the integration tolerances given reference position and velocity vectors.
        
        Specified by: getTolerances in interface CartesianToleranceProvider
        
        Parameters:
            position (Vector3D): reference position vector
            velocity (Vector3D): reference velocity vector
        
        Returns:
            absolute and relative tolerances
        
        
        """
        ...
    @typing.overload
    def getTolerances(self, fieldCartesianOrbit: org.orekit.orbits.FieldCartesianOrbit[_getTolerances_2__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_getTolerances_4__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
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

class PythonEphemerisGenerator(EphemerisGenerator):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getGeneratedEphemeris(self) -> BoundedPropagator:
        """
        Get the ephemeris generated during the propagation.
        
        Specified by: getGeneratedEphemeris in interface EphemerisGenerator
        
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

_PythonFieldAdditionalDataProvider__O = typing.TypeVar('_PythonFieldAdditionalDataProvider__O')  # <O>
_PythonFieldAdditionalDataProvider__T = typing.TypeVar('_PythonFieldAdditionalDataProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdditionalDataProvider(FieldAdditionalDataProvider[_PythonFieldAdditionalDataProvider__O, _PythonFieldAdditionalDataProvider__T], typing.Generic[_PythonFieldAdditionalDataProvider__O, _PythonFieldAdditionalDataProvider__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAdditionalData(self, state: FieldSpacecraftState[_PythonFieldAdditionalDataProvider__T]) -> _PythonFieldAdditionalDataProvider__O:
        """
        Get the additional data.
        
        Specified by: getAdditionalData in interface FieldAdditionalDataProvider
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldAdditionalDataProvider> state): spacecraft state to which additional data should correspond
        
        Returns:
            additional data corresponding to spacecraft state
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Specified by: getName in interface FieldAdditionalDataProvider
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
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

_PythonFieldEphemerisGenerator__T = typing.TypeVar('_PythonFieldEphemerisGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEphemerisGenerator(FieldEphemerisGenerator[_PythonFieldEphemerisGenerator__T], typing.Generic[_PythonFieldEphemerisGenerator__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getGeneratedEphemeris(self) -> FieldBoundedPropagator[_PythonFieldEphemerisGenerator__T]:
        """
        Get the ephemeris generated during the propagation.
        
        Specified by: getGeneratedEphemeris in interface FieldEphemerisGenerator
        
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

_PythonFieldPropagator__T = typing.TypeVar('_PythonFieldPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldPropagator(FieldPropagator[_PythonFieldPropagator__T], typing.Generic[_PythonFieldPropagator__T]):
    def __init__(self): ...
    def addAdditionalDataProvider(self, additionalDataProvider: FieldAdditionalDataProvider[typing.Any, _PythonFieldPropagator__T]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Specified by: addAdditionalDataProvider in interface FieldPropagator
        
        Parameters:
            additionalDataProvider (FieldAdditionalDataProvider<?, PythonFieldPropagator> additionalDataProvider): provider for additional data
        
        
        """
        ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, detector: _addEventDetector__D) -> None:
        """
        Add an event detector.
        
        Specified by: addEventDetector in interface FieldPropagator
        
        Parameters:
            detector (D): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Remove all events detectors.
        
        Specified by: clearEventsDetectors in interface FieldPropagator
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[FieldAdditionalDataProvider[typing.Any, _PythonFieldPropagator__T]]:
        """
        Get an unmodifiable list of providers for additional data.
        
        Specified by: getAdditionalDataProviders in interface FieldPropagator
        
        Returns:
            providers for the additional states
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get attitude provider.
        
        Specified by: getAttitudeProvider in interface FieldPropagator
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldPropagator__T]:
        """
        Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           FieldEphemerisGenerator<T> generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           FieldBoundedPropagator<T> ephemeris = generator.getGeneratedEphemeris();
         
        
        Specified by: getEphemerisGenerator in interface FieldPropagator
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldPropagator__T]]:
        """
        Get all the events detectors that have been added.
        
        Specified by: getEventDetectors in interface FieldPropagator
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface FieldPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> FieldSpacecraftState[_PythonFieldPropagator__T]:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface FieldPropagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed data.
        
        Specified by: getManagedAdditionalData in interface FieldPropagator
        
        Returns:
            names of all managed data
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_PythonFieldPropagator__T]:
        """
        Get the multiplexer holding all step handlers.
        
        Specified by: getMultiplexer in interface FieldPropagator
        
        Returns:
            multiplexer holding all step handlers
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_PythonFieldPropagator__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface FieldPropagator
        
        Specified by: getPVCoordinates in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldPropagator> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which an FieldAdditionalDataProvider has been registered by calling the addAdditionalDataProvider method. If the propagator is an FieldAbstractIntegratedPropagator, the states for which a set of FieldAdditionalDerivativesProvider has been registered by calling the addAdditionalDerivativesProvider method are also counted as managed additional states.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface FieldPropagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
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
    def resetInitialState(self, state: FieldSpacecraftState[_PythonFieldPropagator__T]) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface FieldPropagator
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldPropagator> state): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface FieldPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...

class PythonMatricesHarvester(MatricesHarvester):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getJacobiansColumnsNames(self) -> java.util.List[str]:
        """
        Get the names of the parameters in the matrix returned by getParametersJacobian.
        
        Beware that the names of the parameters are fully known only once all force models have been set up and their parameters properly selected. Applications that retrieve the matrices harvester first and select the force model parameters to retrieve afterwards (but obviously before starting propagation) must take care to wait until the parameters have been set up before they call this method. Calling the method too early would return wrong results.
        
        The names are returned in the Jacobians matrix columns order
        
        Specified by: getJacobiansColumnsNames in interface MatricesHarvester
        
        Returns:
            names of the parameters (i.e. columns) of the Jacobian matrix
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Description copied from interface: getOrbitType Get the orbit type used for the matrix computation.
        
        Specified by: getOrbitType in interface MatricesHarvester
        
        Returns:
            the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, state: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the Jacobian with respect to propagation parameters.
        
        Specified by: getParametersJacobian in interface MatricesHarvester
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Description copied from interface: getPositionAngleType Get the position angle used for the matrix computation.
        
        Irrelevant if getOrbitType returns CARTESIAN.
        
        Specified by: getPositionAngleType in interface MatricesHarvester
        
        Returns:
            the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, state: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Extract state transition matrix from state.
        
        Specified by: getStateTransitionMatrix in interface MatricesHarvester
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
            OrbitType.
        
        
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
    def setReferenceState(self, reference: SpacecraftState) -> None:
        """
        Set up reference state.
        
        This method is called whenever the global propagation reference state changes. This corresponds to the start of propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering. Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not use it at all.
        
        Specified by: setReferenceState in interface MatricesHarvester
        
        Parameters:
            reference (SpacecraftState): reference state to set
        
        
        """
        ...

class PythonPropagator(Propagator):
    def __init__(self): ...
    def addAdditionalDataProvider(self, additionalDataProvider: AdditionalDataProvider[typing.Any]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Specified by: addAdditionalDataProvider in interface Propagator
        
        Parameters:
            additionalDataProvider (AdditionalDataProvider<?> additionalDataProvider): provider for additional data
        
        
        """
        ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, detector: _addEventDetector__T) -> None:
        """
        Add an event detector.
        
        Specified by: addEventDetector in interface Propagator
        
        Parameters:
            detector (T): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Remove all events detectors.
        
        Specified by: clearEventsDetectors in interface Propagator
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[AdditionalDataProvider[typing.Any]]:
        """
        Get an unmodifiable list of providers for additional data.
        
        Specified by: getAdditionalDataProviders in interface Propagator
        
        Returns:
            providers for the additional data
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get attitude provider.
        
        Specified by: getAttitudeProvider in interface Propagator
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
        Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           EphemerisGenerator generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
         
        
        Specified by: getEphemerisGenerator in interface Propagator
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]:
        """
        Get all the events detectors that have been added.
        
        Specified by: getEventDetectors in interface Propagator
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface Propagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> SpacecraftState:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface Propagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed additional data.
        
        Specified by: getManagedAdditionalData in interface Propagator
        
        Returns:
            names of all managed additional data
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer:
        """
        Get the multiplexer holding all step handlers.
        
        Specified by: getMultiplexer in interface Propagator
        
        Returns:
            multiplexer holding all step handlers
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface Propagator
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which a AdditionalDataProvider has been registered by calling the addAdditionalDataProvider method.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface Propagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
        Propagate towards a target date.
        
        Simple propagators use only the target date as the specification for computing the propagated state. More feature rich propagators can consider other information and provide different operating modes or G-stop facilities to stop at pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
        Specified by: propagate in interface Propagator
        
        Parameters:
            target (AbsoluteDate): target date towards which orbit state should be propagated
        
        Returns:
            propagated state
        
        Propagate from a start date towards a target date.
        
        Those propagators use a start date and a target date to compute the propagated state. For propagators using event detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is performed, without processing any event computation. Then complete propagation is performed from start date to target date.
        
        Specified by: propagate in interface Propagator
        
        Parameters:
            start (AbsoluteDate): start date from which orbit state should be propagated
            target (AbsoluteDate): target date to which orbit state should be propagated
        
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
    def pythonExtension(self, long: int) -> None: ...
    def resetInitialState(self, state: SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface Propagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    def setupMatricesComputation(self, stmName: str, initialStm: org.hipparchus.linear.RealMatrix, initialJacobianColumns: org.orekit.utils.DoubleArrayDictionary) -> MatricesHarvester:
        """
        Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
        If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
        The arguments for initial matrices must be compatible with the OrbitType and PositionAngleType that will be used by the propagator.
        
        The default implementation throws an exception as the method is not supported by all propagators.
        
        Specified by: setupMatricesComputation in interface Propagator
        
        Parameters:
            stmName (String): State Transition Matrix state name
            initialStm (RealMatrix): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
            initialJacobianColumns (DoubleArrayDictionary): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                from the dictionary, the corresponding initial column is assumed to be 0
        
        Returns:
            harvester to retrieve computed matrices during and after propagation
        
        
        """
        ...

class StateCovarianceBlender(AbstractStateCovarianceInterpolator):
    """
    State covariance blender.
    
    Its purpose is to interpolate state covariance between tabulated state covariances by using the concept of blending, exposed in : "Efficient Covariance Interpolation using Blending of Approximate State Error Transitions" by Sergei Tanygin.
    
    It propagates tabulated values to the interpolation date assuming a standard Keplerian model and then blend each propagated covariances using a smoothstep function.
    
    It gives accurate results as explained technical. In the very poorly tracked test case evolving in a highly dynamical environment mentioned in the linked thread, the user can expect at worst errors of less than 0.25% in position sigmas and less than 0.4% in velocity sigmas with steps of 40mn between tabulated values.
    
        class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.SmoothStepFactory?is`, SmoothStepFunction
    """
    @typing.overload
    def __init__(self, smoothStepFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], frame: org.orekit.frames.Frame, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType): ...
    @typing.overload
    def __init__(self, smoothStepFunction: org.hipparchus.analysis.polynomials.SmoothStepFactory.SmoothStepFunction, timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.orbits.Orbit], lOFType: org.orekit.frames.LOFType): ...

class StateCovarianceKeplerianHermiteInterpolator(AbstractStateCovarianceInterpolator):
    """
    State covariance Keplerian quintic interpolator.
    
    Its purpose is to interpolate state covariance between tabulated state covariances using polynomial interpolation. To do so, it uses a HermiteInterpolator and compute the first and second order derivatives at tabulated states assuming a standard Keplerian motion depending on given derivatives filter.
    
    It gives very accurate results as explained technical. In the very poorly tracked test case evolving in a highly dynamical environment mentioned in the linked thread, the user can expect at worst errors of less than 0.2% in position sigmas and less than 0.35% in velocity sigmas with steps of 40mn between tabulated values.
    
    However, note that this method does not guarantee the positive definiteness of the computed state covariance as opposed to StateCovarianceBlender.
    
        class:`~org.orekit.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.interpolation.HermiteInterpolator?is`, StateCovarianceBlender
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
        Get Filter defining if only the state covariance value are used or if first or/and second Keplerian derivatives should be used.
        
        Returns:
            Filter defining if only the state covariance value are used or if first or/and second Keplerian derivatives should be
            used.
        
        
        """
        ...

class StateCovarianceMatrixProvider(AdditionalDataProvider[org.hipparchus.linear.RealMatrix]):
    """
    Additional state provider for state covariance matrix.
    
    This additional state provider allows computing a propagated covariance matrix based on a user defined input state covariance matrix. The computation of the propagated covariance matrix uses the State Transition Matrix between the propagated spacecraft state and the initial state. As a result, the user must define the name of the provider for the State Transition Matrix.
    
    As the State Transition Matrix and the input state covariance matrix can be expressed in different orbit types, the user must specify both orbit types when building the covariance provider. In addition, the position angle used in both matrices must also be specified.
    
    In order to add this additional state provider to an orbit propagator, user must use the addAdditionalDataProvider method.
    
    For a given propagated spacecraft state, the propagated state covariance matrix is accessible through the method getStateCovariance
    
    Since:
        11.3
    """
    def __init__(self, additionalName: str, stmName: str, harvester: MatricesHarvester, covInit: StateCovariance):
        """
        Constructor.
        
        Parameters:
            additionalName (String): name of the additional state
            stmName (String): name of the state for State Transition Matrix
            harvester (MatricesHarvester): matrix harvester as returned by setupMatricesComputation(stmName, null, null)
            covInit (StateCovariance): initial state covariance
        
        
        """
        ...
    def getAdditionalData(self, state: SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the additional data.
        
        Specified by: getAdditionalData in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): spacecraft state to which additional data should correspond
        
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
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Specified by: getName in interface AdditionalDataProvider
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    @typing.overload
    def getStateCovariance(self, spacecraftState: SpacecraftState) -> StateCovariance:
        """
        Get the state covariance in the same frame/local orbital frame, orbit type and position angle as the initial covariance.
        
        Parameters:
            state (SpacecraftState): spacecraft state to which the covariance matrix should correspond
        
        Returns:
            the state covariance
        
        Also see:
            getStateCovariance,
            getStateCovariance
        
        Get the state covariance expressed in a given frame.
        
        The output covariance matrix is expressed in the same orbit type as getCovarianceOrbitType.
        
        Parameters:
            state (SpacecraftState): spacecraft state to which the covariance matrix should correspond
            frame (Frame): output frame for which the output covariance matrix must be expressed (must be inertial)
        
        Returns:
            the state covariance expressed in frame
        
        Also see:
            getStateCovariance,
            getStateCovariance
        
        Get the state covariance expressed in a given orbit type.
        
        Parameters:
            state (SpacecraftState): spacecraft state to which the covariance matrix should correspond
            orbitType (OrbitType): output orbit type
            angleType (PositionAngleType): output position angle (not used if orbitType equals CARTESIAN)
        
        Returns:
            the state covariance in orbitType and angleType
        
        Also see:
            getStateCovariance,
            getStateCovariance
        
        
        """
        ...
    @typing.overload
    def getStateCovariance(self, spacecraftState: SpacecraftState, frame: org.orekit.frames.Frame) -> StateCovariance: ...
    @typing.overload
    def getStateCovariance(self, spacecraftState: SpacecraftState, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> StateCovariance: ...
    def init(self, initialState: SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the additional data provider at the start of propagation.
        
        Specified by: init in interface AdditionalDataProvider
        
        Parameters:
            initialState (SpacecraftState): initial spacecraft state information at the start of propagation
            target (AbsoluteDate): date of propagation
        
        
        """
        ...
    def yields(self, state: SpacecraftState) -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional data being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final SpacecraftState state) {
             return !state.hasAdditionalData("STM");
         }
         
        
        The default implementation returns false, meaning that state data can be getAdditionalData immediately.
        
        The covariance matrix can be computed only if the State Transition Matrix state is available.
        
        Specified by: yields in interface AdditionalDataProvider
        
        Parameters:
            state (SpacecraftState): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

class ToleranceProvider(CartesianToleranceProvider):
    """
    Interface to define integration tolerances for adaptive schemes (like the embedded Runge-Kutta ones) propagating the position-velocity vector (or an equivalent set of coordinates) and the mass, for a total of 7 primary dependent variables (in that order). The tolerances are given as an array of array: each row has 7 elements, whilst the first column is the absolute tolerances and the second the relative ones.
    
    Since:
        13.0
    
    Also see:
        NumericalPropagator,
        FieldNumericalPropagator,
        CartesianToleranceProvider
    """
    @staticmethod
    def getDefaultToleranceProvider(dP: float) -> 'ToleranceProvider':
        """
        Defines a default tolerance provider. It is consistent with values from previous versions of Orekit obtained via other APIs.
        
        The tolerances are only orders of magnitude, and integrator tolerances are only local estimates, not global ones. So some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will guarantee a 1mm error position after several orbits integration.
        
        Parameters:
            dP (double): expected position error
        
        Returns:
            tolerances
        
        
        """
        ...
    _getTolerances_2__T = typing.TypeVar('_getTolerances_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_4__T = typing.TypeVar('_getTolerances_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_6__T = typing.TypeVar('_getTolerances_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_7__T = typing.TypeVar('_getTolerances_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_8__T = typing.TypeVar('_getTolerances_8__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTolerances(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Retrieve the integration tolerances given a reference orbit.
        
        Parameters:
            referenceOrbit (Orbit): orbit
            propagationOrbitType (OrbitType): orbit type for propagation (can be different from the input orbit one)
            positionAngleType (PositionAngleType): reference position angle type
        
        Returns:
            absolute and relative tolerances
        
        Retrieve the integration tolerances given a reference orbit.
        
        Parameters:
            referenceOrbit (Orbit): orbit
            propagationOrbitType (OrbitType): orbit type for propagation (can be different from the input orbit one)
        
        Returns:
            absolute and relative tolerances
        
        """
        ...
    @typing.overload
    def getTolerances(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_2__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_2__T]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Retrieve the integration tolerances given a reference Field orbit.
        
        Parameters:
            referenceOrbit (FieldOrbit<T> referenceOrbit): orbit
            propagationOrbitType (OrbitType): orbit type for propagation (can be different from the input orbit one)
            positionAngleType (PositionAngleType): reference position angle type
        
        Returns:
            absolute and relative tolerances
        
        Retrieve the integration tolerances given a reference Field orbit.
        
        Parameters:
            referenceOrbit (FieldOrbit<T> referenceOrbit): orbit
            propagationOrbitType (OrbitType): orbit type for propagation (can be different from the input orbit one)
        
        Returns:
            absolute and relative tolerances
        
        
        """
        ...
    @typing.overload
    def getTolerances(self, cartesianOrbit: org.orekit.orbits.CartesianOrbit) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldCartesianOrbit: org.orekit.orbits.FieldCartesianOrbit[_getTolerances_4__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_getTolerances_6__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_getTolerances_7__T], orbitType: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_getTolerances_8__T], orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def of(absoluteTolerance: float, relativeTolerance: float) -> 'ToleranceProvider':
        """
        Build a provider using a single value for absolute and respective tolerance respectively.
        
        Parameters:
            absoluteTolerance (double): absolute tolerance value to be used
            relativeTolerance (double): relative tolerance value to be used
        
        Returns:
            tolerance provider
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(cartesianToleranceProvider: typing.Union[CartesianToleranceProvider, typing.Callable]) -> 'ToleranceProvider':
        """
        Build a provider based on a tolerance provider for Cartesian coordinates.
        
        Orbits Jacobian matrices are used to get consistent errors on orbital parameters.
        
        
        Parameters:
            cartesianToleranceProvider (CartesianToleranceProvider): tolerance provider dedicated to Cartesian propagation
        
        Returns:
            tolerance provider
        
        
        """
        ...

class PythonAbstractMatricesHarvester(AbstractMatricesHarvester):
    def __init__(self, stmName: str, initialStm: org.hipparchus.linear.RealMatrix, initialJacobianColumns: org.orekit.utils.DoubleArrayDictionary):
        """
        Simple constructor.
        
        The arguments for initial matrices must be compatible with the OrbitType and PositionAngleType that will be used by propagator
        
        Parameters:
            stmName (String): State Transition Matrix state name
            initialStm (RealMatrix): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
            initialJacobianColumns (DoubleArrayDictionary): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                from the dictionary, the corresponding
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def freezeColumnsNames(self) -> None:
        """
        Freeze the names of the Jacobian columns.
        
        This method is called when propagation starts, i.e. when configuration is completed
        
        Specified by: freezeColumnsNames in class AbstractMatricesHarvester
        
        
        """
        ...
    def getJacobiansColumnsNames(self) -> java.util.List[str]:
        """
        Get the names of the parameters in the matrix returned by getParametersJacobian.
        
        Beware that the names of the parameters are fully known only once all force models have been set up and their parameters properly selected. Applications that retrieve the matrices harvester first and select the force model parameters to retrieve afterwards (but obviously before starting propagation) must take care to wait until the parameters have been set up before they call this method. Calling the method too early would return wrong results.
        
        The names are returned in the Jacobians matrix columns order
        
        Returns:
            names of the parameters (i.e. columns) of the Jacobian matrix
        
        
        """
        ...
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
        
        Irrelevant if getOrbitType returns CARTESIAN.
        
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
    def __init__(self): ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, detector: _addEventDetector__T) -> None:
        """
        Description copied from interface: addEventDetector Add an event detector.
        
        Parameters:
            detector (T): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Description copied from interface: clearEventsDetectors Remove all events detectors.
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
        Description copied from interface: getEphemerisGenerator Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           EphemerisGenerator generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
         
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]:
        """
        Description copied from interface: getEventDetectors Get all the events detectors that have been added.
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    @typing.overload
    def propagate(self, start: org.orekit.time.AbsoluteDate, target: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
        Description copied from interface: propagate Propagate from a start date towards a target date.
        
        Those propagators use a start date and a target date to compute the propagated state. For propagators using event detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is performed, without processing any event computation. Then complete propagation is performed from start date to target date.
        
        Parameters:
            start (AbsoluteDate): start date from which orbit state should be propagated
            target (AbsoluteDate): target date to which orbit state should be propagated
        
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
    def __init__(self): ...
    def change(self, state: SpacecraftState) -> SpacecraftState:
        """
        Description copied from class: change Change main state.
        
        Specified by: change in class AbstractStateModifier
        
        Parameters:
            state (SpacecraftState): spacecraft state to change
        
        Returns:
            changed state
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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

class PythonBoundedPropagator(BoundedPropagator):
    def __init__(self): ...
    def addAdditionalDataProvider(self, additionalDataProvider: AdditionalDataProvider[typing.Any]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Specified by: addAdditionalDataProvider in interface Propagator
        
        Parameters:
            additionalDataProvider (AdditionalDataProvider<?> additionalDataProvider): provider for additional data
        
        
        """
        ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, detector: _addEventDetector__T) -> None:
        """
        Add an event detector.
        
        Specified by: addEventDetector in interface Propagator
        
        Parameters:
            detector (T): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Remove all events detectors.
        
        Specified by: clearEventsDetectors in interface Propagator
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[AdditionalDataProvider[typing.Any]]:
        """
        Get an unmodifiable list of providers for additional data.
        
        Specified by: getAdditionalDataProviders in interface Propagator
        
        Returns:
            providers for the additional data
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get attitude provider.
        
        Specified by: getAttitudeProvider in interface Propagator
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> EphemerisGenerator:
        """
        Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           EphemerisGenerator generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           BoundedPropagator ephemeris = generator.getGeneratedEphemeris();
         
        
        Specified by: getEphemerisGenerator in interface Propagator
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]:
        """
        Get all the events detectors that have been added.
        
        Specified by: getEventDetectors in interface Propagator
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface Propagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> SpacecraftState:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface Propagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed additional data.
        
        Specified by: getManagedAdditionalData in interface Propagator
        
        Returns:
            names of all managed additional data
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer:
        """
        Get the multiplexer holding all step handlers.
        
        Specified by: getMultiplexer in interface Propagator
        
        Returns:
            multiplexer holding all step handlers
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface Propagator
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which a AdditionalDataProvider has been registered by calling the addAdditionalDataProvider method.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface Propagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState:
        """
        Propagate towards a target date.
        
        Simple propagators use only the target date as the specification for computing the propagated state. More feature rich propagators can consider other information and provide different operating modes or G-stop facilities to stop at pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
        Specified by: propagate in interface Propagator
        
        Parameters:
            target (AbsoluteDate): target date towards which orbit state should be propagated
        
        Returns:
            propagated state
        
        Propagate from a start date towards a target date.
        
        Those propagators use a start date and a target date to compute the propagated state. For propagators using event detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is performed, without processing any event computation. Then complete propagation is performed from start date to target date.
        
        Specified by: propagate in interface Propagator
        
        Parameters:
            start (AbsoluteDate): start date from which orbit state should be propagated
            target (AbsoluteDate): target date to which orbit state should be propagated
        
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
    def resetInitialState(self, state: SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface Propagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...

_PythonFieldAbstractPropagator__T = typing.TypeVar('_PythonFieldAbstractPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractPropagator(FieldAbstractPropagator[_PythonFieldAbstractPropagator__T], typing.Generic[_PythonFieldAbstractPropagator__T]):
    def __init__(self, field: org.hipparchus.Field[_PythonFieldAbstractPropagator__T]):
        """
        Build a new instance.
        
        Parameters:
            field (Field<PythonFieldAbstractPropagator> field): setting the field
        
        
        """
        ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, detector: _addEventDetector__D) -> None:
        """
        Add an event detector.
        
        Parameters:
            detector (D): 
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Remove all events detectors.
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldAbstractPropagator__T]:
        """
        Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           FieldEphemerisGenerator<T> generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           FieldBoundedPropagator<T> ephemeris = generator.getGeneratedEphemeris();
         
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldAbstractPropagator__T]]:
        """
        Get all the events detectors that have been added.
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
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
    def __init__(self): ...
    def addAdditionalDataProvider(self, additionalDataProvider: FieldAdditionalDataProvider[typing.Any, _PythonFieldBoundedPropagator__T]) -> None:
        """
        Add a set of user-specified data to be computed along with the orbit propagation.
        
        Specified by: addAdditionalDataProvider in interface FieldPropagator
        
        Parameters:
            additionalDataProvider (FieldAdditionalDataProvider<?, PythonFieldBoundedPropagator> additionalDataProvider): provider for additional data
        
        
        """
        ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, detector: _addEventDetector__D) -> None:
        """
        Add an event detector.
        
        Specified by: addEventDetector in interface FieldPropagator
        
        Parameters:
            detector (D): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEventsDetectors(self) -> None:
        """
        Remove all events detectors.
        
        Specified by: clearEventsDetectors in interface FieldPropagator
        
        Also see:
            addEventDetector,
            getEventDetectors
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAdditionalDataProviders(self) -> java.util.List[FieldAdditionalDataProvider[typing.Any, _PythonFieldBoundedPropagator__T]]:
        """
        Get an unmodifiable list of providers for additional data.
        
        Specified by: getAdditionalDataProviders in interface FieldPropagator
        
        Returns:
            providers for the additional states
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get attitude provider.
        
        Specified by: getAttitudeProvider in interface FieldPropagator
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldBoundedPropagator__T]:
        """
        Set up an ephemeris generator that will monitor the propagation for building an ephemeris from it once completed.
        
        This generator can be used when the user needs fast random access to the orbit state at any time between the initial and target times. A typical example is the implementation of search and iterative algorithms that may navigate forward and backward inside the propagation range before finding their result even if the propagator used is integration-based and only goes from one initial time to one target time.
        
        Beware that when used with integration-based propagators, the generator will store all intermediate results. It is therefore memory intensive for long integration-based ranges and high precision/short time steps. When used with analytical propagators, the generator only stores start/stop time and a reference to the analytical propagator itself to call it back as needed, so it is less memory intensive.
        
        The returned ephemeris generator will be initially empty, it will be filled with propagation data when a subsequent call to either propagate or propagate is called. The proper way to use this method is therefore to do:
        
        
           FieldEphemerisGenerator<T> generator = propagator.getEphemerisGenerator();
           propagator.propagate(target);
           FieldBoundedPropagator<T> ephemeris = generator.getGeneratedEphemeris();
         
        
        Specified by: getEphemerisGenerator in interface FieldPropagator
        
        Returns:
            ephemeris generator
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldBoundedPropagator__T]]:
        """
        Get all the events detectors that have been added.
        
        Specified by: getEventDetectors in interface FieldPropagator
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface FieldPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface FieldPropagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed data.
        
        Specified by: getManagedAdditionalData in interface FieldPropagator
        
        Returns:
            names of all managed data
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]:
        """
        Get the last date of the range.
        
        Specified by: getMaxDate in interface FieldBoundedPVCoordinatesProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]:
        """
        Get the first date of the range.
        
        Specified by: getMinDate in interface FieldBoundedPVCoordinatesProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_PythonFieldBoundedPropagator__T]:
        """
        Get the multiplexer holding all step handlers.
        
        Specified by: getMultiplexer in interface FieldPropagator
        
        Returns:
            multiplexer holding all step handlers
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_PythonFieldBoundedPropagator__T]:
        """
        Get the FieldPVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface FieldPropagator
        
        Specified by: getPVCoordinates in interface FieldPVCoordinatesProvider
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldBoundedPropagator> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which an FieldAdditionalDataProvider has been registered by calling the addAdditionalDataProvider method. If the propagator is an FieldAbstractIntegratedPropagator, the states for which a set of FieldAdditionalDerivativesProvider has been registered by calling the addAdditionalDerivativesProvider method are also counted as managed additional states.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface FieldPropagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
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
    def resetInitialState(self, state: FieldSpacecraftState[_PythonFieldBoundedPropagator__T]) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface FieldPropagator
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldBoundedPropagator> state): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface FieldPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...

class PythonToleranceProvider(ToleranceProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getTolerances_0__T = typing.TypeVar('_getTolerances_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_2__T = typing.TypeVar('_getTolerances_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_4__T = typing.TypeVar('_getTolerances_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_5__T = typing.TypeVar('_getTolerances_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getTolerances_6__T = typing.TypeVar('_getTolerances_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTolerances(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_0__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTolerances_0__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, cartesianOrbit: org.orekit.orbits.CartesianOrbit) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Retrieve the integration tolerances given a reference orbit.
        
        Specified by: getTolerances in interface ToleranceProvider
        
        Parameters:
            referenceOrbit (Orbit): orbit
            propagationOrbitType (OrbitType): orbit type for propagation (can be different from the input orbit one)
            positionAngleType (PositionAngleType): reference position angle type
        
        Returns:
            absolute and relative tolerances
        
        Retrieve the integration tolerances given reference position and velocity vectors.
        
        Specified by: getTolerances in interface CartesianToleranceProvider
        
        Parameters:
            position (Vector3D): reference position vector
            velocity (Vector3D): reference velocity vector
        
        Returns:
            absolute and relative tolerances
        
        
        """
        ...
    @typing.overload
    def getTolerances(self, fieldCartesianOrbit: org.orekit.orbits.FieldCartesianOrbit[_getTolerances_2__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_getTolerances_4__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_getTolerances_5__T], orbitType: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_getTolerances_6__T], orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def getTolerances(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation")``.

    AbstractMatricesHarvester: typing.Type[AbstractMatricesHarvester]
    AbstractPropagator: typing.Type[AbstractPropagator]
    AbstractStateCovarianceInterpolator: typing.Type[AbstractStateCovarianceInterpolator]
    AbstractStateModifier: typing.Type[AbstractStateModifier]
    AdditionalDataProvider: typing.Type[AdditionalDataProvider]
    BoundedPropagator: typing.Type[BoundedPropagator]
    CartesianToleranceProvider: typing.Type[CartesianToleranceProvider]
    EphemerisGenerator: typing.Type[EphemerisGenerator]
    FieldAbstractPropagator: typing.Type[FieldAbstractPropagator]
    FieldAbstractStateModifier: typing.Type[FieldAbstractStateModifier]
    FieldAdditionalDataProvider: typing.Type[FieldAdditionalDataProvider]
    FieldBoundedPropagator: typing.Type[FieldBoundedPropagator]
    FieldEphemerisGenerator: typing.Type[FieldEphemerisGenerator]
    FieldPropagator: typing.Type[FieldPropagator]
    FieldSpacecraftState: typing.Type[FieldSpacecraftState]
    FieldSpacecraftStateInterpolator: typing.Type[FieldSpacecraftStateInterpolator]
    FieldStateCovariance: typing.Type[FieldStateCovariance]
    LinearKeplerianCovarianceHandler: typing.Type[LinearKeplerianCovarianceHandler]
    MatricesHarvester: typing.Type[MatricesHarvester]
    PropagationType: typing.Type[PropagationType]
    Propagator: typing.Type[Propagator]
    PropagatorsParallelizer: typing.Type[PropagatorsParallelizer]
    PythonAbstractMatricesHarvester: typing.Type[PythonAbstractMatricesHarvester]
    PythonAbstractPropagator: typing.Type[PythonAbstractPropagator]
    PythonAbstractStateCovarianceInterpolator: typing.Type[PythonAbstractStateCovarianceInterpolator]
    PythonAbstractStateModifier: typing.Type[PythonAbstractStateModifier]
    PythonAdditionalDataProvider: typing.Type[PythonAdditionalDataProvider]
    PythonBoundedPropagator: typing.Type[PythonBoundedPropagator]
    PythonCartesianToleranceProvider: typing.Type[PythonCartesianToleranceProvider]
    PythonEphemerisGenerator: typing.Type[PythonEphemerisGenerator]
    PythonFieldAbstractPropagator: typing.Type[PythonFieldAbstractPropagator]
    PythonFieldAdditionalDataProvider: typing.Type[PythonFieldAdditionalDataProvider]
    PythonFieldBoundedPropagator: typing.Type[PythonFieldBoundedPropagator]
    PythonFieldEphemerisGenerator: typing.Type[PythonFieldEphemerisGenerator]
    PythonFieldPropagator: typing.Type[PythonFieldPropagator]
    PythonMatricesHarvester: typing.Type[PythonMatricesHarvester]
    PythonPropagator: typing.Type[PythonPropagator]
    PythonToleranceProvider: typing.Type[PythonToleranceProvider]
    SpacecraftState: typing.Type[SpacecraftState]
    SpacecraftStateInterpolator: typing.Type[SpacecraftStateInterpolator]
    StateCovariance: typing.Type[StateCovariance]
    StateCovarianceBlender: typing.Type[StateCovarianceBlender]
    StateCovarianceKeplerianHermiteInterpolator: typing.Type[StateCovarianceKeplerianHermiteInterpolator]
    StateCovarianceMatrixProvider: typing.Type[StateCovarianceMatrixProvider]
    ToleranceProvider: typing.Type[ToleranceProvider]
    analytical: org.orekit.propagation.analytical.__module_protocol__
    conversion: org.orekit.propagation.conversion.__module_protocol__
    events: org.orekit.propagation.events.__module_protocol__
    integration: org.orekit.propagation.integration.__module_protocol__
    numerical: org.orekit.propagation.numerical.__module_protocol__
    sampling: org.orekit.propagation.sampling.__module_protocol__
    semianalytical: org.orekit.propagation.semianalytical.__module_protocol__
